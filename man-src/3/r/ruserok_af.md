---
title: "ruserok_af(3)"
name: "ruserok_af"
section: "3"
letter: "r"
url: "/docs/linux/man/3-ruserok_af/"
description: "rcmd, rresvport, iruserok, ruserok, rcmd_af, rresvport_af, iruserok_af, ruserok_af – routines for returning a stream to a remote command"
---

<p>rcmd, rresvport, iruserok, ruserok, rcmd_af, rresvport_af, iruserok_af, ruserok_af &#8211; routines for returning a stream to a remote command</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;netdb.h&gt; /* Or &lt;unistd.h&gt; on some systems */

int rcmd(char **ahost, unsigned short inport, const char *locuser,
         const char *remuser, const char *cmd, int *fd2p);

int rresvport(int *port);

int iruserok(uint32_t raddr, int superuser,
             const char *ruser, const char *luser);

int ruserok(const char *rhost, int superuser,
            const char *ruser, const char *luser);

int rcmd_af(char **ahost, unsigned short inport, const char *locuser,
            const char *remuser, const char *cmd, int *fd2p,
            sa_family_t af);

int rresvport_af(int *port, sa_family_t af);

int iruserok_af(const void *raddr, int superuser,
                const char *ruser, const char *luser, sa_family_t af);

int ruserok_af(const char *rhost, int superuser,
               const char *ruser, const char *luser, sa_family_t af);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>rcmd</code>(), <code>rcmd_af</code>(), <code>rresvport</code>(), <code>rresvport_af</code>(), <code>iruserok</code>(), <code>iruserok_af</code>(), <code>ruserok</code>(), <code>ruserok_af</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE</p>
<h2>Description</h2>
<p>The <code>rcmd</code>() function is used by the superuser to execute a command on a remote machine using an authentication scheme based on privileged port numbers. The <code>rresvport</code>() function returns a file descriptor to a socket with an address in the privileged port space. The <code>iruserok</code>() and <code>ruserok</code>() functions are used by servers to authenticate clients requesting service with <code>rcmd</code>(). All four functions are used by the <code><a href="/docs/linux/man/8-rshd/">rshd</a></code>(8) server (among others).</p>
<h3>rcmd()</h3>
<p>The <code>rcmd</code>() function looks up the host <i>*ahost</i> using <code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3), returning -1 if the host does not exist. Otherwise, <i>*ahost</i> is set to the standard name of the host and a connection is established to a server residing at the well-known Internet port <i>inport</i>. </p>
<p> If the connection succeeds, a socket in the Internet domain of type <code>SOCK_STREAM</code> is returned to the caller, and given to the remote command as <i>stdin</i> and <i>stdout</i>. If <i>fd2p</i> is nonzero, then an auxiliary channel to a control process will be set up, and a file descriptor for it will be placed in <i>*fd2p</i>. The control process will return diagnostic output from the command (unit 2) on this channel, and will also accept bytes on this channel as being UNIX signal numbers, to be forwarded to the process group of the command. If <i>fd2p</i> is 0, then the <i>stderr</i> (unit 2 of the remote command) will be made the same as the <i>stdout</i> and no provision is made for sending arbitrary signals to the remote process, although you may be able to get its attention by using out-of-band data. </p>
<p> The protocol is described in detail in <code><a href="/docs/linux/man/8-rshd/">rshd</a></code>(8).</p>
<h3>rresvport()</h3>
<p>The <code>rresvport</code>() function is used to obtain a socket with a privileged port bound to it. This socket is suitable for use by <code>rcmd</code>() and several other functions. Privileged ports are those in the range 0 to 1023. Only a privileged process (on Linux: a process that has the <code>CAP_NET_BIND_SERVICE</code> capability in the user namespace governing its network namespace). is allowed to bind to a privileged port. In the glibc implementation, this function restricts its search to the ports from 512 to 1023. The <i>port</i> argument is value-result: the value it supplies to the call is used as the starting point for a circular search of the port range; on (successful) return, it contains the port number that was bound to.</p>
<h3>iruserok() and ruserok()</h3>
<p>The <code>iruserok</code>() and <code>ruserok</code>() functions take a remote host&#8217;s IP address or name, respectively, two usernames and a flag indicating whether the local user&#8217;s name is that of the superuser. Then, if the user is <i>not</i> the superuser, it checks the <i>/etc/hosts.equiv</i> file. If that lookup is not done, or is unsuccessful, the <i>.rhosts</i> in the local user&#8217;s home directory is checked to see if the request for service is allowed. </p>
<p> If this file does not exist, is not a regular file, is owned by anyone other than the user or the superuser, is writable by anyone other than the owner, or is hardlinked anywhere, the check automatically fails. Zero is returned if the machine name is listed in the <i>hosts.equiv</i> file, or the host and remote username are found in the <i>.rhosts</i> file; otherwise <code>iruserok</code>() and <code>ruserok</code>() return -1. If the local domain (as obtained from <code><a href="/docs/linux/man/2-gethostname/">gethostname</a></code>(2)) is the same as the remote domain, only the machine name need be specified. </p>
<p> If the IP address of the remote host is known, <code>iruserok</code>() should be used in preference to <code>ruserok</code>(), as it does not require trusting the DNS server for the remote host&#8217;s domain.</p>
<h3>*_af() variants</h3>
<p>All of the functions described above work with IPv4 (<code>AF_INET</code>) sockets. The &quot;_af&quot; variants take an extra argument that allows the socket address family to be specified. For these functions, the <i>af</i> argument can be specified as <code>AF_INET</code> or <code>AF_INET6</code>. In addition, <code>rcmd_af</code>() supports the use of <code>AF_UNSPEC</code>.</p>
<h2>Return Value</h2>
<p>The <code>rcmd</code>() function returns a valid socket descriptor on success. It returns -1 on error and prints a diagnostic message on the standard error. </p>
<p> The <code>rresvport</code>() function returns a valid, bound socket descriptor on success. It returns -1 on error with the global value <i>errno</i> set according to the reason for failure. The error code <code>EAGAIN</code> is overloaded to mean &quot;All network ports in use.&quot; </p>
<p> For information on the return from <code>ruserok</code>() and <code>iruserok</code>(), see above.</p>
<h2>Versions</h2>
<p>The functions <code>iruserok_af</code>(), <code>rcmd_af</code>(), <code>rresvport_af</code>(), and <code>ruserok_af</code>() functions are provide in glibc since version 2.2.</p>
<h2>Attributes</h2>
<p>For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>rcmd</code>(), <code>rcmd_af</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe
</td>
</tr>
<tr VALIGN=top>
<td> <code>rresvport</code>(), <code>rresvport_af</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
<tr VALIGN=top>
<td> <code>iruserok</code>(), <code>ruserok</code>(),<br />
 <code>iruserok_af</code>(), <code>ruserok_af</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>Not in POSIX.1. Present on the BSDs, Solaris, and many other systems. These functions appeared in 4.2BSD. The &quot;_af&quot; variants are more recent additions, and are not present on as wide a range of systems.</p>
<h2>Bugs</h2>
<p><code>iruserok</code>() and <code>iruserok_af</code>() are declared in glibc headers only since version 2.12.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-rlogin/">rlogin</a></code>(1), <code><a href="/docs/linux/man/1-rsh/">rsh</a></code>(1), <code><a href="/docs/linux/man/3-rexec/">rexec</a></code>(3), <code><a href="/docs/linux/man/8-rexecd/">rexecd</a></code>(8), <code><a href="/docs/linux/man/8-rlogind/">rlogind</a></code>(8), <code><a href="/docs/linux/man/8-rshd/">rshd</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
