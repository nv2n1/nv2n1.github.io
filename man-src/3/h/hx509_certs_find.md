---
title: "hx509_certs_find(3)"
name: "hx509_certs_find"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hx509_certs_find/"
description: "hx509 certificate store functions –"
---

<h2 class="name">NAME</h2>
<p> hx509 certificate store functions &#8211; </p>
<h3>Functions</h3>
<p> int <code>hx509_certs_add</code> (hx509_context, hx509_certs, hx509_cert) </p>
<p> int <code>hx509_certs_append</code> (hx509_context, hx509_certs, hx509_lock, const char *) </p>
<p> int <code>hx509_certs_end_seq</code> (hx509_context, hx509_certs, hx509_cursor) </p>
<p> int <code>hx509_certs_filter</code> (hx509_context, hx509_certs, const hx509_query *, hx509_certs *) </p>
<p> int <code>hx509_certs_find</code> (hx509_context, hx509_certs, const hx509_query *, hx509_cert *) </p>
<p> void <code>hx509_certs_free</code> (hx509_certs *) </p>
<p> int <code>hx509_certs_info</code> (hx509_context, hx509_certs, int(*)(void *, const char *), void *) </p>
<p> int <code>hx509_certs_init</code> (hx509_context, const char *, int, hx509_lock, hx509_certs *) </p>
<p> int <code>hx509_certs_iter_f</code> (hx509_context, hx509_certs, int(*)(hx509_context, void *, hx509_cert), void *) </p>
<p> int <code>hx509_certs_merge</code> (hx509_context, hx509_certs, hx509_certs) </p>
<p> int <code>hx509_certs_next_cert</code> (hx509_context, hx509_certs, hx509_cursor, hx509_cert *) </p>
<p> int <code>hx509_certs_start_seq</code> (hx509_context, hx509_certs, hx509_cursor *) </p>
<p> int <code>hx509_certs_store</code> (hx509_context, hx509_certs, int, hx509_lock) </p>
<p> int <code>hx509_ci_print_names</code> (hx509_context, void *, hx509_cert) </p>
<p> int <code>hx509_get_one_cert</code> (hx509_context, hx509_certs, hx509_cert *) </p>
<h2>Detailed Description</h2>
<p> See the <code>Certificate store operations</code> for description and examples.</p>
<h2>Function Documentation</h2>
<h3>int hx509_certs_add (hx509_contextcontext, hx509_certscerts, hx509_certcert)</h3>
<p> Add a certificate to the certificiate store. </p>
<p> The receiving keyset certs will either increase reference counter of the cert or make a deep copy, either way, the caller needs to free the cert itself. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a hx509 context.<br />
 <i>certs</i> certificate store to add the certificate to.<br />
 <i>cert</i> certificate to add.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns an hx509 error code.</dl>
<h3>int hx509_certs_append (hx509_contextcontext, hx509_certsto, hx509_locklock, const char *name)</h3>
<p> Same a <code>hx509_certs_merge()</code> but use a lock and name to describe the from source. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a hx509 context.<br />
 <i>to</i> the store to merge into.<br />
 <i>lock</i> a lock that unlocks the certificates store, use NULL to select no password/certifictes/prompt lock (see <code>Locking and unlocking certificates and encrypted data.</code>).<br />
 <i>name</i> name of the source store</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns an hx509 error code.</dl>
<h3>int hx509_certs_end_seq (hx509_contextcontext, hx509_certscerts, hx509_cursorcursor)</h3>
<p> End the iteration over certificates. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a hx509 context.<br />
 <i>certs</i> certificate store to iterate over.<br />
 <i>cursor</i> cursor that will keep track of progress, freed.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns an hx509 error code.</dl>
<h3>int hx509_certs_filter (hx509_contextcontext, hx509_certscerts, const hx509_query *q, hx509_certs *result)</h3>
<p> Filter certificate matching the query. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a hx509 context.<br />
 <i>certs</i> certificate store to search.<br />
 <i>q</i> query allocated with <code>hx509 query functions</code> functions.<br />
 <i>result</i> the filtered certificate store, caller must free with <code>hx509_certs_free()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns an hx509 error code.</dl>
<p> Return HX509_CERT_NOT_FOUND if no certificate in certs matched the query.</p>
<h3>int hx509_certs_find (hx509_contextcontext, hx509_certscerts, const hx509_query *q, hx509_cert *r)</h3>
<p> Find a certificate matching the query. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a hx509 context.<br />
 <i>certs</i> certificate store to search.<br />
 <i>q</i> query allocated with <code>hx509 query functions</code> functions.<br />
 <i>r</i> return certificate (or NULL on error), should be freed with <code>hx509_cert_free()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns an hx509 error code.</dl>
<p> Return HX509_CERT_NOT_FOUND if no certificate in certs matched the query.</p>
<h3>void hx509_certs_free (hx509_certs *certs)</h3>
<p> Free a certificate store. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>certs</i> certificate store to free.</dl>
<h3>int hx509_certs_info (hx509_contextcontext, hx509_certscerts, int(*)(void *, const char *)func, void *ctx)</h3>
<p> Print some info about the certificate store. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a hx509 context.<br />
 <i>certs</i> certificate store to print information about.<br />
 <i>func</i> function that will get each line of the information, if NULL is used the data is printed on a FILE descriptor that should be passed in ctx, if ctx also is NULL, stdout is used.<br />
 <i>ctx</i> parameter to func.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns an hx509 error code.</dl>
