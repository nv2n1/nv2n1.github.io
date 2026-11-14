---
title: "xhost(1)"
name: "xhost"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xhost/"
description: "xhost – server access control program for X"
---

<h2 class="name">NAME</h2>
<p> xhost &#8211; server access control program for X </p>
<h2>SYNOPSIS</h2>
<p> <code>xhost</code> [[+-]name &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The <i>xhost</i> program is used to add and delete host names or user names to the list allowed to make connections to the X server. In the case of hosts, this provides a rudimentary form of privacy control and security. It is only sufficient for a workstation (single user) environment, although it does limit the worst abuses. Environments which require more sophisticated measures should implement the user-based mechanism or use the hooks in the protocol for passing other authentication data to the server.</p>
<h2>OPTIONS</h2>
<p> <i>Xhost</i> accepts the following command line options described below. For security, the options that affect access control may only be run from the &quot;controlling host&quot;. For workstations, this is the same machine as the server. For X terminals, it is the login host.</p>
<dl>
<dt><code>-help</code></p>
<dd> Prints a usage message.</p>
<dt><code>[+]</code><i>name</i></p>
<dd> The given <i>name</i> (the plus sign is optional) is added to the list allowed to connect to the X server. The name can be a host name or a complete name (See <font SIZE="-1"><code>NAMES</code> </font> for more details).</p>
<dt><code>&#8211;</code><i>name</i></p>
<dd> The given <i>name</i> is removed from the list of allowed to connect to the server. The name can be a host name or a complete name (See <font SIZE="-1"><code>NAMES</code> </font> for more details). Existing connections are not broken, but new connection attempts will be denied. Note that the current machine is allowed to be removed; however, further connections (including attempts to add it back) will not be permitted. Resetting the server (thereby breaking all connections) is the only way to allow local connections again.</p>
<dt><code>+</code></p>
<dd> Access is granted to everyone, even if they aren&#8217;t on the list (i.e., access control is turned off).</p>
<dt><code>&#8211;</code></p>
<dd> Access is restricted to only those on the list (i.e., access control is turned on).</p>
<dt><i>nothing</i></p>
<dd> If no command line arguments are given, a message indicating whether or not access control is currently enabled is printed, followed by the list of those allowed to connect. This is the only option that may be used from machines other than the controlling host.</dl>
<h2>NAMES</h2>
<p> A complete name has the syntax &#8220;family:name&#8221; where the families are as follows: </p>
<pre>
inet      Internet host (IPv4)
inet6     Internet host (IPv6)
dnet      DECnet host
nis       Secure RPC network name
krb       Kerberos V5 principal
local     contains only one name, the empty string
si        Server Interpreted
</pre>
<p> The family is case insensitive. The format of the name varies with the family. </p>
<p> When Secure RPC is being used, the network independent netname (e.g., &quot;nis:unix.<i>uid</i>@<i>domainname</i>&quot;) can be specified, or a local user can be specified with just the username and a trailing at-sign (e.g., &quot;nis:pat@&quot;). </p>
<p> For backward compatibility with pre-R6 <i>xhost</i>, names that contain an at-sign (@) are assumed to be in the nis family. Otherwise they are assumed to be Internet addresses. If compiled to support IPv6, then all IPv4 and IPv6 addresses returned by <a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a>(3) are added to the access list in the appropriate inet or inet6 family. </p>
<p> The local family specifies all the local connections at once. However, the server interpreted address &quot;si:localuser:<i>username</i>&quot; can be used to specify a single local user. (See the <i><a href="/docs/linux/man/7-xsecurity/">Xsecurity</a></i>(7) manual page for more details.) </p>
<p> Server interpreted addresses consist of a case-sensitive type tag and a string representing a given value, separated by a colon. For example, &quot;si:hostname:almas&quot; is a server interpreted address of type <i>hostname</i>, with a value of <i>almas</i>. For more information on the available forms of server interpreted addresses, see the <i><a href="/docs/linux/man/7-xsecurity/">Xsecurity</a></i>(7) manual page. </p>
<p> The initial access control list for display number <code>n</code> may be set by the file <i>/etc/X</i><code>n</code><i>.hosts</i>, where <code>n</code> is the display number of the server. See <i><a href="/docs/linux/man/1-xserver/">Xserver</a></i>(1) for details.</p>
<h2>DIAGNOSTICS</h2>
<p> For each name added to the access control list, a line of the form &quot;<i>name</i> being added to access control list&quot; is printed. For each name removed from the access control list, a line of the form &quot;<i>name</i> being removed from access control list&quot; is printed.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/7-xsecurity/">Xsecurity</a>(7), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/1-xdm/">xdm</a>(1), <a href="/docs/linux/man/1-xauth/">xauth</a>(1), <a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a>(3)</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></p>
<dd> to get the default host and display to use.</dl>
<h2>BUGS</h2>
<p> You can&#8217;t specify a display on the command line because <code>-display</code> is a valid command line argument (indicating that you want to remove the machine named <i>&#8220;display&#8221;</i> from the access list). </p>
<p> The X server stores network addresses, not host names, unless you use the server-interpreted hostname type address. If somehow you change a host&#8217;s network address while the server is still running, and you are using a network-address based form of authentication, <i>xhost</i> must be used to add the new address and/or remove the old address.</p>
<h2>AUTHORS</h2>
<p> Bob Scheifler, MIT Laboratory for Computer Science,<br />
 Jim Gettys, MIT Project Athena (DEC). </p>
<h2>Index</h2>
