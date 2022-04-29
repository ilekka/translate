#!/bin/bash

source /home/ilkka/anaconda3/etc/profile.d/conda.sh
conda activate deepl
python /home/ilkka/.translate/translate.py
conda deactivate
