---
title: "xmltvgunzip(3)"
name: "xmltvgunzip"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmltvgunzip/"
description: "XMLTV::Gunzip - Wrapper to Compress::Zlib or"
---

<pre> XMLTV::Gunzip - Wrapper to Compress::Zlib or </p><a HREF="//www.systutorials.com/docs/linux/man/1-gzip/">gzip</a>(1)</pre><h2>Synopsis</h2><pre> use XMLTV::Gunzip;
 my $decompressed = gunzip($gzdata);
 my $fh = gunzip_open('file.gz') or die;
 while (&lt;$fh&gt;) { print }</pre>Compress::Zlib will be used if installed, otherwise an external gzip will be spawned. <i>gunzip()</i> returns the decompressed data and throws an exception if things go wrong; <i>gunzip_open()</i> returns a filehandle, or undef.
<h2>Author</h2>Ed Avis, ed [at] membled.com. Distributed as part of the xmltv package.
<h2>See Also</h2>Compress::Zlib, <i><a HREF="/docs/linux/man/1-gzip/">gzip</a></i>(1), <font SIZE="-1">XMLTV</font>.
