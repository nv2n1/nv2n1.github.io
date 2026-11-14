---
title: "shorewall6-tcdevices(5)"
name: "shorewall6-tcdevices"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall6-tcdevices/"
description: "tcdevices – Shorewall6 Traffic Shaping Devices file"
---

<p>tcdevices &#8211; Shorewall6 Traffic Shaping Devices file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall6/tcdevices</code></dl>
<h2>Description</h2>
<dd>Entries in this file define the bandwidth for interfaces on which you want traffic shaping to be enabled. </p>
<p> If you do not plan to use traffic shaping for a device, don&#8217;t put it in here as it limits the throughput of that device to the limits you set here. </p>
<p> A note on the <i>bandwidth</i> definitions used in this file: </p>
<dl>
<dd>&bull; don&#8217;t use a space between the integer value and the unit: 30kbit is valid while 30 kbit is not.</dl>
<dl>
<dd>&bull; you can use one of the following units: </p>
<p> <code>kbps</code></p>
<dl>
<dd>Kilobytes per second.</dl>
<p> <code>mbps</code></p>
<dl>
<dd>Megabytes per second.</dl>
<p> <code>kbit</code></p>
<dl>
<dd>Kilobits per second.</dl>
<p> <code>mbit</code></p>
<dl>
<dd>Megabits per second.</dl>
<p> <code>bps</code> or <code>number</code></p>
<dl>
<dd>Bytes per second.</dl>
</dl>
<dl>
<dd>&bull; Only whole integers are allowed.</dl>
<p> The columns in the file are as follows (where the column name is followed by a different name in parentheses, the different name is used in the alternate specification syntax). </p>
<p> <code>INTERFACE</code> &#8211; [<i>number</i>:]<i>interface</i></p>
<dl>
<dd>Name of <i>interface</i>. Each interface may be listed only once in this file. You may NOT specify the name of an alias (e.g., eth0:0) here; see m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/FAQ.htm#faq18">http://www.shorewall.net/FAQ.htm#faq18</a></code>m[]<font SIZE="-2">[1]</font> </p>
<p> You may NOT specify wildcards here, e.g. if you have multiple ppp interfaces, you need to put them all in here! </p>
<p> If the device doesn&#8217;t exist, a warning message will be issued during &quot;shorewall6 [re]start&quot; and &quot;shorewall6 refresh&quot; and traffic shaping configuration will be skipped for that device. </p>
<p> Shorewall6 assigns a sequential interface number to each interface (the first entry in the file is interface 1, the second is interface 2 and so on) Beginning with Shorewall6-perl 4.1.6, you can explicitly specify the interface number by prefixing the interface name with the number and a colon (&quot;:&quot;). Example: 1:eth0.</dl>
<p> <code>IN-BANDWIDTH (in_bandwidth)</code> &#8211; {-|<i>bandwidth</i>[:<i>burst</i>]|~<i>bandwidth</i>[:<i>interval</i>:<i>decay_interval</i>]}</p>
<dl>
<dd>The incoming <i>bandwidth</i> of that interface. Please note that you are not able to do traffic shaping on incoming traffic, as the traffic is already received before you could do so. But this allows you to define the maximum traffic allowed for this interface in total, if the rate is exceeded, the packets are dropped. You want this mainly if you have a DSL or Cable connection to avoid queuing at your providers side. </p>
<p> If you don&#8217;t want any traffic to be dropped, set this to a value to zero in which case Shorewall will not create an ingress qdisc.Must be set to zero if the REDIRECTED INTERFACES column is non-empty. </p>
<p> The optional burst option was added in Shorewall 4.4.18. The default <i>burst</i> is 10kb. A larger <i>burst</i> can help make the <i>bandwidth</i> more accurate; often for fast lines, the enforced rate is well below the specified <i>bandwidth</i>. </p>
<p> What is described above creates a rate/burst policing filter. Beginning with Shorewall 4.4.25, a rate-estimated policing filter may be configured instead. Rate-estimated filters should be used with Ethernet adapters that have Generic Receive Offload enabled by default. See m[blue]<code>Shorewall FAQ 97a</code>m[]<font SIZE="-2">[2]</font>. </p>
<p> To create a rate-estimated filter, precede the bandwidth with a tilde (&quot;~&quot;). The optional interval and decay_interval determine how often the rate is estimated and how many samples are retained for estimating. Please see m[blue]<code><a rel="nofollow" href="http://ace-host.stuart.id.au/russell/files/tc/doc/estimators.txt">http://ace-host.stuart.id.au/russell/files/tc/doc/estimators.txt</a></code>m[] for details.</dl>
<p> <code>OUT-BANDWIDTH</code> (out_bandwidth) &#8211; <i>bandwidth</i></p>
<dl>
<dd>The outgoing <i>bandwidth</i> of that interface. This is the maximum speed your connection can handle. It is also the speed you can refer as &quot;full&quot; if you define the tc classes in m[blue]<code>shorewall6-tcclasses</code>m[]<font SIZE="-2">[3]</font>(5). Outgoing traffic above this rate will be dropped.</dl>
<p> <code>OPTIONS</code> &#8211; {<code>&#8211;</code>|<code>{classify</code>|htb|<code>hfsc</code>|<code>linklayer</code>={<code>ethernet</code>|<code>atm</code>|<code>adsl</code>}|<code>tsize</code>=<i>tsize</i>|<code>mtu</code>=<i>mtu</i>|<code>mpu</code>=<i>mpu</i>|<code>overhead</code>=<i>overhead</i>} ,&#8230;}</p>
<dl>
<dd><code>classify</code> &#8212; When specified, Shorewall will not generate tc or Netfilter rules to classify traffic based on packet marks. You must do all classification using CLASSIFY rules in m[blue]<code>shorewall6-tcrules</code>m[]<font SIZE="-2">[4]</font>(5). </p>
<p> <code>htb</code> &#8211; Use the Hierarchical Token Bucket queuing discipline. This is the default. </p>
<p> <code>hfsc</code> &#8211; Shorewall normally uses the Hierarchical Token Bucket queuing discipline. When <code>hfsc</code> is specified, the Hierarchical Fair Service Curves discipline is used instead(see tc-hfsc (7)). </p>
<p> <code>linklayer</code> &#8211; Added in Shorewall 4.5.6. Type of link (ethernet, atm, adsl). When specified, causes scheduler packet size manipulation as described in tc-stab (8). When this option is given, the following options may also be given after it: <code>mtu</code>=<i>mtu</i> &#8211; The device MTU; default 2048 (will be rounded up to a power of two) </p>
<p> <code>mpu</code>=<i>mpubytes</i> &#8211; Minimum packet size used in calculations. Smaller packets will be rounded up to this size </p>
<p> <code>tsize</code>=<i>tablesize</i> &#8211; Size table entries; default is 512 </p>
<p> <code>overhead</code>=<i>overheadbytes</i> &#8211; Number of overhead bytes per packet.</dl>
<p> <code>REDIRECTED INTERFACES</code> (redirect) &#8211; [<i>interface</i>[,<i>interface</i>]&#8230;]</p>
<dl>
<dd>Added in Shorewall6-perl 4.1.6. May only be specified if the interface in the INTERFACE column is an Intermediate Frame Block (IFB) device. Causes packets that enter each listed interface to be passed through the egress filters defined for this device, thus providing a form of incoming traffic shaping. When this column is non-empty, the <code>classify</code> option is assumed.</dl>
<h2>Examples</h2>
<p>Example 1:</p>
<dl>
<dd>Suppose you are using PPP over Ethernet (DSL) and ppp0 is the interface for this. The device has an outgoing bandwidth of 500kbit and an incoming bandwidth of 6000kbit </p>
<dl>
<dd>
<pre> #INTERFACE IN-BANDWIDTH OUT-BANDWIDTH OPTIONS REDIRECTED
 # INTERFACES
 1:ppp0 6000kbit 500kbit</pre>
