---
title: "bson_iter_init(3)"
name: "bson_iter_init"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_iter_init/"
description: "bson_iter_init() – The bson_iter_init() function shall initialize iter to iterate upon the BSON document bson. Upon initialization, iter is placed before the first element. Callers must call bson_i..."
---

<h2>NAME</h2>
<p> bson_iter_init() &#8211; The bson_iter_init() function shall initialize iter to iterate upon the BSON document bson. Upon initialization, iter is placed before the first element. Callers must call bson_iter_next(), bson_iter_find(), or bson_iter_find_case() to advance to an element.</p>
<h2>SYNOPSIS</h2>
<pre>
bool
bson_iter_init (bson_iter_t  *iter,
                const bson_t *bson);
</pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>iter</code></p>
<dd> A <code>bson_iter_t</code> \&amp;.</dl>
<dl>
<dt><code>bson</code></p>
<dd> A <code>bson_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_iter_init/">bson_iter_init</a>(3)</code> function shall initialize <code>iter</code> to iterate upon the BSON document <code>bson</code> \&amp;. Upon initialization, <code>iter</code> is placed before the first element. Callers must call <code><a href="/docs/linux/man/3-bson_iter_next/">bson_iter_next</a>(3)</code> , <code><a href="/docs/linux/man/3-bson_iter_find/">bson_iter_find</a>(3)</code> , or <code><a href="/docs/linux/man/3-bson_iter_find_case/">bson_iter_find_case</a>(3)</code> to advance to an element. </p>
<h2>RETURNS</h2>
<p> Returns true if the iter was successfuly initialized. </p>
<h2>EXAMPLE</h2>
<pre><code>
static void
print_doc_id(const bson_t *doc)
{
    bson_iter_t iter;
    bson_oid_t oid;
    char oidstr[25];
    if (bson_iter_init(&amp;iter, doc) &amp;&amp;
        bson_iter_find(&amp;iter, "_id") &amp;&amp;
        BSON_ITER_HOLDS_OID(&amp;iter)) {
        bson_iter_oid(&amp;iter, &amp;oid);
        bson_oid_to_string(&amp;oid, oidstr);
        printf("%s
", oidstr);
    } else {
        printf("Document is missing _id.
");
    }
}
/* alternatively */
static void
print_doc_id(const bson_t *doc)
{
    bson_iter_t iter;
    bson_oid_t oid;
    char oidstr[25];
    if (bson_iter_init_find(&amp;iter, doc, "_id") &amp;&amp;
        BSON_ITER_HOLDS_OID(&amp;iter)) {
        bson_iter_oid(&amp;iter, &amp;oid);
        bson_oid_to_string(&amp;oid, oidstr);
        printf("%s
", oidstr);
    } else {
        printf("Document is missing _id.
");
    }
}
</code></pre>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
