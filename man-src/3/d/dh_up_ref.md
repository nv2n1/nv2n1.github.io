---
title: "dh_up_ref(3)"
name: "dh_up_ref"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dh_up_ref/"
description: "Diffie-Hellman functions –"
---

<p>Diffie-Hellman functions &#8211; </p>
<h3>Functions</h3>
<p>const DH_METHOD * <code>DH_ltm_method</code> (void) </p>
<p> DH * <code>DH_new</code> (void) </p>
<p> DH * <code>DH_new_method</code> (ENGINE *engine) </p>
<p> void <code>DH_free</code> (DH *dh) </p>
<p> int <code>DH_up_ref</code> (DH *dh) </p>
<p> int <code>DH_size</code> (const DH *dh) </p>
<p> int <code>DH_set_ex_data</code> (DH *dh, int idx, void *data) </p>
<p> void * <code>DH_get_ex_data</code> (DH *dh, int idx) </p>
<p> int <code>DH_generate_parameters_ex</code> (DH *dh, int prime_len, int generator, BN_GENCB *cb) </p>
<p> int <code>DH_check_pubkey</code> (const DH *dh, const BIGNUM *pub_key, int *codes) </p>
<p> int <code>DH_generate_key</code> (DH *dh) </p>
<p> int <code>DH_compute_key</code> (unsigned char *shared_key, const BIGNUM *peer_pub_key, DH *dh) </p>
<p> int <code>DH_set_method</code> (DH *dh, const DH_METHOD *method) </p>
<p> const DH_METHOD * <code>DH_null_method</code> (void) </p>
<p> void <code>DH_set_default_method</code> (const DH_METHOD *meth) </p>
<p> const DH_METHOD * <code>DH_get_default_method</code> (void) </p>
<h2>Detailed Description</h2>
<p>See the <code>DH &#8211; Diffie-Hellman key exchange</code> for description and examples.</p>
<h2>Function Documentation</h2>
<h3>int DH_check_pubkey (const DH *dh, const BIGNUM *pub_key, int *codes)</h3>
<p>Check that the public key is sane. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dh</i> the local peer DH parameters.<br />
 <i>pub_key</i> the remote peer public key parameters.<br />
 <i>codes</i> return that the failures of the pub_key are.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 on failure and *codes is set the the combined fail check for the public key</dl>
<p> Checks that the function performs are:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>pub_key is not negative</p>
<dt>&bull;</p>
<dd>pub_key &gt; 1 and pub_key &lt; p &#8211; 1, to avoid small subgroups attack.</p>
<dt>&bull;</p>
<dd>if g == 2, pub_key have more then one bit set, if bits set is 1, log_2(pub_key) is trival</dl>
<h3>int DH_compute_key (unsigned char *shared_key, const BIGNUM *peer_pub_key, DH *dh)</h3>
<p>Complute the shared secret key. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>shared_key</i> the resulting shared key, need to be at least <code>DH_size()</code> large.<br />
 <i>peer_pub_key</i> the peer&#8217;s public key.<br />
 <i>dh</i> the dh key pair.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success.</dl>
<p> Checks that the pubkey passed in is valid using <code>DH_check_pubkey()</code>.</p>
<h3>void DH_free (DH *dh)</h3>
<p>Free a DH object and release related resources, like ENGINE, that the object was using. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dh</i> object to be freed.</dl>
<h3>int DH_generate_key (DH *dh)</h3>
<p>Generate a new DH private-public key pair. The dh parameter must be allocted first with <code>DH_new()</code>. dh-&gt;p and dp-&gt;g must be set. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dh</i> dh parameter.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success.</dl>
<h3>int DH_generate_parameters_ex (DH *dh, intprime_len, intgenerator, BN_GENCB *cb)</h3>
<p>Generate DH parameters for the DH object give parameters. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dh</i> The DH object to generate parameters for.<br />
 <i>prime_len</i> length of the prime<br />
 <i>generator</i> generator, g<br />
 <i>cb</i> Callback parameters to show progress, can be NULL.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the maximum size in bytes of the out data.</dl>
<h3>const DH_METHOD* DH_get_default_method (void)</h3>
<p>Return the default DH implementation. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>pointer to a DH_METHOD.</dl>
<h3>void* DH_get_ex_data (DH *dh, intidx)</h3>
<p>Get the data for index idx in the DH object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dh</i> DH object.<br />
 <i>idx</i> index to get the data for.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the object store in index idx</dl>
<h3>const DH_METHOD* DH_ltm_method (void)</h3>
<p>DH implementation using libtommath. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the DH_METHOD for the DH implementation using libtommath.</dl>
<h3>DH* DH_new (void)</h3>
<p>Create a new DH object using DH_new_method(NULL), see <code>DH_new_method()</code>. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a newly allocated DH object.</dl>
<h3>DH* DH_new_method (ENGINE *engine)</h3>
<p>Create a new DH object from the given engine, if the NULL is used, the default engine is used. Free the DH object with <code>DH_free()</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>engine</i> The engine to use to allocate the DH object.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a newly allocated DH object.</dl>
<h3>const DH_METHOD* DH_null_method (void)</h3>
<p>Return the dummy DH implementation. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>pointer to a DH_METHOD.</dl>
<h3>void DH_set_default_method (const DH_METHOD *meth)</h3>
<p>Set the default DH implementation. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>meth</i> pointer to a DH_METHOD.</dl>
<h3>int DH_set_ex_data (DH *dh, intidx, void *data)</h3>
<p>Set the data index idx in the DH object to data. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dh</i> DH object.<br />
 <i>idx</i> index to set the data for.<br />
 <i>data</i> data to store for the index idx.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success.</dl>
<h3>int DH_set_method (DH *dh, const DH_METHOD *method)</h3>
<p>Set a new method for the DH keypair. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dh</i> dh parameter.<br />
 <i>method</i> the new method for the DH parameter.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success.</dl>
<h3>int DH_size (const DH *dh)</h3>
<p>The maximum output size of the <code>DH_compute_key()</code> function. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dh</i> The DH object to get the size from.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the maximum size in bytes of the out data.</dl>
<h3>int DH_up_ref (DH *dh)</h3>
<p>Add a reference to the DH object. The object should be free with <code>DH_free()</code> to drop the reference. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dh</i> the object to increase the reference count too.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the updated reference count, can&#8217;t safely be used except for debug printing.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Heimdal crypto library from the source code.</p>
