---
title: "ethtool(8)"
name: "ethtool"
section: "8"
letter: "e"
url: "/docs/linux/man/8-ethtool/"
description: "ethtool – query or control network driver and hardware settings"
---

<p>ethtool &#8211; query or control network driver and hardware settings</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ethtool</code> <i>devname</i></p>
<dt> <code>ethtool -h|&#8211;help</code></p>
<dt> <code>ethtool &#8211;version</code></p>
<dt> <code>ethtool -a|&#8211;show-pause</code> <i>devname</i></p>
<dt> <code>ethtool -A|&#8211;pause</code> <i>devname</i> [<code></p>
<dd>autoneg</code>&nbsp;<wbr><code>on</code>|<code>off</code>] [<code>rx</code>&nbsp;<wbr><code>on</code>|<code>off</code>] [<code>tx</code>&nbsp;<wbr><code>on</code>|<code>off</code>]</p>
<dt> <code>ethtool -c|&#8211;show-coalesce</code> <i>devname</i></p>
<dt> <code>ethtool -C|&#8211;coalesce</code> <i>devname</i> [<code></p>
<dd>adaptive-rx</code>&nbsp;<wbr><code>on</code>|<code>off</code>] [<code>adaptive-tx</code>&nbsp;<wbr><code>on</code>|<code>off</code>] [<code>rx-usecs</code>&nbsp;<wbr><i>N</i>] [<code>rx-frames</code>&nbsp;<wbr><i>N</i>] [<code>rx-usecs-irq</code>&nbsp;<wbr><i>N</i>] [<code>rx-frames-irq</code>&nbsp;<wbr><i>N</i>] [<code>tx-usecs</code>&nbsp;<wbr><i>N</i>] [<code>tx-frames</code>&nbsp;<wbr><i>N</i>] [<code>tx-usecs-irq</code>&nbsp;<wbr><i>N</i>] [<code>tx-frames-irq</code>&nbsp;<wbr><i>N</i>] [<code>stats-block-usecs</code>&nbsp;<wbr><i>N</i>] [<code>pkt-rate-low</code>&nbsp;<wbr><i>N</i>] [<code>rx-usecs-low</code>&nbsp;<wbr><i>N</i>] [<code>rx-frames-low</code>&nbsp;<wbr><i>N</i>] [<code>tx-usecs-low</code>&nbsp;<wbr><i>N</i>] [<code>tx-frames-low</code>&nbsp;<wbr><i>N</i>] [<code>pkt-rate-high</code>&nbsp;<wbr><i>N</i>] [<code>rx-usecs-high</code>&nbsp;<wbr><i>N</i>] [<code>rx-frames-high</code>&nbsp;<wbr><i>N</i>] [<code>tx-usecs-high</code>&nbsp;<wbr><i>N</i>] [<code>tx-frames-high</code>&nbsp;<wbr><i>N</i>] [<code>sample-interval</code>&nbsp;<wbr><i>N</i>]</p>
<dt> <code>ethtool -g|&#8211;show-ring</code> <i>devname</i></p>
<dt> <code>ethtool -G|&#8211;set-ring</code> <i>devname</i> [<code></p>
<dd>rx</code>&nbsp;<wbr><i>N</i>] [<code>rx-mini</code>&nbsp;<wbr><i>N</i>] [<code>rx-jumbo</code>&nbsp;<wbr><i>N</i>] [<code>tx</code>&nbsp;<wbr><i>N</i>]</p>
<dt> <code>ethtool -i|&#8211;driver</code> <i>devname</i></p>
<dt> <code>ethtool -d|&#8211;register-dump</code> <i>devname</i> [<code></p>
<dd>raw</code>&nbsp;<wbr><code>on</code>|<code>off</code>] [<code>hex</code>&nbsp;<wbr><code>on</code>|<code>off</code>] [<code>file</code> <i>name</i>]</p>
<dt> <code>ethtool -e|&#8211;eeprom-dump</code> <i>devname</i> [<code></p>
<dd>raw</code>&nbsp;<wbr><code>on</code>|<code>off</code>] [<code>offset</code>&nbsp;<wbr><i>N</i>] [<code>length</code>&nbsp;<wbr><i>N</i>]</p>
<dt> <code>ethtool -E|&#8211;change-eeprom</code> <i>devname</i> [<code></p>
<dd>magic</code>&nbsp;<wbr><i>N</i>] [<code>offset</code>&nbsp;<wbr><i>N</i>] [<code>length</code>&nbsp;<wbr><i>N</i>] [<code>value</code>&nbsp;<wbr><i>N</i>]</p>
<dt> <code>ethtool -k|&#8211;show-features|&#8211;show-offload</code> <i>devname</i></p>
<dt> <code>ethtool -K|&#8211;features|&#8211;offload</code> <i>devname feature</i> <code></p>
<dd>on</code>|<code>off</code> &#8230;</p>
<dt> <code>ethtool -p|&#8211;identify</code> <i>devname</i> [<i>N</i>]</p>
<dt> <code>ethtool -P|&#8211;show-permaddr</code> <i>devname</i></p>
<dt> <code>ethtool -r|&#8211;negotiate</code> <i>devname</i></p>
<dt> <code>ethtool -S|&#8211;statistics</code> <i>devname</i></p>
<dt> <code>ethtool &#8211;phy-statistics</code> <i>devname</i></p>
<dt> <code>ethtool -t|&#8211;test</code> <i>devname</i> [<code>offline</code>|<code>online</code>|<code>external_lb</code>]</p>
<dt> <code>ethtool -s</code> <i>devname</i> [<code></p>
<dd>speed</code>&nbsp;<wbr><i>N</i>] [<code>duplex</code>&nbsp;<wbr><code>half</code>|<code>full</code>] [<code>port</code>&nbsp;<wbr><code>tp</code>|<code>aui</code>|<code>bnc</code>|<code>mii</code>] [<code>mdix</code>&nbsp;<wbr><code>auto</code>|<code>on</code>|<code>off</code>] [<code>autoneg</code>&nbsp;<wbr><code>on</code>|<code>off</code>] [<code>advertise</code>&nbsp;<wbr><i>N</i>] [<code>phyad</code>&nbsp;<wbr><i>N</i>] [<code>xcvr</code>&nbsp;<wbr><code>internal</code>|<code>external</code>] [<code>wol</code>&nbsp;<wbr><code>p</code>|<code>u</code>|<code>m</code>|<code>b</code>|<code>a</code>|<code>g</code>|<code>s</code>|<code>d</code>&#8230;] [<code>sopass</code>&nbsp;<wbr><i>xx</i><code>:</code><i>yy</i><code>:</code><i>zz</i><code>:</code><i>aa</i><code>:</code><i>bb</i><code>:</code><i>cc</i>] [<code>msglvl</code> <i>N</i>&nbsp;<wbr>| <code>msglvl</code><i>&nbsp;<wbr>type</i> <code>on</code>|<code>off</code> &#8230;]</p>
<dt> <code>ethtool -n|-u|&#8211;show-nfc|&#8211;show-ntuple</code> <i>devname</i> [&nbsp;<wbr><code>rx-flow-hash</code>&nbsp;<wbr><code>tcp4</code>|<code>udp4</code>|<code>ah4</code>|<code>esp4</code>|<code>sctp4</code>|<code>tcp6</code>|<code>udp6</code>|<code>ah6</code>|<code>esp6</code>|<code>sctp6</code><code>&nbsp;<wbr>|</code></p>
<dd><code>rule</code><i>&nbsp;<wbr>N</i> ]</p>
<dt> <code>ethtool -N|-U|&#8211;config-nfc|&#8211;config-ntuple</code> <i>devname</i> <code>rx-flow-hash</code>&nbsp;<wbr><code>tcp4</code>|<code>udp4</code>|<code>ah4</code>|<code>esp4</code>|<code>sctp4</code>|<code>tcp6</code>|<code>udp6</code>|<code>ah6</code>|<code>esp6</code>|<code>sctp6</code><code>&nbsp;<wbr>:</code><code>m</code>|<code>v</code>|<code>t</code>|<code>s</code>|<code>d</code>|<code>f</code>|<code>n</code>|<code>r</code>&#8230;<code>&nbsp;<wbr>|</code></p>
<dd><code>flow-type <code>ether</code>|<code>ip4</code>|<code>tcp4</code>|<code>udp4</code>|<code>sctp4</code>|<code>ah4</code>|<code>esp4</code>|<code>ip6</code>|<code>tcp6</code>|<code>udp6</code>|<code>ah6</code>|<code>esp6</code>|<code>sctp6</code></code> [<code>src</code>&nbsp;<wbr><i>xx</i><code>:</code><i>yy</i><code>:</code><i>zz</i><code>:</code><i>aa</i><code>:</code><i>bb</i><code>:</code><i>cc</i>&nbsp;<wbr>[<code>m</code>&nbsp;<wbr><i>xx</i><code>:</code><i>yy</i><code>:</code><i>zz</i><code>:</code><i>aa</i><code>:</code><i>bb</i><code>:</code><i>cc</i>]] [<code>dst</code>&nbsp;<wbr><i>xx</i><code>:</code><i>yy</i><code>:</code><i>zz</i><code>:</code><i>aa</i><code>:</code><i>bb</i><code>:</code><i>cc</i>&nbsp;<wbr>[<code>m</code>&nbsp;<wbr><i>xx</i><code>:</code><i>yy</i><code>:</code><i>zz</i><code>:</code><i>aa</i><code>:</code><i>bb</i><code>:</code><i>cc</i>]] [<code></p>
<dd>proto</code>&nbsp;<wbr><i>N</i>&nbsp;<wbr>[<code>m</code>&nbsp;<wbr><i>N</i>]] [<code>src-ip</code>&nbsp;<wbr><i>ip-address</i>&nbsp;<wbr>[<code>m</code>&nbsp;<wbr><i>ip-address</i>]] [<code>dst-ip</code>&nbsp;<wbr><i>ip-address</i>&nbsp;<wbr>[<code>m</code>&nbsp;<wbr><i>ip-address</i>]] [<code>tos</code>&nbsp;<wbr><i>N</i>&nbsp;<wbr>[<code>m</code>&nbsp;<wbr><i>N</i>]] [<code>tclass</code>&nbsp;<wbr><i>N</i>&nbsp;<wbr>[<code>m</code>&nbsp;<wbr><i>N</i>]] [<code>l4proto</code>&nbsp;<wbr><i>N</i>&nbsp;<wbr>[<code>m</code>&nbsp;<wbr><i>N</i>]] [<code>src-port</code>&nbsp;<wbr><i>N</i>&nbsp;<wbr>[<code>m</code>&nbsp;<wbr><i>N</i>]] [<code>dst-port</code>&nbsp;<wbr><i>N</i>&nbsp;<wbr>[<code>m</code>&nbsp;<wbr><i>N</i>]] [<code>spi</code>&nbsp;<wbr><i>N</i>&nbsp;<wbr>[<code>m</code>&nbsp;<wbr><i>N</i>]] [<code>l4data</code>&nbsp;<wbr><i>N</i>&nbsp;<wbr>[<code>m</code>&nbsp;<wbr><i>N</i>]] [<code>vlan-etype</code>&nbsp;<wbr><i>N</i>&nbsp;<wbr>[<code>m</code>&nbsp;<wbr><i>N</i>]] [<code>vlan</code>&nbsp;<wbr><i>N</i>&nbsp;<wbr>[<code>m</code>&nbsp;<wbr><i>N</i>]] [<code>user-def</code>&nbsp;<wbr><i>N</i>&nbsp;<wbr>[<code>m</code>&nbsp;<wbr><i>N</i>]] [<code>dst-mac</code>&nbsp;<wbr><i>xx</i><code>:</code><i>yy</i><code>:</code><i>zz</i><code>:</code><i>aa</i><code>:</code><i>bb</i><code>:</code><i>cc</i>&nbsp;<wbr>[<code>m</code>&nbsp;<wbr><i>xx</i><code>:</code><i>yy</i><code>:</code><i>zz</i><code>:</code><i>aa</i><code>:</code><i>bb</i><code>:</code><i>cc</i>]] [<code>action</code>&nbsp;<wbr><i>N</i>] [<code>loc</code>&nbsp;<wbr><i>N</i>] |<br />
 <code>delete</code><i>&nbsp;<wbr>N</i></p>
