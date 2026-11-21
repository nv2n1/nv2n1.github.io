---
title: "bson_strnlen(3)"
name: "bson_strnlen"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_strnlen/"
description: "bson_strnlen() – A portable version of strnlen()."
---
<h2>NAME</h2>
<p> bson_strnlen() - A portable version of strnlen().  </p>
<h2>SYNOPSIS</h2>
<pre><code>size_t
bson_strnlen (const char *s,
              size_t maxlen);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>s</code></dt>
<dd> <p> A string. </p>
 </dd></dl>
<dl>
<dt><code>maxlen</code></dt>
<dd> <p> The maximum size of string to check. </p>
 </dd></dl>
<h2>DESCRIPTION</h2>
<p> A portable version of <code><a href="/docs/linux/man/3-strnlen/">strnlen</a>(3)</code> \&amp;. </p>
<h2>RETURNS</h2>
<p> The length of <code>s</code> in bytes or <code>maxlen</code> if no <code>\0</code> was found. </p>
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
