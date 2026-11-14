---
title: "fvwmrearrange(1)"
name: "fvwmrearrange"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwmrearrange/"
---

FvwmRearrange - rearrange fvwm windows 

<h2>Synopsis</h2>FvwmRearrange is spawned by fvwm, so no command line invocation will work. 

<h2>Description</h2>This module can be called to tile or cascade windows. 

 When tiling the module attempts to tile windows on the current screen subject to certain constraints. Horizontal or vertical tiling is performed so that each window does not overlap another, and by default each window is resized to its nearest resize increment (note sometimes some space might appear between tiled windows -- this is why). 

 When cascading the module attempts to cascade windows on the current screen subject to certain constraints. Layering is performed so consecutive windows will have their window titles visible underneath the previous. 

<h2>Invocation</h2>FvwmRearrange is best invoked from a menu, pop up or button. There are a number of command line options which can be used to constrain the layering, these are described below. As an example case, one could call FvwmRearrange with the following arguments: 

 <pre>FvwmRearrange -tile -h 10 10 90 90</pre>or 

 <pre>FvwmRearrange -cascade -resize 10 2 80 70</pre>The first invocation will horizontally tile windows with a bounding box which starts at 10 by 10 percent into and down the screen and ends at 90 by 90 percent into and down the screen. 

 The second invocation will cascade windows starting 10 by 2 percent into and down the screen. Windows will be constrained to 80 by 70 percent of the screen dimensions. Since the <i>resize</i> is also specified, windows will be resized to the given constrained width and height. 

 FvwmRearrange can be called as FvwmTile or FvwmCascade. This is equivalent to providing the -tile or -cascade option. This form is obsolete and supplied for backwards compatibility only. 

 Command-line arguments passed to FvwmRearrange are described here.
<dl><dt>-a
<dd>Causes <i>all</i> window types to be affected, even ones with the WindowListSkip style.
<dt>-animate
<dd>Attempt to do an animated move, this is ignored if <i>-resize</i> or <i>-maximize</i> are used.
<dt>-cascade
<dd>Cascade windows. This argument must be the first on the command line. This is the default.
<dt>-desk
<dd>Causes all windows on the desk to be cascaded/tiled instead of the current screen only.
<dt>-flatx
<dd>Inhibits border width increment. Only used when cascading.
<dt>-flaty
<dd>Inhibits border height increment. Only used when cascading.
<dt>-h
<dd>Tiles horizontally (default is to tile vertically). Used for tiling only.
<dt>-incx <i>arg</i>
<dd>Specifies a horizontal increment which is successively added to cascaded windows. <i>arg</i> is a percentage of screen width, or pixel value if a <i>p</i> is suffixed. Default is zero. Used only for cascading.
<dt>-incy <i>arg</i>
<dd>Specifies a vertical increment which is successively added to cascaded windows. <i>arg</i> is a percentage of screen height, or pixel value if a <i>p</i> is suffixed. Default is zero. Used only for cascading. 

<dt>-m
<dd>Causes maximized windows to also be affected (implied by -a).
<dt>-maximize
<dd>When moving/resizing a window, put it also into maximized state.
<dt>-mn <i>arg</i>
<dd>Tiles up to <i>arg</i> windows in tile direction. If more windows exist, a new direction row or column is created (in effect, a matrix is created). Used only when tiling windows.
<dt>-noanimate
<dd>Do not attempt to do an animated move.
<dt>-nomaximize
<dd>Do not put windows into maximized state.
<dt>-noraise
<dd>Inhibits window raising, leaving the depth ordering intact.
<dt>-noresize
<dd>Inhibits window resizing, leaving window sizes intact. This is the default when cascading windows.
<dt>-nostretch
<dd>If tiling: inhibits window growth to fit tile. Windows are shrunk to fit the tile but not expanded. 

 If cascading: inhibits window expansion when using the -resize option. Windows will only shrink to fit the maximal width and height (if given).
<dt>-r
<dd>Reverses the window sequence.
<dt>-resize
<dd>Forces all windows to resize to the constrained width and height (if given). This is the default when tiling windows.
<dt>-s
<dd>Causes sticky windows to also be affected (implied by -a).
<dt>-sp
<dd>Causes windows sticky across pages to also be affected (implied by -a).
<dt>-sd
<dd>Causes windows sticky across desks to also be affected (implied by -a).
<dt>-t
<dd>Causes transient windows to also be affected (implied by -a).
<dt>-tile
<dd>Tile windows. This argument must be the first on the command line.
<dt>-u
<dd>Causes untitled windows to also be affected (implied by -a).
<dt>-ewmhiwa
<dd>When rearranging windows, make the calculation ignore the working area, such as EwmhBaseStruts; by default, FvwmRearrange will honour the working area. 

 Up to four numbers can be placed on the command line that are not switches. The first pair specify an x and y offset to start the first window (default is 0, 0). The meaning of the second pair depends on operation mode: 

 When tiling windows it specifies an absolute coordinate reference denoting the lower right bounding box for tiling. 

 When cascading it specifies a maximal width and height for the layered windows. If an affected window exceeds either this width or height, it is resized to the maximal width or height. 

 If any number is suffixed with the letter p, then it is taken to be a pixel value, otherwise it is interpreted as a screen percentage. Specifying zero for any parameter is equivalent to not specifying it. 

</dl><h2>Bugs</h2>It is probably not a good idea to delete windows while windows are being rearranged. 

<h2>Authors</h2>Andrew Veliath (original FvwmTile and FvwmCascade modules) Dominik Vogt (merged FvwmTile and FvwmCascade to FvwmRearrange)
