---
title: "ne_ssl_set_verify(3)"
name: "ne_ssl_set_verify"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ne_ssl_set_verify/"
description: "ne_ssl_set_verify – register an SSL certificate verification callback"
---

<p>ne_ssl_set_verify &#8211; register an SSL certificate verification callback</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ne_session.h&gt;

typedef int ne_ssl_verify_fn(void *userdata, int failures, const ne_ssl_certificate *cert);

void ne_ssl_set_verify(ne_session *session, ne_ssl_verify_fn verify_fn, void *userdata);</code></pre>
<h2>Description</h2>
<dd>To enable manual SSL certificate verification, a callback can be registered using <code>ne_ssl_set_verify</code>. If such a callback is not registered, when a connection is established to an SSL server which does not present a certificate signed by a trusted CA (see ne_ssl_trust_cert), or if the certificate presented is invalid in some way, the connection will fail. </p>
<p> When the callback is invoked, the <i>failures</i> parameter gives a bitmask indicating in what way the automatic certificate verification failed. The value is equal to the bit-wise OR of one or more of the following constants (and is guaranteed to be non-zero): </p>
<p> <code>NE_SSL_NOTYETVALID</code></p>
<dl>
<dd>The certificate is not yet valid.</dl>
<p> <code>NE_SSL_EXPIRED</code></p>
<dl>
<dd>The certificate has expired.</dl>
<p> <code>NE_SSL_IDMISMATCH</code></p>
<dl>
<dd>The hostname used for the session does not match the hostname to which the certificate was issued.</dl>
<p> <code>NE_SSL_UNTRUSTED</code></p>
<dl>
<dd>The Certificate Authority which signed the certificate is not trusted.</dl>
<p> Note that if either of the <code>NE_SSL_IDMISMATCH</code> or <code>NE_SSL_UNTRUSTED</code> failures is given, the connection may have been intercepted by a third party, and must not be presumed to be &#8220;secure&#8221;. </p>
<p> The <i>cert</i> parameter passed to the callback represents the certificate which was presented by the server. If the server presented a chain of certificates, the chain can be accessed using ne_ssl_cert_signedby. The <i>cert</i> object given is not valid after the callback returns.</p>
<h2>Return Value</h2>
<p>The verification callback must return zero to indicate that the certificate should be trusted; and non-zero otherwise (in which case, the connection will fail).</p>
<h2>Examples</h2>
<p>The following code implements an example verification callback, using the <code>dump_cert</code> function from ne_ssl_cert_subject to display certification information. Notice that the hostname of the server used for the session is passed as the <i>userdata</i> parameter to the callback. </p>
<pre><code>static int
my_verify(void *userdata, int failures, const ne_ssl_certificate *cert)
{
    const char *hostname = userdata;

    dump_cert(cert);

    puts(&quot;Certificate verification failed - the connection may have been &quot;
         &quot;intercepted by a third party!&quot;);

    if (failures &amp; NE_SSL_IDMISMATCH) {
        const char *id = ne_ssl_cert_identity(cert);
        if (id)
            printf(&quot;Server certificate was issued to '%s' not '%s'.
&quot;,
                   id, hostname);
        else
            printf(&quot;The certificate was not issued for '%s'
&quot;, hostname);
    }

    if (failures &amp; NE_SSL_UNTRUSTED)
        puts(&quot;The certificate is not signed by a trusted Certificate Authority.&quot;);

    /* ... check for validity failures ... */

    if (prompt_user())
        return 1; /* fail verification */
    else
        return 0; /* trust the certificate anyway */
}

int main(...)
{
    ne_session *sess = ne_session_create(&quot;https&quot;, &quot;some.host.name&quot;, 443);
    ne_ssl_set_verify(sess, my_verify, &quot;some.host.name&quot;);
    ...
}</code></pre>
<h2>See Also</h2>
<p>ne_ssl_trust_cert, ne_ssl_readable_dname, ne_ssl_cert_subject</p>
<h2>Author</h2>
<p><code>Joe Orton</code> &lt;neon [at] lists.manyfish.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
