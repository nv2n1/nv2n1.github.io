---
title: "rabbitmq-env-conf(5)"
name: "rabbitmq-env-conf"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rabbitmq-env-conf/"
description: "rabbitmq-env.conf – default settings for RabbitMQ AMQP server"
---

<p>rabbitmq-env.conf &#8211; default settings for RabbitMQ AMQP server</p>
<h2>Description</h2>
<p>/etc/rabbitmq/rabbitmq-env.conf contains variable settings that override the defaults built in to the RabbitMQ startup scripts. </p>
<p> The file is interpreted by the system shell, and so should consist of a sequence of shell environment variable definitions. Normal shell syntax is permitted (since the file is sourced using the shell &quot;.&quot; operator), including line comments starting with &quot;#&quot;. </p>
<p> In order of preference, the startup scripts get their values from the environment, from /etc/rabbitmq/rabbitmq-env.conf and finally from the built-in default values. For example, for the <code>RABBITMQ_NODENAME</code> setting, </p>
<p> <code>RABBITMQ_NODENAME</code> </p>
<p> from the environment is checked first. If it is absent or equal to the empty string, then </p>
<p> <code>NODENAME</code> </p>
<p> from /etc/rabbitmq/rabbitmq-env.conf is checked. If it is also absent or set equal to the empty string then the default value from the startup script is used. </p>
<p> The variable names in /etc/rabbitmq/rabbitmq-env.conf are always equal to the environment variable names, with the <code>RABBITMQ_</code> prefix removed: <code>RABBITMQ_NODE_PORT</code> from the environment becomes <code>NODE_PORT</code> in the /etc/rabbitmq/rabbitmq-env.conf file, etc. </p>
<p> For example: </p>
<pre># I am a complete /etc/rabbitmq/rabbitmq-env.conf file.
# Comment lines start with a hash character.
# This is a /bin/sh script file - use ordinary envt var syntax
NODENAME=hare</pre>
<p>This is an example of a complete /etc/rabbitmq/rabbitmq-env.conf file that overrides the default Erlang node name from &quot;rabbit&quot; to &quot;hare&quot;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-rabbitmq-server/">rabbitmq-server</a></code>(1)<code><a href="/docs/linux/man/1-rabbitmqctl/">rabbitmqctl</a></code>(1)</p>
<h2>Author</h2>
<p><code>The RabbitMQ Team &lt;</code><code>m[blue]&lt;info [at] rabbitmq.com&gt;</code>m[]<code>&gt;</code></p>
