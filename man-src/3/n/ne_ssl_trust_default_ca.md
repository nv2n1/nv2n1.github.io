---
title: "ne_ssl_trust_default_ca(3)"
name: "ne_ssl_trust_default_ca"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ne_ssl_trust_default_ca/"
description: "ne_ssl_trust_cert, ne_ssl_trust_default_ca – functions to indicate that certificates are trusted"
---

<p>ne_ssl_trust_cert, ne_ssl_trust_default_ca &#8211; functions to indicate that certificates are trusted</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ne_session.h&gt;

void ne_ssl_trust_cert(ne_session *session, const ne_ssl_certificate *cert);

void ne_ssl_trust_default_ca(ne_session *session);</code></pre>
<h2>Description</h2>
<dd>To indicate that a given certificate is trusted by the user, the certificate object can be passed to <code>ne_ssl_trust_cert</code>. The certificate object is duplicated internally and can subsequently be destroyed. </p>
<p> The SSL library in use by neon may include a default set of CA certificates; calling the <code>ne_ssl_trust_default_ca</code> function will indicate that these CAs are trusted by the user.</p>
<h2>Examples</h2>
<p>Load the CA certificate stored in /path/to/cacert.pem: </p>
<pre><code>ne_session *sess = ne_session_create(...);
ne_ssl_certificate *cert = ne_ssl_cert_read(&quot;/path/to/cacert.pem&quot;);

if (cert) {
    ne_ssl_trust_cert(sess, cert);
    ne_ssl_cert_free(cert);
} else {
    printf(&quot;Could not load CA cert: %s
&quot;, ne_get_error(sess));
}</code></pre>
<h2>See Also</h2>
<p>ne_ssl_cert_read, ne_ssl_cert_import, ne_ssl_cert_free</p>
<h2>Author</h2>
<p><code>Joe Orton</code> &lt;neon [at] lists.manyfish.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
