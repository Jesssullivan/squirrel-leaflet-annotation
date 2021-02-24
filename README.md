## *leaflet audio annotator for the squirrels & munks*


# *archived* [visit squirrel & munk audio annotator](https://ai.columbari.us/annotator/audio)
# source zinged [into CI-EC2 branch](https://github.com/Jesssullivan/tmpUI/tree/CI-EC2) @ [tmpUI](https://github.com/Jesssullivan/tmpUI) 


1.  *setup:*
```
# node:
npm install
```
```
# python:
python3 -m venv merlinai_venv
source merlinai_venv/bin/activate
pip3 install -r requirements.txt
```

2.  *build & launch:*
```
# build:
npm run-script build
```
```
# run:
npm run-script run
```


3.  *Annotate:*
  - *open a browser to `127.0.0.1:5000/`*
  - *select & import directory ./squirrels_munks_task/*
  - *have at it*
