---
title: "lchage(1)"
name: "lchage"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lchage/"
description: "lchage – Display or change user password policy"
---

<h2 class="name">NAME</h2>
<p> lchage &#8211; Display or change user password policy</p>
<h2>SYNOPSIS</h2>
<p> lchage [<i>OPTION</i>]&#8230; <i>user</i> </p>
<h2>DESCRIPTION</h2>
<p> Displays or allows changing password policy of <i>user</i>. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;date</code>=<i>days</i></p>
<dd> Set the date of last password change to <i>days</i> after Jan 1 1970. </p>
<p> Set <i>days</i> to -1 to disable password expiration (i.e. to ignore <code>&#8211;mindays</code>, and <code>&#8211;maxdays</code> and related settings). </p>
<p> Set <i>days</i> to 0 to enforce password change on next login. (This also disables password expiration until the password is changed.) </p>
<dt><code>-E</code>, <code>&#8211;expire</code>=<i>days</i></p>
<dd> Set the account expiration date to <i>days</i> after Jan 1 1970. Set <i>days</i> to -1 to disable account expiration. </p>
<dt><code>-i</code>, <code>&#8211;interactive</code></p>
<dd> Ask all questions when connecting to the user database, even if default answers are set up in <code>libuser</code> configuration. </p>
<dt><code>-I</code>, <code>&#8211;inactive</code>=<i>days</i></p>
<dd> Disable the account after <i>days</i> after password expires (after the user is required to change the password). Set <i>days</i> to -1 to keep the account enabled indefinitely after password expiration. </p>
<dt><code>-l</code>, <code>&#8211;list</code></p>
<dd> Only list current <i>user</i>&#8216;s policy and make no changes. </p>
<dt><code>-m</code>, <code>&#8211;mindays</code>=<i>days</i></p>
<dd> Require at least <i>days</i> days between password changes. Set <i>days</i> to 0 or -1 to disable this requirement. </p>
<p> If this value is larger than the value set by <code>&#8211;maxdays</code>, the user cannot change the pasword. </p>
<dt><code>-M</code>, <code>&#8211;maxdays</code>=<i>days</i></p>
<dd> Require changing the password after <i>days</i> since last password change. Set <i>days</i> to -1 to disable password expiration. </p>
<dt><code>-W</code>, <code>&#8211;warndays</code>=<i>days</i></p>
<dd> Start warning the user <i>days</i> before password expires (before the user is required to change the password). Set <i>days</i> to 0 or -1 to disable the warning. </p>
</dl>
<h2>EXIT STATUS</h2>
<p> The exit status is 0 on success, nonzero on error. </p>
<h2>NOTES</h2>
<p> Note that &#8220;account expiration&#8221; (set by <code>&#8211;expire</code>) is distinct from &#8220;password expiration&#8221; (set by <code>&#8211;maxdays</code>). Account expiration happens on a fixed date regardless of password changes. Password expiration is relative to the date of last password change. </p>
<h2>Index</h2>
