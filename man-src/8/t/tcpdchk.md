---
title: "tcpdchk(8)"
name: "tcpdchk"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tcpdchk/"
---

tcpdchk - tcp wrapper configuration checker

<h2>Synopsis</h2>

tcpdchk [-a] [-d] [-i inet_conf] [-v]

<h2>Description</h2>

<i>tcpdchk</i> examines your tcp wrapper configuration and reports all potential and real problems it can find. The program examines the <i>tcpd</i> access control files (by default, these are <i>/etc/hosts.allow</i> and <i>/etc/hosts.deny</i>), and compares the entries in these files against entries in the <i>inetd</i> network configuration file. 

 <i>tcpdchk</i> reports problems such as non-existent pathnames; services that appear in <i>tcpd</i> access control rules, but are not controlled by <i>tcpd</i>; services that should not be wrapped; non-existent host names or non-internet address forms; occurrences of host aliases instead of official host names; hosts with a name/address conflict; inappropriate use of wildcard patterns; inappropriate use of NIS netgroups or references to non-existent NIS netgroups; references to non-existent options; invalid arguments to options; and so on. 

 Where possible, <i>tcpdchk</i> provides a helpful suggestion to fix the problem.

<h2>Options</h2>

<dl><dt>-a
<dd>Report access control rules that permit access without an explicit ALLOW keyword.
<dt>-d
<dd>Examine <i>hosts.allow</i> and <i>hosts.deny</i> files in the current directory instead of the default ones.
<dt>-i inet_conf
<dd>Specify this option when <i>tcpdchk</i> is unable to find your <i>inetd.conf</i> network configuration file, or when you suspect that the program uses the wrong one.
<dt>-v
<dd>Display the contents of each access control rule. Daemon lists, client lists, shell commands and options are shown in a pretty-printed format; this makes it easier for you to spot any discrepancies between what you want and what the program understands.</dl>

<h2>Files</h2>

The default locations of the <i>tcpd</i> access control tables are: 

 /etc/hosts.allow 
 /etc/hosts.deny

<h2>See Also</h2>

<pre><a HREF="//www.systutorials.com/docs/linux/man/8-tcpdmatch/">tcpdmatch</a>(8), explain what tcpd would do in specific cases.
<a HREF="//www.systutorials.com/docs/linux/man/5-hosts_access/">hosts_access</a>(5), format of the tcpd access control tables.
<a HREF="//www.systutorials.com/docs/linux/man/5-hosts_options/">hosts_options</a>(5), format of the language extensions.
<a HREF="//www.systutorials.com/docs/linux/man/5-inetd.conf/">inetd.conf</a>(5), format of the inetd control file.</pre>

<h2>Authors</h2>

<pre>Wietse Venema (wietse [at] wzv.win.tue.nl),
Department of Mathematics and Computing Science,
Eindhoven University of Technology
Den Dolech 2, P.O. Box 513, 
5600 MB Eindhoven, The Netherlands</pre>
