---
title: "bson_unichar_t(3)"
name: "bson_unichar_t"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_unichar_t/"
description: "bson_unichar_t – Unicode Character Abstraction"
---

<h2>NAME</h2>
<p> bson_unichar_t &#8211; Unicode Character Abstraction</p>
<h2>SYNOPSIS</h2>
<pre>
typedef uint32_t bson_unichar_t;
</pre>
<h2>DESCRIPTION</h2>
<p> <code>bson_unichar_t</code> provides an abstraction on a single unicode character. It is the 32-bit representation of a character. As UTF-8 can contain multi-byte characters, this should be used when iterating through UTF-8 text. </p>
<h2>EXAMPLE</h2>
<pre><code>
static void
print_each_char(const char *str)
{
    bson_unichar_t c;
    for (; *str; str = bson_utf8_next_char(str)) {
        c = bson_utf8_get_char(str);
        printf("The numberic value is %u.
", (unsigned)c);
    }
}
</code></pre>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
