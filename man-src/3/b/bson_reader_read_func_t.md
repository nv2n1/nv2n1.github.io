---

title: "bson_reader_read_func_t(3)"
name: "bson_reader_read_func_t"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_reader_read_func_t/"
description: "bson_reader_read_func_t – A callback function that will be called by bson_reader_t to read the next chunk of data from the underlying opaque file descriptor."
---

<h2>NAME</h2>
<p> bson_reader_read_func_t &#8211; A callback function that will be called by bson_reader_t to read the next chunk of data from the underlying opaque file descriptor.</p>
<pre><code>
typedef ssize_t (*bson_reader_read_func_t)(void *handle,
                                           void *buf,
                                           size_t count);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>handle</code></dt>
<dd> The handle to read from.</dd></dl>
<dl>
<dt><code>buf</code></dt>
<dd> The buffer to read into.</dd></dl>
<dl>
<dt><code>count</code></dt>
<dd> The number of bytes to read.</dd></dl>
<p> A callback function that will be called by <code>bson_reader_t</code> to read the next chunk of data from the underlying opaque file descriptor. </p>
<p> This function is meant to operate similar to the <code><a href="/docs/linux/man/2-read/">read</a>(2)</code> function as part of libc on UNIX-like systems. </p>
<h2>RETURNS</h2>
<p> 0 for end of stream. </p>
<p> -1 for a failure on read. </p>
<p> A value greater than zero for the number of bytes read into <code>buf</code> \&amp;. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
