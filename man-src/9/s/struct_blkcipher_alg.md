---
title: "struct_blkcipher_alg(9)"
name: "struct_blkcipher_alg"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_blkcipher_alg/"
description: "struct_blkcipher_alg – synchronous block cipher definition"
---

<p>struct_blkcipher_alg &#8211; synchronous block cipher definition</p>
<h2>Synopsis</h2>
<pre><code>struct blkcipher_alg {
    int (*setkey)(struct crypto_tfm *tfm, const u8 *key, unsigned int keylen);
    int (*encrypt)(struct blkcipher_desc *desc, struct scatterlist *dst, struct scatterlist *src, unsigned int nbytes);
    int (*decrypt)(struct blkcipher_desc *desc, struct scatterlist *dst, struct scatterlist *src, unsigned int nbytes);
    const char *geniv;
    unsigned int min_keysize;
    unsigned int max_keysize;
    unsigned int ivsize;
};</code></pre>
<h2>Members</h2>
<p>setkey</p>
<dl>
<dd>see struct ablkcipher_alg</dl>
<p> encrypt</p>
<dl>
<dd>see struct ablkcipher_alg</dl>
<p> decrypt</p>
<dl>
<dd>see struct ablkcipher_alg</dl>
<p> geniv</p>
<dl>
<dd>see struct ablkcipher_alg</dl>
<p> min_keysize</p>
<dl>
<dd>see struct ablkcipher_alg</dl>
<p> max_keysize</p>
<dl>
<dd>see struct ablkcipher_alg</dl>
<p> ivsize</p>
<dl>
<dd>see struct ablkcipher_alg</dl>
<h2>Description</h2>
<p>All fields except <i>geniv</i> and <i>ivsize</i> are mandatory and must be filled.</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
