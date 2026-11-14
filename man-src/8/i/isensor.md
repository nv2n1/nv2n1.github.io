---
title: "isensor(8)"
name: "isensor"
section: "8"
letter: "i"
url: "/docs/linux/man/8-isensor/"
description: "ipmiutil_sensor – show Sensor Data Records"
---

<p>ipmiutil_sensor &#8211; show Sensor Data Records</p>
<h2>Synopsis</h2>
<p><code>ipmiutil sensor [-abcdefgjkmpqrstuvwxL -i id -n snum -h tval -l tval -NUPREFJTVY]</code> </p>
<h2>Description</h2>
<p><i>ipmiutil sensor</i> is a program that uses IPMI commands to show and decode Sensor Data Records and current sensor readings for all sensors in the system. This utility can use either the /dev/ipmi0 driver from OpenIPMI, the /dev/imb driver from Intel, the /dev/ipmikcs driver from valinux, direct user-space IOs, or the IPMI LAN interface if -N. Note that this utility by default only displays Sensor Data Records reported by from the Baseboard Management Controller. To show sensors for other controllers, see options -b and -m below. </p>
<h2>Options</h2>
<p>Command line options are described below.</p>
<dl>
<dt>-a snum</p>
<dd>ReArms the sensor number for events</p>
<dt>-b</p>
<dd>Shows SDRs for Bladed (PICMG or ATCA) systems by traversing the child MCs (same as -e).</p>
<dt>-c</p>
<dd>Show sensor list in a simpler/Canonical format without uninterpreted binary values. Only the user-friendly interpreted sensor information is shown. (same as -s).</p>
<dt>-d &lt;file&gt;</p>
<dd>Dump the SDRs to a specified binary file. This file can be used with -j to jumpstart getting the sensor readings.</p>
<dt>-e</p>
<dd>Show Every SDR in a bladed system by traversing the child MCs (same as -b).</p>
<dt>-f &lt;file&gt;</p>
<dd>Restore the SDRs from the specified binary File. This is normally only done with the initial factory provisioning.</p>
<dt>-g sens_type</p>
<dd>Shows only those SDRs matching the given sensor type group. The sens_type string can be &quot;fan&quot;, &quot;temp&quot;, &quot;voltage&quot;, or any string or substring matching those in the IPMI 2.0 Table 42-3 for Sensor Types. Multiple types can be listed, separated by a comma (,) but no spaces.</p>
<dt>-h tval</p>
<dd>Highest threshold value to set for the specified sensor. This tval can be in decimal, or of the form 0x1a, to match the raw reading value shown by sensor following the &quot; = &quot;. The value passed is set as the non-critical threshold value, with the more critical ones set by the utility as incrementally lower. This simplifies the interface and ensures that the threshold values do not get out of order. This requires specifying the sensor number via -n.</p>
<dt>-i ID</p>
<dd>Show or set only the sensor Index corresponding to ID, where ID is the hex ID of the SDR as shown in the sensor output under &quot;_ID_&quot;. The ID argument can be one hex number (e.g. 0x0e or 0e), or a range of hex numbers (e.g. 0e-1a or 1a,2a or 0x0e-0x2a). This is useful to repeatedly view just a few sensor readings for changes, or to set just one sensor quickly without reading all of the SDRs.</p>
<dt>-j file</p>
<dd>Jump-start by caching the SDRs from a file. This uses an SDR binary file to read the SDRs, so that only the sensor readings need to be read from the firmware. This avoids getting the SDR reservation and reading each SDR, so it makes getting the sensor readings more efficient. The SDR binary file can be created using the -d option to dump the SDRs to a file, or -j will try to create the file if not there.</p>
<dt>-k K</p>
<dd>When looping with -L, wait K seconds between loops. Default is 1 second.</p>
<dt>-l tval</p>
<dd>Lowest threshold value to set for the specified sensor. This tval can be in decimal, or of the form 0x1a, to match the raw reading value shown by sensor following the &quot; = &quot;. The value passed is set as the non-critical threshold value, with the more critical ones set by the utility as incrementally higher. This simplifies the interface and ensures that the threshold values do not get out of order. This requires specifying the sensor number via -n.</p>
<dt>-m 002000s</p>
<dd>Show SDRs for a specific MC (e.g. bus 00, sa 20, lun 00). This could be used for PICMG or ATCA blade systems. The trailing character, if present, indicates SMI addressing if &#8216;s&#8217;, or IPMB addressing if &#8216;i&#8217; or not present.</p>
<dt>-n snum</p>
<dd>Number of the sensor to set. This num can be in decimal, or of the form 0x1a, to match the value shown by sensor following the &quot;snum&quot; tag. This is required if setting hi/lo thresholds via -h/-l.</p>
<dt>-o</p>
<dd>Output the memory DIMM information from SMBIOS, including size. Not available if using IPMI LAN via -N. Sample output:<br />
 Memory Device (0,0): DIMM_A1 : size=2048MB<br />
 Memory Device (0,1): DIMM_A2 : not present</p>
