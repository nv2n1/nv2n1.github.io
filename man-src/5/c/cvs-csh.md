---
title: "cvs-csh(5)"
name: "cvs-csh"
section: "5"
letter: "c"
url: "/docs/linux/man/5-cvs-csh/"
description: "cvs.sh – C shell log-in script for CVS users"
---

<p>cvs.sh &#8211; C shell log-in script for CVS users</p>
<h2>Synopsis</h2>
<p><code>/etc/profile.d/cvs.csh</code></p>
<h2>Description</h2>
<p>The <code>cvs.csh</code> script is sourced when a user of a C log-in shell is logged in. The purpose is to set <code>CVS_RSH</code> environment variable, so that a cvs user connecting to a remote CVS server utilizes SSH-secured connection by default.</p>
<h2>Example</h2>
<p>if ( &quot;$?CVS_RSH&quot; == 0 ) setenv CVS_RSH ssh</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/profile.d/cvs.csh</code></p>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-csh/">csh</a></code>(1), <code><a href="/docs/linux/man/1-cvs/">cvs</a></code>(1), <code><a href="/docs/linux/man/1-bash/">bash</a></code>(1). </p>
