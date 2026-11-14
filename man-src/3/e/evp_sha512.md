---
title: "evp_sha512(3)"
name: "evp_sha512"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evp_sha512/"
description: "EVP generic crypto functions –"
---

<p>EVP generic crypto functions &#8211; </p>
<h3>Functions</h3>
<p>const EVP_CIPHER * <code>EVP_wincrypt_des_ede3_cbc</code> (void) </p>
<p> const EVP_CIPHER * <code>EVP_hcrypto_aes_128_cbc</code> (void) </p>
<p> const EVP_CIPHER * <code>EVP_hcrypto_aes_192_cbc</code> (void) </p>
<p> const EVP_CIPHER * <code>EVP_hcrypto_aes_256_cbc</code> (void) </p>
<p> const EVP_CIPHER * <code>EVP_hcrypto_aes_128_cfb8</code> (void) </p>
<p> const EVP_CIPHER * <code>EVP_hcrypto_aes_192_cfb8</code> (void) </p>
<p> const EVP_CIPHER * <code>EVP_hcrypto_aes_256_cfb8</code> (void) </p>
<p> const EVP_MD * <code>EVP_hcrypto_sha256</code> (void) </p>
<p> const EVP_MD * <code>EVP_hcrypto_sha384</code> (void) </p>
<p> const EVP_MD * <code>EVP_hcrypto_sha512</code> (void) </p>
<p> const EVP_MD * <code>EVP_hcrypto_sha1</code> (void) </p>
<p> const EVP_MD * <code>EVP_hcrypto_md5</code> (void) </p>
<p> const EVP_MD * <code>EVP_hcrypto_md4</code> (void) </p>
<p> const EVP_MD * <code>EVP_hcrypto_md2</code> (void) </p>
<p> const EVP_CIPHER * <code>EVP_hcrypto_des_cbc</code> (void) </p>
<p> const EVP_CIPHER * <code>EVP_hcrypto_des_ede3_cbc</code> (void) </p>
<p> const EVP_CIPHER * <code>EVP_hcrypto_rc2_cbc</code> (void) </p>
<p> const EVP_CIPHER * <code>EVP_hcrypto_rc2_40_cbc</code> (void) </p>
<p> const EVP_CIPHER * <code>EVP_hcrypto_rc2_64_cbc</code> (void) </p>
<p> const EVP_CIPHER * <code>EVP_hcrypto_camellia_128_cbc</code> (void) </p>
<p> const EVP_CIPHER * <code>EVP_hcrypto_camellia_192_cbc</code> (void) </p>
<p> const EVP_CIPHER * <code>EVP_hcrypto_camellia_256_cbc</code> (void) </p>
<p> size_t <code>EVP_MD_size</code> (const EVP_MD *md) </p>
<p> size_t <code>EVP_MD_block_size</code> (const EVP_MD *md) </p>
<p> EVP_MD_CTX * <code>EVP_MD_CTX_create</code> (void) </p>
<p> void <code>EVP_MD_CTX_init</code> (EVP_MD_CTX *ctx) HC_DEPRECATED </p>
<p> void <code>EVP_MD_CTX_destroy</code> (EVP_MD_CTX *ctx) </p>
<p> int <code>EVP_MD_CTX_cleanup</code> (EVP_MD_CTX *ctx) HC_DEPRECATED </p>
<p> const EVP_MD * <code>EVP_MD_CTX_md</code> (EVP_MD_CTX *ctx) </p>
<p> size_t <code>EVP_MD_CTX_size</code> (EVP_MD_CTX *ctx) </p>
<p> size_t <code>EVP_MD_CTX_block_size</code> (EVP_MD_CTX *ctx) </p>
<p> int <code>EVP_DigestInit_ex</code> (EVP_MD_CTX *ctx, const EVP_MD *md, ENGINE *engine) </p>
<p> int <code>EVP_DigestUpdate</code> (EVP_MD_CTX *ctx, const void *data, size_t size) </p>
<p> int <code>EVP_DigestFinal_ex</code> (EVP_MD_CTX *ctx, void *hash, unsigned int *size) </p>
<p> int <code>EVP_Digest</code> (const void *data, size_t dsize, void *hash, unsigned int *hsize, const EVP_MD *md, ENGINE *engine) </p>
<p> const EVP_MD * <code>EVP_sha256</code> (void) </p>
<p> const EVP_MD * <code>EVP_sha384</code> (void) </p>
<p> const EVP_MD * <code>EVP_sha512</code> (void) </p>
<p> const EVP_MD * <code>EVP_sha1</code> (void) </p>
<p> const EVP_MD * <code>EVP_sha</code> (void) </p>
<p> const EVP_MD * <code>EVP_md5</code> (void) </p>
<p> const EVP_MD * <code>EVP_md4</code> (void) </p>
<p> const EVP_MD * <code>EVP_md2</code> (void) </p>
<p> const EVP_MD * <code>EVP_md_null</code> (void) </p>
<p> size_t <code>EVP_CIPHER_block_size</code> (const EVP_CIPHER *c) </p>
<p> size_t <code>EVP_CIPHER_key_length</code> (const EVP_CIPHER *c) </p>
<p> size_t <code>EVP_CIPHER_iv_length</code> (const EVP_CIPHER *c) </p>
<p> void <code>EVP_CIPHER_CTX_init</code> (EVP_CIPHER_CTX *c) </p>
<p> int <code>EVP_CIPHER_CTX_cleanup</code> (EVP_CIPHER_CTX *c) </p>
<p> int <code>EVP_CIPHER_CTX_set_key_length</code> (EVP_CIPHER_CTX *c, int length) </p>
<p> const EVP_CIPHER * <code>EVP_CIPHER_CTX_cipher</code> (EVP_CIPHER_CTX *ctx) </p>
<p> size_t <code>EVP_CIPHER_CTX_block_size</code> (const EVP_CIPHER_CTX *ctx) </p>
<p> size_t <code>EVP_CIPHER_CTX_key_length</code> (const EVP_CIPHER_CTX *ctx) </p>
<p> size_t <code>EVP_CIPHER_CTX_iv_length</code> (const EVP_CIPHER_CTX *ctx) </p>
<p> unsigned long <code>EVP_CIPHER_CTX_flags</code> (const EVP_CIPHER_CTX *ctx) </p>
<p> int <code>EVP_CIPHER_CTX_mode</code> (const EVP_CIPHER_CTX *ctx) </p>
<p> void * <code>EVP_CIPHER_CTX_get_app_data</code> (EVP_CIPHER_CTX *ctx) </p>
<p> void <code>EVP_CIPHER_CTX_set_app_data</code> (EVP_CIPHER_CTX *ctx, void *data) </p>
<p> int <code>EVP_CipherInit_ex</code> (EVP_CIPHER_CTX *ctx, const EVP_CIPHER *c, ENGINE *engine, const void *key, const void *iv, int encp) </p>
<p> int <code>EVP_CipherUpdate</code> (EVP_CIPHER_CTX *ctx, void *out, int *outlen, void *in, size_t inlen) </p>
<p> int <code>EVP_CipherFinal_ex</code> (EVP_CIPHER_CTX *ctx, void *out, int *outlen) </p>
<p> const EVP_CIPHER * <code>EVP_enc_null</code> (void) </p>
<p> const EVP_CIPHER * <code>EVP_rc2_cbc</code> (void) </p>
<p> const EVP_CIPHER * <code>EVP_rc2_40_cbc</code> (void) </p>
<p> const EVP_CIPHER * <code>EVP_rc2_64_cbc</code> (void) </p>
<p> const EVP_CIPHER * <code>EVP_rc4</code> (void) </p>
<p> const EVP_CIPHER * <code>EVP_rc4_40</code> (void) </p>
<p> const EVP_CIPHER * <code>EVP_des_cbc</code> (void) </p>
<p> const EVP_CIPHER * <code>EVP_des_ede3_cbc</code> (void) </p>
<p> const EVP_CIPHER * <code>EVP_aes_128_cbc</code> (void) </p>
<p> const EVP_CIPHER * <code>EVP_aes_192_cbc</code> (void) </p>
<p> const EVP_CIPHER * <code>EVP_aes_256_cbc</code> (void) </p>
<p> const EVP_CIPHER * <code>EVP_aes_128_cfb8</code> (void) </p>
<p> const EVP_CIPHER * <code>EVP_aes_192_cfb8</code> (void) </p>
<p> const EVP_CIPHER * <code>EVP_aes_256_cfb8</code> (void) </p>
<p> const EVP_CIPHER * <code>EVP_camellia_128_cbc</code> (void) </p>
<p> const EVP_CIPHER * <code>EVP_camellia_192_cbc</code> (void) </p>
<p> const EVP_CIPHER * <code>EVP_camellia_256_cbc</code> (void) </p>
<p> const EVP_CIPHER * <code>EVP_get_cipherbyname</code> (const char *name) </p>
<p> int <code>EVP_BytesToKey</code> (const EVP_CIPHER *type, const EVP_MD *md, const void *salt, const void *data, size_t datalen, unsigned int count, void *keydata, void *ivdata) </p>
<h2>Detailed Description</h2>
<p>See the <code>EVP &#8211; generic crypto interface</code> for description and examples.</p>
<h2>Function Documentation</h2>
<h3>const EVP_CIPHER* EVP_aes_128_cbc (void)</h3>
<p>The AES-128 cipher type </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the AES-128 EVP_CIPHER pointer.</dl>
<p> <code>Examples: </code> <code>example_evp_cipher.c</code>.</p>
<h3>const EVP_CIPHER* EVP_aes_128_cfb8 (void)</h3>
<p>The AES-128 cipher type </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the AES-128 EVP_CIPHER pointer.</dl>
<h3>const EVP_CIPHER* EVP_aes_192_cbc (void)</h3>
<p>The AES-192 cipher type </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the AES-192 EVP_CIPHER pointer.</dl>
<h3>const EVP_CIPHER* EVP_aes_192_cfb8 (void)</h3>
<p>The AES-192 cipher type </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the AES-192 EVP_CIPHER pointer.</dl>
<h3>const EVP_CIPHER* EVP_aes_256_cbc (void)</h3>
<p>The AES-256 cipher type </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the AES-256 EVP_CIPHER pointer.</dl>
<h3>const EVP_CIPHER* EVP_aes_256_cfb8 (void)</h3>
<p>The AES-256 cipher type </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the AES-256 EVP_CIPHER pointer.</dl>
<h3>int EVP_BytesToKey (const EVP_CIPHER *type, const EVP_MD *md, const void *salt, const void *data, size_tdatalen, unsigned intcount, void *keydata, void *ivdata)</h3>
<p>Provides a legancy string to key function, used in PEM files. </p>
<p> New protocols should use new string to key functions like NIST SP56-800A or PKCS#5 v2.0 (see <code>PKCS5_PBKDF2_HMAC_SHA1()</code>). </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>type</i> type of cipher to use<br />
 <i>md</i> message digest to use<br />
 <i>salt</i> salt salt string, should be an binary 8 byte buffer.<br />
 <i>data</i> the password/input key string.<br />
 <i>datalen</i> length of data parameter.<br />
 <i>count</i> iteration counter.<br />
 <i>keydata</i> output keydata, needs to of the size <code>EVP_CIPHER_key_length()</code>.<br />
 <i>ivdata</i> output ivdata, needs to of the size <code>EVP_CIPHER_block_size()</code>.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the size of derived key.</dl>
