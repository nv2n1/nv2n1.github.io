---
title: "in-rlogind(8)"
name: "in-rlogind"
section: "8"
letter: "i"
url: "/docs/linux/man/8-in-rlogind/"
description: "rlogind – remote login server"
---

<p><code>rlogind</code> &#8211; remote login server</p>
<h2>Synopsis</h2>
<p><code>rlogind</code> [-<code>ahlLn </code></p>
<h2>Description</h2>
<p>] <code>Rlogind</code> is the server for the <a href="/docs/linux/man/1-rlogin/">rlogin</a>(1) program. The server provides a remote login facility with authentication based on privileged port numbers from trusted hosts. </p>
<p> Options supported by <code>rlogind</code></p>
<dl>
<dt><code>-a</code></p>
<dd>Ask hostname for verification.</p>
<dt><code>-h</code></p>
<dd>Permit use of superuser &#8220;.rhosts &#8221; files.</p>
<dt><code>-l</code></p>
<dd>Prevent any authentication based on the user&#8217;s &#8220;.rhosts &#8221; file. If the user is logging in as the superuser and the -h option is used, &#8220;.rhosts &#8221; processing is still enabled.</p>
<dt><code>-L</code></p>
<dd>Prevent any authentication based on &#8220;.rhosts &#8221; or &#8220;hosts.equiv &#8221; information.</p>
<dt><code>-n</code></p>
<dd>Disable keep-alive messages.</dl>
<p> The -h, -l, and -L flags are not used if PAM (Pluggable Authentication Module) support is in use. In this case the same effects can be achieved by editing /etc/pam.conf </p>
<p> The &#8211;<code>h</code> and &#8211;<code>l</code> options should also not be trusted without verifying that they work as expected with the particular version of libc installed on your system (and should be tested again after any libc update) because some versions of libc may not honor the internal flags used by <code>rlogind</code> As the &#8211;<code>L</code> option bypasses the libc functions entirely, it is not subject to this problem. </p>
<p> Also note that the design of the .rhosts system is COMPLETELY INSECURE except on a carefully firewalled private network. Always use the &#8211;<code>L</code> option under all other circumstances. Also, since <code>rlogind</code> does not encrypt communications, it should not, in general, be used at all. Consider <a href="/docs/linux/man/8-ssh/">ssh</a>(8). </p>
<p> <code>Rlogind</code> listens for service requests at the port indicated in the &#8220;login&#8221; service specification; see <a href="/docs/linux/man/5-services/">services</a>(5). When a service request is received the following protocol is initiated: </p>
<ol>
<li> The server checks the client&#8217;s source port. If the port is not in the range 512-1023, the server aborts the connection.
<li> The server checks the client&#8217;s source address and requests the corresponding host name (see <a href="/docs/linux/man/3-gethostbyaddr/">gethostbyaddr</a>(3), <a href="/docs/linux/man/5-hosts/">hosts</a>(5) and <a href="/docs/linux/man/8-named/">named</a>(8)). If the hostname cannot be determined, the dot-notation representation of the host address is used. If the hostname is in the same domain as the server (according to the last two components of the domain name), or if the &#8211;<code>a</code> option is given, the addresses for the hostname are requested, verifying that the name and address correspond. Normal authentication is bypassed if the address verification fails. </ol>
<p> Once the source port and address have been checked, <code>rlogind</code> proceeds with the authentication process described in <a href="/docs/linux/man/8-rshd/">rshd</a>(8). It then allocates a pseudo terminal (see <a href="/docs/linux/man/4-pty/">pty</a>(4)), and manipulates file descriptors so that the slave half of the pseudo terminal becomes the <i>stdin</i> <i>stdout</i> and <i>stderr</i> for a login process. The login process is an instance of the <a href="/docs/linux/man/1-login/">login</a>(1) program, invoked with the &#8211;<code>f</code> option if authentication has succeeded. If automatic authentication fails, the user is prompted to log in as if on a standard terminal line. </p>
<p> The parent of the login process manipulates the master side of the pseudo terminal, operating as an intermediary between the login process and the client instance of the rlogin program. In normal operation, the packet protocol described in <a href="/docs/linux/man/4-pty/">pty</a>(4) is invoked to provide `^S/^Q&#8217; type facilities and propagate interrupt signals to the remote programs. The login process propagates the client terminal&#8217;s baud rate and terminal type, as found in the environment variable, `<code>TERM</code> &#8216; ; see <a href="/docs/linux/man/7-environ/">environ</a>(7). The screen or window size of the terminal is requested from the client, and window size changes from the client are propagated to the pseudo terminal. </p>
<p> Transport-level keepalive messages are enabled unless the &#8211;<code>n</code> option is present. The use of keepalive messages allows sessions to be timed out if the client crashes or becomes unreachable.</p>
<h2>Diagnostics</h2>
<p>All initial diagnostic messages are indicated by a leading byte with a value of 1, after which any network connections are closed. If there are no errors before login is invoked, a null byte is returned as in indication of success.</p>
<dl>
<dt><code>Try again.</code></p>
<dd>A fork by the server failed.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-login/">login</a>(1), <a href="/docs/linux/man/3-ruserok/">ruserok</a>(3), <a href="/docs/linux/man/8-rshd/">rshd</a>(8)</p>
<h2>Bugs</h2>
<p>The authentication procedure used here assumes the integrity of each client machine and the connecting medium. This is insecure, but is useful in an &#8220;open&#8221; environment. </p>
<p> A facility to allow all data exchanges to be encrypted should be present. </p>
<p> A more extensible protocol should be used.</p>
<h2>History</h2>
<p>The <code>rlogind</code> command appeared in BSD 4.2</p>
