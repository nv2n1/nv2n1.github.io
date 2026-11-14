---
title: "oggz-rip(1)"
name: "oggz-rip"
section: "1"
letter: "o"
url: "/docs/linux/man/1-oggz-rip/"
description: "oggz-rip — Extract one or more logical bitstreams from an Ogg file."
---

<h2>NAME</h2>
<p> oggz-rip &#8212; Extract one or more logical bitstreams from an Ogg file.<br />
&nbsp;<wbr></p>
<h2>SYNOPSIS</h2>
<p> <code>oggz-rip</code> [-o <code>filename</code> | &#8211;output <code>filename</code> ] filename </p>
<p> <code>oggz-rip</code> [-h | &#8211;help ] [-v | &#8211;version ]</p>
<h2>Description</h2>
<p> <code>oggz-rip</code> extracts one or more tracks from an Ogg file. In Ogg terminology, <code>oggz-rip</code> extracts one or more logical bitstreams.<br />
&nbsp;<wbr> </p>
<p> For example, to extract just the Vorbis audio track from any Ogg file:<br />
&nbsp;<wbr> </p>
<p> <code>oggz-rip -c vorbis input.ogx &gt; output.ogg</code> </p>
<p> This will removed any other tracks: Skeleton, Theora, image, etc. The output will be a valid Ogg Vorbis I file, suitable for use on hardware players that do not support multiplexed (ie. multi-track) Ogg files. If the input file contains multiple Vorbis, the desired once can be specified by serialno with the <code>-s</code> option. Use <code>oggz-info</code> to view the serialno of each track in a file.<br />
&nbsp;<wbr></p>
<h2>Options</h2>
<p> <code>oggz-rip</code> accepts the following options:<br />
&nbsp;<wbr></p>
<h3>Miscellaneous options</h3>
<dl>
<dt>-o <code>filename</code>, &#8211;output <code>filename</code></p>
<dd> Write output to the specified <code>filename</code> instead of printing it to standard output.<br />
&nbsp;<wbr></p>
<dt>-h, &#8211;help</p>
<dd> Display usage information and exit.</p>
<dt>-v, &#8211;version</p>
<dd> Output version information and exit.</dl>
<h3>Filter options</h3>
<p> These options can be used multiple times. Pages matching ANY of the filter options will be included into the output.<br />
&nbsp;<wbr></p>
<dl>
<dt>-s <code>serialno</code>, &#8211;serialno <code>serialno</code></p>
<dd> Output streams with given serialno.</p>
<dt>-i <code>index</code>, &#8211;stream-index <code>index</code></p>
<dd> Filter by stream index. These are assigned to streams in the order of their BOS pages, starting at 0.<br />
&nbsp;<wbr></p>
<dt>-c <code>content-type</code> &#8211;content-type <code>content-type</code></p>
<dd> Filter by content-type. Run <code><a href="/docs/linux/man/1-oggz-known-codecs/">oggz-known-codecs</a></code><code>(1)</code> for a full list of codecs known by the installed version of oggz. </p>
</dl>
<h2>EXAMPLES</h2>
<p> Extract all bitstreams from file.ogg: </p>
<dl>
<dt>
<dd> <tt>oggz rip -o output.ogg file.ogg</tt></dl>
<p> Extract only the Theora bitstream from file.ogv: </p>
<dl>
<dt>
<dd> <tt>oggz rip -c theora -o output.ogv file.ogv</tt></dl>
<p>&nbsp;<wbr></p>
<h2>AUTHOR</h2>
<p> David Kuehling January 1, 2005;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2005 CSIRO Australia<br />
&nbsp;<wbr></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-oggz-merge/">oggz-merge</a></code><code>(1)</code>, <code><a href="/docs/linux/man/1-oggz-chop/">oggz-chop</a></code><code>(1)</code>, <code><a href="/docs/linux/man/1-oggz-dump/">oggz-dump</a></code><code>(1)</code>, <code><a href="/docs/linux/man/1-oggz-diff/">oggz-diff</a></code><code>(1)</code> <code><a href="/docs/linux/man/1-hogg/">hogg</a></code><code>(1)</code> </p>
<h2>Index</h2>
