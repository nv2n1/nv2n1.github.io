---
title: "icmd(8)"
name: "icmd"
section: "8"
letter: "i"
url: "/docs/linux/man/8-icmd/"
description: "ipmiutil_cmd – a tool to send specific IPMI commands via the command line."
---

<p>ipmiutil_cmd &#8211; a tool to send specific IPMI commands via the command line. </p>
<h2>Synopsis</h2>
<p><code>ipmiutil cmd [-pqsx -NUPREFJTVY] bus rsSa netFn/lun cmd [data bytes]</code> </p>
<h2>Description</h2>
<p>This <i>ipmiutil cmd</i> tool sends specific IPMI commands to the firmware. The commands are composed as hex values on the command line. This tool was written to allow in-band use to match the DOS CMDTOOL.EXE or IPMITOOL.EXE program which is distributed with many Intel servers. Certain scripts or pre-written commands may have been supplied for the DOS tool that can now be used while the system is running Linux or Windows. This utility can use either the /dev/ipmi0 driver from OpenIPMI, the /dev/imb driver from Intel, the /dev/ipmikcs driver from valinux, direct user-space IOs, or the IPMI LAN interface if -N. This tool should only be used if you are familiar with the IPMI 1.5 specification, or you have specific pre-written commands to send. </p>
<h2>Options</h2>
<p>Command line options are described below.</p>
<dl>
<dt>-p</p>
<dd>Port to use. Defaults to RMCP port 623.</p>
<dt>-q</p>
<dd>Quiet mode. Show only minimal header information.</p>
<dt>-s</p>
<dd>Skips the GetDeviceID command</p>
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
<p>The following parameters are used by icmd. Each is represented as a two-digit hex byte. The parameters have no default values. </p>
<dl>
<dt>bus</p>
<dd>This byte contains the bus number for this command, usually 00. </p>
<dt>rsSa</p>
<dd>This is the resource slave address, usually 0x20 for the BMC. </p>
<dt>netFn/lun</p>
<dd>This byte combines the net Function and Lun. The 2 low-order bits are the Lun and the 6 high-order bits are the net Function. This representation is consistent with the DOS CMDTOOL/IPMITOOL. </p>
<dt>cmd</p>
<dd>This byte contains the IPMI command. </p>
<dt>[data bytes]</p>
<dd>This is a sequence of zero to 16 bytes that represent data bytes specific to this command. </p>
</dl>
<h2>Examples</h2>
<p>icmd 00 20 18 01<br />
 Sends the GetDevice ID command to the BMC. icmd 00 20 28 43 00 00 ff ff 00 ff<br />
 Sends a Get SEL entry command for the last entry in the firmware log. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ipmiutil/">ipmiutil</a>(8) <a href="/docs/linux/man/8-ialarms/">ialarms</a>(8) <a href="/docs/linux/man/8-iconfig/">iconfig</a>(8) <a href="/docs/linux/man/8-idiscover/">idiscover</a>(8) <a href="/docs/linux/man/8-ievents/">ievents</a>(8) <a href="/docs/linux/man/8-ifru/">ifru</a>(8) <a href="/docs/linux/man/8-igetevent/">igetevent</a>(8) <a href="/docs/linux/man/8-ihealth/">ihealth</a>(8) <a href="/docs/linux/man/8-ilan/">ilan</a>(8) <a href="/docs/linux/man/8-ireset/">ireset</a>(8) <a href="/docs/linux/man/8-isel/">isel</a>(8) <a href="/docs/linux/man/8-isensor/">isensor</a>(8) <a href="/docs/linux/man/8-iserial/">iserial</a>(8) <a href="/docs/linux/man/8-isol/">isol</a>(8) <a href="/docs/linux/man/8-iwdt/">iwdt</a>(8) </p>
<h2>Warnings</h2>
<p>See <a rel="nofollow" href="http://ipmiutil.sourceforge.net/">http://ipmiutil.sourceforge.net/</a> for the latest version of ipmiutil and any bug fix list.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2009 Kontron America, Inc. </p>
<p> See the file COPYING in the distribution for more details regarding redistribution. </p>
<p> This utility is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY.</p>
<h2>Author</h2>
<p>Andy Cress &lt;arcress at users.sourceforge.net&gt;</p>
