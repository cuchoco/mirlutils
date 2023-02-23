import numpy as np
import SimpleITK as sitk 
import pydicom

def dicom_to_nifti(src:str , dst:str):
    """
    src : dicom directory path
    dst : nifti save path with .nii suffix 
    """
    reader = sitk.ImageSeriesReader()
    dicoms = reader.GetGDCMSeriesFileNames(str(src))
    reader.SetFileNames(dicoms)
    image = reader.Execute()
    sitk.WriteImage(image, str(dst))

def get_array(file_path:str, dtype=np.float64):
    """
    Get numpy array from .img, .dcm, .hdr, .nii
    file_path : path
    """
    temp = sitk.ReadImage(str(file_path))
    return sitk.GetArrayFromImage(temp).astype(dtype)

def windowing(array, wl, ww, normalize=True):
    """
    array : target array to adjust window setting
    wl : window level
    ww : window width
    normalize : return values in range (0-1) 
    """
    lower_bound = wl - ww/2
    upper_bound = wl + ww/2

    if normalize:
        return (np.clip(array, lower_bound, upper_bound) - lower_bound) / ww
    else:
        return np.clip(array, lower_bound, upper_bound) 

# Save as dicom file
def save_dicom(src_dicom_path:str, pixel_array:np.array, dst_dicom_path:str):
    """
    Save output image to dicom
    """
    dcm = pydicom.dcmread(src_dicom_path, force=True)
    intercept = dcm.RescaleIntercept
    slope = dcm.RescaleSlope
    pixel_array = (pixel_array - intercept) / slope
    pixel_array = pixel_array.astype(np.int16)

    dcm.file_meta.TransferSyntaxUID = pydicom.uid.ExplicitVRLittleEndian
    dcm.PixelData = pixel_array.squeeze().tobytes()

    if hasattr(dcm, 'SmallestImagePixelValue') and hasattr(dcm, 'LargestImagePixelValue'):
        dcm.SmallestImagePixelValue = pixel_array.min()
        dcm.LargestImagePixelValue = pixel_array.max()
        dcm[0x0028,0x0106].VR = 'US'
        dcm[0x0028,0x0107].VR = 'US'

    dcm.save_as(dst_dicom_path)