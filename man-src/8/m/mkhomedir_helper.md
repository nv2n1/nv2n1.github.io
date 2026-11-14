---
title: "mkhomedir_helper(8)"
name: "mkhomedir_helper"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mkhomedir_helper/"
description: "mkhomedir_helper – Helper binary that creates home directories"
---

<p>mkhomedir_helper &#8211; Helper binary that creates home directories</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>mkhomedir_helper</code> {<i>user</i>} [<i>umask</i>&nbsp;[&nbsp;<i>path-to-skel</i>&nbsp;]]</dl>
<h2>Description</h2>
<p><i>mkhomedir_helper</i></p>
<dd>is a helper program for the <i>pam_mkhomedir</i> module that creates home directories and populates them with contents of the specified skel directory. </p>
<p> The default value of <i>umask</i> is 0022 and the default value of <i>path-to-skel</i> is <i>/etc/skel</i>. </p>
<p> The helper is separated from the module to not require direct access from login SELinux domains to the contents of user home directories. The SELinux domain transition happens when the module is executing the <i>mkhomedir_helper</i>. </p>
<p> The helper never touches home directories if they already exist.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pam_mkhomedir/">pam_mkhomedir</a></code>(8)</p>
<h2>Author</h2>
<p>Written by Tomas Mraz based on the code originally in <i>pam_mkhomedir</i> module.</p>
