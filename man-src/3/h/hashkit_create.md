---
title: "hashkit_create(3)"
name: "hashkit_create"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hashkit_create/"
description: "hashkit_create – libhashkit Documentation"
---

<h2>NAME</h2>
<p> hashkit_create &#8211; libhashkit Documentation</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libhashkit/hashkit.h&gt;</p>
<dl>
<dt><code>hashkit_st</code></p>
<dd>
<dt><i>hashkit_st</i> *hashkit_create(<i>hashkit_st</i><i>&nbsp;<wbr>*hash</i>)</p>
<dd>
<dt><i>hashkit_st</i> *hashkit_clone(<i>hashkit_st</i><i>&nbsp;<wbr>*destination</i>, const <i>hashkit_st</i><i>&nbsp;<wbr>*ptr</i>)</p>
<dd>
<dt><code>void hashkit_free(</code><i>hashkit_st</i><i>&nbsp;<wbr>*hash</i>)</p>
<dd>
<dt><code>bool hashkit_is_allocated(const </code><i>hashkit_st</i><i>&nbsp;<wbr>*hash</i>)</p>
<dd>
<p> Compile and link with -lhashkit</dl>
<h2>DESCRIPTION</h2>
<p> The <i>hashkit_create()</i> function initializes a hashkit object for use. If you pass a NULL argument for hash, then the memory for the object is allocated. If you specify a pre-allocated piece of memory, that is initialized for use. </p>
<p> The <i>hashkit_clone()</i> function initializes a hashkit object much like <i>hashkit_create()</i>, but instead of using default settings it will use the settings of the ptr hashkit object. </p>
<p> The <i>hashkit_free()</i> frees any resources being consumed by the hashkit objects that were initialized with <i>hashkit_create()</i> or <i>hashkit_clone()</i>. </p>
<p> The <i>hashkit_is_allocated()</i> reports where the memory was allocated for a hashkit object.</p>
<h2>RETURN VALUE</h2>
<p> <i>hashkit_create()</i> and <i>hashkit_clone()</i> will return NULL on failure or non-NULL on success. </p>
<p> <i>hashkit_is_allocated()</i> returns true if the memory for the hashkit object was allocated inside of <i>hashkit_create()</i> or <i>hashkit_clone()</i>, otherwise it is false and was user-supplied memory.</p>
<h2>HOME</h2>
<p> To find out more information please check: <i><a rel="nofollow" href="http://libmemcached.org/">http://libmemcached.org/</a></i></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-hashkit_create/">hashkit_create</a>(3)</i> <i><a href="/docs/linux/man/3-hashkit_value/">hashkit_value</a>(3)</i> <i><a href="/docs/linux/man/3-hashkit_set_hash_fn/">hashkit_set_hash_fn</a>(3)</i></p>
<h2>AUTHOR</h2>
<p> Brian Aker</p>
<h2>COPYRIGHT</h2>
<p> 2011-2013, Brian Aker DataDifferential, <a rel="nofollow" href="http://datadifferential.com/">http://datadifferential.com/</a> </p>
<h2>Index</h2>
