---
title: "bcfg2-remote(8)"
name: "bcfg2-remote"
section: "8"
letter: "b"
url: "/docs/linux/man/8-bcfg2-remote/"
description: "bcfg2-remote – Connect to a bcfg2 agent and trigger client execution"
---

<p>bcfg2-remote &#8211; Connect to a bcfg2 agent and trigger client execution</p>
<h2>Synopsis</h2>
<p><code>bcfg2-remote</code> <i>[-d &lt;debug level&gt;]</i> <i>[-H &lt;agent host&gt;]</i> <i>[-C &lt;configfile&gt;]</i> <i>[-k &lt;ssl key&gt;]</i> <i>[-p &lt;agent tcp port&gt;]</i></p>
<h2>Description</h2>
<p>bcfg2-remote connects to a client agent, uses the server certificate for authentication, and causes that client to run the bcfg2 client code with the options specified on the client.</p>
<h2>Options</h2>
<p><code>-d debuglevel</code></p>
<dl>
<dd>Set debug level (0-40).</dl>
<p> <code>-H hostname</code></p>
<dl>
<dd>Connect to the agent on the specified host.</dl>
<p> <code>-C configfile</code></p>
<dl>
<dd>Use the specified bcfg2.conf.</dl>
<p> <code>-k sslkey</code></p>
<dl>
<dd>Use the ssl certificate at the following path.</dl>
<p> <code>-p port</code></p>
<dl>
<dd>Connect to the agent on the specified TCP port.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-bcfg2/">bcfg2</a>(1)</code> </p>
