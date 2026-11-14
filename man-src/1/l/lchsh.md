---
title: "lchsh(1)"
name: "lchsh"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lchsh/"
description: "lchsh – Change login shell"
---

<h2 class="name">NAME</h2>
<p> lchsh &#8211; Change login shell</p>
<h2>SYNOPSIS</h2>
<p> lchsh [<i>OPTION</i>]&#8230; [<i>user</i>] </p>
<h2>DESCRIPTION</h2>
<p> Displays and allows changing login shell of <i>user</i>. </p>
<p> If the <i>user</i> argument is not provided, username of the invoking user is used; the <i>user</i> argument is ignored if <code>lchsh</code> is run set-uid to a different user. </p>
<p> Entering an empty string (by pressing Enter) at the &quot;New Shell&quot; prompt is interpreted as accepting the current value. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i</code>, <code>&#8211;interactive</code></p>
<dd> Ask all questions when connecting to the user database, even if default answers are set up in <code>libuser</code> configuration. </p>
</dl>
<h2>EXIT STATUS</h2>
<p> The exit status is 0 on success, 1 on error. </p>
<h2>BUGS</h2>
<p> <code>lchsh</code> ignores <i>/etc/shells</i>. </p>
<h2>Index</h2>
