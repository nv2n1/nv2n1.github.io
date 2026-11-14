---
title: "trafshow(1)"
name: "trafshow"
section: "1"
letter: "t"
url: "/docs/linux/man/1-trafshow/"
description: "trafshow – full screen show network traffic"
---

<h2>NAME</h2>
<p> trafshow &#8211; full screen show network traffic</p>
<h2>SYNOPSIS</h2>
<p> <code>trafshow</code> [<code>-vpnb</code>] [<code>-a</code> <i>len</i>] [<code>-c</code> <i>conf</i>] [<code>-i</code> <i>name</i>] [<code>-s</code> <i>str</i>] [<code>-u</code> <i>port</i>] [<code>-R</code> <i>refresh</i>] [<code>-P</code> <i>purge</i>] [<code>-F</code> <i>file</i> | <i>expr</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>TrafShow</code> is a simple interactive program that gather the <code>network traffic</code> from all libpcap-capable interfaces to accumulate it in memory cache, and then separately display it on appropriated curses window in line-narrowed manner as a list of network flows sorted by throughput. Display updates occurs nearly in real time, asynchronously from the data collecting. It look like a <code>live show</code> of traffic flows. Any kind of network traffic are mixed together in the one live-show screen, an Ethernet, IP, etc.<br />
 <code>Hint</code>: Please press `<code>H</code>&#8216; key inside a show to get brief help! </p>
<p> The IP traffic can be <code>aggregated</code> by netmask prefix bits and service ports to reorganize a heap of trivial flows into the treelike hierarchies suitable for human perception. The user can glance over the list of resulting flows and select at their to browse detail. So you can deepen into the traffic inheritance hierarchy and inspect the packets of each trivial flow in variety of presentations: raw-hex, ascii, time-stamp.<br />
 The program make aggregation automatically when number of flows will exceed some reasonable amount. Just a few seconds after launch may be required for adaptation to your volume of traffic. Use <code>-a</code> <i>len</i> option (see below) to overwrite the default behaviour. </p>
<p> <code>TrafShow</code> also listens on UDP port (9995 by default) for diverse feeders of <code>Cisco Netflow</code> and then separately display the collected data in the same manner as described above. The following versions of Netflow are currently supported: V1, V5, V7. Use <code>-u</code> <i>port</i> option (see below) to overwrite the default behaviour. </p>
<p> This program may be found wonderful at lest to locate suspicious traffic on the net very quickly on demand, or to evaluate real time traffic bandwidth utilization, in a simplest and convenient environment. But it is not intended for collecting and analysis of the network traffic for a long period of time, nor for billing! </p>
<p> The program pretend to be IPv6 compatible and ready to using, but it is not tested enough. You can define INET6 to do so.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code></p>
<dd> Print detailed version information and exit.</p>
<dt><code>-p</code></p>
<dd> Do not put interface(s) into promiscuous mode.</p>
<dt><code>-n</code></p>
<dd> Do not convert numeric values to names (host addresses, port numbers, etc.). The mode can be toggled On/Off during a show by pressing the `<code>N</code>&#8216; key.</p>
<dt><code>-b</code></p>
<dd> To place a backflow entries near to the main streams in the sorted list of traffic flows.<br />
 <code>Note</code>: this mode can raise the system load dangerously high because it take a lot of CPU cycles!</p>
<dt><code>-a</code> <i>len</i></p>
<dd> To aggregate traffic flows using IP netmask prefix <i>len</i>. This option also turn on service ports aggregation. The <i>len</i> expected as number of <code>bits</code> in the network portion of IP addresses (like CIDR). The aggragation <i>len</i> can be changed during a show by pressing the `<code>A</code>&#8216; key, and turned Off by empty string.<br />
 <code>Hint</code>: Please use <i>0</i> to reduce output just for network services.</p>
<dt><code>-c</code> <i>conf</i></p>
<dd> Use alternate color <i>config file</i> instead of default <i>/etc/trafshow</i>.</p>
<dt><code>-i</code> <i>name</i></p>
<dd> Listen on the specified network interface <i>name</i>. If unspecified, <code>TrafShow</code> collect data from <i>all</i> network interfaces, configured <code>UP</code> in the system. In the last case the system must supply enough number of packet capture devices (like /dev/bpf#).</p>
<dt><code>-s</code> <i>str</i></p>
<dd> To search and follow for list <code>item</code> matched by <i>string</i>, moving the cursor bar. The found <code>item</code> try to stay highlighted. The mode can be turned Off by `<code>Ctrl</code>&#8211;<code>/</code>&#8216; key press or [re]entered again by `<code>/</code>&#8216; key directly in the live show.</p>
<dt><code>-u</code> <i>port</i></p>
<dd> Listen on the specified UDP <i>port</i> number for the <code>Cisco Netflow</code> feed. The default port number is <i>9995</i>.<br />
 <code>Hint</code>: Please use <i>0</i> to disable this functionality.</p>
<dt><code>-R</code> <i>refresh</i></p>
<dd> Set the <code>refresh period</code> of data show to <i>seconds</i>, <i>2</i> seconds by default. This option can be changed during a show by pressing the `<code>R</code>&#8216; key.</p>
<dt><code>-P</code> <i>purge</i></p>
<dd> Set the expired data <code>purge period</code> to <i>seconds</i>, <i>10</i> seconds by default. This option can be changed during a show by pressing the `<code>P</code>&#8216; key.</p>
<dt><code>-F</code> <i>file</i></p>
<dd> Use <i>file</i> as input for the <code>filter expression</code>.</p>
<dt><i>expr</i></p>
<dd> Select which packets will be displayed. If no <i>expression</i> is given, all packets on the net will be displayed. Otherwise, only packets for which <i>expression</i> is `true&#8217; will be displayed.<br />
 The <code>filter expression</code> can be changed during a show by pressing the `<code>F</code>&#8216; key, and turned Off by empty string.<br />
 Please see <code><a href="/docs/linux/man/1-tcpdump/">tcpdump</a></code>(1) man page for syntax of <code>filter expression</code>.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/trafshow</i></p>
<dd> The default colors configuration file if any.</p>
<dt><i>$HOME/.trafshow</i></p>
<dd> The personal file with the user defined colors.</dl>
<h2>COLORS</h2>
<p> If <code>TrafShow</code> has been compiled with modern curses libraries such as <code>Slang</code> or <code>Ncurses</code> it been able to show colored traffic on the color-capable terminal. Hopefully, no special actions required to install them because your system has it by default (leastwise last years). </p>
<p> The syntax of <code>TrafShow</code> color configuration file as follow:</p>
<dl>
<dt><i>default</i> <i>fcolor</i><code>:</code><i>bcolor</i></p>
<dd> Set the default screen background color-pair</p>
<dt><i>port</i>[<code>/</code><i>proto</i>] <i>fcolor</i><code>:</code><i>bcolor</i></p>
<dd> Set color pattern by service port</p>
<dt>[<i>proto</i>] <i>src</i>[<code>/</code><i>mask</i>][<code>,</code><i>port</i>] <i>dst</i>[<code>/</code><i>mask</i>][<code>,</code><i>port</i>] <i>fcolor</i><code>:</code><i>bcolor</i></p>
<dd> Set color pattern by pair of source and destination addresses</dl>
<p> The tokens <i>*</i>, <i>any</i>, or <i>all</i> matchs <code>ANY</code> in the pattern. Where <i>fcolor</i> is foreground color and <i>bcolor</i> is background color.<br />
 The fcolor and bcolor may be one of the following:</p>
<dl>
<dt><i>black red green yellow blue magenta cyan white</i></p>
<dd> It posible to indicate color as number from 0 to 7.</dl>
<p> The upper-case <i>F</i>color mean <code>bright on</code>. The upper-case <i>B</i>color mean <code>blink on</code>.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-pcap/">pcap</a>(3), <a href="/docs/linux/man/1-tcpdump/">tcpdump</a>(1), <a href="/docs/linux/man/4-bpf/">bpf</a>(4)</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> Thanks to Van Jacobson &lt;van(at)helios.ee.lbl.gov&gt; and Steven McCanne &lt;mccanne(at)helios.ee.lbl.gov&gt;, all of Lawrence Berkeley Laboratory, University of California, Berkeley. Special thank to Jun-ichiro itojun Hagino &lt;itojun(at)iijlab.net&gt; for IPv6 patches.</p>
<h2>AUTHOR</h2>
<p> Vladimir Vorobyev &lt;bob(at)turbo.nsk.su&gt;.</p>
<h2>BUGS</h2>
<p> Depending of traffic volume, <code>TrafShow</code> can take a lot of CPU cycles and memory.<br />
 It is impossible to use packet matching <code>expressions</code> in the NetFlow mode. </p>
<h2>Index</h2>
