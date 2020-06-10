DeepTrack model trained on 100k examples on collab

The base distributions:

train_img_dist = {   
    'n_particles': lambda: <variable>,
    'size': lambda: 51,
    'bkgd_level': lambda: uniform(0.2,0.8),
    'gradient_intensity': lambda: uniform(0,1),
    'gradient_direction': lambda: uniform(-pi,pi),
    'snr': lambda: uniform(10,100),
}

train_p_dist = {
    # the position of the particle relative to center of image. -1 to +1 being the edges in each direction.
    'x': lambda: <variable>,
    'y': lambda: <variable>,
    
    # I don't know what units this is in... pixels?
    'radius': lambda: uniform(1.5, 3),
    'intensities': lambda: [uniform(.7, .9, 1), -uniform(.2, .3, 1)],
    'bessel_orders': lambda: [1, 2]    ,
    'ellip_direction': lambda: uniform(-pi, pi),
    'ellipticity':  lambda: 1,
}

Each of the model files:

Different modification the to the base ditsributions

Multiple Particles:
05p_close/export.pkl : Number of particles between 0 and 5, x and y from normal(0, 0.01)
05p_spread/export.pkl : Number of particles between 0 and 5, x and y from normal(0, 0.3)

Up to 1 particle:
01p_close/export.pkl : Either 0 or 1 particles, x/y from normal(0, 0.01)
01p_spread/export.pkl :  Either 0 or 1 particles, x/y from normal(0, 0.3)

Exactly 1 particle:
1p_close/export.pkl : Exactly 1 particle, x/y from normal(0,0.01) 
1p_spread/export.pkl : Exactly 1 particle, x/y from normal(0,0.3)
