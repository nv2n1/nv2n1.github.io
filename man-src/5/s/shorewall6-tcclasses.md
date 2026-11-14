---
title: "shorewall6-tcclasses(5)"
name: "shorewall6-tcclasses"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall6-tcclasses/"
description: "tcclasses – Shorewall6 file to define HTB and HFSC classes"
---

<p>tcclasses &#8211; Shorewall6 file to define HTB and HFSC classes</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall6/tcclasses</code></dl>
<h2>Description</h2>
<dd>A note on the <i>rate</i>/bandwidth definitions used in this file:</p>
<dl>
<dd>&bull; don&#8217;t use a space between the integer value and the unit: 30kbit is valid while 30 kbit is NOT.</dl>
<dl>
<dd>&bull; you can use one of the following units: <code>kpbs</code></p>
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
<dd>&bull; if you want the values to be calculated for you depending on the output bandwidth setting defined for an interface in tcdevices, you can use expressions like the following: full/3</p>
<dl>
<dd>causes the bandwidth to be calculated as 1/3 of the full outgoing speed that is defined.</dl>
<p> full*9/10</p>
<dl>
<dd>will set this bandwidth to 9/10 of the full bandwidth</dl>
<p> Note that in a sub-class (a class that has a specified parent class), full refers to the RATE or CEIL of the parent class rather than to the OUT-BANDWIDTH of the device. DO NOT add a unit to the rate if it is calculated !</dl>
<p> The columns in the file are as follows. <code>INTERFACE</code> &#8211; <i>interface</i>[[:<i>parent</i>]:<i>class</i>]</p>
<dl>
<dd>Name of <i>interface</i>. You may specify either the interface number or the interface name. If the <code>classify</code> option is given for the interface in m[blue]<code>shorewall6-tcdevices</code>m[]<font SIZE="-2">[1]</font>(5), then you must also specify an interface class (an integer that must be unique within classes associated with this interface). You may NOT specify wildcards here, e.g. if you have multiple ppp interfaces, you need to put them all in here! Please note that you can only use interface names in here that have a bandwidth defined in the m[blue]<code>shorewall6-tcdevices</code>m[]<font SIZE="-2">[1]</font>(5) file. Normally, all classes defined here are sub-classes of a root class (class number 1) that is implicitly defined from the entry in m[blue]<code>shorewall6-tcdevices</code>m[]<font SIZE="-2">[1]</font>(5). You can establish a class hierarchy by specifying a <i>parent</i> class &#8212; the number of a class that you have previously defined. The sub-class may borrow unused bandwidth from its parent.</dl>
<p> <code>MARK</code> &#8211; {-|<i>value</i>[:<i>priority</i>]}</p>
<dl>
<dd>The mark <i>value</i> which is an integer in the range 1-255. You set mark values in the m[blue]<code>shorewall-mangle</code>m[]<font SIZE="-2">[2]</font>(5) file, marking the traffic you want to fit in the classes defined in here. You can use the same marks for different interfaces. The <i>priority</i>, if specified, is an integer in the range 1-65535 and determines the relative order in which the tc mark classification filter for this class is to be applied to packets being sent on the <i>interface</i>. Filters are applied in ascending numerical order. If not supplied, the value is derived from the class priority (PRIORITY column value below): (<i>class priority</i> &lt;&lt; 8) | 20.</dl>
<p> <code>RATE</code> &#8211; {-|<i>rate</i>[:<i>dmax</i>[:<i>umax</i>]]}</p>
<dl>
<dd>The minimum bandwidth this class should get, when the traffic load rises. If the sum of the rates in this column exceeds the INTERFACE&#8217;s OUT-BANDWIDTH, then the OUT-BANDWIDTH limit may not be honored. Similarly, if the sum of the rates of sub-classes of a class exceed the CEIL of the parent class, things don&#8217;t work well. When using the HFSC queuing discipline, this column specify the real-time (RT) service curve. leaf classes may specify <i>dmax</i>, the maximum delay in milliseconds that the first queued packet for this class should experience. May be expressed as an integer, optionally followed by &#8216;ms&#8217; with no intervening white-space (e.g., 10ms). HFSC leaf classes may also specify <i>umax</i>, the largest packet expected in this class. May be expressed as an integer. The unit of measure is <i>bytes</i> and the integer may be optionally followed by &#8216;b&#8217; with no intervening white-space (e.g., 800b). <i>umax</i> may only be given if <i>dmax</i> is also given. Beginning with Shorewall 4.5.6, HFSC classes may omit this column (e.g, &#8216;-&#8216; in the column), provided that an <i>lsrate</i> is specified (see CEIL below). These rates are used to arbitrate between classes of the same priority.</dl>
<p> <code>CEIL</code> &#8211; [<i>lsrate</i>:]<i>rate</i></p>
<dl>
<dd>The maximum bandwidth this class is allowed to use when the link is idle. Useful if you have traffic which can get full speed when more needed services (e.g. ssh) are not used. You can use the value <code>full</code> in here for setting the maximum bandwidth to the RATE of the parent class, or the OUT-BANDWIDTH of the device if there is no parent class. Beginning with Shorewall 4.5.6, you can also specify an <i>lsrate</i> (link sharing rate).</dl>
<p> <code>PRIORITY</code> &#8211; <i>priority</i></p>
<dl>
<dd>For HTB: The <i>priority</i> in which classes will be serviced by the packet shaping scheduler and also the priority in which bandwidth in excess of the rate will be given to each class. Higher priority classes will experience less delay since they are serviced first. Priority values are serviced in ascending order (e.g. 0 is higher priority than 1). Classes may be set to the same priority, in which case they will be serviced as equals. For both HTB and HFSC, the <i>priority</i> is used to calculate the priority of following Shorewall-generated classification filters that refer to the class:</p>
<dl>
<dd>&bull; Packet MARK</dl>
<dl>
<dd>&bull; <code>tcp-ack</code> and the <code>tos</code> options (see below)</dl>
<p> The rules for classes with lower numeric priorities will appear before those with higher numeric priorities. Beginning with Shorewall 4.5.8, the PRIORITY may be omitted from an HFSC class if you do not use the MARK column or the <code>tcp-ack</code> or <code>tos</code> options. If you use those features and omit the PRIORITY, then you must specify a <i>priority</i> along with the MARK or option.</dl>
<p> <code>OPTIONS</code> (Optional) &#8211; [<i>option</i>[<code>,</code><i>option</i>]&#8230;]</p>
<dl>
<dd>A comma-separated list of options including the following: <code>default</code></p>
<dl>
<dd>This is the default class for that interface where all traffic should go, that is not classified otherwise.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 You must define <code>default</code> for exactly one class per interface.  <code>tos=0x</code><i>value</i>[/0x<i>mask</i>][:<i>priority</i>] (mask defaults to 0xff)</p>
<dl>
<dd>This lets you define a classifier for the given <i>value</i>/<i>mask</i> combination of the IP packet&#8217;s TOS/Precedence/DiffSrv octet (aka the TOS byte). Beginning with Shorewall 4.5.8, the <i>value/mask</i> may be followed by a colon (&quot;:&quot;) and a <i>priority</i>. This priority determines the order in which filter rules are processed during packet classification. If not specified, the value (<i>class priority</i> &lt;&lt; 8) | 15) is used.</dl>
<p> <code>tos-</code><i>tosname</i>[:<i>priority</i>]</p>
<dl>
<dd>Aliases for the following TOS octet value and mask encodings. TOS encodings of the &quot;TOS byte&quot; have been deprecated in favor of diffserve classes, but programs like ssh, rlogin, and ftp still use them.</p>
<dl>
<dd>
<pre> <code>tos-minimize-delay</code> 0x10/0x10
 <code>tos-maximize-throughput</code> 0x08/0x08
 <code>tos-maximize-reliability</code> 0x04/0x04
 <code>tos-minimize-cost</code> 0x02/0x02
 <code>tos-normal-service</code> 0x00/0x1e</pre>
