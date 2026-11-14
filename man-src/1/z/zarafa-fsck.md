---
title: "zarafa-fsck(1)"
name: "zarafa-fsck"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zarafa-fsck/"
description: "zarafa-fsck – Start the Zarafa fsck calendar check program."
---

<h2 class="name">NAME</h2>
<p> zarafa-fsck &#8211; Start the Zarafa fsck calendar check program. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>zarafa-fsck</code> [<i>OPTION</i>&#8230;] [<i>FILTER</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<dd>The program finds all items in the default calendar folder of the given user, and checks if all items are compatible with Microsoft Outlook. It specifically tests for known issues with reminders and recurrcences.</p>
<h2>OPTIONS</h2>
<p> Various options are possible. Only the &#8211;user options is required. </p>
<p> <code>&#8211;user</code>, <code>-u</code> <i>username</i></p>
<dl>
<dt>
<dd> The name of the user to login with, and to check the calender of.</dl>
<p> <code>&#8211;pass</code>, <code>-p</code> <i>password</i></p>
<dl>
<dt>
<dd> The password of the user to login with. If this is not passed, you will be prompted for the password, and it will not be displayed when typed.</dl>
<p> <code>&#8211;prompt</code>, <code>-P</code></p>
<dl>
<dt>
<dd> Prompt for the password of the user to login with. Overrides the &#8211;pass option.</dl>
<p> <code>&#8211;acceptdisclaimer</code></p>
<dl>
<dt>
<dd> Auto accept the disclaimer so no user input is needed to accept the disclaimer. This can be used for scripts along with <i>&#8211;autofix </i>argument.</dl>
<p> <code>&#8211;public</code></p>
<dl>
<dt>
<dd> Check the public store for user given with the <i>&#8211;user</i>argument.</dl>
<p> <code>&#8211;host</code>, <code>-h</code> <i>path</i></p>
<dl>
<dt>
<dd> Connect to the Zarafa server through <i>path</i>, e.g. file:///path/to/socket. Default: file:///var/run/zarafa.</dl>
<p> <code>&#8211;autofix</code> <i>[yes|no]</i></p>
<dl>
<dt>
<dd> Whether the items should immediately be fixed, and not be prompted for.</dl>
<p> <code>&#8211;autodel</code> <i>[yes|no]</i></p>
<dl>
<dt>
<dd> When the item certainly is broken, and cannot be fixed by the program, it may be deleted.</dl>
<p> <code>&#8211;checkonly</code></p>
<dl>
<dt>
<dd> You will only receive a report of which items are probably broken. The calendar folder will not be written to.</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print a help screen of all possible options.</dl>
<h2>FILTERS</h2>
<p> At least one filter is required. A filter defines which kind of items are checked. </p>
<p> <code>&#8211;calendar</code></p>
<dl>
<dt>
<dd> All calendar folders in the store will be checked, and only calendar items will be tried to fix if needed.</dl>
<p> <code>&#8211;contact</code></p>
<dl>
<dt>
<dd> All contact folders in the store will be checked, and only contact items will be tried to fix if needed.</dl>
<p> <code>&#8211;task</code></p>
<dl>
<dt>
<dd> All task folders in the store will be checked, and only task items will be tried to fix if needed.</dl>
<p> <code>&#8211;all</code></p>
<dl>
<dt>
<dd> All filters listed above will be checked.</dl>
<h2>AUTHOR</h2>
<p> Written by Zarafa.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-zarafa/">zarafa</a></code>(1) </p>
<h2>Index</h2>
