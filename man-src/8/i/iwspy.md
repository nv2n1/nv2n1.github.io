---
title: "iwspy(8)"
name: "iwspy"
section: "8"
letter: "i"
url: "/docs/linux/man/8-iwspy/"
description: "iwspy – Get wireless statistics from specific nodes"
---

<p>iwspy &#8211; Get wireless statistics from specific nodes</p>
<h2>Synopsis</h2>
<p><code>iwspy [</code><i>interface</i><code>]</code><br />
 <code>iwspy </code><i>interface</i><code> [+] </code><i>DNSNAME</i><code> | </code><i>IPADDR</i><code> | </code><i>HWADDR</i><code> [&#8230;]</code><br />
 <code>iwspy </code><i>interface</i><code> off</code><br />
 <code>iwspy </code><i>interface</i><code> setthr </code><i>low high</i><br />
 <code>iwspy </code><i>interface</i><code> getthr</code></p>
<h2>Description</h2>
<p><code>Iwspy</code> is used to set a list of addresses to monitor in a wireless network interface and to read back quality of link information for each of those. This information is the same as the one available in <i>/proc/net/wireless</i> : quality of the link, signal strength and noise level. </p>
<p> This information is updated each time a new packet is received, so each address of the list adds some overhead in the driver. </p>
<p> Note that this functionality works only for nodes part of the current wireless cell, you can not monitor Access Points you are not associated with (you can use Scanning for that) and nodes in other cells. In Managed mode, in most case packets are relayed by the Access Point, in this case you will get the signal strength of the Access Point. For those reasons this functionality is mostly useful in Ad-Hoc and Master mode.</p>
<h2>Parameters</h2>
<p>You may set any number of addresses up to 8.</p>
<dl>
<dt><code>DNSNAME</code> | <code>IPADDR</code></p>
<dd>Set an IP address, or in some cases a DNS name (using the name resolver). As the hardware works with hardware addresses, <code>iwspy</code> will translate this IP address through <i>ARP</i>. In some case, this address might not be in the ARP cache and <code>iwspy</code> will fail. In those case, <i><a href="/docs/linux/man/8-ping/">ping</a></i>(8) this name/address and retry.</p>
<dt><code>HWADDR</code></p>
<dd>Set a hardware (MAC) address (this address is not translated &amp; checked like the IP one). The address must contain a colon (<code>:</code>) to be recognised as a hardware address.</p>
<dt><code>+</code></p>
<dd>Add the new set of addresses at the end of the current list instead of replacing it. The address list is unique for each device, so each user should use this option to avoid conflicts.</p>
<dt><code>off</code></p>
<dd>Remove the current list of addresses and disable the spy functionality</p>
<dt><code>setthr</code></p>
<dd>Set the <i>low</i> and <i>high</i> signal strength threshold for the iwspy event (for drivers that support it).<br />
 Every time the signal strength for any of the address monitored with iwspy goes lower than the low threshold or goes higher than the high threshold, a Wireless Event will be generated.<br />
 This can be used to monitor link outages without having to run iwspy periodically.</p>
<dt><code>getthr</code></p>
<dd>Retrieve the current <i>low</i> and <i>high</i> signal strength threshold for the iwspy event.</dl>
<h2>Files</h2>
<p><i>/proc/net/wireless</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-iwconfig/">iwconfig</a></code>(8), <code><a href="/docs/linux/man/8-iwlist/">iwlist</a></code>(8), <code><a href="/docs/linux/man/8-iwevent/">iwevent</a></code>(8), <code><a href="/docs/linux/man/8-iwpriv/">iwpriv</a></code>(8), <code><a href="/docs/linux/man/7-wireless/">wireless</a></code>(7). </p>
