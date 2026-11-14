---
title: "lvmlockd(8)"
name: "lvmlockd"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lvmlockd/"
description: "lvmlockd — LVM locking daemon"
---

<p>lvmlockd &#8212; LVM locking daemon</p>
<h2>Description</h2>
<p>LVM commands use lvmlockd to coordinate access to shared storage.<br />
 When LVM is used on devices shared by multiple hosts, locks will: &bull; coordinate reading and writing of LVM metadata<br />
 &bull; validate caching of LVM metadata<br />
 &bull; prevent concurrent activation of logical volumes<br />
 lvmlockd uses an external lock manager to perform basic locking.<br />
 Lock manager (lock type) options are: &bull; sanlock: places locks on disk within LVM storage.<br />
 &bull; dlm: uses network communication and a cluster manager. </p>
<h2>Options</h2>
<p>lvmlockd [options] </p>
<p> For default settings, see lvmlockd -h. </p>
<p> <code>&#8211;help | -h</code><br />
&nbsp;<wbr>&nbsp;<wbr>Show this help information. </p>
<p> <code>&#8211;version | -V</code><br />
&nbsp;<wbr>&nbsp;<wbr>Show version of lvmlockd. </p>
<p> <code>&#8211;test | -T</code><br />
&nbsp;<wbr>&nbsp;<wbr>Test mode, do not call lock manager. </p>
<p> <code>&#8211;foreground | -f</code><br />
&nbsp;<wbr>&nbsp;<wbr>Don&#8217;t fork. </p>
<p> <code>&#8211;daemon-debug | -D</code><br />
&nbsp;<wbr>&nbsp;<wbr>Don&#8217;t fork and print debugging to stdout. </p>
<p> <code>&#8211;pid-file | -p</code> <i>path</i><br />
&nbsp;<wbr>&nbsp;<wbr>Set path to the pid file. </p>
<p> <code>&#8211;socket-path | -s</code> <i>path</i><br />
&nbsp;<wbr>&nbsp;<wbr>Set path to the socket to listen on. </p>
<p> <code>&#8211;syslog-priority | -S err|warning|debug</code><br />
&nbsp;<wbr>&nbsp;<wbr>Write log messages from this level up to syslog. </p>
<p> <code>&#8211;gl-type | -g sanlock|dlm</code><br />
&nbsp;<wbr>&nbsp;<wbr>Set global lock type to be sanlock or dlm. </p>
<p> <code>&#8211;host-id | -i</code> <i>num</i><br />
&nbsp;<wbr>&nbsp;<wbr>Set the local sanlock host id. </p>
<p> <code>&#8211;host-id-file | -F</code> <i>path</i><br />
&nbsp;<wbr>&nbsp;<wbr>A file containing the local sanlock host_id. </p>
<p> <code>&#8211;sanlock-timeout | -o</code> <i>seconds</i><br />
&nbsp;<wbr>&nbsp;<wbr>Override the default sanlock I/O timeout. </p>
<p> <code>&#8211;adopt | -A 0|1</code><br />
&nbsp;<wbr>&nbsp;<wbr>Adopt locks from a previous instance of lvmlockd.</p>
<h2>Usage</h2>
<h3>Initial set up</h3>
<p>Using LVM with lvmlockd for the first time includes some one-time set up steps:</p>
<h3>1. choose a lock manager</h3>
<p><i>dlm</i><br />
 If dlm (or corosync) are already being used by other cluster software, then select dlm. dlm uses corosync which requires additional configuration beyond the scope of this document. See corosync and dlm documentation for instructions on configuration, setup and usage. </p>
<p> <i>sanlock</i><br />
 Choose sanlock if dlm/corosync are not otherwise required. sanlock does not depend on any clustering software or configuration.</p>
<h3>2. configure hosts to use lvmlockd</h3>
<p>On all hosts running lvmlockd, configure lvm.conf: </p>
<pre>locking_type = 1
use_lvmlockd = 1</pre>
<p><i>sanlock</i><br />
 Assign each host a unique host_id in the range 1-2000 by setting<br />
 /etc/lvm/lvmlocal.conf local/host_id</p>
