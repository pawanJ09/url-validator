ROOT_PATH := ${CURDIR}
SRC_PATH = ${ROOT_PATH}/src
SHEET_PATH = ${ROOT_PATH}/sheet
ZIP_PATH = ${ROOT_PATH}/url-validator.zip

install:
	pip install -r requirements.txt

bundle-lambda-function-zip:
	rm -rf ${ZIP_PATH}
	zip ${ZIP_PATH} requirements.txt
	cd ${SRC_PATH} && zip -r ${ZIP_PATH} .
	cd ${SHEET_PATH} && zip -r ${ZIP_PATH} .
