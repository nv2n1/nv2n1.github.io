---
title: "amqp-consume(1)"
name: "amqp-consume"
section: "1"
letter: "a"
url: "/docs/linux/man/1-amqp-consume/"
description: "amqp-consume – Consume messages from a queue on an AMQP server"
---

<h2 class="name">NAME</h2>
<p> amqp-consume &#8211; Consume messages from a queue on an AMQP server </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>amqp-consume</code> [<i>OPTION</i>&#8230;] {<i>command</i>} [<i>args</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>amqp-consume</code></p>
<dd>consumes messages from a queue on an AMQP server. For each message that arrives, a receiving command is run, with the message body supplied to it on standard input. </p>
<p> <code>amqp-consume</code> can consume from an existing queue, or it can create a new queue. It can optionally bind the queue to an existing exchange. </p>
<p> By default, messages will be consumed with explicit acknowledgements. A message will only be acknowledged if the receiving command exits successfully (i.e. with an exit code of zero). The AMQP &#8220;no ack&#8221; mode (a.k.a. auto-ack mode) can be enable with the <code>-A</code> option.</p>
<h2>OPTIONS</h2>
<p> <code>-q</code>, <code>&#8211;queue</code>=<i>queue name</i></p>
<dl>
<dt>
<dd> The name of the queue to consume messages from. </p>
<p> If the <code>&#8211;queue</code> option is omitted, the AMQP server will assign a unique name to the queue, and that server-assigned name will be dixsplayed on stderr; this case implies that an exclusive queue should be declared.</dl>
<p> <code>-e</code>, <code>&#8211;exchange</code>=<i>exchange name</i></p>
<dl>
<dt>
<dd> Specifies that an exclusive queue should be declared, and bound to the given exchange. The specified exchange should already exist unless the <code>&#8211;exchange-type</code> option is used to request the creation of an exchange.</dl>
<p> <code>-r</code>, <code>&#8211;routing-key</code>=<i>routing key</i></p>
<dl>
<dt>
<dd> The routing key for binding. If omitted, an empty routing key is assumed.</dl>
<p> <code>-d</code>, <code>&#8211;declare</code></p>
<dl>
<dt>
<dd> Forces an exclusive queue to be declared, even when it otherwise would not be. That is, when a queue name is specified with the <code>&#8211;queue</code> option, but no binding to an exchange is requested with the <code>&#8211;exchange</code> option. Note: this option is deprecated and may be removed in a future version, use the <code>&#8211;exclusive</code> option to explicitly declare an exclusive queue.</dl>
<p> <code>-x</code>, <code>&#8211;exclusive</code></p>
<dl>
<dt>
<dd> Declared queues are non-exclusive by default, this option forces declaration of exclusive queues.</dl>
<p> <code>-A</code>, <code>&#8211;no-ack</code>=<i>routing key</i></p>
<dl>
<dt>
<dd> Enable &#8220;no ack&#8221; mode: The AMQP server will unconditionally acknowledge each message that is delivered, regardless of whether the target command exits successfully or not.</dl>
<p> <code>-c</code>, <code>&#8211;count</code>=<i>limit</i></p>
<dl>
<dt>
<dd> Stop consuming after the given number of messages have been received.</dl>
<p> <code>-p</code>, <code>&#8211;prefetch-count</code>=<i>limit</i></p>
<dl>
<dt>
<dd> Request the server to only send <i>limit</i> messages at a time. </p>
<p> If any value was passed to <code>&#8211;count</code>, the value passed to <code>&#8211;prefetch-count</code> should be smaller than that, or otherwise it will be ignored. </p>
<p> If <code>-A</code>/<code>&#8211;no-ack</code> is passed, this option has no effect.</dl>
<h2>EXAMPLES</h2>
<p> Consume messages from an existing queue &#8220;myqueue&#8221;, and output the message bodies on standard output via <code>cat</code>:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
$ <code>amqp-publish -q myqueue cat</code>
</pre>
</dl>
</dl>
<p> Bind a new exclusive queue to an exchange &#8220;myexch&#8221;, and send each message body to the script myscript, automatically acknowledging them on the server:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
$ <code>amqp-consume -A -e myexch ./myscript</code>
</pre>
</dl>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-librabbitmq-tools/">librabbitmq-tools</a></code>(7) describes connection-related options common to all the RabbitMQ C Client tools.</p>
<h2>AUTHOR</h2>
<p> <code>The RabbitMQ Team &lt;</code><code>m[blue]&lt;info [at] rabbitmq.com&gt;</code>m[]<code>&gt;</code> </p>
<h2>Index</h2>
