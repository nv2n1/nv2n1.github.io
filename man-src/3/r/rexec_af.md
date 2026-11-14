---
title: "rexec_af(3)"
name: "rexec_af"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rexec_af/"
description: "rexec, rexec_af – return stream to a remote command"
---

<p>rexec, rexec_af &#8211; return stream to a remote command</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;netdb.h&gt;

int rexec(char **ahost, int inport, const char *user,
          const char *passwd, const char *cmd, int *fd2p);

int rexec_af(char **ahost, int inport, const char *user,
             const char *passwd, const char *cmd, int *fd2p,
             sa_family_t af);</code></pre>
<p> <code>rexec</code>(), <code>rexec_af</code>(): </p>
<pre> Since glibc 2.19:
 _DEFAULT_SOURCE
 In glibc up to and including 2.19:
 _BSD_SOURCE</pre>
<h2>Description</h2>
<p>This interface is obsoleted by <code><a href="/docs/linux/man/3-rcmd/">rcmd</a></code>(3). </p>
<p> The <code>rexec</code>() function looks up the host <i>*ahost</i> using <code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3), returning -1 if the host does not exist. Otherwise, <i>*ahost</i> is set to the standard name of the host. If a username and password are both specified, then these are used to authenticate to the foreign host; otherwise the environment and then the <i>.netrc</i> file in user&#8217;s home directory are searched for appropriate information. If all this fails, the user is prompted for the information. </p>
<p> The port <i>inport</i> specifies which well-known DARPA Internet port to use for the connection; the call <i>getservbyname(exec, tcp)</i> (see <code><a href="/docs/linux/man/3-getservent/">getservent</a></code>(3)) will return a pointer to a structure that contains the necessary port. The protocol for connection is described in detail in <code><a href="/docs/linux/man/8-rexecd/">rexecd</a></code>(8). </p>
<p> If the connection succeeds, a socket in the Internet domain of type <code>SOCK_STREAM</code> is returned to the caller, and given to the remote command as <i>stdin</i> and <i>stdout</i>. If <i>fd2p</i> is nonzero, then an auxiliary channel to a control process will be setup, and a file descriptor for it will be placed in <i>*fd2p</i>. The control process will return diagnostic output from the command (unit 2) on this channel, and will also accept bytes on this channel as being UNIX signal numbers, to be forwarded to the process group of the command. The diagnostic information returned does not include remote authorization failure, as the secondary connection is set up after authorization has been verified. If <i>fd2p</i> is 0, then the <i>stderr</i> (unit 2 of the remote command) will be made the same as the <i>stdout</i> and no provision is made for sending arbitrary signals to the remote process, although you may be able to get its attention by using out-of-band data.</p>
<h3>rexec_af()</h3>
<p>The <code>rexec</code>() function works over IPv4 (<code>AF_INET</code>). By contrast, the <code>rexec_af</code>() function provides an extra argument, <i>af</i>, that allows the caller to select the protocol. This argument can be specified as <code>AF_INET</code>, <code>AF_INET6</code>, or <code>AF_UNSPEC</code> (to allow the implementation to select the protocol).</p>
<h2>Versions</h2>
<p>The <code>rexec_af</code>() function was added to glibc in version 2.2.</p>
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
<td> <code>rexec</code>(), <code>rexec_af</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>These functions are not in POSIX.1. The <code>rexec</code>() function first appeared in 4.2BSD, and is present on the BSDs, Solaris, and many other systems. The <code>rexec_af</code>() function is more recent, and less widespread.</p>
<h2>Bugs</h2>
<p>The <code>rexec</code>() function sends the unencrypted password across the network. </p>
<p> The underlying service is considered a big security hole and therefore not enabled on many sites; see <code><a href="/docs/linux/man/8-rexecd/">rexecd</a></code>(8) for explanations.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-rcmd/">rcmd</a></code>(3), <code><a href="/docs/linux/man/8-rexecd/">rexecd</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
