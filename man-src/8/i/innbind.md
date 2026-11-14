---
title: "innbind(8)"
name: "innbind"
section: "8"
letter: "i"
url: "/docs/linux/man/8-innbind/"
description: "innbind – Helper program to bind sockets to privileged ports"
---

<p>innbind &#8211; Helper program to bind sockets to privileged ports</p>
<h2>Synopsis</h2>
<p><code>innbind</code> [<code>-p</code>] <i>fd</i>,<i>family</i>,<i>address</i>,<i>port</i> [&#8230;]</p>
<h2>Description</h2>
<p><code>innbind</code> is a helper program that&#8217;s not meant to be run directly. Instead, <code>innd</code> and <code>nnrpd</code> use it internally to bind to ports that require root privileges to bind to. </p>
<p> This program must be installed setuid root in order for <code>innd</code> or <code>nnrpd</code> to bind to ports under 1024. The only functions that it&#8217;s willing to perform are to bind an open file descriptor to a given address and port or to create a new socket, bind it, and return the bound socket to its caller. It can only be run as the news user (as specified at configure time), and will only bind to ports 119, 433, 563, an additional port specified with the <code>&#8211;with-innd-port</code> argument to configure, or ports numbered 1024 or higher. </p>
<p> Each argument to <code>innbind</code> must be a comma-separated list of four elements. The first is the file descriptor number that should be bound, the second is the numeric family of the socket (<font SIZE="-1">AF_INET</font> or <font SIZE="-1">AF_INET6</font>), the third is the local address to bind to (in dotted-quad format for IPv4 and in colon-separated address format for IPv6), and the fourth is the port number. To bind to all addresses with IPv4, use <tt>0.0.0.0</tt> as the address. To bind to all addresses with IPv6, use <tt>&quot;::&quot;</tt> as the address. </p>
<p> Multiple arguments can be specified to tell <code>innbind</code> to bind multiple sockets at the same time. Any errors (other than permission denied &#8212; see below) encountered will cause <code>innbind</code> to abort, and error messages will be sent both to syslog and to standard error. </p>
<p> By default, <code>innbind</code> attempts to just bind the already open file descriptor that it inherits from its caller. For each successfully bound file descriptor (in the order given on the command line), <code>innbind</code> prints <tt>&quot;ok&quot;</tt> and a newline to its standard output. </p>
<p> On some systems (apparently just STREAMS-based systems), however, even a setuid root program cannot bind a socket to a privileged port that was created by a process that didn&#8217;t have permissions. If <code>innbind</code> gets permission denied when trying to bind a socket, it will print <tt>&quot;no&quot;</tt> and a newline to its standard output. It will then create a new socket, bind it as specified, and then attempt to pass that socket back to its caller using the I_SENDFD <font SIZE="-1">STREAMS</font> ioctl. The caller should receive that file descriptor with I_RECVFD and use it instead of the one that it created. </p>
<p> Note that file descriptor passing is only supported on STREAMS-based systems since it is done with ioctls over a pipe. However, it is believed that those systems are exactly the systems that can&#8217;t simply bind the inherited file descriptor. If this assumption proves to be incorrect, traditional <font SIZE="-1">BSD</font> file descriptor passing over a Unix domain socket will have to be added.</p>
<h2>Options</h2>
<dl>
<dt><code>-p</code></p>
<dd>If given as the first command-line argument, no attempt will be made to bind the inherited file descriptor and <code>innbind</code> will only try creation of a new file descriptor and passing it back via standard output. This option is primarily useful for testing.</dl>
<h2>Security</h2>
<p>As <code>innbind</code> is normally installed setuid root, security is even more of an issue for it than for other parts of <font SIZE="-1">INN</font>. It is a fairly short program, and if you understand C, you are encouraged to audit it yourself to be certain that it does only what it is supposed to do. The only <font SIZE="-1">INN</font> library functions it uses are the vector functions, the message functions for error reporting, and xstrdup. </p>
<p> The ports that will be bound are restricted to prevent potential attacks made possible by the ability to bind low-numbered ports, such as exploits of the <i><a href="/docs/linux/man/1-rsh/">rsh</a></i>(1) family of commands on some systems. If <code>innbind</code> is installed setuid root, it can only be executed by the news user to prevent other users on the system from being able to bind to even those few privileged ports that it allows. </p>
<p> <code>innbind</code> uses no external configuration files; the only files it might open are through the system <i><a href="/docs/linux/man/3-getpwnam/">getpwnam</a></i>(3) service to get the <font SIZE="-1">UID</font> of the news user. The only user input that it accepts are its command-line arguments.</p>
<h2>Diagnostics</h2>
<p><code>innbind</code> may log the following messages to syslog and print them to standard error.</p>
<dl>
<dt>cannot create socket for %s: %s</p>
<dd>(Fatal) <code>innbind</code> fell back on attempting to create a new socket to bind for the given argument, and the socket creation failed.</p>
<dt>cannot bind socket for %s: %s</p>
<dd>(Fatal) Calling bind for the socket corresponding to the given argument failed with a system error. If the error indicates permission denied, make sure that <code>innbind</code> is setuid root. This can also be caused by trying to use IPv6 on a system whose kernel does not support it.</p>
<dt>cannot bind to restricted port %hu in %s</p>
<dd>(Fatal) The port number portion of the given command-line argument is for a port below 1024 which is not 119, 433, 563, or a port given to <code>&#8211;with-innd-port</code> at configure time. Other ports are not allowed for security reasons.</p>
<dt>cannot get socket options for file descriptor %d: %s</p>
<dd>(Fatal) <code>innbind</code> was unable to get the socket options for that file descriptor. The most likely cause of this error is passing the wrong file descriptor number to <code>innbind</code> (a file descriptor that isn&#8217;t open, or that corresponds to a regular file rather than a network socket).</p>
<dt>cannot get <font SIZE="-1">UID</font> for %s</p>
<dd>(Fatal) <code>innbind</code> was unable to get the <font SIZE="-1">UID</font> for the news user specified during configure (and defaulting to <tt>&quot;news&quot;</tt>). This normally means that user isn&#8217;t in the system <i>passwd</i> file.</p>
<dt>cannot mark socket reusable for %s: %s</p>
<dd>(Fatal) <code>innbind</code> created a new socket for the given argument but was unable to mark its bind address reusable (the <font SIZE="-1">SO_REUSEADDR</font> socket option).</p>
<dt>cannot pass file descriptor: %s</p>
<dd>(Fatal) <code>innbind</code> created and bound a new file descriptor but was unable to pass it back to its caller via its standard output, using the I_SENDFD <font SIZE="-1">STREAMS</font> ioctl.</p>
<dt>invalid file descriptor %d: not <font SIZE="-1">SOCK_STREAM</font></p>
<dd>(Fatal) The given file descriptor is not a <font SIZE="-1">SOCK_STREAM</font> socket. <code>innbind</code> can only bind <font SIZE="-1">SOCK_STREAM</font> sockets.</p>
<dt>invalid IPv4 address %s in %s</p>
<dd>(Fatal) The IPv4 address specified in the given command-line option could not be parsed by <i><a href="/docs/linux/man/3-inet_aton/">inet_aton</a></i>(3). IPv4 addresses should be specified in the standard dotted-quad format (10.2.3.4).</p>
<dt>invalid IPv6 address %s in %s</p>
<dd>(Fatal) The IPv6 address specified in the given command-line option could not be parsed by <i><a href="/docs/linux/man/3-inet_pton/">inet_pton</a></i>(3). IPv6 addresses should be specified in <font SIZE="-1">RFC</font>&nbsp;<wbr>4291 format (1080:0:0:0:8:800:200C:417A or 1080::8:800:200C:417A).</p>
<dt>invalid command-line argument %s</p>
<dd>(Fatal) The specified command-line argument could not be parsed or was not in the correct format.</p>
<dt>invalid file descriptor %s in %s</p>
<dd>(Fatal) The file descriptor portion of the given command-line argument is not a non-negative integer.</p>
<dt>invalid port number %s in %s</p>
<dd>(Fatal) The port number portion of the given command-line argument is not a non-negative integer.</p>
<dt>invalid protocol family %s in %s</p>
<dd>(Fatal) The protocol family portion of the given command-line argument is not a non-negative integer. It should be equal to either <font SIZE="-1">AF_INET</font> or <font SIZE="-1">AF_INET6</font> on the system where <code>innbind</code> is run.</p>
<dt>must be run by user %s (%lu), not %lu</p>
<dd>(Fatal) When setuid root, <code>innbind</code> may only be run by the news user as specified at configure time (<tt>&quot;news&quot;</tt> by default), for security reasons.</p>
<dt>no addresses specified</p>
<dd>(Fatal) No arguments were given on the command line (except maybe <code>-p</code>).</p>
<dt>port may not be zero in %s</p>
<dd>(Fatal) The port number portion of the given command-line argument was zero.</p>
<dt>unknown protocol family %s in %s</p>
<dd>(Fatal) The protocol number portion of the given command-line argument is neither <font SIZE="-1">AF_INET</font> nor <font SIZE="-1">AF_INET6</font>.</dl>
<h2>Examples</h2>
<p>As mentioned above, <code>innbind</code> is never run directly, only by <code>innd</code> and other programs that need to bind to and listen to network ports. Sample invocations by <code>innd</code> would be: </p>
<pre> innbind 3,10,::,119</pre>
<p>to bind the IPv6 socket on file descriptor 3 to port 119, all addresses, or: </p>
<pre> innbind 6,2,10.0.0.3,433</pre>
<p>to bind the IPv4 socket on file descriptor 6 to port 433 in the address 10.0.0.3.</p>
<h2>History</h2>
<p>Written by Russ Allbery &lt;eagle [at] eyrie.org&gt; for InterNetNews. </p>
<p> <tt>$Id:</tt> innbind.pod 9768 2014-12-07 21:22:57Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/3-inet_aton/">inet_aton</a></i>(3), <i><a href="/docs/linux/man/3-inet_pton/">inet_pton</a></i>(3), <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8), <i><a href="/docs/linux/man/8-nnrpd/">nnrpd</a></i>(8). </p>
