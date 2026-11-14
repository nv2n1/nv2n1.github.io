---
title: "single2bin(1)"
name: "single2bin"
section: "1"
letter: "s"
url: "/docs/linux/man/1-single2bin/"
description: "megatron, unhex, unbin, unsingle, hqx2bin, single2bin, macbinary – Macintosh file format transformer"
---

<h2 class="name">NAME</h2>
<p> megatron, unhex, unbin, unsingle, hqx2bin, single2bin, macbinary &#8211; Macintosh file format transformer </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>megatron</code> [<i>sourcefile</i>&#8230;]</p>
<dd> <code>unbin</code> [<i>sourcefile</i>&#8230;]</p>
<dd> <code>unhex</code> [<i>sourcefile</i>&#8230;]</p>
<dd> <code>unsingle</code> [<i>sourcefile</i>&#8230;]</p>
<dd> <code>hqx2bin</code> [<i>sourcefile</i>&#8230;]</p>
<dd> <code>single2bin</code> [<i>sourcefile</i>&#8230;]</p>
<dd> <code>macbinary</code> [<i>sourcefile</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>megatron</code></p>
<dd>is used to transform files from BinHex, MacBinary, AppleSingle, or <code>netatalk</code> style AppleDouble formats into MacBinary or <code>netatalk</code> style AppleDouble formats. The <code>netatalk</code> style AppleDouble format is the file format used by <code>afpd,</code> the <code>netatalk</code> Apple Filing Protocol (AppleShare) server. BinHex, MacBinary, and AppleSingle are commonly used formats for transferring Macintosh files between machines via email or file transfer protocols. <code>megatron</code> uses its name to determine what type of tranformation is being asked of it. </p>
<p> If <code>megatron</code> is called as <code>unhex</code> , <code>unbin</code> or <code>unsingle</code>, it tries to convert file(s) from BinHex, MacBinary, or AppleSingle into AppleDouble format. BinHex is the format most often used to send Macintosh files by e-mail. Usually these files have an extension of &quot;.hqx&quot;. MacBinary is the format most often used by terminal emulators &quot;on the fly&quot; when transferring Macintosh files in binary mode. MacBinary files often have an extension of &quot;.bin&quot;. Some Macintosh LAN-based email packages use uuencoded AppleSingle format to &quot;attach&quot; or &quot;enclose&quot; files in email. AppleSingle files don&#8217;t have a standard filename extension. </p>
<p> If <code>megatron</code> is called as <code>hqx2bin</code>, <code>single2bin</code>, or <code>macbinary</code>, it will try to convert the file(s) from BinHex, AppleSingle, or AppleDouble into MacBinary. This last translation may be useful in moving Macintosh files from your <code>afpd</code> server to some other machine when you can&#8217;t copy them from the server using a Macintosh for some reason. </p>
<p> If <code>megatron</code> is called with any other name, it uses the default translation, namely <code>unhex</code>. </p>
<p> If no source file is given, or if <i>sourcefile</i> is `<code>&#8211;</code>&#8216;, and if the conversion is from a BinHex or MacBinary file, <code>megatron</code> will read from standard input. </p>
<p> The filename used to store any output file is the filename that is encoded in the source file. MacBinary files are created with a &quot;.bin&quot; extension. In the case of conflicts, the old file is overwritten!</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-afpd/">afpd</a></code>(8) </p>
<h2>Index</h2>
