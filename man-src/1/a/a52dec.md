---
title: "a52dec(1)"
name: "a52dec"
section: "1"
letter: "a"
url: "/docs/linux/man/1-a52dec/"
description: "a52dec – decode ATSC A/52 audio streams"
---

<h2>NAME</h2>
<p> a52dec &#8211; decode ATSC A/52 audio streams</p>
<h2>SYNOPSIS</h2>
<p> <code>a52dec</code> [<i>-h</i>] [<i>-s [track]</i>] [<i>-t pid</i>] [<i>-c</i>] [<i>-r</i>] [<i>-o mode</i>] [<i>file</i>]</p>
<h2>DESCRIPTION</h2>
<p> `a52dec&#8217; plays ATSC A/52 audio streams. Input is from stdin if no file is given.</p>
<dl>
<dt><code>-h</code></p>
<dd> display help and available audio modes</p>
<dt><code>-s</code></p>
<dd> use program stream demultiplexer, track 0-7 or 0x80-0x87</p>
<dt><code>-t pid</code></p>
<dd> use transport stream demultiplexer, pid 0x10-0x1ffe</p>
<dt><code>-c</code></p>
<dd> use c implementation, disables all accelerations</p>
<dt><code>-r</code></p>
<dd> disable dynamic range compression</p>
<dt><code>-o</code> <i>mode</i></p>
<dd> use audio output driver `mode&#8217;.<br />
 A list of modes is available using the <code>-h</code> option.</dl>
<h2>AUTHORS</h2>
<p> Michel Lespinasse &lt;walken [at] zoy.org&gt;<br />
 Aaron Holtzman &lt;aholtzma [at] ess.engr.uvic.ca&gt;<br />
 And many others on the net.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;liba52-devel [at] lists.sourceforge.net&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2000-2002 Michel Lespinasse<br />
 Copyright &#169; 1999-2000 Aaron Holtzman<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-extract_a52/">extract_a52</a></code>(1) </p>
<h2>Index</h2>
