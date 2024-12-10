# Developing a CNN for Identifying Specific Individuals in Varying Image Qualities

**Authors:** Anthony DiBenedetto, Austin Kind  
**Course:** DATA-49000  
**Department:** Engineering, Computing, and Mathematical Sciences, Lewis University  
**Date:** 24 November 2024  

---

## Overview

This repository contains the resources, data, and code for the research project titled **"Developing a CNN for Identifying Specific Individuals in Varying Image Qualities"**. The project investigates how Convolutional Neural Networks (CNNs) can be optimized for facial recognition in images with varying levels of noise and quality. A novel dynamic denoising layer utilizing Gaussian filters was introduced to improve performance on noisy data.

---

## Table of Contents

1. [Abstract](#abstract)  
2. [Features](#features)  
3. [Dataset](#dataset)  
4. [Methodology](#methodology)  
5. [Results](#results)  
6. [Installation](#installation)  
7. [Usage](#usage)  
8. [Acknowledgments](#acknowledgments)  
9. [References](#references)  

---

## Abstract

This study explores the integration of a dynamic denoising layer into a CNN for facial recognition under varying conditions. The model was trained on images of Tony Soprano from *The Sopranos* with different noise levels (low, moderate, and high) and simulated infrared conditions. The proposed architecture achieved an overall average accuracy of **72%**, with **85.7% accuracy on base images** and a significant decline in performance on higher noise levels. The project provides a foundation for improving recognition systems in noisy or low-quality environments.

---

## Features

- **Dynamic Denoising Layer:** Implements Gaussian smoothing to reduce noise dynamically.
- **Custom Dataset:** Contains 125 images with varying noise levels and infrared simulations.
- **Model Architecture:** Seven convolutional and pooling layers, optimized for noisy inputs.
- **Performance Metrics:** Evaluated with mean squared error and custom bounding box thresholds.

---

## Dataset

The dataset includes 125 images of Tony Soprano divided into five groups:
- Base (original, high-quality images)
- Low-noise
- Moderate-noise
- High-noise
- Simulated infrared

Each group contains 25 annotated images labeled with bounding boxes using [LabelImg](https://github.com/tzutalin/labelImg). Noise levels were applied using a Gaussian noise function with varying variances.

---

## Methodology

### Model Design
The CNN includes:
- A **dynamic denoising layer** using Gaussian filters.
- Seven convolutional layers and pooling layers for feature extraction.
- Dropout layers to prevent overfitting.
- Fully connected layers for predicting bounding box coordinates.

### Training
- Dataset split: 80% training, 20% testing.
- Augmentation: Horizontal flipping, rotation, and brightness adjustments.
- Optimizer: Adam optimizer with a mean squared error (MSE) loss function.

---

## Results

- **Base Images:** 85.7% accuracy.  
- **Low-Noise Images:** High accuracy with slight misalignments.  
- **Moderate-Noise Images:** Occasional bounding box misalignment.  
- **High-Noise Images:** 50% accuracy due to extreme graininess.  
- **Infrared Images:** Moderate performance with some missed detections.  

Visualization examples and performance metrics are detailed in the results folder.

---
