---
title: "ntpstat(8)"
name: "ntpstat"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ntpstat/"
description: "ntpstat – show network time synchronisation status"
---

<p>ntpstat &#8211; show network time synchronisation status</p>
<h2>Synopsis</h2>
<p><code>ntpstat</code></p>
<h2>Description</h2>
<p><i>ntpstat</i> will report the synchronisation state of the NTP daemon (ntpd) running on the local machine. If the local system is found to be synchronised to a reference time source, <i>ntpstat</i> will report the approximate time accuracy. When the synchronised state is reported, it means the system clock was updated at some point. There is no timeout for this state. It will stay there even when the source becomes unreachable and there are no other sources available. However, the reported accuracy will be slowly increasing, in the default ntpd configuration by 15 microseconds per second. </p>
<h2>Returns</h2>
<p><i>ntpstat</i> returns 0 if clock is synchronised. <i>ntpstat</i> returns 1 if clock is not synchronised. <i>ntpstat</i> returns 2 if clock state is indeterminant, for example if ntpd is not contactable.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-ntp_misc/">ntp_misc</a></code>(5), <code><a href="/docs/linux/man/8-ntpd/">ntpd</a></code>(8), <code><a href="/docs/linux/man/8-ntpq/">ntpq</a></code>(8), <code><a href="/docs/linux/man/8-ntpdc/">ntpdc</a></code>(8) </p>
<h2>Author</h2>
<p>G. Richard Keech (rkeech [at] redhat.com)</p>
