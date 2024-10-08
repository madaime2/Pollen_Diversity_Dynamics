# -*- coding: utf-8 -*-
"""Estimating_Biodiversity.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bxVgXkcax1qOGd5ZKRNkQUZAvCzimEY9

# Load CNNs and extract classification features

# H-CNN
"""

PATH = 'Semi_Supervised_Grass_Images_Split01.pth'

model =  models.resnext101_32x8d(pretrained=True)
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, 60);
model.load_state_dict(torch.load(PATH));
#model.load_state_dict(torch.load(PATH, map_location="cpu"))
model.to(device);

from torchvision.transforms.transforms import ConvertImageDtype
from torchvision.transforms.functional import convert_image_dtype
import glob
from PIL import Image

transform = transforms.Compose([
    torchvision.transforms.Resize((224,224)),
        transforms.ToTensor(),
])

def extract_features(model, image_dir, k=100):
    """
    """
    patch_paths = glob.glob(os.path.join(image_dir, '*'))

    images = []
    for path in patch_paths:
        image = Image.open(path).convert('RGB')
        image = transform(image)
        images.append(image)

    images = torch.stack(images, 0).to(device)
    feats = model(images)
    feats = feats.detach().cpu().numpy()
    patcho = image_dir

    # Take average and get final prediction
    # feats = feats.mean(0)

    ###### Add line below to group all patch features / image
    feats = np.sort(feats, 0)[::-1][:k].mean(0)
    print(feats.shape)
    return feats


# Extract features from fossil specimens

val_dir =  "E:Grass_Images_Fossils"

val_class_dirs = glob.glob(os.path.join(val_dir,'*'))

# Modify output
model.fc = nn.Identity()
model.eval()

class_map = {name: idx for idx, name in enumerate(class_names)}
all_image_dirs = []
features = []
labels = []
for d in val_class_dirs:
    image_dirs = glob.glob(os.path.join(d, '*'))
    for image_dir in image_dirs:
        class_name = os.path.basename(image_dir).split('.')[0]
        #label = class_map[class_name]
        #labels.append(label)
        all_image_dirs.append(image_dir)
        feats = extract_features(model, image_dir)
        features.append(feats)

features = np.stack(features, 0)

image_features = features

"""# P-CNN"""

PATH = 'Semi_Supervised_Grass_Patches_Split01.pth'

model =  models.resnext101_32x8d(pretrained=True)
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, 60);
model.load_state_dict(torch.load(PATH));
#model.load_state_dict(torch.load(PATH, map_location="cpu"))
model.to(device);

from torchvision.transforms.transforms import ConvertImageDtype
from torchvision.transforms.functional import convert_image_dtype
import glob
from PIL import Image

transform = transforms.Compose([
    torchvision.transforms.Resize((224,224)),
        transforms.ToTensor(),
])

def extract_features(model, image_dir, k=100):
    """
    """
    patch_paths = glob.glob(os.path.join(image_dir, '*'))

    images = []
    for path in patch_paths:
        image = Image.open(path).convert('RGB')
        image = transform(image)
        images.append(image)

    images = torch.stack(images, 0).to(device)
    feats = model(images)
    feats = feats.detach().cpu().numpy()
    patcho = image_dir

    # Take average and get final prediction
    # feats = feats.mean(0)

    ###### Add line below to group all patch features / image
    feats = np.sort(feats, 0)[::-1][:k].mean(0)
    print(feats.shape)
    return feats


# Extract features from fossil specimens

val_dir =  "E:Grass_Patches_Fossils"

val_class_dirs = glob.glob(os.path.join(val_dir,'*'))

# Modify output
model.fc = nn.Identity()
model.eval()

class_map = {name: idx for idx, name in enumerate(class_names)}
all_image_dirs = []
features = []
labels = []
for d in val_class_dirs:
    image_dirs = glob.glob(os.path.join(d, '*'))
    for image_dir in image_dirs:
        class_name = os.path.basename(image_dir).split('.')[0]
        #label = class_map[class_name]
        #labels.append(label)
        all_image_dirs.append(image_dir)
        feats = extract_features(model, image_dir)
        features.append(feats)

features = np.stack(features, 0)

patch_features = features

# Concatenate image and patch features and save tensor
import pandas as pd
import torch

