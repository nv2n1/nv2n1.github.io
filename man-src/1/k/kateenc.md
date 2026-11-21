---
title: "kateenc(1)"
name: "kateenc"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kateenc/"
description: "kateenc – create Kate streams from text input"
---

<h2 class="name">NAME</h2>
<p> kateenc &#8211; create Kate streams from text input</p>
<h2>SYNOPSIS</h2>
<p> <code>kateenc</code> <code>[-hVM]</code> <code>[-o </code><i>outfile</i><code>]</code> <code>[-l </code><i>language</i><code>]</code> <code>[-c </code><i>category</i><code>]</code> <code>[-s </code><i>serial</i><code>]</code> <code>[-C </code><i>tag=value</i><code>]</code> <code>[-R </code><i>threshold</i><code>]</code> <code>[-K </code><i>threshold</i><code>]</code> <code>-t </code><i>filetype</i> [ infile ] </p>
<h2>DESCRIPTION</h2>
<p> <code>kateenc</code> creates Kate streams from input files (SubRip SRT subtitles, LRC lyrics, and libkate&#8217;s custom description language). When saved to an Ogg stream (the default behavior), a Kate stream may then be merged with other Ogg streams (eg, a Theora video) using the oggz tools. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></dt>
<dd> Show command line help.</dd>
<dt><code>-V</code></dt>
<dd> Show version information.</dd>
<dt><code>-M</code></dt>
<dd> Allow simple HTML-like markup in SRT files. If this parameter is used, strings such as &quot;&lt;i&gt;&quot; will be interpreted to mean italics, rather than appear as such. Note that various players interpret a slightly different set of HTML tags, and some do not.</dd>
<dt><code>-o</code> outfile</dt>
<dd> Write the output Kate stream to the given file name (writes to stdout if not specified).</dd>
<dt><code>-l</code> language</dt>
<dd> Sets the language for the stream (default is the language specified in the input, or none).</dd>
<dt><code>-c</code> category</dt>
<dd> Sets the category for the stream (default is the category specified in the input, or none).</dd>
<dt><code>-s</code> serial</dt>
<dd> Sets the serial number for the output Kate stream (does not apply to raw streams).</dd>
<dt><code>-C</code> tag=value</dt>
<dd> Adds a comment to encode into the output Kate stream. The comment must be of the form tag=value, and comply with the Vorbis comment rules (eg, tag is composed of a particular subset of ASCII characters, and value is valid UTF-8). Note that you might have to escape or quote the comment for it to be seen as a single command line parameter.</dd>
<dt><code>-t</code> filetype</dt>
<dd> Specifies the type of the input (srt, lrc, kate)</dd>
<dt><code>-R</code> threshold</dt>
<dd> Use repeat packets, with the given threshold (in seconds). Data packets will be repeated at intervals of roughly threshold seconds, while active.</dd>
<dt><code>-K</code> threshold</dt>
<dd> Use keepalive packets, with the given threshold (in seconds). Keepalive packets will be emitted when no other packet has been emitted for roughly threshold seconds. </dd>
</dl>
<h2>EXAMPLES</h2>
<p> Create a Kate stream for Welsh subtitles from a SubRip file: </p>
<p>&nbsp;<wbr>kateenc -t srt -l cy -c SUB -o output.ogg input.srt </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-katedec/">katedec</a></code>(1), <code><a href="/docs/linux/man/1-katalyzer/">katalyzer</a></code>(1) </p>
