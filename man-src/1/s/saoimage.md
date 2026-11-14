---
title: "saoimage(1)"
name: "saoimage"
section: "1"
letter: "s"
url: "/docs/linux/man/1-saoimage/"
description: "SAOimage 1.23 – X11 window based, interactive, color or halftone image display program for astronomical images"
---

<h2>NAME</h2>
<p> SAOimage 1.23 &#8211; X11 window based, interactive, color or halftone image display program for astronomical images</p>
<h2>SYNOPSIS</h2>
<p> <code>saoimage</code> [ <code>-display </code><i>nodename:0.0 </i>] [ <code>-geometry | -gd </code><i>geometry </i>]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <code>-pros | +/-imtool | -fits | -dfits | -oif </code>]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <code>-u1 | -u2 | -i2 | -i4 | -r4 | -r8 [ </code><i>width height </i>] ]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <code>-byteswap </code>] [ <code>-skip </code><i>bytes </i>]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <code>-upperleft | -lowerleft </code>] [ <code>-one | -zero </code>] [ <code>-rotate </code><i>code </i>]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <code>-linear </code>| <code>-wrap </code>[ <i>wraps </i>] | <code>-log </code>[ <i>exponent </i>] | <code>-sqrt </code>[ <i>power </i>] | <code>-histeq </code>]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <code>-min </code><i>val </i>] [ <code>-max </code><i>val </i>] [ <code>-rmin </code><i>val </i>] [ <code>-rmax </code><i>val </i>] [ <code>-scalebias </code><i>scale bias </i>]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <code>-palette </code><i>val </i>] [ <code>-red | -green | -blue </code>]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <code>-vertgraph | -horizgraph </code>]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <code>+/-coord </code>] [ <code>+/-magnifier </code>] [ <code>-mag </code><i>val </i>]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <code>-panboxav | -panboxsum | -panboxsample | -panboxmax </code>]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <code>-idev </code><i>pipename </i>] [ <code>-odev </code><i>pipename </i>] [ <code>-fbconfig </code><i>filename </i>]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <code>+/-verbose </code>] [ <code>-quiet </code>] [ <code>-lprbuttons </code>] [ <code>-mtf </code>] [ <code>-bordercolor </code><i>color </i>] [ <code>-lfrac </code><i>histogram fraction </i>] [ <code>-wcscom </code><i>WCS command </i>] [ <code>-gal | -fk4 | -fk5 </code>] [ <code>-zf </code><i>zoom factor</i>]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <i>filename</i> | <code>-name </code><i>filename </i>]</p>
<h2>DESCRIPTION</h2>
<p> <i>SAOimage</i> is a utility for displaying astronomical images which runs under the X11 window environment. Image files can be read directly, or image data may be passed through a named pipe (Unix) or a mailbox (VMS) from IRAF display tasks. <i>SAOimage</i> provides a large selection of options for zooming, panning, scaling, coloring, pixel readback, display blinking, and region specification. User interactions are generally performed with the mouse. </p>
<p> The <i>SAOimage</i> desktop includes, a main image display window, a button menu panel, a display magnifier, a pan and zoom reference image, and a color bar. A color table graph window can be brought up by clicking on the color bar.</p>
<h2>WORLD COORDINATE SYSTEMS</h2>
<p> <code>saoimage</code> tracks world coordinate systems as well as pixel coordinates within the image, if WCS information is present. Several single character keyboard commands have been added. <code>c</code> prints the world coordinate (RA and Dec as hh:mm:ss.sss dd:mm:ss.ss and Lat Long as dd.ddddd dd.ddddd) and image pixel coordinate, along with the value of that pixel to standard output. <code>w</code> executes the command set by <code>-wcscom</code>, substituting that same world coordinate string for %s. <code>b</code> prints the world coordinate RA and Dec in the FK4/B1950 system. <code>j</code> prints the world coordinate RA and Dec in the FK5/J2000 system. <code>g</code> prints the world coordinates as galactic longitude and latitude. <code>e</code> prints the world coordinates as ecliptic longitude and latitude. <code>i</code> prints the world coordinates as the image header defines them. <code>h</code> toggles between degrees and sexigesimal units for RA and Dec.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-blue</code></p>
<dd> Set the color of all graphics to be blue. Some inexpensive systems use a monochrome monitor connected to one of the three color outputs on the computer. That color must be specified to make the graphics visible.</p>
<dt><code>-bordercolor </code><i>colorname</i></p>
<dd> Specify the color of all subwindow borders. The color name must be a recognized X color (there are many). This is a style issue. <code>-bc</code> may be used instead of <code>-bordercolor</code>.</p>
<dt><code>-byteswap</code></p>
<dd> Switch the bytes order between big-endian and little-endian order. This may be needed where data has been copied from another machine or if there is some confusion about the FITS file format. This switch toggles the previous setting. <code>-bswap</code> may be used instead of <code>-byteswap</code>.</p>
<dt><code>+/-coord</code></p>
<dd> Set the coordinate tracking state initially on or off. In coordinate tracking, the coordinates of the mouse and value of the pixel under it are printed in the upper-left text area, above the main display window. <code>+/-ct</code> can be used instead of <code>+/-coord</code>.</p>
<dt><code>-display </code><i>nodename:0.0</i></p>
<dd> Specify the name of the X display server. This makes it possible to run the <i>SAOimage</i> program on a machine other than the one connected to your display screen, with no difference in appearance or use. By default, <i>SAOimage</i> gets the server name from the <code>DISPLAY</code> environment variable. See the <i>xhost</i> manual page for more details. The display server cannot be changed once <i>SAOimage</i> is running. <code>-display</code> may be abbreviated <code>-d</code>.</p>
<dt><code>-dfits</code></p>
<dd> Image file is a FITS file (see <code>-fits</code>), but in unexpected byteswapped order. The FITS standard is not swapped, but some naive VAX applications may swap it (see <code>-bswap</code>).</p>
<dt><code>-fbconfig </code><i>filename</i></p>
<dd> Specify an alternate frame buffer configuration file for use with IRAF. By default, the file installed with <i>SAOimage</i> (/usr/local/lib/imtoolrc) is used.</p>
<dt><code>-fits</code></p>
<dd> Image file is a FITS file. If the image filename ends in <i>.fits</i>, this switch is not necessary. Only T=SIMPLE array types are supported. The header BITPIX card must be 8 (unsigned byte), 16 (signed short), 32 (signed int), -32 (float), -64 (double), or -16 (unsigned short). (The last two are not recognized standards). IEEE floats are not converted if that is not the machine format.</p>
<dt><code>-fk4</code></p>
<dd> If WCS information is available in the image header, track the cursor in FK4/B1950 right ascension and declination as well as pixel coordinates. These coordinates, followed by <i>B1950</i> will be fed to an external program if the <code>w</code> command is used.</p>
<dt><code>-fk5</code></p>
<dd> If WCS information is available in the image header, track the cursor in FK5/J2000 right ascension and declination as well as pixel coordinates. These coordinates, followed by <i>J2000</i> will be fed to an external program if the <code>w</code> command is used.</p>
<dt><code>-gal</code></p>
<dd> If WCS information is available in the image header, track the cursor in galactic longitude and latitude as well as pixel coordinates. These coordinates, followed by <i>galactic</i> will be fed to an external program if the <code>w</code> command is used.</p>
<dt><code>-gd </code><i>geometry</i></p>
<dd> Specify the size of the image display subwindow and/or the screen position of <i>SAOimage</i>. The format is a standard X geometry statement. This switch works like <code>-geometry</code>, except that width and height (if given) are applied to the display subwindow. The overall <i>SAOimage</i> window is sized accordingly.</p>
<dt><code>-geometry </code><i>geometry</i></p>
<dd> Specify the size and/or the screen position of <i>SAOimage</i>. The format is a standard X geometry statement. Both size and position may be specified, or only the size or the position. Width and height refer to the dimensions of <i>SAOimage</i>&#8216;s desktop window (see <code>-gd</code> for sizing just the image display window). <i>+x</i> and <i>+y</i> refer to the upper left corner in screen coordinates. <i>-x</i> positions the right edge from the right edge of the screen. <i>-y</i> would positions the lower edge from the bottom of the screen. Width and height below a minimum size are defaulted to the minimum. Specifying the default minimum size (<code>-geometry 0x0</code>) also triggers <i>SAOimage</i> to use smaller dimensions for its internal windows. Once <i>SAOimage</i> is running, use the window manager&#8217;s normal size and move mechanisms to make adjustments to <i>SAOimage</i>&#8216;s main window. <code>-geometry</code> may be abbreviated <code>-g</code>.</p>
<dt><code>-green</code></p>
<dd> Set the color of all graphics to be green. See <code>-blue</code>.</p>
<dt><code>-histeq</code> may be abbreviated <code>-hi</code>.</p>
<dd> Set the scaling mode for histogram equalization.</p>
<dt><code>-horizgraph</code></p>
<dd> Use a horizontal auxiliary color graph window, with a color bar along the bottom. See <code>-vertgraph</code>. <code>-hg</code> can be used as a shorthand for <code>-horizgraph</code>.</p>
<dt><code>-i2 </code><i>width height</i></p>
<dd> Image file is a signed short integer array file of the given dimensions. If the file is square and has no added padding, the dimensions are not necessary. <code>-shortarray </code><i>width height</i> has the same function.</p>
<dt><code>-i4 </code><i>width height</i></p>
<dd> Image file is a signed long integer array file of the given dimensions. If the file is square and has no added padding, the dimensions are not necessary. <code>-longarray </code><i>width height</i> has the same function.</p>
<dt><code>-idev </code><i>pipename</i></p>
<dd> Specify the name of the named pipe used for listening. The default is /dev/imt1o, which is the default used by IRAF. See <code>-odev</code>.</p>
<dt><code>+/-imtool</code></p>
<dd> Open/close the named input pipe connection and wait for input from IRAF. When open, <i>SAOimage</i> emulates IRAF&#8217;s <i>imtool</i>. IRAF&#8217;s image loading and cursor read-back functions are supported. Unlike <i>imtool</i>, <i>SAOimage</i> has only one frame buffer; IRAF&#8217;s frame buffer numbers are ignored. Listening on the pipe is possible even while reading image files directly. The connection may be opened, closed, or re-opened at any time. When supported, the default mode is commonly to start with the IRAF connection open. See <code>-idev</code>, <code>-odev</code>, and <code>-pros</code>.</p>
<dt><code>-lfrac </code>[<i>fraction of histogram numerical peak</i>]</p>
<dd> Set the linear scaling limits to the values where the pixel value distribution is at a given fraction of its peak</p>
<dt><code>-linear</code></p>
<dd> Set the scaling mode to linear.</p>
<dt><code>-log </code>[<i>exponent for exponential curve</i>]</p>
<dd> Set the scaling mode to log (exponential), and set the exponent for the curve function e sup n if given.</p>
<dt><code>-lowerleft</code></p>
<dd> First pixel in file represents the lower left of the image, assuming the lines of input run left to right on the screen. This is the IRAF standard and the <i>SAOimage</i> default. See <code>-rotate</code>, <code>-upperleft</code>, and <code>-zero</code>. <code>-lowerleft</code> may be abbreviated <code>-ll</code>.</p>
<dt><code>-lprbuttons</code></p>
<dd> Include the button menu in the hardcopy image (only on color workstations). The default on color workstations includes the area above the button panel, but excludes the buttons.</p>
<dt><code>-mag </code><i>magnification</i></p>
<dd> Set the magnification factor of the magnifier. This factor relates the magnifier to the magnification of the display window. The default is 4; the magnifier magnifies the image to 4 times the magnification of the main display window (but never less than zoom 1 of the original data).</p>
<dt><code>+/-magnifier</code></p>
<dd> Set the magnifier tracking state initially on or off. With magnifier tracking, the magnifier window is continuously updated to show a magnification of the image the image under the mouse. <code>+/-mt</code> can be used instead of <code>+/-magnifier</code>.</p>
<dt><code>-max </code>[<i>max val</i>]</p>
<dd> Set the maximum for the image value range used to compute scaling. The default is to take the maximum from the image shown in the display window. <code>-max</code> with no value resets the default. If the maximum value in the displayed image is lower than the given maximum, the image&#8217;s maximum vale is used for the scaling range.</p>
<dt><code>-min </code>[<i>min val</i>]</p>
<dd> Set the minimum for the image value range used to compute scaling. The default is to take the minimum from the image shown in the display window. <code>-min</code> with no value resets the default. If the minimum value in the displayed image is higher than the given minimum, the image&#8217;s minimum vale is used for the scaling range.</p>
<dt><code>-mtf</code></p>
<dd> Give the button panel a chiseled look popularized by HP&#8217;s widget set. This appearance may contrast less with other applications being used at the same time.</p>
<dt><code>-name </code><i>filename</i></p>
<dd> This switch is only needed if the filename starts with a number or might otherwise be recognized as a switch.</p>
<dt><code>-odev </code><i>pipename</i></p>
<dd> Specify the name of the named pipe used for sending feedback. The default is /dev/imt1i, which is the default used by IRAF. See <code>-idev</code>.</p>
<dt><code>-oif</code></p>
<dd> Image file is an IRAF image header file in OIF format. If the image filename ends in <i>.imh</i>, this switch is not necessary. IRAF STF and QPOE formats are not supported. Complex data cannot be handled. The data must have at least 2 dimensions. Only the first plane of multidimensional images is read. The data file is read directly by <i>SAOimage</i> (see <code>-imtool</code> and <code>-pros</code>).</p>
<dt><code>-one</code></p>
<dd> The file coordinate of the first pixel is (1,1). The real coordinates of the center of the first pixel are (1.0,1.0). This is the IRAF standard and the default for <i>SAOimage</i>. The second pixel is (2,1). See <code>-zero</code>.</p>
<dt><code>-palette </code><i>number</i></p>
<dd> Specify the number of read/write color cells to reserve. On color workstations, <i>SAOimage</i> reserves color cells in the default colormap for its own use. <i>SAOimage</i> reserves as many color cells as it can get, up to the number given (the default is 200). If the number given is negative, <i>SAOimage</i> comes up in overlay mode, using 1/2 + 2 of the color cells for overlays and graphics. In verbose mode (see <code>-verbose</code>), <i>SAOimage</i> tells you how many cells it is able to use for display colors. This number can be re-entered at run-time, unless <code>-palette 1</code> is given, in which case <i>SAOimage</i> stays in halftone mode. <code>-p</code> is an acceptable shorthand for <code>-palette</code>.</p>
<dt><code>-panboxav | -panboxsum | -panboxsamp | -panboxmax</code></p>
<dd> These switches select the kind of image reduction used to fit a picture of the entire image into the pan window. Each pixel is computed from a block of image pixels by averaging, summing, sampling, or taking the maximum. The default is to show the maximum from each block. When zooming in the main display involves reduction, subsampling is always used.</p>
<dt><code>-pros</code></p>
<dd> Virtually identical to the <code>+imtool</code> switch. The difference occurs when the user writes the saved regions to a disk file. <i>imtool</i> emulation includes writing only an IRAF list file giving center coordinates only. With <code>-pros</code>, <i>SAOimage</i>&#8216;s normal region descriptor file will be written in place of the simpler list file. One may switch between this mode and <code>+imtool</code>, or close the IRAF connection with <code>-imtool</code>.</p>
<dt><code>-quiet</code></p>
<dd> Disable verbose mode;<code>-q</code> may also be used. See <code>-verbose</code>.</p>
<dt><code>-r4 </code><i>width height</i></p>
<dd> Image file is a real*4 array file of the given dimensions. If the file is square and has no added padding, the dimensions are not necessary. <code>-floatarray </code><i>width height</i> has the same function.</p>
<dt><code>-r8 </code><i>width height</i></p>
<dd> Image file is a real*8 array file of the given dimensions. If the file is square and has no added padding, the dimensions are not necessary. <code>-doublearray </code><i>width height</i> has the same function.</p>
<dt><code>-red</code></p>
<dd> Set the color of all graphics to be red. See <code>-blue</code>.</p>
<dt><code>-rmax </code>[<i>max val</i>]</p>
<dd> Set maximum value for reading from the image file. This value is used as the maximum value when images are pre-scaled to fit the 16 bit (signed short) working buffer.</p>
<dt><code>-rmin </code>[<i>min val</i>]</p>
<dd> Set minimum value for reading from the image file. This value is used as the minimum value when images are pre-scaled to fit the 16 bit (signed short) working buffer.</p>
<dt><code>-rotate </code><i>1,2,or 3</i></p>
<dd> Rotate the image 90, 180, or 270 degrees (respectively) before displaying it. Rotation is applied after conversion to a lower left coordinate system (<code>-ll</code>) if such conversion is also requested. This is useful for images when the CCD was not mounted North-up. <code>-rot</code> can be used as a shorthand for <code>-rotate</code>.</p>
<dt><code>-scalebias </code><i>scale bias</i></p>
<dd> The data in the image file should be scaled and biased to get the true image value (TrueValue = (scale * FileValue) + bias). This cannot be used with the <code>-fits</code> image type (scale and bias are in the FITS header), nor with <code>-imtool</code> or <code>-pros</code> (they are passed by IRAF). <code>-sb</code> is a shorthand for <code>-scalebias</code>.</p>
<dt><code>-skip </code><i>bytes</i></p>
<dd> Skip over the given number of bytes at the head of the file before reading<tt>&nbsp;<wbr></tt>data. This is used to skip header information or the first<br />
 image if two images are stored in one file. <code>-header</code> and <code>-sk</code> are aliases for <code>-skip</code>.</p>
