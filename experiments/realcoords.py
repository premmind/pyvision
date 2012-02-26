from vision.track.realprior import *
import vision.detectionreader
import vision.drawer
import os.path
from vision import visualize
import random

import vision.track.dp

logging.basicConfig(level = logging.DEBUG)

path = ("/csail/vision-videolabelme/databases/"
        "video_adapt/home_ac_a/frames/0/bundler")
path = "/csail/vision-videolabelme/databases/video_adapt/demos/bottle_table/bundler"
path = "/csail/vision-videolabelme/databases/video_adapt/home_ac_a/frames/5/bundler"

video = vision.flatframeiterator(path + "/..", start = 1)

root = os.path.join(path, "pmvs")
patches, projections = pmvs.read(root, start = 1)

category = 'sofa'

detections = vision.detectionreader.exemplarsvm('/csail/vision-videolabelme/databases/video_adapt/home_ac_a/frames/5/dets-sun11-dpm-{0}.mat'.format(category))

prior = ThreeD(video, patches, projections, sigma = 0.1)
prior.build(detections)

import pylab, numpy, Image
for frame, nd in prior.scoreall():
    print frame
    pylab.subplot(221)
    pylab.set_cmap("gray")
    pylab.title("min={0}, max={1}".format(nd.min(), nd.max()))
    pylab.imshow(nd.transpose())

    pylab.subplot(222)
    pylab.imshow(numpy.asarray(video[frame]))

#    box = prior.boxfit(frame)
#    if box:
#        pylab.subplot(223)
#        im = visualize.highlight_box(box, video[frame])
#        print box
#        pylab.imshow(numpy.asarray(im))

    pylab.savefig("tmp/{0}{1}.png".format(category, frame))
    pylab.clf()
