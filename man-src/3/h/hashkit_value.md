---
title: "hashkit_value(3)"
name: "hashkit_value"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hashkit_value/"
description: "hashkit_value – libhashkit Documentation"
---

<h2>NAME</h2>
<p> hashkit_value &#8211; libhashkit Documentation </p>
<p> Generate a value for the given key</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libhashkit/hashkit.h&gt;</p>
<dl>
<dt><code>uint32_t hashkit_value(hashkit_st</code><i>&nbsp;<wbr>*hash</i>, const char<i>&nbsp;<wbr>*key</i>, size_t<i>&nbsp;<wbr>key_length</i>)</p>
<dd>
<p> Compile and link with -lhashkit</dl>
<h2>DESCRIPTION</h2>
<p> The <i>hashkit_value()</i> function generates a 32-bit hash value from the given key and key_length. The hash argument is an initialized hashkit object, and distribution type and hash function is used from this object while generating the value.</p>
<h2>RETURN VALUE</h2>
<p> A 32-bit hash value.</p>
<h2>HOME</h2>
<p> To find out more information please check: <i><a rel="nofollow" href="http://libmemcached.org/">http://libmemcached.org/</a></i></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-hashkit_create/">hashkit_create</a>(3)</i> <i><a href="/docs/linux/man/3-hashkit_set_distribution/">hashkit_set_distribution</a>(3)</i> <i><a href="/docs/linux/man/3-hashkit_set_hash_fn/">hashkit_set_hash_fn</a>(3)</i></p>
<h2>AUTHOR</h2>
<p> Brian Aker</p>
<h2>COPYRIGHT</h2>
<p> 2011-2013, Brian Aker DataDifferential, <a rel="nofollow" href="http://datadifferential.com/">http://datadifferential.com/</a> </p>
<h2>Index</h2>
