---
title: "mdmon(8)"
name: "mdmon"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mdmon/"
description: "mdmon – monitor MD external metadata arrays"
---

<p>mdmon &#8211; monitor MD external metadata arrays</p>
<h2>Synopsis</h2>
<p><code>mdmon</code><i> [&#8211;all] [&#8211;takeover] [&#8211;foreground] CONTAINER</i> </p>
<h2>Overview</h2>
<p>The 2.6.27 kernel brings the ability to support external metadata arrays. External metadata implies that user space handles all updates to the metadata. The kernel&#8217;s responsibility is to notify user space when a &quot;metadata event&quot; occurs, like disk failures and clean-to-dirty transitions. The kernel, in important cases, waits for user space to take action on these notifications.</p>
<h2>Description</h2>
<h3>Metadata updates:</h3>
<p>To service metadata update requests a daemon, <i>mdmon</i>, is introduced. <i>Mdmon</i> is tasked with polling the sysfs namespace looking for changes in <code>array_state</code>, <code>sync_action</code>, and per disk <code>state</code> attributes. When a change is detected it calls a per metadata type handler to make modifications to the metadata. The following actions are taken:</p>
<dl>
<dd>
<dl>
<dt><code>array_state &#8211; inactive</code></p>
<dd>Clear the dirty bit for the volume and let the array be stopped</p>
<dt><code>array_state &#8211; write pending</code></p>
<dd>Set the dirty bit for the array and then set <code>array_state</code> to <code>active</code>. Writes are blocked until userspace writes <code>active.</code></p>
<dt><code>array_state &#8211; active-idle</code></p>
<dd>The safe mode timer has expired so set array state to clean to block writes to the array</p>
<dt><code>array_state &#8211; clean</code></p>
<dd>Clear the dirty bit for the volume</p>
<dt><code>array_state &#8211; read-only</code></p>
<dd>This is the initial state that all arrays start at. <i>mdmon</i> takes one of the three actions:</p>
<dl>
<dd>
<dl>
<dt>1/</p>
<dd>Transition the array to read-auto keeping the dirty bit clear if the metadata handler determines that the array does not need resyncing or other modification</p>
<dt>2/</p>
<dd>Transition the array to active if the metadata handler determines a resync or some other manipulation is necessary</p>
<dt>3/</p>
<dd>Leave the array read-only if the volume is marked to not be monitored; for example, the metadata version has been set to &quot;external:-dev/md127&quot; instead of &quot;external:/dev/md127&quot;</dl>
</dl>
<dt><code>sync_action &#8211; resync-to-idle</code></p>
<dd>Notify the metadata handler that a resync may have completed. If a resync process is idled before it completes this event allows the metadata handler to checkpoint resync.</p>
<dt><code>sync_action &#8211; recover-to-idle</code></p>
<dd>A spare may have completed rebuilding so tell the metadata handler about the state of each disk. This is the metadata handler&#8217;s opportunity to clear any &quot;out-of-sync&quot; bits and clear the volume&#8217;s degraded status. If a recovery process is idled before it completes this event allows the metadata handler to checkpoint recovery.</p>
<dt><code>&lt;disk&gt;/state &#8211; faulty</code></p>
<dd>A disk failure kicks off a series of events. First, notify the metadata handler that a disk has failed, and then notify the kernel that it can unblock writes that were dependent on this disk. After unblocking the kernel this disk is set to be removed+ from the member array. Finally the disk is marked failed in all other member arrays in the container.</p>
<dd>+ Note This behavior differs slightly from native MD arrays where removal is reserved for a <code>mdadm &#8211;remove</code> event. In the external metadata case the container holds the final reference on a block device and a <code>mdadm &#8211;remove &lt;container&gt; &lt;victim&gt;</code> call is still required.</dl>
</dl>
<h3>Containers:</h3>
<p>External metadata formats, like DDF, differ from the native MD metadata formats in that they define a set of disks and a series of sub-arrays within those disks. MD metadata in comparison defines a 1:1 relationship between a set of block devices and a RAID array. For example to create 2 arrays at different RAID levels on a single set of disks, MD metadata requires the disks be partitioned and then each array can be created with a subset of those partitions. The supported external formats perform this disk carving internally. Container devices simply hold references to all member disks and allow tools like <i>mdmon</i> to determine which active arrays belong to which container. Some array management commands like disk removal and disk add are now only valid at the container level. Attempts to perform these actions on member arrays are blocked with error messages like:</p>
<dl>
<dd>&quot;mdadm: Cannot remove disks from a &#8216;member&#8217; array, perform this operation on the parent container&quot;</dl>
<p> Containers are identified in /proc/mdstat with a metadata version string &quot;external:&lt;metadata name&gt;&quot;. Member devices are identified by &quot;external:/&lt;container device&gt;/&lt;member index&gt;&quot;, or &quot;external:-&lt;container device&gt;/&lt;member index&gt;&quot; if the array is to remain readonly. </p>
<h2>Options</h2>
<dl>
<dt>CONTAINER</p>
<dd>The <code>container</code> device to monitor. It can be a full path like /dev/md/container, or a simple md device name like md127.</p>
<dt><code>&#8211;foreground</code></p>
<dd>Normally, <i>mdmon</i> will fork and continue in the background. Adding this option will skip that step and run <i>mdmon</i> in the foreground.</p>
<dt><code>&#8211;takeover</code></p>
<dd>This instructs <i>mdmon</i> to replace any active <i>mdmon</i> which is currently monitoring the array. This is primarily used late in the boot process to replace any <i>mdmon</i> which was started from an <code>initramfs</code> before the root filesystem was mounted. This avoids holding a reference on that <code>initramfs</code> indefinitely and ensures that the <i>pid</i> and <i>sock</i> files used to communicate with <i>mdmon</i> are in a standard place.</p>
<dt><code>&#8211;all</code></p>
<dd>This tells mdmon to find any active containers and start monitoring each of them if appropriate. This is normally used with <code>&#8211;takeover</code> late in the boot sequence. A separate <i>mdmon</i> process is started for each container as the <code>&#8211;all</code> argument is over-written with the name of the container. To allow for containers with names longer than 5 characters, this argument can be arbitrarily extended, e.g. to <code>&#8211;all-active-arrays</code>.</p>
<dd></dl>
<p> Note that <i>mdmon</i> is automatically started by <i>mdadm</i> when needed and so does not need to be considered when working with RAID arrays. The only times it is run other than by <i>mdadm</i> is when the boot scripts need to restart it after mounting the new root filesystem.</p>
<h2>Start Up And Shutdown</h2>
<p>As <i>mdmon</i> needs to be running whenever any filesystem on the monitored device is mounted there are special considerations when the root filesystem is mounted from an <i>mdmon</i> monitored device. Note that in general <i>mdmon</i> is needed even if the filesystem is mounted read-only as some filesystems can still write to the device in those circumstances, for example to replay a journal after an unclean shutdown. </p>
<p> When the array is assembled by the <code>initramfs</code> code, mdadm will automatically start <i>mdmon</i> as required. This means that <i>mdmon</i> must be installed on the <code>initramfs</code> and there must be a writable filesystem (typically tmpfs) in which <code>mdmon</code> can create a <code>.pid</code> and <code>.sock</code> file. The particular filesystem to use is given to mdmon at compile time and defaults to <code>/run/mdadm</code>. </p>
<p> This filesystem must persist through to shutdown time. </p>
<p> After the final root filesystem has be instantiated (usually with <code>pivot_root</code>) <i>mdmon</i> should be run with <i>&#8211;all &#8211;takeover</i> so that the <i>mdmon</i> running from the <code>initramfs</code> can be replaced with one running in the main root, and so the memory used by the initramfs can be released. </p>
<p> At shutdown time, <i>mdmon</i> should not be killed along with other processes. Also as it holds a file (socket actually) open in <code>/dev</code> (by default) it will not be possible to unmount <code>/dev</code> if it is a separate filesystem.</p>
<h2>Examples</h2>
<p><code> mdmon &#8211;all-active-arrays &#8211;takeover</code><br />
 Any <i>mdmon</i> which is currently running is killed and a new instance is started. This should be run during in the boot sequence if an initramfs was used, so that any mdmon running from the initramfs will not hold the initramfs active.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-mdadm/">mdadm</a></i>(8), <i><a href="/docs/linux/man/4-md/">md</a></i>(4). </p>
