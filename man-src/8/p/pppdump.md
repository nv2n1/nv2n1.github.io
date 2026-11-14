---
title: "pppdump(8)"
name: "pppdump"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pppdump/"
description: "pppdump – convert PPP record file to readable format"
---

<p>pppdump &#8211; convert PPP record file to readable format</p>
<h2>Synopsis</h2>
<p><code>pppdump</code> [ <code>-h</code> | <code>-p</code> [ <code>-d</code> ]] [ <code>-r</code> ] [ <code>-a</code> ] [ <code>-m </code><i>mru</i> ] [ <i>file </i>&#8230; ]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</p>
<h2>Description</h2>
<p>The <code>pppdump</code> utility converts the files written using the <i>record</i> option of <code>pppd</code> into a human-readable format. If one or more filenames are specified, <code>pppdump</code> will read each in turn; otherwise it will read its standard input. In each case the result is written to standard output. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-h</code></p>
<dd>Prints the bytes sent and received in hexadecimal. If neither this option nor the <code>-p</code> option is specified, the bytes are printed as the characters themselves, with non-printing and non-ASCII characters printed as escape sequences.</p>
<dt><code>-p</code></p>
<dd>Collects the bytes sent and received into PPP packets, interpreting the async HDLC framing and escape characters and checking the FCS (frame check sequence) of each packet. The packets are printed as hex values and as characters (non-printable characters are printed as `.&#8217;).</p>
<dt><code>-d</code></p>
<dd>With the <code>-p</code> option, this option causes <code>pppdump</code> to decompress packets which have been compressed with the BSD-Compress or Deflate methods.</p>
<dt><code>-r</code></p>
<dd>Reverses the direction indicators, so that `sent&#8217; is printed for bytes or packets received, and `rcvd&#8217; is printed for bytes or packets sent.</p>
<dt><code>-a</code></p>
<dd>Prints absolute times.</p>
<dt><code>-m </code><i>mru</i></p>
<dd>Use <i>mru</i> as the MRU (maximum receive unit) for both directions of the link when checking for over-length PPP packets (with the <code>-p</code> option).</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-pppd/">pppd</a>(8) </p>
