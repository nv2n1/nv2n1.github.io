---
title: "pam_namespace_helper(8)"
name: "pam_namespace_helper"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_namespace_helper/"
description: "pam_namespace_helper – Helper binary that creates home directories"
---

<p>pam_namespace_helper &#8211; Helper binary that creates home directories</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_namespace_helper</code></dl>
<h2>Description</h2>
<p><i>pam_namespace_helper</i></p>
<dd>is a helper program for the <i>pam_namespace</i> module that sets up a private namespace for a session with polyinstantiated directories. The helper ensures that the namespace mount points exist before they are started to be used for the polyinstantiated directories. Mount points for home directories (lines with $HOME) are not created. </p>
<p> <i>pam_namespace_helper</i> should be run by systemd at system startup. It should also be run by the administrator after defining the polyinstantiated directories but before enabling them.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pam_namespace/">pam_namespace</a></code>(8)</p>
<h2>Author</h2>
<p>Written by Topi Miettinen.</p>
