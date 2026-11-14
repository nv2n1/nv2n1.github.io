---
title: "tincd(8)"
name: "tincd"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tincd/"
description: "tincd – tinc VPN daemon"
---

<p><code>tincd</code> &#8211; tinc VPN daemon</p>
<h2>Synopsis</h2>
<p>[-<code>cdDkKnoLRU</code> ] [-<code>-config = </code><i>DIR</i> ] [-<code>-no-detach</code> ] [-<code>-debug </code>[= <i>LEVEL</i> ] ] [-<code>-kill </code>[= <i>SIGNAL</i> ] ] [-<code>-net = </code><i>NETNAME</i> ] [-<code>-generate-keys </code>[= <i>BITS</i> ] ] [-<code>-option = </code><i>[HOST.]KEY=VALUE</i> ] [-<code>-mlock</code> ] [-<code>-logfile </code>[= <i>FILE</i> ] ] [-<code>-pidfile = </code><i>FILE</i> ] [-<code>-bypass-security</code> ] [-<code>-chroot</code> ] [-<code>-user = </code><i>USER</i> ] [-<code>-help</code> ] [-<code>-version</code> ]</p>
<h2>Description</h2>
<p>This is the daemon of tinc, a secure virtual private network (VPN) project. When started, will read it&#8217;s configuration file to determine what virtual subnets it has to serve and to what other tinc daemons it should connect. It will connect to the ethertap or tun/tap device and set up a socket for incoming connections. Optionally a script will be executed to further configure the virtual device. If that succeeds, it will detach from the controlling terminal and continue in the background, accepting and setting up connections to other tinc daemons that are part of the virtual private network. Under Windows (not Cygwin) tinc will install itself as a service, which will be restarted automatically after reboots.</p>
<h2>Options</h2>
<dl>
<dt><code>-c, -config = </code><i>DIR</i></p>
<dd>Read configuration files from <i>DIR</i> instead of /etc/tinc/</p>
<dt><code>-D, -no-detach</code></p>
<dd>Don&#8217;t fork and detach. This will also disable the automatic restart mechanism for fatal errors. If not mentioned otherwise, this will show log messages on the standard error output.</p>
<dt><code>-d, -debug </code>[= <i>LEVEL</i> ]</p>
<dd>Increase debug level or set it to <i>LEVEL</i> (see below).</p>
<dt><code>-k, -kill </code>[= <i>SIGNAL</i> ]</p>
<dd>Attempt to kill a running (optionally with the specified <i>SIGNAL</i> instead of SIGTERM) and exit. Under Windows (not Cygwin) the optional argument is ignored, the service will always be stopped and removed.</p>
<dt><code>-n, -net = </code><i>NETNAME</i></p>
<dd>Connect to net <i>NETNAME</i> This will let tinc read all configuration files from /etc/tinc/ <i>NETNAME</i> Specifying <code>.</code> for <i>NETNAME</i> is the same as not specifying any <i>NETNAME</i></p>
<dt><code>-K, -generate-keys </code>[= <i>BITS</i> ]</p>
<dd>Generate public/private RSA keypair and exit. If <i>BITS</i> is omitted, the default length will be 2048 bits. When saving keys to existing files, tinc will not delete the old keys, you have to remove them manually.</p>
<dt><code>-o, -option = </code><i>[HOST.]KEY=VALUE</i></p>
<dd>Without specifying a <i>HOST</i> this will set server configuration variable <i>KEY </i> to <i>VALUE</i> If specified as <i>HOST.KEY=VALUE</i> this will set the host configuration variable <i>KEY</i> of the host named <i>HOST</i> to <i>VALUE</i> This option can be used more than once to specify multiple configuration variables.</p>
<dt><code>-L, -mlock</code></p>
<dd>Lock tinc into main memory. This will prevent sensitive data like shared private keys to be written to the system swap files/partitions.</p>
<dt><code>&#8211;logfile </code>[= <i>FILE</i> ]</p>
<dd>Write log entries to a file instead of to the system logging facility. If <i>FILE</i> is omitted, the default is /var/log/tinc. <i>NETNAME </i><code>.log. </code></p>
<dt><code>&#8211;pidfile = </code><i>FILE</i></p>
<dd>Write PID to <i>FILE</i> instead of /var/run/tinc. <i>NETNAME </i><code>.pid. </code> Under Windows this option will be ignored.</p>
<dt><code>&#8211;bypass-security</code></p>
<dd>Disables encryption and authentication of the meta protocol. Only useful for debugging.</p>
<dt><code>-R, -chroot</code></p>
<dd>With this option tinc chroots into the directory where network config is located (/etc/tinc/NETNAME if -n option is used, or to the directory specified with -c option) after initialization.</p>
<dt><code>-U, -user = </code><i>USER</i></p>
<dd>setuid to the specified <i>USER</i> after initialization.</p>
<dt><code>&#8211;help</code></p>
<dd>Display short list of options.</p>
<dt><code>&#8211;version</code></p>
<dd>Output version information and exit.</dl>
<h2>Signals</h2>
<dl>
<dt><code>ALRM</code></p>
<dd>Forces to try to connect to all uplinks immediately. Usually attempts to do this itself, but increases the time it waits between the attempts each time it failed, and if didn&#8217;t succeed to connect to an uplink the first time after it started, it defaults to the maximum time of 15 minutes.</p>
<dt><code>HUP</code></p>
<dd>Partially rereads configuration files. Connections to hosts whose host config file are removed are closed. New outgoing connections specified in tinc.conf will be made. If the &#8211;<code>-logfile</code> option is used, this will also close and reopen the log file, useful when log rotation is used.</p>
<dt><code>INT</code></p>
<dd>Temporarily increases debug level to 5. Send this signal again to revert to the original level.</p>
<dt><code>USR1</code></p>
<dd>Dumps the connection list to syslog.</p>
<dt><code>USR2</code></p>
<dd>Dumps virtual network device statistics, all known nodes, edges and subnets to syslog.</p>
<dt><code>WINCH</code></p>
<dd>Purges all information remembered about unreachable nodes.</dl>
<h2>Debug Levels</h2>
<p>The tinc daemon can send a lot of messages to the syslog. The higher the debug level, the more messages it will log. Each level inherits all messages of the previous level:</p>
<dl>
<dt><code>0</code></p>
<dd>This will log a message indicating has started along with a version number. It will also log any serious error.</p>
<dt><code>1</code></p>
<dd>This will log all connections that are made with other tinc daemons.</p>
<dt><code>2</code></p>
<dd>This will log status and error messages from scripts and other tinc daemons.</p>
<dt><code>3</code></p>
<dd>This will log all requests that are exchanged with other tinc daemons. These include authentication, key exchange and connection list updates.</p>
<dt><code>4</code></p>
<dd>This will log a copy of everything received on the meta socket.</p>
<dt><code>5</code></p>
<dd>This will log all network traffic over the virtual private network.</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/tinc/ </code></p>
<dd>Directory containing the configuration files tinc uses. For more information, see tinc.conf5.</p>
<dt><code>/var/run/tinc. </code><i>NETNAME </i><code>.pid </code></p>
<dd>The PID of the currently running is stored in this file.</dl>
<h2>Bugs</h2>
<p>The <i>BindToInterface</i> option may not work correctly. </p>
<p> <code>The cryptography in tinc is not well tested yet. Use it at your own risk!</code> </p>
<p> If you find any bugs, report them to tinc [at] tinc-vpn.org.</p>
<h2>Todo</h2>
<p>A lot, especially security auditing.</p>
<h2>See Also</h2>
<p>tinc.conf5, <a rel="nofollow" href="https://www.tinc-vpn.org/">https://www.tinc-vpn.org/</a> <a rel="nofollow" href="http://www.cabal.org/">http://www.cabal.org/</a> </p>
<p> The full documentation for tinc is maintained as a Texinfo manual. If the info and tinc programs are properly installed at your site, the command <code>info tinc</code> should give you access to the complete manual. </p>
<p> tinc comes with ABSOLUTELY NO WARRANTY. This is free software, and you are welcome to redistribute it under certain conditions; see the file COPYING for details.</p>
<h2>Authors</h2>
<p>An Ivo Timmermans An Guus Sliepen Aq guus [at] tinc-vpn.org </p>
<p> And thanks to many others for their contributions to tinc!</p>
