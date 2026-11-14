---
title: "astraceroute(8)"
name: "astraceroute"
section: "8"
letter: "a"
url: "/docs/linux/man/8-astraceroute/"
description: "astraceroute – autonomous system trace route utility"
---

<p>astraceroute &#8211; autonomous system trace route utility </p>
<h2>Synopsis</h2>
<p><code>astraceroute</code> [<i>options</i>] </p>
<h2>Description</h2>
<p>astraceroute is a small utility to retrieve path information in a traceroute like way, but with additional geographical location information. It tracks the route of a packet from the local host to the remote host by successively increasing the IP&#8217;s TTL field, starting from 1, in the hope that each intermediate node will send an ICMP TIME_EXCEEDED notification back to the local host when the TTL value is decremented to 0. astraceroute supports IPv4 and IPv6 queries and will display country and city information, if available, the AS number the hop belongs to, and its ISP name. astraceroute also displays timing information and reverse DNS data. Due to astraceroute&#8217;s configurability, it is also possible to gather some more useful information about the hop regarding what it does and does not allow to pass through. This is done by using clear text strings for probing DPIs or keywords. This tool might be a good start for further in-depth analysis of such systems. </p>
<h2>Options</h2>
<h3>-H &lt;host&gt;, &#8211;host &lt;host&gt;</h3>
<p>Hostname or IPv4 or IPv6 address of the remote host where the AS route should be traced to. In the case of an IPv6 address or host, option &#8221;-6&#8221; must be used. IPv4 is the default.</p>
<h3>-p &lt;port&gt;, &#8211;port &lt;port&gt;</h3>
<p>TCP port for the remote host to use. If not specified, the default port used is 80.</p>
<h3>-i &lt;device&gt;, -d &lt;device&gt;, &#8211;dev &lt;device&gt;</h3>
<p>Networking device to start the trace route from, e.g. eth0, wlan0.</p>
<h3>-f &lt;ttl&gt;, &#8211;init-ttl &lt;ttl&gt;</h3>
<p>Initial TTL value to be used. This option might be useful if you are not interested in the first n hops, but only the following ones. The default initial TTL value is 1.</p>
<h3>-m &lt;ttl&gt;, &#8211;max-ttl &lt;ttl&gt;</h3>
<p>Maximum TTL value to be used. If not otherwise specified, the maximum TTL value is 30. Thus, after this has been reached astraceroute exits.</p>
<h3>-q &lt;num&gt;, &#8211;num-probes &lt;num&gt;</h3>
<p>Specifies the number of queries to be done on a particular hop. The default is 2 query requests.</p>
<h3>-x &lt;sec&gt;, &#8211;timeout &lt;sec&gt;</h3>
<p>Tells astraceroute the probe response timeout in seconds, in other words the maximum time astraceroute must wait for an ICMP response from the current hop. The default is 3 seconds.</p>
<h3>-X &lt;string&gt;, &#8211;payload &lt;string&gt;</h3>
<p>Places an ASCII cleartext string into the packet payload. Cleartext that contains whitespace must be put into quotes (e.g.: &quot;censor me&quot;).</p>
<h3>-l &lt;len&gt;, &#8211;totlen &lt;len&gt;</h3>
<p>Specifies the total length of the packet. Payload that does not have a cleartext string in it is padded with random garbage.</p>
<h3>-4, &#8211;ipv4</h3>
<p>Use IPv4 only requests. This is the default.</p>
<h3>-6, &#8211;ipv6</h3>
<p>Use IPv6 only requests. This must be used when passing an IPv6 host as an argument.</p>
<h3>-n, &#8211;numeric</h3>
<p>Tells astraceroute to not perform reverse DNS lookup for hop replies. The reverse option is &#8221;-N&#8221;.</p>
<h3>-u, &#8211;update</h3>
<p>The built-in geo-database update mechanism will be invoked to get Maxmind&#8217;s latest version. To configure search locations for databases, the file /etc/netsniff-ng/geoip.conf contains possible addresses. Thus, to save bandwidth or for mirroring Maxmind&#8217;s databases (to bypass their traffic limit policy), different hosts or IP addresses can be placed into geoip.conf, separated by a newline.</p>
<h3>-L, &#8211;latitude</h3>
<p>Also show latitude and longitude of hops.</p>
<h3>-N, &#8211;dns</h3>
<p>Tells astraceroute to perform reverse DNS lookup for hop replies. The reverse option is &#8221;-n&#8221;.</p>
<h3>-S, &#8211;syn</h3>
<p>Use TCP&#8217;s SYN flag for the request.</p>
<h3>-A, &#8211;ack</h3>
<p>Use TCP&#8217;s ACK flag for the request.</p>
<h3>-F, &#8211;fin</h3>
<p>Use TCP&#8217;s FIN flag for the request.</p>
<h3>-P, &#8211;psh</h3>
<p>Use TCP&#8217;s PSH flag for the request.</p>
<h3>-U, &#8211;urg</h3>
<p>Use TCP&#8217;s URG flag for the request.</p>
<h3>-R, &#8211;rst</h3>
<p>Use TCP&#8217;s RST flag for the request.</p>
<h3>-E, &#8211;ecn-syn</h3>
<p>Use TCP&#8217;s ECN flag for the request.</p>
<h3>-t &lt;tos&gt;, &#8211;tos &lt;tos&gt;</h3>
<p>Explicitly specify IP&#8217;s TOS.</p>
<h3>-G, &#8211;nofrag</h3>
<p>Set IP&#8217;s no fragmentation flag.</p>
<h3>-Z, &#8211;show-packet</h3>
<p>Show and dissect the returned packet.</p>
<h3>-v, &#8211;version</h3>
<p>Show version information and exit.</p>
<h3>-h, &#8211;help</h3>
<p>Show user help and exit.</p>
<h2>Usage Example</h2>
<h3>astraceroute -i eth0 -N -S -H netsniff-ng.org</h3>
<p>This sends out a TCP SYN probe via the &#8221;eth0&#8221; networking device to the remote IPv4 host netsniff-ng.org. This request is most likely to pass. Also, tell astraceroute to perform reverse DNS lookups for each hop.</p>
<h3>astraceroute -6 -i eth0 -S -E -N -H <a rel="nofollow" href="http://www.6bone.net">www.6bone.net</a></h3>
<p>In this example, a TCP SYN/ECN probe for the IPv6 host <a rel="nofollow" href="http://www.6bone.net">www.6bone.net</a> is being performed. Also in this case, the &#8221;eth0&#8221; device is being used as well as a reverse DNS lookup for each hop.</p>
<h3>astraceroute -i eth0 -N -F -H netsniff-ng.org</h3>
<p>Here, we send out a TCP FIN probe to the remote host netsniff-ng.org. Again, on each hop a reverse DNS lookup is being done and the queries are transmitted from &#8221;eth0&#8221;. IPv4 is used.</p>
<h3>astraceroute -i eth0 -N -FPU -H netsniff-ng.org</h3>
<p>As in most other examples, we perform a trace route to IPv4 host netsniff-ng.org and do a TCP Xmas probe this time.</p>
<h3>astraceroute -i eth0 -N -H netsniff-ng.org -X censor-me -Z</h3>
<p>In this example, we have a Null probe to the remote host netsniff-ng.org, port 80 (default) and this time, we append the cleartext string &quot;censor-me&quot; into the packet payload to test if a firewall or DPI will let this string pass. Such a trace could be done once without, and once with, a blacklisted string to gather possible information about censorship.</p>
<h2>Note</h2>
<p>If a TCP-based probe fails after a number of retries, astraceroute will automatically fall back to ICMP-based probes to pass through firewalls and routers used in load balancing for example. </p>
<p> To gather more information about astraceroute&#8217;s displayed AS numbers, see e.g.: <a rel="nofollow" href="http://bgp.he.net/AS">http://bgp.he.net/AS</a>&lt;number&gt;.</p>
<h2>Bugs</h2>
<p>The geographical locations are estimated with the help of Maxmind&#8217;s GeoIP database and can differ from the real physical location. To decrease the possible errors, update the database regularly using astraceroute&#8217;s &#8211;update option. At some point in time, we need a similar approach to gather more reliable path information such as in the paris-traceroute tool. Due to the generic nature of astraceroute, it currently has a built-in mechanism to stop the trace after a fixed number of hops, since the configurable TCP flags can have anything included. It is possible to decrease this number of course. In the future, if a SYN probe is sent out, there should be a listener so that we can stop the trace if we detect a handshake in progress. </p>
<h2>Legal</h2>
<p>astraceroute is licensed under the GNU GPL version 2.0.</p>
<h2>History</h2>
<p><code>astraceroute</code> was originally written for the netsniff-ng toolkit by Daniel Borkmann. It is currently maintained by Tobias Klauser &lt;tklauser [at] distanz.ch&gt; and Daniel Borkmann &lt;dborkma [at] tik.ee.ethz.ch&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-netsniff-ng/">netsniff-ng</a></code>(8), <code><a href="/docs/linux/man/8-trafgen/">trafgen</a></code>(8), <code><a href="/docs/linux/man/8-mausezahn/">mausezahn</a></code>(8), <code><a href="/docs/linux/man/8-ifpps/">ifpps</a></code>(8), <code><a href="/docs/linux/man/8-bpfc/">bpfc</a></code>(8), <code><a href="/docs/linux/man/8-flowtop/">flowtop</a></code>(8), <code><a href="/docs/linux/man/8-curvetun/">curvetun</a></code>(8) </p>
<h2>Author</h2>
<p>Manpage was written by Daniel Borkmann.</p>
<h2>Colophon</h2>
<p>This page is part of the Linux netsniff-ng toolkit project. A description of the project, and information about reporting bugs, can be found at <a rel="nofollow" href="http://netsniff-ng.org/.">http://netsniff-ng.org/.</a> </p>
