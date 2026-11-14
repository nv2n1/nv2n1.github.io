---
title: "xsetdashes(3)"
name: "xsetdashes"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xsetdashes/"
description: "XSetLineAttributes, XSetDashes – GC convenience routines"
---

<p>XSetLineAttributes, XSetDashes &#8211; GC convenience routines </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XSetLineAttributes(Display *<i>display</i>, GC <i>gc</i>, unsigned int <i>line_width</i>, int <i>line_style</i>, int <i>cap_style</i>, int <i>join_style</i>);</p>
<dd>int XSetDashes(Display *<i>display</i>, GC <i>gc</i>, int <i>dash_offset</i>, char <i>dash_list</i>[], int <i>n</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>cap_style</i></p>
<dd>Specifies the line-style and cap-style you want to set for the specified GC. You can pass <code>CapNotLast</code>, <code>CapButt</code>, <code>CapRound</code>, or <code>CapProjecting</code>.</p>
<dt><i>dash_list</i></p>
<dd>Specifies the dash-list for the dashed line-style you want to set for the specified GC.</p>
<dt><i>dash_offset</i></p>
<dd>Specifies the phase of the pattern for the dashed line-style you want to set for the specified GC.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>gc</i></p>
<dd>Specifies the GC.</p>
<dt><i>join_style</i></p>
<dd>Specifies the line join-style you want to set for the specified GC. You can pass <code>JoinMiter</code>, <code>JoinRound</code>, or <code>JoinBevel</code>.</p>
<dt><i>line_style</i></p>
<dd>Specifies the line-style you want to set for the specified GC. You can pass <code>LineSolid</code>, <code>LineOnOffDash</code>, or <code>LineDoubleDash</code>.</p>
<dt><i>line_width</i></p>
<dd>Specifies the line-width you want to set for the specified GC.</p>
<dt><i>n</i></p>
<dd>Specifies the number of elements in dash_list.</dl>
<h2>Description</h2>
<p>The <code>XSetLineAttributes</code> function sets the line drawing components in the specified GC. </p>
<p> <code>XSetLineAttributes</code> can generate <code>BadAlloc</code>, <code>BadGC</code>, and <code>BadValue</code> errors. </p>
<p> The <code>XSetDashes</code> function sets the dash-offset and dash-list attributes for dashed line styles in the specified GC. There must be at least one element in the specified dash_list, or a <code>BadValue</code> error results. The initial and alternating elements (second, fourth, and so on) of the dash_list are the even dashes, and the others are the odd dashes. Each element specifies a dash length in pixels. All of the elements must be nonzero, or a <code>BadValue</code> error results. Specifying an odd-length list is equivalent to specifying the same list concatenated with itself to produce an even-length list. </p>
<p> The dash-offset defines the phase of the pattern, specifying how many pixels into the dash-list the pattern should actually begin in any single graphics request. Dashing is continuous through path elements combined with a join-style but is reset to the dash-offset between each sequence of joined lines. </p>
<p> The unit of measure for dashes is the same for the ordinary coordinate system. Ideally, a dash length is measured along the slope of the line, but implementations are only required to match this ideal for horizontal and vertical lines. Failing the ideal semantics, it is suggested that the length be measured along the major axis of the line. The major axis is defined as the x axis for lines drawn at an angle of between -45 and +45 degrees or between 135 and 225 degrees from the x axis. For all other lines, the major axis is the y axis. </p>
<p> <code>XSetDashes</code> can generate <code>BadAlloc</code>, <code>BadGC</code>, and <code>BadValue</code> errors.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>The server failed to allocate the requested resource or server memory.</p>
<dt><code>BadGC</code></p>
<dd>A value for a GContext argument does not name a defined GContext.</p>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xcreategc/">XCreateGC</a>(3), <a href="/docs/linux/man/3-xquerybestsize/">XQueryBestSize</a>(3), <a href="/docs/linux/man/3-xsetarcmode/">XSetArcMode</a>(3), <a href="/docs/linux/man/3-xsetcliporigin/">XSetClipOrigin</a>(3), <a href="/docs/linux/man/3-xsetfillstyle/">XSetFillStyle</a>(3), <a href="/docs/linux/man/3-xsetfont/">XSetFont</a>(3), <a href="/docs/linux/man/3-xsetstate/">XSetState</a>(3), <a href="/docs/linux/man/3-xsettile/">XSetTile</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
