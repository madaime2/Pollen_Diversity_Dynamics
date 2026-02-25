# Deep learning of fossil pollen morphology reveals 25,000 years of ecological change in East African grasslands

<p align="center">
  <img src="https://github.com/madaime2/Pollen_Biodiversity_Reconstruction/blob/main/Figures_Rutundu/Rutundu_Figure_2_Revised.png" width="950" title="hover text">
</p>



<p align="center">
  <img src="https://github.com/madaime2/Pollen_Biodiversity_Reconstruction/blob/main/Figures_Rutundu/Rutundu_Figure_1_4_Revised.png" width="750" title="hover text">
</p>
  
# Abstract
Grass pollen is largely overlooked in investigating grassland evolution because the pollen of most species cannot be differentiated using traditional optical microscopy. However, deep learning can quantify small variations in pollen morphology visible under superresolution microscopy. We use the abstract features output by deep learning to estimate the taxonomic diversity and physiology of fossil grass pollen assemblages. Using a semi-supervised learning strategy, we trained convolutional neural networks (CNNs) on superresolution pollen images of modern grasses and unlabeled fossil Poaceae. Our models captured features that reflected both the taxonomic diversity of grass communities along an elevational gradient and morphological differences between C<sub>3</sub> and C<sub>4</sub> species. We applied our trained models to fossil grass pollen assemblages from a 25,000-year lake-sediment record from eastern equatorial Africa (Mt. Kenya) and correlated past shifts in grass diversity with atmospheric CO<sub>2</sub> concentration and proxy records of local temperature, precipitation, and fire occurrence. We quantified changes in grass diversity using morphological variability of fossil pollen assemblages, approximated by the Shannon entropy of CNN features. Our data show that grassland species diversity was strongly reduced between 21,500 and 16,000 years ago, coincident with most severe regional cooling during the last ice age. C<sub>3</sub>:C<sub>4</sub> ratios reconstructed using a gradient-boosted decision tree classifier infer a gradual decrease in C<sub>4</sub> grasses since the late-glacial to Holocene transition, associated with decreasing fire activity and elevated temperatures. Our results demonstrate that CNN features of pollen morphology can advance palynological analysis, enabling robust estimation of grass diversity and C<sub>3</sub>:C<sub>4</sub> ratio in ancient grassland ecosystems. 

# Significance Statement 
Although the pollen of most grass species are morphologically indistinguishable using traditional optical microscopy, we show that they can be differentiated through deep learning analyses of superresolution images. Abstracted morphological features derived from convolutional neural networks can be used to quantify the biological and physiological diversity of grass pollen assemblages, without a priori knowledge of the species present, and used to reconstruct past changes in the taxonomic diversity and relative abundance of C<sub>4</sub> grasses in ancient grasslands. This approach unlocks ecological information previously unattainable from the fossil pollen record and demonstrates that deep learning can solve some of the most intractable identification problems in the reconstruction of past vegetation dynamics.

# Main Structure 
There are three main folders in this repository:
1. [Training and Classification](https://github.com/madaime2/Pollen_Diversity_Dynamics/tree/main/00_Training_and_Classification): Scripts for training the two classification models described in the paper using two modalities: maximum intensity projection (MIP) images, and patches.
2. [Diversity Estimation](https://github.com/madaime2/Pollen_Diversity_Dynamics/tree/main/01_Diversity_Estimation): Scripts for running the ecological simulations described in the paper and for applying Shannon entropy to calculate morphological diversity along the Lake Rutundu sediment core over the past 25,000 years. 
3. [Photosynthetic Pathway Analysis](https://github.com/madaime2/Pollen_Diversity_Dynamics/tree/main/02_Photosynthetic_Pathway_Analysis): Scripts for detecting morphological differences between C<sub>3</sub> and C<sub>4</sub> grass pollen while accounting for phylogenetic relatedness, and for developing a random forest classifier to identify the photosynthetic pathway (C<sub>3</sub> or C<sub>4</sub>) of grass fossil pollen based on morphology alone. 

# Hardware Specifications
Experiments were conducted on an NVIDIA GeForce RTX3090 GPU card with 24 GB of memory and an NVIDIA A100 SXM4 card with 40 GB of memory. We used the [PyTorch toolbox](https://pytorch.org/) for training neural networks. Additionally, some analyses were performed using R on a standard CPU.
