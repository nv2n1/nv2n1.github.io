---
title: "evp_cipher_ctx_rand_key(3)"
name: "evp_cipher_ctx_rand_key"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evp_cipher_ctx_rand_key/"
description: "hcrypto function controlling behavior –"
---

<p>hcrypto function controlling behavior &#8211; </p>
<h3>Functions</h3>
<p>int <code>EVP_CIPHER_CTX_rand_key</code> (EVP_CIPHER_CTX *ctx, void *key) </p>
<p> int <code>EVP_CIPHER_CTX_ctrl</code> (EVP_CIPHER_CTX *ctx, int type, int arg, void *data) </p>
<p> void <code>OpenSSL_add_all_algorithms</code> (void) </p>
<p> void <code>OpenSSL_add_all_algorithms_conf</code> (void) </p>
<p> void <code>OpenSSL_add_all_algorithms_noconf</code> (void) </p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>int EVP_CIPHER_CTX_ctrl (EVP_CIPHER_CTX *ctx, inttype, intarg, void *data)</h3>
<p>Perform a operation on a ctx </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> context to perform operation on.<br />
 <i>type</i> type of operation.<br />
 <i>arg</i> argument to operation.<br />
 <i>data</i> addition data to operation.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 for success, 0 for failure.</dl>
<h3>int EVP_CIPHER_CTX_rand_key (EVP_CIPHER_CTX *ctx, void *key)</h3>
<p>Generate a random key for the specificed EVP_CIPHER. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> EVP_CIPHER_CTX type to build the key for.<br />
 <i>key</i> return key, must be at least <code>EVP_CIPHER_key_length()</code> byte long.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 for success, 0 for failure.</dl>
<h3>void OpenSSL_add_all_algorithms (void)</h3>
<p>Add all algorithms to the crypto core.</p>
<h3>void OpenSSL_add_all_algorithms_conf (void)</h3>
<p>Add all algorithms to the crypto core using configuration file.</p>
<h3>void OpenSSL_add_all_algorithms_noconf (void)</h3>
<p>Add all algorithms to the crypto core, but don&#8217;t use the configuration file.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Heimdal crypto library from the source code.</p>
