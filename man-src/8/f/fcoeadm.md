---
title: "fcoeadm(8)"
name: "fcoeadm"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fcoeadm/"
description: "fcoeadm – The Open-FCoE Administration Tool"
---

<p>fcoeadm &#8211; The Open-FCoE Administration Tool</p>
<h2>Synopsis</h2>
<p><code>fcoeadm</code> [-m|&#8211;mode fabric|vn2vn] -c|&#8211;create <i>ethX</i> </p>
<p> <code>fcoeadm</code> -d|&#8211;destroy <i>ethX</i> </p>
<p> <code>fcoeadm</code> -r|&#8211;reset <i>ethX</i> </p>
<p> <code>fcoeadm</code> -S|&#8211;Scan [<i>ethX</i>] </p>
<p> <code>fcoeadm</code> -i|&#8211;interface [<i>ethX</i>] </p>
<p> <code>fcoeadm</code> -f|&#8211;fcf [<i>ethX</i>] </p>
<p> <code>fcoeadm</code> -t|&#8211;target [<i>ethX</i>] </p>
<p> <code>fcoeadm</code> -l|&#8211;lun [<i>ethX</i>] </p>
<p> <code>fcoeadm</code> -s|&#8211;stats <i>ethX</i> [<i>interval</i>] </p>
<p> <code>fcoeadm</code> -b|&#8211;lesb <i>ethX</i> [<i>interval</i>] </p>
<p> <code>fcoeadm</code> -h|&#8211;help </p>
<p> <code>fcoeadm</code> -v|&#8211;version</p>
<h2>Description</h2>
<p>The <code>fcoeadm</code> utility is the Fibre Channel over Ethernet (FCoE) management tool for the <i>Open-FCoE</i> project. <code>fcoeadm</code> may be used to create, destroy, and reset an FCoE instance on a given network interface. For these operations <code>fcoeadm</code> sends a command to a running <code>fcoemon</code> process, via a socket interface. <code>fcoemon</code> will then perform the requested operation. </p>
<p> <code>fcoeadm</code> also provides operations to query information about FCoE instances, including interface information, target information, LUN information, and port statistics. For much of this information, <code>fcoeadm</code> relies on the <i>libhbalinux</i> implementation of the <i>HBA API</i>. Only one operation may be given on a command.</p>
<h2>Options</h2>
<p><code>-m</code>, <code>&#8211;mode</code> fabric|vn2vn</p>
<dl>
<dd>Used together with the create option to control the FCoE mode of operation. The mode defaults to fabric but this option allows the selection of vn2vn mode.</dl>
<h2>Operations</h2>
<p><code>-c</code>, <code>&#8211;create</code> <i>ethX</i></p>
<dl>
<dd>Creates an FCoE instance based on the specified network interface. Note that if there is not an fcoemon configuration file for the interface (/etc/fcoe/cfg-ethX, see <code>fcoemon</code>), then the created FCoE instance will not require DCB.</dl>
<p> <code>-d</code>, <code>&#8211;destroy</code> <i>ethX</i></p>
<dl>
<dd>Destroys the FCoE instance on the specified network interface. This will not destroy FCoE instances created by fipvlan.</dl>
<p> <code>-r</code>, <code>&#8211;reset</code> <i>ethX</i></p>
<dl>
<dd>Resets the FCoE instance on the specified network interface. This will not reset FCoE instances created by fipvlan.</dl>
<p> <code>-S</code>, <code>&#8211;Scan</code> <i>ethX</i></p>
<dl>
<dd>Rescan for new targets and LUNs on the provided instance. This command will not rescan any NPIV instances created on the same port. This will not rescan any FCoE instance created by fipvlan.</dl>
<p> <code>-i</code>, <code>&#8211;interface</code> [<i>ethX</i>]</p>
<dl>
<dd>Show information about the FCoE instance on the specified network interface, or all FCoE instances if no network interface is specified.</dl>
<p> <code>-f</code>, <code>&#8211;fcf</code> [<i>ethX</i>]</p>
<dl>
<dd>Show information about the discovered Fibre Channel Forwarders (FCFs) on the specified network interface, or all discovered FCFs if no network interface is specified.</dl>
<p> <code>-t</code>, <code>&#8211;target</code> [<i>ethX</i>]</p>
<dl>
<dd>Show information about the discovered targets associated with the FCoE instance on the specified network interface. If no network interface is specified, information about discovered targets from all FCoE instances will be shown.</dl>
<p> <code>-l</code>, <code>&#8211;lun</code> [<i>ethX</i>]</p>
<dl>
<dd>Show detailed information about the discovered SCSI LUNs associated with the FCoE instance on the specified network interface. If no network interface is specified, information about SCSI LUNs from all FCoE instances will be shown.</dl>
<p> <code>-s</code>, <code>&#8211;stats</code> <i>ethX</i> [<i>interval</i>]</p>
<dl>
<dd>Show the statistics (including FC4 statistics) of the FCoE connection on the specified network interface. The information will be displayed repeatedly until the user cancels the command. The statistics will be printed every specified <i>interval</i> (in seconds). <i>interval</i> should be specified as a whole number greater than 0. If <i>interval</i> is not specified, a default interval of one second is used.</dl>
<p> <code>-b</code>, <code>&#8211;lesb</code> <i>ethX</i> [<i>interval</i>]</p>
<dl>
<dd>Show the Link Error Statistics Block (LESB) of the FCoE connection on the specified network interface. The information will be displayed repeatedly until the user cancels the command. The LESB statistics will be printed every specified <i>interval</i> (in seconds). <i>interval</i> should be specified in whole integers greater than 0. If the <i>interval</i> is not specified, a default interval of one second is used.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Displays the usage message of the <code>fcoeadm</code> command.</dl>
<p> <code>-v</code>, <code>&#8211;version</code></p>
<dl>
<dd>Displays the version of the <code>fcoeadm</code> command.</dl>
<h2>Interface Names</h2>
<p>The actual name for <i>ethX</i> depends on the <code>AUTO_VLAN</code> setting in the fcoemon interface configuration (/etc/fcoe/cfg-ethX, see <code>fcoemon</code>). </p>
<p> If <code>AUTO_VLAN</code> is set to <i>yes</i>, the interface name <i>ethX</i> references the network device itself. If <code>AUTO_VLAN</code> is set to <i>no</i>, the interface name <i>ethX</i> references the VLAN device.</p>
<h2>Examples</h2>
<p>Creates an FCoE instance on eth2.101 </p>
<dl>
<dd>
<pre>fcoeadm -c eth2.101</pre>
</dl>
<p> Creates an FCoE VN2VN instance on eth2.101 </p>
<dl>
<dd>
<pre>fcoeadm -m vn2vn -c eth2.101</pre>
</dl>
<p> Destroys the FCoE instance on eth2.101 </p>
<dl>
<dd>
<pre>fcoeadm -d eth2.101</pre>
</dl>
<p> Resets the FCoE instance on eth2.101 </p>
<dl>
<dd>
<pre>fcoeadm -r eth2.101</pre>
</dl>
<p> Show the information of all the adapters and their ports having FCoE instances created </p>
<dl>
<dd>
<pre>fcoeadm -i</pre>
</dl>
<p> Show the information of all FCoE instances on interface eth3. </p>
<dl>
<dd>
<pre>fcoeadm -i eth3</pre>
</dl>
<p> Show the information of all the discovered targets from all the ports having FCoE instances created (they may be on different adapter cards). A brief listing of discovered LUNs are listed after the target they are associated with, if any </p>
<dl>
<dd>
<pre>fcoeadm -t</pre>
</dl>
<p> Show the information of all the discovered targets from a given port (eth3) having FCoE instance created. A brief listing of discovered LUNs are listed after each target they are associated with, if any </p>
<dl>
<dd>
<pre>fcoeadm -t eth3</pre>
</dl>
<p> Show the detailed information of all the LUNs discovered on all FCoE connections </p>
<dl>
<dd>
<pre>fcoeadm -l</pre>
</dl>
<p> Show the detailed information of all the LUNs associated with a specific interface </p>
<dl>
<dd>
<pre>fcoeadm -l eth3.101</pre>
</dl>
<p> Show the statistics information of a specific port eth3 having FCoE instances created. The statistics are displayed one line per time interval. The default interval is one second if an interval is not specified </p>
<dl>
<dd>
<pre>fcoeadm -s eth3</pre>
</dl>
<dl>
<dd>
<pre>fcoeadm -s eth3 3</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-fcoemon/">fcoemon</a></code>(8)</p>
<h2>Support</h2>
<p><code>fcoeadm</code> is part of the <i>fcoe-utils</i> package, maintained through the <i>Open-FCoE</i> project. Resources for both developers and users can be found at the <i>Open-FCoE</i> website <a rel="nofollow" href="http://open-fcoe.org/">http://open-fcoe.org/</a></p>
