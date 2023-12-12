# -*- coding: utf-8 -*-

import json
import pandas as pd

def load_json_summary(path: str) -> pd.DataFrame:

    """
    Load the summary file generated by BUSCO into a pandas DataFrame.
    
    Parameters:
        path (str): The path to the BUSCO json summary file.
        
    Returns:
        pd.DataFrame: The loaded summary table with busco gene information.
    """
    
    # Read the summary table from the file
    dict = json.load(open(path))

    # Populate the columns of the summary table with data from the dict
    summary_table = pd.DataFrame({
        'max_intron': dict['parameters']['max_intron'],
        'max_seq_len': dict['parameters']['max_seq_len'],
        'metaeuk_parameters': dict['parameters']['metaeuk_parameters'],
        "metaeuk_rerun_parameters": dict['parameters']['metaeuk_rerun_parameters'],
        "contig_break": dict['parameters']['contig_break'],
        "scaffold_composition": dict['parameters']['scaffold_composition'],
        "gene_predictor": dict['parameters']['gene_predictor'],
        'dataset_name': dict['lineage_dataset']['name'],
        'number_of_buscos': dict['lineage_dataset']['number_of_buscos'],
        'number_of_species': dict['lineage_dataset']['number_of_species'],
        'metaeuk_version': dict['versions']['metaeuk'],
        'bbtools_version': dict['versions']['bbtools'],
        'busco_version': dict['versions']['busco'],
        'hmmsearch_version': dict['versions']['hmmsearch'],
        'one_line_summary': dict['results']['one_line_summary'],
        'complete': dict['results']['Complete'],
        'single copy': dict['results']['Single copy'],
        'multi copy': dict['results']['Multi copy'],
        'fragmented': dict['results']['Fragmented'],
        'missing': dict['results']['Missing'],
        'n_markers': dict['results']['n_markers'],
        'domain': dict['results']['domain'],
        'number_of_scaffolds': dict['results']['Number of scaffolds'],
        'number_of_contigs': dict['results']['Number of contigs'],
        'total length': dict['results']['Total length'],
        'percent gaps': dict['results']['Percent gaps'],
        'scaffold N50': dict['results']['Scaffold N50'],
        'contigs N50': dict['results']['Contigs N50']
    }, index=[0])

    return summary_table