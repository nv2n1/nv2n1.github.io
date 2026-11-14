---
title: "xsetroot(1)"
name: "xsetroot"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xsetroot/"
description: "xsetroot – root window parameter setting utility for X"
---

<h2 class="name">NAME</h2>
<p> xsetroot &#8211; root window parameter setting utility for X </p>
<h2>SYNOPSIS</h2>
<p> <code>xsetroot</code> [-help] [-version] [-def] [-display <i>display</i>] [-cursor <i>cursorfile maskfile</i>] [-cursor_name <i>cursorfontname</i>] [-xcf <i>cursorfile</i> <i>cursorsize</i>] [-bitmap <i>filename</i> | -mod <i>x y</i> | -gray | -grey | -solid <i>color</i>] [-bg <i>color</i>] [-fg <i>color</i>] [-rv] [-name <i>string</i>] [-d <i>display</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <i>xsetroot</i> program allows you to tailor the appearance of the background (&quot;root&quot;) window on a workstation display running X. Normally, you experiment with <i>xsetroot</i> until you find a personalized look that you like, then put the <i>xsetroot</i> command that produces it into your X startup file. If no options are specified, or if <i>-def</i> is specified, the window is reset to its default state. The <i>-def</i> option can be specified along with other options and only the non-specified characteristics will be reset to the default state. </p>
<p> Only one of the background color/tiling changing options (-solid, -gray, -grey, -bitmap, and -mod) may be specified at a time.</p>
<h2>OPTIONS</h2>
<p> The various options are as follows:</p>
<dl>
<dt><code>-help</code></p>
<dd> Print a usage message and exit.</p>
<dt><code>-version</code></p>
<dd> Print a version message and exit.</p>
<dt><code>-def, -default</code></p>
<dd> Reset unspecified attributes to the default values. (Restores the background to the familiar gray mesh and the cursor to the hollow x shape.)</p>
<dt><code>-cursor</code> <i>cursorfile</i> <i>maskfile</i></p>
<dd> This lets you change the pointer cursor to whatever you want when the pointer cursor is outside of any window. Cursor and mask files are bitmaps (little pictures), and can be made with the <i><a href="/docs/linux/man/1-bitmap/">bitmap</a>(1)</i> program. You probably want the mask file to be all black until you get used to the way masks work.</p>
<dt><code>-cursor_name</code> <i>cursorfontname</i></p>
<dd> This lets you change the pointer cursor to one of the standard cursors from the cursor font. Refer to appendix B of the X protocol for the names (except that the XC_ prefix is elided for this option).</p>
<dt><code>-xcf</code> <i>cursorfile</i> <i>cursorsize</i></p>
<dd> This lets you change the pointer cursor to one loaded from an Xcursor file as defined by libXcursor, at the specified size.</p>
<dt><code>-bitmap</code> <i>filename</i></p>
<dd> Use the bitmap specified in the file to set the window pattern. You can make your own bitmap files (little pictures) using the <i><a href="/docs/linux/man/1-bitmap/">bitmap</a>(1)</i> program. The entire background will be made up of repeated &quot;tiles&quot; of the bitmap.</p>
<dt><code>-mod</code> <i>x</i> <i>y</i></p>
<dd> This is used if you want a plaid-like grid pattern on your screen. x and y are integers ranging from 1 to 16. Try the different combinations. Zero and negative numbers are taken as 1.</p>
<dt><code>-gray, -grey</code></p>
<dd> Make the entire background gray (Easier on the eyes).</p>
<dt><code>-bg, -background</code> <i>color</i></p>
<dd> Use &#8220;color&#8221; as the background color.</p>
<dt><code>-fg, -foreground</code> <i>color</i></p>
<dd> Use &#8220;color&#8221; as the foreground color. Foreground and background colors are meaningful only in combination with -cursor, -bitmap, or -mod.</p>
<dt><code>-rv, -reverse</code></p>
<dd> This exchanges the foreground and background colors. Normally the foreground color is black and the background color is white.</p>
<dt><code>-solid</code> <i>color</i></p>
<dd> This sets the background of the root window to the specified color. This option is only useful on color servers.</p>
<dt><code>-name</code> <i>string</i></p>
<dd> Set the name of the root window to &#8220;string&#8221;. There is no default value. Usually a name is assigned to a window so that the window manager can use a text representation when the window is iconified. This option is unused since you can&#8217;t iconify the background.</p>
<dt><code>-d, -display</code> <i>display</i></p>
<dd> Specifies the server to connect to; see <i><a href="/docs/linux/man/7-x/">X</a>(7)</i>.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/1-xset/">xset</a>(1), <a href="/docs/linux/man/1-xrdb/">xrdb</a>(1), <a href="/docs/linux/man/3-xcursor/">Xcursor</a>(3)</p>
<h2>AUTHOR</h2>
<p> Mark Lillibridge, MIT Project Athena </p>
<h2>Index</h2>
