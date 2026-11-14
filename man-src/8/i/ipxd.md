---
title: "ipxd(8)"
name: "ipxd"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipxd/"
description: "ipxd – IPX RIP/SAP daemon program"
---

<p>ipxd &#8211; IPX RIP/SAP daemon program</p>
<h2>Synopsis</h2>
<p><code>ipxd</code> [ <code>-d</code> ] [ <code>-p</code> ] [ <code>-l </code> <i>log_file</i> ] [ <code>-t</code> <i>ticks_file</i> ] </p>
<h2>Description</h2>
<p>The IPX RIP/SAP daemon <code>ipxd</code> is invoked at boot time to manage the kernel IPX routing tables. When ipxd is started, it scans the file /proc/net/ipx_interfaces to find the ipx networks the computer is directly connected to. It sends the RIP and SAP response and request packets required by the IPX router specification v1.20 to the interfaces it found, so that an initial RIP and SAP table can be built. During normal operation, ipxd listens on the RIP and SAP ports of each directly connected interface for broadcasts that other routers on the network send out, as well as requests issued by workstations. This way the full router functionality required by the IPX router specification v1.20 is hopefully implemented. Every 30 seconds, as well as on request by a HUP signal, the file /proc/net/ipx_interfaces is re-scanned. Changes in the network topology are detected this way and broadcasted appropriately. This could eventually make Linux a quite flexible IPX router. </p>
<h2>Options</h2>
<p><code>-d</code></p>
<dl>
<dd>With option <code>-d,</code> ipxd does not daemonize itself and logs the IPX traffic it receives and sends out to the log file.</dl>
<p> <code>-p</code></p>
<dl>
<dd>With option <code>-p,</code> ipxd works in passive mode. This means it does not output any response on the net. It does not broadcast its internal tables, and does not answer requests. This makes it suitable for use in a normal IPX workstation, which should not act as a router. By starting ipxd in passive mode, the kernel routing tables are kept up to date. This means that utilities like slist or nprint do not have to run suid root, to be able to add IPX routing table entries. </p>
<p> It is not possible to use ipxd in passive mode when you have an internal net, because other IPX nodes must know how to reach the internal net. They can only know it if ipxd tells them where the internal net is.</dl>
<p> <code>-l</code> <i>logfile</i></p>
<dl>
<dd>With this option you can tell ipxd where to put its log output. The default is /dev/null.</dl>
<p> <code>-t</code> <i>ticks_file</i></p>
<dl>
<dd>With this option you can override the default file name for the ticks file. The default is /etc/ipx_ticks. See <a href="/docs/linux/man/5-ipx_ticks/">ipx_ticks</a>(5) for more information. </p>
</dl>
<h2>Files</h2>
<p>/etc/ipx_ticks</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-ipx_ticks/">ipx_ticks</a>(5), <a href="/docs/linux/man/8-ipx_interface/">ipx_interface</a>(8) </p>
<h2>Author</h2>
<p>Volker Lendecke &lt;lendecke [at] namu01.gwdg.de&gt;</p>
