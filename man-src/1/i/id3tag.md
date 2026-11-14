---
title: "id3tag(1)"
name: "id3tag"
section: "1"
letter: "i"
url: "/docs/linux/man/1-id3tag/"
description: "id3tag – Tags an mp3 file with id3v1 and/or id3v2 tags."
---

<h2>NAME</h2>
<p> id3tag &#8211; Tags an mp3 file with id3v1 and/or id3v2 tags.</p>
<h2>SYNOPSIS</h2>
<p> <code>id3tag</code> [ <i>OPTION</i> ]<code>&#8230;</code> [ <i>FILE</i> ]<code>&#8230;</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>Id3tag</code> will render both types of tag by default. Only the last tag type indicated in the option list will be used. Non- rendered will remain unchanged in the original file. Will also parse and convert Lyrics3 v2.0 frames, but will not render them. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-1, &#8211;v1tag</code></p>
<dd> Render only the id3v1 tag</p>
<dt><code>-2, &#8211;v2tag</code></p>
<dd> Render only the id3v2 tag</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Display help and exit</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Display version information and exit</p>
<dt><code>-a, &#8211;artist ARTIST</code></p>
<dd> Set the artist information</p>
<dt><code>-s, &#8211;song SONG</code></p>
<dd> Set the song title information</p>
<dt><code>-A, &#8211;album ALBUM</code></p>
<dd> Set the album title information</p>
<dt><code>-c, &#8211;comment COMMENT</code></p>
<dd> Set the comment information</p>
<dt><code>-C, &#8211;desc DESCRIPTION</code></p>
<dd> Set the comment description</p>
<dt><code>-g, &#8211;genre num</code></p>
<dd> Set the genre number</p>
<dt><code>-y, &#8211;year num</code></p>
<dd> Set the year</p>
<dt><code>-t, &#8211;track num</code></p>
<dd> Set the track number</p>
<dt><code>-T, &#8211;total num</code></p>
<dd> Set the total number of tracks on the album </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-id3convert/">id3convert</a>(1), <a href="/docs/linux/man/1-id3info/">id3info</a>(1), <a href="/docs/linux/man/1-id3v2/">id3v2</a>(1)</p>
<h2>AUTHOR</h2>
<p> <code>id3lib</code> was originally designed and implemented by Dirk Mahoney and is maintained by Scott Thomas Haug &lt;sth2 [at] cs.wustl.edu&gt;. Manual page written for Debian GNU/Linux by Robert Woodcock &lt;rcw [at] debian.org&gt;. </p>
<h2>Index</h2>
