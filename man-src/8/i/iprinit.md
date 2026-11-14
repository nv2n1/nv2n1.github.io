---
title: "iprinit(8)"
name: "iprinit"
section: "8"
letter: "i"
url: "/docs/linux/man/8-iprinit/"
description: "iprinit – IBM Power RAID adapter/device initialization utility"
---

<p>iprinit &#8211; IBM Power RAID adapter/device initialization utility</p>
<h2>Synopsis</h2>
<p><code>iprinit</code> </p>
<p> <code>iprinit &#8211;debug &#8211;daemon &#8211;use-polling &#8211;use-uevents</code></p>
<h2>Description</h2>
<p><code>iprinit</code> is used to setup IBM Power RAID adapters and devices for optimal performance. It will enable U320 scsi speeds if it is determined the disk enclosure supports it. It will also enable tagged command queuing. Any scsi bus attributes, such as bus width, or disk attributes, such as queue depth, that have been setup by iprconfig will be loaded as well. It is desired that this be called in the boot process, using the init.d script provided.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd>Print the version number of <code>iprinit</code></p>
<dt><code>&#8211;debug</code></p>
<dd>Enable additional error logging. Enabling this will result in additional errors logging to /var/log/messages.</p>
<dt><code>&#8211;daemon</code></p>
<dd>Run as a daemon to handle adapters and devices being hotplugged.</p>
<dt><code>&#8211;use-polling</code></p>
<dd>Do not use netlink/uevent notification, but rather poll for adapter and device configuration changes.</p>
<dt><code>&#8211;use-uevents</code></p>
<dd>Use netlink/uevent notification rather than polling for adapter and device configuration changes. If not specified, polling will be used until the first uevent notification appears, then netlink will be used.</dl>
<h2>Author</h2>
<p>Brian King (brking [at] us.ibm.com)</p>
