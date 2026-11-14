---
title: "smp_utils(8)"
name: "smp_utils"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smp_utils/"
description: "smp_* – invoke a SAS Serial Management Protocol (SMP) function"
---

<p>smp_* &#8211; invoke a SAS Serial Management Protocol (SMP) function</p>
<h2>Synopsis</h2>
<p><code>smp_*</code> [<i>&#8211;expected=EX</i>] [<i>&#8211;help</i>] [<i>&#8211;hex</i>] [<i>&#8211;interface=PARAMS</i>] [<i>&#8211;raw</i>] [<i>&#8211;sa=SAS_ADDR</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>SMP_DEVICE[,N]</i></p>
<h2>Description</h2>
<p>Serial Attached SCSI (SAS) is a transport (also known as a interconnect) used by storage systems. A SAS system is made up of Host Bus Adapters (HBAs typically containing SCSI initiators), disks (referred to in SCSI as both targets and logical units) and optionally some switching hardware called &quot;expanders&quot;. Expanders are not SCSI devices so a new protocol was required to control and monitor them. Its full name is the SAS Serial Management Protocol which is abbreviated to SMP. </p>
<p> smp_utils is a package of utilities. Each utility sends an SMP function request to a <i>SMP_DEVICE</i> (an SMP target). Some utilities may invoke the same function more than once. If an error occurs then an error message is sent to stderr. If no error occurs, the response is decoded (the default), output in ASCII hex (when <i>&#8211;hex</i> is given) or output in binary to stdout (when the <i>&#8211;raw</i> option is given). </p>
<p> If <i>SMP_DEVICE[,N]</i> is not given then the value in the environment variable SMP_UTILS_DEVICE is used. </p>
<p> This package was originally written for Linux and has been ported to FreeBSD and Solaris.</p>
<h2>Linux Interface</h2>
<p>Currently there are multiple interfaces that allow SMP functions to be passed through to an SMP target. </p>
<p> One method is to have a <i>SMP_DEVICE</i> which is actually the SMP initiator (e.g. &#8216;/dev/mptctl,0&#8217;). In this case the SMP target&#8217;s SAS address must be supplied with the <i>&#8211;sa=SAS_ADDR</i> option. </p>
<p> Another method is to have a <i>SMP_DEVICE</i> which represents the SMP target. In this case no <i>SAS_ADDRESS</i> needs to be given (since it is implicit). </p>
<p> Each utility in smp_utils attempts to work out which interface it has been given by examining the <i>SMP_DEVICE</i> file. There are three interfaces supported currently:</p>
<dl>
<dt><code>aac</code></p>
<dd>This specifies the aacraid SAS pass-through associated with Adaptec/PMC RAID products. The <i>SMP_DEVICE[,N]</i> argument takes the form <i>/dev/aac[N[,E_ID]]</i> where &quot;N&quot; is the raid controller number (typically 0) and &quot;E_ID&quot; is the expander identifier (typically 0); both default to 0 so <i>/dev/aac</i> is equivalent to <i>/dev/aac0</i> and <i>/dev/aac0,0</i> . The &quot;N&quot; is the unique_id found in /sys/class/scsi_host&lt;HN&gt;/unique_id . The &quot;HN&quot; is the host number which is the first number to appear on each line in the lsscsi utility which by default uses one line to list each accessible SCSI device (typically SCSI or ATA disks). The &quot;E_ID&quot; is the expander identifier which can be found with the Adaptec/PMC arcconf utility using the form &quot;arcconf expanderlist &lt;ControllerNum&gt;&quot;. The &lt;ControllerNum&gt;s start at 1 . If an aac RAID controller is present then the /dev/acc device node will be created by the first smp utility to use this interface.</p>
<dt><code>mpt</code></p>
<dd>This specifies the MPT fusion SAS pass-through. The mptsas driver uses the &#8216;/dev/mptctl&#8217; device node (character device major 10, minor 220) while the mpt2sas driver uses &#8216;/dev/mpt2ctl&#8217; device node (major 10, minor 221). For the mpt3sas driver the corresponding device node is &#8216;/dev/mpt3ctl&#8217;. The &#8216;modprobe mptctl&#8217; or &#8216;modprobe mpt2ctl&#8217; command may be needed. If there are multiple mpt fusion controllers (HBAs) in the computer, then the user will need to specify which one to use with the syntax: &#8216;/dev/mptctl,&lt;n&gt;&#8217; where &lt;n&gt; is the &quot;ioc_num&quot;. This number can be found with dmesg after the mptsas driver is registered and appears as a suffix to the driver name (e.g. mpt2sas0). It can also be found in &#8216;/sys/class/scsi_host/host&lt;n&gt;/unique_id&#8217;. When this interface is used the <i>&#8211;sa=SAS_ADDR</i> option must be given to specify the SAS address of the SMP target.</p>
<dt><code>sgv4</code> (<code>sg</code>)</p>
<dd>This interface is more generic and supported by several SAS HBA drivers including mptsas (and mpt2sas). It was introduced in the Linux 2.6.24 kernel. The SMP functions are passed to the kernel via the bsg driver using a format known as &quot;SCSI Generic Version 4&quot; which gives this interface its name: &quot;sgv4&quot; or just &quot;sg&quot;. The SAS transport layer within the SCSI sub-system unpacks the SMP requests and forwards them to SAS low level drivers that support this interface. The <i>SMP_DEVICE</i> is either a member of the &#8216;/sys/class/bsg&#8217; directory (e.g. /sys/class/bsg/expander-6:0 ) or a device node made for the bsg driver (e.g. /dev/bsg/expander-6:0 ). Such device nodes are dynamic (i.e. they don&#8217;t have fixed major and minor numbers) and should correspond to the major and minor numbers found in the &#8216;sys/class/bsg/&lt;smp_target_device&gt;/dev&#8217; file.</dl>
<h2>Freebsd Interface</h2>
<p>The CAM subsystem has been enhanced in FreeBSD 9 to pass-through SMP requests and return the corresponding responses. However CAM does not directly access expander devices because they are not SCSI devices. It makes the assumption that each SAS expander has an integrated SES (enclosure) device and that is addressed. This assumption seems to be true for SAS-2 expanders but not some SAS-1 expanders. Thus invocations look like this: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>smp_discover&nbsp;<wbr>/dev/ses0 </p>
<p> where /dev/ses0 is a SES device associated with a SAS expander.</p>
<h2>Solaris Interface</h2>
<p>The USMP pass-through mechanism is used. Invocations look like this: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>smp_rep_manufacturer&nbsp;<wbr>/dev/smp/expd0</p>
<h2>Environment Variables</h2>
<p>If the device name is not given then the SMP_UTILS_DEVICE environment variable is checked and if present its contents are used as the device name. </p>
<p> If the SAS address (of the SMP target) is not given and it is required (i.e. it is not implicit in the device name) then the SMP_UTILS_SAS_ADDR environment variable is checked and if present its contents are used as the SAS address. SAS addresses are usually given in hex indicated by a leading &#8216;0x&#8217; or trailing &#8216;h&#8217;. </p>
<p> If either or both environment variables and the corresponding command line options are given, then the command line options take precedence.</p>
<h2>Common Options</h2>
<p>Mandatory arguments to long options are mandatory for short options as well. If an option takes a numeric argument then that argument is assumed to be decimal unless otherwise indicated (e.g. with a leading &quot;0x&quot; or a trailing &quot;h&quot;).</p>
<dl>
<dt><code>-E</code>, <code>&#8211;expected</code>=<i>EX</i></p>
<dd>revision 4a of the SAS-2 draft introduced an &#8216;expected expander change count&#8217; field in some SMP requests. The idea is to detect other SMP initiators trying to change the state of an expander. The value <i>EX</i> is from 0 to 65535 inclusive with 0 being the default value. When <i>EX</i> is greater than zero then if the value doesn&#8217;t match the expander change count of the SMP target (i.e. the expander) when the request arrives then the target ignores the request and sets a function result of &quot;invalid expander change count&quot; in the response.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message for the utility then exit.</p>
<dt><code>-H</code>, <code>&#8211;hex</code></p>
<dd>output the response in hexadecimal. This does not include the trailing CRC field.</p>
<dt><code>-I</code>, <code>&#8211;interface</code>=<i>PARAMS</i></p>
<dd>interface specific parameters. This option is usually not needed since the interface type is guessed by a utility based on the characteristics of the given <i>SMP_DEVICE</i> argument or what is in the corresponding environment variables. <i>PARAMS</i> is of the form: <i>INTF[,force]</i>. If the guess doesn&#8217;t work then the interface can be specified by giving a <i>INTF</i> of either &#8216;mpt&#8217; or &#8216;sgv4&#8217;. Sanity checks are still performed and a utility may refuse if it doesn&#8217;t agree with the given <i>INTF</i>. If the user is really sure then adding a &#8216;,force&#8217; will force the utility to use the given interface.</p>
<dt><code>-r</code>, <code>&#8211;raw</code></p>
<dd>send the response to stdout in binary. This does not include the trailing CRC field. All error messages are sent to stderr.</p>
<dt><code>-s</code>, <code>&#8211;sa</code>=<i>SAS_ADDR</i></p>
<dd>specifies the SAS address of the SMP target device. Typically this is an expander. This option may not be needed if the <i>SMP_DEVICE</i> has the target&#8217;s SAS address associated with it. The <i>SAS_ADDR</i> is in decimal but most SAS addresses are shown in hexadecimal. To give a number in hexadecimal either prefix it with &#8216;0x&#8217; or put a trailing &#8216;h&#8217; on it. If this option is not given then the value in the environment variable SMP_UTILS_SAS_ADDR is used.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the verbosity of the output. Can be used multiple times.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</dl>
<h2>Exit Status</h2>
<p>To aid scripts that call these utilities, the exit status is set to indicate success (0) or failure (1 or more):</p>
<dl>
<dt><code>0</code></p>
<dd>success</p>
<dt><code>1 &#8211; 63</code></p>
<dd>reserved for SMP function result codes. See the SAS-2 (or later) draft, in the section on the application layer, drilling down further: management application layer then SMP functions. Here are some common function result codes: 1 [unknown SMP function], 2 [SMP function failed], 16 [phy does not exist], 17 [index does not exist], 18 [phy does not support SATA], 19 [unknown phy operation], 22 [phy vacant] and 35 [zone lock violation].</p>
<dt><code>91</code></p>
<dd>syntax error. Either illegal options, options with bad arguments or a combination of options that is not permitted.</p>
<dt><code>92</code></p>
<dd>the utility is unable to open, close or use the given <i>SMP_DEVICE</i>. The given file name could be incorrect or there may be file permission problems. Adding the <i>&#8211;verbose</i> option may give more information.</p>
<dt><code>97</code></p>
<dd>the response to an SMP function failed sanity checks.</p>
<dt><code>99</code></p>
<dd>any error that can&#8217;t be categorized into values 1 to 97 may yield this value. This includes transport and operating system errors.</dl>
<h2>Notes</h2>
<p>Finding the SAS address of an expander can be a challenge in some environments. An enclosure containing one or more expanders may have the expander SAS address(es) printed on the back of the device, a bit like Ethernet MAC addresses. In the Linux 2.6 kernel series the expander SAS address may well be in the sysfs tree but it is not always easy to find. Doing this search may help: </p>
<pre><code># find /sys -name &quot;*expander*&quot;</code></pre>
<p> That should show the suffix on any expanders that have been detected. Then a command like &#8216;cat /sys/class/sas_device/expander-6:0/sas_address&#8217; should show its SAS address. Another approach is to work backwards from SCSI devices (i.e. logical units). The protocol specific port log page (log page 18h) contains fields for the &quot;attached SAS address&quot;. The sg_logs utility from the sg3_utils package could be used like this: </p>
<pre><code># sg_logs --page=18h /dev/sdb</code></pre>
<p> Any given &quot;attached SAS address&quot; is either a HBA, an expander or 0 indicating that port is not connected. An expander is indicated by &quot;attached device type: expander device&quot;. A SAS disk&#8217;s target port identifiers (also known as SAS addresses), device name and logical unit name (all NAA 5 format) can be found with the sg_vpd utility (e.g. &#8216;sg_vpd -i &lt;disk_dev&gt;&#8217;). The sdparm utility can provide the same information (e.g. &#8216;sdparm -i &lt;disk_dev&gt;&#8217;). A SAS expander is often associated with a SCSI Enclosure Services (SES) device sometimes on the same silicon attached via a virtual phy to the expander. That SES device may be able to access and control an attached enclosure or backplane via SGPIO or I2C on sideband signals (e.g. in a SFF-8087 cable). To interact with a SES device, see the sg_ses utility. Often expander phys are grouped in fours on the same connector (e.g. SFF-8088). Care needs to be taken when multiple expanders are interconnected. An enclosure <code>universal</code> port is one in which the &quot;table to table supported&quot; attribute is set (in the REPORT GENERAL response) and the associated phys have the table routing attribute (in the DISCOVER response). Enclosure <code>universal</code> ports were introduced in SAS-2 and have few restrictions when used to interconnect expanders or connect SAS or SATA devices. An enclosure <code>out</code> port is one in which the &quot;table to table supported&quot; attribute is clear and the associated phys have the table routing attribute. An enclosure <code>in</code> port is one in which the associated phys have the subtractive routing attribute. When <code>universal</code> ports are not available, an expander interconnect should be between an <code>in</code> port and an <code>out</code> port.</p>
<h2>Examples</h2>
<p>See &quot;Examples&quot; section in <a rel="nofollow" href="http://sg.danny.cz/sg/smp_utils.html">http://sg.danny.cz/sg/smp_utils.html</a> .</p>
<h2>Conforming To</h2>
<p>SAS has multiple generations. The early standards are: the original SAS (ANSI INCITS 376-2003), SAS 1.1 (INCITS 417-2006) and SAS-2 (ANSI INCITS 457-2010) . SAS-2.1 work was split into an electrical and physical layers document (standardized as SAS-2.1 ANSI INCITS 478-2011) with the upper level layers placed in a document called the SAS Protocol Layer and it was standardized as SPL ANSI INCITS 476-2011. Next came SPL-2 which was standardized as SPL-2 ANSI INCITS 505-2013. SPL-3 is near standardization and its most recent draft is spl3r07.pdf. To avoid confusion, the multiple generations of SAS will be referred to in these man pages as SAS 1, 1.1, 2, 2.1 (SPL) and 3 (SPL-2 and SPL-3). Roughly speaking SAS-1 runs at 3 Gbps, SAS-2 at 6 Gbps and SAS-3 at 12 Gbps. Drafts, including those just prior to standardization can be found at the <a rel="nofollow" href="http://www.t10.org">http://www.t10.org</a> site (e.g. spl-r07.pdf and spl2r04c.pdf). INCITS policy now requires a registration to view these drafts, a break from t10.org tradition. </p>
<p> The two utilities for reading and writing to GPIO registers, smp_read_gpio and smp_write_gpio, are defined in the Small Form Factor document SFF-8485 found at <a rel="nofollow" href="http://www.sffcommittee.com">http://www.sffcommittee.com</a> . &quot;Enhanced&quot; versions of the corresponding SMP functions have been mentioned in some drafts but no definitions have been published and the references have been removed in more recent drafts. </p>
<p> In this section of each utility&#8217;s man page is the first standard in which the associated SMP function appeared and whether there have been significant additions in later standards. </p>
<p> The COVERAGE file in the smp_utils source tarball shows a table of all SMP function names defined in the drafts, the versions of those standards in which those SMP functions first appeared and the corresponding smp_utils utility names. A lot of extra SMP functions have been added in SAS-2 associated with zoning.</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2006-2014 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>sg_logs, sg_vpd, sg_ses(sg3_utils); sdparm(sdparm); lsscsi(lsscsi)</code> </p>