</dl>
<p> Beginning with Shorewall 4.5.8, the <i>tos-name</i> may be followed by a colon (&quot;:&quot;) and a <i>priority</i>. This priority determines the order in which filter rules are processed during packet classification. If not specified, the value (<i>class priority</i> &lt;&lt; 8) | 10) is used.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 Each of these options is only valid for ONE class per interface.  <code>tcp-ack</code>[:<i>priority</i>]</p>
<dl>
<dd>If defined, causes a tc filter to be created that puts all tcp ack packets on that interface that have a size of &lt;=64 Bytes to go in this class. This is useful for speeding up downloads. Please note that the size of the ack packets is limited to 64 bytes because we want only packets WITHOUT payload to match. Beginning with Shorewall 4.5.8, the <code>tcp-ack</code> may be followed by a colon (&quot;:&quot;) and a <i>priority</i>. This priority determines the order in which filter rules are processed during packet classification. If not specified, the value (<i>class priority</i> &lt;&lt; 8) | 10) is used.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 This option is only valid for ONE class per interface.  flow=<i>keys</i></p>
<dl>
<dd>Shorewall attaches an SFQ queuing discipline to each leaf HTB class. SFQ ensures that each flow gets equal access to the interface. The default definition of a flow corresponds roughly to a Netfilter connection. So if one internal system is running BitTorrent, for example, it can have lots of &#8216;flows&#8217; and can thus take up a larger share of the bandwidth than a system having only a single active connection. The <code>flow</code> classifier (module cls_flow) works around this by letting you define what a &#8216;flow&#8217; is. The classifier must be used carefully or it can block off all traffic on an interface! The flow option can be specified for an HTB leaf class (one that has no sub-classes). We recommend that you use the following:</p>
<dl>
<dd>Shaping internet-bound traffic:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>flow=nfct-src</dl>
<dl>
<dd>Shaping traffic bound for your local net:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>flow=dst</dl>
<p> These will cause a &#8216;flow&#8217; to consists of the traffic to/from each internal system. When more than one key is give, they must be enclosed in parenthesis and separated by commas. To see a list of the possible flow keys, run this command: <code>tc filter add flow help</code> Those that begin with &quot;nfct-&quot; are Netfilter connection tracking fields. As shown above, we recommend flow=nfct-src; that means that we want to use the source IP address <i>before NAT</i> as the key.</dl>
<p> pfifo</p>
<dl>
<dd>When specified for a leaf class, the pfifo queuing discipline is applied to the class rather than the sfq queuing discipline.</dl>
<p> limit=<i>number</i></p>
<dl>
<dd>Added in Shorewall 4.4.3. When specified for a leaf class, determines the maximum number of packets that may be queued within the class. The <i>number</i> must be &gt; 2 and &lt;= 128. If not specified, the value 127 is assumed.</dl>
<p> red=(<i>redoption</i>=<i>value</i>, &#8230;)</p>
<dl>
<dd>Added in Shorewall 4.5.6. When specified on a leaf class, causes the class to use the RED (Random Early Detection) queuing discipline rather than SFQ. See tc-red (8) for additional information. Allowable redoptions are: min <i>min</i></p>
<dl>
<dd>Average queue size at which marking becomes a possibility.</dl>
<p> max <i>max</i></p>
<dl>
<dd>At this average queue size, the marking probability is maximal. Must be at least twice <i>min</i> to prevent synchronous retransmits, higher for low <i>min</i>.</dl>
<p> probability <i>probability</i></p>
<dl>
<dd>Maximum probability for marking, specified as a floating point number from 0.0 to 1.0. Suggested values are 0.01 or 0.02 (1 or 2%, respectively).</dl>
<p> limit <i>limit</i></p>
<dl>
<dd>Hard limit on the real (not average) queue size in bytes. Further packets are dropped. Should be set higher than <i>max</i>+<i>burst</i>. It is advised to set this a few times higher than <i>max</i>. Shorewall requires that <i>limit</i> be at least twice <i>min</i>.</dl>
<p> burst <i>burst</i></p>
<dl>
<dd>Used for determining how fast the average queue size is influenced by the real queue size. Larger values make the calculation more sluggish, allowing longer bursts of traffic before marking starts. Real life experiments support the following guide-line: (<i>min</i>+<i>min</i>+<i>max</i>)/(3*<i>avpkt</i>).</dl>
<p> avpkt <i>avpkt</i></p>
<dl>
<dd>Optional. Specified in bytes. Used with burst to determine the time constant for average queue size calculations. 1000 is a good value and is the Shorewall default.</dl>
<p> bandwidth <i>bandwidth</i></p>
<dl>
<dd>Optional. This rate is used for calculating the average queue size after some idle time. Should be set to the bandwidth of your interface. Does not mean that RED will shape for you!</dl>
<p> ecn</p>
<dl>
<dd>RED can either &#8216;mark&#8217; or &#8216;drop&#8217;. Explicit Congestion Notification allows RED to notify remote hosts that their rate exceeds the amount of bandwidth available. Non-ECN capable hosts can only be notified by dropping a packet. If this parameter is specified, packets which indicate that their hosts honor ECN will only be marked and not dropped, unless the queue size hits <i>limit</i> bytes. Needs a tc binary with RED support compiled in. Recommended.</dl>
</dl>
<p> fq_codel[=(<i>codeloption</i>=<i>value</i>, &#8230;)]</p>
<dl>
<dd>Added in Shorewall 4.5.12. When specified for a leaf class, causes the class to use the FQ_CODEL (Fair-queuing Controlled-Delay) queuing discipline rather than SFQ. See tc-fq_codel (8) for additional information. Allowable <i>codeloptions</i> are: limit</p>
<dl>
<dd>hard limit on the real queue size. When this limit is reached, incoming packets are dropped. If the value is lowered, packets are dropped so that the new limit is met. Default is 1000 packets.</dl>
<p> flows</p>
<dl>
<dd>is the number of flows into which the incoming packets are classified. Due to the stochastic nature of hashing, multiple flows may end up being hashed into the same slot. Newer flows have priority over older ones. This parameter can be set only at load time since memory has to be allocated for the hash table. Default value is 1024.</dl>
<p> target</p>
<dl>
<dd>is the acceptable minimum standing/persistent queue delay. This minimum delay is identified by tracking the local minimum queue delay that packets experience. Default and recommended value is 5ms.</dl>
<p> interval</p>
<dl>
<dd>is used to ensure that the measured minimum delay does not become too stale. The minimum delay must be experienced in the last epoch of length interval. It should be set on the order of the worst-case RTT through the bottleneck to give endpoints sufficient time to react. Default value is 100ms.</dl>
<p> quantum</p>
<dl>
<dd>is the number of bytes used as &#8216;deficit&#8217; in the fair queuing algorithm. Default is set to 1514 bytes which corresponds to the Ethernet MTU plus the hardware header length of 14 bytes.</dl>
<p> ecn | noecn</p>
<dl>
<dd>can be used to mark packets instead of dropping them. If ecn has been enabled, noecn can be used to turn it off and vice-a-versa. By default, ecn is enabled.</dl>
</dl>
</dl>
<h2>Examples</h2>
<p>Example 1:</p>
<dl>
<dd>Suppose you are using PPP over Ethernet (DSL) and ppp0 is the interface for this. You have 4 classes here, the first you can use for voice over IP traffic, the second interactive traffic (e.g. ssh/telnet but not scp), the third will be for all unclassified traffic, and the forth is for low priority traffic (e.g. peer-to-peer). </p>
<p> The voice traffic in the first class will be guaranteed a minimum of 100kbps and always be serviced first (because of the low priority number, giving less delay) and will be granted excess bandwidth (up to 180kbps, the class ceiling) first, before any other traffic. A single VoIP stream, depending upon codecs, after encapsulation, can take up to 80kbps on a PPPoE/DSL link, so we pad a little bit just in case. (TOS byte values 0xb8 and 0x68 are DiffServ classes EF and AFF3-1 respectively and are often used by VOIP devices). </p>
<p> Interactive traffic (tos-minimum-delay) and TCP acks (and ICMP echo traffic if you use the example in tcrules) and any packet with a mark of 2 will be guaranteed 1/4 of the link bandwidth, and may extend up to full speed of the link. </p>
<p> Unclassified traffic and packets marked as 3 will be guaranteed 1/4th of the link bandwidth, and may extend to the full speed of the link. </p>
<p> Packets marked with 4 will be treated as low priority packets. (The tcrules example marks p2p traffic as such.) If the link is congested, they&#8217;re only guaranteed 1/8th of the speed, and even if the link is empty, can only expand to 80% of link bandwidth just as a precaution in case there are upstream queues we didn&#8217;t account for. This is the last class to get additional bandwidth and the last to get serviced by the scheduler because of the low priority. </p>
<dl>
<dd>
<pre> #INTERFACE MARK RATE CEIL PRIORITY OPTIONS
 ppp0 1 100kbit 180kbit 1 tos=0x68/0xfc,tos=0xb8/0xfc
 ppp0 2 full/4 full 2 tcp-ack,tos-minimize-delay
 ppp0 3 full/4 full 3 default
 ppp0 4 full/8 full*8/10 4</pre>
</dl>
</dl>
<h2>Files</h2>
<p>/etc/shorewall6/tcclasses</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/7-tc-hfsc/">tc-hfsc</a>(7) </p>
<p> <a href="/docs/linux/man/8-tc-red/">tc-red</a>(8) </p>
<p> m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/traffic_shaping.htm">http://www.shorewall.net/traffic_shaping.htm</a></code>m[]<font SIZE="-2">[3]</font> </p>
<p> m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></code>m[]<font SIZE="-2">[4]</font> </p>
<p> <a href="/docs/linux/man/8-shorewall6/">shorewall6</a>(8), <a href="/docs/linux/man/5-shorewall6-accounting/">shorewall6-accounting</a>(5), <a href="/docs/linux/man/5-shorewall6-actions/">shorewall6-actions</a>(5), <a href="/docs/linux/man/5-shorewall6-blacklist/">shorewall6-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall6-hosts/">shorewall6-hosts</a>(5), <a href="/docs/linux/man/5-shorewall6-interfaces/">shorewall6-interfaces</a>(5), <a href="/docs/linux/man/5-shorewall6-maclist/">shorewall6-maclist</a>(5), <a href="/docs/linux/man/5-shorewall6-netmap/">shorewall6-netmap</a>(5),<a href="/docs/linux/man/5-shorewall6-params/">shorewall6-params</a>(5), <a href="/docs/linux/man/5-shorewall6-policy/">shorewall6-policy</a>(5), <a href="/docs/linux/man/5-shorewall6-providers/">shorewall6-providers</a>(5), <a href="/docs/linux/man/5-shorewall6-rtrules/">shorewall6-rtrules</a>(5), <a href="/docs/linux/man/5-shorewall6-routestopped/">shorewall6-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall6-rules/">shorewall6-rules</a>(5), <a href="/docs/linux/man/5-shorewall6-conf/">shorewall6.conf</a>(5), <a href="/docs/linux/man/5-shorewall6-secmarks/">shorewall6-secmarks</a>(5), <a href="/docs/linux/man/5-shorewall6-tcdevices/">shorewall6-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall6-mangle/">shorewall6-mangle</a>(5), <a href="/docs/linux/man/5-shorewall6-tos/">shorewall6-tos</a>(5), <a href="/docs/linux/man/5-shorewall6-tunnels/">shorewall6-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall6-zones/">shorewall6-zones</a>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>shorewall6-tcdevices</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6-tcdevices.html">http://www.shorewall.net/manpages6/shorewall6-tcdevices.html</a></dl>
<dt> 2.</p>
<dd>shorewall-mangle</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-mangle.html">http://www.shorewall.net/manpages/shorewall-mangle.html</a></dl>
<dt> 3.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/traffic_shaping.htm">http://www.shorewall.net/traffic_shaping.htm</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/traffic_shaping.htm">http://www.shorewall.net/traffic_shaping.htm</a></dl>
<dt> 4.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></dl>
