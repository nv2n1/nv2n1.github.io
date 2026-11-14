---
title: "oggz-comment(1)"
name: "oggz-comment"
section: "1"
letter: "o"
url: "/docs/linux/man/1-oggz-comment/"
description: "oggz-comment — List or edit comments in an Ogg file."
---

<h2>NAME</h2>
<p> oggz-comment &#8212; List or edit comments in an Ogg file.<br />
&nbsp;<wbr></p>
<h2>SYNOPSIS</h2>
<p> <code>oggz-comment</code> [-l | &#8211;list ] </p>
<p> <code>oggz-comment</code> [-o <code>filename</code> | &#8211;output <code>filename</code> ] [-d | &#8211;delete ] [-a | &#8211;all ] [-s <code>serialno</code> | &#8211;serialno <code>serialno</code> ] [-c <code>content-type</code> | &#8211;content-type <code>content-type</code> ] filename </p>
<p> <code>oggz-comment</code> [-h | &#8211;help ] [-v | &#8211;version ]</p>
<h2>Description</h2>
<p> <code>oggz-comment</code> lists or edits the comments of an Ogg file.<br />
&nbsp;<wbr></p>
<h2>Options</h2>
<p> <code>oggz-comment</code> accepts the following options:<br />
&nbsp;<wbr></p>
<h3>Listing options</h3>
<dl>
<dt>-l, &#8211;list</p>
<dd> List the comments in the given file.</dl>
<h3>Editing options</h3>
<dl>
<dt>-o <code>filename</code>, &#8211;output <code>filename</code></p>
<dd> Write output to the specified <code>filename</code>.<br />
&nbsp;<wbr></p>
<dt>-d, &#8211;delete</p>
<dd> Delete comments before editing.</p>
<dt>-a, &#8211;all</p>
<dd> Edit comments for all logical bitstreams.</p>
<dt>-c <code>content-type</code>, &#8211;content-type <code>content-type</code></p>
<dd> Edit comments of the logical bitstreams with specified <code>content-type</code>. Run <code><a href="/docs/linux/man/1-oggz-known-codecs/">oggz-known-codecs</a></code><code>(1)</code> for a full list of codecs known by the installed version of oggz.<br />
&nbsp;<wbr></p>
<dt>-s <code>serialno</code>, &#8211;serialno <code>serialno</code></p>
<dd> Edit comments of the logical bitstream with specified <code>serialno</code>.</dl>
<h3>Miscellaneous options</h3>
<dl>
<dt>-h, &#8211;help</p>
<dd> Display usage information and exit.</p>
<dt>-v, &#8211;version</p>
<dd> Output version information and exit. </p>
</dl>
<h2>EXAMPLES</h2>
<p> List all comments in file.ogg: </p>
<dl>
<dt>
<dd> <tt>oggz comment -l file.ogg</tt></dl>
<p> List only the comments in the Theora bitstream in file.ogv: </p>
<dl>
<dt>
<dd> <tt>oggz comment -l -c theora file.ogv</tt></dl>
<p> Add the comment &quot;GENRE=Rock&quot; to the Vorbis bitstream of file.ogv, writing output to output.ogv: </p>
<dl>
<dt>
<dd> <tt>oggz comment -c vorbis -o output.ogv file.ogg GENRE=Rock</tt></dl>
<h2>AUTHOR</h2>
<p> Kangyuan Niu August 5, 2007;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2007 Annodex Association<br />
&nbsp;<wbr></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-vorbiscomment/">vorbiscomment</a></code><code>(1)</code>, <code><a href="/docs/linux/man/1-ogginfo/">ogginfo</a></code><code>(1)</code>, <code><a href="/docs/linux/man/1-oggz-info/">oggz-info</a></code><code>(1)</code>, <code><a href="/docs/linux/man/1-hogg/">hogg</a></code><code>(1)</code> </p>
<h2>Index</h2>
