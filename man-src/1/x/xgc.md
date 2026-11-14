---
title: "xgc(1)"
name: "xgc"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xgc/"
description: "xgc – X graphics demo"
---

<h2 class="name">NAME</h2>
<p> xgc &#8211; X graphics demo </p>
<h2>SYNOPSIS</h2>
<p> <code>xgc</code> [-<i>toolkitoption</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The <i>xgc</i> program demonstrates various features of the X graphics primitives. In X, most of the details about the graphics to be generated are stored in a resource called a graphics context (GC). The <code>xgc</code> program provides a user interface for setting various GC components. Pressing the &quot;Run&quot; button causes these results to be displayed in the large drawing window on the right. Timing information is displayed in the window immediately below. </p>
<p> The items in the upper left hand window work as follows: </p>
<p> <i>Function</i> &#8211; specify the logical function with which primitives will drawn. The most usual setting is &quot;set&quot;, i.e. simply to render pixels without regard to what has been drawn before. </p>
<p> <i>LineStyle</i> &#8211; specify whether lines should be drawn solid in foreground, dashed in foreground or alternating foreground and background. </p>
<p> <i>CapStyle</i> &#8211; specify the appearance of the ends of a line. </p>
<p> <i>JoinStyle</i> &#8211; specify the appearance of joints between consecutive lines drawn within a single graphics primitive. </p>
<p> <i>FillStyle</i> &#8211; specify whether lines, text and fill requests are solid, tiled with a pixmap or stippled. </p>
<p> <i>FillRule</i> &#8211; specifies the rule used to fill polygons. The EvenOdd rule means that if areas overlap an odd number of times, they are not drawn. Winding rule means that overlapping areas are always filled, regardless of how many times they overlap. </p>
<p> <i>ArcMode</i> &#8211; specifies the rule for filling of arcs. The boundary of the arc is either a Chord or two radii. </p>
<p> <i>planemask</i> &#8211; specifies which planes of the drawing window are modified. By default, all planes are modified. </p>
<p> <i>dashlist</i> &#8211; specifies a pattern to be used when drawing dashed lines. </p>
<p> <i>Line Width</i> &#8211; specifies the width in pixels of lines to be drawn. Zero means to draw using the server&#8217;s fastest algorithm with a line width of one pixel. </p>
<p> <i>Font</i> &#8211; specifies the font to be used for text primitives. </p>
<p> <i>Foreground</i> and <i>Background</i> &#8211; specify the pixel values to be applied when drawing primitives. The Foreground value is used as the pixel value for set bits in the source in all primitives. The Background value is used as the pixel value for unset bits in the source when using Copy Plane, drawing lines with LineStyle of DoubleDash and filling with FillStyle of OpaqueStippled. </p>
<p> <i>Percentage of Test</i> &#8211; scrollbar permits specifying only a percentage of the test to be run. The number at the left indicates the current setting, which defaults to 100%. </p>
<p> The window labeled &quot;Test&quot; permits choice of one a number of graphics primitive tests, including Points, Segments, Lines, Arcs and Filled Arcs, 8-bit Text and Image Text, Rectangles and Filled Rectangles, Image draws, as well as Copy Plane and Copy Area. </p>
<p> The window to the right of this has buttons which permit record/playback of the primitives rendered.</p>
<h2>OPTIONS</h2>
<p> <i>Xgc</i> accepts all of the standard X Toolkit command line options.</p>
<h2>X DEFAULTS</h2>
<p> This program accepts the usual defaults for toolkit applications.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></p>
<dd> to get the default host and display number.</p>
<dt><code>XENVIRONMENT</code></p>
<dd> to get the name of a resource file that overrides the global resources stored in the RESOURCE_MANAGER property.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7)</p>
<h2>BUGS</h2>
<p> This program isn&#8217;t really finished yet, but it probably never will be, since it only demonstrates the original X11 core protocol rendering operations, which few modern programs use anymore.</p>
<h2>AUTHORS</h2>
<p> Dan Schmidt, MIT </p>
<h2>Index</h2>