<dt><code>-sqrt </code>[<i>inverse of exponent for geometric curve</i>]</p>
<dd> Set the scaling function to square root (geometric), and set the inverse of the exponent for the x sup {1/n} curve, if given.</p>
<dt><code>-u1 </code><i>width height</i></p>
<dd> Image file is an unsigned byte array file of the given dimensions. If the file is square and has no added padding, the dimensions are not necessary. <code>-chararray </code><i>width height</i> has the same function.</p>
<dt><code>-u2 </code><i>width height</i></p>
<dd> Image file is a unsigned short integer array file of the given dimensions. If the file is square and has no added padding, the dimensions are not necessary. <code>-ushortarray </code><i>width height</i> has the same function.</p>
<dt><code>-upperleft</code></p>
<dd> First pixel in file represents the upper left of the image, assuming the lines of input run left to right on the screen (see <code>-rotate</code> and <code>-lowerleft</code>). This switch does not override IRAF WCS image coordinates. <code>-upperleft</code> may be abbreviated <code>-ul</code>.</p>
<dt><code>+/-verbose</code></p>
<dd> Set <i>verbose</i> mode on or off. In verbose mode, informative statements are printed to the terminal window when various actions are taken. The default mode is to be verbose. <code>+/-v</code> can be used instead of <code>+/-verbose</code>.</p>
<dt><code>-vertgraph</code></p>
<dd> Use a vertical auxiliary color graph window, with a color bar along the left side. See <code>-horizgraph</code>. <code>-vg</code> can be used as a shorthand for <code>-vertgraph</code>.</p>
<dt><code>-wcscom </code>[<i>format for command to be executed</i>]</p>
<dd> Set the command to be executed when the <code>w</code> key is struck, where the world coordinates are substituted for %s in the string. Underscores should be used instead of spaces.</p>
<dt><code>-wrap </code>[<i>number of wraps within scaling range</i>]</p>
<dd> Set the scaling mode to wrapped linear, and set the number of wraps for this mode, if given.</p>
<dt><code>-zero</code></p>
<dd> The file coordinate of the first pixel is (0,0). The real coordinates of the center of the first pixel are (0.5,0.5) which makes the very edge (0,0). This is the standard coordinate system for image displays, but not the default for <i>SAOimage</i>. The second pixel is indexed (1,0). See <code>-one</code>.</p>
<dt><code>-zf </code><i>zoom factor</i></p>
<dd> Zoom the initial display of the image by <i>zoom factor</i>. A number larger than one makes the image larger by that factor, using that many display pixels per image pixel. A fractional <i>zoom factor</i> displays that the image with that fraction of a display pixel per image pixel.</dl>
<h2>USAGE</h2>
<p> Refer to the <i>SAOimage User Manual</i> for detailed descriptions of all functions. </p>
<p> Most control actions take place within the context of a mode. Modes are selected by clicking on menu buttons in the top row of the button panel. Each menu mode brings up its own submenu buttons (the lower row in the button panel) for mode specific selections. Actions and submodes are selected by clicking on buttons in the submenu row of the menu panel. </p>
<p> The mouse controls specific functions in both the main display window and the pan/zoom window. In the main display window, the function of the mouse is determined by the mode and submode selections from the button menu. The function can also be recognized by the appearance of the mouse pointer icon. </p>
<p> The button interface is designed to be user friendly. The user is encouraged to try any and all buttons to become familiar with their functions. To exit, use the <i>QUIT</i> button in the <i>etc</i> submenu (click on <i>etc</i>, then click on <i>QUIT</i>).</p>
<h3>Reading images</h3>
<p> To read an image directly from a file, give its name anywhere on the command line. The <code>-name</code> switch is needed only when the image file name could be mistaken for a number or switch. <i>SAOimage</i> recognizes the <i>.fits</i> and <i>.imh</i> filename suffixes as belonging to FITS and IRAF OIF files. All other file types must be specified by an appropriate file type switch. </p>
<p> Raw array file types must be specified by an array data type switch (<code>-u1</code>, <code>-u2</code>, <code>-i2</code>, <code>-i4</code>, <code>-r4</code>, <code>-r8</code>) followed by width and height dimensions. To skip over a file header, use the <code>-sk</code> switch followed by the number of bytes. This can also be used to skip over entire images, if more than one are stored in the same file.</p>
<h3>Use with IRAF</h3>
<p> To emulate <i>imtool</i> and communicate with IRAF tasks, use either the <code>-imtool</code> or <code>-pros</code> switch. The two switches indicate which file format to use in recording saved cursors or regions. With <code>-imtool</code>, an IRAF list file containing only center coordinates is used (like that of <i>imtool</i>). With <code>-pros</code>, a file containing a full description of the saved cursors and their dimensions is used. The latter file can be read by tasks in the IRAF PROS spatial package for making image masks and performing image analyses. Both file types are ASCII and can be read and edited by the user. In either case, the file is not actually written until the user clicks on the <i>write</i> button in the <i>region</i> submenu. Both file types can be read back to reproduce the saved cursors.</p>
<h3>New command input</h3>
<p> A new command line can be entered at any time, by selecting the <i>new</i> button in the <i>etc</i> submenu or striking the <i>N</i> key on the keyboard. This allows the user to read in new images, change in and out of <code>-imtool</code> or <code>pros</code> mode, set new scaling parameters, or change the number of reserved display color cells. Most command line switches (except <code>-d</code>, <code>-g</code>, <code>-gd</code>, <code>-red</code>, <code>-green</code>, <code>-blue</code>, and <code>-vertgraph</code>) will be accepted at any time. </p>
<p> When a new command line is requested, the previous command line is presented in an emacs-like popup editor for editing. Ctrl-N clears the previous line. Striking the RETURN key enters the line in the popup window as the new command. Ctrl-C returns with no action taken.</p>
<h3>Using the mouse</h3>
<p> Most mouse interactions are based on mouse dragging (holding a button down while moving the mouse). The user should try clicking and/or dragging the mouse in each subwindow to become familiar with its functions. Modes selected in the button panel determine the response to the mouse buttons in the main display window. </p>
<p> In <code>Scale</code> mode, the mouse buttons control blinking of displays (saved by clicking with the same mouse button in the <i>blink</i> submenu button). </p>
<p> In <code>Color</code> mode, mouse dragging stretches and shifts the color map as per the <i>contrast/bias, threshold/saturation,</i> and <i>gamma</i> submenu selections. </p>
<p> In the <code>color graph window,</code> color table vertexes may be added or moved by clicking or dragging with the LEFT (red), MIDDLE (green), or RIGHT (blue) mouse buttons. The graph will update continuously only if <i>tracking</i> is turned on. </p>
<p> In <code>Cursor</code> mode, the mouse controls the size and locations of cursors. The rule is: LEFT button for position, MIDDLE button for size, and RIGHT button for angle or deletion (depending on the cursor).</p>
<h3>Cursors</h3>
<p> For <i>box</i> and <i>ellipse</i> cursors, MIDDLE button sizing is restricted depending on whether dragging started on a side or near a corner. </p>
<p> With the <i>point</i> cursor, the LEFT and MIDDLE buttons save the current mouse pointer position with a + or &#8211; indication, while the RIGHT button deletes saved points. </p>
<p> For the <i>polygon</i> cursor, the MIDDLE button adds or moves a single vertex, while the RIGHT button will delete vertexes. The LEFT button moves the whole polygon. </p>
<p> When <i>annuli</i> is set for a <i>box, circle,</i> or <i>ellipse</i> cursor, the MIDDLE button adds or resizes an annulus, while the RIGHT button deletes annuli. </p>
<p> For manipulating cursors, the <i>ovlay</i> selection in the <i>Color</i> submenu, enables the cursor to track smoothly as an overlay graphic. The <i>region</i> submenu button brings up another submenu with selections to display, review, and edit the saved regions, and read from or write to disk files.</p>
<h3>Pan and zoom</h3>
<p> In <i>Pan</i> mode, and in the pan window (regardless of mode), the LEFT button selects the center of the image, while the MIDDLE button selects the edge of the display, zoomed from the given center. When either function is dragged, the rectangle in the pan window shows the area that would appear in the display when the button is released.</p>
<h3>Keys</h3>
<p> In the cursor mode, the <i>S</i> and <i>E</i> keys, save the current cursor in a region list, while the <i>D</i> and DELETE keys can be used to forget a region. At any time, with the pointer in the display or pan windows, the <i>T</i> key prints a table of pixel values at the pointer position to <i>stdout</i>. The 4 arrow keys can be used for fine movement of the pointer in any window. The SHIFT and SHIFT LOCK keys will reverse the magnifier window, color graph window and coordinate tracking status. The <i>N</i> key summons the pop-up editor for new command input. The <i>A</i> key raises and redraws all of <i>SAOimage</i>&#8216;s windows.</p>
<h2>BUGS</h2>
<p> <i>SAOimage</i> does not allocate its own colormap and thus fails with static color (i.e. NeWS) window managers. X resource settings of a user&#8217;s default preferences are not read.</p>
<h2>ONLINE HELP</h2>
<p> Additional information about <i>SAOimage</i> is available on the World-Wide Web at <a rel="nofollow" href="http://tdc-www.harvard.edu/software/saoimage.html">http://tdc-www.harvard.edu/software/saoimage.html</a> </p>
<h2>Index</h2>
