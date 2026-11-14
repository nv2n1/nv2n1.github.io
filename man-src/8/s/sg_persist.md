---
title: "sg_persist(8)"
name: "sg_persist"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_persist/"
description: "sg_persist – use SCSI PERSISTENT RESERVE command to access registrations and reservations"
---

<p>sg_persist &#8211; use SCSI PERSISTENT RESERVE command to access registrations and reservations</p>
<h2>Synopsis</h2>
<p><code>sg_persist</code> [<i>OPTIONS</i>] <i>DEVICE</i> </p>
<p> <code>sg_persist</code> [<i>OPTIONS</i>] <i>&#8211;device=DEVICE</i> </p>
<p> <code>sg_persist</code> <i>&#8211;help</i> | <i>&#8211;version</i></p>
<h2>Description</h2>
<p>This utility allows Persistent reservations and registrations to be queried and changed. Persistent reservations and registrations are queried by sub-commands (called &quot;service actions&quot; in SPC-4) of the SCSI PERSISTENT RESERVE IN (PRIN) command. Persistent reservations and registrations are changed by sub-commands of the SCSI PERSISTENT RESERVE OUT (PROUT) command. </p>
<p> There is a two stage process to obtain a persistent reservation. First an application (an I_T nexus in standard&#8217;s jargon) must register a reservation key. If that is accepted (and it should be unless some other I_T nexus has registered that key) then the application can try and reserve the device. The reserve operation must specify the reservation key and a &quot;type&quot; (see the <i>&#8211;prout-type=TYPE</i> option). </p>
<p> It is relatively safe to query the state of Persistent reservations and registrations. With no options this utility defaults to the READ KEYS sub-command of the PRIN command. Other PRIN sub-commands are READ RESERVATION, REPORT CAPABILITIES and READ FULL STATUS. </p>
<p> Before trying to change Persistent reservations and registrations users should be aware of what they are doing. The relevant sections of the SCSI Primary Commands document (i.e. SPC-4 whose most recent draft is revision 20 dated 22 May 2009) are sections 5.7 (titled &quot;Reservations&quot;), 6.13 (for the PRIN command) and 6.14 (for the PROUT command). To safeguard against accidental use, the <i>&#8211;out</i> option must be given when a PROUT sub-command (e.g. <i>&#8211;register</i>) is used. </p>
<p> The older SCSI RESERVE and RELEASE commands (both 6 and 10 byte variants) are not supported by this utility. In SPC-3, RESERVE and RELEASE are deprecated, replaced by Persistent Reservations. RESERVE and RELEASE have been removed from SPC-4 and Annex B is provided showing how to convert to persistent reservation commands. See a utility called &#8216;scsires&#8217; for support of the SCSI RESERVE and RELEASE commands. </p>
<p> The <i>DEVICE</i> is required by all variants of this utility apart from <i>&#8211;help</i>. The <i>DEVICE</i> can be given either as an argument (typically but not necessarily the last one) or via the <i>&#8211;device=DEVICE</i> option. </p>
<p> SPC-4 does not use the term &quot;sub-command&quot;. It uses the term &quot;service action&quot; for this and for part of a field&#8217;s name in the parameter block associated with the PROUT command (i.e. &quot;service action reservation key&quot;). To lessen the potential confusion the term &quot;sub-command&quot; has been introduced.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well. The following options are sorted in alphabetical order, based on their long option name.</p>
<dl>
<dt><code>-l</code>, <code>&#8211;alloc-length</code>=<i>LEN</i></p>
<dd>specify the allocation length of the PRIN command. <i>LEN</i> is a hex value. By default this value is set to the size of the data-in buffer (8192). This parameter is of use for verification that response to PRIN commands with various allocation lengths is per section 4.3.5.6 of SPC-4 revision 18. Valid <i>LEN</i> values are 0-8192.</p>
<dt><code>-C</code>, <code>&#8211;clear</code></p>
<dd>Clear is a sub-command of the PROUT command. It releases the persistent reservation (if any) and clears all registrations from the device. It is required to supply a reservation key that is registered for this I_T_L nexus (identified by <i>&#8211;param-rk=RK</i>).</p>
<dt><code>-d</code>, <code>&#8211;device</code>=<i>DEVICE</i></p>
<dd><i>DEVICE</i> to send SCSI commands to. The <i>DEVICE</i> can either be provided via this option or via a freestanding argument. For example, these two: &#8216;sg_persist &#8211;device=/dev/sg2&#8217; and &#8216;sg_persist /dev/sg2&#8217; are equivalent.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output a usage message.</p>
<dt><code>-H</code>, <code>&#8211;hex</code></p>
<dd>the response to a valid PRIN sub-command will be output in hexadecimal. By default (i.e. without this option) if the PRIN sub-command is recognised then the response will be decoded as per SPC-4.</p>
<dt><code>-i</code>, <code>&#8211;in</code></p>
<dd>specify that a SCSI PERSISTENT RESERVE IN command is required. This is the default.</p>
<dt><code>-n</code>, <code>&#8211;no-inquiry</code></p>
<dd>the default action is to do a standard SCSI INQUIRY command and output make, product and revision strings plus the peripheral device type prior to executing a PRIN or PROUT command. With this option the INQUIRY command is skipped.</p>
<dt><code>-o</code>, <code>&#8211;out</code></p>
<dd>specify that a SCSI PERSISTENT RESERVE OUT command is required.</p>
<dt><code>-Y</code>, <code>&#8211;param-alltgpt</code></p>
<dd>set the &#8216;all target ports&#8217; (ALL_TG_PT) flag in the parameter block of the PROUT command. Only relevant for &#8216;register&#8217; and &#8216;register and ignore existing key&#8217; sub-commands.</p>
<dt><code>-Z</code>, <code>&#8211;param-aptpl</code></p>
<dd>set the &#8216;activate persist through power loss&#8217; (APTPL) flag in the parameter block of the PROUT command. Relevant for &#8216;register&#8217;, &#8216;register and ignore existing key&#8217; and &#8216;register and move&#8217; sub-commands.</p>
<dt><code>-K</code>, <code>&#8211;param-rk</code>=<i>RK</i></p>
<dd>specify the reservation key found in the parameter block of the PROUT command. <i>RK</i> is assumed to be hex (up to 8 bytes long). Default value is 0. This option is needed by most PROUT sub-commands.</p>
<dt><code>-S</code>, <code>&#8211;param-sark</code>=<i>SARK</i></p>
<dd>specify the service action reservation key found in the parameter block of the PROUT command. <i>SARK</i> is assumed to be hex (up to 8 bytes long). Default value is 0. This option is needed by some PROUT sub-commands.</p>
<dt><code>-P</code>, <code>&#8211;preempt</code></p>
<dd>Preempt is a sub-command of the PROUT command. Preempts the existing persistent reservation (identified by <i>&#8211;param-sark=SARK</i>) with the registration key that is registered for this I_T_L nexus (identified by <i>&#8211;param-rk=RK</i>). If a new reservation is establised as a result of the preemption then the supplied <i>&#8211;prout-type=TYPE</i> is used as the type for this new reservation.</p>
<dt><code>-A</code>, <code>&#8211;preempt-abort</code></p>
<dd>Preempt and Abort is a sub-command of the PROUT command. Preempts the existing persistent reservation (identified by <i>&#8211;param-sark=SARK</i>) with the registration key that is registered for this I_T_L nexus (identified by <i>&#8211;param-rk=RK</i>). If a new reservation is establised as a result of the preemption then the supplied <i>&#8211;prout-type=TYPE</i> is used as the type for this new reservation. ACA and other pending tasks are aborted.</p>
<dt><code>-T</code>, <code>&#8211;prout-type</code>=<i>TYPE</i></p>
<dd>specify the PROUT command&#8217;s &#8216;type&#8217; argument. Required by the &#8216;register-move&#8217;, &#8216;reserve&#8217;, &#8216;release&#8217; and &#8216;preempt (and abort)&#8217; sub-commands. Valid <i>TYPE</i> values: 1-&gt; write exclusive, 3-&gt; exclusive access, 5-&gt; write exclusive &#8211; registrants only, 6-&gt; exclusive access &#8211; registrants only, 7-&gt; write exclusive &#8211; all registrants, 8-&gt; exclusive access &#8211; all registrants. Default value is 0 (which is an invalid type). Each &quot;persistent reservation type&quot; is explained in more detail in a subsection of that name in the read reservation section of the PRIN command (section 6.13.3.4 of SPC-4 revision 9).</p>
<dt><code>-s</code>, <code>&#8211;read-full-status</code></p>
<dd>Read Full Status is a sub-command of the PRIN command. For each registration with the given SCSI device, it lists the reservation key and associated information. TransportIDs, if supplied in the response, are decoded.</p>
<dt><code>-k</code>, <code>&#8211;read-keys</code></p>
<dd>Read Keys is a sub-command of the PRIN command. Lists all the reservation keys registered (i.e. registrations) with the given SCSI device. This is the default sub-command for the SCSI PRIN command.</p>
<dt><code>-r</code>, <code>&#8211;read-reservation</code></p>
<dd>Read Reservation is a sub-command of the PRIN command. List information about the current holder of the reservation on the <i>DEVICE</i>. If there is no current reservation this will be noted. Information about the current holder of the reservation includes its reservation key, scope and type.</p>
<dt><code>-s</code>, <code>&#8211;read-status</code></p>
<dd>same as <i>&#8211;read-full-status</i>.</p>
<dt><code>-G</code>, <code>&#8211;register</code></p>
<dd>Register is a sub-command of the PROUT command. It has 3 different actions depending on associated parameters. a) add a new registration with &#8216;&#8211;param-rk=0&#8217; and &#8216;&#8211;param-sark=&lt;new_rk&gt;&#8217;; b) Change an existing registration with &#8216;&#8211;param-rk=&lt;old_rk&gt;&#8217; and &#8216;&#8211;param-sark=&lt;new_rk&gt;&#8217;; or c) Delete an existing registration with &#8216;&#8211;param-rk=&lt;old_rk&gt;&#8217; and &#8216;&#8211;param-sark=0&#8217;.</p>
<dt><code>-I</code>, <code>&#8211;register-ignore</code></p>
<dd>Register and Ignore Existing Key is a sub-command of the PROUT command. Similar to <i>&#8211;register</i> except that when changing a reservation key the old key is not specified. The &#8216;&#8211;param-sark=&lt;new_rk&gt;&#8217; option should also be given.</p>
<dt><code>-M</code>, <code>&#8211;register-move</code></p>
<dd>register (another initiator) and move (the reservation held by the current initiator to that other initiator) is a sub-command of the PROUT command. It requires the transportID of the other initiator. [The standard uses the term I_T nexus but the point to stress is that there are two initiators (the one sending this command and another one) but only one logical unit.] The <i>&#8211;prout-type=TYPE</i> and <i>&#8211;param-rk=RK</i> options need to match that of the existing reservation while <i>&#8211;param-sark=SARK</i> option specifies the reservation key of the new (i.e. destination) registration.</p>
<dt><code>-Q</code>, <code>&#8211;relative-target-port</code>=<i>RTPI</i></p>
<dd>relative target port identifier that reservation is to be moved to by PROUT &#8216;register and move&#8217; sub-command. <i>RTPI</i> is assumed to be hex in the range 0 to ffff inclusive. Defaults to 0 .</p>
<dt><code>-L</code>, <code>&#8211;release</code></p>
<dd>Release is a sub-command of the PROUT command. It releases the current persistent reservation. The <i>&#8211;prout-type=TYPE</i> and <i>&#8211;param-rk=RK</i> options, matching the reservation, must also be specified.</p>
<dt><code>-c</code>, <code>&#8211;report-capabilities</code></p>
<dd>Report Capabilities is a sub-command of the PRIN command. It lists information about the aspects of persistent reservations that the <i>DEVICE</i> supports.</p>
<dt><code>-R</code>, <code>&#8211;reserve</code></p>
<dd>Reserve is a sub-command of the PROUT command. It creates a new persistent reservation (if permitted). The <i>&#8211;prout-type=TYPE</i> and <i>&#8211;param-rk=RK</i> options must also be specified.</p>
<dt><code>-X</code>, <code>&#8211;transport-id</code>=<i>TIDS</i></p>
<dd>The <i>TIDS</i> argument can take one of several forms. It can be a comma (or single space) separated list of ASCII hex bytes representing a single TransportID as defined in SPC-4. They are usually 24 bytes long apart from in iSCSI. The <i>TIDS</i> argument may be a transport specific form (e.g. &quot;sas,5000c50005b32001&quot;). The <i>TIDS</i> argument may be &quot;-&quot; in which case one or more TransportIDs can be read from stdin. The <i>TIDS</i> argument may be of the form &quot;file=&lt;name&gt;&quot; in which case one or more TransportIDs can be read from a file called &lt;name&gt;. See the &quot;TRANSPORT IDs&quot; section below for more information.</p>
<dt><code>-U</code>, <code>&#8211;unreg</code></p>
<dd>optional when the PROUT register and move sub-command is invoked. If given it will unregister the current initiator (I_T nexus) after the other initiator has been registered and the reservation moved to it. When not given the initiator (I_T nexus) that sent the PROUT command remains registered.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>print out cdb of issued commands prior to execution. If used twice prints out the parameter block associated with the PROUT command prior to its execution as well. If used thrice decodes given transportID(s) as well. To see the response to a PRIN command in low level form use the <i>&#8211;hex</i> option.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print out version string. Ignore all other parameters.</p>
<dt><code>-?</code></p>
<dd>output usage message. Ignore all other parameters.</dl>
<h2>TRANSPORT IDs</h2>
<p>TransportIDs are used in persistent reservations to identify initiators. The format of a TransportID differs depending on the type of transport being used. Their format is described in SPC-4 (in draft revision 20 see section 7.5.4). </p>
<p> A TransportID is required for the PROUT &#8216;register and move&#8217; sub-command and the PROUT &#8216;register&#8217; sub-command can have zero, one or more TransportIDs. </p>
<p> When the <i>&#8211;transport-id=TIDS</i> option is given then the <i>TIDS</i> argument may be a comma (or single space) separated list of ASCII hex bytes that represent a single TransportID as defined in SPC-4. Alternatively the <i>TIDS</i> argument may be a transport specific string starting with either &quot;fcp,&quot;, &quot;spi,&quot;, &quot;sbp,&quot;, &quot;srp,&quot;, &quot;iqn&quot;, or &quot;sas,&quot;. The &quot;iqn&quot; form is an iSCSI qualified name. Apart from &quot;iqn&quot; the other transport specific leadin string may be given in upper case (e.g. &quot;FCP,&quot;). </p>
<p> The &quot;fcp,&quot; form should be followed by 16 ASCII hex digits that represent an initiator&#8217;s N_PORT_NAME. The &quot;spi,&quot; form should be followed by &quot;&lt;scsi_address&gt;,&lt;relative_target_port_identifier&gt;&quot; (both decimal numbers). The &quot;sbp,&quot; form should be followed by 16 ASCII hex digits that represent an initiator&#8217;s EUI-64 name. The &quot;srp,&quot; form should be followed by 32 ASCII hex digits that represent an initiator port identifier. The &quot;sas,&quot; form should be followed by 16 ASCII hex digits that represent an initiator&#8217;s port SAS address. </p>
<p> There are two iSCSI qualified name forms. The shorter form contains the iSCSI name of the initiator port (e.g. &quot;iqn.5886.com.acme.diskarrays-sn-a8675309&quot;). The longer form adds the initiator session id (ISID in hex) separated by &quot;,i,0x&quot;. For example &quot;iqn.5886.com.acme.diskarrays-sn-a8675309,i,0x1234567890ab&quot;. On the command line to stop punctuation in an iSCSI name being (mis)-interpreted by the shell, putting the option argument containing the iSCSI name in double quotes is advised. iSCSI names are encoded in UTF-8 so if non (7 bit) ASCII characters appear in the iSCSI name on the command line, there will be difficulties if they are not encoded in UTF-8. The locale can be changed temporarily by prefixing the command line invocation of sg_persist with &quot;LANG=en_US.utf-8&quot; for example. </p>
<p> Alternatively the <i>TIDS</i> argument may specify a file (or pipe) from which one or more TransportIDs may be read. If the <i>TIDS</i> argument is &quot;-&quot; then stdin (standard input) is read. If the <i>TIDS</i> argument is of the form &quot;file=&lt;name&gt;&quot; than a file called &lt;name&gt; is read. A valid SPC-4 TransportID is built from the transport specific string outlined in the previous paragraphs. The parsing of the data read is realtively simple. Empty lines are ignored. Everything from and including a &quot;#&quot; on a line is ignored. Leading spaces and tabs are ignored. There can be one transportID per line. The transportID can either be a comma, space or tab separated list of ASCII hex bytes that represent a TransportID as defined in SPC-4. Padding with zero bytes to a minimum length of 24 bytes is performed if necessary. The transportID may also be transport specific string type discussed above. </p>
<p> In SPC-3 the SPEC_I_PT bit set to one and TransportIDs were allowed for the PROUT register and ignore existing key sub-command. In SPC-4 that is disallowed yielding a CHECK CONDITION status with and ILLEGAL REQUEST sense key and an additional sense code set to INVALID FIELD IN PARAMETER LIST.</p>
<h2>Notes</h2>
<p>In the 2.4 series of Linux kernels the <i>DEVICE</i> must be a SCSI generic (sg) device. In the 2.6 series any SCSI device name (e.g. /dev/sdc, /dev/st1m or /dev/sg3) can be specified. For example &quot;sg_persist &#8211;read-keys /dev/sdb&quot; will work in the 2.6 series kernels. </p>
<p> The only scope for PROUT commands supported in the current draft of SPC-4 is &quot;LU_SCOPE&quot;. Hence there seems to be no point in offering an option to set scope to another value. </p>
<p> Most errors with the PROUT sub-commands (e.g. missing or mismatched <i>&#8211;prout-type=TYPE</i>) will result in a RESERVATION CONFLICT status. This can be a bit confusing when you know there is only one (active) initiator: the &quot;conflict&quot; is with the SPC standard, not another initiator. </p>
<p> Some recent disks accept some PRIN and PROUT sub-commands when the media is stopped. One exception was setting the APTPL flag (with the <i>&#8211;param-aptpl</i> option) during a key register operation, it complained if the disk one stopped. The error indicated it wanted the disk spun up and when that happened, the registration was successful.</p>
<h2>Examples</h2>
<p>These examples use Linux device names. For suitable device names in other supported Operating Systems see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page. Due to the various option defaults the simplest example executes the &#8216;read keys&#8217; sub-command of the PRIN command:<br />
sg_persist&nbsp;<wbr>/dev/sdb This is the same as the following (long-winded) command: </p>
<pre><code>sg_persist --in --read-keys --device=/dev/sdb</code></pre>
<p> To read the current reservation either the &#8216;&#8211;read-reservation&#8217; form or the shorter &#8216;-r&#8217; can be used:<br />
sg_persist -r&nbsp;<wbr>/dev/sdb To <code>register</code> the new reservation key 0x123abc the following could be used: sg_persist &#8211;out &#8211;register &#8211;param-sark=123abc /dev/sdb Given the above registration succeeds, to <code>reserve</code> the <i>DEVICE</i> (with type &#8216;write exclusive&#8217;) the following could be used: sg_persist &#8211;out &#8211;reserve &#8211;param-rk=123abc</p>
<p>&#8211;prout-type=1 /dev/sdb To <code>release</code> the reservation the following can be given (note that the &#8211;param-rk and &#8211;prout-type arguments must match those of the reservation): sg_persist &#8211;out &#8211;release &#8211;param-rk=123abc</p>
<p>&#8211;prout-type=1 /dev/sdb Finally to <code>unregister</code> a reservation key (and not effect other registrations which is what &#8216;&#8211;clear&#8217; would do) the command is a little surprising: </p>
<pre><code>sg_persist --out --register --param-rk=123abc /dev/sdb</code></pre>
<p> Now have a close look at the difference between the register and unregister examples above. An example file that is suitably formatted to pass transportIDs via a &#8216;&#8211;transport-id=file=transport_ids.txt&#8217; option can be found in the examples sub-directory of the sg3_utils package. There is also a simple test script called sg_persist_tst.sh in the same directory. The above sequence of commands was tested successfully on a Seagate Savvio 10K.3 disk which has a SAS interface.</p>
<h2>Exit Status</h2>
<p>The exit status of sg_persist is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Author</h2>
<p>Written by Douglas Gilbert</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2004-2012 Douglas Gilbert<br />
 This software is distributed under the GPL version 2. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>sg3_utils(sg3_utils), scsires(internet)</code> </p>
