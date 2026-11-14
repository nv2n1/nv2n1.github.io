---
title: "isunoem(8)"
name: "isunoem"
section: "8"
letter: "i"
url: "/docs/linux/man/8-isunoem/"
description: "ipmiutil_sunoem – OEM commands for Sun servers"
---

<p>ipmiutil_sunoem &#8211; OEM commands for Sun servers</p>
<h2>Synopsis</h2>
<p><code>ipmiutil sunoem [-mx -NPRUEFJTVY] commands</code> </p>
<h2>Description</h2>
<p><i>ipmiutil sunoem commands</i> is a program that uses Sun OEM IPMI commands to perform platform-specific functions. </p>
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
<dt><i>led</i></p>
<dd>
<dl>
<dd>These commands provide a way to get and set the status of LEDs on a Sun Microsystems server. Use &#8216;sdr list generic&#8217; to get a list of devices that are controllable LEDs. The <i>ledtype</i> parameter is optional and not necessary to provide on the command line unless it is required by hardware.</p>
<dl>
<dt><i>get</i> <code>sensorid</code> [<code>ledtype</code>]</p>
<dd>Get status of a particular LED described by a Generic Device Locator record in the SDR. A sensorid of <i>all</i> will get the status of all available LEDS.</p>
<dt><i>set</i> <code>sensorid</code> <code>ledmode</code> [<code>ledtype</code>]</p>
<dd>Set status of a particular LED described by a Generic Device Locator record in the SDR. A sensorid of <i>all</i> will set the status of all available LEDS to the specified <i>ledmode</i> and <i>ledtype</i>.</p>
<dt>LED Mode is required for set operations:</p>
<dd><i>OFF</i> Off<br />
 <i>ON</i> Steady On<br />
 <i>STANDBY</i> 100ms on 2900ms off blink rate<br />
 <i>SLOW</i> 1HZ blink rate<br />
 <i>FAST</i> 4HZ blink rate</p>
<dt>LED Type is optional:</p>
<dd><i>OK2RM</i> Ok to Remove<br />
 <i>SERVICE</i> Service Required<br />
 <i>ACT</i> Activity<br />
 <i>LOCATE</i> Locate </p>
</dl>
</dl>
<dt><i>fan</i> <i>speed</i> 0-100</p>
<dd>Set system fan speed (PWM duty cycle).</p>
<dl>
<dd>
<dl>
<dt><i>sshkey</i></p>
<dd>
<dl>
<dd>
<dl>
<dt><i>set</i> <code>userid</code> <code>keyfile</code></p>
<dd>This command will allow you to specify an SSH key to use for a particular user on the Service Processor. This key will be used for CLI logins to the SP and not for IPMI sessions. View available users and their userids with the &#8216;user list&#8217; command.</p>
<dt><i>del</i> <code>userid</code></p>
<dd>This command will delete the SSH key for a specified userid.</dl>
</dl>
</dl>
</dl>
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
