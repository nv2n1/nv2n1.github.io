---
title: "flow-tools-examples(1)"
name: "flow-tools-examples"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flow-tools-examples/"
description: "flow-tools-examples – Example usage of flow-tools."
---

<h2>NAME</h2>
<p> flow-tools-examples &#8211; Example usage of flow-tools.</p>
<h2>EXAMPLE &#8211; CONFIGURING CISCO IOS ROUTER</h2>
<p> NetFlow is configured on each input interface, then global commands are used to specify the export destination. To ensure a consistant source address address Loopback0 is configured as the export source. </p>
<pre>
ip cef distributed
ip flow-export version 5 origin-as
ip flow-export destination 10.0.0.100 5004
ip flow-export source Loopback0
interface Loopback0
 ip address 10.1.1.1 255.255.255.255
interface FastEthernet0/1/0 
 ip address 10.0.0.1 255.255.255.0
 no ip directed-broadcast
 ip route-cache flow
 ip route-cache distributed
</pre>
<p> Many other options exist such as aggregated NetFlow and sampled NetFlow which are detailed at &lt;URL:<a rel="nofollow" href="http://www.cisco.com">http://www.cisco.com</a>&gt;.</p>
<h2>EXAMPLE &#8211; CONFIGURING CISCO CATIOS SWITCH</h2>
<p> Some Cisco Catalyst switches support a different implementation of NetFlow that is performed on the supervisor. With the cache based forwarding model which is implemented in the Catalyst 55xx with Route Switch Module (RSM) and NetFlow Feature Card (NFFC), the RSM processes the first flow and the remaining packets in the flow are forwarded by the Supervisor. This is also implemented in the early versions of the 65xx with MSFC. The deterministic forwarding model used in the 65xx with MSFC2 do not use NetFlow to determine the forwarding path, the flow cache is only used for statistics as in the current IOS implementations. In all of of the above configurations flow exports arrive from both the RSM/MSFC and the Supervisor engines as distinct streams. In the worst cast the RSM exports in version 5 and the Supervisor exports in version 7. Fortunately flow-capture and flow-receive can sort all this out by processing flows from both sources and converting them to a common export format. </p>
<p> The router side running IOS is configured identically to the example given above. The CatIOS NetFlow Data Export configuration follows: </p>
<pre>
set mls flow full
set mls nde version 7
set mls nde 10.0.0.1 9800
set mls nde enable
</pre>
<p> When the 65xx is running in Native mode, from a users perspective the switch is only running IOS. </p>
<p> More detailed examples can be found on Cisco&#8217;s web site<br />
&nbsp;<wbr>&lt;URL:<a rel="nofollow" href="http://www.cisco.com">http://www.cisco.com</a>&gt;.</p>
<h2>EXAMPLE &#8211; CONFIGURING JUNIPER ROUTER</h2>
<p> Juniper supports flow exports by the routing engine sampling packet headers and aggregating them into flows. Packet sampling is done by defining a firewall filter to accept and sample all traffic, applying that rule to the interface, then configuring the sampling forwarding option. </p>
<pre><code>
interfaces
{
    ge - 0 / 3 / 0
    {
        unit 0
        {
            family inet
            {
                filter
                {
                    input all;
                    output all;
                }
                address 10.0.0.1 / 24;
            }
        }
    }
    firewall
    {
        filter all
        {
            term all
            {
                then
                {
                    sample;
                    accept;
                }
            }
        }
    }
    forwarding - options
    {
        sampling
        {
            input
            {
                family inet
                {
                    rate 100;
                }
            }
            output
            {
                cflowd 10.0.0.100
                {
                    port 9800;
                    version 5;
                }
            }
        }
    }
</code></pre>
<p> Other options exist such as aggregated flows which are detailed at &lt;URL:<a rel="nofollow" href="http://www.juniper.net">http://www.juniper.net</a>&gt;.</p>
<h2>EXAMPLE &#8211; NETWORK TOPOLOGY AND FLOW.ACL</h2>
<p> The network topology and flow.acl will be used for many of the examples that follow. Flows are collected and stored in <i>/flows/R</i>. </p>
<pre><code>
ISP - A ISP - B + + + +IP = 10.1.2.1 / 24 + +IP = 10.1.1.1 / 24 ifIndex = 2 + +ifIndex = 1 interface = serial1 / 1 + +interface = serial0 / 0 -- -- - | R | Campus Router-- -- -+ +IP = 10.1.4.1 / 24 + +IP = 10.1.3.1 / 24 ifIndex = 4 + +ifIndex = 3 interface = Ethernet1 / 1 + +interface = Ethernet0 / 0 + +Sales Marketing
</code></pre>
<pre>
ip access-list standard sales permit 10.1.4.0 0.0.0.255
ip access-list standard not_sales deny 10.1.4.0 0.0.0.255
ip access-list standard marketing permit 10.1.3.0 0.0.0.255
ip access-list standard not_marketing deny 10.1.3.0 0.0.0.255
ip access-list standard campus permit 10.1.4.0 0.0.0.255
ip access-list standard campus permit 10.1.3.0 0.0.0.255
ip access-list standard not_campus deny 10.1.4.0 0.0.0.255
ip access-list standard not_campus deny 10.1.3.0 0.0.0.255
ip access-list standard evil_hacket permit host 10.6.6.6
ip access-list standard spoofer permit host 10.9.9.9
ip access-list standard multicast 224.0.0.0 15.255.255.255
</pre>
<h2>EXAMPLE &#8211; FINDING SPOOFED ADDRESSES</h2>
<p> A common problem on the Internet is the use of &quot;spoofed&quot; (addresses that are not assigned to an organization) for use in DoS attacks or compromising servers that rely on the source IP address for authentication. </p>
<p> Display all flow records that originate from the campus and are sent to the Internet but are not using legal addresses. </p>
<p> <code>flow-cat /flows/R | flow-filter -Snot_campus -I1,2 | flow-print</code> </p>
<p> Summary of the destinations of the internally spoofed addresses sorted by octets. </p>
<p> <code>flow-cat /flows/R | flow-filter -Snot_campus -I1,2 | flow-stat -f8 -S2</code> </p>
<p> Summary of the sources of the internally spoofed addresses sorted by flows. </p>
<p> <code>flow-cat /flows/R | flow-filter -Snot_campus -I1,2 | flow-stat -f9 -S1</code> </p>
<p> Summary of the internally spoofed sources and destination pairs sorted by packets. </p>
<p> <code>flow-cat /flows/R | flow-filter -Snot_campus -I1,2 | flow-stat -f10 -S4</code> </p>
<p> Display all flow records that originate external to the campus that have campus addresses. Many times these can be attackers trying to exploit host based authentication mechanisms like unix r* commands. Another common source is mobile clients which send packets with their campus addresses before obtaining a valid IP. </p>
<p> <code>flow-cat /flows/R | flow-filter -Scampus -i1,2 | flow-print</code> </p>
<p> Summary of the destinations of the externally spoofed addresses sorted by octets. </p>
<p> <code>flow-cat /flows/R | flow-filter -Scampus -i1,2 | flow-stat -f8 -S2</code></p>
<h2>EXAMPLE &#8211; LOCATE HOSTS USING OR RUNNING SERVICES</h2>
<p> Find all SMTP servers active during the collection period that have established connections to the Internet. Summarize sorted by octets. </p>
<p> <code>flow-cat /flows/R | flow-filter -I1,2 -P25 | flow-stat -f9 -S2</code> </p>
<p> Find all outbound NNTP connections to the Internet. Summarize with source and destination IP sorted by octets. </p>
<p> <code>flow-cat /flows/R | flow-filter -I1,2 -P119 | flow-stat -f10 -S3</code> </p>
<p> Find all inbound NNTP connections to the Internet. Summarize with source and destination IP sorted by octets. </p>
<p> <code>flow-cat /flows/R | flow-filter -i1,2 -P119 | flow-stat -f10 -S3</code></p>
<h2>EXAMPLE &#8211; MULTICAST USAGE</h2>
<p> Summarize Multicast S,G where sources are on campus. </p>
<p> <code>flow-cat /flows/R | flow-filter -Dmulticast -I1,2 | flow-stat -f10 -S3</code> </p>
<p> Summarize Multicast S,G where sources are off campus. </p>
<p> <code>flow-cat /flows/R | flow-filter -Dmulticast -i1,2 | flow-stat -f10 -S3</code></p>
<h2>EXAMPLE &#8211; FIND SCANNERS</h2>
<p> Find SMTP scanners with flow-dscan. This will also find SMTP clients which try to contact many servers. This behavior is characterized by a recent Microsoft worm. </p>
<pre>
<code>touch dscan.suppress.src dscan.suppress.dst</code>
<code>flow-cat /flows/R | flow-filter -P25 | flow-dscan -b</code>
</pre>
<h2>AUTHOR</h2>
<p> Mark Fullmer &lt;maf [at] splintered.net&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flow-tools/">flow-tools</a></code>(1) </p>
<h2>Index</h2>
