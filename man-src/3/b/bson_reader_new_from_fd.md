---
title: "bson_reader_new_from_fd(3)"
name: "bson_reader_new_from_fd"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_reader_new_from_fd/"
description: "bson_reader_new_from_fd() – The bson_reader_new_from_fd() function shall create a new bson_reader_t that will read from the provided file-descriptor."
---

<h2>NAME</h2>
<p> bson_reader_new_from_fd() &#8211; The bson_reader_new_from_fd() function shall create a new bson_reader_t that will read from the provided file-descriptor.</p>
<h2>SYNOPSIS</h2>
<pre>
bson_reader_t *
bson_reader_new_from_fd (int  fd,
                         bool close_on_destroy);
</pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>fd</code></p>
<dd> A valid file-descriptor.</dl>
<dl>
<dt><code>close_on_destroy</code></p>
<dd> Whether <code><a href="/docs/linux/man/3-close/">close</a>(3)</code> should be called on <code>fd</code> when the reader is destroyed.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_reader_new_from_fd/">bson_reader_new_from_fd</a>(3)</code> function shall create a new <code>bson_reader_t</code> that will read from the provided file-descriptor. </p>
<p> fd <code>MUST</code> be in blocking mode. </p>
<p> If <code>close_fd</code> is true, then <code>fd</code> will be closed when the <code>bson_reader_t</code> is destroyed with <code><a href="/docs/linux/man/3-bson_reader_destroy/">bson_reader_destroy</a>(3)</code> \&amp;. </p>
<h2>RETURNS</h2>
<p> A newly allocated <code>bson_reader_t</code> that should be freed with <code>bson_reader_destroy</code> \&amp;. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
