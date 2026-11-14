---
title: "xwd(1)"
name: "xwd"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xwd/"
description: "xwd – dump an image of an X window"
---

<h2 class="name">NAME</h2>
<p> xwd &#8211; dump an image of an X window </p>
<h2>SYNOPSIS</h2>
<p> <code>xwd</code> [-debug] [-help] [-nobdrs] [-out <i>file</i>] [-xy] [-frame] [-add <i>value</i>] [-root | -id <i>id</i> | -name <i>name</i> ] [-icmap] [-screen] [-silent] [-display <i>display</i>] [-version]</p>
<h2>DESCRIPTION</h2>
<p> <i>Xwd</i> is an X Window System window dumping utility. <i>Xwd</i> allows X users to store window images in a specially formatted dump file. This file can then be read by various other X utilities for redisplay, printing, editing, formatting, archiving, image processing, etc. The target window is selected by clicking the pointer in the desired window. The keyboard bell is rung once at the beginning of the dump and twice when the dump is completed.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-display </code><i>display</i></p>
<dd> This argument allows you to specify the server to connect to; see <i><a href="/docs/linux/man/7-x/">X</a>(7)</i>.</dl>
<dl>
<dt><code>-help</code></p>
<dd> Print out the `Usage:&#8217; command syntax summary.</dl>
<dl>
<dt><code>-nobdrs</code></p>
<dd> This argument specifies that the window dump should not include the pixels that compose the X window border. This is useful in situations where you may wish to include the window contents in a document as an illustration.</dl>
<dl>
<dt><code>-out </code><i>file</i></p>
<dd> This argument allows the user to explicitly specify the output file on the command line. The default is to output to standard out.</dl>
<dl>
<dt><code>-xy</code></p>
<dd> This option applies to color displays only. It selects `XY&#8217; format dumping instead of the default `Z&#8217; format.</dl>
<dl>
<dt><code>-add </code><i>value</i></p>
<dd> This option specifies a signed value to be added to every pixel.</dl>
<dl>
<dt><code>-frame</code></p>
<dd> This option indicates that the window manager frame should be included when manually selecting a window.</dl>
<dl>
<dt><code>-root</code></p>
<dd> This option indicates that the root window should be selected for the window dump, without requiring the user to select a window with the pointer.</dl>
<dl>
<dt><code>-id </code><i>id</i></p>
<dd> This option indicates that the window with the specified resource id should be selected for the window dump, without requiring the user to select a window with the pointer.</dl>
<dl>
<dt><code>-name </code><i>name</i></p>
<dd> This option indicates that the window with the specified WM_NAME property should be selected for the window dump, without requiring the user to select a window with the pointer.</dl>
<dl>
<dt><code>-icmap</code></p>
<dd> Normally the colormap of the chosen window is used to obtain RGB values. This option forces the first installed colormap of the screen to be used instead.</dl>
<dl>
<dt><code>-screen</code></p>
<dd> This option indicates that the GetImage request used to obtain the image should be done on the root window, rather than directly on the specified window. In this way, you can obtain pieces of other windows that overlap the specified window, and more importantly, you can capture menus or other popups that are independent windows but appear over the specified window.</dl>
<dl>
<dt><code>-silent</code></p>
<dd> Operate silently, i.e. don&#8217;t ring any bells before and after dumping the window.</dl>
<dl>
<dt><code>-version</code></p>
<dd> This option indicates that <i>xwd</i> should print its version information and exit.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></p>
<dd> To get default host and display number.</dl>
<h2>FILES</h2>
<dl>
<dt><code>XWDFile.h</code></p>
<dd> X Window Dump File format definition file.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-xwud/">xwud</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7)</p>
<h2>AUTHORS</h2>
<p> Tony Della Fera, Digital Equipment Corp., MIT Project Athena<br />
 William F. Wyatt, Smithsonian Astrophysical Observatory </p>
<h2>Index</h2>
