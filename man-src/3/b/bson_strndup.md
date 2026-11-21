---

title: "bson_strndup(3)"
name: "bson_strndup"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_strndup/"
description: "bson_strndup() – Allocates a new string and copies up to n_bytes from str into it. A trailing is always set."
---

<p> bson_strndup() - Allocates a new string and copies up to n_bytes from str into it. A trailing &nbsp;<wbr> is always set.  </p>
<h2>SYNOPSIS</h2>
<pre><code>char *
bson_strndup (const char *str,
              size_t n_bytes);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>str</code></dt>
<dd> <p> A string to copy. </p>
 </dd></dl>
<dl>
<dt><code>n_bytes</code></dt>
<dd> <p> A size_t. </p>
 </dd></dl>
<h2>DESCRIPTION</h2>
<p> Allocates a new string and copies up to <code>n_bytes</code> from <code>str</code> into it. A trailing <code>\0</code> is always set. </p>
<h2>RETURNS</h2>
<p> A newly allocated string that should be freed with bson_free(). </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
