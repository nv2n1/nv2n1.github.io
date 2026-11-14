---
title: "photo(1)"
name: "photo"
section: "1"
letter: "p"
url: "/docs/linux/man/1-photo/"
description: "photo.rectify"
---

<h2>NAME</h2>
<p> <i></i><code>photo.rectify</code></p>
<h2>DESCRIPTION</h2>
<p> <i>photo.rectify</i> rectifies an image by using the image to photo coordinate transformation matrix created by photo.2image and the rectification parameters created by photo.2target. Rectification is the process by which the geometry of an image is made planimetric. This is accomplished by mapping an image from one coordinate system to another. In photo.rectify the parameters computed by photo.2image and photo.2target are used in equations to convert x,y image coordinates to standard map coordinates for each pixel in the image. The result is an image with a standard map coordinate system, compensated for relief distortions and photographic tilt. Upon completion of the program the rectified image is deposited in a previously targeted GRASS LOCATION. </p>
<p>&nbsp;<wbr>You are asked to select the file(s)&nbsp;<wbr>within the imagery group to be rectified: </p>
<p>&nbsp;<wbr>Please select the file(s)&nbsp;<wbr>to rectify by naming an </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gs13.1 in PERMANENT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gs13.orect&#8230; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gs14.1 in PERMANENT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8230;&#8230;&#8230;&#8230;. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>(enter list by any name to get a list of existing raster maps) </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> AFTER COMPLETING ALL ANSWERS, HIT &lt;ESC&gt; TO CONTINUE</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> (OR &lt;Ctrl-C&gt; TO CANCEL)</p>
<p> More than one file may be rectified at a time. Each file should have a unique output file name. </p>
<p> The next prompt asks you to select one of two windows: </p>
<p>Please select one of the following options </p>
<p>1.&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Use the current window in the target location </p>
<p>2.&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Determine the smallest window which covers the image </p>
<p>&gt; </p>
<p> <i>photo.rectify</i> will only rectify that portion of the image that occurs within the chosen window. Only that portion will be relocated in the target database. It is therefore important to check the current window in the target LOCATION if choice number one is selected. </p>
<p> The process may take an hour or more depending on the size of the image, the speed of the computer, the number files, and the size and resolution of the selected window. </p>
<p> The rectified image will be located in the target LOCATION when the program is completed. The original unrectified files are not modified or removed.</p>
<h2>SEE ALSO</h2>
<p> <i> i.ortho.photo<br />
 photo.camera<br />
 photo.2image<br />
 photo.2target<br />
 photo.init </i></p>
<h2>AUTHOR</h2>
<p> Mike Baba, DBA Systems, Inc.<br />
 Updated rectification and elevation map to FP 1/2002 Markus Neteler </p>
<p> <i>Last changed: $Date: 2006-12-15 11:10:21 +0100 (Fri, 15 Dec 2006) $</i> </p>
<h2>Index</h2>