<dt> <code>ethtool -w|&#8211;get-dump</code> <i>devname</i> [<code>data</code> <i>filename</i>]</p>
<dt> <code>ethtool -W|&#8211;set-dump</code> <i>devname N</i></p>
<dt> <code>ethtool -T|&#8211;show-time-stamping</code> <i>devname</i></p>
<dt> <code>ethtool -x|&#8211;show-rxfh-indir|&#8211;show-rxfh</code> <i>devname</i></p>
<dt> <code>ethtool -X|&#8211;set-rxfh-indir|&#8211;rxfh</code> <i>devname</i> [<code>hkey</code>&nbsp;<wbr><i>xx</i><code>:</code><i>yy</i><code>:</code><i>zz</i><code>:</code><i>aa</i><code>:</code><i>bb</i><code>:</code><i>cc</i>:&#8230;] [&nbsp;<wbr><code>equal</code> <i>N</i>&nbsp;<wbr>| <code>weight&nbsp;<wbr></code><i>W0</i> <i>W1</i> &#8230; |<code>&nbsp;<wbr>default</code>&nbsp;<wbr>]</p>
<dt> <code>ethtool -f|&#8211;flash</code> <i>devname file</i> [<i>N</i>]</p>
<dt> <code>ethtool -l|&#8211;show-channels</code> <i>devname</i></p>
<dt> <code>ethtool -L|&#8211;set-channels</code> <i>devname</i> [<code></p>
<dd>rx</code>&nbsp;<wbr><i>N</i>] [<code>tx</code>&nbsp;<wbr><i>N</i>] [<code>other</code>&nbsp;<wbr><i>N</i>] [<code>combined</code>&nbsp;<wbr><i>N</i>]</p>
<dt> <code>ethtool -m|&#8211;dump-module-eeprom|&#8211;module-info</code> <i>devname</i> [<code></p>
<dd>raw</code>&nbsp;<wbr><code>on</code>|<code>off</code>] [<code>hex</code>&nbsp;<wbr><code>on</code>|<code>off</code>] [<code>offset</code>&nbsp;<wbr><i>N</i>] [<code>length</code>&nbsp;<wbr><i>N</i>]</p>
<dt> <code>ethtool &#8211;show-priv-flags</code> <i>devname</i></p>
<dt> <code>ethtool &#8211;set-priv-flags</code> <i>devname flag</i> <code></p>
<dd>on</code>|<code>off</code> &#8230;</p>
<dt> <code>ethtool &#8211;show-eee</code> <i>devname</i></p>
<dt> <code>ethtool &#8211;set-eee</code> <i>devname</i> [<code></p>
<dd>eee</code>&nbsp;<wbr><code>on</code>|<code>off</code>] [<code>tx-lpi</code>&nbsp;<wbr><code>on</code>|<code>off</code>] [<code>tx-timer</code>&nbsp;<wbr><i>N</i>] [<code>advertise</code>&nbsp;<wbr><i>N</i>] </p>
<h2>Description</h2>
<p><code>ethtool</code> is used to query and control network device driver and hardware settings, particularly for wired Ethernet devices. <i>devname</i> is the name of the network device on which ethtool should operate. </p>
<h2>Options</h2>
<p><code>ethtool</code> with a single argument specifying the device name prints current settings of the specified device.</p>
<dl>
<dt><code>-h &#8211;help</code></p>
<dd>Shows a short help message.</p>
<dt><code>&#8211;version</code></p>
<dd>Shows the ethtool version number.</p>
<dt><code>-a &#8211;show-pause</code></p>
<dd>Queries the specified Ethernet device for pause parameter information.</p>
<dt><code>-A &#8211;pause</code></p>
<dd>Changes the pause parameters of the specified Ethernet device.</p>
<dl>
<dd>
<dl>
<dt> <code>autoneg</code>&nbsp;<wbr><code>on</code>|<code>off</code></p>
<dd>Specifies whether pause autonegotiation should be enabled.</p>
<dt> <code>rx</code>&nbsp;<wbr><code>on</code>|<code>off</code></p>
<dd>Specifies whether RX pause should be enabled.</p>
<dt> <code>tx</code>&nbsp;<wbr><code>on</code>|<code>off</code></p>
<dd>Specifies whether TX pause should be enabled.</dl>
</dl>
<dt><code>-c &#8211;show-coalesce</code></p>
<dd>Queries the specified network device for coalescing information.</p>
<dt><code>-C &#8211;coalesce</code></p>
<dd>Changes the coalescing settings of the specified network device.</p>
<dt><code>-g &#8211;show-ring</code></p>
<dd>Queries the specified network device for rx/tx ring parameter information.</p>
<dt><code>-G &#8211;set-ring</code></p>
<dd>Changes the rx/tx ring parameters of the specified network device.</p>
<dl>
<dd>
<dl>
<dt><code>rx</code><i>&nbsp;<wbr>N</i></p>
<dd>Changes the number of ring entries for the Rx ring.</p>
<dt><code>rx-mini</code><i>&nbsp;<wbr>N</i></p>
<dd>Changes the number of ring entries for the Rx Mini ring.</p>
<dt><code>rx-jumbo</code><i>&nbsp;<wbr>N</i></p>
<dd>Changes the number of ring entries for the Rx Jumbo ring.</p>
<dt><code>tx</code><i>&nbsp;<wbr>N</i></p>
<dd>Changes the number of ring entries for the Tx ring.</dl>
</dl>
<dt><code>-i &#8211;driver</code></p>
<dd>Queries the specified network device for associated driver information.</p>
<dt><code>-d &#8211;register-dump</code></p>
<dd>Retrieves and prints a register dump for the specified network device. The register format for some devices is known and decoded others are printed in hex. When <i>raw </i> is enabled, then ethtool dumps the raw register data to stdout. If <i>file</i> is specified, then use contents of previous raw register dump, rather than reading from the device.</p>
<dt><code>-e &#8211;eeprom-dump</code></p>
<dd>Retrieves and prints an EEPROM dump for the specified network device. When raw is enabled, then it dumps the raw EEPROM data to stdout. The length and offset parameters allow dumping certain portions of the EEPROM. Default is to dump the entire EEPROM.</p>
<dl>
<dd>
<dl>
<dt><code>raw</code><i>&nbsp;<wbr>on|off</i></p>
<dd>
<dt><code>offset</code><i>&nbsp;<wbr>N</i></p>
<dd>
<dt><code>length</code><i>&nbsp;<wbr>N</i></p>
<dd></dl>
</dl>
<dt><code>-E &#8211;change-eeprom</code></p>
<dd>If value is specified, changes EEPROM byte for the specified network device. offset and value specify which byte and it&#8217;s new value. If value is not specified, stdin is read and written to the EEPROM. The length and offset parameters allow writing to certain portions of the EEPROM. Because of the persistent nature of writing to the EEPROM, a device-specific magic key must be specified to prevent the accidental writing to the EEPROM.</p>
<dt><code>-k &#8211;show-features &#8211;show-offload</code></p>
<dd>Queries the specified network device for the state of protocol offload and other features.</p>
<dt><code>-K &#8211;features &#8211;offload</code></p>
<dd>Changes the offload parameters and other features of the specified network device. The following feature names are built-in and others may be defined by the kernel.</p>
<dl>
<dd>
<dl>
<dt> <code>rx</code>&nbsp;<wbr><code>on</code>|<code>off</code></p>
<dd>Specifies whether RX checksumming should be enabled.</p>
<dt> <code>tx</code>&nbsp;<wbr><code>on</code>|<code>off</code></p>
<dd>Specifies whether TX checksumming should be enabled.</p>
<dt> <code>sg</code>&nbsp;<wbr><code>on</code>|<code>off</code></p>
<dd>Specifies whether scatter-gather should be enabled.</p>
<dt> <code>tso</code>&nbsp;<wbr><code>on</code>|<code>off</code></p>
<dd>Specifies whether TCP segmentation offload should be enabled.</p>
<dt> <code>ufo</code>&nbsp;<wbr><code>on</code>|<code>off</code></p>
<dd>Specifies whether UDP fragmentation offload should be enabled</p>
<dt> <code>gso</code>&nbsp;<wbr><code>on</code>|<code>off</code></p>
<dd>Specifies whether generic segmentation offload should be enabled</p>
<dt> <code>gro</code>&nbsp;<wbr><code>on</code>|<code>off</code></p>
<dd>Specifies whether generic receive offload should be enabled</p>
<dt> <code>lro</code>&nbsp;<wbr><code>on</code>|<code>off</code></p>
<dd>Specifies whether large receive offload should be enabled</p>
<dt> <code>rxvlan</code>&nbsp;<wbr><code>on</code>|<code>off</code></p>
<dd>Specifies whether RX VLAN acceleration should be enabled</p>
<dt> <code>txvlan</code>&nbsp;<wbr><code>on</code>|<code>off</code></p>
<dd>Specifies whether TX VLAN acceleration should be enabled</p>
<dt> <code>ntuple</code>&nbsp;<wbr><code>on</code>|<code>off</code></p>
<dd>Specifies whether Rx ntuple filters and actions should be enabled</p>
<dt> <code>rxhash</code>&nbsp;<wbr><code>on</code>|<code>off</code></p>
<dd>Specifies whether receive hashing offload should be enabled</dl>
</dl>
<dt><code>-p &#8211;identify</code></p>
<dd>Initiates adapter-specific action intended to enable an operator to easily identify the adapter by sight. Typically this involves blinking one or more LEDs on the specific network port.</p>
<dl>
<dd>
<dl>
<dt> [&nbsp;<wbr><i>N</i>]</p>
<dd>Length of time to perform phys-id, in seconds.</dl>
</dl>
<dt><code>-P &#8211;show-permaddr</code></p>
<dd>Queries the specified network device for permanent hardware address.</p>
<dt><code>-r &#8211;negotiate</code></p>
<dd>Restarts auto-negotiation on the specified Ethernet device, if auto-negotiation is enabled.</p>
<dt><code>-S &#8211;statistics</code></p>
<dd>Queries the specified network device for NIC- and driver-specific statistics.</p>
<dt><code>&#8211;phy-statistics</code></p>
<dd>Queries the specified network device for PHY specific statistics.</p>
<dt><code>-t &#8211;test</code></p>
<dd>Executes adapter selftest on the specified network device. Possible test modes are:</p>
<dl>
<dd>
<dl>
<dt><code>offline</code></p>
<dd>Perform full set of tests, possibly interrupting normal operation during the tests,</p>
<dt><code>online</code></p>
<dd>Perform limited set of tests, not interrupting normal operation,</p>
<dt><code>external_lb</code></p>
<dd>Perform full set of tests, as for <code>offline</code>, and additionally an external-loopback test.</dl>
</dl>
<dt><code>-s &#8211;change</code></p>
<dd>Allows changing some or all settings of the specified network device. All following options only apply if <code>-s</code> was specified.</p>
<dl>
<dd>
<dl>
<dt><code>speed</code><i>&nbsp;<wbr>N</i></p>
<dd>Set speed in Mb/s. <code>ethtool</code> with just the device name as an argument will show you the supported device speeds.</p>
<dt> <code>duplex</code>&nbsp;<wbr><code>half</code>|<code>full</code></p>
<dd>Sets full or half duplex mode.</p>
<dt> <code>port</code>&nbsp;<wbr><code>tp</code>|<code>aui</code>|<code>bnc</code>|<code>mii</code></p>
<dd>Selects device port.</p>
<dt> <code>mdix</code>&nbsp;<wbr><code>auto</code>|<code>on</code>|<code>off</code></p>
<dd>Selects MDI-X mode for port. May be used to override the automatic detection feature of most adapters. An argument of <code>auto</code> means automatic detection of MDI status, <code>on</code> forces MDI-X (crossover) mode, while <code>off</code> means MDI (straight through) mode. The driver should guarantee that this command takes effect immediately, and if necessary may reset the link to cause the change to take effect.</p>
<dt> <code>autoneg</code>&nbsp;<wbr><code>on</code>|<code>off</code></p>
<dd>Specifies whether autonegotiation should be enabled. Autonegotiation is enabled by default, but in some network devices may have trouble with it, so you can disable it if really necessary.</p>
<dt><code>advertise</code><i>&nbsp;<wbr>N</i></p>
<dd>Sets the speed and duplex advertised by autonegotiation. The argument is a hexadecimal value using one or a combination of the following values: </p>
<table>
<tr VALIGN=top>
<td><code>0x001</code></td>
<td>10baseT Half</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>0x002</code></td>
<td>10baseT Full</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>0x004</code></td>
<td>100baseT Half</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>0x008</code></td>
<td>100baseT Full</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>0x010</code></td>
<td>1000baseT Half</td>
<td><code>(not supported by IEEE standards)</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>0x020</code></td>
<td>1000baseT Full</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>0x20000</code></td>
<td>1000baseKX Full</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>0x20000000000</code></td>
<td>1000baseX Full</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>0x8000</code></td>
<td>2500baseX Full</td>
<td><code>(not supported by IEEE standards)</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>0x1000</code></td>
<td>10000baseT Full</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>0x40000</code></td>
<td>10000baseKX4 Full</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>0x80000</code></td>
<td>10000baseKR Full</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>0x40000000000</code></td>
<td>10000baseCR Full</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>0x80000000000</code></td>
<td>10000baseSR Full</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>0x100000000000</code></td>
<td>10000baseLR Full</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>0x200000000000</code></td>
<td>10000baseLRM Full</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>0x400000000000</code></td>
<td>10000baseER Full</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>0x200000</code></td>
<td>20000baseMLD2 Full</td>
<td><code>(not supported by IEEE standards)</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>0x400000</code></td>
<td>20000baseKR2 Full</td>
<td><code>(not supported by IEEE standards)</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>0x80000000</code></td>
<td>25000baseCR Full</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>0x100000000</code></td>
<td>25000baseKR Full</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>0x200000000</code></td>
<td>25000baseSR Full</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>0x800000</code></td>
<td>40000baseKR4 Full</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>0x1000000</code></td>
<td>40000baseCR4 Full</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>0x2000000</code></td>
<td>40000baseSR4 Full</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>0x4000000</code></td>
<td>40000baseLR4 Full</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>0x400000000</code></td>
<td>50000baseCR2 Full</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>0x800000000</code></td>
<td>50000baseKR2 Full</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>0x10000000000</code></td>
<td>50000baseSR2 Full</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>0x1000000000</code></td>
<td>100000baseKR4 Full</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>0x2000000000</code></td>
<td>100000baseSR4 Full</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>0x4000000000</code></td>
<td>100000baseCR4 Full</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>0x8000000000</code></td>
<td>100000baseLR4_ER4 Full</td>
<td>
</td>
</tr>
</table>
<dt><code>phyad</code><i>&nbsp;<wbr>N</i></p>
<dd>PHY address.</p>
<dt> <code>xcvr</code>&nbsp;<wbr><code>internal</code>|<code>external</code></p>
<dd>Selects transceiver type. Currently only internal and external can be specified, in the future further types might be added.</p>
<dt><code>wol</code>&nbsp;<wbr><code>p</code>|<code>u</code>|<code>m</code>|<code>b</code>|<code>a</code>|<code>g</code>|<code>s</code>|<code>d</code>&#8230;</p>
<dd>Sets Wake-on-LAN options. Not all devices support this. The argument to this option is a string of characters specifying which options to enable. </p>
<table>
<tr VALIGN=top>
<td><code>p</code></td>
<td>Wake on PHY activity
</td>
</tr>
<tr VALIGN=top>
<td><code>u</code></td>
<td>Wake on unicast messages
</td>
</tr>
<tr VALIGN=top>
<td><code>m</code></td>
<td>Wake on multicast messages
</td>
</tr>
<tr VALIGN=top>
<td><code>b</code></td>
<td>Wake on broadcast messages
</td>
</tr>
<tr VALIGN=top>
<td><code>a</code></td>
<td>Wake on ARP
</td>
</tr>
<tr VALIGN=top>
<td><code>g</code></td>
<td>Wake on MagicPacket&trade;
</td>
</tr>
<tr VALIGN=top>
<td><code>s</code></td>
<td>Enable SecureOn&trade; password for MagicPacket&trade;
</td>
</tr>
<tr VALIGN=top>
<td><code>d</code></td>
<td> Disable (wake on nothing). This option clears all previous options.
</td>
</tr>
</table>
<dt><code>sopass <i>xx</i><code>:</code><i>yy</i><code>:</code><i>zz</i><code>:</code><i>aa</i><code>:</code><i>bb</i><code>:</code><i>cc</i></code></p>
<dd>Sets the SecureOn&trade; password. The argument to this option must be 6 bytes in Ethernet MAC hex format (<i>xx</i><code>:</code><i>yy</i><code>:</code><i>zz</i><code>:</code><i>aa</i><code>:</code><i>bb</i><code>:</code><i>cc</i>).</dl>
<p> <code>msglvl</code><i>&nbsp;<wbr>N</i><br />
 <code>msglvl</code><i>&nbsp;<wbr>type</i> <code>on</code>|<code>off</code> &#8230;</p>
