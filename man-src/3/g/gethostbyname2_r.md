---
title: "gethostbyname2_r(3)"
name: "gethostbyname2_r"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gethostbyname2_r/"
description: "gethostbyname, gethostbyaddr, sethostent, gethostent, endhostent, h_errno, herror, hstrerror, gethostbyaddr_r, gethostbyname2, gethostbyname2_r, gethostbyname_r, gethostent_r – get network host entry"
---

<h2 class="name">NAME</h2>
<p> gethostbyname, gethostbyaddr, sethostent, gethostent, endhostent, h_errno, herror, hstrerror, gethostbyaddr_r, gethostbyname2, gethostbyname2_r, gethostbyname_r, gethostent_r &#8211; get network host entry </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;netdb.h&gt;
extern int h_errno;
struct hostent *gethostbyname(const char *name);
#include &lt;sys/socket.h&gt; /* for AF_INET */
struct hostent *gethostbyaddr(const void *addr,
                              socklen_t len, int type);
void sethostent(int stayopen);
void endhostent(void);
void herror(const char *s);
const char *hstrerror(int err);
/* System V/POSIX extension */
struct hostent *gethostent(void);
/* GNU extensions */
struct hostent *gethostbyname2(const char *name, int af);
int gethostent_r(
    struct hostent *ret, char *buf, size_t buflen,
    struct hostent **result, int *h_errnop);
int gethostbyaddr_r(const void *addr, socklen_t len, int type,
                    struct hostent *ret, char *buf, size_t buflen,
                    struct hostent **result, int *h_errnop);
int gethostbyname_r(const char *name,
                    struct hostent *ret, char *buf, size_t buflen,
                    struct hostent **result, int *h_errnop);
int gethostbyname2_r(const char *name, int af,
                     struct hostent *ret, char *buf, size_t buflen,
                     struct hostent **result, int *h_errnop);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>gethostbyname2</code>(), <code>gethostent_r</code>(), <code>gethostbyaddr_r</code>(), <code>gethostbyname_r</code>(), <code>gethostbyname2_r</code>():</p>
