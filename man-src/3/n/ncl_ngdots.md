---
title: "ncl_ngdots(3)"
name: "ncl_ngdots"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ngdots/"
---

NGDOTS - Draws filled circular dots at coordinate positions (X(I),Y(I),I=1,NUM) at size SIZE with color given by the color index ICOLOR. 

<h2>Synopsis</h2>CALL NGDOTS(X,Y,NUM,SIZE,ICOLOR)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_ngdots(float *x, float *y, int num, float size, 
 int icolor)
<h2>Description</h2><dl COMPACT><dt>X
<dd>(an input array of type REAL) defining the X world coordinates where a sequence of circular filled dots is to be drawn.
<dt>Y
<dd>(an input array of type REAL) defining the Y world coordinates where a sequence of circular filled dots is to be drawn.
<dt>NUM
<dd>(an input parameter of type INTEGER) the value of which is the number of dots to be drawn.
<dt>SIZE
<dd>(an input parameter of type REAL) the value of which is the size, in world coordinate Y-axis units, of the diameter of each dot to be drawn.
<dt>ICOLOR
<dd>(an input parameter of type INTEGER) the value of which is the GKS color index specifying what color the dots will be.</dl><h2>C-Binding Description</h2>The C binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>The coordinates must be world coordinates and not user coordinates. NGDOTS does not respect the log scaling or axis reversal options of the SET call and will report a warning if these are not set to their default values. 

 The dots are scaled appropriately so that they will be circular when the normalization transformation does not preserve aspect ratio. 

 The algorithm is to construct a single circle and then translate it to the various coordinate positions. The original circle is computed by using trig functions to get points in the first octant, and then using symmetries to get the rest of the points on the circle. 

 The number of points used for the circle is adjusted depending on the relative size of the circle. The maximum number of points is 512 and the minimum is 8.
<h2>Examples</h2>Assuming that normalization transformation 0 is in effect and that color index 2 has been defined as red in a call to GSCR, then <pre> CALL NGDOTS(.5,.25,1,.1,2)</pre>would draw a single red dot at world coordinate position (.5,.25) with a diameter of .1 . 

 Use the ncargex command to see the following relevant example: fngngdts.
<h2>Access</h2>To use NGDOTS or c_ngdots, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>Warning messages will be issued if one calls NGDOTS after having called SET with any final argument other than &quot;1&quot;.
<h2>See Also</h2><pre><code>Online:
gpm(3NCARG),
point(3NCARG),
points(3NCARG),
set(3NCARG),
ncarg_cbind(3NCARG)</code></pre> Online URL: <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/gks/gkshome.html">http://ngwww.ucar.edu/ngdoc/ng/gks/gkshome.html</a> Hardcopy: NCAR Graphics Fundamentals, UNIX Version; &quot;The Use of X/Y Coordinates in NCAR Graphics&quot; SCD User Document
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
