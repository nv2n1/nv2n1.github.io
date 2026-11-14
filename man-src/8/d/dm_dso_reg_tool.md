---
title: "dm_dso_reg_tool(8)"
name: "dm_dso_reg_tool"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dm_dso_reg_tool/"
description: "dmevent_tool – A utility used to load a DSO into dmeventd and (un)register devices with it for monitoring"
---

<p><code>dmevent_tool</code> &#8211; A utility used to load a DSO into dmeventd and (un)register devices with it for monitoring</p>
<h2>Synopsis</h2>
<p>dmevent_tool -[Vhmru] {RAID device name} {DSO Name}<br />
&nbsp;<wbr></p>
<h2>Description</h2>
<p>dmevent_tool is a userspace utility used to register/unregister DSOs with the daemon dmeventd. If used with the <code>-m</code> command line parameter users can display all of the actively dmeventd monitored devices. </p>
<h2>Options</h2>
<dl>
<dt>-V Show version of dmevent_tool</p>
<dd></dl>
<p> -{h/?} Show this help information </p>
<p> -m[r|u] List all currently active device mapper devices<br />
&nbsp;<wbr>&nbsp;<wbr>and their current status with dmeventd<br />
&nbsp;<wbr>&nbsp;<wbr>for registered&nbsp;<wbr>(-r)/unregistered&nbsp;<wbr>(-m)&nbsp;<wbr>devices<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Syntax: dmevent_tool -m[u|r] </p>
<p> -a[r|u] Same as -m, but for devices with UUID only!<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Syntax: dmevent_tool -a[u|r] </p>
<p> -r Register a device with dmeventd<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Syntax: dmevent_tool -r&nbsp;<wbr>&lt;device name&gt;&nbsp;<wbr>&lt;path to DSO library&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Example: dmevent_tool -r isw_abcdeh_Volume0 libdmraid-events.so </p>
<p> -u Unregister a device with dmeventd<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Syntax: dmevent_tool -u&nbsp;<wbr>&lt;device name&gt;&nbsp;<wbr>[&lt;path to DSO library&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Example: dmevent_tool -u isw_abcdefgh_Volume0</p>
<h2>Examples</h2>
<p><code>dmevent_tool -m</code> is used to display all of the actively monitored devices </p>
<p>&nbsp;<wbr>dmevent_tool -m<br />
&nbsp;<wbr>Device Name: isw_defeaigdde_Volume0_dmraid00<br />
&nbsp;<wbr>&nbsp;<wbr>Registered DSO:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>libdmraid-events.so<br />
&nbsp;<wbr>&nbsp;<wbr>UUID:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>isw_defeaigdde_Volume0_dmraid00<br />
&nbsp;<wbr>&nbsp;<wbr>status:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Active<br />
&nbsp;<wbr>&nbsp;<wbr>major device&nbsp;<wbr>#:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>253<br />
&nbsp;<wbr>&nbsp;<wbr>minor device&nbsp;<wbr>#:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0<br />
&nbsp;<wbr>&nbsp;<wbr>read only device:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>No<br />
&nbsp;<wbr>&nbsp;<wbr>number of recorded kernel events: 0<br />
&nbsp;<wbr>&nbsp;<wbr>SATA drives in this volume group:&nbsp;<wbr>/dev/sdb&nbsp;<wbr>/dev/sdc<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><br />
 <code>dmevent_tool -r</code> is used to register a volume group device with dmeventd </p>
<p>&nbsp;<wbr>dmevent_tool -r isw_defeaigdde_Volume0_dmraid00 libdmraid-events.so <code>dmevent_tool -u</code> is used to unregister a volume group from dmeventd </p>
<p>&nbsp;<wbr>dmevent_tool -u isw_defeaigdde_Volume0_dmraid00 </p>
<h2>Diagnostics</h2>
<p>dmevent_tool returns an exit code of 0 for success or 1 for error.</p>
<h2>Author</h2>
<p>Brian Wood &lt;brian.j.wood [at] intel.com&gt;</p>
