---
title: "bson_md5_append(3)"
name: "bson_md5_append"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_md5_append/"
description: "bson_md5_append() – Feeds more data into the MD5 algorithm."
---

<h2>NAME</h2>
<p> bson_md5_append() &#8211; Feeds more data into the MD5 algorithm.</p>
<h2>SYNOPSIS</h2>
<pre><code>
void bson_md5_append(bson_md5_t *pms,
                     const uint8_t *data,
                     uint32_t nbytes);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>pms</code></dt>
<dd> A <code>bson_md5_t</code> \&amp;.</dd></dl>
<dl>
<dt><code>data</code></dt>
<dd> A memory region to feed to the md5 algorithm.</dd></dl>
<dl>
<dt><code>nbytes</code></dt>
<dd> The length of <code>data</code> in bytes.</dd></dl>
<h2>DESCRIPTION</h2>
<p> Feeds more data into the MD5 algorithm. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
