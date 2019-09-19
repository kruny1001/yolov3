
## Quick Start

Create `conda` environment depending on whether you have a supported GPU or not:

```
mkdir cfg
cd cfg
wget https://pjreddie.com/media/files/yolov3.weights
cd cfg
wget https://pjreddie.com/media/files/yolov3-tiny.weights
```

```
conda env create -f environment-[c|g]pu.yml
conda env create -f environment-cpu.yml
conda env create -f environment-gpu.yml
source activate yolov3-[c|g]pu
source activate yolov3-gpu
```
### Demo on Web Cam:


To see it live on your Web Cam:

```
python webcam.py
```

