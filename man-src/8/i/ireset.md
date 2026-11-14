---
title: "ireset(8)"
name: "ireset"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ireset/"
description: "ipmiutil_reset – perform a hardware reset on the system"
---

<p>ipmiutil_reset &#8211; perform a hardware reset on the system</p>
<h2>Synopsis</h2>
<p><code>ipmiutil reset [-bcdDefhijmnoprsuwxy -N node -U user -P/-R pswd -EFJTVY]</code> </p>
<h2>Description</h2>
<p><i>ipmiutil reset</i> is a program that uses IPMI commands to perform a hardware reset of the chassis, or boot to a specific device. This utility can use either the /dev/ipmi0 driver from OpenIPMI, the /dev/imb driver from Intel, the /dev/ipmikcs driver from valinux, direct user-space IOs, or the IPMI LAN interface if -N. </p>
<h2>Options</h2>
<p>Command line options are described below.</p>
<dl>
<dt>-c</p>
<dd>Power Cycle the system chassis</p>
<dt>-d</p>
<dd>Power Down the system chassis</p>
<dt>-n</p>
<dd>Send NMI to the system</p>
<dt>-u</p>
<dd>Power Up the system chassis</p>
<dt>-r</p>
<dd>Hard Reset the system chassis</p>
<dt>-D</p>
<dd>Do a soft shutdown of the OS, and then power down. Note that remote soft shutdown (-D -N) for Intel S5000 baseboard requires ipmiutil getevt -a running on the target server.</p>
<dt>-o</p>
<dd>Do a soft shutdown of the OS, and then reset. Note that remote soft shutdown (-o -N) for Intel S5000 baseboard requires ipmiutil getevt -a running on the target server.</p>
<dt>-k</p>
<dd>Do a cold reset to restart the BMC firmware.</p>
<dt>-m 002000s</p>
<dd>Perform these function for a specific MC (e.g. bus 00, sa 20, lun 00). The trailing character, if present, indicates SMI addressing if &#8216;s&#8217;, or IPMB addressing if &#8216;i&#8217; or not present.</p>
<dt>-b</p>
<dd>Do a hard reset and reboot to the BIOS Setup menu, for this reboot only.</p>
<dt>-e</p>
<dd>Do a hard reset to EFI, if IPMI EFI boot is enabled, for this reboot only.</p>
<dt>-f</p>
<dd>Do a hard reset to Floppy/Removable, for this reboot only.</p>
<dt>-h</p>
<dd>Do a hard reset to a Hard Disk, for this reboot only.</p>
<dt>-i</p>
<dd>Set the boot Initiator mailbox string, usually for PXE use. The string must be less than 78 characters.</p>
<dt>-j</p>
<dd>Set the IANA number used for the boot Initiator mailbox string.</p>
<dt>-p</p>
<dd>Do a hard reset and network boot to PXE server, for this reboot only.</p>
<dt>-s</p>
<dd>Do a hard reset and reboot to the Service/Diagnostic Partition, for this reboot only. Reboots to the default if no service partition is configured.</p>
<dt>-v</p>
<dd>Do a hard reset to DVD/CDROM Media, for this reboot only.</p>
<dt>-w</p>
<dd>Wait for BMC ready after a reset before exiting the utility.</p>
<dt>-x</p>
<dd>Causes extra debug messages to be displayed.</p>
<dt>-y</p>
<dd>Yes, try to persist any boot options used [-befhprsv]. This requires the IPMI firmware to ask the BIOS to change boot order settings, so it may not be supported by all BMC firmware vendors.</p>
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
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ipmiutil/">ipmiutil</a>(8) <a href="/docs/linux/man/8-ialarms/">ialarms</a>(8) <a href="/docs/linux/man/8-iconfig/">iconfig</a>(8) <a href="/docs/linux/man/8-icmd/">icmd</a>(8) <a href="/docs/linux/man/8-idiscover/">idiscover</a>(8) <a href="/docs/linux/man/8-ievents/">ievents</a>(8) <a href="/docs/linux/man/8-ifru/">ifru</a>(8) <a href="/docs/linux/man/8-igetevent/">igetevent</a>(8) <a href="/docs/linux/man/8-ihealth/">ihealth</a>(8) <a href="/docs/linux/man/8-ilan/">ilan</a>(8) <a href="/docs/linux/man/8-isel/">isel</a>(8) <a href="/docs/linux/man/8-isensor/">isensor</a>(8) <a href="/docs/linux/man/8-iserial/">iserial</a>(8) <a href="/docs/linux/man/8-isol/">isol</a>(8) <a href="/docs/linux/man/8-iwdt/">iwdt</a>(8) </p>
<h2>Warnings</h2>
<p>See <a rel="nofollow" href="http://ipmiutil.sourceforge.net/">http://ipmiutil.sourceforge.net/</a> for the latest version of ipmiutil and any bug fix list.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2009 Kontron America, Inc. </p>
<p> See the file COPYING in the distribution for more details regarding redistribution. </p>
<p> This utility is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY.</p>
<h2>Author</h2>
<p>Andy Cress &lt;arcress at users.sourceforge.net&gt;</p>