<h3>const EVP_CIPHER* EVP_camellia_128_cbc (void)</h3>
<p>The Camellia-128 cipher type </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the Camellia-128 EVP_CIPHER pointer.</dl>
<h3>const EVP_CIPHER* EVP_camellia_192_cbc (void)</h3>
<p>The Camellia-198 cipher type </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the Camellia-198 EVP_CIPHER pointer.</dl>
<h3>const EVP_CIPHER* EVP_camellia_256_cbc (void)</h3>
<p>The Camellia-256 cipher type </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the Camellia-256 EVP_CIPHER pointer.</dl>
<h3>size_t EVP_CIPHER_block_size (const EVP_CIPHER *c)</h3>
<p>Return the block size of the cipher. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>c</i> cipher to get the block size from.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the block size of the cipher.</dl>
<p> <code>Examples: </code> <code>example_evp_cipher.c</code>.</p>
<h3>size_t EVP_CIPHER_CTX_block_size (const EVP_CIPHER_CTX *ctx)</h3>
<p>Return the block size of the cipher context. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> cipher context to get the block size from.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the block size of the cipher context.</dl>
<h3>const EVP_CIPHER* EVP_CIPHER_CTX_cipher (EVP_CIPHER_CTX *ctx)</h3>
<p>Return the EVP_CIPHER for a EVP_CIPHER_CTX context. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> the context to get the cipher type from.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the EVP_CIPHER pointer.</dl>
<h3>int EVP_CIPHER_CTX_cleanup (EVP_CIPHER_CTX *c)</h3>
<p>Clean up the EVP_CIPHER_CTX context. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>c</i> the cipher to clean up.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success.</dl>
<p> <code>Examples: </code> <code>example_evp_cipher.c</code>.</p>
<h3>unsigned long EVP_CIPHER_CTX_flags (const EVP_CIPHER_CTX *ctx)</h3>
<p>Get the flags for an EVP_CIPHER_CTX context. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> the EVP_CIPHER_CTX to get the flags from</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the flags for an EVP_CIPHER_CTX.</dl>
<h3>void* EVP_CIPHER_CTX_get_app_data (EVP_CIPHER_CTX *ctx)</h3>
<p>Get the app data for an EVP_CIPHER_CTX context. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> the EVP_CIPHER_CTX to get the app data from</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the app data for an EVP_CIPHER_CTX.</dl>
<h3>void EVP_CIPHER_CTX_init (EVP_CIPHER_CTX *c)</h3>
<p>Initiate a EVP_CIPHER_CTX context. Clean up with <code>EVP_CIPHER_CTX_cleanup()</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>c</i> the cipher initiate.</dl>
<p> <code>Examples: </code> <code>example_evp_cipher.c</code>.</p>
<h3>size_t EVP_CIPHER_CTX_iv_length (const EVP_CIPHER_CTX *ctx)</h3>
<p>Return the IV size of the cipher context. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> cipher context to get the IV size from.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the IV size of the cipher context.</dl>
<h3>size_t EVP_CIPHER_CTX_key_length (const EVP_CIPHER_CTX *ctx)</h3>
<p>Return the key size of the cipher context. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> cipher context to get the key size from.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the key size of the cipher context.</dl>
<h3>int EVP_CIPHER_CTX_mode (const EVP_CIPHER_CTX *ctx)</h3>
<p>Get the mode for an EVP_CIPHER_CTX context. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> the EVP_CIPHER_CTX to get the mode from</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the mode for an EVP_CIPHER_CTX.</dl>
<h3>void EVP_CIPHER_CTX_set_app_data (EVP_CIPHER_CTX *ctx, void *data)</h3>
<p>Set the app data for an EVP_CIPHER_CTX context. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> the EVP_CIPHER_CTX to set the app data for<br />
 <i>data</i> the app data to set for an EVP_CIPHER_CTX.</dl>
