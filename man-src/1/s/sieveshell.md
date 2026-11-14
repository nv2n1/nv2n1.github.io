---
title: "sieveshell(1)"
name: "sieveshell"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sieveshell/"
description: "sieveshell – remotely manipulate sieve scripts"
---

<h2 class="name">NAME</h2>
<p> sieveshell &#8211; remotely manipulate sieve scripts </p>
<h2>SYNOPSIS</h2>
<p> sieveshell [<code>&#8211;user</code>=<i>user</i>] [<code>&#8211;authname</code>=<i>authname</i>] [<code>&#8211;realm</code>=<i>realm</i>] [<code>&#8211;exec</code>=<i>script</i>] <i>server</i>[<code>:</code><i>port</i>] </p>
<p> sieveshell <code>&#8211;help</code></p>
<h2>DESCRIPTION</h2>
<p> <code>sieveshell</code> allows users to manipulate their scripts on a remote server. It works via <font SIZE="-1">MANAGESIEVE,</font> a work in progress. </p>
<p> The following commands are recognized: </p>
<dl>
<dt>
<dd> <code>list</code> list scripts on server. </p>
<p> <code>put</code> &lt;filename&gt; upload script to server. </p>
<p> <code>get</code> &lt;name&gt; [&lt;filename&gt;] get script. if no filename display to stdout </p>
<p> <code>delete</code> &lt;name&gt; delete script. </p>
<p> <code>activate</code> &lt;name&gt; activate script. </p>
<p> <code>deactivate</code> deactivate all scripts.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-u</code> <i>user</i>, <code>&#8211;user</code>=<i>user</i></p>
<dd> The authorization name to request; by default, derived from the authentication credentials.</p>
<dt><code>-a</code> <i>authname</i>, <code>&#8211;authname</code>=<i>authname</i></p>
<dd> The user to use for authentication (defaults to current user).</p>
<dt><code>-r</code> <i>realm</i>, <code>&#8211;realm</code>=<i>realm</i></p>
<dd> The realm to attempt authentication in.</p>
<dt><code>-e</code> <i>script</i>, <code>&#8211;exec</code>=<i>script</i></p>
<dd> Instead of working interactively, run commands from <i>script</i>, and exit when done.</dl>
<h2>REFERENCES</h2>
<p> [<font SIZE="-1">MANAGESIEVE</font>] Martin, T.; &#8220;A Protocol for Remotely Managing Sieve Scripts&#8221;, draft-ietf-managesieve-03.txt, Mirapoint, Inc.; May 2001, work in progress.</p>
<h2>AUTHOR</h2>
<p> Tim Martin &lt;tmartin [at] mirapoint.com&gt;, and the rest of the Cyrus team &lt;cyrus-bugs [at] andrew.cmu.edu&gt;. </p>
<h2>Index</h2>
