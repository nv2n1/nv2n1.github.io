---
title: "geeqie(1)"
name: "geeqie"
section: "1"
letter: "g"
url: "/docs/linux/man/1-geeqie/"
description: "Geeqie – GTK based multiformat image viewer"
---

<h2 class="name">NAME</h2>
<p> Geeqie &#8211; GTK based multiformat image viewer </p>
<h2>SYNOPSIS</h2>
<p> <code>geeqie</code> [<i>options</i>] [<i>path</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>Geeqie</code> is an interactive GTK based image viewer that supports multiple image formats, zooming, panning, thumbnails and sorting images into collections. </p>
<h2>OPTIONS</h2>
<p> <code></p>
<dl>
<dt>+t,&#8211;with-tools</p>
<dd> </code> Force the toolbox to be shown.<br />
 <code></p>
<dt>-t,&#8211;without-tools</p>
<dd> </code> Force the toolbox to be hidden.<br />
 <code></p>
<dt>-f,&#8211;fullscreen</p>
<dd> </code> Start in full screen mode.<br />
 <code></p>
<dt>-s,&#8211;slideshow</p>
<dd> </code> Start in slideshow mode.<br />
 <code></p>
<dt>-l,&#8211;list</p>
<dd> </code> Open collection window for command line files.<br />
 <code></p>
<dt>&#8211;debug</p>
<dd> </code> Turn on debugging output.<br />
 <code></p>
<dt>-v,&#8211;version</p>
<dd> </code> Print version.<br />
 <code></p>
<dt>-h,&#8211;help</p>
<dd> </code> Print command line options. </p>
</dl>
<h2>USAGE</h2>
<p> Key naming is similar to that of <code><a href="/docs/linux/man/1-emacs/">emacs</a></code>(1): <i>C-key</i> indicates that control should be held, and key should be pressed; <i>S-key</i> indicates that shift should be held and key should be pressed; these two can be combined, also, into <i>C-S-key</i>. <code></p>
<dl>
<dt>left-mouse-click</p>
<dd> </code> (on image) next image<br />
 <code></p>
<dt>middle-mouse-click</p>
<dd> </code> (on image) previous image<br />
 <code></p>
<dt>right-mouse</p>
<dd> </code> context menu<br />
 <code></p>
<dt>middle-mouse-drag</p>
<dd> </code> drag and drop operations<br />
 <code></p>
<dt>mouse-wheel</p>
<dd> </code> (on image) Changes to the next or previous image, or if option is enabled, scrolls the image vertically.<br />
 <code></p>
<dt>mouse-wheel+Shift-key</p>
<dd> </code> (on image) Inverts the mouse wheel behavior between scrolling image or changing image.<br />
 <code></p>
<dt>mouse-wheel+Control-key</p>
<dd> </code> (on image) Zooms the image in and out.
</dl>
<h3>GENERAL KEYS</h3>
<p> <code></p>
<dl>
<dt>PageDown</p>
<dd> </code> next image<br />
 <code></p>
<dt>PageUp</p>
<dd> </code> previous image<br />
 <code></p>
<dt>Home</p>
<dd> </code> first image in list<br />
 <code></p>
<dt>End</p>
<dd> </code> last image in list<br />
 <code></p>
<dt>Tab</p>
<dd> </code> tab completion in path entry window<br />
 <code></p>
<dt>Escape</p>
<dd> </code> cancel completion in path entry window or stop generating thumbnails
</dl>
<h3>IMAGE KEYS</h3>
<p> Keys that are valid when the image part of the window is focused. <code></p>
<dl>
<dt>Arrows</p>
<dd> </code> pan image<br />
 <code></p>
<dt>Shift+Arrows</p>
<dd> </code> pan image faster<br />
 <code></p>
<dt>Space,N</p>
<dd> </code> next image<br />
 <code></p>
<dt>Backspace,B</p>
<dd> </code> previous image
</dl>
<h3>FILE RELATED KEYS</h3>
<p> <code></p>
<dl>
<dt>C</p>
<dd> </code> new empty collection<br />
 <code></p>
<dt>O</p>
<dd> </code> open collection<br />
 <code></p>
<dt>D</p>
<dd> </code> open the Find Duplicates window<br />
 <code></p>
<dt>C-F</p>
<dd> </code> new folder<br />
 <code></p>
<dt>C-C</p>
<dd> </code> copy file<br />
 <code></p>
<dt>C-M</p>
<dd> </code> move file<br />
 <code></p>
<dt>C-R</p>
<dd> </code> rename file<br />
 <code></p>
<dt>C-D,Delete</p>
<dd> </code> delete file<br />
 <code></p>
<dt>C-N</p>
<dd> </code> new window<br />
 <code></p>
<dt>C-W</p>
<dd> </code> close window<br />
 <code></p>
<dt>C-Q</p>
<dd> </code> quit
</dl>
<h3>EDIT MENU RELATED KEYS</h3>
<p> <code></p>
<dl>
<dt>C-1,2..9,0</p>
<dd> </code> run external editor<br />
 <code></p>
<dt>C-A</p>
<dd> </code> select all files<br />
 <code></p>
<dt>C-S-A</p>
<dd> </code> unselect all files<br />
 <code></p>
<dt>C-O</p>
<dd> </code> go to the Configuration window<br />
 <code></p>
<dt>C-P</p>
<dd> </code> display image properties<br />
 <code></p>
<dt>]</p>
<dd> </code> rotate image clockwise<br />
 <code></p>
