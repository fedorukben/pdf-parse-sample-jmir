# This is a simple demonstration of parsing PDFs for JMIR

There are a few files. The main python file -- pdfparse.py -- contains all of the code for the demonstration. Aside from this file, you will see sets of "duplicate" files (with differing extensions). The PDFs are the important documents, the odts and odf documents were created in LibreOffice (and should be accessible in Microsoft Word if necessary). 

pdf-only-text contains various types of text to ensure that the parser works for all forms of text-based inputs.

sample-equation contains a sample equation created in LibreOffice Math. The PDF contains the formatted equation and the command used to create it -- what is imortant in this demonstration is how the equation itself is displayed. 

pdf-visuals contains several types of visuals in a PDF along with text -- it is implied that captions will work, as they are simply text. The visuals include tables, as well as images with/without text. All images are not parsed. 
