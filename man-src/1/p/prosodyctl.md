---

title: "prosodyctl(1)"
name: "prosodyctl"
section: "1"
letter: "p"
url: "/docs/linux/man/1-prosodyctl/"
description: "prosodyctl – Manage a Prosody XMPP server"
---

<p> <code>prosodyctl</code> <i>command</i> [<i>&#8211;help</i>] </p>
<p> <code>prosodyctl</code> is the control tool for the Prosody XMPP server. It may be used to control the server daemon and manage users. </p>
<p> <code>prosodyctl</code> needs to be executed with sufficient privileges to perform its commands. This typically means executing <code>prosodyctl</code> as the root user. If a user named &quot;prosody&quot; is found then <code>prosodyctl</code> will change to that user before executing its commands. </p>
<h2>COMMANDS</h2>
<h3>User Management</h3>
<p> In the following commands users are identified by a Jabber ID, <i>jid</i>, of the usual form: user [at] domain. </p>
<dl>
<dt><code>adduser</code> <i>jid</i></dt>
<dd> Adds a user with Jabber ID, <i>jid</i>, to the server. You will be prompted to enter the user&#8217;s password. </dd>
<dt><code>passwd</code> <i>jid</i></dt>
<dd> Changes the password of an existing user with Jabber ID, <i>jid</i>. You will be prompted to enter the user&#8217;s new password. </dd>
<dt><code>deluser</code> <i>jid</i></dt>
<dd> Deletes an existing user with Jabber ID, <i>jid</i>, from the server. </dd>
</dl>
<h3>Daemon Management</h3>
<p> Although <code>prosodyctl</code> has commands to manage the <code>prosody</code> daemon it is recommended that you utilize your distributions daemon management features if you attained Prosody through a package. </p>
<p> To perform daemon control commands <code>prosodyctl</code> needs a <i>pidfile</i> value specified in <i>/etc/prosody/prosody.cfg.lua</i>. Failure to do so will cause <code>prosodyctl</code> to complain. </p>
<dl>
<dt><code>start</code></dt>
<dd> Starts the <code>prosody</code> server daemon. If run as root <code>prosodyctl</code> will attempt to change to a user named &quot;prosody&quot; before executing. This operation will block for up to five seconds to wait for the server to execute. </dd>
<dt><code>stop</code></dt>
<dd> Stops the <code>prosody</code> server daemon. This operation will block for up to five seconds to wait for the server to stop executing. </dd>
<dt><code>restart</code></dt>
<dd> Restarts the <code>prosody</code> server daemon. Equivalent to running <code>prosodyctl stop</code> followed by <code>prosodyctl start</code>. </dd>
<dt><code>status</code></dt>
<dd> Prints the current execution status of the <code>prosody</code> server daemon. </dd>
</dl>
<h3>Ejabberd Compatibility</h3>
<p> <code>ejabberd</code> is another XMPP server which provides a comparable control tool, <code>ejabberdctl</code>, to control its server&#8217;s operations. <code>prosodyctl</code> implements some commands which are compatible with <code>ejabberdctl</code>. For details of how these commands work you should see <code>ejabberdctl</code>(8). </p>
<dl>
<dt><code>register</code> <i>user server password</i></dt>
<dd>
</dd><dt><code>unregister</code> <i>user server</i></dt>
<dd>
</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><i>&#8211;help</i></dt>
<dd> Display help text for the specified command. </dd>
</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/prosody/prosody.cfg.lua</i></dt>
<dd> The main <code>prosody</code> configuration file. <code>prosodyctl</code> reads this to determine the process ID file of the <code>prosody</code> server daemon and to determine if a host has been configured. </dd>
</dl>
<h2>ONLINE</h2>
<p> More information may be found online at: <i><a rel="nofollow" href="http://prosody.im/">http://prosody.im/</a></i> </p>
<h2>AUTHORS</h2>
<p> Dwayne Bent &lt;dbb.1 [at] liqd.org&gt; </p>
