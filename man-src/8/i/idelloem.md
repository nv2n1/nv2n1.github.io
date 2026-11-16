---
title: "idelloem(8)"
name: "idelloem"
section: "8"
letter: "i"
url: "/docs/linux/man/8-idelloem/"
description: "ipmiutil_delloem – OEM commands for Dell servers"
---

<p>ipmiutil_delloem &#8211; OEM commands for Dell servers</p>
<h2>Synopsis</h2>
<p><code>ipmiutil delloem [-mx -NPRUEFJTVY] commands</code> </p>
<h2>Description</h2>
<p><i>ipmiutil delloem commands</i> is a program that uses Dell OEM IPMI commands to perform platform-specific functions. </p>
<h2>Options</h2>
<dl>
<dt>-m 002000</dt>
<dd>Show FRU for a specific MC (e.g. bus 00, sa 20, lun 00). This could be used for PICMG or ATCA blade systems. The trailing character, if present, indicates SMI addressing if &#8216;s&#8217;, or IPMB addressing if &#8216;i&#8217; or not present.</dd>
<dt>-x</dt>
<dd>Causes extra debug messages to be displayed.</dd>
<dt>-N nodename</dt>
<dd>Nodename or IP address of the remote target system. If a nodename is specified, IPMI LAN interface is used. Otherwise the local system management interface is used.</dd>
<dt>-P/-R rmt_pswd</dt>
<dd>Remote password for the nodename given. The default is a null password.</dd>
<dt>-U rmt_user</dt>
<dd>Remote username for the nodename given. The default is a null username.</dd>
<dt>-E</dt>
<dd>Use the remote password from Environment variable IPMI_PASSWORD.</dd>
<dt>-F drv_t</dt>
<dd>Force the driver type to one of the followng: imb, va, open, gnu, landesk, lan, lan2, lan2i, kcs, smb. Note that lan2i means lan2 with intelplus. The default is to detect any available driver type and use it.</dd>
<dt>-J</dt>
<dd>Use the specified LanPlus cipher suite (0 thru 17): 0=none/none/none, 1=sha1/none/none, 2=sha1/sha1/none, 3=sha1/sha1/cbc128, 4=sha1/sha1/xrc4_128, 5=sha1/sha1/xrc4_40, 6=md5/none/none, &#8230; 14=md5/md5/xrc4_40. Default is 3.</dd>
<dt>-T</dt>
<dd>Use a specified IPMI LAN Authentication Type: 0=None, 1=MD2, 2=MD5, 4=Straight Password, 5=OEM.</dd>
<dt>-V</dt>
<dd>Use a specified IPMI LAN privilege level. 1=Callback level, 2=User level, 3=Operator level, 4=Administrator level (default), 5=OEM level.</dd>
<dt>-Y</dt>
<dd>Yes, do prompt the user for the IPMI LAN remote password. Alternatives for the password are -E or -P. </dd>
</dl>
<h2>Commands</h2>
<dl>
<dd></dd></dl>
<dl>
<dt><i>mac</i> <i>list</i></dt>
<dd>
</dd><dl>
<dd>Lists the MAC address of LOMs </dd>
</dl>
<dt><i>mac</i> <i>get</i> &lt;<code>NIC number</code>&gt;</dt>
<dd>
</dd><dl>
<dd>Shows the MAC address of specified LOM. 0-7 System LOM, 8- DRAC/iDRAC. </dd>
</dl>
<dt><i>lan</i> <i>set</i> &lt;<code>Mode</code>&gt;</dt>
<dd>
</dd><dl>
<dd>Sets the NIC Selection Mode&nbsp;<wbr>(dedicated, shared,<br />
&nbsp;<wbr>shared with failover lom2, shared with Failover all loms). </dd>
</dl>
<dt><i>lan</i> <i>get</i></dt>
<dd>
</dd><dl>
<dd>Returns the current NIC Selection Mode&nbsp;<wbr>(dedicated, shared,<br />
&nbsp;<wbr>shared with failover lom2, shared with Failover all loms). </dd>
</dl>
<dt><i>lan</i> <i>get</i> <i>active</i></dt>
<dd>
</dd><dl>
<dd>Returns the current active NIC&nbsp;<wbr>(dedicated, LOM1, LOM2, LOM3, LOM4). </dd>
</dl>
<dt><i>powermonitor</i></dt>
<dd>
</dd><dl>
<dd>Shows power tracking statistics </dd>
</dl>
<dt><i>powermonitor</i> <i>clear</i> <i>cumulativepower</i></dt>
<dd>
</dd><dl>
<dd>Reset cumulative power reading </dd>
</dl>
<dt><i>powermonitor</i> <i>clear</i> <i>peakpower</i></dt>
<dd>
</dd><dl>
<dd>Reset peak power reading </dd>
</dl>
<dt><i>powermonitor</i> <i>powerconsumption</i></dt>
<dd>
</dd><dl>
<dd>Displays power consumption in&nbsp;<wbr>&lt;watt|btuphr&gt; </dd>
</dl>
<dt><i>powermonitor</i> <i>powerconsumptionhistory</i> &lt;<code>watt|btuphr</code>&gt;</dt>
<dd>
</dd><dl>
<dd>Displays power consumption history </dd>
</dl>
<dt><i>powermonitor</i> <i>getpowerbudget</i></dt>
<dd>
</dd><dl>
<dd>Displays power cap in&nbsp;<wbr>&lt;watt|btuphr&gt; </dd>
</dl>
<dt><i>powermonitor</i> <i>setpowerbudget</i> &lt;<code>val</code>&gt; &lt;<code>watt|btuphr|percent</code>&gt;</dt>
<dd>
</dd><dl>
<dd>Allows user to set the&nbsp;<wbr>&nbsp;<wbr>power cap in&nbsp;<wbr>&lt;watt|BTU/hr|percentage&gt; </dd>
</dl>
<dt><i>powermonitor</i> <i>enablepowercap</i></dt>
<dd>
</dd><dl>
<dd>To enable set power cap </dd>
</dl>
<dt><i>powermonitor</i> <i>disablepowercap</i></dt>
<dd>
</dd><dl>
<dd>To disable set power cap </dd>
</dl>
<dt><i>windbg</i> <i>start</i></dt>
<dd>
</dd><dl>
<dd>Starts the windbg session&nbsp;<wbr>(Cold Reset&nbsp;<wbr>&amp;&nbsp;<wbr>SOL Activation) </dd>
</dl>
<dt><i>windbg</i> <i>end</i></dt>
<dd>
</dd><dl>
<dd>Ends the windbg session&nbsp;<wbr>(SOL Deactivation) </dd>
</dl>
<dt><i>vFlash</i> <i>info</i> <i>Card</i></dt>
<dd>
</dd><dl>
<dd>Shows Extended SD Card information</dd></dl>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ipmiutil/">ipmiutil</a>(8) <a href="/docs/linux/man/8-ialarms/">ialarms</a>(8) <a href="/docs/linux/man/8-iconfig/">iconfig</a>(8) <a href="/docs/linux/man/8-icmd/">icmd</a>(8) <a href="/docs/linux/man/8-idiscover/">idiscover</a>(8) <a href="/docs/linux/man/8-ievents/">ievents</a>(8) <a href="/docs/linux/man/8-ifru/">ifru</a>(8) <a href="/docs/linux/man/8-igetevent/">igetevent</a>(8) <a href="/docs/linux/man/8-ihealth/">ihealth</a>(8) <a href="/docs/linux/man/8-ilan/">ilan</a>(8) <a href="/docs/linux/man/8-ireset/">ireset</a>(8) <a href="/docs/linux/man/8-isel/">isel</a>(8) <a href="/docs/linux/man/8-isensor/">isensor</a>(8) <a href="/docs/linux/man/8-iserial/">iserial</a>(8) <a href="/docs/linux/man/8-isol/">isol</a>(8) </p>
<h2>Warnings</h2>
<p>See <a rel="nofollow" href="http://ipmiutil.sourceforge.net/">http://ipmiutil.sourceforge.net/</a> for the latest version of ipmiutil and any bug fix list.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2009 Kontron America, Inc. </p>
<p> See the file COPYING in the distribution for more details regarding redistribution. </p>
<p> This utility is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY.</p>
<h2>Author</h2>
<p>Andy Cress &lt;arcress at users.sourceforge.net&gt;</p>
