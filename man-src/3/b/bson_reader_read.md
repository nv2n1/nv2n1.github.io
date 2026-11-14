---
title: "bson_reader_read(3)"
name: "bson_reader_read"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_reader_read/"
description: "bson_reader_read() – The bson_reader_read() function shall read the next document from the underlying file-descriptor or buffer."
---

<h2>NAME</h2>
<p> bson_reader_read() &#8211; The bson_reader_read() function shall read the next document from the underlying file-descriptor or buffer.</p>
<h2>SYNOPSIS</h2>
<pre>
const bson_t *
bson_reader_read (bson_reader_t *reader,
                  bool          *reached_eof);
</pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>reader</code></p>
<dd> A <code>bson_reader_t</code> \&amp;.</dl>
<dl>
<dt><code>reached_eof</code></p>
<dd> A UNKNOWN.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_reader_read/">bson_reader_read</a>(3)</code> function shall read the next document from the underlying file-descriptor or buffer. </p>
<p> If there are no further documents or a failure was detected, then NULL is returned. </p>
<p> If we reached the end of the sequence, <code>reached_eof</code> is set to true. </p>
<p> To detect an error, check for NULL and <code>reached_of</code> is false. </p>
<h2>RETURNS</h2>
<p> A <code>bson_t</code> that should not be modified or freed. </p>
<h2>EXAMPLE</h2>
<pre><code>
const bson_t *doc;
bool reached_eof = false;
while ((doc = bson_reader_read(reader, &amp;reached_eof))) {
    /* do something */
}
if (!reached_eof) {
    fprintf(stderr, "Failed to read all documents.
");
}
</code></pre>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
