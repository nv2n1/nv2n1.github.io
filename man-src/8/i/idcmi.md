---
title: "idcmi(8)"
name: "idcmi"
section: "8"
letter: "i"
url: "/docs/linux/man/8-idcmi/"
description: "ipmiutil_dcmi – handle DCMI functions"
---

<p>ipmiutil_dcmi &#8211; handle DCMI functions </p>
<h2>Synopsis</h2>
<p><code>ipmiutil dcmi [-admsx -NUPREFTVY] &lt;function&gt;</code> </p>
<h2>Description</h2>
<p>This <i>ipmiutil dcmi</i> subcommand handles DCMI command functions according to the DCMI specification. This utility can use either the /dev/ipmi0 driver from OpenIPMI, the /dev/imb driver from Intel, the /dev/ipmikcs driver from valinux, direct user-space IOs, or the IPMI LAN interface if -N. </p>
<h2>Options</h2>
<p>Command line options are described below.</p>
<dl>
<dt>-a string</p>
<dd>Set the DCMI Asset Tag to this string.</p>
<dt>-d string</p>
<dd>Set the DCMI MC ID to this string.</p>
<dt>-m 002000</p>
<dd>Target a specific MC (e.g. bus 00, sa 20, lun 00). This could be used for PICMG or ATCA blade systems. The trailing character, if present, indicates SMI addressing if &#8216;s&#8217;, or IPMB addressing if &#8216;i&#8217; or not present.</p>
<dt>-s</p>
<dd>When getting info, also get the DCMI sensor information.</p>
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
<h2>Functions</h2>
<dl>
<dt>info</p>
<dd>Get DCMI Capabilities, MC ID, and Asset Tag. This is the default function if no function was specified. </p>
<dt>power</p>
<dd>Get DCMI Power reading and DCMI Power limit, if supported in the DCMI capabilties.</p>
<dt>power set_limit</p>
<dd>Set Power limit</p>
<dt>power set_action &lt;action&gt;</p>
<dd>Set Power limit exception action (where action = no_action | power_off | log_sel)</p>
<dt>power set_correction</p>
<dd>Set Power limit correction time (in ms)</p>
<dt>power set_sample</p>
<dd>Set Power limit sampling period (in sec)</p>
<dt>power activate</p>
<dd>Activate Power limit</p>
<dt>power deactivate</p>
<dd>Deactivate Power limit </p>
<dt>thermal</p>
<dd>Get/Set DCMI Thermal parameters. This requires DCMI 1.5 support. </p>
<dt>config</p>
<dd>Get/Set DCMI Configuration parameters. This requires DCMI 1.5 support. </p>
<dt>help</p>
<dd>Show the help (usage) message </p>
</dl>
<h2>Examples</h2>
<p>ipmiutil dcmi info -s<br />
 Gets DCMI information, plus DCMI sensor information ipmiutil dcmi -N 192.168.1.1 -U root -P pswd<br />
 Gets DCMI information over IPMI LAN. </p>
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
