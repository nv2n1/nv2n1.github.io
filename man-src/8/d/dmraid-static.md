---
title: "dmraid-static(8)"
name: "dmraid-static"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dmraid-static/"
description: "dmraid – discover, configure and activate software (ATA)RAID"
---

<p>dmraid &#8211; discover, configure and activate software (ATA)RAID</p>
<h2>Synopsis</h2>
<p><code>dmraid</code><br />
&nbsp;<wbr>{-a|&#8211;activate}&nbsp;<wbr>{y|n|yes|no}&nbsp;<wbr><br />
&nbsp;<wbr>[-d|&#8211;debug]&#8230;&nbsp;<wbr>[-v|&#8211;verbose]&#8230;&nbsp;<wbr>[-i|&#8211;ignorelocking]<br />
&nbsp;<wbr>[-f|&#8211;format FORMAT[,FORMAT&#8230;]]<br />
&nbsp;<wbr>[{-P|&#8211;partchar}&nbsp;<wbr>CHAR]<br />
&nbsp;<wbr>[-p|&#8211;no_partitions]<br />
&nbsp;<wbr>[-Z|&#8211;rm_partitions]<br />
&nbsp;<wbr>[&#8211;separator SEPARATOR]<br />
&nbsp;<wbr>[-t|&#8211;test]<br />
&nbsp;<wbr>[-u|&#8211;update_defer]<br />
&nbsp;<wbr>[RAID-set&#8230;] <code>dmraid</code><br />
&nbsp;<wbr>{-b|&#8211;block_devices}<br />
&nbsp;<wbr>[-c|&#8211;display_columns][FIELD[,FIELD&#8230;]]&#8230;<br />
&nbsp;<wbr>[-d|&#8211;debug]&#8230;&nbsp;<wbr>[-v|&#8211;verbose]&#8230;<br />
&nbsp;<wbr>[&#8211;separator SEPARATOR]<br />
&nbsp;<wbr>[device-path&#8230;] <code>dmraid</code><br />
&nbsp;<wbr>{-h|&#8211;help} <code>dmraid</code><br />
&nbsp;<wbr>{-l|&#8211;list_formats}<br />
&nbsp;<wbr>[-d|&#8211;debug]&#8230;&nbsp;<wbr>[-v|&#8211;verbose]&#8230; <code>dmraid</code><br />
&nbsp;<wbr>{-n|&#8211;native_log}<br />
&nbsp;<wbr>[-d|&#8211;debug]&#8230;&nbsp;<wbr>[-v|&#8211;verbose]&#8230;&nbsp;<wbr>[-i|&#8211;ignorelocking]<br />
&nbsp;<wbr>[-f|&#8211;format FORMAT[,FORMAT&#8230;]]<br />
&nbsp;<wbr>[&#8211;separator SEPARATOR]<br />
&nbsp;<wbr>[device-path&#8230;] <code>dmraid</code><br />
&nbsp;<wbr>{-R| &#8211;rebuild}<br />
&nbsp;<wbr>RAID-set<br />
&nbsp;<wbr>[device-path]<br />
&nbsp;<wbr>[-u|&#8211;update_defer] <code>dmraid</code><br />
&nbsp;<wbr>{-x| &#8211;remove}<br />
&nbsp;<wbr>[RAID-set] <code>dmraid</code><br />
&nbsp;<wbr>-f FORMAT-handler {-C| &#8211;create} set<br />
&nbsp;<wbr>&#8211;type raidlevel<br />
&nbsp;<wbr>[&#8211;size setsize &#8211;str[ide]&nbsp;<wbr>stridesize]&nbsp;<wbr><br />
&nbsp;<wbr>&#8211;disk&nbsp;<wbr>&quot;device-path, device-path&nbsp;<wbr>[, device-path &#8230;]&quot; <code>dmraid</code> [ -f|&#8211;format FORMAT-handler] -S|&#8211;spare [RAID-set] -M|&#8211;media &quot;device-path&quot; <code>dmraid</code><br />
&nbsp;<wbr>{-r|&#8211;raid_devices}<br />
&nbsp;<wbr>[-c|&#8211;display_columns][FIELD[,FIELD&#8230;]]&#8230;<br />
&nbsp;<wbr>[-d|&#8211;debug]&#8230;&nbsp;<wbr>[-v|&#8211;verbose]&#8230;&nbsp;<wbr>[-i|&#8211;ignorelocking]<br />
&nbsp;<wbr>[-D|&#8211;dump_metadata]<br />
&nbsp;<wbr>[-f|&#8211;format FORMAT[,FORMAT&#8230;]]<br />
&nbsp;<wbr>[&#8211;separator SEPARATOR]<br />
&nbsp;<wbr>[device-path&#8230;] <code>dmraid</code><br />
&nbsp;<wbr>{-r|&#8211;raid_devices}<br />
&nbsp;<wbr>[-d|&#8211;debug]&#8230;&nbsp;<wbr>[-v|&#8211;verbose]&#8230;&nbsp;<wbr>[-i|&#8211;ignorelocking]<br />
&nbsp;<wbr>[-E|&#8211;erase_metadata]<br />
&nbsp;<wbr>[-f|&#8211;format FORMAT[,FORMAT&#8230;]]<br />
&nbsp;<wbr>[&#8211;separator SEPARATOR]<br />
&nbsp;<wbr>[device-path&#8230;] <code>dmraid</code><br />
&nbsp;<wbr>{-s|&#8211;sets}&#8230;[a|i|active|inactive]<br />
&nbsp;<wbr>[-c|&#8211;display_columns][FIELD[,FIELD&#8230;]]&#8230;<br />
&nbsp;<wbr>[-d|&#8211;debug]&#8230;&nbsp;<wbr>[-v|&#8211;verbose]&#8230;&nbsp;<wbr>[-i|&#8211;ignorelocking]<br />
&nbsp;<wbr>[-f|&#8211;format FORMAT[,FORMAT&#8230;]]<br />
&nbsp;<wbr>[-g|&#8211;display_group]<br />
&nbsp;<wbr>[&#8211;separator SEPARATOR]<br />
&nbsp;<wbr>[RAID-set&#8230;] <code>dmraid</code><br />
&nbsp;<wbr>{-V/&#8211;version} </p>
<h2>Description</h2>
<p>dmraid discovers block and software RAID devices (e.g., ATARAID) by using multiple different metadata format handlers which support various formats (e.g., Highpoint 37x series). It offers activating RAID sets made up by 2 or more discovered RAID devices, display properties of devices and sets (see option <code>-l</code> for supported metadata formats). Block device access to activated RAID sets occurs via device-mapper nodes /dev/mapper/RaidSetName. RaidSetName starts with the format name (see <code>-l</code> option) which can be used to access all RAID sets of a specific format easily with certain options (e.g., <code>-a</code> below).</p>
<h3>Options</h3>
<dl>
<dt><i>-a, &#8211;activate {y|n} [RAID set&#8230;]</i></p>
<dd>Activates or deactivates all or particular software RAID set. In case metadata format handlers are chosen with <code>-f</code> , only RAID sets with such format(s) can be activated or deactivated. Useful if devices have multiple metadata signatures. When activating RAID sets, <code>-p</code> disables the activation of partitions on them, and <code>-Z</code> will make dmraid tell the kernel to remove the partitions from the disks underlying the set, i.e. if sda is part of the set, remove sda1, sda2, etc. This prevents applications from directly accessiong the disks bypassing dmraid. RAID set names given on command line don&#8217;t need to be fully specified (e.g., &quot;dmraid -ay sil&quot; would activate all discovered Silicon Image Medley RAID sets). Option <code>-u</code> defers metadata update in case of rebuild is triggered parallelly with activation. Avoids metadata update to &quot;OK&quot; state if volume is not registered to the event monitoring. Useful if volume is activating at early stage of booting process when registration to the event monitoring is impossible.</p>
<dt><i>{-b|&#8211;block_devices} [device-path&#8230;]</i></p>
<dd>List all or particular discovered block devices with their properties (size, serial number). Add <code>-c</code> to display block device names only and <code>-cc</code> for CSV column output of block device properties. See description of <code>-c</code> below for FIELD identifiers.</p>
<dt><i>[-d|&#8211;debug]&#8230;</i></p>
<dd>Enable debugging output. Option can be given multiple times increasing the debug output level.</p>
<dt><i>[-c|&#8211;display_columns][FIELD[,FIELD&#8230;]]&#8230;</i></p>
<dd>Display properties of block devices, RAID sets and devices in column(s). Optional list specifying which FIELDs to display.<br />
 For <code>-b:</code><br />
 d[evpath]|p[ath], sec[tors]|si[ze], ser[ialnumber].<br />
 For <code>-r:</code><br />
 de[vpath]|p[ath], f[ormat], r[aidname], t[ype], st[atus], se[ctors]|si[ze], da[taoffset]|o[ffset].<br />
 For <code>-s:</code><br />
 f[ormat], r[aidname], t[ype], sta[tus], str[ide], se[ctors]|si[ze], su[bsets], d[evices], sp[ares]. </p>
<dt><i>[-f|&#8211;format FORMAT[,FORMAT&#8230;]]</i></p>
<dd>Use metadata format handler(s) to discover RAID devices. See <code>-l</code> for a list of supported format handler names. This is useful to select particular formats in case multiple metadata signatures are found on a device. A comma separated list of format names can be specified which may not contain white space.</p>
<dt><i>{-h|&#8211;help}</i></p>
<dd>Display help text.</p>
<dt><i>{-i|&#8211;ignorelocking}</i></p>
<dd>Don&#8217;t take out any locks. Useful in early boot where no read/write access to /var is available.</p>
<dt><i>{-l|&#8211;list_formats}</i></p>
<dd>List all available metadata format handlers with their names and descriptions. Supported RAID levels are listed in parenthesis:<br />
 S: Span (concatenation)<br />
 0: RAID0 (stripe)<br />
 1: RAID1 (mirror)<br />
 10: RAID10 (mirror on top of stripes)<br />
 01: RAID10 (stripe on top of mirrors) Note: Intel OROM displays this as RAID10</p>
<dt><i>{-n|&#8211;native_log} [device-path&#8230;]</i></p>
<dd>Display metadata in native, vendor-specific format. In case a metadata format handler is chosen with <code>-f</code> only RAID devices with such format will be displayed in native format. If device-path(s) is/are given on the command line, native metadata output is restricted to those listed.</p>
<dt><i>[{-P|&#8211;partchar} CHAR]</i></p>
<dd>Use CHAR as the separator between the device name and the partition number.</p>
<dt><i>{-R| &#8211;rebuild} RAID-set [device-path]</i></p>
<dd>Rebuild raid array after a drive has failed and a new drive is added. For Intel chipset based systems, there are two methods in which a new drive is added to the system. Option <code>-u</code> defers metadata update in case of rebuild is triggered. Avoids metadata update to &quot;OK&quot; state if volume is not registered to the event monitoring. 1. Using OROM to identify a new drive<br />
&nbsp;<wbr>During system reboot, enter OROM and mark the new drive as the rebuild drive.&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>After booting to the OS, use the dmraid command to rebuild.<br />
&nbsp;<wbr>Example: dmraid -R raid_set&nbsp;<wbr> 2. Using dmraid to identify a new drive<br />
&nbsp;<wbr>Boot to the OS and use the dmraid command with the new drive as the second parameter.<br />
&nbsp;<wbr>Example: dmraid -R raid_set&nbsp;<wbr>/dev/sdc 3. Using hot spare drive<br />
&nbsp;<wbr>Mark a drive as hot spare using the&nbsp;<wbr>&quot;dmraid -f isw -S&quot;&nbsp;<wbr>command. Then use the dmraid command to start the rebuild.<br />
&nbsp;<wbr>Example: dmraid -R raid_set</p>
<dt><i>{-x|&#8211;remove} [RAID-set]</i></p>
<dd>Delete one or all existing software RAID devices from the metadata.</p>
<dt><i>-f FORMAT-handler {-C|&#8211;create} &#8211;type raidlevel [&#8211;size=setsize &#8211;strip stripsize] &#8211;disk[s] device-path, device-path [,device-path]</i></p>
<dd>Delete one or all existing Configure a software RAID device and store the configuration data in a group of hard drive devices consisting of this array. This command requires the following options: -f FORMAT-handler<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>metadata format (see &quot;dmraid -l&quot;)</p>
<p> &#8211;type digit[digit&#8230;]<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>specify the raid level of the software RAID set. </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0: raid0</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1: raid1</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>5: raid5</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>01: raid01 (isw raid10)</p>
<p> &#8211;size: [digits[k|K|m|M|g|G][b|B]]<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>specify the size of the RAID set.The number is an integer followed by [kKmMgG] and/or [bB].</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>b: byte (default)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>B: block (512 bytes)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>K or K: on the base of 1024</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>m or M: on the base of 1024*1024</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>g or G: on the base of 1024*1024*1024</p>
<p> If this option is missing, it&#8217;s set to the default value pre-configured by the vendor. Note that different vendors may apply different constraints on the granularity of the size or the minimal value.<br />
 &#8211;strip: [digits[k|K|m|M|g|G][b|B]]<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>specify the strip size of a RAID1, RAID5, and RAID10 RAID set (as above)</p>
<p> &#8211;disk: device-path[{,| }device-path&#8230;]<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>specify the array of the hard drives, e.g. /dev/sda.</p>
<dt><i>-f FORMAT-handler -S -M device-path</i></p>
<dd><i>-S -M device-path</i> This command adds hot spare support for one or more RAID sets. 1. When used with a format handler, which supports hot spare sets (e.g. isw), a hot spare is marked to be used when rebuilding any RAID set of that format. 2. When used when specifying a RAID set, the drive is added to that RAID set and will be used only to rebuild that set. Note: If the specified name does not match an existing RAID-set, a set with the new name will be created.</p>
<dt><i>{-r|&#8211;raid_devices} [device-path&#8230;]</i></p>
<dd>List all discovered RAID devices with format, RAID level, sectors used and data offset into the device. In case a metadata format handler is chosen with <code>-f</code> , only RAID devices with such format can be discovered. Useful if devices have multiple metadata signatures. If <code>-D</code> is added to <code>-r</code> the RAID metadata gets dumped into a subdirectory named dmraid.format_name (e.g. format_name = isw) in files named devicename.dat. The byte offset where the metadata is located on the device is written into files named devicename.offset and the size of the device in sectors into files named devicename.size. If <code>-E</code> is added to <code>-r</code> the RAID metadata on the devices gets conditionally erased. Useful to erase old metadata after new one of different type has been stored on a device in order to avoid discovering both. If you enter <code>-E</code> option <code>-D</code> will be enforced in order to have a fallback in case the wrong metadata got erased. Manual copying back onto the device is needed to recover from erasing the wrong metadata using the dumped files devicename_formatname.dat and devicename_formatname.offset. Eg, to restore all *.dat files in the working directory to the respective devices:  If device-path(s) is/are given on the command line, the above actions are restricted to those listed. Add <code>-c</code> to display RAID device names only and <code>-cc</code> for CSV column output of RAID device properties. See description of <code>-c</code> above for FIELD identifiers.</p>
<dt><i>&#8211;separator SEPARATOR</i></p>
<dd>Use SEPARATOR as a delimiter for all options taking or displaying lists.</p>
<dt><i>-s&#8230; [a|i] [RAID-set&#8230;]</i></p>
<dd>Display properties of RAID sets. Multiple RAID set names can be given on the command line which don&#8217;t need to be fully specified (e.g., &quot;dmraid -s hpt&quot; would display all discovered Highpoint RAID sets). Enter <code>-s</code> twice to display RAID subsets too. Add <code>-c</code> to display names of RAID sets only, <code>-cc</code> for CSV column output of RAID set properties and <code>-ccc</code> for inclusion of block devices in the listing. Doesn&#8217;t imply <code>-s -s</code> to show RAID subsets (implied for group sets, e.g. isw). Add <code>-g</code> to include information about group RAID sets (as with Intel Software RAID) in the listing. See description of <code>-c</code> above for FIELD identifiers. Note: Size is given in sectors (not bytes).</p>
<dt><i>[-v|&#8211;verbose]&#8230;</i></p>
<dd>Enable verbose runtime information output. Option can be given multiple times increasing the verbosity level. </p>
<h2>Examples</h2>
<p>&quot;dmraid -l&quot; lists all supported metadata formats with their names along with some descriptive information, e.g.:<br />
 hpt37x : (+) Highpoint HPT37X<br />
 hpt45x : (+) Highpoint HPT45X<br />
 isw : (+) Intel Software RAID<br />
 lsi : (0) LSI Logic MegaRAID<br />
 nvidia : (+) NVidia RAID<br />
 pdc : (+) Promise FastTrack<br />
 sil : (+) Silicon Image(tm) Medley(tm)<br />
 via : (+) VIA Software RAID<br />
 dos : (+) DOS partitions on SW RAIDs<br />
 (0): Discover, (+): Discover+Activate &quot;dmraid -ay&quot; activates all software RAID sets discovered. &quot;dmraid -an&quot; deactivates all active software RAID sets which are not open (e.g., mounted filesystem on them). &quot;dmraid -ay -f pdc&quot; (pdc looked up from &quot;dmraid -l&quot;) activates all software RAID sets with Promise format discovered and ignores all other supported formats. &quot;dmraid -r&quot; discovers all software RAID devices supported on your system, e.g.:<br />
 /dev/dm-46: hpt45x, &quot;hpt45x_chidjhaiaa-0&quot;, striped, ok, 320172928 sectors, data@ 0<br />
 /dev/dm-50: hpt45x, &quot;hpt45x_chidjhaiaa-0&quot;, striped, ok, 320172928 sectors, data@ 0<br />
 /dev/dm-54: hpt45x, &quot;hpt45x_chidjhaiaa-1&quot;, striped, ok, 320172928 sectors, data@ 0<br />
 /dev/dm-58: hpt45x, &quot;hpt45x_chidjhaiaa-1&quot;, striped, ok, 320172928 sectors, data@ 0 &quot;dmraid -s -s hpt45x_chidjhaiaa&quot; displays properties of set &quot;hpt45x_chidjhaiaa&quot;, e.g.:<br />
 *** Superset<br />
 name : hpt45x_chidjhaiaa<br />
 size : 640345856<br />
 stride : 128<br />
 type : raid10<br />
 status : ok<br />
 subsets: 2<br />
 dev : 4<br />
 spare : 0<br />
 &#8212;&gt; Subset<br />
 name : hpt45x_chidjhaiaa-0<br />
 size : 640345856<br />
 stride : 128<br />
 type : stripe<br />
 status : ok<br />
 subsets: 0<br />
 dev : 2<br />
 spare : 0<br />
 &#8212;&gt; Subset<br />
 name : hpt45x_chidjhaiaa-1<br />
 size : 640345856<br />
 stride : 128<br />
 type : stripe<br />
 status : ok<br />
 subsets: 0<br />
 dev : 2<br />
 spare : 0<br />
 &quot;dmraid -s -ccs hpt45&quot; displays properties in column format of all sets and subsets with hpt45* format, e.g.:<br />
 hpt45x_chidjhaiaa,640345856,128,raid10,ok,4,0<br />
 hpt45x_chidjhaiaa-a,640345856,128,stripe,ok,2,0<br />
 hpt45x_chidjhaiaa-b,640345856,128,stripe,ok,2,0 &quot;dmraid -r &#8211;sep : -cpath:size&quot; display paths and sizes in sectors for RAID devices in column format using &#8216;:&#8217; as a delimiter, e.g.:<br />
 /dev/dm-8:320173055<br />
 /dev/dm-12:320173055<br />
 /dev/dm-22:320173055<br />
 /dev/dm-26:320173055<br />
 /dev/dm-30:586114703<br />
 /dev/dm-34:586114703<br />
 /dev/dm-38:586114703<br />
 /dev/dm-42:586114703<br />
 /dev/dm-46:156301487<br />
 /dev/dm-50:156301487<br />
 /dev/dm-54:390624896<br />
 /dev/dm-58:390624896<br />
 /dev/dm-62:390624896<br />
 /dev/dm-66:390624896 &quot;dmraid -f isw -C Raid0 &#8211;type 0 &#8211;strip 8k &#8211;size 20g &#8211;disk &quot;/dev/sdb /dev/sdc&quot;&quot; creates an ISW volume with a name of &quot;Raid0&quot;, 20Gig bytes in total, and 8kilo bytes strip size on two disks. &quot;dmraid -f isw -C Test0 &#8211;type 0 &#8211;disk &quot;/dev/sdd /dev/sde&quot;&quot; creates an ISW volume with the default size and strip size. &quot;dmraid -f isw -C Test10 &#8211;type 01 &#8211;strip 128B &#8211;disk &quot;/dev/sda /dev/sdb /dev/sdc /dev/sdd&quot; creates a stacked RAID device, RAID10 (isw format), with a name of &quot;Test10&quot;, 128 blocks (512bytes) strip size , and the default volume size on 4 disks. &quot;dmraid -f isw -S -M /dev/sde&quot; marks the device /dev/sde as a hot spare for rebuild &quot;dmraid -R isw_djaggchdde_RAID1 /dev/sde&quot; starts rebuild of the RAID volume on device /dev/sde </p>
<h2>Diagnostics</h2>
<p>dmraid returns an exit code of 0 for success or 1 for error.</p>
<h2>Author</h2>
<p>Heinz Mauelshagen &lt;Mauelshagen [at] RedHat.com&gt;</p>
