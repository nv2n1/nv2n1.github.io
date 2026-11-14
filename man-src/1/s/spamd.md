---
title: "spamd(1)"
name: "spamd"
section: "1"
letter: "s"
url: "/docs/linux/man/1-spamd/"
description: "spamd – daemonized version of spamassassin"
---

<h2 class="name">NAME</h2>
<p> spamd &#8211; daemonized version of spamassassin </p>
<h2>SYNOPSIS</h2>
<p> spamd [options] </p>
<p> Options: </p>
<pre><code>
 -l, --allow-tell                  Allow learning/reporting
 -c, --create-prefs                Create user preferences files
 -C path, --configpath=path        Path for default config files
 --siteconfigpath=path             Path for site configs
 --cf='config line'                Additional line of configuration
 -d, --daemonize                   Daemonize
 -h, --help                        Print usage message
 -i [ip_or_name[:port]], --listen=[ip_or_name[:port]] Listen on IP addr and port
 -p port, --port=port              Listen on specified port, may be overridden by -i
 -4, --ipv4-only, --ipv4           Use IPv4 where applicable, disables IPv6
 -6                                Use IPv6 where applicable, disables IPv4
 -A host,..., --allowed-ips=..,..  Restrict to IP addresses which can connect
 -m num, --max-children=num        Allow maximum num children
 --min-children=num                Allow minimum num children
 --min-spare=num                   Lower limit for number of spare children
 --max-spare=num                   Upper limit for number of spare children
 --max-conn-per-child=num          Maximum connections accepted by child 
                                   before it is respawned
 --round-robin                     Use traditional prefork algorithm
 --timeout-tcp=secs                Connection timeout for client headers
 --timeout-child=secs              Connection timeout for message checks
 -q, --sql-config                  Enable SQL config (needs -x)
 -Q, --setuid-with-sql             Enable SQL config (needs -x,
                                   enables use of -H)
 --ldap-config                     Enable LDAP config (needs -x)
 --setuid-with-ldap                Enable LDAP config (needs -x,
                                   enables use of -H)
 --virtual-config-dir=dir          Enable pattern based Virtual configs
                                   (needs -x)
 -r pidfile, --pidfile             Write the process id to pidfile
 -s facility, --syslog=facility    Specify the syslog facility
 --syslog-socket=type              How to connect to syslogd
 --log-timestamp-fmt=fmt           strftime(3) format for timestamps, may be
                                   empty to disable timestamps, or 'default'
 -u username, --username=username  Run as username
 -g groupname, --groupname=groupname  Run as groupname
 -v, --vpopmail                    Enable vpopmail config
 -x, --nouser-config               Disable user config files
 --auth-ident                      Use ident to identify spamc user (deprecated)
 --ident-timeout=timeout           Timeout for ident connections
 -D, --debug[=areas]               Print debugging messages (for areas)
 -L, --local                       Use local tests only (no DNS)
 -P, --paranoid                    Die upon user errors
 -H [dir], --helper-home-dir[=dir] Specify a different HOME directory
 --ssl                             Enable SSL on TCP connections
 --ssl-port port                   Override --port setting for SSL connections
 --ssl-version sslversion          Specify SSL protocol version to use
 --server-key keyfile              Specify an SSL keyfile
 --server-cert certfile            Specify an SSL certificate
 --socketpath=path                 Listen on a given UNIX domain socket
 --socketowner=name                Set UNIX domain socket file's owner
 --socketgroup=name                Set UNIX domain socket file's group
 --socketmode=mode                 Set UNIX domain socket file's mode
 -V, --version                     Print version and exit
