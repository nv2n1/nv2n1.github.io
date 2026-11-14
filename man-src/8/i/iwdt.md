---
title: "iwdt(8)"
name: "iwdt"
section: "8"
letter: "i"
url: "/docs/linux/man/8-iwdt/"
description: "ipmiutil_wdt- display and set WatchDog Timer parameters"
---

<p>ipmiutil_wdt- display and set WatchDog Timer parameters</p>
<h2>Synopsis</h2>
<p><code>ipmiutil wdt [-acdelrtx -N node -P/-R pswd -U user -EFJTVY]</code> </p>
<h2>Description</h2>
<p><i>ipmiutil wdt</i> is a program that uses IPMI commands to display and set WatchDog Timer parameters. This utility can use either any available IPMI driver, or direct user-space IOs, or the IPMI LAN interface if -N. This utility is an example of how to access the IPMI watchdog parameters directly, which allows changing the timer configuration. There is an init script provided with ipmiutil to automate the task of managing the watchdog timer in user-space.<br />
 # chkconfig &#8211;add ipmiutil_wdt (skip this if no chkconfig)<br />
 # /etc/init.d/ipmiutil_wdt start<br />
 This sets the watchdog timer to reset the system if the wdt is not restarted within 90 seconds. It creates an /etc/cron.d/wdt file to restart wdt every 60 seconds. See also ipmiutil UserGuide section 4.4 for more information. </p>
<h2>Options</h2>
<p>Command line options are described below.</p>
<dl>
<dt>-a N</p>
<dd>Set watchdog event Action to N. Values: 0 = No action, 1 = Hard Reset(default), 2 = Power down, 3 = Power cycle.</p>
<dt>-c</p>
<dd>Show watchdog output in a canonical format, with a default delimiter of &#8216;|&#8217;.</p>
<dt>-d</p>
<dd>Disables the watchdog timer.</p>
<dt>-e</p>
<dd>Enables the watchdog timer. The timer is not actually started, however, until the timer is reset. The pre-timeout action is not enabled.</p>
<dt>-l</p>
<dd>Set the watchdog dontLog bit to not log watchdog events in the SEL.</p>
<dt>-p N</p>
<dd>Set watchdog Pretimeout event action to N. Values: 0 = No action(default), 1 = SMI, 2 = NMI, 3 = Messaging Interrupt. If this is set to an action other than 0, the pretimeout will also be set to 90% of the timeout. However, if the timeout is less than 20 seconds, the pretimeout will not be enabled.</p>
<dt>-q S</p>
<dd>Set watchdog pretimeout value to S seconds, rather than 90% of the timeout as in -p. The pretimeout value must be &gt;= 5 and at least 5 seconds less than the timeout value.</p>
<dt>-r</p>
<dd>Resets the watchdog timer. This should be done every N seconds if the timer is running to prevent the watchdog action (usually a system reset) from occurring.</p>
<dt>-tN</p>
<dd>Set the watchdog Timeout to N seconds. The default is 120 seconds (2 minutes).</p>
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
