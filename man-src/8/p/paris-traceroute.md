---
title: "paris-traceroute(8)"
name: "paris-traceroute"
section: "8"
letter: "p"
url: "/docs/linux/man/8-paris-traceroute/"
description: "paris-traceroute – print the IP-level routes between two Internet hosts."
---

<p>paris-traceroute &#8211; print the IP-level routes between two Internet hosts.</p>
<h2>Synopsis</h2>
<p><code>paris-traceroute</code> [ <code>-fhilnqvV</code> ] [ <code>-b</code> <i>initial_id</i> ] </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <code>-d</code> <i>dest_port</i> ] [ <code>-a</code> <i>algorithm</i> ] [ <code>-f</code> <i>first_ttl</i> ] </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <code>-L</code> <i>packetlen</i> ] [ <code>-m</code> <i>max_ttl</i> ] </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <code>-M</code> <i>max_missing_hops</i> ] [ <code>-p</code> <i>protocol</i> ] </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <code>-q</code> <i>nqueries</i> ] [ <code>-s</code> <i>source_port</i> ] [ <code>-t</code> <i>tos</i> ] </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <code>-T</code> <i>delaymsecs</i> ] [ <code>-w</code> <i>waittime</i> ] </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> <i>host</i></p>
<h2>Description</h2>
<p>Paris traceroute is a new version of the well-known network diagnosis tool. It addresses problems caused by load balancers with the initial <i><a href="/docs/linux/man/8-traceroute/">traceroute</a></i>(8) implementation. By controlling the flow identifier of the probes, it is able to follow accurate paths in networks with load balancers. It is also able to find all the load balanced paths to the destination. Finally, it enriches its output with information extracted from the received packets, allowing a more precise analysis of the discovered paths. Options are:</p>
<dl>
<dt><code>-a</code></p>
<dd>Set the probing algorithm:</p>
<dt><font SIZE="-1"><code>hopbyhop</code> </font></p>
<dd>Send q (configured with the <code>-q</code> flag) probes with the same TTL, then wait for all the replies or a timeout. Increment the TTL and reiter the operation until we reach the destination. All packets hold the same flow identifier.</p>
<dt><font SIZE="-1"><code>packetbypacket</code> </font></p>
<dd>It is the classic <i><a href="/docs/linux/man/8-traceroute/">traceroute</a></i>(8) algorithm: send one probe at a time, then wait for a reply or a timeout. Reiter the operation until we reach the destination.</p>
<dt><font SIZE="-1"><code>concurrent</code> </font></p>
<dd>Send all the probes from min_ttl to max_ttl and wait for all replies or a timeout.</p>
<dt><font SIZE="-1"><code>scout</code> </font></p>
<dd>Send a scout probe with a ttl max to the destination. If the destination can be reached, compute the number of hops used to reach the destination and start the concurrent algorithm with a max_ttl equal to this number of hops. If the destination cannot be reached, the hopbyhop algorithm will be used instead. This algorithm is only usable with UDP probes.</p>
<dt><font SIZE="-1"><code>exhaustive</code> </font></p>
<dd>Print all the possible &quot;load balanced&quot; paths to the destination. (See section <code>EXHAUSTIVE ALGORITHM</code> )</p>
<dt><code>-b</code></p>
<dd>Set the initial probe identifier.</p>
<dt><code>-d</code></p>
<dd>Set the the UDP/TCP destination port (default: 33457).</p>
<dt><code>-f</code></p>
<dd>Set the initial ttl (default: 1).</p>
<dt><code>-h</code></p>
<dd>Print help.</p>
<dt><code>-i</code></p>
<dd>Print the &quot;IP Identifier&quot; value of the responses. It is used to identify the different interfaces of a router, or uncover NAT boxes.</p>
<dt><code>-l</code></p>
<dd>Display the ttl value of the reply. Useful to study asymmetric routing and NAT boxes.</p>
<dt><code>-L</code></p>
<dd>Set the data length to be used in outgoing packets. (default: 0).</p>
<dt><code>-m</code></p>
<dd>Set the maximum ttl (default: 30).</p>
<dt><code>-M</code></p>
<dd>Set the maximum number of consecutive unresponsive hops which causes the program to abort (default 3).</p>
<dt><code>-n</code></p>
<dd>Print hop addresses numerically. The default is to print also hostnames.</p>
<dt><code>-p</code></p>
<dd>Set the protocol to use (possible values: udp, tcp, icmp).</p>
<dt><code>-q</code></p>
<dd>Set the number of probes per hop (default: 3).</p>
<dt><code>-s</code></p>
<dd>Set the UDP/TCP source port (default: 33456).</p>
<dt><code>-t</code></p>
<dd>Set the Type of Service (default: 0). This field is taken into account by many per-flow load balancers: in presence of such a load balancer, packets having different TOS values are likely to follow a different paths.</p>
<dt><code>-T</code></p>
<dd>Set the time to wait between probes, in milliseconds (default 50ms).</p>
<dt><code>-v</code></p>
<dd>Print debug messages.</p>
<dt><code>-V</code></p>
<dd>Print the program version.</p>
<dt><code>-w</code></p>
<dd>Set the time to wait for a response, in milliseconds (default 5000ms). </p>
<h2>Exhaustive Algorithm</h2>
<p>With the deployment of load balancing, there is no longer only one path between two Internet hosts. This algorithm sends enough probes at each hop to find all the possible interfaces. Unlike the other algorithms, it varies the flow identifier of the probes in a controlled manner, to ensure the discovery of all the interfaces with a high confidence degree. It also categorizes load balancers as &quot;per-packet&quot; (pseudo-random, round-robin packet balancing) or &quot;per-flow&quot; (packets belonging to the same flow follow the same path). </p>
<p> In case of per-flow load balancing, it prints additional information to track flows. The following trace shows the enriched output: </p>
<dl>
<dd>
<pre>14 1.1.1.1:0,1,3 539.065 ms 1.1.1.2:2,4,5 492.152 ms
15 2.2.2.2:0,1,3 563.163 ms 2.2.2.3:2,4,5 470.919 ms</pre>
</dl>
<p> Integers listed after the interface addresses are &quot;flow identifiers&quot;: they are used to identify a flow in the set of interfaces found by the algorithm. For example, flow #0 traverses interfaces 1.1.1.1 and 2.2.2.2. This is the same for flows 1 and 3 while flows 2, 4 and 5 traverse 1.1.1.2 and 2.2.2.3.</p>
<h2>Output</h2>
<p>The following information are extracted from the response packets and displayed: </p>
<dl>
<dt><code>Response TTL</code></p>
<dd>The TTL of the responses (from the routers and the destination) is optionally displayed in square brackets (Use the <code>-l flag</code> ).</p>
<dt><code>Original TTL</code></p>
<dd>This is the TTL of the probe when it was received and dropped by the router. If the original TTL is different than 1, it is displayed with a <i>!Tx</i> symbol, where <i>x</i> is the value of the TTL. For example, <i>!T0 </i> indicates that the value of the TTL was 0 when the probe reached the router that discarded it.</p>
<dt><code>IP Identifier </code></p>
<dd>This the identifier of the IP error packet sent by the router. This field is set with the value of an internal 16-bit counter usually incremented for each packet sent. This value is optionally displayed inside brackets. For instance <i>{1234}</i> indicates that the probe had its identifier set to 1234.</p>
<dt><code>MPLS labels</code></p>
<dd>If the packet contains ICMP extensions for MPLS, the MPLS label stack is diplayed in an additionnal line just after the current hop line. Labels of the same stack are separated with a &quot;|&quot; character.</p>
<dt><code>Other ICMP error messages</code></p>
<dd>Paris traceroutes uses the same convensions as <i><a href="/docs/linux/man/8-traceroute/">traceroute</a></i>(8) to display unexpected ICMP messages (i.e. different than TIME_EXCEEDED, PORT_UNREACHABLE and ECHO_REPLY).</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-traceroute/">traceroute</a>(8), <a href="/docs/linux/man/8-pathchar/">pathchar</a>(8), <a href="/docs/linux/man/1-netstat/">netstat</a>(1), <a href="/docs/linux/man/8-ping/">ping</a>(8)</p>
<h2>Author</h2>
<p>The initial version of <i><a href="/docs/linux/man/8-traceroute/">traceroute</a></i>(8) was implemented by Van Jacobson from a suggestion by Steve Deering. Paris traceroute was implemented by Xavier Cuvellier. Debugged and enhanced by Brice Augustin. </p>
<p> The current version is available at: </p>
<dl>
<dd><i><a rel="nofollow" href="http://www.paris-traceroute.net">http://www.paris-traceroute.net</a></i></dl>
<h2>Bugs</h2>
<p>Please send bug reports to brice.augustin [at] rp.lip6.fr. </p>
