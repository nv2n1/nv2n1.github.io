---
title: "hash_futex(9)"
name: "hash_futex"
section: "9"
letter: "h"
url: "/docs/linux/man/9-hash_futex/"
description: "hash_futex – Return the hash bucket in the global hash"
---

<p>hash_futex &#8211; Return the hash bucket in the global hash</p>
<h2>Synopsis</h2>
<pre><code>struct futex_hash_bucket *hash_futex(union futex_key *key);</code></pre>
<h2>Arguments</h2>
<p><i>key</i></p>
<dl>
<dd>
<dd>Pointer to the futex key for which the hash is calculated</dl>
<h2>Description</h2>
<p>We hash on the keys returned from get_futex_key (see below) and return the corresponding hash bucket in the global hash.</p>
<h2>Author</h2>
<p><code>Rusty Russell</code> &lt;rusty [at] rustcorp.com.au&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
