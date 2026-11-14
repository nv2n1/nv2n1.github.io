---
title: "struct_shash_alg(9)"
name: "struct_shash_alg"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_shash_alg/"
description: "struct_shash_alg – synchronous message digest definition"
---

<p>struct_shash_alg &#8211; synchronous message digest definition</p>
<h2>Synopsis</h2>
<pre><code>struct shash_alg {
    int (*init)(struct shash_desc *desc);
    int (*update)(struct shash_desc *desc, const u8 *data, unsigned int len);
    int (*final)(struct shash_desc *desc, u8 *out);
    int (*finup)(struct shash_desc *desc, const u8 *data, unsigned int len, u8 *out);
    int (*digest)(struct shash_desc *desc, const u8 *data, unsigned int len, u8 *out);
    int (*export)(struct shash_desc *desc, void *out);
    int (*import)(struct shash_desc *desc, const void *in);
    int (*setkey)(struct crypto_shash *tfm, const u8 *key, unsigned int keylen);
    unsigned int descsize;
    unsigned int digestsize;
    unsigned int statesize;
    struct crypto_alg base;
};</code></pre>
<h2>Members</h2>
<p>init</p>
<dl>
<dd>see struct ahash_alg</dl>
<p> update</p>
<dl>
<dd>see struct ahash_alg</dl>
<p> final</p>
<dl>
<dd>see struct ahash_alg</dl>
<p> finup</p>
<dl>
<dd>see struct ahash_alg</dl>
<p> digest</p>
<dl>
<dd>see struct ahash_alg</dl>
<p> export</p>
<dl>
<dd>see struct ahash_alg</dl>
<p> import</p>
<dl>
<dd>see struct ahash_alg</dl>
<p> setkey</p>
<dl>
<dd>see struct ahash_alg</dl>
<p> descsize</p>
<dl>
<dd>Size of the operational state for the message digest. This state size is the memory size that needs to be allocated for shash_desc.__ctx</dl>
<p> digestsize</p>
<dl>
<dd>see struct ahash_alg</dl>
<p> statesize</p>
<dl>
<dd>see struct ahash_alg</dl>
<p> base</p>
<dl>
<dd>internally used</dl>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
