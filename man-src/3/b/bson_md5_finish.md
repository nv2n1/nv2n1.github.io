---
title: "bson_md5_finish(3)"
name: "bson_md5_finish"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_md5_finish/"
description: "bson_md5_finish() – Completes the MD5 algorithm and stores the digest in digest."
---

<h2>NAME</h2>
<p> bson_md5_finish() &#8211; Completes the MD5 algorithm and stores the digest in digest.</p>
<h2>SYNOPSIS</h2>
<pre><code>
void bson_md5_finish(bson_md5_t *pms,
                     uint8_t digest[16]);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>pms</code></p>
<dd> A <code>bson_md5_t</code> \&amp;.</dl>
<dl>
<dt><code>digest</code></p>
<dd> A location for the digest.</dl>
<h2>DESCRIPTION</h2>
<p> Completes the MD5 algorithm and stores the digest in <code>digest</code> \&amp;. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
