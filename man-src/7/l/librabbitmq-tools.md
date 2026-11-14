---
title: "librabbitmq-tools(7)"
name: "librabbitmq-tools"
section: "7"
letter: "l"
url: "/docs/linux/man/7-librabbitmq-tools/"
description: "librabbitmq-tools – Command line AMQP tools"
---

<p>librabbitmq-tools &#8211; Command line AMQP tools</p>
<h2>Description</h2>
<p>A set of command line AMQP tools based on librabbitmq. This page describes common options and conventions used by all of the tools.</p>
<h2>Common Options</h2>
<p><code>-s</code>, <code>&#8211;server</code>=<i>hostname:port</i></p>
<dl>
<dd>The host name (or address) to connect to. Defaults to localhost. The port number may also be specified; if omitted, it defaults to the standard AMQP port number (5672).</dl>
<p> <code>&#8211;vhost</code>=<i>vhost</i></p>
<dl>
<dd>The AMQP vhost to specify when connnecting. Defaults to /.</dl>
<p> <code>&#8211;username</code>=<i>username</i></p>
<dl>
<dd>The username to authenticate to the AMQP server with. Defaults to guest.</dl>
<p> <code>&#8211;password</code>=<i>password</i></p>
<dl>
<dd>The password to authenticate to the AMQP server with. Defaults to guest.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-amqp-publish/">amqp-publish</a></code>(1), <code><a href="/docs/linux/man/1-amqp-consume/">amqp-consume</a></code>(1), <code><a href="/docs/linux/man/1-amqp-get/">amqp-get</a></code>(1)</p>
<h2>Author</h2>
<p><code>The RabbitMQ Team &lt;</code><code>m[blue]&lt;info [at] rabbitmq.com&gt;</code>m[]<code>&gt;</code></p>
