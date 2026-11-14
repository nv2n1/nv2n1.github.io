---
title: "tcpdmatch(8)"
name: "tcpdmatch"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tcpdmatch/"
---

tcpdmatch - tcp wrapper oracle

<h2>Synopsys</h2>

tcpdmatch [-d] daemon client 

 tcpdmatch [-d] daemon[@server] [user@]client

<h2>Description</h2>

<i>tcpdmatch</i> predicts how the tcp wrapper would handle a specific request for service. Examples are given below. 

 The program examines the <i>tcpd</i> access control tables (default <i>/etc/hosts.allow</i> and <i>/etc/hosts.deny</i>) and prints its conclusion. For maximal accuracy, it extracts additional information from your <i>inetd</i> or <i>tlid</i> network configuration file. 

 When <i>tcpdmatch</i> finds a match in the access control tables, it identifies the matched rule. In addition, it displays the optional shell commands or options in a pretty-printed format; this makes it easier for you to spot any discrepancies between what you want and what the program understands.

<h2>Arguments</h2>

The following two arguments are always required:
<dl><dt>daemon
<dd>A daemon process name. Typically, the last component of a daemon executable pathname.
<dt>client
<dd>A host name or network address, or one of the `unknown' or `paranoid' wildcard patterns. 

 When a client host name is specified, <i>tcpdmatch</i> gives a prediction for each address listed for that client. 

 When a client address is specified, <i>tcpdmatch</i> predicts what <i>tcpd</i> would do when client name lookup fails.</dl>
 

 Optional information specified with the <i>daemon [at] server</i> form:
<dl><dt>server
<dd>A host name or network address, or one of the `unknown' or `paranoid' wildcard patterns. The default server name is `unknown'.</dl>
 

 Optional information specified with the <i>user [at] client</i> form:
<dl><dt>user
<dd>A client user identifier. Typically, a login name or a numeric userid. The default user name is `unknown'.</dl>

<h2>Options</h2>

<dl><dt>-d
<dd>Examine <i>hosts.allow</i> and <i>hosts.deny</i> files in the current directory instead of the default ones.</dl>

<h2>Examples</h2>

To predict how <i>tcpd</i> would handle a telnet request from the local system: 

 
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> tcpdmatch in.telnetd localhost 

 The same request, pretending that hostname lookup failed: 

 
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> tcpdmatch in.telnetd 127.0.0.1 

 To predict what tcpd would do when the client name does not match the client address: 

 
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> tcpdmatch in.telnetd paranoid 

 On some systems, daemon names have no `in.' prefix, or <i>tcpdmatch</i> may need some help to locate the inetd configuration file.

<h2>Files</h2>

The default locations of the <i>tcpd</i> access control tables are: 

 /etc/hosts.allow 
 /etc/hosts.deny

<h2>See Also</h2>

<pre><a HREF="//www.systutorials.com/docs/linux/man/5-hosts_access/">hosts_access</a>(5), format of the tcpd access control tables.
<a HREF="//www.systutorials.com/docs/linux/man/5-hosts_options/">hosts_options</a>(5), format of the language extensions.</pre>

<h2>Authors</h2>

<pre>Wietse Venema (wietse [at] wzv.win.tue.nl),
Department of Mathematics and Computing Science,
Eindhoven University of Technology
Den Dolech 2, P.O. Box 513, 
5600 MB Eindhoven, The Netherlands</pre>
