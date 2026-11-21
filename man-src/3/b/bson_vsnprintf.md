---
title: "bson_vsnprintf(3)"
name: "bson_vsnprintf"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_vsnprintf/"
description: "bson_vsnprintf() – Like bson_snprintf() but allows for variadic parameters."
---
<h2>NAME</h2>
<p> bson_vsnprintf() - Like bson_snprintf() but allows for variadic parameters.  </p>
<h2>SYNOPSIS</h2>
<pre><code>int
bson_vsnprintf (char *str,
                size_t size,
                const char *format,
                va_list ap) BSON_GNUC_PRINTF (3, 0);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>str</code></dt>
<dd> <p> A location for the resulting string. </p>
 </dd></dl>
<dl>
<dt><code>size</code></dt>
<dd> <p> The size of str in bytes. </p>
 </dd></dl>
<dl>
<dt><code>format</code></dt>
<dd> <p> A printf style format string. </p>
 </dd></dl>
<dl>
<dt><code>ap</code></dt>
<dd> <p> A va_list of parameters for the format. </p>
 </dd></dl>
<h2>DESCRIPTION</h2>
<p> Like bson_snprintf() but allows for variadic parameters. </p>
<h2>RETURNS</h2>
<p> The number of bytes written to <code>str</code> excluding the <code>\0</code> byte. </p>
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
