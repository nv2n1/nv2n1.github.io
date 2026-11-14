---
title: "nuclient(5)"
name: "nuclient"
section: "5"
letter: "n"
url: "/docs/linux/man/5-nuclient/"
description: "nuclient.conf – nuauth client configuration file"
---

<p>nuclient.conf &#8211; nuauth client configuration file</p>
<h2>Synopsis</h2>
<p><code>/etc/nuclient.conf</code> </p>
<h2>Description</h2>
<p>The configuration file <code>nuclient.conf</code> is used by all nuauth clients (for ex, nutcpc or nuapplet2). </p>
<p> The file is designed to be human readable and contains a list of keywords with values that provide configuration values for libnuclient. Configuration file uses the key=value format, without spaces between around the &#8216;=&#8217; sign. </p>
<p> Global configuration file is stored in <i>CONFDIR/nuclient.conf</i> and per-user file can be stored in <i>HOME/.nufw/nuclient.conf</i>. Any variable set in the user file will overwrite the one set in the global file. </p>
<p> Original packaging and informations and help can be found from <a rel="nofollow" href="http://www.nufw.org/">http://www.nufw.org/</a></p>
<h2>Options</h2>
<p>The different configuration options are:</p>
<dl>
<dt><code>nuauth_ip </code></p>
<dd>Name of the nuauth server (fully qualified domain name, or IP address).</p>
<dt><code>nuauth_port </code></p>
<dd>Port number to use on the nuauth server (default: 4129).</p>
<dt><code>nuauth_tls_ca </code></p>
<dd>Certificate authority used to check the validity of nuauth certificate.</p>
<dt><code>nuauth_tls_cert </code></p>
<dd>Certificate file used to negotiate the TLS connection to nuauth.</p>
<dt><code>nuauth_tls_key </code></p>
<dd>Key of the certificate file from the <i>nuauth_tls_cert</i> option.</p>
<dt><code>nuauth_tls_crl </code></p>
<dd>Certificate revocation list file to use. If the client is disconnected from nuauth, it will reload this file at reconnect.</p>
<dt><code>nuauth_suppress_fqdn_verif </code></p>
<dd>If set to 1, suppress error if server FQDN does not match certificate CN (default: 0).</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-nufw/">nufw</a>(8) </p>
<p> <a href="/docs/linux/man/8-nuauth/">nuauth</a>(8) </p>
<p> <a href="/docs/linux/man/1-nutcpc/">nutcpc</a>(1)</p>
<h2>Author</h2>
<p>Nuauth was designed and coded by Eric Leblond, aka Regit (&lt;eric [at] regit.org&gt;) , and Vincent Deffontaines, aka gryzor (&lt;vincent [at] gryzor.com&gt;). Original idea in 2001, while working on NSM Ldap support. </p>
<p> This manual page was written by Pierre Chifflier. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 2 as published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts and no Back-Cover Texts.</p>
