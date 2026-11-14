---
title: "sil_dev_config(9)"
name: "sil_dev_config"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sil_dev_config/"
description: "sil_dev_config – Apply device/host-specific errata fixups"
---

<p>sil_dev_config &#8211; Apply device/host-specific errata fixups</p>
<h2>Synopsis</h2>
<pre><code>void sil_dev_config(struct ata_device *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>Device to be examined</dl>
<h2>Description</h2>
<p>After the IDENTIFY [PACKET] DEVICE step is complete, and a device is known to be present, this function is called. We apply two errata fixups which are specific to Silicon Image, a Seagate and a Maxtor fixup. </p>
<p> For certain Seagate devices, we must limit the maximum sectors to under 8K. </p>
<p> For certain Maxtor devices, we must not program the drive beyond udma5. </p>
<p> Both fixups are unfairly pessimistic. As soon as I get more information on these errata, I will create a more exhaustive list, and apply the fixups to only the specific devices/hosts/firmwares that need it. </p>
<p> 20040111 &#8211; Seagate drives affected by the Mod15Write bug are blacklisted The Maxtor quirk is in the blacklist, but I&#8217;m keeping the original pessimistic fix for the following reasons&#8230; &#8211; There seems to be less info on it, only one device gleaned off the Windows driver, maybe only one is affected. More info would be greatly appreciated. &#8211; But then again UDMA5 is hardly anything to complain about</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
