---
title: "ifirewall(8)"
name: "ifirewall"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ifirewall/"
description: "ipmiutil_firewall – configure the IPMI firmware firewall functions"
---

<p>ipmiutil_firewall &#8211; configure the IPMI firmware firewall functions </p>
<h2>Synopsis</h2>
<p><code>ipmiutil firewall [-mxNUPREFJTVY] parameters</code> </p>
<h2>Description</h2>
<p>This <i>ipmiutil firewall</i> command supports the IPMI Firmware Firewall capability. It may be used to add or remove security-based restrictions on certain commands/command sub-functions or to list the current firmware firewall restrictions set on any commands. For each firmware firewall command listed below, parameters may be included to cause the command to be executed with increasing granularity on a specific LUN, for a specific NetFn, for a specific IPMI Command, and finally for a specific command&#8217;s sub-function. See Appendix H in the IPMI 2.0 Specification for a listing of any sub-function numbers that may be associated with a particular command. This utility can use either the /dev/ipmi0 driver from OpenIPMI, the /dev/imb driver from Intel, the /dev/ipmikcs driver from valinux, direct user-space IOs, or the IPMI LAN interface if -N. </p>
<h2>Options</h2>
<p>Command line options are described below.</p>
<dl>
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
<p>Parameter syntax and dependencies are as follows: </p>
<p> firewall [<i>channel</i> <code>H</code>] [<i>lun</i> <code>L</code> [ <i>netfn</i> <code>N</code> [<i>command</i> <code>C</code> [<i>subfn</i> <code>S</code>]]]] </p>
<p> Note that if &quot;netfn <code>N</code>&quot; is specified, then &quot;lun <code>L</code>&quot; must also be specified; if &quot;command <code>C</code>&quot; is specified, then &quot;netfn <code>N</code>&quot; (and therefore &quot;lun <code>L</code>&quot;) must also be specified, and so forth. </p>
<p> &quot;channel <code>H</code>&quot; is an optional and standalone parameter. If not specified, the requested operation will be performed on the current channel. Note that command support may vary from channel to channel. </p>
<p> Firmware firewall commands:</p>
<dl>
<dd>
<dl>
<dt><i>info</i> [<code>(Parms as described above)</code>]</p>
<dd>List firmware firewall information for the specified LUN, NetFn, and Command (if supplied) on the current or specified channel. Listed information includes the support, configurable, and enabled bits for the specified command or commands. </p>
<p> Some usage examples:</p>
<dl>
<dd>
<dl>
<dt><i>info</i> [<code>channel H</code>] [<code>lun L</code>]</p>
<dd>This command will list firmware firewall information for all NetFns for the specified LUN on either the current or the specified channel.</p>
<dt><i>info</i> [<code>channel H</code>] [<code>lun L</code> [ <code>netfn N</code> ]</p>
<dd>This command will print out all command information for a single LUN/NetFn pair.</p>
<dt><i>info</i> [<code>channel H</code>] [<code>lun L</code> [ <code>netfn N</code> [<code>command C</code>] ]]</p>
<dd>This prints out detailed, human-readable information showing the support, configurable, and enabled bits for the specified command on the specified LUN/NetFn pair. Information will be printed about each of the command subfunctions.</p>
<dt><i>info</i> [<code>channel H</code>] [<code>lun L</code> [ <code>netfn N</code> [<code>command C</code> [<code>subfn S</code>]]]]</p>
<dd>Print out information for a specific sub-function.</dl>
</dl>
<dt><i>enable</i> [<code>(Parms as described above)</code>]</p>
<dd>This command is used to enable commands for a given NetFn/LUN combination on the specified channel.</p>
<dt><i>disable</i> [<code>(Parms as described above)</code>] [<code>force</code>]</p>
<dd>This command is used to disable commands for a given NetFn/LUN combination on the specified channel. Great care should be taken if using the &quot;force&quot; option so as not to disable the &quot;Set Command Enables&quot; command.</p>
<dt><i>reset</i> [<code>(Parms as described above)</code>]</p>
<dd>This command may be used to reset the firmware firewall back to a state where all commands and command sub-functions are enabled. </p>
</dl>
</dl>
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
