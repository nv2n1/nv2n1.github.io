---
title: "pfmtopam(1)"
name: "pfmtopam"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pfmtopam/"
description: "pamtopfm – Convert PFM (Portable Float Map) image to Netpbm format"
---

<h2>NAME</h2>
<p> pamtopfm &#8211; Convert PFM (Portable Float Map) image to Netpbm format </p>
<h2>SYNOPSIS</h2>
<p> <code>pfmtopam</code> [<code>-maxval=</code><i>n</i>] [<code>-verbose</code>] [<i>imagefile</i>] </p>
<p> All options can be abbreviated to their shortest unique prefix. You may use two hyphens instead of one. You may separate an option name and its value with white space instead of an equals sign. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pfmtopam</code> reads a PFM (Portable Float Map) image and converts it to PAM. </p>
<p> See <code><a href="/docs/linux/man/1-pamtopfm/">pamtopfm</a></code>(1)<br />
&nbsp;<wbr>for a description of PFM. </p>
<p> If you want one of the older, more portable Netpbm formats, run the output through <code>pamtopnm</code>. </p>
<p> <code>pamtopfm</code> creates a PAM with tuple type &#8216;RGB&#8217; or &#8216;GRAYSCALE&#8217; depending on whether or not the PFM is in the color subformat. </p>
<p> Use <code><a href="/docs/linux/man/1-pamtopfm/">pamtopfm</a></code>(1)<br />
&nbsp;<wbr>to convert a PFM image to Netpbm format. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-maxval=</code><i>n</i></p>
<dd>
<p> This specifies the maxval for the PAM. Default is 255. </p>
<dt><code>-verbose</code></p>
<dd>
<p> This causes <code>pfmtopam</code> to display messages describing<br />
&nbsp;<wbr>&nbsp;<wbr>the PFM input file. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pamtopfm/">pamtopfm</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) , </p>
<h2>HISTORY</h2>
<p> <code>pfmtopam</code> was added to Netpbm in Release 10.22 (April 2004). </p>
<h2>Index</h2>
