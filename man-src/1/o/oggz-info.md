---
title: "oggz-info(1)"
name: "oggz-info"
section: "1"
letter: "o"
url: "/docs/linux/man/1-oggz-info/"
description: "oggz-info — Display information about one or more Ogg files and their bitstreams."
---

<h2>NAME</h2>
<p> oggz-info &#8212; Display information about one or more Ogg files and their bitstreams.<br />
&nbsp;<wbr></p>
<h2>SYNOPSIS</h2>
<p> <code>oggz-info</code> [-l | &#8211;length ] [-b | &#8211;bitrate ] [-g | &#8211;page-stats ] [-p | &#8211;packet-stats ] [-k | &#8211;skeleton ] [-a | &#8211;all ] filename &#8230; </p>
<p> <code>oggz-info</code> [-h | &#8211;help ] [-v | &#8211;version ]</p>
<h2>Description</h2>
<p> <code>oggz-info</code> displays information about one or more Ogg files and their bitstreams.<br />
&nbsp;<wbr></p>
<h2>Options</h2>
<p> <code>oggz-info</code> accepts the following options:<br />
&nbsp;<wbr></p>
<h3>Display options</h3>
<dl>
<dt>-l, &#8211;length</p>
<dd> Display content lengths.</p>
<dt>-b, &#8211;bitrate</p>
<dd> Display bitrate information.</p>
<dt>-g, &#8211;page-stats</p>
<dd> Display Ogg page statistics.</p>
<dt>-p, &#8211;packet-stats</p>
<dd> Display Ogg packet statistics.</p>
<dt>-k, &#8211;skeleton</p>
<dd> Display Extra data from OggSkeleton bitstream.</p>
<dt>-a, &#8211;all</p>
<dd> Display all information.</dl>
<h3>Miscellaneous options</h3>
<dl>
<dt>-h, &#8211;help</p>
<dd> Display usage information and exit.</p>
<dt>-v, &#8211;version</p>
<dd> Output version information and exit.</dl>
<h2>Units of measurement</h2>
<p> <code>oggz-info</code> displays information using the following units:<br />
&nbsp;<wbr></p>
<h3>Byte lengths</h3>
<dl>
<dt>bytes</p>
<dd> (8 bits)</p>
<dt>kB</p>
<dd> kilobytes (1024 bytes)</p>
<dt>MB</p>
<dd> megabytes (1024*1024 bytes)</p>
<dt>GB</p>
<dd> gigabytes (1024*1024*1024 bytes)</dl>
<h3>Bitrates</h3>
<dl>
<dt>bps</p>
<dd> bits per second (bit/s)</p>
<dt>kbps</p>
<dd> kilobits per second (1000 bit/s)</p>
<dt>Mbps</p>
<dd> megabits per second (1000000 bit/s)</p>
<dt>Gbps</p>
<dd> gigabits per second (1000000000 bit/s) </p>
</dl>
<h2>EXAMPLES</h2>
<p> Describe all bitstreams in file.ogg: </p>
<dl>
<dt>
<dd> <tt>oggz info file.ogg</tt></dl>
<p> Describe only the Theora bitstream in file.ogv: </p>
<dl>
<dt>
<dd> <tt>oggz info -c theora file.ogv</tt></dl>
<h2>AUTHOR</h2>
<p> Conrad Parker March 10, 2005;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2005 CSIRO Australia<br />
&nbsp;<wbr></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-oggz-dump/">oggz-dump</a></code><code>(1)</code>, <code><a href="/docs/linux/man/1-oggz-rip/">oggz-rip</a></code><code>(1)</code>, <code><a href="/docs/linux/man/1-oggz-diff/">oggz-diff</a></code><code>(1)</code> <code><a href="/docs/linux/man/1-hogg/">hogg</a></code><code>(1)</code> </p>
<h2>Index</h2>
