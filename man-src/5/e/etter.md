---
title: "etter(5)"
name: "etter"
section: "5"
letter: "e"
url: "/docs/linux/man/5-etter/"
description: "etter.conf – Ettercap configuration file"
---

<p><code>etter.conf </code> &#8211; Ettercap configuration file </p>
<h2>Description</h2>
<p><code>etter.conf</code> is the configuration file that determines ettercap behaviour. It is always loaded at startup and it configures some attributes used at runtime. The file contains entries of the form:</p>
<dl>
<dd>
<pre><code>[section]
entry = value
</code><i>...</i></pre>
</dl>
<p> Each entry defines a variable that can be customized. Every value MUST be an integer. Sections are used only to group together some variables. <code>NOTE: </code> if you omit a variable in the conf file, it will be initialized with the value 0. It is strongly discouraged to not initialize critical variables such as &quot;arp_poison_delay&quot; or &quot;connection_timeout&quot;. The following is a list of available variables:</p>
<dl>
<dt><code>[privs]</code></p>
<dd>
<dt><code>ec_uid</code></p>
<dd>This variable specifies the UID to which privileges are dropped at startup. After the socket at link layer has been opened the privileges are dropped to a specific uid different from root for security reasons. etter.conf is the only file that is read with root privs. Be sure that the specified uid has enough privs to read other files (etter.*) You can bypass this variable by setting the environment variable EC_UID.</p>
<dt><code>[mitm]</code></p>
<dd>
<dt><code>arp_storm_delay</code></p>
<dd>The value represents the milliseconds to wait between two consecutive packets during the initial ARP scan. You can increment this value to be less aggressive at startup. The randomized scan plus a high delay can fool some types of ARP scan detectors.</p>
<dt><code>arp_poison_warm_up</code></p>
<dd>When the poisoning process starts, the inter-packet delay is low for the first 5 poisons (to be sure the poisoning process has been successful). After the first 5 poisons, the delay is incremented (to keep up the poisoning). This variable controls the delay for the first 5 poisons. The value is in seconds.<br />
 The same delay is used when the victims are restored to the original associations (RE-ARPing) when ettercap is closed.</p>
<dt><code>arp_poison_delay</code></p>
<dd>This variable controls the poisoning delay after the first 5 poisons. The value is expressed in seconds. You can increase this value (to try to fool the IDS) up to the timeout of the ARP cache (which depends on the poisoned operating system).</p>
<dt><code>arp_poison_icmp</code></p>
<dd>Enable the sending of a spoofed ICMP message to force the targets to make an arp request. This will create an arp entry in the host cache, so ettercap will be able to win the race condition and poison the target. Useful against targets that don&#8217;t accept gratuitous arp if the entry is not in the cache.</p>
<dt><code>arp_poison_reply</code></p>
<dd>Use ARP replies to poison the targets. This is the classic attack.</p>
<dt><code>arp_poison_request</code></p>
<dd>Use ARP request to poison the targets. Useful against targets that cache even arp request values.</p>
<dt><code>arp_poison_equal_mac</code></p>
<dd>Set this option to 0 if you want to skip the poisoning of two hosts with the same mac address. This may happen if a NIC has one or more aliases on the same network.</p>
<dt><code>dhcp_lease_time</code></p>
<dd>This is the lease time (in seconds) for a dhcp assignment. You can lower this value to permit the victims to receive a correct dhcp reply after you have stopped your attack. Using higher timeouts can seriously mess up your network after the attack has finished. On the other hand some clients will prefer a higher lease time, so you have to increase it to win the race condition against the real server.</p>
<dt><code>port_steal_delay</code></p>
<dd>This is the delay time (in milliseconds) between stealing packets for the &quot;port&quot; mitm method. With low delays you will be able to intercept more packets, but you will generate more traffic. You have to tune this value in order to find a good balance between the number of intercepted packets, re-transmitted packets and lost packets. This value depends on full/half duplex channels, network drivers and adapters, network general configuration and hardware.</p>
<dt><code>port_steal_send_delay</code></p>
<dd>This is the delay time (in microseconds) between packets when the &quot;port&quot; mitm method has to re-send packets queues. As said for port_steal_delay you have to tune this option to the lowest acceptable value.</p>
<dt><code>[connections]</code></p>
<dd>
<dt><code>connection_timeout</code></p>
<dd>Every time a new connection is discovered, ettercap allocates the needed structures. After a customizable timeout, you can free these structures to keep the memory usage low. This variable represents this timeout. The value is expressed in seconds. This timeout is applied even to the session tracking system (the protocol state machine for dissectors).</p>
<dt><code>connection_idle</code></p>
<dd>The number of seconds to wait before a connection is marked as IDLE.</p>
<dt><code>connection_buffer</code></p>
<dd>This variable controls the size of the buffer linked to each connection. Every sniffed packet is added to the buffer and when the buffer is full the older packets are deleted to make room for newer ones. This buffer is useful to view data that went on the cable before you select and view a specific connection. The higher this value, the higher the ettercap memory occupation. By the way, the buffer is dynamic, so if you set a buffer of 100.000 byte it is not allocated all together at the first packet of a connection, but it is filled as packets arrive.</p>
<dt><code>connect_timeout</code></p>
<dd>The timeout in seconds when using the connect() syscall. Increase it if you get a &quot;Connection timeout&quot; error. This option has nothing to do with connections sniffed by ettercap. It is a timeout for the connections made by ettercap to other hosts (for example when fingerprinting remote host).</p>
<dt><code>[stats]</code></p>
<dd>
<dt><code>sampling_rate</code></p>
<dd>Ettercap keeps some statistics on the processing time of the bottom half (the sniffer) and top half (the protocol decoder). These statistics are made on the average processing time of sampling_rate packets. You can decrease this value to have a more accurate real-time picture of processing time or increase it to have a smoother picture. The total average will not change, but the worst value will be heavily influenced by this value.</p>
<dt><code>[misc]</code></p>
<dd>
<dt><code>close_on_eof</code></p>
<dd>When reading from a dump file and using console or daemon UI, this variable is used to determine what action has to be done on EOF. It is a boolean value. If set to 1 ettercap will close itself (useful in scripts). Otherwise the session will continue waiting for user input.</p>
<dt><code>store_profiles</code></p>
<dd>Ettercap collects in memory a profile for each host it detects. Users and passwords are collected there. If you want to run ettercap in background logging all the traffic, you may want to disable the collecting in memory to save system memory. Set this option to 0 (zero) to disable profiles collection. A value of 1 will enable collection for all the hosts, 2 will collect only local hosts and 3 only remote hosts (a host is considered remote if it does not belong to the netmask).</p>
<dt><code>aggressive_dissectors</code></p>
<dd>Some dissectors (such as SSH and HTTPS) need to modify the payload of the packets in order to collect passwords and perform a decryption attack. If you want to disable the &quot;dangerous&quot; dissectors all together, set this value to 0.</p>
<dt><code>skip_forwarded</code></p>
<dd>If you set this value to 0 you will sniff even packets forwarded by ettercap or by the kernel. It will generate packets duplicates in conjuction with arp mitm method (for example). It could be useful while running ettercap in unoffensive mode on a host with more than one network interface (waiting for the multiple-interface feature&#8230;)</p>
<dt><code>checksum_warning</code></p>
<dd>If you set the value to 0 the messages about incorrect checksums will not be displayed in the user messages windows (nor logged to a file with -m).<br />
 Note that this option won&#8217;t disable the check on the packets, but only prevent the message to be displayed (see below).</p>
<dt><code>checksum_check</code></p>
<dd>This option is used to completely disable the check on the checksum of the packets that ettercap receives. The check on the packets is performed to avoid ettercap spotting thru bad checsum packets (see Phrack 60.12). If you disable the check, you will be able to sniff even bad checksummed packet, but you will be spotted if someone is searching for you&#8230;</p>
<dt><code>[dissectors]</code></p>
<dd>
<dt><code>protocol_name</code></p>
<dd>This value represents the port on which the protocol dissector has to be bound. A value of 0 will disable the dissector. The name of the variable is the same of the protocol name. You can specify a non standard port for each dissector as well as multiple ports. The syntax for multiport selection is the following: port1,port2,port3,&#8230;<br />
 NOTE: some dissectors are conditionally compiled . This means that depending on the libraries found in your system some dissectors will be enabled and some others will not. By default etter.conf contains all supported dissectors. if you got a &quot;FATAL: Dissector &quot;xxx&quot; does not exists (etter.conf line yy)&quot; error, you have to comment out the yy line in etter.conf.</p>
<dt><code>[curses]</code></p>
<dd>
<dt><code>color</code></p>
<dd>You can customize the colors of the curses GUI.<br />
 Simply set a field to one of the following values and look at the GUI aspect :)<br />
 Here is a list of values: 0 Black, 1 Red, 2 Green, 3 Yellow, 4 Blue, 5 Magenta, 6 Cyan, 7 White</p>
