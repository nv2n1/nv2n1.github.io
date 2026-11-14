---
title: "prosodyctl(1)"
name: "prosodyctl"
section: "1"
letter: "p"
url: "/docs/linux/man/1-prosodyctl/"
description: "prosodyctl – Manage a Prosody XMPP server"
---

<h2 class="name">NAME</h2>
<p> prosodyctl &#8211; Manage a Prosody XMPP server</p>
<h2>SYNOPSIS</h2>
<p> <code>prosodyctl</code> <i>command</i> [<i>&#8211;help</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>prosodyctl</code> is the control tool for the Prosody XMPP server. It may be used to control the server daemon and manage users. </p>
<p> <code>prosodyctl</code> needs to be executed with sufficient privileges to perform its commands. This typically means executing <code>prosodyctl</code> as the root user. If a user named &quot;prosody&quot; is found then <code>prosodyctl</code> will change to that user before executing its commands. </p>
<h2>COMMANDS</h2>
<h3>User Management</h3>
<p> In the following commands users are identified by a Jabber ID, <i>jid</i>, of the usual form: user [at] domain. </p>
<dl>
<dt><code>adduser</code> <i>jid</i></p>
<dd> Adds a user with Jabber ID, <i>jid</i>, to the server. You will be prompted to enter the user&#8217;s password. </p>
<dt><code>passwd</code> <i>jid</i></p>
<dd> Changes the password of an existing user with Jabber ID, <i>jid</i>. You will be prompted to enter the user&#8217;s new password. </p>
<dt><code>deluser</code> <i>jid</i></p>
<dd> Deletes an existing user with Jabber ID, <i>jid</i>, from the server. </p>
</dl>
<h3>Daemon Management</h3>
<p> Although <code>prosodyctl</code> has commands to manage the <code>prosody</code> daemon it is recommended that you utilize your distributions daemon management features if you attained Prosody through a package. </p>
<p> To perform daemon control commands <code>prosodyctl</code> needs a <i>pidfile</i> value specified in <i>/etc/prosody/prosody.cfg.lua</i>. Failure to do so will cause <code>prosodyctl</code> to complain. </p>
<dl>
<dt><code>start</code></p>
<dd> Starts the <code>prosody</code> server daemon. If run as root <code>prosodyctl</code> will attempt to change to a user named &quot;prosody&quot; before executing. This operation will block for up to five seconds to wait for the server to execute. </p>
<dt><code>stop</code></p>
<dd> Stops the <code>prosody</code> server daemon. This operation will block for up to five seconds to wait for the server to stop executing. </p>
<dt><code>restart</code></p>
<dd> Restarts the <code>prosody</code> server daemon. Equivalent to running <code>prosodyctl stop</code> followed by <code>prosodyctl start</code>. </p>
<dt><code>status</code></p>
<dd> Prints the current execution status of the <code>prosody</code> server daemon. </p>
</dl>
<h3>Ejabberd Compatibility</h3>
<p> <code>ejabberd</code> is another XMPP server which provides a comparable control tool, <code>ejabberdctl</code>, to control its server&#8217;s operations. <code>prosodyctl</code> implements some commands which are compatible with <code>ejabberdctl</code>. For details of how these commands work you should see <code><a href="/docs/linux/man/8-ejabberdctl/">ejabberdctl</a></code>(8). </p>
<dl>
<dt><code>register</code> <i>user server password</i></p>
<dd>
<dt><code>unregister</code> <i>user server</i></p>
<dd>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><i>&#8211;help</i></p>
<dd> Display help text for the specified command. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/prosody/prosody.cfg.lua</i></p>
<dd> The main <code>prosody</code> configuration file. <code>prosodyctl</code> reads this to determine the process ID file of the <code>prosody</code> server daemon and to determine if a host has been configured. </p>
</dl>
<h2>ONLINE</h2>
<p> More information may be found online at: <i><a rel="nofollow" href="http://prosody.im/">http://prosody.im/</a></i> </p>
<h2>AUTHORS</h2>
<p> Dwayne Bent &lt;dbb.1 [at] liqd.org&gt; </p>
<h2>Index</h2>
