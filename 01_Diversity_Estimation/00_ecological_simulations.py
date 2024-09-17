# -*- coding: utf-8 -*-
"""Ecological Simulations.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pPITBj-RONCJJT-mSUwxt05XyUNY0zvw
"""

import torch
import numpy as np
import pandas as pd

Y = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,16,16,16,16,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29]

#Genera = ['Agropyron_ciliare_Elymus_ciliaris', 'Agrostis_mexicana_Agrostis_tolucensis', 'Agrostis_quinqueseta', 'Agrostis_trachyphylla', 'Agrostis_volkensii', 'Amphibromus_neesii', 'Andropogon_amethystinus', 'Andropogon_chrysostachyus', 'Andropogon_contortus_Heteropogon_contortus', 'Andropogon_lima', 'Andropogon_schirensis', 'Anthoxanthum_nivale', 'Aristida_implexa_Aristida_megapotamica', 'Bothriochloa_bladhii', 'Brachiaria_brizantha_Urochloa_brizantha', 'Brachypodium_flexum', 'Bromus_auleticus', 'Bromus_brachyphyllus_Bromus_orcuttianus', 'Bromus_ciliatus', 'Bromus_lanatus', 'Bromus_leptoclados', 'Bromus_thominei_Bromus_hordeaceus_subsp_thominei', 'Calamagrostis_epigejos', 'Chrysopogon_fallax', 'Cymbopogon_nardus', 'Cynodon_dactylon', 'Dactylis_glomerata', 'Digitaria_abyssinica', 'Echinopogon_caespitosus', 'Ehrharta_erecta', 'Ehrharta_erecta_var_natalensis', 'Eleusine_coracana', 'Eleusine_jaegeri', 'Exotheca_abyssinica', 'Festuca africana_Pseudobromus_africanus', 'Festuca_costata', 'Festuca_elatior_Ampelodesmos_mauritanicus', 'Isachne_mauritiana', 'Koeleria_capensis', 'Lolium_perenne', 'Melica_onoei', 'Miscanthus_violaceus_Miscanthidium_violaceum', 'Oplismenus_compositus', 'Oplismenus_hirtellus', 'Pennisetum_longistylum_Cenchrus_clandestinus', 'Pentaschistis_borussica_Pentameris_borussica', 'Phalaris_arundinacea', 'Poa_anceps', 'Poa_leptoclada', 'Poa_schimperiana', 'Saccharum_arundinaceum_Tripidium_arundinaceum', 'Secale_cereale', 'Setaria_megaphylla', 'Sinarundinaria_alpina_Oldeania_alpina', 'Sorghum_halepense', 'Spartina_pectinata_Sporobolus_michauxianus', 'Stipa_compacta_Austrostipa_flavescens', 'Streblochaete_longiarista_Koordersiochloa_longiarista', 'Themeda_triandra', 'Zea_mays'];

# Load the test dataset (containing 30 species excluded from the classification models) - used for simulating artificial pollen assemblages
df = pd.read_csv("Modern_Test_Images_Patches_Features.csv", header = None)

X_train = torch.tensor(df.values)

print(X_train.shape)

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.neighbors import KernelDensity
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from collections import Counter
from scipy.stats import pearsonr
import seaborn as sns


X_train_np = X_train.to_numpy() if isinstance(X_train, pd.DataFrame) else X_train

Y_np = np.array(Y)

def simulate_community(Y_np, num_species_range, species_max_counts):
    num_species_select = np.random.randint(num_species_range[0], num_species_range[1] + 1)
    selected_species = np.random.choice(np.unique(Y_np), size=num_species_select, replace=False)
    community_indices = []

    for species in selected_species:
        indices = np.where(Y_np == species)[0]
        num_specimens = np.random.randint(0, species_max_counts[species] + 1)
        selected_indices = np.random.choice(indices, size=num_specimens, replace=False)
        community_indices.extend(selected_indices)

    return np.array(community_indices)

def shannon_diversity(species_counts):
    total = sum(species_counts.values())
    proportions = np.array(list(species_counts.values())) / total
    return -np.sum(proportions * np.log(proportions))

def shannon_entropy_kde(X_pca):
    kde = KernelDensity(kernel='gaussian', bandwidth=0.5).fit(X_pca)
    log_dens = kde.score_samples(X_pca)
    p = np.exp(log_dens)
    p /= p.sum()
    return -np.sum(p * np.log(p))

# Dictionary with the maximum number of specimens for each species in the dataset
species_max_counts = {species: Y_np[Y_np == species].shape[0] for species in np.unique(Y_np)}

num_communities = 1000
diversity_values = []
entropy_values = []

for _ in range(num_communities):
    community_indices = simulate_community(Y_np, num_species_range=(2, 30), species_max_counts=species_max_counts)
    community_X = X_train_np[community_indices]
    community_species = Y_np[community_indices]
    species_counts = Counter(community_species)

    diversity = shannon_diversity(species_counts)
    diversity_values.append(diversity)

    # Standardize community features and perform PCA to obtain PC1 scores
    scaler = StandardScaler()
    community_X_standardized = scaler.fit_transform(community_X)
    pca = PCA(n_components=1)
    community_pca_scores = pca.fit_transform(community_X_standardized)
    entropy = shannon_entropy_kde(community_pca_scores)
    entropy_values.append(entropy)


# Linear regression
model = LinearRegression()
X = np.array(entropy_values).reshape(-1, 1)
y = np.array(diversity_values).reshape(-1, 1)
model.fit(X, y)

fitted_y = model.predict(X)

# Mask for y-values ≥ 0
mask = fitted_y >= 0
positive_y_values = fitted_y[mask]
positive_X_values = X[mask]

plt.figure(figsize=(10, 8), dpi = 500)
sns.scatterplot(x=entropy_values, y=diversity_values, s=20, alpha=0.6)  # Scatterplot
plt.plot(positive_X_values, positive_y_values, color='black')  # Regression Line

# Highlight range of entropy
plt.axvspan(3, 4, color='red', alpha=0.1)

# Add regression
slope = model.coef_[0][0]
intercept = model.intercept_[0]
r_squared = model.score(X, y)
pearson_r, p_value = pearsonr(entropy_values, diversity_values)

intercept_sign = '+' if intercept >= 0 else '-'
intercept_value = abs(intercept)

# Conditional formatting for p-value
if p_value < 0.0001:
    p_value_display = "p < 0.0001"
else:
    p_value_display = f"p = {p_value:.4f}"

# r and p-value
regression_text = (f"y = {slope:.2f}x {intercept_sign} {intercept_value:.2f}\n"
                   f"r = {pearson_r:.3f}, {p_value_display}")


plt.text(0.05, 0.95, regression_text, verticalalignment='top', horizontalalignment='left', transform=plt.gca().transAxes, fontsize=12,
         bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

plt.xlabel('Shannon Entropy (probabilities estimated via KDE)', fontsize=14)
plt.ylabel('Shannon Index with Species Identifications', fontsize=14)
plt.title('Relationship between Shannon Entropy and Shannon Diversity', fontsize=14)

plt.ylim(bottom=-0.1)

plt.grid(True)
plt.show()