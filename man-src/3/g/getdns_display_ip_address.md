---

title: "getdns_display_ip_address(3)"
name: "getdns_display_ip_address"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getdns_display_ip_address/"
description: "getdns_display_ip_address — convert an getdns ip address to string"
---

<h2>NAME</h2>
<p> <code>getdns_display_ip_address</code> &#8212; convert an getdns ip address to string </p>
<h2>LIBRARY</h2>
<p> DNS Resolver library (libgetdns, -lgetdns) </p>
<p> #include &lt;getdns.h&gt; </p>
<p> char *<br />
 <code>getdns_display_ip_address</code> (const getdns_bindata *ipv4_or_ipv6_addr) </p>
<p> This helper function returns a nicely formatted string representation of the IPv4 or IPv6 address. The length of the bindata is used to determine whether the address is IPv4 or IPv6. </p>
<dl>
<dt> <i>ipv4_or_ipv6_addr</i></dt>
<dd>bindata of the address to print </dd>
<dt></dt></dl>
<h2>RETURN VALUES</h2>
<dd>Returns a string representation of the IP address (allocated using the system allocator &#8211; malloc), the caller is responsible for freeing the storage using free(). </dd>
<h2>EXAMPLES</h2>
<p> TBD </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libgetdns/">libgetdns</a></code>(3) </p>
