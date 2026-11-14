---
title: "rxecho(8)"
name: "rxecho"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rxecho/"
description: "rxecho – Route AX.25 packets between ports transparently."
---

<p>rxecho &#8211; Route AX.25 packets between ports transparently.</p>
<h2>Synopsis</h2>
<p><code>rxecho [-l] [-v]</code></p>
<h2>Description</h2>
<p><code>Rxecho</code> copies AX.25 frames between interfaces without altering their contents. The purpose of this utility is to allow other AX.25 aware programs/computers to share the same AX.25 ports as the Linux kernel AX.25 code. It could be used to route packets out onto another serial port to allow another machine running DOS based programs to share the same radio ports as the Linux machine, or it could route packets out onto a pseudo-tty to another application on the same machine. The copying could even be to another radio port. </p>
<p> The copying of the packets is controlled by a configuration file <a href="/docs/linux/man/5-rxecho-conf/">rxecho.conf</a>(5), which can be set up to selectively copy packets.</p>
<h2>Options</h2>
<dl>
<dt><code>-l</code></p>
<dd>Enables logging of errors to the system log, the default is off.</p>
<dt><code>-v</code></p>
<dd>Display the version.</dl>
<h2>Files</h2>
<pre>/etc/ax25/axports
<br>
/etc/ax25/rxecho.conf</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-axports/">axports</a></code>(5), <code><a href="/docs/linux/man/5-rxecho-conf/">rxecho.conf</a></code>(5), <code><a href="/docs/linux/man/8-kissattach/">kissattach</a></code>(8).</p>
<h2>Author</h2>
<p>Tomi Manninen OH2BNS &lt;oh2bns [at] sral.fi&gt;</p>
