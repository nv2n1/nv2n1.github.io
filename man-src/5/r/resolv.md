---
title: "resolv(5)"
name: "resolv"
section: "5"
letter: "r"
url: "/docs/linux/man/5-resolv/"
description: "resolv.conf – resolver configuration file"
---

<p>resolv.conf &#8211; resolver configuration file</p>
<h2>Synopsis</h2>
<p><code>/etc/resolv.conf</code></p>
<h2>Description</h2>
<p>The <i>resolver</i> is a set of routines in the C library that provide access to the Internet Domain Name System (DNS). The resolver configuration file contains information that is read by the resolver routines the first time they are invoked by a process. The file is designed to be human readable and contains a list of keywords with values that provide various types of resolver information. The configuration file is considered a trusted source of DNS information (e.g., DNSSEC AD-bit information will be returned unmodified from this source). </p>
<p> If this file does not exist, only the name server on the local machine will be queried; the domain name is determined from the hostname and the domain search path is constructed from the domain name. </p>
<p> The different configuration options are:</p>
<dl>
<dt><code>nameserver</code> Name server IP address</p>
<dd>Internet address of a name server that the resolver should query, either an IPv4 address (in dot notation), or an IPv6 address in colon (and possibly dot) notation as per RFC 2373. Up to <code>MAXNS</code> (currently 3, see <i>&lt;resolv.h&gt;</i>) name servers may be listed, one per keyword. If there are multiple servers, the resolver library queries them in the order listed. If no <code>nameserver</code> entries are present, the default is to use the name server on the local machine. (The algorithm used is to try a name server, and if the query times out, try the next, until out of name servers, then repeat trying all the name servers until a maximum number of retries are made.)</p>
<dt><code>domain</code> Local domain name.</p>
<dd>Most queries for names within this domain can use short names relative to the local domain. If set to &#8216;.&#8217;, the root domain is considered. If no <code>domain</code> entry is present, the domain is determined from the local hostname returned by <code><a href="/docs/linux/man/2-gethostname/">gethostname</a></code>(2); the domain part is taken to be everything after the first &#8216;.&#8217;. Finally, if the hostname does not contain a domain part, the root domain is assumed.</p>
<dt><code>search</code> Search list for host-name lookup.</p>
<dd>The search list is normally determined from the local domain name; by default, it contains only the local domain name. This may be changed by listing the desired domain search path following the <i>search</i> keyword with spaces or tabs separating the names. Resolver queries having fewer than <i>ndots</i> dots (default is 1) in them will be attempted using each component of the search path in turn until a match is found. For environments with multiple subdomains please read <code>options ndots:</code><i>n</i> below to avoid man-in-the-middle attacks and unnecessary traffic for the root-dns-servers. Note that this process may be slow and will generate a lot of network traffic if the servers for the listed domains are not local, and that queries will time out if no server is available for one of the domains.</p>
<dd>The search list is currently limited to six domains with a total of 256 characters.</p>
<dt><code>sortlist</code></p>
<dd>This option allows addresses returned by <code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3) to be sorted. A sortlist is specified by IP-address-netmask pairs. The netmask is optional and defaults to the natural netmask of the net. The IP address and optional network pairs are separated by slashes. Up to 10 pairs may be specified. Here is an example: </p>
<p> sortlist 130.155.160.0/255.255.240.0 130.155.0.0 </p>
<dt><code>options</code></p>
<dd>Options allows certain internal resolver variables to be modified. The syntax is</p>
<dl>
<dd>
<dl>
<dd><code>options</code> <i>option</i> <i>&#8230;</i></dl>
<p> where <i>option</i> is one of the following:</p>
<dl>
<dt><code>debug</code></p>
<dd>sets <code>RES_DEBUG</code> in <i>_res.options</i> (effective only if glibc was built with debug support; see <code><a href="/docs/linux/man/3-resolver/">resolver</a></code>(3)).</p>
<dt><code>ndots:</code><i>n</i></p>
<dd>sets a threshold for the number of dots which must appear in a name given to <code><a href="/docs/linux/man/3-res_query/">res_query</a></code>(3) (see <code><a href="/docs/linux/man/3-resolver/">resolver</a></code>(3)) before an <i>initial absolute query</i> will be made. The default for <i>n</i> is 1, meaning that if there are any dots in a name, the name will be tried first as an absolute name before any <i>search list</i> elements are appended to it. The value for this option is silently capped to 15.</p>
<dt><code>timeout:</code><i>n</i></p>
<dd>sets the amount of time the resolver will wait for a response from a remote name server before retrying the query via a different name server. Measured in seconds, the default is <code>RES_TIMEOUT</code> (currently 5, see <i>&lt;resolv.h&gt;</i>). The value for this option is silently capped to 30.</p>
<dt><code>attempts:</code><i>n</i></p>
<dd>sets the number of times the resolver will send a query to its name servers before giving up and returning an error to the calling application. The default is <code>RES_DFLRETRY</code> (currently 2, see <i>&lt;resolv.h&gt;</i>). The value for this option is silently capped to 5.</p>
<dt><code>rotate</code></p>
<dd>sets <code>RES_ROTATE</code> in <i>_res.options</i>, which causes round-robin selection of name servers from among those listed. This has the effect of spreading the query load among all listed servers, rather than having all clients try the first listed server first every time.</p>
<dt><code>no-check-names</code></p>
<dd>sets <code>RES_NOCHECKNAME</code> in <i>_res.options</i>, which disables the modern BIND checking of incoming hostnames and mail names for invalid characters such as underscore (_), non-ASCII, or control characters.</p>
<dt><code>inet6</code></p>
<dd>sets <code>RES_USE_INET6</code> in <i>_res.options</i>. This has the effect of trying a AAAA query before an A query inside the <code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3) function, and of mapping IPv4 responses in IPv6 &quot;tunneled form&quot; if no AAAA records are found but an A record set exists.</p>
<dt><code>ip6-bytestring</code> (since glibc 2.3.4)</p>
<dd>sets <code>RES_USE_BSTRING</code> in <i>_res.options</i>. This causes reverse IPv6 lookups to be made using the bit-label format described in RFC 2673; if this option is not set, then nibble format is used.</p>
<dt><code>ip6-dotint</code>/<code>no-ip6-dotint</code> (since glibc 2.3.4)</p>
<dd>Clear/set <code>RES_NOIP6DOTINT</code> in <i>_res.options</i>. When this option is clear (<code>ip6-dotint</code>), reverse IPv6 lookups are made in the (deprecated) <i>ip6.int</i> zone; when this option is set (<code>no-ip6-dotint</code>), reverse IPv6 lookups are made in the <i>ip6.arpa</i> zone by default. This option is set by default.</p>
<dt><code>edns0</code> (since glibc 2.6)</p>
<dd>sets <code>RES_USE_EDNSO</code> in <i>_res.options</i>. This enables support for the DNS extensions described in RFC 2671.</p>
<dt><code>single-request</code> (since glibc 2.10)</p>
<dd>sets <code>RES_SNGLKUP</code> in <i>_res.options</i>. By default, glibc performs IPv4 and IPv6 lookups in parallel since version 2.9. Some appliance DNS servers cannot handle these queries properly and make the requests time out. This option disables the behavior and makes glibc perform the IPv6 and IPv4 requests sequentially (at the cost of some slowdown of the resolving process).</p>
<dt><code>single-request-reopen</code> (since glibc 2.9)</p>
<dd>The resolver uses the same socket for the A and AAAA requests. Some hardware mistakenly sends back only one reply. When that happens the client system will sit and wait for the second reply. Turning this option on changes this behavior so that if two requests from the same port are not handled correctly it will close the socket and open a new one before sending the second request.</dl>
</dl>
</dl>
<p> The <i>domain</i> and <i>search</i> keywords are mutually exclusive. If more than one instance of these keywords is present, the last instance wins. </p>
<p> The <i>search</i> keyword of a system&#8217;s <i>resolv.conf</i> file can be overridden on a per-process basis by setting the environment variable <code>LOCALDOMAIN</code> to a space-separated list of search domains. </p>
<p> The <i>options</i> keyword of a system&#8217;s <i>resolv.conf</i> file can be amended on a per-process basis by setting the environment variable <code>RES_OPTIONS</code> to a space-separated list of resolver options as explained above under <code>options</code>. </p>
<p> The keyword and value must appear on a single line, and the keyword (e.g., <code>nameserver</code>) must start the line. The value follows the keyword, separated by white space. </p>
<p> Lines that contain a semicolon (;) or hash character (#) in the first column are treated as comments.</p>
<h2>Files</h2>
<p><i>/etc/resolv.conf</i>, <i>&lt;resolv.h&gt;</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3), <code><a href="/docs/linux/man/3-resolver/">resolver</a></code>(3), <code><a href="/docs/linux/man/7-hostname/">hostname</a></code>(7), <code><a href="/docs/linux/man/8-named/">named</a></code>(8)<br />
 Name Server Operations Guide for BIND</p>
<h2>Colophon</h2>
<p>This page is part of release 3.69 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="http://www.kernel.org/doc/man-pages/.">http://www.kernel.org/doc/man-pages/.</a> </p>
