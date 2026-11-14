---
title: "bson_append_regex(3)"
name: "bson_append_regex"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_append_regex/"
description: "bson_append_regex() – Appends a new field to bson of type BSON_TYPE_REGEX. regex should be the regex string. options should contain the options for the regex."
---

<h2>NAME</h2>
<p> bson_append_regex() &#8211; Appends a new field to bson of type BSON_TYPE_REGEX. regex should be the regex string. options should contain the options for the regex.</p>
<h2>SYNOPSIS</h2>
<pre><code>
bool bson_append_regex(bson_t *bson,
                       const char *key,
                       int key_length,
                       const char *regex,
                       const char *options);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>bson</code></p>
<dd> A <code>bson_t</code> \&amp;.</dl>
<dl>
<dt><code>key</code></p>
<dd> An ASCII C string containing the name of the field.</dl>
<dl>
<dt><code>key_length</code></p>
<dd> The length of <code>key</code> in bytes, or -1 to determine the length with <code><a href="/docs/linux/man/3-strlen/">strlen</a>(3)</code> \&amp;.</dl>
<dl>
<dt><code>regex</code></p>
<dd> An ASCII string containing the regex.</dl>
<dl>
<dt><code>options</code></p>
<dd> An optional string containing the regex options as a string.</dl>
<h2>DESCRIPTION</h2>
<p> Appends a new field to <code>bson</code> of type BSON_TYPE_REGEX. <code>regex</code> should be the regex string. <code>options</code> should contain the options for the regex. </p>
<p> Valid characters for <code>options</code> include: </p>
<dl>
<dt>\[bu]</p>
<dd> <code>&#8216;i&#8217;</code> for case-insensitive.</p>
<dt>\[bu]</p>
<dd> <code>&#8216;m&#8217;</code> for multiple matching.</p>
<dt>\[bu]</p>
<dd> <code>&#8216;x&#8217;</code> for verbose mode.</p>
<dt>\[bu]</p>
<dd> <code>&#8216;l&#8217;</code> to make \w and \W locale dependent.</p>
<dt>\[bu]</p>
<dd> <code>&#8216;s&#8217;</code> for dotall mode (&#8216;.&#8217; matches everything)</p>
<dt>\[bu]</p>
<dd> <code>&#8216;u&#8217;</code> to make \w and \W match unicode. </p>
</dl>
<h2>RETURNS</h2>
<p> true if the operation was applied successfully, otherwise false and <code>bson</code> should be discarded. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
