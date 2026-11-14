---
title: "smp_rep_phy_event_list(8)"
name: "smp_rep_phy_event_list"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smp_rep_phy_event_list/"
description: "smp_rep_phy_event_list – invoke REPORT PHY EVENT LIST SMP function"
---

<p>smp_rep_phy_event_list &#8211; invoke REPORT PHY EVENT LIST SMP function</p>
<h2>Synopsis</h2>
<p><code>smp_rep_phy_event_list</code> [<i>&#8211;desc</i>] [<i>&#8211;enumerate</i>] [<i>&#8211;force</i>] [<i>&#8211;help</i>] [<i>&#8211;hex</i>] [<i>&#8211;index=IN</i>] [<i>&#8211;interface=PARAMS</i>] [<i>&#8211;long</i>] [<i>&#8211;nonz</i>] [<i>&#8211;raw</i>] [<i>&#8211;sa=SAS_ADDR</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] [<i>&#8211;zero</i>] <i>SMP_DEVICE[,N]</i></p>
<h2>Description</h2>
<p>Sends a SAS Serial Management Protocol (SMP) REPORT PHY EVENT LIST function request to an SMP target. The SMP target is identified by the <i>SMP_DEVICE</i> and the <i>SAS_ADDR</i>. Depending on the interface, the <i>SAS_ADDR</i> may be deduced from the <i>SMP_DEVICE</i>. The mpt interface uses <i>SMP_DEVICE</i> to identify a HBA (an SMP initiator) and needs the additional <i>,N</i> to differentiate between HBAs if there are multiple present. </p>
<p> Reports zero or more phy event list descriptors. Each descriptor contains a phy identifier, a phy event source, a phy event (i.e. a count) and a peak value detector theshold. At least one phy event should be maintained for each phy.</p>
<h2>Options</h2>
<p>Mandatory arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-d</code>, <code>&#8211;desc</code></p>
<dd>precede each phy event descriptor with a line announcing its descriptor index number. Index numbers start at 1.</p>
<dt><code>-e</code>, <code>&#8211;enumerate</code></p>
<dd>enumerate all of the known Phy Event Source names, one per line preceded by its value in hex. Ignores <i>SMP_DEVICE</i> if it is given; most other options are also ignored. Exits after displaying the names.</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd>force the report to continue after the last descriptor index has been exceeded. The default action is too stop the report when the last descriptor index has been exceeded. at 1.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-H</code>, <code>&#8211;hex</code></p>
<dd>output the response (less the CRC field) in hexadecimal.</p>
<dt><code>-i</code>, <code>&#8211;index</code>=<i>IN</i></p>
<dd>starting phy event list descriptor index. <i>IN</i> is a value between 0 and 65535. The default is 1. If <i>IN</i> is 0 then the response should contain no phy event list descriptors but the &#8216;last phy event list descriptor index&#8217; and &#8216;phy event list descriptor length&#8217; fields in the response should be set appropriately. The last point was clarified in SPL-2 revision 3.</p>
<dt><code>-l</code>, <code>&#8211;long</code></p>
<dd>prefix each phy event source string with its numeric identifier in hex. Also place &quot;phy_id=&quot; in front of the phy identifier number. For example: &quot;phy_id=3: [0x1]: Invalid word count: 29&quot;; without this option this line would be: &quot;3: Invalid word count: 29&quot;.</p>
<dt><code>-n</code>, <code>&#8211;nonz</code></p>
<dd>only show phy events with non-zero counts or peak values. The default is to show all phy events in the response.</p>
<dt><code>-I</code>, <code>&#8211;interface</code>=<i>PARAMS</i></p>
<dd>interface specific parameters. In this case &quot;interface&quot; refers to the path through the operating system to the SMP initiator. See the smp_utils man page for more information.</p>
<dt><code>-r</code>, <code>&#8211;raw</code></p>
<dd>send the response (less the CRC field) to stdout in binary. All error messages are sent to stderr.</p>
<dt><code>-s</code>, <code>&#8211;sa</code>=<i>SAS_ADDR</i></p>
<dd>specifies the SAS address of the SMP target device. Typically this is an expander. This option may not be needed if the <i>SMP_DEVICE</i> has the target&#8217;s SAS address within it. The <i>SAS_ADDR</i> is in decimal but most SAS addresses are shown in hexadecimal. To give a number in hexadecimal either prefix it with &#8216;0x&#8217; or put a trailing &#8216;h&#8217; on it.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the verbosity of the output. Can be used multiple times</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</dl>
<h2>Notes</h2>
<p>Similar information is maintained for SAS SSP target phys (e.g. on a SAS disk). It can be obtained from the Protocol Specific Port log page with the sg_logs utility. </p>
<p> Similar information may be obtained for SAS initiator phys (e.g. on a SAS HBA). As an example in Linux 2.6.28 error information can be found in this directory /sys/class/sas_phy/phy-4:0 (for the phy 0 in SCSI/SAS host 4). </p>
<p> Similar information may be obtained for SATA device phys (e.g. on a SATA disk). If there is a SAT layer between OS and the SATA device then the sg_sat_phy_event utility can fetch the information.</p>
<h2>Conforming To</h2>
<p>The SMP REPORT PHY EVENT LIST function was introduced in SAS-2 .</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2011 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>smp_utils, smp_phy_control, smp_rep_phy_event(smp_utils)</code> <code>sg_logs, sg_sat_phy_event(sg3_utils)</code> </p>
