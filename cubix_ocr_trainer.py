
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
    def makeData(self, folderPath, createBox=True):
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
                    box_file = tif_file.split(".")[0] + "." + tif_file.split(".")[1] + ".box"
                    components = box_file.split(".")
                    lang = components[0]
                    font = components[1]
                    if createBox == True:
                        os.system("tesseract " + tif_file + " " + lang +"."+font+".box nobatch box.train")
                except Exception as e:
                    print("your data may not be properly created :" + str(e))

        os.system("unicharset_extractor "+lang+"*.box")
        os.system("mftraining -F font_properties -U unicharset " + lang + "*.tr")
        os.system("cntraining " + lang + "*.tr")

        # Remove unnecessory files from directory
        os.rename('inttemp', lang + '.inttemp')
        os.rename('shapetable', lang + '.shapetable')
        os.rename('normproto', lang + '.normproto')
        os.rename('pffmtable', lang + '.pffmtable')
        os.rename('unicharset', lang + '.unicharset')
        os.system("combine_tessdata " + lang + '.')

        print("copy your " + lang + ".traineddata to tesserect-ocr folder")
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
        for tif_file in os.listdir(tiff_folder):
            if tif_file.split(".")[-1] in ["tif"]:
                lang = tif_file.split(".")[0]
                os.system("tesseract " + tif_file + " " + lang + ".box nobatch box.train")
        print("boxes for each tiff image created, you can update those files....")
