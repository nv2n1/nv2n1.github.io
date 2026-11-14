---
title: "zeppelin(8)"
name: "zeppelin"
section: "8"
letter: "z"
url: "/docs/linux/man/8-zeppelin/"
description: "zeppelin – ATM LAN Emulation client demon (LED) Zeppelin"
---

<p>zeppelin &#8211; ATM LAN Emulation client demon (LED) Zeppelin</p>
<h2>Synopsis</h2>
<p><code>zeppelin</code> [<code>-b&nbsp;<wbr>]</code> [<code>-c&nbsp;<wbr></code><i>LECS_address</i>&nbsp;<wbr>| -s&nbsp;<wbr><i>LES_address</i>] [<code>-e&nbsp;<wbr></code><i>esi</i>] [<code>-n&nbsp;<wbr></code><i>VLAN_name</i>] [<code>-m&nbsp;<wbr></code><i>mesg_mask</i>] [<code>-l&nbsp;<wbr></code><i>listen_address |</i>&nbsp;<wbr>selector<code>]</code> [<code>-i&nbsp;<wbr></code><i>interface_number</i>] [<code>-I&nbsp;<wbr></code><i>physical_interface_number</i>] [<code>-t&nbsp;<wbr></code><i>1516|1580|4544|9234|18190</i>] [<code>-1&nbsp;<wbr>]</code> [<code>-2&nbsp;<wbr>]</code> [<code>-p&nbsp;<wbr>]</code> [<code>-F&nbsp;<wbr></code><i>logfile</i>] [<code>-f&nbsp;<wbr></code><i>Fore_specific_name</i>]</p>
<h2>Description</h2>
<p>A LAN Emulation Client is an entity in an ATM endstation that performs data forwarding, address resolution and other control functions. It uses the LUNI interface when communicating with other components in emulated LANs. It provides upper protocol layers a MAC like interface similar to IEEE 802.3/Ethernet or IEEE 802.5/Token Ring LAN. </p>
<p> LAN Emulation client code is divided into two parts: user space application LAN Emulation Demon called (LED) <code><a href="/docs/linux/man/8-zeppelin/">zeppelin</a>(8)</code>, and the kernel component. <code>Zeppelin</code> is responsible for control operations needed in LAN Emulation clienthood. It forms the necessary VCCs and receives all the LE control frames and acts accordingly. It also controls the operation of the LEC kernel component. </p>
<p> Linux LEC supports only Ethernet type of emulated LAN. </p>
<p> <code>SIGHUP</code> causes restart of the LEC. All resources are released and <code>zeppelin</code> is started.</p>
<h2>Options</h2>
<dl>
<dt><code>-b</code></p>
<dd>Run in background (i.e. in a forked child process) after initializing kernel interface.</p>
<dt><code>-c&nbsp;<wbr></code><i>LECS_address</i></p>
<dd>ATM address of <code><a href="/docs/linux/man/8-lecs/">lecs</a>(8)</code> (Lan Emulation Configuration Server), if not set, Well-Known server address is used.</p>
<dt><code>-s&nbsp;<wbr></code><i>LES_address</i></p>
<dd>ATM address of <code><a href="/docs/linux/man/8-les/">les</a>(8)</code> (Lan Emulation Server), can be used in bypassing configuration phase in joining emulated Lan i.e <code>lecs</code> address is not used.</p>
<dt><code>-e&nbsp;<wbr></code><i>esi</i></p>
<dd>Mac address to use when communicating in Emulated LAN. E.g. 00:20:22:23:04:05 .</p>
<dt><code>-n&nbsp;<wbr></code><i>VLAN_name</i></p>
<dd>Name of the virtual LAN to which joining is requested. This is used in LE_CONFIGURE_REQUEST to LECS or LE_JOIN_RESPONSE to LES, if configuration phase is bypassed.</p>
<dt><code>-m&nbsp;<wbr></code><i>mesg_mask</i></p>
<dd>Sometimes one wants to know more what is happening in LE daemon e.g. when nothing works. This is a hexadecimal long value setting global message mask. 0 = No messages, ffff = All messages.</p>
<dt><code>-l&nbsp;<wbr></code><i>listen_address | selector</i></p>
<dd>Local ATM address that zeppelin uses as local binding point in signalling. Use this if you are running more than one client or a set of LE servers. The local ATM address can be specified by either giving the full ATM address or the desired selector byte.</p>
<dt><code>-i&nbsp;<wbr></code><i>interface_number</i></p>
<dd>Linux LEC supports up to 40+8 network interfaces. The interface_number tells zeppelin to which of these to attach. Ethernet type network interfaces are numbered from &quot;lec0&quot; to &quot;lec39&quot; and Token Ring interfaces are from &quot;lec40&quot; to &quot;lec47&quot;. These parameters are tweakable during the kernel compile, see &lt;linux/atmlec.h&gt;.</p>
<dt><code>-I&nbsp;<wbr></code><i>physical_interface_number</i></p>
<dd>The physical interface this LANE client should bind to. If your host has multiple ATM network cards, you can use this option to choose which card this zeppelin will use.</p>
<dt><code>-t&nbsp;<wbr></code><i>MTU</i></p>
<dd>The MTU of ELAN to join. You need to also use <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a>(8)</code> to set the MTU of the LANE interface.</p>
<dt><code>-1</code></p>
<dd>Run as LANEv1 client. This is the default.</p>
<dt><code>-2</code></p>
<dd>Run as LANEv2 client. This is required by MPOA.</p>
<dt><code>-p</code></p>
<dd>Enable proxy. When started with this option, it is possible to bridge packets between ATM and Ethernet. That is, you can use LANE interfaces with normal bridging. See the Bridging mini-Howto for more info.</p>
<dt><code>-F&nbsp;<wbr></code><i>logfile</i></p>
<dd>Instead of writing debug messages to <code>stderr</code>, write the messages to the file <code>logfile</code>. Use <code>syslog</code> as the file name to use the <code><a href="/docs/linux/man/3-syslog/">syslog</a>(3)</code> facility.</p>
<dt><code>-f&nbsp;<wbr></code><i>Fore specific name</i></p>
<dd>The LANE servers on Fore ATM switches can display a special name if a client can supply one. This name shows with command &#8216;conf lane les show advanced&#8217;.</dl>
<h2>Token Ring Considerations</h2>
<p>A number of lec interfaces is reserved for Token Ring ELANs when the kernel is compiled with Token Ring (CONFIG_TR) support. See the discussion about interface_number command line option above. The Linux Token Ring LANE client does not support bridging between legacy Token Ring and ATM parts of the ELAN, so using the -p option is not recommended. Token Ring support has received less testing than its Ethernet counterpart.</p>
<h2>Files</h2>
<p><i>/var/run/lec[interface number].pid</i> The file containing the process id of zeppelin.</p>
<h2>Bugs</h2>
<p>John Bonham died 1980 and Led Zeppelin broke. </p>
<p> Please report any other bugs to Heikki Vatiainen &lt;hessu [at] cs.tut.fi&gt;</p>
<h2>Authors</h2>
<p>Marko Kiiskila, TUT &lt;carnil [at] cs.tut.fi&gt; and Heikki Vatiainen, TUT &lt;hessu [at] cs.tut.fi&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-lecs/">lecs</a>(8), <a href="/docs/linux/man/8-mpcd/">mpcd</a>(8), <a href="/docs/linux/man/8-atmsigd/">atmsigd</a>(8), <a href="/docs/linux/man/8-les/">les</a>(8), <a href="/docs/linux/man/7-qos/">qos</a>(7) </p>
