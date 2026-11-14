---
title: "bson_writer_get_length(3)"
name: "bson_writer_get_length"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_writer_get_length/"
description: "bson_writer_get_length() – Fetches the current length of the content written by the buffer (including the initial offset). This includes a partly written document currently being written."
---

<h2>NAME</h2>
<p> bson_writer_get_length() &#8211; Fetches the current length of the content written by the buffer (including the initial offset). This includes a partly written document currently being written.</p>
<h2>SYNOPSIS</h2>
<pre>
size_t
bson_writer_get_length (bson_writer_t *writer);
</pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>writer</code></p>
<dd> A <code>bson_writer_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> Fetches the current length of the content written by the buffer (including the initial offset). This includes a partly written document currently being written. </p>
<p> This is useful if you want to check to see if you&#8217;ve passed a given memory boundry that cannot be sent in a packet. See <code><a href="/docs/linux/man/3-bson_writer_rollback/">bson_writer_rollback</a>(3)</code> to abort the current document being written. </p>
<h2>RETURNS</h2>
<p> The length of the underlying buffer. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