</code></pre>
<p> The &#8211;listen option (or -i) may be specified multiple times, its syntax is: [ ssl: ] [ host-name-or-IP-address ] [ : port ] or an absolute path (filename) of a Unix socket. If port is omitted it defaults to &#8211;port or to 783. Option &#8211;ssl implies a prefix &#8216;ssl:&#8217;. An IPv6 address should be enclosed in square brackets, e.g. [::1]:783, an IPv4 address may be but need not be enclosed in square brackets. An asterisk &#8216;*&#8217; in place of a hostname implies an unspecified address, (&#8216;0.0.0.0&#8217; or &#8216;::&#8217;), i.e. it binds to all interfaces. An empty option value implies &#8216;*&#8217;. A default is &#8216;&#8211;listen localhost&#8217;, which binds to a loopback interface only.</p>
<h2>DESCRIPTION</h2>
<p> The purpose of this program is to provide a daemonized version of the spamassassin executable. The goal is improving throughput performance for automated mail checking. </p>
<p> This is intended to be used alongside <tt>&quot;spamc&quot;</tt>, a fast, low-overhead C client program. </p>
<p> See the <font SIZE="-1">README</font> file in the <tt>&quot;spamd&quot;</tt> directory of the SpamAssassin distribution for more details. </p>
<p> Note: Although <tt>&quot;spamd&quot;</tt> will check per-user config files for every message, any changes to the system-wide config files will require either restarting spamd or forcing it to reload itself via <font SIZE="-1"><code>SIGHUP</code></font> for the changes to take effect. </p>
<p> Note: If <tt>&quot;spamd&quot;</tt> receives a <font SIZE="-1"><code>SIGHUP</code></font>, it internally reloads itself, which means that it will change its pid and might not restart at all if its environment changed (ie. if it can&#8217;t change back into its own directory). If you plan to use <font SIZE="-1"><code>SIGHUP</code></font>, you should always start <tt>&quot;spamd&quot;</tt> with the <code>-r</code> switch to know its current pid.</p>
<h2>OPTIONS</h2>
<p> Options of the long form can be shortened as long as they remain unambiguous. (i.e. <code>&#8211;dae</code> can be used instead of <code>&#8211;daemonize</code>) Also, boolean options (like <code>&#8211;user-config</code>) can be negated by adding <i>no</i> (<code>&#8211;nouser-config</code>), however, this is usually unnecessary.</p>
<dl>
<dt><code>-l</code>, <code>&#8211;allow-tell</code></p>
<dd> Allow learning and forgetting (to a local Bayes database), reporting and revoking (to a remote database) by spamd. The client issues a <font SIZE="-1">TELL</font> command to tell what type of message is being processed and whether local (learn/forget) or remote (report/revoke) databases should be updated. </p>
<p> Note that spamd always trusts the username passed in (unless <code>&#8211;auth-ident</code> is used) so clients could maliciously learn messages for other users. (This is not ususally a concern with an <font SIZE="-1">SQL</font> Bayes store as users will typically have read-write access directly to the database, and can also use <tt>&quot;sa-learn&quot;</tt> with the <code>-u</code> option to achieve the same result.)</p>
<dt><code>-c</code>, <code>&#8211;create-prefs</code></p>
<dd> Create user preferences files if they don&#8217;t exist (default: don&#8217;t).</p>
<dt><code>-C</code> <i>path</i>, <code>&#8211;configpath</code>=<i>path</i></p>
<dd> Use the specified path for locating the distributed configuration files. Ignore the default directories (usually <tt>&quot;/usr/share/spamassassin&quot;</tt> or similar).</p>
<dt><code>&#8211;siteconfigpath</code>=<i>path</i></p>
<dd> Use the specified path for locating site-specific configuration files. Ignore the default directories (usually <tt>&quot;/etc/mail/spamassassin&quot;</tt> or similar).</p>
<dt><code>&#8211;cf=&#8217;config line&#8217;</code></p>
<dd> Add additional lines of configuration directly from the command-line, parsed after the configuration files are read. Multiple <code>&#8211;cf</code> arguments can be used, and each will be considered a separate line of configuration.</p>
<dt><code>-d</code>, <code>&#8211;daemonize</code></p>
<dd> Detach from starting process and run in background (daemonize).</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print a brief help message, then exit without further action.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print version information, then exit without further action.</p>
<dt><code>-i</code> [<i>ipaddress</i>[:&lt;port&gt;]], <code>&#8211;listen</code>[=<i>ipaddress</i>[:&lt;port&gt;]]</p>
<dd> Additional alias names for this option are &#8211;listen-ip and &#8211;ip-address. Tells spamd to listen on the specified <font SIZE="-1">IP</font> address, defaults to a loopback interface, i.e. <tt>&quot;--listen localhost&quot;</tt>). If no value is specified after the switch, or if an asterisk &#8216;*&#8217; stands in place of an &lt;ipaddress&gt;, spamd will listen on all interfaces &#8211; this is equivalent to address &#8216;0.0.0.0&#8217; for IPv4 and to &#8216;::&#8217; for IPv6. You can also use a valid hostname which will make spamd listen on all addresses that a name resolves to. The option may be specified multiple times. See also options -4 and -6 for restricting address family to IPv4 or to IPv6. If a port is specified it overrides for this socket the global &#8211;port (and &#8211;ssl-port) setting. An IPv6 addresses should be enclosed in square brackets, e.g. [::1]:783. For compatibility square brackets on an IPv6 address may be omitted if a port number specification is also omitted.</p>
<dt><code>-p</code> <i>port</i>, <code>&#8211;port</code>=<i>port</i></p>
<dd> Optionally specifies the port number for the server to listen on (default: 783). </p>
<p> If the <code>&#8211;ssl</code> switch is used, and <code>&#8211;ssl-port</code> is not supplied, then this port will be used to accept <font SIZE="-1">SSL</font> connections instead of unencrypted connections. If the <code>&#8211;ssl</code> switch is used, and <code>&#8211;ssl-port</code> is set, then unencrypted connections will be accepted on the <code>&#8211;port</code> at the same time as encrypted connections are accepted at <code>&#8211;ssl-port</code>.</p>
<dt><code>-q</code>, <code>&#8211;sql-config</code></p>
<dd> Turn on <font SIZE="-1">SQL</font> lookups even when per-user config files have been disabled with <code>-x</code>. this is useful for spamd hosts which don&#8217;t have user&#8217;s home directories but do want to load user preferences from an <font SIZE="-1">SQL</font> database. </p>
<p> If your spamc client does not support sending the <tt>&quot;User:&quot;</tt> header, like <tt>&quot;exiscan&quot;</tt>, then the <font SIZE="-1">SQL</font> username used will always be <code>nobody</code>. </p>
<p> This inhibits the <i>setuid()</i> behavior, so the <tt>&quot;-u&quot;</tt> option is required. If you want the <i>setuid()</i> behaviour, use <tt>&quot;-Q&quot;</tt> or <tt>&quot;--setuid-with-sql&quot;</tt> instead.</p>
<dt><code>&#8211;ldap-config</code></p>
<dd> Turn on <font SIZE="-1">LDAP</font> lookups. This is completely analog to <tt>&quot;--sql-config&quot;</tt>, only it is using an <font SIZE="-1">LDAP</font> server. </p>
<p> Like <tt>&quot;--sql-config&quot;</tt>, this disables the setuid behavior, and requires <tt>&quot;-u&quot;</tt>. If you want it, use <tt>&quot;--setuid-with-ldap&quot;</tt> instead.</p>
<dt><code>-Q</code>, <code>&#8211;setuid-with-sql</code></p>
<dd> Turn on <font SIZE="-1">SQL</font> lookups even when per-user config files have been disabled with <code>-x</code> and also setuid to the user. This is useful for spamd hosts which want to load user preferences from an <font SIZE="-1">SQL</font> database but also wish to support the use of <code>-H</code> (Helper home directories.)</p>
<dt><code>&#8211;setuid-with-ldap</code></p>
<dd> Turn on <font SIZE="-1">LDAP</font> lookups even when per-user config files have been disabled with <code>-x</code> and also setuid to the user. This is again completely analog to <tt>&quot;--setuid-with-sql&quot;</tt>, only it is using an <font SIZE="-1">LDAP</font> server.</p>
<dt><code>&#8211;virtual-config-dir</code>=<i>pattern</i></p>
<dd> This option specifies where per-user preferences can be found for virtual users, for the <code>-x</code> switch. The <i>pattern</i> is used as a base pattern for the directory name. Any of the following escapes can be used:</p>
<dl>
<dt>
<dd>
<dl>
<dt>%u &#8212; replaced with the full name of the current user, as sent by spamc.</p>
<dd>
<dt>%l &#8212; replaced with the &#8216;local part&#8217; of the current username. In other words, if the username is an email address, this is the part before the &quot;@&quot; sign.</p>
<dd>
<dt>%d &#8212; replaced with the &#8216;domain&#8217; of the current username. In other words, if the username is an email address, this is the part after the &quot;@&quot; sign.</p>
<dd>
<dt>%% &#8212; replaced with a single percent sign (%).</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd>
<p> So for example, if <tt>&quot;/vhome/users/%u/spamassassin&quot;</tt> is specified, and spamc sends a virtual username of <tt>&quot;jm [at] example.com&quot;</tt>, the directory <tt>&quot;/vhome/users/jm [at] example.com/spamassassin&quot;</tt> will be used. </p>
<p> The set of characters allowed in the virtual username for this path are restricted to: </p>
<pre>
        A-Z a-z 0-9 - + _ . , @ =
</pre>
<p> All others will be replaced by underscores (<tt>&quot;_&quot;</tt>). </p>
<p> This path must be a writable directory. It will be created if it does not already exist. If a file called <code>user_prefs</code> exists in this directory (note: <code>not</code> in a <tt>&quot;.spamassassin&quot;</tt> subdirectory!), it will be loaded as the user&#8217;s preferences. The Bayes databases for that user will be stored in this directory. </p>
<p> Note that this <code>requires</code> that <code>-x</code> is used, and cannot be combined with <font SIZE="-1">SQL-</font> or LDAP-based configuration. </p>
<p> The pattern <code>must</code> expand to an absolute directory when spamd is running daemonized (<code>-d</code>). </p>
<p> Currently, use of this without <code>-u</code> is not supported. This inhibits setuid.</dl>
<dt><code>-r</code> <i>pidfile</i>, <code>&#8211;pidfile</code>=<i>pidfile</i></p>
<dd> Write the process <font SIZE="-1">ID</font> of the spamd parent to the file specified by <i>pidfile</i>. The file will be unlinked when the parent exits. Note that when running with the <code>-u</code> option, the file must be writable by that user.</p>
<dt><code>-v</code>, <code>&#8211;vpopmail</code></p>
<dd> Enable vpopmail config. If specified with with <code>-u</code> set to the vpopmail user, this allows spamd to lookup/create user_prefs in the vpopmail user&#8217;s own maildir. This option is useful for vpopmail virtual users who do not have an entry in the system /etc/passwd file. </p>
<p> Currently, use of this without <code>-u</code> is not supported. This inhibits setuid.</p>
<dt><code>-s</code> <i>facility</i>, <code>&#8211;syslog</code>=<i>facility</i></p>
<dd> Specify the syslog facility to use (default: mail). If <tt>&quot;stderr&quot;</tt> is specified, output will be written to stderr. (This is useful if you&#8217;re running <tt>&quot;spamd&quot;</tt> under the <tt>&quot;daemontools&quot;</tt> package.) With a <i>facility</i> of <tt>&quot;file&quot;</tt>, all output goes to spamd.log. <i>facility</i> is interpreted as a file name to log to if it contains any characters except a-z and 0-9. <tt>&quot;null&quot;</tt> disables logging completely (used internally). </p>
<p> Examples: <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>spamd -s mail # use syslog, facility mail (default)<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>spamd -s ./mail # log to file ./mail<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>spamd -s stderr 2&gt;/dev/null # log to stderr, throw messages away<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>spamd -s null # the same as above<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>spamd -s file # log to file ./spamd.log<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>spamd -s /var/log/spamd.log # log to file /var/log/spamd.log</p>
<p> If logging to a file is enabled and that log file is rotated, the spamd server must be restarted with a <font SIZE="-1">SIGHUP. </font>(If the log file is just truncated, this is not needed but still recommended.) </p>
<p> Note that logging to a file does not use locking, so you cannot intermix logging from spamd and other processes into the same file. If you want to mix logging like this, use syslog instead. </p>
<p> If you use syslog logging, it is essential to send a <font SIZE="-1">SIGHUP</font> to the spamd daemon when you restart the syslogd daemon. (This is due to a shortcoming in Perl&#8217;s syslog handling, where the disappearance of the connection to the syslogd is considered a fatal error.)</p>
<dt><code>&#8211;syslog-socket</code>=<i>type</i></p>
<dd> Specify how spamd should send messages to syslogd. The <i>type</i> can be any of the socket types or logging mechanisms as accepted by the subroutine <i>Sys::Syslog::setlogsock()</i>. Depending on a version of Sys::Syslog and on the underlying operating system, one of the following values (or their subset) can be used: <tt>&quot;native&quot;</tt>, <tt>&quot;eventlog&quot;</tt>, <tt>&quot;tcp&quot;</tt>, <tt>&quot;udp&quot;</tt>, <tt>&quot;inet&quot;</tt>, <tt>&quot;unix&quot;</tt>, <tt>&quot;stream&quot;</tt>, <tt>&quot;pipe&quot;</tt>, or <tt>&quot;console&quot;</tt>. The value <tt>&quot;eventlog&quot;</tt> is specific to Win32 events logger and requires a perl module Win32::EventLog to be installed. For more information please consult the Sys::Syslog documentation. </p>
<p> A historical setting &#8211;syslog-socket=none is mapped to &#8211;syslog=stderr. </p>
<p> A default for Windows platforms is <tt>&quot;none&quot;</tt>, otherwise the default is to try <tt>&quot;unix&quot;</tt> first, falling back to <tt>&quot;inet&quot;</tt> if perl detects errors in its <tt>&quot;unix&quot;</tt> support. </p>
<p> Some platforms, or versions of perl, are shipped with old or dysfunctional versions of the <code>Sys::Syslog</code> module which do not support some socket types, so you may need to set this option explicitly. If you get error messages regarding <code>__PATH_LOG</code> or similar spamd, try changing this setting. </p>
<p> The socket types <tt>&quot;file&quot;</tt> is used internally and should not be specified. Use the <tt>&quot;-s&quot;</tt> switch instead.</p>
<dt><code>&#8211;log-timestamp-fmt</code>=<i>format</i></p>
<dd> The &#8211;log-timestamp-fmt option can provide a <font SIZE="-1">POSIX</font> <i><a href="/docs/linux/man/3-strftime/">strftime</a></i>(3) format for timestamps included in each logged message. Each logger (stderr, file, syslog) has its own default value for a timestamp format, which applies when &#8211;log-timestamp-fmt option is not given, or with &#8211;log-timestamp-fmt=default . Timestamps can be turned off by specifying an empty string with this option, e.g. &#8211;log-timestamp-fmt=&#8221; or just &#8211;log-timestamp-fmt= . Typical use: &#8211;log-timestamp-fmt=&#8217;%a <tt>%b</tt> <tt>%e</tt> <tt>%H:</tt>%M:%S <tt>%Y</tt>&#8216; (provides localized weekday and month names in the <i><a href="/docs/linux/man/3-ctime/">ctime</a></i>(3) style), or &#8216;%a, <tt>%e</tt> <tt>%b</tt> <tt>%Y</tt> <tt>%H:</tt>%M:%S <tt>%z</tt> (%Z)&#8217; for a <font SIZE="-1">RFC 2822</font> format, or maybe &#8216;%Y-%m-%d <tt>%H:</tt>%M:%S%z&#8217; for an <font SIZE="-1">ISO 8601 </font>(<font SIZE="-1">EN 28601</font>) format, or just &#8216;%Y%m%dT%H%M%S&#8217; .</p>
<dt><code>-u</code> <i>username</i>, <code>&#8211;username</code>=<i>username</i></p>
<dd> Run as the named user. If this option is not set, the default behaviour is to <i>setuid()</i> to the user running <tt>&quot;spamc&quot;</tt>, if <tt>&quot;spamd&quot;</tt> is running as root. </p>
<p> Note: &#8220;&#8211;username=root&#8221; is not a valid option. If specified, <tt>&quot;spamd&quot;</tt> will exit with a fatal error on startup.</p>
<dt><code>-g</code> <i>groupname</i>, <code>&#8211;groupname</code>=<i>groupname</i></p>
<dd> Run as the named group if &#8211;username is being used. If this option is not set when &#8211;username is used then the primary group for the user given to &#8211;username is used.</p>
<dt><code>-x</code>, <code>&#8211;nouser-config</code>, <code>&#8211;user-config</code></p>
<dd> Turn off (on) reading of per-user configuration files (user_prefs) from the user&#8217;s home directory. The default behaviour is to read per-user configuration from the user&#8217;s home directory (<code>&#8211;user-config</code>). </p>
<p> This option does not disable or otherwise influence the <font SIZE="-1">SQL, LDAP</font> or Virtual Config Dir settings.</p>
<dt><code>&#8211;auth-ident</code></p>
<dd> Verify the username provided by spamc using ident. This is only useful if connections are only allowed from trusted hosts (because an identd that lies is trivial to create) and if spamc <font SIZE="-1">REALLY SHOULD</font> be running as the user it represents. Connections are terminated immediately if authentication fails. In this case, spamc will pass the mail through unchecked. Failure to connect to an ident server, and response timeouts are considered authentication failures. This requires that Net::Ident be installed. Deprecated.</p>
<dt><code>&#8211;ident-timeout</code>=<i>timeout</i></p>
<dd> Wait at most <i>timeout</i> seconds for a response to ident queries. Ident query that takes longer that <i>timeout</i> seconds will fail, and mail will not be processed. Setting this to 0.0 or less results in no timeout, which is <font SIZE="-1">STRONGLY</font> discouraged. The default is 5 seconds.</p>
<dt><code>-A</code> <i>host,&#8230;</i>, <code>&#8211;allowed-ips</code>=<i>host,&#8230;</i></p>
<dd> Specify a comma-separated list of authorized hosts or networks which can connect to this spamd instance. Each element of the list is either a single <font SIZE="-1">IP</font> addresses, or a range of <font SIZE="-1">IP</font> addresses in address/masklength <font SIZE="-1">CIDR</font> notation, or ranges of IPv4 addresses by specifying 3 or less octets with a trailing dot. Hostnames are not supported, only IPv4 or IPv6 addresses. This option can be specified multiple times, or can take a list of addresses separated by commas. IPv6 addresses may be (but need not be) enclosed in square brackets for consistency with option <code>&#8211;listen</code>. Examples: </p>
<p> <code>-A 10.11.12.13</code> &#8212; only allow connections from <tt>10.11.12.13</tt>. </p>
<p> <code>-A 10.11.12.13,10.11.12.14</code> &#8212; only allow connections from <tt>10.11.12.13</tt> and <tt>10.11.12.14</tt>. </p>
<p> <code>-A 10.200.300.0/24</code> &#8212; allow connections from any machine in the range <tt>&quot;10.200.300.*&quot;</tt>. </p>
<p> <code>-A 10.</code> &#8212; allow connections from any machine in the range <tt>&quot;10.*.*.*&quot;</tt>. </p>
<p> <code>-A [2001:db8::]/32,192.0.2.0/24,::1,127.0.0.0/8</code> &#8212; only accept connections from specified test networks and from localhost. </p>
<p> In absence of the <code>-A</code> option, connections are only accepted from <font SIZE="-1">IP</font> address 127.0.0.1 or ::1, i.e. from localhost on a loopback interface.</p>
<dt><code>-D</code> [<i>area,&#8230;</i>], <code>&#8211;debug</code> [<i>area,&#8230;</i>]</p>
<dd> Produce debugging output. If no areas are listed, all debugging information is printed. Diagnostic output can also be enabled for each area individually; <i>area</i> is the area of the code to instrument. For example, to produce diagnostic output on bayes, learn, and dns, use: </p>
<pre>
        spamassassin -D bayes,learn,dns
</pre>
<p> Higher priority informational messages that are suitable for logging in normal circumstances are available with an area of &#8220;info&#8221;. </p>
<p> For more information about which areas (also known as channels) are available, please see the documentation at: </p>
<pre>
        C&lt;<a rel="nofollow" href="http://wiki.apache.org/spamassassin/DebugChannels">http://wiki.apache.org/spamassassin/DebugChannels</a>&gt;
</pre>
<dt><code>-4</code>, <code>&#8211;ipv4only</code>, <code>&#8211;ipv4-only</code>, <code>&#8211;ipv4</code></p>
<dd> Use IPv4 where applicable, do not use IPv6. The option affects a set of listen sockets (see option <tt>&quot;--listen&quot;</tt>) and disables IPv6 for <font SIZE="-1">DNS</font> tests.</p>
<dt><code>-6</code></p>
<dd> Use IPv6 where applicable, do not use IPv4. The option affects a set of listen sockets (see option <tt>&quot;--listen&quot;</tt>) and disables IPv4 for <font SIZE="-1">DNS</font> tests. Installing a module IO::Socket::IP is recommended if spamd is expected to receive requests over IPv6.</p>
<dt><code>-L</code>, <code>&#8211;local</code></p>
<dd> Perform only local tests on all mail. In other words, skip <font SIZE="-1">DNS</font> and other network tests. Works the same as the <tt>&quot;-L&quot;</tt> flag to <tt><a href="/docs/linux/man/1-spamassassin/">spamassassin</a>(1)</tt>.</p>
<dt><code>-P</code>, <code>&#8211;paranoid</code></p>
<dd> Die on user errors (for the user passed from spamc) instead of falling back to user <i>nobody</i> and using the default configuration.</p>
<dt><code>-m</code> <i>number</i> , <code>&#8211;max-children</code>=<i>number</i></p>
<dd> This option specifies the maximum number of children to spawn. Spamd will spawn that number of children, then sleep in the background until a child dies, wherein it will go and spawn a new child. </p>
<p> Incoming connections can still occur if all of the children are busy, however those connections will be queued waiting for a free child. The minimum value is <tt>1</tt>, the default value is <tt>5</tt>. </p>
<p> Please note that there is a <font SIZE="-1">OS</font> specific maximum of connections that can be queued (Try <tt>&quot;perl -MSocket -e'print SOMAXCONN'&quot;</tt> to find this maximum). </p>
<p> Note that if you run too many servers for the amount of free <font SIZE="-1">RAM</font> available, you run the danger of hurting performance by causing a high swap load as server processes are swapped in and out continually.</p>
<dt><code>&#8211;min-children</code>=<i>number</i></p>
<dd> The minimum number of children that will be kept running. The minimum value is <tt>1</tt>, the default value is <tt>1</tt>. If you have lots of free <font SIZE="-1">RAM,</font> you may want to increase this.</p>
<dt><code>&#8211;min-spare</code>=<i>number</i></p>
<dd> The lower limit for the number of spare children allowed to run. A spare, or idle, child is one that is not handling a scan request. If there are too few spare children available, a new server will be started every second or so. The default value is <tt>1</tt>.</p>
<dt><code>&#8211;max-spare</code>=<i>number</i></p>
<dd> The upper limit for the number of spare children allowed to run. If there are too many spare children, one will be killed every second or so until the number of idle children is in the desired range. The default value is <tt>2</tt>.</p>
<dt><code>&#8211;max-conn-per-child</code>=<i>number</i></p>
<dd> This option specifies the maximum number of connections each child should process before dying and letting the master spamd process spawn a new child. The minimum value is <tt>1</tt>, the default value is <tt>200</tt>.</p>
<dt><code>&#8211;round-robin</code></p>
<dd> By default, <tt>&quot;spamd&quot;</tt> will attempt to keep a small number of &#8220;hot&#8221; child processes as busy as possible, and keep any others as idle as possible, using something similar to the Apache httpd server scaling algorithm. This is accomplished by the master process coordinating the activities of the children. This switch will disable this scaling algorithm, and the behaviour seen in the 3.0.x versions will be used instead, where all processes receive an equal load and no scaling takes place.</p>
<dt><code>&#8211;timeout-tcp</code>=<i>number</i></p>
<dd> This option specifies the number of seconds to wait for headers from a client (spamc) before closing the connection. The minimum value is <tt>1</tt>, the default value is <tt>30</tt>, and a value of <tt>0</tt> will disable socket timeouts completely.</p>
<dt><code>&#8211;timeout-child</code>=<i>number</i></p>
<dd> This option specifies the number of seconds to wait for a spamd child to process or check a message. The minimum value is <tt>1</tt>, the default value is <tt>300</tt>, and a value of <tt>0</tt> will disable child timeouts completely.</p>
<dt><code>-H</code> <i>directory</i>, <code>&#8211;helper-home-dir</code>=<i>directory</i></p>
<dd> Specify that external programs such as Razor, <font SIZE="-1">DCC,</font> and Pyzor should have a <font SIZE="-1">HOME</font> environment variable set to a specific directory. The default is to use the <font SIZE="-1">HOME</font> environment variable setting from the shell running spamd. By specifying no argument, spamd will use the spamc caller&#8217;s home directory instead.</p>
<dt><code>&#8211;ssl</code></p>
<dd> Accept only <font SIZE="-1">SSL</font> connections on the associated port. The <code>IO::Socket::SSL</code> perl module must be installed. </p>
<p> If the <code>&#8211;ssl</code> switch is used, and <code>&#8211;ssl-port</code> is not supplied, then <code>&#8211;port</code> port will be used to accept <font SIZE="-1">SSL</font> connections instead of unencrypted connections. If the <code>&#8211;ssl</code> switch is used, and <code>&#8211;ssl-port</code> is set, then unencrypted connections will be accepted on the <code>&#8211;port</code>, at the same time as encrypted connections are accepted at <code>&#8211;ssl-port</code>.</p>
<dt><code>&#8211;ssl-port</code>=<i>port</i></p>
<dd> Optionally specifies the port number for the server to listen on for <font SIZE="-1">SSL</font> connections (default: whatever &#8211;port uses). See <code>&#8211;ssl</code> for more details.</p>
<dt><code>&#8211;ssl-version</code>=<i>sslversion</i></p>
<dd> Specify the <font SIZE="-1">SSL</font> protocol version to use, one of <code>sslv3</code> or <code>tlsv1</code>. The default, <code>sslv3</code>, is the most flexible, accepting a SSLv3 or higher hello handshake, then negotiating use of SSLv3 or TLSv1 protocol if the client can accept it. Specifying <code>&#8211;ssl-version</code> implies <code>&#8211;ssl</code>.</p>
<dt><code>&#8211;server-key</code> <i>keyfile</i></p>
<dd> Specify the <font SIZE="-1">SSL</font> key file to use for <font SIZE="-1">SSL</font> connections.</p>
<dt><code>&#8211;server-cert</code> <i>certfile</i></p>
<dd> Specify the <font SIZE="-1">SSL</font> certificate file to use for <font SIZE="-1">SSL</font> connections.</p>
<dt><code>&#8211;socketpath</code> <i>pathname</i></p>
<dd> Listen on a <font SIZE="-1">UNIX</font> domain socket at path <i>pathname</i>, in addition to sockets specified with a <tt>&quot;--listen&quot;</tt> option. This option is provided for compatibility with older versions of spamd. Starting with version 3.4.0 the <tt>&quot;--listen&quot;</tt> option can also take a <font SIZE="-1">UNIX</font> domain socket as its value (an absolute path name). Unlike <tt>&quot;--socketpath&quot;</tt>, the <tt>&quot;--listen&quot;</tt> option may be specified multiple times if spamd needs to listen on multiple <font SIZE="-1">UNIX</font> or <font SIZE="-1">INET</font> or <font SIZE="-1">INET6</font> sockets. </p>
<p> Warning: the Perl support on <font SIZE="-1">BSD</font> platforms for <font SIZE="-1">UNIX</font> domain sockets seems to have a bug regarding paths of over 100 bytes or so (SpamAssassin bug 4380). If you see a &#8216;could not find newly-created <font SIZE="-1">UNIX</font> socket&#8217; error message, and the path appears truncated, this may be the cause. Try using a shorter path to the socket. </p>
<p> By default, use of <code>&#8211;socketpath</code> without <code>&#8211;listen</code> will inhibit <font SIZE="-1">SSL</font> connections and unencrypted <font SIZE="-1">TCP</font> connections. To add other sockets, specify them with <code>&#8211;listen</code>, e.g. &#8216;&#8211;listen=:&#8217; or &#8216;&#8211;listen=*:&#8217;</p>
<dt><code>&#8211;socketowner</code> <i>name</i></p>
<dd> Set <font SIZE="-1">UNIX</font> domain socket to be owned by the user named <i>name</i>. Note that this requires that spamd be started as <tt>&quot;root&quot;</tt>, and if <tt>&quot;-u&quot;</tt> is used, that user should have write permissions to unlink the file later, for when the <tt>&quot;spamd&quot;</tt> server is killed.</p>
<dt><code>&#8211;socketgroup</code> <i>name</i></p>
<dd> Set <font SIZE="-1">UNIX</font> domain socket to be owned by the group named <i>name</i>. See <tt>&quot;--socketowner&quot;</tt> for notes on ownership and permissions.</p>
<dt><code>&#8211;socketmode</code> <i>mode</i></p>
<dd> Set <font SIZE="-1">UNIX</font> domain socket to use the octal mode <i>mode</i>. Note that if <tt>&quot;-u&quot;</tt> is used, that user should have write permissions to unlink the file later, for when the <tt>&quot;spamd&quot;</tt> server is killed.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-spamc/">spamc</a></i>(1) <i><a href="/docs/linux/man/1-spamassassin/">spamassassin</a></i>(1) <i><a href="/docs/linux/man/3-mail--spamassassin--conf/">Mail::SpamAssassin::Conf</a></i>(3) <i><a href="/docs/linux/man/3-mail--spamassassin/">Mail::SpamAssassin</a></i>(3)</p>
<h2>PREREQUISITES</h2>
<p> <tt>&quot;Mail::SpamAssassin&quot;</tt></p>
<h2>AUTHORS</h2>
<p> The SpamAssassin(tm) Project (<a rel="nofollow" href="http://spamassassin.apache.org/)">http://spamassassin.apache.org/)</a></p>
<h2>LICENSE</h2>
<p> SpamAssassin is distributed under the Apache License, Version 2.0, as described in the file <tt>&quot;LICENSE&quot;</tt> included with the distribution. </p>
<h2>Index</h2>
