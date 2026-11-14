---
title: "ilan(8)"
name: "ilan"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ilan/"
description: "ipmiutil_lan – show and configure IPMI LAN parameters, users, and set up a PEF rule to send BMC LAN Alerts for OS Critical Stop log events"
---

<p>ipmiutil_lan &#8211; show and configure IPMI LAN parameters, users, and set up a PEF rule to send BMC LAN Alerts for OS Critical Stop log events</p>
<h2>Synopsis</h2>
<p><code>ipmiutil lan [-abcdefghijklmnopq#rstuvwxyzBDQK -i eth1 ]</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[-I ipadr -M macadr -S subnet -B baud_sol&nbsp;<wbr>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[-G gwyip -H gwymac -L lan_channel_num&nbsp;<wbr>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[-A alertip -X alertmac -C community&nbsp;<wbr>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[-u user_to_set -p password_to_set&nbsp;<wbr>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[-N nodename&nbsp;<wbr>&nbsp;<wbr>-U username -Fimb&nbsp;<wbr>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[-P/-R rmt_node_pswd -EFJTVY&nbsp;<wbr>] </p>
<h2>Description</h2>
<p><i>ipmiutil lan</i> shows or sets all of the IPMI LAN Parameters and users to enable remote LAN sessions or BMC LAN Alerts. The IP address and MAC address of the local system, the default gateway, and the alert destination can be defaulted to those specified in Linux, or can be overridden by specific parameters. It also creates a new Platform Event Filter table rule for an OS Critical Stop (0x20) SEL firmware log event, so that it will be enabled to send a BMC LAN Alert. This utility will skip the PEF records if the system does not support IPMI 1.5 or greater. This utility can use either the /dev/ipmi0 driver from OpenIPMI, the /dev/imb driver from Intel, the /dev/ipmikcs driver from valinux, direct user-space IOs, or the IPMI LAN interface if -N. </p>
<h2>Options</h2>
<p>Command line options are described below. Note that without options, ipmiutil lan behaves as if option -r were used. To configure IPMI LAN &amp; PEF, use option -e. </p>
<dl>
<dt>-a alertnum</p>
<dd>Specify which PEF alert number is to be used. Default is 1. This would only be used if extra PEF alert destinations had been set.</p>
<dt>-b authmask</p>
<dd>Specify a certain authtype mask in hex to use when configuring this channel. The default mask is 0x16, so to include authtype None (bit 0), it would require entering &#8216;-b 17&#8217;.</p>
<dt>-c</p>
<dd>Show Canonical output, which shows only interpreted text and streamlines the parameters shown, using a common delimiter.</p>
<dt>-d</p>
<dd>This option disables the IPMI LAN and PEF parameters, so as not to allow BMC LAN connections or alerts. This option also sets the IP address to zeros.</p>
<dt>-e</p>
<dd>This option enables the BMC LAN configuration and PEF event alerts. The utility will attempt to obtain the default BMC LAN parameters from the OS automatically, or they can be specified with command options below.</p>
<dt>-f</p>
<dd>Set the ARP control parameter to 1 = gratuituous ARPs, 2 = ARP responses, or 3 = both grat ARP and ARP responses. The default is 1.</p>
<dt>-g</p>
<dd>This specifies the secondary gateway IP address to use for the BMC LAN. The default is to omit this parameter and only use the default gateway. See also -G.</p>
<dt>-h</p>
<dd>Set the IPMI VLAN ID to this value. Setting to a value &gt;=4096 disables the VLAN ID. The default behavior is not to set this parameter.</p>
<dt>-i ethif</p>
<dd>By default, the eth0 interface is used to find IP and MAC addresses. Sometimes, however, the first ethernet port on the baseboard may be represented by Linux as eth1 or eth2 instead. If so, use this option to indicate the correct ethernet interface to use. By default, ipmiutil lan will scan up to 32 eth interfaces for the onboard one that BMC LAN uses.</p>
<dt>-j</p>
<dd>This sets a custom PEF rule as the last PEF entry. The input is a series of 10 hex bytes, forming the PEF entry. For example, this sample PEF entry would perform a power down action if the Baseboard Temp reached its threshold.<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;ipmiutil lan -e -j020110ffff013001950a&quot;</p>
<dt>-k</p>
<dd>This causes ipmiutil lan to also insert two rules to send alerts for transition-to-OK events, including Power Redundancy OK and Temperature OK.</p>
<dt>-l</p>
<dd>This option enables the BMC LAN configuration, but not PEF events. The utility will attempt to obtain the default BMC LAN parameters from the OS automatically, or they can be specified with command options below.</p>
<dt>-n num</p>
<dd>By default, the new PEF entry for OS Critical Stop is inserted at offset 12 into the table. This can be changed to insert it at an offset &gt; 12 if another entry already exists at offset 12.</p>
<dt>-o</p>
<dd>Disable Only SOL. This could be used after the IPMI LAN was configured, to disable Serial-Over-LAN console access but still allow other IPMI LAN access.</p>
<dt>-p password_to_set</p>
<dd>This specifies the firmware password to set for BMC LAN access. If not specified, the user and password configuration will not be changed.</p>
<dt>-q</p>
<dd>Specify an alternate user number for the LAN username from the -u option. This is normally user number 2, 3, or 4, where 2 is the default. The maximum number of users is 15. Same as -# below.</p>
<dt>-#</p>
<dd>Specify an alternate user number for the LAN username from the -u option. Same as -q above.</p>
<dt>-r</p>
<dd>This option just reads the configuration without writing any BMC LAN parameters or writing any new entries to the PEF table.</p>
<dt>-s</p>
<dd>This option will also display some of the Serial parameters.</p>
<dt>-t</p>
<dd>Test if the BMC LAN has already been configured. Returns 0 if so.</p>
<dt>-u username_to_set</p>
<dd>This specifies the firmware username to set for BMC LAN access. If a username is specified, user 3 will be set. If not specified, the default user 1 will be used.</p>
<dt>-v priv</p>
<dd>Set a specific access priVilege for this user, where priv can be: 1=Callback, 2=User, 3=Operator, 4=Admin, 5=OEM, 15=NoAccess The default if not specified or specified in error, is to use 4=Admin.</p>
<dt>-w N</p>
<dd>Set the Gratuitous ARP Interval to N seconds. This has no effect if the firmware does not support Grat-ARP, as shown in Lan Param 10. If not set, the interval remains at the firmware default.</p>
<dt>-x</p>
<dd>Causes extra debug messages to be displayed.</p>
<dt>-y N</p>
<dd>Set the OEM LAN Failover parameter to N. Values for N with Intel Romley/S2600 baseboards: 1 = enable, 0 = disable. Values for N with SuperMicro baseboards: 2 = failover, 1 = lan1 , 0 = dedicated.</p>
<dt>-z</p>
<dd>Also show the IPMI LAN Statistics</p>
<dt>-A alert_ip_addr</p>
<dd>This specifies the SNMP Alert Destination IP address to use for the BMC LAN. By default, this utility will attempt to obtain this from the /etc/snmp/snmpd.conf file, via the trapsink parameter. The alert destination will see the BMC LAN traps with the enterprises.3183.1.1 OID. If no alert IP address is specified in either snmpd.conf or this parameter, or if that IP address does not respond, the other SNMP parameters for BMC LAN will be skipped.</p>
<dt>-B baud_sol</p>
<dd>This specifies the Baud rate for SerialOverLan. The possible values are: 9600, 19.2k, 38.4k, 57.6k, and 115.2k. The default is 19.2k.</p>
<dt>-C snmp_community</p>
<dd>This specifies the SNMP Community name to use for BMC LAN Alerts. The default community string is &quot;public&quot;. This parameter is ignored if there is no Alert IP address.</p>
<dt>-D</p>
<dd>This causes the local IP address to be determined by DHCP instead of a static IP address.</p>
<dt>-E</p>
<dd>Use the remote password from Environment variable IPMI_PASSWORD.</p>
<dt>-F drv_t</p>
<dd>Force the driver type to one of the followng: imb, va, open, gnu, landesk, lan, lan2, lan2i, kcs, smb. Note that lan2i means lan2 with intelplus. The default is to detect any available driver type and use it.</p>
<dt>-G gwy_ip_addr</p>
<dd>This specifies the default gateway IP address to use for the BMC LAN. The default is to automatically obtain this from the Linux route table.</p>
<dt>-H gwy_mac_addr</p>
<dd>This specifies the default gateway MAC address to use for the BMC LAN. The format can be either 11:22:33:44:55:66 or 11-22-33-44-55-66. The default is to try to automatically obtain this by sending an arp request from an OS LAN eth interface: the default one, or as specified by -i.</p>
<dt>-K hostname</p>
<dd>This specifies the IPMI hostname to set, for Kontron servers only. This enables the firmware to properly map the IP address to a hostname, especially with the web interface. The default is not to set this parameter, and use IP address only.</p>
<dt>-I ip_addr</p>
<dd>This specifies the local IP address to use for the BMC LAN on eth0. The default is to automatically obtain this from the Linux ifconfig.</p>
<dt>-J</p>
<dd>Use the specified LanPlus cipher suite (0 thru 17): 0=none/none/none, 1=sha1/none/none, 2=sha1/sha1/none, 3=sha1/sha1/cbc128, 4=sha1/sha1/xrc4_128, 5=sha1/sha1/xrc4_40, 6=md5/none/none, &#8230; 14=md5/md5/xrc4_40. Default is 3.</p>
<dt>-L lan_ch_num</p>
<dd>This specifies the IPMI LAN channel number used for BMC LAN. This varies by platform, and can be found in the platform technical specifications. For instance, Intel platforms usually use channels 1 &amp; 2 for onboard NICs, and channel 3 for optional RMM NICs. By default, ipmiutil lan scans all IPMI channels to find the first LAN channel for BMC LAN. To just list all IPMI channels to see what is available, use the string &#8216;list&#8217; instead of a LAN channel number. This will list the channels and exit.</p>
<dt>-M mac_addr</p>
<dd>This specifies the local MAC address to use for the BMC LAN on eth0. The format can be either 11:22:33:44:55:66 or 11-22-33-44-55-66. The default is to automatically obtain this from the Linux ifconfig.</p>
<dt>-N nodename</p>
<dd>Nodename or IP address of the remote target system. If a nodename is specified, IPMI LAN interface is used. Otherwise the local system management interface is used.</p>
<dt>-O</p>
<dd>Observe security. Disables the default null user and disable cipher 0.</p>
<dt>-P rmt_pswd</p>
<dd>Remote password for the nodename given. The default is a null password. Same as -R below.</p>
<dt>-Q</p>
<dd>Set the IPMI VLAN Priority. The default priority is 0.</p>
<dt>-R rmt_pswd</p>
<dd>Remote password for the nodename given. The default is a null password. Same as -P above.</p>
<dt>-S subnet</p>
<dd>This specifies the local subnet mask to use for the BMC LAN on eth0. The default is to automatically obtain this from the Linux ifconfig.</p>
<dt>-T</p>
<dd>Use a specified IPMI LAN Authentication Type: 0=None, 1=MD2, 2=MD5, 4=Straight Password, 5=OEM.</p>
<dt>-U rmt_user</p>
<dd>Remote username for the nodename given. The default is a null username.</p>
<dt>-V</p>
<dd>Use a specified IPMI LAN privilege level. 1=Callback level, 2=User level, 3=Operator level, 4=Administrator level (default), 5=OEM level.</p>
<dt>-X alert_mac_addr</p>
<dd>This specifies the SNMP Alert Destinations&#8217;s MAC address to use for the BMC LAN. The format can be either 11:22:33:44:55:66 or 11-22-33-44-55-66. The default is to attempt to obtain this from the Linux arp cache. This parameter is ignored if there is no Alert IP address.</p>
<dt>-Y</p>
<dd>Yes, do prompt the user for the IPMI LAN remote password. Alternatives for the password are -E or -P. </p>
</dl>
<h2>Examples</h2>
<p>To read existing settings:<br />
 ipmiutil lan -r To enable IPMI LAN with default settings detected, assuming shared MAC/IP:<br />
 ipmiutil lan -e To set up IPMI LAN for a unique IP address and set PEF SNMP Alerts:<br />
 ipmiutil lan -e -I 192.168.1.1 -A 192.168.1.10 To set the IPMI LAN password for the default user:<br />
 ipmiutil lan -e -p mypassword To disable access to the IPMI LAN channel:<br />
 ipmiutil lan -d </p>
<h2>Sample Pef Table</h2>
<p>These 11 PEF table entries are configured from the factory for various Intel Sahalee BMC systems, and will be applied as the defaults for a system with an empty PEF table:<br />
 PEF(01): 01 Temperature Sensor event &#8211; enabled for alert<br />
 01 c0 01 01 00 ff ff 01 ff 01 95 0a 00 00 00 00 00 00 00 00 00<br />
 PEF(02): 02 Voltage Sensor event &#8211; enabled for alert<br />
 02 c0 01 01 00 ff ff 02 ff 01 95 0a 00 00 00 00 00 00 00 00 00<br />
 PEF(03): 04 Fan Failure event &#8211; enabled for alert<br />
 03 c0 01 01 00 ff ff 04 ff 01 95 0a 00 00 00 00 00 00 00 00 00<br />
 PEF(04): 05 Chassis Intrusion event &#8211; enabled for alert<br />
 04 c0 01 01 00 ff ff 05 05 6f 01 00 00 00 00 00 00 00 00 00 00<br />
 PEF(05): 08 Power Supply Fault event &#8211; enabled for alert<br />
 05 c0 01 01 00 ff ff 08 ff 6f 06 00 00 00 00 00 00 00 00 00 00<br />
 PEF(06): 0c Memory ECC Error event &#8211; enabled for alert<br />
 06 c0 01 01 00 ff ff 0c 08 6f 02 00 00 00 00 00 00 00 00 00 00<br />
 PEF(07): 0f FRB Failure event &#8211; enabled for alert<br />
 07 c0 01 01 00 ff ff 0f 06 6f 01 00 00 00 00 00 00 00 00 00 00<br />
 PEF(08): 07 BIOS POST Error event &#8211; enabled for alert<br />
 08 c0 01 01 00 ff ff 07 ff 6f 1c 00 00 00 00 00 00 00 00 00 00<br />
 PEF(09): 13 Fatal NMI event &#8211; enabled for alert<br />
 09 c0 01 01 00 ff ff 13 ff 6f 3e 03 00 00 00 00 00 00 00 00 00<br />
 PEF(10): 23 Watchdog Timer Reset event &#8211; enabled for alert<br />
 0a c0 01 01 00 ff ff 23 03 6f 0e 00 00 00 00 00 00 00 00 00 00<br />
 PEF(11): 12 System Restart event &#8211; enabled for alert<br />
 0b c0 01 01 00 ff ff 12 ff 6f 02 00 00 00 00 00 00 00 00 00 00</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ipmiutil/">ipmiutil</a>(8) <a href="/docs/linux/man/8-ialarms/">ialarms</a>(8) <a href="/docs/linux/man/8-iconfig/">iconfig</a>(8) <a href="/docs/linux/man/8-icmd/">icmd</a>(8) <a href="/docs/linux/man/8-idiscover/">idiscover</a>(8) <a href="/docs/linux/man/8-ievents/">ievents</a>(8) <a href="/docs/linux/man/8-ifru/">ifru</a>(8) <a href="/docs/linux/man/8-igetevent/">igetevent</a>(8) <a href="/docs/linux/man/8-ihealth/">ihealth</a>(8) <a href="/docs/linux/man/8-ireset/">ireset</a>(8) <a href="/docs/linux/man/8-isel/">isel</a>(8) <a href="/docs/linux/man/8-isensor/">isensor</a>(8) <a href="/docs/linux/man/8-iserial/">iserial</a>(8) <a href="/docs/linux/man/8-isol/">isol</a>(8) <a href="/docs/linux/man/8-iwdt/">iwdt</a>(8) </p>
<h2>Warnings</h2>
<p>See <a rel="nofollow" href="http://ipmiutil.sourceforge.net/">http://ipmiutil.sourceforge.net/</a> for the latest version of ipmiutil and any bug fix list.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2009 Kontron America, Inc. </p>
<p> See the file COPYING in the distribution for more details regarding redistribution. </p>
<p> This utility is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY.</p>
<h2>Author</h2>
<p>Andy Cress &lt;arcress at users.sourceforge.net&gt;</p>
