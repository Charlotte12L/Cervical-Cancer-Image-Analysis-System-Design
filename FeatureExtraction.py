import SimpleITK as sitk
import six
import sys, os
import radiomics
from ToolsFunc import select_file, write_csv, Normalize, fuse_mask

def FeatureExtraction(Param, addr, selector, sav_folder, mask_value):

    subjects = os.listdir(addr)

    for i in subjects:
        # i = 'B10'
        img_addr = addr + i + '/Tumor/'
        mask_addr = addr + i + '/Label/'
        saving_folder = sav_folder + selector + '_Features/'
        if os.path.exists(saving_folder) == 0:
            os.makedirs(saving_folder)

        print('----' + selector + '----' + i + '----begin------')

        ImageName = select_file(img_addr, selector)
        MaskName = select_file(mask_addr, selector)
        img = sitk.ReadImage(ImageName)
        img_normed = Normalize(img, 255)

        if os.path.isfile(MaskName):
            mask_init = sitk.ReadImage(MaskName)
            mask = fuse_mask(mask_init)

        extractor = radiomics.featureextractor.RadiomicsFeaturesExtractor(Param)

        # calculate features on prostate mask

        result_Of_prostate = extractor.execute(img_normed, mask)
        filename_of_prostate = saving_folder + '/' + str(i) + '.csv'
        write_csv(result_Of_prostate, filename_of_prostate)
        print('----' + selector + '----' + i + '----end------')