---
title: "ip-sentinel(8)"
name: "ip-sentinel"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ip-sentinel/"
description: "ip-sentinel – keeps your IP space clean"
---

<p>ip-sentinel &#8211; keeps your IP space clean</p>
<h2>Synopsis</h2>
<p><code>ip-sentinel</code> [<code>&#8211;user</code>|<code>-u</code> <i>username</i>] [<code>&#8211;group</code>|<code>-g</code> <i>groupname</i>] [<code>&#8211;chroot</code>|<code>-r</code> <i>dir</i>] [<code>&#8211;ipfile</code>|<code>-i</code> <i>file</i>] [<code>&#8211;pidfile</code>|<code>-p</code> <i>file</i>] [<code>&#8211;logfile</code>|<code>-l</code> <i>file</i>] [<code>&#8211;errfile</code>|<code>-e</code> <i>file</i>] [<code>&#8211;mac</code> <i>mac</i>] [<code>&#8211;llmac</code> <i>mac</i>] [<code>&#8211;direction</code> <i>dir</i>] [<code>&#8211;action</code> <i>program</i>] [<code>&#8211;nofork</code>|<code>-n</code>] [<code>&#8211;help</code>|<code>-h</code>] [<code>&#8211;version</code>] <i>interface</i></p>
<h2>Description</h2>
<p><code>ip-sentinel</code> starts a daemon which tries to prevent unauthorized usage of IPs within an ethernet broadcastdomain by answering ARP requests. After receiving such a faked reply, the requesting party stores the MAC address in its ARP-table and will send future packets to this invalid MAC, rendering the IP unreachable. </p>
<p> After startup it opens its logfiles, goes into a chroot jail, drops privileges and forks itself into background by default. The parameters of these operations can by changed by the options described below. </p>
<p> <code>Warning:</code> with an uncareful configuration, ip-sentinel can bring down the entire network and your physical presence at the ip-sentinel machine and/or the switch will be required to fix it. Some switches can show an unexpected behavior are even crash when the special <i>802.*</i> mac-addresses will be used.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;user</code>|<code>-u&nbsp;<wbr></code><i>username&nbsp;<wbr></i>and<code>&nbsp;<wbr>&#8211;group</code>|<code>-g&nbsp;<wbr></code><i>groupname</i></p>
<dd>After doing basical initializations, the program will drop its privilegies by changing its user and group ID. The <i>username</i> and <i>groupname</i> parameters determine these new IDs and must be an alphanumeric username/groupname or a numeric uid/gid. </p>
<p> <code>Attention:</code> When having a dietlibc-compiled version in a system which uses remote NSS (e.g. LDAP, NIS) to make passwd-lookups, you will have to use numeric IDs.</p>
<dt><code>&#8211;chroot</code>|<code>-r&nbsp;<wbr></code><i>dirname</i></p>
<dd>Specifies the directory where the program shall go into and call <code>chroot()</code> after finishing its initialization. By default it is the homedirectory of the user specified with the <code>&#8211;user</code> option.</p>
<dt><code>&#8211;ipfile</code>|<code>-i&nbsp;<wbr></code><i>filename</i></p>
<dd>Sets the name of the configuration file which contains the list of forbidden IPs. This name is relative to the chroot and is <code>ips.cfg</code> by default. This file will be reread automatically after changes.</p>
<dt><code>&#8211;pidfile</code>|<code>-p&nbsp;<wbr></code><i>filename</i></p>
<dd>Sets the file where the pid of the daemon will be written into. This filename is relative to the root-filesystem and is <code>/var/run/ip-sentinel.run</code> by default.</p>
<dt><code>&#8211;logfile</code>|<code>-l&nbsp;<wbr></code><i>filename</i></p>
<dd>Sets the file where normal operations will be logged. Normal operations are e.g. an ARP-reply for a forbidden IP. This filename is relative to the root-filesystem and <code>/var/log/ip-sentinel.out</code> by default.</p>
<dt><code>&#8211;errfile</code>|<code>-e&nbsp;<wbr></code><i>filename</i></p>
<dd>Sets the file where error-conditions will be logged. Error-conditions are e.g. detected DOS attacks (bombing the ip-sentinel with ARP-requests) or errors in the configuration file. This filename is relative to the root-filesystem and <code>/var/log/ip-sentinel.err</code> by default.</p>
<dt><code>&#8211;nofork</code>|<code>-n</code></p>
<dd>Prevents daemon from going into background after initialization. This option may be useful when using advanced init-concepts like minit (<a rel="nofollow" href="http://www.fefe.de/minit/">http://www.fefe.de/minit/</a>).</p>
<dt><code>&#8211;direction&nbsp;<wbr></code><i>dir</i></p>
<dd>ip-sentinel can answer both requests asking for an intruder&#8217;s address, and requests coming from an intruder asking for official addresses. This parameter specifies which requests shall be answered. Possible values are <i>FROM</i> (requests from intruders), <i>TO</i> (requests to intruders) and <i>BOTH</i>. The current default value is <i>TO</i>, but will probably change to <i>BOTH</i> in future versions.</p>
<dt><code>&#8211;mac&nbsp;<wbr></code><i>mac</i></p>
<dd>Use <i>mac</i> as the default faked mac-address; see below for possible values. This parameter can be overriden in the ipfile for each questionable IP. The default value is <i>RANDOM</i>.</p>
<dt><code>&#8211;llmac&nbsp;<wbr></code><i>mac</i></p>
<dd>Specifies the mac-address which will be used in the link-level headers when answering requests <code>from</code> intruders. Additionally to the values described below, ip-sentinel understands the <i>SAME</i> string, which means that the address from the ARP-header will be used. When not using the <i>FROM</i> or <i>BOTH</i> directions, the assigned value will not have any effect. The default is <i>LOCAL</i>.</p>
<dt><code>&#8211;poison</code></p>
<dd>When an intruder sends a request <code>from</code> a registered ip address and this option is set, ip-sentinel will send ARP replies which are poisoning this ip. When the <i>@!srcmac</i> syntax is used for the questionable ip, the <i>srcmac</i> is used as the is-at mac. Else, the mac specified by the <i>&#8211;mac</i> option is used. </p>
<p> This option takes an affect only when <i>&#8211;destination BOTH </i>or<i> FROM</i> is specified.</p>
<dt><code>&#8211;action&nbsp;<wbr></code><i>program</i></p>
<dd>Execute <code>program</code> when a faked ARP reply will be generated. It will be called with 6 arguments:</p>
<dl>
<dd>
<dl>
<dt>*</p>
<dd><i>type</i> 0 when an intruder sent the request, 1 when a protected IP was requested and -1 else (should never happen)</p>
<dt>*</p>
<dd><i>spa</i> the protocol address (IP) of the source</p>
<dt>*</p>
<dd><i>sha</i> the hardware address (MAC) of the source</p>
<dt>*</p>
<dd><i>tpa</i> the protocol address (IP) of the target</p>
<dt>*</p>
<dd><i>tha</i> the hardware address (MAC) of the target</p>
<dt>*</p>
<dd><i>mac</i> the generated MAC address</dl>
</dl>
<dl>
<dd>The program will be executed only without evaluating its return value or something else. Please note, that the program will be executed in the chroot with restricted rights.</dl>
<dt><code>&#8211;help</code>|<code>-h</code></p>
<dd>Prints help message and exits.</p>
<dt><code>&#8211;version</code></p>
<dd>Prints the version of the program and exits.</p>
<dt><i>interface</i></p>
<dd>Specifies the network-interface where ip-sentinel listens for ARP-requests and sends ARP-replies. It is a name like &quot;eth0&quot;; aliases like &quot;eth0:1&quot; are not possible.</dl>
<h2>Configuration File</h2>
<p>The location of the configfile is relatively to the choosen chroot-directory. Its default is determined at compilation time but it can be overriden by the <code>&#8211;ipfile</code> option. </p>
<p> The content of this file has the following syntax:</p>
<dl>
<dt><i>ip&nbsp;<wbr></i>[<i>mac</i>]</p>
<dd>Specifies an IP which shall be blocked. &quot;Blocked&quot; means that ARP-replies will be generated telling that the IP address <i>ip</i> has the MAC <i>mac</i>. When the MAC parameter is not given, a random one will be choosen. </p>
<p> <code>Attention:</code> Assigning a MAC in a switched environment will not have the desired effect, because the switch will be confused when receiving ARP-replies for the same IP on different ports (this one of the bad-host and this one of the ip-sentinel host). </p>
<p> Examples are: &quot;192.168.42.23 11:22:33:44:55:66&quot; or &quot;10.0.0.0&quot;.</p>
<dt><i>ip</i><code>@</code><i>[</i><code>!</code><i>]srcmac&nbsp;<wbr>[mac]</i></p>
<dd>Similarly to above, but when receiving ARP-requests, the entire sender-address (IP and MAC) will be compared against the <i>ip</i> and <i>srcmac</i> values. This setting affects packets <code>from</code> intruders only; ip-sentinel will not generate replies when <i>ip</i> is requested. </p>
<p> When the <i>srcmac</i> is negated with &quot;<i>!</i>&quot;, only addresses from this ip which are <code>not</code> having this mac will be matching. </p>
<p> Examples are: &quot;10.0.0.1@0:1:2:3:4:5&quot; or &quot;10.0.0.2@!a:b:c:d:e:f&quot;.</p>
<dt><code>*@</code><i>srcmac&nbsp;<wbr>[mac]</i></p>
<dd>Every host using the srcmac will be blocked unless there is a matching <i>ip [at] srcmac</i> specification. This option does <code>not</code> support &#8216;!&#8217; modifiers.</p>
<dt><i>net</i><code>/</code><i>mask&nbsp;<wbr></i>[<i>mac</i>]</p>
<dd>
<dt> <i>net</i><code>/</code><i>mask</i><code>@</code><i>[</i><code>!</code><i>]srcmac&nbsp;<wbr></i>[<i>mac</i>]</p>
<dd>Specifies that IPs of an entiry network shall be blocked. See above for the meaning of &quot;blocked&quot;. It is possible to specify a MAC address; else a random one will be generated. </p>
<p> Examples are: &quot;169.0.0.0/8&quot;, &quot;192.168.8.15/255.255.65.31&quot; or &quot;192.168.23.42/26 a:b:c:d:e:f&quot;.</p>
<dt><code>!</code><i>ip</i></p>
<dd>
<dt> <code>!</code><i>ip</i><code>@</code><i>[</i><code>!</code><i>]srcmac</i></p>
<dd>The given IP address <i>ip</i> will be ignored. By default, any not specified address will be ignored but when having blocked netmasks it may be usefully to allow certain IPs. </p>
<p> An example is: &quot;!192.168.23.42&quot;</p>
<dt><code>!</code><i>net</i><code>/</code><i>mask</i></p>
<dd>
<dt> <code>!</code><i>net</i><code>/</code><i>mask</i><code>@</code><i>[</i><code>!</code><i>]srcmac</i></p>
<dd>Tells that IPs of the given network shall be ignored. </p>
<p> Examples are: &quot;!192.168.1.0/255.255.255.0&quot; or &quot;!0.0.0.0/0&quot; (the default).</p>
<dt><code>#&nbsp;<wbr></code><i>comment&nbsp;<wbr></i>(and empty lines)</p>
<dd>A comment; will be ignored </p>
</dl>
<p> To be switch-friendly, there are only a few random MACs possible which are having the format &quot;de:ad:be:ef:00:XX&quot;. Within a short timespan only 32 values are possible for <i>XX</i>. </p>
<p> When having overlapping networks and/or single IPs, this one with the most specified netmask (count of 1&#8217;s) takes precedence. When netmasks are equal, networks which are using the &quot;@srcmac&quot; or &quot;@!srcmac&quot; syntax are taking precedence over those without source-macs. This &quot;@&#8230;&quot; rule <code>does not</code> apply to IPs. The behavior is unspecified when having overlapping networks with the same count of 1&#8217;s and &quot;@&#8230;&quot; specification, or when having duplicate IPs.</p>
<h3>Performance</h3>
<p>The lookup of single IPs has a complexity of O(log n) and this of netmasks a complexity of <a href="/docs/linux/man/n-o/">O</a>(n).</p>
<h3>Special Mac Addresses</h3>
<p>Beside the usual hex-octets-delimited-by-colons mac addresses, ip-sentinel understands some special strings both on the commandline and in the configuration file:</p>
<dl>
<dt><code>LOCAL</code></p>
<dd>expands to the mac-address of the used interface</p>
<dt><code>RANDOM</code></p>
<dd>means a random mac-address which is newly calculated on every usage</p>
<dt><code>802.1d</code></p>
<dd>expands to 01:80:C2:00:00:00 which is the &quot;Bridge Group Address&quot;.</p>
<dt><code>802.3x</code></p>
<dd>expands to 01:80:C2:00:00:01 which is the &quot;IEEE Std. 802.3x Full Duplex PAUSE operation&quot;. This MAC address will be blocked by a lot of switches and will probably become the default in future versions.</dl>
<p> The <i>802.*</i> addresses are having a special meaning for some switches and packets having them as destination-address will be dropped by the switch instead of flooding all ports. But it depends on the used switch how/if these macs are honored. </p>
<p> Some switches can show an unexpected behavior are even crash if the special <i>802.*</i> mac-addresses will be used.</p>
<h3>Ranges</h3>
<p>Except in comments, it is possible to specify ranges everywhere in the configuration file. These ranges are having the format &quot;{from-to}&quot; or &quot;{item1,item2,&#8230;,itemN}&quot;. The first format includes any number beginning at &quot;from&quot; till &quot;to&quot; (inclusive), while the latter format expands to the listed items only. The expansion happens on a line-level and it is possible to use more than one range per line, so that </p>
<dl>
<dd>192.168.0.{1-3} 0:0:0:0:0:1</p>
<dl>
<dd>192.168.1.{1,3} 0:0:0:0:0:2</p>
<dl>
<dd>192.168.{2,4}.{1-3} 0:0:0:0:0:3 </p>
<p> is the same like writing </p>
<dl>
<dd>192.168.0.1 0:0:0:0:0:1</p>
<dl>
<dd>192.168.0.2 0:0:0:0:0:1</p>
<dl>
<dd>192.168.0.3 0:0:0:0:0:1</p>
<dl>
<dd>192.168.1.1 0:0:0:0:0:1</p>
<dl>
<dd>192.168.1.3 0:0:0:0:0:1</p>
<dl>
<dd>192.168.2.1 0:0:0:0:0:3</p>
<dl>
<dd>192.168.2.2 0:0:0:0:0:3</p>
<dl>
<dd>192.168.2.3 0:0:0:0:0:3</p>
<dl>
<dd>192.168.4.1 0:0:0:0:0:3</p>
<dl>
<dd>192.168.4.2 0:0:0:0:0:3</p>
<dl>
<dd>192.168.4.3 0:0:0:0:0:3 </p>
<p> Because there can be created very much entries with a single line (e.g. &quot;{0-255}.{0-255}.{0-255}.{0-255}&quot; would cover the entire IPv4 internet), ranges should be used sparely. When possible, large ranges should be expressed with netmasks. </p>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
<h3>Example</h3>
<dl>
<dd>0.0.0.0/0 ## Block anything</p>
<dl>
<dd>!192.168.0.0/24 ## Allow IPs of the form 192.168.0.*</p>
<dl>
<dd>192.168.0.0 ## but block 192.168.0.0</p>
<dl>
<dd>192.168.0.1 a:b:c:d:e:f ## use a special mac for 192.168.0.1</p>
<dl>
<dd>192.168.0.2 802.1d ## and 01:80:C2:00:00:00 for 192.168.0.2</p>
<dl>
<dd>10.0.0.1@a:a:a:a:a:a</p>
<dl>
<dd>10.0.0.2@!1:1:1:1:1:1</p>
<dl>
<dd>*@b:b:b:b:b:b ## block MAC b:b:b:b:b:b regardless of the IP </p>
<p> This setup will not send ARP-replies for the IPs 192.168.0.{3-255} but when a host tries to use e.g. 169.254.145.213, ip-sentinel will tell that this IP has a MAC of &quot;de:ad:be:ef:00:XX&quot;. </p>
<p> When an intruder is at &quot;10.0.0.1&quot; and uses the mac &quot;a:a:a:a:a:a:&quot;, a faked reply will be generated. Users at the same ip but another mac will be ignored. </p>
<p> In opposite, users with ip &quot;10.0.0.2&quot; and mac &quot;1:1:1:1:1:1&quot; will be ignored but intruders with other macs (e.g. &quot;2:2:2:2:2:2&quot;) are getting faked replies. When <i>&#8211;poision</i> is used, ip-sentinel will generate a &quot;10.0.0.2 is at 1:1:1:1:1:1&quot; arp-reply to a broad address.</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
<h2>See Also</h2>
<p><code>RFC 826</code>, <code>IEEE Std 802.1D</code></p>
<h2>Author</h2>
<p>Enrico Scholz &lt;enrico.scholz [at] informatik.tu-chemnitz.de&gt;</p>
