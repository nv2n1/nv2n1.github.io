---
title: "nping(1)"
name: "nping"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nping/"
description: "nping – Network packet generation tool / ping utility"
---

<h2 class="name">NAME</h2>
<p> nping &#8211; Network packet generation tool / ping utility </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>nping</code> [<i>Options</i>] {<i>targets</i>}</dl>
<h2>DESCRIPTION</h2>
<dd>Nping is an open-source tool for network packet generation, response analysis and response time measurement. Nping allows users to generate network packets of a wide range of protocols, letting them tune virtually any field of the protocol headers. While Nping can be used as a simple ping utility to detect active hosts, it can also be used as a raw packet generator for network stack stress tests, ARP poisoning, Denial of Service attacks, route tracing, and other purposes. </p>
<p> Additionally, Nping offers a special mode of operation called the &quot;Echo Mode&quot;, that lets users see how the generated probes change in transit, revealing the differences between the transmitted packets and the packets received at the other end. See section &quot;Echo Mode&quot; for details. </p>
<p> The output from Nping is a list of the packets that are being sent and received. The level of detail depends on the options used. </p>
<p> A typical Nping execution is shown in Example 1. The only Nping arguments used in this example are <code>-c</code>, to specify the number of times to target each host, <code>&#8211;tcp</code> to specify TCP Probe Mode, <code>-p 80,433</code> to specify the target ports; and then the two target hostnames. </p>
<p> <code>Example 1. A representative Nping execution</code> </p>
<dl>
<dt>
<dd>
<pre>
# <code>nping -c 1 --tcp -p 80,433 scanme.nmap.org google.com</code>
Starting Nping ( <a rel="nofollow" href="https://nmap.org/nping">https://nmap.org/nping</a> )
SENT (0.0120s) TCP 96.16.226.135:50091 &gt; 64.13.134.52:80 S ttl=64 id=52072 iplen=40  seq=1077657388 win=1480 
RCVD (0.1810s) TCP 64.13.134.52:80 &gt; 96.16.226.135:50091 SA ttl=53 id=0 iplen=44  seq=4158134847 win=5840 &lt;mss 1460&gt;
SENT (1.0140s) TCP 96.16.226.135:50091 &gt; 74.125.45.100:80 S ttl=64 id=13932 iplen=40  seq=1077657388 win=1480 
RCVD (1.1370s) TCP 74.125.45.100:80 &gt; 96.16.226.135:50091 SA ttl=52 id=52913 iplen=44  seq=2650443864 win=5720 &lt;mss 1430&gt;
SENT (2.0140s) TCP 96.16.226.135:50091 &gt; 64.13.134.52:433 S ttl=64 id=8373 iplen=40  seq=1077657388 win=1480 
SENT (3.0140s) TCP 96.16.226.135:50091 &gt; 74.125.45.100:433 S ttl=64 id=23624 iplen=40  seq=1077657388 win=1480 
Statistics for host scanme.nmap.org (64.13.134.52):
 |  Probes Sent: 2 | Rcvd: 1 | Lost: 1  (50.00%)
 |_ Max rtt: 169.720ms | Min rtt: 169.720ms | Avg rtt: 169.720ms
Statistics for host google.com (74.125.45.100):
 |  Probes Sent: 2 | Rcvd: 1 | Lost: 1  (50.00%)
 |_ Max rtt: 122.686ms | Min rtt: 122.686ms | Avg rtt: 122.686ms
Raw packets sent: 4 (160B) | Rcvd: 2 (92B) | Lost: 2 (50.00%)
Tx time: 3.00296s | Tx bytes/s: 53.28 | Tx pkts/s: 1.33
Rx time: 3.00296s | Rx bytes/s: 30.64 | Rx pkts/s: 0.67
Nping done: 2 IP addresses pinged in 4.01 seconds
</pre>
</dl>
<p> The newest version of Nping can be obtained with Nmap at m[blue]<code><a rel="nofollow" href="https://nmap.org">https://nmap.org</a></code>m[]. The newest version of this man page is available at m[blue]<code><a rel="nofollow" href="https://nmap.org/book/nping-man.html">https://nmap.org/book/nping-man.html</a></code>m[]. </p>
<p> &#8211;&gt;<br />
&nbsp;<wbr>&nbsp;.SH&nbsp;&quot;OPTIONS SUMMARY&quot; </p>
<p> This options summary is printed when Nping is run with no arguments. It helps people remember the most common options, but is no substitute for the in-depth documentation in the rest of this manual. Some obscure options aren&#8217;t even included here. </p>
<dl>
<dt>
<dd>
<pre><code>
Nping 0.5.59BETA1 ( https://nmap.org/nping )
Usage: nping [Probe mode] [Options] {target specification}
TARGET SPECIFICATION:
  Targets may be specified as hostnames, IP addresses, networks, etc.
  Ex: scanme.nmap.org, microsoft.com/24, 192.168.0.1; 10.0.0-255.1-254
PROBE MODES:
  --tcp-connect                    : Unprivileged TCP connect probe mode.
  --tcp                            : TCP probe mode.
  --udp                            : UDP probe mode.
  --icmp                           : ICMP probe mode.
  --arp                            : ARP/RARP probe mode.
  --tr, --traceroute               : Traceroute mode (can only be used with 
                                     TCP/UDP/ICMP modes).
TCP CONNECT MODE:
   -p, --dest-port &lt;port spec&gt;     : Set destination port(s).
   -g, --source-port &lt;portnumber&gt;  : Try to use a custom source port.
TCP PROBE MODE:
   -g, --source-port &lt;portnumber&gt;  : Set source port.
   -p, --dest-port &lt;port spec&gt;     : Set destination port(s).
   --seq &lt;seqnumber&gt;               : Set sequence number.
   --flags &lt;flag list&gt;             : Set TCP flags (ACK,PSH,RST,SYN,FIN...)
   --ack &lt;acknumber&gt;               : Set ACK number.
   --win &lt;size&gt;                    : Set window size.
   --badsum                        : Use a random invalid checksum. 
UDP PROBE MODE:
   -g, --source-port &lt;portnumber&gt;  : Set source port.
   -p, --dest-port &lt;port spec&gt;     : Set destination port(s).
   --badsum                        : Use a random invalid checksum. 
ICMP PROBE MODE:
  --icmp-type &lt;type&gt;               : ICMP type.
  --icmp-code &lt;code&gt;               : ICMP code.
  --icmp-id &lt;id&gt;                   : Set identifier.
  --icmp-seq &lt;n&gt;                   : Set sequence number.
  --icmp-redirect-addr &lt;addr&gt;      : Set redirect address.
  --icmp-param-pointer &lt;pnt&gt;       : Set parameter problem pointer.
  --icmp-advert-lifetime &lt;time&gt;    : Set router advertisement lifetime.
  --icmp-advert-entry &lt;IP,pref&gt;    : Add router advertisement entry.
  --icmp-orig-time  &lt;timestamp&gt;    : Set originate timestamp.
  --icmp-recv-time  &lt;timestamp&gt;    : Set receive timestamp.
  --icmp-trans-time &lt;timestamp&gt;    : Set transmit timestamp.
ARP/RARP PROBE MODE:
  --arp-type &lt;type&gt;                : Type: ARP, ARP-reply, RARP, RARP-reply.
  --arp-sender-mac &lt;mac&gt;           : Set sender MAC address.
  --arp-sender-ip  &lt;addr&gt;          : Set sender IP address.
  --arp-target-mac &lt;mac&gt;           : Set target MAC address.
  --arp-target-ip  &lt;addr&gt;          : Set target IP address.
IPv4 OPTIONS:
  -S, --source-ip                  : Set source IP address.
  --dest-ip &lt;addr&gt;                 : Set destination IP address (used as an 
                                     alternative to {target specification} ). 
  --tos &lt;tos&gt;                      : Set type of service field (8bits).
  --id  &lt;id&gt;                       : Set identification field (16 bits).
  --df                             : Set Don't Fragment flag.
  --mf                             : Set More Fragments flag.
  --ttl &lt;hops&gt;                     : Set time to live [0-255].
  --badsum-ip                      : Use a random invalid checksum. 
  --ip-options &lt;S|R [route]|L [route]|T|U ...&gt; : Set IP options
  --ip-options &lt;hex string&gt;                    : Set IP options
  --mtu &lt;size&gt;                     : Set MTU. Packets get fragmented if MTU is
                                     small enough.
IPv6 OPTIONS:
  -6, --IPv6                       : Use IP version 6.
  --dest-ip                        : Set destination IP address (used as an
                                     alternative to {target specification}).
  --hop-limit                      : Set hop limit (same as IPv4 TTL).
  --traffic-class &lt;class&gt; :        : Set traffic class.
  --flow &lt;label&gt;                   : Set flow label.
ETHERNET OPTIONS:
  --dest-mac &lt;mac&gt;                 : Set destination mac address. (Disables
                                     ARP resolution)
  --source-mac &lt;mac&gt;               : Set source MAC address.
  --ether-type &lt;type&gt;              : Set EtherType value.
PAYLOAD OPTIONS:
  --data &lt;hex string&gt;              : Include a custom payload.
  --data-string &lt;text&gt;             : Include a custom ASCII text.
  --data-length &lt;len&gt;              : Include len random bytes as payload.
ECHO CLIENT/SERVER:
  --echo-client &lt;passphrase&gt;       : Run Nping in client mode.
  --echo-server &lt;passphrase&gt;       : Run Nping in server mode.
  --echo-port &lt;port&gt;               : Use custom &lt;port&gt; to listen or connect.
  --no-crypto                      : Disable encryption and authentication.
  --once                           : Stop the server after one connection.
  --safe-payloads                  : Erase application data in echoed packets.
TIMING AND PERFORMANCE:
  Options which take &lt;time&gt; are in seconds, or append 'ms' (milliseconds),
  's' (seconds), 'm' (minutes), or 'h' (hours) to the value (e.g. 30m, 0.25h).
  --delay &lt;time&gt;                   : Adjust delay between probes.
  --rate  &lt;rate&gt;                   : Send num packets per second.
MISC:
  -h, --help                       : Display help information.
  -V, --version                    : Display current version number. 
  -c, --count &lt;n&gt;                  : Stop after &lt;n&gt; rounds.
  -e, --interface &lt;name&gt;           : Use supplied network interface.
  -H, --hide-sent                  : Do not display sent packets.
  -N, --no-capture                 : Do not try to capture replies.
  --privileged                     : Assume user is fully privileged.
  --unprivileged                   : Assume user lacks raw socket privileges.
  --send-eth                       : Send packets at the raw ethernet layer.
  --send-ip                        : Send packets using raw IP sockets.
  --bpf-filter &lt;filter spec&gt;       : Specify custom BPF filter.
OUTPUT:
  -v                               : Increment verbosity level by one.
  -v[level]                        : Set verbosity level. E.g: -v4
  -d                               : Increment debugging level by one.
  -d[level]                        : Set debugging level. E.g: -d3
  -q                               : Decrease verbosity level by one.
  -q[N]                            : Decrease verbosity level N times
  --quiet                          : Set verbosity and debug level to minimum.
  --debug                          : Set verbosity and debug to the max level.
EXAMPLES:
  nping scanme.nmap.org
  nping --tcp -p 80 --flags rst --ttl 2 192.168.1.1
  nping --icmp --icmp-type time --delay 500ms 192.168.254.254
  nping --echo-server "public" -e wlan0 -vvv 
  nping --echo-client "public" echo.nmap.org --tcp -p1-1024 --flags ack
SEE THE MAN PAGE FOR MANY MORE OPTIONS, DESCRIPTIONS, AND EXAMPLES
</code></pre>
</dl>
<h2>TARGET SPECIFICATION</h2>
<p> Everything on the Nping command line that isn&#8217;t an option or an option argument is treated as a target host specification. Nping uses the same syntax for target specifications that Nmap does. The simplest case is a single target given by IP address or hostname. </p>
<p> Nping supports CIDR-style addressing. You can append /<i>numbits</i> to an IPv4 address or hostname and Nping will send probes to every IP address for which the first <i>numbits</i> are the same as for the reference IP or hostname given. For example, 192.168.10.0/24 would send probes to the 256 hosts between 192.168.10.0 (binary: 11000000 10101000 00001010 00000000) and 192.168.10.255 (binary: 11000000 10101000 00001010 11111111), inclusive. 192.168.10.40/24 would ping exactly the same targets. Given that the host scanme.nmap.org is at the IP address 64.13.134.52, the specification scanme.nmap.org/16 would send probes to the 65,536 IP addresses between 64.13.0.0 and 64.13.255.255. The smallest allowed value is /0, which targets the whole Internet. The largest value is /32, which targets just the named host or IP address because all address bits are fixed. </p>
<p> CIDR notation is short but not always flexible enough. For example, you might want to send probes to 192.168.0.0/16 but skip any IPs ending with .0 or .255 because they may be used as subnet network and broadcast addresses. Nping supports this through octet range addressing. Rather than specify a normal IP address, you can specify a comma-separated list of numbers or ranges for each octet. For example, 192.168.0-255.1-254 will skip all addresses in the range that end in .0 or .255, and 192.168.3-5,7.1 will target the four addresses 192.168.3.1, 192.168.4.1, 192.168.5.1, and 192.168.7.1. Either side of a range may be omitted; the default values are 0 on the left and 255 on the right. Using &#8211; by itself is the same as 0-255, but remember to use 0- in the first octet so the target specification doesn&#8217;t look like a command-line option. Ranges need not be limited to the final octets: the specifier 0-.-.13.37 will send probes to all IP addresses on the Internet ending in .13.37. This sort of broad sampling can be useful for Internet surveys and research. </p>
<p> IPv6 addresses can only be specified by their fully qualified IPv6 address or hostname. CIDR and octet ranges aren&#8217;t supported for IPv6 because they are rarely useful. </p>
<p> Nping accepts multiple host specifications on the command line, and they don&#8217;t need to be the same type. The command <code>nping scanme.nmap.org 192.168.0.0/8 10.0.0,1,3-7.-</code> does what you would expect.</p>
<h2>OPTION SPECIFICATION</h2>
<p> Nping is designed to be very flexible and fit a wide variety of needs. As with most command-line tools, its behavior can be adjusted using command-line options. These general principles apply to option arguments, unless stated otherwise. </p>
<p> Options that take integer numbers can accept values specified in decimal, octal or hexadecimal base. When a number starts with 0x, it will be treated as hexadecimal; when it simply starts with 0, it will be treated as octal. Otherwise, Nping will assume the number has been specified in base 10. Virtually all numbers that can be supplied from the command line are unsigned so, as a general rule, the minimum value is zero. Users may also specify the word random or rand to make Nping generate a random value within the expected range. </p>
<p> IP addresses may be given as IPv4 addresses (e.g. 192.168.1.1), IPv6 addresses (e.g. 2001:db8:85a3::8e4c:760:7146), or hostnames, which will be resolved using the default DNS server configured in the host system. </p>
<p> Options that take MAC addresses accept the usual colon-separated 6 hex byte format (e.g. 00:50:56:d4:01:98). Hyphens may also be used instead of colons (e.g. 00-50-56-c0-00-08). The special word random or rand sets a random address and the word broadcast or bcast sets ff:ff:ff:ff:ff:ff.</p>
<h2>GENERAL OPERATION</h2>
<p> Unlike other ping and packet generation tools, Nping supports multiple target host and port specifications. While this provides great flexibility, it is not obvious how Nping handles situations where there is more than one host and/or more than one port to send probes to. This section explains how Nping behaves in these cases. </p>
<p> When multiple target hosts are specified, Nping rotates among them in round-robin fashion. This gives slow hosts more time to send their responses before another probe is sent to them. Ports are also scheduled using round robin. So, unless only one port is specified, Nping never sends two probes to the same target host and port consecutively. </p>
<p> The loop around targets is the &#8220;inner loop&#8221; and the loop around ports is the &#8220;outer loop&#8221;. All targets will be sent a probe for a given port before moving on to the next port. Between probes, Nping waits a configurable amount of time called the &#8220;inter-probe delay&#8221;, which is controlled by the <code>&#8211;delay</code> option. These examples show how it works. </p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
# <code>nping --tcp -c 2 1.1.1.1 -p 100-102</code>
Starting Nping ( <a rel="nofollow" href="https://nmap.org/nping">https://nmap.org/nping</a> )
SENT (0.0210s) TCP 192.168.1.77 &gt; 1.1.1.1:100
SENT (1.0230s) TCP 192.168.1.77 &gt; 1.1.1.1:101
SENT (2.0250s) TCP 192.168.1.77 &gt; 1.1.1.1:102
SENT (3.0280s) TCP 192.168.1.77 &gt; 1.1.1.1:100
SENT (4.0300s) TCP 192.168.1.77 &gt; 1.1.1.1:101
SENT (5.0320s) TCP 192.168.1.77 &gt; 1.1.1.1:102
</pre>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
# <code>nping --tcp -c 2 1.1.1.1 2.2.2.2 3.3.3.3 -p 8080</code>
Starting Nping ( <a rel="nofollow" href="https://nmap.org/nping">https://nmap.org/nping</a> )
SENT (0.0230s) TCP 192.168.0.21 &gt; 1.1.1.1:8080
SENT (1.0240s) TCP 192.168.0.21 &gt; 2.2.2.2:8080
SENT (2.0260s) TCP 192.168.0.21 &gt; 3.3.3.3:8080
SENT (3.0270s) TCP 192.168.0.21 &gt; 1.1.1.1:8080
SENT (4.0290s) TCP 192.168.0.21 &gt; 2.2.2.2:8080
SENT (5.0310s) TCP 192.168.0.21 &gt; 3.3.3.3:8080
</pre>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
# <code>nping --tcp -c 1 --delay 500ms 1.1.1.1 2.2.2.2 3.3.3.3 -p 137-139</code>
Starting Nping ( <a rel="nofollow" href="https://nmap.org/nping">https://nmap.org/nping</a> )
SENT (0.0230s) TCP 192.168.0.21 &gt; 1.1.1.1:137
SENT (0.5250s) TCP 192.168.0.21 &gt; 2.2.2.2:137
SENT (1.0250s) TCP 192.168.0.21 &gt; 3.3.3.3:137
SENT (1.5280s) TCP 192.168.0.21 &gt; 1.1.1.1:138
SENT (2.0280s) TCP 192.168.0.21 &gt; 2.2.2.2:138
SENT (2.5310s) TCP 192.168.0.21 &gt; 3.3.3.3:138
SENT (3.0300s) TCP 192.168.0.21 &gt; 1.1.1.1:139
SENT (3.5330s) TCP 192.168.0.21 &gt; 2.2.2.2:139
SENT (4.0330s) TCP 192.168.0.21 &gt; 3.3.3.3:139
</pre>
</dl>
</dl>
<h2>PROBE MODES</h2>
<p> Nping supports a wide variety of protocols. Although in some cases Nping can automatically determine the mode from the options used, it is generally a good idea to specify it explicitly. </p>
<p> <code>&#8211;tcp-connect</code> (TCP Connect mode)</p>
<dl>
<dt>
<dd> TCP connect mode is the default mode when a user does not have raw packet privileges. Instead of writing raw packets as most other modes do, Nping asks the underlying operating system to establish a connection with the target machine and port by issuing the connect system call. This is the same high-level system call that web browsers, P2P clients, and most other network-enabled applications use to establish a connection. It is part of a programming interface known as the Berkeley Sockets API. Rather than read raw packet responses off the wire, Nping uses this API to obtain status information on each connection attempt. For this reason, you will not be able to see the contents of the packets that are sent or received but only status information about the TCP connection establishment taking place.</dl>
<p> <code>&#8211;tcp</code> (TCP mode)</p>
<dl>
<dt>
<dd> TCP is the mode that lets users create and send any kind of TCP packet. TCP packets are sent embedded in IP packets that can also be tuned. This mode can be used for many different purposes. For example you could try to discover open ports by sending TCP SYN messages without completing the three-way handshake. This technique is often referred to as half-open scanning, because you don&#8217;t open a full TCP connection. You send a SYN packet, as if you are going to open a real connection and then wait for a response. A SYN/ACK indicates the port is open, while a RST indicates it&#8217;s closed. If no response is received one could assume that some intermediate network device is filtering the responses. Another use could be to see how a remote TCP/IP stack behaves when it receives a non-RFC-compliant packet, like one with both SYN and RST flags set. One could also do some evil by creating custom RST packets using an spoofed IP address with the intent of closing an active TCP connection.</dl>
<p> <code>&#8211;udp</code> (UDP mode)</p>
<dl>
<dt>
<dd> UDP mode can have two different behaviours. Under normal circumstances, it lets users create custom IP/UDP packets. However, if Nping is run by a user without raw packet privileges and no changes to the default protocol headers are requested, then Nping enters the unprivileged UDP mode which basically sends UDP packets to the specified target hosts and ports using the sendto system call. Note that in this unprivileged mode it is not possible to see low-level header information of the packets on the wire but only status information about the amount of bytes that are being transmitted and received. UDP mode can be used to interact with any UDP-based server. Examples are DNS servers, streaming servers, online gaming servers, and port knocking/single-packet authorization daemons.</dl>
<p> <code>&#8211;icmp</code> (ICMP mode)</p>
<dl>
<dt>
<dd> ICMP mode is the default mode when the user runs Nping with raw packet privileges. Any kind of ICMP message can be created. The default ICMP type is Echo, i.e., ping. ICMP mode can be used for many different purposes, from a simple request for a timestamp or a netmask to the transmission of fake destination unreachable messages, custom redirects, and router advertisements.</dl>
<p> <code>&#8211;arp</code> (ARP/RARP mode)</p>
<dl>
<dt>
<dd> ARP lets you create and send a few different ARP-related packets. These include ARP, RARP, DRARP, and InARP requests and replies. This mode can ban be used to perform low-level host discovery, and conduct ARP-cache poisoning attacks.</dl>
<p> <code>&#8211;traceroute</code> (Traceroute mode)</p>
<dl>
<dt>
<dd> Traceroute is not a mode by itself but a complement to TCP, UDP, and ICMP modes. When this option is specified Nping will set the IP TTL value of the first probe to 1. When the next router receives the packet it will drop it due to the expiration of the TTL and it will generate an ICMP destination unreachable message. The next probe will have a TTL of 2 so now the first router will forward the packet while the second router will be the one that drops the packet and generates the ICMP message. The third probe will have a TTL value of 3 and so on. By examining the source addresses of all those ICMP Destination Unreachable messages it is possible to determine the path that the probes take until they reach their final destination.</dl>
<h2>TCP CONNECT MODE</h2>
<p> <code>-p </code><i>port_spec</i>, <code>&#8211;dest-port </code><i>port_spec</i> (Target ports)</p>
<dl>
<dt>
<dd> This option specifies which ports you want to try to connect to. It can be a single port, a comma-separated list of ports (e.g. 80,443,8080), a range (e.g. 1-1023), and any combination of those (e.g. 21-25,80,443,1024-2048). The beginning and/or end values of a range may be omitted, causing Nping to use 1 and 65535, respectively. So you can specify -p- to target ports from 1 through 65535. Using port zero is allowed if you specify it explicitly.</dl>
<p> <code>-g </code><i>portnumber</i>, <code>&#8211;source-port </code><i>portnumber</i> (Spoof source port)</p>
<dl>
<dt>
<dd> This option asks Nping to use the specified port as source port for the TCP connections. Note that this might not work on all systems or may require root privileges. Specified value must be an integer in the range [0-65535].</dl>
<h2>TCP MODE</h2>
<p> <code>-p </code><i>port_spec</i>, <code>&#8211;dest-port </code><i>port_spec</i> (Target ports)</p>
<dl>
<dt>
<dd> This option specifies which destination ports you want to send probes to. It can be a single port, a comma-separated list of ports (e.g. 80,443,8080), a range (e.g. 1-1023), and any combination of those (e.g. 21-25,80,443,1024-2048). The beginning and/or end values of a range may be omitted, causing Nping to use 1 and 65535, respectively. So you can specify -p- to target ports from 1 through 65535. Using port zero is allowed if you specify it explicitly.</dl>
<p> <code>-g </code><i>portnumber</i>, <code>&#8211;source-port </code><i>portnumber</i> (Spoof source port)</p>
<dl>
<dt>
<dd> This option asks Nping to use the specified port as source port for the TCP connections. Note that this might not work on all systems or may require root privileges. Specified value must be an integer in the range [0-65535].</dl>
<p> <code>&#8211;seq </code><i>seqnumber</i> (Sequence Number)</p>
<dl>
<dt>
<dd> Specifies the TCP sequence number. In SYN packets this is the initial sequence number (ISN). In a normal transmission this corresponds to the sequence number of the first byte of data in the segment. <i>seqnumber</i> must be a number in the range [0-4294967295].</dl>
<p> <code>&#8211;flags </code><i>flags</i> (TCP Flags)</p>
<dl>
<dt>
<dd> This option specifies which flags should be set in the TCP packet. <i>flags</i> may be specified in three different ways: </p>
<dl>
<dt>
<dd> 1. As a comma-separated list of flags, e.g. <code>&#8211;flags syn,ack,rst</code></dl>
<dl>
<dt>
<dd> 2. As a list of one-character flag initials, e.g. <code>&#8211;flags SAR</code> tells Nping to set flags SYN, ACK, and RST.</dl>
<dl>
<dt>
<dd> 3. As an 8-bit hexadecimal number, where the supplied number is the exact value that will be placed in the flags field of the TCP header. The number should start with the prefix 0x and should be in the range [0x00-0xFF], e.g. &#8211;flags 0x20 sets the URG flag as 0x20 corresponds to binary 00100000 and the URG flag is represented by the third bit.</dl>
<p> There are 8 possible flags to set: CWR, ECN, URG, ACK, PSH, RST, SYN, and FIN. The special value ALL means to set all flags. NONE means to set no flags. It is important that if you don&#8217;t want any flag to be set, you request it explicitly because in some cases the SYN flag may be set by default. Here is a brief description of the meaning of each flag: </p>
<p> CWR (Congestion Window Reduced)</p>
<dl>
<dt>
<dd> Set by an ECN-Capable sender when it reduces its congestion window (due to a retransmit timeout, a fast retransmit or in response to an ECN notification.</dl>
<p> ECN (Explicit Congestion Notification)</p>
<dl>
<dt>
<dd> During the three-way handshake it indicates that sender is capable of performing explicit congestion notification. Normally it means that a packet with the IP Congestion Experienced flag set was received during normal transmission. See RFC 3168 for more information.</dl>
<p> URG (Urgent)</p>
<dl>
<dt>
<dd> Segment is urgent and the urgent pointer field carries valid information.</dl>
<p> ACK (Acknowledgement)</p>
<dl>
<dt>
<dd> The segment carries an acknowledgement and the value of the acknowledgement number field is valid and contains the next sequence number that is expected from the receiver.</dl>
<p> PSH (Push)</p>
<dl>
<dt>
<dd> The data in this segment should be immediately pushed to the application layer on arrival.</dl>
<p> RST (Reset)</p>
<dl>
<dt>
<dd> There was some problem and the sender wants to abort the connection.</dl>
<p> SYN (Synchronize)</p>
<dl>
<dt>
<dd> The segment is a request to synchronize sequence numbers and establish a connection. The sequence number field contains the sender&#8217;s initial sequence number.</dl>
<p> FIN (Finish)</p>
<dl>
<dt>
<dd> The sender wants to close the connection.</dl>
</dl>
<p> <code>&#8211;win </code><i>size</i> (Window Size)</p>
<dl>
<dt>
<dd> Specifies the TCP window size, this is, the number of octets the sender of the segment is willing to accept from the receiver at one time. This is usually the size of the reception buffer that the OS allocates for a given connection. <i>size</i> must be a number in the range [0-65535].</dl>
<p> <code>&#8211;badsum</code> (Invalid Checksum)</p>
<dl>
<dt>
<dd> Asks Nping to use an invalid TCP checksum for the packets sent to target hosts. Since virtually all host IP stacks properly drop these packets, any responses received are likely coming from a firewall or an IDS that didn&#8217;t bother to verify the checksum. For more details on this technique, see m[blue]<code><a rel="nofollow" href="https://nmap.org/p60-12.html">https://nmap.org/p60-12.html</a></code>m[].</dl>
<h2>UDP MODE</h2>
<p> <code>-p </code><i>port_spec</i>, <code>&#8211;dest-port </code><i>port_spec</i> (Target ports)</p>
<dl>
<dt>
<dd> This option specifies which ports you want UDP datagrams to be sent to. It can be a single port, a comma-separated list of ports (e.g. 80,443,8080), a range (e.g. 1-1023), and any combination of those (e.g. 21-25,80,443,1024-2048). The beginning and/or end values of a range may be omitted, causing Nping to use 1 and 65535, respectively. So you can specify -p- to target ports from 1 through 65535. Using port zero is allowed if you specify it explicitly.</dl>
<p> <code>-g </code><i>portnumber</i>, <code>&#8211;source-port </code><i>portnumber</i> (Spoof source port)</p>
<dl>
<dt>
<dd> This option asks Nping to use the specified port as source port for the transmitted datagrams. Note that this might not work on all systems or may require root privileges. Specified value must be an integer in the range [0-65535].</dl>
<p> <code>&#8211;badsum</code> (Invalid Checksum)</p>
<dl>
<dt>
<dd> Asks Nping to use an invalid UDP checksum for the packets sent to target hosts. Since virtually all host IP stacks properly drop these packets, any responses received are likely coming from a firewall or an IDS that didn&#8217;t bother to verify the checksum. For more details on this technique, see m[blue]<code><a rel="nofollow" href="https://nmap.org/p60-12.html">https://nmap.org/p60-12.html</a></code>m[].</dl>
<h2>ICMP MODE</h2>
<p> <code>&#8211;icmp-type </code><i>type</i> (ICMP type)</p>
<dl>
<dt>
<dd> This option specifies which type of ICMP messages should be generated. <i>type</i> can be supplied in two different ways. You can use the m[blue]<code>official type numbers assigned by IANA</code>m[]<font SIZE="-2">[1]</font> (e.g. <code>&#8211;icmp-type 8</code> for ICMP Echo Request), or you can use any of the mnemonics listed in the section called &#8220;ICMP Types&#8221;.</dl>
<p> <code>&#8211;icmp-code </code><i>code</i> (ICMP code)</p>
<dl>
<dt>
<dd> This option specifies which ICMP code should be included in the generated ICMP messages. <i>code</i> can be supplied in two different ways. You can use the m[blue]<code>official code numbers assigned by IANA</code>m[]<font SIZE="-2">[1]</font> (e.g. <code>&#8211;icmp-code 1</code> for Fragment Reassembly Time Exceeded), or you can use any of the mnemonics listed in the section called &#8220;ICMP Codes&#8221;.</dl>
<p> <code>&#8211;icmp-id </code><i>id</i> (ICMP identifier)</p>
<dl>
<dt>
<dd> This option specifies the value of the identifier used in some of the ICMP messages. In general it is used to match request and reply messages. <i>id</i> must be a number in the range [0-65535].</dl>
<p> <code>&#8211;icmp-seq </code><i>seq</i> (ICMP sequence)</p>
<dl>
<dt>
<dd> This option specifies the value of the sequence number field used in some ICMP messages. In general it is used to match request and reply messages. <i>id</i> must be a number in the range [0-65535].</dl>
<p> <code>&#8211;icmp-redirect-addr </code><i>addr</i> (ICMP Redirect address)</p>
<dl>
<dt>
<dd> This option sets the address field in ICMP Redirect messages. In other words, it sets the IP address of the router that should be used when sending IP datagrams to the original destination. <i>addr</i> can be either an IPv4 address or a hostname.</dl>
<p> <code>&#8211;icmp-param-pointer </code><i>pointer</i> (ICMP Parameter Problem pointer)</p>
<dl>
<dt>
<dd> This option specifies the pointer that indicates the location of the problem in ICMP Parameter Problem messages. <i>pointer</i> should be a number in the range [0-255]. Normally this option is only used when ICMP code is set to 0 (&quot;Pointer indicates the error&quot;).</dl>
<p> <code>&#8211;icmp-advert-lifetime </code><i>ttl</i> (ICMP Router Advertisement Lifetime)</p>
<dl>
<dt>
<dd> This option specifies the router advertisement lifetime, this is, the number of seconds the information carried in an ICMP Router Advertisement can be considered valid for. <i>ttl</i> must be a positive integer in the range [0-65535].</dl>
<p> <code>&#8211;icmp-advert-entry </code><i>addr</i><code>,</code><i>pref</i> (ICMP Router Advertisement Entry)</p>
<dl>
<dt>
<dd> This option adds a Router Advertisement entry to an ICMP Router Advertisement message. The parameter must be two values separated by a comma. <i>addr</i> is the router&#8217;s IP and can be specified either as an IP address in dot-decimal notation or as a hostname. <i>pref</i> is the preference level for the specified IP. It must be a number in the range [0-4294967295]. An example is <code>&#8211;icmp-advert-entry 192.168.128.1,3</code>.</dl>
<p> <code>&#8211;icmp-orig-time </code><i>timestamp</i> (ICMP Originate Timestamp)</p>
<dl>
<dt>
<dd> This option sets the Originate Timestamp in ICMP Timestamp messages. The Originate Timestamp is expressed as the number of milliseconds since midnight UTC and it corresponds to the time the sender last touched the Timestamp message before its transmission. <i>timestamp</i> can be specified as a regular time (e.g. 10s, 3h, 1000ms), or the special string now. You can add or subtract values from now, for example <code>&#8211;icmp-orig-time now-2s</code>, <code>&#8211;icmp-orig-time now+1h</code>, <code>&#8211;icmp-orig-time now+200ms</code>.</dl>
<p> <code>&#8211;icmp-recv-time </code><i>timestamp</i> (ICMP Receive Timestamp)</p>
<dl>
<dt>
<dd> This option sets the Receive Timestamp in ICMP Timestamp messages. The Receive Timestamp is expressed as the number of milliseconds since midnight UTC and it corresponds to the time the echoer first touched the Timestamp message on receipt. <i>timestamp</i> is as with <code>&#8211;icmp-orig-time</code>.</dl>
<p> <code>&#8211;icmp-trans-time </code><i>timestamp</i> (ICMP Transmit Timestamp)</p>
<dl>
<dt>
<dd> This option sets the Transmit Timestamp in ICMP Timestamp messages. The Transmit Timestamp is expressed as the number of milliseconds since midnight UTC and it corresponds to the time the echoer last touched the Timestamp message before its transmission. <i>timestamp</i> is as with <code>&#8211;icmp-orig-time</code>.</dl>
<h3>ICMP Types</h3>
<p> These identifiers may be used as mnemonics for the ICMP type numbers given to the <code>&#8211;icmp-type</code> option. In general there are three forms of each identifier: the full name (e.g. destination-unreachable), the short name (e.g. dest-unr), or the initials (e.g. du). In ICMP types that request something, the word &quot;request&quot; is omitted. </p>
<p> echo-reply, echo-rep, er</p>
<dl>
<dt>
<dd> Echo Reply (type 0). This message is sent in response to an Echo Request message.</dl>
<p> destination-unreachable, dest-unr, du</p>
<dl>
<dt>
<dd> Destination Unreachable (type 3). This message indicates that a datagram could not be delivered to its destination.</dl>
<p> source-quench, sour-que, sq</p>
<dl>
<dt>
<dd> Source Quench (type 4). This message is used by a congested IP device to tell other device that is sending packets too fast and that it should slow down.</dl>
<p> redirect, redi, r</p>
<dl>
<dt>
<dd> Redirect (type 5). This message is normally used by routers to inform a host that there is a better route to use for sending datagrams. See also the <code>&#8211;icmp-redirect-addr</code> option.</dl>
<p> echo-request, echo, e</p>
<dl>
<dt>
<dd> Echo Request (type 8). This message is used to test the connectivity of another device on a network.</dl>
<p> router-advertisement, rout-adv, ra</p>
<dl>
<dt>
<dd> Router Advertisement (type 9). This message is used by routers to let hosts know of their existence and capabilities. See also the <code>&#8211;icmp-advert-lifetime</code> option.</dl>
<p> router-solicitation, rout-sol, rs</p>
<dl>
<dt>
<dd> Router Solicitation (type 10). This message is used by hosts to request Router Advertisement messages from any listening routers.</dl>
<p> time-exceeded, time-exc, te</p>
<dl>
<dt>
<dd> Time Exceeded (type 11). This message is generated by some intermediate device (normally a router) to indicate that a datagram has been discarded before reaching its destination because the IP TTL expired.</dl>
<p> parameter-problem, member-pro, pp</p>
<dl>
<dt>
<dd> Parameter Problem (type 12). This message is used when a device finds a problem with a parameter in an IP header and it cannot continue processing it. See also the <code>&#8211;icmp-param-pointer</code> option.</dl>
<p> timestamp, time, tm</p>
<dl>
<dt>
<dd> Timestamp Request (type 13). This message is used to request a device to send a timestamp value for propagation time calculation and clock synchronization. See also the <code>&#8211;icmp-orig-time</code>, <code>&#8211;icmp-recv-time</code>, and <code>&#8211;icmp-trans-time</code>.</dl>
<p> timestamp-reply, time-rep, tr</p>
<dl>
<dt>
<dd> Timestamp Reply (type 14). This message is sent in response to a Timestamp Request message.</dl>
<p> information, info, i</p>
<dl>
<dt>
<dd> Information Request (type 15). This message is now obsolete but it was originally used to request configuration information from another device.</dl>
<p> information-reply, info-rep, ir</p>
<dl>
<dt>
<dd> Information Reply (type 16). This message is now obsolete but it was originally sent in response to an Information Request message to provide configuration information.</dl>
<p> mask-request, mask, m</p>
<dl>
<dt>
<dd> Address Mask Request (type 17). This message is used to ask a device to send its subnet mask.</dl>
<p> mask-reply, mask-rep, mr</p>
<dl>
<dt>
<dd> Address Mask Reply (type 18). This message contains a subnet mask and is sent in response to a Address Mask Request message.</dl>
<p> traceroute, trace, tc</p>
<dl>
<dt>
<dd> Traceroute (type 30). This message is normally sent by an intermediate device when it receives an IP datagram with a traceroute option. ICMP Traceroute messages are still experimental, see RFC 1393 for more information.</dl>
<h3>ICMP Codes</h3>
<p> These identifiers may be used as mnemonics for the ICMP code numbers given to the <code>&#8211;icmp-code</code> option. They are listed by the ICMP type they correspond to. </p>
<p> <font SIZE="+1"> <code>Destination Unreachable</code></p>
<dl>
<dt>
<dd>
<p> network-unreachable, netw-unr, net</p>
<dl>
<dt>
<dd> Code 0. Datagram could not be delivered to its destination network (probably due to some routing problem).</dl>
<p> host-unreachable, host-unr, host</p>
<dl>
<dt>
<dd> Code 1. Datagram was delivered to the destination network but it was impossible to reach the specified host (probably due to some routing problem).</dl>
<p> protocol-unreachable, prot-unr, proto</p>
<dl>
<dt>
<dd> Code 2. The protocol specified in the Protocol field of the IP datagram is not supported by the host to which the datagram was delivered.</dl>
<p> port-unreachable, port-unr, port</p>
<dl>
<dt>
<dd> Code 3. The TCP/UDP destination port was invalid.</dl>
<p> needs-fragmentation, need-fra, frag</p>
<dl>
<dt>
<dd> Code 4. Datagram had the DF bit set but it was too large for the MTU of the next physical network so it had to be dropped.</dl>
<p> source-route-failed, sour-rou, routefail</p>
<dl>
<dt>
<dd> Code 5. IP datagram had a Source Route option but a router couldn&#8217;t pass it to the next hop.</dl>
<p> network-unknown, netw-unk, net?</p>
<dl>
<dt>
<dd> Code 6. Destination network is unknown. This code is never used. Instead, Network Unreachable is used.</dl>
<p> host-unknown, host-unk, host?</p>
<dl>
<dt>
<dd> Code 7. Specified host is unknown. Usually generated by a router local to the destination host to inform of a bad address.</dl>
<p> host-isolated, host-iso, isolated</p>
<dl>
<dt>
<dd> Code 8. Source Host Isolated. Not used.</dl>
<p> network-prohibited, netw-pro, !net</p>
<dl>
<dt>
<dd> Code 9. Communication with destination network is administratively prohibited (source device is not allowed to send packets to the destination network).</dl>
<p> host-prohibited, host-pro, !host</p>
<dl>
<dt>
<dd> Code 10. Communication with destination host is administratively prohibited. (The source device is allowed to send packets to the destination network but not to the destination device.)</dl>
<p> network-tos, unreachable-network-tos, netw-tos, tosnet</p>
<dl>
<dt>
<dd> Code 11. Destination network unreachable because it cannot provide the type of service specified in the IP TOS field.</dl>
<p> host-tos, unreachable-host-tos, toshost</p>
<dl>
<dt>
<dd> Code 12. Destination host unreachable because it cannot provide the type of service specified in the IP TOS field.</dl>
<p> communication-prohibited, comm-pro, !comm</p>
<dl>
<dt>
<dd> Code 13. Datagram could not be forwarded due to filtering that blocks the message based on its contents.</dl>
<p> host-precedence-violation, precedence-violation, prec-vio, violation</p>
<dl>
<dt>
<dd> Code 14. Precedence value in the IP TOS field is not permitted.</dl>
<p> precedence-cutoff, prec-cut, cutoff</p>
<dl>
<dt>
<dd> Code 15. Precedence value in the IP TOS field is lower than the minimum allowed for the network.</dl>
</dl>
<p> </font><font SIZE="+2"> <code>Redirect</code></p>
<dl>
<dt>
<dd>
<p> redirect-network, redi-net, net</p>
<dl>
<dt>
<dd> Code 0. Redirect all future datagrams with the same destination network as the original datagram, to the router specified in the Address field. The use of this code is prohibited by RFC 1812.</dl>
<p> redirect-host, redi-host, host</p>
<dl>
<dt>
<dd> Code 1. Redirect all future datagrams with the same destination host as the original datagram, to the router specified in the Address field.</dl>
<p> redirect-network-tos, redi-ntos, redir-ntos</p>
<dl>
<dt>
<dd> Code 2. Redirect all future datagrams with the same destination network and IP TOS value as the original datagram, to the router specified in the Address field. The use of this code is prohibited by RFC 1812.</dl>
<p> redirect-host-tos, redi-htos, redir-htos</p>
<dl>
<dt>
<dd> Code 3. Redirect all future datagrams with the same destination host and IP TOS value as the original datagram, to the router specified in the Address field.</dl>
</dl>
<p> </font><font SIZE="+3"> <code>Router Advertisement</code></p>
<dl>
<dt>
<dd>
<p> normal-advertisement, norm-adv, normal, zero, default, def</p>
<dl>
<dt>
<dd> Code 0. Normal router advertisement. In Mobile IP: Mobility agent can act as a router for IP datagrams not related to mobile nodes.</dl>
<p> not-route-common-traffic, not-rou, mobile-ip, !route, !commontraffic</p>
<dl>
<dt>
<dd> Code 16. Used for Mobile IP. The mobility agent does not route common traffic. All foreign agents must forward to a default router any datagrams received from a registered mobile node</dl>
</dl>
<p> </font><font SIZE="+4"> <code>Time Exceeded</code></p>
<dl>
<dt>
<dd>
<p> ttl-exceeded-in-transit, ttl-exc, ttl-transit</p>
<dl>
<dt>
<dd> Code 0. IP Time To Live expired during transit.</dl>
<p> fragment-reassembly-time-exceeded, frag-exc, frag-time</p>
<dl>
<dt>
<dd> Code 1. Fragment reassembly time has been exceeded.</dl>
</dl>
<p> </font><font SIZE="+5"> <code>Parameter Problem</code></p>
<dl>
<dt>
<dd>
<p> pointer-indicates-error, poin-ind, pointer</p>
<dl>
<dt>
<dd> Code 0. The pointer field indicates the location of the problem. See the <code>&#8211;icmp-param-pointer</code> option.</dl>
<p> missing-required-option, miss-option, option-missing</p>
<dl>
<dt>
<dd> Code 1. IP datagram was expected to have an option that is not present.</dl>
<p> bad-length, bad-len, badlen</p>
<dl>
<dt>
<dd> Code 2. The length of the IP datagram is incorrect.</dl>
</dl>
<p> </font></p>
<h2>ARP MODE</h2>
<p> <code>&#8211;arp-type </code><i>type</i> (ICMP Type)</p>
<dl>
<dt>
<dd> This option specifies which type of ARP messages should be generated. <i>type</i> can be supplied in two different ways. You can use the m[blue]<code>official numbers assigned by IANA</code>m[]<font SIZE="-2">[2]</font> (e.g. <code>&#8211;arp-type 1</code> for ARP Request), or you can use one of the mnemonics from the section called &#8220;ARP Types&#8221;.</dl>
<p> <code>&#8211;arp-sender-mac </code><i>mac</i> (Sender MAC address)</p>
<dl>
<dt>
<dd> This option sets the Sender Hardware Address field of the ARP header. Although ARP supports many types of link layer addresses, currently Nping only supports MAC addresses. <i>mac</i> must be specified using the traditional MAC notation (e.g. 00:0a:8a:32:f4:ae). You can also use hyphens as separators (e.g. 00-0a-8a-32-f4-ae).</dl>
<p> <code>&#8211;arp-sender-ip </code><i>addr</i> (Sender IP address)</p>
<dl>
<dt>
<dd> This option sets the Sender IP field of the ARP header. <i>addr</i> can be given as an IPv4 address or a hostname.</dl>
<p> <code>&#8211;arp-target-mac </code><i>mac</i> (target MAC address)</p>
<dl>
<dt>
<dd> This option sets the Target Hardware Address field of the ARP header.</dl>
<p> <code>&#8211;arp-target-ip </code><i>addr</i> (target ip address)</p>
<dl>
<dt>
<dd> This option sets the Target IP field of the ARP header.</dl>
<h3>ARP Types</h3>
<p> These identifiers may be used as mnemonics for the ARP type numbers given to the <code>&#8211;arp-type</code> option. </p>
<p> arp-request, arp, a</p>
<dl>
<dt>
<dd> ARP Request (type 1). ARP requests are used to translate network layer addresses (normally IP addresses) to link layer addresses (usually MAC addresses). Basically, and ARP request is a broadcasted message that asks the host in the same network segment that has a given IP address to provide its MAC address.</dl>
<p> arp-reply, arp-rep, ar</p>
<dl>
<dt>
<dd> ARP Reply (type 2). An ARP reply is a message that a host sends in response to an ARP request to provide its link layer address.</dl>
<p> rarp-request, rarp, r</p>
<dl>
<dt>
<dd> RARP Requests (type 3). RARP requests are used to translate a link layer address (normally a MAC address) to a network layer address (usually an IP address). Basically a RARP request is a broadcasted message sent by a host that wants to know his own IP address because it doesn&#8217;t have any. It was the first protocol designed to solve the bootstrapping problem. However, RARP is now obsolete and DHCP is used instead. For more information about RARP see RFC 903.</dl>
<p> rarp-reply, rarp-rep, rr</p>
<dl>
<dt>
<dd> RARP Reply (type 4). A RARP reply is a message sent in response to a RARP request to provide an IP address to the host that sent the RARP request in the first place.</dl>
<p> drarp-request, drarp, d</p>
<dl>
<dt>
<dd> Dynamic RARP Request (type 5). Dynamic RARP is an extension to RARP used to obtain or assign a network layer address from a fixed link layer address. DRARP was used mainly in Sun Microsystems platforms in the late 90&#8217;s but now it&#8217;s no longer used. See RFC 1931 for more information.</dl>
<p> drarp-reply, drarp-rep, dr</p>
<dl>
<dt>
<dd> Dynamic RARP Reply (type 6). A DRARP reply is a message sent in response to a RARP request to provide network layer address.</dl>
<p> drarp-error, drarp-err, de</p>
<dl>
<dt>
<dd> DRARP Error (type 7). DRARP Error messages are usually sent in response to DRARP requests to inform of some error. In DRARP Error messages, the Target Protocol Address field is used to carry an error code (usually in the first byte). The error code is intended to tell why no target protocol address is being returned. For more information see RFC 1931.</dl>
<p> inarp-request, inarp, i</p>
<dl>
<dt>
<dd> Inverse ARP Request (type 8). InARP requests are used to translate a link layer address to a network layer address. It is similar to RARP request but in this case, the sender of the InARP request wants to know the network layer address of another node, not its own address. InARP is mainly used in Frame Relay and ATM networks. For more information see RFC 2390.</dl>
<p> inarp-reply, inarp-rep, ir</p>
<dl>
<dt>
<dd> Inverse ARP Reply (type 9). InARP reply messages are sent in response to InARP requests to provide the network layer address associated with the host that has a given link layer address.</dl>
<p> arp-nak, an</p>
<dl>
<dt>
<dd> ARP NAK (type 10). ARP NAK messages are an extension to the ATMARP protocol and they are used to improve the robustness of the ATMARP server mechanism. With ARP NAK, a client can determine the difference between a catastrophic server failure and an ATMARP table lookup failure. See RFC 1577 for more information.</dl>
<h2>IPV4 OPTIONS</h2>
<p> <code>-S </code><i>addr</i>, <code>&#8211;source-ip </code><i>addr</i> (Source IP Address)</p>
<dl>
<dt>
<dd> Sets the source IP address. This option lets you specify a custom IP address to be used as source IP address in sent packets. This allows spoofing the sender of the packets. <i>addr</i> can be an IPv4 address or a hostname.</dl>
<p> <code>&#8211;dest-ip </code><i>addr</i> (Destination IP Address)</p>
<dl>
<dt>
<dd> Adds a target to Nping&#8217;s target list. This option is provided for consistency but its use is deprecated in favor of plain target specifications. See the section called &#8220;TARGET SPECIFICATION&#8221;.</dl>
<p> <code>&#8211;tos </code><i>tos</i> (Type of Service)</p>
<dl>
<dt>
<dd> Sets the IP TOS field. The TOS field is used to carry information to provide quality of service features. It is normally used to support a technique called Differentiated Services. See RFC 2474 for more information. <i>tos</i> must be a number in the range [0-255].</dl>
<p> <code>&#8211;id </code><i>id</i> (Identification)</p>
<dl>
<dt>
<dd> Sets the IPv4 Identification field. The Identification field is a 16-bit value that is common to all fragments belonging to a particular message. The value is used by the receiver to reassemble the original message from the fragments received. <i>id</i> must be a number in the range [0-65535].</dl>
<p> <code>&#8211;df</code> (Don&#8217;t Fragment)</p>
<dl>
<dt>
<dd> Sets the Don&#8217;t Fragment bit in sent packets. When an IP datagram has its DF flag set, intermediate devices are not allowed to fragment it so if it needs to travel across a network with a MTU smaller that datagram length the datagram will have to be dropped. Normally an ICMP Destination Unreachable message is generated and sent back to the sender.</dl>
<p> <code>&#8211;mf</code> (More Fragments)</p>
<dl>
<dt>
<dd> Sets the More Fragments bit in sent packets. The MF flag is set to indicate the receiver that the current datagram is a fragment of some larger datagram. When set to zero it indicates that the current datagram is either the last fragment in the set or that it is the only fragment.</dl>
<p> <code>&#8211;ttl </code><i>hops</i> (Time To Live)</p>
<dl>
<dt>
<dd> Sets the IPv4 Time-To-Live (TTL) field in sent packets to the given value. The TTL field specifies how long the datagram is allowed to exist on the network. It was originally intended to represent a number of seconds but it actually represents the number of hops a packet can traverse before being dropped. The TTL tries to avoid a situation in which undeliverable datagrams keep being forwarded from one router to another endlessly. <i>hops</i> must be a number in the range [0-255].</dl>
<p> <code>&#8211;badsum-ip</code> (Invalid IP checksum)</p>
<dl>
<dt>
<dd> Asks Nping to use an invalid IP checksum for packets sent to target hosts. Note that some systems (like most Linux kernels), may fix the checksum before placing the packet on the wire, so even if Nping shows the incorrect checksum in its output, the packets may be transparently corrected by the kernel.</dl>
<p> <code>&#8211;ip-options </code><i>S|R [route]|L [route]|T|U &#8230;</i>, <code>&#8211;ip-options </code><i>hex string</i> (IP Options)</p>
<dl>
<dt>
<dd> The IP protocol offers several options which may be placed in packet headers. Unlike the ubiquitous TCP options, IP options are rarely seen due to practicality and security concerns. In fact, many Internet routers block the most dangerous options such as source routing. Yet options can still be useful in some cases for determining and manipulating the network route to target machines. For example, you may be able to use the record route option to determine a path to a target even when more traditional traceroute-style approaches fail. Or if your packets are being dropped by a certain firewall, you may be able to specify a different route with the strict or loose source routing options. </p>
<p> The most powerful way to specify IP options is to simply pass in hexadecimal data as the argument to <code>&#8211;ip-options</code>. Precede each hex byte value with 
