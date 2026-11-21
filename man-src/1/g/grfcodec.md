---

title: "grfcodec(1)"
name: "grfcodec"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grfcodec/"
description: "GRFCodec – A tool to convert a GRF file into graphics files and meta data, and vice versa."
---

<h2>NAME</h2>
<p> <code>GRFCodec</code> &#8211; A tool to convert a GRF file into graphics files and meta data, and vice versa.</p>
<p> <code>grfcodec</code> [-<code>sv</code> ] [-<code>d | e</code> ] [options] <i>GRF-file</i> [Directory] </p>
<p> &lt;GRF-File&gt; denotes the .GRF file you want to work on, e.g. TRG1.GRF </p>
<p> &lt;Directory&gt; is where the individual sprites should be saved. If omitted, they will default to a subdirectory called sprites/.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211; </code></dt>
<dd> Display the help message.</dd>
<dt><code>-e</code></dt>
<dd> Encode a GRF file. The <i>GRF-file</i> to pass is the file where to encode to. The source of the GRF-file, i.e. the .nfo, will be looked for in sprites/GRF-file.nfo All PCX files will be searched for relative from the location of the GRF-file.</dd>
<dt><code>-d</code></dt>
<dd> Decode a GRF file. The <i>GRF-file</i> to pass is the file to decode. The result will be in sprites/GRF-file.nfo and sprites/GRF-file.pcx</dd>
<dt><code>-s</code></dt>
<dd> Silences the progress output in interactive mode</dd>
<dt><code>-v</code></dt>
<dd> Display the version.</dd></dl>
<p> Options for decoding:</p>
<dl>
<dt><code>-w </code><i>num</i></dt>
<dd> Write PCX files with the given width (default 800, minimum 16)</dd>
<dt><code>-h </code><i>num</i></dt>
<dd> Split PCX files when they reach this height (default no limit, minimum 16)</dd>
<dt><code>-b </code><i>num</i></dt>
<dd> Organize sprites in boxes of this size (default 16)</dd>
<dt><code>-p </code><i>pal</i></dt>
<dd> Use this palette instead of the default. See &#8211;<code>p</code> ? for a list.</dd>
<dt><code>-t</code></dt>
<dd> Disable decoding of plain text characters as strings.</dd>
<dt><code>-x</code></dt>
<dd> Disable production of unquoted escape sequences.</dd>
<dt><code>-xx</code></dt>
<dd> Disable production of both quoted and unquoted escape sequences. </dd>
<p> This has the side effect of producing a version 6 .nfo, instead of a version 7 .nfo.</p>
<dt><code>-X</code></dt>
<dd> List sprite numbers in the PCX file in hex.</dd></dl>
<p> Options for encoding:</p>
<dl>
<dt><code>-c</code></dt>
<dd> Crop extraneous transparent blue from real sprites</dd>
<dt><code>-u</code></dt>
<dd> Save uncompressed data (probably not a good idea)</dd>
<dt><code>-q</code></dt>
<dd> Suppress warning messages</dd></dl>
<p> Options for both encoding and decoding:</p>
<dl>
<dt><code>-m </code><i>num</i></dt>
<dd> Apply colour translation to all sprites except character-glyphs.</dd>
<dt><code>-M </code><i>num</i></dt>
<dd> Apply colour translation to all sprites. </dd>
<p> If both of these are specified, only the last is obeyed. &#8211;<code>m</code> ? or &#8211;<code>M</code> ? for a list of colour translations.</dl>
<h2>SEE ALSO</h2>
<p> The documentation in /usr/share/doc/grfcodec/</p>
<h2>AUTHOR</h2>
<p> GRFCodec was written by Josef Drexler. </p>
<p> This manual page was written by Remko Bijker.</p>
<h2>COPYRIGHT</h2>
<p> GRFCodec is Copyright (C) 2000-2005 by Josef Drexler &lt;josef [at] ttdpatch.net&gt; </p>
