---
title: "xbrlapi(1)"
name: "xbrlapi"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xbrlapi/"
description: "xbrlapi – X11 BrlAPI helper for Linux/Unix"
---

<h2 class="name">NAME</h2>
<p> xbrlapi &#8211; X11 BrlAPI helper for Linux/Unix </p>
<h2>SYNOPSIS</h2>
<p> <code>xbrlapi</code> [<i>option</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>xbrlapi</code> connects to a <code>BrlAPI</code> server in order to provide it with the ID of the <code>X11</code> window which currently has focus. It also simulates <code>X</code> keysyms from braille key presses (else brltty would simulate them using a qwerty keyboard). By default, it puts itself in the background, unless option <code>-n</code> is given.</p>
<h2>OPTIONS</h2>
<p> Options are processed sequentially from left to right. If an option is specified more than once, or in case of a conflict, the rightmost specification takes precedence. </p>
<p> The following options are supported:</p>
<dl>
<dt><code>-b</code> [<i>host</i>][:<i>port</i>] (<code>&#8211;brlapi=</code>)</p>
<dd> The <code>BrlAPI</code> server to connect to.</p>
<dt><code>-a</code> <i>string</i> (<code>&#8211;auth=</code>)</p>
<dd> The <code>BrlAPI</code> authorization/authentication string.</p>
<dt><code>-d</code> <i>display</i> (<code>&#8211;display=</code>)</p>
<dd> The <code>X</code> display to connect to. If not specified, the content of the <code>DISPLAY</code> environment variable is used.</p>
<dt><code>-n</code> (<code>&#8211;no-daemon</code>)</p>
<dd> Keep xbrlapi in the foreground.</p>
<dt><code>-q</code> (<code>&#8211;quiet</code>)</p>
<dd> Do not write any text to the braille device.</p>
<dt><code>-h</code> (<code>&#8211;help</code>)</p>
<dd> Print a command line usage summary and then exit.</p>
<dt><code>-H</code> (<code>&#8211;full-help</code>)</p>
<dd> Print a thorough command line usage summary and then exit.</dl>
<h2>SEE ALSO</h2>
<p> For more details on the purpose of <code>xbrlapi</code>, see <code>BrlAPI</code>&#8216;s on-line manual at [<code><a rel="nofollow" href="http://brltty.app/doc/Manual-BrlAPI/English/BrlAPI-3.html">http://brltty.app/doc/Manual-BrlAPI/English/BrlAPI-3.html</a></code>]. </p>
<h2>Index</h2>
