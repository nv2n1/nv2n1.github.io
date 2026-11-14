---
title: "nufw(8)"
name: "nufw"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nufw/"
description: "nufw – NUFW User filtering gateway server"
---

<p>nufw &#8211; NUFW User filtering gateway server</p>
<h2>Synopsis</h2>
<p><code>nufw</code> [ <code>-h</code> ] [ <code>-V</code> ] [ <code>-D</code> ] [ <code>-m</code> ] [ <code>-v[v&#8230;]</code> ] [ <code>-s</code> ] [ <code>-S</code> ] [ <code>-N</code> ] [ <code>-A </code><i>debug_area</i> ] [ <code>-k </code><i>keyfile</i> ] [ <code>-c </code><i>certfile</i> ] [ <code>-a </code><i>cafile</i> ] [ <code>-r </code><i>crlfile</i> ] [ <code>-n </code><i>nuauth_cert_dn</i> ] [ <code>-d </code><i>address</i> ] [ <code>-p </code><i>(remote) port</i> ] [ <code>-t </code><i>timeout</i> ] [ <code>-T </code><i>track_size</i> ] [ <code>-q </code><i>NfQueue_num</i> ] [ <code>-L </code><i>Nfqueue_length</i> ] [ <code>-C</code> ] [ <code>-M</code> ] </p>
<h2>Description</h2>
<p>This manual page documents the <code>nufw</code> command. </p>
<p> nufw is the minimalist server, designed to run on the gateway(s) of the network. nufw is designed to run in conjunction with nuauth, the authenticating server. nufw receives network packets from the local firewall (on Linux 2.4 and 2.6, this is set up with the help of &#8216;-j NFQUEUE&#8217; or &#8216;-j QUEUE&#8217; netfilter target), and synchronizes with a nuauth server to check packet is authorized to travel through the gateway. </p>
<p> The design of the NUFW package lets administrator filter network traffic per user, not only per IP. This means you can now deal with different permissions for user A and user B, even if they work at the same moment, on the same multiuser machine. In other words, this extends firewalling criteria to userID, at the network scale. </p>
<p> Original packaging and informations and help can be found from <a rel="nofollow" href="http://www.nufw.org/">http://www.nufw.org/</a></p>
<h2>Options</h2>
<dl>
<dt><code>-h </code></p>
<dd>Issues usage details and exits.</p>
<dt><code>-V </code></p>
<dd>Issues version and exits.</p>
<dt><code>-D </code></p>
<dd>Run as a daemon. If started as a daemon, nufw logs message to syslog. If you don&#8217;t specify this option, messages go to the console nufw is running on, both on STDOUT and STDERR. Unless you are debugging something, you should run nufw with this option.</p>
<dt><code>-m </code></p>
<dd>Mark packets with UserID. This requires the wvmark POM patch applied to netfilter, and is necessary for per user QoS or routing.</p>
<dt><code>-v </code></p>
<dd>Increases debug level. Multiple switches are accepted and each of them increases the debug level by one. Default debug level is 2, max is 10.</p>
<dt><code>-A </code><i>debug_areas</i></p>
<dd>Chooses debug_area. Default debug area is ALL. To select a subset add value from the following list:</p>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>DEBUG_AREA_MAIN (1) main domain</p>
<dt>*</p>
<dd>DEBUG_AREA_PACKET (2) packet domain</p>
<dt>*</p>
<dd>DEBUG_AREA_USER (4) user domain</p>
<dt>*</p>
<dd>DEBUG_AREA_GW (8) Gateway domain, interaction with nufw servers.</p>
<dt>*</p>
<dd>DEBUG_AREA_AUTH (16) Authentication domain</dl>
</dl>
<dt><code>-k </code><i>keyfile</i></p>
<dd>Use specified file as SSL (private) key file.</p>
<dt><code>-c </code><i>certfile</i></p>
<dd>Use specified file as SSL (public) certificate file.</p>
<dt><code>-a </code><i>cafile</i></p>
<dd>Use specified file as SSL certificate authority file.</p>
<dt><code>-r </code><i>crlfile</i></p>
<dd>Use specified file as SSL certificate revocation list file. You will need to restart nufw if you modify this file. Since 2.2.19, nufw reloads this file dynamically when receiving a HUP signal.</p>
<dt><code>-n </code><i>nuauth_dn</i></p>
<dd>Use specified string as the needed DN of nuauth. nufw will refuse to connect if the provided string does not match the DN of the certificate provided by nuauth. If you do not use this option, the DN of the nuauth certificate will be checked against the fully qualified domain name of the nuauth server, obtained from a reverse DNS lookup on nuauth IP address.</p>
<dt><code>-s </code></p>
<dd>Disable strict TLS checking of the certificate provided by nuauth.</p>
<dt><code>-S </code></p>
<dd>Force strict TLS checking of the certificate provided by nuauth. This is the default behavior of the daemon since 2.2.18.</p>
<dt><code>-N </code></p>
<dd>Suppress error if server FQDN does not match certificate CN.</p>
<dt><code>-d </code><i>address</i></p>
<dd>Network address of the nuauth server.</p>
<dt><code>-p </code><i>port</i></p>
<dd>Specifies TCP port to send data to when addressing the nuauth server. Nuauth server must be setup to listen on that port. Default value : 4128</p>
<dt><code>-t </code><i>seconds</i></p>
<dd>Specifies timeout to forget packets not answered for by nuauth. Default value : 15 s.</p>
<dt><code>-T </code><i>track_size</i></p>
<dd>Set maximum number of packets that can wait a decision in nufw. Default value : 1000.</p>
<dt><code>-q </code><i>NfQueue number</i></p>
<dd>If Nufw was compiled with NfQueue support, Id of the NfQueue to use (default : 0).</p>
<dt><code>-L </code><i>NfQueue length</i></p>
<dd>Specify the length of the nfnetlink queue used by nufw. This is the number of packets that the kernel will keep internally before dropping new coming packets.</p>
<dt><code>-C </code></p>
<dd>Listen to conntrack events (needed for connection expiration).</p>
<dt><code>-M </code></p>
<dd>Only report event on marked connections to nuauth (implies -C and -m) </p>
<p> This is the way to do an efficient selection of events to be sent to nuauth but this REQUIRES a kernel with transmit_mark applied (should be ok for 2.6.18+) and the use of CONNMARK to propagate the initial mark across all the packets of the connection.</dl>
<h2>Signals</h2>
<p>The <code>nufw</code> daemon is designed to deal with several signals : USR1, USR2, SYS, WINCH and POLL.</p>
<dl>
<dt><code>USR1 </code></p>
<dd>Increases verbosity. The daemon then acts as if it had been launched with one supplementary &#8216;-v&#8217;.A line is also added to the system log to mention the signal event.</p>
<dt><code>USR2 </code></p>
<dd>Decreases verbosity. The daemon then acts as if it had been launched with one less &#8216;-v&#8217;. A line is also added to the system log to mention the signal event.</p>
<dt><code>SYS </code></p>
<dd>Removes the Conntrack events thread. This gets the daemon to work as if the &quot;-C&quot; switch had not been set. This is useful on HA configurations, when one firewall gets passive, for instance.</p>
<dt><code>WINCH </code></p>
<dd>Starts the Conntrack events thread. This gets the daemon to work as if the &quot;-C&quot; switch had been set at startup. This is useful on HA configurations, when one firewall gets active, for instance.</p>
<dt><code>POLL </code></p>
<dd>Logs an &quot;audit&quot; line, mentionning how many network datagrams were received and sent since daemon startup.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-nuauth/">nuauth</a>(8)</p>
<h2>Author</h2>
<p>Nufw was designed and coded by Eric Leblond, aka Regit (&lt;eric [at] regit.org&gt;) , and Vincent Deffontaines, aka gryzor (&lt;vincent [at] gryzor.com&gt;). Original idea in 2001, while working on NSM Ldap support. </p>
<p> This manual page was written by Vincent Deffontaines </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 2 as published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts and no Back-Cover Texts.</p>
