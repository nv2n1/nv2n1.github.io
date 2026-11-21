---
title: "gqview(1)"
name: "gqview"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gqview/"
description: "GQview – GTK based multiformat image viewer"
---

<h2>SYNOPSIS</h2>
<p> <code>gqview</code> [<i>options</i>] [<i>path</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>GQview</code> is an interactive GTK based image viewer that supports multiple image formats, zooming, panning, thumbnails and sorting images into collections. </p>
<h2>OPTIONS</h2>
<p> <code></p>
<dl>
<dt>+t,&#8211;with-tools</dt>
<dd> </code> Force the toolbox to be shown.<br />
 <code></dd>
<dt>-t,&#8211;without-tools</dt>
<dd> </code> Force the toolbox to be hidden.<br />
 <code></dd>
<dt>-f,&#8211;fullscreen</dt>
<dd> </code> Start in full screen mode.<br />
 <code></dd>
<dt>-s,&#8211;slideshow</dt>
<dd> </code> Start in slideshow mode.<br />
 <code></dd>
<dt>-l,&#8211;list</dt>
<dd> </code> Open collection window for command line files.<br />
 <code></dd>
<dt>&#8211;debug</dt>
<dd> </code> Turn on debugging output.<br />
 <code></dd>
<dt>-v,&#8211;version</dt>
<dd> </code> Print version.<br />
 <code></dd>
<dt>-h,&#8211;help</dt>
<dd> </code> Print command line options. </dd>
</dl>
<h2>USAGE</h2>
<p> Key naming is similar to that of <code><a href="/docs/linux/man/1-emacs/">emacs</a></code>(1): <i>C-key</i> indicates that control should be held, and key should be pressed; <i>S-key</i> indicates that shift should be held and key should be pressed; these two can be combined, also, into <i>C-S-key</i>. <code></p>
<dl>
<dt>left-mouse-click</dt>
<dd> </code> (on image) next image<br />
 <code></dd>
<dt>middle-mouse-click</dt>
<dd> </code> (on image) previous image<br />
 <code></dd>
<dt>right-mouse</dt>
<dd> </code> context menu<br />
 <code></dd>
<dt>middle-mouse-drag</dt>
<dd> </code> drag and drop operations<br />
 <code></dd>
<dt>mouse-wheel</dt>
<dd> </code> (on image) Changes to the next or previous image, or if option is enabled, scrolls the image vertically.<br />
 <code></dd>
<dt>mouse-wheel+Shift-key</dt>
<dd> </code> (on image) Inverts the mouse wheel behavior between scrolling image or changing image.<br />
 <code></dd>
<dt>mouse-wheel+Control-key</dt>
<dd> </code> (on image) Zooms the image in and out.
</dd></dl>
<h3>GENERAL KEYS</h3>
<p> <code></p>
<dl>
<dt>PageDown</dt>
<dd> </code> next image<br />
 <code></dd>
<dt>PageUp</dt>
<dd> </code> previous image<br />
 <code></dd>
<dt>Home</dt>
<dd> </code> first image in list<br />
 <code></dd>
<dt>End</dt>
<dd> </code> last image in list<br />
 <code></dd>
<dt>Tab</dt>
<dd> </code> tab completion in path entry window<br />
 <code></dd>
<dt>Escape</dt>
<dd> </code> cancel completion in path entry window or stop generating thumbnails
</dd></dl>
<h3>IMAGE KEYS</h3>
<p> Keys that are valid when the image part of the window is focused. <code></p>
<dl>
<dt>Arrows</dt>
<dd> </code> pan image<br />
 <code></dd>
<dt>Shift+Arrows</dt>
<dd> </code> pan image faster<br />
 <code></dd>
<dt>Space,N</dt>
<dd> </code> next image<br />
 <code></dd>
<dt>Backspace,B</dt>
<dd> </code> previous image
</dd></dl>
<h3>FILE RELATED KEYS</h3>
<p> <code></p>
<dl>
<dt>C</dt>
<dd> </code> new empty collection<br />
 <code></dd>
<dt>O</dt>
<dd> </code> open collection<br />
 <code></dd>
<dt>D</dt>
<dd> </code> open the Find Duplicates window<br />
 <code></dd>
<dt>C-F</dt>
<dd> </code> new folder<br />
 <code></dd>
<dt>C-C</dt>
<dd> </code> copy file<br />
 <code></dd>
<dt>C-M</dt>
<dd> </code> move file<br />
 <code></dd>
<dt>C-R</dt>
<dd> </code> rename file<br />
 <code></dd>
<dt>C-D,Delete</dt>
<dd> </code> delete file<br />
 <code></dd>
<dt>C-N</dt>
<dd> </code> new window<br />
 <code></dd>
<dt>C-W</dt>
<dd> </code> close window<br />
 <code></dd>
<dt>C-Q</dt>
<dd> </code> quit
</dd></dl>
<h3>EDIT MENU RELATED KEYS</h3>
<p> <code></p>
<dl>
<dt>C-1,2..9,0</dt>
<dd> </code> run external editor<br />
 <code></dd>
<dt>C-A</dt>
<dd> </code> select all files<br />
 <code></dd>
<dt>C-S-A</dt>
<dd> </code> unselect all files<br />
 <code></dd>
<dt>C-O</dt>
<dd> </code> go to the Configuration window<br />
 <code></dd>
<dt>C-P</dt>
<dd> </code> display image properties<br />
 <code></dd>
<dt>]</dt>
<dd> </code> rotate image clockwise<br />
 <code></dd>
