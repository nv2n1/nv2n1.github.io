---
title: "tinyca2(1)"
name: "tinyca2"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tinyca2/"
description: "tinyca2 – Very simple Certification Authority"
---

<h2 class="name">NAME</h2>
<p> tinyca2 &#8211; Very simple Certification Authority </p>
<h2>SYNOPSIS</h2>
<p> <code>tinyca2</code></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>tinyca2</code> command. This manual page was written for the Debian distribution because the original program does not have a manual page and was modified for Foobar Linux. </p>
<p> <code>tinyca2</code> is a very simple Certification Authority. It features a graphical interface to create Certificate Requests, sign them with the key of the Certificate Authority and export the signed certificate and the corresponding keys in various formats. </p>
<p> On first time, run with &#8211;ManageCA to create information for a new Certificate Authority.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> show program version/exit</p>
<dt><code>&#8211;ManageCA</code></p>
<dd> enable CA management options</dl>
<h2>FILES</h2>
<dl>
<dt>/etc/tinyca2/openssl.cnf</p>
<dd> Openssl configuration template for tinyca</p>
<dt>~/.TinyCA/</p>
<dd> Storage place for the different CAs</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-openssl/">openssl</a>(1).</code></p>
<h2>AUTHOR</h2>
<p> This manual page was written by Ulrich Scholler &lt;scholler [at] fnb.tu-darmstadt.de&gt;, for the Debian GNU/Linux system (but may be used by others). Modifications for Tinyca2 version 0.7.6 were done by Tuomo Soini &lt;tis [at] foobar.fi&gt; </p>
<h2>Index</h2>
