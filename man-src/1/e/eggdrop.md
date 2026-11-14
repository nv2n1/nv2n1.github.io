---
title: "eggdrop(1)"
name: "eggdrop"
section: "1"
letter: "e"
url: "/docs/linux/man/1-eggdrop/"
description: "eggdrop – an IRC bot"
---

<h2>NAME</h2>
<p> eggdrop &#8211; an IRC bot</p>
<h2>SYNOPSIS</h2>
<p> <code>eggdrop</code> [<code>options</code>] [<code>config-file</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Eggdrop</code> is the World&#8217;s most popular Internet Relay Chat (IRC) bot; it is freely distributable under the GNU General Public License (GPL). Eggdrop is a feature rich program designed to be easily used and expanded upon by both novice and advanced IRC users on a variety of hardware and software platforms. </p>
<p> An IRC bot is a program that sits on an IRC channel and performs automated tasks while looking just like a normal user on the channel. Some of these functions include protecting the channel from abuse, allowing privileged users to gain op or voice status, logging channel events, providing information, hosting games, etc. </p>
<p> One of the features that makes Eggdrop stand out from other bots is module and Tcl scripting support. With scripts and modules, you can make the bot perform almost any task you want. They can do anything from preventing floods to greeting users and banning advertisers from channels. </p>
<p> You can also link multiple Eggdrop bots together to form a botnet. This can allow bots to op each other securely, control floods efficiently, and even link channels across multiple IRC networks. It also allows the Eggdrops share user lists, ban lists, exempt/invite lists, and ignore lists with other bots if userfile sharing is enabled. This allows users to have the same access on every bot on your botnet. It also allows the bots to distribute tasks such as opping and banning users. See doc/BOTNET for information on setting up a botnet. </p>
<p> Eggdrop needs a config file to run. For an example, have a look at <code>eggdrop.conf</code> which is distributed with Eggdrop.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> Display a list of command-line options.</p>
<dt><code>-n</code></p>
<dd> Don&#8217;t background. Normally, Eggdrop will move itself into the background when you start it up, meaning you&#8217;ll get another shell prompt, and you can do other things while the bot is running. With -n, you won&#8217;t return to the shell prompt until the bot exits (which won&#8217;t normally happen until it&#8217;s killed). By default, -n will send all log entries to the console.</p>
<dt><code>-nt</code></p>
<dd> Don&#8217;t background, use terminal. This is just like -n, except that instead of seeing log entries, your console will simulate a DCC chat with the bot.</p>
<dt><code>-nc</code></p>
<dd> Don&#8217;t background, show channel info. This is just like -n, except that instead of seeing log entries, every 10 seconds your screen will clear and you will see the current channel status, sort of like &quot;top&quot;.</p>
<dt><code>-m</code></p>
<dd> Create userfile. If you don&#8217;t have a userfile, this will make Eggdrop create one and give owner status to the first person that introduces himself or herself to it. You&#8217;ll need to do this when you first set up your bot.</p>
<dt><code>-v</code></p>
<dd> Show version info, then quit.</dl>
<h2>SIGNALS</h2>
<dl>
<dt><code>SIGCHLD</code></p>
<dd> This signal is ignored by Eggdrop and can be used to determine whether it&#8217;s running or not.</p>
<dt><code>SIGTERM</code></p>
<dd> Depending on die-on-sigterm being set to 0 or 1 in the config file, Eggdrop will save its user and channel file and/or die.</p>
<dt><code>SIGHUP</code></p>
<dd> Depending on die-on-sighup being set to 0 or 1 in the config file, Eggdrop will rehash (reload its config file) or die.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>EGG_LANG</code></p>
<dd> This variable can be set to the language in which you want Eggdrop to speak<br />
&nbsp;<wbr>to you. It defaults to English, but German, French, Finnish, and Danish are supported, too.</p>
<dt><code>EGG_LANGDIR</code></p>
<dd> Specifies the directory where all your language files are stored. The default is ./language.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-tclsh/">tclsh</a>(1), <a href="/docs/linux/man/1-irc/">irc</a>(1), <a href="/docs/linux/man/1-ircii/">ircII</a>(1), <a href="/docs/linux/man/8-ircd/">ircd</a>(8) </p>
<p> There is extensive <code>online documentation.</code> Once you get the bot running, open a DCC chat with it, and type: <code>.help</code> </p>
<p> In addition, the files in the <code>doc/</code> directory provide <code>detailed information</code> about how Eggdrop works and how to use it.</p>
<h2>AUTHORS</h2>
<p> Written by Robey Pointer, the Eggheads Development Team and various others. See the files <code>AUTHORS</code> for a list of Eggdrop developers and major contributors, <code>THANKS</code> for a full list of Eggdrop contributors, and the <code>doc/Changes</code> files for a list of changes made to each version of Eggdrop.</p>
<h2>REPORTING BUGS</h2>
<p> See <code>doc/BUG-REPORT</code>. </p>
<p> Bugs can either be reported directly to BugZilla, at <code><a rel="nofollow" href="http://bugzilla.eggheads.org">http://bugzilla.eggheads.org</a></code>, or via e-mail to &lt;<code>bugs [at] eggheads.org</code>&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1997 Robey Pointer<br />
 Copyright (C) 1999 &#8211; 2011 Eggheads Development Team </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple Place &#8211; Suite 330, Boston, MA 02111-1307, USA. </p>
<h2>Index</h2>
