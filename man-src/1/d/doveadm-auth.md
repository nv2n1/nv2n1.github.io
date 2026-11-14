---
title: "doveadm-auth(1)"
name: "doveadm-auth"
section: "1"
letter: "d"
url: "/docs/linux/man/1-doveadm-auth/"
description: "doveadm-auth – Test authentication for a user"
---

<h2>NAME</h2>
<p> doveadm-auth &#8211; Test authentication for a user</p>
<h2>SYNOPSIS</h2>
<p> <code>doveadm</code> [<code>-Dv</code>] <code>auth</code> [<code>-a</code> <i>auth_socket_path</i>] [<code>-x</code> <i>auth_info</i>] <i>user</i> [<i>password</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>auth</code> command can be used to test the authentication for the given <i>user</i>.</p>
<h2>OPTIONS</h2>
<p> Global <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) <i>options</i>:</p>
<dl>
<dt><code>-D</code></p>
<dd> Enables verbosity and debug messages.</p>
<dt><code>-v</code></p>
<dd> Enables verbosity, including progress counter.</dl>
<p> Command specific <i>options</i>:</p>
<dl>
<dt><code>-a&nbsp;<wbr></code><i>auth_socket_path</i></p>
<dd> This option is used to specify an absolute path to an alternative UNIX domain socket. </p>
<p> By default <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) will use the socket <i>/var/run/dovecot/auth-client</i>. The socket may be located in another directory, when the default <i>base_dir</i> setting was overridden in <i>/etc/dovecot/dovecot.conf</i>.</p>
<dt><code>-x&nbsp;<wbr></code><i>auth_info</i></p>
<dd> <i>auth_info</i> specifies additional conditions for the <code>auth</code> command. The <i>auth_info</i> option string has to be given as <i>name</i><code>=</code><i>value</i> pair. For multiple conditions the <code>-x</code> option could be supplied multiple times.<br />
 Possible names for the <i>auth_info</i> are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>service</code></p>
<dd> The service for which the authentication lookup should be tested. The value may be the name of a service, commonly used with Dovecot. For example: <code>imap</code>, <code>pop3&nbsp;<wbr></code>or <code>smtp</code>.</p>
<dt><code>lip</code></p>
<dd> The local IP address (server) for the test.</p>
<dt><code>rip</code></p>
<dd> The remote IP address (client) for the test.</p>
<dt><code>lport</code></p>
<dd> The local port, e.g. 143</p>
<dt><code>rport</code></p>
<dd> The remote port, e.g. 24567</dl>
</dl>
</dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><i>user</i></p>
<dd> The <i>user</i>&#8216;s login name. Depending on the configuration, the login name may be for example <code>jane</code> or <code>john [at] example.com</code>.</p>
<dt><i>password</i></p>
<dd> Optionally the user&#8217;s password. <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) will prompt for the password, if none was given.</dl>
<h2>EXAMPLE</h2>
<p> This example demonstrates an imap authentication test for user john, assuming the user is connected from the host with the IP address 192.0.2.143. </p>
<pre>
<code>doveadm auth -x service=imap -x rip=192.0.2.143 john johns_password</code>
passdb: john auth succeeded
extra fields:
  user=john
</pre>
<h2>REPORTING BUGS</h2>
<p> Report bugs, including <i>doveconf -n</i> output, to the Dovecot Mailing List &lt;dovecot [at] dovecot.org&gt;. Information about reporting bugs is available at: <a rel="nofollow" href="http://dovecot.org/bugreport.html">http://dovecot.org/bugreport.html</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1), <code><a href="/docs/linux/man/1-doveconf/">doveconf</a></code>(1) </p>
<h2>Index</h2>
