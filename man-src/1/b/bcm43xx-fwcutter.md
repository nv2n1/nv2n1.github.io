---

title: "bcm43xx-fwcutter(1)"
name: "bcm43xx-fwcutter"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bcm43xx-fwcutter/"
description: "bcm43xx-fwcutter – manual page for bcm43xx-fwcutter"
---

<p> bcm43xx-fwcutter &#8211; manual page for bcm43xx-fwcutter</p>
<h2>SYNOPSIS</h2>
<p> <code>bcm43xx-fwcutter</code> [<i>OPTION</i>] [<i>DRIVER</i>]</p>
<h2>DESCRIPTION</h2>
<p> Bcm43xx-fwcutter can extract the firmware for your Broadcom 43xx hardware from different closed source drivers. The bcm43xx driver depends on this firmware files and can&#8217;t work without them. </p>
<p> Currently bcm43xx-fwcutter supports Apple MacOS X, Microsoft Windows 98/ME/2000/XP and Linux drivers, but keep in mind that bcm43xx-fwcutter doesn&#8217;t support all driver versions. </p>
<p> Example:</p>
<dl>
<dt>
</dt><dd> bcm43xx-fwcutter bcmwl5.sys</dd></dl>
<p> to cut the firmware out of bcmwl5.sys</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-l</code>|&#8211;list</dt>
<dd> List supported driver versions</dd>
<dt><code>-i</code>|&#8211;identify</dt>
<dd> Only identify the driver file (don&#8217;t extract)</dd>
<dt><code>-w</code>|&#8211;target-dir DIR</dt>
<dd> Extract and write firmware to DIR</dd>
<dt><code>-a</code>|&#8211;alt-iv</dt>
<dd> Extract alternative initvals (only 3.10.x.x)</dd>
<dt><code>-p</code>|&#8211;postfix &quot;.FOO&quot;</dt>
<dd> Postfix for firmware filenames (.FOO.fw)</dd>
<dt><code>-v</code>|&#8211;version</dt>
<dd> Print bcm43xx-fwcutter version</dd>
<dt><code>-h</code>|&#8211;help</dt>
<dd> Print help information</dd></dl>
<h2>DRIVERS</h2>
<dl>
<dt><code>AppleAirPort2</code></dt>
<dd> Apple MacOS 10.x driver file (ppc, x86)</dd>
<dt><code>AppleAirPort3</code></dt>
<dd> Apple MacOS 10.x driver file (ppc)</dd>
<dt><code>AppleAirPortBrcm4311</code></dt>
<dd> Apple MacOS 10.4 driver file (x86)</dd>
<dt><code>bcmwl5.sys</code></dt>
<dd> Microsoft Windows driver file, 32bit (x86)</dd>
<dt><code>bcmwl564.sys</code></dt>
<dd> Microsoft Windows driver file, 64bit (x86-64)</dd>
<dt><code>bcmwl5a.sys</code></dt>
<dd> Microsoft Windows driver file, 32bit (x86)</dd>
<dt><code>mn720-50.sys</code></dt>
<dd> This is a renamed bcmwl5.sys driver for Microsoft Wireless MN-720 Notebook Adapter and MN-730 PCI Adapter</dd>
<dt><code>n54gnds.sys</code></dt>
<dd> This is a renamed bcmwl5.sys driver for Planex GW-NS54G 54Mbps Wireless LAN Cards</dd>
<dt><code>wmp11v27.sys</code></dt>
<dd> This is a renamed bcmwl5.sys driver for Linksys WMP-11 802.11b PCI Cards</dd>
<dt><code>wn511b.sys</code></dt>
<dd> This is a renamed bcmwl5.sys driver for Netgear WN511B Cards</dd>
<dt><code>ap_d11ucode.o</code></dt>
<dd> Linux 2.4.x driver file (mips)</dd>
<dt><code>apsta_d11ucode.o</code></dt>
<dd> Linux 2.4.x driver file (mips)</dd>
<dt><code>sta_d11ucode.o</code></dt>
<dd> Linux 2.4.x driver file (mips)</dd>
<dt><code>wl.o</code></dt>
<dd> Linux 2.4.x driver file (mips)</dd>
<dt><code>wl_ap.o</code></dt>
<dd> Linux 2.4.x driver file (mips)</dd>
<dt><code>wl_apsta.o</code></dt>
<dd> Linux 2.4.x driver file (mips)</dd>
<dt><code>wl_sta.o</code></dt>
<dd> Linux 2.4.x driver file (mips)</dd>
<dt><code>wl96345GW.o_save</code></dt>
<dd> Linux 2.6.x driver file (mips, bcm6345)</dd>
<dt><code>wl96348GW.o_save</code></dt>
<dd> Linux 2.6.x driver file (mips, bcm6348)</dd>
<dt><code>wl96348GWV_DT.o_save</code></dt>
<dd> Linux 2.6.x driver file (mips, bcm6348)</dd></dl>
<h2>AUTHORS</h2>
<p> BCM43xx development team, <a rel="nofollow" href="http://bcm43xx.berlios.de">http://bcm43xx.berlios.de</a> </p>
