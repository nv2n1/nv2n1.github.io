---
title: "ievents(8)"
name: "ievents"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ievents/"
description: "ievents – decode IPMI and PET event data"
---

<p>ievents &#8211; decode IPMI and PET event data</p>
<h2>Synopsis</h2>
<p><code>ievents [-bfhnprsx] 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f 10</code> </p>
<h2>Description</h2>
<p><i>ievents</i> is a standalone utility delivered with ipmiutil, used to interpret raw hex data from IPMI events or from IPMI PET SNMP trap varbind data. This utility uses the same interpretation logic as is used by &quot;ipmiutil sel&quot; (showsel) and &quot;ipmiutil getevt&quot; (getevents). The data bytes in the input are always assumed to be in hex form. This could be useful if a utility other than &quot;ipmiutil sel&quot; were used to obtain IPMI SEL records or events and interpretation is needed. This would also be needed at an enterprise management station to interpret the PET SNMP trap hex data into human-readable form, see option -p. </p>
<h2>Options</h2>
<dl>
<dt>-b bin_file</p>
<dd>Interpret a file containing raw binary/hex SEL data dumped in binary form, such as that produced by &quot;ipmitool sel writeraw bin_file&quot;. Each set of 16 bytes in the file will be interpreted as an IPMI event. (same as -h) </p>
<dt>-f sel_file</p>
<dd>Interpret a file containing raw ascii text SEL data captured with ipmiutil sel -r, or some other similar utility. Each line in the file should be in this form, with no leading spaces:<br />
 04 00 02 76 a9 4a 47 20 00 04 10 09 6f 42 0f ff<br />
 If this option is not specified, the default is to use the 16 bytes taken from the command-line arguments. (same as -r) </p>
<dt>-h bin_file</p>
<dd>Interpret a file containing raw binary/hex SEL data dumped in binary form, such as that produced by &quot;ipmitool sel writeraw bin_file&quot;. Each set of 16 bytes in the file will be interpreted as an IPMI event. (same as -b) </p>
<dt>-n</p>
<dd>This option generates a New IPMI platform event, using 9 bytes of input. The input bytes are the same as the last 9 bytes of an IPMI event. </p>
<dt>-p</p>
<dd>Decode as PET event bytes, where the input is 34 PET hex data bytes, skipping the first 8 of the 47-byte PET data. The default without -p assumes that the input is a 16-byte IPMI event. </p>
<dt>-r sel_file</p>
<dd>Interpret a file containing raw ascii text SEL data captured with ipmiutil sel -r, or some other similar utility. (same as -f) </p>
<dt>-s sensor_file</p>
<dd>Sensor file with the output of &quot;ipmiutil sensor&quot;, used to get the PET sensor_type from the sensor_num. The default is /usr/share/ipmiutil/sensor_out.txt as generated during the ipmiutil package installation. This is only needed with PET interpretation (-p). </p>
<dt>-x</p>
<dd>show eXtra debug messages </p>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ipmiutil/">ipmiutil</a>(8) <a href="/docs/linux/man/8-ialarms/">ialarms</a>(8) <a href="/docs/linux/man/8-iconfig/">iconfig</a>(8) <a href="/docs/linux/man/8-icmd/">icmd</a>(8) <a href="/docs/linux/man/8-idiscover/">idiscover</a>(8) <a href="/docs/linux/man/8-ifru/">ifru</a>(8) <a href="/docs/linux/man/8-igetevent/">igetevent</a>(8) <a href="/docs/linux/man/8-ihealth/">ihealth</a>(8) <a href="/docs/linux/man/8-ilan/">ilan</a>(8) <a href="/docs/linux/man/8-ireset/">ireset</a>(8) <a href="/docs/linux/man/8-isel/">isel</a>(8) <a href="/docs/linux/man/8-isensor/">isensor</a>(8) <a href="/docs/linux/man/8-iserial/">iserial</a>(8) <a href="/docs/linux/man/8-isol/">isol</a>(8) <a href="/docs/linux/man/8-iwdt/">iwdt</a>(8) </p>
<h2>Warnings</h2>
<p>See <a rel="nofollow" href="http://ipmiutil.sourceforge.net/">http://ipmiutil.sourceforge.net/</a> for the latest version of ipmiutil and any bug fix list.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2009 Kontron America, Inc. </p>
<p> See the file COPYING in the distribution for more details regarding redistribution. </p>
<p> This utility is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY.</p>
<h2>Author</h2>
<p>Andy Cress &lt;arcress at users.sourceforge.net&gt;</p>
