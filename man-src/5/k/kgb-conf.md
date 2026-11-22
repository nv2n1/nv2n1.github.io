---
title: "kgb-conf(5)"
name: "kgb-conf"
section: "5"
letter: "k"
url: "/docs/linux/man/5-kgb-conf/"
description: "kgb.conf — KGB bot configuration file"
---

<p>kgb.conf &#8212; KGB bot configuration file</p>
<h2>Description</h2>
<p><i>kgb.conf</i> is the main configuration file of the KGB bot. Its location is in <i>/etc/kgb-bot/</i> unless changed with the <code>&#8211;conf</code> command line option. See <i><a href="/docs/linux/man/1-kgb-bot/">kgb-bot</a></i>(1). </p>
<p> The file format is YAML. Elaborate example configuration is at the end of this document.</p>
<h2>Settings</h2>
<h3>soap</h3>
<p>A map with the following possible keys:</p>
<dl>
<dt><code>server_addr</code></dt>
<dd>IP address to listen to.</dd>
<dt><code>server_port</code></dt>
<dd>Port to listen to.</dd>
<dt><code>service_name</code></dt>
<dd>SOAP service name. Defaults to <tt>&quot;KGB&quot;</tt>.</dd></dl>
<h3>pid_dir</h3>
<p>Directory to store PID file to. Defautls to <i>/var/run/kgb-bot/</i>.</p>
<h3>include</h3>
<p>Path to file with additional configuration. May be a path to a directory, in which case all files in it ending with <tt>&quot;.conf&quot;</tt> are loaded, in alphabetical order.</p>
<h3>min_protocol_version</h3>
<p>Minimum version of the protocol that will be supported by the server. Defaults to <tt>1</tt>. Protocol version 0 has no authentication.</p>
<h3>queue_limit</h3>
<p>When messages are sent to IRC, there is certain rate limitting, which may prevent the message to be sent right away. In this case messages are enqueued, and this parameter configures the size of the queue. When the queue is full client requests are rejected.</p>
<h3>repositories</h3>
<p>A map with keys project names and values maps with project details:</p>
<dl>
<dt>password</dt>
<dd>Password used for authenticating all requests from this project.</dd>
<dt>private</dt>
<dd>If true, disables commit announces to &#8216;broadcast&#8217; IRC channels.</dd></dl>
<h3>networks</h3>
<p>A map with keys network names and values map of network configuration, containing the following items:</p>
<dl>
<dt>server</dt>
<dd>IP address/hostname of the IRC server to connect to.</dd>
<dt>port</dt>
<dd>Port number to connect to.</dd>
<dt>nick</dt>
<dd>Bot&#8217;s nick on the network.</dd>
<dt>ircname</dt>
<dd>The full name of the bot on the network.</dd>
<dt>username</dt>
<dd>The username presented to the network.</dd>
<dt>password</dt>
<dd>A password for the network.</dd>
<dt>nickserv_password</dt>
<dd>A password for Nick server identification.</dd>
<dt>flood</dt>
<dd>If defined to a true value, the built-in rate-limitting feature of the IRC component will be turned off. <code>WARNING</code>: this may cause the bot to be kicked off the IRC network. Use only when you control both the bot and the IRC network (e.g. when testing).</dd></dl>
<h3>channels</h3>
<p>A list of channels. Each element is a map and represents the channel&#8217;s configuration:</p>
<dl>
<dt>name</dt>
<dd>Channel name, e.g. <tt>&quot;#commits&quot;</tt>. <code>Mandatory</code>.</dd>
<dt>network</dt>
<dd>Network name, as described in the <code>networks</code> map. <code>Mandatory</code>.</dd>
<dt>broadcast</dt>
<dd>Enables broadcasting all commit notifications to this channel.</dd>
<dt>repos</dt>
<dd>A list of project names, as described in the <code>repositories</code> map. Mandatory unless broadcast is enabled.</dd>
<dt>smart_answers</dt>
<dd>Each channel can contain separate list of smart answers, see below.</dd></dl>
<h3>smart_answers</h3>
<p>A list of strings to be used as replies when the bot is addressed on IRC.</p>
<h3>smart_answers_polygen</h3>
<p>If set to a true value, <i>polygen</i>(1) will be used to generate replies when the bot is addressed on IRC.</p>
<h3>debug</h3>
<p>Enables logging of additional diagnostic information.</p>
<h3>admins</h3>
<p>A list of IRC masks, used to determine if a given IRC nick is bot administrator. Note that currently these nicks have no additional power.</p>
<h3>colors</h3>
<p>A map of colors to be used when painting commit messages. The following keys are recognized:</p>
<dl>
<dt>revision</dt>
<dd>Commit ID. Default: none.</dd>
<dt>path</dt>
<dd>Changed path. Default: teal. </dd>
<p> Depending on the action performed to the path, additional coloring is made:</p>
<dl>
<dd>
</dd><dl>
<dt>addition</dt>
<dd>Used for added paths. Default: green.</dd>
<dt>modification</dt>
<dd>Used for modified paths. Default: teal.</dd>
<dt>deletion</dt>
<dd>Used for deleted paths. Default: bold red.</dd>
<dt>replacement</dt>
<dd>Used for replaced paths (a Subversion concept). Default: brown.</dd>
<dt>prop_change</dt>
<dd>Used for paths with changed properties (a Subversion concept), combined with other colors depending on the action &#8212; addition, modification or replacement. Default: underline.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
<dt>author</dt>
<dd>Commit author. Default: green.</dd>
<dt>branch</dt>
<dd>Commit branch. Default: brown.</dd>
<dt>module</dt>
<dd>Project module. Default: purple.</dd>
<dt>web</dt>
<dd>URL to commit information. Default: silver.</dd>
<dt>separator</dt>
<dd>The separator before the commit log. Default: none.</dd></dl>
<h2>Example Confguration</h2>
<pre> # vim: filetype=yaml
 ---
 soap:
 server_addr: 127.0.0.1
 server_port: 9999
 service_name: KGB
 queue_limit: 150
 log_file: &quot;/var/log/kgb-bot.log&quot;
 include: &quot;/etc/kgb-bot/kgb.conf.d&quot;
 repositories:
 # just a name to identify it
 foo:
 # needs to be the same on the client
 password: supersecret
 # private repositories aren't announced to broadcast channels
 # private: yes
 # Some witty answer for people that talk to the bot
 #smart_answers:
 # - &quot;I wont speak with you!&quot;
 # - &quot;Do not disturb!&quot;
 # - &quot;Leave me alone, I am buzy!&quot;
 # Admins are allowed some special !commands (currently only !version)
 #admins:
 # - some!irc [at] mask
 # - some!other [at] host
 networks:
 freenode:
 nick: KGB
 ircname: KGB bot
 username: kgb
 password: ~
 nickserv_password: ~
 server: irc.freenode.net
 port: 6667
 channels:
 # a broadcast channel
 - name: '#commits'
 network: freenode
 broadcast: yes
 # a channel, tied to one or several repositories
 - name: '#foo'
 network: freenode
 repos:
 - foo
 # Can also be set per-channel
 #smart_answers:
 # - &quot;I'm in ur channel, watching ur commits!&quot;
 # - &quot;I am not listening&quot;
 # - &quot;Shut up! I am buzy watching you.&quot;
 pid_dir: /var/run/kgb-bot
 # anything less is rejected
 min_protocol_ver: 1
 # default colors:
 colors:
 repository: bold
 revision: bold
 author: green
 branch: brown
 module: purple
 path: teal
 addition: green
 modification: teal
 deletion: &quot;bold red&quot;
 replacement: reverse
 prop_change: underline
 web: silver
 # you can combine them like &quot;bold red&quot; (ouch!)
 # available colors: black, navy, green, red, brown, purple, orange, yellow,
 # lime, teal, aqua, blue, fuchsia, gray, silver, white
 # available modifiers: bold underline reverse</pre>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-kgb-bot/">kgb-bot</a></i>(1), <i><a href="/docs/linux/man/1-kgb-client/">kgb-client</a></i>(1)</p>
<h2>Author</h2>
<dl>
<dt>Damyan Ivanov dmn [at] debian.org</dt>
<dd></dd></dl>
<h2>COPYRIGHT &amp; LICENSE</h2>
<p>Copyright (C) 2012, 2013 Damyan Ivanov </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.</p>
