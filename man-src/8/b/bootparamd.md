---
title: "bootparamd(8)"
name: "bootparamd"
section: "8"
letter: "b"
url: "/docs/linux/man/8-bootparamd/"
description: "bootparamd – boot parameter server"
---

<p>bootparamd &#8211; boot parameter server</p>
<h2>Synopsis</h2>
<p><code>rpc.bootparamd </code> [ <code>-d</code> ] [ <code>-s</code> ] [ <code>-r</code> <i>router</i> ] [ <code>-f</code> <i>file</i> ] [ <code>-l</code> ]</p>
<h2>Description</h2>
<p><i>bootparamd</i> is a server process that provides information to diskless clients necessary for booting. It consults the <code>/etc/bootparams</code> file to find the information it needs. This version will allow the use of aliases on the hostname in the <code>/etc/bootparams</code> file. The returned hostname to the whoami request done by the booting client will be the name that appears in <code>/etc/bootparams</code> and not the canonical name. In this way you can keep the answer short enough so that machines that cannot handle long hostnames won&#8217;t fail during boot. If the machine running this server is not a router and user doesn&#8217;t specify the <code>-r</code> option, bootparamd will try to find one. Server will make the following attempts to find a router for the client:</p>
<dl>
<dd>1) Find a router by sending ICMP_ECHO to ALL_ROUTERS.</dl>
<dl>
<dd>2) Return our own interface address if we&#8217;re a router.</dl>
<dl>
<dd>3) See if our default route can be used by the client.</dl>
<h2>Options</h2>
<dl>
<dt>
<dt><code>-d</code></p>
<dd>
<dd>Display debugging information.</p>
<dt><code>-s</code></p>
<dd>Log the debugging information to syslog.</p>
<dt><code>-r </code><i>router</i></p>
<dd>The default router (a machine or an IP-address). If you use this option, bootparamd won&#8217;t look for any other routers.</p>
<dt><code>-f </code><i>file</i></p>
<dd>The file to use as boot parameter file instead of /etc/bootparams.</p>
<dt><code>-l</code></p>
<dd>Turn off DNS lookup during host search.</dl>
<h2>Files</h2>
<p><code>/etc/bootparams</code></p>
<h2>Bugs</h2>
<p>You may find the syslog loggings too verbose.</p>
<h2>Author</h2>
<p>Written by Klas Heggemann &lt;klas [at] nada.kth.se&gt;</p>
