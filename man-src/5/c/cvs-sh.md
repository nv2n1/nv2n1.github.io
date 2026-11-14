---
title: "cvs-sh(5)"
name: "cvs-sh"
section: "5"
letter: "c"
url: "/docs/linux/man/5-cvs-sh/"
description: "cvs.sh – Bourne shell log-in script for CVS users"
---

<p>cvs.sh &#8211; Bourne shell log-in script for CVS users</p>
<h2>Synopsis</h2>
<p><code>/etc/profile.d/cvs.sh</code></p>
<h2>Description</h2>
<p>The <code>cvs.sh</code> script is sourced when a user of a Bourne log-in shell is logged in. The purpose is to set <code>CVS_RSH</code> environment variable, so that a cvs user connecting to a remote CVS server utilizes SSH-secured connection by default.</p>
<h2>Example</h2>
<pre><code>export CVS_RSH=${CVS_RSH-ssh}</code></pre>
<h2>Files</h2>
<dl>
<dt><code>/etc/profile.d/cvs.sh</code></p>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-cvs/">cvs</a></code>(1), <code><a href="/docs/linux/man/1-bash/">bash</a></code>(1), <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1). </p>
