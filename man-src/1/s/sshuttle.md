---
title: "sshuttle(1)"
name: "sshuttle"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sshuttle/"
description: "sshuttle – sshuttle documentation"
---

<h2 class="name">NAME</h2>
<p> sshuttle &#8211; sshuttle documentation </p>
<h2>SYNOPSIS</h2>
<p> <code>sshuttle</code> [<i>options</i>] [<code>-r</code> <i>[username@]sshserver[:port]</i>] &lt;<i>subnets</i> …&gt;</p>
<h2>DESCRIPTION</h2>
<p> <code>sshuttle</code> allows you to create a VPN connection from your machine to any remote server that you can connect to via ssh, as long as that server has python 2.3 or higher. </p>
<p> To work, you must have root access on the local machine, but you can have a normal account on the server. </p>
<p> It’s valid to run <code>sshuttle</code> more than once simultaneously on a single client machine, connecting to a different server every time, so you can be on more than one VPN at once. </p>
<p> If run on a router, <code>sshuttle</code> can forward traffic for your entire subnet to the VPN.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>subnets</code></p>
<dd> A list of subnets to route over the VPN, in the form <code>a.b.c.d[/width][port[-port]]</code>. Valid examples are 1.2.3.4 (a single IP address), 1.2.3.4/32 (equivalent to 1.2.3.4), 1.2.3.0/24 (a 24-bit subnet, ie. with a 255.255.255.0 netmask), and 0/0 (‘just route everything through the VPN’). Any of the previous examples are also valid if you append a port or a port range, so 1.2.3.4:8000 will only tunnel traffic that has as the destination port 8000 of 1.2.3.4 and 1.2.3.0/24:8000-9000 will tunnel traffic going to any port between 8000 and 9000 (inclusive) for all IPs in the 1.2.3.0/24 subnet. It is also possible to use a name in which case the first IP it resolves to during startup will be routed over the VPN. Valid examples are example.com, example.com:8000 and example.com:8000-9000.</p>
<dt><code>&#8211;method [auto|nat|tproxy|pf]</code></p>
<dd> Which firewall method should sshuttle use? For auto, sshuttle attempts to guess the appropriate method depending on what it can find in PATH. The default value is auto.</p>
<dt><code>-l, &#8211;listen=[ip:]port</code></p>
<dd> Use this ip address and port number as the transparent proxy port. By default <code>sshuttle</code> finds an available port automatically and listens on IP 127.0.0.1 (localhost), so you don’t need to override it, and connections are only proxied from the local machine, not from outside machines. If you want to accept connections from other machines on your network (ie. to run <code>sshuttle</code> on a router) try enabling IP Forwarding in your kernel, then using <code>&#8211;listen 0.0.0.0:0</code>. You can use any name resolving to an IP address of the machine running <code>sshuttle</code>, e.g. <code>&#8211;listen localhost</code>. </p>
<p> For the tproxy and pf methods this can be an IPv6 address. Use this option twice if required, to provide both IPv4 and IPv6 addresses.</p>
<dt><code>-H, &#8211;auto-hosts</code></p>
<dd> Scan for remote hostnames and update the local /etc/hosts file with matching entries for as long as the VPN is open. This is nicer than changing your system’s DNS (/etc/resolv.conf) settings, for several reasons. First, hostnames are added without domain names attached, so you can <code>ssh thatserver</code> without worrying if your local domain matches the remote one. Second, if you <code>sshuttle</code> into more than one VPN at a time, it’s impossible to use more than one DNS server at once anyway, but <code>sshuttle</code> correctly merges /etc/hosts entries between all running copies. Third, if you’re only routing a few subnets over the VPN, you probably would prefer to keep using your local DNS server for everything else.</p>
<dt><code>-N, &#8211;auto-nets</code></p>
<dd> In addition to the subnets provided on the command line, ask the server which subnets it thinks we should route, and route those automatically. The suggestions are taken automatically from the server’s routing table.</p>
<dt><code>&#8211;dns</code></p>
<dd> Capture local DNS requests and forward to the remote DNS server. All queries to any of the local system’s DNS servers (/etc/resolv.conf) will be intercepted and resolved on the remote side of the tunnel instead, there using the DNS specified via the <code>&#8211;to-ns=</code> option, if specified.</p>
<dt><code>&#8211;ns-hosts=server1[,server2[,server3[&#8230;]]]</code></p>
<dd> Capture local DNS requests to the specified server(s) and forward to the remote DNS server. Contrary to the <i>&#8211;dns</i> option, this flag allows to specify the DNS server(s) the queries to which to intercept, instead of intercepting all DNS traffic on the local machine. This can be useful when only certain DNS requests should be resolved on the remote side of the tunnel, e.g. in combination with dnsmasq.</p>
<dt><code>&#8211;to-ns=server</code></p>
<dd> The DNS to forward requests to when remote DNS resolution is enabled. If not given, sshuttle will simply resolve using the system configured resolver on the remote side (via /etc/resolv.conf on the remote side).</p>
<dt><code>&#8211;python</code></p>
<dd> Specify the name/path of the remote python interpreter. The default is just <code>python</code>, which means to use the default python interpreter on the remote system’s PATH.</p>
<dt><code>-r, &#8211;remote=[username@]sshserver[:port]</code></p>
<dd> The remote hostname and optional username and ssh port number to use for connecting to the remote server. For example, example.com, <i>testuser [at] example.com</i>, <i>testuser [at] example.com</i>:2222, or example.com:2244.</p>
<dt><code>-x, &#8211;exclude=subnet</code></p>
<dd> Explicitly exclude this subnet from forwarding. The format of this option is the same as the <code>&lt;subnets&gt;</code> option. To exclude more than one subnet, specify the <code>-x</code> option more than once. You can say something like <code>0/0 -x 1.2.3.0/24</code> to forward everything except the local subnet over the VPN, for example.</p>
<dt><code>-X, &#8211;exclude-from=file</code></p>
<dd> Exclude the subnets specified in a file, one subnet per line. Useful when you have lots of subnets to exclude.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Print more information about the session. This option can be used more than once for increased verbosity. By default, <code>sshuttle</code> prints only error messages.</p>
<dt><code>-e, &#8211;ssh-cmd</code></p>
<dd> The command to use to connect to the remote server. The default is just <code>ssh</code>. Use this if your ssh client is in a non-standard location or you want to provide extra options to the ssh command, for example, <code>-e &#8216;ssh -v&#8217;</code>.</p>
<dt><code>&#8211;seed-hosts</code></p>
<dd> A comma-separated list of hostnames to use to initialize the <i>&#8211;auto-hosts</i> scan algorithm. <i>&#8211;auto-hosts</i> does things like poll local SMB servers for lists of local hostnames, but can speed things up if you use this option to give it a few names to start from. </p>
<p> If this option is used <i>without</i> <i>&#8211;auto-hosts</i>, then the listed hostnames will be scanned and added, but no further hostnames will be added.</p>
<dt><code>&#8211;no-latency-control</code></p>
<dd> Sacrifice latency to improve bandwidth benchmarks. ssh uses really big socket buffers, which can overload the connection if you start doing large file transfers, thus making all your other sessions inside the same tunnel go slowly. Normally, <code>sshuttle</code> tries to avoid this problem using a “fullness check” that allows only a certain amount of outstanding data to be buffered at a time. But on high-bandwidth links, this can leave a lot of your bandwidth underutilized. It also makes <code>sshuttle</code> seem slow in bandwidth benchmarks (benchmarks rarely test ping latency, which is what <code>sshuttle</code> is trying to control). This option disables the latency control feature, maximizing bandwidth usage. Use at your own risk.</p>
<dt><code>-D, &#8211;daemon</code></p>
<dd> Automatically fork into the background after connecting to the remote server. Implies <i>&#8211;syslog</i>.</p>
<dt><code>&#8211;syslog</code></p>
<dd> after connecting, send all log messages to the <code><a href="/docs/linux/man/3-syslog/">syslog</a>(3)</code> service instead of stderr. This is implicit if you use <i>&#8211;daemon</i>.</p>
<dt><code>&#8211;pidfile=pidfilename</code></p>
<dd> when using <i>&#8211;daemon</i>, save <code>sshuttle</code>’s pid to <i>pidfilename</i>. The default is <code>sshuttle.pid</code> in the current directory.</p>
<dt><code>&#8211;disable-ipv6</code></p>
<dd> If using tproxy or pf methods, this will disable IPv6 support.</p>
<dt><code>&#8211;firewall</code></p>
<dd> (internal use only) run the firewall manager. This is the only part of <code>sshuttle</code> that must run as root. If you start <code>sshuttle</code> as a non-root user, it will automatically run <code>sudo</code> or <code>su</code> to start the firewall manager, but the core of <code>sshuttle</code> still runs as a normal user.</p>
<dt><code>&#8211;hostwatch</code></p>
<dd> (internal use only) run the hostwatch daemon. This process runs on the server side and collects hostnames for the <i>&#8211;auto-hosts</i> option. Using this option by itself makes it a lot easier to debug and test the <i>&#8211;auto-hosts</i> feature.</p>
<dt><code>&#8211;version</code></p>
<dd> Print program version.</dl>
<h2>CONFIGURATION FILE</h2>
<p> All the options described above can optionally be specified in a configuration file. </p>
<p> To run <code>sshuttle</code> with options defined in, e.g., <i>/etc/sshuttle.conf</i> just pass the path to the file preceded by the <i>@</i> character, e.g. <code>@/etc/sshuttle.conf</code>. </p>
<p> When running <code>sshuttle</code> with options defined in a configuration file, options can still be passed via the command line in addition to what is defined in the file. If a given option is defined both in the file and in the command line, the value in the command line will take precedence. </p>
<p> Arguments read from a file must be one per line, as shown below: </p>
<pre>
value
--option1
value1
--option2
value2
</pre>
<h2>EXAMPLES</h2>
<p> Test locally by proxying all local connections, without using ssh: </p>
<pre><code>
$ sshuttle - v 0 / 0 Starting sshuttle proxy.Listening on('0.0.0.0', 12300).[local sudo] Password : firewall manager ready.c : connecting to server... s : available routes : s : 192.168.42.0 / 24 c : connected.firewall manager : starting transproxy.c : Accept : 192.168.42.106 : 50035-&gt;192.168.42.121 : 139. c : Accept : 192.168.42.121 : 47523-&gt;77.141.99.22 : 443. ... etc... ^ C
                                                                                                                                                                                                                                                                                                                                                                                          firewall manager : undoing changes.KeyboardInterrupt
                                                                                                                                                                                                                                                                                                                                                                                                             c : Keyboard interrupt : exiting.c : SW #8 : 192.168.42.121 : 47523 : deleting
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   c : SW #6 : 192.168.42.106 : 50035 : deleting
</code></pre>
<p> Test connection to a remote server, with automatic hostname and subnet guessing: </p>
<pre>
$ sshuttle -vNHr example.org
Starting sshuttle proxy.
Listening on ('0.0.0.0', 12300).
firewall manager ready.
c : connecting to server...
 s: available routes:
 s:   77.141.99.0/24
