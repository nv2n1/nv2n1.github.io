---
title: "nmap(1)"
name: "nmap"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nmap/"
description: "nmap – Network exploration tool and security / port scanner"
---

<h2 class="name">NAME</h2>
<p> nmap &#8211; Network exploration tool and security / port scanner </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>nmap</code> [<i>Scan Type</i>&#8230;] [<i>Options</i>] {<i>target specification</i>}</dl>
<h2>DESCRIPTION</h2>
<dd>Nmap (&#8220;Network Mapper&#8221;) is an open source tool for network exploration and security auditing. It was designed to rapidly scan large networks, although it works fine against single hosts. Nmap uses raw IP packets in novel ways to determine what hosts are available on the network, what services (application name and version) those hosts are offering, what operating systems (and OS versions) they are running, what type of packet filters/firewalls are in use, and dozens of other characteristics. While Nmap is commonly used for security audits, many systems and network administrators find it useful for routine tasks such as network inventory, managing service upgrade schedules, and monitoring host or service uptime. </p>
<p> The output from Nmap is a list of scanned targets, with supplemental information on each depending on the options used. Key among that information is the &#8220;interesting ports table&#8221;. That table lists the port number and protocol, service name, and state. The state is either open, filtered, closed, or unfiltered. Open means that an application on the target machine is listening for connections/packets on that port. Filtered means that a firewall, filter, or other network obstacle is blocking the port so that Nmap cannot tell whether it is open or closed. Closed ports have no application listening on them, though they could open up at any time. Ports are classified as unfiltered when they are responsive to Nmap&#8217;s probes, but Nmap cannot determine whether they are open or closed. Nmap reports the state combinations open|filtered and closed|filtered when it cannot determine which of the two states describe a port. The port table may also include software version details when version detection has been requested. When an IP protocol scan is requested (<code>-sO</code>), Nmap provides information on supported IP protocols rather than listening ports. </p>
<p> In addition to the interesting ports table, Nmap can provide further information on targets, including reverse DNS names, operating system guesses, device types, and MAC addresses. </p>
<p> A typical Nmap scan is shown in Example 1. The only Nmap arguments used in this example are <code>-A</code>, to enable OS and version detection, script scanning, and traceroute; <code>-T4</code> for faster execution; and then the hostname. </p>
<p> <code>Example 1. A representative Nmap scan</code> </p>
<dl>
<dt>
<dd>
<pre><code>
#nmap - A - T4 scanme.nmap.org
Nmap scan report for scanme.nmap.org (74.207.244.221)
Host is up (0.029s latency).
rDNS record for 74.207.244.221: li86-221.members.linode.com
Not shown: 995 closed ports
PORT     STATE    SERVICE     VERSION
22/tcp   open     ssh         OpenSSH 5.3p1 Debian 3ubuntu7 (protocol 2.0)
| ssh-hostkey: 1024 8d:60:f1:7c:ca:b7:3d:0a:d6:67:54:9d:69:d9:b9:dd (DSA)
|_2048 79:f8:09:ac:d4:e2:32:42:10:49:d3:bd:20:82:85:ec (RSA)
80/tcp   open     http        Apache httpd 2.2.14 ((Ubuntu))
|_http-title: Go ahead and ScanMe!
646/tcp  filtered ldp
1720/tcp filtered H.323/Q.931
9929/tcp open     nping-echo  Nping echo
Device type: general purpose
Running: Linux 2.6.X
OS CPE: cpe:/o:linux:linux_kernel:2.6.39
OS details: Linux 2.6.39
Network Distance: 11 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:kernel
TRACEROUTE (using port 53/tcp)
HOP RTT      ADDRESS
[Cut first 10 hops for brevity]
11  17.65 ms li86-221.members.linode.com (74.207.244.221)
Nmap done: 1 IP address (1 host up) scanned in 14.40 seconds
</code></pre>
</dl>
<p> The newest version of Nmap can be obtained from m[blue]<code><a rel="nofollow" href="https://nmap.org">https://nmap.org</a></code>m[]. The newest version of this man page is available at m[blue]<code><a rel="nofollow" href="https://nmap.org/book/man.html">https://nmap.org/book/man.html</a></code>m[]. It is also included as a chapter of Nmap Network Scanning: The Official Nmap Project Guide to Network Discovery and Security Scanning (see m[blue]<code><a rel="nofollow" href="https://nmap.org/book/">https://nmap.org/book/</a></code>m[]).</p>
<h2>OPTIONS SUMMARY</h2>
<p> This options summary is printed when Nmap is run with no arguments, and the latest version is always available at m[blue]<code><a rel="nofollow" href="https://svn.nmap.org/nmap/docs/nmap.usage.txt">https://svn.nmap.org/nmap/docs/nmap.usage.txt</a></code>m[]. It helps people remember the most common options, but is no substitute for the in-depth documentation in the rest of this manual. Some obscure options aren&#8217;t even included here. </p>
<dl>
<dt>
<dd>
<pre><code>
Nmap 7.70SVN ( https://nmap.org )
Usage: nmap [Scan Type(s)] [Options] {target specification}
TARGET SPECIFICATION:
  Can pass hostnames, IP addresses, networks, etc.
  Ex: scanme.nmap.org, microsoft.com/24, 192.168.0.1; 10.0.0-255.1-254
  -iL &lt;inputfilename&gt;: Input from list of hosts/networks
  -iR &lt;num hosts&gt;: Choose random targets
  --exclude &lt;host1[,host2][,host3],...&gt;: Exclude hosts/networks
  --excludefile &lt;exclude_file&gt;: Exclude list from file
HOST DISCOVERY:
  -sL: List Scan - simply list targets to scan
  -sn: Ping Scan - disable port scan
  -Pn: Treat all hosts as online -- skip host discovery
  -PS/PA/PU/PY[portlist]: TCP SYN/ACK, UDP or SCTP discovery to given ports
  -PE/PP/PM: ICMP echo, timestamp, and netmask request discovery probes
  -PO[protocol list]: IP Protocol Ping
  -n/-R: Never do DNS resolution/Always resolve [default: sometimes]
  --dns-servers &lt;serv1[,serv2],...&gt;: Specify custom DNS servers
  --system-dns: Use OS's DNS resolver
  --traceroute: Trace hop path to each host
SCAN TECHNIQUES:
  -sS/sT/sA/sW/sM: TCP SYN/Connect()/ACK/Window/Maimon scans
  -sU: UDP Scan
  -sN/sF/sX: TCP Null, FIN, and Xmas scans
  --scanflags &lt;flags&gt;: Customize TCP scan flags
  -sI &lt;zombie host[:probeport]&gt;: Idle scan
  -sY/sZ: SCTP INIT/COOKIE-ECHO scans
  -sO: IP protocol scan
  -b &lt;FTP relay host&gt;: FTP bounce scan
PORT SPECIFICATION AND SCAN ORDER:
  -p &lt;port ranges&gt;: Only scan specified ports
    Ex: -p22; -p1-65535; -p U:53,111,137,T:21-25,80,139,8080,S:9
  --exclude-ports &lt;port ranges&gt;: Exclude the specified ports from scanning
  -F: Fast mode - Scan fewer ports than the default scan
  -r: Scan ports consecutively - don't randomize
  --top-ports &lt;number&gt;: Scan &lt;number&gt; most common ports
  --port-ratio &lt;ratio&gt;: Scan ports more common than &lt;ratio&gt;
SERVICE/VERSION DETECTION:
  -sV: Probe open ports to determine service/version info
  --version-intensity &lt;level&gt;: Set from 0 (light) to 9 (try all probes)
  --version-light: Limit to most likely probes (intensity 2)
  --version-all: Try every single probe (intensity 9)
  --version-trace: Show detailed version scan activity (for debugging)
SCRIPT SCAN:
  -sC: equivalent to --script=default
  --script=&lt;Lua scripts&gt;: &lt;Lua scripts&gt; is a comma separated list of
           directories, script-files or script-categories
  --script-args=&lt;n1=v1,[n2=v2,...]&gt;: provide arguments to scripts
  --script-args-file=filename: provide NSE script args in a file
  --script-trace: Show all data sent and received
  --script-updatedb: Update the script database.
  --script-help=&lt;Lua scripts&gt;: Show help about scripts.
           &lt;Lua scripts&gt; is a comma-separated list of script-files or
           script-categories.
OS DETECTION:
  -O: Enable OS detection
  --osscan-limit: Limit OS detection to promising targets
  --osscan-guess: Guess OS more aggressively
TIMING AND PERFORMANCE:
  Options which take &lt;time&gt; are in seconds, or append 'ms' (milliseconds),
  's' (seconds), 'm' (minutes), or 'h' (hours) to the value (e.g. 30m).
  -T&lt;0-5&gt;: Set timing template (higher is faster)
  --min-hostgroup/max-hostgroup &lt;size&gt;: Parallel host scan group sizes
  --min-parallelism/max-parallelism &lt;numprobes&gt;: Probe parallelization
  --min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout &lt;time&gt;: Specifies
      probe round trip time.
  --max-retries &lt;tries&gt;: Caps number of port scan probe retransmissions.
  --host-timeout &lt;time&gt;: Give up on target after this long
  --scan-delay/--max-scan-delay &lt;time&gt;: Adjust delay between probes
  --min-rate &lt;number&gt;: Send packets no slower than &lt;number&gt; per second
  --max-rate &lt;number&gt;: Send packets no faster than &lt;number&gt; per second
FIREWALL/IDS EVASION AND SPOOFING:
  -f; --mtu &lt;val&gt;: fragment packets (optionally w/given MTU)
  -D &lt;decoy1,decoy2[,ME],...&gt;: Cloak a scan with decoys
  -S &lt;IP_Address&gt;: Spoof source address
  -e &lt;iface&gt;: Use specified interface
  -g/--source-port &lt;portnum&gt;: Use given port number
  --proxies &lt;url1,[url2],...&gt;: Relay connections through HTTP/SOCKS4 proxies
  --data &lt;hex string&gt;: Append a custom payload to sent packets
  --data-string &lt;string&gt;: Append a custom ASCII string to sent packets
  --data-length &lt;num&gt;: Append random data to sent packets
  --ip-options &lt;options&gt;: Send packets with specified ip options
  --ttl &lt;val&gt;: Set IP time-to-live field
  --spoof-mac &lt;mac address/prefix/vendor name&gt;: Spoof your MAC address
  --badsum: Send packets with a bogus TCP/UDP/SCTP checksum
OUTPUT:
  -oN/-oX/-oS/-oG &lt;file&gt;: Output scan in normal, XML, s|&lt;rIpt kIddi3,
     and Grepable format, respectively, to the given filename.
  -oA &lt;basename&gt;: Output in the three major formats at once
  -v: Increase verbosity level (use -vv or more for greater effect)
  -d: Increase debugging level (use -dd or more for greater effect)
  --reason: Display the reason a port is in a particular state
  --open: Only show open (or possibly open) ports
  --packet-trace: Show all packets sent and received
  --iflist: Print host interfaces and routes (for debugging)
  --append-output: Append to rather than clobber specified output files
  --resume &lt;filename&gt;: Resume an aborted scan
  --stylesheet &lt;path/URL&gt;: XSL stylesheet to transform XML output to HTML
  --webxml: Reference stylesheet from Nmap.Org for more portable XML
  --no-stylesheet: Prevent associating of XSL stylesheet w/XML output
MISC:
  -6: Enable IPv6 scanning
  -A: Enable OS detection, version detection, script scanning, and traceroute
  --datadir &lt;dirname&gt;: Specify custom Nmap data file location
  --send-eth/--send-ip: Send using raw ethernet frames or IP packets
  --privileged: Assume that the user is fully privileged
  --unprivileged: Assume the user lacks raw socket privileges
  -V: Print version number
  -h: Print this help summary page.
EXAMPLES:
  nmap -v -A scanme.nmap.org
  nmap -v -sn 192.168.0.0/16 10.0.0.0/8
  nmap -v -iR 10000 -Pn -p 80
SEE THE MAN PAGE (https://nmap.org/book/man.html) FOR MORE OPTIONS AND EXAMPLES
</code></pre>
</dl>
<h2>TARGET SPECIFICATION</h2>
<p> Everything on the Nmap command-line that isn&#8217;t an option (or option argument) is treated as a target host specification. The simplest case is to specify a target IP address or hostname for scanning. </p>
<p> When a hostname is given as a target, it is resolved via the Domain Name System (DNS) to determine the IP address to scan. If the name resolves to more than one IP address, only the first one will be scanned. To make Nmap scan all the resolved addresses instead of only the first one, use the <code>&#8211;resolve-all</code> option. </p>
<p> Sometimes you wish to scan a whole network of adjacent hosts. For this, Nmap supports CIDR-style addressing. You can append /<i>numbits</i> to an IP address or hostname and Nmap will scan every IP address for which the first <i>numbits</i> are the same as for the reference IP or hostname given. For example, 192.168.10.0/24 would scan the 256 hosts between 192.168.10.0 (binary: 11000000 10101000 00001010 00000000) and 192.168.10.255 (binary: 11000000 10101000 00001010 11111111), inclusive. 192.168.10.40/24 would scan exactly the same targets. Given that the host scanme.nmap.org is at the IP address 64.13.134.52, the specification scanme.nmap.org/16 would scan the 65,536 IP addresses between 64.13.0.0 and 64.13.255.255. The smallest allowed value is /0, which targets the whole Internet. The largest value for IPv4 is /32, which scans just the named host or IP address because all address bits are fixed. The largest value for IPv6 is /128, which does the same thing. </p>
<p> CIDR notation is short but not always flexible enough. For example, you might want to scan 192.168.0.0/16 but skip any IPs ending with .0 or .255 because they may be used as subnet network and broadcast addresses. Nmap supports this through octet range addressing. Rather than specify a normal IP address, you can specify a comma-separated list of numbers or ranges for each octet. For example, 192.168.0-255.1-254 will skip all addresses in the range that end in .0 or .255, and 192.168.3-5,7.1 will scan the four addresses 192.168.3.1, 192.168.4.1, 192.168.5.1, and 192.168.7.1. Either side of a range may be omitted; the default values are 0 on the left and 255 on the right. Using &#8211; by itself is the same as 0-255, but remember to use 0- in the first octet so the target specification doesn&#8217;t look like a command-line option. Ranges need not be limited to the final octets: the specifier 0-255.0-255.13.37 will perform an Internet-wide scan for all IP addresses ending in 13.37. This sort of broad sampling can be useful for Internet surveys and research. </p>
<p> IPv6 addresses can be specified by their fully qualified IPv6 address or hostname or with CIDR notation for subnets. Octet ranges aren&#8217;t yet supported for IPv6. </p>
<p> IPv6 addresses with non-global scope need to have a zone ID suffix. On Unix systems, this is a percent sign followed by an interface name; a complete address might be fe80::a8bb:ccff:fedd:eeff%eth0. On Windows, use an interface index number in place of an interface name: fe80::a8bb:ccff:fedd:eeff%1. You can see a list of interface indexes by running the command <code>netsh.exe interface ipv6 show interface</code>. </p>
<p> Nmap accepts multiple host specifications on the command line, and they don&#8217;t need to be the same type. The command <code>nmap scanme.nmap.org 192.168.0.0/8 10.0.0,1,3-7.-</code> does what you would expect. </p>
<p> While targets are usually specified on the command lines, the following options are also available to control target selection: </p>
<p> <code>-iL </code><i>inputfilename</i> (Input from list)</p>
<dl>
<dt>
<dd> Reads target specifications from <i>inputfilename</i>. Passing a huge list of hosts is often awkward on the command line, yet it is a common desire. For example, your DHCP server might export a list of 10,000 current leases that you wish to scan. Or maybe you want to scan all IP addresses <i>except</i> for those to locate hosts using unauthorized static IP addresses. Simply generate the list of hosts to scan and pass that filename to Nmap as an argument to the <code>-iL</code> option. Entries can be in any of the formats accepted by Nmap on the command line (IP address, hostname, CIDR, IPv6, or octet ranges). Each entry must be separated by one or more spaces, tabs, or newlines. You can specify a hyphen (-) as the filename if you want Nmap to read hosts from standard input rather than an actual file. </p>
<p> The input file may contain comments that start with # and extend to the end of the line.</dl>
<p> <code>-iR </code><i>num hosts</i> (Choose random targets)</p>
<dl>
<dt>
<dd> For Internet-wide surveys and other research, you may want to choose targets at random. The <i>num hosts</i> argument tells Nmap how many IPs to generate. Undesirable IPs such as those in certain private, multicast, or unallocated address ranges are automatically skipped. The argument 0 can be specified for a never-ending scan. Keep in mind that some network administrators bristle at unauthorized scans of their networks and may complain. Use this option at your own risk! If you find yourself really bored one rainy afternoon, try the command <code>nmap -Pn -sS -p 80 -iR 0 &#8211;open</code> to locate random web servers for browsing.</dl>
<p> <code>&#8211;exclude </code><i>host1</i><code>[,</code><i>host2</i>[,&#8230;]] (Exclude hosts/networks)</p>
<dl>
<dt>
<dd> Specifies a comma-separated list of targets to be excluded from the scan even if they are part of the overall network range you specify. The list you pass in uses normal Nmap syntax, so it can include hostnames, CIDR netblocks, octet ranges, etc. This can be useful when the network you wish to scan includes untouchable mission-critical servers, systems that are known to react adversely to port scans, or subnets administered by other people.</dl>
<p> <code>&#8211;excludefile </code><i>exclude_file</i> (Exclude list from file)</p>
<dl>
<dt>
<dd> This offers the same functionality as the <code>&#8211;exclude</code> option, except that the excluded targets are provided in a newline-, space-, or tab-delimited <i>exclude_file</i> rather than on the command line. </p>
<p> The exclude file may contain comments that start with # and extend to the end of the line.</dl>
<h2>HOST DISCOVERY</h2>
<p> One of the very first steps in any network reconnaissance mission is to reduce a (sometimes huge) set of IP ranges into a list of active or interesting hosts. Scanning every port of every single IP address is slow and usually unnecessary. Of course what makes a host interesting depends greatly on the scan purposes. Network administrators may only be interested in hosts running a certain service, while security auditors may care about every single device with an IP address. An administrator may be comfortable using just an ICMP ping to locate hosts on his internal network, while an external penetration tester may use a diverse set of dozens of probes in an attempt to evade firewall restrictions. </p>
<p> Because host discovery needs are so diverse, Nmap offers a wide variety of options for customizing the techniques used. Host discovery is sometimes called ping scan, but it goes well beyond the simple ICMP echo request packets associated with the ubiquitous ping tool. Users can skip the ping step entirely with a list scan (<code>-sL</code>) or by disabling ping (<code>-Pn</code>), or engage the network with arbitrary combinations of multi-port TCP SYN/ACK, UDP, SCTP INIT and ICMP probes. The goal of these probes is to solicit responses which demonstrate that an IP address is actually active (is being used by a host or network device). On many networks, only a small percentage of IP addresses are active at any given time. This is particularly common with private address space such as 10.0.0.0/8. That network has 16 million IPs, but I have seen it used by companies with less than a thousand machines. Host discovery can find those machines in a sparsely allocated sea of IP addresses. </p>
<p> If no host discovery options are given, Nmap sends an ICMP echo request, a TCP SYN packet to port 443, a TCP ACK packet to port 80, and an ICMP timestamp request. (For IPv6, the ICMP timestamp request is omitted because it is not part of ICMPv6.) These defaults are equivalent to the <code>-PE -PS443 -PA80 -PP</code> options. The exceptions to this are the ARP (for IPv4) and Neighbor Discovery (for IPv6) scans which are used for any targets on a local ethernet network. For unprivileged Unix shell users, the default probes are a SYN packet to ports 80 and 443 using the <code>connect</code> system call. This host discovery is often sufficient when scanning local networks, but a more comprehensive set of discovery probes is recommended for security auditing. </p>
<p> The <code>-P*</code> options (which select ping types) can be combined. You can increase your odds of penetrating strict firewalls by sending many probe types using different TCP ports/flags and ICMP codes. Also note that ARP/Neighbor Discovery (<code>-PR</code>) is done by default against targets on a local ethernet network even if you specify other <code>-P*</code> options, because it is almost always faster and more effective. </p>
<p> By default, Nmap does host discovery and then performs a port scan against each host it determines is online. This is true even if you specify non-default host discovery types such as UDP probes (<code>-PU</code>). Read about the <code>-sn</code> option to learn how to perform only host discovery, or use <code>-Pn</code> to skip host discovery and port scan all target hosts. The following options control host discovery: </p>
<p> <code>-sL</code> (List Scan)</p>
<dl>
<dt>
<dd> The list scan is a degenerate form of host discovery that simply lists each host of the network(s) specified, without sending any packets to the target hosts. By default, Nmap still does reverse-DNS resolution on the hosts to learn their names. It is often surprising how much useful information simple hostnames give out. For example, fw.chi is the name of one company&#8217;s Chicago firewall. </p>
<p> Nmap also reports the total number of IP addresses at the end. The list scan is a good sanity check to ensure that you have proper IP addresses for your targets. If the hosts sport domain names you do not recognize, it is worth investigating further to prevent scanning the wrong company&#8217;s network. </p>
<p> Since the idea is to simply print a list of target hosts, options for higher level functionality such as port scanning, OS detection, or ping scanning cannot be combined with this. If you wish to disable ping scanning while still performing such higher level functionality, read up on the <code>-Pn</code> (skip ping) option.</dl>
<p> <code>-sn</code> (No port scan)</p>
<dl>
<dt>
<dd> This option tells Nmap not to do a port scan after host discovery, and only print out the available hosts that responded to the host discovery probes. This is often known as a &#8220;ping scan&#8221;, but you can also request that traceroute and NSE host scripts be run. This is by default one step more intrusive than the list scan, and can often be used for the same purposes. It allows light reconnaissance of a target network without attracting much attention. Knowing how many hosts are up is more valuable to attackers than the list provided by list scan of every single IP and host name. </p>
<p> Systems administrators often find this option valuable as well. It can easily be used to count available machines on a network or monitor server availability. This is often called a ping sweep, and is more reliable than pinging the broadcast address because many hosts do not reply to broadcast queries. </p>
<p> The default host discovery done with <code>-sn</code> consists of an ICMP echo request, TCP SYN to port 443, TCP ACK to port 80, and an ICMP timestamp request by default. When executed by an unprivileged user, only SYN packets are sent (using a <code>connect</code> call) to ports 80 and 443 on the target. When a privileged user tries to scan targets on a local ethernet network, ARP requests are used unless <code>&#8211;send-ip</code> was specified. The <code>-sn</code> option can be combined with any of the discovery probe types (the <code>-P*</code> options, excluding <code>-Pn</code>) for greater flexibility. If any of those probe type and port number options are used, the default probes are overridden. When strict firewalls are in place between the source host running Nmap and the target network, using those advanced techniques is recommended. Otherwise hosts could be missed when the firewall drops probes or their responses. </p>
<p> In previous releases of Nmap, <code>-sn</code> was known as <code>-sP</code>.</dl>
<p> <code>-Pn</code> (No ping)</p>
<dl>
<dt>
<dd> This option skips the Nmap discovery stage altogether. Normally, Nmap uses this stage to determine active machines for heavier scanning. By default, Nmap only performs heavy probing such as port scans, version detection, or OS detection against hosts that are found to be up. Disabling host discovery with <code>-Pn</code> causes Nmap to attempt the requested scanning functions against <i>every</i> target IP address specified. So if a class B target address space (/16) is specified on the command line, all 65,536 IP addresses are scanned. Proper host discovery is skipped as with the list scan, but instead of stopping and printing the target list, Nmap continues to perform requested functions as if each target IP is active. To skip ping scan <i>and</i> port scan, while still allowing NSE to run, use the two options <code>-Pn -sn</code> together. </p>
<p> For machines on a local ethernet network, ARP scanning will still be performed (unless <code>&#8211;disable-arp-ping</code> or <code>&#8211;send-ip</code> is specified) because Nmap needs MAC addresses to further scan target hosts. In previous versions of Nmap, <code>-Pn</code> was <code>-P0</code> and <code>-PN</code>.</dl>
<p> <code>-PS </code><i>port list</i> (TCP SYN Ping)</p>
<dl>
<dt>
<dd> This option sends an empty TCP packet with the SYN flag set. The default destination port is 80 (configurable at compile time by changing <i>DEFAULT_TCP_PROBE_PORT_SPEC</i> in nmap.h). Alternate ports can be specified as a parameter. The syntax is the same as for the <code>-p</code> except that port type specifiers like T: are not allowed. Examples are <code>-PS22</code> and <code>-PS22-25,80,113,1050,35000</code>. Note that there can be no space between <code>-PS</code> and the port list. If multiple probes are specified they will be sent in parallel. </p>
<p> The SYN flag suggests to the remote system that you are attempting to establish a connection. Normally the destination port will be closed, and a RST (reset) packet sent back. If the port happens to be open, the target will take the second step of a TCP three-way-handshake by responding with a SYN/ACK TCP packet. The machine running Nmap then tears down the nascent connection by responding with a RST rather than sending an ACK packet which would complete the three-way-handshake and establish a full connection. The RST packet is sent by the kernel of the machine running Nmap in response to the unexpected SYN/ACK, not by Nmap itself. </p>
<p> Nmap does not care whether the port is open or closed. Either the RST or SYN/ACK response discussed previously tell Nmap that the host is available and responsive. </p>
<p> On Unix boxes, only the privileged user root is generally able to send and receive raw TCP packets. For unprivileged users, a workaround is automatically employed whereby the <code>connect</code> system call is initiated against each target port. This has the effect of sending a SYN packet to the target host, in an attempt to establish a connection. If <code>connect</code> returns with a quick success or an ECONNREFUSED failure, the underlying TCP stack must have received a SYN/ACK or RST and the host is marked available. If the connection attempt is left hanging until a timeout is reached, the host is marked as down.</dl>
<p> <code>-PA </code><i>port list</i> (TCP ACK Ping)</p>
<dl>
<dt>
<dd> The TCP ACK ping is quite similar to the just-discussed SYN ping. The difference, as you could likely guess, is that the TCP ACK flag is set instead of the SYN flag. Such an ACK packet purports to be acknowledging data over an established TCP connection, but no such connection exists. So remote hosts should always respond with a RST packet, disclosing their existence in the process. </p>
<p> The <code>-PA</code> option uses the same default port as the SYN probe (80) and can also take a list of destination ports in the same format. If an unprivileged user tries this, the <code>connect</code> workaround discussed previously is used. This workaround is imperfect because <code>connect</code> is actually sending a SYN packet rather than an ACK. </p>
<p> The reason for offering both SYN and ACK ping probes is to maximize the chances of bypassing firewalls. Many administrators configure routers and other simple firewalls to block incoming SYN packets except for those destined for public services like the company web site or mail server. This prevents other incoming connections to the organization, while allowing users to make unobstructed outgoing connections to the Internet. This non-stateful approach takes up few resources on the firewall/router and is widely supported by hardware and software filters. The Linux Netfilter/iptables firewall software offers the <code>&#8211;syn</code> convenience option to implement this stateless approach. When stateless firewall rules such as this are in place, SYN ping probes (<code>-PS</code>) are likely to be blocked when sent to closed target ports. In such cases, the ACK probe shines as it cuts right through these rules. </p>
<p> Another common type of firewall uses stateful rules that drop unexpected packets. This feature was initially found mostly on high-end firewalls, though it has become much more common over the years. The Linux Netfilter/iptables system supports this through the <code>&#8211;state</code> option, which categorizes packets based on connection state. A SYN probe is more likely to work against such a system, as unexpected ACK packets are generally recognized as bogus and dropped. A solution to this quandary is to send both SYN and ACK probes by specifying <code>-PS</code> and <code>-PA</code>.</dl>
<p> <code>-PU </code><i>port list</i> (UDP Ping)</p>
<dl>
<dt>
<dd> Another host discovery option is the UDP ping, which sends a UDP packet to the given ports. For most ports, the packet will be empty, though some use a protocol-specific payload that is more likely to elicit a response. The payload database is described at m[blue]<code><a rel="nofollow" href="https://nmap.org/book/nmap-payloads.html">https://nmap.org/book/nmap-payloads.html</a></code>m[]. </p>
<p> . Packet content can also be affected with the <code>&#8211;data</code>, <code>&#8211;data-string</code>, and <code>&#8211;data-length</code> options. </p>
<p> The port list takes the same format as with the previously discussed <code>-PS</code> and <code>-PA</code> options. If no ports are specified, the default is 40125. This default can be configured at compile-time by changing <i>DEFAULT_UDP_PROBE_PORT_SPEC</i> in nmap.h. A highly uncommon port is used by default because sending to open ports is often undesirable for this particular scan type. </p>
<p> Upon hitting a closed port on the target machine, the UDP probe should elicit an ICMP port unreachable packet in return. This signifies to Nmap that the machine is up and available. Many other types of ICMP errors, such as host/network unreachables or TTL exceeded are indicative of a down or unreachable host. A lack of response is also interpreted this way. If an open port is reached, most services simply ignore the empty packet and fail to return any response. This is why the default probe port is 40125, which is highly unlikely to be in use. A few services, such as the Character Generator (chargen) protocol, will respond to an empty UDP packet, and thus disclose to Nmap that the machine is available. </p>
<p> The primary advantage of this scan type is that it bypasses firewalls and filters that only screen TCP. For example, I once owned a Linksys BEFW11S4 wireless broadband router. The external interface of this device filtered all TCP ports by default, but UDP probes would still elicit port unreachable messages and thus give away the device.</dl>
<p> <code>-PY </code><i>port list</i> (SCTP INIT Ping)</p>
<dl>
<dt>
<dd> This option sends an SCTP packet containing a minimal INIT chunk. The default destination port is 80 (configurable at compile time by changing <i>DEFAULT_SCTP_PROBE_PORT_SPEC</i> in nmap.h). Alternate ports can be specified as a parameter. The syntax is the same as for the <code>-p</code> except that port type specifiers like S: are not allowed. Examples are <code>-PY22</code> and <code>-PY22,80,179,5060</code>. Note that there can be no space between <code>-PY</code> and the port list. If multiple probes are specified they will be sent in parallel. </p>
<p> The INIT chunk suggests to the remote system that you are attempting to establish an association. Normally the destination port will be closed, and an ABORT chunk will be sent back. If the port happens to be open, the target will take the second step of an SCTP four-way-handshake by responding with an INIT-ACK chunk. If the machine running Nmap has a functional SCTP stack, then it tears down the nascent association by responding with an ABORT chunk rather than sending a COOKIE-ECHO chunk which would be the next step in the four-way-handshake. The ABORT packet is sent by the kernel of the machine running Nmap in response to the unexpected INIT-ACK, not by Nmap itself. </p>
<p> Nmap does not care whether the port is open or closed. Either the ABORT or INIT-ACK response discussed previously tell Nmap that the host is available and responsive. </p>
<p> On Unix boxes, only the privileged user root is generally able to send and receive raw SCTP packets. Using SCTP INIT Pings is currently not possible for unprivileged users.</dl>
<p> <code>-PE</code>; <code>-PP</code>; <code>-PM</code> (ICMP Ping Types)</p>
<dl>
<dt>
<dd> In addition to the unusual TCP, UDP and SCTP host discovery types discussed previously, Nmap can send the standard packets sent by the ubiquitous ping program. Nmap sends an ICMP type 8 (echo request) packet to the target IP addresses, expecting a type 0 (echo reply) in return from available hosts. Unfortunately for network explorers, many hosts and firewalls now block these packets, rather than responding as required by m[blue]<code>RFC 1122</code>m[]<font SIZE="-2">[2]</font>. For this reason, ICMP-only scans are rarely reliable enough against unknown targets over the Internet. But for system administrators monitoring an internal network, they can be a practical and efficient approach. Use the <code>-PE</code> option to enable this echo request behavior. </p>
<p> While echo request is the standard ICMP ping query, Nmap does not stop there. The ICMP standards (m[blue]<code>RFC 792</code>m[]<font SIZE="-2">[3]</font> and m[blue]<code>RFC 950</code>m[]<font SIZE="-2">[4]</font> ) also specify timestamp request, information request, and address mask request packets as codes 13, 15, and 17, respectively. While the ostensible purpose for these queries is to learn information such as address masks and current times, they can easily be used for host discovery. A system that replies is up and available. Nmap does not currently implement information request packets, as they are not widely supported. RFC 1122 insists that &#8220;a host SHOULD NOT implement these messages&#8221;. Timestamp and address mask queries can be sent with the <code>-PP</code> and <code>-PM</code> options, respectively. A timestamp reply (ICMP code 14) or address mask reply (code 18) discloses that the host is available. These two queries can be valuable when administrators specifically block echo request packets while forgetting that other ICMP queries can be used for the same purpose.</dl>
<p> <code>-PO </code><i>protocol list</i> (IP Protocol Ping)</p>
<dl>
<dt>
<dd> One of the newer host discovery options is the IP protocol ping, which sends IP packets with the specified protocol number set in their IP header. The protocol list takes the same format as do port lists in the previously discussed TCP, UDP and SCTP host discovery options. If no protocols are specified, the default is to send multiple IP packets for ICMP (protocol 1), IGMP (protocol 2), and IP-in-IP (protocol 4). The default protocols can be configured at compile-time by changing <i>DEFAULT_PROTO_PROBE_PORT_SPEC</i> in nmap.h. Note that for the ICMP, IGMP, TCP (protocol 6), UDP (protocol 17) and SCTP (protocol 132), the packets are sent with the proper protocol headers while other protocols are sent with no additional data beyond the IP header (unless any of <code>&#8211;data</code>, <code>&#8211;data-string</code>, or <code>&#8211;data-length</code> options are specified). </p>
<p> This host discovery method looks for either responses using the same protocol as a probe, or ICMP protocol unreachable messages which signify that the given protocol isn&#8217;t supported on the destination host. Either type of response signifies that the target host is alive.</dl>
<p> <code>-PR</code> (ARP Ping)</p>
<dl>
<dt>
<dd> One of the most common Nmap usage scenarios is to scan an ethernet LAN. On most LANs, especially those using private address ranges specified by m[blue]<code>RFC 1918</code>m[]<font SIZE="-2">[5]</font>, the vast majority of IP addresses are unused at any given time. When Nmap tries to send a raw IP packet such as an ICMP echo request, the operating system must determine the destination hardware (ARP) address corresponding to the target IP so that it can properly address the ethernet frame. This is often slow and problematic, since operating systems weren&#8217;t written with the expectation that they would need to do millions of ARP requests against unavailable hosts in a short time period. </p>
<p> ARP scan puts Nmap and its optimized algorithms in charge of ARP requests. And if it gets a response back, Nmap doesn&#8217;t even need to worry about the IP-based ping packets since it already knows the host is up. This makes ARP scan much faster and more reliable than IP-based scans. So it is done by default when scanning ethernet hosts that Nmap detects are on a local ethernet network. Even if different ping types (such as <code>-PE</code> or <code>-PS</code>) are specified, Nmap uses ARP instead for any of the targets which are on the same LAN. If you absolutely don&#8217;t want to do an ARP scan, specify <code>&#8211;disable-arp-ping</code>. </p>
<p> For IPv6 (-6 option), <code>-PR</code> uses ICMPv6 Neighbor Discovery instead of ARP. Neighbor Discovery, defined in RFC 4861, can be seen as the IPv6 equivalent of ARP.</dl>
<p> <code>&#8211;disable-arp-ping</code> (No ARP or ND Ping)</p>
<dl>
<dt>
<dd> Nmap normally does ARP or IPv6 Neighbor Discovery (ND) discovery of locally connected ethernet hosts, even if other host discovery options such as <code>-Pn</code> or <code>-PE</code> are used. To disable this implicit behavior, use the <code>&#8211;disable-arp-ping</code> option. </p>
<p> The default behavior is normally faster, but this option is useful on networks using proxy ARP, in which a router speculatively replies to all ARP requests, making every target appear to be up according to ARP scan.</dl>
<p> <code>&#8211;traceroute</code> (Trace path to host)</p>
<dl>
<dt>
<dd> Traceroutes are performed post-scan using information from the scan results to determine the port and protocol most likely to reach the target. It works with all scan types except connect scans (<code>-sT</code>) and idle scans (<code>-sI</code>). All traces use Nmap&#8217;s dynamic timing model and are performed in parallel. </p>
<p> Traceroute works by sending packets with a low TTL (time-to-live) in an attempt to elicit ICMP Time Exceeded messages from intermediate hops between the scanner and the target host. Standard traceroute implementations start with a TTL of 1 and increment the TTL until the destination host is reached. Nmap&#8217;s traceroute starts with a high TTL and then decrements the TTL until it reaches zero. Doing it backwards lets Nmap employ clever caching algorithms to speed up traces over multiple hosts. On average Nmap sends 5-10 fewer packets per host, depending on network conditions. If a single subnet is being scanned (i.e. 192.168.0.0/24) Nmap may only have to send two packets to most hosts.</dl>
<p> <code>-n</code> (No DNS resolution)</p>
<dl>
<dt>
<dd> Tells Nmap to <i>never</i> do reverse DNS </p>
<p> resolution on the active IP addresses it finds. Since DNS can be slow even with Nmap&#8217;s built-in parallel stub resolver, this option can slash scanning times.</dl>
<p> <code>-R</code> (DNS resolution for all targets)</p>
<dl>
<dt>
<dd> Tells Nmap to <i>always</i> do reverse DNS resolution on the target IP addresses. Normally reverse DNS is only performed against responsive (online) hosts.</dl>
<p> <code>&#8211;resolve-all</code> (Scan each resolved address)</p>
<dl>
<dt>
<dd> If a hostname target resolves to more than one address, scan all of them. The default behavior is to only scan the first resolved address. Regardless, only addresses in the appropriate address family will be scanned: IPv4 by default, IPv6 with <code>-6</code>.</dl>
<p> <code>&#8211;system-dns</code> (Use system DNS resolver)</p>
<dl>
<dt>
<dd> By default, Nmap reverse-resolves IP addresses by sending queries directly to the name servers configured on your host and then listening for responses. Many requests (often dozens) are performed in parallel to improve performance. Specify this option to use your system resolver instead (one IP at a time via the <code>getnameinfo</code> call). This is slower and rarely useful unless you find a bug in the Nmap parallel resolver (please let us know if you do). The system resolver is always used for forward lookups (getting an IP address from a hostname).</dl>
<p> <code>&#8211;dns-servers </code><i>server1</i><code>[,</code><i>server2</i>[,&#8230;]] (Servers to use for reverse DNS queries)</p>
<dl>
<dt>
<dd> By default, Nmap determines your DNS servers (for rDNS resolution) from your resolv.conf file (Unix) or the Registry (Win32). Alternatively, you may use this option to specify alternate servers. This option is not honored if you are using <code>&#8211;system-dns</code>. Using multiple DNS servers is often faster, especially if you choose authoritative servers for your target IP space. This option can also improve stealth, as your requests can be bounced off just about any recursive DNS server on the Internet. </p>
<p> This option also comes in handy when scanning private networks. Sometimes only a few name servers provide proper rDNS information, and you may not even know where they are. You can scan the network for port 53 (perhaps with version detection), then try Nmap list scans (<code>-sL</code>) specifying each name server one at a time with <code>&#8211;dns-servers</code> until you find one which works. </p>
<p> This option might not be honored if the DNS response exceeds the size of a UDP packet. In such a situation our DNS resolver will make the best effort to extract a response from the truncated packet, and if not successful it will fall back to using the system resolver. Also, responses that contain CNAME aliases will fall back to the system resolver.</dl>
<h2>PORT SCANNING BASICS</h2>
<p> While Nmap has grown in functionality over the years, it began as an efficient port scanner, and that remains its core function. The simple command <code>nmap </code><i>target</i> scans 1,000 TCP ports on the host <i>target</i>. While many port scanners have traditionally lumped all ports into the open or closed states, Nmap is much more granular. It divides ports into six states: open, closed, filtered, unfiltered, open|filtered, or closed|filtered. </p>
<p> These states are not intrinsic properties of the port itself, but describe how Nmap sees them. For example, an Nmap scan from the same network as the target may show port 135/tcp as open, while a scan at the same time with the same options from across the Internet might show that port as filtered. </p>
<p> <code>The six port states recognized by Nmap</code> </p>
<p> open</p>
<dl>
<dt>
<dd> An application is actively accepting TCP connections, UDP datagrams or SCTP associations on this port. Finding these is often the primary goal of port scanning. Security-minded people know that each open port is an avenue for attack. Attackers and pen-testers want to exploit the open ports, while administrators try to close or protect them with firewalls without thwarting legitimate users. Open ports are also interesting for non-security scans because they show services available for use on the network.</dl>
<p> closed</p>
<dl>
<dt>
<dd> A closed port is accessible (it receives and responds to Nmap probe packets), but there is no application listening on it. They can be helpful in showing that a host is up on an IP address (host discovery, or ping scanning), and as part of OS detection. Because closed ports are reachable, it may be worth scanning later in case some open up. Administrators may want to consider blocking such ports with a firewall. Then they would appear in the filtered state, discussed next.</dl>
<p> filtered</p>
<dl>
<dt>
<dd> Nmap cannot determine whether the port is open because packet filtering prevents its probes from reaching the port. The filtering could be from a dedicated firewall device, router rules, or host-based firewall software. These ports frustrate attackers because they provide so little information. Sometimes they respond with ICMP error messages such as type 3 code 13 (destination unreachable: communication administratively prohibited), but filters that simply drop probes without responding are far more common. This forces Nmap to retry several times just in case the probe was dropped due to network congestion rather than filtering. This slows down the scan dramatically.</dl>
<p> unfiltered</p>
<dl>
<dt>
<dd> The unfiltered state means that a port is accessible, but Nmap is unable to determine whether it is open or closed. Only the ACK scan, which is used to map firewall rulesets, classifies ports into this state. Scanning unfiltered ports with other scan types such as Window scan, SYN scan, or FIN scan, may help resolve whether the port is open.</dl>
<p> open|filtered</p>
<dl>
<dt>
<dd> Nmap places ports in this state when it is unable to determine whether a port is open or filtered. This occurs for scan types in which open ports give no response. The lack of response could also mean that a packet filter dropped the probe or any response it elicited. So Nmap does not know for sure whether the port is open or being filtered. The UDP, IP protocol, FIN, NULL, and Xmas scans classify ports this way.</dl>
<p> closed|filtered</p>
<dl>
<dt>
<dd> This state is used when Nmap is unable to determine whether a port is closed or filtered. It is only used for the IP ID idle scan.</dl>
<h2>PORT SCANNING TECHNIQUES</h2>
<p> As a novice performing automotive repair, I can struggle for hours trying to fit my rudimentary tools (hammer, duct tape, wrench, etc.) to the task at hand. When I fail miserably and tow my jalopy to a real mechanic, he invariably fishes around in a huge tool chest until pulling out the perfect gizmo which makes the job seem effortless. The art of port scanning is similar. Experts understand the dozens of scan techniques and choose the appropriate one (or combination) for a given task. Inexperienced users and script kiddies, on the other hand, try to solve every problem with the default SYN scan. Since Nmap is free, the only barrier to port scanning mastery is knowledge. That certainly beats the automotive world, where it may take great skill to determine that you need a strut spring compressor, then you still have to pay thousands of dollars for it. </p>
<p> Most of the scan types are only available to privileged users. This is because they send and receive raw packets, which requires root access on Unix systems. Using an administrator account on Windows is recommended, though Nmap sometimes works for unprivileged users on that platform when Npcap has already been loaded into the OS. Requiring root privileges was a serious limitation when Nmap was released in 1997, as many users only had access to shared shell accounts. Now, the world is different. Computers are cheaper, far more people have always-on direct Internet access, and desktop Unix systems (including Linux and Mac OS X) are prevalent. A Windows version of Nmap is now available, allowing it to run on even more desktops. For all these reasons, users have less need to run Nmap from limited shared shell accounts. This is fortunate, as the privileged options make Nmap far more powerful and flexible. </p>
<p> While Nmap attempts to produce accurate results, keep in mind that all of its insights are based on packets returned by the target machines (or firewalls in front of them). Such hosts may be untrustworthy and send responses intended to confuse or mislead Nmap. Much more common are non-RFC-compliant hosts that do not respond as they should to Nmap probes. FIN, NULL, and Xmas scans are particularly susceptible to this problem. Such issues are specific to certain scan types and so are discussed in the individual scan type entries. </p>
<p> This section documents the dozen or so port scan techniques supported by Nmap. Only one method may be used at a time, except that UDP scan (<code>-sU</code>) and any one of the SCTP scan types (<code>-sY</code>, <code>-sZ</code>) may be combined with any one of the TCP scan types. As a memory aid, port scan type options are of the form <code>-s</code><i>C</i>, where <i>C</i> is a prominent character in the scan name, usually the first. The one exception to this is the deprecated FTP bounce scan (<code>-b</code>). By default, Nmap performs a SYN Scan, though it substitutes a connect scan if the user does not have proper privileges to send raw packets (requires root access on Unix). Of the scans listed in this section, unprivileged users can only execute connect and FTP bounce scans. </p>
<p> <code>-sS</code> (TCP SYN scan)</p>
<dl>
<dt>
<dd> SYN scan is the default and most popular scan option for good reasons. It can be performed quickly, scanning thousands of ports per second on a fast network not hampered by restrictive firewalls. It is also relatively unobtrusive and stealthy since it never completes TCP connections. SYN scan works against any compliant TCP stack rather than depending on idiosyncrasies of specific platforms as Nmap&#8217;s FIN/NULL/Xmas, Maimon and idle scans do. It also allows clear, reliable differentiation between the open, closed, and filtered states. </p>
<p> This technique is often referred to as half-open scanning, because you don&#8217;t open a full TCP connection. You send a SYN packet, as if you are going to open a real connection and then wait for a response. A SYN/ACK indicates the port is listening (open), while a RST (reset) is indicative of a non-listener. If no response is received after several retransmissions, the port is marked as filtered. The port is also marked filtered if an ICMP unreachable error (type 3, code 0, 1, 2, 3, 9, 10, or 13) is received. The port is also considered open if a SYN packet (without the ACK flag) is received in response. This can be due to an extremely rare TCP feature known as a simultaneous open or split handshake connection (see m[blue]<code><a rel="nofollow" href="https://nmap.org/misc/split-handshake.pdf">https://nmap.org/misc/split-handshake.pdf</a></code>m[]).</dl>
<p> <code>-sT</code> (TCP connect scan)</p>
<dl>
<dt>
<dd> TCP connect scan is the default TCP scan type when SYN scan is not an option. This is the case when a user does not have raw packet privileges. Instead of writing raw packets as most other scan types do, Nmap asks the underlying operating system to establish a connection with the target machine and port by issuing the <code>connect</code> system call. This is the same high-level system call that web browsers, P2P clients, and most other network-enabled applications use to establish a connection. It is part of a programming interface known as the Berkeley Sockets API. Rather than read raw packet responses off the wire, Nmap uses this API to obtain status information on each connection attempt. </p>
<p> When SYN scan is available, it is usually a better choice. Nmap has less control over the high level <code>connect</code> call than with raw packets, making it less efficient. The system call completes connections to open target ports rather than performing the half-open reset that SYN scan does. Not only does this take longer and require more packets to obtain the same information, but target machines are more likely to log the connection. A decent IDS will catch either, but most machines have no such alarm system. Many services on your average Unix system will add a note to syslog, and sometimes a cryptic error message, when Nmap connects and then closes the connection without sending data. Truly pathetic services crash when this happens, though that is uncommon. An administrator who sees a bunch of connection attempts in her logs from a single system should know that she has been connect scanned.</dl>
<p> <code>-sU</code> (UDP scans)</p>
<dl>
<dt>
<dd> While most popular services on the Internet run over the TCP protocol, m[blue]<code>UDP</code>m[]<font SIZE="-2">[6]</font> services are widely deployed. DNS, SNMP, and DHCP (registered ports 53, 161/162, and 67/68) are three of the most common. Because UDP scanning is generally slower and more difficult than TCP, some security auditors ignore these ports. This is a mistake, as exploitable UDP services are quite common and attackers certainly don&#8217;t ignore the whole protocol. Fortunately, Nmap can help inventory UDP ports. </p>
<p> UDP scan is activated with the <code>-sU</code> option. It can be combined with a TCP scan type such as SYN scan (<code>-sS</code>) to check both protocols during the same run. </p>
<p> UDP scan works by sending a UDP packet to every targeted port. For some common ports such as 53 and 161, a protocol-specific payload is sent to increase response rate, but for most ports the packet is empty unless the <code>&#8211;data</code>, <code>&#8211;data-string</code>, or <code>&#8211;data-length</code> options are specified. If an ICMP port unreachable error (type 3, code 3) is returned, the port is closed. Other ICMP unreachable errors (type 3, codes 0, 1, 2, 9, 10, or 13) mark the port as filtered. Occasionally, a service will respond with a UDP packet, proving that it is open. If no response is received after retransmissions, the port is classified as open|filtered. This means that the port could be open, or perhaps packet filters are blocking the communication. Version detection (<code>-sV</code>) can be used to help differentiate the truly open ports from the filtered ones. </p>
<p> A big challenge with UDP scanning is doing it quickly. Open and filtered ports rarely send any response, leaving Nmap to time out and then conduct retransmissions just in case the probe or response were lost. Closed ports are often an even bigger problem. They usually send back an ICMP port unreachable error. But unlike the RST packets sent by closed TCP ports in response to a SYN or connect scan, many hosts rate limit ICMP port unreachable messages by default. Linux and Solaris are particularly strict about this. For example, the Linux 2.4.20 kernel limits destination unreachable messages to one per second (in net/ipv4/icmp.c). </p>
<p> Nmap detects rate limiting and slows down accordingly to avoid flooding the network with useless packets that the target machine will drop. Unfortunately, a Linux-style limit of one packet per second makes a 65,536-port scan take more than 18 hours. Ideas for speeding your UDP scans up include scanning more hosts in parallel, doing a quick scan of just the popular ports first, scanning from behind the firewall, and using <code>&#8211;host-timeout</code> to skip slow hosts.</dl>
<p> <code>-sY</code> (SCTP INIT scan)</p>
<dl>
<dt>
<dd> m[blue]<code>SCTP</code>m[]<font SIZE="-2">[7]</font> is a relatively new alternative to the TCP and UDP protocols, combining most characteristics of TCP and UDP, and also adding new features like multi-homing and multi-streaming. It is mostly being used for SS7/SIGTRAN related services but has the potential to be used for other applications as well. SCTP INIT scan is the SCTP equivalent of a TCP SYN scan. It can be performed quickly, scanning thousands of ports per second on a fast network not hampered by restrictive firewalls. Like SYN scan, INIT scan is relatively unobtrusive and stealthy, since it never completes SCTP associations. It also allows clear, reliable differentiation between the open, closed, and filtered states. </p>
<p> This technique is often referred to as half-open scanning, because you don&#8217;t open a full SCTP association. You send an INIT chunk, as if you are going to open a real association and then wait for a response. An INIT-ACK chunk indicates the port is listening (open), while an ABORT chunk is indicative of a non-listener. If no response is received after several retransmissions, the port is marked as filtered. The port is also marked filtered if an ICMP unreachable error (type 3, code 0, 1, 2, 3, 9, 10, or 13) is received.</dl>
<p> <code>-sN</code>; <code>-sF</code>; <code>-sX</code> (TCP NULL, FIN, and Xmas scans)</p>
<dl>
<dt>
<dd> These three scan types (even more are possible with the <code>&#8211;scanflags</code> option described in the next section) exploit a subtle loophole in the m[blue]<code>TCP RFC</code>m[]<font SIZE="-2">[8]</font> to differentiate between open and closed ports. Page 65 of RFC 793 says that &#8220;if the [destination] port state is CLOSED &#8230;. an incoming segment not containing a RST causes a RST to be sent in response.&#8221; Then the next page discusses packets sent to open ports without the SYN, RST, or ACK bits set, stating that: &#8220;you are unlikely to get here, but if you do, drop the segment, and return.&#8221; </p>
<p> When scanning systems compliant with this RFC text, any packet not containing SYN, RST, or ACK bits will result in a returned RST if the port is closed and no response at all if the port is open. As long as none of those three bits are included, any combination of the other three (FIN, PSH, and URG) are OK. Nmap exploits this with three scan types: </p>
<p> Null scan (<code>-sN</code>)</p>
<dl>
<dt>
<dd> Does not set any bits (TCP flag header is 0)</dl>
<p> FIN scan (<code>-sF</code>)</p>
<dl>
<dt>
<dd> Sets just the TCP FIN bit.</dl>
<p> Xmas scan (<code>-sX</code>)</p>
<dl>
<dt>
<dd> Sets the FIN, PSH, and URG flags, lighting the packet up like a Christmas tree.</dl>
<p> These three scan types are exactly the same in behavior except for the TCP flags set in probe packets. If a RST packet is received, the port is considered closed, while no response means it is open|filtered. The port is marked filtered if an ICMP unreachable error (type 3, code 0, 1, 2, 3, 9, 10, or 13) is received. </p>
<p> The key advantage to these scan types is that they can sneak through certain non-stateful firewalls and packet filtering routers. Another advantage is that these scan types are a little more stealthy than even a SYN scan. Don&#8217;t count on this though&#8212;most modern IDS products can be configured to detect them. The big downside is that not all systems follow RFC 793 to the letter. A number of systems send RST responses to the probes regardless of whether the port is open or not. This causes all of the ports to be labeled closed. Major operating systems that do this are Microsoft Windows, many Cisco devices, BSDI, and IBM OS/400. This scan does work against most Unix-based systems though. Another downside of these scans is that they can&#8217;t distinguish open ports from certain filtered ones, leaving you with the response open|filtered.</dl>
<p> <code>-sA</code> (TCP ACK scan)</p>
<dl>
<dt>
<dd> This scan is different than the others discussed so far in that it never determines open (or even open|filtered) ports. It is used to map out firewall rulesets, determining whether they are stateful or not and which ports are filtered. </p>
<p> The ACK scan probe packet has only the ACK flag set (unless you use <code>&#8211;scanflags</code>). When scanning unfiltered systems, open and closed ports will both return a RST packet. Nmap then labels them as unfiltered, meaning that they are reachable by the ACK packet, but whether they are open or closed is undetermined. Ports that don&#8217;t respond, or send certain ICMP error messages back (type 3, code 0, 1, 2, 3, 9, 10, or 13), are labeled filtered.</dl>
<p> <code>-sW</code> (TCP Window scan)</p>
<dl>
<dt>
<dd> Window scan is exactly the same as ACK scan except that it exploits an implementation detail of certain systems to differentiate open ports from closed ones, rather than always printing unfiltered when a RST is returned. It does this by examining the TCP Window field of the RST packets returned. On some systems, open ports use a positive window size (even for RST packets) while closed ones have a zero window. So instead of always listing a port as unfiltered when it receives a RST back, Window scan lists the port as open or closed if the TCP Window value in that reset is positive or zero, respectively. </p>
<p> This scan relies on an implementation detail of a minority of systems out on the Internet, so you can&#8217;t always trust it. Systems that don&#8217;t support it will usually return all ports closed. Of course, it is possible that the machine really has no open ports. If most scanned ports are closed but a few common port numbers (such as 22, 25, 53) are filtered, the system is most likely susceptible. Occasionally, systems will even show the exact opposite behavior. If your scan shows 1,000 open ports and three closed or filtered ports, then those three may very well be the truly open ones.</dl>
<p> <code>-sM</code> (TCP Maimon scan)</p>
<dl>
<dt>
<dd> The Maimon scan is named after its discoverer, Uriel Maimon. He described the technique in Phrack Magazine issue #49 (November 1996). Nmap, which included this technique, was released two issues later. This technique is exactly the same as NULL, FIN, and Xmas scans, except that the probe is FIN/ACK. According to m[blue]<code>RFC 793</code>m[]<font SIZE="-2">[8]</font> (TCP), a RST packet should be generated in response to such a probe whether the port is open or closed. However, Uriel noticed that many BSD-derived systems simply drop the packet if the port is open.</dl>
<p> <code>&#8211;scanflags</code> (Custom TCP scan)</p>
<dl>
<dt>
<dd> Truly advanced Nmap users need not limit themselves to the canned scan types offered. The <code>&#8211;scanflags</code> option allows you to design your own scan by specifying arbitrary TCP flags. Let your creative juices flow, while evading intrusion detection systems whose vendors simply paged through the Nmap man page adding specific rules! </p>
<p> The <code>&#8211;scanflags</code> argument can be a numerical flag value such as 9 (PSH and FIN), but using symbolic names is easier. Just mash together any combination of URG, ACK, PSH, RST, SYN, and FIN. For example, <code>&#8211;scanflags URGACKPSHRSTSYNFIN</code> sets everything, though it&#8217;s not very useful for scanning. The order these are specified in is irrelevant. </p>
<p> In addition to specifying the desired flags, you can specify a TCP scan type (such as <code>-sA</code> or <code>-sF</code>). That base type tells Nmap how to interpret responses. For example, a SYN scan considers no-response to indicate a filtered port, while a FIN scan treats the same as open|filtered. Nmap will behave the same way it does for the base scan type, except that it will use the TCP flags you specify instead. If you don&#8217;t specify a base type, SYN scan is used.</dl>
<p> <code>-sZ</code> (SCTP COOKIE ECHO scan)</p>
<dl>
<dt>
<dd> SCTP COOKIE ECHO scan is a more advanced SCTP scan. It takes advantage of the fact that SCTP implementations should silently drop packets containing COOKIE ECHO chunks on open ports, but send an ABORT if the port is closed. The advantage of this scan type is that it is not as obvious a port scan than an INIT scan. Also, there may be non-stateful firewall rulesets blocking INIT chunks, but not COOKIE ECHO chunks. Don&#8217;t be fooled into thinking that this will make a port scan invisible; a good IDS will be able to detect SCTP COOKIE ECHO scans too. The downside is that SCTP COOKIE ECHO scans cannot differentiate between open and filtered ports, leaving you with the state open|filtered in both cases.</dl>
<p> <code>-sI </code><i>zombie host</i><code>[:</code><i>probeport</i>] (idle scan)</p>
<dl>
<dt>
<dd> This advanced scan method allows for a truly blind TCP port scan of the target (meaning no packets are sent to the target from your real IP address). Instead, a unique side-channel attack exploits predictable IP fragmentation ID sequence generation on the zombie host to glean information about the open ports on the target. IDS systems will display the scan as coming from the zombie machine you specify (which must be up and meet certain criteria). This fascinating scan type is too complex to fully describe in this reference guide, so I wrote and posted an informal paper with full details at m[blue]<code><a rel="nofollow" href="https://nmap.org/book/idlescan.html">https://nmap.org/book/idlescan.html</a></code>m[]. </p>
<p> Besides being extraordinarily stealthy (due to its blind nature), this scan type permits mapping out IP-based trust relationships between machines. The port listing shows open ports <i>from the perspective of the zombie host.</i> So you can try scanning a target using various zombies that you think might be trusted (via router/packet filter rules). </p>
<p> You can add a colon followed by a port number to the zombie host if you wish to probe a particular port on the zombie for IP ID changes. Otherwise Nmap will use the port it uses by default for TCP pings (80).</dl>
<p> <code>-sO</code> (IP protocol scan)</p>
<dl>
<dt>
<dd> IP protocol scan allows you to determine which IP protocols (TCP, ICMP, IGMP, etc.) are supported by target machines. This isn&#8217;t technically a port scan, since it cycles through IP protocol numbers rather than TCP or UDP port numbers. Yet it still uses the <code>-p</code> option to select scanned protocol numbers, reports its results within the normal port table format, and even uses the same underlying scan engine as the true port scanning methods. So it is close enough to a port scan that it belongs here. </p>
<p> Besides being useful in its own right, protocol scan demonstrates the power of open-source software. While the fundamental idea is pretty simple, I had not thought to add it nor received any requests for such functionality. Then in the summer of 2000, Gerhard Rieger conceived the idea, wrote an excellent patch implementing it, and sent it to the announce mailing list (then called nmap-hackers). I incorporated that patch into the Nmap tree and released a new version the next day. Few pieces of commercial software have users enthusiastic enough to design and contribute their own improvements! </p>
<p> Protocol scan works in a similar fashion to UDP scan. Instead of iterating through the port number field of a UDP packet, it sends IP packet headers and iterates through the eight-bit IP protocol field. The headers are usually empty, containing no data and not even the proper header for the claimed protocol. The exceptions are TCP, UDP, ICMP, SCTP, and IGMP. A proper protocol header for those is included since some systems won&#8217;t send them otherwise and because Nmap already has functions to create them. Instead of watching for ICMP port unreachable messages, protocol scan is on the lookout for ICMP <i>protocol</i> unreachable messages. If Nmap receives any response in any protocol from the target host, Nmap marks that protocol as open. An ICMP protocol unreachable error (type 3, code 2) causes the protocol to be marked as closed while port unreachable (type 3, code 3) marks the protocol open. Other ICMP unreachable errors (type 3, code 0, 1, 9, 10, or 13) cause the protocol to be marked filtered (though they prove that ICMP is open at the same time). If no response is received after retransmissions, the protocol is marked open|filtered</dl>
<p> <code>-b </code><i>FTP relay host</i> (FTP bounce scan)</p>
<dl>
<dt>
<dd> An interesting feature of the FTP protocol (m[blue]<code>RFC 959</code>m[]<font SIZE="-2">[9]</font>) is support for so-called proxy FTP connections. This allows a user to connect to one FTP server, then ask that files be sent to a third-party server. Such a feature is ripe for abuse on many levels, so most servers have ceased supporting it. One of the abuses this feature allows is causing the FTP server to port scan other hosts. Simply ask the FTP server to send a file to each interesting port of a target host in turn. The error message will describe whether the port is open or not. This is a good way to bypass firewalls because organizational FTP servers are often placed where they have more access to other internal hosts than any old Internet host would. Nmap supports FTP bounce scan with the <code>-b</code> option. It takes an argument of the form <i>username</i>:<i>password</i>@<i>server</i>:<i>port</i>. <i>Server</i> is the name or IP address of a vulnerable FTP server. As with a normal URL, you may omit <i>username</i>:<i>password</i>, in which case anonymous login credentials (user: anonymous password:-wwwuser@) are used. The port number (and preceding colon) may be omitted as well, in which case the default FTP port (21) on <i>server</i> is used. </p>
<p> This vulnerability was widespread in 1997 when Nmap was released, but has largely been fixed. Vulnerable servers are still around, so it is worth trying when all else fails. If bypassing a firewall is your goal, scan the target network for port 21 (or even for any FTP services if you scan all ports with version detection) and use the ftp-bounce NSE script. Nmap will tell you whether the host is vulnerable or not. If you are just trying to cover your tracks, you don&#8217;t need to (and, in fact, shouldn&#8217;t) limit yourself to hosts on the target network. Before you go scanning random Internet addresses for vulnerable FTP servers, consider that sysadmins may not appreciate you abusing their servers in this way.</dl>
<h2>PORT SPECIFICATION AND SCAN ORDER</h2>
<p> In addition to all of the scan methods discussed previously, Nmap offers options for specifying which ports are scanned and whether the scan order is randomized or sequential. By default, Nmap scans the most common 1,000 ports for each protocol. </p>
<p> <code>-p </code><i>port ranges</i> (Only scan specified ports)</p>
<dl>
<dt>
<dd> This option specifies which ports you want to scan and overrides the default. Individual port numbers are OK, as are ranges separated by a hyphen (e.g. 1-1023). The beginning and/or end values of a range may be omitted, causing Nmap to use 1 and 65535, respectively. So you can specify <code>-p-</code> to scan ports from 1 through 65535. Scanning port zero is allowed if you specify it explicitly. For IP protocol scanning (<code>-sO</code>), this option specifies the protocol numbers you wish to scan for (0-255). </p>
<p> When scanning a combination of protocols (e.g. TCP and UDP), you can specify a particular protocol by preceding the port numbers by T: for TCP, U: for UDP, S: for SCTP, or P: for IP Protocol. The qualifier lasts until you specify another qualifier. For example, the argument <code>-p U:53,111,137,T:21-25,80,139,8080</code> would scan UDP ports 53, 111,and 137, as well as the listed TCP ports. Note that to scan both UDP and TCP, you have to specify <code>-sU</code> and at least one TCP scan type (such as <code>-sS</code>, <code>-sF</code>, or <code>-sT</code>). If no protocol qualifier is given, the port numbers are added to all protocol lists. Ports can also be specified by name according to what the port is referred to in the nmap-services. You can even use the wildcards * and ? with the names. For example, to scan FTP and all ports whose names begin with &#8220;http&#8221;, use <code>-p ftp,http*</code>. Be careful about shell expansions and quote the argument to <code>-p</code> if unsure. </p>
<p> Ranges of ports can be surrounded by square brackets to indicate ports inside that range that appear in nmap-services. For example, the following will scan all ports in nmap-services equal to or below 1024: <code>-p [-1024]</code>. Be careful with shell expansions and quote the argument to <code>-p</code> if unsure.</dl>
<p> <code>&#8211;exclude-ports </code><i>port ranges</i> (Exclude the specified ports from scanning)</p>
<dl>
<dt>
<dd> This option specifies which ports you do want Nmap to exclude from scanning. The <i>port ranges</i> are specified similar to <code>-p</code>. For IP protocol scanning (<code>-sO</code>), this option specifies the protocol numbers you wish to exclude (0-255). </p>
<p> When ports are asked to be excluded, they are excluded from all types of scans (i.e. they will not be scanned under any circumstances). This also includes the discovery phase.</dl>
<p> <code>-F</code> (Fast (limited port) scan)</p>
<dl>
<dt>
<dd> Specifies that you wish to scan fewer ports than the default. Normally Nmap scans the most common 1,000 ports for each scanned protocol. With <code>-F</code>, this is reduced to 100. </p>
<p> Nmap needs an nmap-services file with frequency information in order to know which ports are the most common. If port frequency information isn&#8217;t available, perhaps because of the use of a custom nmap-services file, Nmap scans all named ports plus ports 1-1024. In that case, <code>-F</code> means to scan only ports that are named in the services file.</dl>
<p> <code>-r</code> (Don&#8217;t randomize ports)</p>
<dl>
<dt>
<dd> By default, Nmap randomizes the scanned port order (except that certain commonly accessible ports are moved near the beginning for efficiency reasons). This randomization is normally desirable, but you can specify <code>-r</code> for sequential (sorted from lowest to highest) port scanning instead.</dl>
<p> <code>&#8211;port-ratio </code><i>ratio</i><code>&lt;decimal number between 0 and 1&gt;</code></p>
<dl>
<dt>
<dd> Scans all ports in nmap-services file with a ratio greater than the one given. <i>ratio</i> must be between 0.0 and 1.0.</dl>
<p> <code>&#8211;top-ports </code><i>n</i></p>
<dl>
<dt>
<dd> Scans the <i>n</i> highest-ratio ports found in nmap-services file after excluding all ports specified by <code>&#8211;exclude-ports</code>. <i>n</i> must be 1 or greater.</dl>
<h2>SERVICE AND VERSION DETECTION</h2>
<p> Point Nmap at a remote machine and it might tell you that ports 25/tcp, 80/tcp, and 53/udp are open. Using its nmap-services database of about 2,200 well-known services, Nmap would report that those ports probably correspond to a mail server (SMTP), web server (HTTP), and name server (DNS) respectively. This lookup is usually accurate&#8212;the vast majority of daemons listening on TCP port 25 are, in fact, mail servers. However, you should not bet your security on this! People can and do run services on strange ports. </p>
<p> Even if Nmap is right, and the hypothetical server above is running SMTP, HTTP, and DNS servers, that is not a lot of information. When doing vulnerability assessments (or even simple network inventories) of your companies or clients, you really want to know which mail and DNS servers and versions are running. Having an accurate version number helps dramatically in determining which exploits a server is vulnerable to. Version detection helps you obtain this information. </p>
<p> After TCP and/or UDP ports are discovered using one of the other scan methods, version detection interrogates those ports to determine more about what is actually running. The nmap-service-probes database contains probes for querying various services and match expressions to recognize and parse responses. Nmap tries to determine the service protocol (e.g. FTP, SSH, Telnet, HTTP), the application name (e.g. ISC BIND, Apache httpd, Solaris telnetd), the version number, hostname, device type (e.g. printer, router), the OS family (e.g. Windows, Linux). When possible, Nmap also gets the Common Platform Enumeration (CPE) representation of this information. Sometimes miscellaneous details like whether an X server is open to connections, the SSH protocol version, or the KaZaA user name, are available. Of course, most services don&#8217;t provide all of this information. If Nmap was compiled with OpenSSL support, it will connect to SSL servers to deduce the service listening behind that encryption layer. Some UDP ports are left in the open|filtered state after a UDP port scan is unable to determine whether the port is open or filtered. Version detection will try to elicit a response from these ports (just as it does with open ports), and change the state to open if it succeeds. open|filtered TCP ports are treated the same way. Note that the Nmap <code>-A</code> option enables version detection among other things. A paper documenting the workings, usage, and customization of version detection is available at m[blue]<code><a rel="nofollow" href="https://nmap.org/book/vscan.html">https://nmap.org/book/vscan.html</a></code>m[]. </p>
<p> When RPC services are discovered, the Nmap RPC grinder is automatically used to determine the RPC program and version numbers. It takes all the TCP/UDP ports detected as RPC and floods them with SunRPC program NULL commands in an attempt to determine whether they are RPC ports, and if so, what program and version number they serve up. Thus you can effectively obtain the same info as <code>rpcinfo -p</code> even if the target&#8217;s portmapper is behind a firewall (or protected by TCP wrappers). Decoys do not currently work with RPC scan. </p>
<p> When Nmap receives responses from a service but cannot match them to its database, it prints out a special fingerprint and a URL for you to submit if to if you know for sure what is running on the port. Please take a couple minutes to make the submission so that your find can benefit everyone. Thanks to these submissions, Nmap has about 6,500 pattern matches for more than 650 protocols such as SMTP, FTP, HTTP, etc. </p>
<p> Version detection is enabled and controlled with the following options: </p>
<p> <code>-sV</code> (Version detection)</p>
<dl>
<dt>
<dd> Enables version detection, as discussed above. Alternatively, you can use <code>-A</code>, which enables version detection among other things. </p>
<p> <code>-sR</code> is an alias for <code>-sV</code>. Prior to March 2011, it was used to active the RPC grinder separately from version detection, but now these options are always combined.</dl>
<p> <code>&#8211;allports</code> (Don&#8217;t exclude any ports from version detection)</p>
<dl>
<dt>
<dd> By default, Nmap version detection skips TCP port 9100 because some printers simply print anything sent to that port, leading to dozens of pages of HTTP GET requests, binary SSL session requests, etc. This behavior can be changed by modifying or removing the Exclude directive in nmap-service-probes, or you can specify <code>&#8211;allports</code> to scan all ports regardless of any Exclude directive.</dl>
<p> <code>&#8211;version-intensity </code><i>intensity</i> (Set version scan intensity)</p>
<dl>
<dt>
<dd> When performing a version scan (<code>-sV</code>), Nmap sends a series of probes, each of which is assigned a rarity value between one and nine. The lower-numbered probes are effective against a wide variety of common services, while the higher-numbered ones are rarely useful. The intensity level specifies which probes should be applied. The higher the number, the more likely it is the service will be correctly identified. However, high intensity scans take longer. The intensity must be between 0 and 9. The default is 7. When a probe is registered to the target port via the nmap-service-probes ports directive, that probe is tried regardless of intensity level. This ensures that the DNS probes will always be attempted against any open port 53, the SSL probe will be done against 443, etc.</dl>
<p> <code>&#8211;version-light</code> (Enable light mode)</p>
<dl>
<dt>
<dd> This is a convenience alias for <code>&#8211;version-intensity 2</code>. This light mode makes version scanning much faster, but it is slightly less likely to identify services.</dl>
<p> <code>&#8211;version-all</code> (Try every single probe)</p>
<dl>
<dt>
<dd> An alias for <code>&#8211;version-intensity 9</code>, ensuring that every single probe is attempted against each port.</dl>
<p> <code>&#8211;version-trace</code> (Trace version scan activity)</p>
<dl>
<dt>
<dd> This causes Nmap to print out extensive debugging info about what version scanning is doing. It is a subset of what you get with <code>&#8211;packet-trace</code>.</dl>
<h2>OS DETECTION</h2>
<p> One of Nmap&#8217;s best-known features is remote OS detection using TCP/IP stack fingerprinting. Nmap sends a series of TCP and UDP packets to the remote host and examines practically every bit in the responses. After performing dozens of tests such as TCP ISN sampling, TCP options support and ordering, IP ID sampling, and the initial window size check, Nmap compares the results to its nmap-os-db database of more than 2,600 known OS fingerprints and prints out the OS details if there is a match. Each fingerprint includes a freeform textual description of the OS, and a classification which provides the vendor name (e.g. Sun), underlying OS (e.g. Solaris), OS generation (e.g. 10), and device type (general purpose, router, switch, game console, etc). Most fingerprints also have a Common Platform Enumeration (CPE) representation, like cpe:/o:linux:linux_kernel:2.6. </p>
<p> If Nmap is unable to guess the OS of a machine, and conditions are good (e.g. at least one open port and one closed port were found), Nmap will provide a URL you can use to submit the fingerprint if you know (for sure) the OS running on the machine. By doing this you contribute to the pool of operating systems known to Nmap and thus it will be more accurate for everyone. </p>
<p> OS detection enables some other tests which make use of information that is gathered during the process anyway. One of these is TCP Sequence Predictability Classification. This measures approximately how hard it is to establish a forged TCP connection against the remote host. It is useful for exploiting source-IP based trust relationships (rlogin, firewall filters, etc) or for hiding the source of an attack. This sort of spoofing is rarely performed any more, but many machines are still vulnerable to it. The actual difficulty number is based on statistical sampling and may fluctuate. It is generally better to use the English classification such as &#8220;worthy challenge&#8221; or &#8220;trivial joke&#8221;. This is only reported in normal output in verbose (<code>-v</code>) mode. When verbose mode is enabled along with <code>-O</code>, IP ID sequence generation is also reported. Most machines are in the &#8220;incremental&#8221; class, which means that they increment the ID field in the IP header for each packet they send. This makes them vulnerable to several advanced information gathering and spoofing attacks. </p>
<p> Another bit of extra information enabled by OS detection is a guess at a target&#8217;s uptime. This uses the TCP timestamp option (m[blue]<code>RFC 1323</code>m[]<font SIZE="-2">[10]</font>) to guess when a machine was last rebooted. The guess can be inaccurate due to the timestamp counter not being initialized to zero or the counter overflowing and wrapping around, so it is printed only in verbose mode. </p>
<p> A paper documenting the workings, usage, and customization of OS detection is available at m[blue]<code><a rel="nofollow" href="https://nmap.org/book/osdetect.html">https://nmap.org/book/osdetect.html</a></code>m[]. </p>
<p> OS detection is enabled and controlled with the following options: </p>
<p> <code>-O</code> (Enable OS detection)</p>
<dl>
<dt>
<dd> Enables OS detection, as discussed above. Alternatively, you can use <code>-A</code> to enable OS detection along with other things.</dl>
<p> <code>&#8211;osscan-limit</code> (Limit OS detection to promising targets)</p>
<dl>
<dt>
<dd> OS detection is far more effective if at least one open and one closed TCP port are found. Set this option and Nmap will not even try OS detection against hosts that do not meet this criteria. This can save substantial time, particularly on <code>-Pn</code> scans against many hosts. It only matters when OS detection is requested with <code>-O</code> or <code>-A</code>.</dl>
<p> <code>&#8211;osscan-guess</code>; <code>&#8211;fuzzy</code> (Guess OS detection results)</p>
<dl>
<dt>
<dd> When Nmap is unable to detect a perfect OS match, it sometimes offers up near-matches as possibilities. The match has to be very close for Nmap to do this by default. Either of these (equivalent) options make Nmap guess more aggressively. Nmap will still tell you when an imperfect match is printed and display its confidence level (percentage) for each guess.</dl>
<p> <code>&#8211;max-os-tries</code> (Set the maximum number of OS detection tries against a target)</p>
<dl>
<dt>
<dd> When Nmap performs OS detection against a target and fails to find a perfect match, it usually repeats the attempt. By default, Nmap tries five times if conditions are favorable for OS fingerprint submission, and twice when conditions aren&#8217;t so good. Specifying a lower <code>&#8211;max-os-tries</code> value (such as 1) speeds Nmap up, though you miss out on retries which could potentially identify the OS. Alternatively, a high value may be set to allow even more retries when conditions are favorable. This is rarely done, except to generate better fingerprints for submission and integration into the Nmap OS database.</dl>
<h2>NMAP SCRIPTING ENGINE (NSE)</h2>
<p> The Nmap Scripting Engine (NSE) is one of Nmap&#8217;s most powerful and flexible features. It allows users to write (and share) simple scripts (using the m[blue]<code>Lua programming language</code>m[]<font SIZE="-2">[11]</font> </p>
<p> ) to automate a wide variety of networking tasks. Those scripts are executed in parallel with the speed and efficiency you expect from Nmap. Users can rely on the growing and diverse set of scripts distributed with Nmap, or write their own to meet custom needs. </p>
<p> Tasks we had in mind when creating the system include network discovery, more sophisticated version detection, vulnerability detection. NSE can even be used for vulnerability exploitation. </p>
<p> To reflect those different uses and to simplify the choice of which scripts to run, each script contains a field associating it with one or more categories. Currently defined categories are auth, broadcast, default. discovery, dos, exploit, external, fuzzer, intrusive, malware, safe, version, and vuln. These are all described at m[blue]<code><a rel="nofollow" href="https://nmap.org/book/nse-usage.html#nse-categories">https://nmap.org/book/nse-usage.html#nse-categories</a></code>m[]. </p>
<p> Scripts are not run in a sandbox and thus could accidentally or maliciously damage your system or invade your privacy. Never run scripts from third parties unless you trust the authors or have carefully audited the scripts yourself. </p>
<p> The Nmap Scripting Engine is described in detail at m[blue]<code><a rel="nofollow" href="https://nmap.org/book/nse.html">https://nmap.org/book/nse.html</a></code>m[] </p>
<p> and is controlled by the following options: </p>
<p> <code>-sC</code></p>
<dl>
<dt>
<dd> Performs a script scan using the default set of scripts. It is equivalent to <code>&#8211;script=default</code>. Some of the scripts in this category are considered intrusive and should not be run against a target network without permission.</dl>
<p> <code>&#8211;script </code><i>filename</i><code>|</code><i>category</i><code>|</code><i>directory</i><code>|</code><i>expression</i><code>[,&#8230;]</code></p>
<dl>
<dt>
<dd> Runs a script scan using the comma-separated list of filenames, script categories, and directories. Each element in the list may also be a Boolean expression describing a more complex set of scripts. Each element is interpreted first as an expression, then as a category, and finally as a file or directory name. </p>
<p> There are two special features for advanced users only. One is to prefix script names and expressions with + to force them to run even if they normally wouldn&#8217;t (e.g. the relevant service wasn&#8217;t detected on the target port). The other is that the argument all may be used to specify every script in Nmap&#8217;s database. Be cautious with this because NSE contains dangerous scripts such as exploits, brute force authentication crackers, and denial of service attacks. </p>
<p> File and directory names may be relative or absolute. Absolute names are used directly. Relative paths are looked for in the scripts of each of the following places until found:</p>
<dl>
<dt>
<dd> <code>&#8211;datadir</code></dl>
<dl>
<dt>
<dd> <code>$NMAPDIR</code></dl>
<dl>
<dt>
<dd> ~/.nmap (not searched on Windows)</dl>
<dl>
<dt>
<dd> <i>HOME</i>\AppData\Roaming
map (only on Windows)</dl>
<dl>
<dt>
<dd> the directory containing the nmap executable</dl>
<dl>
<dt>
<dd> the directory containing the nmap executable, followed by ../share/nmap</dl>
<dl>
<dt>
<dd> <i>NMAPDATADIR</i></dl>
<dl>
<dt>
<dd> the current directory.</dl>
<p> When a directory name is given, Nmap loads every file in the directory whose name ends with .nse. All other files are ignored and directories are not searched recursively. When a filename is given, it does not have to have the .nse extension; it will be added automatically if necessary. Nmap scripts are stored in a scripts subdirectory of the Nmap data directory by default (see m[blue]<code><a rel="nofollow" href="https://nmap.org/book/data-files.html">https://nmap.org/book/data-files.html</a></code>m[]). </p>
<p> For efficiency, scripts are indexed in a database stored in scripts/script.db, which lists the category or categories in which each script belongs. When referring to scripts from script.db by name, you can use a shell-style &#8216;*&#8217; wildcard. </p>
<p> <code>nmap &#8211;script &quot;http-*&quot;</code></p>
<dl>
<dt>
<dd> Loads all scripts whose name starts with http-, such as http-auth and http-open-proxy. The argument to <code>&#8211;script</code> had to be in quotes to protect the wildcard from the shell.</dl>
<p> More complicated script selection can be done using the and, or, and not operators to build Boolean expressions. The operators have the same m[blue]<code>precedence</code>m[]<font SIZE="-2">[12]</font> as in Lua: not is the highest, followed by and and then or. You can alter precedence by using parentheses. Because expressions contain space characters it is necessary to quote them. </p>
<p> <code>nmap &#8211;script &quot;not intrusive&quot;</code></p>
<dl>
<dt>
<dd> Loads every script except for those in the intrusive category.</dl>
<p> <code>nmap &#8211;script &quot;default or safe&quot;</code></p>
<dl>
<dt>
<dd> This is functionally equivalent to <code>nmap &#8211;script &quot;default,safe&quot;</code>. It loads all scripts that are in the default category or the safe category or both.</dl>
<p> <code>nmap &#8211;script &quot;default and safe&quot;</code></p>
<dl>
<dt>
<dd> Loads those scripts that are in <i>both</i> the default and safe categories.</dl>
<p> <code>nmap &#8211;script &quot;(default or safe or intrusive) and not http-*&quot;</code></p>
<dl>
<dt>
<dd> Loads scripts in the default, safe, or intrusive categories, except for those whose names start with http-.</dl>
</dl>
<p> <code>&#8211;script-args </code><i>n1</i><code>=</code><i>v1</i><code>,</code><i>n2</i><code>={</code><i>n3</i><code>=</code><i>v3</i><code>},</code><i>n4</i><code>={</code><i>v4</i><code>,</code><i>v5</i><code>}</code></p>
<dl>
<dt>
<dd> Lets you provide arguments to NSE scripts. Arguments are a comma-separated list of name=value pairs. Names and values may be strings not containing whitespace or the characters &#8216;{&#8216;, &#8216;}&#8217;, &#8216;=&#8217;, or &#8216;,&#8217;. To include one of these characters in a string, enclose the string in single or double quotes. Within a quoted string, &#8216;\&#8217; escapes a quote. A backslash is only used to escape quotation marks in this special case; in all other cases a backslash is interpreted literally. Values may also be tables enclosed in {}, just as in Lua. A table may contain simple string values or more name-value pairs, including nested tables. Many scripts qualify their arguments with the script name, as in xmpp-info.server_name. You may use that full qualified version to affect just the specified script, or you may pass the unqualified version (server_name in this case) to affect all scripts using that argument name. A script will first check for its fully qualified argument name (the name specified in its documentation) before it accepts an unqualified argument name. A complex example of script arguments is <code>&#8211;script-args &#8216;user=foo,pass=&quot;,{}=bar&quot;,whois={whodb=nofollow+ripe},xmpp-info.server_name=localhost&#8217;</code>. The online NSE Documentation Portal at m[blue]<code><a rel="nofollow" href="https://nmap.org/nsedoc/">https://nmap.org/nsedoc/</a></code>m[] lists the arguments that each script accepts.</dl>
<p> <code>&#8211;script-args-file </code><i>filename</i></p>
<dl>
<dt>
<dd> Lets you load arguments to NSE scripts from a file. Any arguments on the command line supersede ones in the file. The file can be an absolute path, or a path relative to Nmap&#8217;s usual search path (NMAPDIR, etc.) Arguments can be comma-separated or newline-separated, but otherwise follow the same rules as for <code>&#8211;script-args</code>, without requiring special quoting and escaping, since they are not parsed by the shell.</dl>
<p> <code>&#8211;script-help </code><i>filename</i><code>|</code><i>category</i><code>|</code><i>directory</i><code>|</code><i>expression</i><code>|all</code><code>[,&#8230;]</code></p>
<dl>
<dt>
<dd> Shows help about scripts. For each script matching the given specification, Nmap prints the script name, its categories, and its description. The specifications are the same as those accepted by <code>&#8211;script</code>; so for example if you want help about the ftp-anon script, you would run <code>nmap &#8211;script-help ftp-anon</code>. In addition to getting help for individual scripts, you can use this as a preview of what scripts will be run for a specification, for example with <code>nmap &#8211;script-help default</code>.</dl>
<p> <code>&#8211;script-trace</code></p>
<dl>
<dt>
<dd> This option does what <code>&#8211;packet-trace</code> does, just one ISO layer higher. If this option is specified all incoming and outgoing communication performed by a script is printed. The displayed information includes the communication protocol, the source, the target and the transmitted data. If more than 5% of all transmitted data is not printable, then the trace output is in a hex dump format. Specifying <code>&#8211;packet-trace</code> enables script tracing too.</dl>
<p> <code>&#8211;script-updatedb</code></p>
<dl>
<dt>
<dd> This option updates the script database found in scripts/script.db which is used by Nmap to determine the available default scripts and categories. It is only necessary to update the database if you have added or removed NSE scripts from the default scripts directory or if you have changed the categories of any script. This option is generally used by itself: <code>nmap &#8211;script-updatedb</code>.</dl>
<h2>TIMING AND PERFORMANCE</h2>
<p> One of my highest Nmap development priorities has always been performance. A default scan (<code>nmap </code><i>hostname</i>) of a host on my local network takes a fifth of a second. That is barely enough time to blink, but adds up when you are scanning hundreds or thousands of hosts. Moreover, certain scan options such as UDP scanning and version detection can increase scan times substantially. So can certain firewall configurations, particularly response rate limiting. While Nmap utilizes parallelism and many advanced algorithms to accelerate these scans, the user has ultimate control over how Nmap runs. Expert users carefully craft Nmap commands to obtain only the information they care about while meeting their time constraints. </p>
<p> Techniques for improving scan times include omitting non-critical tests, and upgrading to the latest version of Nmap (performance enhancements are made frequently). Optimizing timing parameters can also make a substantial difference. Those options are listed below. </p>
<p> Some options accept a time parameter. This is specified in seconds by default, though you can append &#8216;ms&#8217;, &#8216;s&#8217;, &#8216;m&#8217;, or &#8216;h&#8217; to the value to specify milliseconds, seconds, minutes, or hours. So the <code>&#8211;host-timeout</code> arguments 900000ms, 900, 900s, and 15m all do the same thing. </p>
<p> <code>&#8211;min-hostgroup </code><i>numhosts</i>; <code>&#8211;max-hostgroup </code><i>numhosts</i> (Adjust parallel scan group sizes)</p>
<dl>
<dt>
<dd> Nmap has the ability to port scan or version scan multiple hosts in parallel. Nmap does this by dividing the target IP space into groups and then scanning one group at a time. In general, larger groups are more efficient. The downside is that host results can&#8217;t be provided until the whole group is finished. So if Nmap started out with a group size of 50, the user would not receive any reports (except for the updates offered in verbose mode) until the first 50 hosts are completed. </p>
<p> By default, Nmap takes a compromise approach to this conflict. It starts out with a group size as low as five so the first results come quickly and then increases the groupsize to as high as 1024. The exact default numbers depend on the options given. For efficiency reasons, Nmap uses larger group sizes for UDP or few-port TCP scans. </p>
<p> When a maximum group size is specified with <code>&#8211;max-hostgroup</code>, Nmap will never exceed that size. Specify a minimum size with <code>&#8211;min-hostgroup</code> and Nmap will try to keep group sizes above that level. Nmap may have to use smaller groups than you specify if there are not enough target hosts left on a given interface to fulfill the specified minimum. Both may be set to keep the group size within a specific range, though this is rarely desired. </p>
<p> These options do not have an effect during the host discovery phase of a scan. This includes plain ping scans (<code>-sn</code>). Host discovery always works in large groups of hosts to improve speed and accuracy. </p>
<p> The primary use of these options is to specify a large minimum group size so that the full scan runs more quickly. A common choice is 256 to scan a network in Class C sized chunks. For a scan with many ports, exceeding that number is unlikely to help much. For scans of just a few port numbers, host group sizes of 2048 or more may be helpful.</dl>
<p> <code>&#8211;min-parallelism </code><i>numprobes</i>; <code>&#8211;max-parallelism </code><i>numprobes</i> (Adjust probe parallelization)</p>
<dl>
<dt>
<dd> These options control the total number of probes that may be outstanding for a host group. They are used for port scanning and host discovery. By default, Nmap calculates an ever-changing ideal parallelism based on network performance. If packets are being dropped, Nmap slows down and allows fewer outstanding probes. The ideal probe number slowly rises as the network proves itself worthy. These options place minimum or maximum bounds on that variable. By default, the ideal parallelism can drop to one if the network proves unreliable and rise to several hundred in perfect conditions. </p>
<p> The most common usage is to set <code>&#8211;min-parallelism</code> to a number higher than one to speed up scans of poorly performing hosts or networks. This is a risky option to play with, as setting it too high may affect accuracy. Setting this also reduces Nmap&#8217;s ability to control parallelism dynamically based on network conditions. A value of 10 might be reasonable, though I only adjust this value as a last resort. </p>
<p> The <code>&#8211;max-parallelism</code> option is sometimes set to one to prevent Nmap from sending more than one probe at a time to hosts. The <code>&#8211;scan-delay</code> option, discussed later, is another way to do this.</dl>
<p> <code>&#8211;min-rtt-timeout </code><i>time</i>, <code>&#8211;max-rtt-timeout </code><i>time</i>, <code>&#8211;initial-rtt-timeout </code><i>time</i> (Adjust probe timeouts)</p>
<dl>
<dt>
<dd> Nmap maintains a running timeout value for determining how long it will wait for a probe response before giving up or retransmitting the probe. This is calculated based on the response times of previous probes. </p>
<p> If the network latency shows itself to be significant and variable, this timeout can grow to several seconds. It also starts at a conservative (high) level and may stay that way for a while when Nmap scans unresponsive hosts. </p>
<p> Specifying a lower <code>&#8211;max-rtt-timeout</code> and <code>&#8211;initial-rtt-timeout</code> than the defaults can cut scan times significantly. This is particularly true for pingless (<code>-Pn</code>) scans, and those against heavily filtered networks. Don&#8217;t get too aggressive though. The scan can end up taking longer if you specify such a low value that many probes are timing out and retransmitting while the response is in transit. </p>
<p> If all the hosts are on a local network, 100 milliseconds (<code>&#8211;max-rtt-timeout 100ms</code>) is a reasonable aggressive value. If routing is involved, ping a host on the network first with the ICMP ping utility, or with a custom packet crafter such as Nping that is more likely to get through a firewall. Look at the maximum round trip time out of ten packets or so. You might want to double that for the <code>&#8211;initial-rtt-timeout</code> and triple or quadruple it for the <code>&#8211;max-rtt-timeout</code>. I generally do not set the maximum RTT below 100 ms, no matter what the ping times are. Nor do I exceed 1000 ms. </p>
<p> <code>&#8211;min-rtt-timeout</code> is a rarely used option that could be useful when a network is so unreliable that even Nmap&#8217;s default is too aggressive. Since Nmap only reduces the timeout down to the minimum when the network seems to be reliable, this need is unusual and should be reported as a bug to the nmap-dev mailing list.</dl>
<p> <code>&#8211;max-retries </code><i>numtries</i> (Specify the maximum number of port scan probe retransmissions)</p>
<dl>
<dt>
<dd> When Nmap receives no response to a port scan probe, it could mean the port is filtered. Or maybe the probe or response was simply lost on the network. It is also possible that the target host has rate limiting enabled that temporarily blocked the response. So Nmap tries again by retransmitting the initial probe. If Nmap detects poor network reliability, it may try many more times before giving up on a port. While this benefits accuracy, it also lengthens scan times. When performance is critical, scans may be sped up by limiting the number of retransmissions allowed. You can even specify <code>&#8211;max-retries 0</code> to prevent any retransmissions, though that is only recommended for situations such as informal surveys where occasional missed ports and hosts are acceptable. </p>
<p> The default (with no <code>-T</code> template) is to allow ten retransmissions. If a network seems reliable and the target hosts aren&#8217;t rate limiting, Nmap usually only does one retransmission. So most target scans aren&#8217;t even affected by dropping <code>&#8211;max-retries</code> to a low value such as three. Such values can substantially speed scans of slow (rate limited) hosts. You usually lose some information when Nmap gives up on ports early, though that may be preferable to letting the <code>&#8211;host-timeout</code> expire and losing all information about the target.</dl>
<p> <code>&#8211;host-timeout </code><i>time</i> (Give up on slow target hosts)</p>
<dl>
<dt>
<dd> Some hosts simply take a <i>long</i> time to scan. This may be due to poorly performing or unreliable networking hardware or software, packet rate limiting, or a restrictive firewall. The slowest few percent of the scanned hosts can eat up a majority of the scan time. Sometimes it is best to cut your losses and skip those hosts initially. Specify <code>&#8211;host-timeout</code> with the maximum amount of time you are willing to wait. For example, specify 30m to ensure that Nmap doesn&#8217;t waste more than half an hour on a single host. Note that Nmap may be scanning other hosts at the same time during that half an hour, so it isn&#8217;t a complete loss. A host that times out is skipped. No port table, OS detection, or version detection results are printed for that host.</dl>
<p> <code>&#8211;script-timeout </code><i>time</i></p>
<dl>
<dt>
<dd> While some scripts complete in fractions of a second, others can take hours or more depending on the nature of the script, arguments passed in, network and application conditions, and more. The <code>&#8211;script-timeout</code> option sets a ceiling on script execution time. Any script instance which exceeds that time will be terminated and no output will be shown. If debugging (<code>-d</code>) is enabled, Nmap will report on each timeout. For host and service scripts, a script instance only scans a single target host or port and the timeout period will be reset for the next instance.</dl>
<p> <code>&#8211;scan-delay </code><i>time</i>; <code>&#8211;max-scan-delay </code><i>time</i> (Adjust delay between probes)</p>
<dl>
<dt>
<dd> This option causes Nmap to wait at least the given amount of time between each probe it sends to a given host. This is particularly useful in the case of rate limiting. Solaris machines (among many others) will usually respond to UDP scan probe packets with only one ICMP message per second. Any more than that sent by Nmap will be wasteful. A <code>&#8211;scan-delay</code> of 1s will keep Nmap at that slow rate. Nmap tries to detect rate limiting and adjust the scan delay accordingly, but it doesn&#8217;t hurt to specify it explicitly if you already know what rate works best. </p>
<p> When Nmap adjusts the scan delay upward to cope with rate limiting, the scan slows down dramatically. The <code>&#8211;max-scan-delay</code> option specifies the largest delay that Nmap will allow. A low <code>&#8211;max-scan-delay</code> can speed up Nmap, but it is risky. Setting this value too low can lead to wasteful packet retransmissions and possible missed ports when the target implements strict rate limiting. </p>
<p> Another use of <code>&#8211;scan-delay</code> is to evade threshold based intrusion detection and prevention systems (IDS/IPS).</dl>
<p> <code>&#8211;min-rate </code><i>number</i>; <code>&#8211;max-rate </code><i>number</i> (Directly control the scanning rate)</p>
<dl>
<dt>
<dd> Nmap&#8217;s dynamic timing does a good job of finding an appropriate speed at which to scan. Sometimes, however, you may happen to know an appropriate scanning rate for a network, or you may have to guarantee that a scan will be finished by a certain time. Or perhaps you must keep Nmap from scanning too quickly. The <code>&#8211;min-rate</code> and <code>&#8211;max-rate</code> options are designed for these situations. </p>
<p> When the <code>&#8211;min-rate</code> option is given Nmap will do its best to send packets as fast as or faster than the given rate. The argument is a positive real number representing a packet rate in packets per second. For example, specifying <code>&#8211;min-rate 300</code> means that Nmap will try to keep the sending rate at or above 300 packets per second. Specifying a minimum rate does not keep Nmap from going faster if conditions warrant. </p>
<p> Likewise, <code>&#8211;max-rate</code> limits a scan&#8217;s sending rate to a given maximum. Use <code>&#8211;max-rate 100</code>, for example, to limit sending to 100 packets per second on a fast network. Use <code>&#8211;max-rate 0.1</code> for a slow scan of one packet every ten seconds. Use <code>&#8211;min-rate</code> and <code>&#8211;max-rate</code> together to keep the rate inside a certain range. </p>
<p> These two options are global, affecting an entire scan, not individual hosts. They only affect port scans and host discovery scans. Other features like OS detection implement their own timing. </p>
<p> There are two conditions when the actual scanning rate may fall below the requested minimum. The first is if the minimum is faster than the fastest rate at which Nmap can send, which is dependent on hardware. In this case Nmap will simply send packets as fast as possible, but be aware that such high rates are likely to cause a loss of accuracy. The second case is when Nmap has nothing to send, for example at the end of a scan when the last probes have been sent and Nmap is waiting for them to time out or be responded to. It&#8217;s normal to see the scanning rate drop at the end of a scan or in between hostgroups. The sending rate may temporarily exceed the maximum to make up for unpredictable delays, but on average the rate will stay at or below the maximum. </p>
<p> Specifying a minimum rate should be done with care. Scanning faster than a network can support may lead to a loss of accuracy. In some cases, using a faster rate can make a scan take <i>longer</i> than it would with a slower rate. This is because Nmap&#8217;s </p>
<p> adaptive retransmission algorithms will detect the network congestion caused by an excessive scanning rate and increase the number of retransmissions in order to improve accuracy. So even though packets are sent at a higher rate, more packets are sent overall. Cap the number of retransmissions with the <code>&#8211;max-retries</code> option if you need to set an upper limit on total scan time.</dl>
<p> <code>&#8211;defeat-rst-ratelimit</code></p>
<dl>
<dt>
<dd> Many hosts have long used rate limiting to reduce the number of ICMP error messages (such as port-unreachable errors) they send. Some systems now apply similar rate limits to the RST (reset) packets they generate. This can slow Nmap down dramatically as it adjusts its timing to reflect those rate limits. You can tell Nmap to ignore those rate limits (for port scans such as SYN scan which <i>don&#8217;t</i> treat non-responsive ports as open) by specifying <code>&#8211;defeat-rst-ratelimit</code>. </p>
<p> Using this option can reduce accuracy, as some ports will appear non-responsive because Nmap didn&#8217;t wait long enough for a rate-limited RST response. With a SYN scan, the non-response results in the port being labeled filtered rather than the closed state we see when RST packets are received. This option is useful when you only care about open ports, and distinguishing between closed and filtered ports isn&#8217;t worth the extra time.</dl>
<p> <code>&#8211;defeat-icmp-ratelimit</code></p>
<dl>
<dt>
<dd> Similar to <code>&#8211;defeat-rst-ratelimit</code>, the <code>&#8211;defeat-icmp-ratelimit</code> option trades accuracy for speed, increasing UDP scanning speed against hosts that rate-limit ICMP error messages. Because this option causes Nmap to not delay in order to receive the port unreachable messages, a non-responsive port will be labeled closed|filtered instead of the default open|filtered. This has the effect of only treating ports which actually respond via UDP as open. Since many UDP services do not respond in this way, the chance for inaccuracy is greater with this option than with <code>&#8211;defeat-rst-ratelimit</code>.</dl>
<p> <code>&#8211;nsock-engine epoll|kqueue|poll|select</code></p>
<dl>
<dt>
<dd> Enforce use of a given nsock IO multiplexing engine. Only the <a href="/docs/linux/man/2-select/">select</a>(2)-based fallback engine is guaranteed to be available on your system. Engines are named after the name of the IO management facility they leverage. Engines currently implemented are epoll, kqueue, poll, and select, but not all will be present on any platform. Use <code>nmap -V</code> to see which engines are supported.</dl>
<p> <code>-T paranoid|sneaky|polite|normal|aggressive|insane</code> (Set a timing template)</p>
<dl>
<dt>
<dd> While the fine-grained timing controls discussed in the previous section are powerful and effective, some people find them confusing. Moreover, choosing the appropriate values can sometimes take more time than the scan you are trying to optimize. Fortunately, Nmap offers a simpler approach, with six timing templates. You can specify them with the <code>-T</code> option and their number (0-5) or their name. The template names are <code>paranoid</code>&nbsp;(<code>0</code>), <code>sneaky</code>&nbsp;(<code>1</code>), <code>polite</code>&nbsp;(<code>2</code>), <code>normal</code>&nbsp;(<code>3</code>), <code>aggressive</code>&nbsp;(<code>4</code>), and <code>insane</code>&nbsp;(<code>5</code>). The first two are for IDS evasion. Polite mode slows down the scan to use less bandwidth and target machine resources. Normal mode is the default and so <code>-T3</code> does nothing. Aggressive mode speeds scans up by making the assumption that you are on a reasonably fast and reliable network. Finally insane mode assumes that you are on an extraordinarily fast network or are willing to sacrifice some accuracy for speed. </p>
<p> These templates allow the user to specify how aggressive they wish to be, while leaving Nmap to pick the exact timing values. The templates also make some minor speed adjustments for which fine-grained control options do not currently exist. For example, <code>-T4</code> prohibits the dynamic scan delay from exceeding 10 ms for TCP ports and <code>-T5</code> caps that value at 5 ms. Templates can be used in combination with fine-grained controls, and the fine-grained controls that you specify will take precedence over the timing template default for that parameter. I recommend using <code>-T4</code> when scanning reasonably modern and reliable networks. Keep that option even when you add fine-grained controls so that you benefit from those extra minor optimizations that it enables. </p>
<p> If you are on a decent broadband or ethernet connection, I would recommend always using <code>-T4</code>. Some people love <code>-T5</code> though it is too aggressive for my taste. People sometimes specify <code>-T2</code> because they think it is less likely to crash hosts or because they consider themselves to be polite in general. They often don&#8217;t realize just how slow <code>-T polite</code> really is. Their scan may take ten times longer than a default scan. Machine crashes and bandwidth problems are rare with the default timing options (<code>-T3</code>) and so I normally recommend that for cautious scanners. Omitting version detection is far more effective than playing with timing values at reducing these problems. </p>
<p> While <code>-T0</code> and <code>-T1</code> may be useful for avoiding IDS alerts, they will take an extraordinarily long time to scan thousands of machines or ports. For such a long scan, you may prefer to set the exact timing values you need rather than rely on the canned <code>-T0</code> and <code>-T1</code> values. </p>
<p> The main effects of <code>T0</code> are serializing the scan so only one port is scanned at a time, and waiting five minutes between sending each probe. <code>T1</code> and <code>T2</code> are similar but they only wait 15 seconds and 0.4 seconds, respectively, between probes. <code>T3</code> is Nmap&#8217;s default behavior, which includes parallelization. <code>-T4</code> does the equivalent of <code>&#8211;max-rtt-timeout 1250ms &#8211;min-rtt-timeout 100ms &#8211;initial-rtt-timeout 500ms &#8211;max-retries 6</code> and sets the maximum TCP scan delay to 10 milliseconds. <code>T5</code> does the equivalent of <code>&#8211;max-rtt-timeout 300ms &#8211;min-rtt-timeout 50ms &#8211;initial-rtt-timeout 250ms &#8211;max-retries 2 &#8211;host-timeout 15m &#8211;script-timeout 10m</code> as well as setting the maximum TCP scan delay to 5 ms.</dl>
<h2>FIREWALL/IDS EVASION AND SPOOFING</h2>
<p> Many Internet pioneers envisioned a global open network with a universal IP address space allowing virtual connections between any two nodes. This allows hosts to act as true peers, serving and retrieving information from each other. People could access all of their home systems from work, changing the climate control settings or unlocking the doors for early guests. This vision of universal connectivity has been stifled by address space shortages and security concerns. In the early 1990s, organizations began deploying firewalls for the express purpose of reducing connectivity. Huge networks were cordoned off from the unfiltered Internet by application proxies, network address translation, and packet filters. The unrestricted flow of information gave way to tight regulation of approved communication channels and the content that passes over them. </p>
<p> Network obstructions such as firewalls can make mapping a network exceedingly difficult. It will not get any easier, as stifling casual reconnaissance is often a key goal of implementing the devices. Nevertheless, Nmap offers many features to help understand these complex networks, and to verify that filters are working as intended. It even supports mechanisms for bypassing poorly implemented defenses. One of the best methods of understanding your network security posture is to try to defeat it. Place yourself in the mind-set of an attacker, and deploy techniques from this section against your networks. Launch an FTP bounce scan, idle scan, fragmentation attack, or try to tunnel through one of your own proxies. </p>
<p> In addition to restricting network activity, companies are increasingly monitoring traffic with intrusion detection systems (IDS). All of the major IDSs ship with rules designed to detect Nmap scans because scans are sometimes a precursor to attacks. Many of these products have recently morphed into intrusion <i>prevention</i> systems (IPS) that actively block traffic deemed malicious. Unfortunately for network administrators and IDS vendors, reliably detecting bad intentions by analyzing packet data is a tough problem. Attackers with patience, skill, and the help of certain Nmap options can usually pass by IDSs undetected. Meanwhile, administrators must cope with large numbers of false positive results where innocent activity is misdiagnosed and alerted on or blocked. </p>
<p> Occasionally people suggest that Nmap should not offer features for evading firewall rules or sneaking past IDSs. They argue that these features are just as likely to be misused by attackers as used by administrators to enhance security. The problem with this logic is that these methods would still be used by attackers, who would just find other tools or patch the functionality into Nmap. Meanwhile, administrators would find it that much harder to do their jobs. Deploying only modern, patched FTP servers is a far more powerful defense than trying to prevent the distribution of tools implementing the FTP bounce attack. </p>
<p> There is no magic bullet (or Nmap option) for detecting and subverting firewalls and IDS systems. It takes skill and experience. A tutorial is beyond the scope of this reference guide, which only lists the relevant options and describes what they do. </p>
<p> <code>-f</code> (fragment packets); <code>&#8211;mtu</code> (using the specified MTU)</p>
<dl>
<dt>
<dd> The <code>-f</code> option causes the requested scan (including ping scans) to use tiny fragmented IP packets. The idea is to split up the TCP header over several packets to make it harder for packet filters, intrusion detection systems, and other annoyances to detect what you are doing. Be careful with this! Some programs have trouble handling these tiny packets. The old-school sniffer named Sniffit segmentation faulted immediately upon receiving the first fragment. Specify this option once, and Nmap splits the packets into eight bytes or less after the IP header. So a 20-byte TCP header would be split into three packets. Two with eight bytes of the TCP header, and one with the final four. Of course each fragment also has an IP header. Specify <code>-f</code> again to use 16 bytes per fragment (reducing the number of fragments). Or you can specify your own offset size with the <code>&#8211;mtu</code> option. Don&#8217;t also specify <code>-f</code> if you use <code>&#8211;mtu</code>. The offset must be a multiple of eight. While fragmented packets won&#8217;t get by packet filters and firewalls that queue all IP fragments, such as the <i>CONFIG_IP_ALWAYS_DEFRAG</i> option in the Linux kernel, some networks can&#8217;t afford the performance hit this causes and thus leave it disabled. Others can&#8217;t enable this because fragments may take different routes into their networks. Some source systems defragment outgoing packets in the kernel. Linux with the iptables connection tracking module is one such example. Do a scan while a sniffer such as Wireshark is running to ensure that sent packets are fragmented. If your host OS is causing problems, try the <code>&#8211;send-eth</code> option to bypass the IP layer and send raw ethernet frames. </p>
<p> Fragmentation is only supported for Nmap&#8217;s raw packet features, which includes TCP and UDP port scans (except connect scan and FTP bounce scan) and OS detection. Features such as version detection and the Nmap Scripting Engine generally don&#8217;t support fragmentation because they rely on your host&#8217;s TCP stack to communicate with target services.</dl>
<p> <code>-D </code><i>decoy1</i><code>[,</code><i>decoy2</i>]<code>[,ME]</code><code>[,&#8230;]</code> (Cloak a scan with decoys)</p>
<dl>
<dt>
<dd> Causes a decoy scan to be performed, which makes it appear to the remote host that the host(s) you specify as decoys are scanning the target network too. Thus their IDS might report 5-10 port scans from unique IP addresses, but they won&#8217;t know which IP was scanning them and which were innocent decoys. While this can be defeated through router path tracing, response-dropping, and other active mechanisms, it is generally an effective technique for hiding your IP address. </p>
<p> Separate each decoy host with commas, and you can optionally use ME as one of the decoys to represent the position for your real IP address. If you put ME in the sixth position or later, some common port scan detectors (such as Solar Designer&#8217;s excellent Scanlogd) are unlikely to show your IP address at all. If you don&#8217;t use ME, Nmap will put you in a random position. You can also use RND to generate a random, non-reserved IP address, or RND:<i>number</i> to generate <i>number</i> addresses. </p>
<p> Note that the hosts you use as decoys should be up or you might accidentally SYN flood your targets. Also it will be pretty easy to determine which host is scanning if only one is actually up on the network. You might want to use IP addresses instead of names (so the decoy networks don&#8217;t see you in their nameserver logs). Right now random IP address generation is only supported with IPv4 </p>
<p> Decoys are used both in the initial ping scan (using ICMP, SYN, ACK, or whatever) and during the actual port scanning phase. Decoys are also used during remote OS detection (<code>-O</code>). Decoys do not work with version detection or TCP connect scan. When a scan delay is in effect, the delay is enforced between each batch of spoofed probes, not between each individual probe. Because decoys are sent as a batch all at once, they may temporarily violate congestion control limits. </p>
<p> It is worth noting that using too many decoys may slow your scan and potentially even make it less accurate. Also, some ISPs will filter out your spoofed packets, but many do not restrict spoofed IP packets at all.</dl>
<p> <code>-S </code><i>IP_Address</i> (Spoof source address)</p>
<dl>
<dt>
<dd> In some circumstances, Nmap may not be able to determine your source address (Nmap will tell you if this is the case). In this situation, use <code>-S</code> with the IP address of the interface you wish to send packets through. </p>
<p> Another possible use of this flag is to spoof the scan to make the targets think that <i>someone else</i> is scanning them. Imagine a company being repeatedly port scanned by a competitor! The <code>-e</code> option and <code>-Pn</code> are generally required for this sort of usage. Note that you usually won&#8217;t receive reply packets back (they will be addressed to the IP you are spoofing), so Nmap won&#8217;t produce useful reports.</dl>
<p> <code>-e </code><i>interface</i> (Use specified interface)</p>
<dl>
<dt>
<dd> Tells Nmap what interface to send and receive packets on. Nmap should be able to detect this automatically, but it will tell you if it cannot.</dl>
<p> <code>&#8211;source-port </code><i>portnumber</i><code>;</code> <code>-g </code><i>portnumber</i> (Spoof source port number)</p>
<dl>
<dt>
<dd> One surprisingly common misconfiguration is to trust traffic based only on the source port number. It is easy to understand how this comes about. An administrator will set up a shiny new firewall, only to be flooded with complaints from ungrateful users whose applications stopped working. In particular, DNS may be broken because the UDP DNS replies from external servers can no longer enter the network. FTP is another common example. In active FTP transfers, the remote server tries to establish a connection back to the client to transfer the requested file. </p>
<p> Secure solutions to these problems exist, often in the form of application-level proxies or protocol-parsing firewall modules. Unfortunately there are also easier, insecure solutions. Noting that DNS replies come from port 53 and active FTP from port 20, many administrators have fallen into the trap of simply allowing incoming traffic from those ports. They often assume that no attacker would notice and exploit such firewall holes. In other cases, administrators consider this a short-term stop-gap measure until they can implement a more secure solution. Then they forget the security upgrade. </p>
<p> Overworked network administrators are not the only ones to fall into this trap. Numerous products have shipped with these insecure rules. Even Microsoft has been guilty. The IPsec filters that shipped with Windows 2000 and Windows XP contain an implicit rule that allows all TCP or UDP traffic from port 88 (Kerberos). In another well-known case, versions of the Zone Alarm personal firewall up to 2.1.25 allowed any incoming UDP packets with the source port 53 (DNS) or 67 (DHCP). </p>
<p> Nmap offers the <code>-g</code> and <code>&#8211;source-port</code> options (they are equivalent) to exploit these weaknesses. Simply provide a port number and Nmap will send packets from that port where possible. Most scanning operations that use raw sockets, including SYN and UDP scans, support the option completely. The option notably doesn&#8217;t have an effect for any operations that use normal operating system sockets, including DNS requests, TCP <code>connect</code> scan, version detection, and script scanning. Setting the source port also doesn&#8217;t work for OS detection, because Nmap must use different port numbers for certain OS detection tests to work properly.</dl>
<p> <code>&#8211;data </code><i>hex string</i> (Append custom binary data to sent packets)</p>
<dl>
<dt>
<dd> This option lets you include binary data as payload in sent packets. <i>hex string</i> may be specified in any of the following formats: 0xAABBCCDDEEFF<i>&#8230;</i>, AABBCCDDEEFF<i>&#8230;</i> or ������<i>&#8230;</i>. Examples of use are <code>&#8211;data 0xdeadbeef</code> and <code>&#8211;data ��	</code>. Note that if you specify a number like 0x00ff no byte-order conversion is performed. Make sure you specify the information in the byte order expected by the receiver.</dl>
<p> <code>&#8211;data-string </code><i>string</i> (Append custom string to sent packets)</p>
<dl>
<dt>
<dd> This option lets you include a regular string as payload in sent packets. <i>string</i> can contain any string. However, note that some characters may depend on your system&#8217;s locale and the receiver may not see the same information. Also, make sure you enclose the string in double quotes and escape any special characters from the shell. Examples: <code>&#8211;data-string &quot;Scan conducted by Security Ops, extension 7192&quot;</code> or <code>&#8211;data-string &quot;Ph34r my l33t skills&quot;</code>. Keep in mind that nobody is likely to actually see any comments left by this option unless they are carefully monitoring the network with a sniffer or custom IDS rules.</dl>
<p> <code>&#8211;data-length </code><i>number</i> (Append random data to sent packets)</p>
<dl>
<dt>
<dd> Normally Nmap sends minimalist packets containing only a header. So its TCP packets are generally 40 bytes and ICMP echo requests are just 28. Some UDP ports and IP protocols get a custom payload by default. This option tells Nmap to append the given number of random bytes to most of the packets it sends, and not to use any protocol-specific payloads. (Use <code>&#8211;data-length 0</code> for no random or protocol-specific payloads. OS detection (<code>-O</code>) packets are not affected because accuracy there requires probe consistency, but most pinging and portscan packets support this. It slows things down a little, but can make a scan slightly less conspicuous.</dl>
<p> <code>&#8211;ip-options </code><i>S|R [route]|L [route]|T|U &#8230; </i><code>;</code> <code>&#8211;ip-options </code><i>hex string</i> (Send packets with specified ip options)</p>
<dl>
<dt>
<dd> The m[blue]<code>IP protocol</code>m[]<font SIZE="-2">[13]</font> offers several options which may be placed in packet headers. Unlike the ubiquitous TCP options, IP options are rarely seen due to practicality and security concerns. In fact, many Internet routers block the most dangerous options such as source routing. Yet options can still be useful in some cases for determining and manipulating the network route to target machines. For example, you may be able to use the record route option to determine a path to a target even when more traditional traceroute-style approaches fail. Or if your packets are being dropped by a certain firewall, you may be able to specify a different route with the strict or loose source routing options. </p>
<p> The most powerful way to specify IP options is to simply pass in values as the argument to <code>&#8211;ip-options</code>. Precede each hex number with 
