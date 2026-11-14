---
title: "mkqdisk(8)"
name: "mkqdisk"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mkqdisk/"
description: "mkqdisk – Cluster Quorum Disk Utility"
---

<p>mkqdisk &#8211; Cluster Quorum Disk Utility</p>
<h2>Warning</h2>
<p>Use of this command can cause the cluster to malfunction.</p>
<h2>Synopsis</h2>
<p><code>mkqdisk [-?|-h] | [-L] | [-f </code>label<code>] [-c </code>device <code> -l </code>label<code>] [-d [-d &#8230;]] </code></p>
<h2>Description</h2>
<p>The <code>mkqdisk</code> command is used to create a new quorum disk or display existing quorum disks accessible from a given cluster node.</p>
<h2>Options</h2>
<dl>
<dt>-c device -l label</p>
<dd>Initialize a new cluster quorum disk. This will destroy all data on the given device. If a cluster is currently using that device as a quorum disk, the entire cluster will malfunction. Do not run this on an active cluster when qdiskd is running. Only one device on the SAN should ever have the given label; using multiple different devices is currently not supported (it is expected a RAID array is used for quorum disk redundancy). The label can be any textual string up to 127 characters &#8211; and is therefore enough space to hold a UUID created with <a href="/docs/linux/man/1-uuidgen/">uuidgen</a>(1).</p>
<dt>-f label</p>
<dd>Find the cluster quorum disk with the given label and display information about it.</p>
<dt>-L</p>
<dd>Display information on all accessible cluster quorum disks.</p>
<dt>-d</p>
<dd>Increase debugging level. Specify multiple times for more information. Currently, specifying more than twice has no effect. </p>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-qdisk/">qdisk</a>(5), <a href="/docs/linux/man/8-qdiskd/">qdiskd</a>(8), <a href="/docs/linux/man/1-uuidgen/">uuidgen</a>(1) </p>