<dl>
<dd>Sets the driver message type flags by name or number. <i>type</i> names the type of message to enable or disable; <i>N</i> specifies the new flags numerically. The defined type names and numbers are: </p>
<table>
<tr VALIGN=top>
<td><code>drv</code></td>
<td>0x0001 General driver status</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>probe</code></td>
<td>0x0002 Hardware probing</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>link</code></td>
<td>0x0004 Link state</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>timer</code></td>
<td>0x0008 Periodic status check</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>ifdown</code></td>
<td>0x0010 Interface being brought down</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>ifup</code></td>
<td>0x0020 Interface being brought up</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>rx_err</code></td>
<td>0x0040 Receive error</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>tx_err</code></td>
<td>0x0080 Transmit error</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>tx_queued</code></td>
<td>0x0100 Transmit queueing</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>intr</code></td>
<td>0x0200 Interrupt handling</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>tx_done</code></td>
<td>0x0400 Transmit completion</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>rx_status</code></td>
<td>0x0800 Receive completion</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>pktdata</code></td>
<td>0x1000 Packet contents</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>hw</code></td>
<td>0x2000 Hardware status</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>wol</code></td>
<td>0x4000 Wake-on-LAN status</td>
<td>
</td>
</tr>
</table>
<p> The precise meanings of these type flags differ between drivers.</dl>
</dl>
<dt><code>-n -u &#8211;show-nfc &#8211;show-ntuple</code></p>
<dd>Retrieves receive network flow classification options or rules.</p>
<dl>
<dd>
<dl>
<dt><code>rx-flow-hash</code>&nbsp;<wbr><code>tcp4</code>|<code>udp4</code>|<code>ah4</code>|<code>esp4</code>|<code>sctp4</code>|<code>tcp6</code>|<code>udp6</code>|<code>ah6</code>|<code>esp6</code>|<code>sctp6</code></p>
<dd>Retrieves the hash options for the specified flow type. </p>
<table>
<tr VALIGN=top>
<td><code>tcp4</code></td>
<td>TCP over IPv4
</td>
</tr>
<tr VALIGN=top>
<td><code>udp4</code></td>
<td>UDP over IPv4
</td>
</tr>
<tr VALIGN=top>
<td><code>ah4</code></td>
<td>IPSEC AH over IPv4
</td>
</tr>
<tr VALIGN=top>
<td><code>esp4</code></td>
<td>IPSEC ESP over IPv4
</td>
</tr>
<tr VALIGN=top>
<td><code>sctp4</code></td>
<td>SCTP over IPv4
</td>
</tr>
<tr VALIGN=top>
<td><code>tcp6</code></td>
<td>TCP over IPv6
</td>
</tr>
<tr VALIGN=top>
<td><code>udp6</code></td>
<td>UDP over IPv6
</td>
</tr>
<tr VALIGN=top>
<td><code>ah6</code></td>
<td>IPSEC AH over IPv6
</td>
</tr>
<tr VALIGN=top>
<td><code>esp6</code></td>
<td>IPSEC ESP over IPv6
</td>
</tr>
<tr VALIGN=top>
<td><code>sctp6</code></td>
<td>SCTP over IPv6
</td>
</tr>
</table>
<dt><code>rule</code><i>&nbsp;<wbr>N</i></p>
<dd>Retrieves the RX classification rule with the given ID.</dl>
</dl>
<dt><code>-N -U &#8211;config-nfc &#8211;config-ntuple</code></p>
<dd>Configures receive network flow classification options or rules.</p>
<dl>
<dd>
<dl>
<dt><code>rx-flow-hash</code>&nbsp;<wbr><code>tcp4</code>|<code>udp4</code>|<code>ah4</code>|<code>esp4</code>|<code>sctp4</code>|<code>tcp6</code>|<code>udp6</code>|<code>ah6</code>|<code>esp6</code>|<code>sctp6</code><code>:</code><code>m</code>|<code>v</code>|<code>t</code>|<code>s</code>|<code>d</code>|<code>f</code>|<code>n</code>|<code>r</code>&#8230;</p>
<dd>Configures the hash options for the specified flow type. </p>
<table>
<tr VALIGN=top>
<td><code>m</code></td>
<td>Hash on the Layer 2 destination address of the rx packet.
</td>
</tr>
<tr VALIGN=top>
<td><code>v</code></td>
<td>Hash on the VLAN tag of the rx packet.
</td>
</tr>
<tr VALIGN=top>
<td><code>t</code></td>
<td>Hash on the Layer 3 protocol field of the rx packet.
</td>
</tr>
<tr VALIGN=top>
<td><code>s</code></td>
<td>Hash on the IP source address of the rx packet.
</td>
</tr>
<tr VALIGN=top>
<td><code>d</code></td>
<td>Hash on the IP destination address of the rx packet.
</td>
</tr>
<tr VALIGN=top>
<td><code>f</code></td>
<td>Hash on bytes 0 and 1 of the Layer 4 header of the rx packet.
</td>
</tr>
<tr VALIGN=top>
<td><code>n</code></td>
<td>Hash on bytes 2 and 3 of the Layer 4 header of the rx packet.
</td>
</tr>
<tr VALIGN=top>
<td><code>r</code></td>
<td> Discard all packets of this flow type. When this option is set, all other options are ignored.
</td>
</tr>
</table>
<dt><code>flow-type <code>ether</code>|<code>ip4</code>|<code>tcp4</code>|<code>udp4</code>|<code>sctp4</code>|<code>ah4</code>|<code>esp4</code>|<code>ip6</code>|<code>tcp6</code>|<code>udp6</code>|<code>ah6</code>|<code>esp6</code>|<code>sctp6</code></code></p>
<dd>Inserts or updates a classification rule for the specified flow type. </p>
<table>
<tr VALIGN=top>
<td><code>ether</code></td>
<td>Ethernet
</td>
</tr>
<tr VALIGN=top>
<td><code>ip4</code></td>
<td>Raw IPv4
</td>
</tr>
<tr VALIGN=top>
<td><code>tcp4</code></td>
<td>TCP over IPv4
</td>
</tr>
<tr VALIGN=top>
<td><code>udp4</code></td>
<td>UDP over IPv4
</td>
</tr>
<tr VALIGN=top>
<td><code>sctp4</code></td>
<td>SCTP over IPv4
</td>
</tr>
<tr VALIGN=top>
<td><code>ah4</code></td>
<td>IPSEC AH over IPv4
</td>
</tr>
<tr VALIGN=top>
<td><code>esp4</code></td>
<td>IPSEC ESP over IPv4
</td>
</tr>
<tr VALIGN=top>
<td><code>ip6</code></td>
<td>Raw IPv6
</td>
</tr>
<tr VALIGN=top>
<td><code>tcp6</code></td>
<td>TCP over IPv6
</td>
</tr>
<tr VALIGN=top>
<td><code>udp6</code></td>
<td>UDP over IPv6
</td>
</tr>
<tr VALIGN=top>
<td><code>sctp6</code></td>
<td>SCTP over IPv6
</td>
</tr>
<tr VALIGN=top>
<td><code>ah6</code></td>
<td>IPSEC AH over IPv6
</td>
</tr>
<tr VALIGN=top>
<td><code>esp6</code></td>
<td>IPSEC ESP over IPv6
</td>
</tr>
</table>
</dl>
<p> For all fields that allow both a value and a mask to be specified, the mask may be specified immediately after the value using the <code>m</code> keyword, or separately using the field name keyword with <code>-mask</code> appended, e.g. <code>src-mask</code>.</p>
<dl>
<dt><code>src</code>&nbsp;<wbr><i>xx</i><code>:</code><i>yy</i><code>:</code><i>zz</i><code>:</code><i>aa</i><code>:</code><i>bb</i><code>:</code><i>cc</i>&nbsp;<wbr>[<code>m</code>&nbsp;<wbr><i>xx</i><code>:</code><i>yy</i><code>:</code><i>zz</i><code>:</code><i>aa</i><code>:</code><i>bb</i><code>:</code><i>cc</i>]</p>
<dd>Includes the source MAC address, specified as 6 bytes in hexadecimal separated by colons, along with an optional mask. Valid only for flow-type ether.</p>
<dt><code>dst</code>&nbsp;<wbr><i>xx</i><code>:</code><i>yy</i><code>:</code><i>zz</i><code>:</code><i>aa</i><code>:</code><i>bb</i><code>:</code><i>cc</i>&nbsp;<wbr>[<code>m</code>&nbsp;<wbr><i>xx</i><code>:</code><i>yy</i><code>:</code><i>zz</i><code>:</code><i>aa</i><code>:</code><i>bb</i><code>:</code><i>cc</i>]</p>
<dd>Includes the destination MAC address, specified as 6 bytes in hexadecimal separated by colons, along with an optional mask. Valid only for flow-type ether.</p>
<dt><code>proto</code><i>&nbsp;<wbr>N</i><code>R&nbsp;<wbr>[Pm</code><i>&nbsp;<wbr>N</i><code>R]P</code></p>
<dd>Includes the Ethernet protocol number (ethertype) and an optional mask. Valid only for flow-type ether.</p>
<dt><code>src-ip</code>&nbsp;<wbr><i>ip-address</i>&nbsp;<wbr>[<code>m</code>&nbsp;<wbr><i>ip-address</i>]</p>
<dd>Specify the source IP address of the incoming packet to match along with an optional mask. Valid for all IP based flow-types.</p>
<dt><code>dst-ip</code>&nbsp;<wbr><i>ip-address</i>&nbsp;<wbr>[<code>m</code>&nbsp;<wbr><i>ip-address</i>]</p>
<dd>Specify the destination IP address of the incoming packet to match along with an optional mask. Valid for all IP based flow-types.</p>
<dt><code>tos</code><i>&nbsp;<wbr>N</i><code>R&nbsp;<wbr>[Pm</code><i>&nbsp;<wbr>N</i><code>R]P</code></p>
<dd>Specify the value of the Type of Service field in the incoming packet to match along with an optional mask. Applies to all IPv4 based flow-types.</p>
<dt><code>tclass</code><i>&nbsp;<wbr>N</i><code>R&nbsp;<wbr>[Pm</code><i>&nbsp;<wbr>N</i><code>R]P</code></p>
<dd>Specify the value of the Traffic Class field in the incoming packet to match along with an optional mask. Applies to all IPv6 based flow-types.</p>
<dt><code>l4proto</code><i>&nbsp;<wbr>N</i><code>R&nbsp;<wbr>[Pm</code><i>&nbsp;<wbr>N</i><code>R]P</code></p>
<dd>Includes the layer 4 protocol number and optional mask. Valid only for flow-types ip4 and ip6.</p>
<dt><code>src-port</code><i>&nbsp;<wbr>N</i><code>R&nbsp;<wbr>[Pm</code><i>&nbsp;<wbr>N</i><code>R]P</code></p>
<dd>Specify the value of the source port field (applicable to TCP/UDP packets) in the incoming packet to match along with an optional mask. Valid for flow-types ip4, tcp4, udp4, and sctp4 and their IPv6 equivalents.</p>
<dt><code>dst-port</code><i>&nbsp;<wbr>N</i><code>R&nbsp;<wbr>[Pm</code><i>&nbsp;<wbr>N</i><code>R]P</code></p>
<dd>Specify the value of the destination port field (applicable to TCP/UDP packets)in the incoming packet to match along with an optional mask. Valid for flow-types ip4, tcp4, udp4, and sctp4 and their IPv6 equivalents.</p>
<dt><code>spi</code><i>&nbsp;<wbr>N</i><code>R&nbsp;<wbr>[Pm</code><i>&nbsp;<wbr>N</i><code>R]P</code></p>
<dd>Specify the value of the security parameter index field (applicable to AH/ESP packets)in the incoming packet to match along with an optional mask. Valid for flow-types ip4, ah4, and esp4 and their IPv6 equivalents.</p>
<dt><code>l4data</code><i>&nbsp;<wbr>N</i><code>R&nbsp;<wbr>[Pm</code><i>&nbsp;<wbr>N</i><code>R]P</code></p>
<dd>Specify the value of the first 4 Bytes of Layer 4 in the incoming packet to match along with an optional mask. Valid for ip4 and ip6 flow-types.</p>
<dt><code>vlan-etype</code><i>&nbsp;<wbr>N</i><code>R&nbsp;<wbr>[Pm</code><i>&nbsp;<wbr>N</i><code>R]P</code></p>
<dd>Includes the VLAN tag Ethertype and an optional mask.</p>
<dt><code>vlan</code><i>&nbsp;<wbr>N</i><code>R&nbsp;<wbr>[Pm</code><i>&nbsp;<wbr>N</i><code>R]P</code></p>
<dd>Includes the VLAN tag and an optional mask.</p>
<dt><code>user-def</code><i>&nbsp;<wbr>N</i><code>R&nbsp;<wbr>[Pm</code><i>&nbsp;<wbr>N</i><code>R]P</code></p>
<dd>Includes 64-bits of user-specific data and an optional mask.</p>
<dt><code>dst-mac</code>&nbsp;<wbr><i>xx</i><code>:</code><i>yy</i><code>:</code><i>zz</i><code>:</code><i>aa</i><code>:</code><i>bb</i><code>:</code><i>cc</i>&nbsp;<wbr>[<code>m</code>&nbsp;<wbr><i>xx</i><code>:</code><i>yy</i><code>:</code><i>zz</i><code>:</code><i>aa</i><code>:</code><i>bb</i><code>:</code><i>cc</i>]</p>
<dd>Includes the destination MAC address, specified as 6 bytes in hexadecimal separated by colons, along with an optional mask. Valid for all IP based flow-types.</p>
<dt><code>action</code><i>&nbsp;<wbr>N</i></p>
<dd>Specifies the Rx queue to send packets to, or some other action. </p>
<table>
<tr VALIGN=top>
<td><code>-1</code></td>
<td>Drop the matched flow
</td>
</tr>
<tr VALIGN=top>
<td><code>0 or higher</code></td>
<td>Rx queue to route the flow
</td>
</tr>
</table>
<dt><code>loc</code><i>&nbsp;<wbr>N</i></p>
<dd>Specify the location/ID to insert the rule. This will overwrite any rule present in that location and will not go through any of the rule ordering process.</p>
<dt><code>delete</code><i>&nbsp;<wbr>N</i></p>
<dd>Deletes the RX classification rule with the given ID.</dl>
</dl>
<dt><code>-w &#8211;get-dump</code></p>
<dd>Retrieves and prints firmware dump for the specified network device. By default, it prints out the dump flag, version and length of the dump data. When <i>data</i> is indicated, then ethtool fetches the dump data and directs it to a <i>file.</i></p>
<dt><code>-W &#8211;set-dump</code></p>
<dd>Sets the dump flag for the device.</p>
<dt><code>-T &#8211;show-time-stamping</code></p>
<dd>Show the device&#8217;s time stamping capabilities and associated PTP hardware clock.</p>
<dt><code>-x &#8211;show-rxfh-indir &#8211;show-rxfh</code></p>
<dd>Retrieves the receive flow hash indirection table and/or RSS hash key.</p>
<dt><code>-X &#8211;set-rxfh-indir &#8211;rxfh</code></p>
<dd>Configures the receive flow hash indirection table and/or RSS hash key.</p>
<dl>
<dd>
<dl>
<dt><code>hkey</code></p>
<dd>Sets RSS hash key of the specified network device. RSS hash key should be of device supported length. Hash key format must be in xx:yy:zz:aa:bb:cc format meaning both the nibbles of a byte should be mentioned even if a nibble is zero.</p>
<dt><code>equal&nbsp;<wbr></code><i>N</i></p>
<dd>Sets the receive flow hash indirection table to spread flows evenly between the first <i>N</i> receive queues.</p>
<dt><code>weight</code> <i>W0 W1</i> &#8230;</p>
<dd>Sets the receive flow hash indirection table to spread flows between receive queues according to the given weights. The sum of the weights must be non-zero and must not exceed the size of the indirection table.</p>
<dt><code>default</code></p>
<dd>Sets the receive flow hash indirection table to its default value.</dl>
</dl>
<dt><code>-f &#8211;flash</code></p>
<dd>Write a firmware image to flash or other non-volatile memory on the device.</p>
<dl>
<dd>
<dl>
<dt><i>file</i></p>
<dd>Specifies the filename of the firmware image. The firmware must first be installed in one of the directories where the kernel firmware loader or firmware agent will look, such as /lib/firmware.</p>
<dt><i>N</i></p>
<dd>If the device stores multiple firmware images in separate regions of non-volatile memory, this parameter may be used to specify which region is to be written. The default is 0, requesting that all regions are written. All other values are driver-dependent.</dl>
</dl>
<dt><code>-l &#8211;show-channels</code></p>
<dd>Queries the specified network device for the numbers of channels it has. A channel is an IRQ and the set of queues that can trigger that IRQ.</p>
<dt><code>-L &#8211;set-channels</code></p>
<dd>Changes the numbers of channels of the specified network device.</p>
<dl>
<dd>
<dl>
<dt><code>rx</code><i>&nbsp;<wbr>N</i></p>
<dd>Changes the number of channels with only receive queues.</p>
<dt><code>tx</code><i>&nbsp;<wbr>N</i></p>
<dd>Changes the number of channels with only transmit queues.</p>
<dt><code>other</code><i>&nbsp;<wbr>N</i></p>
<dd>Changes the number of channels used only for other purposes e.g. link interrupts or SR-IOV co-ordination.</p>
<dt><code>combined</code><i>&nbsp;<wbr>N</i></p>
<dd>Changes the number of multi-purpose channels.</dl>
</dl>
<dt><code>-m &#8211;dump-module-eeprom &#8211;module-info</code></p>
<dd>Retrieves and if possible decodes the EEPROM from plugin modules, e.g SFP+, QSFP. If the driver and module support it, the optical diagnostic information is also read and decoded.</p>
<dt><code>&#8211;show-priv-flags</code></p>
<dd>Queries the specified network device for its private flags. The names and meanings of private flags (if any) are defined by each network device driver.</p>
<dt><code>&#8211;set-priv-flags</code></p>
<dd>Sets the device&#8217;s private flags as specified.</p>
<dl>
<dd><i>flag</i> <code>on</code>|<code>off</code> Sets the state of the named private flag.</dl>
<dt><code>&#8211;show-eee</code></p>
<dd>Queries the specified network device for its support of Energy-Efficient Ethernet (according to the IEEE 802.3az specifications)</p>
<dt><code>&#8211;set-eee</code></p>
<dd>Sets the device EEE behaviour.</p>
<dl>
<dd>
<dl>
<dt> <code>eee</code>&nbsp;<wbr><code>on</code>|<code>off</code></p>
<dd>Enables/disables the device support of EEE.</p>
<dt> <code>tx-lpi</code>&nbsp;<wbr><code>on</code>|<code>off</code></p>
<dd>Determines whether the device should assert its Tx LPI.</p>
<dt><code>advertise</code><i>&nbsp;<wbr>N</i></p>
<dd>Sets the speeds for which the device should advertise EEE capabilities. Values are as for <code>&#8211;change advertise</code></p>
<dt><code>tx-timer</code><i>&nbsp;<wbr>N</i></p>
<dd>Sets the amount of time the device should stay in idle mode prior to asserting its Tx LPI (in microseconds). This has meaning only when Tx LPI is enabled.</dl>
</dl>
</dl>
<h2>Bugs</h2>
<p>Not supported (in part or whole) on all network drivers.</p>
<h2>Author</h2>
<p><code>ethtool</code> was written by David Miller. </p>
<p> Modifications by Jeff Garzik, Tim Hockin, Jakub Jelinek, Andre Majorel, Eli Kupermann, Scott Feldman, Andi Kleen, Alexander Duyck, Sucheta Chakraborty, Jesse Brandeburg, Ben Hutchings.</p>
<h2>Availability</h2>
<p><code>ethtool</code> is available from <a rel="nofollow" href="http://www.kernel.org/pub/software/network/ethtool/">http://www.kernel.org/pub/software/network/ethtool/</a> �e�?</p>