<dl>
<dt>
<dd>
<dl>
<dt>Since glibc 2.19:</p>
<dd> _DEFAULT_SOURCE</p>
<dt>Glibc versions up to and including 2.19:</p>
<dd> _BSD_SOURCE || _SVID_SOURCE</dl>
</dl>
<p> <code>herror</code>(), <code>hstrerror</code>():</p>
<dl>
<dt>
<dd>
<dl>
<dt>Since glibc 2.19:</p>
<dd> _DEFAULT_SOURCE</p>
<dt>Glibc 2.8 to 2.19:</p>
<dd> _BSD_SOURCE || _SVID_SOURCE</p>
<dt>Before glibc 2.8:</p>
<dd> none</dl>
</dl>
<p> <code>h_errno</code>:</p>
<dl>
<dt>
<dd>
<dl>
<dt>Since glibc 2.19</p>
<dd> _DEFAULT_SOURCE || _POSIX_C_SOURCE &lt; 200809L</p>
<dt>Glibc 2.12 to 2.19:</p>
<dd> _BSD_SOURCE || _SVID_SOURCE || _POSIX_C_SOURCE &lt; 200809L</p>
<dt>Before glibc 2.12:</p>
<dd> none</dl>
</dl>
<h2>DESCRIPTION</h2>
<p> The <code>gethostbyname*</code>(), <code>gethostbyaddr*</code>(), <code>herror</code>(), and <code>hstrerror</code>() functions are obsolete. Applications should use <code><a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a></code>(3), <code><a href="/docs/linux/man/3-getnameinfo/">getnameinfo</a></code>(3), and <code><a href="/docs/linux/man/3-gai_strerror/">gai_strerror</a></code>(3) instead. </p>
<p> The <code>gethostbyname</code>() function returns a structure of type <i>hostent</i> for the given host <i>name</i>. Here <i>name</i> is either a hostname or an IPv4 address in standard dot notation (as for <code><a href="/docs/linux/man/3-inet_addr/">inet_addr</a></code>(3)). If <i>name</i> is an IPv4 address, no lookup is performed and <code>gethostbyname</code>() simply copies <i>name</i> into the <i>h_name</i> field and its <i>struct in_addr</i> equivalent into the <i>h_addr_list[0]</i> field of the returned <i>hostent</i> structure. If <i>name</i> doesn&#8217;t end in a dot and the environment variable <code>HOSTALIASES</code> is set, the alias file pointed to by <code>HOSTALIASES</code> will first be searched for <i>name</i> (see <code><a href="/docs/linux/man/7-hostname/">hostname</a></code>(7) for the file format). The current domain and its parents are searched unless <i>name</i> ends in a dot. </p>
<p> The <code>gethostbyaddr</code>() function returns a structure of type <i>hostent</i> for the given host address <i>addr</i> of length <i>len</i> and address type <i>type</i>. Valid address types are <code>AF_INET</code> and <code>AF_INET6</code>. The host address argument is a pointer to a struct of a type depending on the address type, for example a <i>struct in_addr *</i> (probably obtained via a call to <code><a href="/docs/linux/man/3-inet_addr/">inet_addr</a></code>(3)) for address type <code>AF_INET</code>. </p>
<p> The <code>sethostent</code>() function specifies, if <i>stayopen</i> is true (1), that a connected TCP socket should be used for the name server queries and that the connection should remain open during successive queries. Otherwise, name server queries will use UDP datagrams. </p>
<p> The <code>endhostent</code>() function ends the use of a TCP connection for name server queries. </p>
<p> The (obsolete) <code>herror</code>() function prints the error message associated with the current value of <i>h_errno</i> on <i>stderr</i>. </p>
<p> The (obsolete) <code>hstrerror</code>() function takes an error number (typically <i>h_errno</i>) and returns the corresponding message string. </p>
<p> The domain name queries carried out by <code>gethostbyname</code>() and <code>gethostbyaddr</code>() rely on the Name Service Switch (<code><a href="/docs/linux/man/5-nsswitch-conf/">nsswitch.conf</a></code>(5)) configured sources or a local name server (<code><a href="/docs/linux/man/8-named/">named</a></code>(8)). The default action is to query the Name Service Switch (<code><a href="/docs/linux/man/5-nsswitch-conf/">nsswitch.conf</a></code>(5)) configured sources, failing that, a local name server (<code><a href="/docs/linux/man/8-named/">named</a></code>(8)).</p>
<h3>Historical</h3>
<p> The <code><a href="/docs/linux/man/5-nsswitch-conf/">nsswitch.conf</a></code>(5) file is the modern way of controlling the order of host lookups. </p>
<p> In glibc 2.4 and earlier, the <i>order</i> keyword was used to control the order of host lookups as defined in <i>/etc/host.conf</i> (<code><a href="/docs/linux/man/5-host-conf/">host.conf</a></code>(5)). </p>
<p> The <i>hostent</i> structure is defined in <i>&lt;netdb.h&gt;</i> as follows: </p>
<p> struct hostent {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;*h_name;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;official name of host&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;**h_aliases;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;alias list&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;h_addrtype;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;host address type&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;h_length;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;length of address&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;**h_addr_list;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;list of addresses&nbsp;*/ } #define h_addr h_addr_list[0] /* for backward compatibility */ </p>
<p> The members of the <i>hostent</i> structure are:</p>
<dl>
<dt><i>h_name</i></p>
<dd> The official name of the host.</p>
<dt><i>h_aliases</i></p>
<dd> An array of alternative names for the host, terminated by a null pointer.</p>
<dt><i>h_addrtype</i></p>
<dd> The type of address; always <code>AF_INET</code> or <code>AF_INET6</code> at present.</p>
<dt><i>h_length</i></p>
<dd> The length of the address in bytes.</p>
<dt><i>h_addr_list</i></p>
<dd> An array of pointers to network addresses for the host (in network byte order), terminated by a null pointer.</p>
<dt><i>h_addr</i></p>
<dd> The first address in <i>h_addr_list</i> for backward compatibility.</dl>
<h2>RETURN VALUE</h2>
<p> The <code>gethostbyname</code>() and <code>gethostbyaddr</code>() functions return the <i>hostent</i> structure or a null pointer if an error occurs. On error, the <i>h_errno</i> variable holds an error number. When non-NULL, the return value may point at static data, see the notes below.</p>
<h2>ERRORS</h2>
<p> The variable <i>h_errno</i> can have the following values:</p>
<dl>
<dt><code>HOST_NOT_FOUND</code></p>
<dd> The specified host is unknown.</p>
<dt><code>NO_DATA</code></p>
<dd> The requested name is valid but does not have an IP address. Another type of request to the name server for this domain may return an answer. The constant <code>NO_ADDRESS</code> is a synonym for <code>NO_DATA</code>.</p>
<dt><code>NO_RECOVERY</code></p>
<dd> A nonrecoverable name server error occurred.</p>
<dt><code>TRY_AGAIN</code></p>
<dd> A temporary error occurred on an authoritative name server. Try again later.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/host.conf</i></p>
<dd> resolver configuration file</p>
<dt><i>/etc/hosts</i></p>
<dd> host database file</p>
<dt><i>/etc/nsswitch.conf</i></p>
<dd> name service switch configuration</dl>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>gethostbyname</code>() </td>
<td>Thread safety</td>
<td> MT-Unsafe race:hostbyname env<br />
 locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>gethostbyaddr</code>() </td>
<td>Thread safety</td>
<td> MT-Unsafe race:hostbyaddr env<br />
 locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>sethostent</code>(),<br />
 <code>endhostent</code>(),<br />
 <code>gethostent_r</code>() </td>
<td>Thread safety</td>
<td> MT-Unsafe race:hostent env<br />
 locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>herror</code>(),<br />
 <code>hstrerror</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
