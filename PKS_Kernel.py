#!/usr/bin/python
#-*- coding: utf-8 -*
import re
import os
from math import ceil
import numpy as np
from scipy.stats import ks_2samp
from ks_test import ks
import operator

def parseFiles(log_location, nexus_file_path):
    
    #Read Parameters File (*.p)
    p_file = open(nexus_file_path+".p")
    p = p_file.readlines()                      #p is a list of all lines in parameter file
    p_file.close()
    
    #Extract All LnL Values => dic={gen:LnL}

    dic_of_lnl={}
    for line in p[2:]:
        line2=line.split('\t')
        gen=int(line2[0])
        LnL=float(line2[1])
        if gen != 0:
            dic_of_lnl[gen]=LnL
    
    #Read Tree File (*.t)
    t_file = open(nexus_file_path + ".t")
    t = t_file.readlines()                           #t is a list of all lines in tree file
    t_file.close()
    
    #Extract All Trees => dic = {gen:tree in newick format}
    dic_of_trees={}
    for line in t:
        if 'tree gen.' in line:
            if ' = [&U] ' in line:
                line=line.split(' = [&U] ')
            else:
                line=line.split(' = [&R] ')
            gen=line[0].split('.')
            gen=int(gen[1])
            tree=line[1].strip()
            n = line[1].count(':')
            if gen != 0:
                dic_of_trees[gen]=tree
    
    #return dic_of_lnl, dic_of_trees
    return dic_of_trees, dic_of_lnl

def extract_branchLength(dic_of_trees,nexus_file_path):
    pattern = re.compile(r"[0-9]+(?:\.[0-9]+[e]+[-])+[0-9]+[0-9]")
    dic_of_treesMutations={}
    nchar=get_Nchar(nexus_file_path)

    for gen in dic_of_trees:
        NewickTree = [dic_of_trees[gen]]
        for tree in NewickTree:
            list_of_bl_perTree= pattern.findall(tree)
            new_list=[]
            for bl in list_of_bl_perTree:
                new_list.append(int(round(float(bl)*nchar)))
            dic_of_treesMutations[gen]= new_list
    
    return dic_of_treesMutations, nchar

def extract_branchLength_float(dic_of_trees,nexus_file_path):
    pattern = re.compile(r"[0-9]+(?:\.[0-9]+[e]+[-])+[0-9]+[0-9]")
    dic_of_treesMutations={}
    nchar=get_Nchar(nexus_file_path)

    for gen in dic_of_trees:
        NewickTree = [dic_of_trees[gen]]
        for tree in NewickTree:
            list_of_bl_perTree= pattern.findall(tree)
            new_list=[]
            for bl in list_of_bl_perTree:
                new_list.append(float(bl))
            dic_of_treesMutations[gen]= new_list
    
    return dic_of_treesMutations


def get_Nchar(nexus_file_path):
    ncharFile = open(nexus_file_path)
    ncharFile=ncharFile.readlines()
    for line in ncharFile:
        line=line.lower()
        if "nchar" in line:
            line = line[line.index("nchar="):line.index(";")]
            line=line.split('=')
            nchar=float(line[1])
            return nchar

def logMaker_LnlTree(log_location, dic_of_lnl, dic_of_treesMutations):
    #Creates log file of all LnL values: gen -> LnL        
    log_LnlTree=open(log_location + 'log_LnL&Trees.csv','w')
    
    #decreasingly sort  dictionary of LnLs accordingly LnL values: list of tuple (gen, lnl)
    sorted_Lnldic = sorted(dic_of_lnl.items(), key=operator.itemgetter(1))
    sorted_Lnldic.reverse()
    
    #write the lnl values to log file
    for item in sorted_Lnldic:
        for gen, lnl in dic_of_lnl.items():
            if lnl == item[1]:
                mutations_per_gen=''
                list_mutations=dic_of_treesMutations[gen]
                for mutation in list_mutations:
                    mutations_per_gen+=','+str(mutation) 
                log_LnlTree.write(str(gen)+','+str(dic_of_lnl[gen])+mutations_per_gen+'\n')
    
    log_LnlTree.close()

def logMaker_LnlTree_float(log_location, dic_of_lnl, dic_of_treesMutations):
    #Creates log file of all LnL values: gen -> LnL        
    log_LnlTree=open(log_location + 'log_LnL&Trees_float.csv','w')
    
    #decreasingly sort  dictionary of LnLs accordingly LnL values: list of tuple (gen, lnl)
    sorted_Lnldic = sorted(dic_of_lnl.items(), key=operator.itemgetter(1))
    sorted_Lnldic.reverse()
    
    #write the lnl values to log file
    for item in sorted_Lnldic:
        for gen, lnl in dic_of_lnl.items():
            if lnl == item[1]:
                mutations_per_gen=''
                list_mutations=dic_of_treesMutations[gen]
                for mutation in list_mutations:
                    mutations_per_gen+=','+str(mutation) 
                log_LnlTree.write(str(gen)+','+str(dic_of_lnl[gen])+mutations_per_gen+'\n')
    
    log_LnlTree.close()

