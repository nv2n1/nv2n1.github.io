---
title: "ath_info(8)"
name: "ath_info"
section: "8"
letter: "a"
url: "/docs/linux/man/8-ath_info/"
description: "ath_info – print module version info, write some eeprom fields"
---

<p>ath_info &#8211; print module version info, write some eeprom fields</p>
<h2>Synopsis</h2>
<p><code>ath_info</code> [-w [-g N:M]] [-v] [-f] &lt;pci_address&gt; [&lt;field1&gt; &lt;val1&gt; [&lt;field2&gt; &lt;val2&gt; &#8230;]] </p>
<h2>Description</h2>
<p><code>ath_info</code> prints some version information of Atheros WLAN modules. It furthermore allows to change regulatory domain and PCI ID fields in the EEPROM. You must first retrieve the PCI memory address of the module by <code>lspci -v</code> and maybe activate the module by <code>setpci</code> (see example below). <code>DISCLAIMER:</code> Use the write function only if you know what you are doing! There is the chance to brick your module. The authors aren&#8217;t responsible for any damage caused by using this program. <code> Transmitting on illegal frequencies may violate state laws. Obey the local regulations!</code> </p>
<h2>Options</h2>
<dl>
<dt><code>-w</code></p>
<dd>Write to the EEPROM. You need to specify at least one <code>field value</code> pair (see below).</p>
<dt><code>-g N:M</code></p>
<dd>Set the GPIO pin N to level M (N=0..5, M=0,1). Only useful with <code>-w</code>. <code>ath_info</code> sets GPIO 4 to 0 (low) for chipsets newer or equal to 5213 to enable writing to the EEPROM. If your module has a different layout, you may need to overwrite this.</p>
<dt><code>-v</code></p>
<dd>verbose printouts</p>
<dt><code>-f</code></p>
<dd>force, don&#8217;t ask before writing to EEPROM (with <code>-w).</p>
<dt>&lt;pci_address&gt;</code></p>
<dd>The PCI address of the module. You must retrieve it with <code>lspci</code>.</p>
<dt><code>&lt;field&gt; &lt;value&gt;</code></p>
<dd>Field and value names for EEPROM writing. Possible fields are: <code>pci_dev_id, pci_vendor_id, pci_class, pci_rev_id, pci_subsys_dev_id, pci_subsys_vendor_id, regdomain</code> </p>
</dl>
<h2>Example</h2>
<p>Execute the commands below from a root account. Retrieve the module&#8217;s PCI memory address with <code>lspci</code>: </p>
<pre># lspci -v
0b:00.0 Ethernet controller: Atheros Communications, Inc. AR5211 802.11ab NIC
(rev 01)
 Subsystem: Standard Microsystems Corp [SMC] Unknown device 2335
 Flags: medium devsel, IRQ 20
 Memory at 6c000000 (32-bit, non-prefetchable) [size=64K]
 Capabilities: [44] Power Management version 2</pre>
<p>The above card has its memory mapped at 0x6c000000. If no madwifi driver is running or the module isn&#8217;t recognized by the driver anymore, e.g. due to wrong PCI id values (check your syslog), you must manually enable the PCI device with <code>setpci</code>. The argument to &quot;-s&quot; comes from the output above: </p>
<pre>setpci -s 0b:00.0 command=0x41f cache_line_size=0x10</pre>
<p>Retrieve some information of the module: </p>
<pre># ./ath_info 0x6c000000
 -==Device Information==-
MAC Version: 5211 (0x40) 
MAC Revision: 5211 (0x42) 
5GHz PHY Revision: 5111 (0x17) 
2GHz PHY Revision: 2111 (0x23) 
 -==EEPROM Information==-
EEPROM Version: 3.2 
EEPROM Size: 16K
Regulatory Domain: 0x20
 -==== Capabilities ====-
| 802.11a Support: yes |
| 802.11b Support: yes |
| 802.11g Support: no |
| RFKill Support: no |
 ========================</pre>
<p>Set the regulatory domain to 0. You need to confirm to write with &#8216;y&#8217; (-f turns this off). Check <code><a rel="nofollow" href="http://madwifi-project.org/wiki/UserDocs/CountryCode">http://madwifi-project.org/wiki/UserDocs/CountryCode</a></code> for more information on regdomains and country codes: </p>
<pre># ./ath_info -w 0x6c000000 regdomain 0
 -==Device Information==-
MAC Version: 5211 (0x40) 
MAC Revision: 5211 (0x42) 
5GHz PHY Revision: 5111 (0x17) 
2GHz PHY Revision: 2111 (0x23) 
 -==EEPROM Information==-
EEPROM Version: 3.2 
EEPROM Size: 16K
Regulatory Domain: 0x20 
 -==== Capabilities ====-
| 802.11a Support: yes |
| 802.11b Support: yes |
| 802.11g Support: no |
| RFKill Support: no |
 ========================
GPIO registers: CR 00000000 DO 00000000 DI 00000000
 regdomain (0x00bf) := 0x0000
WARNING: The write function may easy brick your device or
violate state regulation on frequency usage.
Proceed on your own risk!
Shall I write the above value(s)? (y/n)
y</pre>
<h2>Bugs</h2>
<p>The write function is currently not tested with 5210 devices. Use at your own risk, entering a false device address will have really nasty results! An invalid magic in the EEPROM will cause <code>ath_info</code> to fail. </p>
