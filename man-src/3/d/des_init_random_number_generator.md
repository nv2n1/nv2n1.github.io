---
title: "des_init_random_number_generator(3)"
name: "des_init_random_number_generator"
section: "3"
letter: "d"
url: "/docs/linux/man/3-des_init_random_number_generator/"
description: "DES crypto functions –"
---

<p>DES crypto functions &#8211; </p>
<h3>Functions</h3>
<p>void <code>DES_set_odd_parity</code> (DES_cblock *key) </p>
<p> int HC_DEPRECATED <code>DES_check_key_parity</code> (DES_cblock *key) </p>
<p> int <code>DES_is_weak_key</code> (DES_cblock *key) </p>
<p> int HC_DEPRECATED <code>DES_set_key</code> (DES_cblock *key, DES_key_schedule *ks) </p>
<p> int <code>DES_set_key_unchecked</code> (DES_cblock *key, DES_key_schedule *ks) </p>
<p> int <code>DES_set_key_checked</code> (DES_cblock *key, DES_key_schedule *ks) </p>
<p> int <code>DES_key_sched</code> (DES_cblock *key, DES_key_schedule *ks) </p>
<p> void <code>DES_encrypt</code> (uint32_t u[2], DES_key_schedule *ks, int encp) </p>
<p> void <code>DES_ecb_encrypt</code> (DES_cblock *input, DES_cblock *output, DES_key_schedule *ks, int encp) </p>
<p> void <code>DES_cbc_encrypt</code> (const void *in, void *out, long length, DES_key_schedule *ks, DES_cblock *iv, int encp) </p>
<p> void <code>DES_pcbc_encrypt</code> (const void *in, void *out, long length, DES_key_schedule *ks, DES_cblock *iv, int encp) </p>
<p> void <code>DES_ecb3_encrypt</code> (DES_cblock *input, DES_cblock *output, DES_key_schedule *ks1, DES_key_schedule *ks2, DES_key_schedule *ks3, int encp) </p>
<p> void <code>DES_ede3_cbc_encrypt</code> (const void *in, void *out, long length, DES_key_schedule *ks1, DES_key_schedule *ks2, DES_key_schedule *ks3, DES_cblock *iv, int encp) </p>
<p> void <code>DES_cfb64_encrypt</code> (const void *in, void *out, long length, DES_key_schedule *ks, DES_cblock *iv, int *num, int encp) </p>
<p> uint32_t <code>DES_cbc_cksum</code> (const void *in, DES_cblock *output, long length, DES_key_schedule *ks, DES_cblock *iv) </p>
<p> void <code>DES_string_to_key</code> (const char *str, DES_cblock *key) </p>
<p> int HC_DEPRECATED <code>DES_new_random_key</code> (DES_cblock *key) </p>
<p> void HC_DEPRECATED <code>DES_init_random_number_generator</code> (DES_cblock *seed) </p>
<p> void HC_DEPRECATED <code>DES_random_key</code> (DES_cblock *key) </p>
<h2>Detailed Description</h2>
<p>See the <code>DES &#8211; Data Encryption Standard crypto interface</code> for description and examples.</p>
<h2>Function Documentation</h2>
<h3>uint32_t DES_cbc_cksum (const void *in, DES_cblock *output, longlength, DES_key_schedule *ks, DES_cblock *iv)</h3>
<p>Crete a checksum using DES in CBC encryption mode. This mode is only used for Kerberos 4, and it should stay that way. </p>
<p> The IV must always be diffrent for diffrent input data blocks. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>in</i> data to checksum<br />
 <i>output</i> the checksum<br />
 <i>length</i> length of data<br />
 <i>ks</i> key schedule to use<br />
 <i>iv</i> initial vector to use</dl>
<h3>void DES_cbc_encrypt (const void *in, void *out, longlength, DES_key_schedule *ks, DES_cblock *iv, intencp)</h3>
<p>Encrypt/decrypt a block using DES in Chain Block Cipher mode (cbc). </p>
<p> The IV must always be diffrent for diffrent input data blocks. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>in</i> data to encrypt<br />
 <i>out</i> data to encrypt<br />
 <i>length</i> length of data<br />
 <i>ks</i> key schedule to use<br />
 <i>iv</i> initial vector to use<br />
 <i>encp</i> if non zero, encrypt. if zero, decrypt.</dl>
<h3>void DES_cfb64_encrypt (const void *in, void *out, longlength, DES_key_schedule *ks, DES_cblock *iv, int *num, intencp)</h3>
<p>Encrypt/decrypt using DES in cipher feedback mode with 64 bit feedback. </p>
<p> The IV must always be diffrent for diffrent input data blocks. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>in</i> data to encrypt<br />
 <i>out</i> data to encrypt<br />
 <i>length</i> length of data<br />
 <i>ks</i> key schedule to use<br />
 <i>iv</i> initial vector to use<br />
 <i>num</i> offset into in cipher block encryption/decryption stop last time.<br />
 <i>encp</i> if non zero, encrypt. if zero, decrypt.</dl>
<h3>int HC_DEPRECATED DES_check_key_parity (DES_cblock *key)</h3>
<p>Check if the key have correct parity. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> key to check the parity.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 on failure.</dl>
<h3>void DES_ecb3_encrypt (DES_cblock *input, DES_cblock *output, DES_key_schedule *ks1, DES_key_schedule *ks2, DES_key_schedule *ks3, intencp)</h3>
<p>Encrypt/decrypt a block using triple DES using EDE mode, encrypt/decrypt/encrypt. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>input</i> data to encrypt<br />
 <i>output</i> data to encrypt<br />
 <i>ks1</i> key schedule to use<br />
 <i>ks2</i> key schedule to use<br />
 <i>ks3</i> key schedule to use<br />
 <i>encp</i> if non zero, encrypt. if zero, decrypt.</dl>
