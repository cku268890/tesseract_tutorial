# tesseract_tutorial
This is tutorial shows how to install tesseract 4.1.1 correctly and list the [FAQ](#FAQ) down below.
## Environment
- centos 8.2

## Install
- Install version
  - tesseract 4.1.1
  - leptonica 1.80.0
- Requirement package (make sure account can use sudo!)
  - gcc-c++
  - zlib-devel
  - pkg-config
  - libtool automake autoconf
  - libjpeg-devel
  - libpng-devel
  - libtiff-devel
- Install steps
  - Install leptonica
    ```
    wget http://www.leptonica.org/source/leptonica-1.80.0.tar.gz
    tar -zvf leptonica-1.80.0.tar.gz
    cd leptonica-1.80.0
    ./configure
    make
    make install
    export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig/
    ```
  - Intsall tesseract
    ```
    wget -c -t 20 https://github.com/tesseract-ocr/tesseract/archive/4.1.1.tar.gz
    tar -xvf 4.1.1.tar.gz
    cd tesseract-4.1.1/
    ./autogen.sh
    ./configure --with-extra-includes=/usr/local/include --with-extra-libraries=/usr/local/include
    make
    make install
    ```
  - Download language library
  ```
  wget https://github.com/tesseract-ocr/tessdata/raw/master/eng.traineddata
  mv *.traineddata /usr/local/share/tessdata/
  ```
  - Usage
  ```
  tesseract <your_picture_file> <output_file_name> -l eng --psm 7 --oem 3 -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ
  ```
  - Tesseract parameters
    - --psm
    ```
    0 Orientation and script detection (OSD) only.
    1 Automatic page segmentation with OSD.
    2 Automatic page segmentation, but no OSD, or OCR.
    3 Fully automatic page segmentation, but no OSD. (Default)
    4 Assume a single column of text of variable sizes.
    5 Assume a single uniform block of vertically aligned text.
    6 Assume a single uniform block of text.
    7 Treat the image as a single text line.
    8 Treat the image as a single word.
    9 Treat the image as a single word in a circle.
    10 Treat the image as a single character.
    ```
    - --oem
    ```
    0 = Original Tesseract only.
    1 = Neural nets LSTM only.
    2 = Tesseract + LSTM.
    3 = Default, based on what is available.
    ```
## FAQ
- Nothing provides liblept.so.5()(64bit) needed by tesseract
  → ```[Condition]```While using tesseract show up this message!!
  → ```[SOLVE]```Install leptonica library, install step had been mention in the previous section.
- error: Leptonica 1.74 or higher is required. Try to install libleptonica-dev package
  → ```[Condition]``` While install tesseract and run the command: ./configure --with-extra-includes=/usr/local/include --with-extra-libraries=/usr/local/include
  → ```[SOLVE]``` export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig/
- Error opening data file /usr/local/share/tessdata/eng.traineddata  
  Please make sure the TESSDATA_PREFIX environment variable is set to your "tessdata" directory.  
  Failed loading language 'eng'  
  Tesseract couldn't load any languages!  
  Could not initialize tesseract.  
  → ```[Condition]``` After install tesseract, and running command: tesseract <your_picture_file> <output_file_name> -l eng
  → ```[SOLVE]``` export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig/
