---
title: "bson_vsnprintf(3)"
name: "bson_vsnprintf"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_vsnprintf/"
description: "bson_vsnprintf() – Like bson_snprintf() but allows for variadic parameters."
---

<h2>NAME</h2>
<p> bson_vsnprintf() &#8211; Like bson_snprintf() but allows for variadic parameters.</p>
<h2>SYNOPSIS</h2>
<pre><code>
int bson_vsnprintf(char *str,
                   size_t size,
                   const char *format,
                   va_list ap) BSON_GNUC_PRINTF(3, 0);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>str</code></dt>
<dd> A location for the resulting string.</dd></dl>
<dl>
<dt><code>size</code></dt>
<dd> The size of str in bytes.</dd></dl>
<dl>
<dt><code>format</code></dt>
<dd> A printf style format string.</dd></dl>
<dl>
<dt><code>ap</code></dt>
<dd> A va_list of parameters for the format.</dd></dl>
<h2>DESCRIPTION</h2>
<p> Like bson_snprintf() but allows for variadic parameters. </p>
<h2>RETURNS</h2>
<p> The number of bytes written to <code>str</code> excluding the <code>
</p>
</code>
