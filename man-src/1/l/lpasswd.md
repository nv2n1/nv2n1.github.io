---
title: "lpasswd(1)"
name: "lpasswd"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lpasswd/"
description: "lpasswd – Change group or user password"
---

<h2 class="name">NAME</h2>
<p> lpasswd &#8211; Change group or user password</p>
<h2>SYNOPSIS</h2>
<p> lpasswd [<i>OPTION</i>]&#8230; [<i>name</i>] </p>
<h2>DESCRIPTION</h2>
<p> Changes password of user or group <i>name</i>. </p>
<p> If the <i>name</i> argument is not provided, username of the invoking user is used; the <i>name</i> argument is ignored if <code>lpasswd</code> is run set-uid to a different user. </p>
<p> Entering an empty password (by pressing Enter) aborts the password setting operation. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-F</code>, <code>&#8211;plainpassword-fd</code>=<i>fd</i></p>
<dd> Read password from file descriptor <i>fd</i>, terminated by end of file, <code>&#8216;&#8217;</code> or <code>&#8216;
&#8217;</code>. </p>
<dt><code>-f</code>, <code>&#8211;password-fd</code>=<i>fd</i></p>
<dd> Read password hash from file descriptor <i>fd</i>, terminated by end of file, <code>&#8216;&#8217;</code> or <code>&#8216;
&#8217;</code>. </p>
<dt><code>-g</code>, <code>&#8211;group</code></p>
<dd> Change password of group <i>name</i>. By default the password of user <i>name</i> is changed. </p>
<dt><code>-i</code>, <code>&#8211;interactive</code></p>
<dd> Ask all questions when connecting to the user database, even if default answers are set up in <code>libuser</code> configuration. </p>
<dt><code>-P</code>, <code>&#8211;plainpassword</code>=<i>password</i></p>
<dd> Set the password to <i>password</i>. Note that the password can be viewed while running <code>lpasswd</code> using tools such as <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1). </p>
<dt><code>-p</code>, <code>&#8211;password</code>=<i>encrypted</i></p>
<dd> Set the password to the password represented by the hash <i>encrypted</i>. Note that the hash can be viewed while running <code>lpasswd</code> using tools such as <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1). </p>
</dl>
<h2>EXIT STATUS</h2>
<p> The exit status is 0 on success, nonzero on error. </p>
<h2>Index</h2>
