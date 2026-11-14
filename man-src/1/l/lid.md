---
title: "lid(1)"
name: "lid"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lid/"
description: "lid – Display user’s groups or group’s users"
---

<h2 class="name">NAME</h2>
<p> lid &#8211; Display user&#8217;s groups or group&#8217;s users</p>
<h2>SYNOPSIS</h2>
<p> lid [<i>OPTION</i>]&#8230; [<i>name</i>] </p>
<h2>DESCRIPTION</h2>
<p> Displays information about groups containing user <i>name</i>, or users contained in group <i>name</i>. </p>
<p> By default <code>lid</code> lists groups containing user <i>name</i>, or groups containing the invoking user if <i>name</i> is not specified; the mode of operation can be changed using the <code>-g</code> option. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-g</code>, <code>&#8211;group</code></p>
<dd> List users in a group <i>name</i>, or in the invoking user&#8217;s primary group if <i>name</i> is not specified. </p>
<dt><code>-i</code>, <code>&#8211;interactive</code></p>
<dd> Ask all questions when connecting to the user database, even if default answers are set up in <code>libuser</code> configuration. </p>
<dt><code>-n</code>, <code>&#8211;onlynames</code></p>
<dd> List only group or user names. By default the corresponging user or group IDs are listed too. </p>
</dl>
<h2>EXIT STATUS</h2>
<p> The exit status is 0 on success, 1 on error. </p>
<h2>Index</h2>
