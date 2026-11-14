---
title: "ne_ssl_cert_subject(3)"
name: "ne_ssl_cert_subject"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ne_ssl_cert_subject/"
description: "ne_ssl_cert_identity, ne_ssl_cert_signedby, ne_ssl_cert_issuer, ne_ssl_cert_subject – functions to access certificate properties"
---

<p>ne_ssl_cert_identity, ne_ssl_cert_signedby, ne_ssl_cert_issuer, ne_ssl_cert_subject &#8211; functions to access certificate properties</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ne_ssl.h&gt;

const char *ne_ssl_cert_identity(const ne_ssl_certificate *cert);

const ne_ssl_certificate *ne_ssl_cert_signedby(const ne_ssl_certificate *cert);

const ne_ssl_dname *ne_ssl_cert_subject(const ne_ssl_certificate *cert);

const ne_ssl_dname *ne_ssl_cert_issuer(const ne_ssl_certificate *cert);</code></pre>
<h2>Description</h2>
<dd>The function <code>ne_ssl_cert_identity</code> retrieves the &#8220;identity&#8221; of a certificate; for an SSL server certificate, this will be the hostname for which the certificate was issued. In PKI parlance, the identity is the <i>common name</i> attribute of the distinguished name of the certificate subject. </p>
<p> The functions <code>ne_ssl_cert_subject</code> and <code>ne_ssl_cert_issuer</code> can be used to access the objects representing the distinguished name of the subject and of the issuer of a certificate, respectively. </p>
<p> If a certificate object is part of a certificate chain, then <code>ne_ssl_cert_signedby</code> can be used to find the certificate which signed a particular certificate. For a self-signed certificate or a certificate for which the full chain is not available, this function will return NULL.</p>
<h2>Return Value</h2>
<p><code>ne_ssl_cert_issuer</code> and <code>ne_ssl_cert_subject</code> are guaranteed to never return NULL. <code>ne_ssl_cert_identity</code> may return NULL if the certificate has no specific &#8220;identity&#8221;. <code>ne_ssl_cert_signedby</code> may return NULL as covered above.</p>
<h2>Examples</h2>
<p>The following function could be used to display information about a given certificate: </p>
<pre><code>void dump_cert(const ne_ssl_certificate *cert)
{
    const char *id = ne_ssl_cert_identity(cert);
    char *dn;

    if (id)
        printf(&quot;Certificate was issued for '%s'.
&quot;, id);

    dn = ne_ssl_readable_dname(ne_ssl_cert_subject(cert));
    printf(&quot;Subject: %s
&quot;, dn);
    free(dn);

    dn = ne_ssl_readable_dname(ne_ssl_cert_issuer(cert));
    printf(&quot;Issuer: %s
&quot;, dn);
    free(dn);
}</code></pre>
<h2>See Also</h2>
<p>ne_ssl_cert_cmp, ne_ssl_readable_dname</p>
<h2>Author</h2>
<p><code>Joe Orton</code> &lt;neon [at] lists.manyfish.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
