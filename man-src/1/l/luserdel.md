---
title: "luserdel(1)"
name: "luserdel"
section: "1"
letter: "l"
url: "/docs/linux/man/1-luserdel/"
description: "luserdel – Delete an user"
---

<h2 class="name">NAME</h2>
<p> luserdel &#8211; Delete an user</p>
<h2>SYNOPSIS</h2>
<p> luserdel [<i>OPTION</i>]&#8230; <i>user</i> </p>
<h2>DESCRIPTION</h2>
<p> Deletes the user with name <i>user</i>. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-G</code>, <code>&#8211;dontremovegroup</code></p>
<dd> By default the user&#8217;s primary group is removed if it has group name <i>user</i> (user&#8217;s private group). This option disables this behavior. </p>
<dt><code>-i</code>, <code>&#8211;interactive</code></p>
<dd> Ask all questions when connecting to the user database, even if default answers are set up in <code>libuser</code> configuration. </p>
<dt><code>-r</code>, <code>&#8211;removehome</code></p>
<dd> Remove user&#8217;s home directory and mail spool after deleting the user. </p>
</dl>
<h2>EXIT STATUS</h2>
<p> The exit status is 0 on success, nonzero on error. </p>
<h2>Index</h2>
