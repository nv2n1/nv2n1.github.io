---
title: "ettercap_plugins(8)"
name: "ettercap_plugins"
section: "8"
letter: "e"
url: "/docs/linux/man/8-ettercap_plugins/"
description: "ettercap-plugins NG-0.7.3 – A collection of plugins for ettercap"
---

<p><code>ettercap-plugins NG-0.7.3 &#8211; A collection of plugins for ettercap</code> </p>
<h2>Description</h2>
<p><a href="/docs/linux/man/8-ettercap/">Ettercap</a>(8) supports loadable modules at runtime. They are called plugins and they come within the source tarball. They are automatically compiled if your system supports them or until you specify the &#8211;disable-plugins option to the configure script.<br />
 Some of older ettercap plugins (roper, banshee, and so on) have not been ported in the new version. By the way, you can achieve the same results by using new filtering engine.<br />
 If you use interactive mode, most plugins need to &quot;Start Sniff&quot; before using them.</p>
<dl>
<dt>To have a list of plugins installed in your system do that command:</p>
<dd><i>ettercap -P list</i>  The following is a list of available plugins:</p>
<dl>
<dt><code>arp_cop</code></p>
<dd>It reports suspicious ARP activity by passively monitoring ARP requests/replies. It can report ARP posioning attempts, or simple IP-conflicts or IP-changes. If you build the initial host list the plugin will run more accurately. <i>example :</i> ettercap -TQP arp_cop //</p>
<dt><code>autoadd</code></p>
<dd>It will automatically add new victims to the ARP poisoning mitm attack when they come up. It looks for ARP requests on the lan and when detected it will add the host to the victims list if it was specified in the TARGET. The host is added when an arp request is seen form it, since communicating hosts are alive :)</p>
<dt><code>chk_poison</code></p>
<dd>It performs a check to see if the arp poisoning module of ettercap was successful. It sends spoofed ICMP echo packets to all the victims of the poisoning pretending to be each of the other targets. If we can catch an ICMP reply with our MAC address as destination it means that the poisoning between those two targets is successful. It checks both ways of each communication. This plugin makes sense only where poisoning makes sense. The test fails if you specify only one target in silent mode. You can&#8217;t run this plugin from command line because the poisoning process is not started yet. You have to launch it from the proper menu.</p>
<dt><code>dns_spoof</code></p>
<dd>This plugin intercepts DNS query and reply with a spoofed answer. You can chose to which address the plugin has to reply by modifying the etter.dns file. The plugin intercepts A, PTR and MX request. If it was an A request, the name is searched in the file and the ip address is returned (you can use wildcards in the name). If if was a PTR request, the ip is searched in the file and the name is returned (except for those name containing a wildcard). In case of MX request a special reply is crafted. The host is resolved with a fake host &#8216;mail.host&#8217; and the additional record contains the ip address of &#8216;mail.host&#8217;. The first address or name that matches is returned, so be careful with the order.</p>
<dt><code>dos_attack</code></p>
<dd>This plugin runs a d.o.s. attack against a victim IP address. It first &quot;scans&quot; the victim to find open ports, then starts to flood these ports with SYN packets, using a &quot;phantom&quot; address as source IP. Then it uses fake ARP replies to intercept packets for the phantom host. When it receives SYN-ACK from the victim, it replies with an ACK packet creating an ESTABLISHED connection. You have to use a free IP address in your subnet to create the &quot;phantom&quot; host (you can use find_ip for this purpose). You can&#8217;t run this plugin in unoffensive mode.<br />
 This plugin is based on the original Naptha DoS attack (<a rel="nofollow" href="http://razor.bindview.com/publish/advisories/adv_NAPTHA.html)">http://razor.bindview.com/publish/advisories/adv_NAPTHA.html)</a> <i>example :</i> ettercap -TQP dos_attack</p>
<dt><code>dummy</code></p>
<dd>Only a template to demonstrate how to write a plugin.</p>
<dt><code>find_conn</code></p>
<dd>Very simple plugin that listens for ARP requests to show you all the targets an host wants to talk to. It can also help you finding addresses in an unknown LAN. <i>example :</i> ettercap -TQzP find_conn ettercap -TQu -i eth0 -P find_conn</p>
<dt><code>find_ettercap</code></p>
<dd>Try to identify ettercap packets sent on the LAN. It could be useful to detect if someone is using ettercap. Do not rely on it 100% since the tests are only on particular sequence/identification numbers.</p>
<dt><code>find_ip</code></p>
<dd>Find the first unused IP address in the range specified by the user in the target list. Some other plugins (such as gre_relay) need an unused IP address of the LAN to create a &quot;fake&quot; host. It can also be useful to obtain an IP address in an unknown LAN where there is no dhcp server. You can use find_conn to determine the IP addressing of the LAN, and then find_ip. You have to build host list to use this plugin so you can&#8217;t use it in unoffensive mode. If you don&#8217;t have an IP address for your interface, give it a bogus one (e.g. if the LAN is 192.168.0.0/24, use 10.0.0.1 to avoid conflicting IP), then launch this plugin specifying the subnet range. You can run it either from the command line or from the proper menu. <i>example :</i> ettercap -TQP find_ip // ettercap -TQP find_ip /192.168.0.1-254/</p>
<dt><code>finger</code></p>
<dd>Uses the passive fingerprint capabilities to fingerprint a remote host. It does a connect() to the remote host to force the kernel to reply to the SYN with a SYN+ACK packet. The reply will be collected and the fingerprint is displayed. The connect() obey to the connect_timeout parameter in <a href="/docs/linux/man/5-etter-conf/">etter.conf</a>(5). You can specify a target on command-line or let the plugin ask the target host to be fingerprinted. You can also specify multiple target with the usual multi-target specification (see <a href="/docs/linux/man/8-ettercap/">ettercap</a>(8)). if you specify multiple ports, all the ports will be tested on all the IPs. <i>example :</i> ettercap -TzP finger /192.168.0.1/22<br />
 ettercap -TzP finger /192.168.0.1-50/22,23,25</p>
<dt><code>finger_submit</code></p>
<dd>Use this plugin to submit a fingerprint to the ettercap website. If you found an unknown fingerprint, but you know for sure the operating system of the target, you can submit it so it will be inserted in the database in the next ettercap release. We need your help to increase the passive fingerprint database. Thank you very much. <i>example :</i> ettercap -TzP finger_submit</p>
<dt><code>gre_relay</code></p>
<dd>This plugin can be used to sniff GRE-redirected remote traffic. The basic idea is to create a GRE tunnel that sends all the traffic on a router interface to the ettercap machine. The plugin will send back the GRE packets to the router, after ettercap &quot;manipulation&quot; (you can use &quot;active&quot; plugins such as smb_down, ssh decryption, filters, etc&#8230; on redirected traffic) It needs a &quot;fake&quot; host where the traffic has to be redirected to (to avoid kernel&#8217;s responses). The &quot;fake&quot; IP will be the tunnel endpoint. Gre_relay plugin will impersonate the &quot;fake&quot; host. To find an unused IP address for the &quot;fake&quot; host you can use find_ip plugin. Based on the original Tunnelx technique by Anthony C. Zboralski published in <a rel="nofollow" href="http://www.phrack.org/show.php?p=56">http://www.phrack.org/show.php?p=56</a>&amp;a=10 by HERT.</p>
<dt><code>gw_discover</code></p>
<dd>This plugin try to discover the gateway of the lan by sending TCP SYN packets to a remote host. The packet has the destination IP of a remote host and the destination mac address of a local host. If ettercap receives the SYN+ACK packet, the host which own the source mac address of the reply is the gatway. This operation is repeated for each host in the &#8216;host list&#8217;, so you need to have a valid host list before launching this plugin. <i>example :</i> ettercap -TP gw_discover /192.168.0.1-50/</p>
<dt><code>isolate</code></p>
<dd>The isolate plugin will isolate an host form the LAN. It will poison the victim&#8217;s arp cache with its own mac address associated with all the host it tries to contact. This way the host will not be able to contact other hosts because the packet will never reach the wire.<br />
 You can specify all the host or only a group. the targets specification work this way: the target1 is the victim and must be a single host, the target2 can be a range of addresses and represent the hosts that will be blocked to the victim. <i>examples :</i> ettercap -TzqP isolate /192.168.0.1/ //<br />
 ettercap -TP isolate /192.168.0.1/ /192.168.0.2-30/</p>
<dt><code>link_type</code></p>
<dd>It performs a check of the link type (hub or switch) by sending a spoofed ARP request and listening for replies. It needs at least one entry in the host list to perform the check. With two or more hosts the test will be more accurate. <i>example :</i> ettercap -TQP link_type /192.168.0.1/<br />
 ettercap -TQP link_type //</p>
<dt><code>pptp_chapms1</code></p>
<dd>It forces the pptp tunnel to negotiate MS-CHAPv1 authentication instead of MS-CHAPv2, that is usually easier to crack (for example with LC4). You have to be in the &quot;middle&quot; of the connection to use it successfully. It hooks the ppp dissector, so you have to keep them active.</p>
<dt><code>pptp_clear</code></p>
<dd>Forces no compression/encryption for pptp tunnels during negotiation. It could fail if client (or the server) is configured to hang off the tunnel if no encryption is negotiated. You have to be in the &quot;middle&quot; of the connection to use it successfully. It hooks the ppp dissector, so you have to keep them active.</p>
<dt><code>pptp_pap</code></p>
<dd>It forces the pptp tunnel to negotiate PAP (cleartext) authentication. It could fail if PAP is not supported, if pap_secret file is missing, or in case windows is configured with &quot;authomatic use of domain account&quot;. (It could fail for many other reasons too). You have to be in the &quot;middle&quot; of the connection to use it successfully. It hooks the ppp dissector, so you have to keep them active.</p>
<dt><code>pptp_reneg</code></p>
<dd>Forces re-negotiation on an existing pptp tunnel. You can force re-negotiation for grabbing passwords already sent. Furthermore you can launch it to use pptp_pap, pptp_chapms1 or pptp_clear on existing tunnels (those plugins work only during negotiation phase). You have to be in the &quot;middle&quot; of the connection to use it successfully. It hooks the ppp dissector, so you have to keep them active.</p>
<dt><code>rand_flood</code></p>
<dd>Floods the LAN with random MAC addresses. Some switches will fail open in repeating mode, facilitating sniffing. The delay between each packet is based on the port_steal_send_delay value in etter.conf.<br />
 It is useful only on ethernet switches. <i>example :</i> ettercap -TP rand_flood</p>
<dt><code>remote_browser</code></p>
<dd>It sends to the browser the URLs sniffed thru HTTP sessions. So you are able to see the webpages in real time. The command executed is configurable in the <a href="/docs/linux/man/5-etter-conf/">etter.conf</a>(5) file. It sends to the browser only the GET requests and only for webpages, ignoring single request to images or other amenities. Don&#8217;t use it to view your own connection :)</p>
<dt><code>reply_arp</code></p>
<dd>Simple arp responder. When it intercepts an arp request for a host in the targets&#8217; lists, it replies with attacker&#8217;s MAC address. <i>example :</i> ettercap -TQzP reply_arp /192.168.0.1/<br />
 ettercap -TQzP reply_arp //</p>
<dt><code>repoison_arp</code></p>
<dd>It solicits poisoning packets after broadcast ARP requests (or replies) from a posioned host. For example: we are poisoning Group1 impersonating Host2. If Host2 makes a broadcast ARP request for Host3, it is possible that Group1 caches the right MAC address for Host2 contained in the ARP packet. This plugin re-poisons Group1 cache immediately after a legal broadcast ARP request (or reply).<br />
 This plugin is effective only during an arp-posioning session.<br />
 In conjuction with reply_arp plugin, repoison_arp is a good support for standard arp-poisoning mitm method. <i>example :</i> ettercap -T -M arp:remote -P repoison_arp /192.168.0.10-20/ /192.168.0.1/</p>
<dt><code>scan_poisoner</code></p>
<dd>Check if someone is poisoning between some host in the list and us. First of all it checks if two hosts in the list have the same mac address. It could mean that one of those is poisoning us pretending to be the other. It could generate many false-positives in a proxy-arp environment. You have to build hosts list to perform this check. After that, it sends icmp echo packets to each host in the list and checks if the source mac address of the reply differs from the address we have stored in the list for that ip. It could mean that someone is poisoning that host pretending to have our ip address and forwards intercepted packets to us. You can&#8217;t perform this active test in unoffensive mode. <i>example :</i> ettercap -TQP scan_poisoner //</p>
<dt><code>search_promisc</code></p>
<dd>It tries to find if anyone is sniffing in promisc mode. It sends two different kinds of malformed arp request to each target in the host list and waits for replies. If a reply arrives from the target host, it&#8217;s more or less probable that this target has the NIC in promisc mode. It could generate false-positives. You can launch it either from the command line or from the plugin menu. Since it listens for arp replies it is better that you don&#8217;t use it while sending arp request. <i>example :</i> ettercap -TQP search_promisc /192.168.0.1/<br />
 ettercap -TQP search_promisc //</p>
<dt><code>smb_clear</code></p>
<dd>It forces the client to send smb password in clear-text by mangling protocol negotiation. You have to be in the &quot;middle&quot; of the connection to successfully use it. It hooks the smb dissector, so you have to keep it active. If you use it against a windows client it will probably result in a failure. Try it against a *nix smbclient :) </p>
<dt><code>smb_down</code></p>
<dd>It forces the client to not to use NTLM2 password exchange during smb authentication. This way, obtained hashes can be easily cracked by LC4. You have to be in the &quot;middle&quot; of the connection to successfully use it. It hooks the smb dissector, so you have to keep it active.</p>
<dt><code>stp_mangler</code></p>
<dd>It sends spanning tree BPDUs pretending to be a switch with the highest priority. Once in the &quot;root&quot; of the spanning tree, ettercap can receive all the &quot;unmanaged&quot; network traffic.<br />
 It is useful only against a group of switches running STP.<br />
 If there is another switch with the highest priority, try to manually decrease your MAC address before running it. <i>example :</i> ettercap -TP stp_mangler </p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-ettercap/">ettercap</a>(8)</i> <i><a href="/docs/linux/man/8-ettercap_curses/">ettercap_curses</a>(8)</i> <i><a href="/docs/linux/man/8-etterlog/">etterlog</a>(8)</i> <i><a href="/docs/linux/man/8-etterfilter/">etterfilter</a>(8)</i> <i><a href="/docs/linux/man/5-etter-conf/">etter.conf</a>(5)</i> </p>
