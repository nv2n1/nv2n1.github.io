---
title: "anxrip(1)"
name: "anxrip"
section: "1"
letter: "a"
url: "/docs/linux/man/1-anxrip/"
description: "anxrip — Extract annotations and data tracks from annodexed media"
---

<h2>NAME</h2>
<p> anxrip &#8212; Extract annotations and data tracks from annodexed media<br />
&nbsp;<wbr></p>
<h2>SYNOPSIS</h2>
<p> <code>anxrip</code> [-c | &#8211;cmml ] [&#8211;head ] [-g | &#8211;granulerate ] [-m | &#8211;media ] [-o <code>filename</code> | &#8211;output <code>filename</code> ] [-h | &#8211;help ] filename</p>
<h2>Description</h2>
<p> <code>anxrip</code> extracts annotations and data tracks from annodexed media. The default behavior of <code>anxrip</code> is to extract annotations in the form of a valid CMML file.<br />
&nbsp;<wbr></p>
<h2>Options</h2>
<p> <code>anxrip</code> accepts the following options:<br />
&nbsp;<wbr></p>
<h3>CMML generation options</h3>
<dl>
<dt>-c, &#8211;cmml</p>
<dd> Extract annotations as a valid CMML file (default)<br />
&nbsp;<wbr></p>
<dt>&#8211;head</p>
<dd> Extract only the CMML head element<br />
&nbsp;<wbr></p>
<dt>-g, &#8211;granulerate</p>
<dd> Include information about media granulerates<br />
&nbsp;<wbr></dl>
<h3>Data track options</h3>
<dl>
<dt>-m, &#8211;media</p>
<dd> Extract media from annodexed media</dl>
<h3>Miscellaneous options</h3>
<dl>
<dt>-o <code>filename</code>, &#8211;output <code>filename</code></p>
<dd> Write output to the specified <code>filename</code> instead of printing it to standard output.<br />
&nbsp;<wbr></p>
<dt>-h, &#8211;help</p>
<dd> Display usage information and exit.</dl>
<h2>AUTHOR</h2>
<p> Conrad Parker November 15, 2003;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2003 CSIRO Australia<br />
&nbsp;<wbr></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-anxgrep/">anxgrep</a></code><code>(1)</code> <code><a href="/docs/linux/man/1-anxinfo/">anxinfo</a></code><code>(1)</code> <code><a href="/docs/linux/man/1-anxenc/">anxenc</a></code><code>(1)</code> </p>
<p> More information is available at <i>Annodex.net (link to URL <a rel="nofollow" href="http://www.annodex.net/)">http://www.annodex.net/)</a> </i> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> </p>
<h2>Index</h2>
