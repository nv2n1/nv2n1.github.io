---
title: "sg_rdac(8)"
name: "sg_rdac"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_rdac/"
description: "sg_rdac – display or modify SCSI RDAC Redundant Controller mode page"
---

<p>sg_rdac &#8211; display or modify SCSI RDAC Redundant Controller mode page</p>
<h2>Synopsis</h2>
<p><code>sg_rdac</code> [<i>-a</i>] [<i>-f=LUN</i>] [<i>-v</i>] [<i>-V</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>sg_rdac displays or modifies the RDAC controller settings via the Redundant Controller mode page (0x2C). When modifying the settings it allows to transfer the ownership of individual drives to the controller the command was received on.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code></p>
<dd>Transfer all (visible) devices</p>
<dt><code>-f</code>=<i>LUN</i></p>
<dd>Transfer the device identified by <i>LUN</i>. This command will only work if the controller supports &#8216;Dual Active Mode&#8217; (aka active/active mode). <i>LUN</i> is a decimal number which cannot exceed 31 when the <i>-6</i> option is given, otherwise is cannot exceed 255.</p>
<dt><code>-v</code></p>
<dd>be verbose</p>
<dt><code>-V</code></p>
<dd>print version string then exit</dl>
<h2>Exit Status</h2>
<p>The exit status of sg_rdac is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Author</h2>
<p>Written by Hannes Reinecke &lt;hare at suse dot com&gt;, based on sg_emc_trespass.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2006-2016 Hannes Reinecke, Douglas Gilbert.<br />
 This software is distributed under the GPL version 2. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
