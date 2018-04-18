# TesserectOCR
This project is to contribute to applications of tesserect OCR


1) You have to create a directory where you have all tif files
2) Now run makeBox method by applying tif images directory

###### if you have single tif image, use format language.fontStyle.tif, i-e eng.arial.tif
###### if you have multiple tif images use format language.fontStyle.Num.tif, i-e eng.arial.1.tif, eng.arial.2.tif

###### You can also make box files manually using https://pp19dd.com/tesseract-ocr-chopper/?i=ocrdMTGbD

3) You will see *.box files (one per tif image file)
4) Make correction in that box files by opening in editor like notepad++
5) Then execute makeData method by giving directory of tif images as an argument
6) You will see language.traineddata file, like eng.traineddata
7) Copy that file to tesserect-ocr/tessdata folder

:) Enjoy your own trained tesserect ocr. 
