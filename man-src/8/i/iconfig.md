---
title: "iconfig(8)"
name: "iconfig"
section: "8"
letter: "i"
url: "/docs/linux/man/8-iconfig/"
description: "ipmiutil_config – list, save, and restore BMC configuration parameters"
---

<p>ipmiutil_config &#8211; list, save, and restore BMC configuration parameters</p>
<h2>Synopsis</h2>
<p><code>ipmiutil config [-lpxLNUPREFJTVY] [-r file] [-s file]</code> </p>
<h2>Description</h2>
<p><i>ipmiutil config</i> is a program that uses an IPMI driver to send IPMI commands which list, save and restore BMC configuration parameters for LAN, Serial, PEF, SOL, User, Channel. This combines the functionality of ipmiutil lan (ilan) and ipmiutil serial (iserial). Note that some of the LAN parameters cannot be restored remotely over the IPMI LAN, changing the configuration that is in use. This utility can use either the /dev/ipmi0 driver from OpenIPMI, the /dev/imb driver from Intel, the /dev/ipmikcs driver from valinux, direct user-space IOs, or the IPMI LAN interface if -N. </p>
<h2>Options</h2>
<p>Command line options are described below. </p>
<dl>
<dt>-l</p>
<dd>Lists BMC configuration parameters with a keyword, index, and its hex values. This is the default behavior if no options are specified.</p>
<dt>-r config_file</p>
<dd>Restores BMC configuration from config_file, which was produced with -s below.</p>
<dt>-s config_file</p>
<dd>Saves BMC configuration to config_file. This file could be edited, in certain cases, such as to vary the BMC IP address (LanParam 3), or to use the UserPassword records. Note that lines beginning with &#8216;#&#8217; are comments and are ignored. For editing UserPassword records, convert your text value to hex format; for example &quot;echo &#8216;mypassword&#8217; |od -t x1&quot;, and leave off the trailing 0a.</p>
<dt>-x</p>
<dd>Causes extra debug messages to be displayed.</p>
<dt>-p password_to_set</p>
<dd>This specifies the firmware password to set for BMC LAN access for all users during the restore. If not specified, the password configuration will not be changed, unless a valid UserPassword record is present in the file to be restored. Note that user passwords are write-only via standard IPMI commands.</p>
<dt>-L lan_ch_num</p>
<dd>This specifies the IPMI LAN channel number used for BMC LAN. This varies by platform, and can be found in the platform technical specifications. By default, bmcconfig scans all IPMI channels to find a LAN channel for BMC LAN. </p>
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
<p><a href="/docs/linux/man/8-ipmiutil/">ipmiutil</a>(8) <a href="/docs/linux/man/8-ialarms/">ialarms</a>(8) <a href="/docs/linux/man/8-icmd/">icmd</a>(8) <a href="/docs/linux/man/8-idiscover/">idiscover</a>(8) <a href="/docs/linux/man/8-ievents/">ievents</a>(8) <a href="/docs/linux/man/8-ifru/">ifru</a>(8) <a href="/docs/linux/man/8-igetevent/">igetevent</a>(8) <a href="/docs/linux/man/8-ihealth/">ihealth</a>(8) <a href="/docs/linux/man/8-ilan/">ilan</a>(8) <a href="/docs/linux/man/8-ireset/">ireset</a>(8) <a href="/docs/linux/man/8-isel/">isel</a>(8) <a href="/docs/linux/man/8-isensor/">isensor</a>(8) <a href="/docs/linux/man/8-iserial/">iserial</a>(8) <a href="/docs/linux/man/8-isol/">isol</a>(8) <a href="/docs/linux/man/8-iwdt/">iwdt</a>(8) </p>
<h2>Warnings</h2>
<p>See <a rel="nofollow" href="http://ipmiutil.sourceforge.net/">http://ipmiutil.sourceforge.net/</a> for the latest version of ipmiutil and any bug fix list.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2009 Kontron America, Inc. </p>
<p> See the file COPYING in the distribution for more details regarding redistribution. </p>
<p> This utility is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY.</p>
<h2>Author</h2>
<p>Andy Cress &lt;arcress at users.sourceforge.net&gt;</p>
