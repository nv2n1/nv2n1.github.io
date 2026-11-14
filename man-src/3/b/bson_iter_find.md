---
title: "bson_iter_find(3)"
name: "bson_iter_find"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_iter_find/"
description: "bson_iter_find() – The bson_iter_find()function shall advance iterto the element named keyor exhaust all elements of iter. If iteris exhausted, false is returned and itershould be considered invalid."
---

<h2>NAME</h2>
<p> bson_iter_find() &#8211; The bson_iter_find()function shall advance iterto the element named keyor exhaust all elements of iter. If iteris exhausted, false is returned and itershould be considered invalid.</p>
<h2>SYNOPSIS</h2>
<pre><code>
bool bson_iter_find(bson_iter_t *iter,
                    const char *key);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>iter</code></p>
<dd> A <code>bson_iter_t</code> \&amp;.</dl>
<dl>
<dt><code>key</code></p>
<dd> A string containing the requested key.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_iter_find/">bson_iter_find</a>(3)</code> function shall advance <code>iter</code> to the element named <code>key</code> or exhaust all elements of <code>iter</code> \&amp;. If <code>iter</code> is exhausted, false is returned and <code>iter</code> should be considered invalid. </p>
<p> <code>key</code> is case-sensitive. For a case-folded version, see <code><a href="/docs/linux/man/3-bson_iter_find_case/">bson_iter_find_case</a>(3)</code> \&amp;. </p>
<h2>RETURNS</h2>
<p> true is returned if the requested key was found. If not, <code>iter</code> was exhausted and should now be considered invalid. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
