---
title: "zmq_plain(7)"
name: "zmq_plain"
section: "7"
letter: "z"
url: "/docs/linux/man/7-zmq_plain/"
description: "zmq_plain – clear-text authentication"
---

<p>zmq_plain &#8211; clear-text authentication</p>
<h2>Synopsis</h2>
<p>The PLAIN mechanism defines a simple username/password mechanism that lets a server authenticate a client. PLAIN makes no attempt at security or confidentiality. It is intended for use on internal networks where security requirements are low. The PLAIN mechanism is defined by this document: m[blue]<code><a rel="nofollow" href="http://rfc.zeromq.org/spec:24">http://rfc.zeromq.org/spec:24</a></code>m[].</p>
<h2>Usage</h2>
<p>To use PLAIN, the server shall set the ZMQ_PLAIN_SERVER option, and the client shall set the ZMQ_PLAIN_USERNAME and ZMQ_PLAIN_PASSWORD socket options. Which peer binds, and which connects, is not relevant.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-zmq_setsockopt/">zmq_setsockopt</a></code>(3) <code><a href="/docs/linux/man/7-zmq_null/">zmq_null</a></code>(7) <code><a href="/docs/linux/man/7-zmq_curve/">zmq_curve</a></code>(7) <code><a href="/docs/linux/man/7-zmq/">zmq</a></code>(7)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
