---
title: "sg_map(8)"
name: "sg_map"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_map/"
description: "sg_map – displays mapping between Linux sg and other SCSI devices"
---

<p>sg_map &#8211; displays mapping between Linux sg and other SCSI devices</p>
<h2>Synopsis</h2>
<p><code>sg_map</code> [<i>-a</i>] [<i>-h</i>] [<i>-i</i>] [<i>-n</i>] [<i>-scd</i>] [<i>-sd</i>] [<i>-sr</i>] [<i>-st</i>] [<i>-V</i>] [<i>-x</i>]</p>
<h2>Description</h2>
<p>Sometimes it is difficult to determine which SCSI device a sg device name (e.g. /dev/sg0) refers to. This command loops through the sg devices and finds the corresponding SCSI disk, cdrom or tape device name (if any). Scanners are an example of SCSI devices that have no alternate SCSI device name apart from their sg device name. </p>
<p> This utility is deprecated and has not been updated for years, only very obvious bugs will be fixed. Unless a very old version of Linux is being used (e.g. 2.4 series or earlier), then please use a utility like <a href="/docs/linux/man/8-lsscsi/">lsscsi</a>(8) or the facilities offered by <a href="/docs/linux/man/8-udev/">udev</a>(8).</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code></p>
<dd>assume the sg devices have alphabetical device names and loop through /dev/sga, /dev/sgb, etc. Default is numeric scan. Note that sg device nodes with an alphabetical index have been deprecated since the Linux kernel 2.2 series.</p>
<dt><code>-h</code></p>
<dd>print usage message then exit.</p>
<dt><code>-i</code></p>
<dd>in addition do a standard INQUIRY and output vendor, product and revision strings for devices that are found.</p>
<dt><code>-n</code></p>
<dd>assume the sg devices have numeric device names and loop through /dev/sg0, /dev/sg1, etc. Default is numeric scan</p>
<dt><code>-scd</code></p>
<dd>display mappings to SCSI cdrom device names of the form /dev/scd0, /dev/scd1 etc</p>
<dt><code>-sd</code></p>
<dd>display mappings to SCSI disk device names</p>
<dt><code>-sr</code></p>
<dd>display mappings to SCSI cdrom device names of the form /dev/sr0, /dev/sr1 etc</p>
<dt><code>-st</code></p>
<dd>display mappings to SCSI tape device names</p>
<dt><code>-V</code></p>
<dd>print out version string then exit (without further ado).</p>
<dt><code>-x</code></p>
<dd>after each active sg device name is displayed there are five digits: &lt;host_number&gt; &lt;bus&gt; &lt;scsi_id&gt; &lt;lun&gt; &lt;scsi_type&gt;</dl>
<h2>Notes</h2>
<p>If no options starting with &quot;-s&quot; are given then the mapping to all SCSI disk, cdrom and tape device names is shown. </p>
<p> If the device file system (devfs) is present a line noting this is output. The &quot;native&quot; devfs scsi hierarchy makes the relationship between a sg device name and any corresponding disk, cdrom or tape device name easy to establish. This replaces the need for this command. However many applications will continue to look for Linux SCSI device names in their traditional places. [Devfs supplies a compatibility daemon called devfsd whose default configuration adds back the Linux device names in their traditional positions. </p>
<p> Quite often the mapping information can be derived by observing the output of the command: &quot;cat /proc/scsi/scsi&quot;. However if devices have been added since boot this can be deceptive. </p>
<p> In the Linux kernel 2.6 series something close to the mapping shown by this utility can be found by analysing sysfs. The main difference is that sysfs analysis will show the mapping between sg nodes and other SCSI device nodes in terms of major and minor numbers. While major 8, minor 16 will usually be /dev/sdb this is not necessarily so. Facilities associated with udev may assign major 8, minor 16 some other device node name. This version of sg_map has been extended to cope with sparse disk device node names of the form &quot;/dev/sd&lt;str&gt;&quot; where &lt;str&gt; can be one of [a-z,aa-zz,aaa-zzz]. See the sg_map26 utility for a more precise way (i.e. less directory scanning) for mapping between sg device names and higher level names; including finding user defined names. </p>
<p> This utility was written at a time when hotplugging of SCSI devices was not supported in Linux. It used a simple algorithm to scan sg device nodes in ascending numeric or alphabetical order, stopping after there were 5 consecutive errors. </p>
<p> In the Linux kernel 2.6 series, this utility uses sysfs to find which sg device nodes are active and only checks those. Hence there can be large &quot;holes&quot; in the numbering of sg device nodes (e.g. after an adapter has been removed) and still all active sg device nodes will be listed. This utility assumes that sg device nodes are named using the normal conventions and searches from /dev/sg0 to /dev/sg4095 inclusive.</p>
<h2>Examples</h2>
<p>My system has a SCSI disk, a cd writer and a dvd player: </p>
<p>$&nbsp;<wbr>sg_map </p>
<p>#&nbsp;<wbr>Note: the devfs pseudo file system is present </p>
<p>/dev/sg0&nbsp;<wbr>&nbsp;<wbr>/dev/sda </p>
<p>/dev/sg1&nbsp;<wbr>&nbsp;<wbr>/dev/sr0 </p>
<p>/dev/sg2&nbsp;<wbr>&nbsp;<wbr>/dev/sr1 </p>
<p> In order to find which sg device name corresponds to the disk: </p>
<p>$&nbsp;<wbr>sg_map -sd </p>
<p>#&nbsp;<wbr>Note: the devfs pseudo file system is present </p>
<p>/dev/sg0&nbsp;<wbr>&nbsp;<wbr>/dev/sda </p>
<p>/dev/sg1 </p>
<p>/dev/sg2 </p>
<p> The &quot;-x&quot; option gives the following output: </p>
<p>sg_map -x </p>
<p>#&nbsp;<wbr>Note: the devfs pseudo file system is present </p>
<p>/dev/sg0&nbsp;<wbr>&nbsp;<wbr>1 0 1 0&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>/dev/sda </p>
<p>/dev/sg1&nbsp;<wbr>&nbsp;<wbr>2 0 4 0&nbsp;<wbr>&nbsp;<wbr>5&nbsp;<wbr>&nbsp;<wbr>/dev/sr0 </p>
<p>/dev/sg2&nbsp;<wbr>&nbsp;<wbr>2 0 6 0&nbsp;<wbr>&nbsp;<wbr>5&nbsp;<wbr>&nbsp;<wbr>/dev/sr1 </p>
<p> When a SCSI scanner is added the output becomes: </p>
<p>$&nbsp;<wbr>sg_map </p>
<p>#&nbsp;<wbr>Note: the devfs pseudo file system is present </p>
<p>/dev/sg0&nbsp;<wbr>&nbsp;<wbr>/dev/sda </p>
<p>/dev/sg1&nbsp;<wbr>&nbsp;<wbr>/dev/sr0 </p>
<p>/dev/sg2&nbsp;<wbr>&nbsp;<wbr>/dev/sr1 </p>
<p>/dev/sg3 </p>
<p> By process of elimination /dev/sg3 must be the scanner.</p>
<h2>Exit Status</h2>
<p>The exit status of sg_map is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Author</h2>
<p>Written by Douglas Gilbert</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2000-2013 Douglas Gilbert<br />
 This software is distributed under the GPL version 2. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-sg_map26/">sg_map26</a>(8)</code> , <code><a href="/docs/linux/man/8-scsi_info/">scsi_info</a>(8)</code> , <code><a href="/docs/linux/man/8-scsidev/">scsidev</a>(8)</code> , <code><a href="/docs/linux/man/8-devfsd/">devfsd</a>(8)</code> , <code><a href="/docs/linux/man/8-lsscsi/">lsscsi</a>(8)</code> , <code><a href="/docs/linux/man/7-udev/">udev</a>(7)</code> </p>
