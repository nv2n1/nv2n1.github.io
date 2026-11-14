---
title: "struct_ahash_alg(9)"
name: "struct_ahash_alg"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_ahash_alg/"
description: "struct_ahash_alg – asynchronous message digest definition"
---

<p>struct_ahash_alg &#8211; asynchronous message digest definition</p>
<h2>Synopsis</h2>
<pre><code>struct ahash_alg {
    int (*init)(struct ahash_request *req);
    int (*update)(struct ahash_request *req);
    int (*final)(struct ahash_request *req);
    int (*finup)(struct ahash_request *req);
    int (*digest)(struct ahash_request *req);
    int (*export)(struct ahash_request *req, void *out);
    int (*import)(struct ahash_request *req, const void *in);
    int (*setkey)(struct crypto_ahash *tfm, const u8 *key, unsigned int keylen);
    struct hash_alg_common halg;
};</code></pre>
<h2>Members</h2>
<p>init</p>
<dl>
<dd>Initialize the transformation context. Intended only to initialize the state of the HASH transformation at the beginning. This shall fill in the internal structures used during the entire duration of the whole transformation. No data processing happens at this point.</dl>
<p> update</p>
<dl>
<dd>Push a chunk of data into the driver for transformation. This function actually pushes blocks of data from upper layers into the driver, which then passes those to the hardware as seen fit. This function must not finalize the HASH transformation by calculating the final message digest as this only adds more data into the transformation. This function shall not modify the transformation context, as this function may be called in parallel with the same transformation object. Data processing can happen synchronously [SHASH] or asynchronously [AHASH] at this point.</dl>
<p> final</p>
<dl>
<dd>Retrieve result from the driver. This function finalizes the transformation and retrieves the resulting hash from the driver and pushes it back to upper layers. No data processing happens at this point.</dl>
<p> finup</p>
<dl>
<dd>Combination of <i>update</i> and <i>final</i>. This function is effectively a combination of <i>update</i> and <i>final</i> calls issued in sequence. As some hardware cannot do <i>update</i> and <i>final</i> separately, this callback was added to allow such hardware to be used at least by IPsec. Data processing can happen synchronously [SHASH] or asynchronously [AHASH] at this point.</dl>
<p> digest</p>
<dl>
<dd>Combination of <i>init</i> and <i>update</i> and <i>final</i>. This function effectively behaves as the entire chain of operations, <i>init</i>, <i>update</i> and <i>final</i> issued in sequence. Just like <i>finup</i>, this was added for hardware which cannot do even the <i>finup</i>, but can only do the whole transformation in one run. Data processing can happen synchronously [SHASH] or asynchronously [AHASH] at this point.</dl>
<p> export</p>
<dl>
<dd>Export partial state of the transformation. This function dumps the entire state of the ongoing transformation into a provided block of data so it can be <i>import</i> &#8216;ed back later on. This is useful in case you want to save partial result of the transformation after processing certain amount of data and reload this partial result multiple times later on for multiple re-use. No data processing happens at this point.</dl>
<p> import</p>
<dl>
<dd>Import partial state of the transformation. This function loads the entire state of the ongoing transformation from a provided block of data so the transformation can continue from this point onward. No data processing happens at this point.</dl>
<p> setkey</p>
<dl>
<dd>Set optional key used by the hashing algorithm. Intended to push optional key used by the hashing algorithm from upper layers into the driver. This function can store the key in the transformation context or can outright program it into the hardware. In the former case, one must be careful to program the key into the hardware at appropriate time and one must be careful that .<code>setkey</code> can be called multiple times during the existence of the transformation object. Not all hashing algorithms do implement this function as it is only needed for keyed message digests. SHAx/MDx/CRCx do NOT implement this function. HMAC(MDx)/HMAC(SHAx)/CMAC(AES) do implement this function. This function must be called before any other of the <i>init</i>, <i>update</i>, <i>final</i>, <i>finup</i>, <i>digest</i> is called. No data processing happens at this point.</dl>
<p> halg</p>
<dl>
<dd>see struct hash_alg_common</dl>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
