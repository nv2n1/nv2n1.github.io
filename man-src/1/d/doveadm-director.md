---
title: "doveadm-director(1)"
name: "doveadm-director"
section: "1"
letter: "d"
url: "/docs/linux/man/1-doveadm-director/"
description: "doveadm-director – Manage Dovecot directors"
---

<h2>NAME</h2>
<p> doveadm-director &#8211; Manage Dovecot directors</p>
<h2>SYNOPSIS</h2>
<p> <code>doveadm</code> [<code>-Dv</code>] <code>director add</code> [<code>-a</code> <i>director_socket_path</i>] <i>host</i> [<i>vhost_count</i>]<br />
 <code>doveadm</code> [<code>-Dv</code>] <code>director flush</code> [<code>-a</code> <i>director_socket_path</i>] <i>host</i>|<code>all</code><br />
 <code>doveadm</code> [<code>-Dv</code>] <code>director map</code> [<code>-a</code> <i>director_socket_path</i>] [<code>-f</code> <i>users_file</i>] [<i>host</i>]<br />
 <code>doveadm</code> [<code>-Dv</code>] <code>director remove</code> [<code>-a</code> <i>director_socket_path</i>] <i>host</i><br />
 <code>doveadm</code> [<code>-Dv</code>] <code>director dump</code> [<code>-a</code> <i>director_socket_path</i>]<br />
 <code>doveadm</code> [<code>-Dv</code>] <code>director status</code> [<code>-a</code> <i>director_socket_path</i>] [<i>user</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>doveadm director</code> can be used to manage and query the status of the list of backend mail servers where Dovecot proxy can redirect connections to.</p>
<h2>OPTIONS</h2>
<p> Global <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) <i>options</i>:</p>
<dl>
<dt><code>-D</code></p>
<dd> Enables verbosity and debug messages.</p>
<dt><code>-v</code></p>
<dd> Enables verbosity, including progress counter.</dl>
<p> Command specific <i>options</i>:</p>
<dl>
<dt><code>-a&nbsp;<wbr></code><i>director_socket_path</i></p>
<dd> This option is used to specify an alternative socket. The option&#8217;s argument is either an absolute path to a local UNIX domain socket, or a hostname and port (<i>hostname</i>:<i>port</i>), in order to connect a remote host via a TCP socket. </p>
<p> By default <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) will use the socket <i>/var/run/dovecot/director-admin</i>. The socket may be located in another directory, when the default <i>base_dir</i> setting was overridden in <i>/etc/dovecot/dovecot.conf</i>.</dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><i>host</i></p>
<dd> A mail server&#8217;s hostname or IP address.</p>
<dt><i>user</i></p>
<dd> Is a <i>user</i>&#8216;s login name. Depending on the configuration, a login name may be for example <code>jane</code> or <code>john [at] example.com</code>.</p>
<dt><i>vhost_count</i></p>
<dd> The number of &quot;virtual hosts&quot; to assign to this server. The higher the number is relative to other servers, the more connections it gets. The default is 100.</dl>
<h2>COMMANDS</h2>
<h3>director add</h3>
<p> <code>doveadm director add</code> [<code>-a</code> <i>director_socket_path</i>] <i>host</i> [<i>vhost_count</i>] </p>
<p> The command&#8217;s tasks are:</p>
<dl>
<dt>*</p>
<dd> assign a new mail server to the director.</p>
<dt>*</p>
<dd> increase/decrease the <i>vhost_count</i> of an already assigned server.</dl>
<h3>director flush</h3>
<p> <code>doveadm director flush</code> [<code>-a</code> <i>director_socket_path</i>] <i>host</i>|<code>all</code> </p>
<p> <code>doveadm director flush</code> drops all user associations either from the given <i>host</i> or <code>all</code> hosts. This command is intended mainly for testing purposes.</p>
<h3>director map</h3>
<p> <code>doveadm director map</code> [<code>-a</code> <i>director_socket_path</i>] [<code>-f</code> <i>users_file</i>] [<i>host</i>] </p>
<p> The command <code>doveadm director map</code> is used to list current <i>user</i>&nbsp;<wbr>&rarr;&nbsp;<wbr><i>host</i> mappings. Note that the director works using 32bit hashes which makes collisions quite likely, so this command can&#8217;t reliably list exactly which users have recently logged in. </p>
<dl>
<dt><code>-f&nbsp;<wbr></code><i>users_file</i></p>
<dd> Path to a file containing all user names (one per line). When given no <i>userdb</i> lookup will be performed. This may be a helpful alternative when for example the network connection to the LDAP or SQL server is slow.</p>
<dt><i>host</i></p>
<dd> Specify a server&#8217;s IP address or hostname, to list only mappings of the given <i>host</i>.</dl>
<h3>director remove</h3>
<p> <code>doveadm director remove</code> [<code>-a</code> <i>director_socket_path</i>] <i>host</i> </p>
<p> Use this command in order to remove the given <i>host</i> from the director.</p>
<h3>director dump</h3>
<p> <code>doveadm director dump</code> [<code>-a</code> <i>director_socket_path</i>] </p>
<p> Dump the current host configuration as doveadm commands. These commands can be easily run after a full director cluster restart to get back to the dumped state.</p>
<h3>director status</h3>
<p> <code>doveadm director status</code> [<code>-a</code> <i>director_socket_path</i>] [<i>user</i>] </p>
<p> This command is used to show the current usage of all assigned mail servers.<br />
 When a user name is given, this command shows which server the <i>user</i> is currently assigned to, where the user will be assigned after the current saved assignment gets removed and where the user would be assigned to if the whole proxy cluster was restarted fresh.</p>
<h2>FILES</h2>
<dl>
<dt><i>/etc/dovecot/dovecot.conf</i></p>
<dd> Dovecot&#8217;s main configuration file.</p>
<dt><i>/etc/dovecot/conf.d/10-director.conf</i></p>
<dd> Director specific settings.</dl>
<h2>EXAMPLE</h2>
<p> Add a director with vhost count 150 (or change existing one&#8217;s vhost count to 150): </p>
<pre>
<code>doveadm -v director add x1357.imap.ha.example.net 150</code>
2001:db8:543:6861:143::1357: OK
</pre>
<p> Remove a director: </p>
<pre>
<code>doveadm director remove x1357.imap.ha.example.net</code>
</pre>
<p> Query the status of mail hosts in a director: </p>
<pre>
<code>doveadm director status</code>
mail server ip       vhosts  users
192.168.10.1            100    125
192.168.10.2            100    144
192.168.10.3            100    115
</pre>
<p> Query the status of a user&#8217;s assignment: </p>
<pre>
<code>doveadm director status user [at] example.com</code>
Current: 192.168.10.1 (expires 2010-06-18 20:17:04)
Hashed: 192.168.10.2
Initial config: 192.168.10.3
</pre>
<p> This means that the user is currently assigned to mail server on IP 192.168.10.1. After all of user&#8217;s connections have logged out, the assignment will be removed (currently it looks like at 20:17:04, but that may be increased). After the assignment has expired, the user will next time be redirected to 192.168.10.2 (assuming no changes to director settings). If the entire Dovecot proxy cluster was restarted, so that all of the director configuration would revert back to its initial values, the user would be redirected to 192.168.10.3.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs, including <i>doveconf -n</i> output, to the Dovecot Mailing List &lt;dovecot [at] dovecot.org&gt;. Information about reporting bugs is available at: <a rel="nofollow" href="http://dovecot.org/bugreport.html">http://dovecot.org/bugreport.html</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) </p>
<h2>Index</h2>