<h3>void DES_ecb_encrypt (DES_cblock *input, DES_cblock *output, DES_key_schedule *ks, intencp)</h3>
<p>Encrypt/decrypt a block using DES. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>input</i> data to encrypt<br />
 <i>output</i> data to encrypt<br />
 <i>ks</i> key schedule to use<br />
 <i>encp</i> if non zero, encrypt. if zero, decrypt.</dl>
<h3>void DES_ede3_cbc_encrypt (const void *in, void *out, longlength, DES_key_schedule *ks1, DES_key_schedule *ks2, DES_key_schedule *ks3, DES_cblock *iv, intencp)</h3>
<p>Encrypt/decrypt using Triple DES in Chain Block Cipher mode (cbc). </p>
<p> The IV must always be diffrent for diffrent input data blocks. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>in</i> data to encrypt<br />
 <i>out</i> data to encrypt<br />
 <i>length</i> length of data<br />
 <i>ks1</i> key schedule to use<br />
 <i>ks2</i> key schedule to use<br />
 <i>ks3</i> key schedule to use<br />
 <i>iv</i> initial vector to use<br />
 <i>encp</i> if non zero, encrypt. if zero, decrypt.</dl>
<h3>void DES_encrypt (uint32_tu[2], DES_key_schedule *ks, intencp)</h3>
<p>Encrypt/decrypt a block using DES. Also called ECB mode </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>u</i> data to encrypt<br />
 <i>ks</i> key schedule to use<br />
 <i>encp</i> if non zero, encrypt. if zero, decrypt.</dl>
<h3>void HC_DEPRECATED DES_init_random_number_generator (DES_cblock *seed)</h3>
<p>Seed the random number generator. Deprecated, use <code>RAND &#8211; random number</code> </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>seed</i> a seed to seed that random number generate with.</dl>
<h3>int DES_is_weak_key (DES_cblock *key)</h3>
<p>Checks if the key is any of the weaks keys that makes DES attacks trival. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> key to check.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if the key is weak, 0 otherwise.</dl>
<h3>int DES_key_sched (DES_cblock *key, DES_key_schedule *ks)</h3>
<p>Compatibility function for eay libdes, works just like <code>DES_set_key_checked()</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> a key to initialize the key schedule with.<br />
 <i>ks</i> a key schedule to initialize.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, -1 on invalid parity, -2 on weak key.</dl>
<h3>int HC_DEPRECATED DES_new_random_key (DES_cblock *key)</h3>
<p>Generate a random des key using a random block, fixup parity and skip weak keys. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> is set to a random key.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, non zero on random number generator failure.</dl>
<h3>void DES_pcbc_encrypt (const void *in, void *out, longlength, DES_key_schedule *ks, DES_cblock *iv, intencp)</h3>
<p>Encrypt/decrypt a block using DES in Propagating Cipher Block Chaining mode. This mode is only used for Kerberos 4, and it should stay that way. </p>
<p> The IV must always be diffrent for diffrent input data blocks. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>in</i> data to encrypt<br />
 <i>out</i> data to encrypt<br />
 <i>length</i> length of data<br />
 <i>ks</i> key schedule to use<br />
 <i>iv</i> initial vector to use<br />
 <i>encp</i> if non zero, encrypt. if zero, decrypt.</dl>
<h3>void HC_DEPRECATED DES_random_key (DES_cblock *key)</h3>
<p>Generate a random key, deprecated since it doesn&#8217;t return an error code, use <code>DES_new_random_key()</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> is set to a random key.</dl>
<h3>int HC_DEPRECATED DES_set_key (DES_cblock *key, DES_key_schedule *ks)</h3>
<p>Setup a des key schedule from a key. Deprecated function, use <code>DES_set_key_unchecked()</code> or <code>DES_set_key_checked()</code> instead. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> a key to initialize the key schedule with.<br />
 <i>ks</i> a key schedule to initialize.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success</dl>
<h3>int DES_set_key_checked (DES_cblock *key, DES_key_schedule *ks)</h3>
<p>Just like <code>DES_set_key_unchecked()</code> except checking that the key is not weak for or have correct parity. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> a key to initialize the key schedule with.<br />
 <i>ks</i> a key schedule to initialize.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, -1 on invalid parity, -2 on weak key.</dl>
<h3>int DES_set_key_unchecked (DES_cblock *key, DES_key_schedule *ks)</h3>
<p>Setup a des key schedule from a key. The key is no longer needed after this transaction and can cleared. </p>
<p> Does NOT check that the key is weak for or have wrong parity. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> a key to initialize the key schedule with.<br />
 <i>ks</i> a key schedule to initialize.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success</dl>
<h3>void DES_set_odd_parity (DES_cblock *key)</h3>
<p>Set the parity of the key block, used to generate a des key from a random key. See <code>DES key generation</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> key to fixup the parity for.</dl>
<h3>void DES_string_to_key (const char *str, DES_cblock *key)</h3>
<p>Convert a string to a DES key. Use something like <code>PKCS5_PBKDF2_HMAC_SHA1()</code> to create key from passwords. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>str</i> The string to convert to a key<br />
 <i>key</i> the resulting key</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Heimdal crypto library from the source code.</p>