<h3>int EVP_CIPHER_CTX_set_key_length (EVP_CIPHER_CTX *c, intlength)</h3>
<p>If the cipher type supports it, change the key length </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>c</i> the cipher context to change the key length for<br />
 <i>length</i> new key length</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success.</dl>
<h3>size_t EVP_CIPHER_iv_length (const EVP_CIPHER *c)</h3>
<p>Return the IV size of the cipher. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>c</i> cipher to get the IV size from.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the IV size of the cipher.</dl>
<p> <code>Examples: </code> <code>example_evp_cipher.c</code>.</p>
<h3>size_t EVP_CIPHER_key_length (const EVP_CIPHER *c)</h3>
<p>Return the key size of the cipher. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>c</i> cipher to get the key size from.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the key size of the cipher.</dl>
<p> <code>Examples: </code> <code>example_evp_cipher.c</code>.</p>
<h3>int EVP_CipherFinal_ex (EVP_CIPHER_CTX *ctx, void *out, int *outlen)</h3>
<p>Encipher/decipher final data </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> the cipher context.<br />
 <i>out</i> output data from the operation.<br />
 <i>outlen</i> output length</dl>
<p> The input length needs to be at least <code>EVP_CIPHER_block_size()</code> bytes long. </p>
<p> See <code>EVP Cipher</code> for an example how to use this function. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success.</dl>
<p> <code>Examples: </code> <code>example_evp_cipher.c</code>.</p>
<h3>int EVP_CipherInit_ex (EVP_CIPHER_CTX *ctx, const EVP_CIPHER *c, ENGINE *engine, const void *key, const void *iv, intencp)</h3>
<p>Initiate the EVP_CIPHER_CTX context to encrypt or decrypt data. Clean up with <code>EVP_CIPHER_CTX_cleanup()</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> context to initiate<br />
 <i>c</i> cipher to use.<br />
 <i>engine</i> crypto engine to use, NULL to select default.<br />
 <i>key</i> the crypto key to use, NULL will use the previous value.<br />
 <i>iv</i> the IV to use, NULL will use the previous value.<br />
 <i>encp</i> non zero will encrypt, -1 use the previous value.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success.</dl>
