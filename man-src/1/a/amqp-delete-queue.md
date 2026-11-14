---
title: "amqp-delete-queue(1)"
name: "amqp-delete-queue"
section: "1"
letter: "a"
url: "/docs/linux/man/1-amqp-delete-queue/"
description: "amqp-delete-queue – Delete a queue from an AMQP server"
---

<h2 class="name">NAME</h2>
<p> amqp-delete-queue &#8211; Delete a queue from an AMQP server </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>amqp-delete-queue</code> [<i>OPTION</i>&#8230;] {-q&nbsp;<wbr><i>queue name</i>}</dl>
<h2>DESCRIPTION</h2>
<p> <code>amqp-delete-queue</code></p>
<dd>deletes a queue from an AMQP server, and exits after printing to standard output the number of messages that were in the queue at the time of its deletion.</p>
<h2>OPTIONS</h2>
<p> <code>-q</code>, <code>&#8211;queue</code>=<i>queue name</i></p>
<dl>
<dt>
<dd> The name of the queue to delete.</dl>
<h2>EXIT STATUS</h2>
<p> If the queue was successfully deleted, the exit status is 0. If an error occurs, the exit status is 1.</p>
<h2>EXAMPLES</h2>
<p> Delete the queue &#8220;myqueue&#8221; at a moment when it has 123 messages waiting on it:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
$ <code>amqp-delete-queue -q myqueue</code>
123
</pre>
</dl>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-librabbitmq-tools/">librabbitmq-tools</a></code>(7) describes connection-related options common to all the RabbitMQ C Client tools.</p>
<h2>AUTHOR</h2>
<p> <code>The RabbitMQ Team &lt;</code><code>m[blue]&lt;info [at] rabbitmq.com&gt;</code>m[]<code>&gt;</code> </p>
<h2>Index</h2>
