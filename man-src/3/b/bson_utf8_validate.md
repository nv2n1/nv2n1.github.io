---

title: "bson_utf8_validate(3)"
name: "bson_utf8_validate"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_utf8_validate/"
description: "bson_utf8_validate() – Validates that the content within utf8 is valid UTF-8. If allow_null is true, then embedded NULL bytes are allowed ( )."
---

<h2>NAME</h2>
<p> bson_utf8_validate() - Validates that the content within utf8 is valid UTF-8. If allow_null is true, then embedded NULL bytes are allowed (&nbsp;<wbr>).  </p>
<pre><code>bool
bson_utf8_validate (const char *utf8,
                    size_t utf8_len,
                    bool allow_null);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>utf8</code></dt>
<dd> <p> A string to verify. </p>
 </dd></dl>
<dl>
<dt><code>utf8_len</code></dt>
<dd> <p> The length of <code>utf8</code> in bytes. </p>
 </dd></dl>
<dl>
<dt><code>allow_null</code></dt>
<dd> <p> A bool indicating that embedded <code>\0</code> bytes are allowed. </p>
 </dd></dl>
<p> Validates that the content within <code>utf8</code> is valid UTF-8. If <code>allow_null</code> is <code>true</code> , then embedded NULL bytes are allowed ( <code>\0</code> ). </p>
<h2>RETURNS</h2>
<p> true if <code>utf8</code> contains valid UTF-8. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
