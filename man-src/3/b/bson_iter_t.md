---
title: "bson_iter_t(3)"
name: "bson_iter_t"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_iter_t/"
description: "bson_iter_t – BSON Document Iterator"
---

<h2>NAME</h2>
<p> bson_iter_t &#8211; BSON Document Iterator</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;bson.h&gt;
typedef struct
{
    /*&lt; private &gt;*/
} bson_iter_t;
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>bson_iter_t</code> is a structure used to iterate through the elements of a <code>bson_t</code> \&amp;. It is meant to be used on the stack and can be discarded at any time as it contains no external allocation. The contents of the structure should be considered private and may change between releases, however the structure size will not change. </p>
<p> The <code>bson_t</code> </p>
<p> <code>MUST</code> be valid for the lifetime of the iter and it is an error to modify the <code>bson_t</code> while using the iter. </p>
<h2>EXAMPLES</h2>
<p>bson_iter_t iter;<br />
if (bson_iter_init(&amp;iter, my_bson_doc)) {<br />
    while (bson_iter_next(&amp;iter)) {<br />
        printf(&#8220;Found a field named: %s
&#8221;, bson_iter_key(&amp;iter));<br />
    }<br />
}</p>
<p>bson_iter_t iter;<br />
if (bson_iter_init(&amp;iter, my_bson_doc) &amp;&amp;<br />
    bson_iter_find(&amp;iter, &#8220;my_field&#8221;)) {<br />
    printf(&#8220;Found the field named: %s
&#8221;, bson_iter_key(&amp;iter));<br />
}</p>
<p>bson_iter_t iter;<br />
bson_iter_t sub_iter;<br />
if (bson_iter_init_find(&amp;iter, my_bson_doc, &#8220;mysubdoc&#8221;) &amp;&amp;<br />
    (BSON_ITER_HOLDS_DOCUMENT(&amp;iter) ||<br />
     BSON_ITER_HOLDS_ARRAY(&amp;iter)) &amp;&amp;<br />
    bson_iter_recurse(&amp;iter, &amp;sub_iter)) {<br />
    while (bson_iter_next(&amp;sub_iter)) {<br />
        printf(&#8220;Found key \&#8221;%s\&#8221; in sub document.
&#8221;,<br />
               bson_iter_key(&amp;sub_iter));<br />
    }<br />
}</p>
<pre><code>
bson_iter_t iter;
if (bson_iter_init(&amp;iter, my_doc) &amp;&amp;
    bson_iter_find_descendant(&amp;iter, "a.b.c.d", &amp;sub_iter)) {
    printf("The type of a.b.c.d is: %d
",
           (int)bson_iter_type(&amp;sub_iter));
}
</code></pre>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
