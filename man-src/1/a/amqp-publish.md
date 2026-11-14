---
title: "amqp-publish(1)"
name: "amqp-publish"
section: "1"
letter: "a"
url: "/docs/linux/man/1-amqp-publish/"
description: "amqp-publish – Publish a message on an AMQP server"
---

<h2 class="name">NAME</h2>
<p> amqp-publish &#8211; Publish a message on an AMQP server </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>amqp-publish</code> [<i>OPTION</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<dd>Publishes a message to an exchange on an AMQP server. Options allow the various properties of the message and parameters of the AMQP <code>basic.publish</code> method to be specified. </p>
<p> By default, the message body is read from standard input. Alternatively, the <code>-b</code> option allows the message body to be provided as part of the command.</p>
<h2>OPTIONS</h2>
<p> <code>-e</code>, <code>&#8211;exchange</code>=<i>exchange name</i></p>
<dl>
<dt>
<dd> The name of the exchange to publish to. If omitted, the default exchange (also known as the nameless exchange) is used.</dl>
<p> <code>-r</code>, <code>&#8211;routing-key</code>=<i>routing key</i></p>
<dl>
<dt>
<dd> The routing key to publish with. If omitted, an empty routing key is assumed. A routing key must be specified when publishing to the default exchange; in that case, accoding to the AMQP specification, the routing key corresponds to a queue name.</dl>
<p> <code>-p</code>, <code>&#8211;persistent</code></p>
<dl>
<dt>
<dd> Use the persistent delivery mode. Without this option, non-persistent delivery is used.</dl>
<p> <code>-C</code>, <code>&#8211;content-type</code>=<i>MIME type</i></p>
<dl>
<dt>
<dd> Specifies the content-type property for the message. If omitted, the content-type property is not set on the message.</dl>
<p> <code>-E</code>, <code>&#8211;content-encoding</code>=<i>content coding</i></p>
<dl>
<dt>
<dd> Specifies the content-encoding property for the message. If omitted, the content-encoding property is not set on the message.</dl>
<p> <code>-b</code>, <code>&#8211;body</code>=<i>message body</i></p>
<dl>
<dt>
<dd> Specifies the message body. If omitted, the message body is read from standard input.</dl>
<h2>EXAMPLES</h2>
<p> Send a short message, consisting of the word &#8220;Hello&#8221; to the queue &#8220;myqueue&#8221; via the default exchange:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
$ <code>amqp-publish -r myqueue -b Hello</code>
</pre>
</dl>
</dl>
<p> Send some XML data from a file to the exchange &#8220;events&#8221;, with persistent delivery mode, setting the content-type property on the message to make the data format explicit:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
$ <code>amqp-publish -e events -p -C text/xml &lt;event.xml</code>
</pre>
</dl>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-librabbitmq-tools/">librabbitmq-tools</a></code>(7) describes connection-related options common to all the RabbitMQ C Client tools.</p>
<h2>AUTHOR</h2>
<p> <code>The RabbitMQ Team &lt;</code><code>m[blue]&lt;info [at] rabbitmq.com&gt;</code>m[]<code>&gt;</code> </p>
<h2>Index</h2>
