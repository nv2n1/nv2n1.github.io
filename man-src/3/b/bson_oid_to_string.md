---

title: "bson_oid_to_string(3)"
name: "bson_oid_to_string"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_oid_to_string/"
description: "bson_oid_to_string() – Converts oid into a hex encoded string."
---

<h2>NAME</h2>
<p> bson_oid_to_string() &#8211; Converts oid into a hex encoded string.</p>
<pre><code>
void bson_oid_to_string(const bson_oid_t *oid,
                        char str[25]);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>oid</code></dt>
<dd> A <code>bson_oid_t</code> \&amp;.</dd></dl>
<dl>
<dt><code>str</code></dt>
<dd> A location for the resulting string.</dd></dl>
<p> Converts <code>oid</code> into a hex encoded string. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
