---

title: "id3convert(1)"
name: "id3convert"
section: "1"
letter: "i"
url: "/docs/linux/man/1-id3convert/"
description: "id3convert – Converts between id3v1 and id3v2 tags of an mp3 file."
---

<p> id3convert &#8211; Converts between id3v1 and id3v2 tags of an mp3 file.</p>
<h2>SYNOPSIS</h2>
<p> <code>id3convert</code> [ <i>OPTION</i> ] [ <i>FILE</i> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>Id3convert</code> converts between id3v1 and id3v2 tags of an mp3 file. Id3convert will render both types of tag by default. Only the last tag type indicated in the option list will be used. Non-rendered tags will remain unchanged in the original file. Id3convert will also parse and convert Lyrics3 v2.0 frames, but will not render them. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-1, &#8211;v1tag</code></dt>
<dd> Render only the id3v1 tag</dd>
<dt><code>-2, &#8211;v2tag</code></dt>
<dd> Render only the id3v2 tag</dd>
<dt><code>-s, &#8211;strip</code></dt>
<dd> Strip, rather than render, the tags</dd>
<dt><code>-p, &#8211;padding</code></dt>
<dd> Use padding in the tag</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> Display help and exit</dd>
<dt><code>-v, &#8211;version</code></dt>
<dd> Display version information and exit </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-id3tag/">id3tag</a>(1), <a href="/docs/linux/man/1-id3info/">id3info</a>(1), <a href="/docs/linux/man/1-id3v2/">id3v2</a>(1)</p>
<h2>AUTHOR</h2>
<p> <code>id3lib</code> was originally designed and implemented by Dirk Mahoney and is maintained by Scott Thomas Haug &lt;sth2 [at] cs.wustl.edu&gt;. Manual page written for Debian GNU/Linux by Robert Woodcock &lt;rcw [at] debian.org&gt;. </p>
