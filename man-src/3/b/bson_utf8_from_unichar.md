---

title: "bson_utf8_from_unichar(3)"
name: "bson_utf8_from_unichar"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_utf8_from_unichar/"
description: "bson_utf8_from_unichar() – Converts a single unicode character to a multi-byte UTF-8 sequence. The result is stored in utf8 and the number of bytes used in len."
---

<h2>NAME</h2>
<p> bson_utf8_from_unichar() &#8211; Converts a single unicode character to a multi-byte UTF-8 sequence. The result is stored in utf8 and the number of bytes used in len.</p>
<pre><code>
void bson_utf8_from_unichar(bson_unichar_t unichar,
                            char utf8[6],
                            uint32_t *len);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>unichar</code></dt>
<dd> A <code>bson_unichar_t</code> \&amp;.</dd></dl>
<dl>
<dt><code>utf8</code></dt>
<dd> A location for the utf8 sequence.</dd></dl>
<dl>
<dt><code>len</code></dt>
<dd> A location for the number of bytes in the resulting utf8 sequence.</dd></dl>
<p> Converts a single unicode character to a multi-byte UTF-8 sequence. The result is stored in <code>utf8</code> and the number of bytes used in <code>len</code> \&amp;. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
