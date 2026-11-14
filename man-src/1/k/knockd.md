---
title: "knockd(1)"
name: "knockd"
section: "1"
letter: "k"
url: "/docs/linux/man/1-knockd/"
description: "knockd – port-knock server"
---

<h2>NAME</h2>
<p> knockd &#8211; port-knock server</p>
<h2>SYNOPSIS</h2>
<p> <code>knockd [options]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>knockd</code> is a <i>port-knock</i> server. It listens to all traffic on an ethernet (or PPP) interface, looking for special &quot;knock&quot; sequences of port-hits. A client makes these port-hits by sending a TCP (or UDP) packet to a port on the server. This port need not be open &#8212; since knockd listens at the link-layer level, it sees all traffic even if it&#8217;s destined for a closed port. When the server detects a specific sequence of port-hits, it runs a command defined in its configuration file. This can be used to open up holes in a firewall for quick access.</p>
<h2>COMMANDLINE OPTIONS</h2>
<dl>
<dt><code>-i, &#8211;interface &lt;int&gt;</code></p>
<dd> Specify an interface to listen on. The default is <i>eth0</i>.</p>
<dt><code>-d, &#8211;daemon</code></p>
<dd> Become a daemon. This is usually desired for normal server-like operation.</p>
<dt><code>-c, &#8211;config &lt;file&gt;</code></p>
<dd> Specify an alternate location for the config file. Default is <i>/etc/knockd.conf</i>.</p>
<dt><code>-D, &#8211;debug</code></p>
<dd> Ouput debugging messages.</p>
<dt><code>-l, &#8211;lookup</code></p>
<dd> Lookup DNS names for log entries. This may be a security risk! See section <code>SECURITY NOTES</code>.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Output verbose status messages.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Display the version.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Syntax help.</dl>
<h2>CONFIGURATION</h2>
<p> knockd reads all knock/event sets from a configuration file. Each knock/event begins with a title marker, in the form <code>[name]</code>, where <i>name</i> is the name of the event that will appear in the log. A special marker, <code>[options]</code>, is used to define global options.</p>
<dl>
<dt></dl>
<h2>Example #1:</h2>
<dd>
<dl>
<dt>
<dd> This example uses two knocks. The first will allow the knocker to access port 22 (SSH), and the second will close the port when the knocker is complete. As you can see, this could be useful if you run a very restrictive (DENY policy) firewall and would like to access it discreetly. </p>
<pre><code>
[options] logfile = / var / log / knockd.log[openSSH] sequence = 7000, 8000, 9000 seq_timeout = 10 tcpflags = syn command = / usr / sbin / iptables - A INPUT - s % IP % --dport 22 - j ACCEPT[closeSSH] sequence = 9000, 8000, 7000 seq_timeout = 10 tcpflags = syn command = / usr / sbin / iptables - D INPUT - s % IP % --dport 22 - j ACCEPT
</code></pre>
</dl>
<dl>
<dt></dl>
<h2>Example #2:</h2>
<dd>
<dl>
<dt>
<dd> This example uses a single knock to control access to port 22 (SSH). After receiving a successful knock, the daemon will run the <code>start_command</code>, wait for the time specified in <code>cmd_timeout</code>, then execute the <code>stop_command</code>. This is useful to automatically close the door behind a knocker. The knock sequence uses both UDP and TCP ports. </p>
<p>[options] logfile = / var / log / knockd.log[opencloseSSH] sequence = 2222 : udp, 3333 : tcp, 4444 : udp seq_timeout = 15 tcpflags = syn, ack start_command = / usr / sbin / iptables &#8211; A INPUT &#8211; s % IP % -p tcp&#8211; syn &#8211; j ACCEPT cmd_timeout = 5 stop_command = / usr / sbin / iptables &#8211; D INPUT &#8211; s % IP % -p tcp&#8211; syn &#8211; j ACCEPT
</dl>
<dl>
<dt></dl>
<h2>Example #3:</h2>
<dd>
<dl>
<dt>
<dd> This example doesn&#8217;t use a single, fixed knock sequence to trigger an event, but a set of sequences taken from a sequence file (one time sequences), specified by the <code>one_time_sequences</code> directive. After each successful knock, the used sequence will be invalidated and the next sequence from the sequence file has to be used for a successful knock. This prevents an attacker from doing a replay attack after having discovered a sequence (eg, while sniffing the network). </p>
<pre><code>
[options] logfile = / var / log / knockd.log[opencloseSMTP] one_time_sequences = / etc / knockd / smtp_sequences seq_timeout = 15 tcpflags = fin, !ack
                                                                                                                                                      start_command = / usr / sbin / iptables - A INPUT - s % IP % -p tcp-- dport 25 - j ACCEPT cmd_timeout = 5 stop_command = / usr / sbin / iptables - D INPUT - s % IP % -p tcp-- dport 25 - j ACCEPT
