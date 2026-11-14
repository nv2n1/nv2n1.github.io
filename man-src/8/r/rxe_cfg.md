---
title: "rxe_cfg(8)"
name: "rxe_cfg"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rxe_cfg/"
description: "rxe_cfg – rxe configuration tool for RXE (Soft RoCE)"
---

<p>rxe_cfg &#8211; rxe configuration tool for RXE (Soft RoCE)</p>
<h2>Synopsis</h2>
<p><code>rxe_cfg [status]</code><br />
 <code>rxe_cfg start</code> [<code>-p</code> <i>proto</i>]<br />
 <code>rxe_cfg stop</code><br />
 <code>rxe_cfg persistent</code><br />
 <code>rxe_cfg add</code> [<code>-n</code>] <i>ethN</i><br />
 <code>rxe_cfg remove</code> [<code>-n</code>] <i>ethN</i>|<i>rxeN</i><br />
 <code>rxe_cfg crc enable</code>|<code>disable</code><br />
 <code>rxe_cfg</code> <code>mtu</code> [<code>-f</code>] [<i>rxeN</i>] <i>mtu_size</i></p>
<h2>Description</h2>
<p>rxe_cfg is the configuration tool for the RXE software implementation of the RoCE protocol. The RXE kernel modules are loaded, configured, reconfigured and unloaded via the various rxe_cfg command options, documented below. </p>
<h2>Parameters</h2>
<dl>
<dt><i>proto</i></p>
<dd>Ethertype field. Default value is 0x8915. This value must be changed to use RXE on Mellanox ConnectX adapters. </p>
<dt><i>ethN</i></p>
<dd>Network device name as listed in /sys/class/net. Only Ethernet devices are supported; ie. eth0 or eth0.1234 for VLANs. </p>
<dt><i>rxeN</i></p>
<dd>RXE device name as listed in /sys/class/infiniband/. Examples are rxe0 or rxe1. </p>
<dt><i>mtu_size</i></p>
<dd>RoCE mtu. For RoCE the mtu represents the payload excluding headers and has the possible values: 256, 512, 1024, 2048 and 4096. </p>
</dl>
<h2>Commands</h2>
<dl>
<dt>[<code>status</code>]</p>
<dd>The <code>status</code> command prints a table of information on available Ethernet devices and configured RXE instances. The status display is the default if no options are provided. </p>
<dt><code>start</code> [<code>-p</code> <i>proto</i>]</p>
<dd>The <code>start</code> command loads the RXE modules and configures any persistent instances. If the <code>-p</code> <i>proto</i> option is included, the RXE modules will be configured to use Ethertype = <i>proto</i>. (This allows testing RXE on devices, like Mellanox ConnectX, that already support the default RoCE Ethertype in hardware.) </p>
<dt><code>stop</code></p>
<dd>The <code>stop</code> command unconfigures all RXE instances and attempts to unload the kernel modules. </p>
<dt><code>persistent</code></p>
<dd>The <code>persistent</code> command prints the list of Ethernet devices for which a RXE instance is persistently configured. </p>
<dt><code>add</code> [<code>-n</code>] <i>ethN</i></p>
<dd>The <code>add</code> command will configure a RXE instance on Ethernet device <i>ethN</i> (e.g. eth0). The RXE modules must have already been loaded via <code>rxe_cfg start</code>. </p>
<p> The default behavior is to add <i>ethN</i> to a file of persistent configurations and the same RXE device will be configured the next time that <code>rxe_cfg start</code> is run. If the <code>-n</code> option is included the device is not added to the persistence file. </p>
<dt><code>remove</code> [<code>-n</code>] <i>ethN</i>|<i>rxeN</i></p>
<dd>The <code>remove</code> command will remove the specified RXE instance. The parameter must match a currently active ethN or rxeN name. </p>
<p> If the <code>-n</code> option is included the RXE device will be removed but not removed from the persistent state. So it will be recreated the next time that <code>rxe_cfg start</code> is run. </p>
<dt><code>mtu</code> [<code>-f</code>] [<i>rxeN</i>] <i>mtu_size</i></p>
<dd>The <code>mtu</code> command will set the RoCE MTU of all RXE devices to <i>mtu_size</i>, provided that the underlying Ethernet MTU is sufficiently large. If the Ethernet MTU is not large enough, RXE will use the largest MTU that fits; the driver remembers the requested RoCE MTU and will increase the currently active MTU if the Ethernet MTU is later changed up to the requested MTU. </p>
<p> If the <code>-f</code> option is included the underlying Ethernet MTUs will be increased if necessary to the minimum size to accommodate a RoCE MTU of <i>size</i>. </p>
<p> If a <i>rxeN</i> instance is specified then only that instance will be affected by the command. </p>
<dt><code>crc</code> <code>enable</code>|<code>disable</code></p>
<dd>The <code>crc</code> command will enable or disable RoCE ICRC calculation. Valid ICRCs are be required to communicate hardware RoCE NICs, but when a RXE instance is communicating with another RXE instance the performance will be better with the CRC disabled. </p>
<p> This option is global to all RXE instances. </p>
</dl>
<h2>Files</h2>
<dl>
<dt><code>[PREFIX]/etc/rxe.conf</code></p>
<dd>RXE configuration file. Contains the list of persistent RXE instances. All persistent RXE instances can be removed by deleting this file (note this will take effect on the next &quot;rxe_cfg start&quot; &#8212; to remove actively configured instances, you must &quot;rxe_cfg stop&quot;). </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-rxe/">rxe</a></code>(7),</p>
<h2>Authors</h2>
<p>Written by John Groves, Frank Zago and Bob Pearson at System Fabric Works.</p>
