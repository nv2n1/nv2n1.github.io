---

title: "sg_referrals(8)"
name: "sg_referrals"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_referrals/"
---

<p> sg_referrals &#8211; send SCSI REPORT REFERRALS command  </p>
<h2>SYNOPSIS</h2>
<p> <code>sg_referrals</code> [<i>--help</i>] [<i>--hex</i>] [<i>--lba=LBA</i>] [<i>--maxlen=LEN</i>] [<i>--one-segment</i>] [<i>--raw</i>] [<i>--verbose</i>] [<i>--version</i>] <i>DEVICE</i>  </p>
<h2>DESCRIPTION</h2>
<p> Send the SCSI REPORT REFERRALS command to the <i>DEVICE</i> and outputs the response. This command was introduced in (draft) SBC-3 revision 24 and devices that support referrals should support this command. </p>
<p> The default action is to decode the response for all user data segment referral descriptors. The amount of output can be reduced by the <i>--lba</i> and <i>--one-segment</i> options.  </p>
<h2>OPTIONS</h2>
<p> Arguments to long options are mandatory for short options as well. </p>
<dl>
<dt><code>-h</code>, <code>--help</code></dt>
<dd> <p> output the usage message then exit. </p>
 </dd>
<dt><code>-H</code>, <code>--hex</code></dt>
<dd> <p> output response to this command in ASCII hex. </p>
 </dd>
<dt><code>-l</code>, <code>--lba</code>=<i>LBA</i></dt>
<dd> <p> where <i>LBA</i> is the Logical Block Address (LBA) in the first user data segment the <i>DEVICE</i> should report the referrals parameter data for. </p>
 </dd>
<dt><code>-m</code>, <code>--maxlen</code>=<i>LEN</i></dt>
<dd> <p> where <i>LEN</i> is the (maximum) response length in bytes. It is placed in the cdb&#8217;s &quot;allocation length&quot; field. If not given then 256 is used. 256 is enough space for the response header and user data segment descriptors. </p>
 </dd>
<dt><code>-s</code>, <code>--one-segment</code></dt>
<dd> <p> report the user data segment of the segment spefified by the <i>LBA</i> parameter only. </p>
 </dd>
<dt><code>-r</code>, <code>--raw</code></dt>
<dd> <p> output response in binary (to stdout). </p>
 </dd>
<dt><code>-v</code>, <code>--verbose</code></dt>
<dd> <p> increase the level of verbosity, (i.e. debug output). Additional output caused by this option is sent to stderr. </p>
 </dd>
<dt><code>-V</code>, <code>--version</code></dt>
<dd> <p> print the version string and then exit. </p>
 </dd></dl>
<h2>NOTES</h2>
<p> For a discussion of referrals see section 4.25 of sbc3r25.pdf at <a rel="nofollow" href="http://www.t10.org">http://www.t10.org</a> (or the corresponding section of a later draft).  </p>
<h2>EXIT STATUS</h2>
<p> The exit status of sg_referrals is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.  </p>
<h2>AUTHORS</h2>
<p> Written by Douglas Gilbert and Hannes Reinecke.  </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;dgilbert at interlog dot com&gt;.  </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2009-2012 Douglas Gilbert and Hannes Reinecke <br/>
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-sg_vpd/">sg_vpd</a>(8)</code> </p>
