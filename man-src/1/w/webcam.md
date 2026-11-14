---
title: "webcam(1)"
name: "webcam"
section: "1"
letter: "w"
url: "/docs/linux/man/1-webcam/"
description: "webcam – capture images and upload them to a webserver using ftp"
---

<h2>NAME</h2>
<p> webcam &#8211; capture images and upload them to a webserver using ftp</p>
<h2>SYNOPSIS</h2>
<p> <code>webcam [ config file ]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>webcam</code> captures images from a video4linux device like bttv, annotates them and and uploads them to a webserver using ftp in a endless loop.</p>
<h2>CONFIGURATION</h2>
<p> At startup <code>webcam</code> reads the configuration from the given config file or ~/.webcamrc if none is specified in the command line. </p>
<p> The config file has at least two sections. The &quot;grab&quot; section holds the capture parameters. Any other section describes where the image should be uploaded. Older versions used &quot;ftp&quot; as name for that section. Recently the webcam utility got support for multiple connections, thus any section name is accepted and you can have more than one ftp section (you have to use another name for each section througth, name them by upload servers for example). </p>
<p> Here is an sample config file (the given values are the defaults): </p>
<pre><code>
[grab] device = / dev / video0 driver = libv4l
                    text = "webcam %Y-%m-%d %H:%M:%S" infofile = filename
                        fg_red = 255 fg_green = 255 fg_blue = 255 width = 320 height = 240 delay = 3 wait = 0 input = composite1
                            norm = pal
                                rotate = 0 top = 0 left = 0 bottom = -1 right = -1 quality = 75 trigger = 0 once = 0
                                    [ftp] host = www
                                        user = webcam
                                            pass = xxxxxx
                                                dir = public_html / images
                                                                        file = webcam.jpeg
                                                                                   tmp = uploading.jpeg
                                                                                             passive = 1 debug = 0 auto = 0 local = 0 ssh = 0
</code></pre>
<p> The annotation <code>text</code> is processed with strftime. Check the <a href="/docs/linux/man/3-strftime/">strftime</a>(3) or <a href="/docs/linux/man/1-date/">date</a>(1) manpage to see how you can format the timestamps. The text can also be read from a extern file (use <code>infofile</code> for that). The default color for the text overlay is white (RGB=255,255,255). Entries in the range of 0 through 255 for <code>fg_red,</code> <code>fg_green,</code> and <code>fg_blue</code> can be used to define a different color. Likewise <code>bg_red,</code> <code>bg_green,</code> and <code>bg_blue</code> can be used to set the background color (which defaults to transparent). </p>
<p> <code>input</code> is the video source (TV/composite/whatever), <code>norm</code> the TV norm. <code>delay</code> is the delay between two images in seconds. <code>wait</code> is the initial delay before the first image is grabbed (some cameras need some time for adapting to lightning, thus don&#8217;t return images with reasonable quality within the first few seconds &#8230;). <code>quality</code> is the JPEG quality for the stored images. </p>
<p> <code>top, bottom, left,</code> and <code>right</code> in the grab section allow cropping the image after it is grabbed. They should satisfy 0&lt;=top&lt;bottom&lt;=height and 0&lt;=left&lt;right&lt;=width. (0,0 is the top, left corner.) If <code>rotate</code> is positive, the output image will be rotated counter-clockwise 90 degrees that number of times (1, 2, or 3). </p>
<p> With <code>trigger</code> set to a non-zero value webcam will upload the image only if the content of the image has changed. It just looks for the maximum difference between the last uploaded and current image and if it is greater than the specified value the image will be uploaded. If <code>once</code> is set to 1 webcam will upload a single frame and quit. </p>
<p> <code>archive</code> can be used to create a (local) archive of the webcam images. Just specify the filename for the files as argument. The filename will be processed with <a href="/docs/linux/man/3-strftime/">strftime</a>(3), so you can use the place the usual time format controls into the string to get unique filenames. Non-existing directories are created if needed. </p>
<p> If <code>debug</code> in the ftp section is set to 1 the complete communication between webcam and the ftp utility is printed to stderr. <code>auto</code> enables autologin via ~/.netrc (starts the ftp utility without the &#8216;-n&#8217; switch, check the <a href="/docs/linux/man/1-ftp/">ftp</a>(1) man page for more info about the ~/.netrc file). If <code>local</code> in the ftp section is non-zero, files will be stored locally (using the <code>dir, tmp,</code> and <code>file</code> parameters) rather than ftped. <code>ssh</code> set to non-zero makes webcam use ssh instead of ftp.</p>
<h2>CORRECTION OF DISTORTION</h2>
<p> contributed by Frederic Helin, the parameters belong into the [grab] section of the config file too.</p>
<dl>
<dt><code>distor = 1</code></p>
<dd> If distor param is set to 1, the correction of distortion works.</p>
<dt><code>distor_k = 700</code></p>
<dd> This is the coefficient of distortion. This algorithm is based on the paper &quot;Correcting Distortion of Image by Image Registration&quot; of Toru Tamaki, Tsuyoshi Yamamura and Noboru Ahnishi. More your lens has an important distortion, more &#8216;distor_k&#8217; must be neared of 0. 700 is the default value. Coefficient k of program is x100 than article.</p>
<dt><code>distor_cx = 192</code></p>
<dd>
<dt><code>distor_cy = 144</code></p>
<dd> Coordinates of the lens optical axis: width/2 and height/2 are the default values. The axis doesn&#8217;t go through the image center. So, you can change its coordinates around the center of image to affine correction.</p>
<dt><code>distor_zoom = 30</code></p>
<dd> Zoom parameter is used to cache the distorted borders of image, if you don&#8217;t like this. Default value is 100.</p>
<dt><code>distor_sensorw = 320</code></p>
<dd>
<dt><code>distor_sensorh = 240</code></p>
<dd> Dimensions of camera sensor. Default values are for 1/4p sensor. This parameters used to have the same k coefficient than article.</dl>
<h2>AUTHOR</h2>
<p> Gerd Knorr &lt;kraxel [at] bytesex.org&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1997-2002 Gerd Knorr<br />
 This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
