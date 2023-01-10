import dicom2nifti
import os

patients_folders = os.listdir(path_to_all_patients)

for patients in patients_folder:
  dicom2nifti.convert_directory(os.path.join(path_to_all_patients, patient), os.path.join(path_to_all_patients, patient, ".nii.gz"))
