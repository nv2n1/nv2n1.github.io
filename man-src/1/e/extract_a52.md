---
title: "extract_a52(1)"
name: "extract_a52"
section: "1"
letter: "e"
url: "/docs/linux/man/1-extract_a52/"
description: "extract_a52 – extract ATSC A/52 audio from a MPEG stream."
---

<h2>NAME</h2>
<p> extract_a52 &#8211; extract ATSC A/52 audio from a MPEG stream.</p>
<h2>SYNOPSIS</h2>
<p> <code>extract_a52</code> [<i>-h</i>] [<i>-s [track]</i>] [<i>-t pid</i>] [<i>file</i>]</p>
<h2>DESCRIPTION</h2>
<p> `extract_a52&#8242; extracts ATSC A/52 audio from a MPEG stream. Input is from stdin if no file is given.</p>
<dl>
<dt><code>-h</code></p>
<dd> display help</p>
<dt><code>-s track</code></p>
<dd> set track number (0-7 or 0x80-0x87)</p>
<dt><code>-t pid</code></p>
<dd> use transport stream demultiplexer, pid 0x10-0x1ffe</dl>
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
<p> <code><a href="/docs/linux/man/1-a52dec/">a52dec</a></code>(1) </p>
<h2>Index</h2>
