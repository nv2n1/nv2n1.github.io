---
title: "struct_akcipher_alg(9)"
name: "struct_akcipher_alg"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_akcipher_alg/"
description: "struct_akcipher_alg – generic public key algorithm"
---

<p>struct_akcipher_alg &#8211; generic public key algorithm</p>
<h2>Synopsis</h2>
<pre><code>struct akcipher_alg {
    int (*sign)(struct akcipher_request *req);
    int (*verify)(struct akcipher_request *req);
    int (*encrypt)(struct akcipher_request *req);
    int (*decrypt)(struct akcipher_request *req);
    int (*set_pub_key)(struct crypto_akcipher *tfm, const void *key, unsigned int keylen);
    int (*set_priv_key)(struct crypto_akcipher *tfm, const void *key, unsigned int keylen);
    int (*max_size)(struct crypto_akcipher *tfm);
    int (*init)(struct crypto_akcipher *tfm);
    void (*exit)(struct crypto_akcipher *tfm);
    unsigned int reqsize;
    struct crypto_alg base;
};</code></pre>
<h2>Members</h2>
<p>sign</p>
<dl>
<dd>Function performs a sign operation as defined by public key algorithm. In case of error, where the dst_len was insufficient, the req-&gt;dst_len will be updated to the size required for the operation</dl>
<p> verify</p>
<dl>
<dd>Function performs a sign operation as defined by public key algorithm. In case of error, where the dst_len was insufficient, the req-&gt;dst_len will be updated to the size required for the operation</dl>
<p> encrypt</p>
<dl>
<dd>Function performs an encrypt operation as defined by public key algorithm. In case of error, where the dst_len was insufficient, the req-&gt;dst_len will be updated to the size required for the operation</dl>
<p> decrypt</p>
<dl>
<dd>Function performs a decrypt operation as defined by public key algorithm. In case of error, where the dst_len was insufficient, the req-&gt;dst_len will be updated to the size required for the operation</dl>
<p> set_pub_key</p>
<dl>
<dd>Function invokes the algorithm specific set public key function, which knows how to decode and interpret the BER encoded public key</dl>
<p> set_priv_key</p>
<dl>
<dd>Function invokes the algorithm specific set private key function, which knows how to decode and interpret the BER encoded private key</dl>
<p> max_size</p>
<dl>
<dd>Function returns dest buffer size required for a given key.</dl>
<p> init</p>
<dl>
<dd>Initialize the cryptographic transformation object. This function is used to initialize the cryptographic transformation object. This function is called only once at the instantiation time, right after the transformation context was allocated. In case the cryptographic hardware has some special requirements which need to be handled by software, this function shall check for the precise requirement of the transformation and put any software fallbacks in place.</dl>
<p> exit</p>
<dl>
<dd>Deinitialize the cryptographic transformation object. This is a counterpart to <i>init</i>, used to remove various changes set in <i>init</i>.</dl>
<p> reqsize</p>
<dl>
<dd>Request context size required by algorithm implementation</dl>
<p> base</p>
<dl>
<dd>Common crypto API algorithm data structure</dl>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
