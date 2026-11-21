---

title: "bson_copy_to_excluding(3)"
name: "bson_copy_to_excluding"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_copy_to_excluding/"
description: "bson_copy_to_excluding() – The bson_copy_to_excluding() function shall copy all fields from src to dst except those speified by the variadic, NULL terminated list of keys starting from first_exclude."
---

<h2>NAME</h2>
<p> bson_copy_to_excluding() &#8211; The bson_copy_to_excluding() function shall copy all fields from src to dst except those speified by the variadic, NULL terminated list of keys starting from first_exclude.</p>
<pre><code>
void bson_copy_to_excluding(const bson_t *src,
                            bson_t *dst,
                            const char *first_exclude,
                            ...) BSON_GNUC_NULL_TERMINATED;
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>src</code></dt>
<dd> A <code>bson_t</code> \&amp;.</dd></dl>
<dl>
<dt><code>dst</code></dt>
<dd> A <code>bson_t</code> \&amp;.</dd></dl>
<dl>
<dt><code>first_exclude</code></dt>
<dd> The first field name to exclude.</dd></dl>
<p> The <code><a href="/docs/linux/man/3-bson_copy_to_excluding/">bson_copy_to_excluding</a>(3)</code> function shall copy all fields from <code>src</code> to <code>dst</code> except those speified by the variadic, NULL terminated list of keys starting from <code>first_exclude</code> \&amp;. </p>
<p> <code>NOTE</code></p>
<dl>
<dt>
</dt><dd> This is generally not needed except in very special situations.</dd></dl>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
