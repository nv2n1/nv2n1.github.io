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
<p><code>racoon</code> speaks the IKE (ISAKMP/Oakley) key management protocol, to establish security associations with other hosts. The SPD (Security Policy Database) in the kernel usually triggers <code>.</code> <code>racoon</code> usually sends all informational messages, warnings and error messages to syslogd(8) with the facility <code>LOG_DAEMON</code> and the priority <code>LOG_INFO</code> Debugging messages are sent with the priority <code>LOG_DEBUG</code> You should configure syslog.conf5 appropriately to see these messages.</p>
<dl>
<dt><code>-4</code></dt>
<dd>
</dd><dt><code>-6</code></dt>
<dd>Specify the default address family for the sockets.</dd>
<dt><code>-B</code></dt>
<dd>Install SA(s) from the file which is specified in racoon.conf5.</dd>
<dt><code>-d</code></dt>
<dd>Increase the debug level. Multiple &#8211;<code>d</code> arguments will increase the debug level even more.</dd>
<dt><code>-F</code></dt>
<dd>Run <code>racoon</code> in the foreground.</dd>
<dt><code>-f </code><i>configfile</i></dt>
<dd>Use <i>configfile</i> as the configuration file instead of the default.</dd>
<dt><code>-L</code></dt>
<dd>Include <i>file_name:line_number:function_name</i> in all messages.</dd>
<dt><code>-l </code><i>logfile</i></dt>
<dd>Use <i>logfile</i> as the logging file instead of syslogd(8).</dd>
<dt><code>-P </code><i>isakmp-natt-port</i></dt>
<dd>Use <i>isakmp-natt-port</i> for NAT-Traversal port-floating. The default is 4500.</dd>
<dt><code>-p </code><i>isakmp-port</i></dt>
<dd>Listen to the ISAKMP key exchange on port <i>isakmp-port</i> instead of the default port number, 500.</dd>
<dt><code>-V</code></dt>
<dd>Print racoon version and compilation options and exit.</dd>
<dt><code>-v</code></dt>
<dd>This flag causes the packet dump be more verbose, with higher debugging level.</dd></dl>
<p> <code>racoon</code> assumes the presence of the kernel random number device rnd(4) at /dev/urandom</p>
<h2>Return Values</h2>
<p>The command exits with 0 on success, and non-zero on errors.</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/racoon.conf </code></dt>
<dd>default configuration file.</dd></dl>
<h2>See Also</h2>
<p>ipsec(4), racoon.conf5, syslog.conf5, <a href="/docs/linux/man/8-setkey/">setkey</a>(8), syslogd(8)</p>
<h2>History</h2>
<p>The <code>racoon</code> command first appeared in the &#8220;YIPS&#8221; Yokogawa IPsec implementation.</p>
<h2>Security Considerations</h2>
<p>The use of IKE phase 1 aggressive mode is not recommended, as described in <a rel="nofollow" href="http://www.kb.cert.org/vuls/id/886601">http://www.kb.cert.org/vuls/id/886601</a></p>
