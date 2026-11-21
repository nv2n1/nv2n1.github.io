---

title: "bson_json_reader_read(3)"
name: "bson_json_reader_read"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_json_reader_read/"
description: "bson_json_reader_read() – Reads the next BSON document from the underlying JSON source."
---

<h2>NAME</h2>
<p> bson_json_reader_read() &#8211; Reads the next BSON document from the underlying JSON source.</p>
<pre>
int
bson_json_reader_read (bson_json_reader_t *reader,
                       bson_t             *bson,
                       bson_error_t       *error);
</pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>reader</code></dt>
<dd> A <code>bson_json_reader_t</code> \&amp;.</dd></dl>
<dl>
<dt><code>bson</code></dt>
<dd> A <code>bson_t</code> \&amp;.</dd></dl>
<dl>
<dt><code>error</code></dt>
<dd> A <code>bson_error_t</code> \&amp;.</dd></dl>
<p> Reads the next BSON document from the underlying JSON source. </p>
<h2>ERRORS</h2>
<p> Errors are propagated via the <code>error</code> parameter. </p>
<h2>RETURNS</h2>
<p> 1 if successful and data was read. 0 if successful and no data was read. -1 if there was an error. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
