---
title: "sg_reset(8)"
name: "sg_reset"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_reset/"
description: "sg_reset – sends SCSI device, target, bus or host reset; or checks reset state"
---

<p>sg_reset &#8211; sends SCSI device, target, bus or host reset; or checks reset state</p>
<h2>Synopsis</h2>
<p><code>sg_reset</code> [<i>&#8211;bus</i>] [<i>&#8211;device</i>] [<i>&#8211;help</i>] [<i>&#8211;host</i>] [<i>&#8211;no-esc</i>] [<i>&#8211;target</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>The sg_reset utility with no options (just a <i>DEVICE</i>) reports on the reset state (e.g. if a reset is underway) of the <i>DEVICE</i>. When given a <i>&#8211;device</i>, <i>&#8211;target</i>, <i>&#8211;bus</i> or <i>&#8211;host</i> option it requests a device, target, bus or host reset respectively. </p>
<p> A device reset is applied to the Logical Unit (LU) corresponding to <i>DEVICE</i>. It is most likely implemented by a Low level Driver (LLD) in Linux as a LOGICAL UNIT RESET task management function. </p>
<p> The ability to reset a SCSI target was added in Linux kernel 2.6.27 . A LLD may send Low level Drivers (LLDs) the I_T NEXUS RESET task management function. Alternatively it may use a transport mechanism to do the same thing (e.g. a hard reset on the link containing a SAS target). </p>
<p> In the Linux kernel 2.6 and 3 series this utility can be called on sd, sr (cd/dvd), st or sg device nodes; if the user has appropriate permissions. </p>
<p> Users of this utility can check whether a reset recovery is already underway before trying to send a new reset with this utility. Calling this utility with no options, just the <i>DEVICE</i>, will do such a check.</p>
<h2>Options</h2>
<dl>
<dt><code>-b</code>, <code>&#8211;bus</code></p>
<dd>attempt a SCSI bus reset. A bus reset is a SCSI Parallel Interface (SPI) concept not found in modern transports. A recent LLD may implement it as a series of resets on targets that might be considered as siblings to the target on the <i>DEVICE</i> path.</p>
<dt><code>-d</code>, <code>&#8211;device</code></p>
<dd>attempt a SCSI device reset. This would typically involve sending a LOGICAL UNIT RESET task management function to <i>DEVICE</i>.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>print the usage message then exit.</p>
<dt><code>-H</code>, <code>&#8211;host</code></p>
<dd>attempt a host reset. The &quot;host&quot; in this context is often called a Host Bus Adapter (HBA) and contains one or more SCSI initiators.</p>
<dt><code>-N</code>, <code>&#8211;no-esc</code></p>
<dd>without this option, if a device reset (<i>&#8211;device</i>) fails then it will escalate to a target reset. And if a target reset (<i>&#8211;target</i>) fails then it will escalate to a bus reset. And if a bus reset (<i>&#8211;bus</i>) fails then it will escalate to a host reset. With this option only the requested reset is attempted. An alternate option name of <i>&#8211;no-escalate</i> is also accepted.</p>
<dt><code>-t</code>, <code>&#8211;target</code></p>
<dd>attempt a SCSI target reset. A SCSI target contains one or more LUs. This would typically involve sending a I_T NEXUS RESET task management function to <i>DEVICE</i> There may be a transport action that is equivalent (e.g. in SAS a hard reset on the link that contains the target).</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the degree of verbosity (debug messages).</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>prints the version string then exits.</dl>
<h2>Notes</h2>
<p>The error recovery code within the Linux kernel (SCSI mid-level) when faced with a SCSI command timing out and no response from the device (LU) does the following. First it tries a device reset and if that is not successful tries a target reset. If that is not successful it tries a bus reset. If that is not successful it tries a host reset. The &quot;device,target,bus,host&quot; order is the reset escalation that the <i>&#8211;no-esc</i> option attempts to stop. In large storage configurations the escalation may be (very) undesirable. This utility calls the SG_SCSI_RESET ioctl and as of lk 3.10.7 the <i>&#8211;no-esc</i> option is not supported. Patches to implement this functionality have not been accepted. If you want it, post your concern to linux-scsi [at] vger.kernel.org which is the linux-scsi list. SAM-4 and 5 define a hard reset, a LOGICAL UNIT RESET and a I_T NEXUS RESET. A hard reset is defined to be a power on condition, a microcode change or a transport reset event. LOGICAL UNIT RESET and I_T NEXUS RESET can be requested via task management functions (and support for LOGICAL UNIT RESET is mandatory). In Linux the SCSI subsystem leaves it up to the LLDs as to exactly what type (if any) of reset is performed. The &quot;bus reset&quot; is SCSI Parallel Interface (SPI) concept that may not map well to recent SCSI transports so it may be a dummy operation. A &quot;host reset&quot; attempts to re-initialize the HBA that the request passes through en route to the <i>DEVICE</i>. Note that a &quot;host reset&quot; and a &quot;bus reset&quot; may cause collateral damage. This utility does not allow individual SCSI commands to be aborted. SAM-4 defines ABORT TASK and ABORT TASK SET task management functions for that. Prior to SAM-3 there was a TARGET RESET task management function. And in SAM-4 I_T NEXUS RESET appeared which seems closely related: the &quot;I_T&quot; stands for Initiator-Target. Transports may have their own types of resets not supported by this utility. For example SAS has a link reset in which both ends of a physical link (e.g. between a SAS expander and a SAS tape drive) renegotiate their connection. Prior to version 0.57 of this utility the command line had short options only (e.g. <i>-d</i> but not <i>&#8211;device</i>). Also <i>-h</i> invoked a host reset while in the current version <i>-h</i> is equivalent to <i>&#8211;help</i> and both <i>-H</i> and <i>&#8211;host</i> invoke a host reset. For backward compatibility define the environment variable SG3_UTILS_OLD_OPTS or SG_RESET_OLD_OPTS . In this case <i>-h</i> will invoke a host reset and the output will be verbose as it was previously (equivalent to using the <i>&#8211;verbose</i> option now). For example: </p>
<pre><code>SG_RESET_OLD_OPTS=1 sg_reset -h /dev/sg1

sg_reset: starting host reset

sg_reset: completed host reset</code></pre>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 1999-2013 Douglas Gilbert<br />
 This software is distributed under the GPL version 2. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
