---
title: "racoon(8)"
name: "racoon"
section: "8"
letter: "r"
url: "/docs/linux/man/8-racoon/"
description: "racoon – IKE (ISAKMP/Oakley) key management daemon"
---

<p><code>racoon</code> &#8211; IKE (ISAKMP/Oakley) key management daemon</p>
<h2>Synopsis</h2>
<p><code>racoon</code> -words [-<code>46BdFLVv </code>-words ] [-<code>f </code><i>configfile</i> ] -words [-<code>l </code><i>logfile</i> ] -words [-<code>P </code><i>isakmp-natt-port</i> ] -words [-<code>p </code><i>isakmp-port</i> ]</p>
<h2>Description</h2>
<p><code>racoon</code> speaks the IKE (ISAKMP/Oakley) key management protocol, to establish security associations with other hosts. The SPD (Security Policy Database) in the kernel usually triggers <code>.</code> <code>racoon</code> usually sends all informational messages, warnings and error messages to <a href="/docs/linux/man/8-syslogd/">syslogd</a>(8) with the facility <code>LOG_DAEMON</code> and the priority <code>LOG_INFO</code> Debugging messages are sent with the priority <code>LOG_DEBUG</code> You should configure syslog.conf5 appropriately to see these messages.</p>
<dl>
<dt><code>-4</code></p>
<dd>
<dt><code>-6</code></p>
<dd>Specify the default address family for the sockets.</p>
<dt><code>-B</code></p>
<dd>Install SA(s) from the file which is specified in racoon.conf5.</p>
<dt><code>-d</code></p>
<dd>Increase the debug level. Multiple &#8211;<code>d</code> arguments will increase the debug level even more.</p>
<dt><code>-F</code></p>
<dd>Run <code>racoon</code> in the foreground.</p>
<dt><code>-f </code><i>configfile</i></p>
<dd>Use <i>configfile</i> as the configuration file instead of the default.</p>
<dt><code>-L</code></p>
<dd>Include <i>file_name:line_number:function_name</i> in all messages.</p>
<dt><code>-l </code><i>logfile</i></p>
<dd>Use <i>logfile</i> as the logging file instead of <a href="/docs/linux/man/8-syslogd/">syslogd</a>(8).</p>
<dt><code>-P </code><i>isakmp-natt-port</i></p>
<dd>Use <i>isakmp-natt-port</i> for NAT-Traversal port-floating. The default is 4500.</p>
<dt><code>-p </code><i>isakmp-port</i></p>
<dd>Listen to the ISAKMP key exchange on port <i>isakmp-port</i> instead of the default port number, 500.</p>
<dt><code>-V</code></p>
<dd>Print racoon version and compilation options and exit.</p>
<dt><code>-v</code></p>
<dd>This flag causes the packet dump be more verbose, with higher debugging level.</dl>
<p> <code>racoon</code> assumes the presence of the kernel random number device <a href="/docs/linux/man/4-rnd/">rnd</a>(4) at /dev/urandom</p>
<h2>Return Values</h2>
<p>The command exits with 0 on success, and non-zero on errors.</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/racoon.conf </code></p>
<dd>default configuration file.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/4-ipsec/">ipsec</a>(4), racoon.conf5, syslog.conf5, <a href="/docs/linux/man/8-setkey/">setkey</a>(8), <a href="/docs/linux/man/8-syslogd/">syslogd</a>(8)</p>
<h2>History</h2>
<p>The <code>racoon</code> command first appeared in the &#8220;YIPS&#8221; Yokogawa IPsec implementation.</p>
<h2>Security Considerations</h2>
<p>The use of IKE phase 1 aggressive mode is not recommended, as described in <a rel="nofollow" href="http://www.kb.cert.org/vuls/id/886601">http://www.kb.cert.org/vuls/id/886601</a></p>
