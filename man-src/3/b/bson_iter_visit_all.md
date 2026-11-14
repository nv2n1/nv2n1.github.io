---
title: "bson_iter_visit_all(3)"
name: "bson_iter_visit_all"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_iter_visit_all/"
description: "bson_iter_visit_all() – A convenience function to iterate all remaining fields of iter using the callback vtable provided by visitor."
---

<h2>NAME</h2>
<p> bson_iter_visit_all() &#8211; A convenience function to iterate all remaining fields of iter using the callback vtable provided by visitor.</p>
<h2>SYNOPSIS</h2>
<pre><code>
bool bson_iter_visit_all(bson_iter_t *iter,
                         const bson_visitor_t *visitor,
                         void *data);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>iter</code></p>
<dd> A <code>bson_iter_t</code> \&amp;.</dl>
<dl>
<dt><code>visitor</code></p>
<dd> A <code>bson_visitor_t</code> \&amp;.</dl>
<dl>
<dt><code>data</code></p>
<dd> Optional data for <code>visitor</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> A convenience function to iterate all remaining fields of <code>iter</code> using the callback vtable provided by <code>visitor</code> \&amp;. </p>
<h2>RETURNS</h2>
<p> true if visitation was pre-maturely stopped by a callback function. Otherwise false. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
