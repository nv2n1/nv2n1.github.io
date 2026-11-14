---
title: "bcm43xx-fwcutter(1)"
name: "bcm43xx-fwcutter"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bcm43xx-fwcutter/"
description: "bcm43xx-fwcutter – manual page for bcm43xx-fwcutter"
---

<h2>NAME</h2>
<p> bcm43xx-fwcutter &#8211; manual page for bcm43xx-fwcutter</p>
<h2>SYNOPSIS</h2>
<p> <code>bcm43xx-fwcutter</code> [<i>OPTION</i>] [<i>DRIVER</i>]</p>
<h2>DESCRIPTION</h2>
<p> Bcm43xx-fwcutter can extract the firmware for your Broadcom 43xx hardware from different closed source drivers. The bcm43xx driver depends on this firmware files and can&#8217;t work without them. </p>
<p> Currently bcm43xx-fwcutter supports Apple MacOS X, Microsoft Windows 98/ME/2000/XP and Linux drivers, but keep in mind that bcm43xx-fwcutter doesn&#8217;t support all driver versions. </p>
<p> Example:</p>
<dl>
<dt>
<dd> bcm43xx-fwcutter bcmwl5.sys</dl>
<p> to cut the firmware out of bcmwl5.sys</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-l</code>|&#8211;list</p>
<dd> List supported driver versions</p>
<dt><code>-i</code>|&#8211;identify</p>
<dd> Only identify the driver file (don&#8217;t extract)</p>
<dt><code>-w</code>|&#8211;target-dir DIR</p>
<dd> Extract and write firmware to DIR</p>
<dt><code>-a</code>|&#8211;alt-iv</p>
<dd> Extract alternative initvals (only 3.10.x.x)</p>
<dt><code>-p</code>|&#8211;postfix &quot;.FOO&quot;</p>
<dd> Postfix for firmware filenames (.FOO.fw)</p>
<dt><code>-v</code>|&#8211;version</p>
<dd> Print bcm43xx-fwcutter version</p>
<dt><code>-h</code>|&#8211;help</p>
<dd> Print help information</dl>
<h2>DRIVERS</h2>
<dl>
<dt><code>AppleAirPort2</code></p>
<dd> Apple MacOS 10.x driver file (ppc, x86)</p>
<dt><code>AppleAirPort3</code></p>
<dd> Apple MacOS 10.x driver file (ppc)</p>
<dt><code>AppleAirPortBrcm4311</code></p>
<dd> Apple MacOS 10.4 driver file (x86)</p>
<dt><code>bcmwl5.sys</code></p>
<dd> Microsoft Windows driver file, 32bit (x86)</p>
<dt><code>bcmwl564.sys</code></p>
<dd> Microsoft Windows driver file, 64bit (x86-64)</p>
<dt><code>bcmwl5a.sys</code></p>
<dd> Microsoft Windows driver file, 32bit (x86)</p>
<dt><code>mn720-50.sys</code></p>
<dd> This is a renamed bcmwl5.sys driver for Microsoft Wireless MN-720 Notebook Adapter and MN-730 PCI Adapter</p>
<dt><code>n54gnds.sys</code></p>
<dd> This is a renamed bcmwl5.sys driver for Planex GW-NS54G 54Mbps Wireless LAN Cards</p>
<dt><code>wmp11v27.sys</code></p>
<dd> This is a renamed bcmwl5.sys driver for Linksys WMP-11 802.11b PCI Cards</p>
<dt><code>wn511b.sys</code></p>
<dd> This is a renamed bcmwl5.sys driver for Netgear WN511B Cards</p>
<dt><code>ap_d11ucode.o</code></p>
<dd> Linux 2.4.x driver file (mips)</p>
<dt><code>apsta_d11ucode.o</code></p>
<dd> Linux 2.4.x driver file (mips)</p>
<dt><code>sta_d11ucode.o</code></p>
<dd> Linux 2.4.x driver file (mips)</p>
<dt><code>wl.o</code></p>
<dd> Linux 2.4.x driver file (mips)</p>
<dt><code>wl_ap.o</code></p>
<dd> Linux 2.4.x driver file (mips)</p>
<dt><code>wl_apsta.o</code></p>
<dd> Linux 2.4.x driver file (mips)</p>
<dt><code>wl_sta.o</code></p>
<dd> Linux 2.4.x driver file (mips)</p>
<dt><code>wl96345GW.o_save</code></p>
<dd> Linux 2.6.x driver file (mips, bcm6345)</p>
<dt><code>wl96348GW.o_save</code></p>
<dd> Linux 2.6.x driver file (mips, bcm6348)</p>
<dt><code>wl96348GWV_DT.o_save</code></p>
<dd> Linux 2.6.x driver file (mips, bcm6348)</dl>
<h2>AUTHORS</h2>
<p> BCM43xx development team, <a rel="nofollow" href="http://bcm43xx.berlios.de">http://bcm43xx.berlios.de</a> </p>
<h2>Index</h2>
