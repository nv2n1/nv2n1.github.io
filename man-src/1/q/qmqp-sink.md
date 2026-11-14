---
title: "qmqp-sink(1)"
name: "qmqp-sink"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qmqp-sink/"
description: "qmqp-sink – parallelized QMQP test server"
---

<h2 class="name">NAME</h2>
<p> qmqp-sink &#8211; parallelized QMQP test server </p>
<h2>SYNOPSIS</h2>
<p> <code>qmqp-sink</code> [<code>-46cv</code>] [<code>-x </code><i>time</i>] [<code>inet:</code>][<i>host</i>]:<i>port</i> <i>backlog</i> </p>
<p> <code>qmqp-sink</code> [<code>-46cv</code>] [<code>-x </code><i>time</i>] <code>unix:</code><i>pathname</i> <i>backlog</i></p>
<h2>DESCRIPTION</h2>
<p> <code>qmqp-sink</code> listens on the named host (or address) and port. It receives messages from the network and throws them away. The purpose is to measure QMQP client performance, not protocol compliance. Connections can be accepted on IPv4 or IPv6 endpoints, or on UNIX-domain sockets. IPv4 and IPv6 are the default. This program is the complement of the <code><a href="/docs/linux/man/1-qmqp-source/">qmqp-source</a></code>(1) program. </p>
<p> Note: this is an unsupported test program. No attempt is made to maintain compatibility between successive versions. </p>
<p> Arguments:</p>
<dl>
<dt><code>-4</code></p>
<dd> Support IPv4 only. This option has no effect when Postfix is built without IPv6 support.</p>
<dt><code>-6</code></p>
<dd> Support IPv6 only. This option is not available when Postfix is built without IPv6 support.</p>
<dt><code>-c</code></p>
<dd> Display a running counter that is updated whenever a delivery is completed.</p>
<dt><code>-v</code></p>
<dd> Increase verbosity. Specify <code>-v -v</code> to see some of the QMQP conversation.</p>
<dt><code>-x </code><i>time</i></p>
<dd> Terminate after <i>time</i> seconds. This is to facilitate memory leak testing.</dl>
<h2>SEE ALSO</h2>
<pre>
<a href="//www.systutorials.com/docs/linux/man/1-qmqp-source/">qmqp-source</a>(1), QMQP message generator
</pre>
<h2>LICENSE</h2>
<p> The Secure Mailer license must be distributed with this software.</p>
<h2>AUTHOR(S)</h2>
<pre>
Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA
Wietse Venema
Google, Inc.
111 8th Avenue
New York, NY 10011, USA
</pre>
<h2>Index</h2>
