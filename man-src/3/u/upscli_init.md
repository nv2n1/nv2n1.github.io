---
title: "upscli_init(3)"
name: "upscli_init"
section: "3"
letter: "u"
url: "/docs/linux/man/3-upscli_init/"
description: "upscli_init – Initialize upsclient module specifying security properties."
---

<p>upscli_init &#8211; Initialize upsclient module specifying security properties.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;upsclient.h&gt;
int upscli_init(int certverify, const char *certpath,
                const char *certname, const char *certpasswd);</code></pre>
<h2>Description</h2>
<p>The <code>upscli_init()</code> function initialize upsclient module and set many SSL-related properties: <i>certverify</i> to 1 makes certificate verification required for all SSL connections and <i>certpath</i> is the location of certificate database. </p>
<p> If compiled with OpenSSL, certpath refers to a .pem file containing certificates and if compiled with NSS, certpath refers to a directory containing database files. </p>
<p> If compiled with NSS and using SSL, you can specify <i>certname</i> the name of the certificate to send to upsd and <i>certpasswd</i> the password used to decrypt certificate private key. </p>
<p> You can call <code><a href="/docs/linux/man/3-upscli_add_host_cert/">upscli_add_host_cert</a></code>(3) to register specific host security policy before initialize connections to them. </p>
<p> You must call <code><a href="/docs/linux/man/3-upscli_cleanup/">upscli_cleanup</a></code>(3) when exiting application.</p>
<h2>Return Value</h2>
<p>The <code>upscli_init()</code> function returns 1 on success, or -1 if an error occurs.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-upscli_add_host_cert/">upscli_add_host_cert</a></code>(3), <code><a href="/docs/linux/man/3-upscli_cleanup/">upscli_cleanup</a></code>(3), <code><a href="/docs/linux/man/3-upscli_disconnect/">upscli_disconnect</a></code>(3), <code><a href="/docs/linux/man/3-upscli_fd/">upscli_fd</a></code>(3), <code><a href="/docs/linux/man/3-upscli_splitaddr/">upscli_splitaddr</a></code>(3), <code><a href="/docs/linux/man/3-upscli_splitname/">upscli_splitname</a></code>(3), <code><a href="/docs/linux/man/3-upscli_ssl/">upscli_ssl</a></code>(3), <code><a href="/docs/linux/man/3-upscli_strerror/">upscli_strerror</a></code>(3), <code><a href="/docs/linux/man/3-upscli_upserror/">upscli_upserror</a></code>(3) </p>
