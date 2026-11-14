---
title: "freeifaddrs(3)"
name: "freeifaddrs"
section: "3"
letter: "f"
url: "/docs/linux/man/3-freeifaddrs/"
---

<h2 class="name">NAME</h2>
 

 getifaddrs, freeifaddrs - get interface addresses 

<h2>SYNOPSIS</h2>

 <pre><code>
#include &lt;ifaddrs.h&gt;
#include &lt;sys/types.h&gt;
int getifaddrs(struct ifaddrs **ifap);
void freeifaddrs(struct ifaddrs *ifa);
</code></pre>

<h2>DESCRIPTION</h2>

 The <b>getifaddrs</b>() function creates a linked list of structures describing the network interfaces of the local system, and stores the address of the first item of the list in <i>*ifap</i>. The list consists of <i>ifaddrs</i> structures, defined as follows: 

 struct ifaddrs { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct ifaddrs&nbsp;<wbr>&nbsp;*ifa_next;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Next item in list&nbsp;*/ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*ifa_name;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Name of interface&nbsp;*/ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ifa_flags;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Flags from SIOCGIFFLAGS&nbsp;*/ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct sockaddr&nbsp;*ifa_addr;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Address of interface&nbsp;*/ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct sockaddr&nbsp;*ifa_netmask;&nbsp;/*&nbsp;Netmask of interface&nbsp;*/ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;union&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct sockaddr&nbsp;*ifu_broadaddr; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Broadcast address of interface&nbsp;*/ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct sockaddr&nbsp;*ifu_dstaddr; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Point-to-point destination address&nbsp;*/ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;ifa_ifu; #define ifa_broadaddr ifa_ifu.ifu_broadaddr #define ifa_dstaddr ifa_ifu.ifu_dstaddr 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*ifa_data;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Address-specific data&nbsp;*/ }; 

 The <i>ifa_next</i> field contains a pointer to the next structure on the list, or NULL if this is the last item of the list. 

 The <i>ifa_name</i> points to the null-terminated interface name. 

 The <i>ifa_flags</i> field contains the interface flags, as returned by the <b>SIOCGIFFLAGS</b> <b><a HREF="/docs/linux/man/2-ioctl/">ioctl</a></b>(2) operation (see <b><a HREF="/docs/linux/man/7-netdevice/">netdevice</a></b>(7) for a list of these flags). 

 The <i>ifa_addr</i> field points to a structure containing the interface address. (The <i>sa_family</i> subfield should be consulted to determine the format of the address structure.) This field may contain a null pointer. 

 The <i>ifa_netmask</i> field points to a structure containing the netmask associated with <i>ifa_addr</i>, if applicable for the address family. This field may contain a null pointer. 

 Depending on whether the bit <b>IFF_BROADCAST</b> or <b>IFF_POINTOPOINT</b> is set in <i>ifa_flags</i> (only one can be set at a time), either <i>ifa_broadaddr</i> will contain the broadcast address associated with <i>ifa_addr</i> (if applicable for the address family) or <i>ifa_dstaddr</i> will contain the destination address of the point-to-point interface. 

 The <i>ifa_data</i> field points to a buffer containing address-family-specific data; this field may be NULL if there is no such data for this interface. 

 The data returned by <b>getifaddrs</b>() is dynamically allocated and should be freed using <b>freeifaddrs</b>() when no longer needed.

<h2>RETURN VALUE</h2>

 On success, <b>getifaddrs</b>() returns zero; on error, -1 is returned, and <i>errno</i> is set appropriately.

<h2>ERRORS</h2>

 <b>getifaddrs</b>() may fail and set <i>errno</i> for any of the errors specified for <b><a HREF="/docs/linux/man/2-socket/">socket</a></b>(2), <b><a HREF="/docs/linux/man/2-bind/">bind</a></b>(2), <b><a HREF="/docs/linux/man/2-getsockname/">getsockname</a></b>(2), <b><a HREF="/docs/linux/man/2-recvmsg/">recvmsg</a></b>(2), <b><a HREF="/docs/linux/man/2-sendto/">sendto</a></b>(2), <b><a HREF="/docs/linux/man/3-malloc/">malloc</a></b>(3), or <b><a HREF="/docs/linux/man/3-realloc/">realloc</a></b>(3).

<h2>VERSIONS</h2>

 The <b>getifaddrs</b>() function first appeared in glibc 2.3, but before glibc 2.3.3, the implementation supported only IPv4 addresses; IPv6 support was added in glibc 2.3.3. Support of address families other than IPv4 is available only on kernels that support netlink.

<h2>ATTRIBUTES</h2>

 For an explanation of the terms used in this section, see <b><a HREF="/docs/linux/man/7-attributes/">attributes</a></b>(7). <table BORDER> <tr VALIGN=top><td><b>Interface</b></td><td><b>Attribute</b></td><td><b>Value</b>
</td></tr> <tr VALIGN=top><td> <b>getifaddrs</b>(), <b>freeifaddrs</b>() </td><td>Thread safety</td><td>MT-Safe
</td></tr> </table> 

<h2>CONFORMING TO</h2>

 Not in POSIX.1. This function first appeared in BSDi and is present on the BSD systems, but with slightly different semantics documented---returning one entry per interface, not per address. This means <i>ifa_addr</i> and other fields can actually be NULL if the interface has no address, and no link-level address is returned if the interface has an IP address assigned. Also, the way of choosing either <i>ifa_broadaddr</i> or <i>ifa_dstaddr</i> differs on various systems.

<h2>NOTES</h2>

 The addresses returned on Linux will usually be the IPv4 and IPv6 addresses assigned to the interface, but also one <b>AF_PACKET</b> address per interface containing lower-level details about the interface and its physical layer. In this case, the <i>ifa_data</i> field may contain a pointer to a <i>struct rtnl_link_stats</i>, defined in <i>&lt;linux/if_link.h&gt;</i> (in Linux 2.4 and earlier, <i>struct net_device_stats</i>, defined in <i>&lt;linux/netdevice.h&gt;</i>), which contains various interface attributes and statistics.

<h2>EXAMPLES</h2>

 The program below demonstrates the use of <b>getifaddrs</b>(), <b>freeifaddrs</b>(), and <b><a HREF="/docs/linux/man/3-getnameinfo/">getnameinfo</a></b>(3). Here is what we see when running this program on one system: 

 $ <b>./a.out</b> lo AF_PACKET (17) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tx_packets&nbsp;=&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;524;&nbsp;rx_packets&nbsp;=&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;524 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tx_bytes&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;38788;&nbsp;rx_bytes&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;38788 wlp3s0 AF_PACKET (17) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tx_packets&nbsp;=&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;108391;&nbsp;rx_packets&nbsp;=&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;130245 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tx_bytes&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;<wbr>&nbsp;<wbr>&nbsp;30420659;&nbsp;rx_bytes&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;<wbr>&nbsp;<wbr>&nbsp;94230014 em1 AF_PACKET (17) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tx_packets&nbsp;=&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0;&nbsp;rx_packets&nbsp;=&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tx_bytes&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0;&nbsp;rx_bytes&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0 lo AF_INET (2) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;address:&nbsp;&lt;127.0.0.1&gt; wlp3s0 AF_INET (2) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;address:&nbsp;&lt;192.168.235.137&gt; lo AF_INET6 (10) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;address:&nbsp;&lt;::1&gt; wlp3s0 AF_INET6 (10) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;address:&nbsp;&lt;fe80::7ee9:d3ff:fef5:1a91%wlp3s0&gt;

<h3>Program source</h3>

 #define _GNU_SOURCE /* To get defns of NI_MAXSERV and NI_MAXHOST */ #include &lt;arpa/inet.h&gt; #include &lt;sys/socket.h&gt; #include &lt;netdb.h&gt; #include &lt;ifaddrs.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;unistd.h&gt; #include &lt;linux/if_link.h&gt; 

 int main(int argc, char *argv[]) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct ifaddrs&nbsp;*ifaddr; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int family, s; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char host[NI_MAXHOST]; 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(getifaddrs(&amp;ifaddr)&nbsp;==&nbsp;-1)&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;getifaddrs&quot;); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Walk through linked list, maintaining head pointer so we 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;can free list later&nbsp;*/ 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(struct ifaddrs&nbsp;*ifa&nbsp;=&nbsp;ifaddr;&nbsp;ifa&nbsp;!=&nbsp;NULL; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ifa&nbsp;=&nbsp;ifa-&gt;ifa_next)&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(ifa-&gt;ifa_addr&nbsp;==&nbsp;NULL) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;continue; 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;family&nbsp;=&nbsp;ifa-&gt;ifa_addr-&gt;sa_family; 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Display interface name and family&nbsp;(including symbolic 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;form of the latter for the common families)&nbsp;*/ 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%-8s&nbsp;%s&nbsp;(%d)\n&quot;, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ifa-&gt;ifa_name, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(family&nbsp;==&nbsp;AF_PACKET)&nbsp;?&nbsp;&quot;AF_PACKET&quot;&nbsp;: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(family&nbsp;==&nbsp;AF_INET)&nbsp;?&nbsp;&quot;AF_INET&quot;&nbsp;: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(family&nbsp;==&nbsp;AF_INET6)&nbsp;?&nbsp;&quot;AF_INET6&quot;&nbsp;:&nbsp;&quot;???&quot;, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;family); 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;For an AF_INET*&nbsp;interface address, display the address&nbsp;*/ 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(family&nbsp;==&nbsp;AF_INET || family&nbsp;==&nbsp;AF_INET6)&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;s&nbsp;=&nbsp;getnameinfo(ifa-&gt;ifa_addr, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(family&nbsp;==&nbsp;AF_INET)&nbsp;?&nbsp;sizeof(struct sockaddr_in)&nbsp;: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sizeof(struct sockaddr_in6), 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;host, NI_MAXHOST, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;NULL, 0, NI_NUMERICHOST); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(s&nbsp;!=&nbsp;0)&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;getnameinfo()&nbsp;failed:&nbsp;%s\n&quot;, gai_strerror(s)); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;\t\taddress:&nbsp;&lt;%s&gt;\n&quot;, host); 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;else if&nbsp;(family&nbsp;==&nbsp;AF_PACKET&nbsp;&amp;&amp;&nbsp;ifa-&gt;ifa_data&nbsp;!=&nbsp;NULL)&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct rtnl_link_stats&nbsp;*stats&nbsp;=&nbsp;ifa-&gt;ifa_data; 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;\t\ttx_packets&nbsp;=&nbsp;%10u;&nbsp;rx_packets&nbsp;=&nbsp;%10u\n&quot; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;\t\ttx_bytes&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;%10u;&nbsp;rx_bytes&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;%10u\n&quot;, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;stats-&gt;tx_packets, stats-&gt;rx_packets, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;stats-&gt;tx_bytes, stats-&gt;rx_bytes); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;freeifaddrs(ifaddr); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }

<h2>SEE ALSO</h2>

 <b><a HREF="/docs/linux/man/2-bind/">bind</a></b>(2), <b><a HREF="/docs/linux/man/2-getsockname/">getsockname</a></b>(2), <b><a HREF="/docs/linux/man/2-socket/">socket</a></b>(2), <b><a HREF="/docs/linux/man/7-packet/">packet</a></b>(7), <b><a HREF="/docs/linux/man/8-ifconfig/">ifconfig</a></b>(8)

<h2>COLOPHON</h2>

 This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" HREF="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> 

<h2>Index</h2>


