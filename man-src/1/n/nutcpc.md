---
title: "nutcpc(1)"
name: "nutcpc"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nutcpc/"
description: "nutcpc – NuFW console-mode client for GNU/Linux and BSD systems"
---

<h2 class="name">NAME</h2>
<p> nutcpc &#8211; NuFW console-mode client for GNU/Linux and BSD systems </p>
<h2>SYNOPSIS</h2>
<p> <code>nutcpc</code> [ <code>-d </code> ] [ <code>-l </code> ] [ <code>-k </code> ] [ <code>-c </code> ] [ <code>-V </code> ] [ <code>-h </code> ] [ <code>-q </code> ] [ <code>-Q </code> ] [ <code>-N </code> ] [ <code>-H </code><i>Nuauth IP</i> ] [ <code>-p </code><i>Nuauth port </i> ] [ <code>-U </code><i>UserID</i> ] [ <code>-P </code><i>UserPassword</i> ] [ <code>-I </code><i>Interval</i> ] [ <code>-Z </code><i>Service</i> ] [ <code>-C </code><i>CertFile</i> ] [ <code>-A </code><i>AuthorityFile</i> ] [ <code>-K </code><i>KeyFile</i> ] [ <code>-W </code><i>CertPass</i> ] [ <code>-R </code><i>CrlFile</i> ] [ <code>-a </code><i>NuauthDN</i> ] </p>
<h2>DESCRIPTION</h2>
<p> This manual page documents the <code>nutcpc</code> command. </p>
<p> nutcpc is a console-mode client for the NuFW authenticating firewall. It sends authentication packets to the nuauth server. All parameters can be set on commandline but nutcpc can also be configured via the file <a href="/docs/linux/man/5-nuclient-conf/">nuclient.conf</a>(5). </p>
<p> Original packaging and informations and help can be found from <a rel="nofollow" href="http://www.nufw.org/">http://www.nufw.org/</a></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d </code></p>
<dd> Debug mode, don&#8217;t go into background.</p>
<dt><code>-l </code></p>
<dd> Do not verify whether lock file exists before starting. And do not create lock file.</p>
<dt><code>-k </code></p>
<dd> Kill existing instances of the program running on our local userID.</p>
<dt><code>-c </code></p>
<dd> Check if a client is already running. Return error if no client are running.</p>
<dt><code>-V </code></p>
<dd> Issues program version and exits.</p>
<dt><code>-h </code></p>
<dd> Issues usage details and exits.</p>
<dt><code>-q </code></p>
<dd> Do not display running nutcpc options on &quot;ps&quot;. Useful when using &quot;-W&quot;</p>
<dt><code>-H </code><i>Nuauth IP</i></p>
<dd> Send authentication packet to <i>Nuauth IP</i>.</p>
<dt><code>-p </code><i>Nuauth port</i></p>
<dd> Send authentication packet to <i>Nuauth port</i>.</p>
<dt><code>-U </code><i>User ID</i></p>
<dd> Set nufw userid to <i>User ID</i>.</p>
<dt><code>-P </code><i>User Password</i></p>
<dd> Set nufw password to <i>User Password</i>.</p>
<dt><code>-I </code><i>Interval</i></p>
<dd> Set connection list refresh interval to <i>Interval</i>. This option is only useful if nuauth server is in POLL mode.</p>
<dt><code>-Z </code><i>Service</i></p>
<dd> Set kerberos service name to <i>Service</i>.</p>
<dt><code>-C </code><i>CertFile</i></p>
<dd> Use certificate file stored in the file <i>CertFile</i> to negotiate the TLS connection to nuauth.</p>
<dt><code>-A </code><i>AuthorityFile</i></p>
<dd> Use authority file stored in <i>AuthorityFile</i> and check the validity of nuauth certificate against this authority. Nutcpc will leave if this is not the case.</p>
<dt><code>-K </code><i>KeyFile</i></p>
<dd> Use key file stored in the file <i>KeyFile</i> to negotiate the TLS connection to nuauth.</p>
<dt><code>-W </code><i>CertPass</i></p>
<dd> Use the passphrase <i>CertPass</i> to decrypt the certificate. Check the <i>-q</i> option if you use this.</p>
<dt><code>-R </code><i>CrlFile</i></p>
<dd> Use certificate revocation list file stored in the file <i>CrlFile</i> to negotiate the TLS connection to nuauth. nutcpc reloads this file if it gets disconnected from nuauth and needs to reconnect. Since version 2.2.19, nutcpc reloads the CRL file when receiving a HUP signal.</p>
<dt><code>-a </code><i>NuauthDN</i></p>
<dd> Verify that the certificate given by nuauth has a DN equal to <i>NuauthDN</i>. Nutcpc will leave if this is not the case.</p>
<dt><code>-Q </code></p>
<dd> Suppress warning if no certificate authority is configured.</p>
<dt><code>-N </code></p>
<dd> Suppress error if server FQDN does not match certificate CN.</dl>
<h2>LOCK FILE</h2>
<p> By default, the lock file set by nutcpc is at ~/.nufw/nutcpc.</p>
<h2>CERTIFICATE AUTHENTICATION</h2>
<p> User authentication can be done using a certificate and a private key. Such a method will be used, if nutcpc can find a certificate at ~/.nufw/cert.pem and the corresponding private key at ~/.nufw/key.pem. The server identity will be checked if a CA certificate is provided in ~/.nufw/cacert.pem. Certificates and key can also be provided on command line or via <a href="/docs/linux/man/5-nuclient-conf/">nuclient.conf</a>(5).</p>
<h2>SIGNALS</h2>
<dl>
<dt><code>HUP </code></p>
<dd> When receiving this signal, nutcpc attempts to immediately reconnect to the server, if disconnected. The signal is ignored in other cases.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-nufw/">nufw</a>(8) </p>
<p> <a href="/docs/linux/man/8-nuauth/">nuauth</a>(8) </p>
<p> <a href="/docs/linux/man/5-nuclient-conf/">nuclient.conf</a>(5)</p>
<h2>AUTHOR</h2>
<p> Nuauth was designed and coded by Eric Leblond, aka Regit (&lt;eric [at] regit.org&gt;) , and Vincent Deffontaines, aka gryzor (&lt;vincent [at] gryzor.com&gt;). Original idea in 2001, while working on NSM Ldap support. </p>
<p> This manual page was written by Eric Leblond. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 2 as published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts and no Back-Cover Texts. </p>
<h2>Index</h2>
