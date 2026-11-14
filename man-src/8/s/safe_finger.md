---
title: "safe_finger(8)"
name: "safe_finger"
section: "8"
letter: "s"
url: "/docs/linux/man/8-safe_finger/"
description: "safe_finger – finger client wrapper that protects against nasty stuff from finger servers"
---

<p>safe_finger &#8211; finger client wrapper that protects against nasty stuff from finger servers</p>
<h2>Synopsis</h2>
<p><code>safe_finger [finger_options]</code></p>
<h2>Description</h2>
<p>The <code>safe_finger</code> command protects against nasty stuff from finger servers. Use this program for automatic reverse finger probes from the <code>tcp_wrapper</code> <code>(tcpd)</code> , not the raw finger command. The <code>safe_finger</code> command makes sure that the finger client is not run with root privileges. It also runs the finger client with a defined PATH environment. <code>safe_finger</code> will also protect you from problems caused by the output of some finger servers. The problem: some programs may react to stuff in the first column. Other programs may get upset by thrash anywhere on a line. File systems may fill up as the finger server keeps sending data. Text editors may bomb out on extremely long lines. The finger server may take forever because it is somehow wedged. <code>safe_finger</code> takes care of all this badness.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-hosts_access/">hosts_access</a></code>(5), <code><a href="/docs/linux/man/5-hosts_options/">hosts_options</a></code>(5), <code><a href="/docs/linux/man/8-tcpd/">tcpd</a></code>(8)</p>
<h2>Author</h2>
<p>Wietse Venema, Eindhoven University of Technology, The Netherlands.</p>