def bestTreeSelector(percentage, dic_of_lnl):
    '''select the percentage of best tree in dic_of_treesMutations to be analysed
    The selection is made through the LnL values, in dic_of_LnL'''
    percentage/=100.
    
    bestGen = []
    
    sorted_Lnldic = sorted(dic_of_lnl.items(), key=operator.itemgetter(1))
    sorted_Lnldic.reverse()
    
    numberTotalTrees = len(dic_of_lnl)
    numberBestTrees = int(round(percentage*numberTotalTrees))
    
    for i in range(0, numberBestTrees):
        bestGen.append(sorted_Lnldic[i][0])
        
    return bestGen, numberBestTrees, numberTotalTrees
    
def logMaker_bestLnlTree(log_location, bestGen, dic_of_lnl, dic_of_treesMutations):

    
    bestLnLTree_log = open(log_location + 'log_BestLnL&Trees.csv','w')
    
    for gen in bestGen:
        
        listMutations=''
        tree = dic_of_treesMutations[gen]
        for mutation in tree:
            listMutations+=',' + str(mutation)
        bestLnLTree_log.write(str(gen)+','+str(dic_of_lnl[gen])+listMutations+'\n')
        
    bestLnLTree_log.close()
 
def logMaker_bestLnlTree_float(log_location, bestGen, dic_of_lnl, dic_of_treesMutations):

    
    bestLnLTree_log = open(log_location + 'log_BestLnL&Trees_float.csv','w')
    
    for gen in bestGen:
        
        listMutations=''
        tree = dic_of_treesMutations[gen]
        for mutation in tree:
            listMutations+=',' + str(mutation)
        bestLnLTree_log.write(str(gen)+','+str(dic_of_lnl[gen])+listMutations+'\n')
        
    bestLnLTree_log.close() 
    
def bestLnL_statistics(bestGen, dic_of_lnl):
    
    bestLnL = []
    
    for gen in bestGen:
        bestLnL.append(dic_of_lnl[gen])
        
    meanLnL = np.mean(bestLnL)
    varLnL = np.var(bestLnL)
    
    return meanLnL, varLnL
    
def bestTrees_statistics(bestGen, dic_of_treesMutations):
    
    bestTrees  = []
    
    for gen in bestGen:
        tree = dic_of_treesMutations[gen]
        for mutation in tree:
            bestTrees.append(mutation)
    
    meanTrees = np.mean(bestTrees)
    varTrees = np.var(bestTrees)
    
    return meanTrees, varTrees, bestTrees

def core(nexus_file_path, percentage, confidence):

    #create a file path for log files
    log_location = nexus_file_path[:nexus_file_path.rfind("/")]+"/PKS_Test_Logs/"
    if not os.path.exists(log_location): os.makedirs(log_location)
    
    #Parse parameter and Tree files from MrBayes and return tow dictionaries: dic_of_trees={gen:tree} and dic_of_lnl={gen:LnL}
    dic_of_trees, dic_of_lnl = parseFiles(log_location, nexus_file_path)
    
    #extract all branch lengths from every tree in the dic_of_trees and transforms each branch length into number of mutations
    #return a dic_of_trees by number of mutations: dic_of_treesMutations={gen:list of mutations}
    dic_of_treesMutations, nchar = extract_branchLength(dic_of_trees,nexus_file_path)
    dic_of_treesMutations_float = extract_branchLength_float(dic_of_trees,nexus_file_path)
    
    #Creates a log file containing gen, lnl and all number of mutations in that tree
    #logMaker_LnlTree_float(log_location, dic_of_lnl, dic_of_treesMutations_float)
    logMaker_LnlTree(log_location, dic_of_lnl, dic_of_treesMutations)
    logMaker_LnlTree_float(log_location, dic_of_lnl, dic_of_treesMutations_float)

    #select the percentage of best tree in dic_of_treesMutations to be analysed
    #the selection is made through the LnL values, in dic_of_LnL
    bestGen, numberBestTrees, numberTotalTrees = bestTreeSelector(percentage, dic_of_lnl)
    
    #create a log file containing only the best trees in the format gen, LnL, mutations
    logMaker_bestLnlTree(log_location, bestGen, dic_of_lnl, dic_of_treesMutations)
    logMaker_bestLnlTree_float(log_location, bestGen, dic_of_lnl, dic_of_treesMutations_float)    

    #get the median and variance of the LnL values that were selected (best LnLs)
    meanLnL, varLnL = bestLnL_statistics(bestGen, dic_of_lnl)
    
    #get the mean, variance and a list of all mutations in all the trees that were selected (best Trees)
    meanTrees, varTrees, bestTrees = bestTrees_statistics(bestGen, dic_of_treesMutations)
    
    #create a sample with random numbers generated from a poisson distribution with lambda = mean of observed mutations
    expectedMutations = np.random.poisson(meanTrees, size=10000)
    observedMutations = bestTrees
    
    #apply the 2 Sample Kolmogorov-Smirnov test on the observed and expected list of mutations
    n =len(observedMutations)/numberBestTrees
    D, testResult, criticalValue = ks(observedMutations, expectedMutations, n, confidence, meanTrees)
    
    #pass all the information to the PKS_Test.py file (the user interface)
    return numberBestTrees, meanLnL, meanTrees, log_location, varLnL, varTrees, D, testResult, criticalValue,observedMutations, expectedMutations,n

