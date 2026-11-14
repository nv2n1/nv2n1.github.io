---
title: "oggslideshow(1)"
name: "oggslideshow"
section: "1"
letter: "o"
url: "/docs/linux/man/1-oggslideshow/"
description: "oggSlideshow – creates slideshows from pictures"
---

<p>oggSlideshow &#8211; creates slideshows from pictures</p>
<h2>Synopsis</h2>
<p><code>oggSlideshow [options] picture1 [ picture2 [&#8230;] ] </code></p>
<h2>Description</h2>
<p><code>oggSlideshow </code> creates a theora video from a number of pictures in JPEG- or PNG-format with different visual effects.</p>
<h2>Options</h2>
<dl COMPACT>
<dt>-s</p>
<dd>Sets the size of the video frame. The size is given as <code>&lt;width&gt;x&lt;height&gt;</code> </p>
<p> <i>Example: -s 320&#215;240</i> </p>
<dt>-f</p>
<dd>Sets the frame rate of the video. This is given by the pictures per second. The default frame rate is 24 pictures per second. </p>
<p> <i>Example: -f 16</i> </p>
<dt>-o</p>
<dd>Sets the output file name of the created video. The default name is slideshow.ogv. </p>
<p> <i>Example: -o myShow.ogv</i> </p>
<dt>-l</p>
<dd>Sets the presentation time (length) of one picture. So if your have 10 pictures and specify a length of 10 seconds, then your overall video length is 1:40 (100 seconds). </p>
<p> <i>Example: -l 10</i> </p>
<dt>-d</p>
<dd>Sets the datarate in byte per seconds for the video encoder. This more meant to be a upper threshold. So the file may be smaller than assumed. </p>
<p> <i>Example: -d 1024000</i> </p>
<dt>-t</p>
<dd>Sets the presentation type, as shown above. Actually types are: </p>
<p> <code>kb: </code><br />
&nbsp;<wbr>Ken Burns effect&nbsp;<wbr>(default) </p>
<p> <code>cf:</code><br />
&nbsp;<wbr>Picture crossfade for changeover </p>
<p> <code>p:</code><br />
&nbsp;<wbr>Plain picture presentation </p>
<p> <code>bl: </code><br />
&nbsp;<wbr>Bluring at changeover<br />
&nbsp;<wbr> <i>Example: -t p</i> </p>
<dt>-e</p>
<dd>Enables the reframing. In case a picture does not match the aspect ratio of the video frame, it can be &quot;reframed&quot;, which means black borders are inserted. This option is only usefull with the Ken Burns effect (option -t kb). The pictures are automaticaly &quot;reframed&quot; with the other two slideshow types to match the aspect ratio. </p>
<p> <i>Example: -e</i> </p>
<dt>-r</p>
<dd>Enables the resampling to a certain value. This is really only for experts and may not be available with newer version of oggSlideshow. </p>
<p> To understand this option you need some more internal information: The picture is loaded by the gd lib. So the transformation from png or jpeg to a plain RGBA is done here. The second reason for using gd is the great resizing facilities as pictures are often much bigger than the video frame. OggSlideshow can handle pictures from 0.5 to 2 times of the video frame width and height best, as it uses a linear pixel interpolation. With the resizing feature of gd, oggSlideshow reads pictures with a size &quot;near&quot; to the video output size and can then operate with that picture. This produces a very good quality output, as you can see above. </p>
<p> The value given with this option is the factor the picture is read in in respect of the video frame size. When the video frame size is 320&#215;240 and the resample factor is 1.2 than the picture that is read is resized to 384&#215;288. Specially for the ken burns effect this is important as the sliding is done on a picture bigger than the video frame size.</dl>
<h2>Example</h2>
<p><i>oggSlideshow -l3 -tp -d1024000 -s480x320 -o demo-plain.ogv &lt;picture1.jpg&gt; &lt;picture2.jpg&gt; &#8230;</i> </p>
<h2>Author</h2>
<p>Joern Seger &lt;yorn at gmx dot net&gt;</p>
