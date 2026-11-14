---
title: "sshuttle(8)"
name: "sshuttle"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sshuttle/"
description: "sshuttle – a transparent proxy-based VPN using ssh"
---

<p>sshuttle &#8211; a transparent proxy-based VPN using ssh</p>
<h2>Synopsis</h2>
<p>sshuttle [options&#8230;] [-r [username@]sshserver[:port]] \&lt;subnets&#8230;&gt;</p>
<h2>Description</h2>
<p>sshuttle allows you to create a VPN connection from your machine to any remote server that you can connect to via ssh, as long as that server has python 2.3 or higher. </p>
<p> To work, you must have root access on the local machine, but you can have a normal account on the server. </p>
<p> It&#8217;s valid to run sshuttle more than once simultaneously on a single client machine, connecting to a different server every time, so you can be on more than one VPN at once. </p>
<p> If run on a router, sshuttle can forward traffic for your entire subnet to the VPN.</p>
<h2>Options</h2>
<p>\&lt;subnets&#8230;&gt; : a list of subnets to route over the VPN, in the form <code>a.b.c.d[/width]</code>. Valid examples are 1.2.3.4 (a single IP address), 1.2.3.4/32 (equivalent to 1.2.3.4), 1.2.3.0/24 (a 24-bit subnet, ie. with a 255.255.255.0 netmask), and 0/0 (&#8216;just route everything through the VPN&#8217;). </p>
<p> -l, &#8211;listen=<i>[ip:]port</i> : use this ip address and port number as the transparent proxy port. By default sshuttle finds an available port automatically and listens on IP 127.0.0.1 (localhost), so you don&#8217;t need to override it, and connections are only proxied from the local machine, not from outside machines. If you want to accept connections from other machines on your network (ie. to run sshuttle on a router) try enabling IP Forwarding in your kernel, then using <code>&#8211;listen 0.0.0.0:0</code>. </p>
<p> -H, &#8211;auto-hosts : scan for remote hostnames and update the local /etc/hosts file with matching entries for as long as the VPN is open. This is nicer than changing your system&#8217;s DNS (/etc/resolv.conf) settings, for several reasons. First, hostnames are added without domain names attached, so you can <code>ssh thatserver</code> without worrying if your local domain matches the remote one. Second, if you sshuttle into more than one VPN at a time, it&#8217;s impossible to use more than one DNS server at once anyway, but sshuttle correctly merges /etc/hosts entries between all running copies. Third, if you&#8217;re only routing a few subnets over the VPN, you probably would prefer to keep using your local DNS server for everything else. </p>
<p> -N, &#8211;auto-nets : in addition to the subnets provided on the command line, ask the server which subnets it thinks we should route, and route those automatically. The suggestions are taken automatically from the server&#8217;s routing table. </p>
<p> &#8211;dns : capture local DNS requests and forward to the remote DNS server. </p>
<p> &#8211;python : specify the name/path of the remote python interpreter. The default is just <code>python</code>, which means to use the default python interpreter on the remote system&#8217;s PATH. </p>
<p> -r, &#8211;remote=<i>[username@]sshserver[:port]</i> : the remote hostname and optional username and ssh port number to use for connecting to the remote server. For example, example.com, testuser [at] example.com, testuser [at] example.com:2222, or example.com:2244. </p>
<p> -x, &#8211;exclude=<i>subnet</i> : explicitly exclude this subnet from forwarding. The format of this option is the same as the <code>&lt;subnets&gt;</code> option. To exclude more than one subnet, specify the <code>-x</code> option more than once. You can say something like <code>0/0 -x 1.2.3.0/24</code> to forward everything except the local subnet over the VPN, for example. </p>
<p> &#8211;exclude-from=<i>file</i> : exclude the subnets specified in a file, one subnet per line. Useful when you have lots of subnets to exclude. </p>
<p> -v, &#8211;verbose : print more information about the session. This option can be used more than once for increased verbosity. By default, sshuttle prints only error messages. </p>
<p> -e, &#8211;ssh-cmd : the command to use to connect to the remote server. The default is just <code>ssh</code>. Use this if your ssh client is in a non-standard location or you want to provide extra options to the ssh command, for example, <code>-e &#8216;ssh -v&#8217;</code>. </p>
<p> &#8211;seed-hosts : a comma-separated list of hostnames to use to initialize the <code>&#8211;auto-hosts</code> scan algorithm. <code>&#8211;auto-hosts</code> does things like poll local SMB servers for lists of local hostnames, but can speed things up if you use this option to give it a few names to start from. </p>
<p> &#8211;no-latency-control : sacrifice latency to improve bandwidth benchmarks. ssh uses really big socket buffers, which can overload the connection if you start doing large file transfers, thus making all your other sessions inside the same tunnel go slowly. Normally, sshuttle tries to avoid this problem using a &quot;fullness check&quot; that allows only a certain amount of outstanding data to be buffered at a time. But on high-bandwidth links, this can leave a lot of your bandwidth underutilized. It also makes sshuttle seem slow in bandwidth benchmarks (benchmarks rarely test ping latency, which is what sshuttle is trying to control). This option disables the latency control feature, maximizing bandwidth usage. Use at your own risk. </p>
<p> -D, &#8211;daemon : automatically fork into the background after connecting to the remote server. Implies <code>&#8211;syslog</code>. </p>
<p> &#8211;syslog : after connecting, send all log messages to the <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) service instead of stderr. This is implicit if you use <code>&#8211;daemon</code>. </p>
<p> &#8211;pidfile=<i>pidfilename</i> : when using <code>&#8211;daemon</code>, save sshuttle&#8217;s pid to <i>pidfilename</i>. The default is <code>sshuttle.pid</code> in the current directory. </p>
<p> &#8211;server : (internal use only) run the sshuttle server on stdin/stdout. This is what the client runs on the remote end. </p>
<p> &#8211;firewall : (internal use only) run the firewall manager. This is the only part of sshuttle that must run as root. If you start sshuttle as a non-root user, it will automatically run <code>sudo</code> or <code>su</code> to start the firewall manager, but the core of sshuttle still runs as a normal user. </p>
<p> &#8211;hostwatch : (internal use only) run the hostwatch daemon. This process runs on the server side and collects hostnames for the <code>&#8211;auto-hosts</code> option. Using this option by itself makes it a lot easier to debug and test the <code>&#8211;auto-hosts</code> feature.</p>
<h2>Examples</h2>
<p>Test locally by proxying all local connections, without using ssh:</p>
<dl>
<dd>
<pre>$ sshuttle -v 0/0
Starting sshuttle proxy.
Listening on ('0.0.0.0', 12300).
[local sudo] Password: 
firewall manager ready.
c : connecting to server...
 s: available routes:
 s: 192.168.42.0/24
c : connected.
firewall manager: starting transproxy.
c : Accept: 192.168.42.106:50035 -&gt; 192.168.42.121:139.
c : Accept: 192.168.42.121:47523 -&gt; 77.141.99.22:443.
 ...etc...
^C
firewall manager: undoing changes.
KeyboardInterrupt
c : Keyboard interrupt: exiting.
c : SW#8:192.168.42.121:47523: deleting
c : SW#6:192.168.42.106:50035: deleting</pre>
</dl>
<p> Test connection to a remote server, with automatic hostname and subnet guessing:</p>
<dl>
<dd>
<pre>$ sshuttle -vNHr example.org
Starting sshuttle proxy.
Listening on ('0.0.0.0', 12300).
firewall manager ready.
c : connecting to server...
 s: available routes:
 s: 77.141.99.0/24
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
c : SW#6:192.168.42.121:60554: deleting</pre>
</dl>
<h2>Discussion</h2>
<p>When it starts, sshuttle creates an ssh session to the server specified by the <code>-r</code> option. If <code>-r</code> is omitted, it will start both its client and server locally, which is sometimes useful for testing. </p>
<p> After connecting to the remote server, sshuttle uploads its (python) source code to the remote end and executes it there. Thus, you don&#8217;t need to install sshuttle on the remote server, and there are never sshuttle version conflicts between client and server. </p>
<p> Unlike most VPNs, sshuttle forwards sessions, not packets. That is, it uses kernel transparent proxying (<code>iptables REDIRECT</code> rules on Linux, or <code>ipfw fwd</code> rules on BSD) to capture outgoing TCP sessions, then creates entirely separate TCP sessions out to the original destination at the other end of the tunnel. </p>
<p> Packet-level forwarding (eg. using the tun/tap devices on Linux) seems elegant at first, but it results in several problems, notably the &#8216;tcp over tcp&#8217; problem. The tcp protocol depends fundamentally on packets being dropped in order to implement its congestion control agorithm; if you pass tcp packets through a tcp-based tunnel (such as ssh), the inner tcp packets will never be dropped, and so the inner tcp stream&#8217;s congestion control will be completely broken, and performance will be terrible. Thus, packet-based VPNs (such as IPsec and openvpn) cannot use tcp-based encrypted streams like ssh or ssl, and have to implement their own encryption from scratch, which is very complex and error prone. </p>
<p> sshuttle&#8217;s simplicity comes from the fact that it can safely use the existing ssh encrypted tunnel without incurring a performance penalty. It does this by letting the client-side kernel manage the incoming tcp stream, and the server-side kernel manage the outgoing tcp stream; there is no need for congestion control to be shared between the two separate streams, so a tcp-based tunnel is fine.</p>
<h2>Bugs</h2>
<p>On MacOS 10.6 (at least up to 10.6.6), your network will stop responding about 10 minutes after the first time you start sshuttle, because of a MacOS kernel bug relating to arp and the net.inet.ip.scopedroute sysctl. To fix it, just switch your wireless off and on. Sshuttle makes the kernel setting it changes permanent, so this won&#8217;t happen again, even after a reboot.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1), <code><a href="/docs/linux/man/1-python/">python</a></code>(1)</p>
<h2>Author</h2>
<p>Avery Pennarun penwarr [at] gmail.com</p>