<h3>int hx509_certs_init (hx509_contextcontext, const char *name, intflags, hx509_locklock, hx509_certs *certs)</h3>
<p> Open or creates a new hx509 certificate store. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context<br />
 <i>name</i> name of the store, format is TYPE:type-specific-string, if NULL is used the MEMORY store is used.<br />
 <i>flags</i> list of flags:</p>
<dl>
<dt>&bull;</p>
<dd> HX509_CERTS_CREATE create a new keystore of the specific TYPE.</p>
<dt>&bull;</p>
<dd> HX509_CERTS_UNPROTECT_ALL fails if any private key failed to be extracted.</dl>
<p> <i>lock</i> a lock that unlocks the certificates store, use NULL to select no password/certifictes/prompt lock (see <code>Locking and unlocking certificates and encrypted data.</code>).<br />
 <i>certs</i> return pointer, free with <code>hx509_certs_free()</code>.</dl>
<h3>int hx509_certs_iter_f (hx509_contextcontext, hx509_certscerts, int(*)(hx509_context, void *, hx509_cert)func, void *ctx)</h3>
<p> Iterate over all certificates in a keystore and call an block for each fo them. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a hx509 context.<br />
 <i>certs</i> certificate store to iterate over.<br />
 <i>func</i> block to call for each certificate. The function should return non-zero to abort the iteration, that value is passed back to the caller of hx509_certs_iter().</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns an hx509 error code. Iterate over all certificates in a keystore and call an function for each fo them.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a hx509 context.<br />
 <i>certs</i> certificate store to iterate over.<br />
 <i>func</i> function to call for each certificate. The function should return non-zero to abort the iteration, that value is passed back to the caller of <code>hx509_certs_iter_f()</code>.<br />
 <i>ctx</i> context variable that will passed to the function.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns an hx509 error code.</dl>
<p> Iterate over all certificates in a keystore and call an function for each fo them. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a hx509 context.<br />
 <i>certs</i> certificate store to iterate over.<br />
 <i>func</i> function to call for each certificate. The function should return non-zero to abort the iteration, that value is passed back to the caller of <code>hx509_certs_iter_f()</code>.<br />
 <i>ctx</i> context variable that will passed to the function.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns an hx509 error code.</dl>
<h3>int hx509_certs_merge (hx509_contextcontext, hx509_certsto, hx509_certsfrom)</h3>
<p> Merge a certificate store into another. The from store is keep intact. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a hx509 context.<br />
 <i>to</i> the store to merge into.<br />
 <i>from</i> the store to copy the object from.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns an hx509 error code.</dl>
<h3>int hx509_certs_next_cert (hx509_contextcontext, hx509_certscerts, hx509_cursorcursor, hx509_cert *cert)</h3>
<p> Get next ceritificate from the certificate keystore pointed out by cursor. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a hx509 context.<br />
 <i>certs</i> certificate store to iterate over.<br />
 <i>cursor</i> cursor that keeps track of progress.<br />
 <i>cert</i> return certificate next in store, NULL if the store contains no more certificates. Free with <code>hx509_cert_free()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns an hx509 error code.</dl>
<h3>int hx509_certs_start_seq (hx509_contextcontext, hx509_certscerts, hx509_cursor *cursor)</h3>
<p> Start the integration </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a hx509 context.<br />
 <i>certs</i> certificate store to iterate over<br />
 <i>cursor</i> cursor that will keep track of progress, free with <code>hx509_certs_end_seq()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns an hx509 error code. HX509_UNSUPPORTED_OPERATION is returned if the certificate store doesn&#8217;t support the iteration operation.</dl>
<h3>int hx509_certs_store (hx509_contextcontext, hx509_certscerts, intflags, hx509_locklock)</h3>
<p> Write the certificate store to stable storage. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>certs</i> a certificate store to store.<br />
 <i>flags</i> currently unused, use 0.<br />
 <i>lock</i> a lock that unlocks the certificates store, use NULL to select no password/certifictes/prompt lock (see <code>Locking and unlocking certificates and encrypted data.</code>).</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns an hx509 error code. HX509_UNSUPPORTED_OPERATION if the certificate store doesn&#8217;t support the store operation.</dl>
<h3>int hx509_ci_print_names (hx509_contextcontext, void *ctx, hx509_certc)</h3>
<p> Function to use to <code>hx509_certs_iter_f()</code> as a function argument, the ctx variable to <code>hx509_certs_iter_f()</code> should be a FILE file descriptor. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a hx509 context.<br />
 <i>ctx</i> used by <code>hx509_certs_iter_f()</code>.<br />
 <i>c</i> a certificate</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns an hx509 error code.</dl>
<p> Iterate over all certificates in a keystore and call an function for each fo them. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a hx509 context.<br />
 <i>certs</i> certificate store to iterate over.<br />
 <i>func</i> function to call for each certificate. The function should return non-zero to abort the iteration, that value is passed back to the caller of hx509_certs_iter().</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns an hx509 error code. Function to use to <code>hx509_certs_iter_f()</code> as a function argument, the ctx variable to <code>hx509_certs_iter_f()</code> should be a FILE file descriptor.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a hx509 context.<br />
 <i>ctx</i> used by <code>hx509_certs_iter_f()</code>.<br />
 <i>c</i> a certificate</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns an hx509 error code.</dl>
<h3>int hx509_get_one_cert (hx509_contextcontext, hx509_certscerts, hx509_cert *c)</h3>
<p> Get one random certificate from the certificate store. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a hx509 context.<br />
 <i>certs</i> a certificate store to get the certificate from.<br />
 <i>c</i> return certificate, should be freed with <code>hx509_cert_free()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns an hx509 error code.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Heimdalx509library from the source code. </p>
<h2>Index</h2>
