---

title: "oggz-codecs(1)"
name: "oggz-codecs"
section: "1"
letter: "o"
url: "/docs/linux/man/1-oggz-codecs/"
description: "oggz-codecs — List codecs in one or more Ogg files and their bitstreams."
---

<h2>NAME</h2>
<p> oggz-codecs &#8212; List codecs in one or more Ogg files and their bitstreams.<br />
&nbsp;<wbr></p>
<p> <code>oggz-codecs</code> [-a | &#8211;all ] [-m | &#8211;mime ] [-1 | &#8211;one-per-line] filename &#8230; </p>
<p> <code>oggz-codecs</code> [-h | &#8211;help ] [-v | &#8211;version ]</p>
<h2>Description</h2>
<p> <code>oggz-codecs</code> displays a list of codecs found in one or more Ogg files and their bitstreams. The default comma-separated output is designed for use in an HTML5 &lt;video&gt; codecs attribute.<br />
&nbsp;<wbr></p>
<h2>Options</h2>
<p> <code>oggz-codecs</code> accepts the following options:<br />
&nbsp;<wbr></p>
<h3>Display options</h3>
<dl>
<dt>-a, &#8211;all</dt>
<dd> Display codec names multiple times if present in multiple tracks.</dd>
<dt>-m, &#8211;mime</dt>
<dd> Display MIME types rather than codec names.</dd>
<dt>-1, &#8211;one-per-line</dt>
<dd> Display one entry per line.</dd></dl>
<h3>Miscellaneous options</h3>
<dl>
<dt>-h, &#8211;help</dt>
<dd> Display usage information and exit.</dd>
<dt>-v, &#8211;version</dt>
<dd> Output version information and exit.</dd></dl>
<h2>AUTHOR</h2>
<p> Conrad Parker May 15, 2008;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2009 Annodex Association<br />
&nbsp;<wbr></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-oggz-info/">oggz-info</a></code><code>(1)</code> <code>hogg</code><code>(1)</code> </p>
