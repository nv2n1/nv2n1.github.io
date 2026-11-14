---
title: "amqp-get(1)"
name: "amqp-get"
section: "1"
letter: "a"
url: "/docs/linux/man/1-amqp-get/"
description: "amqp-get – Get a message from a queue on an AMQP server"
---

<h2 class="name">NAME</h2>
<p> amqp-get &#8211; Get a message from a queue on an AMQP server </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>amqp-get</code> [<i>OPTION</i>&#8230;] {-q&nbsp;<wbr><i>queue name</i>}</dl>
<h2>DESCRIPTION</h2>
<p> <code>amqp-get</code></p>
<dd>attempts to consume a single message from a queue on an AMQP server, and exits. Unless the queue was empty, the body of the resulting message is sent to standard output.</p>
<h2>OPTIONS</h2>
<p> <code>-q</code>, <code>&#8211;queue</code>=<i>queue name</i></p>
<dl>
<dt>
<dd> The name of the queue to consume messages from.</dl>
<h2>EXIT STATUS</h2>
<p> If the queue is not empty, and a message is successfully retrieved, the exit status is 0. If an error occurs, the exit status is 1. If the queue is found to be empty, the exit status is 2.</p>
<h2>EXAMPLES</h2>
<p> Get a message from the queue &#8220;myqueue&#8221;, and display its body on standard output:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
$ <code>amqp-get -q myqueue</code>
</pre>
</dl>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-librabbitmq-tools/">librabbitmq-tools</a></code>(7) describes connection-related options common to all the RabbitMQ C Client tools.</p>
<h2>AUTHOR</h2>
<p> <code>The RabbitMQ Team &lt;</code><code>m[blue]&lt;info [at] rabbitmq.com&gt;</code>m[]<code>&gt;</code> </p>
<h2>Index</h2>
