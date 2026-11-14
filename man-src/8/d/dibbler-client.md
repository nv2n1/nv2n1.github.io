---
title: "dibbler-client(8)"
name: "dibbler-client"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dibbler-client/"
description: "dibbler-client – a portable DHCPv6 client"
---

<p>dibbler-client &#8211; a portable DHCPv6 client</p>
<h2>Description</h2>
<p><code>dibbler-client</code> is a portable implementation of the DHCPv6 client. It supports both stateful (i.e. IPv6 address granting) and stateless (i.e. options granting) autoconfiguration. There are ports available for Linux 2.4/2.6 systems as well as MS Windows XP and 2003. They are freely available under <code>GNU GPL </code> version 2 (or later) license. </p>
<h2>Synopsis</h2>
<p><code>dibbler-client</code> [ run | start | stop | status | install | uninstall ] </p>
<h2>Options</h2>
<p><i>run</i> &#8211; starts client in the console. Client can be closed using ctrl-c. </p>
<p> <i>start </i> &#8211; starts client in daemon mode. </p>
<p> <i>stop</i> &#8211; stops running clients. </p>
<p> <i>status</i> &#8211; shows status of the client and server. </p>
<p> <i>install</i> &#8211; installs client as a service. This is not implemented yet. </p>
<p> <i>uninstall</i> &#8211; uninstall client service. This is not implemented yet.</p>
<h2>Examples</h2>
<p>Let&#8217;s start with simple configuration. We want receive one IPv6 address and there is only one Ethernet interface present. In that case client.conf file might be completly empty. Dibbler client will request for one IPv6 address on each up, running and multicast capable interface (except loopback). Now some real example. We want one IPv6 address and receive DNS servers and domain name. We are also not interested in the details, so debug mode is disabled. </p>
<pre>log-mode short
log-level 6
iface eth0
{
 ia { }
 option dns-server
 option domain
}</pre>
<p>Next example: we want only NIS domain and NIS server information. That information should be periodicaly renewed, so we use lifetime option. We don&#8217;t need any addresses so stateless mode is used. </p>
<pre>log-mode short
iface eth0
{
 stateless
 option nis-server
 option nis-domain
 option lifetime
}</pre>
<p>More examples can be found in the User&#8217;s Guide. </p>
<h2>Files</h2>
<p>All files are created in the /var/lib/dibbler directory. Dibbler client reads /var/lib/dibbler/client.conf file. During operation, Dibbler saves various file in that directory. After reception of the DNS servers or domain informations, they are added to the /etc/resolv.conf file. After shutdown, that information is removed from that file. Option values are stored in the option-* files. Log file is named client.log.</p>
<h2>Standards</h2>
<p>This implementation aims at conformance to the following standards: </p>
<p> <i>RFC 3315 </i> DHCP for IPv6 </p>
<p> <i>RFC 3319</i> SIP options for DHCPv6 </p>
<p> <i>RFC 3646</i> DNS server options for DHCPv6 </p>
<p> <i>RFC 3736</i> Stateless DHCPv6 </p>
<p> <i>RFC 3898</i> NIS options for DHCPv6 </p>
<p> Also options specified in following drafts are implemented: </p>
<p> <i>draft-ietf-dhc-dhcpv6-opt-timeconfig-03.txt</i> NTP and timezone options. </p>
<p> <i>draft-ietf-dhc-dhcpv6-opt-lifetime-00.txt</i> Option renewal.</p>
<h2>Bugs</h2>
<p>Bugs are tracked with bugzilla, available at <i><a rel="nofollow" href="http://klub.com.pl/bugzilla/">http://klub.com.pl/bugzilla/</a></i>. If you belive you have found a bug, don&#8217;t hesitate to report it. </p>
<h2>Author</h2>
<p>Dibbler was developed as master thesis on the Technical University of Gdansk by Tomasz Mrugalski and Marek Senderski. Currently Marek has not enough free time, so this project is being developed by Tomasz Mrugalski. Authors can be reached at thomson [at] klub.com.pl and msend [at] o2.pl</p>
<h2>See Also</h2>
<p>There is <a href="/docs/linux/man/8-dibbler-server/">dibbler-server</a>(8) manual page. You are also advised to take a look at project website located at <i><a rel="nofollow" href="http://klub.com.pl/dhcpv6/">http://klub.com.pl/dhcpv6/</a></i>. As far as authors know, this is the only Windows DHCPv6 stateful implementation available. It is also one of two freely available under Linux. The other Linux implementation is available at <i><a rel="nofollow" href="http://dhcpv6.sourceforge.net">http://dhcpv6.sourceforge.net</a></i>, but it is rather outdated and seems not being actively developed. </p>
