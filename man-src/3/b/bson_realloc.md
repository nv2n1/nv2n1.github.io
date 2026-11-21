---

title: "bson_realloc(3)"
name: "bson_realloc"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_realloc/"
description: "bson_realloc() – This is a portable realloc() wrapper."
---

<h2>NAME</h2>
<p> bson_realloc() &#8211; This is a portable realloc() wrapper.</p>
<pre><code>
void *
bson_realloc(void *mem,
             size_t num_bytes);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>mem</code></dt>
<dd> A memory region.</dd></dl>
<dl>
<dt><code>num_bytes</code></dt>
<dd> A size_t containing the new requested size.</dd></dl>
<p> This is a portable <code><a href="/docs/linux/man/3-realloc/">realloc</a>(3)</code> wrapper. </p>
<p> In general, this function will return an allocation at least <code>sizeof(void*)</code> bytes or bigger. If <code>num_bytes</code> is 0, then the allocation will be freed. </p>
<p> If there was a failure to allocate <code>num_bytes</code> bytes, the process will be aborted. </p>
<p> <code>NOTE</code></p>
<dl>
<dt>
</dt><dd> This function will abort on failure to allocate memory.</dd></dl>
<h2>RETURNS</h2>
<p> A pointer to a memory region which <code>HAS NOT</code> been zeroed. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
