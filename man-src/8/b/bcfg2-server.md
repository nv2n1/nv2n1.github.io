---
title: "bcfg2-server(8)"
name: "bcfg2-server"
section: "8"
letter: "b"
url: "/docs/linux/man/8-bcfg2-server/"
description: "bcfg2-server – Server for client configuration specifications"
---

<p>bcfg2-server &#8211; Server for client configuration specifications</p>
<h2>Synopsis</h2>
<p><code>bcfg2-server</code> <i>[-D &lt;pidfile&gt;] [-d] [-v] [-C &lt;Client&gt;]</i></p>
<h2>Description</h2>
<p><code>bcfg2-server</code> This daemon serves configurations to clients based on the data in its repository.</p>
<h2>Options</h2>
<p><code>-d </code></p>
<dl>
<dd>Run bcfg2 in debug mode.</dl>
<p> <code>-v</code></p>
<dl>
<dd>Run bcfg2 in verbose mode.</dl>
<p> <code>-C &lt;ConfigFile Path&gt; </code></p>
<dl>
<dd>Use an alternative path for bcfg2.conf. The default is /etc/bcfg2.conf</dl>
<p> <code>-D </code></p>
<dl>
<dd>Daemonize, placing the program pid in the specified pidfile.</dl>
<p> <code>-o &lt;LogFile Path&gt;</code></p>
<dl>
<dd>Writes a log to the specified path.</dl>
<p> <code>-E &lt;encoding&gt;</code></p>
<dl>
<dd>Unicode encoding of config files</dl>
<p> <code>-x &lt;password&gt;</code></p>
<dl>
<dd>Set server password</dl>
<p> <code>-S &lt;server url&gt;</code></p>
<dl>
<dd>Set server address</dl>
<p> <code>-Q &lt;repo path&gt;</code></p>
<dl>
<dd>Set repository path</dl>
<p> <code>-K &lt;key path&gt;</code></p>
<dl>
<dd>Set path to ssl key</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-bcfg2/">bcfg2</a>(1),</code> <code><a href="/docs/linux/man/8-bcfg2-repo-validate/">bcfg2-repo-validate</a>(8)</code></p>
<h2>Bugs</h2>
<p>None currently known </p>
