---
title: "struct_cipher_alg(9)"
name: "struct_cipher_alg"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_cipher_alg/"
description: "struct_cipher_alg – single-block symmetric ciphers definition"
---

<p>struct_cipher_alg &#8211; single-block symmetric ciphers definition</p>
<h2>Synopsis</h2>
<pre><code>struct cipher_alg {
    unsigned int cia_min_keysize;
    unsigned int cia_max_keysize;
    int (*cia_setkey)(struct crypto_tfm *tfm, const u8 *key, unsigned int keylen);
    void (*cia_encrypt)(struct crypto_tfm *tfm, u8 *dst, const u8 *src);
    void (*cia_decrypt)(struct crypto_tfm *tfm, u8 *dst, const u8 *src);
};</code></pre>
<h2>Members</h2>
<p>cia_min_keysize</p>
<dl>
<dd>Minimum key size supported by the transformation. This is the smallest key length supported by this transformation algorithm. This must be set to one of the pre-defined values as this is not hardware specific. Possible values for this field can be found via git grep &#8220;_MIN_KEY_SIZE&#8221; include/crypto/</dl>
<p> cia_max_keysize</p>
<dl>
<dd>Maximum key size supported by the transformation. This is the largest key length supported by this transformation algorithm. This must be set to one of the pre-defined values as this is not hardware specific. Possible values for this field can be found via git grep &#8220;_MAX_KEY_SIZE&#8221; include/crypto/</dl>
<p> cia_setkey</p>
<dl>
<dd>Set key for the transformation. This function is used to either program a supplied key into the hardware or store the key in the transformation context for programming it later. Note that this function does modify the transformation context. This function can be called multiple times during the existence of the transformation object, so one must make sure the key is properly reprogrammed into the hardware. This function is also responsible for checking the key length for validity.</dl>
<p> cia_encrypt</p>
<dl>
<dd>Encrypt a single block. This function is used to encrypt a single block of data, which must be <i>cra_blocksize</i> big. This always operates on a full <i>cra_blocksize</i> and it is not possible to encrypt a block of smaller size. The supplied buffers must therefore also be at least of <i>cra_blocksize</i> size. Both the input and output buffers are always aligned to <i>cra_alignmask</i>. In case either of the input or output buffer supplied by user of the crypto API is not aligned to <i>cra_alignmask</i>, the crypto API will re-align the buffers. The re-alignment means that a new buffer will be allocated, the data will be copied into the new buffer, then the processing will happen on the new buffer, then the data will be copied back into the original buffer and finally the new buffer will be freed. In case a software fallback was put in place in the <i>cra_init</i> call, this function might need to use the fallback if the algorithm doesn&#8217;t support all of the key sizes. In case the key was stored in transformation context, the key might need to be re-programmed into the hardware in this function. This function shall not modify the transformation context, as this function may be called in parallel with the same transformation object.</dl>
<p> cia_decrypt</p>
<dl>
<dd>Decrypt a single block. This is a reverse counterpart to <i>cia_encrypt</i>, and the conditions are exactly the same.</dl>
<h2>Description</h2>
<p>All fields are mandatory and must be filled.</p>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
