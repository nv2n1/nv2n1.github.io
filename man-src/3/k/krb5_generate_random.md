---
title: "krb5_generate_random(3)"
name: "krb5_generate_random"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_generate_random/"
description: "Heimdal Kerberos 5 cryptography functions –"
---

<h2 class="name">NAME</h2>
<p> Heimdal Kerberos 5 cryptography functions &#8211; </p>
<h3>Functions</h3>
<p> HEIMDAL_WARN_UNUSED_RESULT_ATTRIBUTE<br />
 KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_generate_random</code> (void *buf, size_t len)&quot; </p>
<p> KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL <code>krb5_generate_random_block</code> (void *buf, size_t len)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_enctype_valid</code> (krb5_context context, krb5_enctype etype)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cksumtype_to_enctype</code> (krb5_context context, krb5_cksumtype ctype, krb5_enctype *etype)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_encrypt_iov_ivec</code> (krb5_context context, krb5_crypto crypto, unsigned usage, <code>krb5_crypto_iov</code> *data, int num_data, void *ivec)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_decrypt_iov_ivec</code> (krb5_context context, krb5_crypto crypto, unsigned usage, <code>krb5_crypto_iov</code> *data, unsigned int num_data, void *ivec)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_create_checksum_iov</code> (krb5_context context, krb5_crypto crypto, unsigned usage, <code>krb5_crypto_iov</code> *data, unsigned int num_data, krb5_cksumtype *type)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_verify_checksum_iov</code> (krb5_context context, krb5_crypto crypto, unsigned usage, <code>krb5_crypto_iov</code> *data, unsigned int num_data, krb5_cksumtype *type)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_crypto_init</code> (krb5_context context, const krb5_keyblock *key, krb5_enctype etype, krb5_crypto *crypto)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_crypto_destroy</code> (krb5_context context, krb5_crypto crypto)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_crypto_getblocksize</code> (krb5_context context, krb5_crypto crypto, size_t *blocksize)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_crypto_getenctype</code> (krb5_context context, krb5_crypto crypto, krb5_enctype *enctype)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_crypto_getpadsize</code> (krb5_context context, krb5_crypto crypto, size_t *padsize)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_crypto_getconfoundersize</code> (krb5_context context, krb5_crypto crypto, size_t *confoundersize)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_enctype_disable</code> (krb5_context context, krb5_enctype enctype)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_enctype_enable</code> (krb5_context context, krb5_enctype enctype)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_allow_weak_crypto</code> (krb5_context context, krb5_boolean enable)&quot; </p>
<p> KRB5_LIB_FUNCTION krb5_boolean<br />
 KRB5_LIB_CALL <code>krb5_is_enctype_weak</code> (krb5_context context, krb5_enctype enctype)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_random_to_key</code> (krb5_context context, krb5_enctype type, const void *data, size_t size, krb5_keyblock *key)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_crypto_fx_cf2</code> (krb5_context context, const krb5_crypto crypto1, const krb5_crypto crypto2, krb5_data *pepper1, krb5_data *pepper2, krb5_enctype enctype, krb5_keyblock *res)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_generate_subkey_extended</code> (krb5_context context, const krb5_keyblock *key, krb5_enctype etype, krb5_keyblock **subkey)&quot; </p>
<p> KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL <code>krb5_keyblock_zero</code> (krb5_keyblock *keyblock)&quot; </p>
<p> KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL <code>krb5_free_keyblock_contents</code> (krb5_context context, krb5_keyblock *keyblock)&quot; </p>
<p> KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL <code>krb5_free_keyblock</code> (krb5_context context, krb5_keyblock *keyblock)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_copy_keyblock_contents</code> (krb5_context context, const krb5_keyblock *inblock, krb5_keyblock *to)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_copy_keyblock</code> (krb5_context context, const krb5_keyblock *inblock, krb5_keyblock **to)&quot; </p>
<p> KRB5_LIB_FUNCTION krb5_enctype<br />
 KRB5_LIB_CALL <code>krb5_keyblock_get_enctype</code> (const krb5_keyblock *block)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_keyblock_init</code> (krb5_context context, krb5_enctype type, const void *data, size_t size, krb5_keyblock *key)&quot; </p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_allow_weak_crypto (krb5_contextcontext, krb5_booleanenable)</h3>
