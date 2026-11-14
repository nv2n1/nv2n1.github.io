---
title: "devlink-region(8)"
name: "devlink-region"
section: "8"
letter: "d"
url: "/docs/linux/man/8-devlink-region/"
description: "devlink-region – devlink address region access"
---

<p>devlink-region &#8211; devlink address region access</p>
<h2>Synopsis</h2>
<pre><code>devlink

[ OPTIONS ]

region

{ COMMAND |

    help }

OPTIONS := {

    -V[ersion] |
    -n[no-nice-names] }</code></pre>
<p> <code>devlink region show</code> [ <i>DEV/REGION</i> ]<br />
 <code>devlink region del</code> <i>DEV/REGION</i> <code>snapshot</code> <i>SNAPSHOT_ID</i><br />
 <code>devlink region dump</code> <i>DEV/REGION</i> <code>snapshot</code> <i>SNAPSHOT_ID</i><br />
 <code>devlink region read</code> <i>DEV/REGION</i> <code>[ </code> <code>snapshot</code> <i>SNAPSHOT_ID</i> <code>]</code> <code>address</code> <i>ADDRESS</i> <code>length</code> <i>LENGTH</i><br />
 <code>devlink region help</code> </p>
<h2>Description</h2>
<h3>devlink region show &#8211; Show all supported address regions names, snapshots and sizes</h3>
<p><i>DEV/REGION</i> &#8211; specifies the devlink device and address-region to query.</p>
<h3>devlink region del &#8211; Delete a snapshot specified by address-region name and snapshot ID</h3>
<p><i>DEV/REGION</i> &#8211; specifies the devlink device and address-region to delete the snapshot from snapshot <i>SNAPSHOT_ID</i> &#8211; specifies the snapshot ID to delete</p>
<h3>devlink region dump &#8211; Dump all the available data from a region or from snapshot of a region</h3>
<p><i>DEV/REGION</i> &#8211; specifies the device and address-region to dump from. snapshot <i>SNAPSHOT_ID</i> &#8211; specifies the snapshot-id of the region to dump.</p>
<h3>devlink region read &#8211; Read from a specific region address for a given length</h3>
<p><i>DEV/REGION</i> &#8211; specifies the device and address-region to read from. snapshot <i>SNAPSHOT_ID</i> &#8211; specifies the snapshot-id of the region to read. address <i>ADDRESS</i> &#8211; specifies the address to read from. length <i>LENGTH</i> &#8211; specifies the length of data to read. </p>
<h2>Examples</h2>
<p>devlink region show</p>
<dl>
<dd>List available address regions and snapshot.</dl>
<p> devlink region del pci/0000:00:05.0/cr-space snapshot 1</p>
<dl>
<dd>Delete snapshot id 1 from cr-space address region from device pci/0000:00:05.0.</dl>
<p> devlink region dump pci/0000:00:05.0/cr-space snapshot 1</p>
<dl>
<dd>Dump the snapshot taken from cr-space address region with ID 1</dl>
<p> devlink region read pci/0000:00:05.0/cr-space snapshot 1 address 0x10 legth 16</p>
<dl>
<dd>Read from address 0x10, 16 Bytes of snapshot ID 1 taken from cr-space address region</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-devlink/">devlink</a></code>(8), <code><a href="/docs/linux/man/8-devlink-dev/">devlink-dev</a></code>(8), <code><a href="/docs/linux/man/8-devlink-port/">devlink-port</a></code>(8), <code><a href="/docs/linux/man/8-devlink-monitor/">devlink-monitor</a></code>(8), </p>
<h2>Author</h2>
<p>Alex Vesker &lt;valex [at] mellanox.com&gt;</p>
