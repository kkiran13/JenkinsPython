p=`pwd`
echo $p
export PYTHONPATH=$p
pip install -r requirements.txt
python test/addtest.py