<p> Enable or disable all weak encryption types </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context<br />
 <i>enable</i> true to enable, false to disable</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cksumtype_to_enctype (krb5_contextcontext, krb5_cksumtypectype, krb5_enctype *etype)</h3>
<p> Return the coresponding encryption type for a checksum type. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos context<br />
 <i>ctype</i> The checksum type to get the result enctype for<br />
 <i>etype</i> The returned encryption, when the matching etype is not found, etype is set to ETYPE_NULL.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code for an failure or 0 on success.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_copy_keyblock (krb5_contextcontext, const krb5_keyblock *inblock, krb5_keyblock **to)</h3>
<p> Copy a keyblock, free the output keyblock with <code>krb5_free_keyblock()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Kerberos 5 context<br />
 <i>inblock</i> the key to copy<br />
 <i>to</i> the output key.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success or a Kerberos 5 error code</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_copy_keyblock_contents (krb5_contextcontext, const krb5_keyblock *inblock, krb5_keyblock *to)</h3>
<p> Copy a keyblock, free the output keyblock with <code>krb5_free_keyblock_contents()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Kerberos 5 context<br />
 <i>inblock</i> the key to copy<br />
 <i>to</i> the output key.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success or a Kerberos 5 error code</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_create_checksum_iov (krb5_contextcontext, krb5_cryptocrypto, unsignedusage, <code>krb5_crypto_iov</code> *data, unsigned intnum_data, krb5_cksumtype *type)</h3>
<p> Create a Kerberos message checksum. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos context<br />
 <i>crypto</i> Kerberos crypto context<br />
 <i>usage</i> Key usage for this buffer<br />
 <i>data</i> array of buffers to process<br />
 <i>num_data</i> length of array<br />
 <i>type</i> output data</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_crypto_destroy (krb5_contextcontext, krb5_cryptocrypto)</h3>
<p> Free a crypto context created by <code>krb5_crypto_init()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos context<br />
 <i>crypto</i> crypto context to free</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_crypto_fx_cf2 (krb5_contextcontext, const krb5_cryptocrypto1, const krb5_cryptocrypto2, krb5_data *pepper1, krb5_data *pepper2, krb5_enctypeenctype, krb5_keyblock *res)</h3>
<p> The FX-CF2 key derivation function, used in FAST and preauth framework. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context<br />
 <i>crypto1</i> first key to combine<br />
 <i>crypto2</i> second key to combine<br />
 <i>pepper1</i> factor to combine with first key to garante uniqueness<br />
 <i>pepper2</i> factor to combine with second key to garante uniqueness<br />
 <i>enctype</i> the encryption type of the resulting key<br />
 <i>res</i> allocated key, free with <code>krb5_free_keyblock_contents()</code></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_crypto_getblocksize (krb5_contextcontext, krb5_cryptocrypto, size_t *blocksize)</h3>
<p> Return the blocksize used algorithm referenced by the crypto context </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos context<br />
 <i>crypto</i> crypto context to query<br />
 <i>blocksize</i> the resulting blocksize</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_crypto_getconfoundersize (krb5_contextcontext, krb5_cryptocrypto, size_t *confoundersize)</h3>
<p> Return the confounder size used by the crypto context </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos context<br />
 <i>crypto</i> crypto context to query<br />
 <i>confoundersize</i> the returned confounder size</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_crypto_getenctype (krb5_contextcontext, krb5_cryptocrypto, krb5_enctype *enctype)</h3>
<p> Return the encryption type used by the crypto context </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos context<br />
 <i>crypto</i> crypto context to query<br />
 <i>enctype</i> the resulting encryption type</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_crypto_getpadsize (krb5_contextcontext, krb5_cryptocrypto, size_t *padsize)</h3>
<p> Return the padding size used by the crypto context </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos context<br />
 <i>crypto</i> crypto context to query<br />
 <i>padsize</i> the return padding size</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_crypto_init (krb5_contextcontext, const krb5_keyblock *key, krb5_enctypeetype, krb5_crypto *crypto)</h3>
