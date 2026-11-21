---

title: "bson_init_from_json(3)"
name: "bson_init_from_json"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_init_from_json/"
description: "bson_init_from_json() – The bson_init_from_json() function will initialize a new bson_t by parsing the JSON found in data. Only a single JSON object may exist in data or an error will be set and fa..."
---

<p> bson_init_from_json() - The bson_init_from_json() function will initialize a new bson_t by parsing the JSON found in data. Only a single JSON object may exist in data or an error will be set and false returned.  </p>
<h2>SYNOPSIS</h2>
<pre><code>bool
bson_init_from_json (bson_t *bson,
                     const char *data,
                     ssize_t len,
                     bson_error_t *error);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>bson</code></dt>
<dd> <p> A <code>bson_t</code> \&amp;. </p>
 </dd></dl>
<dl>
<dt><code>data</code></dt>
<dd> <p> A UTF-8 encoded string containing valid JSON. </p>
 </dd></dl>
<dl>
<dt><code>len</code></dt>
<dd> <p> The length of <code>data</code> in bytes excluding a trailing <code>\0</code> or -1 to determine the length with <code><a href="/docs/linux/man/3-strlen/">strlen</a>(3)</code> \&amp;. </p>
 </dd></dl>
<dl>
<dt><code>error</code></dt>
<dd> <p> An optional location for a <code>bson_error_t</code> \&amp;. </p>
 </dd></dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_init_from_json/">bson_init_from_json</a>(3)</code> function will initialize a new <code>bson_t</code> by parsing the JSON found in <code>data</code> \&amp;. Only a single JSON object may exist in <code>data</code> or an error will be set and false returned. </p>
<p> <code>data</code> should be in <code>MongoDB Extended JSON</code> format. </p>
<h2>ERRORS</h2>
<p> Errors are propagated via the <code>error</code> parameter. </p>
<h2>RETURNS</h2>
<p> true if successful, otherwise false and <code>error</code> is set. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
