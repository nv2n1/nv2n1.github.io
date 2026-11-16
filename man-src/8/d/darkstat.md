---
title: "darkstat(8)"
name: "darkstat"
section: "8"
letter: "d"
url: "/docs/linux/man/8-darkstat/"
description: "darkstat – network statistics gatherer"
---

<p>darkstat &#8211; network statistics gatherer</p>
<h2>Synopsis</h2>
<p><code>darkstat</code> [ <code>-i</code><i> interface</i> ] [ <code>-r</code><i> file</i> ] [ <code>&#8211;snaplen</code><i> bytes</i> ] [ <code>&#8211;pppoe</code> ] [ <code>&#8211;syslog</code> ] [ <code>&#8211;verbose</code> ] [ <code>&#8211;no-daemon</code> ] [ <code>&#8211;no-promisc</code> ] [ <code>&#8211;no-dns</code> ] [ <code>&#8211;no-macs</code> ] [ <code>&#8211;no-lastseen</code> ] [ <code>-p</code><i> port</i> ] [ <code>-b</code><i> bindaddr</i> ] [ <code>&#8211;base</code><i> path</i> ] [ <code>-f</code><i> filter</i> ] [ <code>-l</code><i> network/netmask</i> ] [ <code>&#8211;local-only</code> ] [ <code>&#8211;chroot</code><i> dir</i> ] [ <code>&#8211;user</code><i> username</i> ] [ <code>&#8211;daylog</code><i> filename</i> ] [ <code>&#8211;import</code><i> filename</i> ] [ <code>&#8211;export</code><i> filename</i> ] [ <code>&#8211;pidfile</code><i> filename</i> ] [ <code>&#8211;hosts-max</code><i> count</i> ] [ <code>&#8211;hosts-keep</code><i> count</i> ] [ <code>&#8211;ports-max</code><i> count</i> ] [ <code>&#8211;ports-keep</code><i> count</i> ] [ <code>&#8211;highest-port</code><i> port</i> ] [ <code>&#8211;wait</code><i> secs</i> ] [ <code>&#8211;hexdump</code> ]</p>
<h2>Description</h2>
<p><i>darkstat</i> is a packet sniffer that runs as a background process, gathers all sorts of statistics about network usage, and serves them over HTTP. </p>
<p> All settings are passed on the commandline.</p>
<h2>Options</h2>
<dl>
<dt><code>-i</code><i> interface</i></dt>
<dd>Capture traffic on the specified network interface. This is the only mandatory commandline argument.</dd>
<dt><code>-r</code><i> file</i></dt>
<dd>Instead of capturing live traffic, read it from a <code>pcap</code>(3) capture file. This is only useful for development and benchmarking. The <code>-r</code> and <code>-i</code> arguments are mutually exclusive.</dd>
<dt><code>&#8211;snaplen</code><i> bytes</i></dt>
<dd>How many bytes to capture from the start of each packet. You should not need to specify this; <i>darkstat</i> will calculate it automatically.</dd>
<dt><code>&#8211;pppoe</code></dt>
<dd>Don&#8217;t use this. </dd>
<p> Instead, capture on the tunnel interface that your PPPoE software provides, for example <code>tun0</code> on <i>FreeBSD</i>, <code>pppoe0</code> on <i>OpenBSD</i> or <i>NetBSD</i>. </p>
<p> If you really must, you can capture on an Ethernet interface and pass this argument to have <i>darkstat</i> decode PPPoE frames and ignore everything else. Make sure you also specify your local address with the <code>-l</code> argument!</p>
<dt><code>&#8211;syslog</code></dt>
<dd>Errors, warnings, and verbose messages will go to <code>syslog</code> (facility daemon, priority debug) instead of <code>stderr</code>. </dd>
<p> On some systems, these messages end up in <code>/var/log/debug</code> by default.</p>
<dt><code>&#8211;verbose</code></dt>
<dd>Produce more verbose debugging messages.</dd>
<dt><code>&#8211;no-daemon</code></dt>
<dd>Do not detach from the controlling terminal; stay in the foreground.</dd>
<dt><code>&#8211;no-promisc</code></dt>
<dd>Do not use promiscuous mode to capture. Note that an interface may already be in promiscuous mode, or may later enter promiscuous mode, due to circumstances beyond <i>darkstat</i>&#8216;s control. If this is a problem, use <code>-f</code> to specify an appropriate <code>bpf</code>(4) filter.</dd>
<dt><code>&#8211;no-dns</code></dt>
<dd>Do not resolve IPs to host names. This can significantly reduce memory footprint on small systems as an extra process is created for DNS resolution.</dd>
<dt><code>&#8211;no-macs</code></dt>
<dd>Do not display MAC addresses in the hosts table.</dd>
<dt><code>&#8211;no-lastseen</code></dt>
<dd>Do not display the last seen time in the hosts table.</dd>
<dt><code>-p</code><i> port</i></dt>
<dd>Bind the web interface to the specified port. The default is 667.</dd>
<dt><code>-b</code><i> bindaddr</i></dt>
<dd>Bind the web interface to the specified address. The default is to listen on all interfaces.</dd>
<dt><code>&#8211;base</code><i> path</i></dt>
<dd>
</dd><dl>
<dd>Specify the path of the base URL. This can be useful if <i>darkstat</i> is accessed via a reverse proxy. </dd>
<p> For example, if you use Apache&#8217;s <i>mod_proxy</i> and want to avoid a complicated setup with <i>mod_proxy_html</i> (and <i>mod_header</i> to unset the <i>Accept-Encoding</i> header), just set the base path to something like <i>stats</i> and use a config similar to the following snippet: </p>
<dl>
<dd>&nbsp;<wbr>ProxyPass&nbsp;<wbr>/stats/&nbsp;<wbr><a rel="nofollow" href="http://localhost:667/stats/">http://localhost:667/stats/</a><br />
&nbsp;<wbr>ProxyPassReverse&nbsp;<wbr>/stats/&nbsp;<wbr><a rel="nofollow" href="http://localhost:667/stats/">http://localhost:667/stats/</a></dd></dl>
<p> The default is <i>/</i> (i.e. the root).</dl>
<dt><code>-f</code><i> filter</i></dt>
<dd>Use the specified filter expression when capturing traffic. The filter syntax is beyond the scope of this manual page; please refer to the <code>tcpdump</code>(1) documentation.</dd>
<dt><code>-l</code><i> network/netmask</i></dt>
<dd>Define a &quot;local network&quot; according to the network and netmask addresses. All traffic entering or leaving this network will be graphed, as opposed to the default behaviour of only graphing traffic to and from the local host.</dd>
<dl>
<dd>The rule is that if <code>ip_addr &amp; netmask == network</code>, then that address is considered local. See the usage example below.</dd></dl>
<dt><code>&#8211;local-only</code></dt>
<dd>Make the web interface only display hosts on the &quot;local network.&quot; This is intended to be used together with the <code>-l</code> argument.</dd>
<dt><code>&#8211;chroot</code><i> dir</i></dt>
<dd>Force <i>darkstat</i> to <code>chroot()</code> into the specified directory. Without this argument, a default directory will be used, which is determined at build time. Usually <i>/var/empty</i> or <i>/var/lib/empty</i>.</dd>
<dl>
<dd>For security reasons, this directory should be empty, and the user that <i>darkstat</i> is running as should not have write access to it. </dd>
<p> However, if you wish to use <code>&#8211;daylog</code> or <code>&#8211;export</code>, <i>darkstat</i> will need write access to the chroot. If you are uncomfortable with the security implications, don&#8217;t use any functionality that requires write access.</dl>
<dt><code>&#8211;user</code><i> username</i></dt>
<dd>Force <i>darkstat</i> to drop privileges to the <code>uid</code> and <code>gid</code> of the specified user. Without this argument, a default value will be used, which is set at build time. Usually <code>nobody</code>.</dd>
<dl>
<dd>For security reasons, this should not be <code>root</code>.</dd></dl>
<dt><code>&#8211;daylog</code><i> filename</i></dt>
<dd>
</dd><dl>
<dd>Log daily traffic statistics into the named file, relative to the chroot directory. If you wish to use <code>&#8211;daylog</code>, you must first specify a <code>&#8211;chroot</code> directory, and it must be writeable by the <i>darkstat</i> user. A writeable chroot has security implications; if you are uncomfortable with this, do not use the <code>&#8211;daylog</code> functionality. </dd>
<p> If the daylog argument is not specified, no logging is performed. </p>
<p> The daylog format is: </p>
<p> localtime|time_t|bytes_in|bytes_out|pkts_in|pkts_outs </p>
<p> Lines starting with a # are comments stating when logging started and stopped.</dl>
<dt><code>&#8211;import</code><i> filename</i></dt>
<dd>Upon starting, import a <i>darkstat</i> database from the named file, relative to the chroot directory. If you wish to use <code>&#8211;import</code>, you must first specify a <code>&#8211;chroot</code> directory. If the import is unsuccessful, <i>darkstat</i> will start with an empty database.</dd>
<dt><code>&#8211;export</code><i> filename</i></dt>
<dd>On shutdown, or upon receiving SIGUSR1 or SIGUSR2, export the in-memory database to the named file, relative to the chroot directory. If you wish to use <code>&#8211;export</code>, you must first specify a <code>&#8211;chroot</code> directory, and it must be writeable by the <i>darkstat</i> user. A writeable chroot has security implications &#8211; if you are uncomfortable with this, do not use the <code>&#8211;export</code> functionality.</dd>
<dt><code>&#8211;pidfile</code><i> filename</i></dt>
<dd>
</dd><dl>
<dd>Creates a file containing the process ID of <i>darkstat</i>. This file will be unlinked upon clean shutdown. As with all pidfiles, if <i>darkstat</i> dies uncleanly, a stale pidfile can be left over. </dd>
<p> For example, start <i>darkstat</i> with:</p>
<dl>
<dd>darkstat -i fxp0 &#8211;chroot /var/run/darkstat &#8211;pidfile darkstat.pid</dd></dl>
<p> And stop with:</p>
<dl>
<dd>kill `cat /var/run/darkstat/darkstat.pid`</dd></dl>
<p> By default, <code><a href="/docs/linux/man/1-kill/">kill</a></code>(1) will send SIGTERM, which will cause <i>darkstat</i> to shut down cleanly.</dl>
<dt><code>&#8211;hosts-max</code><i> count</i></dt>
<dd>The maximum number of hosts that will be kept in the hosts table. This is used to limit how much accounting data will be kept in memory. The number of <code>&#8211;hosts-max</code> must be greater than <code>&#8211;hosts-keep</code></dd>
<dt><code>&#8211;hosts-keep</code><i> count</i></dt>
<dd>When the hosts table hits <code>&#8211;hosts-max</code> and traffic is seen from a new host, we clean out the hosts table, keeping only the top <code>&#8211;hosts-keep</code> number of hosts, sorted by total traffic.</dd>
<dt><code>&#8211;ports-max</code><i> count</i></dt>
<dd>The maximum number of ports that will be tracked for each host. This is used to limit how much accounting data will be kept in memory. The number of <code>&#8211;ports-max</code> must be greater than <code>&#8211;ports-keep</code></dd>
<dt><code>&#8211;ports-keep</code><i> count</i></dt>
<dd>When a ports table fills up, this many ports are kept and the rest are discarded.</dd>
<dt><code>&#8211;highest-port</code><i> port</i></dt>
<dd>Ports that are numerically higher than this will not appear in the per-host ports tables, although their traffic will still be accounted for. This can be used to hide ephemeral ports. By default, all ports are tracked.</dd>
<dt><code>&#8211;wait</code><i> secs</i></dt>
<dd>Don&#8217;t use this. It&#8217;s a hack to help victims of <i>NetworkManager</i> and similar systems.</dd>
<dl>
<dd>You should start <i>darkstat</i> after the capture interface has come up. If you can&#8217;t, specifying the <code>&#8211;wait</code> option will make <i>darkstat</i> sleep up to the specified number of seconds for the interface to become ready. Zero means wait indefinitely.</dd></dl>
<dt><code>&#8211;hexdump</code></dt>
<dd>Show hex dumps of received traffic. This is only for debugging, and implies <code>&#8211;verbose</code> and <code>&#8211;no-daemon</code>.</dd></dl>
<h2>Usage Examples</h2>
<p>To gather statistics on the <i>fxp0</i> interface:</p>
<dl>
<dd>darkstat -i fxp0</dd></dl>
<p> We want to account for traffic on the Internet-facing interface, but only serve web pages to our private local network where we have the IP address 192.168.0.1:</p>
<dl>
<dd>darkstat -i fxp0 -b 192.168.0.1</dd></dl>
<p> We want to serve web pages on the standard HTTP port:</p>
<dl>
<dd>darkstat -i fxp0 -p 80</dd></dl>
<p> We are on Optus (cable) and don&#8217;t want to account for the constant ARP traffic we are receiving:</p>
<dl>
<dd>darkstat -i fxp0 -f &quot;not arp&quot;</dd></dl>
<p> We only want to account for SSH traffic:</p>
<dl>
<dd>darkstat -i fxp0 -f &quot;port 22&quot;</dd></dl>
<p> We don&#8217;t want to account for traffic between internal IPs:</p>
<dl>
<dd>darkstat -i fxp0 -f &quot;not (src net 192.168.0 and dst net 192.168.0)&quot;</dd></dl>
<p> (For a full reference on filter syntax, refer to the <code>tcpdump</code>(1) manpage) </p>
<p> We have a network consisting of a gateway server (192.168.1.1) and a few workstations (192.168.1.2, 192.168.1.3, etc.) and we want to graph all traffic entering and leaving the local network, not just the gateway server (which is running <i>darkstat</i>):</p>
<dl>
<dd>darkstat -i fxp0 -l 192.168.1.0/255.255.255.0</dd></dl>
<p> On some systems, we can&#8217;t capture on a &quot;decoded&quot; interface but only on <i>nas0</i> which returns PPPoE encapsulated packets. Do PPPoE decoding, and override the local IP manually since it cannot be automatically detected. Note the /32 netmask:</p>
<dl>
<dd>darkstat -i nas0 &#8211;pppoe -l 192.168.1.1/255.255.255.255</dd></dl>
<h2>Signals</h2>
<p>To shut <i>darkstat</i> down cleanly, send a SIGTERM or SIGINT signal to the <i>darkstat</i> parent process. </p>
<p> Sending the SIGUSR1 signal will cause <i>darkstat</i> to empty out its in-memory database. If an <code>&#8211;export</code> file was set, it will first save the database to file. Sending SIGUSR2 will save the database without emptying it.</p>
<h2>Frequently Asked Questions</h2>
<h3>How many bytes does each bar on the graph represent?</h3>
<p>Hover your mouse cursor over a bar and you should get a tooltip saying exactly how many bytes in and out the bar represents.</p>
<h3>Why aren&#8217;t there labels / tics / a scale on the graphs?</h3>
<p>Because implementing them is hard. And doing so <i>correctly</i>, and in a way that works across all browsers, looks pretty much impossible. </p>
<p> I might attempt it some day. In the meantime, patches would be gladly accepted.</p>
<h3>Why are the graphs blank? All the bars are zero.</h3>
<p>The graphs only show traffic in/out of the local host, which is determined by getting the IP address of the interface you&#8217;re sniffing on. </p>
<p> You can use the <code>-l</code> argument to override the local address for accounting purposes. You can also use it to do accounting for a whole subnet by specifying an appropriate netmask.</p>
<h2>See Also</h2>
<p><code>tcpdump</code>(1)</p>
<h2>History</h2>
<p><i>darkstat</i> was written in 2001, largely as a result of a certain Australian cable Internet provider introducing a 3GB monthly traffic limit.</p>
<h2>Authors</h2>
<p>Emil Mikulic and others. (see the AUTHORS file)</p>
<h2>Website</h2>
<p><a rel="nofollow" href="http://unix4lyfe.org/darkstat/">http://unix4lyfe.org/darkstat/</a></p>
