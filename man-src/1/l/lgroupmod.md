---
title: "lgroupmod(1)"
name: "lgroupmod"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lgroupmod/"
description: "lgroupmod – Modify an user group"
---

<h2 class="name">NAME</h2>
<p> lgroupmod &#8211; Modify an user group</p>
<h2>SYNOPSIS</h2>
<p> lgroupmod [<i>OPTION</i>]&#8230; <i>group</i> </p>
<h2>DESCRIPTION</h2>
<p> Modifies the user group with name <i>group</i>. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-A</code>, <code>&#8211;admin-add</code>=<i>list</i></p>
<dd> Add users in comma-separated <i>list</i> among <i>group</i>&#8216;s administrators. </p>
<dt><code>-a</code>, <code>&#8211;admin-remove</code>=<i>list</i></p>
<dd> Remove users in comma-separated <i>list</i> from <i>group</i>&#8216;s administrators. Removing users that are not currently among <i>group</i>&#8216;s administrators silently succeeds. </p>
<dt><code>-g</code>, <code>&#8211;gid</code>=<i>gid</i></p>
<dd> Change <i>group</i>&#8216;s group ID to <i>gid</i>. </p>
<dt><code>-i</code>, <code>&#8211;interactive</code></p>
<dd> Ask all questions when connecting to the user database, even if default answers are set up in <code>libuser</code> configuration. </p>
<dt><code>-L</code>, <code>&#8211;lock</code></p>
<dd> Lock <i>group</i>. This prevents users from using the group password with <code><a href="/docs/linux/man/1-newgrp/">newgrp</a></code>(1) to become a member of <i>group</i>. </p>
<dt><code>-M</code>, <code>&#8211;member-add</code>=<i>list</i></p>
<dd> Add users in comma-separated <i>list</i> among <i>group</i>&#8216;s members. </p>
<dt><code>-m</code>, <code>&#8211;member-remove</code>=<i>list</i></p>
<dd> Remove users in comma-separated <i>list</i> from <i>group</i>&#8216;s members. Removing users that are not currently among <i>group</i>&#8216;s members silently succeeds. </p>
<dt><code>-n</code>, <code>&#8211;name</code>=<i>name</i></p>
<dd> Rename <i>group</i> to <i>name</i>. </p>
<dt><code>-P</code>, <code>&#8211;plainpassword</code>=<i>password</i></p>
<dd> Set <i>group</i>&#8216;s password to <i>password</i>. Note that the password can be viewed while running <code>lgroupmod</code> using tools such as <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1). </p>
<dt><code>-p</code>, <code>&#8211;password</code>=<i>encrypted</i></p>
<dd> Set <i>group</i>&#8216;s password to the password represented by the hash <i>encrypted</i>. Note that the hash can be viewed while running <code>lgroupmod</code> using tools such as <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1). </p>
<dt><code>-U</code>, <code>&#8211;unlock</code></p>
<dd> Unlock <i>group</i>. </p>
</dl>
<h2>EXIT STATUS</h2>
<p> The exit status is 0 on success, nonzero on error. </p>
<h2>Index</h2>