<dt><code>[strings]</code></p>
<dd>
<dt><code>utf8_encoding</code></p>
<dd>specifies the encoding to be used while displaying the packets in UTF-8 format. Use the `iconv &#8211;list` command for a list of supported encodings.</p>
<dt><code>remote_broswer</code></p>
<dd>This command is executed by the remote_browser plugin each time it catches a good URL request into an HTTP connection. The command should be able to get 2 parameters:</p>
<dl>
<dd>
<dl>
<dt><code>%host</code></p>
<dd>the Host: tag in the HTTP header. Used to create the full request into the browser.</p>
<dt><code>%url</code></p>
<dd>The page requested inside the GET request.</dl>
</dl>
<dt><code>redir_command_on</code></p>
<dd>You have to provide a valid command (or script) to enable tcp redirection at kernel level in order to be able to use SSL dissection. Your script should be able to get 3 parameters:</p>
<dl>
<dd>
<dl>
<dt><code>%iface</code></p>
<dd>The network interface on which the rule must be set</p>
<dt><code>%port</code></p>
<dd>The source port of the packets to be redirected (443 for HTTPS, 993 for imaps, etc).</p>
<dt><code>%rport</code></p>
<dd>The internally bound port to which ettercap listens for connections.</dl>
</dl>
<p> NOTE: this script is executed with an execve(), so you can&#8217;t use pipes or output redirection as if you were in a shell. We suggest you to make a script if you need those commands.</p>
<dt><code>redir_command_off</code></p>
<dd>This script is used to remove the redirect rules applied by &#8216;redir_command_on&#8217;. You should note that this script is called atexit() and thus it has not high privileges. You should provide a setuid program or set ec_uid to 0 in order to be sure that the script is executed successfully. </p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-ettercap/">ettercap</a>(8)</i> <i><a href="/docs/linux/man/8-ettercap_curses/">ettercap_curses</a>(8)</i> <i><a href="/docs/linux/man/8-ettercap_plugins/">ettercap_plugins</a>(8)</i> <i><a href="/docs/linux/man/8-etterlog/">etterlog</a>(8)</i> <i><a href="/docs/linux/man/8-etterfilter/">etterfilter</a>(8)</i> </p>
