---
title: "ssh-sk-helper(8)"
name: "ssh-sk-helper"
section: "8"
letter: "s"
url: "/docs/linux/man/8-ssh-sk-helper/"
description: "ssh-sk-helper – OpenSSH helper for FIDO authenticator support"
---

<p><code>ssh-sk-helper</code> &#8211; OpenSSH helper for FIDO authenticator support</p>
<h2>Synopsis</h2>
<p><code>ssh-sk-helper</code> [-<code>v</code> ]</p>
<h2>Description</h2>
<p><code>ssh-sk-helper</code> is used by ssh-agent1 to access keys provided by a FIDO authenticator. <code>ssh-sk-helper</code> is not intended to be invoked by the user, but from ssh-agent1. A single option is supported:</p>
<dl>
<dt><code>-v</code></p>
<dd>Verbose mode. Causes <code>ssh-sk-helper</code> to print debugging messages about its progress. This is helpful in debugging problems. Multiple &#8211;<code>v</code> options increase the verbosity. The maximum is 3. Note that ssh-agent1 will automatically pass the &#8211;<code>v</code> flag to <code>ssh-sk-helper</code> when it has itself been placed in debug mode.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-ssh/">ssh</a>(1), ssh-add1, ssh-agent1</p>
<h2>History</h2>
<p><code>ssh-sk-helper</code> first appeared in Ox 6.7 .</p>
<h2>Authors</h2>
<p>An Damien Miller Aq Mt djm [at] openbsd.org</p>
