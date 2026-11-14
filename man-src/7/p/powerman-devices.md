---
title: "powerman-devices(7)"
name: "powerman-devices"
section: "7"
letter: "p"
url: "/docs/linux/man/7-powerman-devices/"
description: "powerman-devices – Powerman Device Configuration Notes"
---

<p>powerman-devices &#8211; Powerman Device Configuration Notes</p>
<h2>Description</h2>
<p>Following are notes on configuring various remote power controllers and related equipment supported by PowerMan.</p>
<h2>Cyclades Ts-1000</h2>
<p>A cyclades TS-1000 configured so that PowerMan can connect to serial-port-based remote power control devices using telnet is set up as follows: Attach console cable between laptop running minicom and console port at 9600,8n1 and authenticate with default account: root/tslinux. Edit the following files (assumes no off-subnet routing or name service required):</p>
<dl>
<dt><i>/etc/portslave/portslave.conf</i></p>
<dd>
<pre>conf.eth_ip 192.168.54.151
conf.eth_mask 255.255.255.0 
conf.dhcp_client 0
#
all.speed 9600
all.datasize 8
all.stopbits 1
all.parity none
all.flow none
all.dcd 0
all.DTR_reset 1
all.protocol socket_server
all.authtype none
#all.ipno
all.socket_port 7001+
#
s1.tty ttyS1
s2.tty ttyS2
s3.tty ttyS3
s4.tty ttyS4
s5.tty ttyS5
s6.tty ttyS6
s7.tty ttyS7
s8.tty ttyS8
s9.tty ttyS9
s10.tty ttyS10
s11.tty ttyS11
s12.tty ttyS12
s13.tty ttyS13
s14.tty ttyS14
s15.tty ttyS15
s16.tty ttyS16</pre>
<dt><i>/etc/hostname</i></p>
<dd>cyclades-ts-test</p>
<dt><i>/etc/hosts</i></p>
<dd>
<pre>127.0.0.1 localhost
192.168.54.151 cycaldes-ts-test</pre>
<p>Next, run <code>signal_ras hup</code> and <code>saveconf</code> and finally, power cycle the unit. It should be possible to configure PowerMan to connect to hostname:7001 for port 1, hostname:7002 for port 2, etc..</dl>
<h2>BAYTECH RPC-3 (non-NC models) (network port 23)</h2>
<p>Attach console cable between laptop running minicom and console port at 9600,8n1. Main menu should display. From main menu, select 3)&#8230;Configuration, then set IP parameters. From Configuration menu, select 5)&#8230;Access, then disable command confirmation, set admin password to baytech, and enable prompt for password. Exit Access menu by typing return. From Configuration menu, select 6)&#8230;Outlets. Ensure that 1)&#8230;Outlet Status display is disabled, and 2)&#8230;Command Confirmation is disabled. Exit back to main menu by typing return twice, then answer Y to the Accept changes? prompt.</p>
<h2>BAYTECH RPC-28-NC (serial 9600,8n1)</h2>
<p>Attach console cable between laptop running minicom and console port at 9600,8n1. Type return to get RPC-28&gt; prompt. Type Help for a list of commands. Select config. Select 3)&#8230;Enable/Disable Confirmation and disable confirmation. Select 4)&#8230;Enable/Disable Status Menu and disable status menu</p>
<h2>LNXI ICEBOX V2 (network port 1010)</h2>
<p>Attach console cable between laptop running minicom and console port at 9600,8n1. Enter default password of icebox.</p>
<dl>
<dt><i>net ip 192.168.54.153</i></p>
<dd>Sets IP address.</p>
<dt><i>net mask 255.255.255.0</i></p>
<dd>Sets network mask</p>
<dt><i>net gw 192.168.54.254</i></p>
<dd>Set default gateway. Note: this may need to be set to an address in the same subnet as the ice box regardless of whether it is to be used or not.</p>
<dt><i>reboot</i></p>
<dd>Reboots the icebox.</dl>
<h2>LNXI ICEBOX V3 (network port 1010)</h2>
<p>Attach console cable between laptop running minicom and console port at 9600,8n1. Authenticate with default account admin/icebox. Configuration is the same as the V2 ICE BOX.</p>
<h2>APC MASTERSWITCH MODEL AP9606 (network port 23)</h2>
<p>Attach console cable between laptop running minicom and console port (may be labeled &#8220;advanced port&#8221;) at 2400,8n1. Press enter, then authenticate with default account apc/apc. Choose Network from main menu. Choose TCP/IP from Network menu, then diable BOOTP, and accept changes. Set the IP address, subnet mask, and default gateway, and accept changes. Pres ESC until the main menu appears, then select Logout.</p>
<h2>WTI RPS10 (serial 9600,8n1)</h2>
<p>Set address of box using the rotary dial on the back. The Master module must be set to address 0. Slave modules may be set to unique values from 1-9. The address corresponds to the plug name in the powerman.conf file. Setup switches on each module should be set to 9600 baud (sw1 down), 5 sec toggle delay (sw2 down), power up to previous state (sw3 down).</p>
<h2>WTI NPS (network port 23)</h2>
<p>Attach console cable between laptop running minicom and console port at 9600,8n1. Try password &quot;wti&quot; if prompted. Select /N &#8211; View/set network parameters, then set the IP address, subnet mask, and gateway. Select /G &#8211; General paramters, then disable command confirmation, enable command echo, and set disconnect timeout to the maximum value (30 minutes). Set password to &quot;wti&quot;.</p>
<h2>CYCLADES PM8 and PM8i (serial 9600,8n1)</h2>
<p>Attach console cable between laptop running minicom and serial port 9600,8n1. Press enter, then authenticate with default account admin/pm8. Run factory_defaults command. The PM8 can run in a mode where it can be daisy chained from a Cyclades terminal server. This mode is not yet supported by PowerMan.</p>
<h2>Sun ILOM</h2>
<p>The dedicated ILOM serial port (SER MGT RJ-45) runs at 9600,8n1 and the default login is root/changeme. Use a Sun/NETRA/Cisco RJ45 adapter to connect to Cyclades TS. The dedicated ILOM ethernet port (NET MGT RJ-45) can be configured for DHCP (the default) or static IP settings. To configure static IP via the ILOM serial port, run:</p>
<dl>
<dd>
<pre> cd /SP/network
 set pendingipdiscovery=static
 set pendingipaddress=xxx.xxx.xxx.xxx
 set pendingipnetmask=xxx.xxx.xxx.xxx
 set pendingipgateway=xxx.xxx.xxx.xxx
 set commitpending=true</pre>
<p>The ILOM network configuration can alternatively be set up via the system BIOS setup screen. Hit F2 during boot to access BIOS setup, go to the &quot;Advanced&quot; tab, select &quot;IPMI 2.0 configuration&quot; and &quot;set LAN configuration&quot;. Make your changes and commit them.</dl>
<h2>IPMI (via Ipmipower)</h2>
<p>IPMI based power control is supported via FreeIPMI&#8217;s <code>ipmipower.</code> It is configured by running <code>ipmipower</code> in coprocess mode in powerman.conf </p>
<p> Due to semantic differences between IPMI and traditional remote power control devices, some power control operations may not seem to work properly by default with <code>Powerman. </code> For example, several IPMI power control operations are allowed to return prior to the operation fully completing. A machine that has been powered off by IPMI may be later queried as being powered on. This is because IPMI may successfully return from a power off operation to the user, but the machine may elect to power itself off at a later time. In order to get around several of these issues, it is recommended that the user configure <code>ipmipower </code> with the <code>&#8211;wait-until-on</code> and <code>&#8211;wait-until-off</code> options. With these options set, <code>ipmipower</code> will behave more like traditional remote power control devices. </p>
<p> In order to hide IPMI usernames and passwords from <code><a href="/docs/linux/man/1-ps/">ps</a>(1), </code> it is also recommended that the user configure the username and password (and at your discretion, the above options) using the FreeIPMI configuration file and not in the powerman.conf file. Please see the <code>ipmipower</code> section of the <code><a href="/docs/linux/man/5-freeipmi-conf/">freeipmi.conf</a>(5)</code> manpage for more information. </p>
<p> Because IPMI usernames and passwords are sensitive, the default FreeIPMI configuration file is only readable and writable by root. This may conflict with the default <code>powermand</code> daemon settings, thus making the configuration file non-readable. Administrators may wish to run the <code>powermand</code> daemon as root or adjust the configuration file permissions as needed.</p>
<h2>HP iLO</h2>
<p>The &quot;hpilo&quot; script supports the Integrated Lights-Out management processor in HP ProLiant servers, including both rack-mount and blade servers. Configure the iLO to allow Telnet access on port 23, and add a user &quot;Admin&quot; with password &quot;Admin&quot;. You may have to reduce the minimum password length on the Administration/Access/Options tab of the web interface.</p>
<h2>Hp Mp</h2>
<p>The &quot;hpmp&quot; script supports the Management Processor in HP non-cellular, rack-mount Integrity servers. Configure the MP to allow Telnet access with the &quot;CM:SA&quot; command, and make sure there&#8217;s a user &quot;Admin&quot; with password &quot;Admin&quot;. If the MP enforces a minimum password length, you may have to use &quot;uc -all default&quot; to restore the default Admin/Admin user.</p>
<h2>HP MP (cellular)</h2>
<p>The &quot;hpmpcell&quot; script supports the Management Processor in HP mid-range cellular servers. Configure the MP to allow Telnet access with the &quot;CM:SA&quot; command, and make sure there&#8217;s a user &quot;Admin&quot; with password &quot;Admin&quot;.</p>
<h2>HP MP (Superdome)</h2>
<p>The &quot;hpmpdome&quot; script supports the Management Processor in HP Superdome servers. Configure the MP to allow Telnet access with the &quot;CM:SA&quot; command, and make sure there&#8217;s a user &quot;Admin&quot; with password &quot;Admin&quot;.</p>
<h2>HP MP (Integrity blades)</h2>
<p>The &quot;hpmpblade&quot; script supports the Management Processor in HP Integrity blade servers. Configure the MP to allow Telnet access with the &quot;CM:SA&quot; command, and make sure there&#8217;s a user &quot;Admin&quot; with password &quot;Admin&quot;.</p>
<h2>Origin</h2>
<p>PowerMan was originally developed by Andrew Uselton on LLNL&#8217;s Linux clusters. This software is open source and distributed under the terms of the GNU GPL.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-powerman/">powerman</a></code>(1), <code><a href="/docs/linux/man/8-powermand/">powermand</a></code>(8), <code><a href="/docs/linux/man/8-httppower/">httppower</a></code>(8), <code><a href="/docs/linux/man/8-plmpower/">plmpower</a></code>(8), <code><a href="/docs/linux/man/8-vpcd/">vpcd</a></code>(8), <code><a href="/docs/linux/man/5-powerman-conf/">powerman.conf</a></code>(5), <code><a href="/docs/linux/man/5-powerman-dev/">powerman.dev</a></code>(5), <code><a href="/docs/linux/man/7-powerman-devices/">powerman-devices</a></code>(7). <code><a rel="nofollow" href="http://sourceforge.net/projects/powerman">http://sourceforge.net/projects/powerman</a></code> </p>