</dl>
</dl>
<h2>Files</h2>
<p>/etc/shorewall6/tcdevices</p>
<h2>See Also</h2>
<p>tc-hfsc (7) </p>
<p> m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/traffic_shaping.htm">http://www.shorewall.net/traffic_shaping.htm</a></code>m[]<font SIZE="-2">[5]</font> </p>
<p> m[blue]<code><a rel="nofollow" href="http://ace-host.stuart.id.au/russell/files/tc/doc/estimators.txt">http://ace-host.stuart.id.au/russell/files/tc/doc/estimators.txt</a></code>m[] </p>
<p> <a href="/docs/linux/man/8-shorewall6/">shorewall6</a>(8), <a href="/docs/linux/man/5-shorewall6-accounting/">shorewall6-accounting</a>(5), <a href="/docs/linux/man/5-shorewall6-actions/">shorewall6-actions</a>(5), <a href="/docs/linux/man/5-shorewall6-blacklist/">shorewall6-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall6-hosts/">shorewall6-hosts</a>(5), <a href="/docs/linux/man/5-shorewall6-interfaces/">shorewall6-interfaces</a>(5), <a href="/docs/linux/man/5-shorewall6-maclist/">shorewall6-maclist</a>(5), <a href="/docs/linux/man/5-shorewall6-netmap/">shorewall6-netmap</a>(5),<a href="/docs/linux/man/5-shorewall6-params/">shorewall6-params</a>(5), <a href="/docs/linux/man/5-shorewall6-policy/">shorewall6-policy</a>(5), <a href="/docs/linux/man/5-shorewall6-providers/">shorewall6-providers</a>(5), <a href="/docs/linux/man/5-shorewall6-rtrules/">shorewall6-rtrules</a>(5), <a href="/docs/linux/man/5-shorewall6-routestopped/">shorewall6-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall6-rules/">shorewall6-rules</a>(5), <a href="/docs/linux/man/5-shorewall6-conf/">shorewall6.conf</a>(5), <a href="/docs/linux/man/5-shorewall6-secmarks/">shorewall6-secmarks</a>(5), <a href="/docs/linux/man/5-shorewall6-tcclasses/">shorewall6-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall6-mangle/">shorewall6-mangle</a>(5), <a href="/docs/linux/man/5-shorewall6-tos/">shorewall6-tos</a>(5), <a href="/docs/linux/man/5-shorewall6-tunnels/">shorewall6-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall6-zones/">shorewall6-zones</a>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/FAQ.htm#faq18">http://www.shorewall.net/FAQ.htm#faq18</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/FAQ.htm#faq18">http://www.shorewall.net/FAQ.htm#faq18</a></dl>
<dt> 2.</p>
<dd>Shorewall FAQ 97a</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/FAQ.htm#faq97a">http://www.shorewall.net/FAQ.htm#faq97a</a></dl>
<dt> 3.</p>
<dd>shorewall6-tcclasses</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6-tcclasses.html">http://www.shorewall.net/manpages6/shorewall6-tcclasses.html</a></dl>
<dt> 4.</p>
<dd>shorewall6-tcrules</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6-tcrules.html">http://www.shorewall.net/manpages6/shorewall6-tcrules.html</a></dl>
<dt> 5.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/traffic_shaping.htm">http://www.shorewall.net/traffic_shaping.htm</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/traffic_shaping.htm">http://www.shorewall.net/traffic_shaping.htm</a></dl>