</code></pre>
</dl>
<h2>CONFIGURATION: GLOBAL DIRECTIVES</h2>
<dl>
<dt><code>UseSyslog</code></p>
<dd> Log action messages through syslog(). This will insert log entries into your /var/log/messages or equivalent.</p>
<dt><code>LogFile = /path/to/file</code></p>
<dd> Log actions directly to a file, usually /var/log/knockd.log.</p>
<dt><code>PidFile = /path/to/file</code></p>
<dd> Pidfile to use when in daemon mode, default: /var/run/knockd.pid.</p>
<dt><code>Interface = &lt;interface_name&gt;</code></p>
<dd> Network interface to listen on. Only its name has to be given, not the path to the device (eg, &quot;eth0&quot; and not &quot;/dev/eth0&quot;). Default: eth0.</dl>
<h2>CONFIGURATION: KNOCK/EVENT DIRECTIVES</h2>
<dl>
<dt><code>Sequence = &lt;port1&gt;[:&lt;tcp|udp&gt;],&lt;port2&gt;[:&lt;tcp|udp&gt;][,&lt;port3&gt;[:&lt;tcp|udp&gt;] &#8230;]</code></p>
<dd> Specify the sequence of ports in the special knock. If a wrong port with the same flags is received, the knock is discarded. Optionally, you can define the protocol to be used on a per-port basis (default is TCP).</p>
<dt><code>One_Time_Sequences = /path/to/one_time_sequences_file</code></p>
<dd> File containing the one time sequences to be used. Instead of using a fixed sequence, knockd will read the sequence to be used from that file. After each successful knock attempt this sequence will be disabled by writing a &#8216;#&#8217; character at the first position of the line containing the used sequence. That used sequence will then be replaced by the next valid sequence from the file. </p>
<p> Because the first character is replaced by a &#8216;#&#8217;, it is recommended that you leave a space at the beginning of each line. Otherwise the first digit in your knock sequence will be overwritten with a &#8216;#&#8217; after it has been used. </p>
<p> Each line in the one time sequences file contains exactly one sequence and has the same format as the one for the <code>Sequence</code> directive. Lines beginning with a &#8216;#&#8217; character will be ignored. </p>
<p> <code>Note</code>: Do not edit the file while knockd is running!</p>
<dt><code>Seq_Timeout = &lt;timeout&gt;</code></p>
<dd> Time to wait for a sequence to complete in seconds. If the time elapses before the knock is complete, it is discarded.</p>
<dt><code>TCPFlags = fin|syn|rst|psh|ack|urg</code></p>
<dd> Only pay attention to packets that have this flag set. When using TCP flags, knockd will IGNORE tcp packets that don&#8217;t match the flags. This is different than the normal behavior, where an incorrect packet would invalidate the entire knock, forcing the client to start over. Using &quot;TCPFlags = syn&quot; is useful if you are testing over an SSH connection, as the SSH traffic will usually interfere with (and thus invalidate) the knock. </p>
<p> Separate multiple flags with commas (eg, TCPFlags = syn,ack,urg). Flags can be explicitly excluded by a &quot;!&quot; (eg, TCPFlags = syn,!ack).</p>
<dt><code>Target = &lt;ip-address&gt;</code></p>
<dd> Use the specified IP address instead of the address determined for the <code>Interface</code> when matching the <code>Sequence</code>. This is useful if knockd is running on a router and you want to do something in response to an actual connection attempt to a routed host &#8211; e.g., invoking etherwake to send the host a WOL packet.</p>
<dt><code>Start_Command = &lt;command&gt;</code></p>
<dd> Specify the command to be executed when a client makes the correct port-knock. All instances of <code>%IP%</code> will be replaced with the knocker&#8217;s IP address. The <code>Command</code> directive is an alias for <code>Start_Command</code>.</p>
<dt><code>Cmd_Timeout = &lt;timeout&gt;</code></p>
<dd> Time to wait (in seconds) between <code>Start_Command</code> and <code>Stop_Command</code>. This directive is optional, only required if <code>Stop_Command</code> is used.</p>
<dt><code>Stop_Command = &lt;command&gt;</code></p>
<dd> Specify the command to be executed when <code>Cmd_Timeout</code> seconds have passed since <code>Start_Command</code> has been executed. All instances of <code>%IP%</code> will be replaced with the knocker&#8217;s IP address. This directive is optional.</dl>
<h2>SECURITY NOTES</h2>
<p> Using the <code>-l</code> or <code>&#8211;lookup</code> commandline option to resolve DNS names for log entries may be a security risk! An attacker may find out the first port of a sequence if he can monitor the DNS traffic of the host running knockd. Also a host supposed to be stealth (eg, dropping packets to closed TCP ports instead of replying with an ACK+RST packet) may give itself away by resolving a DNS name if an attacker manages to hit the first (unknown) port of a sequence.</p>
<h2>SEE ALSO</h2>
<p> <code>knock</code> is the accompanying port-knock client, though <code>telnet</code> or <code>netcat</code> could be used for simple TCP knocks instead. For more advanced knocks, see <code>hping</code>, <code>sendip</code> or <code>packit</code>.</p>
<h2>AUTHOR</h2>
<pre>
Judd Vinet &lt;jvinet [at] zeroflux.org&gt;
</pre>
<h2>Index</h2>