c : connected.
c : seed_hosts: []
firewall manager: starting transproxy.
hostwatch: Found: testbox1: 1.2.3.4
hostwatch: Found: mytest2: 5.6.7.8
hostwatch: Found: domaincontroller: 99.1.2.3
c : Accept: 192.168.42.121:60554 -&gt; 77.141.99.22:22.
^C
firewall manager: undoing changes.
c : Keyboard interrupt: exiting.
c : SW#6:192.168.42.121:60554: deleting
</pre>
<p> Run <code>sshuttle</code> with a <i>/etc/sshuttle.conf</i> configuration file: </p>
<pre>
$ sshuttle @/etc/sshuttle.conf
</pre>
<p> Use the options defined in <i>/etc/sshuttle.conf</i> but be more verbose: </p>
<pre>
$ sshuttle @/etc/sshuttle.conf -vvv
</pre>
<p> Override the remote server defined in <i>/etc/sshuttle.conf</i>: </p>
<pre>
$ sshuttle @/etc/sshuttle.conf -r otheruser [at] test.example.com
</pre>
<p> Example configuration file: </p>
<pre>
192.168.0.0/16
--remote
user [at] example.com
</pre>
<h2>DISCUSSION</h2>
<p> When it starts, <code>sshuttle</code> creates an ssh session to the server specified by the <code>-r</code> option. If <code>-r</code> is omitted, it will start both its client and server locally, which is sometimes useful for testing. </p>
<p> After connecting to the remote server, <code>sshuttle</code> uploads its (python) source code to the remote end and executes it there. Thus, you don’t need to install <code>sshuttle</code> on the remote server, and there are never <code>sshuttle</code> version conflicts between client and server. </p>
<p> Unlike most VPNs, <code>sshuttle</code> forwards sessions, not packets. That is, it uses kernel transparent proxying (<i>iptables REDIRECT</i> rules on Linux) to capture outgoing TCP sessions, then creates entirely separate TCP sessions out to the original destination at the other end of the tunnel. </p>
<p> Packet-level forwarding (eg. using the tun/tap devices on Linux) seems elegant at first, but it results in several problems, notably the ‘tcp over tcp’ problem. The tcp protocol depends fundamentally on packets being dropped in order to implement its congestion control agorithm; if you pass tcp packets through a tcp-based tunnel (such as ssh), the inner tcp packets will never be dropped, and so the inner tcp stream’s congestion control will be completely broken, and performance will be terrible. Thus, packet-based VPNs (such as IPsec and openvpn) cannot use tcp-based encrypted streams like ssh or ssl, and have to implement their own encryption from scratch, which is very complex and error prone. </p>
<p> <code>sshuttle</code>’s simplicity comes from the fact that it can safely use the existing ssh encrypted tunnel without incurring a performance penalty. It does this by letting the client-side kernel manage the incoming tcp stream, and the server-side kernel manage the outgoing tcp stream; there is no need for congestion control to be shared between the two separate streams, so a tcp-based tunnel is fine. </p>
<p> <code>SEE ALSO:</code> <code><a href="/docs/linux/man/1-ssh/">ssh</a>(1)</code>, <code><a href="/docs/linux/man/1-python/">python</a>(1)</code></p>
<h2>AUTHOR</h2>
<p> Brian May</p>
<h2>COPYRIGHT</h2>
<p> 2019, Brian May </p>
<h2>Index</h2>
