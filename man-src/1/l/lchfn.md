---
title: "lchfn(1)"
name: "lchfn"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lchfn/"
description: "lchfn – Change finger information"
---

<h2 class="name">NAME</h2>
<p> lchfn &#8211; Change finger information</p>
<h2>SYNOPSIS</h2>
<p> lchfn [<i>OPTION</i>]&#8230; [<i>user</i>] </p>
<h2>DESCRIPTION</h2>
<p> Displays and allows changing information about <i>user</i> that is available using the <code><a href="/docs/linux/man/1-finger/">finger</a></code>(1) command (usually stored in the &quot;gecos&quot; field of <i>/etc/passwd</i>). </p>
<p> If the <i>user</i> argument is not provided, username of the invoking user is used; the <i>user</i> argument is ignored if <code>lchfn</code> is run set-uid to a different user. </p>
<p> Entering an empty string (by pressing Enter) at a prompt is interpreted as accepting a default value; to erase an attribute (or to use an empty string as the attribute value), enter a single dot character. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i</code>, <code>&#8211;interactive</code></p>
<dd> Ask all questions when connecting to the user database, even if default answers are set up in <code>libuser</code> configuration. </p>
</dl>
<h2>EXIT STATUS</h2>
<p> The exit status is 0 on success, 1 on error. </p>
<h2>Index</h2>
