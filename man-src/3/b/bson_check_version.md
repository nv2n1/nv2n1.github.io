---
title: "bson_check_version(3)"
name: "bson_check_version"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_check_version/"
description: "bson_check_version() – Check at runtime if this release of libbson meets a required version."
---

<h2>NAME</h2>
<p> bson_check_version() &#8211; Check at runtime if this release of libbson meets a required version.</p>
<h2>SYNOPSIS</h2>
<pre><code>
bool bson_check_version(int required_major,
                        int required_minor,
                        int required_micro);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>required_major</code></p>
<dd> The minimum major version required.</dl>
<dl>
<dt><code>required_minor</code></p>
<dd> The minimum minor version required.</dl>
<dl>
<dt><code>required_micro</code></p>
<dd> The minimum micro version required.</dl>
<h2>DESCRIPTION</h2>
<p> Check at runtime if this release of libbson meets a required version. </p>
<h2>RETURNS</h2>
<p> True if libbson&#8217;s version is greater than or equal to the required version. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
