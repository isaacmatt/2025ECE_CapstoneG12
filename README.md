# Pothole Detection on Raspberry Pi

Real-time pothole detection system built on Raspberry Pi using a custom-trained YOLO model, with GPS tagging for geolocated reporting.

Capstone project — University of Manitoba, Computer Engineering (Group 12), Sept 2024 – Apr 2025.

---

## Overview

Roads accumulate damage faster than municipalities can survey it. This project explores a low-cost, vehicle-mountable solution: a Raspberry Pi paired with a camera and GPS module that detects potholes in real time as the vehicle drives, tags each detection with coordinates, and produces a structured log that can be fed into a municipal work-order system.

The system was designed end-to-end — from data collection and model training through edge deployment, GPS integration, and verification testing.


---

## System Architecture

```
┌─────────────┐     ┌──────────────┐     ┌──────────────┐
│   Camera    │────▶│  Raspberry   │────▶│  Detection   │
│   (Pi Cam)  │     │     Pi       │     │  Output Log  │
└─────────────┘     │              │     │  (CSV + GPS) │
                    │  YOLO model  │     └──────────────┘
┌─────────────┐     │  inference   │
│  GPS Module │────▶│              │
└─────────────┘     └──────────────┘
```

- **Capture layer:** Raspberry Pi [model — e.g., Pi 4B, 4GB] with [camera module — e.g., Pi Camera v2 or USB webcam]
- **Detection layer:** YOLO[v5/v8/n] model trained on a custom pothole dataset
- **Localization layer:** Serial GPS module providing real-time coordinates
- **Output layer:** Detection events written with timestamp, GPS coordinates, and confidence score for downstream processing

---

## My Contributions

As **Computer Vision & Machine Learning Lead**, I owned:

- **Detection pipeline design** — selected YOLO as the detection architecture based on edge-inference constraints, designed the end-to-end image capture → inference → logging pipeline
- **Model training and tuning** — curated and augmented the dataset using Roboflow, trained custom YOLO models, iterated on hyperparameters and dataset balance to improve precision/recall on real road imagery
- **Edge optimization** — tuned inference parameters on the Pi to hit a usable real-time frame rate while keeping detection accuracy acceptable
- **Verification** — translated system requirements into testable features and wrote staged test procedures covering camera capture, model inference, GPS integration, and end-to-end logging
- **Technical documentation** — authored design and verification documentation supporting capstone design reviews

---

## Dataset

- **Source:** [self-collected / public datasets / mix of both]
- **Size:** ~[1400] labeled images
- **Classes:** pothole (single-class detection)
- **Augmentation:** [rotation, brightness, blur, etc. — what you applied via Roboflow or `AugPhotos.py`]
- **Split:** [e.g., 70/20/10 train/val/test]
- **Roboflow project:** https://app.roboflow.com/capstone-g12/projects

The augmentation pipeline (`AugPhotos.py`) was used to expand training coverage for varied lighting, shadow, and surface conditions — pothole imagery in real driving conditions varies a lot more than typical benchmark datasets.

---

## Results

| Metric                           | Value                       |
|----------------------------------|-----------------------------|
| Precision                        | [91]%                        |
| Recall                           | [85]%                        |
| mAP@0.5                          | [90]                         |




---

## Repository Contents

| File                              | Purpose                                                              |
|-----------------------------------|----------------------------------------------------------------------|
| `AugPhotos.py`                    | Dataset augmentation script — expands training set with image variations |
| `GPS_extraction_from_Filename.py` | Parses GPS coordinates embedded in image filenames for ground-truth labeling |
| `CameraWithGPS_no_Bugs.txt`       | Working camera + GPS capture pipeline for the Pi                     |
| `bootscript.txt`                  | Boot-time setup script for autonomous startup on the Pi              |

---

## Hardware

- Raspberry Pi [model]
- [Camera module — model]
- [GPS module — model, e.g., NEO-6M]
- Power: [battery pack / vehicle 12V to 5V converter / etc.]

---



## Team

Capstone Group 12 — University of Manitoba, ECE Department, 2024–2025.

I led the computer vision / ML subsystem. Other team members contributed to [hardware integration / mechanical mounting / data collection / etc. — list briefly].

---

## License

MIT — see [LICENSE](LICENSE).
