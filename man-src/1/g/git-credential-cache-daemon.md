---
title: "git-credential-cache-daemon(1)"
name: "git-credential-cache-daemon"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-credential-cache-daemon/"
description: "git-credential-cache–daemon – Temporarily store user credentials in memory"
---

<p>git-credential-cache&#8211;daemon &#8211; Temporarily store user credentials in memory </p>
<h2>Synopsis</h2>
<pre>git credential-cache---daemon [--debug] &lt;socket&gt;</pre>
<h2>Description</h2>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> You probably don&#8217;t want to invoke this command yourself; it is started automatically when you use <code><a href="/docs/linux/man/1-git-credential-cache/">git-credential-cache</a></code>(1). </p>
</dl>
<p> This command listens on the Unix domain socket specified by <code>&lt;socket&gt;</code> for <code>git-credential-cache</code> clients. Clients may store and retrieve credentials. Each credential is held for a timeout specified by the client; once no credentials are held, the daemon exits. </p>
<p> If the <code>&#8211;debug</code> option is specified, the daemon does not close its stderr stream, and may output extra diagnostics to it even after it has begun listening for clients.</p>
<h2>Git</h2>
<p>Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite</p>
