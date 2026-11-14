---
title: "eurephiadm(7)"
name: "eurephiadm"
section: "7"
letter: "e"
url: "/docs/linux/man/7-eurephiadm/"
description: "eurephiadm – eurephia administration utility"
---

<p>eurephiadm &#8211; eurephia administration utility</p>
<h2>Synopsis</h2>
<p><code>eurephiadm</code> &lt;command&gt; [\-h|\-\-help] [\-V|\-\-version] [&lt;global options&gt;] [\-l|\-\-log &lt;filename&gt;] [\-L|\-\-log\-level &lt;log level&gt;] [&lt;command arguments&gt;]</p>
<h2>Description</h2>
<p><code>eurephiadm</code> is a generic command line tool for administering and configuring the eurephia plug-in for OpenVPN.</p>
<h2>Commands</h2>
<p>Available commands in <code>eurephiadm</code></p>
<dl>
<dt><code>help</code> [&lt;command&gt;]</p>
<dd>This help screen if no arguments are given. If a command is given, the help screen for that command is provided.</p>
<dt><code>logout</code></p>
<dd>Logout from an active eurephiadm session. Most of the operations in eurephiadm requires the user to authenticate him/herself. The session will then be active for a predefined amount of time, not requiring new authentications. The user will have to authenticate him/herself again if the session timesout or the <code>logout</code> command is used.</p>
<dt><code>users</code> [&lt;arguments&gt;]</p>
<dd>User management module. Lists, adds, removes, activates, deactivates and shows user account information for each eurephia user.</p>
<dt><code>lastlog</code></p>
<dd>Query the eurephia lastlog. This log contains information about OpenVPN session authenticated via eurephia.</p>
<dt><code>attempts</code> [&lt;arguments&gt;]</p>
<dd>Show or reset registered failed login attempts registrations.</p>
<dt><code>blacklist</code> [&lt;arguments&gt;]</p>
<dd>Show, add or delete blacklisted user accounts, certificates or IP addresses.</p>
<dt><code>certs</code> [&lt;arguments&gt;]</p>
<dd>SSL Certificate management for eurephia authentication.</p>
<dt><code>usercerts</code> [&lt;arguments&gt;]</p>
<dd>Manages the relations between eurephia user accounts and certificates. This combination is called a user access, and defines which access level the authenticated eurephia user will have to the network.</p>
<dt><code>fwprofiles</code> [&lt;arguments&gt;]</p>
<dd>Firewall profile management. Add, list or delete (iptables) profiles available for eurephia in the operating system. This feature is only available if eurephiadm was compiled with firewall support.</p>
<dt><code>adminaccess</code> [&lt;arguments&gt;]</p>
<dd>Manages eurephia user accesses to administration utilities like <code>eurephiadm</code>.</p>
<dt><code>show-config</code></p>
<dd>List all config settings set in the database and in the <code>~/.eurephia/eurephiadm.cfg</code> file.</p>
<dt><code>show-configfile</code></p>
<dd>Similar to the <code>show-config</code> command, but lists only the parsed settings in the <code>~/.eurephia/eurephiadm.cfg</code> file.</p>
<dt><code>config</code> [&lt;arguments&gt;]</p>
<dd>Add, delete or show eurephia configuration settings stored in the database.</dl>
<h2>Files</h2>
<dl>
<dt><code>~/.eurephia/eurephiadm.cfg</code></p>
<dd>Default configuration file which defines the database driver and the needed database parameters.</dl>
<h2>Configuration File</h2>
<p>The configuration file is a simple key-value based text file, where keys and values are separated by an equal sign (&quot;=&quot;). All text coming after a hash (&quot;#&quot;) will be ignored and considered as comments. The variables eurephiadm uses are:</p>
<dl>
<dt><code>database_driver</code></p>
<dd>Contains a full path to the database driver eurephiadm need to use.</p>
<dt><code>database_params</code></p>
<dd>All database arguments the database driver requires must be set here. See the man page for the corresponding database driver for more information about valid options.</p>
<dt><code>log</code></p>
<dd>Defines how to log. If a file name is given, logging will be sent to this log file. Other valid values are:</p>
<dd><code>stderr:</code> or <code>stdout:</code><br />
 Logging will go directly to stderr or stdout</p>
<dd><code>syslog:[local0..local7 | daemon | authpriv]</code><br />
 Logging will be sent to syslog. The default syslog destination is daemon<code>.</p>
<dt>log_level</code></p>
<dd>Sets the log verbosity. Normally the values will be from 0 to 10, where 0 is as little logging as possible and 10 is very verbose. If eurephiadm or the database driver is compiled with debug logging, values up to 50 will be valid.</p>
<dt><code>username</code></p>
<dd><code>eurephiadm</code> will always be asking for a user name when logging into the administration application. By setting this variable, you will set a default user name eurephiadm will use when logging in and it will only ask for a password directly.</dl>
<h2>Environment</h2>
<dl>
<dt><code>EUREPHIA_DIR</code></p>
<dd>The <code>eurephiadm</code> utility looks for a configuration file by default in <code>~/.eurephia/eurephiadm.cfg</code>. This directory can be overridden by setting the <code>EUREPHIA_DIR</code> environment variable, and eurephiadm will use the <code>eurephiadm.cfg</code> file in this directory instead.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-eurephiadm-users/">eurephiadm-users</a></code>(7), <code><a href="/docs/linux/man/7-eurephiadm-lastlog/">eurephiadm-lastlog</a></code>(7), <code><a href="/docs/linux/man/7-eurephiadm-attempts/">eurephiadm-attempts</a></code>(7), <code><a href="/docs/linux/man/7-eurephiadm-blacklist/">eurephiadm-blacklist</a></code>(7), <code><a href="/docs/linux/man/7-eurephiadm-certs/">eurephiadm-certs</a></code>(7), <code><a href="/docs/linux/man/7-eurephiadm-usercerts/">eurephiadm-usercerts</a></code>(7), <code><a href="/docs/linux/man/7-eurephiadm-fwprofiles/">eurephiadm-fwprofiles</a></code>(7), <code><a href="/docs/linux/man/7-eurephiadm-adminaccess/">eurephiadm-adminaccess</a></code>(7), <code><a href="/docs/linux/man/7-eurephiadm-config/">eurephiadm-config</a></code>(7), <code><a href="/docs/linux/man/7-edb-sqlite/">edb-sqlite</a></code>(7)</p>
<h2>Author</h2>
<p>Copyright (C) 2008-2010 David Sommerseth &lt;dazo [at] users.sourceforge.net&gt;</p>
