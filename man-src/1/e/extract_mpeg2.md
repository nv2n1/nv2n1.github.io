---
title: "extract_mpeg2(1)"
name: "extract_mpeg2"
section: "1"
letter: "e"
url: "/docs/linux/man/1-extract_mpeg2/"
description: "extract_mpeg2 – extract MPEG video streams from a multiplexed stream."
---

<h2>NAME</h2>
<p> extract_mpeg2 &#8211; extract MPEG video streams from a multiplexed stream.</p>
<h2>SYNOPSIS</h2>
<p> <code>extract_mpeg2</code> [<i>-h</i>] [<i>-s [track]</i>] [<i>-t pid</i>] [<i>file</i>]</p>
<h2>DESCRIPTION</h2>
<p> `extract_mpeg2&#8242; extracts MPEG video streams from a multiplexed stream. Input is from stdin if no file is given.</p>
<dl>
<dt><code>-h</code></p>
<dd> display help</p>
<dt><code>-s track</code></p>
<dd> set track number (0-0xf or 0xe0-0xef)</p>
<dt><code>-t pid</code></p>
<dd> use transport stream demultiplexer, pid 0x10-0x1ffe</dl>
<h2>AUTHORS</h2>
<p> Michel Lespinasse &lt;walken [at] zoy.org&gt;<br />
 Aaron Holtzman &lt;aholtzma [at] ess.engr.uvic.ca&gt;<br />
 And many others on the net.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;libmpeg2-devel [at] lists.sourceforge.net&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2000-2003 Michel Lespinasse<br />
 Copyright &#169; 1999-2000 Aaron Holtzman<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mpeg2dec/">mpeg2dec</a></code>(1) </p>
<h2>Index</h2>
