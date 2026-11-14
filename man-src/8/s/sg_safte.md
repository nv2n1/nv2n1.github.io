---
title: "sg_safte(8)"
name: "sg_safte"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_safte/"
description: "sg_safte – access SCSI Accessed Fault-Tolerant Enclosure (SAF-TE) device"
---

<p>sg_safte &#8211; access SCSI Accessed Fault-Tolerant Enclosure (SAF-TE) device</p>
<h2>Synopsis</h2>
<p><code>sg_safte</code> [<i>&#8211;config</i>] [<i>&#8211;devstatus</i>] [<i>&#8211;encstatus</i>] [<i>&#8211;flags</i>] [<i>&#8211;help</i>] [<i>&#8211;hex</i>] [<i>&#8211;insertions</i>] [<i>&#8211;raw</i>] [<i>&#8211;usage</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>Fetches enclosure status (via a SCSI READ BUFFER command). The <i>DEVICE</i> should be a SAF-TE device which may be a storage array controller (INQUIRY peripheral device type 0xc) or a generic processor device (INQUIRY peripheral device type 0x3). </p>
<p> If no options are given (only the <i>DEVICE</i> argument) then the overall enclosure status as reported by the option <i>&#8211;config</i> is reported.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well. The options are arranged in alphabetical order based on the long option name.</p>
<dl>
<dt><code>-c</code>, <code>&#8211;config</code></p>
<dd>will issues a <i>Read Enclosure Configuration</i> (READ BUFFER ID 0) cdb to the device, which returns a list of the enclosure hardware resources.</p>
<dt><code>-d</code>, <code>&#8211;devstatus</code></p>
<dd>will issue a <i>Read Device Slot Status</i> (READ BUFFER ID 4) cdb to the device, which returns information about the current state of each drive or slot.</p>
<dt><code>-s</code>, <code>&#8211;encstatus</code></p>
<dd>will issue a <i>Read Enclosure Status</i> (READ BUFFER ID 1) cdb to the device, which returns the operational state of the components.</p>
<dt><code>-f</code>, <code>&#8211;flags</code></p>
<dd>will issue a <i>Read Global Flags</i> (READ BUFFER ID 5) cdb to the device, which read the most recent state of the global flags of the RAID processor device.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-H</code>, <code>&#8211;hex</code></p>
<dd>output the response to a READ BUFFER command in ASCII hex to stdout. If used once, output the response to the first READ BUFFER command (i.e. with buffer_id=0). This should be the enclosure configuration. If used twice (or more often), the response to subsequent READ BUFFER commands is output.</p>
<dt><code>-i</code>, <code>&#8211;insertions</code></p>
<dd>will issue a <i>Read Device Insertions</i> (READ BUFFER ID 3) cdb to the device, which returns information about the number of times devices have been inserted whilst the RAID system was powered on.</p>
<dt><code>-r</code>, <code>&#8211;raw</code></p>
<dd>output the response to a READ BUFFER command in binary to stdout. If used once, output the response to the first READ BUFFER command (i.e. with buffer_id=0). This should be the enclosure configuration. If used twice (or more often), the response to subsequent READ BUFFER commands is output.</p>
<dt><code>-u</code>, <code>&#8211;usage</code></p>
<dd>will issue a <i>Read Usage Statistics</i> (READ BUFFER ID 2) cdb to the device, which returns the information on total usage time and number of power-on cycles of the RAID device.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the level of verbosity, (i.e. debug output).</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</dl>
<h2>Notes</h2>
<p>The implementation is based on the intermediate review document eg as found at </p>
<p> <a rel="nofollow" href="http://www.intel.com/design/servers/ipmi/saf-te.htm">http://www.intel.com/design/servers/ipmi/saf-te.htm</a> </p>
<p> As the specification was never finalized this document serves as the de-facto standard. </p>
<p> Similar functionality is provided by SPC-4 SCSI Enclosure Services devices (Peripheral device type 0xd), which can be queried with the sg_ses utility.</p>
<h2>Examples</h2>
<p>To view the configuration:<br />
sg_safte&nbsp;<wbr>/dev/sg1 To view the device slot status:<br />
sg_safte &#8211;devstatus&nbsp;<wbr>/dev/sg1 </p>
<h2>Exit Status</h2>
<p>The exit status of sg_safte is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Authors</h2>
<p>Written by Hannes Reinecke and Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2004-2012 Hannes Reinecke and Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>sg_inq, sg_ses (in sg3_utils package); safte-monitor (internet)</code> </p>
