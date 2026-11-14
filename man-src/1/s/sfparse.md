---
title: "sfparse(1)"
name: "sfparse"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sfparse/"
description: "sfparse – string file parse"
---

<h2>NAME</h2>
<p> sfparse &#8211; string file parse </p>
<h2>SYNOPSIS</h2>
<p> <code>sfparse</code> [ <i>&#8211;utf8</i> | <i>&#8211;unicode</i> ] <i>filename</i> </p>
<h2>DESCRIPTION</h2>
<p> This tool has two different functions. When invoked with just a filename as argument, it checks that a file is a valid strings-file, which basically amounts to seeing whether the file is in proper serialized NSDictionary format (type &quot;<i>defaults plist</i>&quot; for info on this). </p>
<p> On the other hand, if one of the two options is given, no such checking is performed, but the file IS converted into the named encoding. </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;unicode</code> &#8211; convert an ASCII or UTF8 file to Unicode </p>
<p> <code>&#8211;utf8</code> &#8211; convert an ASCII or Unicode to UTF8 </p>
<h2>HISTORY</h2>
<dl>
<dt>
<dd> Written in 1999. </p>
<p> This manual page first appeared in gnustep-base 1.9.2 (March 2004). </p>
</dl>
<h2>AUTHORS</h2>
<p> <code>sfparse</code> was written by Richard Frith-Macdonald &lt;rfm [at] gnu.org&gt; </p>
<h2>Index</h2>
