---
title: "rsa_new(3)"
name: "rsa_new"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rsa_new/"
description: "RSA functions –"
---

<p>RSA functions &#8211; </p>
<h3>Functions</h3>
<p>RSA * <code>RSA_new</code> (void) </p>
<p> RSA * <code>RSA_new_method</code> (ENGINE *engine) </p>
<p> void <code>RSA_free</code> (RSA *rsa) </p>
<p> int <code>RSA_up_ref</code> (RSA *rsa) </p>
<p> const RSA_METHOD * <code>RSA_get_method</code> (const RSA *rsa) </p>
<p> int <code>RSA_set_method</code> (RSA *rsa, const RSA_METHOD *method) </p>
<p> int <code>RSA_set_app_data</code> (RSA *rsa, void *arg) </p>
<p> void * <code>RSA_get_app_data</code> (const RSA *rsa) </p>
<h2>Detailed Description</h2>
<p>See the <code>RSA &#8211; public-key cryptography</code> for description and examples.</p>
<h2>Function Documentation</h2>
<h3>void RSA_free (RSA *rsa)</h3>
<p>Free an allocation RSA object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rsa</i> the RSA object to free.</dl>
<h3>void* RSA_get_app_data (const RSA *rsa)</h3>
<p>Get the application data for the RSA object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rsa</i> the rsa object to get the parameter for</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the data object</dl>
<h3>const RSA_METHOD* RSA_get_method (const RSA *rsa)</h3>
<p>Return the RSA_METHOD used for this RSA object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rsa</i> the object to get the method from.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the method used for this RSA object.</dl>
<h3>RSA* RSA_new (void)</h3>
<p>Same as <code>RSA_new_method()</code> using NULL as engine. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a newly allocated RSA object. Free with <code>RSA_free()</code>.</dl>
<h3>RSA* RSA_new_method (ENGINE *engine)</h3>
<p>Allocate a new RSA object using the engine, if NULL is specified as the engine, use the default RSA engine as returned by ENGINE_get_default_RSA(). </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>engine</i> Specific what ENGINE RSA provider should be used.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a newly allocated RSA object. Free with <code>RSA_free()</code>.</dl>
<h3>int RSA_set_app_data (RSA *rsa, void *arg)</h3>
<p>Set the application data for the RSA object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rsa</i> the rsa object to set the parameter for<br />
 <i>arg</i> the data object to store</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success.</dl>
<h3>int RSA_set_method (RSA *rsa, const RSA_METHOD *method)</h3>
<p>Set a new method for the RSA keypair. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rsa</i> rsa parameter.<br />
 <i>method</i> the new method for the RSA parameter.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success.</dl>
<h3>int RSA_up_ref (RSA *rsa)</h3>
<p>Add an extra reference to the RSA object. The object should be free with <code>RSA_free()</code> to drop the reference. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rsa</i> the object to add reference counting too.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the current reference count, can&#8217;t safely be used except for debug printing.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Heimdal crypto library from the source code.</p>