<dt>[</dt>
<dd> </code> rotate image counterclockwise<br />
 <code></dd>
<dt>S-R</dt>
<dd> </code> rotate image 180 degrees<br />
 <code></dd>
<dt>S-M</dt>
<dd> </code> mirror image (horizontal)<br />
 <code></dd>
<dt>S-F</dt>
<dd> </code> flip image (vertical)
</dd></dl>
<h3>VIEW MENU RELATED KEYS</h3>
<p> <code></p>
<dl>
<dt>+,=</dt>
<dd> </code> zoom in<br />
 <code></dd>
<dt>&#8211;</dt>
<dd> </code> zoom out<br />
 <code></dd>
<dt>Z,KeyPad-/</dt>
<dd> </code> zoom to original size<br />
 <code></dd>
<dt>X,KeyPad-*</dt>
<dd> </code> zoom to fit window<br />
 <code></dd>
<dt>1,2,3,4</dt>
<dd> </code> zoom in to X scale factor<br />
 <code></dd>
<dt>9,8,7</dt>
<dd> </code> zoom to -2, -3, -4, respectively<br />
 <code></dd>
<dt>T</dt>
<dd> </code> toggle thumbnail display<br />
 <code></dd>
<dt>C-L</dt>
<dd> </code> display files in list format<br />
 <code></dd>
<dt>C-I</dt>
<dd> </code> display files in icon format<br />
 <code></dd>
<dt>C-T</dt>
<dd> </code> toggle tree view for directories<br />
 <code></dd>
<dt>R</dt>
<dd> </code> refresh file list<br />
 <code></dd>
<dt>L</dt>
<dd> </code> toggle floating of file selection area<br />
 <code></dd>
<dt>H</dt>
<dd> </code> toggle hiding of file selection area<br />
 <code></dd>
<dt>F,V</dt>
<dd> </code> toggle full-screen mode<br />
 <code></dd>
<dt>S</dt>
<dd> </code> toggle slide-show mode<br />
 <code></dd>
<dt>P</dt>
<dd> </code> toggle pause of slideshow<br />
 <code></dd>
<dt>C-E</dt>
<dd> </code> toggle display of exif sidebar<br />
 <code></dd>
<dt>C-S</dt>
<dd> </code> toggle display of sort manager
</dd></dl>
<h3>COLLECTION WINDOW KEYS</h3>
<p> <code></p>
<dl>
<dt>Arrows</dt>
<dd> </code> move selection<br />
 <code></dd>
<dt>Shift+Arrows</dt>
<dd> </code> select multiple images<br />
 <code></dd>
<dt>Control+Arrows</dt>
<dd> </code> move selector without changing selection<br />
 <code></dd>
<dt>Space</dt>
<dd> </code> select the image under the selector<br />
 <code></dd>
<dt>Control+Space</dt>
<dd> </code> toggle selection of the image under the selector<br />
 <code></dd>
<dt>Home</dt>
<dd> </code> move selector to the top image<br />
 <code></dd>
<dt>End</dt>
<dd> </code> move selector to bottom image<br />
 Adding Shift or Control to Home and End has a similar effect as adding them to the arrows. <code></dd>
<dt>C-A</dt>
<dd> </code> select all images<br />
 <code></dd>
<dt>C-S-A</dt>
<dd> </code> unselect all images<br />
 <code></dd>
<dt>Delete</dt>
<dd> </code> remove image form collection (does not delete the file)<br />
 <code></dd>
<dt>C-L</dt>
<dd> </code> add images to collection form main file list<br />
 <code></dd>
<dt>N</dt>
<dd> </code> sort collection by name<br />
 <code></dd>
<dt>D</dt>
<dd> </code> sort collection by date<br />
 <code></dd>
<dt>B</dt>
<dd> </code> sort collection by file size<br />
 <code></dd>
<dt>P</dt>
<dd> </code> sort collection by pathname<br />
 <code></dd>
<dt>I</dt>
<dd> </code> sort collection by name numerically (*)<br />
 <code></dd>
<dt>Enter</dt>
<dd> </code> view image under selector in the main image window<br />
 <code></dd>
<dt>V</dt>
<dd> </code> view image under selector in new window<br />
 <code></dd>
<dt>C-1,2..9,0</dt>
<dd> </code> open selected image(s) in external editor<br />
 <code></dd>
<dt>S</dt>
<dd> </code> save collection<br />
 <code></dd>
<dt>C-S</dt>
<dd> </code> save collection as<br />
 <code></dd>
<dt>A</dt>
<dd> </code> append current collection to existing collection<br />
 <code></dd>
<dt>C-C</dt>
<dd> </code> copy selected files<br />
 <code></dd>
<dt>C-M</dt>
<dd> </code> move selected files<br />
 <code></dd>
<dt>C-R</dt>
<dd> </code> rename selected files<br />
 <code></dd>
<dt>C-D</dt>
<dd> </code> delete selected files<br />
 <code></dd>
<dt>C-W</dt>
<dd> </code> close window
</dd></dl>
<h3>DUPLICATES WINDOW KEYS</h3>
<p> <code></p>
<dl>
<dt>C-A</dt>
<dd> </code> select all images<br />
 <code></dd>
<dt>C-S-A</dt>
<dd> </code> unselect all images<br />
 <code></dd>
<dt>1</dt>
<dd> </code> select group 1 images<br />
 <code></dd>
<dt>2</dt>
<dd> </code> select group 2 images<br />
 <code></dd>
<dt>C-L</dt>
<dd> </code> add images from main window file list<br />
 <code></dd>
<dt>C</dt>
<dd> </code> add selected images to new collection<br />
 <code></dd>
<dt>Delete</dt>
<dd> </code> remove selected images from list<br />
 <code></dd>
<dt>C-Delete</dt>
<dd> </code> clear window<br />
 <code></dd>
<dt>Enter</dt>
<dd> </code> view image with focus in main window<br />
 <code></dd>
<dt>V</dt>
<dd> </code> view image with focus in new window<br />
 <code></dd>
<dt>C-1,2..9,0</dt>
<dd> </code> open selected image(s) in editor<br />
 <code></dd>
<dt>C-P</dt>
<dd> </code> display properties window for selected images<br />
 <code></dd>
<dt>C-C</dt>
<dd> </code> copy selected files<br />
 <code></dd>
<dt>C-M</dt>
<dd> </code> move selected files<br />
 <code></dd>
<dt>C-R</dt>
<dd> </code> rename selected files<br />
 <code></dd>
<dt>C-D</dt>
<dd> </code> delete selected files<br />
 <code></dd>
<dt>C-W</dt>
<dd> </code> close window </dd>
</dl>
<h2>LICENSE</h2>
<p> Copyright (C) 1999-2004 by John Ellis. Use this software at your own risk! This software released under the GNU General Public License. Please read the COPYING file for more information.</p>
<h2>BUGS</h2>
<p> Please send bug reports and feedback to gqview [at] users.sourceforge.net or the author, below.</p>
<h2>AUTHOR</h2>
<p> <code>John Ellis</code> &lt;johne [at] verizon.net&gt;<br />
 Manpage originally prepared by <code>Nick Rusnov</code> &lt;nick [at] grawk.net&gt; </p>