fossil_image_features_tensor = torch.tensor(fossil_image_features)
fossil_patch_features_tensor = torch.tensor(fossil_patch_features)

# Concatenate the tensors
combined_tensor = torch.cat((fossil_image_features_tensor, fossil_patch_features_tensor), dim=1)

pd.DataFrame(np.array(combined_tensor)).to_csv("Grass_Images_Patches_Fossils_Concatenated_Features.csv")

"""# Calculating Shannon entropy values for each and every pollen assemblage across Lake Rutundu sediment core"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.neighbors import KernelDensity
import torch
from sklearn.cluster import KMeans


# Y defines different ages (along Lake Rutundu sediment core)
Y = [20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,134,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,163,173,173,173,173,173,173,173,173,173,173,173,173,173,173,173,173,173,173,173,173,173,173,173,173,173,173,173,173,173,173,173,173,173,173,173,173,173,173,173,173,173,173,173,173,173,173,173,173,173,173,195,195,195,195,195,195,195,195,195,195,195,195,195,195,195,195,195,195,195,195,195,195,195,195,195,195,195,195,195,195,195,195,195,195,195,195,195,195,195,195,195,195,195,195,195,195,195,195,195,195,195,236,236,236,236,236,236,236,236,236,236,236,236,236,236,236,236,236,236,236,236,236,236,236,236,236,236,236,236,236,236,236,236,236,236,236,236,236,236,236,236,236,236,236,236,236,236,236,236,236,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,256,263,263,263,263,263,263,263,263,263,263,263,263,263,263,263,263,263,263,263,263,263,263,263,263,263,263,263,263,263,263,263,263,263,263,263,263,263,263,263,263,263,263,263,263,263,263,263,263,263,286,286,286,286,286,286,286,286,286,286,286,286,286,286,286,286,286,286,286,286,286,286,286,286,286,286,286,286,286,286,286,286,286,286,286,286,286,286,286,286,286,286,286,286,286,286,286,286,286,286,298,298,298,298,298,298,298,298,298,298,298,298,298,298,298,298,298,298,298,298,298,298,298,298,298,298,298,298,298,298,298,298,298,298,298,298,298,298,298,298,298,298,298,298,298,298,298,298,298,298,531,531,531,531,531,531,531,531,531,531,531,531,531,531,531,531,531,531,531,531,531,531,531,531,531,531,531,531,531,531,531,531,531,531,531,531,531,531,531,531,531,531,531,531,531,531,531,531,531,531,321,321,321,321,321,321,321,321,321,321,321,321,321,321,321,321,321,321,321,321,321,321,321,321,321,321,321,321,321,321,321,321,321,321,321,321,321,321,321,321,321,321,321,321,321,321,321,321,321,321,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,375,375,375,375,375,375,375,375,375,375,375,375,375,375,375,375,375,375,375,375,375,375,375,375,375,375,375,375,375,375,375,375,375,375,375,375,375,375,375,375,375,375,375,375,375,375,375,375,375,375,397,397,397,397,397,397,397,397,397,397,397,397,397,397,397,397,397,397,397,397,397,397,397,397,397,397,397,397,397,397,397,397,397,397,397,397,397,397,397,397,397,397,397,397,397,397,397,397,397,423,423,423,423,423,423,423,423,423,423,423,423,423,423,423,423,423,423,423,423,423,423,423,423,423,423,423,423,423,423,423,423,423,423,423,423,423,423,423,423,423,423,423,423,423,423,423,423,423,423,432,432,432,432,432,432,432,432,432,432,432,432,432,432,432,432,432,432,432,432,432,432,432,432,432,432,432,432,432,432,432,432,432,432,432,432,432,432,432,432,432,432,432,432,432,432,432,432,453,453,453,453,453,453,453,453,453,453,453,453,453,453,453,453,453,453,453,453,453,453,453,453,453,453,453,453,453,453,453,453,453,453,453,453,453,453,453,453,453,453,453,453,453,453,453,453,453,470,470,470,470,470,470,470,470,470,470,470,470,470,470,470,470,470,470,470,470,470,470,470,470,470,470,470,470,470,470,470,470,470,470,470,470,470,470,470,470,470,470,470,470,470,470,470,470,470,470,470,483,483,483,483,483,483,483,483,483,483,483,483,483,483,483,483,483,483,483,483,483,483,483,483,483,483,483,483,483,483,483,483,483,483,483,483,483,483,483,483,483,483,483,483,483,483,483,483,483,483,483,516,516,516,516,516,516,516,516,516,516,516,516,516,516,516,516,516,516,516,516,516,516,516,516,516,516,516,516,516,516,516,516,516,516,516,516,516,516,516,516,516,516,516,516,516,516,516,516,516,516]

# Depth to age mapping
depth_to_age = {20:252.922, 39:1006.79, 71:2446.333, 124:4497.479, 134:5001.556, 163:6496.673, 173:7022.491, 195:8195.662, 236:9281.874, 256:10554.34, 263:11004.19, 286:12497.5, 298:13285.34, 321:14230.91, 335:14995.26, 375:17204.36, 397:18434.3, 423:19520.83, 432:20040.09, 453:21257.91, 470:22249.94, 483:23012.15, 516:24014.17, 531:25000.81}

# Round ages in the dictionary to the nearest 5
for depth in depth_to_age:
    depth_to_age[depth] = 5 * round(depth_to_age[depth] / 5)

# Replace depth values in Y with their corresponding ages
ages = [depth_to_age[depth] for depth in Y]

# Convert the list of ages to a tensor
age_tensor = torch.tensor(ages)

Y_tens = age_tensor

# Load the datasets
df_images = pd.read_csv("Grass_Images_Patches_Fossils_Concatenated_Features.csv", header=None)

# Convert DataFrames to Numpy arrays and standardize
X_Rutundu_images = df_images.to_numpy()
scaler = StandardScaler()
X_Rutundu_images_std = scaler.fit_transform(X_Rutundu_images)

# Perform PCA
pca = PCA(n_components=1)
X_Rutundu_images_pca = pca.fit_transform(X_Rutundu_images_std)

# Define Shannon Entropy
def shannon_entropy(probabilities):
    return -np.sum(probabilities * np.log(probabilities))  # Small constant to avoid log(0)

# Calculate entropy for each age using the first PC
age_entropies = {}
for age in set(age_tensor.numpy()):
    # Select PCA feature vectors for the current age
    age_vectors_pca = X_Rutundu_images_pca[age_tensor == age]

    # Estimate probability distribution using Kernel Density Estimation
    kde = KernelDensity(kernel='gaussian', bandwidth=0.5).fit(age_vectors_pca)
    log_dens = kde.score_samples(age_vectors_pca)
    probabilities = np.exp(log_dens)
    probabilities /= probabilities.sum()  # Normalize to sum to 1

    # Calculate Shannon Entropy for the current age
    entropy = shannon_entropy(probabilities)
    age_entropies[age] = entropy

# Sort ages and get corresponding entropies
sorted_ages = sorted(age_entropies.keys(), reverse=False)
entropies = [age_entropies[age] for age in sorted_ages]

# Plot Entropy over Age
plt.figure(figsize=(2, 5))
plt.plot(entropies, sorted_ages)
plt.ylabel('Age (cal. yr BP)')
plt.xlabel('Shannon Entropy')
plt.title('Shannon Entropy Over Time')
plt.gca().invert_yaxis()
plt.show()

"""# Converting the raw entropy measurements into Shannon diversity index values"""

