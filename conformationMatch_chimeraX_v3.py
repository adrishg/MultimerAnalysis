import os
from chimerax.core.commands import run  

# Specify the folder containing the NMR reference PDB files
nmr_folder = "/Users/adrianahernandezgonzalez/Documents/YarovLab/repositories/repo-MultimerAnalysis/2i53_NMR_reference"

# Specify the folder containing the models PDB files
models_folder = "/Users/adrianahernandezgonzalez/Library/CloudStorage/Box-Box/Rosetta-brainstorm/Adriana/Cav_channels/Cav1.2-CaM/AF/withTemplates/proteinBound/hCav1.2p_CaM_Templ/hCav1.2p_CaM_Templ_1cm1/relaxed/"

# Create a list to store the names of the opened models
opened_refs = {}
opened_models = {}

counterOpened = 1

# Iterate through the NMR reference PDB files
for nmr_file in os.listdir(nmr_folder):
    if nmr_file.endswith(".pdb"):
        # Get the full path to the NMR reference PDB file
        nmr_path = os.path.join(nmr_folder, nmr_file)
        
        # Open the NMR reference PDB file in ChimeraX
        run(session, 'open '+str(nmr_path))
        
        # Append the names of the opened models to the list
        opened_refs[counterOpened] = nmr_file
        counterOpened += 1

# Iterate through the models PDB files
for model_file in os.listdir(models_folder):
    if model_file.endswith(".pdb"):
        # Get the full path to the models PDB file
        model_path = os.path.join(models_folder, model_file)
        
        # Open the models PDB file in ChimeraX
        run(session, 'open '+str(model_path))
        
        # Append the names of the opened models to the list
        opened_models[counterOpened] = model_file
        counterOpened += 1

# Create a matrix to store the similarity scores
similarity_matrix = []
similarity_matrix.append(list( opened_refs.values()) )
#list(opened_refs.keys())


# Iterate through the opened models and run matchmaker
for model_ID in list(opened_models.keys()):
    row = []
    row.append( opened_models[model_ID]) 
    for ref_ID in list(opened_refs.keys()):
        if model_ID != ref_ID:
            # Run the matchmaker command for the current model and reference
            matchmaker_cmd = f'matchmaker #{model_ID}/B to #{ref_ID}/A'
            result = run(session, matchmaker_cmd)
            
            # Extract and store the RMSD value from the result
            rmsd_value = float(result[0]['full RMSD'])
            row.append(rmsd_value)
    
    similarity_matrix.append(row)

# Specify the output file path
output_file = "/Users/adrianahernandezgonzalez/Documents/YarovLab/repositories/repo-MultimerAnalysis/similarity_matrix.tsv"
#index_file = "/Users/adrianahernandezgonzalez/Documents/YarovLab/repositories/repo-MultimerAnalysis/index.txt"

# Save the similarity matrix as a TSV file
with open(output_file, 'w') as f:
    for row in similarity_matrix:
        f.write('\t'.join(map(str, row)) + '\n')

'''with open(index_file, 'w') as f:
    for row in simi'''
