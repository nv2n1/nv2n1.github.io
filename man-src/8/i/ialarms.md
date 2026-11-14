---
title: "ialarms(8)"
name: "ialarms"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ialarms/"
description: "ipmiutil_alarms – display and set alarm indicators"
---

<p>ipmiutil_alarms &#8211; display and set alarm indicators</p>
<h2>Synopsis</h2>
<p><code>ipmiutil alarms [-abcdimnoprx -N node -U user -P/-R pswd -EFJTVY]</code> </p>
<h2>Description</h2>
<p><i>ipmiutil alarms</i> is a program that uses IPMI commands to display and set alarm indicators, which are usually LEDs on the system chassis front panel. This utility can use either the /dev/ipmi0 driver from OpenIPMI, the /dev/imb driver from Intel, the /dev/ipmikcs driver from valinux, direct user-space IOs, or the IPMI LAN interface if -N. Note that a LAN user must have Administrative privileges to read or write the alarm LEDs. Note that this utility may not be the only logic setting alarm states. The BMC firmware, system management software, or cluster fault manager may also want to set alarm states. Intel provides a Telco Alarms Manager API which presents a consolidated interface for all alarm management applications. </p>
<h2>Options</h2>
<p>Command line options are described below.</p>
<dl>
<dt>-r</p>
<dd>Read-only. Show the alarms status, but do not set any states. This is also the default mode if no parameters are specified.</p>
<dt>-iN</p>
<dd>Sets the Chassis Identify feature, which can be an LED or some other alarm. If N=0, turn off the Chassis ID, otherwise turn the ID on for N seconds. N=255 will turn on the ID indefinitely, if it is IPMI 2.0.</p>
<dt>-aN</p>
<dd>Sets Disk A Fault LED. If N=0, turn it off. If N=1, turn it on. Used only for TIGPT1U platform.</p>
<dt>-bN</p>
<dd>Sets Disk B Fault LED. If N=0, turn it off. If N=1, turn it on. Used only for TIGPT1U platform.</p>
<dt>-dXN</p>
<dd>Sets Disk X Fault LED, where X=0-6. If N=0, turn it off. If N=1, turn it on. Used only for NSC2U platform.</p>
<dt>-cN</p>
<dd>Sets the Critical Alarm. If N=0, turn it off. If N=1, turn it on.</p>
<dt>-mN</p>
<dd>Sets the Major Alarm. If N=0, turn it off. If N=1, turn it on.</p>
<dt>-nN</p>
<dd>Sets the Minor Alarm. If N=0, turn it off. If N=1, turn it on.</p>
<dt>-pN</p>
<dd>Sets the Power Alarm. If N=0, turn it off. If N=1, turn it on. Note that the Power LED is also wired to the System Fault LED in the back of the system, so this state may be off for Power, but the LED could be lit for a System Fault reason instead. Refer to the system Technical Product Specification for System Faults.</p>
<dt>-o</p>
<dd>Sets all alarms off, including the Chassis ID.</p>
<dt>-x</p>
<dd>Causes extra debug messages to be displayed. </p>
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
<dd>Use this IPMI LAN Authentication Type: 0=None, 1=MD2, 2=MD5, 4=Straight Password, 5=OEM.</p>
<dt>-V</p>
<dd>Use this IPMI LAN privilege level. 1=Callback level, 2=User level, 3=Operator level, 4=Administrator level (default), 5=OEM level.</p>
<dt>-Y</p>
<dd>Yes, do prompt the user for the IPMI LAN remote password. Alternatives for the password are -E or -P. </p>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ipmiutil/">ipmiutil</a>(8) <a href="/docs/linux/man/8-iconfig/">iconfig</a>(8) <a href="/docs/linux/man/8-icmd/">icmd</a>(8) <a href="/docs/linux/man/8-idiscover/">idiscover</a>(8) <a href="/docs/linux/man/8-ievents/">ievents</a>(8) <a href="/docs/linux/man/8-ifru/">ifru</a>(8) <a href="/docs/linux/man/8-igetevent/">igetevent</a>(8) <a href="/docs/linux/man/8-ihealth/">ihealth</a>(8) <a href="/docs/linux/man/8-ilan/">ilan</a>(8) <a href="/docs/linux/man/8-ireset/">ireset</a>(8) <a href="/docs/linux/man/8-isel/">isel</a>(8) <a href="/docs/linux/man/8-isensor/">isensor</a>(8) <a href="/docs/linux/man/8-iserial/">iserial</a>(8) <a href="/docs/linux/man/8-isol/">isol</a>(8) <a href="/docs/linux/man/8-iwdt/">iwdt</a>(8) </p>
<h2>Warnings</h2>
<p>See <a rel="nofollow" href="http://ipmiutil.sourceforge.net/">http://ipmiutil.sourceforge.net/</a> for the latest version of ipmiutil and any bug fix list.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2009 Kontron America, Inc. </p>
<p> See the file COPYING in the distribution for more details regarding redistribution. </p>
<p> This utility is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY.</p>
<h2>Author</h2>
<p>Andy Cress &lt;arcress at users.sourceforge.net&gt;</p>
