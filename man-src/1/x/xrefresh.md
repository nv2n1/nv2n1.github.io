---
title: "xrefresh(1)"
name: "xrefresh"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xrefresh/"
description: "xrefresh – refresh all or part of an X screen"
---

<h2 class="name">NAME</h2>
<p> xrefresh &#8211; refresh all or part of an X screen </p>
<h2>SYNOPSIS</h2>
<p> <code>xrefresh</code> [-option &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <i>Xrefresh</i> is a simple X program that causes all or part of your screen to be repainted. This is useful when system messages have messed up your screen. <i>Xrefresh</i> maps a window on top of the desired area of the screen and then immediately unmaps it, causing refresh events to be sent to all applications. By default, a window with no background is used, causing all applications to repaint &#8220;smoothly.&#8221; However, the various options can be used to indicate that a solid background (of any color) or the root window background should be used instead.</p>
<h2>ARGUMENTS</h2>
<dl>
<dt><code>-white</code></p>
<dd> Use a white background. The screen just appears to flash quickly, and then repaint.</dl>
<dl>
<dt><code>-black</code></p>
<dd> Use a black background (in effect, turning off all of the electron guns to the tube). This can be somewhat disorienting as everything goes black for a moment.</dl>
<dl>
<dt><code>-solid </code><i>color</i></p>
<dd> Use a solid background of the specified color. Try green.</dl>
<dl>
<dt><code>-root</code></p>
<dd> Use the root window background.</dl>
<dl>
<dt><code>-none</code></p>
<dd> This is the default. All of the windows simply repaint.</dl>
<dl>
<dt><code>-geometry </code><i>WxH+X+Y</i></p>
<dd> Specifies the portion of the screen to be repainted; see <i><a href="/docs/linux/man/7-x/">X</a>(7)</i>.</dl>
<dl>
<dt><code>-display </code><i>display</i></p>
<dd> This argument allows you to specify the server and screen to refresh; see <i><a href="/docs/linux/man/7-x/">X</a>(7)</i>.</dl>
<dl>
<dt><code>-version</code></p>
<dd> This argument prints the program version and exits.</dl>
<h2>X DEFAULTS</h2>
<p> The <i>xrefresh</i> program uses the routine <i><a href="/docs/linux/man/3-xgetdefault/">XGetDefault</a>(3)</i> to read defaults, so its resource names are all capitalized. </p>
<dl>
<dt><code>Black</code>, <code>White</code>, <code>Solid</code>, <code>None</code>, <code>Root</code></p>
<dd> Determines what sort of window background to use.</dl>
<dl>
<dt><code>Geometry</code></p>
<dd> Determines the area to refresh. Not very useful.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt>DISPLAY &#8211; To get default host and display number.</p>
<dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7)</p>
<h2>BUGS</h2>
<p> It should have just one default type for the background.</p>
<h2>AUTHORS</h2>
<p> Jim Gettys, Digital Equipment Corp., MIT Project Athena </p>
<h2>Index</h2>
