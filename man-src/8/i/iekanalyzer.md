---
title: "iekanalyzer(8)"
name: "iekanalyzer"
section: "8"
letter: "i"
url: "/docs/linux/man/8-iekanalyzer/"
description: "ipmiutil_ekanalyzer – run FRU-Ekeying analyzer with FRU files"
---

<p>ipmiutil_ekanalyzer &#8211; run FRU-Ekeying analyzer with FRU files</p>
<h2>Synopsis</h2>
<p><code>ipmiutil ekanalyzer [-mx -NPRUEFJTVY] commands </code> <code>(deprecated, see ifru instead)</code> </p>
<h2>Description</h2>
<p><i>ipmiutil ekanalyzer</i> is a program that analyzes FRU Ekeying information from files saved from PICMG IPMI systems. </p>
<dl>
<dt><i>filename1</i></p>
<dd>binary file that stores FRU data of a Carrier or an AMC module</p>
<dt><i>filename2</i></p>
<dd>binary file that stores FRU data of an AMC module. These binary files can be generated from this command:<br />
&nbsp;<wbr>&nbsp;<wbr><i>ipmiutil fru -i id -d filename</i></p>
<dt><i>filename3</i></p>
<dd>configuration file used for configuring On-Carrier Device ID or OEM GUID. This file is optional.</p>
<dt><i>xx</i></p>
<dd>indicates the type of the file. It can take the following value: </p>
<p>&nbsp;<wbr>&nbsp;<wbr><i>oc</i>&nbsp;<wbr>: On-Carrier device </p>
<p>&nbsp;<wbr>&nbsp;<wbr><i>a1</i>&nbsp;<wbr>: AMC slot A1 </p>
<p>&nbsp;<wbr>&nbsp;<wbr><i>a2</i>&nbsp;<wbr>: AMC slot A2 </p>
<p>&nbsp;<wbr>&nbsp;<wbr><i>a3</i>&nbsp;<wbr>: AMC slot A3 </p>
<p>&nbsp;<wbr>&nbsp;<wbr><i>a4</i>&nbsp;<wbr>: AMC slot A4 </p>
<p>&nbsp;<wbr>&nbsp;<wbr><i>b1</i>&nbsp;<wbr>: AMC slot B1 </p>
<p>&nbsp;<wbr>&nbsp;<wbr><i>b2</i>&nbsp;<wbr>: AMC slot B2 </p>
<p>&nbsp;<wbr>&nbsp;<wbr><i>b3</i>&nbsp;<wbr>: AMC slot B3 </p>
<p>&nbsp;<wbr>&nbsp;<wbr><i>b4</i>&nbsp;<wbr>: AMC slot B4 </p>
<p>&nbsp;<wbr>&nbsp;<wbr><i>sm</i>&nbsp;<wbr>: Shelf Manager </p>
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
<dd>The available commands for ekanalyzer are: </p>
<dl>
<dd>
<dl>
<dt><i>print</i> [<code>carrier</code> | <code>power</code> | <code>all</code>]</p>
<dd>
<dl>
<dd>
<dl>
<dt><i>carrier</i> (default) <code>oc=filename1</code> <code>oc=filename2</code> <code>&#8230;</code></p>
<dd>Display point to point physical connectivity between carriers and AMC modules.<br />
&nbsp;<wbr>Example:<br />
#&nbsp;<wbr>ipmiutil ekanalyzer print carrier oc=fru oc=carrierfru<br />
From Carrier file: fru<br />
Number of AMC bays supported by Carrier: 2<br />
AMC slot B1 topology:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Port 0&nbsp;<wbr>=====&gt;&nbsp;<wbr>On Carrier Device ID 0, Port 16<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Port 1&nbsp;<wbr>=====&gt;&nbsp;<wbr>On Carrier Device ID 0, Port 12<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Port 2&nbsp;<wbr>=====&gt;&nbsp;<wbr>AMC slot B2, Port 2<br />
AMC slot B2 topology:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Port 0&nbsp;<wbr>=====&gt;&nbsp;<wbr>On Carrier Device ID 0, Port 3<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Port 2&nbsp;<wbr>=====&gt;&nbsp;<wbr>AMC slot B1, Port 2<br />
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*<br />
From Carrier file: carrierfru<br />
On Carrier Device ID 0 topology:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Port 0&nbsp;<wbr>=====&gt;&nbsp;<wbr>AMC slot B1, Port 4<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Port 1&nbsp;<wbr>=====&gt;&nbsp;<wbr>AMC slot B1, Port 5<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Port 2&nbsp;<wbr>=====&gt;&nbsp;<wbr>AMC slot B2, Port 6<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Port 3&nbsp;<wbr>=====&gt;&nbsp;<wbr>AMC slot B2, Port 7<br />
AMC slot B1 topology:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Port 0&nbsp;<wbr>=====&gt;&nbsp;<wbr>AMC slot B2, Port 0<br />
AMC slot B1 topology:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Port 1&nbsp;<wbr>=====&gt;&nbsp;<wbr>AMC slot B2, Port 1<br />
Number of AMC bays supported by Carrier: 2 </p>
<dt><i>power</i> <code>xx=filename1</code> <code>xx=filename2</code> <code>&#8230;</code></p>
<dd>Display power supply information between carrier and AMC modules.</p>
<dt><i>all</i> <code>xx=filename</code> <code>xx=filename</code> <code>&#8230;</code></p>
<dd>Display both physical connectivity and power supply of each carrier and AMC modules. </p>
</dl>
</dl>
<dt><i>frushow</i> <code>xx=filename</code></p>
<dd>Convert a binary FRU file into human readable text format. Use -v option to get more display information. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dt><i>summary</i> [<code>match</code> | <code>unmatch</code> | <code>all</code>]</p>
<dd>
<dl>
<dd>
<dl>
<dt><i>match</i> (default) <code>xx=filename</code> <code>xx=filename</code> <code>&#8230;</code></p>
<dd>Display only matched results of Ekeying match between an On-Carrier device and an AMC module or between 2 AMC modules. Example:<br />
&nbsp;<wbr>#&nbsp;<wbr>ipmiutil ekanalyzer summary match oc=fru b1=amcB1 a2=amcA2<br />
&nbsp;<wbr>On-Carrier Device vs AMC slot B1<br />
&nbsp;<wbr>&nbsp;<wbr>AMC slot B1 port 0&nbsp;<wbr>==&gt;&nbsp;<wbr>On-Carrier Device 0 port 16<br />
Matching Result<br />
From On-Carrier Device ID 0<br />
&nbsp;<wbr>&nbsp;<wbr>Channel ID 11 || Lane 0: enable<br />
&nbsp;<wbr>&nbsp;<wbr>Link Type: AMC.2 Ethernet<br />
&nbsp;<wbr>&nbsp;<wbr>Link Type extension: 1000BASE-BX&nbsp;<wbr>(SerDES Gigabit)&nbsp;<wbr>Ethernet link<br />
&nbsp;<wbr>&nbsp;<wbr>Link Group ID: 0 || Link Asym. Match: exact match<br />
To AMC slot B1<br />
&nbsp;<wbr>&nbsp;<wbr>Channel ID 0 || Lane 0: enable<br />
&nbsp;<wbr>&nbsp;<wbr>Link Type: AMC.2 Ethernet<br />
&nbsp;<wbr>&nbsp;<wbr>Link Type extension: 1000BASE-BX&nbsp;<wbr>(SerDES Gigabit)&nbsp;<wbr>Ethernet link<br />
&nbsp;<wbr>&nbsp;<wbr>Link Group ID: 0 || Link Asym. Match: exact match<br />
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*<br />
&nbsp;<wbr>&nbsp;<wbr>AMC slot B1 port 1&nbsp;<wbr>==&gt;&nbsp;<wbr>On-Carrier Device 0 port 12<br />
Matching Result<br />
From On-Carrier Device ID 0<br />
&nbsp;<wbr>&nbsp;<wbr>Channel ID 6 || Lane 0: enable<br />
&nbsp;<wbr>&nbsp;<wbr>Link Type: AMC.2 Ethernet<br />
&nbsp;<wbr>&nbsp;<wbr>Link Type extension: 1000BASE-BX&nbsp;<wbr>(SerDES Gigabit)&nbsp;<wbr>Ethernet link<br />
&nbsp;<wbr>&nbsp;<wbr>Link Group ID: 0 || Link Asym. Match: exact match<br />
To AMC slot B1<br />
&nbsp;<wbr>&nbsp;<wbr>Channel ID 1 || Lane 0: enable<br />
&nbsp;<wbr>&nbsp;<wbr>Link Type: AMC.2 Ethernet<br />
&nbsp;<wbr>&nbsp;<wbr>Link Type extension: 1000BASE-BX&nbsp;<wbr>(SerDES Gigabit)&nbsp;<wbr>Ethernet link<br />
&nbsp;<wbr>&nbsp;<wbr>Link Group ID: 0 || Link Asym. Match: exact match<br />
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*<br />
&nbsp;<wbr>On-Carrier Device vs AMC slot A2<br />
&nbsp;<wbr>&nbsp;<wbr>AMC slot A2 port 0&nbsp;<wbr>==&gt;&nbsp;<wbr>On-Carrier Device 0 port 3<br />
Matching Result<br />
From On-Carrier Device ID 0<br />
&nbsp;<wbr>&nbsp;<wbr>Channel ID 9 || Lane 0: enable<br />
&nbsp;<wbr>&nbsp;<wbr>Link Type: AMC.2 Ethernet<br />
&nbsp;<wbr>&nbsp;<wbr>Link Type extension: 1000BASE-BX&nbsp;<wbr>(SerDES Gigabit)&nbsp;<wbr>Ethernet link<br />
&nbsp;<wbr>&nbsp;<wbr>Link Group ID: 0 || Link Asym. Match: exact match<br />
To AMC slot A2<br />
&nbsp;<wbr>&nbsp;<wbr>Channel ID 0 || Lane 0: enable<br />
&nbsp;<wbr>&nbsp;<wbr>Link Type: AMC.2 Ethernet<br />
&nbsp;<wbr>&nbsp;<wbr>Link Type extension: 1000BASE-BX&nbsp;<wbr>(SerDES Gigabit)&nbsp;<wbr>Ethernet link<br />
&nbsp;<wbr>&nbsp;<wbr>Link Group ID: 0 || Link Asym. Match: exact match<br />
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*<br />
&nbsp;<wbr>AMC slot B1 vs AMC slot A2<br />
&nbsp;<wbr>&nbsp;<wbr>AMC slot A2 port 2&nbsp;<wbr>==&gt;&nbsp;<wbr>AMC slot B1 port 2<br />
Matching Result<br />
From AMC slot B1<br />
&nbsp;<wbr>&nbsp;<wbr>Channel ID 2 || Lane 0: enable<br />
&nbsp;<wbr>&nbsp;<wbr>Link Type: AMC.3 Storage<br />
&nbsp;<wbr>&nbsp;<wbr>Link Type extension: Serial Attached SCSI&nbsp;<wbr>(SAS/SATA)<br />
&nbsp;<wbr>&nbsp;<wbr>Link Group ID: 0 || Link Asym. Match: FC or SAS interface&nbsp;<wbr>{exact match}<br />
To AMC slot A2<br />
&nbsp;<wbr>&nbsp;<wbr>Channel ID 2 || Lane 0: enable<br />
&nbsp;<wbr>&nbsp;<wbr>Link Type: AMC.3 Storage<br />
&nbsp;<wbr>&nbsp;<wbr>Link Type extension: Serial Attached SCSI&nbsp;<wbr>(SAS/SATA)<br />
&nbsp;<wbr>&nbsp;<wbr>Link Group ID: 0 || Link Asym. Match: FC or SAS interface&nbsp;<wbr>{exact match}<br />
&nbsp;<wbr>*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*</p>
<dt><i>unmatch</i> <code>xx=filename</code> <code>xx=filename</code> <code>&#8230;</code></p>
<dd>Display the unmatched results of Ekeying match between an On-Carrier device and an AMC module or between 2 AMC modules</p>
<dt><i>all</i> <code>xx=filename</code> <code>xx=filename</code> <code>&#8230;</code></p>
<dd>Display both matched result and unmatched results of Ekeying match between two cards or two modules.</dl>
</dl>
</dl>
</dl>
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
