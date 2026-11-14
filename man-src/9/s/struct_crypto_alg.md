---
title: "struct_crypto_alg(9)"
name: "struct_crypto_alg"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_crypto_alg/"
description: "struct_crypto_alg – definition of a cryptograpic cipher algorithm"
---

<p>struct_crypto_alg &#8211; definition of a cryptograpic cipher algorithm</p>
<h2>Synopsis</h2>
<pre><code>struct crypto_alg {
    struct list_head cra_list;
    struct list_head cra_users;
    u32 cra_flags;
    unsigned int cra_blocksize;
    unsigned int cra_ctxsize;
    unsigned int cra_alignmask;
    int cra_priority;
    atomic_t cra_refcnt;
    char cra_name[CRYPTO_MAX_ALG_NAME];
    char cra_driver_name[CRYPTO_MAX_ALG_NAME];
    const struct crypto_type *cra_type;
    union cra_u;
    int (*cra_init)(struct crypto_tfm *tfm);
    void (*cra_exit)(struct crypto_tfm *tfm);
    void (*cra_destroy)(struct crypto_alg *alg);
    struct module *cra_module;
};</code></pre>
<h2>Members</h2>
<p>cra_list</p>
<dl>
<dd>internally used</dl>
<p> cra_users</p>
<dl>
<dd>internally used</dl>
<p> cra_flags</p>
<dl>
<dd>Flags describing this transformation. See include/linux/crypto.h CRYPTO_ALG_* flags for the flags which go in here. Those are used for fine-tuning the description of the transformation algorithm.</dl>
<p> cra_blocksize</p>
<dl>
<dd>Minimum block size of this transformation. The size in bytes of the smallest possible unit which can be transformed with this algorithm. The users must respect this value. In case of HASH transformation, it is possible for a smaller block than <i>cra_blocksize</i> to be passed to the crypto API for transformation, in case of any other transformation type, an error will be returned upon any attempt to transform smaller than <i>cra_blocksize</i> chunks.</dl>
<p> cra_ctxsize</p>
<dl>
<dd>Size of the operational context of the transformation. This value informs the kernel crypto API about the memory size needed to be allocated for the transformation context.</dl>
<p> cra_alignmask</p>
<dl>
<dd>Alignment mask for the input and output data buffer. The data buffer containing the input data for the algorithm must be aligned to this alignment mask. The data buffer for the output data must be aligned to this alignment mask. Note that the Crypto API will do the re-alignment in software, but only under special conditions and there is a performance hit. The re-alignment happens at these occasions for different <i>cra_u</i> types: cipher &#8212; For both input data and output data buffer; ahash &#8212; For output hash destination buf; shash &#8212; For output hash destination buf. This is needed on hardware which is flawed by design and cannot pick data from arbitrary addresses.</dl>
<p> cra_priority</p>
<dl>
<dd>Priority of this transformation implementation. In case multiple transformations with same <i>cra_name</i> are available to the Crypto API, the kernel will use the one with highest <i>cra_priority</i>.</dl>
<p> cra_refcnt</p>
<dl>
<dd>internally used</dl>
<p> cra_name[CRYPTO_MAX_ALG_NAME]</p>
<dl>
<dd>Generic name (usable by multiple implementations) of the transformation algorithm. This is the name of the transformation itself. This field is used by the kernel when looking up the providers of particular transformation.</dl>
<p> cra_driver_name[CRYPTO_MAX_ALG_NAME]</p>
<dl>
<dd>Unique name of the transformation provider. This is the name of the provider of the transformation. This can be any arbitrary value, but in the usual case, this contains the name of the chip or provider and the name of the transformation algorithm.</dl>
<p> cra_type</p>
<dl>
<dd>Type of the cryptographic transformation. This is a pointer to struct crypto_type, which implements callbacks common for all transformation types. There are multiple options: crypto_blkcipher_type, crypto_ablkcipher_type, crypto_ahash_type, crypto_rng_type. This field might be empty. In that case, there are no common callbacks. This is the case for: cipher, compress, shash.</dl>
<p> cra_u</p>
<dl>
<dd>Callbacks implementing the transformation. This is a union of multiple structures. Depending on the type of transformation selected by <i>cra_type</i> and <i>cra_flags</i> above, the associated structure must be filled with callbacks. This field might be empty. This is the case for ahash, shash.</dl>
<p> cra_init</p>
<dl>
<dd>Initialize the cryptographic transformation object. This function is used to initialize the cryptographic transformation object. This function is called only once at the instantiation time, right after the transformation context was allocated. In case the cryptographic hardware has some special requirements which need to be handled by software, this function shall check for the precise requirement of the transformation and put any software fallbacks in place.</dl>
<p> cra_exit</p>
<dl>
<dd>Deinitialize the cryptographic transformation object. This is a counterpart to <i>cra_init</i>, used to remove various changes set in <i>cra_init</i>.</dl>
<p> cra_destroy</p>
<dl>
<dd>internally used</dl>
<p> cra_module</p>
<dl>
<dd>Owner of this transformation implementation. Set to THIS_MODULE</dl>
<h2>Description</h2>
<p>The struct crypto_alg describes a generic Crypto API algorithm and is common for all of the transformations. Any variable not documented here shall not be used by a cipher implementation as it is internal to the Crypto API.</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
