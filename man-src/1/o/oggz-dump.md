---
title: "oggz-dump(1)"
name: "oggz-dump"
section: "1"
letter: "o"
url: "/docs/linux/man/1-oggz-dump/"
description: "oggz-dump — Hexdump packets of an Ogg file, or revert an Ogg file from such a hexdump"
---

<h2>NAME</h2>
<p> oggz-dump &#8212; Hexdump packets of an Ogg file, or revert an Ogg file from such a hexdump<br />
&nbsp;<wbr></p>
<h2>SYNOPSIS</h2>
<p> <code>oggz-dump</code> [-b | &#8211;binary ] [-x | &#8211;hexadecimal ] [-n | &#8211;new ] [-o <code>filename</code> | &#8211;output <code>filename</code> ] [-c <code>content-type</code> | &#8211;content-type <code>content-type</code> ] [-s <code>serialno</code> | &#8211;serialno <code>serialno</code> ] [-O | &#8211;hide-offset ] [-S | &#8211;hide-serialno ] [-G | &#8211;hide-granulepos ] [-P | &#8211;hide-packetno ] filename </p>
<p> <code>oggz-dump</code> [-r | &#8211;revert ] [-o <code>filename</code> | &#8211;output <code>filename</code> ] filename </p>
<p> <code>oggz-dump</code> [-h | &#8211;help ] [-v | &#8211;version ]</p>
<h2>Description</h2>
<p> <code>oggz-dump</code> generates a hexadecimal or binary dump of packets in an Ogg file, or creates an Ogg file from a hexadecimal oggz-dump file.<br />
&nbsp;<wbr></p>
<h2>Options</h2>
<p> <code>oggz-dump</code> accepts the following options:<br />
&nbsp;<wbr></p>
<h3>Dump format options</h3>
<dl>
<dt>-b, &#8211;binary</p>
<dd> Generate a binary dump of each packet<br />
&nbsp;<wbr></p>
<dt>-x, &#8211;hexadecimal</p>
<dd> Generate a hexadecimal dump of each packet<br />
&nbsp;<wbr></dl>
<h3>Filtering options</h3>
<dl>
<dt>-n, &#8211;new</p>
<dd> Only dump the first packet of each new logical bitstream found; for correctly formed Ogg files, this dumps only the beginning-of-stream packets.<br />
&nbsp;<wbr></p>
<dt>-c <code>content-type</code>, &#8211;content-type <code>content-type</code></p>
<dd> Dump only the logical bitstreams for a specific <code>content-type</code>. Run <code><a href="/docs/linux/man/1-oggz-known-codecs/">oggz-known-codecs</a></code><code>(1)</code> for a full list of codecs known by the installed version of oggz.<br />
&nbsp;<wbr></p>
<dt>-s <code>serialno</code>, &#8211;serialno <code>serialno</code></p>
<dd> Dump only the logical bitstream with specified <code>serialno</code>.<br />
&nbsp;<wbr></p>
<dt>-O, &#8211;hide-offset</p>
<dd> Hide the byte offset field of the preamble for each packet dumped. This is particularly useful in conjunction with <code><a href="/docs/linux/man/1-oggzdiff/">oggzdiff</a></code><code>(1)</code> when comparing Ogg bitstreams that differ only in page structure.<br />
&nbsp;<wbr></p>
<dt>-S, &#8211;hide-serialno</p>
<dd> Hide the serialno field of the preamble for each packet dumped. This is particularly useful in conjunction with <code><a href="/docs/linux/man/1-oggzdiff/">oggzdiff</a></code><code>(1)</code> when comparing Ogg bitstreams that differ only in serialno assignment.<br />
&nbsp;<wbr></p>
<dt>-G, &#8211;hide-granulepos</p>
<dd> Hide the granulepos field of the preamble for each packet dumped.<br />
&nbsp;<wbr></p>
<dt>-P, &#8211;hide-packetno</p>
<dd> Hide the packetno field of the preamble for each packet dumped.<br />
&nbsp;<wbr></dl>
<h3>Mode options</h3>
<dl>
<dt>-r, &#8211;revert</p>
<dd> Revert an oggz-dump. Generates an Ogg bitstream as prescribed in the input oggz-dump.<br />
&nbsp;<wbr></p>
<dt>
<dd> The serialno, granulepos and packetno fields of the packet preambles in the oggz-dump, as well as any bos or eos markers if present, are used to structure the packets into logical bitstreams. Hence it is advised that the original input oggz-dump not be generated with any hiding filters.<br />
&nbsp;<wbr></p>
<dt>
<dd> Only the hexadecimal data columns of the input oggz-dump are parsed when generating Ogg packet data; the printable character representation is ignored.<br />
&nbsp;<wbr></dl>
<h3>Miscellaneous options</h3>
<dl>
<dt>-o <code>filename</code>, &#8211;output <code>filename</code></p>
<dd> Write output to the specified <code>filename</code> instead of printing it to standard output.<br />
&nbsp;<wbr></p>
<dt>-h, &#8211;help</p>
<dd> Display usage information and exit.</p>
<dt>-v, &#8211;version</p>
<dd> Output version information and exit. </p>
</dl>
<h2>EXAMPLES</h2>
<p> Dump all bitstreams in file.ogg: </p>
<dl>
<dt>
<dd> <tt>oggz dump file.ogg</tt></dl>
<p> Dump only the Theora bitstream in file.ogv: </p>
<dl>
<dt>
<dd> <tt>oggz dump -c theora file.ogv</tt></dl>
<h2>AUTHOR</h2>
<p> Conrad Parker November 17, 2003;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2003 CSIRO Australia<br />
&nbsp;<wbr></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-oggz-diff/">oggz-diff</a></code><code>(1)</code>, <code><a href="/docs/linux/man/1-hogg/">hogg</a></code><code>(1)</code> <code><a href="/docs/linux/man/1-xxd/">xxd</a></code><code>(1)</code>, <code><a href="/docs/linux/man/1-hexdump/">hexdump</a></code><code>(1)</code> </p>
<h2>Index</h2>
