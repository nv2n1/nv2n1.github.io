---
title: "ne_ssl_clicert_free(3)"
name: "ne_ssl_clicert_free"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ne_ssl_clicert_free/"
description: "ne_ssl_clicert_read, ne_ssl_clicert_name, ne_ssl_clicert_encrypted, ne_ssl_clicert_decrypt, ne_ssl_clicert_owner, ne_ssl_clicert_free – SSL client certificate handling"
---

<p>ne_ssl_clicert_read, ne_ssl_clicert_name, ne_ssl_clicert_encrypted, ne_ssl_clicert_decrypt, ne_ssl_clicert_owner, ne_ssl_clicert_free &#8211; SSL client certificate handling</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ne_ssl.h&gt;

ne_ssl_client_cert *ne_ssl_clicert_read(const char *filename);

const char *ne_ssl_clicert_name(const ne_ssl_client_cert *ccert);

int ne_ssl_clicert_encrypted(const ne_ssl_client_cert *ccert);

int ne_ssl_clicert_decrypt(ne_ssl_client_cert *ccert, const char *password);

const ne_ssl_certificate *ne_ssl_clicert_owner(const ne_ssl_client_cert *ccert);

void ne_ssl_clicert_free(ne_ssl_client_cert *ccert);</code></pre>
<h2>Description</h2>
<dd>The <code>ne_ssl_clicert_read</code> function reads a client certificate from a PKCS#12-formatted file, and returns an <code>ne_ssl_client_cert</code> object. If the client certificate is encrypted, it must be decrypted before it is used. An <code>ne_ssl_client_cert</code> object holds a client certificate and the associated private key, not just a certificate; the term &quot;client certificate&quot; will used to refer to this pair. </p>
<p> A client certificate can be in one of two states: <i>encrypted</i> or <i>decrypted</i>. The <code>ne_ssl_clicert_encrypted</code> function will return non-zero if the client certificate is in the <i>encrypted</i> state. A client certificate object returned by <code>ne_ssl_clicert_read</code> may be initially in either state, depending on whether the file was encrypted or not. </p>
<p> <code>ne_ssl_clicert_decrypt</code> can be used to decrypt a client certificate using the appropriate password. This function must only be called if the object is in the <i>encrypted</i> state; if decryption fails, the certificate state does not change, so decryption can be attempted more than once using different passwords. </p>
<p> A client certificate can be given a &quot;friendly name&quot; when it is created; <code>ne_ssl_clicert_name</code> will return this name (or NULL if no friendly name was specified). <code>ne_ssl_clicert_name</code> can be used when the client certificate is in either the encrypted or decrypted state, and will return the same string for the lifetime of the object. </p>
<p> The function <code>ne_ssl_clicert_owner</code> returns the certificate part of the client certificate; it must only be called if the client certificate is in the <i>decrypted</i> state. </p>
<p> When the client certificate is no longer needed, the <code>ne_ssl_clicert_free</code> function should be used to destroy the object.</p>
<h2>Return Value</h2>
<p><code>ne_ssl_clicert_read</code> returns a client certificate object, or NULL if the file could not be read. <code>ne_ssl_clicert_encrypted</code> returns zero if the object is in the decrypted state, or non-zero if it is in the encrypted state. <code>ne_ssl_clicert_name</code> returns a NUL-terminated friendly name string, or NULL. <code>ne_ssl_clicert_owner</code> returns a certificate object.</p>
<h2>Examples</h2>
<p>The following code reads a client certificate and decrypts it if necessary, then loads it into an HTTP session. </p>
<pre><code>ne_ssl_client_cert *ccert;

ccert = ne_ssl_clicert_read(&quot;/path/to/client.p12&quot;);

if (ccert == NULL) {
    /* handle error... */
} else if (ne_ssl_clicert_encrypted(ccert)) {
    char *password = prompt_for_password();

    if (ne_ssl_clicert_decrypt(ccert, password)) {
        /* could not decrypt! handle error... */
    }
}

ne_ssl_set_clicert(sess, ccert);</code></pre>
<h2>See Also</h2>
<p>ne_ssl_cert_read</p>
<h2>Author</h2>
<p><code>Joe Orton</code> &lt;neon [at] lists.manyfish.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