<p> <code>Examples: </code> <code>example_evp_cipher.c</code>.</p>
<h3>int EVP_CipherUpdate (EVP_CIPHER_CTX *ctx, void *out, int *outlen, void *in, size_tinlen)</h3>
<p>Encipher/decipher partial data </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> the cipher context.<br />
 <i>out</i> output data from the operation.<br />
 <i>outlen</i> output length<br />
 <i>in</i> input data to the operation.<br />
 <i>inlen</i> length of data.</dl>
<p> The output buffer length should at least be <code>EVP_CIPHER_block_size()</code> byte longer then the input length. </p>
<p> See <code>EVP Cipher</code> for an example how to use this function. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success.</dl>
<p> If there in no spare bytes in the left from last Update and the input length is on the block boundery, the <code>EVP_CipherUpdate()</code> function can take a shortcut (and preformance gain) and directly encrypt the data, otherwise we hav to fix it up and store extra it the EVP_CIPHER_CTX. </p>
<p> <code>Examples: </code> <code>example_evp_cipher.c</code>.</p>
<h3>const EVP_CIPHER* EVP_des_cbc (void)</h3>
<p>The DES cipher type </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the DES-CBC EVP_CIPHER pointer.</dl>
<h3>const EVP_CIPHER* EVP_des_ede3_cbc (void)</h3>
<p>The tripple DES cipher type </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the DES-EDE3-CBC EVP_CIPHER pointer.</dl>
<h3>int EVP_Digest (const void *data, size_tdsize, void *hash, unsigned int *hsize, const EVP_MD *md, ENGINE *engine)</h3>
<p>Do the whole <code>EVP_MD_CTX_create()</code>, <code>EVP_DigestInit_ex()</code>, <code>EVP_DigestUpdate()</code>, <code>EVP_DigestFinal_ex()</code>, <code>EVP_MD_CTX_destroy()</code> dance in one call. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> the data to update the context with<br />
 <i>dsize</i> length of data<br />
 <i>hash</i> output data of at least <code>EVP_MD_size()</code> length.<br />
 <i>hsize</i> output length of hash.<br />
 <i>md</i> message digest to use<br />
 <i>engine</i> engine to use, NULL for default engine.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success.</dl>
