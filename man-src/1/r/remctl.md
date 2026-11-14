---
title: "remctl(1)"
name: "remctl"
section: "1"
letter: "r"
url: "/docs/linux/man/1-remctl/"
description: "remctl – Remote execution tool"
---

<h2 class="name">NAME</h2>
<p> remctl &#8211; Remote execution tool </p>
<h2>SYNOPSIS</h2>
<p> remctl [<code>-dhv</code>] [<code>-b</code> <i>source-ip</i>] [<code>-p</code> <i>port</i>] [<code>-s</code> <i>service</i>]<br />
&nbsp;<wbr><i>host</i>&nbsp;<wbr><i>command</i>&nbsp;<wbr>[<i>subcommand</i>&nbsp;<wbr>[<i>parameters</i>&nbsp;<wbr>&#8230;]]</p>
<h2>DESCRIPTION</h2>
<p> <code>remctl</code> is a program that allows a user to execute commands remotely on a server that is running the remctld daemon. <code>remctl</code> does not interpret the commands given to it. It passes them to the server and displays the return message. The commands must be defined on the server-side before a <code>remctl</code> client can execute them, and the user running <code>remctl</code> must be authorized to execute the particular command on the server. </p>
<p> Access to remote commands is authenticated via Kerberos GSS-API, so a user must have a ticket granting ticket to use <code>remctl</code>. All transmissions to and from the remctld server are encrypted using GSS-API&#8217;s security layer. </p>
<p> <i>host</i> is the hostname of the target server. <i>command</i> and <i>subcommand</i> together specify the command to run and correspond to the command names in the configuration file on the server. <i>parameters</i> are any additional command-line parameters to pass to the remote command.</p>
<h2>OPTIONS</h2>
<p> The start of each option description is annotated with the version of <code>remctl</code> in which that option was added with its current meaning.</p>
<dl>
<dt><code>-b</code> <i>source-ip</i></p>
<dd> [3.0] When connecting to the remote remctl server, use <i>source-ip</i> as the source <font SIZE="-1">IP</font> address. This can be useful on multihomed systems where the remctl connections need to be made over a particular network. <i>source-ip</i> must be an <font SIZE="-1">IP</font> address, not a hostname, and can be either an IPv4 or IPv6 address (assuming IPv6 is supported).</p>
<dt><code>-d</code></p>
<dd> [1.10] Turn on extra debugging output of the client-server interaction.</p>
<dt><code>-h</code></p>
<dd> [1.10] Show a brief usage message and then exit.</p>
<dt><code>-p</code> <i>port</i></p>
<dd> [1.0] Connect to the server on <i>port</i>. If this option isn&#8217;t given, the client first tries the registered remctl port (4373) and then falls back on the legacy port (4444) if that fails.</p>
<dt><code>-s</code> <i>service</i></p>
<dd> [1.0] Authenticate to the server with a service ticket for <i>service</i> rather than the default server identity of host/<i>hostname</i>. This may be necessary with, for instance, a server where <code>remctld</code> is not running as root.</p>
<dt><code>-v</code></p>
<dd> [1.10] Print the version of <code>remctl</code> and exit.</dl>
<h2>EXIT STATUS</h2>
<p> <code>remctl</code> will exit with the exit status returned by the remote command. If some network or authentication error occurred and <code>remctl</code> was unable to run the remote command or retrieve its exit status, or if <code>remctl</code> was called with invalid arguments, <code>remctl</code> will exit with status 1.</p>
<h2>EXAMPLES</h2>
<p> Release an <font SIZE="-1">AFS</font> volume called ls.tripwire: </p>
<pre>
    remctl lsdb afs release ls.tripwire
</pre>
<h2>COMPATIBILITY</h2>
<p> The default port was changed to the IANA-registered port of 4373 in version 2.11. </p>
<p> Support for IPv6 was added in version 2.4.</p>
<h2>CAVEATS</h2>
<p> If no principal is specified with <code>-s</code>, <code>remctl</code> canonicalizes the server host name using <font SIZE="-1">DNS</font> before connecting. This ensures that the network connection and the GSS-API authentication use the same server name even if some common DNS-based load-balancing schemes are in use. To disable this canonicalization, specify the server principal using <code>-s</code>. </p>
<p> The default behavior, when the port is not specified, of trying 4373 and falling back to 4444 will be removed in a future version of <code>remctl</code> in favor of using the <tt>&quot;remctl&quot;</tt> service in <i>/etc/services</i> if set and then falling back on only 4373. 4444 was the poorly-chosen original remctl port and should be phased out. </p>
<p> When using Heimdal with triple-DES keys and talking to old servers that only speak version one of the remctl protocol, <code>remctl</code> may have problems with <font SIZE="-1">MIC</font> verification. This doesn&#8217;t affect new clients and servers since the version two protocol doesn&#8217;t use MICs. If you are using Heimdal and run into <font SIZE="-1">MIC</font> verification problems, see the <font SIZE="-1">COMPATIBILITY</font> section of <i><a href="/docs/linux/man/3-gssapi/">gssapi</a></i>(3).</p>
<h2>NOTES</h2>
<p> The remctl port number, 4373, was derived by tracing the diagonals of a <font SIZE="-1">QWERTY</font> keyboard up from the letters <tt>&quot;remc&quot;</tt> to the number row.</p>
<h2>AUTHOR</h2>
<p> <code>remctl</code> was originally written by Anton Ushakov. Updates and current maintenance are done by Russ Allbery &lt;eagle [at] eyrie.org&gt;.</p>
<h2>COPYRIGHT AND LICENSE</h2>
<p> Copyright 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2014 The Board of Trustees of the Leland Stanford Junior University </p>
<p> Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved. This file is offered as-is, without any warranty.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-kinit/">kinit</a></i>(1), <i><a href="/docs/linux/man/8-remctld/">remctld</a></i>(8) </p>
<p> The current version of this program is available from its web page at &lt;<a rel="nofollow" href="http://www.eyrie.org/~eagle/software/remctl/">http://www.eyrie.org/~eagle/software/remctl/</a>&gt;. </p>
<h2>Index</h2>
