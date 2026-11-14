---
title: "xwininfo(1)"
name: "xwininfo"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xwininfo/"
description: "xwininfo – window information utility for X"
---

<h2 class="name">NAME</h2>
<p> xwininfo &#8211; window information utility for X </p>
<h2>SYNOPSIS</h2>
<p> <code>xwininfo</code> [-help] [-id <i>wdid</i>] [-root] [-name <i>wdname</i>] [-int] [-children] [-tree] [-stats] [-bits] [-events] [-size] [-wm] [-shape] [-frame] [-all] [-english] [-metric] [-display <i>host:dpy</i>] [-version]</p>
<h2>DESCRIPTION</h2>
<p> <i>Xwininfo</i> is a utility for displaying information about windows. Various information is displayed depending on which options are selected. If no options are chosen, <code>-stats</code> is assumed. </p>
<p> The user has the option of selecting the target window with the mouse (by clicking any mouse button in the desired window) or by specifying its window id on the command line with the <code>-id</code> option. Or instead of specifying the window by its id number, the <code>-name</code> option may be used to specify which window is desired by name. There is also a special <code>-root</code> option to quickly obtain information on the screen&#8217;s root window.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-help</code></p>
<dd> Print out the `Usage:&#8217; command syntax summary.</dl>
<dl>
<dt><code>-id </code><i>wdid</i></p>
<dd> This option allows the user to specify a target window <i>wdid</i> on the command line rather than using the mouse to select the target window. This is very useful in debugging X applications where the target window is not mapped to the screen or where the use of the mouse might be impossible or interfere with the application.</dl>
<dl>
<dt><code>-name </code><i>wdname</i></p>
<dd> This option allows the user to specify that the window named <i>wdname</i> is the target window on the command line rather than using the mouse to select the target window.</dl>
<dl>
<dt><code>-root</code></p>
<dd> This option specifies that X&#8217;s root window is the target window. This is useful in situations where the root window is completely obscured.</dl>
<dl>
<dt><code>-int</code></p>
<dd> This option specifies that all X window ids should be displayed as integer values. The default is to display them as hexadecimal values.</dl>
<dl>
<dt><code>-children</code></p>
<dd> This option causes the root, parent, and children windows&#8217; ids and names of the selected window to be displayed.</dl>
<dl>
<dt><code>-tree</code></p>
<dd> This option is like <code>-children</code> but displays all children recursively.</dl>
<dl>
<dt><code>-stats</code></p>
<dd> This option causes the display of various attributes pertaining to the location and appearance of the selected window. Information displayed includes the location of the window, its width and height, its depth, border width, visual id and class, colormap id if any, map state, backing-store hint, and location of the corners.</dl>
<dl>
<dt><code>-bits</code></p>
<dd> This option causes the display of various attributes pertaining to the selected window&#8217;s raw bits and how the selected window is to be stored. Displayed information includes the selected window&#8217;s bit gravity, window gravity, backing-store hint, backing-planes value, backing pixel, and whether or not the window has save-under set.</dl>
<dl>
<dt><code>-events</code></p>
<dd> This option causes the selected window&#8217;s event masks to be displayed. Both the event mask of events wanted by some client and the event mask of events not to propagate are displayed.</dl>
<dl>
<dt><code>-size</code></p>
<dd> This option causes the selected window&#8217;s sizing hints to be displayed. Displayed information includes: for both the normal size hints and the zoom size hints, the user supplied location if any; the program supplied location if any; the user supplied size if any; the program supplied size if any; the minimum size if any; the maximum size if any; the resize increments if any; and the minimum and maximum aspect ratios if any.</dl>
<dl>
<dt><code>-wm</code></p>
<dd> This option causes the selected window&#8217;s window manager hints to be displayed. Information displayed may include whether or not the application accepts input, what the window&#8217;s icon window # and name is, where the window&#8217;s icon should go, and what the window&#8217;s initial state should be.</dl>
<dl>
<dt><code>-shape</code></p>
<dd> This option causes the selected window&#8217;s window and border shape extents to be displayed.</p>
<dt><code>-frame</code></p>
<dd> This option causes window manager frames to be considered when manually selecting windows.</dl>
<dl>
<dt><code>-metric</code></p>
<dd> This option causes all individual height, width, and x and y positions to be displayed in millimeters as well as number of pixels, based on what the server thinks the resolution is. Geometry specifications that are in <code>+x+y</code> form are not changed.</p>
<dt><code>-english</code></p>
<dd> This option causes all individual height, width, and x and y positions to be displayed in inches (and feet, yards, and miles if necessary) as well as number of pixels. <code>-metric</code> and <code>-english</code> may both be enabled at the same time.</dl>
<dl>
<dt><code>-all</code></p>
<dd> This option is a quick way to ask for all information possible.</dl>
<dl>
<dt><code>-d, -display </code><i>host:dpy</i></p>
<dd> This option allows you to specify the server to connect to; see <i><a href="/docs/linux/man/7-x/">X</a>(7)</i>.</dl>
<dl>
<dt><code>-version</code></p>
<dd> This option indicates that <i>xwininfo</i> should print its version information and exit.</dl>
<h2>EXAMPLE</h2>
<p> The following is a sample summary taken with no options specified: </p>
<p> xwininfo: Window id: 0x60000f &quot;xterm&quot; </p>
<p>&nbsp;<wbr>&nbsp;Absolute upper-left X: 2<br />
&nbsp;<wbr>&nbsp;Absolute upper-left Y: 85<br />
&nbsp;<wbr>&nbsp;Relative upper-left X:&nbsp;<wbr>&nbsp;0<br />
&nbsp;<wbr>&nbsp;Relative upper-left Y:&nbsp;<wbr>&nbsp;25<br />
&nbsp;<wbr>&nbsp;Width: 579<br />
&nbsp;<wbr>&nbsp;Height: 316<br />
&nbsp;<wbr>&nbsp;Depth: 8<br />
&nbsp;<wbr>&nbsp;Visual: 0x1e<br />
&nbsp;<wbr>&nbsp;Visual Class: PseudoColor<br />
&nbsp;<wbr>&nbsp;Border width: 0<br />
&nbsp;<wbr>&nbsp;Class: InputOutput<br />
&nbsp;<wbr>&nbsp;Colormap: 0x27&nbsp;(installed)<br />
&nbsp;<wbr>&nbsp;Bit Gravity State: NorthWestGravity<br />
&nbsp;<wbr>&nbsp;Window Gravity State: NorthWestGravity<br />
&nbsp;<wbr>&nbsp;Backing Store State: NotUseful<br />
&nbsp;<wbr>&nbsp;Save Under State: no<br />
&nbsp;<wbr>&nbsp;Map State: IsViewable<br />
&nbsp;<wbr>&nbsp;Override Redirect State: no<br />
&nbsp;<wbr>&nbsp;Corners:&nbsp;<wbr>&nbsp;+2+85&nbsp;<wbr>&nbsp;-699+85&nbsp;<wbr>&nbsp;-699-623&nbsp;<wbr>&nbsp;+2-623<br />
&nbsp;<wbr>&nbsp;-geometry 80&#215;24+0+58 </p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></p>
<dd> To get the default host and display number.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-x/">X</a></i>(7), <i><a href="/docs/linux/man/1-xprop/">xprop</a></i>(1), <i><a href="/docs/linux/man/1-xdpyinfo/">xdpyinfo</a></i>(1), <i><a href="/docs/linux/man/1-xdriinfo/">xdriinfo</a></i>(1), <i><a href="/docs/linux/man/1-xvinfo/">xvinfo</a></i>(1), <i><a href="/docs/linux/man/1-glxinfo/">glxinfo</a></i>(1)</p>
<h2>BUGS</h2>
<p> Using <code>-stats -bits</code> shows some redundant information. </p>
<p> The <code>-geometry</code> string displayed must make assumptions about the window&#8217;s border width and the behavior of the application and the window manager. As a result, the location given is not always correct.</p>
<h2>AUTHOR</h2>
<p> Mark Lillibridge, MIT Project Athena </p>
<h2>Index</h2>
