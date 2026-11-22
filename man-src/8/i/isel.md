---
title: "isel(8)"
name: "isel"
section: "8"
letter: "i"
url: "/docs/linux/man/8-isel/"
description: "ipmiutil_sel – show firmware System Event Log records"
---

<p>ipmiutil_sel &#8211; show firmware System Event Log records</p>
<h2>Synopsis</h2>
<p><code>ipmiutil sel [-abcflswvx -N node -P/-R pswd -U user -EFJTVY]</code> </p>
<h2>Description</h2>
<p><i>ipmiutil sel</i> is a program that uses IPMI commands to to read and display the System Event Log (SEL) which is stored by the BMC firmware. IPMI commands are issued to read each record, and, if specified, incrementally write records that have not previously been read into the Linux syslog (/var/log/messages). This utility can use either the /dev/ipmi0 driver from OpenIPMI, the /dev/imb driver from Intel, the /dev/ipmikcs driver from valinux, direct user-space IOs, or the IPMI LAN interface if -N. </p>
<h2>Options</h2>
<p>Command line options are described below. </p>
<dl>
<dt>-a string</dt>
<dd>Add a SEL record with a string of up to 13 characters. Longer strings will be truncated. Note that this should be used sparingly, but would be useful for changes made to the hardware or firmware environment, like &quot;Fan replaced&quot; or &quot;flash FW2.1&quot;. </dd>
<dt>-b bin_file</dt>
<dd>Interpret a file containing raw binary/hex SEL data dumped in binary form, such as that produced by &quot;ipmitool sel writeraw bin_file&quot;. Each set of 16 bytes in the file will be interpreted as an IPMI event. </dd>
<dt>-c</dt>
<dd>Show output in a canonical format, with a default delimiter of &#8216;|&#8217;. (same as -n). </dd>
<dt>-d</dt>
<dd>Deletes/Clears the SEL of all records. If the SEL becomes full (free space = 0), it no longer accepts new records, so the SEL should be cleared periodically (use checksel cron script). </dd>
<dt>-e</dt>
<dd>Show Extended sensor descriptions for events if run locally. This option will attempt to get the full sensor description from /var/lib/ipmiutil/sensor_out.txt, and also use its SDR to decode any raw threshold values in the event, if present. </dd>
<dt>-f sel_file</dt>
<dd>Interpret a file containing raw ascii text SEL data captured with ipmiutil sel -r, or some other similar utility. Each line in the file should be in this form, with no leading spaces:<br/>
 04 00 02 76 a9 4a 47 20 00 04 10 09 6f 42 0f ff<br/>
 Lines not in this format will be ignored. </dd>
<dt>-l N</dt>
<dd>Show last N SEL records, in reverse order (newest first). For some BMC implementations, this may not show all N records specified.</dd>
<dt>-n</dt>
<dd>Show output in a nominal/canonical format, with a default delimiter of &#8216;|&#8217;. (same as -c).</dd>
<dt>-r</dt>
<dd>Show the 16 raw hex bytes for each SEL entry. The default is to display interpreted entries, and include relevant hex event bytes.</dd>
<dt>-p</dt>
<dd>Port to use. Defaults to RMCP port 623.</dd>
<dt>-s N</dt>
<dd>Show only SEL events with severity N or greater. Severity 0=INF, 1=MIN, 2=MAJ, 3=CRT. The default is to show all SEL events.</dd>
<dt>-u</dt>
<dd>Show the SEL time as UTC and also get the SEL Time UTC offset if that command is supported. The default is to convert the SEL Time to local time.</dd>
<dt>-v</dt>
<dd>Only show the version information. This shows: the ipmiutil sel utility version, the BMC version, the IPMI version, the SEL version, and the amount of free space in the SEL.</dd>
<dt>-w</dt>
<dd>This option writes SEL records to the Linux syslog (/var/log/messages) or Windows Application Log. It only writes SEL records that have timestamps newer than the last record written to syslog. It saves the last timestamp in an index file named /usr/share/ipmiutil/sel.idx (.\sel.idx in Windows).</dd>
<dt>-x</dt>
<dd>Causes extra debug messages to be displayed.</dd>
<dt>-N nodename</dt>
<dd>Nodename or IP address of the remote target system. If a nodename is specified, IPMI LAN interface is used. Otherwise the local system management interface is used.</dd>
<dt>-U rmt_user</dt>
<dd>Remote username for the nodename given. The default is a null username.</dd>
<dt>-P/-R rmt_pswd</dt>
<dd>Remote password for the nodename given. The default is a null password.</dd>
<dt>-E</dt>
<dd>Use the remote password from Environment variable IPMI_PASSWORD.</dd>
<dt>-F drv_t</dt>
<dd>Force the driver type to one of the followng: imb, va, open, gnu, landesk, lan, lan2, lan2i, kcs, smb. Note that lan2i means lan2 with intelplus. The default is to detect any available driver type and use it.</dd>
<dt>-J</dt>
<dd>Use the specified LanPlus cipher suite (0 thru 17): 0=none/none/none, 1=sha1/none/none, 2=sha1/sha1/none, 3=sha1/sha1/cbc128, 4=sha1/sha1/xrc4_128, 5=sha1/sha1/xrc4_40, 6=md5/none/none, &#8230; 14=md5/md5/xrc4_40. Default is 3.</dd>
<dt>-T</dt>
<dd>Use a specified IPMI LAN Authentication Type: 0=None, 1=MD2, 2=MD5, 4=Straight Password, 5=OEM.</dd>
<dt>-V</dt>
<dd>Use a specified IPMI LAN privilege level. 1=Callback level, 2=User level, 3=Operator level, 4=Administrator level (default), 5=OEM level.</dd>
<dt>-Y</dt>
<dd>Yes, do prompt the user for the IPMI LAN remote password. Alternatives for the password are -E or -P. </dd>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ipmiutil/">ipmiutil</a>(8) <a href="/docs/linux/man/8-ialarms/">ialarms</a>(8) <a href="/docs/linux/man/8-iconfig/">iconfig</a>(8) <a href="/docs/linux/man/8-icmd/">icmd</a>(8) <a href="/docs/linux/man/8-idiscover/">idiscover</a>(8) <a href="/docs/linux/man/8-ievents/">ievents</a>(8) <a href="/docs/linux/man/8-ifru/">ifru</a>(8) <a href="/docs/linux/man/8-igetevent/">igetevent</a>(8) <a href="/docs/linux/man/8-ihealth/">ihealth</a>(8) <a href="/docs/linux/man/8-ilan/">ilan</a>(8) <a href="/docs/linux/man/8-ireset/">ireset</a>(8) <a href="/docs/linux/man/8-isensor/">isensor</a>(8) <a href="/docs/linux/man/8-iserial/">iserial</a>(8) <a href="/docs/linux/man/8-isol/">isol</a>(8) <a href="/docs/linux/man/8-iwdt/">iwdt</a>(8) </p>
<h2>Warnings</h2>
<p>See <a rel="nofollow" href="http://ipmiutil.sourceforge.net/">http://ipmiutil.sourceforge.net/</a> for the latest version of ipmiutil and any bug fix list.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2009 Kontron America, Inc. </p>
<p> See the file COPYING in the distribution for more details regarding redistribution. </p>
<p> This utility is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY.</p>
<h2>Author</h2>
<p>Andy Cress &lt;arcress at users.sourceforge.net&gt;</p>
