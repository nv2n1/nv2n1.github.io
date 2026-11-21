---
title: "dumpet(1)"
name: "dumpet"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dumpet/"
description: "dumpet – dump information about bootable CDs and other similar formats"
---

<h2>NAME</h2>
<p> <code>dumpet</code> &#8211; dump information about bootable CDs and other similar formats</p>
<h2>SYNOPSIS</h2>
<p> &#8211;<code>-iso </code><i>image</i> [-<code>-dumpdisks</code> ] [-<code>-dumphex | &#8211;xml</code> ]</p>
<h2>DESCRIPTION</h2>
<p> is a tool for debugging El Torito boot images. </p>
<p> The following options are available:</p>
<dl>
<dt><code>-? , &#8211;help</code></dt>
<dd> Display help information.</dd>
<dt><code>-i , &#8211;iso </code><i>image</i></dt>
<dd> The file name of the input ISO image.</dd>
<dt><code>-d , &#8211;dumpdisks</code></dt>
<dd> Dump each El Torito boot image into a file. If &#8211;<code>-xml</code> is not given, the files will be named <i>image </i><code>.1</code> <i>image </i><code>.2</code> etc. in sequence. Otherwise, <code>BootImage</code> tags will be added to the output XML document with the content of each boot image in hexadecimal.</dd>
<dt><code>-h , &#8211;dumphex</code></dt>
<dd> Dump each El Torito structure in hexadecimal. This option has no effect if &#8211;<code>-xml</code> is given.</dd>
<dt><code>-x , &#8211;xml</code></dt>
<dd> Dump the El Torito structure to standard output as an XML document.</dd></dl>
<h2>AUTHORS</h2>
<p> An Peter Jones Aq pjones [at] redhat.com </p>
