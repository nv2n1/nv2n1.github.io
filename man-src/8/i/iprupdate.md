---
title: "iprupdate(8)"
name: "iprupdate"
section: "8"
letter: "i"
url: "/docs/linux/man/8-iprupdate/"
description: "iprupdate – IBM Power RAID adapter/device microcode update utility"
---

<p>iprupdate &#8211; IBM Power RAID adapter/device microcode update utility</p>
<h2>Synopsis</h2>
<p><code>iprupdate</code> </p>
<p> <code>iprupdate &#8211;debug &#8211;check_only &#8211;daemon &#8211;use-polling &#8211;use-uevents</code></p>
<h2>Description</h2>
<p><code>iprupdate</code> is used to update the microcode on IBM storage adapters and the disk units attached to them to a minimum supported level. It can be run at any time while the ipr device driver is loaded. The utility will check the microcode revision level of each storage adapter/disk unit on the system and compare it to the microcode revision level that is installed in /etc/microcode, /usr/lib/microcode, and /lib/firmware. If the microcode level on the adapter/device is below the minimum supported level and the level of the latest image is newer, the microcode will be updated to the latest level available. It is desired that this be called in the boot process.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd>Print the version number of <code>iprupdate</code></p>
<dt><code>&#8211;debug</code></p>
<dd>Enable additional error logging. Enabling this will result in additional errors logging to /var/log/messages.</p>
<dt><code>&#8211;check_only</code></p>
<dd>Check if any adapters or disk units are below their minimum supported level.</p>
<dt><code>&#8211;daemon</code></p>
<dd>Run as a daemon to handle adapters and devices being hotplugged.</p>
<dt><code>&#8211;use-polling</code></p>
<dd>Do not use netlink/uevent notification, but rather poll for adapter and device configuration changes.</p>
<dt><code>&#8211;use-uevents</code></p>
<dd>Use netlink/uevent notification rather than polling for adapter and device configuration changes. If not specified, polling will be used until the first uevent notification appears, then netlink will be used.</dl>
<h2>Author</h2>
<p>Brian King (brking [at] us.ibm.com)</p>
