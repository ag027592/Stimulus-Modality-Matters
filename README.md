# Overview
This repository provides the implementation of Stimulus Modality Matters: Impact of Perceptual Evaluations from Different Modalities on Speech Emotion Recognition System Performance, published at the 2025 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP).

📄 IEEE Xplore: https://ieeexplore.ieee.org/abstract/document/10890558

📘 arXiv Preprint: https://arxiv.org/abs/2409.10762

👥 Authors: Huang-Cheng Chou, Haibin Wu, Hung-yi Lee, and Chi-Chun Lee

# Installation
 1. The project is developed based on [s3prl](https://github.com/s3prl/s3prl#installation) toolkit, please install it first.
    * Please follow the [instrution](https://s3prl.github.io/s3prl/tutorial/installation.html#editable-installation) to do editable installation
      ```
      git clone https://github.com/s3prl/s3prl.git
      cd s3prl
      pip install -e .
      ```
2. Move the ```emo``` folder into the path ```s3prl/s3prl/downstream```
3. Move the ```data folder``` into the path ```s3prl/s3prl/``` 
   * Download wav files into the folder for the database (e.g., ```data/CREMA-D/Audios```) by submiting the EULA form for the six databases.
   * [CREMA-D](https://github.com/CheyneyComputerScience/CREMA-D)

# Data Explanation
* fold1 - fold5: voice-only
* fold5 - fold10: audio-visual
* fold11 - fold15: **proposed all-inclusive label set**
* fold16 - fold20: face-only

## Training Models 
### (Example) Use the command line. We take the **fbank** as an example.
```
for upstream in fbank; do 
 for test_fold in fold1 fold2 fold3 fold4 fold5; do
  for corpus in CREMAD; do
  python3 run_downstream.py -n ${upstream}_${corpus}_$test_fold -m train -u ${upstream} -d emo -c downstream/emo/config_${corpus}.yaml -o "config.downstream_expert.datarc.test_fold='$test_fold'"
  python3 run_downstream.py -m evaluate -e result/downstream/${upstream}_${corpus}_${test_fold}_multimodal/dev-best.ckpt
  done;
 done;
done
```

## Model Training and Evaluation
``` bash
$ bash run_log_test.sh
```

## Trained WavLM Models
* All files can be downloaded by the [link](https://drive.google.com/file/d/1mzP6wEJkh4WVHZGsaGiaCcwOT8s0D7GK/view?usp=sharing).
* Unzip the .zip file and move the folder into the path (s3prl/s3prl/result/downstream/)

# Citation
If you find this work useful in your research, please cite:
 ```
@INPROCEEDINGS{Chou_2025,
  author={Chou, Huang-Cheng and Wu, Haibin and Lee, Chi-Chun},
  booktitle={ICASSP 2025 - 2025 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)}, 
  title={Stimulus Modality Matters: Impact of Perceptual Evaluations from Different Modalities on Speech Emotion Recognition System Performance}, 
  year={2025},
  pages={1-5},
  keywords={Training; Emotion recognition; Databases; System performance; Speech recognition; Signal processing; Acoustics; Speech processing; Standards; Testing; speech emotion recognition; the effects of stimulus modality; the ambiguity of emotions},
  doi={10.1109/ICASSP49660.2025.10890558}
}
 ```
