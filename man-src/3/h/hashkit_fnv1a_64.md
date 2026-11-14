---
title: "hashkit_fnv1a_64(3)"
name: "hashkit_fnv1a_64"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hashkit_fnv1a_64/"
description: "hashkit_fnv1a_64 – libhashkit Documentation"
---

<h2>NAME</h2>
<p> hashkit_fnv1a_64 &#8211; libhashkit Documentation </p>
<p> Various hash functions to use for calculating values for keys</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libhashkit/hashkit.h&gt;</p>
<dl>
<dt><code>uint32_t hashkit_default(const char</code><i>&nbsp;<wbr>*key</i>, size_t<i>&nbsp;<wbr>key_length</i>)</p>
<dd>
<dt><code>uint32_t hashkit_fnv1_64(const char</code><i>&nbsp;<wbr>*key</i>, size_t<i>&nbsp;<wbr>key_length</i>)</p>
<dd>
<dt><code>uint32_t hashkit_fnv1a_64(const char</code><i>&nbsp;<wbr>*key</i>, size_t<i>&nbsp;<wbr>key_length</i>)</p>
<dd>
<dt><code>uint32_t hashkit_fnv1_32(const char</code><i>&nbsp;<wbr>*key</i>, size_t<i>&nbsp;<wbr>key_length</i>)</p>
<dd>
<dt><code>uint32_t hashkit_fnv1a_32(const char</code><i>&nbsp;<wbr>*key</i>, size_t<i>&nbsp;<wbr>key_length</i>)</p>
<dd>
<dt><code>uint32_t hashkit_crc32(const char</code><i>&nbsp;<wbr>*key</i>, size_t<i>&nbsp;<wbr>key_length</i>)</p>
<dd>
<dt><code>uint32_t hashkit_hsieh(const char</code><i>&nbsp;<wbr>*key</i>, size_t<i>&nbsp;<wbr>key_length</i>)</p>
<dd>
<dt><code>uint32_t hashkit_murmur(const char</code><i>&nbsp;<wbr>*key</i>, size_t<i>&nbsp;<wbr>key_length</i>)</p>
<dd>
<dt><code>uint32_t hashkit_jenkins(const char</code><i>&nbsp;<wbr>*key</i>, size_t<i>&nbsp;<wbr>key_length</i>)</p>
<dd>
<dt><code>uint32_t hashkit_md5(const char</code><i>&nbsp;<wbr>*key</i>, size_t<i>&nbsp;<wbr>key_length</i>)</p>
<dd>
<p> Compile and link with -lhashkit</dl>
<h2>DESCRIPTION</h2>
<p> These functions generate hash values from a key using a variety of algorithms. These functions can be used standalone, or as arguments to <a href="/docs/linux/man/3-hashkit_set_hash_fn/">hashkit_set_hash_fn</a>(3) or <a href="/docs/linux/man/3-hashkit_set_continuum_hash_fn/">hashkit_set_continuum_hash_fn</a>(3). </p>
<p> The hashkit_hsieh is only available if the library is built with the appropriate flag enabled.</p>
<h2>RETURN VALUE</h2>
<p> A 32-bit hash value.</p>
<h2>HOME</h2>
<p> To find out more information please check: <i><a rel="nofollow" href="http://libmemcached.org/">http://libmemcached.org/</a></i></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-hashkit_create/">hashkit_create</a>(3)</i> <i><a href="/docs/linux/man/3-hashkit_value/">hashkit_value</a>(3)</i> <i><a href="/docs/linux/man/3-hashkit_set_hash_fn/">hashkit_set_hash_fn</a>(3)</i> <i><a href="/docs/linux/man/3-hashkit_set_continuum_hash_fn/">hashkit_set_continuum_hash_fn</a>(3)</i></p>
<h2>AUTHOR</h2>
<p> Brian Aker</p>
<h2>COPYRIGHT</h2>
<p> 2011-2013, Brian Aker DataDifferential, <a rel="nofollow" href="http://datadifferential.com/">http://datadifferential.com/</a> </p>
<h2>Index</h2>
