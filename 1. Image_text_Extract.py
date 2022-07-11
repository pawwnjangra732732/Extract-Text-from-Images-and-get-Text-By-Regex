import os
import glob
import time

import cv2
import numpy
import pytesseract
from pdf2image import convert_from_path
import PyPDF2
from PIL import Image
import pyautogui
import re
import shutil


path=pytesseract.pytesseract.tesseract_cmd=r"H:\AR PRODUCTION REPORTS\Business Intelligence\Chromedriver\tesseract.exe"
list1=[]
path_str=r"H:\AR PRODUCTION REPORTS\Business Intelligence\Python Automation\Payments\All Clients\ERA Renaming HP\Input\*.pdf"
file_locations=r"H:\AR PRODUCTION REPORTS\Business Intelligence\Python Automation\Payments\All Clients\ERA Renaming HP\Input\\"
Output_path=r"H:\AR PRODUCTION REPORTS\Business Intelligence\Python Automation\Payments\All Clients\ERA Renaming HP\Output\\"
for name in glob.glob(path_str):
    list1.append(name)

j=1
image_counter=1
# itereate over the file in the input folder
for item in list1:

    files = glob.glob(r"H:\AR PRODUCTION REPORTS\Business Intelligence\Python Automation\Payments\All Clients\ERA Renaming HP\out_text*.txt")

    for f in files:
        try:
            os.remove(f)
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))
    time.sleep(5)
    print("Item",item)
    #convert all pdf pages to Images and store to this Variable Pages
    pages = convert_from_path(item,poppler_path=r'H:\AR PRODUCTION REPORTS\Business Intelligence\Chromedriver\poppler-0.68.0\bin')
    Pdf_file=item
    #saving Image with different Names Like : page_1.jpg
    image_counter=1
    for page in pages:
        filename = "page_" + str(image_counter) + ".jpg"
        page.save(filename, 'JPEG')
        image_counter = image_counter + 1
    # assign the no of pages that are converted to image to filelimit tag
    filelimit = image_counter-1
    # outfile = "out_text_"+ str(j) +".txt"
    j=j+1
    with open(outfile,"a") as f:
        # Reading the image files using the ocr
        for i in range(1, filelimit + 1):
            filename = "page_" + str(i) + ".jpg"
            text = str(((pytesseract.image_to_string(Image.open(filename)))))
            # pyautogui.alert(text=text)
            time.sleep(1)
            text = text.replace('-\n', '')
            f.write(text)
            os.remove(filename)
        f.close()

    with open(outfile,"r") as f:
        string_text =f.read()
        # print(string_text)
        if ("File Name:" in string_text):
            if ("Provider Control Number" in string_text):

                # print("Provider control Number")

                try:
                    regex = "File\sName:\s.*\w{9,20}"
                    match = re.search(regex, string_text)
                    start = match.start()
                    end = match.end()
                    sub_string = string_text[start:end]
                    number_val = sub_string.split(" ")[-1]
                    number_val=number_val.strip()
                except:
                    regex = "Trace\s*Number:\s*\w{9,20}"
                    match = re.search(regex, string_text)
                    start = match.start()
                    end = match.end()
                    sub_string = string_text[start:end]
                    number_val = sub_string.split(":")[-1]
                    number_val=number_val.strip()
                # print(number_val)
                time.sleep(1)
                regex = "Provider Control Number"
                match = re.search(regex, string_text)
                start = match.start()
                end = match.end()
                pcn_val = string_text[end + 1:end + 4]
                # print(pcn_val)
                filename = pcn_val + "-" + number_val + "_835 Data File.pdf"
                # print(filename)
                try:
                    os.rename(item, file_locations + filename)
                    shutil.move(file_locations + filename, Output_path + filename)
                    print("Moved !")
                except:
                    print("File could Not renamed")

            else:
                try:
                    regex = "File\sName:\s.*\w{9,20}"
                    match = re.search(regex, string_text)
                    start = match.start()
                    end = match.end()
                    sub_string = string_text[start:end]
                    number_val = sub_string.split(" ")[-1]
                    number_val = number_val.strip()
                except:
                    regex = "Trace\s*Number:\s*\w{9,20}"
                    match = re.search(regex, string_text)
                    start = match.start()
                    end = match.end()
                    sub_string = string_text[start:end]
                    number_val = sub_string.split(":")[-1]
                    number_val = number_val.strip()
                # print(number_val)
                filename = number_val + "_835 Data File.pdf"
                # print(filename)
                try:
                    os.rename(item, file_locations + filename)
                    shutil.move(file_locations + filename, Output_path + filename)
                    print("Moved !")
                except:
                    print("File could Not renamed")



        else:
            if ("Unposted Listing" in string_text):
                time.sleep(5)
                # print("Unposted Listing")
                # print("_________________________________________________")
                # print(string_text)
                try:
                    regex = "\w{9,20}\s.*Unposted Listing"
                    match = re.search(regex, string_text)
                    # print(match)
                    start = match.start()
                    end = match.end()
                    sub_string = string_text[start:end]
                    number_val = sub_string.split(" ")[0]
                except:
                    regex = "Page\s*1\s*\w{9,20}"
                    match = re.search(regex, string_text)
                    start = match.start()
                    end = match.end()
                    sub_string = string_text[start:end]
                    number_val = sub_string.split(" ")[-1]
                    number_val = number_val.strip()
                time.sleep(2)
                # print("Unpostedosted_listing", number_val)
                regex = "Batch.*:.*-"
                match = re.search(regex, string_text)
                print(match)
                start = match.start()
                end = match.end()
                sub_string = string_text[start:end]
                value_p = sub_string.split(":")[-1]
                # print("posted Listing Batch ", value_p)
                filename = value_p + number_val + "_Unposted Listing by Check Number.pdf"
                # print(filename)
                time.sleep(2)
                try:
                    os.rename(item, file_locations + filename)
                    shutil.move(file_locations + filename, Output_path + filename)
                    print("Moved !")
                except:
                    print("File could Not renamed")
            else:
                if ("Credit Due Listing" in string_text):
                    # print("Credit Due Listing")
                    regex = "\w{9,20}\sCredit Due Listing"
                    match = re.search(regex, string_text)
                    start = match.start()
                    end = match.end()
                    sub_string = string_text[start:end]
                    number_val = sub_string.split(" ")[0]
                    time.sleep(2)
                    # var1 = string_text.split("Page 1")[-1]
                    # var2 = var1.split("Credit Due Listing")[0]
                    # number_val = var2.strip()
                    # print("Page 1 ", number_val)
                    regex = "\(.*?\)"
                    match = re.search(regex, string_text)
                    print(match)
                    start = match.start()
                    end = match.end()
                    value_in = string_text[start:end]
                    print(value_in)
                    time.sleep(2)
                    regex = "[^()]"
                    match = re.search(regex, value_in)
                    start = match.start()
                    end = match.end()
                    value_final = value_in[start:end + 2]
                    print(value_final)
                    filename = value_final + "-" + number_val + "_Credit Due Listing by Check Number.pdf"
                    print(filename)
                    # os.rename()
                    try:
                        os.rename(item, file_locations + filename)
                        shutil.move(file_locations + filename, Output_path + filename)
                        print("Moved !")
                    except:
                        print("File could Not renamed")

                else:
                    # No input file so block not tested
                    if ("Posted Listing" in string_text):
                        try:
                            print("Posted Listing")
                            time.sleep(5)
                            regex = "\w{9,20}\sPosted"
                            print(string_text)
                            match = re.search(regex, string_text)
                            print(match)
                            start = match.start()
                            end = match.end()
                            sub_string = string_text[start:end]
                            number_val = sub_string.split(" ")[0]
                            # print("Page 1 ", number_val)
                            # print("Posted_listing",number_val)
                            regex = "Batch\s*:\s*\w*"
                            match = re.search(regex, string_text)
                            print(match)
                            start = match.start()
                            end = match.end()
                            sub_string = string_text[start:end]
                            value_p = sub_string.split(":")[-1]
                            # print("posted Listing Batch ",value_p)
                            filename = value_p + "-" +number_val + "_Posted Listing by Check Number.pdf"
                            print(filename)
                            try:
                                os.rename(item, file_locations + filename)
                                shutil.move(file_locations + filename, Output_path + filename)
                                print("Moved !")
                            except:
                                print("File could Not renamed")
                        except:
                            # print("Posted Listing")
                            time.sleep(5)
                            regex = "\w{9,20}APC"
                            print(string_text)
                            match = re.search(regex, string_text)
                            print(match)
                            start = match.start()
                            end = match.end()
                            sub_string = string_text[start:end]
                            number_val = sub_string.split("APC")[0]
                            # print("Page 1 ", number_val)
                            # print("Posted_listing", number_val)
                            regex = "Batch\s*:\s*\w*"
                            match = re.search(regex, string_text)
                            print(match)
                            start = match.start()
                            end = match.end()
                            sub_string = string_text[start:end]
                            value_p = sub_string.split(":")[-1]
                            # print("posted Listing Batch ", value_p)
                            filename = value_p + "-" +number_val + "_Posted Listing by Check Number.pdf"
                            # print(filename)
                            try:
                                os.rename(item, file_locations + filename)
                                shutil.move(file_locations + filename, Output_path + filename)
                                print("Moved !")
                            except:
                                print("File could Not renamed")

                    else:
                        if ("ELECTRONIC REMITTANCE" in string_text):
                            # print("ELECTRONIC REMITTANCE")
                            print(string_text)
                            regex = "CHECK\s*NUMBER:\s*\w{8,20}"
                            match = re.search(regex, string_text)
                            print(match)
                            start = match.start()
                            end = match.end()
                            sub_string = string_text[start:end]
                            number_val = sub_string.split(" ")[-1]
                            # print(number_val)
                            time.sleep(2)
                            regex = "ACT:\s*APC"
                            match = re.search(regex, string_text)
                            # print(match)
                            start = match.start()
                            end = match.end()
                            sub_string = string_text[start:end]
                            value_p = sub_string.split(":")[-1]
                            value_p=value_p.strip()
                            # print(value_p)
                            filename = value_p + "-" + number_val + "_835 Electronic Remittance Summary.pdf"
                            # print(filename)
                            try:
                                os.rename(item, file_locations + filename)
                                shutil.move(file_locations + filename, Output_path + filename)
                                print("Moved !")
                            except:
                                print("File could Not renamed")
    os.remove(outfile)

