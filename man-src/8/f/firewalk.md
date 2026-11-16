---
title: "firewalk(8)"
name: "firewalk"
section: "8"
letter: "f"
url: "/docs/linux/man/8-firewalk/"
description: "firewalk – Active Reconnaissance Network Security Tool with Extreme Prejudice"
---

<p>firewalk &#8211; Active Reconnaissance Network Security Tool with Extreme Prejudice</p>
<h2>Synopsis</h2>
<p><code>firewalk</code> [-dhinprSsTtvx] target_gateway metric<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></p>
<h2>Description</h2>
<p>Firewalk is an active reconnaissance network security tool that attempts to determine what layer 4 protocols a given IP forwarding device will pass. Firewalk works by sending out TCP or UDP packets with a TTL one greater than the targeted gateway. If the gateway allows the traffic, it will forward the packets to the next hop where they will expire and elicit an ICMP_TIME_EXCEEDED message. If the gateway hostdoes not allow the traffic, it will likely drop the packets on the floor and we will see no response. To get the correct IP TTL that will result in expired packets one beyond the gateway we need to ramp up hop-counts. We do this in the same manner that traceroute works. Once we have the gateway hopcount (at that point the scan is said to be `bound`) we can begin our scan. It is significant to note the fact that the ultimate destination host does not have to be reached. It just needs to be somewhere downstream, on the other side of the gateway, from the scanning host. Please see <a rel="nofollow" href="http://www.wiley.com/cda/product/0,,0471205443,00.html">http://www.wiley.com/cda/product/0,,0471205443,00.html</a> for more information on Firewalking and networking security tools in general. </p>
<h2>Command-Line Options</h2>
<p>If an option takes an argument, it procedes the option letter, with the default in parenthesis.</p>
<dl>
<dt><code>-d 1-65535 (34434)</code></dt>
<dd>Specify the initial destination port to use during the network discovery (aka TTL ramping) phase.</dd>
<dt><code>-h</code></dt>
<dd>Program help.</dd>
<dt><code>-i interface_name</code></dt>
<dd>Specify interface to use. Only neccessary on multi-homed machines.</dd>
<dt><code>-n</code></dt>
<dd>Do not resolve IP addresses into hostnames. This saves a DNS lookup and speeds the scans (mainly during network discovery).</dd>
<dt><code>-P 1-2000 (0)</code></dt>
<dd>Set a network writing pause which may be neccessary to keep the program from flooding the network.</dd>
<dt><code>-p TCP, UDP (UDP)</code></dt>
<dd>Type of scan to perform.</dd>
<dt><code>-r</code></dt>
<dd>Strict RFC 793 compliance. This only comes into play when doing a TCP scan when your packets have an expire vector of one and your metric host is one hop from your gateway. Since the packets will reach their destination, they will not expire, so we look for terminal responses. For a TCP port in the listen state, we will get back a SYN|ACK with the ACK as our SEQ + 1. However, for a closed port, the response is stack dependent. If the host is RFC compliant we will receive an RST|ACK with the ACK as our SEQ + 1. However, if the host is not compliant (ie: microsoft) then the best we can do is inverse tuple matching (which is the default).</dd>
<dt><code>-S 1-65535,&#8230; (1-130,139,1025)</code></dt>
<dd>Specify the ports for the scan. Ports may be specified in ranges, delimited by dashes, and multiple ranges may be specified, delimited by commas. Ommiting the terminating port number is shorthand for 65535.</dd>
<dt><code>-s 1-65535 (53)</code></dt>
<dd>Specify the source port for the scan (both phases).</dd>
<dt><code>-T 1-2000 (2)</code></dt>
<dd>Network packet reading timeout. This is the time firewalk will spend waiting for a response before timing out.</dd>
<dt><code>-t 1-25 (1)</code></dt>
<dd>Set the initial IP time to live (TTL) value. If a target gateway is known to be (at least) n hops from the source host, the TTL can be preloaded to facilitate a faster scan.</dd>
<dt><code>-v</code></dt>
<dd>Dump program version and exit.</dd>
<dt><code>-x expire vector (1)</code></dt>
<dd>The expire vector is the number of hops that the scanning probes will expire, past the gateway host. The binding hopcount is the hopcount of the gateway + the expire vector.</dd>
<dd></dd></dl>
<h2>Command-Line Examples</h2>
<h2>Caveats</h2>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-traceroute/">traceroute</a>(8), tracerx(8), pcap(3), libnet(3), dnet(3)</p>
<h2>Author</h2>
<p>Mike D. Schiffman &lt;mike [at] infonexus.com&gt;</p>
<h2>Bugs</h2>
<p>Please send bug reports to mike [at] infonexus.com </p>
