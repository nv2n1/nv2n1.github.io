---
title: "bson_reader_tell(3)"
name: "bson_reader_tell"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_reader_tell/"
description: "bson_reader_tell() – Tells the current position within the underlying stream."
---

<h2>NAME</h2>
<p> bson_reader_tell() &#8211; Tells the current position within the underlying stream.</p>
<h2>SYNOPSIS</h2>
<pre>
off_t
bson_reader_tell (bson_reader_t *reader);
</pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>reader</code></p>
<dd> A <code>bson_reader_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> Tells the current position within the underlying stream. </p>
<h2>RETURNS</h2>
<p> -1 on failure, otherwise the offset within the underlying stream. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
