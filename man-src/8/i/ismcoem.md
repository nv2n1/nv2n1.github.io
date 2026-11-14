---
title: "ismcoem(8)"
name: "ismcoem"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ismcoem/"
description: "ipmiutil_smcoem – OEM commands for SuperMicro servers"
---

<p>ipmiutil_smcoem &#8211; OEM commands for SuperMicro servers</p>
<h2>Synopsis</h2>
<p><code>ipmiutil smcoem [-mx -NPRUEFJTVY] commands</code> </p>
<h2>Description</h2>
<p><i>ipmiutil smcoem</i> is a function that uses SuperMicro OEM IPMI commands to perform platform-specific functions. </p>
<h2>Options</h2>
<dl>
<dt>-m 002000</p>
<dd>Show FRU for a specific MC (e.g. bus 00, sa 20, lun 00). This could be used for PICMG or ATCA blade systems. The trailing character, if present, indicates SMI addressing if &#8216;s&#8217;, or IPMB addressing if &#8216;i&#8217; or not present.</p>
<dt>-x</p>
<dd>Causes extra debug messages to be displayed.</p>
<dt>-N nodename</p>
<dd>Nodename or IP address of the remote target system. If a nodename is specified, IPMI LAN interface is used. Otherwise the local system management interface is used.</p>
<dt>-P/-R rmt_pswd</p>
<dd>Remote password for the nodename given. The default is a null password.</p>
<dt>-U rmt_user</p>
<dd>Remote username for the nodename given. The default is a null username.</p>
<dt>-E</p>
<dd>Use the remote password from Environment variable IPMI_PASSWORD.</p>
<dt>-F drv_t</p>
<dd>Force the driver type to one of the followng: imb, va, open, gnu, landesk, lan, lan2, lan2i, kcs, smb. Note that lan2i means lan2 with intelplus. The default is to detect any available driver type and use it.</p>
<dt>-J</p>
<dd>Use the specified LanPlus cipher suite (0 thru 17): 0=none/none/none, 1=sha1/none/none, 2=sha1/sha1/none, 3=sha1/sha1/cbc128, 4=sha1/sha1/xrc4_128, 5=sha1/sha1/xrc4_40, 6=md5/none/none, &#8230; 14=md5/md5/xrc4_40. Default is 3.</p>
<dt>-T</p>
<dd>Use a specified IPMI LAN Authentication Type: 0=None, 1=MD2, 2=MD5, 4=Straight Password, 5=OEM.</p>
<dt>-V</p>
<dd>Use a specified IPMI LAN privilege level. 1=Callback level, 2=User level, 3=Operator level, 4=Administrator level (default), 5=OEM level.</p>
<dt>-Y</p>
<dd>Yes, do prompt the user for the IPMI LAN remote password. Alternatives for the password are -E or -P. </p>
</dl>
<h2>Commands</h2>
<dl>
<dt><i>intrusion</i></p>
<dd>
<dl>
<dd>This command resets any chassis intrusion condition that may have occurred.</dl>
<dt><i>bmcstatus</i> <code>[enable|disable]</code></p>
<dd>
<dl>
<dd>This command gets or sets the BMC service status. Alone, without arguments, it gets the BMC status as either enabled or disabled. With an argument of either enable or disable, it will also set the BMC status as specified.</dl>
<dt><i>firmware</i></p>
<dd>
<dl>
<dd>This command gets the extra firmware version information, if available. </p>
</dl>
<dt><i>lanport</i> <code>[dedicated|lan1|failover]</code></p>
<dd>
<dl>
<dd>This command gets or sets the IPMI LAN interface port. If set to dedicated, only the dedicated IPMI NIC can be configured for IPMI LAN. If set to lan1, only the first onboard NIC (LAN1) can be configured for IPMI LAN. If set to failover, both the dedicated and onboard LAN1 port would be configured for IPMI LAN, with the same IP address.</dl>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ipmiutil/">ipmiutil</a>(8) <a href="/docs/linux/man/8-ialarms/">ialarms</a>(8) <a href="/docs/linux/man/8-iconfig/">iconfig</a>(8) <a href="/docs/linux/man/8-icmd/">icmd</a>(8) <a href="/docs/linux/man/8-idiscover/">idiscover</a>(8) <a href="/docs/linux/man/8-ievents/">ievents</a>(8) <a href="/docs/linux/man/8-ifru/">ifru</a>(8) <a href="/docs/linux/man/8-igetevent/">igetevent</a>(8) <a href="/docs/linux/man/8-ihealth/">ihealth</a>(8) <a href="/docs/linux/man/8-ilan/">ilan</a>(8) <a href="/docs/linux/man/8-ireset/">ireset</a>(8) <a href="/docs/linux/man/8-isel/">isel</a>(8) <a href="/docs/linux/man/8-isensor/">isensor</a>(8) <a href="/docs/linux/man/8-iserial/">iserial</a>(8) <a href="/docs/linux/man/8-isol/">isol</a>(8) </p>
<h2>Warnings</h2>
<p>See <a rel="nofollow" href="http://ipmiutil.sourceforge.net/">http://ipmiutil.sourceforge.net/</a> for the latest version of ipmiutil and any bug fix list.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2013 Andy Cress </p>
<p> See the file COPYING in the distribution for more details regarding redistribution. </p>
<p> This utility is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY.</p>
<h2>Author</h2>
<p>Andy Cress &lt;arcress at users.sourceforge.net&gt;</p>
