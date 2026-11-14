---
title: "mongoc_check_version(3)"
name: "mongoc_check_version"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_check_version/"
description: "mongoc_check_version() – None"
---

<p>mongoc_check_version() &#8211; None</p>
<h2>Synopsis</h2>
<pre>
bool
mongoc_check_version (int required_major,
                      int required_minor,
                      int required_micro);
</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>required_major</code></p>
<dd> The minimum major version required.</dl>
<dl COMPACT>
<dt><code>required_minor</code></p>
<dd> The minimum minor version required.</dl>
<dl COMPACT>
<dt><code>required_micro</code></p>
<dd> The minimum micro version required.</dl>
<h2>Returns</h2>
<p> True if libmongoc&#8217;s version is greater than or equal to the required version. </p>
<h2>Colophon</h2>
<p> This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