<p> Create a crypto context used for all encryption and signature operation. The encryption type to use is taken from the key, but can be overridden with the enctype parameter. This can be useful for encryptions types which is compatiable (DES for example). </p>
<p> To free the crypto context, use <code>krb5_crypto_destroy()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos context<br />
 <i>key</i> the key block information with all key data<br />
 <i>etype</i> the encryption type<br />
 <i>crypto</i> the resulting crypto context</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_decrypt_iov_ivec (krb5_contextcontext, krb5_cryptocrypto, unsignedusage, <code>krb5_crypto_iov</code> *data, unsigned intnum_data, void *ivec)</h3>
<p> Inline decrypt a Kerberos message. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos context<br />
 <i>crypto</i> Kerberos crypto context<br />
 <i>usage</i> Key usage for this buffer<br />
 <i>data</i> array of buffers to process<br />
 <i>num_data</i> length of array<br />
 <i>ivec</i> initial cbc/cts vector</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0.</dl>
<dl>
<dt>1.</p>
<dd> KRB5_CRYPTO_TYPE_HEADER</p>
<dt>2.</p>
<dd> one KRB5_CRYPTO_TYPE_DATA and array [0,&#8230;] of KRB5_CRYPTO_TYPE_SIGN_ONLY in any order, however the receiver have to aware of the order. KRB5_CRYPTO_TYPE_SIGN_ONLY is commonly used unencrypoted protocol headers and trailers. The output data will be of same size as the input data or shorter.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_encrypt_iov_ivec (krb5_contextcontext, krb5_cryptocrypto, unsignedusage, <code>krb5_crypto_iov</code> *data, intnum_data, void *ivec)</h3>
<p> Inline encrypt a kerberos message </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos context<br />
 <i>crypto</i> Kerberos crypto context<br />
 <i>usage</i> Key usage for this buffer<br />
 <i>data</i> array of buffers to process<br />
 <i>num_data</i> length of array<br />
 <i>ivec</i> initial cbc/cts vector</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0.</dl>
<p> Kerberos encrypted data look like this: </p>
<dl>
<dt>1.</p>
<dd> KRB5_CRYPTO_TYPE_HEADER</p>
<dt>2.</p>
<dd> array [1,&#8230;] KRB5_CRYPTO_TYPE_DATA and array [0,&#8230;] KRB5_CRYPTO_TYPE_SIGN_ONLY in any order, however the receiver have to aware of the order. KRB5_CRYPTO_TYPE_SIGN_ONLY is commonly used headers and trailers.</p>
<dt>3.</p>
<dd> KRB5_CRYPTO_TYPE_PADDING, at least on padsize long if padsize &gt; 1</p>
<dt>4.</p>
<dd> KRB5_CRYPTO_TYPE_TRAILER</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_enctype_disable (krb5_contextcontext, krb5_enctypeenctype)</h3>
<p> Disable encryption type </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context<br />
 <i>enctype</i> encryption type to disable</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_enctype_enable (krb5_contextcontext, krb5_enctypeenctype)</h3>
<p> Enable encryption type </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context<br />
 <i>enctype</i> encryption type to enable</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_enctype_valid (krb5_contextcontext, krb5_enctypeetype)</h3>
<p> Check if a enctype is valid, return 0 if it is. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos context<br />
 <i>etype</i> enctype to check if its valid or not</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code for an failure or 0 on success (enctype valid).</dl>
<h3>KRB5_LIB_FUNCTION void KRB5_LIB_CALL krb5_free_keyblock (krb5_contextcontext, krb5_keyblock *keyblock)</h3>
<p> Free a keyblock, also zero out the content of the keyblock, uses <code>krb5_free_keyblock_contents()</code> to free the content. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Kerberos 5 context<br />
 <i>keyblock</i> keyblock to free, NULL is valid argument</dl>
<h3>KRB5_LIB_FUNCTION void KRB5_LIB_CALL krb5_free_keyblock_contents (krb5_contextcontext, krb5_keyblock *keyblock)</h3>
<p> Free a keyblock&#8217;s content, also zero out the content of the keyblock. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Kerberos 5 context<br />
 <i>keyblock</i> keyblock content to free, NULL is valid argument</dl>
<h3>HEIMDAL_WARN_UNUSED_RESULT_ATTRIBUTE KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_generate_random (void *buf, size_tlen)</h3>
<p> Fill buffer buf with len bytes of PRNG randomness that is ok to use for key generation, padding and public diclosing the randomness w/o disclosing the randomness source. </p>
<p> This function can fail, and callers must check the return value. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>buf</i> a buffer to fill with randomness<br />
 <i>len</i> length of memory that buf points to.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> return 0 on success or HEIM_ERR_RANDOM_OFFLINE if the funcation failed to initialize the randomness source.</dl>
<h3>KRB5_LIB_FUNCTION void KRB5_LIB_CALL krb5_generate_random_block (void *buf, size_tlen)</h3>
<p> Fill buffer buf with len bytes of PRNG randomness that is ok to use for key generation, padding and public diclosing the randomness w/o disclosing the randomness source. </p>
<p> This function can NOT fail, instead it will abort() and program will crash. </p>
<p> If this function is called after a successful <code>krb5_init_context()</code>, the chance of it failing is low due to that <code>krb5_init_context()</code> pulls out some random, and quite commonly the randomness sources will not fail once it have started to produce good output, /dev/urandom behavies that way. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>buf</i> a buffer to fill with randomness<br />
 <i>len</i> length of memory that buf points to.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_generate_subkey_extended (krb5_contextcontext, const krb5_keyblock *key, krb5_enctypeetype, krb5_keyblock **subkey)</h3>
<p> Generate subkey, from keyblock </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> kerberos context<br />
 <i>key</i> session key<br />
 <i>etype</i> encryption type of subkey, if ETYPE_NULL, use key&#8217;s enctype<br />
 <i>subkey</i> returned new, free with <code>krb5_free_keyblock()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success or a Kerberos 5 error code</dl>
<h3>KRB5_LIB_FUNCTION krb5_boolean KRB5_LIB_CALL krb5_is_enctype_weak (krb5_contextcontext, krb5_enctypeenctype)</h3>
<p> Returns is the encryption is strong or weak </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context<br />
 <i>enctype</i> encryption type to probe</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns true if encryption type is weak or is not supported.</dl>
<h3>KRB5_LIB_FUNCTION krb5_enctype KRB5_LIB_CALL krb5_keyblock_get_enctype (const krb5_keyblock *block)</h3>
<p> Get encryption type of a keyblock.</p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_keyblock_init (krb5_contextcontext, krb5_enctypetype, const void *data, size_tsize, krb5_keyblock *key)</h3>
<p> Fill in `key&#8217; with key data of type `enctype&#8217; from `data&#8217; of length `size&#8217;. Key should be freed using <code>krb5_free_keyblock_contents()</code>. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success or a Kerberos 5 error code</dl>
<h3>KRB5_LIB_FUNCTION void KRB5_LIB_CALL krb5_keyblock_zero (krb5_keyblock *keyblock)</h3>
<p> Zero out a keyblock </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>keyblock</i> keyblock to zero out</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_random_to_key (krb5_contextcontext, krb5_enctypetype, const void *data, size_tsize, krb5_keyblock *key)</h3>
<p> Converts the random bytestring to a protocol key according to Kerberos crypto frame work. It may be assumed that all the bits of the input string are equally random, even though the entropy present in the random source may be limited. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context<br />
 <i>type</i> the enctype resulting key will be of<br />
 <i>data</i> input random data to convert to a key<br />
 <i>size</i> size of input random data, at least krb5_enctype_keysize() long<br />
 <i>key</i> key, output key, free with <code>krb5_free_keyblock_contents()</code></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_verify_checksum_iov (krb5_contextcontext, krb5_cryptocrypto, unsignedusage, <code>krb5_crypto_iov</code> *data, unsigned intnum_data, krb5_cksumtype *type)</h3>
<p> Verify a Kerberos message checksum. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos context<br />
 <i>crypto</i> Kerberos crypto context<br />
 <i>usage</i> Key usage for this buffer<br />
 <i>data</i> array of buffers to process<br />
 <i>num_data</i> length of array<br />
 <i>type</i> return checksum type if not NULL</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for HeimdalKerberos5library from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbBH">Author</a></p>
<dd></dl>
