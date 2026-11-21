---
title: "bson_string_truncate(3)"
name: "bson_string_truncate"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_string_truncate/"
description: "bson_string_truncate() – Truncates the string so that it is len bytes in length. This must be smaller or equal to the current length of the string."
---
<h2>NAME</h2>
<p> bson_string_truncate() - Truncates the string so that it is len bytes in length. This must be smaller or equal to the current length of the string.  </p>
<h2>SYNOPSIS</h2>
<pre><code>void
bson_string_truncate (bson_string_t *string,
                      uint32_t len);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>string</code></dt>
<dd> <p> A <code>bson_string_t</code> \&amp;. </p>
 </dd></dl>
<dl>
<dt><code>len</code></dt>
<dd> <p> The new length of the string, excluding the trailing <code>\0</code> \&amp;. </p>
 </dd></dl>
<h2>DESCRIPTION</h2>
<p> Truncates the string so that it is <code>len</code> bytes in length. This must be smaller or equal to the current length of the string. </p>
<p> A <code>\0</code> byte will be placed where the end of the string occurrs. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">SYNOPSIS</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">PARAMETERS</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">DESCRIPTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">COLOPHON</a></dt>
<dd>  </dd></dl>
