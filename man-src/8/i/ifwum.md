---
title: "ifwum(8)"
name: "ifwum"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ifwum/"
description: "ipmiutil_fwum – Update IPMC using Kontron OEM Firmware Update Manager"
---

<p>ipmiutil_fwum &#8211; Update IPMC using Kontron OEM Firmware Update Manager </p>
<h2>Synopsis</h2>
<p><code>ipmiutil fwum [-mixNUPREFJTVY] parameters</code> </p>
<h2>Description</h2>
<p>This <i>ipmiutil fwum</i> subcommand updates IPMC firmware using Kontron OEM Firmware Update Manager. This utility can use either the /dev/ipmi0 driver from OpenIPMI, the /dev/imb driver from Intel, the /dev/ipmikcs driver from valinux, direct user-space IOs, or the IPMI LAN interface if -N. </p>
<h2>Options</h2>
<p>Command line options are described below.</p>
<dl>
<dt>-i 00</p>
<dd>This option specifies a specific FRU ID to show. The input value should be in hex (0b, 1a, etc.), as shown from the sensor SDR output. The default FRU ID is zero (0).</p>
<dt>-m 002000</p>
<dd>Show FRU for a specific MC (e.g. bus 00, sa 20, lun 00). This could be used for PICMG or ATCA blade systems. The trailing character, if present, indicates SMI addressing if &#8216;s&#8217;, or IPMB addressing if &#8216;i&#8217; or not present.</p>
<dt>-x</p>
<dd>Causes extra debug messages to be displayed.</p>
<dt>-N nodename</p>
<dd>Nodename or IP address of the remote target system. If a nodename is specified, IPMI LAN interface is used. Otherwise the local system management interface is used.</p>
<dt>-U rmt_user</p>
<dd>Remote username for the nodename given. The default is a null username.</p>
<dt>-P/-R rmt_pswd</p>
<dd>Remote password for the nodename given. The default is a null password.</p>
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
<h2>Parameters</h2>
<p><i>fwum</i> <code>parameters</code></p>
<dl>
<dd>
<dl>
<dt><i>info</i></p>
<dd>Show information about current firmware. </p>
<dt><i>status</i></p>
<dd>Show status of each firmware bank present in the hardware. </p>
<dt><i>download</i> <code>filename</code></p>
<dd>Download the specified firmware image. </p>
<dt><i>upgrade</i> [<code>filename</code>]</p>
<dd>Install firmware upgrade. If the filename is specified, the file is downloaded first, otherwise the last firmware downloaded is used. </p>
<dt><i>rollback</i></p>
<dd>Ask IPMC to rollback to previous version. </p>
<dt><i>tracelog</i></p>
<dd>Show the firmware upgrade log. </p>
</dl>
</dl>
<h2>Examples</h2>
<p>ipmiutil fwum info<br />
 Gets Firmware information ipmiutil fwum -N 192.168.1.1 -U root -P pswd download firmware.img<br />
 Downloads the firmware version contained in firmware.img over IPMI LAN. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ipmiutil/">ipmiutil</a>(8) <a href="/docs/linux/man/8-ialarms/">ialarms</a>(8) <a href="/docs/linux/man/8-iconfig/">iconfig</a>(8) <a href="/docs/linux/man/8-idiscover/">idiscover</a>(8) <a href="/docs/linux/man/8-ievents/">ievents</a>(8) <a href="/docs/linux/man/8-ifru/">ifru</a>(8) <a href="/docs/linux/man/8-igetevent/">igetevent</a>(8) <a href="/docs/linux/man/8-ihealth/">ihealth</a>(8) <a href="/docs/linux/man/8-ilan/">ilan</a>(8) <a href="/docs/linux/man/8-ireset/">ireset</a>(8) <a href="/docs/linux/man/8-isel/">isel</a>(8) <a href="/docs/linux/man/8-isensor/">isensor</a>(8) <a href="/docs/linux/man/8-iserial/">iserial</a>(8) <a href="/docs/linux/man/8-isol/">isol</a>(8) <a href="/docs/linux/man/8-iwdt/">iwdt</a>(8) </p>
<h2>Warnings</h2>
<p>See <a rel="nofollow" href="http://ipmiutil.sourceforge.net/">http://ipmiutil.sourceforge.net/</a> for the latest version of ipmiutil and any bug fix list.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2010 Kontron America, Inc. </p>
<p> See the file COPYING in the distribution for more details regarding redistribution. </p>
<p> This utility is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY.</p>
<h2>Author</h2>
<p>Andy Cress &lt;arcress at users.sourceforge.net&gt;</p>
