---

title: "freehostent(3)"
name: "freehostent"
section: "3"
letter: "f"
url: "/docs/linux/man/3-freehostent/"
---

getipnodebyname, getipnodebyaddr, freehostent - get network hostnames and addresses 

<pre><code>
#include &lt;netdb.h&gt;
#include &lt;sys/socket.h&gt;
#include &lt;sys/types.h&gt;
struct hostent *getipnodebyname(const char *name, int af,
                                int flags, int *error_num);
struct hostent *getipnodebyaddr(const void *addr, size_t len,
                                int af, int *error_num);
void freehostent(struct hostent *ip);
</code></pre>

These functions are deprecated (and unavailable in glibc). Use <b><a HREF="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a></b>(3) and <b><a HREF="/docs/linux/man/3-getnameinfo/">getnameinfo</a></b>(3) instead. 

 The <b>getipnodebyname</b>() and <b>getipnodebyaddr</b>() functions return the names and addresses of a network host. These functions return a pointer to the following structure: 

 struct hostent { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;*h_name; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;**h_aliases; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;h_addrtype; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;h_length; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;**h_addr_list; }; 

 These functions replace the <b><a HREF="/docs/linux/man/3-gethostbyname/">gethostbyname</a></b>(3) and <b><a HREF="/docs/linux/man/3-gethostbyaddr/">gethostbyaddr</a></b>(3) functions, which could access only the IPv4 network address family. The <b>getipnodebyname</b>() and <b>getipnodebyaddr</b>() functions can access multiple network address families. 

 Unlike the <b>gethostby</b> functions, these functions return pointers to dynamically allocated memory. The <b>freehostent</b>() function is used to release the dynamically allocated memory after the caller no longer needs the <i>hostent</i> structure.

<h3>getipnodebyname() arguments</h3>

 The <b>getipnodebyname</b>() function looks up network addresses for the host specified by the <i>name</i> argument. The <i>af</i> argument specifies one of the following values:
<dl>
<dt><b>AF_INET</b>
</dt><dd> The <i>name</i> argument points to a dotted-quad IPv4 address or a name of an IPv4 network host.
</dd><dt><b>AF_INET6</b>
</dt><dd> The <i>name</i> argument points to a hexadecimal IPv6 address or a name of an IPv6 network host.</dd></dl>
 

 The <i>flags</i> argument specifies additional options. More than one option can be specified by bitwise OR-ing them together. <i>flags</i> should be set to 0 if no options are desired.
<dl>
<dt><b>AI_V4MAPPED</b>
</dt><dd> This flag is used with <b>AF_INET6</b> to request a query for IPv4 addresses instead of IPv6 addresses; the IPv4 addresses will be mapped to IPv6 addresses.
</dd><dt><b>AI_ALL</b>
</dt><dd> This flag is used with <b>AI_V4MAPPED</b> to request a query for both IPv4 and IPv6 addresses. Any IPv4 address found will be mapped to an IPv6 address.
</dd><dt><b>AI_ADDRCONFIG</b>
</dt><dd> This flag is used with <b>AF_INET6</b> to further request that queries for IPv6 addresses should not be made unless the system has at least one IPv6 address assigned to a network interface, and that queries for IPv4 addresses should not be made unless the system has at least one IPv4 address assigned to a network interface. This flag may be used by itself or with the <b>AI_V4MAPPED</b> flag.
</dd><dt><b>AI_DEFAULT</b>
</dt><dd> This flag is equivalent to <b>(AI_ADDRCONFIG | AI_V4MAPPED)</b>.</dd></dl>

<h3>getipnodebyaddr() arguments</h3>

 The <b>getipnodebyaddr</b>() function looks up the name of the host whose network address is specified by the <i>addr</i> argument. The <i>af</i> argument specifies one of the following values:
<dl>
<dt><b>AF_INET</b>
</dt><dd> The <i>addr</i> argument points to a <i>struct in_addr</i> and <i>len</i> must be set to <i>sizeof(struct in_addr)</i>.
</dd><dt><b>AF_INET6</b>
</dt><dd> The <i>addr</i> argument points to a <i>struct in6_addr</i> and <i>len</i> must be set to <i>sizeof(struct in6_addr)</i>.</dd></dl>

<h2>RETURN VALUE</h2>

 NULL is returned if an error occurred, and <i>error_num</i> will contain an error code from the following list:
<dl>
<dt><b>HOST_NOT_FOUND</b>
</dt><dd> The hostname or network address was not found.
</dd><dt><b>NO_ADDRESS</b>
</dt><dd> The domain name server recognized the network address or name, but no answer was returned. This can happen if the network host has only IPv4 addresses and a request has been made for IPv6 information only, or vice versa.
</dd><dt><b>NO_RECOVERY</b>
</dt><dd> The domain name server returned a permanent failure response.
</dd><dt><b>TRY_AGAIN</b>
</dt><dd> The domain name server returned a temporary failure response. You might have better luck next time.</dd></dl>
 

 A successful query returns a pointer to a <i>hostent</i> structure that contains the following fields:
<dl>
<dt><i>h_name</i>
</dt><dd> This is the official name of this network host.
</dd><dt><i>h_aliases</i>
</dt><dd> This is an array of pointers to unofficial aliases for the same host. The array is terminated by a null pointer.
</dd><dt><i>h_addrtype</i>
</dt><dd> This is a copy of the <i>af</i> argument to <b>getipnodebyname</b>() or <b>getipnodebyaddr</b>(). <i>h_addrtype</i> will always be <b>AF_INET</b> if the <i>af</i> argument was <b>AF_INET</b>. <i>h_addrtype</i> will always be <b>AF_INET6</b> if the <i>af</i> argument was <b>AF_INET6</b>.
</dd><dt><i>h_length</i>
</dt><dd> This field will be set to <i>sizeof(struct in_addr)</i> if <i>h_addrtype</i> is <b>AF_INET</b>, and to <i>sizeof(struct in6_addr)</i> if <i>h_addrtype</i> is <b>AF_INET6</b>.
</dd><dt><i>h_addr_list</i>
</dt><dd> This is an array of one or more pointers to network address structures for the network host. The array is terminated by a null pointer.</dd></dl>

<h2>CONFORMING TO</h2>

 RFC 2553.

<h2>NOTES</h2>

 These functions were present in glibc 2.1.91-95, but were removed again. Several UNIX-like systems support them, but all call them deprecated.

<h2>SEE ALSO</h2>

 <b><a HREF="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a></b>(3), <b><a HREF="/docs/linux/man/3-getnameinfo/">getnameinfo</a></b>(3), <b>inet_ntop</b>(3), <b>inet_pton</b>(3)

<h2>COLOPHON</h2>

 This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" HREF="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a>
