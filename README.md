# Radiomics Image Analysis System Design 

This is a system which can extract, select, and analyze radiomics features from medical images. I used cervial cancer images as demo.

## Results
- Background investigation of cervial cancer worldwide

- ROC Curve of SVC classification for radiomics features(SVC achieved the best performance)

- GUI 

## Files
- FeatureExtraction.py: Extracted Radimoics features from images
- LogiRegre_AB.py: Logist Regression for classification
- SVC_AB.py: SVC for classification
- SVR_AB.py: SVR for classification
- StatisticalAnalysis.py: Selected discriminative MRI-defined features with T-test and Rank-test
- ToolsFunc.py: Some tools
- demo_extracting.py: Demo for feature extraction of five modalities
- demo_stats.py: Demo for statistical analysis of five modalities
