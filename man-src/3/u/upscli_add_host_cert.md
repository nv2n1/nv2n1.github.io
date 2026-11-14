---
title: "upscli_add_host_cert(3)"
name: "upscli_add_host_cert"
section: "3"
letter: "u"
url: "/docs/linux/man/3-upscli_add_host_cert/"
description: "upscli_add_host_cert – Register a security rule for an host."
---

<p>upscli_add_host_cert &#8211; Register a security rule for an host.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;upsclient.h&gt;
void upscli_add_host_cert(const char *hostname, const char *certname,
                          int certverify, int forcessl);</code></pre>
<h2>Description</h2>
<p>The <code>upscli_add_host_cert()</code> function register a security rule associated to the <i>hostname</i>. All connections to this host use this rule. </p>
<p> The rule is composed of the certificate name <i>certname &#8216;expected for the host, &#8216;certverify</i> if the certificate must be validated for the host and <i>forcessl</i> if a secured connection must be used to connect to the host.</p>
<h2>Return Value</h2>
<p><code>upscli_add_host_cert()</code> returns no value.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-upscli_init/">upscli_init</a></code>(3), <code><a href="/docs/linux/man/3-upscli_connect/">upscli_connect</a></code>(3), <code><a href="/docs/linux/man/3-upscli_ssl/">upscli_ssl</a></code>(3), <code><a href="/docs/linux/man/3-upscli_strerror/">upscli_strerror</a></code>(3), <code><a href="/docs/linux/man/3-upscli_upserror/">upscli_upserror</a></code>(3) </p>
