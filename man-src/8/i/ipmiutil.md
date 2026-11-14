---
title: "ipmiutil(8)"
name: "ipmiutil"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipmiutil/"
description: "ipmiutil – a meta-command to invoke various IPMI functions."
---

<p>ipmiutil &#8211; a meta-command to invoke various IPMI functions. </p>
<h2>Synopsis</h2>
<p><code>ipmiutil &lt;command&gt; [-x -NUPREFJTVY] [other command options]</code> </p>
<h2>Description</h2>
<p>This utility performs various IPMI functions. Each of the individual commands in the ipmiutil project can be invoked via this meta-command. The &lt;command&gt; is one of the following:<br />
alarms&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show/set the front panel alarm LEDs and relays<br />
leds&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show/set the front panel alarm LEDs and relays<br />
cmd&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>send a specified raw IPMI command to the BMC<br />
config&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list/save/restore BMC configuration parameters<br />
dcmi&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>get/set DCMI parameters<br />
discover&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>discover all IPMI servers on this LAN<br />
ekanalyzer&nbsp;<wbr>&nbsp;<wbr>run FRU-EKeying analyzer on FRU files&nbsp;<wbr>(deprecated, see fru)<br />
events&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>decode IPMI events and display them<br />
firewall show/set firmware firewall functions<br />
fru&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show decoded FRU inventory data, write asset tag<br />
fwum&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>OEM firmware update manager extensions<br />
getevt&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>get IPMI events and display them, event daemon<br />
getevent get IPMI events and display them, event daemon<br />
health&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>check and show the basic health of the IPMI BMC<br />
hpm&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>HPM firmware update manager extensions<br />
lan&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show/set IPMI LAN parameters and PEF table<br />
picmg&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show/set picmg extended functions<br />
reset&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>cause the BMC to reset or power down the system<br />
sel&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show/clear firmware System Event Log records<br />
sensor&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show Sensor Data Records, readings, thresholds<br />
serial&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show/set IPMI Serial&nbsp;<wbr>&amp;&nbsp;<wbr>Terminal Mode parameters<br />
sol&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>start/stop an SOL console session<br />
smcoem&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>SuperMicro OEM functions<br />
sunoem&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Sun OEM functions<br />
delloem&nbsp;<wbr>&nbsp;<wbr>Dell OEM functions<br />
tsol&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Tyan SOL console start/stop session<br />
wdt&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show/set/reset the watchdog timer<br />
 For help on each command (e.g. &#8216;sel&#8217;), enter:<br />
ipmiutil sel -?<br />
 For man pages on each command, its man page is named &quot;i&lt;command&gt;&quot;, or refer to SEE ALSO below.<br />
 This utility can use either the /dev/ipmi0 driver from OpenIPMI, the /dev/imb driver from Intel, the /dev/ipmikcs driver from valinux, direct user-space IOs, or the IPMI LAN interface if -N is used. </p>
<h2>Options</h2>
<p>Command options are described in the man page for each command. Below are a few of the common options.</p>
<dl>
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
<h2>Examples</h2>
<p>ipmiutil sel<br />
 Shows the IPMI System Event Log entries. ipmiutil wdt<br />
 Shows the watchdog timer values. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ialarms/">ialarms</a>(8) <a href="/docs/linux/man/8-iconfig/">iconfig</a>(8) <a href="/docs/linux/man/8-icmd/">icmd</a>(8) <a href="/docs/linux/man/8-idiscover/">idiscover</a>(8) <a href="/docs/linux/man/8-ievents/">ievents</a>(8) <a href="/docs/linux/man/8-ifirewall/">ifirewall</a>(8) <a href="/docs/linux/man/8-ifru/">ifru</a>(8) <a href="/docs/linux/man/8-ifruset/">ifruset</a>(8) <a href="/docs/linux/man/8-ifwum/">ifwum</a>(8) <a href="/docs/linux/man/8-igetevent/">igetevent</a>(8) <a href="/docs/linux/man/8-ihealth/">ihealth</a>(8) <a href="/docs/linux/man/8-ihpm/">ihpm</a>(8) <a href="/docs/linux/man/8-ilan/">ilan</a>(8) <a href="/docs/linux/man/8-ipicmg/">ipicmg</a>(8) <a href="/docs/linux/man/8-ireset/">ireset</a>(8) <a href="/docs/linux/man/8-isel/">isel</a>(8) <a href="/docs/linux/man/8-isensor/">isensor</a>(8) <a href="/docs/linux/man/8-iserial/">iserial</a>(8) <a href="/docs/linux/man/8-isol/">isol</a>(8) <a href="/docs/linux/man/8-isunoem/">isunoem</a>(8) <a href="/docs/linux/man/8-iwdt/">iwdt</a>(8) <a href="/docs/linux/man/8-ipmiutil/">ipmiutil</a>(8) <a href="/docs/linux/man/8-ipmi_port/">ipmi_port</a>(8) </p>
<h2>Warnings</h2>
<p>See <a rel="nofollow" href="http://ipmiutil.sourceforge.net/">http://ipmiutil.sourceforge.net/</a> for the latest version of ipmiutil and any bug fix list.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2009 Kontron America, Inc. </p>
<p> See the file COPYING in the distribution for more details regarding redistribution. </p>
<p> This utility is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY.</p>
<h2>Author</h2>
<p>Andy Cress &lt;arcress at users.sourceforge.net&gt;</p>
