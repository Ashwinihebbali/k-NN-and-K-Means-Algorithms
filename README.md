# k-NN and K-Means Algorithms – Complete Interactive Guide

![ML Algorithms](https://img.shields.io/badge/Machine%20Learning-Algorithms-blue)
![React](https://img.shields.io/badge/React-18.3-61dafb)
![TypeScript](https://img.shields.io/badge/TypeScript-5.5-3178c6)
![License](https://img.shields.io/badge/License-MIT-green)

## Overview

An interactive web-based demonstration of two fundamental machine learning algorithms:

- **k-Nearest Neighbors (k-NN)** → Supervised Learning (Classification)
- **K-Means Clustering** → Unsupervised Learning (Clustering)

Both algorithms are distance-based and widely used in real-world applications. This project provides an educational, visually engaging way to understand how these algorithms work.

## Features

- **Interactive Visualizations**: Real-time canvas-based visualizations showing algorithm behavior
- **Adjustable Parameters**: Experiment with different k values to see how they affect results
- **Educational Content**: Comprehensive explanations, comparisons, and best practices
- **Production Ready**: Built with modern web technologies (React, TypeScript, Tailwind CSS)
- **Responsive Design**: Works seamlessly on desktop and mobile devices

## What is k-Nearest Neighbors (k-NN)?

### Definition

k-Nearest Neighbors (k-NN) is a supervised learning algorithm used for classification and regression. It classifies a new data point based on the majority class of its k nearest neighbors.

### How k-NN Works

1. Choose the number of neighbors `k`
2. Calculate distance (usually Euclidean) from test point to all training points
3. Find the `k` nearest data points
4. Assign the most common class among the neighbors

### Distance Formula (Euclidean)

```
d = √[(x₂-x₁)² + (y₂-y₁)²]
```

### Key Characteristics

- **Lazy learner**: No training phase required
- **Sensitive to feature scaling**: Distance calculations affected by scale
- **Performance depends on k**: Choosing optimal k is crucial

### Real-World Applications

- Recommendation systems
- Medical diagnosis
- Pattern recognition
- Image classification
- Handwriting recognition

## What is K-Means Clustering?

### Definition

K-Means is an unsupervised learning algorithm used to group data into k clusters based on similarity. It iteratively assigns points to clusters and updates cluster centers.

### How K-Means Works

1. Choose the number of clusters `k`
2. Randomly initialize k centroids
3. Assign each point to the nearest centroid
4. Update centroids to the mean of assigned points
5. Repeat steps 3-4 until convergence

### Objective Function (WCSS)

Minimize Within-Cluster Sum of Squares:

```
WCSS = Σ(xᵢ - c)²
```

Where `xᵢ` is a data point and `c` is the centroid.

### Key Characteristics

- **Unsupervised algorithm**: No labeled data required
- **Iterative process**: Converges to local optimum
- **Requires pre-defined k**: Number of clusters must be specified

### Real-World Applications

- Customer segmentation
- Image compression
- Market analysis
- Document clustering
- Anomaly detection

## Comparison: k-NN vs K-Means

| Feature | k-NN | K-Means |
|---------|------|---------|
| **Learning Type** | Supervised | Unsupervised |
| **Requires Labels** | Yes | No |
| **Output** | Class label | Cluster assignment |
| **Training Phase** | None (Lazy) | Yes (Iterative) |
| **Used For** | Classification/Regression | Clustering/Pattern discovery |
| **Parameter** | k (neighbors) | k (clusters) |
| **Computational Cost** | High at prediction | High at training |

## Project Structure

```
knn-kmeans-demo/
│
├── src/
│   ├── algorithms/
│   │   ├── knn.ts              # k-NN implementation
│   │   └── kmeans.ts           # K-Means implementation
│   │
│   ├── components/
│   │   ├── KNNVisualizer.tsx   # Interactive k-NN demo
│   │   ├── KMeansVisualizer.tsx # Interactive K-Means demo
│   │   └── Overview.tsx        # Educational content
│   │
│   ├── types/
│   │   └── algorithms.ts       # TypeScript interfaces
│   │
│   ├── App.tsx                 # Main application
│   ├── main.tsx                # Entry point
│   └── index.css               # Tailwind styles
│
├── index.html
├── package.json
├── tailwind.config.js
├── tsconfig.json
└── README.md
```

## Getting Started

### Prerequisites

- Node.js (v16 or higher)
- npm or yarn

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd knn-kmeans-demo
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

4. Open your browser and navigate to `http://localhost:5173`

### Building for Production

```bash
npm run build
```

The optimized build will be in the `dist/` directory.

## Usage Guide

### k-NN Demonstration

1. Navigate to the "k-NN Demo" tab
2. Adjust the k value using the slider (1-15 neighbors)
3. Click anywhere on the canvas to classify a test point
4. Yellow lines show connections to the k nearest neighbors
5. The predicted class is displayed based on majority voting
6. Click "Generate New Data" to create a fresh dataset

### K-Means Demonstration

1. Navigate to the "K-Means Demo" tab
2. Adjust the k value using the slider (2-6 clusters)
3. Click "Run K-Means" to start clustering
4. Watch as points are assigned to clusters
5. Centroids are shown as larger circles with borders
6. View iterations and WCSS (Within-Cluster Sum of Squares) in the results panel
7. Click "Reset Clustering" to clear and try different parameters

## Evaluation Metrics

### k-NN Metrics

- **Accuracy**: Percentage of correct predictions
- **Precision**: True positives / All predicted positives
- **Recall**: True positives / All actual positives
- **F1-Score**: Harmonic mean of precision and recall

### K-Means Metrics

- **WCSS**: Within-Cluster Sum of Squares (lower is better)
- **Silhouette Score**: Measures cluster separation quality (-1 to 1)
- **Elbow Method**: Plot WCSS vs k to find optimal number of clusters
- **Inertia**: Sum of squared distances to nearest centroid

## Choosing the Right Algorithm

### Use k-NN When:

✓ You have labeled training data
✓ You need to classify new data points
✓ Dataset is relatively small
✓ Decision boundaries are irregular
✓ You need probabilistic predictions

### Use K-Means When:

✓ You have unlabeled data
✓ You want to discover patterns or natural groupings
✓ You need to segment large datasets
✓ Clusters are roughly spherical
✓ You have a good estimate of k

## Technologies Used

- **React 18.3**: Modern UI library
- **TypeScript 5.5**: Type-safe JavaScript
- **Tailwind CSS 3.4**: Utility-first styling
- **Vite 5.4**: Fast build tool
- **Lucide React**: Beautiful icons
- **Canvas API**: High-performance visualizations

## Educational Use Cases

This project is perfect for:

- **College Projects**: Demonstrate understanding of ML algorithms
- **Viva & Exams**: Interactive demonstrations for presentations
- **GitHub Portfolios**: Showcase web development and ML knowledge
- **Interview Preparation**: Explain algorithms with visual aids
- **Teaching**: Use in classroom or tutorial settings
- **Self-Learning**: Experiment and understand algorithm behavior

## Future Enhancements

- [ ] Add more distance metrics (Manhattan, Minkowski)
- [ ] Implement weighted k-NN
- [ ] Add silhouette score visualization for K-Means
- [ ] Include Elbow Method chart
- [ ] Support for uploading custom datasets
- [ ] Add more clustering algorithms (DBSCAN, Hierarchical)
- [ ] Export results and visualizations
- [ ] Performance metrics dashboard
- [ ] Mobile touch gestures for interaction
- [ ] Dark mode support

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Inspired by classic machine learning textbooks and courses
- Built for educational purposes and learning
- Thanks to the open-source community for amazing tools and libraries

## Contact & Support

If you have questions, suggestions, or found this helpful, please:

- Star this repository
- Open an issue for bug reports or feature requests
- Share with others who might benefit from this educational tool

---

**Built with ❤️ for the learning community**

*Making machine learning accessible and interactive, one algorithm at a time.*