<dt>-p</p>
<dd>Persist the threshold being set (as specified via -l or -h). This writes a &quot;sensor -i&quot; script line to the file /usr/share/ipmiutil/thresholds.sh, which can then be executed at each reboot by starting the /etc/init.d/ipmi_port service for the desired runlevels. For Windows, the filename is thresholds.cmd.</p>
<dt>-q</p>
<dd>Show threshold values in d:d:d format. Thresholds are shown for each sensor in short format with &#8216;:&#8217; delimiters, which is useful as an example for setting thresholds with &#8216;-u&#8217;.</p>
<dt>-r</p>
<dd>Show Raw SDR bytes also.</p>
<dt>-s</p>
<dd>Show sensor list in a simpler/canonical format without uninterpreted binary values. Only the user-friendly interpreted sensor information is shown. (same as -c).</p>
<dt>-t</p>
<dd>Show any Thresholds for each sensor also, in text format.</p>
<dt>-u</p>
<dd>Set unique threshold values. The values are specified in a string of threshold values. It can be in raw hex characters or in float values. All 6 possible thresholds must be specified, but only the ones that are valid for this sensor will be applied. These values are validated for ordering. For example:<br />
&nbsp;<wbr>&nbsp;<wbr>-u 6:5:4:60:65:69&nbsp;<wbr>(float)&nbsp;<wbr>or<br />
&nbsp;<wbr>&nbsp;<wbr>-u 0x0605043c4145&nbsp;<wbr>(raw hex)<br />
&nbsp;<wbr>would mean 0x06=noncrit_lo, 0x05=crit_lo, 0x04=nonrec_lo, 0x3c=noncrit_hi, 0x41=crit_hi, 0x45=nonrec_hi.</p>
<dt>-v</p>
<dd>Show Verbose output, including volatile thresholds, SDR thresholds, max/min, hysteresis, and BMC_TAM decoding.</p>
<dt>-w</p>
<dd>Wrap the threshold data onto the same line as the sensor. This may be convenient for scripting.</p>
<dt>-x</p>
<dd>Causes eXtra debug messages to be displayed.</p>
<dt>-L n</p>
<dd>Loop n times every K seconds. Default is one loop and K defaults to 1 second. See option -k to change K seconds if desired. This is useful along with -i or -g to read some sensors as they change. Using -j with this option makes run it quicker.</p>
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
<h2>Examples</h2>
<p>ipmiutil sensor sample output is below.<br />
 ipmiutil ver 2.21<br />
 sensor: version 2.21<br />
 &#8212; BMC version 0.17, IPMI version 2.0<br />
 _ID_ SDR_Type_xx ET Own Typ S_Num Sens_Description Hex &amp; Interp Reading<br />
 000b SDR Full 01 01 20 a 01 snum 30 Baseboard Temp = 2e OK 46.00 degrees C<br />
 000e SDR Full 01 01 20 m 04 snum 50 Fan 1A = 6f OK 7659.00 RPM<br />
 0042 SDR Comp 02 6f 20 a 21 snum e0 DIMM 1A = 00 c0 04 00 Present<br />
 004e SDR FRU 11 1b dev: 20 03 80 00 0a 01 Pwr Supply 1 FRU<br />
 0050 SDR IPMB 12 1b dev: 20 00 bf 07 01 Basbrd Mgmt Ctlr<br />
 0051 SDR OEM c0 09 Intel: 02 02 00 01 70 71<br />
 0065 SDR OEM c0 11 Intel: SDR Package 17<br />
 [&#8230;] Output Columns:<br />
 _ID_: This is an SDR ID or index number, in hex. This may vary from chassis to chassis.<br />
 SDR_Type_xx: This shows the SDR Type and its hex representation. Some SDR types have a custom display. The OEM SDRs only show the OEM vendor by IANA number and then usually the data is listed in hex.<br />
 ET: For Full or Comp SDRs, this shows the Event Type. For other SDRs, this shows the size of the SDR entry in hex (Sz).<br />
 Own: This is the hex slave address of the SDR Owner, usually 20 if BMC.<br />
 a/m: This indicates whether this sensor is either automatically or manually rearmed, respectively.<br />
 Typ: This is the Sensor Type as defined in Table 42-3 of the IPMI 2.0 spec. (01 = Temperature, 02 = Voltage, 03 = Current, 04 = Fan, etc.)<br />
 S_Num: This is the sensor number in hex. This remains consistent across baseboards of the same type. The output can be parsed with the &quot;snum&quot; delimiter to extract this value.<br />
 Sens_Description: This is the text description of this SDR, which is stored within the SDR on the BMC.<br />
 Hex &amp; Interp Reading: This is the raw hex value returned by GetSensorReading, and its interpreted meaning. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ipmiutil/">ipmiutil</a>(8) <a href="/docs/linux/man/8-ialarms/">ialarms</a>(8) <a href="/docs/linux/man/8-iconfig/">iconfig</a>(8) <a href="/docs/linux/man/8-icmd/">icmd</a>(8) <a href="/docs/linux/man/8-idiscover/">idiscover</a>(8) <a href="/docs/linux/man/8-ievents/">ievents</a>(8) <a href="/docs/linux/man/8-ifru/">ifru</a>(8) <a href="/docs/linux/man/8-igetevent/">igetevent</a>(8) <a href="/docs/linux/man/8-ihealth/">ihealth</a>(8) <a href="/docs/linux/man/8-ilan/">ilan</a>(8) <a href="/docs/linux/man/8-ireset/">ireset</a>(8) <a href="/docs/linux/man/8-isel/">isel</a>(8) <a href="/docs/linux/man/8-iserial/">iserial</a>(8) <a href="/docs/linux/man/8-isol/">isol</a>(8) <a href="/docs/linux/man/8-iwdt/">iwdt</a>(8) </p>
<h2>Warnings</h2>
<p>See <a rel="nofollow" href="http://ipmiutil.sourceforge.net/">http://ipmiutil.sourceforge.net/</a> for the latest version of ipmiutil and any bug fix list.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2009 Kontron America, Inc. </p>
<p> See the file COPYING in the distribution for more details regarding redistribution. </p>
<p> This utility is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY.</p>
<h2>Author</h2>
<p>Andy Cress &lt;arcress at users.sourceforge.net&gt;</p>