<h3>3. start lvmlockd</h3>
<p>Use a service/init file if available, or just run &quot;lvmlockd&quot;.</p>
<h3>4. start lock manager</h3>
<p><i>sanlock</i><br />
 systemctl start wdmd sanlock </p>
<p> <i>dlm</i><br />
 Follow external clustering documentation when applicable, otherwise:<br />
 systemctl start corosync dlm</p>
<h3>5. create VG on shared devices</h3>
<p>vgcreate &#8211;shared &lt;vgname&gt; &lt;devices&gt; </p>
<p> The shared option sets the VG lock type to sanlock or dlm depending on which lock manager is running. LVM commands will perform locking for the VG using lvmlockd. lvmlockd will use the chosen lock manager.</p>
<h3>6. start VG on all hosts</h3>
<p>vgchange &#8211;lock-start </p>
<p> lvmlockd requires shared VGs to be started before they are used. This is a lock manager operation to start (join) the VG lockspace, and it may take some time. Until the start completes, locks for the VG are not available. LVM commands are allowed to read the VG while start is in progress. (An init/unit file can also be used to start VGs.)</p>
<h3>7. create and activate LVs</h3>
<p>Standard lvcreate and lvchange commands are used to create and activate LVs in a shared VG. </p>
<p> An LV activated exclusively on one host cannot be activated on another. When multiple hosts need to use the same LV concurrently, the LV can be activated with a shared lock (see lvchange options -aey vs -asy.) (Shared locks are disallowed for certain LV types that cannot be used from multiple hosts.)</p>
<h3>Normal start up and shut down</h3>
<p>After initial set up, start up and shut down include the following general steps. They can be performed manually or using the system service manager. </p>
<p> &bull; start lvmetad<br />
 &bull; start lvmlockd<br />
 &bull; start lock manager<br />
 &bull; vgchange &#8211;lock-start<br />
 &bull; activate LVs in shared VGs </p>
<p> The shut down sequence is the reverse: </p>
<p> &bull; deactivate LVs in shared VGs<br />
 &bull; vgchange &#8211;lock-stop<br />
 &bull; stop lock manager<br />
 &bull; stop lvmlockd<br />
 &bull; stop lvmetad</p>
