---
title: "dibbler-server(8)"
name: "dibbler-server"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dibbler-server/"
description: "dibbler-server – a portable DHCPv6 server"
---

<p>dibbler-server &#8211; a portable DHCPv6 server</p>
<h2>Description</h2>
<p><code>dibbler-server</code> is a portable implementation of the DHCPv6 server. It supports both stateful (i.e. IPv6 address granting) and stateless (i.e. options granting) autoconfiguration. There are ports available for Linux 2.4/2.6 systems as well as MS Windows XP and 2003. They are freely available under <code>GNU GPL </code> version 2 (or later) license. </p>
<h2>Synopsis</h2>
<p><code>dibbler-server</code> [ run | start | stop | status | install | uninstall ] </p>
<h2>Options</h2>
<p><i>run</i> &#8211; starts server in the console. Server can be closed using ctrl-c. </p>
<p> <i>start </i> &#8211; starts server in daemon mode. </p>
<p> <i>stop</i> &#8211; stops running server. </p>
<p> <i>status</i> &#8211; shows status of the server. </p>
<p> <i>install</i> &#8211; installs server as a service. This is not implemented yet. </p>
<p> <i>uninstall</i> &#8211; uninstall server service. This is not implemented yet.</p>
<h2>Examples</h2>
<p>Let&#8217;s assume simple case: server should provide clients located on the eth1 link with IPv6 addresses from range 2000::100/120 and should have preference set to 7: </p>
<pre>iface eth0
{ 
 preference 7
 class
 {
 pool 2000::100-2000::1ff
 } 
}</pre>
<p>Here is exmaple of server configured to work in a stateless mode (i.e. only options, not addresses are served). If client support option renewal, it should do so once in a 500 seconds: </p>
<pre>log-level 7
log-mode short
stateless
iface eth0 {
 option dns-server 2000::100,2000::101
 option domain example.com, test1.example.com
 option ntp-server 2000::200,2000::201,2000::202
 option time-zone CET
 option sip-server 2000::300,2000::302,2000::303,2000::304
 option sip-domain sip1.example.com,sip2.example.com
 option nis-server 2000::400,2000::401,2000::404,2000::405,2000::405
 option nis-domain nis.example.com
 option nis+-server 2000::501,2000::502
 option nis+-domain nisplus.example.com
 option lifetime 500
}</pre>
<p>More examples can be found in the User&#8217;s Guide. </p>
<h2>Files</h2>
<p>All files are created in the /var/lib/dibbler directory. Dibbler server reads /var/lib/dibbler/server.conf file. During operation, Dibbler saves various file in that directory. Log file is named client.log.</p>
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
<p>There is <a href="/docs/linux/man/8-dibbler-client/">dibbler-client</a>(8) manual page. You are also advised to take a look at project website located at <i><a rel="nofollow" href="http://klub.com.pl/dhcpv6/">http://klub.com.pl/dhcpv6/</a></i>. As far as authors know, this is the only Windows DHCPv6 stateful implementation available. It is also one of two freely available under Linux. The other Linux implementation is available at <i><a rel="nofollow" href="http://dhcpv6.sourceforge.net">http://dhcpv6.sourceforge.net</a></i>, but it is rather outdated and seems not being actively developed. </p>
