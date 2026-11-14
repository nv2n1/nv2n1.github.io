---
title: "bson_json_data_reader_ingest(3)"
name: "bson_json_data_reader_ingest"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_json_data_reader_ingest/"
description: "bson_json_data_reader_ingest() – Feed data to a memory based json reader."
---

<h2>NAME</h2>
<p> bson_json_data_reader_ingest() &#8211; Feed data to a memory based json reader.</p>
<h2>SYNOPSIS</h2>
<pre><code>
void bson_json_data_reader_ingest(bson_json_reader_t *reader,
                                  const uint8_t *data,
                                  size_t len);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>reader</code></p>
<dd> A <code>bson_json_reader_t</code> \&amp;.</dl>
<dl>
<dt><code>data</code></p>
<dd> A uint8_t containing data to feed.</dl>
<dl>
<dt><code>len</code></p>
<dd> A size_t containing the length of <code>data</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> Feed data to a memory based json reader. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
