---
title: "nuauth(8)"
name: "nuauth"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nuauth/"
description: "nuauth – NUFW authentication server"
---

<p>nuauth &#8211; NUFW authentication server</p>
<h2>Synopsis</h2>
<p><code>nuauth</code> [ <code>-h</code> ] [ <code>-V</code> ] [ <code>-v[v&#8230;]</code> ] [ <code>-l </code><i>(local, for clients) port</i> ] [ <code>-C </code><i>(local, for clients) address</i> ] [ <code>-L </code><i>(local, for nufw) address</i> ] [ <code>-p </code><i>(local, for nufw) port</i> ] [ <code>-t </code><i>timeout</i> ] [ <code>-D</code> ] </p>
<h2>Description</h2>
<p>This manual page documents the <code>nuauth</code> command. </p>
<p> Nuauth is the authentication server of the NUFW package. Whenever a client sends a <a href="/docs/linux/man/1-packet/">packet</a>(1) to start a connection through the gateway, the client program (nutcpc), installed on the client&#8217;s station, sends an authentication <a href="/docs/linux/man/2-packet/">packet</a>(2) to nuauth. The gateway&#8217;s firewall queues the <a href="/docs/linux/man/1-packet/">packet</a>(1) and sends informations about it directly to the nuauth server. Nuauth&#8217;s job is to analyse both <a href="/docs/linux/man/1-packets/">packets</a>(1) and (2), and check user owns the right to initialize the connection (s)he has tried to. If Nuauth finds so, Nuauth sends authorization to Nufw to accept the <a href="/docs/linux/man/1-packet/">packet</a>(1) through, and the connection gets initialized. If not, the connection is Dropped. </p>
<p> Nuauth can use a backend LDAP server for user and groups definitions, as well as Access Lists associated with those groups. Interface to Users/Groups database can also be performed through PAM/NSS. An option is also to store the user database in DBM files. It should be noted that dynamic modifications of the users base can currently only be performed if an LDAP database is used. </p>
<p> Original packaging and informations and help can be found from <a rel="nofollow" href="http://www.nufw.org/">http://www.nufw.org/</a></p>
<h2>Options</h2>
<dl>
<dt><code>-h </code></p>
<dd>Issues usage details and exits.</p>
<dt><code>-V </code></p>
<dd>Issues version and exits.</p>
<dt><code>-v </code></p>
<dd>Increases verbosity level. Multiple switches are accepted and each of them increases the verbosity level by one. Default verbosity level is 2, max is 10.</p>
<dt><code>-l </code><i>port</i></p>
<dd>Specifies TCP port to listen on for clients. Default value : 4129</p>
<dt><code>-L </code><i>address</i></p>
<dd>Address to listen on for NuFW packets. Default : 127.0.0.1</p>
<dt><code>-C </code><i>address</i></p>
<dd>Address to listen on for clients packets. Default : 0.0.0.0</p>
<dt><code>-d </code><i>address</i></p>
<dd>Network address of the nufw (gateway) servers. Only NuFW servers at those addresses will be allowed to talk to nuauth.</p>
<dt><code>-p </code><i>port</i></p>
<dd>This option is DEPRECATED and was in use only in v1 of the protocol, which was proof of concept, non-encrypted. </p>
<p> Specifies UDP port to send data to when addressing the nufw (gateway) server. Nufw server must be setup to listen on that port. Default value : 4128</p>
<dt><code>-t </code><i>seconds</i></p>
<dd>Specifies timeout to forget packets not identified, and identification packets matching nothing. Default value : 15 s.</p>
<dt><code>-D </code></p>
<dd>Run as a daemon. If started as a daemon, nuauth logs message to syslog. If you don&#8217;t specify this option, messages go to the console nuauth is running on, both on STDOUT and STDERR. Unless you are debugging something, you should run nuauth with this option.</dl>
<h2>Signals</h2>
<p>The <code>nuauth</code> daemon is designed to deal with several signals : HUP, USR1, USR2, and POLL.</p>
<dl>
<dt><code>HUP </code></p>
<dd>Reload configuration. The <code>nuauth</code> daemon reloads its configuration when receiving this signal. Since 2.2.19, it also refreshes the CRL file content.</p>
<dt><code>USR1 </code></p>
<dd>Increases verbosity. The daemon then acts as if it had been launched with one supplementary &#8216;-v&#8217;.A line is also added to the system log to mention the signal event.</p>
<dt><code>USR2 </code></p>
<dd>Decreases verbosity. The daemon then acts as if it had been launched with one less &#8216;-v&#8217;. A line is also added to the system log to mention the signal event.</p>
<dt><code>POLL </code></p>
<dd>Logs an &quot;audit&quot; line, mentioning how many network datagrams were received and sent since daemon startup.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-nufw/">nufw</a>(8)</p>
<h2>Author</h2>
<p>Nuauth was designed and coded by Eric Leblond, aka Regit (&lt;eric [at] regit.org&gt;) , and Vincent Deffontaines, aka gryzor (&lt;vincent [at] gryzor.com&gt;). Original idea in 2001, while working on NSM Ldap support. </p>
<p> This manual page was written by Vincent Deffontaines </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 2 as published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts and no Back-Cover Texts.</p>
