# DocUtils-python

Python script utilities to handle the operations on different documents

## 1st function : convert the encoding of txt file to utf-8

Put the files to into source_dir, run the script and the obtain the output.zip   

### Run with Python  
- `conda create --name docutils python=3.11`
- `conda activate docutils`
- `pip install -r requirements.txt`  
- `python app.py`  
** to remove the env : `conda deactivate && conda env remove --name docutils`
  
### Run with Docker
- `cd /path/to/dir`  
- `docker image build -t docutils-python .`  
- `docker container run --rm -v ./:/usr/src/app --name docutils-python docutils-python`  
  (--rm : remove the container completely, but the dir in host will remain)
