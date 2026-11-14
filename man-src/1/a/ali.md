---
title: "ali(1)"
name: "ali"
section: "1"
letter: "a"
url: "/docs/linux/man/1-ali/"
description: "ali – list mail aliases"
---

<h2 class="name">NAME</h2>
<p> ali &#8211; list mail aliases </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ali</code> [<code>-alias</code> <i>aliasfile</i>] [<code>-list</code> | <code>-nolist</code>] [<code>-user</code> | <code>-nouser</code>] [<code>-version</code>] [<code>-help</code>] [<i>aliases</i> &#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>Ali</code></p>
<dd>searches the named mail alias files for each of the given <i>aliases</i>. It creates a list of addresses for those <i>aliases</i>, and writes that list on standard output. If no arguments are given, <code>ali</code> outputs all alias entries. </p>
<p> By default, when an aliases expands to multiple addresses, the addresses are separated by commas and printed on as few lines as possible. If the <code>-list</code> option is specified, then when an address expands to multiple addresses, each address will appear on a separate line. </p>
<p> The switch <code>-user</code> directs <code>ali</code> to perform its processing in an inverted fashion: instead of listing the addresses that each given alias expands to, <code>ali</code> will list the aliases that expand to each given address. </p>
<p> The files specified by the profile entry &#8220;<i>Aliasfile</i>&#8221; and any additional alias files given by the <code>-alias</code> <i>aliasfile</i> switch will be read. Each <i>alias</i> is processed as described in <i><a href="/docs/linux/man/5-mh-alias/">mh-alias</a></i>(5).</p>
<h2>FILES</h2>
<p> Alias files are looked up in multiple locations: if the pathname is absolute or starts with &#8220;<i>.</i>&#8221; or &#8220;<i>..</i>&#8221; then it&#8217;s accessed directly; otherwise tilde expansion is done on usernames, then files are searched for in the user&#8217;s <i>Mail</i> directory as specified in their profile. If not found there, the directory &#8220;<i>/etc/nmh</i>&#8221; is checked. </p>
<dl>
<dt>$HOME/.mh_profile</p>
<dd> The user&#8217;s profile.</dl>
<h2>PROFILE COMPONENTS</h2>
<dl>
<dt>Path:</p>
<dd> To determine the user&#8217;s nmh directory</p>
<dt>Aliasfile:</p>
<dd> For a default alias file</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-mh-alias/">mh-alias</a></i>(5)</p>
<h2>DEFAULTS</h2>
<dl>
<dt>aliasfile</p>
<dd> /etc/nmh/MailAliases</p>
<dt>-nolist</p>
<dd>
<dt>-nouser</p>
<dd></dl>
<h2>CONTEXT</h2>
<p> None</p>
<h2>BUGS</h2>
<p> The <code>-user</code> option with <code>-nonormalize</code> is not entirely accurate, as it does not replace local nicknames for hosts with their official site names. </p>
<h2>Index</h2>
