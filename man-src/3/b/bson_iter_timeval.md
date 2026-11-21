---

title: "bson_iter_timeval(3)"
name: "bson_iter_timeval"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_iter_timeval/"
description: "bson_iter_timeval() – The bson_iter_timeval() function shall return the number of seconds and microseconds since the UNIX epoch, as contained in the BSON_TYPE_DATE_TIME element into tv."
---

<h2>NAME</h2>
<p> bson_iter_timeval() &#8211; The bson_iter_timeval() function shall return the number of seconds and microseconds since the UNIX epoch, as contained in the BSON_TYPE_DATE_TIME element into tv.</p>
<pre><code>
void bson_iter_timeval(const bson_iter_t *iter,
                       struct timeval *tv);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>iter</code></dt>
<dd> A <code>bson_iter_t</code> \&amp;.</dd></dl>
<dl>
<dt><code>tv</code></dt>
<dd> A struct timeval.</dd></dl>
<p> The <code><a href="/docs/linux/man/3-bson_iter_timeval/">bson_iter_timeval</a>(3)</code> function shall return the number of seconds and microseconds since the UNIX epoch, as contained in the BSON_TYPE_DATE_TIME element into <code>tv</code> \&amp;. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
