---
title: "scsi_mandat(8)"
name: "scsi_mandat"
section: "8"
letter: "s"
url: "/docs/linux/man/8-scsi_mandat/"
description: "scsi_mandat – check SCSI device support for mandatory commands"
---

<p>scsi_mandat &#8211; check SCSI device support for mandatory commands</p>
<h2>Synopsis</h2>
<p><code>scsi_mandat</code> [<i>&#8211;help</i>] [<i>&#8211;log</i>] [<i>&#8211;quiet</i>] [<i>&#8211;verbose</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>This bash shell script calls several SCSI commands on the given <i>DEVICE</i>. These SCSI commands are considered mandatory (although that varies a little depending on which standard/draft the <i>DEVICE</i> complies with). The results of each test and a pass/fail count are output.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>print out the usage message then exit.</p>
<dt><code>-L</code>, <code>&#8211;log</code></p>
<dd>the output to stderr (from each SCSI command executed) is appended to a file called &#8216;scsi_mandat.err&#8217; in the current working directory.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd>the amount of output is reduced and typically only the pass/fail count is output.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase level or verbosity.</dl>
<h2>Exit Status</h2>
<p>The exit status of this script is the number of &quot;bad&quot; errors found. So an exit status of 0 means all mandatory SCSI commands worked as expected.</p>
<h2>Authors</h2>
<p>Written by D. Gilbert</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2011-2013 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>sg_inq,sg_luns,sg_turs,sg_requests,sg_vpd,sg_senddiag (sg3_utils)</code> </p>
