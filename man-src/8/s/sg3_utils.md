---
title: "sg3_utils(8)"
name: "sg3_utils"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg3_utils/"
description: "sg3_utils – a package of utilities for sending SCSI commands"
---

<p>sg3_utils &#8211; a package of utilities for sending SCSI commands</p>
<h2>Synopsis</h2>
<p><code>sg_*</code> [<i>&#8211;help</i>] [<i>&#8211;hex</i>] [<i>&#8211;maxlen=LEN</i>] [<i>&#8211;raw</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] [<i>OTHER_OPTIONS</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>sg3_utils is a package of utilities that send SCSI commands to the given <i>DEVICE</i> via a SCSI pass through interface provided by the host operating system. </p>
<p> The names of all utilities start with &quot;sg&quot; and most start with &quot;sg_&quot; often followed by the name, or a shortening of the name, of the SCSI command that they send. For example the &quot;sg_verify&quot; utility sends the SCSI VERIFY command. A mapping between SCSI commands and the sg3_utils utilities that issue them is shown in the COVERAGE file. </p>
<p> SCSI draft standards can be found at <a rel="nofollow" href="http://www.t10.org">http://www.t10.org</a> . The standards themselves can be purchased from ANSI and other standards organizations. A good overview of various SCSI standards can be seen in <a rel="nofollow" href="http://www.t10.org/scsi-3.htm">http://www.t10.org/scsi-3.htm</a> with the SCSI command sets in the upper part of the diagram. SCSI commands in common with all device types can be found in SPC of which SPC-4 is the latest major version. Block device specific commands (e.g. as used by disks) are in SBC, those for tape drives in SSC and those for CD/DVD/BD drives in MMC. </p>
<p> It is becoming more common to control ATA disks with the SCSI command set. This involves the translation of SCSI commands to their corresponding ATA equivalents (and that is an imperfect mapping in some cases). The relevant standard is called SCSI to ATA Translation (SAT and SAT-2 are now standards at INCITS(ANSI) and ISO while SAT-3 is at the draft stage). The logic to perform the command translation is often called a SAT Layer or SATL and may be within an operating system, in host bus adapter firmware or in an external device (e.g. associated with a SAS expander). See <a rel="nofollow" href="http://www.t10.org">http://www.t10.org</a> for more information. </p>
<p> There is some support for SCSI tape devices but not for their basic commands. The reader is referred to the &quot;mt&quot; utility. </p>
<p> There are two generations of command line option usage. The newer utilities (written since July 2004) use the getopt_long() function to parse command line options. With that function, each option has two representations: a short form (e.g. &#8216;-v&#8217;) and a longer form (e.g. &#8216;&#8211;verbose&#8217;). If an argument is required then it follows a space (optionally) in the short form and a &quot;=&quot; in the longer form (e.g. in the sg_verify utility &#8216;-l 2a6h&#8217; and &#8216;&#8211;lba=2a6h&#8217; are equivalent). Note that with getopt_long(), short form options can be elided, for example: &#8216;-all&#8217; is equivalent to &#8216;-a -l -l&#8217;. The <i>DEVICE</i> argument may appear after, between or prior to any options. </p>
<p> The older utilities, such as sg_inq, had individual command line processing code typically based on a single &quot;-&quot; followed by one or more characters. If an argument is needed then it follows a &quot;=&quot; (e.g. &#8216;-p=1f&#8217; in sg_modes with its older interface). Various options can be elided as long as it is not ambiguous (e.g. &#8216;-vv&#8217; to increase the verbosity). </p>
<p> Over time the command line interface of these older utilities became messy and overloaded with options. So in sg3_utils version 1.23 the command line interface of these older utilities was altered to have both a cleaner getopt_long() interface and their older interface for backward compatibility. By default these older utilities use their getopt_long() based interface. That can be overridden by defining the SG3_UTILS_OLD_OPTS environment variable or using &#8216;-O&#8217; or &#8216;&#8211;old&#8217; as the first command line option. The man pages of the older utilities documents the details. </p>
<p> Several sg3_utils utilities are based on the Unix dd command (e.g. sg_dd) and permit copying data at the level of SCSI READ and WRITE commands. sg_dd is tightly bound to Linux and hence is not ported to other OSes. A more generic utility (than sg_dd) called ddpt in a package of the same name has been ported to other OSes.</p>
<h2>Linux Device Naming</h2>
<p>Normal disk block devices have names like /dev/sda, /dev/sdb, /dev/sdc, etc. SCSI disks in Linux have always had names like that but in recent Linux kernels (e.g. lk 2.6 series) it is becoming more common for almost all disks to be named like that. Partitions within a disk are specified by a number appended to the device name, starting at 1 (e.g. /dev/sda1 ). </p>
<p> Tape drives are named /dev/st&lt;num&gt; or /dev/nst&lt;num&gt; where &lt;num&gt; starts at zero. Additionally one letter from this list: &quot;lma&quot; may be appended to the name. CD, DVD and BD readers (and writers) are named /dev/sr&lt;num&gt; where &lt;num&gt; start at zero. There are less used SCSI device type names, the dmesg and the lsscsi commands may help to find if any are attached to a running system. </p>
<p> There is also a SCSI device driver which offers alternate generic access to SCSI devices. It uses names of the form /dev/sg&lt;num&gt; where &lt;num&gt; starts at zero. The &quot;lsscsi -g&quot; command may be useful in finding these and which generic name corresponds to a device type name (e.g. /dev/sg2 may correspond to /dev/sda). In the lk 2.6 series a block SCSI generic driver was introduced and its names are of the form /dev/bsg/&lt;h:c:t:l&gt; where h, c, t and l are numbers. Again see the lsscsi command to find the correspondence between that SCSI tuple (i.e. &lt;h:c:t:l&gt;) and alternate device names. </p>
<p> Prior to the Linux kernel 2.6 series these utilities could only use generic device names (e.g. /dev/sg1 ). In almost all cases in the Linux kernel 2.6 series, any device name can be used by these utilities.</p>
<h2>Windows Device Naming</h2>
<p>Storage and related devices can have several device names in Windows. Probably the most common in the volume name (e.g. &quot;D:&quot;). There are also a &quot;class&quot; device names such as &quot;PhysicalDrive&lt;n&gt;&quot;, &quot;CDROM&lt;n&gt;&quot; and &quot;TAPE&lt;n&gt;&quot;. &lt;n&gt; is an integer starting at 0 allocated in ascending order as devices are discovered (and sometimes rediscovered). </p>
<p> Some storage devices have a SCSI lower level device name which starts with a SCSI (pseudo) adapter name of the form &quot;SCSI&lt;n&gt;:&quot;. To this is added sub-addressing in the form of a &quot;bus&quot; number, a &quot;target&quot; identifier and a LUN (Logical Unit Number). The &quot;bus&quot; number is also known as a &quot;PathId&quot;. These are assembled to form a device name of the form: &quot;SCSI&lt;n&gt;:&lt;bus&gt;,&lt;target&gt;,&lt;lun&gt;&quot;. The trailing &quot;,&lt;lun&gt;&quot; may be omitted in which case a LUN of zero is assumed. This lower level device name cannot often be used directly since Windows blocks attempts to use it if a class driver has &quot;claimed&quot; the device. There are SCSI device types (e.g. Automation/Drive interface type) for which there is no class driver. At least two transports (&quot;bus types&quot; in Windows jargon): USB and IEEE 1394 do not have a &quot;scsi&quot; device names of this form. </p>
<p> In keeping with DOS file system conventions, the various device names can be given in upper, lower or mixed case. Since &quot;PhysicalDrive&lt;n&gt;&quot; is tedious to write, a shortened form of &quot;PD&lt;n&gt;&quot; is permitted by all utilities in this package. </p>
<p> A single device (e.g. a disk) can have many device names. For example: &quot;PD0&quot; can also be &quot;C:&quot;, &quot;D:&quot; and &quot;SCSI0:0,1,0&quot;. The two volume names reflect that the disk has two partitions on it. Disk partitions that are not recognized by Windows are not usually given a volume name. However Vista does show a volume name for a disk which has no partitions recognized by it and when selected invites the user to format it (which may be rather unfriendly to other OSes). </p>
<p> These utilities assume a given device name is in the Win32 device namespace. To make that explicit &quot;\.\&quot; can be prepended to the device names mentioned in this section. Beware that backslash is an escape character in Unix like shells and the C programming language. In a shell like Msys (from MinGW) each backslash may need to be typed twice. </p>
<p> The sg_scan utility within this package lists out Windows device names in a form that is suitable for other utilities in this package to use.</p>
<h2>Freebsd Device Naming</h2>
<p>SCSI disks have block names of the form /dev/da&lt;num&gt; where &lt;num&gt; is an integer starting at zero. The &quot;da&quot; is replaced by &quot;sa&quot; for SCSI tape drives and &quot;cd&quot; for SCSI CD/DVD/BD drives. Each SCSI device has a corresponding pass-through device name of the form /dev/pass&lt;num&gt; where &lt;num&gt; is an integer starting at zero. The &quot;camcontrol devlist&quot; command may be useful for finding out which SCSI device names are available and the correspondence between class and pass-through names.</p>
<h2>Solaris Device Naming</h2>
<p>SCSI device names below the /dev directory have a form like: c5t4d3s2 where the number following &quot;c&quot; is the controller (HBA) number, the number following &quot;t&quot; is the target number (from the SCSI parallel interface days) and the number following &quot;d&quot; is the LUN. Following the &quot;s&quot; is the slice number which is related to a partition and by convention &quot;s2&quot; is the whole disk. </p>
<p> OpenSolaris also has a c5t4d3p2 form where the number following the &quot;p&quot; is the partition number apart from &quot;p0&quot; which is the whole disk. So a whole disk may be referred to as either c5t4d3, c5t4d3s2 or c5t4d3p0 . </p>
<p> And these device names are duplicated in the /dev/dsk and /dev/rdsk directories. The former is the block device name and the latter is for &quot;raw&quot; (or char device) access which is what sg3_utils needs. So in OpenSolaris something of the form &#8216;sg_inq /dev/rdsk/c5t4d3p0&#8217; should work. If it doesn&#8217;t work then add a &#8216;-vvv&#8217; option for more debug information. Trying this form &#8216;sg_inq /dev/dsk/c5t4d3p0&#8217; (note &quot;rdsk&quot; changed to &quot;dsk&quot;) will result in an &quot;inappropriate ioctl for device&quot; error. </p>
<p> The device names within the /dev directory are typically symbolic links to much longer topological names in the /device directory. In Solaris cd/dvd/bd drives seem to be treated as disks and so are found in the /dev/rdsk directory. Tape drives appear in the /dev/rmt directory. </p>
<p> There is also a sgen (SCSI generic) driver which by default does not attach to any device. See the /kernel/drv/sgen.conf file to control what is attached. Any attached device will have a device name of the form /dev/scsi/c5t4d3 . </p>
<p> Listing available SCSI devices in Solaris seems to be a challenge. &quot;Use the &#8216;format&#8217; command&quot; advice works but seems a very dangerous way to list devices. [It does prompt again before doing any damage.] &#8216;devfsadm -Cv&#8217; cleans out the clutter in the /dev/rdsk directory, only leaving what is &quot;live&quot;. The &quot;cfgadm -v&quot; command looks promising.</p>
<h2>Exit Status</h2>
<p>To aid scripts that call these utilities, the exit status is set to indicate success (0) or failure (1 or more). Note that some of the lower values correspond to the SCSI sense key values. The exit status values are:</p>
<dl>
<dt><code>0</code></p>
<dd>success</p>
<dt><code>1</code></p>
<dd>syntax error. Either illegal command line options, options with bad arguments or a combination of options that is not permitted.</p>
<dt><code>2</code></p>
<dd>the <i>DEVICE</i> reports that it is not ready for the operation requested. The device may be in the process of becoming ready (e.g. spinning up but not at speed) so the utility may work after a wait.</p>
<dt><code>3</code></p>
<dd>the <i>DEVICE</i> reports a medium or hardware error (or a blank check). For example an attempt to read a corrupted block on a disk will yield this value.</p>
<dt><code>5</code></p>
<dd>the <i>DEVICE</i> reports an &quot;illegal request&quot; with an additional sense code other than &quot;invalid command operation code&quot;. This is often a supported command with a field set requesting an unsupported capability. For commands that require a &quot;service action&quot; field this value can indicate that the command with that service action value is not supported.</p>
<dt><code>6</code></p>
<dd>the <i>DEVICE</i> reports a &quot;unit attention&quot; condition. This usually indicates that something unrelated to the requested command has occurred (e.g. a device reset) potentially before the current SCSI command was sent. The requested command has not been executed by the device. Note that unit attention conditions are usually only reported once by a device.</p>
<dt><code>9</code></p>
<dd>the <i>DEVICE</i> reports an illegal request with an additional sense code of &quot;invalid command operation code&quot; which means that it doesn&#8217;t support the requested command.</p>
<dt><code>11</code></p>
<dd>the <i>DEVICE</i> reports an aborted command. In some cases aborted commands can be retried immediately (e.g. if the transport aborted the command due to congestion).</p>
<dt><code>14</code></p>
<dd>the <i>DEVICE</i> reports a miscompare sense key. VERIFY and COMPARE AND WRITE commands may report this.</p>
<dt><code>15</code></p>
<dd>the utility is unable to open, close or use the given <i>DEVICE</i>. The given file name could be incorrect or there may be permission problems. Adding the &#8216;-v&#8217; option may give more information.</p>
<dt><code>20</code></p>
<dd>the <i>DEVICE</i> reports it has a check condition but &quot;no sense&quot; and non-zero information in its additional sense codes. Some polling commands (e.g. REQUEST SENSE) can receive this response.</p>
<dt><code>21</code></p>
<dd>the <i>DEVICE</i> reports a &quot;recovered error&quot;. The requested command was successful. Most likely a utility will report a recovered error to stderr and continue, probably leaving the utility with an exit status of 0 .</p>
<dt><code>33</code></p>
<dd>the command sent to <i>DEVICE</i> has timed out.</p>
<dt><code>97</code></p>
<dd>a SCSI command response failed sanity checks.</p>
<dt><code>98</code></p>
<dd>the <i>DEVICE</i> reports it has a check condition but the error doesn&#8217;t fit into any of the above categories.</p>
<dt><code>99</code></p>
<dd>any errors that can&#8217;t be categorized into values 1 to 98 may yield this value. This includes transport and operating system errors after the command has been sent to the device.</p>
<dt><code>126</code></p>
<dd>the utility was found but could not be executed. That might occur if the executable does not have execute permissions.</p>
<dt><code>127</code></p>
<dd>This is the exit status for utility not found. That might occur when a script calls a utility in this package but the PATH environment variable has not been properly set up, so the script cannot find the executable.</p>
<dt><code>128 + &lt;signum&gt;</code></p>
<dd>If a signal kills a utility then the exit status is 128 plus the signal number. For example if a segmentation fault occurs then a utility is typically killed by SIGSEGV which according to &#8216;man 7 signal&#8217; has an associated signal number of 11; so the exit status will be 139 .</p>
<dt><code>255</code></p>
<dd>the utility tried to yield an exit status of 255 or larger. That should not happen; given here for completeness.</dl>
<p> Most of the error conditions reported above will be repeatable (an example of one that is not is &quot;unit attention&quot;) so the utility can be run again with the &#8216;-v&#8217; option (or several) to obtain more information.</p>
<h2>Common Options</h2>
<p>Arguments to long options are mandatory for short options as well. In the short form an argument to an option uses zero or more spaces as a separator (i.e. the short form does not use &quot;=&quot; as a separator). </p>
<p> If an option takes a numeric argument then that argument is assumed to be decimal unless otherwise indicated (e.g. with a leading &quot;0x&quot;, a trailing &quot;h&quot; or as noted in the usage message). </p>
<p> Some options are used uniformly in most of the utilities in this package. Those options are listed below. Note that there are some exceptions.</p>
<dl>
<dt><code>-h</code>, <code>-?</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit. In a few older utilities the &#8216;-h&#8217; option requests hexadecimal output. In these cases the &#8216;-?&#8217; option will output the usage message then exit.</p>
<dt><code>-H</code>, <code>&#8211;hex</code></p>
<dd>for SCSI commands that yield a non-trivial response, print out that response in ASCII hexadecimal.</p>
<dt><code>-m</code>, <code>&#8211;maxlen</code>=<i>LEN</i></p>
<dd>several important SCSI commands (e.g. INQUIRY and MODE SENSE) have response lengths that vary depending on many factors, only some of which these utilities take into account. The maximum response length is typically specified in the &#8216;allocation length&#8217; field of the cdb. In the absence of this option, several utilities use a default allocation length (sometimes recommended in the SCSI draft standards) or a &quot;double fetch&quot; strategy. See <a href="/docs/linux/man/8-sg_logs/">sg_logs</a>(8) for its description of a &quot;double fetch&quot; strategy. These techniques are imperfect and in the presence of faulty SCSI targets can cause problems (e.g. some USB mass storage devices freeze if they receive an INQUIRY allocation length other than 36). Also use of this option disables any &quot;double fetch&quot; strategy that may have otherwise been used.</p>
<dt><code>-r</code>, <code>&#8211;raw</code></p>
<dd>for SCSI commands that yield a non-trivial response, output that response in binary to stdout. If any error messages or warning are produced they are usually sent to stderr. Some utilities that consume data to send to the device along with the SCSI command, use this option to provide that data or indicate that it can be read from stdin.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the level of verbosity, (i.e. debug output). Can be used multiple times to further increase verbosity. The additional output is usually sent to stderr.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit. Each utility has its own version number and date of last code change.</dl>
<h2>Numeric Arguments</h2>
<p>Many utilities have command line options that take numeric arguments. These numeric arguments can be large values (e.g. a logical block address (LBA) on a disk) and can be inconvenient to enter in the default decimal representation. So various other representations are permitted. </p>
<p> Multiplicative suffixes are accepted. They are one, two or three letter strings appended directly after the number to which they apply: </p>
<p>c C&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*1 </p>
<p>w W&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*2 </p>
<p>b B&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*512 </p>
<p>k K KiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*1024 </p>
<p>KB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*1000 </p>
<p>m M MiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*1048576 </p>
<p>MB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*1000000 </p>
<p>g G GiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*(2^30) </p>
<p>GB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*(10^9) </p>
<p>t T TiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*(2^40) </p>
<p>TB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*(10^12) </p>
<p>p P PiB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*(2^50) </p>
<p>PB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*(10^15) </p>
<p> An example is &quot;2k&quot; for 2048. The large tera and peta suffixes are only available for numeric arguments that might require 64 bits to represent internally. </p>
<p> A suffix of the form &quot;x&lt;n&gt;&quot; multiplies the leading number by &lt;n&gt;. An example is &quot;2&#215;33&quot; for &quot;66&quot;. The leading number cannot be &quot;0&quot; (zero) as that would be interpreted as a hexadecimal number (see below). </p>
<p> These multiplicative suffixes are compatible with GNU&#8217;s dd command (since 2002) which claims compliance with SI and with IEC 60027-2. </p>
<p> Alternatively numerical arguments can be given in hexadecimal. There are two syntaxes. The number can be preceded by either &quot;0x&quot; or &quot;0X&quot; as found in the C programming language. The second hexadecimal representation is a trailing &quot;h&quot; or &quot;H&quot; as found in (storage) standards. When hex numbers are given, multipliers cannot be used. For example the decimal value &quot;256&quot; can be given as &quot;0x100&quot; or &quot;100h&quot;.</p>
<h2>SCRIPTS, EXAMPLES and UTILS</h2>
<p>There are several bash shell scripts in the &#8216;scripts&#8217; subdirectory that invoke compiled utilities (e.g. sg_readcap). The scripts start with &#8216;scsi_&#8217; rather than &#8216;sg_&#8217;. One purpose of these scripts is to call the same utility (e.g. sg_readcap) on multiple disks. Most of the basic compiled utilities only allow one device as an argument. Some distributions install these scripts in a visible directory (e.g. /usr/src/bin). Some of these scripts have man page entries. See the README file in the &#8216;scripts&#8217; subdirectory. </p>
<p> There is some example C code plus examples of complex invocations in the &#8216;examples&#8217; subdirectory. There is also a README file. The example C may be a simpler example of how to use a SCSI pass-through in Linux than the main utilities (found in the &#8216;src&#8217; subdirectory). This is due to the fewer abstraction layers (e.g. they don&#8217;t worry the MinGW in Windows may open a file in text rather than binary mode). </p>
<p> Some utilities that the author has found useful have been placed in the &#8216;utils&#8217; subdirectory.</p>
<h2>Web Site</h2>
<p>There is a web page discussing this package at <a rel="nofollow" href="http://sg.danny.cz/sg/sg3_utils.html">http://sg.danny.cz/sg/sg3_utils.html</a> . The device naming used by this package on various operating systems is discussed at: <a rel="nofollow" href="http://sg.danny.cz/sg/device_name.html">http://sg.danny.cz/sg/device_name.html</a> .</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert. Some utilities have been contributed, see the CREDITS file and individual source files (in the &#8216;src&#8217; directory).</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 1999-2013 Douglas Gilbert<br />
 Some utilities are distributed under a GPL version 2 license while others, usually more recent ones, are under a FreeBSD license. The files that are common to almost all utilities and thus contain the most reusable code, namely sg_lib.[hc], sg_cmds_basic.[hc] and sg_cmds_extra.[hc] are under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>sdparm(sdparm), ddpt(ddpt), lsscsi(lsscsi), <a href="/docs/linux/man/1-dmesg/">dmesg</a>(1), <a href="/docs/linux/man/1-mt/">mt</a>(1)</code> </p>