import pandas as pd
import numpy as np
import torch
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from scipy.stats import pearsonr


pca = PCA(n_components=1)
X_pca = pca.fit_transform(X_Rutundu_images_std)

# Shannon Entropy
def shannon_entropy(counts):
    """Calculate Shannon Entropy."""
    total = np.sum(counts)
    proportions = counts / total
    entropy = -np.sum(proportions * np.log(proportions))
    return entropy

# Calculate diversities for a given K (where K is the number of morphotypes in the assemblage)
def calculate_diversities(K):
    kmeans = KMeans(n_clusters=K, n_init=15, random_state=0)
    clusters = kmeans.fit_predict(X_pca)
    age_diversities = {}
    for cluster in range(K):
        ages_in_cluster = age_tensor[clusters == cluster]
        unique_ages, counts = ages_in_cluster.unique(return_counts=True)
        for age, count in zip(unique_ages, counts):
            age_value = age.item()
            if age_value not in age_diversities:
                age_diversities[age_value] = []
            age_diversities[age_value].append(count.item())
    sorted_ages = sorted(age_diversities.keys())
    diversities = [shannon_entropy(np.array(age_diversities[age])) for age in sorted_ages]
    return diversities

# Iterate over K values and calculate correlation and p-value
K_values = range(2, 50)
correlation_results = []
for K in K_values:
    diversities = calculate_diversities(K)
    # Align entropies with diversities based on ages
    correlation, p_value = pearsonr(diversities, entropies)
    correlation_results.append((correlation, p_value))

