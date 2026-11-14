---
title: "ndiswrapper-1(8)"
name: "ndiswrapper-1"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ndiswrapper-1/"
description: "ndiswrapper – Linux kernel module and user space tool to load and run Windows XP drivers for wireless cards"
---

<p>ndiswrapper &#8211; Linux kernel module and user space tool to load and run Windows XP drivers for wireless cards</p>
<h2>Synopsis</h2>
<p><code>ndiswrapper</code></p>
<h2>Description</h2>
<p><code>ndiswrapper</code> is two parts: user space tool that is used to install Windows XP drivers and kernel module to load the Windows XP drivers. Both are called <code>ndiswrapper.</code> </p>
<h2>ndiswrapper &#8211; tool</h2>
<p>The user space tool (/usr/sbin/ndiswrapper) is used whenever a new Windows XP driver is to be installed. This program takes the following options: </p>
<p> <code>OPTIONS</code></p>
<dl>
<dt><code>-i &lt;inf file&gt;</code></p>
<dd>installs new Windows XP driver, where &lt;inf file&gt; is full path to INF file for that driver.</p>
<dt><code>-l</code></p>
<dd>lists the currently installed drivers.</p>
<dt><code>-e &lt;driver&gt;</code></p>
<dd>removes an installed Windows XP driver named &lt;driver&gt;.</p>
<dt><code>-m</code></p>
<dd>writes an alias for wlan0 (default wireless device) into module configuration file so that ndiswrapper kernel module is loaded automatically when this interface is used. </p>
</dl>
<h2>ndiswrapper &#8211; kernel module</h2>
<p>The kernel module loads the installed Windows drivers and executes them so that the wireless cards can be used in Linux. The module takes the following options: </p>
<p> <code>OPTIONS</code></p>
<dl>
<dt><code>if_name=&lt;basename&gt;</code></p>
<dd>The default basename for the interface is wlan%d, so that the wireless cards will be configured as wlan0, wlan1, &#8230; (%d is replaced with lowest available number). You may use any other basename or fixed name, such as eth%d, ndis2 etc.</p>
<dt><code>proc_uid=&lt;uid&gt;</code></p>
<dd>The module creates files in /proc/net/ndiswrapper that provide some useful information. These files are created so that they can be read only by root by default. If some other user needs to access these files without having to login as root, then replace &lt;uid&gt; with the user ID of that user.</p>
<dt><code>proc_gid=&lt;gid&gt;</code></p>
<dd>The module creates files in /proc/net/ndiswrapper that provide some useful information. These files are created so that they can be read only by people in root group by default. If users from other groups need to access these files, then replace &lt;gid&gt; with the group ID of those users. </p>
<p> ndiswrapper kernel module uses loadndisdriver user space tool to load all the Windows drivers. This tool is not to be used under normal circumstances. Only when ndiswrapper module is already loaded and a new Windows XP driver is installed (by ndiswrapper user space tool) and you want the kernel module to load that driver without having to unload the module that you need to use it.</dl>
<h2>Author</h2>
<p>This manual page was written by Giridhar Pemmasani &lt;ndiswrapper-general [at] lists.sourceforge.net&gt;, for the Debian project (but may be used by others).</p>
