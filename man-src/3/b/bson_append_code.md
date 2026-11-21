---

title: "bson_append_code(3)"
name: "bson_append_code"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_append_code/"
description: "bson_append_code() – The bson_append_code() function shall append a new element to bson using the UTF-8 encoded javascript provided. javascript must be a NULL terminated C string."
---

<p> bson_append_code() &#8211; The bson_append_code() function shall append a new element to bson using the UTF-8 encoded javascript provided. javascript must be a NULL terminated C string.</p>
<h2>SYNOPSIS</h2>
<pre><code>
bool bson_append_code(bson_t *bson,
                      const char *key,
                      int key_length,
                      const char *javascript);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>bson</code></dt>
<dd> A <code>bson_t</code> \&amp;.</dd></dl>
<dl>
<dt><code>key</code></dt>
<dd> The key name.</dd></dl>
<dl>
<dt><code>key_length</code></dt>
<dd> The length of <code>key</code> or -1 to use strlen().</dd></dl>
<dl>
<dt><code>javascript</code></dt>
<dd> A UTF-8 encoded string containing the javascript.</dd></dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_append_code/">bson_append_code</a>(3)</code> function shall append a new element to <code>bson</code> using the UTF-8 encoded <code>javascript</code> provided. <code>javascript</code> must be a NULL terminated C string. </p>
<h2>RETURNS</h2>
<p> true if the operation was applied successfully, otherwise false and <code>bson</code> should be discarded. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
