---
title: "bson_oid_t(3)"
name: "bson_oid_t"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_oid_t/"
description: "bson_oid_t – BSON ObjectID Abstraction"
---

<h2>NAME</h2>
<p> bson_oid_t &#8211; BSON ObjectID Abstraction</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;bson.h&gt;
typedef struct
{
    uint8_t bytes[12];
} bson_oid_t;
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>bson_oid_t</code> structure contains the 12-byte ObjectId notation defined by the <code>BSON ObjectID specificiation</code> \&amp;. </p>
<p> ObjectId is a 12-byte BSON type, constructed using: </p>
<dl>
<dt>\[bu]</p>
<dd> a 4-byte value representing the seconds since the Unix epoch (in Big Endian)</p>
<dt>\[bu]</p>
<dd> a 3-byte machine identifier</p>
<dt>\[bu]</p>
<dd> a 2-byte process id (Big Endian), and</p>
<dt>\[bu]</p>
<dd> a 3-byte counter (Big Endian), starting with a random value. </p>
</dl>
<h2>STRING CONVERSION</h2>
<p> You can convert an Object ID to a string using <code><a href="/docs/linux/man/3-bson_oid_to_string/">bson_oid_to_string</a>(3)</code> and back with <code><a href="/docs/linux/man/3-bson_oid_init_from_string/">bson_oid_init_from_string</a>(3)</code> \&amp;. </p>
<h2>HASHING</h2>
<p> A <code>bson_oid_t</code> can be used in hashtables using the function <code><a href="/docs/linux/man/3-bson_oid_hash/">bson_oid_hash</a>(3)</code> and <code><a href="/docs/linux/man/3-bson_oid_equal/">bson_oid_equal</a>(3)</code> \&amp;. </p>
<h2>COMPARING</h2>
<p> A <code>bson_oid_t</code> can be compared to another using <code><a href="/docs/linux/man/3-bson_oid_compare/">bson_oid_compare</a>(3)</code> for <code><a href="/docs/linux/man/3-qsort/">qsort</a>(3)</code> style comparing and <code><a href="/docs/linux/man/3-bson_oid_equal/">bson_oid_equal</a>(3)</code> for direct equality. </p>
<h2>VALIDATING</h2>
<p> You can validate that a string containing a hex-encoded ObjectID is valid using the function <code><a href="/docs/linux/man/3-bson_oid_is_valid/">bson_oid_is_valid</a>(3)</code> \&amp;. </p>
<h2>EXAMPLE</h2>
<pre><code>
#include &lt;bson.h&gt;
#include &lt;stdio.h&gt;
int main(int argc, char *argv[])
{
    bson_oid_t oid;
    char str[25];
    bson_oid_init(&amp;oid, NULL);
    bson_oid_to_string(&amp;oid, str);
    printf("%s
", str);
    if (bson_oid_is_valid(str, sizeof str)) {
        bson_oid_init_from_string(&amp;oid, str);
    }
    printf("The UNIX time was: %u
",
           (unsigned)bson_oid_get_time_t(&amp;oid));
    return 0;
}
</code></pre>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
