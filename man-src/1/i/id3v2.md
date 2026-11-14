---
title: "id3v2(1)"
name: "id3v2"
section: "1"
letter: "i"
url: "/docs/linux/man/1-id3v2/"
description: "id3v2 – Adds/Modifies/Removes/Views id3v2 tags, converts/lists id3v1 tags"
---

<h2>NAME</h2>
<p> id3v2 &#8211; Adds/Modifies/Removes/Views id3v2 tags, converts/lists id3v1 tags</p>
<h2>SYNOPSIS</h2>
<p> <code>id3v2</code> [ <i>OPTION</i> ] [ <i>FILE</i> ] </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Display help and exit</p>
<dt><code>-f, &#8211;list-frames</code></p>
<dd> Display all possible frames for id3v2</p>
<dt><code>-L, &#8211;list-genres</code></p>
<dd> Lists all id3v1 genres</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Display version information and exit</p>
<dt><code>-l, &#8211;list</code></p>
<dd> Lists the tag(s) on the file(s)</p>
<dt><code>-R, &#8211;list-rfc822</code></p>
<dd> Lists using an rfc822-style format for output</p>
<dt><code>-d, &#8211;delete-v2</code></p>
<dd> Deletes id3v2 tags</p>
<dt><code>-s, &#8211;delete-v1</code></p>
<dd> Deletes id3v1 tags</p>
<dt><code>-D, &#8211;delete-all</code></p>
<dd>
&nbsp;<wbr>Deletes both id3v1 and id3v2 tags</p>
<dt><code>-C, &#8211;convert</code></p>
<dd>
&nbsp;<wbr>Converts id3v1 tag to id3v2</p>
<dt><code>-a, &#8211;artist ARTIST</code></p>
<dd> Set the artist information</p>
<dt><code>-A, &#8211;album ALBUM</code></p>
<dd> Set the album title information</p>
<dt><code>-t, &#8211;song SONG</code></p>
<dd> Set the song title information</p>
<dt><code>-c, &#8211;comment DESCRIPTION:COMMENT</code></p>
<dd> Set the comment information</p>
<dt><code>-g, &#8211;genre num</code></p>
<dd> Set the genre number</p>
<dt><code>-y, &#8211;year num</code></p>
<dd> Set the year</p>
<dt><code>-T, &#8211;track num/num</code></p>
<dd> Set the track number/(optional) total tracks </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-id3tag/">id3tag</a>(1), <a href="/docs/linux/man/1-id3info/">id3info</a>(1), <a href="/docs/linux/man/1-id3convert/">id3convert</a>(1)</p>
<h2>AUTHOR</h2>
<p> <code>id3v2</code> is by myers &lt;myers_carpenter [at] users.sourceforge.net&gt; with major portions used from id3lib examples. Manual page written for Debian GNU/Linux by Robert Woodcock &lt;rcw [at] debian.org&gt;. </p>
<h2>Index</h2>
