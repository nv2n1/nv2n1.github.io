---
title: "bson_snprintf(3)"
name: "bson_snprintf"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_snprintf/"
description: "bson_snprintf() – This is a portable wrapper around snprintf(). It also enforces a trailing in the resulting string."
---
<h2>NAME</h2>
<p> bson_snprintf() - This is a portable wrapper around snprintf(). It also enforces a trailing &nbsp;<wbr> in the resulting string.  </p>
<h2>SYNOPSIS</h2>
<pre><code>int
bson_snprintf (char *str,
               size_t size,
               const char *format,
               ...) BSON_GNUC_PRINTF (3, 4);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>str</code></dt>
<dd> <p> The destination buffer. </p>
 </dd></dl>
<dl>
<dt><code>size</code></dt>
<dd> <p> The size of <code>str</code> \&amp;. </p>
 </dd></dl>
<dl>
<dt><code>format</code></dt>
<dd> <p> A printf style format string. </p>
 </dd></dl>
<h2>DESCRIPTION</h2>
<p> This is a portable wrapper around <code><a href="/docs/linux/man/3-snprintf/">snprintf</a>(3)</code> \&amp;. It also enforces a trailing <code>\0</code> in the resulting string. </p>
<h2>RETURNS</h2>
<p> The number of bytes written to <code>str</code> \&amp;. </p>
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
<dt><a href="#lbAF">RETURNS</a></dt>
<dd>  </dd>
<dt><a href="#lbAG">COLOPHON</a></dt>
<dd>  </dd></dl>
