# Name: Cubix.co
# Version: 1.0
# Summary: Used to train your own custom Tesserect OCR
# Author: Rafi Ullah
# Author-email: rafiullah.khan@cubixlabs.com
# License: Cubix Code OpenSource (C20)

import os
class CubixTOCR:

    # this is used to train you own custom ocr, You have to provide tiff images and box files
    # you must provide font_properties file
    def makeData(self, folderPath, createBox=True, language='eng'):
        '''
        :param folderPath: path where you have tiff files and box files
        :param createBox: if this is true box will also be created
        :return: lang.traineddata file
        '''
        if str(folderPath) == "":
            print("---> Must provide training images folder path <----")
            print("---> /home/cubix/projects/trainingData/ <----")
        elif str(folderPath)[-1] == "/":
            folderPath = folderPath
        else:
            folderPath == folderPath+"/"

        if 'font_properties' not in os.listdir(folderPath):
            print "Provide font_properties file ...."
            return

        # for all tiff file do training process
        for tif_file in os.listdir(folderPath):
            if tif_file.split(".")[-1] in ["tif"]:
                try:
                    print("processing tiff file "+str(tif_file))
                    if createBox == True:
                        filename = tif_file[:-4]
                        os.system("tesseract " + tif_file + " " +filename+".box nobatch box.train")
                except Exception as e:
                    print("your data may not be properly created :" + str(e))

        os.system("unicharset_extractor "+language+"*.box")
        os.system("mftraining -F font_properties -U unicharset " +language+"*.tr")
        os.system("cntraining "+language+"*.tr")

        # Rename files from directory
        os.rename('inttemp', language + '.inttemp')
        os.rename('shapetable', language + '.shapetable')
        os.rename('normproto', language + '.normproto')
        os.rename('pffmtable', language + '.pffmtable')
        os.rename('unicharset', language + '.unicharset')
        os.system("combine_tessdata " + language + '.')

        print("copy your " + language + ".traineddata to tesserect-ocr folder")
        print("directory can be found at usr/share/tesserect-ocr/tessdata")

        #delete all unnessary files
        os.remove("eng.inttemp")
        os.remove("eng.normproto")
        os.remove("eng.pffmtable")
        os.remove("eng.shapetable")
        os.remove("eng.unicharset")

    def makeBox(self, tiff_folder):
        '''
        :param tiff_folder: path of tiff images
        :return:
        '''

        if str(tiff_folder) == "":
            print("---> Must provide training images folder path <----")
            print("---> /home/cubix/projects/trainingData/ <----")
        elif str(tiff_folder)[-1] == "/":
            folderPath = tiff_folder
        else:
            tiff_folder == tiff_folder+"/"

        for tif_file in os.listdir(tiff_folder):
            if tif_file.split(".")[-1] in ["tif"]:
                filename = tif_file[:-4]
                os.system("tesseract " + tif_file + " " + filename + ".box nobatch box.train")
        print("boxes for each tiff image created, you can update those files....")

# cu = CubixTOCR()
# cu.makeBox("/home/rafiullah/PycharmProjects/teeserect_ocr/")