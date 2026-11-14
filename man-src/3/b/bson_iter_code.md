---
title: "bson_iter_code(3)"
name: "bson_iter_code"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_iter_code/"
description: "bson_iter_code() – This function returns the contents of a BSON_TYPE_CODE field. The length of the string is stored in length if non-NULL."
---

<h2>NAME</h2>
<p> bson_iter_code() &#8211; This function returns the contents of a BSON_TYPE_CODE field. The length of the string is stored in length if non-NULL.</p>
<h2>SYNOPSIS</h2>
<pre><code>
#define BSON_ITER_HOLDS_CODE(iter) \
    (bson_iter_type((iter)) == BSON_TYPE_CODE)
const char *
bson_iter_code(const bson_iter_t *iter,
               uint32_t *length);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>iter</code></p>
<dd> A <code>bson_iter_t</code> \&amp;.</dl>
<dl>
<dt><code>length</code></p>
<dd> A location for the length of the UTF-8 encoded string or NULL.</dl>
<h2>DESCRIPTION</h2>
<p> This function returns the contents of a BSON_TYPE_CODE field. The length of the string is stored in <code>length</code> if non-NULL. </p>
<p> It is invalid to call this function on a field that is not of type BSON_TYPE_CODE. </p>
<h2>RETURNS</h2>
<p> A UTF-8 encoded string which should not be modified or freed. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
