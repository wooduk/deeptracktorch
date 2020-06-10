# Welcome to Deep Track Torch
> A deep-learning based particle tracker using PyTorch.


`deeptracktorch` is a library for building and running a neural network that can to extract the position of objects in microscopy images or video. 

It is based on [DeepTrack](https://github.com/softmatterlab/DeepTrack) by Saga Helgadottir, Aykut Argun and Giovanni Volpe.

DeepTrackTorch started as a conversion of the DeepTrack to the PyTorch framework. 

## Installing

deeptracktorch is is on PyPI so you can just run:

`pip install deeptracktorch`

For an editable install, use the following:

```git clone https://github.com/wooduk/deeptracktorch
pip install -e deeptracktorch```

## How to use

The module can either be used as a library within python projects (e.g. Jupyter Notebooks) or as a standalone command line tool.

The module allows you to:
* train a neural net using synthetic images
* use that or pre-trained neural nets to extract particle position information from microscopy images or video.

### Example 1: track particles in a video

`deeptrack track <video>`

### Example 2: Train a NN

`deeptrack generate <params_file>` 

`deeptrack train <model> <input>`
