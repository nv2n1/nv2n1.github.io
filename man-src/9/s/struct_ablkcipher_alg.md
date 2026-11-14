---
title: "struct_ablkcipher_alg(9)"
name: "struct_ablkcipher_alg"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_ablkcipher_alg/"
description: "struct_ablkcipher_alg – asynchronous block cipher definition"
---

<p>struct_ablkcipher_alg &#8211; asynchronous block cipher definition</p>
<h2>Synopsis</h2>
<pre><code>struct ablkcipher_alg {
    int (*setkey)(struct crypto_ablkcipher *tfm, const u8 *key, unsigned int keylen);
    int (*encrypt)(struct ablkcipher_request *req);
    int (*decrypt)(struct ablkcipher_request *req);
    int (*givencrypt)(struct skcipher_givcrypt_request *req);
    int (*givdecrypt)(struct skcipher_givcrypt_request *req);
    const char *geniv;
    unsigned int min_keysize;
    unsigned int max_keysize;
    unsigned int ivsize;
};</code></pre>
<h2>Members</h2>
<p>setkey</p>
<dl>
<dd>Set key for the transformation. This function is used to either program a supplied key into the hardware or store the key in the transformation context for programming it later. Note that this function does modify the transformation context. This function can be called multiple times during the existence of the transformation object, so one must make sure the key is properly reprogrammed into the hardware. This function is also responsible for checking the key length for validity. In case a software fallback was put in place in the <i>cra_init</i> call, this function might need to use the fallback if the algorithm doesn&#8217;t support all of the key sizes.</dl>
<p> encrypt</p>
<dl>
<dd>Encrypt a scatterlist of blocks. This function is used to encrypt the supplied scatterlist containing the blocks of data. The crypto API consumer is responsible for aligning the entries of the scatterlist properly and making sure the chunks are correctly sized. In case a software fallback was put in place in the <i>cra_init</i> call, this function might need to use the fallback if the algorithm doesn&#8217;t support all of the key sizes. In case the key was stored in transformation context, the key might need to be re-programmed into the hardware in this function. This function shall not modify the transformation context, as this function may be called in parallel with the same transformation object.</dl>
<p> decrypt</p>
<dl>
<dd>Decrypt a single block. This is a reverse counterpart to <i>encrypt</i> and the conditions are exactly the same.</dl>
<p> givencrypt</p>
<dl>
<dd>Update the IV for encryption. With this function, a cipher implementation may provide the function on how to update the IV for encryption.</dl>
<p> givdecrypt</p>
<dl>
<dd>Update the IV for decryption. This is the reverse of <i>givencrypt</i> .</dl>
<p> geniv</p>
<dl>
<dd>The transformation implementation may use an &#8220;IV generator&#8221; provided by the kernel crypto API. Several use cases have a predefined approach how IVs are to be updated. For such use cases, the kernel crypto API provides ready-to-use implementations that can be referenced with this variable.</dl>
<p> min_keysize</p>
<dl>
<dd>Minimum key size supported by the transformation. This is the smallest key length supported by this transformation algorithm. This must be set to one of the pre-defined values as this is not hardware specific. Possible values for this field can be found via git grep &#8220;_MIN_KEY_SIZE&#8221; include/crypto/</dl>
<p> max_keysize</p>
<dl>
<dd>Maximum key size supported by the transformation. This is the largest key length supported by this transformation algorithm. This must be set to one of the pre-defined values as this is not hardware specific. Possible values for this field can be found via git grep &#8220;_MAX_KEY_SIZE&#8221; include/crypto/</dl>
<p> ivsize</p>
<dl>
<dd>IV size applicable for transformation. The consumer must provide an IV of exactly that size to perform the encrypt or decrypt operation.</dl>
<h2>Description</h2>
<p>All fields except <i>givencrypt</i> , <i>givdecrypt</i> , <i>geniv</i> and <i>ivsize</i> are mandatory and must be filled.</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
