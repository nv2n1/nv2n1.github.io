---
title: "aead_request_set_crypt(9)"
name: "aead_request_set_crypt"
section: "9"
letter: "a"
url: "/docs/linux/man/9-aead_request_set_crypt/"
description: "aead_request_set_crypt – set data buffers"
---

<p>aead_request_set_crypt &#8211; set data buffers</p>
<h2>Synopsis</h2>
<pre><code>void aead_request_set_crypt(struct aead_request *req, struct scatterlist *src, struct scatterlist *dst, unsigned int cryptlen, u8 *iv);</code></pre>
<h2>Arguments</h2>
<p><i>req</i></p>
<dl>
<dd>
<dd>request handle</dl>
<p> <i>src</i></p>
<dl>
<dd>source scatter / gather list</dl>
<p> <i>dst</i></p>
<dl>
<dd>destination scatter / gather list</dl>
<p> <i>cryptlen</i></p>
<dl>
<dd>number of bytes to process from <i>src</i></dl>
<p> <i>iv</i></p>
<dl>
<dd>IV for the cipher operation which must comply with the IV size defined by <code>crypto_aead_ivsize</code></dl>
<h2>Description</h2>
<p>Setting the source data and destination data scatter / gather lists which hold the associated data concatenated with the plaintext or ciphertext. See below for the authentication tag. For encryption, the source is treated as the plaintext and the destination is the ciphertext. For a decryption operation, the use is reversed &#8211; the source is the ciphertext and the destination is the plaintext. For both src/dst the layout is associated data, plain/cipher text, authentication tag. The content of the AD in the destination buffer after processing will either be untouched, or it will contain a copy of the AD from the source buffer. In order to ensure that it always has a copy of the AD, the user must copy the AD over either before or after processing. Of course this is not relevant if the user is doing in-place processing where src == dst. </p>
<pre><code>IMPORTANT NOTE AEAD requires an authentication tag(MAC). For decryption, the caller must concatenate the ciphertext followed by the authentication tag and provide the entire data stream to the decryption operation (i.e. the data length used for the initialization of the scatterlist and the data length for the decryption operation is identical). For encryption, however, the authentication tag is created while encrypting the data. The destination buffer must hold sufficient space for the ciphertext and the authentication tag while the encryption invocation must only point to the plaintext data size. The following code snippet illustrates the memory usage buffer = kmalloc(ptbuflen + (enc ? authsize : 0));
sg_init_one(sg, buffer, ptbuflen + (enc ? authsize : 0));
aead_request_set_crypt(req,
                       sg,
                       sg, ptbuflen, iv);</code></pre>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
