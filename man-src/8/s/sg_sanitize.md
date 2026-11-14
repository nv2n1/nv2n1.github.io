---
title: "sg_sanitize(8)"
name: "sg_sanitize"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_sanitize/"
description: "sg_sanitize – remove all user data from disk with SCSI SANITIZE command"
---

<p>sg_sanitize &#8211; remove all user data from disk with SCSI SANITIZE command</p>
<h2>Synopsis</h2>
<p><code>sg_sanitize</code> [<i>&#8211;ause</i>] [<i>&#8211;block</i>] [<i>&#8211;count=OC</i>] [<i>&#8211;crypto</i>] [<i>&#8211;early</i>] [<i>&#8211;fail</i>] [<i>&#8211;help</i>] [<i>&#8211;invert</i>] [<i>&#8211;ipl=LEN</i>] [<i>&#8211;overwrite</i>] [<i>&#8211;pattern=PF</i>] [<i>&#8211;quick</i>] [<i>&#8211;test=TE</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] [<i>&#8211;wait</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>This utility invokes the SCSI SANITIZE command. This command was first introduced in the SBC-3 revision 27 draft. The purpose of the sanitize operation is to alter the information in the cache and on the medium of a logical unit (e.g. a disk) so that the recovery of user data is not possible. If that user data cannot be erased, or is in the process of being erased, then the sanitize operation prevents access to that user data. </p>
<p> Once a SCSI SANITIZE command has successfully started, then user data from that disk is no longer available. Even if the disk is power cycled, the sanitize operation will continue after power is re-instated until it is complete. </p>
<p> This utility requires either the <i>&#8211;block</i>, <i>&#8211;crypto</i>, <i>&#8211;fail</i> or <i>&#8211;overwrite</i> option. With the <i>&#8211;block</i>, <i>&#8211;crypto</i> or <i>&#8211;overwrite</i> option the user is given 15 seconds to reconsider whether they wish to erase all the data on a disk, unless the <i>&#8211;quick</i> option is given in which case the sanitize operation starts immediately. The disk&#8217;s INQUIRY response strings are printed out just in case the wrong <i>DEVICE</i> has been given. </p>
<p> If the <i>&#8211;early</i> option is given this utility will exit soon after starting the SANITIZE command with the IMMED bit set. The user can monitor the progress of the sanitize operation with the &quot;sg_request &#8211;num=9999 &#8211;progress&quot; which sends a REQUEST SENSE command every 30 seconds. Otherwise if the <i>&#8211;wait</i> option is given then this utility will wait until the SANITIZE command completes (or fails) and that can be many hours. </p>
<p> If neither the <i>&#8211;early</i> nor <i>&#8211;wait</i> option is given then the SANITIZE command is started with the IMMED bit set. After that this utility sends a REQUEST SENSE command every 60 seconds until there are no more progress indications.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well. The options are arranged in alphabetical order based on the long option name.</p>
<dl>
<dt><code>-A</code>, <code>&#8211;ause</code></p>
<dd>sets the AUSE bit in the cdb. AUSE is an acronym for &quot;allow unrestricted sanitize exit&quot;. Default action is to leave the bit cleared.</p>
<dt><code>-B</code>, <code>&#8211;block</code></p>
<dd>perform a &quot;block erase&quot; sanitize operation.</p>
<dt><code>-c</code>, <code>&#8211;count</code>=<i>OC</i></p>
<dd>where <i>OC</i> is the &quot;overwrite count&quot; associated with the &quot;overwrite&quot; sanitize operation. <i>OC</i> can be a value between 1 and 31 and 1 is the default.</p>
<dt><code>-C</code>, <code>&#8211;crypto</code></p>
<dd>perform a &quot;cryptographic erase&quot; sanitize operation.</p>
<dt><code>-e</code>, <code>&#8211;early</code></p>
<dd>the default action of this utility is to poll the disk every 60 seconds to fetch the progress indication until the sanitize is finished. When this option is given this utility will exit &quot;early&quot; as soon as the sanitize has commenced. This option and <i>&#8211;wait</i> cannot both be given.</p>
<dt><code>-F</code>, <code>&#8211;fail</code></p>
<dd>perform an &quot;exit failure mode&quot; sanitize operation. Typically requires the preceding SANITIZE command to have set the AUSE bit.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>print out the usage information then exit.</p>
<dt><code>-i</code>, <code>&#8211;ipl</code>=<i>LEN</i></p>
<dd>set the initialization pattern length to <i>LEN</i> bytes. By default it is set to the length of the pattern file (<i>PF</i>). Only active when the <i>&#8211;overwrite</i> option is also given. It is the number of bytes from the <i>PF</i> file that will be used as the initialization pattern. The minimum size is 1 byte and the maximum is the logical block size of the <i>DEVICE</i> (and not to exceed 65535). If <i>LEN</i> exceeds the <i>PF</i> file size then the initialization pattern is padded with zeros.</p>
<dt><code>-I</code>, <code>&#8211;invert</code></p>
<dd>set the INVERT bit in the overwrite service action parameter list. This only affects the &quot;overwrite&quot; sanitize operation. The default is a clear INVERT bit. When the INVERT bit is set then the initialization pattern is inverted between consecutive overwrite passes.</p>
<dt><code>-O</code>, <code>&#8211;overwrite</code></p>
<dd>perform an &quot;overwrite&quot; sanitize operation. When this option is given then the <i>&#8211;pattern=PF</i> option is required.</p>
<dt><code>-p</code>, <code>&#8211;pattern</code>=<i>PF</i></p>
<dd>where <i>PF</i> is the filename of a file containing the initialization pattern required by an &quot;overwrite&quot; sanitize operation. The length of this file will be used as the length of the initialization pattern unless the <i>&#8211;ipl=LEN</i> option is given. The length of the initialization pattern must be from 1 to the logical block size of the <i>DEVICE</i>.</p>
<dt><code>-Q</code>, <code>&#8211;quick</code></p>
<dd>the default action (i.e. when the option is not given) is to give the user 15 seconds to reconsider doing a sanitize operation on the <i>DEVICE</i>. When this option is given that step (i.e. the 15 second warning period) is skipped.</p>
<dt><code>-T</code>, <code>&#8211;test</code>=<i>TE</i></p>
<dd>set the TEST field in the overwrite service action parameter list. This only affects the &quot;overwrite&quot; sanitize operation. The default is to place 0 in that field.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the level of verbosity, (i.e. debug output).</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</p>
<dt><code>-w</code>, <code>&#8211;wait</code></p>
<dd>the default action (i.e. without this option and the <i>&#8211;early</i> option) is to start the SANITIZE command with the IMMED bit set then poll for the progress indication with the REQUEST SENSE command until the sanitize operation is complete (or fails). When this option is given (and the <i>&#8211;early</i> option is not given) then the SANITIZE command is started with the IMMED bit clear. For a large disk this might take hours. [A cryptographic erase operation could potentially be very quick.]</dl>
<h2>Notes</h2>
<p>The SCSI SANITIZE command is closely related to the ATA SANITIZE command, both are relatively new with the ATA command being the first one defined. The SCSI to ATA Translation (SAT) definition for the SCSI SANITIZE command appeared in the SAT-3 revision 4 draft. </p>
<p> The SCSI SANITIZE command is related to the SCSI FORMAT UNIT command. It is likely that a block erase sanitize operation would take a similar amount of time as a format on the same disk (e.g. 9 hours for a 2 Terabyte disk). The primary goal of a format is the configuration of the disk at the end of a format (e.g. different logical block size or protection information added). Removal of user data is only a side effect of a format. With the SCSI SANITIZE command, removal of user data is the primary goal. If a sanitize operation is interrupted (e.g. the disk is power cycled) then after power up any remaining user data will not be available and the sanitize operation will continue. When a format is interrupted (e.g. the disk is power cycled) the drafts say very little about the state of the disk. In practice some of the original user data may remain and the format may need to be restarted. </p>
<p> Finding out whether a disk (SCSI or ATA) supports SANITIZE can be a challenge. If the user really needs to find out and no other information is available then try &#8216;sg_sanitize &#8211;fail -vvv &lt;device&gt;&#8217; and observe the sense data returned may be the safest approach. Using the <i>&#8211;fail</i> variant of this utility should have no effect unless it follows an already failed sanitize operation. If the SCSI REPORT SUPPORTED OPERATION CODES command (see sg_opcodes) is supported then using it would be a better approach for finding if sanitize is supported.</p>
<h2>Examples</h2>
<p>These examples use Linux device names. For suitable device names in other supported Operating Systems see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page. As a precaution if this utility is called with no options then apart from printing a usage message, nothing happens:<br />
sg_sanitize&nbsp;<wbr>/dev/sdm To do a &quot;block erase&quot; sanitize the <i>&#8211;block</i> option is required. The user will be given a 15 second period to reconsider, the SCSI SANITIZE command will be started with the IMMED bit set, then this utility will poll for a progress indication with a REQUEST SENSE command until the sanitize operation is finished:<br />
sg_sanitize &#8211;block&nbsp;<wbr>/dev/sdm To start a &quot;block erase&quot; sanitize and return from this utility once it is started (but not yet completed) use the <i>&#8211;early</i> option:<br />
sg_sanitize &#8211;block &#8211;early&nbsp;<wbr>/dev/sdm If the 15 second reconsideration time is not required add the <i>&#8211;quick</i> option:<br />
sg_sanitize &#8211;block &#8211;quick &#8211;early&nbsp;<wbr>/dev/sdm To do an &quot;overwrite&quot; sanitize a pattern file is required: </p>
<pre><code>sg_sanitize --overwrite --pattern=rand.img /dev/sdm</code></pre>
<p> If the length of that &quot;rand.img&quot; is 512 bytes (a typically logical block size) then to use only the first 17 bytes (repeatedly) in the &quot;overwrite&quot; sanitize operation: </p>
<pre><code>sg_sanitize --overwrite --pattern=rand.img --ipl=17 /dev/sdm
</code></pre>
<h2>Exit Status</h2>
<p>The exit status of sg_sanitize is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page. Unless the <i>&#8211;wait</i> option is given, the exit status may not reflect the success of otherwise of the format.</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2011-2013 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-sg_requests/">sg_requests</a>(8), <a href="/docs/linux/man/8-sg_format/">sg_format</a>(8)</code> </p>
