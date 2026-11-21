---

title: "id3tag(1)"
name: "id3tag"
section: "1"
letter: "i"
url: "/docs/linux/man/1-id3tag/"
description: "id3tag – Tags an mp3 file with id3v1 and/or id3v2 tags."
---

<p> id3tag &#8211; Tags an mp3 file with id3v1 and/or id3v2 tags.</p>
<h2>SYNOPSIS</h2>
<p> <code>id3tag</code> [ <i>OPTION</i> ]<code>&#8230;</code> [ <i>FILE</i> ]<code>&#8230;</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>Id3tag</code> will render both types of tag by default. Only the last tag type indicated in the option list will be used. Non- rendered will remain unchanged in the original file. Will also parse and convert Lyrics3 v2.0 frames, but will not render them. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-1, &#8211;v1tag</code></dt>
<dd> Render only the id3v1 tag</dd>
<dt><code>-2, &#8211;v2tag</code></dt>
<dd> Render only the id3v2 tag</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> Display help and exit</dd>
<dt><code>-v, &#8211;version</code></dt>
<dd> Display version information and exit</dd>
<dt><code>-a, &#8211;artist ARTIST</code></dt>
<dd> Set the artist information</dd>
<dt><code>-s, &#8211;song SONG</code></dt>
<dd> Set the song title information</dd>
<dt><code>-A, &#8211;album ALBUM</code></dt>
<dd> Set the album title information</dd>
<dt><code>-c, &#8211;comment COMMENT</code></dt>
<dd> Set the comment information</dd>
<dt><code>-C, &#8211;desc DESCRIPTION</code></dt>
<dd> Set the comment description</dd>
<dt><code>-g, &#8211;genre num</code></dt>
<dd> Set the genre number</dd>
<dt><code>-y, &#8211;year num</code></dt>
<dd> Set the year</dd>
<dt><code>-t, &#8211;track num</code></dt>
<dd> Set the track number</dd>
<dt><code>-T, &#8211;total num</code></dt>
<dd> Set the total number of tracks on the album </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-id3convert/">id3convert</a>(1), <a href="/docs/linux/man/1-id3info/">id3info</a>(1), <a href="/docs/linux/man/1-id3v2/">id3v2</a>(1)</p>
<h2>AUTHOR</h2>
<p> <code>id3lib</code> was originally designed and implemented by Dirk Mahoney and is maintained by Scott Thomas Haug &lt;sth2 [at] cs.wustl.edu&gt;. Manual page written for Debian GNU/Linux by Robert Woodcock &lt;rcw [at] debian.org&gt;. </p>