# Find the K value (number of morphotypes) with the maximum correlation coefficient
optimal_K = K_values[np.argmax([result[0] for result in correlation_results])]
optimal_correlation, optimal_p_value = correlation_results[np.argmax([result[0] for result in correlation_results])]

print("Optimal K:", optimal_K)
print("Optimal Correlation:", optimal_correlation)
print("P-value:", optimal_p_value)

"""# Visualize morphological variability in fossil vs modern data (PC1 and PC2)"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from scipy.spatial import ConvexHull

# Load fossil and modern data
df_rutundu = pd.read_csv("E:Grass_Images_Patches_Fossils_Concatenated_Features.csv", header=None)
df_modern = pd.read_csv("E:Grass_Images_Patches_Concatenated_Features.csv", header=None)

# Assign labels for modern data
modern_labels = ['Modern'] * df_modern.shape[0]

# Concatenate datasets and labels
X_combined = np.concatenate([df_rutundu, df_modern], axis=0)
Y_combined = np.concatenate([ages, modern_labels], axis=0)

scaler = StandardScaler()
X_combined_scaled = scaler.fit_transform(X_combined)


# PCA on the entire concatenated dataset (including modern data)
pca = PCA(n_components=2)
X_pca_combined = pca.fit_transform(X_combined_scaled)

# Sort unique labels with 'Modern' first, followed by the fossil data from youngest to oldest
unique_labels = sorted(np.unique(Y_combined_str), key=lambda x: (x != 'Modern', float(x) if x != 'Modern' else float('inf')))
n_labels = len(unique_labels)

# Subplot grid
n_cols = 6
n_rows = n_labels // n_cols + (n_labels % n_cols > 0)
fig, axes = plt.subplots(n_rows, n_cols, figsize=(25, 18))
fig.subplots_adjust(hspace=0.5, wspace=0.5)

x_limits = [np.min(X_pca_combined[:, 0]), np.max(X_pca_combined[:, 0])]
y_limits = [np.min(X_pca_combined[:, 1]), np.max(X_pca_combined[:, 1])]

# Colors for the convex hulls and points
hull_colors = plt.cm.viridis(np.linspace(1, 0, n_labels))

for i, label in enumerate(unique_labels):
    ax = axes[i // n_cols, i % n_cols]

    # Project PCA scores for given label (depth or modern)
    specimens_at_label = X_combined_scaled[Y_combined_str == label]
    specimens_pca = pca.transform(specimens_at_label)

    # Plot PCA results for the depth/modern
    ax.scatter(specimens_pca[:, 0], specimens_pca[:, 1], s=3, color=hull_colors[i], alpha=0.6, label="")

    # Convex hull
    if len(specimens_pca) > 2:
        hull = ConvexHull(specimens_pca)
        hull_points = specimens_pca[hull.vertices]
        ax.fill(hull_points[:, 0], hull_points[:, 1], color=hull_colors[i], alpha=0.2)
        # For closed polygon
        for simplex in hull.simplices:
            ax.plot(specimens_pca[simplex, 0], specimens_pca[simplex, 1], color=hull_colors[i], linewidth=1)
        ax.plot(np.append(hull_points[:, 0], hull_points[0, 0]), np.append(hull_points[:, 1], hull_points[0, 1]), color=hull_colors[i], linewidth=1)

    ax.set_title(f'{label} cal. yr BP' if label != 'Modern' else 'Modern', fontsize=14)
    ax.set_xlabel('PC1', fontsize=12)
    ax.set_ylabel('PC2', fontsize=12)

    ax.tick_params(axis='both', which='major', labelsize=12)

    ax.set_xlim(x_limits)
    ax.set_ylim(y_limits)

for j in range(i + 1, n_rows * n_cols):
    fig.delaxes(axes[j // n_cols, j % n_cols])

plt.show()