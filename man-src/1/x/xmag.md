---
title: "xmag(1)"
name: "xmag"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xmag/"
description: "xmag – magnify parts of the screen"
---

<h2 class="name">NAME</h2>
<p> xmag &#8211; magnify parts of the screen </p>
<h2>SYNOPSIS</h2>
<p> <code>xmag</code> [ <code>-mag</code> <i>magfactor</i> ] [ <code>-source</code> <i>geom</i> ] [ <i>-toolkitoption</i> &#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> The <i>xmag</i> program allows you to magnify portions of an X screen. If no explicit region is specified, a square with the pointer in the upper left corner is displayed indicating the area to be enlarged. The area can be dragged out to the desired size by pressing Button 2. Once a region has been selected, a window is popped up showing a blown up version of the region in which each pixel in the source image is represented by a small square of the same color. Pressing Button1 in the enlargement window shows the position and RGB value of the pixel under the pointer until the button is released. Typing &#8220;Q&#8221; or &#8220;^C&#8221; in the enlargement window exits the program. The application has 5 buttons across its top. <i>Close</i> deletes this particular magnification instance. <i>Replace</i> brings up the rubber band selector again to select another region for this magnification instance. <i>New</i> brings up the rubber band selector to create a new magnification instance. <i>Select</i> puts the magnification image into the primary selection. <i>Paste</i> copies the primary selection buffer into <i>xmag</i>. Note that you can cut and paste between <i>xmag</i> and the <i>bitmap</i> program. Resizing <i>xmag</i> resizes the magnification area. <i>xmag</i> preserves the colormap, visual, and window depth of the source.</p>
<h2>WIDGETS</h2>
<p> <i>xmag</i> uses the X Toolkit and the Athena Widget Set. The magnified image is displayed in the Scale widget. For more information, see the Athena Widget Set documentation. Below is the widget structure of the <i>xmag</i> application. Indentation indicates hierarchical structure. The widget class name is given first, followed by the widget instance name. </p>
<pre>
        Xmag xmag
                RootWindow root
                TopLevelShell xmag
                        Paned pane1
                                Paned pane2
                                        Command close
                                        Command replace
                                        Command new
                                        Command select
                                        Command paste
                                        Label xmag label
                                Paned pane2
                                        Scale scale
                OverrideShell pixShell
                        Label pixLabel
</pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>-source</code><i> geom</i></p>
<dd> This option specifies the size and/or location of the source region on the screen. By default, a 64&#215;64 square is provided for the user to select an area of the screen.</p>
<dt><code>-mag</code><i> integer</i></p>
<dd> This option indicates the magnification to be used. 5 is the default.</dl>
<h2>AUTHORS</h2>
<p> Dave Sternlicht and Davor Matic, MIT X Consortium. </p>
<h2>Index</h2>
