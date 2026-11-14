---
title: "ifru(8)"
name: "ifru"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ifru/"
description: "ipmiutil_fru – show Field Replacable Unit configuration data"
---

<p>ipmiutil_fru &#8211; show Field Replacable Unit configuration data</p>
<h2>Synopsis</h2>
<p><code>ipmiutil fru [-abcdeikmsvx -N node -U user -P/-R pswd -EFJTVY]</code> </p>
<h2>Description</h2>
<p><i>ipmiutil fru</i> is a program that uses IPMI commands to show FRU configuration data and optionally write an asset tag string into the FRU data. Setting the asset tag is a function that can be used to uniquely identify the unit, even if the storage devices are removed or changed. This utility can use either the /dev/ipmi0 driver from OpenIPMI, the /dev/imb driver from Intel, the /dev/ipmikcs driver from valinux, direct user-space IOs, or the IPMI LAN interface if -N. </p>
<h2>Options</h2>
<p>Command line options are described below.</p>
<dl>
<dt>-a asset_string</p>
<dd>This option specifies an asset tag string to be written to the baseboard FRU Product area. The asset tag length is limited by the existing FRU Product data, but is usually allowed up to 16 characters. The default is to not modify this FRU field.</p>
<dt>-b</p>
<dd>Only show the Baseboard FRU data. The default behavior is to also scan for any SDR FRU data or DIMM SPD data referenced by the SDRs.</p>
<dt>-c</p>
<dd>Show FRU output in a canonical format, with a default delimiter of &#8216;|&#8217;.</p>
<dt>-d file</p>
<dd>Dump binary FRU data to the specified file.</p>
<dt>-e</p>
<dd>Show Every FRU output in a bladed chassis, including those under child MCs. The default is to show FRUs referred to by just the target MC.</p>
<dt>-i 00</p>
<dd>This option specifies a specific FRU ID to show. The input value should be in hex (0b, 1a, etc.), as shown from the sensor SDR output. By default, all FRU IDs that are specified in the FRU locator SDRs are shown.</p>
<dt>-k &lt;setsn | setmfgdate | nextboot&gt;</p>
<dd>These Kontron OEM functions set FRU data based on existing data stored elsewhere. The setsn option sets the FRU Board and Product serial number, and the setmfgdate option sets the FRU Board Mfg DateTime. The nextboot option specifies the boot device for the next boot: BIOS, FDD, HDD, CDROM, or network. These options are only supported on Kontron ATCA boards which have this functionality.</p>
<dt>-m 002000</p>
<dd>Show FRU for a specific MC (e.g. bus 00, sa 20, lun 00). This could be used for PICMG or ATCA blade systems. The trailing character, if present, indicates SMI addressing if &#8216;s&#8217;, or IPMB addressing if &#8216;i&#8217; or not present.</p>
<dt>-s serial_num</p>
<dd>This option specifies a serial number string to be written to the baseboard FRU Product area. The serial number can be any string up to 16 characters. The default is to not modify this FRU field.</p>
<dt>-v prod_ver</p>
<dd>This option specifies a product version number string to be written to the baseboard FRU Product area. The version number can be any string up to 16 characters. The default is to not modify this FRU field.</p>
<dt>-x</p>
<dd>Causes eXtra debug messages to be displayed.</p>
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
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ipmiutil/">ipmiutil</a>(8) <a href="/docs/linux/man/8-ialarms/">ialarms</a>(8) <a href="/docs/linux/man/8-iconfig/">iconfig</a>(8) <a href="/docs/linux/man/8-icmd/">icmd</a>(8) <a href="/docs/linux/man/8-idiscover/">idiscover</a>(8) <a href="/docs/linux/man/8-ievents/">ievents</a>(8) <a href="/docs/linux/man/8-igetevent/">igetevent</a>(8) <a href="/docs/linux/man/8-ihealth/">ihealth</a>(8) <a href="/docs/linux/man/8-ilan/">ilan</a>(8) <a href="/docs/linux/man/8-ireset/">ireset</a>(8) <a href="/docs/linux/man/8-isel/">isel</a>(8) <a href="/docs/linux/man/8-isensor/">isensor</a>(8) <a href="/docs/linux/man/8-iserial/">iserial</a>(8) <a href="/docs/linux/man/8-isol/">isol</a>(8) <a href="/docs/linux/man/8-iwdt/">iwdt</a>(8) </p>
<h2>Warnings</h2>
<p>See <a rel="nofollow" href="http://ipmiutil.sourceforge.net/">http://ipmiutil.sourceforge.net/</a> for the latest version of ipmiutil and any bug fix list.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2009 Kontron America, Inc. </p>
<p> See the file COPYING in the distribution for more details regarding redistribution. </p>
<p> This utility is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY.</p>
<h2>Author</h2>
<p>Andy Cress &lt;arcress at users.sourceforge.net&gt;</p>
