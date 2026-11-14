---
title: "racoon2-iked(8)"
name: "racoon2-iked"
section: "8"
letter: "r"
url: "/docs/linux/man/8-racoon2-iked/"
description: "iked – Internet Key Exchange protocol daemon"
---

<p><code>iked</code> &#8211; Internet Key Exchange protocol daemon</p>
<h2>Synopsis</h2>
<p>[-<code>46hvFV</code> ] [-<code>f </code><i>configfile</i> ] [-<code>l </code><i>logfile</i> ] [-<code>p </code><i>port</i> ] [-<code>I </code><i>peer-address</i> ] [-<code>S </code><i>selector-index</i> ] [-<code>d</code> ] [-<code>D </code><i>level</i> ] [-<code>P </code><i>outfile</i> ]</p>
<h2>Description</h2>
<p>is a key management daemon, which supports the Internet Key Exchange (IKE) protocol version 1 (RFC2409) and version 2 (RFC4306). It is driven by upcalls from the kernel via the PF_KEYv2 interface or by negotiation requests from remote peers, and manages IPsec SAs according to racoon2.conf </p>
<p> The following options are available:</p>
<dl>
<dt><code>-4</code></p>
<dd>Use IPv4 addresses only for local sockets.</p>
<dt><code>-6</code></p>
<dd>Use IPv6 addresses only for local sockets.</p>
<dt><code>-d</code></p>
<dd>Increase the debugging level. This flag may occur multiple times.</p>
<dt><code>-f </code><i>configfile</i></p>
<dd>Read configurations from the specified file.</p>
<dt><code>-I </code><i>peer-address</i></p>
<dd>Immediately initiate to the peer specified.</p>
<dt><code>-S </code><i>selector_index</i></p>
<dd>Immediately initiate using the selector specified.</p>
<dt><code>-h</code></p>
<dd>Show simple help messages.</p>
<dt><code>-l </code><i>logfile</i></p>
<dd>Output log to logfile instead of syslog.</p>
<dt><code>-p </code><i>portnum</i></p>
<dd>Specify default port number for IKE sockets.</p>
<dt><code>-v</code></p>
<dd>Output log to stdout in addition to syslog.</p>
<dt><code>-D </code><i>num</i></p>
<dd>Set debug flag.</p>
<dt><code>-F</code></p>
<dd>Run in the foreground. does not detach itself from the terminal and does not become a daemon. Logs are output to the stderr.</p>
<dt><code>-P </code><i>outfile</i></p>
<dd>Record unencrypted IKE communication packets to the file. This option is available only if was compiled with &#8211;enable-pcap configuration option.</p>
<dt><code>-V</code></p>
<dd>Show the version.</dl>
<p> Upon receiving SIGINT or SIGTERM, shuts down IKEv2 IKE_SAs with peer nodes by sending Informational exchange with Delete payload, deletes relevant IPsec SAs, and then exits. Upon receiving SIGHUP, similarly shuts down IKEv2 IKE_SAs and deletes relevant IPsec SAs, then reloads the configuration file. </p>
<p> IPsec policies are managed by <a href="/docs/linux/man/8-spmd/">spmd</a>(8), thus it must be started before <code>.</code> When <a href="/docs/linux/man/8-spmd/">spmd</a>(8) restarts, needs to be reloaded to reconnect with it.</p>
<h2>Files</h2>
<dl>
<dt><code>@sysconfdir@/racoon2.conf </code></p>
<dd>The default configuration file for racoon2.</p>
<dt><code>/var/run/iked.pid </code></p>
<dd>The PID file of the current instance of the daemon.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/7-racoon2/">racoon2</a>(7), racoon2.conf5, <a href="/docs/linux/man/8-spmd/">spmd</a>(8), <a href="/docs/linux/man/8-kinkd/">kinkd</a>(8), <a href="/docs/linux/man/4-ipsec/">ipsec</a>(4)</p>
<dl>
<dd><i>&quot;The Internet Key Exchange (IKE)&quot;</i> <i>RFC2409</i> November 1998</dl>
<dl>
<dd><i>&quot;Internet Key Exchange (IKEv2) Protocol</i> <i>RFC4306</i> December 2005</dl>
<h2>History</h2>
<p>The command was developed for racoon2 in 2004-2005.</p>
<h2>Authors</h2>
<p>was written and is maintained by An WIDE/racoon2 project Aq <a rel="nofollow" href="http://www.racoon2.wide.ad.jp/">http://www.racoon2.wide.ad.jp/</a></p>
<h2>Acknowledgements</h2>
<p>Part of the codes are derived from ipsec-tools racoon daemon, which was derived from KAME racoon daemon.</p>
<h2>Bugs</h2>
<p>&quot;default&quot; clause of configuration file is used for two purposes: to provide default values for individual field for other sections of configuration, and to specify default kmp configuration when the responder received a message from unknown peer. In latter case, when &quot;default&quot; clause lacks some necessary fields, error message may be cryptic, since it is not checked by configuration check routine of iked. (Probably it will result in &quot;no proposal chosen&quot;.) On FreeBSD/NetBSD, when IPsec SA expires by IPsec SA lifetime, kernel does not notify iked about the sa expiration. To remedy this, iked maintains its own expiration timer for each IPsec SA. Since the iked can&#8217;t know how much bytes used for the SA, lifetime_bytes in the configuration are ignored for now. SA bundles (e.g. AH+ESP) does not conform to protocol spec. After rekeying IKE_SA, iked may spit some warning messages, if the rekey negotiation or delete request was started from both ends at once. </p>