<h3>int EVP_DigestFinal_ex (EVP_MD_CTX *ctx, void *hash, unsigned int *size)</h3>
<p>Complete the message digest. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> the context to complete.<br />
 <i>hash</i> the output of the message digest function. At least <code>EVP_MD_size()</code>.<br />
 <i>size</i> the output size of hash.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success.</dl>
<h3>int EVP_DigestInit_ex (EVP_MD_CTX *ctx, const EVP_MD *md, ENGINE *engine)</h3>
<p>Init a EVP_MD_CTX for use a specific message digest and engine. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> the message digest context to init.<br />
 <i>md</i> the message digest to use.<br />
 <i>engine</i> the engine to use, NULL to use the default engine.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success.</dl>
<h3>int EVP_DigestUpdate (EVP_MD_CTX *ctx, const void *data, size_tsize)</h3>
<p>Update the digest with some data. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> the context to update<br />
 <i>data</i> the data to update the context with<br />
 <i>size</i> length of data</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success.</dl>
<h3>const EVP_CIPHER* EVP_enc_null (void)</h3>
<p>The NULL cipher type, does no encryption/decryption. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the null EVP_CIPHER pointer.</dl>
<h3>const EVP_CIPHER* EVP_get_cipherbyname (const char *name)</h3>
<p>Get the cipher type using their name. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>name</i> the name of the cipher.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the selected EVP_CIPHER pointer or NULL if not found.</dl>
<h3>const EVP_CIPHER* EVP_hcrypto_aes_128_cbc (void)</h3>
<p>The AES-128 cipher type (hcrypto) </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the AES-128 EVP_CIPHER pointer.</dl>
<h3>const EVP_CIPHER* EVP_hcrypto_aes_128_cfb8 (void)</h3>
<p>The AES-128 CFB8 cipher type (hcrypto) </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the AES-128 EVP_CIPHER pointer.</dl>
<h3>const EVP_CIPHER* EVP_hcrypto_aes_192_cbc (void)</h3>
<p>The AES-192 cipher type (hcrypto) </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the AES-192 EVP_CIPHER pointer.</dl>
<h3>const EVP_CIPHER* EVP_hcrypto_aes_192_cfb8 (void)</h3>
<p>The AES-192 CFB8 cipher type (hcrypto) </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the AES-192 EVP_CIPHER pointer.</dl>
<h3>const EVP_CIPHER* EVP_hcrypto_aes_256_cbc (void)</h3>
<p>The AES-256 cipher type (hcrypto) </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the AES-256 EVP_CIPHER pointer.</dl>
<h3>const EVP_CIPHER* EVP_hcrypto_aes_256_cfb8 (void)</h3>
<p>The AES-256 CFB8 cipher type (hcrypto) </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the AES-256 EVP_CIPHER pointer.</dl>
<h3>const EVP_CIPHER* EVP_hcrypto_camellia_128_cbc (void)</h3>
<p>The Camellia-128 cipher type &#8211; hcrypto </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the Camellia-128 EVP_CIPHER pointer.</dl>
<h3>const EVP_CIPHER* EVP_hcrypto_camellia_192_cbc (void)</h3>
<p>The Camellia-198 cipher type &#8211; hcrypto </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the Camellia-198 EVP_CIPHER pointer.</dl>
<h3>const EVP_CIPHER* EVP_hcrypto_camellia_256_cbc (void)</h3>
<p>The Camellia-256 cipher type &#8211; hcrypto </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the Camellia-256 EVP_CIPHER pointer.</dl>
<h3>const EVP_CIPHER* EVP_hcrypto_des_cbc (void)</h3>
<p>The DES cipher type </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the DES-CBC EVP_CIPHER pointer.</dl>
<h3>const EVP_CIPHER* EVP_hcrypto_des_ede3_cbc (void)</h3>
<p>The tripple DES cipher type &#8211; hcrypto </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the DES-EDE3-CBC EVP_CIPHER pointer.</dl>
<h3>const EVP_MD* EVP_hcrypto_md2 (void)</h3>
<p>The message digest MD2 &#8211; hcrypto </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the message digest type.</dl>
<h3>const EVP_MD* EVP_hcrypto_md4 (void)</h3>
<p>The message digest MD4 &#8211; hcrypto </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the message digest type.</dl>
<h3>const EVP_MD* EVP_hcrypto_md5 (void)</h3>
<p>The message digest MD5 &#8211; hcrypto </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the message digest type.</dl>
<h3>const EVP_CIPHER* EVP_hcrypto_rc2_40_cbc (void)</h3>
<p>The RC2-40 cipher type </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the RC2-40 EVP_CIPHER pointer.</dl>
<h3>const EVP_CIPHER* EVP_hcrypto_rc2_64_cbc (void)</h3>
<p>The RC2-64 cipher type </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the RC2-64 EVP_CIPHER pointer.</dl>
<h3>const EVP_CIPHER* EVP_hcrypto_rc2_cbc (void)</h3>
<p>The RC2 cipher type &#8211; hcrypto </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the RC2 EVP_CIPHER pointer.</dl>
<h3>const EVP_MD* EVP_hcrypto_sha1 (void)</h3>
<p>The message digest SHA1 &#8211; hcrypto </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the message digest type.</dl>
<h3>const EVP_MD* EVP_hcrypto_sha256 (void)</h3>
<p>The message digest SHA256 &#8211; hcrypto </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the message digest type.</dl>
<h3>const EVP_MD* EVP_hcrypto_sha384 (void)</h3>
<p>The message digest SHA384 &#8211; hcrypto </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the message digest type.</dl>
<h3>const EVP_MD* EVP_hcrypto_sha512 (void)</h3>
<p>The message digest SHA512 &#8211; hcrypto </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the message digest type.</dl>
<h3>const EVP_MD* EVP_md2 (void)</h3>
<p>The message digest MD2 </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the message digest type.</dl>
<h3>const EVP_MD* EVP_md4 (void)</h3>
<p>The message digest MD4 </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the message digest type.</dl>
<h3>const EVP_MD* EVP_md5 (void)</h3>
<p>The message digest MD5 </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the message digest type.</dl>
<h3>size_t EVP_MD_block_size (const EVP_MD *md)</h3>
<p>Return the blocksize of the message digest function. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>md</i> the evp message</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>size size of the message digest block size</dl>
<h3>size_t EVP_MD_CTX_block_size (EVP_MD_CTX *ctx)</h3>
<p>Return the blocksize of the message digest function. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> the evp message digest context</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>size size of the message digest block size</dl>
<h3>int EVP_MD_CTX_cleanup (EVP_MD_CTX *ctx)</h3>
<p>Free the resources used by the EVP_MD context. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> the context to free the resources from.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success.</dl>
<h3>EVP_MD_CTX* EVP_MD_CTX_create (void)</h3>
<p>Allocate a messsage digest context object. Free with <code>EVP_MD_CTX_destroy()</code>. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a newly allocated message digest context object.</dl>
<h3>void EVP_MD_CTX_destroy (EVP_MD_CTX *ctx)</h3>
<p>Free a messsage digest context object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> context to free.</dl>
<h3>void EVP_MD_CTX_init (EVP_MD_CTX *ctx)</h3>
<p>Initiate a messsage digest context object. Deallocate with <code>EVP_MD_CTX_cleanup()</code>. Please use <code>EVP_MD_CTX_create()</code> instead. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> variable to initiate.</dl>
<h3>const EVP_MD* EVP_MD_CTX_md (EVP_MD_CTX *ctx)</h3>
<p>Get the EVP_MD use for a specified context. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> the EVP_MD context to get the EVP_MD for.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the EVP_MD used for the context.</dl>
<h3>size_t EVP_MD_CTX_size (EVP_MD_CTX *ctx)</h3>
<p>Return the output size of the message digest function. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> the evp message digest context</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>size output size of the message digest function.</dl>
<h3>const EVP_MD* EVP_md_null (void)</h3>
<p>The null message digest </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the message digest type.</dl>
<h3>size_t EVP_MD_size (const EVP_MD *md)</h3>
<p>Return the output size of the message digest function. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>md</i> the evp message</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>size output size of the message digest function.</dl>
<h3>const EVP_CIPHER* EVP_rc2_40_cbc (void)</h3>
<p>The RC2 cipher type </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the RC2 EVP_CIPHER pointer.</dl>
<h3>const EVP_CIPHER* EVP_rc2_64_cbc (void)</h3>
<p>The RC2 cipher type </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the RC2 EVP_CIPHER pointer.</dl>
<h3>const EVP_CIPHER* EVP_rc2_cbc (void)</h3>
<p>The RC2 cipher type </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the RC2 EVP_CIPHER pointer.</dl>
<h3>const EVP_CIPHER* EVP_rc4 (void)</h3>
<p>The RC4 cipher type </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the RC4 EVP_CIPHER pointer.</dl>
<h3>const EVP_CIPHER* EVP_rc4_40 (void)</h3>
<p>The RC4-40 cipher type </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the RC4-40 EVP_CIPHER pointer.</dl>
<h3>const EVP_MD* EVP_sha (void)</h3>
<p>The message digest SHA1 </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the message digest type.</dl>
<h3>const EVP_MD* EVP_sha1 (void)</h3>
<p>The message digest SHA1 </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the message digest type.</dl>
<h3>const EVP_MD* EVP_sha256 (void)</h3>
<p>The message digest SHA256 </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the message digest type.</dl>
<h3>const EVP_MD* EVP_sha384 (void)</h3>
<p>The message digest SHA384 </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the message digest type.</dl>
<h3>const EVP_MD* EVP_sha512 (void)</h3>
<p>The message digest SHA512 </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the message digest type.</dl>
<h3>const EVP_CIPHER* EVP_wincrypt_des_ede3_cbc (void)</h3>
<p>The tripple DES cipher type (Micrsoft crypt provider) </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the DES-EDE3-CBC EVP_CIPHER pointer.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Heimdal crypto library from the source code.</p>
