---

title: "oggz-rip(1)"
name: "oggz-rip"
section: "1"
letter: "o"
url: "/docs/linux/man/1-oggz-rip/"
description: "oggz-rip — Extract one or more logical bitstreams from an Ogg file."
---

<p> oggz-rip &#8212; Extract one or more logical bitstreams from an Ogg file.<br/>
&nbsp;<wbr></p>
<h2>SYNOPSIS</h2>
<p> <code>oggz-rip</code> [-o <code>filename</code> | &#8211;output <code>filename</code> ] filename </p>
<p> <code>oggz-rip</code> [-h | &#8211;help ] [-v | &#8211;version ]</p>
<h2>Description</h2>
<p> <code>oggz-rip</code> extracts one or more tracks from an Ogg file. In Ogg terminology, <code>oggz-rip</code> extracts one or more logical bitstreams.<br/>
&nbsp;<wbr> </p>
<p> For example, to extract just the Vorbis audio track from any Ogg file:<br/>
&nbsp;<wbr> </p>
<p> <code>oggz-rip -c vorbis input.ogx &gt; output.ogg</code> </p>
<p> This will removed any other tracks: Skeleton, Theora, image, etc. The output will be a valid Ogg Vorbis I file, suitable for use on hardware players that do not support multiplexed (ie. multi-track) Ogg files. If the input file contains multiple Vorbis, the desired once can be specified by serialno with the <code>-s</code> option. Use <code>oggz-info</code> to view the serialno of each track in a file.<br/>
&nbsp;<wbr></p>
<h2>Options</h2>
<p> <code>oggz-rip</code> accepts the following options:<br/>
&nbsp;<wbr></p>
<h3>Miscellaneous options</h3>
<dl>
<dt>-o <code>filename</code>, &#8211;output <code>filename</code></dt>
<dd> Write output to the specified <code>filename</code> instead of printing it to standard output.<br/>
&nbsp;<wbr></dd>
<dt>-h, &#8211;help</dt>
<dd> Display usage information and exit.</dd>
<dt>-v, &#8211;version</dt>
<dd> Output version information and exit.</dd></dl>
<h3>Filter options</h3>
<p> These options can be used multiple times. Pages matching ANY of the filter options will be included into the output.<br/>
&nbsp;<wbr></p>
<dl>
<dt>-s <code>serialno</code>, &#8211;serialno <code>serialno</code></dt>
<dd> Output streams with given serialno.</dd>
<dt>-i <code>index</code>, &#8211;stream-index <code>index</code></dt>
<dd> Filter by stream index. These are assigned to streams in the order of their BOS pages, starting at 0.<br/>
&nbsp;<wbr></dd>
<dt>-c <code>content-type</code> &#8211;content-type <code>content-type</code></dt>
<dd> Filter by content-type. Run <code><a href="/docs/linux/man/1-oggz-known-codecs/">oggz-known-codecs</a></code><code>(1)</code> for a full list of codecs known by the installed version of oggz. </dd>
</dl>
<h2>EXAMPLES</h2>
<p> Extract all bitstreams from file.ogg: </p>
<dl>
<dt>
</dt><dd> <tt>oggz rip -o output.ogg file.ogg</tt></dd></dl>
<p> Extract only the Theora bitstream from file.ogv: </p>
<dl>
<dt>
</dt><dd> <tt>oggz rip -c theora -o output.ogv file.ogv</tt></dd></dl>
<p>&nbsp;<wbr></p>
<h2>AUTHOR</h2>
<p> David Kuehling January 1, 2005;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2005 CSIRO Australia<br/>
&nbsp;<wbr></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-oggz-merge/">oggz-merge</a></code><code>(1)</code>, <code><a href="/docs/linux/man/1-oggz-chop/">oggz-chop</a></code><code>(1)</code>, <code><a href="/docs/linux/man/1-oggz-dump/">oggz-dump</a></code><code>(1)</code>, <code><a href="/docs/linux/man/1-oggz-diff/">oggz-diff</a></code><code>(1)</code> <code>hogg</code><code>(1)</code> </p>