<h2>Topics</h2>
<h3>VG access control</h3>
<p>The following terms are used to describe different forms of VG access control. </p>
<p> <i>lockd VG</i> </p>
<p> A &quot;lockd VG&quot; is a shared VG that has a &quot;lock type&quot; of dlm or sanlock. Using it requires lvmlockd. These VGs exist on shared storage that is visible to multiple hosts. LVM commands use lvmlockd to perform locking for these VGs when they are used. </p>
<p> If the lock manager for the lock type is not available (e.g. not started or failed), lvmlockd is unable to acquire locks for LVM commands. LVM commands that only read the VG will generally be allowed to continue without locks in this case (with a warning). Commands to modify or activate the VG will fail without the necessary locks. </p>
<p> <i>local VG</i> </p>
<p> A &quot;local VG&quot; is meant to be used by a single host. It has no lock type or lock type &quot;none&quot;. LVM commands and lvmlockd do not perform locking for these VGs. A local VG typically exists on local (non-shared) devices and cannot be used concurrently from different hosts. </p>
<p> If a local VG does exist on shared devices, it should be owned by a single host by having its system ID set, see <code><a href="/docs/linux/man/7-lvmsystemid/">lvmsystemid</a></code>(7). Only the host with a matching system ID can use the local VG. A VG with no lock type and no system ID should be excluded from all but one host using lvm.conf filters. Without any of these protections, a local VG on shared devices can be easily damaged or destroyed. </p>
<p> <i>clvm VG</i> </p>
<p> A &quot;clvm VG&quot; is a VG on shared storage (like a lockd VG) that requires clvmd for clustering. See below for converting a clvm VG to a lockd VG.</p>
<h3>lockd VGs from hosts not using lvmlockd</h3>
<p>Only hosts that use lockd VGs should be configured to run lvmlockd. However, shared devices used by lockd VGs may be visible from hosts not using lvmlockd. From a host not using lvmlockd, visible lockd VGs are ignored in the same way as foreign VGs (see <code><a href="/docs/linux/man/7-lvmsystemid/">lvmsystemid</a></code>(7).) </p>
<p> The &#8211;shared option for reporting and display commands causes lockd VGs to be displayed on a host not using lvmlockd, like the &#8211;foreign option does for foreign VGs.</p>
<h3>vgcreate comparison</h3>
<p>The type of VG access control is specified in the vgcreate command. See <code><a href="/docs/linux/man/8-vgcreate/">vgcreate</a></code>(8) for all vgcreate options. </p>
<p> <code>vgcreate &lt;vgname&gt; &lt;devices&gt;</code> </p>
<dl>
<dt>&bull;</p>
<dd>Creates a local VG with the local system ID when neither lvmlockd nor clvm are configured.</p>
<dt>&bull;</p>
<dd>Creates a local VG with the local system ID when lvmlockd is configured.</p>
<dt>&bull;</p>
<dd>Creates a clvm VG when clvm is configured. </p>
</dl>
<p> <code>vgcreate &#8211;shared &lt;vgname&gt; &lt;devices&gt;</code></p>
<dl>
<dt>&bull;</p>
<dd>Requires lvmlockd to be configured and running.</p>
<dt>&bull;</p>
<dd>Creates a lockd VG with lock type sanlock|dlm depending on which lock manager is running.</p>
<dt>&bull;</p>
<dd>LVM commands request locks from lvmlockd to use the VG.</p>
<dt>&bull;</p>
<dd>lvmlockd obtains locks from the selected lock manager. </p>
</dl>
<p> <code>vgcreate -c|&#8211;clustered y &lt;vgname&gt; &lt;devices&gt;</code></p>
<dl>
<dt>&bull;</p>
<dd>Requires clvm to be configured and running.</p>
<dt>&bull;</p>
<dd>Creates a clvm VG with the &quot;clustered&quot; flag.</p>
<dt>&bull;</p>
<dd>LVM commands request locks from clvmd to use the VG. </p>
</dl>
<h3>creating the first sanlock VG</h3>
<p>Creating the first sanlock VG is not protected by locking and requires special attention. This is because sanlock locks exist within the VG, so they are not available until the VG exists. The first sanlock VG will contain the &quot;global lock&quot;. </p>
<dl>
<dt>&bull;</p>
<dd>The first vgcreate command needs to be given the path to a device that has not yet been initialized with pvcreate. The pvcreate initialization will be done by vgcreate. This is because the pvcreate command requires the global lock, which will not be available until after the first sanlock VG is created. </p>
<dt>&bull;</p>
<dd>While running vgcreate for the first sanlock VG, ensure that the device being used is not used by another LVM command. Allocation of shared devices is usually protected by the global lock, but this cannot be done for the first sanlock VG which will hold the global lock. </p>
<dt>&bull;</p>
<dd>While running vgcreate for the first sanlock VG, ensure that the VG name being used is not used by another LVM command. Uniqueness of VG names is usually ensured by the global lock. </p>
<dt>&bull;</p>
<dd>Because the first sanlock VG will contain the global lock, this VG needs to be accessible to all hosts that will use sanlock shared VGs. All hosts will need to use the global lock from the first sanlock VG. </p>
<p> See below for more information about managing the sanlock global lock. </p>
</dl>
<h3>using lockd VGs</h3>
<p>There are some special considerations when using lockd VGs. </p>
<p> When use_lvmlockd is first enabled in lvm.conf, and before the first lockd VG is created, no global lock will exist. In this initial state, LVM commands try and fail to acquire the global lock, producing a warning, and some commands are disallowed. Once the first lockd VG is created, the global lock will be available, and LVM will be fully operational. </p>
<p> When a new lockd VG is created, its lockspace is automatically started on the host that creates it. Other hosts need to run &#8216;vgchange &#8211;lock-start&#8217; to start the new VG before they can use it. </p>
<p> From the &#8216;vgs&#8217; command, lockd VGs are indicated by &quot;s&quot; (for shared) in the sixth attr field. The specific lock type and lock args for a lockd VG can be displayed with &#8216;vgs -o+locktype,lockargs&#8217;. </p>
<p> lockd VGs need to be &quot;started&quot; and &quot;stopped&quot;, unlike other types of VGs. See the following section for a full description of starting and stopping. </p>
<p> vgremove of a lockd VG will fail if other hosts have the VG started. Run vgchange &#8211;lock-stop &lt;vgname&gt; on all other hosts before vgremove. (It may take several seconds before vgremove recognizes that all hosts have stopped a sanlock VG.)</p>
<h3>starting and stopping VGs</h3>
<p>Starting a lockd VG (vgchange &#8211;lock-start) causes the lock manager to start (join) the lockspace for the VG on the host where it is run. This makes locks for the VG available to LVM commands on the host. Before a VG is started, only LVM commands that read/display the VG are allowed to continue without locks (and with a warning). </p>
<p> Stopping a lockd VG (vgchange &#8211;lock-stop) causes the lock manager to stop (leave) the lockspace for the VG on the host where it is run. This makes locks for the VG inaccessible to the host. A VG cannot be stopped while it has active LVs. </p>
<p> When using the lock type sanlock, starting a VG can take a long time (potentially minutes if the host was previously shut down without cleanly stopping the VG.) </p>
<p> A lockd VG can be started after all the following are true:<br />
 &bull; lvmlockd is running<br />
 &bull; the lock manager is running<br />
 &bull; the VG is visible to the system </p>
<p> A lockd VG can be stopped if all LVs are deactivated. </p>
<p> All lockd VGs can be started/stopped using:<br />
 vgchange &#8211;lock-start<br />
 vgchange &#8211;lock-stop </p>
<p> Individual VGs can be started/stopped using:<br />
 vgchange &#8211;lock-start &lt;vgname&gt; &#8230;<br />
 vgchange &#8211;lock-stop &lt;vgname&gt; &#8230; </p>
<p> To make vgchange not wait for start to complete:<br />
 vgchange &#8211;lock-start &#8211;lock-opt nowait &#8230; </p>
<p> lvmlockd can be asked directly to stop all lockspaces:<br />
 lvmlockctl &#8211;stop-lockspaces </p>
<p> To start only selected lockd VGs, use the lvm.conf activation/lock_start_list. When defined, only VG names in this list are started by vgchange. If the list is not defined (the default), all visible lockd VGs are started. To start only &quot;vg1&quot;, use the following lvm.conf configuration: </p>
<pre>activation {
 lock_start_list = [ &quot;vg1&quot; ]
 ...
}</pre>
<h3>automatic starting and automatic activation</h3>
<p>Scripts or programs on a host that automatically start VGs will use the &quot;auto&quot; option to indicate that the command is being run automatically by the system: </p>
<p> vgchange &#8211;lock-start &#8211;lock-opt auto [&lt;vgname&gt; &#8230;] </p>
<p> Without any additional configuration, including the &quot;auto&quot; option has no effect; all VGs are started unless restricted by lock_start_list. </p>
<p> However, when the lvm.conf activation/auto_lock_start_list is defined, the auto start command performs an additional filtering phase to all VGs being started, testing each VG name against the auto_lock_start_list. The auto_lock_start_list defines lockd VGs that will be started by the auto start command. Visible lockd VGs not included in the list are ignored by the auto start command. If the list is undefined, all VG names pass this filter. (The lock_start_list is also still used to filter all VGs.) </p>
<p> The auto_lock_start_list allows a user to select certain lockd VGs that should be automatically started by the system (or indirectly, those that should not). </p>
<p> To use auto activation of lockd LVs (see auto_activation_volume_list), auto starting of the corresponding lockd VGs is necessary.</p>
<h3>internal command locking</h3>
<p>To optimize the use of LVM with lvmlockd, be aware of the three kinds of locks and when they are used: </p>
<p> <i>GL lock</i> </p>
<p> The global lock (GL lock) is associated with global information, which is information not isolated to a single VG. This includes: </p>
<p> &bull; The global VG namespace.<br />
 &bull; The set of orphan PVs and unused devices.<br />
 &bull; The properties of orphan PVs, e.g. PV size. </p>
<p> The global lock is used in shared mode by commands that read this information, or in exclusive mode by commands that change it. </p>
<p> The command &#8216;vgs&#8217; acquires the global lock in shared mode because it reports the list of all VG names. </p>
<p> The vgcreate command acquires the global lock in exclusive mode because it creates a new VG name, and it takes a PV from the list of unused PVs. </p>
<p> When an LVM command is given a tag argument, or uses select, it must read all VGs to match the tag or selection, which causes the global lock to be acquired. </p>
<p> <i>VG lock</i> </p>
<p> A VG lock is associated with each VG. The VG lock is acquired in shared mode to read the VG and in exclusive mode to change the VG (modify the VG metadata or activate LVs). This lock serializes access to a VG with all other LVM commands accessing the VG from all hosts. </p>
<p> The command &#8216;vgs&#8217; will not only acquire the GL lock to read the list of all VG names, but will acquire the VG lock for each VG prior to reading it. </p>
<p> The command &#8216;vgs &lt;vgname&gt;&#8217; does not acquire the GL lock (it does not need the list of all VG names), but will acquire the VG lock on each VG name argument. </p>
<p> <i>LV lock</i> </p>
<p> An LV lock is acquired before the LV is activated, and is released after the LV is deactivated. If the LV lock cannot be acquired, the LV is not activated. LV locks are persistent and remain in place after the activation command is done. GL and VG locks are transient, and are held only while an LVM command is running. </p>
<p> <i>lock retries</i> </p>
<p> If a request for a GL or VG lock fails due to a lock conflict with another host, lvmlockd automatically retries for a short time before returning a failure to the LVM command. If those retries are insufficient, the LVM command will retry the entire lock request a number of times specified by global/lvmlockd_lock_retries before failing. If a request for an LV lock fails due to a lock conflict, the command fails immediately.</p>
<h3>managing the global lock in sanlock VGs</h3>
<p>The global lock exists in one of the sanlock VGs. The first sanlock VG created will contain the global lock. Subsequent sanlock VGs will each contain disabled global locks that can be enabled later if necessary. </p>
<p> The VG containing the global lock must be visible to all hosts using sanlock VGs. This can be a reason to create a small sanlock VG, visible to all hosts, and dedicated to just holding the global lock. While not required, this strategy can help to avoid difficulty in the future if VGs are moved or removed. </p>
<p> The vgcreate command typically acquires the global lock, but in the case of the first sanlock VG, there will be no global lock to acquire until the first vgcreate is complete. So, creating the first sanlock VG is a special case that skips the global lock. </p>
<p> vgcreate for a sanlock VG determines it is the first one to exist if no other sanlock VGs are visible. It is possible that other sanlock VGs do exist but are not visible on the host running vgcreate. In this case, vgcreate would create a new sanlock VG with the global lock enabled. When the other VG containing a global lock appears, lvmlockd will see more than one VG with a global lock enabled, and LVM commands will report that there are duplicate global locks. </p>
<p> If the situation arises where more than one sanlock VG contains a global lock, the global lock should be manually disabled in all but one of them with the command: </p>
<p> lvmlockctl &#8211;gl-disable &lt;vgname&gt; </p>
<p> (The one VG with the global lock enabled must be visible to all hosts.) </p>
<p> An opposite problem can occur if the VG holding the global lock is removed. In this case, no global lock will exist following the vgremove, and subsequent LVM commands will fail to acquire it. In this case, the global lock needs to be manually enabled in one of the remaining sanlock VGs with the command: </p>
<p> lvmlockctl &#8211;gl-enable &lt;vgname&gt; </p>
<p> A small sanlock VG dedicated to holding the global lock can avoid the case where the GL lock must be manually enabled after a vgremove.</p>
<h3>internal lvmlock LV</h3>
<p>A sanlock VG contains a hidden LV called &quot;lvmlock&quot; that holds the sanlock locks. vgreduce cannot yet remove the PV holding the lvmlock LV. To remove this PV, change the VG lock type to &quot;none&quot;, run vgreduce, then change the VG lock type back to &quot;sanlock&quot;. Similarly, pvmove cannot be used on a PV used by the lvmlock LV. </p>
<p> To place the lvmlock LV on a specific device, create the VG with only that device, then use vgextend to add other devices.</p>
<h3>shared LVs</h3>
<p>When an LV is used concurrently from multiple hosts (e.g. by a multi-host/cluster application or file system), the LV can be activated on multiple hosts concurrently using a shared lock. </p>
<p> To activate the LV with a shared lock: lvchange -asy vg/lv. </p>
<p> With lvmlockd, an unspecified activation mode is always exclusive, i.e. -ay defaults to -aey. </p>
<p> If the LV type does not allow the LV to be used concurrently from multiple hosts, then a shared activation lock is not allowed and the lvchange command will report an error. LV types that cannot be used concurrently from multiple hosts include thin, cache, raid, mirror, and snapshot. </p>
<p> lvextend on LV with shared locks is not yet allowed. The LV must be deactivated, or activated exclusively to run lvextend.</p>
<h3>recover from lost PV holding sanlock locks</h3>
<p>The general approach is to change the VG lock type to &quot;none&quot;, and then change the lock type back to &quot;sanlock&quot;. This recreates the internal lvmlock LV and the necessary locks on it. Additional steps may be required to deal with the missing PV.</p>
<h3>locking system failures</h3>
<p><code>lvmlockd failure</code> </p>
<p> If lvmlockd fails or is killed while holding locks, the locks are orphaned in the lock manager. lvmlockd can be restarted with an option to adopt locks in the lock manager that had been held by the previous instance. </p>
<p> <code>dlm/corosync failure</code> </p>
<p> If dlm or corosync fail, the clustering system will fence the host using a method configured within the dlm/corosync clustering environment. </p>
<p> LVM commands on other hosts will be blocked from acquiring any locks until the dlm/corosync recovery process is complete. </p>
<p> <code>sanlock lease storage failure</code> </p>
<p> If the PV under a sanlock VG&#8217;s lvmlock LV is disconnected, unresponsive or too slow, sanlock cannot renew the lease for the VG&#8217;s locks. After some time, the lease will expire, and locks that the host owns in the VG can be acquired by other hosts. The VG must be forcibly deactivated on the host with the expiring lease before other hosts can acquire its locks. </p>
<p> When the sanlock daemon detects that the lease storage is lost, it runs the command lvmlockctl &#8211;kill &lt;vgname&gt;. This command emits a syslog message stating that lease storage is lost for the VG and LVs must be immediately deactivated. </p>
<p> If no LVs are active in the VG, then the lockspace with an expiring lease will be removed, and errors will be reported when trying to use the VG. Use the lvmlockctl &#8211;drop command to clear the stale lockspace from lvmlockd. </p>
<p> If the VG has active LVs when the lock storage is lost, the LVs must be quickly deactivated before the lockspace lease expires. After all LVs are deactivated, run lvmlockctl &#8211;drop &lt;vgname&gt; to clear the expiring lockspace from lvmlockd. If all LVs in the VG are not deactivated within about 40 seconds, sanlock will reset the host using the local watchdog. The machine reset is effectively a severe form of &quot;deactivating&quot; LVs before they can be activated on other hosts. The reset is considered a better alternative than having LVs used by multiple hosts at once, which could easily damage or destroy their content. </p>
<p> In the future, the lvmlockctl kill command may automatically attempt to forcibly deactivate LVs before the sanlock lease expires. Until then, the user must notice the syslog message and manually deactivate the VG before sanlock resets the machine. </p>
<p> <code>sanlock daemon failure</code> </p>
<p> If the sanlock daemon fails or exits while a lockspace is started, the local watchdog will reset the host. This is necessary to protect any application resources that depend on sanlock leases which will be lost without sanlock running.</p>
<h3>changing dlm cluster name</h3>
<p>When a dlm VG is created, the cluster name is saved in the VG metadata. To use the VG, a host must be in the named dlm cluster. If the dlm cluster name changes, or the VG is moved to a new cluster, the dlm cluster name saved in the VG must also be changed. </p>
<p> To see the dlm cluster name saved in the VG, use the command:<br />
 vgs -o+locktype,lockargs &lt;vgname&gt; </p>
<p> To change the dlm cluster name in the VG when the VG is still used by the original cluster: </p>
<dl>
<dt>&bull;</p>
<dd>Stop the VG on all hosts:<br />
 vgchange &#8211;lock-stop &lt;vgname&gt; </p>
<dt>&bull;</p>
<dd>Change the VG lock type to none:<br />
 vgchange &#8211;lock-type none &lt;vgname&gt; </p>
<dt>&bull;</p>
<dd>Change the dlm cluster name on the host or move the VG to the new cluster. The new dlm cluster must now be active on the host. Verify the new name by:<br />
 cat /sys/kernel/config/dlm/cluster/cluster_name </p>
<dt>&bull;</p>
<dd>Change the VG lock type back to dlm which sets the new cluster name:<br />
 vgchange &#8211;lock-type dlm &lt;vgname&gt; </p>
<dt>&bull;</p>
<dd>Start the VG on hosts to use it:<br />
 vgchange &#8211;lock-start &lt;vgname&gt; </p>
</dl>
<p> To change the dlm cluster name in the VG when the dlm cluster name has already changed, or the VG has already moved to a different cluster: </p>
<dl>
<dt>&bull;</p>
<dd>Ensure the VG is not being used by any hosts. </p>
<dt>&bull;</p>
<dd>The new dlm cluster must be active on the host making the change. The current dlm cluster name can be seen by:<br />
 cat /sys/kernel/config/dlm/cluster/cluster_name </p>
<dt>&bull;</p>
<dd>Change the VG lock type to none:<br />
 vgchange &#8211;lock-type none &#8211;force &lt;vgname&gt; </p>
<dt>&bull;</p>
<dd>Change the VG lock type back to dlm which sets the new cluster name:<br />
 vgchange &#8211;lock-type dlm &lt;vgname&gt; </p>
<dt>&bull;</p>
<dd>Start the VG on hosts to use it:<br />
 vgchange &#8211;lock-start &lt;vgname&gt; </p>
</dl>
<h3>changing a local VG to a lockd VG</h3>
<p>All LVs must be inactive to change the lock type. </p>
<p> lvmlockd must be configured and running as described in USAGE. </p>
<p> Change a local VG to a lockd VG with the command:<br />
 vgchange &#8211;lock-type sanlock|dlm &lt;vgname&gt; </p>
<p> Start the VG on hosts to use it:<br />
 vgchange &#8211;lock-start &lt;vgname&gt;</p>
<h3>changing a lockd VG to a local VG</h3>
<p>Stop the lockd VG on all hosts, then run:<br />
 vgchange &#8211;lock-type none &lt;vgname&gt; </p>
<p> To change a VG from one lockd type to another (i.e. between sanlock and dlm), first change it to a local VG, then to the new type.</p>
<h3>changing a clvm VG to a lockd VG</h3>
<p>All LVs must be inactive to change the lock type. </p>
<p> First change the clvm VG to a local VG. Within a running clvm cluster, change a clvm VG to a local VG with the command: </p>
<p> vgchange -cn &lt;vgname&gt; </p>
<p> If the clvm cluster is no longer running on any nodes, then extra options can be used to forcibly make the VG local. Caution: this is only safe if all nodes have stopped using the VG: </p>
<p> vgchange &#8211;config &#8216;global/locking_type=0 global/use_lvmlockd=0&#8217;</p>
<dl>
<dd>-cn &lt;vgname&gt;</dl>
<p> After the VG is local, follow the steps described in &quot;changing a local VG to a lockd VG&quot;.</p>
<h3>limitations of lockd VGs</h3>
<p>Things that do not yet work in lockd VGs:<br />
 &bull; creating a new thin pool and a new thin LV in a single command<br />
 &bull; using lvcreate to create cache pools or cache LVs (use lvconvert)<br />
 &bull; using external origins for thin LVs<br />
 &bull; splitting mirrors and snapshots from LVs<br />
 &bull; vgsplit<br />
 &bull; vgmerge<br />
 &bull; resizing an LV that is active in the shared mode on multiple hosts</p>
<h3>lvmlockd changes from clvmd</h3>
<p>(See above for converting an existing clvm VG to a lockd VG.) </p>
<p> While lvmlockd and clvmd are entirely different systems, LVM command usage remains similar. Differences are more notable when using lvmlockd&#8217;s sanlock option. </p>
<p> Visible usage differences between lockd VGs with lvmlockd and clvm VGs with clvmd: </p>
<dl>
<dt>&bull;</p>
<dd>lvm.conf must be configured to use either lvmlockd (use_lvmlockd=1) or clvmd (locking_type=3), but not both. </p>
<dt>&bull;</p>
<dd>vgcreate &#8211;shared creates a lockd VG, and vgcreate &#8211;clustered y creates a clvm VG. </p>
<dt>&bull;</p>
<dd>lvmlockd adds the option of using sanlock for locking, avoiding the need for network clustering. </p>
<dt>&bull;</p>
<dd>lvmlockd defaults to the exclusive activation mode whenever the activation mode is unspecified, i.e. -ay means -aey, not -asy. </p>
<dt>&bull;</p>
<dd>lvmlockd commands always apply to the local host, and never have an effect on a remote host. (The activation option &#8216;l&#8217; is not used.) </p>
<dt>&bull;</p>
<dd>lvmlockd works with thin and cache pools and LVs. </p>
<dt>&bull;</p>
<dd>lvmlockd works with lvmetad. </p>
<dt>&bull;</p>
<dd>lvmlockd saves the cluster name for a lockd VG using dlm. Only hosts in the matching cluster can use the VG. </p>
<dt>&bull;</p>
<dd>lvmlockd requires starting/stopping lockd VGs with vgchange &#8211;lock-start and &#8211;lock-stop. </p>
<dt>&bull;</p>
<dd>vgremove of a sanlock VG may fail indicating that all hosts have not stopped the VG lockspace. Stop the VG on all hosts using vgchange &#8211;lock-stop. </p>
<dt>&bull;</p>
<dd>vgreduce or pvmove of a PV in a sanlock VG will fail if it holds the internal &quot;lvmlock&quot; LV that holds the sanlock locks. </p>
<dt>&bull;</p>
<dd>lvmlockd uses lock retries instead of lock queueing, so high lock contention may require increasing global/lvmlockd_lock_retries to avoid transient lock failures. </p>
<dt>&bull;</p>
<dd>lvmlockd includes VG reporting options lock_type and lock_args, and LV reporting option lock_args to view the corresponding metadata fields. </p>
<dt>&bull;</p>
<dd>In the &#8216;vgs&#8217; command&#8217;s sixth VG attr field, &quot;s&quot; for &quot;shared&quot; is displayed for lockd VGs. </p>
<dt>&bull;</p>
<dd>If lvmlockd fails or is killed while in use, locks it held remain but are orphaned in the lock manager. lvmlockd can be restarted with an option to adopt the orphan locks from the previous instance of lvmlockd. </p>
</dl>
