---
title: "lgroupadd(1)"
name: "lgroupadd"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lgroupadd/"
description: "lgroupadd – Add an user group"
---

<h2 class="name">NAME</h2>
<p> lgroupadd &#8211; Add an user group</p>
<h2>SYNOPSIS</h2>
<p> lgroupadd [<i>OPTION</i>]&#8230; <i>group</i> </p>
<h2>DESCRIPTION</h2>
<p> Adds a new user group with name <i>group</i>. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-g</code>, <code>&#8211;gid</code>=<i>gid</i></p>
<dd> Use group ID <i>gid</i> for the newly created group. A group ID is selected automatically if this option is not present. </p>
<dt><code>-i</code>, <code>&#8211;interactive</code></p>
<dd> Ask all questions when connecting to the user database, even if default answers are set up in <code>libuser</code> configuration. </p>
<dt><code>-r</code>, <code>&#8211;reserved</code></p>
<dd> The group is a system group. Groups that are not marked as system groups usually have automatically selected group IDs above a certain value (configured as <code>LU_GIDNUMBER</code> in <code><a href="/docs/linux/man/5-libuser-conf/">libuser.conf</a></code>(5)). This information is also passed to the <code>libuser</code> backends. </p>
</dl>
<h2>EXIT STATUS</h2>
<p> The exit status is 0 on success, nonzero on error. </p>
<h2>Index</h2>