<tr VALIGN=top>
<td> <code>gethostent</code>() </td>
<td>Thread safety</td>
<td> MT-Unsafe race:hostent<br />
 race:hostentbuf env locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>gethostbyname2</code>() </td>
<td>Thread safety</td>
<td> MT-Unsafe race:hostbyname2<br />
 env locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>gethostbyaddr_r</code>(), <code>gethostbyname_r</code>(), <code>gethostbyname2_r</code>() </td>
<td>Thread safety</td>
<td>MT-Safe env locale
</td>
</tr>
</table>
<p> In the above table, <i>hostent</i> in <i>race:hostent</i> signifies that if any of the functions <code>sethostent</code>(), <code>gethostent</code>(), <code>gethostent_r</code>(), or <code>endhostent</code>() are used in parallel in different threads of a program, then data races could occur.</p>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001 specifies <code>gethostbyname</code>(), <code>gethostbyaddr</code>(), <code>sethostent</code>(), <code>endhostent</code>(), <code>gethostent</code>(), and <i>h_errno</i>; <code>gethostbyname</code>(), <code>gethostbyaddr</code>(), and <i>h_errno</i> are marked obsolescent in that standard. POSIX.1-2008 removes the specifications of <code>gethostbyname</code>(), <code>gethostbyaddr</code>(), and <i>h_errno</i>, recommending the use of <code><a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a></code>(3) and <code><a href="/docs/linux/man/3-getnameinfo/">getnameinfo</a></code>(3) instead.</p>
<h2>NOTES</h2>
<p> The functions <code>gethostbyname</code>() and <code>gethostbyaddr</code>() may return pointers to static data, which may be overwritten by later calls. Copying the <i>struct hostent</i> does not suffice, since it contains pointers; a deep copy is required. </p>
<p> In the original BSD implementation the <i>len</i> argument of <code>gethostbyname</code>() was an <i>int</i>. The SUSv2 standard is buggy and declares the <i>len</i> argument of <code>gethostbyaddr</code>() to be of type <i>size_t</i>. (That is wrong, because it has to be <i>int</i>, and <i>size_t</i> is not. POSIX.1-2001 makes it <i>socklen_t</i>, which is OK.) See also <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2). </p>
<p> The BSD prototype for <code>gethostbyaddr</code>() uses <i>const char&nbsp;*</i> for the first argument.</p>
<h3>System V/POSIX extension</h3>
<p> POSIX requires the <code>gethostent</code>() call, which should return the next entry in the host data base. When using DNS/BIND this does not make much sense, but it may be reasonable if the host data base is a file that can be read line by line. On many systems, a routine of this name reads from the file <i>/etc/hosts</i>. It may be available only when the library was built without DNS support. The glibc version will ignore ipv6 entries. This function is not reentrant, and glibc adds a reentrant version <code>gethostent_r</code>().</p>
<h3>GNU extensions</h3>
<p> Glibc2 also has a <code>gethostbyname2</code>() that works like <code>gethostbyname</code>(), but permits to specify the address family to which the address must belong. </p>
<p> Glibc2 also has reentrant versions <code>gethostent_r</code>(), <code>gethostbyaddr_r</code>(), <code>gethostbyname_r</code>(), and <code>gethostbyname2_r</code>(). The caller supplies a <i>hostent</i> structure <i>ret</i> which will be filled in on success, and a temporary work buffer <i>buf</i> of size <i>buflen</i>. After the call, <i>result</i> will point to the result on success. In case of an error or if no entry is found <i>result</i> will be NULL. The functions return 0 on success and a nonzero error number on failure. In addition to the errors returned by the nonreentrant versions of these functions, if <i>buf</i> is too small, the functions will return <code>ERANGE</code>, and the call should be retried with a larger buffer. The global variable <i>h_errno</i> is not modified, but the address of a variable in which to store error numbers is passed in <i>h_errnop</i>.</p>
<h2>BUGS</h2>
<p> <code>gethostbyname</code>() does not recognize components of a dotted IPv4 address string that are expressed in hexadecimal.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a></code>(3), <code><a href="/docs/linux/man/3-getnameinfo/">getnameinfo</a></code>(3), <code><a href="/docs/linux/man/3-inet/">inet</a></code>(3), <code><a href="/docs/linux/man/3-inet_ntop/">inet_ntop</a></code>(3), <code><a href="/docs/linux/man/3-inet_pton/">inet_pton</a></code>(3), <code><a href="/docs/linux/man/3-resolver/">resolver</a></code>(3), <code><a href="/docs/linux/man/5-hosts/">hosts</a></code>(5), <code><a href="/docs/linux/man/5-nsswitch-conf/">nsswitch.conf</a></code>(5), <code><a href="/docs/linux/man/7-hostname/">hostname</a></code>(7), <code><a href="/docs/linux/man/8-named/">named</a></code>(8)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
