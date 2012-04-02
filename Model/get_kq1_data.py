from numpy import genfromtxt, ma, unique, zeros
from pylab import csv2rec

HISTORICAL, CONCURRENT = 0,1

def get_data(concurrent):

    observations = csv2rec("kq1-2.csv", missing='NA')

    # Filter for historical or concurrent
    observations = observations[observations['concurrent']==concurrent]

    # Unique paper ID values
    unique_papers = set(observations['paper_id'])
    # Re-number papers
    paper_id = zeros(len(observations), int)
    for i,p in enumerate(unique_papers):
        paper_id[observations['paper_id']==p] = i
    
    # Unique grouped ID values
    unique_groups = set(observations['group_id'])
    # Re-number groups
    group_id = zeros(len(observations), int)
    for i,g in enumerate(unique_groups):
        group_id[observations['group_id']==g] = i
    
    # unique_units = set(observations['unit_id'])
    # unit_id = observations['unit_id']-1

    # Index to individual-level data
    indiv = observations['n']==1
    # Individual-level data
    obs_indiv = observations[indiv]
    # Summarized data
    obs_summ = observations[indiv-True]

    # Group IDs for individual data
    group_id_indiv = group_id[indiv]
    # Paper IDs for individual data
    paper_id_indiv = paper_id[indiv]
    # Unit IDs for individual data
    # unit_id_indiv = unit_id[indiv]
    # Unique paper ID's for individual studies
    unique_papers_indiv = set(paper_id_indiv)

    # Group IDs for summarized data
    group_id_summ = group_id[indiv-True]
    # Paper IDs for summarized data
    paper_id_summ = paper_id[indiv-True]
    # Unit IDs for summarized data
    # unit_id_summ = unit_id[indiv-True]
    # Unique paper IDs for group data
    unique_papers_summ = set(paper_id_summ)
    
    return locals()