<dt>[</p>
<dd> </code> rotate image counterclockwise<br />
 <code></p>
<dt>S-R</p>
<dd> </code> rotate image 180 degrees<br />
 <code></p>
<dt>S-M</p>
<dd> </code> mirror image (horizontal)<br />
 <code></p>
<dt>S-F</p>
<dd> </code> flip image (vertical)
</dl>
<h3>VIEW MENU RELATED KEYS</h3>
<p> <code></p>
<dl>
<dt>+,=</p>
<dd> </code> zoom in<br />
 <code></p>
<dt>&#8211;</p>
<dd> </code> zoom out<br />
 <code></p>
<dt>Z,KeyPad-/</p>
<dd> </code> zoom to original size<br />
 <code></p>
<dt>X,KeyPad-*</p>
<dd> </code> zoom to fit window<br />
 <code></p>
<dt>1,2,3,4</p>
<dd> </code> zoom in to X scale factor<br />
 <code></p>
<dt>9,8,7</p>
<dd> </code> zoom to -2, -3, -4, respectively<br />
 <code></p>
<dt>T</p>
<dd> </code> toggle thumbnail display<br />
 <code></p>
<dt>C-L</p>
<dd> </code> display files in list format<br />
 <code></p>
<dt>C-I</p>
<dd> </code> display files in icon format<br />
 <code></p>
<dt>C-T</p>
<dd> </code> toggle tree view for directories<br />
 <code></p>
<dt>R</p>
<dd> </code> refresh file list<br />
 <code></p>
<dt>L</p>
<dd> </code> toggle floating of file selection area<br />
 <code></p>
<dt>H</p>
<dd> </code> toggle hiding of file selection area<br />
 <code></p>
<dt>F,V</p>
<dd> </code> toggle full-screen mode<br />
 <code></p>
<dt>S</p>
<dd> </code> toggle slide-show mode<br />
 <code></p>
<dt>P</p>
<dd> </code> toggle pause of slideshow<br />
 <code></p>
<dt>C-E</p>
<dd> </code> toggle display of exif sidebar<br />
 <code></p>
<dt>C-S</p>
<dd> </code> toggle display of sort manager
</dl>
<h3>COLLECTION WINDOW KEYS</h3>
<p> <code></p>
<dl>
<dt>Arrows</p>
<dd> </code> move selection<br />
 <code></p>
<dt>Shift+Arrows</p>
<dd> </code> select multiple images<br />
 <code></p>
<dt>Control+Arrows</p>
<dd> </code> move selector without changing selection<br />
 <code></p>
<dt>Space</p>
<dd> </code> select the image under the selector<br />
 <code></p>
<dt>Control+Space</p>
<dd> </code> toggle selection of the image under the selector<br />
 <code></p>
<dt>Home</p>
<dd> </code> move selector to the top image<br />
 <code></p>
<dt>End</p>
<dd> </code> move selector to bottom image<br />
 Adding Shift or Control to Home and End has a similar effect as adding them to the arrows. <code></p>
<dt>C-A</p>
<dd> </code> select all images<br />
 <code></p>
<dt>C-S-A</p>
<dd> </code> unselect all images<br />
 <code></p>
<dt>Delete</p>
<dd> </code> remove image form collection (does not delete the file)<br />
 <code></p>
<dt>C-L</p>
<dd> </code> add images to collection form main file list<br />
 <code></p>
<dt>N</p>
<dd> </code> sort collection by name<br />
 <code></p>
<dt>D</p>
<dd> </code> sort collection by date<br />
 <code></p>
<dt>B</p>
<dd> </code> sort collection by file size<br />
 <code></p>
<dt>P</p>
<dd> </code> sort collection by pathname<br />
 <code></p>
<dt>I</p>
<dd> </code> sort collection by name numerically (*)<br />
 <code></p>
<dt>Enter</p>
<dd> </code> view image under selector in the main image window<br />
 <code></p>
<dt>V</p>
<dd> </code> view image under selector in new window<br />
 <code></p>
<dt>C-1,2..9,0</p>
<dd> </code> open selected image(s) in external editor<br />
 <code></p>
<dt>S</p>
<dd> </code> save collection<br />
 <code></p>
<dt>C-S</p>
<dd> </code> save collection as<br />
 <code></p>
<dt>A</p>
<dd> </code> append current collection to existing collection<br />
 <code></p>
<dt>C-C</p>
<dd> </code> copy selected files<br />
 <code></p>
<dt>C-M</p>
<dd> </code> move selected files<br />
 <code></p>
<dt>C-R</p>
<dd> </code> rename selected files<br />
 <code></p>
<dt>C-D</p>
<dd> </code> delete selected files<br />
 <code></p>
<dt>C-W</p>
<dd> </code> close window
</dl>
<h3>DUPLICATES WINDOW KEYS</h3>
<p> <code></p>
<dl>
<dt>C-A</p>
<dd> </code> select all images<br />
 <code></p>
<dt>C-S-A</p>
<dd> </code> unselect all images<br />
 <code></p>
<dt>1</p>
<dd> </code> select group 1 images<br />
 <code></p>
<dt>2</p>
<dd> </code> select group 2 images<br />
 <code></p>
<dt>C-L</p>
<dd> </code> add images from main window file list<br />
 <code></p>
<dt>C</p>
<dd> </code> add selected images to new collection<br />
 <code></p>
<dt>Delete</p>
<dd> </code> remove selected images from list<br />
 <code></p>
<dt>C-Delete</p>
<dd> </code> clear window<br />
 <code></p>
<dt>Enter</p>
<dd> </code> view image with focus in main window<br />
 <code></p>
<dt>V</p>
<dd> </code> view image with focus in new window<br />
 <code></p>
<dt>C-1,2..9,0</p>
<dd> </code> open selected image(s) in editor<br />
 <code></p>
<dt>C-P</p>
<dd> </code> display properties window for selected images<br />
 <code></p>
<dt>C-C</p>
<dd> </code> copy selected files<br />
 <code></p>
<dt>C-M</p>
<dd> </code> move selected files<br />
 <code></p>
<dt>C-R</p>
<dd> </code> rename selected files<br />
 <code></p>
<dt>C-D</p>
<dd> </code> delete selected files<br />
 <code></p>
<dt>C-W</p>
<dd> </code> close window </p>
</dl>
<h2>LICENSE</h2>
<p> Copyright (C) 1999-2004 by John Ellis. Use this software at your own risk! This software released under the GNU General Public License. Please read the COPYING file for more information.</p>
<h2>BUGS</h2>
<p> Please send bug reports and feedback to geeqie-devel [at] lists.sourceforge.net</p>
<h2>AUTHOR</h2>
<p> <code>John Ellis</code> &lt;johne [at] verizon.net&gt;<br />
 Manpage originally prepared by <code>Nick Rusnov</code> &lt;nick [at] grawk.net&gt; </p>
<h2>Index</h2>
