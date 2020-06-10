# set up plot styling
import matplotlib

matplotlib.style.use('ggplot')
font = {'family' : 'Helvetica Neue', 'size'   : 16}
matplotlib.rc('font', **font)
matplotlib.rc('axes',facecolor='#ffffff')
matplotlib.rc('axes',edgecolor='#333333')
matplotlib.rc('figure',figsize=(12,6))