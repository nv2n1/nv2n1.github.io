---
title: "doveadm-kick(1)"
name: "doveadm-kick"
section: "1"
letter: "d"
url: "/docs/linux/man/1-doveadm-kick/"
description: "doveadm-kick – Disconnect users by user name and/or IP address"
---

<h2>NAME</h2>
<p> doveadm-kick &#8211; Disconnect users by user name and/or IP address</p>
<h2>SYNOPSIS</h2>
<p> <code>doveadm</code> [<code>-Dv</code>] <code>kick</code> [ -a <i>anvil_socket_path</i>] [<code>-f</code>] <i>user</i><br />
 <code>doveadm</code> [<code>-Dv</code>] <code>kick</code> [ -a <i>anvil_socket_path</i>] [<code>-f</code>] <i>ip</i>[<code>/</code><i>mask</i>]<br />
 <code>doveadm</code> [<code>-Dv</code>] <code>kick</code> [ -a <i>anvil_socket_path</i>] [<code>-f</code>] <i>user</i> <i>ip</i>[<code>/</code><i>mask</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>doveadm</code>&#8216;s&nbsp;<wbr><code>kick</code> command is used to disconnect users by <i>user</i> name and/or the <i>ip</i> address, from which they are connected. </p>
<p> In the first form, all users, whose login name matches the <i>user</i> argument, will be disconnected. </p>
<p> In the second form, all users, connected from the given IP address or network range, will be disconnected. </p>
<p> In the last form, only users connected from the given IP address or networks range and a matching login name will be disconnected.</p>
<h2>OPTIONS</h2>
<p> Global <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) <i>options</i>:</p>
<dl>
<dt><code>-D</code></p>
<dd> Enables verbosity and debug messages.</p>
<dt><code>-v</code></p>
<dd> Enables verbosity, including progress counter.</dl>
<p> Command specific <i>options</i>:</p>
<dl>
<dt><code>-a&nbsp;<wbr></code><i>anvil_socket_path</i></p>
<dd> This option is used to specify an absolute path to an alternative UNIX domain socket. </p>
<p> By default <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) will use the socket <i>/var/run/dovecot/anvil</i>. The socket may be located in another directory, when the default <i>base_dir</i> setting was overridden in <i>/etc/dovecot/dovecot.conf</i>.</p>
<dt><code>-f</code></p>
<dd> Enforce the disconnect, even when there are multiple <i>user</i>s, from different networks, connected to a single process. This option may be only required when you have configured something like: </p>
<pre>
service imap {
  ...
  client_limit = <i>1+n</i>
  service_count = 0
  ...
}
</pre>
</dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><i>ip</i>[/<i>mask</i>]</p>
<dd> <i>ip</i> or <i>ip</i><code>/</code><i>mask</i> is the host or network, from which the users are connected.</p>
<dt><i>user</i></p>
<dd> Is a <i>user</i>&#8216;s login name. Depending on the configuration, a login name may be for example <code>jane</code> or <code>john [at] example.com</code>. It&#8217;s also possible to use &#8216;<code>*</code>&#8216; and &#8216;<code>?</code>&#8216; wildcards (e.g. -u *@example.org).</dl>
<h2>EXAMPLE</h2>
<p> If you don&#8217;t want to disconnect all users at once, you can check who&#8217;s currently logged in. The first example demonstrates how to disconnect all users whose login name is 3 characters long and begins with <code>ba</code>. </p>
<pre>
<code>doveadm who -1 ja*</code>
username                      proto pid  ip
jane                          imap  8192 ::1
james                         imap  8203 2001:db8:543:2::1
<code>doveadm kick ba?</code>
kicked connections from the following users:
bar baz
</pre>
<p> The next example shows how to kick user foo&#8217;s connections from 192.0.2.*. </p>
<pre>
<code>doveadm who -1 foo</code>
username                     proto pid  ip
foo                          imap  8135 fd95:4eed:38ba::25
foo                          imap  9112 192.0.2.53
foo                          imap  8216 192.0.2.111
<code>doveadm kick foo 192.0.2.0/24</code>
kicked connections from the following users:
foo
<code>doveadm who f*</code>
username                  # proto (pids) (ips)
foo                       1 imap  (8135) (fd95:4eed:38ba::25)
</pre>
<h2>REPORTING BUGS</h2>
<p> Report bugs, including <i>doveconf -n</i> output, to the Dovecot Mailing List &lt;dovecot [at] dovecot.org&gt;. Information about reporting bugs is available at: <a rel="nofollow" href="http://dovecot.org/bugreport.html">http://dovecot.org/bugreport.html</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1), <code><a href="/docs/linux/man/1-doveadm-who/">doveadm-who</a></code>(1) </p>
<h2>Index</h2>
