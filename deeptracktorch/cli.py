# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/99_cli.ipynb (unless otherwise specified).

__all__ = ['dtt_extract']

# Cell
from fastscript import *


# Cell
@call_parse
def dtt_extract(fname:Param("A directory containing images", str)=None,
               oname:Param("Name of output file [positions.csv]", str)='positions.csv'):
    "Extract positions of particles found in images contained in `fname`"
    # load trained model
    # parse directory
    # for each file call predict
    # write predicted position to outputfile

    pass