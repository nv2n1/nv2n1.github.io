---
title: "struct_hash_alg_common(9)"
name: "struct_hash_alg_common"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_hash_alg_common/"
description: "struct_hash_alg_common – define properties of message digest"
---

<p>struct_hash_alg_common &#8211; define properties of message digest</p>
<h2>Synopsis</h2>
<pre><code>struct hash_alg_common {
    unsigned int digestsize;
    unsigned int statesize;
    struct crypto_alg base;
};</code></pre>
<h2>Members</h2>
<p>digestsize</p>
<dl>
<dd>Size of the result of the transformation. A buffer of this size must be available to the <i>final</i> and <i>finup</i> calls, so they can store the resulting hash into it. For various predefined sizes, search include/crypto/ using git grep _DIGEST_SIZE include/crypto.</dl>
<p> statesize</p>
<dl>
<dd>Size of the block for partial state of the transformation. A buffer of this size must be passed to the <i>export</i> function as it will save the partial state of the transformation into it. On the other side, the <i>import</i> function will load the state from a buffer of this size as well.</dl>
<p> base</p>
<dl>
<dd>Start of data structure of cipher algorithm. The common data structure of crypto_alg contains information common to all ciphers. The hash_alg_common data structure now adds the hash-specific information.</dl>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
