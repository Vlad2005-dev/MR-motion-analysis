# PET/MR Motion Analysis using EPI BOLD MRI

This repository contains a small analysis pipeline to extract and visualise 
rigid-body motion of a moving PET/MR head phantom using motion parameters 
derived from EPI BOLD MRI.

The work is based on real PET/MR phantom data acquired on a Siemens Biograph
mMR system and is inspired by the motion-correction framework described in 
*Einspänner et al., 2022*. The paper can be found in references/

To see the plots visualing head movement see results/

---

## Overview

The workflow consists of two stages:

1. Preprocessing and motion estimation (external tools, run via terminal)
2. Motion parameter extraction and visualisation (Python code in this repository)

This repository focuses on stage (2). Stage (1) is documented for reproducibility.

---

## Folder Structure

pet-mr-motion-analysis/
├── data/              # MCFLIRT .par files (motion parameters)
├── motion_plots.py    # Python script for motion extraction and plotting
├── results/           # Generated motion plots
├── references/        # Relevant paper (Einspänner et al., 2022)
└── README.md

## Data and Preprocessing (Terminal-based)

### 1. DICOM to NIfTI conversion

The EPI BOLD MRI data were originally provided in DICOM format and converted to 4D NIfTI using `dcm2niix`:

dcm2niix -z y -o output_nifti_folder input_dicom_folder

This produces a 4D NIfTI file containing the full EPI time series.

### 2. Motion estimation using MCFLIRT

Rigid-body motion parameters were estimated using FSL MCFLIRT, run from the terminal:

mcflirt -in epi_bold.nii.gz -out epi_mc

This generates the file: epi_mc.par which contains six motion parameters per timepoint:

	•	rotations (rx, ry, rz)
	•	translations (x, y, z) in millimetres

These .par files are stored under the data/ directory and are the only inputs used by the Python code in this repository.

## Motion Analysis (Python)

The script motion_plots.py:
	•	Loads MCFLIRT .par files for different motion conditions (4 mm, 8 mm, 12 mm, 20 mm, and a complex motion pattern)
	•	Extracts the translational components
	•	Shifts the motion so that the minimum displacement is zero
	•	Plots translation along the z-direction as a function of time
	•	Saves the resulting figures to the results/ directory

Each timepoint corresponds to 2 seconds, matching the EPI repetition time.

## Notes 

	•	This project does not perform PET reconstruction or motion correction itself.
	•	The aim is to characterise motion from MRI as a precursor to motion-aware PET reconstruction.
	•	The analysis mirrors the motion-extraction step used in published PET/MR motion-correction pipelines.

## References

Einspänner, E. et al.
Evaluating different methods of MR-based motion correction in simultaneous PET/MR using a head phantom moved by a robotic system.
EJNMMI Physics, 2022.


