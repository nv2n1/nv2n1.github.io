---
title: "gluster(8)"
name: "gluster"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gluster/"
description: "gluster – Gluster Console Manager (command line utility)"
---

<p>gluster &#8211; Gluster Console Manager (command line utility)</p>
<h2>Synopsis</h2>
<p><code>gluster</code> To run the program and display gluster prompt: <code>gluster [&#8211;xml]</code> (or) To specify a command directly: <code>gluster</code> <i>[commands] [options] [&#8211;xml]</i> </p>
<h2>Description</h2>
<p>The Gluster Console Manager is a command line utility for elastic volume management. You can run the gluster command on any export server. The command enables administrators to perform cloud operations, such as creating, expanding, shrinking, rebalancing, and migrating volumes without needing to schedule server downtime.</p>
<h2>Commands</h2>
<h3>Volume Commands</h3>
<dl>
<dd><code>&nbsp;<wbr>volume info [all|&lt;VOLNAME&gt;] </code> Display information about all volumes, or the specified volume.</p>
<dt><code>&nbsp;<wbr>volume create &lt;NEW-VOLNAME&gt; [stripe &lt;COUNT&gt;] [replica &lt;COUNT&gt;] [disperse [&lt;COUNT&gt;]] [redundancy &lt;COUNT&gt;] [transport &lt;tcp|rdma|tcp,rdma&gt;] &lt;NEW-BRICK&gt; &#8230; </code></p>
<dd>Create a new volume of the specified type using the specified bricks and transport type (the default transport type is tcp). To create a volume with both transports (tcp and rdma), give &#8216;transport tcp,rdma&#8217; as an option.</p>
<dt><code>&nbsp;<wbr>volume delete &lt;VOLNAME&gt; </code></p>
<dd>Delete the specified volume.</p>
<dt><code>&nbsp;<wbr>volume start &lt;VOLNAME&gt; </code></p>
<dd>Start the specified volume.</p>
<dt><code>&nbsp;<wbr>volume stop &lt;VOLNAME&gt; [force] </code></p>
<dd>Stop the specified volume.</p>
<dt><code>&nbsp;<wbr>volume set &lt;VOLNAME&gt; &lt;OPTION&gt; &lt;PARAMETER&gt; [&lt;OPTION&gt; &lt;PARAMETER&gt;] &#8230; </code></p>
<dd>Set the volume options.</p>
<dt><code>&nbsp;<wbr>volume get &lt;VOLNAME&gt; &lt;OPTION/all&gt;</code></p>
<dd>Get the volume options.</p>
<dt><code>&nbsp;<wbr>volume help </code></p>
<dd>Display help for the volume command.</dl>
<h3>Brick Commands</h3>
<dl>
<dt><code>&nbsp;<wbr>volume add-brick &lt;VOLNAME&gt; &lt;NEW-BRICK&gt; &#8230; </code></p>
<dd>Add the specified brick to the specified volume.</p>
<dt><code>&nbsp;<wbr>volume remove-brick &lt;VOLNAME&gt; &lt;BRICK&gt; &#8230; </code></p>
<dd>Remove the specified brick from the specified volume.</p>
<dd><code>Note:</code> If you remove the brick, the data stored in that brick will not be available. You can migrate data from one brick to another using <code>replace-brick</code> option.</p>
<dt><code>&nbsp;<wbr>volume replace-brick &lt;VOLNAME&gt; &lt;SOURCE-BRICK&gt; &lt;NEW-BRICK&gt; commit force </code></p>
<dd>Replace the specified source brick with a new brick.</p>
<dt><code>&nbsp;<wbr>volume rebalance &lt;VOLNAME&gt; start </code></p>
<dd>Start rebalancing the specified volume.</p>
<dt><code>&nbsp;<wbr>volume rebalance &lt;VOLNAME&gt; stop </code></p>
<dd>Stop rebalancing the specified volume.</p>
<dt><code>&nbsp;<wbr>volume rebalance &lt;VOLNAME&gt; status </code></p>
<dd>Display the rebalance status of the specified volume.</dl>
<h3>Log Commands</h3>
<dl>
<dt><code>&nbsp;<wbr>volume log filename &lt;VOLNAME&gt; [BRICK] &lt;DIRECTORY&gt;</p>
<dd>Set the log directory for the corresponding volume/brick.</p>
<dt>&nbsp;<wbr>volume log locate &lt;VOLNAME&gt; [BRICK]</p>
<dd>Locate the log file for corresponding volume/brick.</p>
<dt>&nbsp;<wbr>volume log rotate &lt;VOLNAME&gt; [BRICK]</p>
<dd>Rotate the log file for corresponding volume/brick.</dl>
<p> </code></p>
<h3>Peer Commands</h3>
<dl>
<dt><code>&nbsp;<wbr>peer probe &lt;HOSTNAME&gt; </code></p>
<dd>Probe the specified peer. In case the &lt;HOSTNAME&gt; given belongs to an already probed peer, the peer probe command will add the hostname to the peer if required.</p>
<dt><code>&nbsp;<wbr>peer detach &lt;HOSTNAME&gt; </code></p>
<dd>Detach the specified peer.</p>
<dt><code>&nbsp;<wbr>peer status </code></p>
<dd>Display the status of peers.</p>
<dt><code>&nbsp;<wbr>peer help </code></p>
<dd>Display help for the peer command.</dl>
<h3>Tier Commands</h3>
<dl>
<dt><code>&nbsp;<wbr>volume tier &lt;VOLNAME&gt; attach [&lt;replica COUNT&gt;] &lt;NEW-BRICK&gt;&#8230; </code></p>
<dd>Attach to an existing volume a tier of specified type using the specified bricks.</p>
<dt><code>&nbsp;<wbr>volume tier &lt;VOLNAME&gt; status </code></p>
<dd>Display statistics on data migration between the hot and cold tiers.</p>
<dt><code>&nbsp;<wbr>volume tier &lt;VOLNAME&gt; detach start</code></p>
<dd>Begin detaching the hot tier from the volume. Data will be moved from the hot tier to the cold tier.</p>
<dt><code>&nbsp;<wbr>volume tier &lt;VOLNAME&gt; detach commit [force]</code></p>
<dd>Commit detaching the hot tier from the volume. The volume will revert to its original state before the hot tier was attached.</p>
<dt><code>&nbsp;<wbr>volume tier &lt;VOLNAME&gt; detach status</code></p>
<dd>Check status of data movement from the hot to cold tier.</p>
<dt><code>&nbsp;<wbr>volume tier &lt;VOLNAME&gt; detach stop</code></p>
<dd>Stop detaching the hot tier from the volume.</dl>
<h3>Geo-replication Commands</h3>
<dl>
<dt><i>&nbsp;<wbr>Note</i>: password-less ssh, from the master node (where these commands are executed) to the slave node &lt;SLAVE_HOST&gt;, is a prerequisite for the geo-replication commands.</p>
<dd>
<dt><code>&nbsp;<wbr>system:: execute gsec_create</code></p>
<dd>Generates pem keys which are required for push-pem</p>
<dt><code>&nbsp;<wbr>volume geo-replication &lt;MASTER_VOL&gt; &lt;SLAVE_HOST&gt;::&lt;SLAVE_VOL&gt; create [push-pem] [force]</code></p>
<dd>Create a new geo-replication session from &lt;MASTER_VOL&gt; to &lt;SLAVE_HOST&gt; host machine having &lt;SLAVE_VOL&gt;. Use push-pem to push the keys automatically.</p>
<dt><code>&nbsp;<wbr>volume geo-replication &lt;MASTER_VOL&gt; &lt;SLAVE_HOST&gt;::&lt;SLAVE_VOL&gt; {start|stop} [force] </code></p>
<dd>Start/stop the geo-replication session from &lt;MASTER_VOL&gt; to &lt;SLAVE_HOST&gt; host machine having &lt;SLAVE_VOL&gt;.</p>
<dt><code>&nbsp;<wbr>volume geo-replication [&lt;MASTER_VOL&gt; [&lt;SLAVE_HOST&gt;::&lt;SLAVE_VOL&gt;]] status [detail] </code></p>
<dd>Query status of the geo-replication session from &lt;MASTER_VOL&gt; to &lt;SLAVE_HOST&gt; host machine having &lt;SLAVE_VOL&gt;.</p>
<dt><code>&nbsp;<wbr>volume geo-replication &lt;MASTER_VOL&gt; &lt;SLAVE_HOST&gt;::&lt;SLAVE_VOL&gt; {pause|resume} [force] </code></p>
<dd>Pause/resume the geo-replication session from &lt;MASTER_VOL&gt; to &lt;SLAVE_HOST&gt; host machine having &lt;SLAVE_VOL&gt;.</p>
<dt><code>&nbsp;<wbr>volume geo-replication &lt;MASTER_VOL&gt; &lt;SLAVE_HOST&gt;::&lt;SLAVE_VOL&gt; delete [reset-sync-time]</code></p>
<dd>Delete the geo-replication session from &lt;MASTER_VOL&gt; to &lt;SLAVE_HOST&gt; host machine having &lt;SLAVE_VOL&gt;. Optionally you can also reset the sync time in case you need to resync the entire volume on session recreate.</p>
<dt><code>&nbsp;<wbr>volume geo-replication &lt;MASTER_VOL&gt; &lt;SLAVE_HOST&gt;::&lt;SLAVE_VOL&gt; config [[!]&lt;options&gt; [&lt;value&gt;]] </code></p>
<dd>View (when no option provided) or set configuration for this geo-replication session. Use &quot;!&lt;OPTION&gt;&quot; to reset option &lt;OPTION&gt; to default value.</dl>
<h3>Bitrot Commands</h3>
<dl>
<dt><code>&nbsp;<wbr>volume bitrot &lt;VOLNAME&gt; {enable|disable} </code></p>
<dd>Enable/disable bitrot for volume &lt;VOLNAME&gt;</p>
<dt><code>&nbsp;<wbr>volume bitrot &lt;VOLNAME&gt; scrub-throttle {lazy|normal|aggressive} </code></p>
<dd>Scrub-throttle value is a measure of how fast or slow the scrubber scrubs the filesystem for volume &lt;VOLNAME&gt;</p>
<dt><code>&nbsp;<wbr>volume bitrot &lt;VOLNAME&gt; scrub-frequency {daily|weekly|biweekly|monthly} </code></p>
<dd>Scrub frequency for volume &lt;VOLNAME&gt;</p>
<dt><code>&nbsp;<wbr>volume bitrot &lt;VOLNAME&gt; scrub {pause|resume|status|ondemand} </code></p>
<dd>Pause/Resume scrub. Upon resume, scrubber continues where it left off. status option shows the statistics of scrubber. ondemand option starts the scrubbing immediately if the scrubber is not paused or already running.</p>
<dt></dl>
<h3>Snapshot Commands</h3>
<dd>
<dl>
<dt><code>&nbsp;<wbr>snapshot create &lt;snapname&gt; &lt;volname&gt; [no-timestamp] [description &lt;description&gt;] [force] </code></p>
<dd>Creates a snapshot of a GlusterFS volume. User can provide a snap-name and a description to identify the snap. Snap will be created by appending timestamp in GMT. User can override this behaviour using &quot;no-timestamp&quot; option. The description cannot be more than 1024 characters. To be able to take a snapshot, volume should be present and it should be in started state.</p>
<dt><code>&nbsp;<wbr>snapshot restore &lt;snapname&gt; </code></p>
<dd>Restores an already taken snapshot of a GlusterFS volume. Snapshot restore is an offline activity therefore if the volume is online (in started state) then the restore operation will fail. Once the snapshot is restored it will not be available in the list of snapshots.</p>
<dt><code>&nbsp;<wbr>snapshot clone &lt;clonename&gt; &lt;snapname&gt; </code></p>
<dd>Create a clone of a snapshot volume, the resulting volume will be GlusterFS volume. User can provide a clone-name. To be able to take a clone, snapshot should be present and it should be in activated state.</p>
<dt><code>&nbsp;<wbr>snapshot delete ( all | &lt;snapname&gt; | volume &lt;volname&gt; ) </code></p>
<dd>If snapname is specified then mentioned snapshot is deleted. If volname is specified then all snapshots belonging to that particular volume is deleted. If keyword *all* is used then all snapshots belonging to the system is deleted.</p>
<dt><code>&nbsp;<wbr>snapshot list [volname] </code></p>
<dd>Lists all snapshots taken. If volname is provided, then only the snapshots belonging to that particular volume is listed.</p>
<dt><code>&nbsp;<wbr>snapshot info [snapname | (volume &lt;volname&gt;)] </code></p>
<dd>This command gives information such as snapshot name, snapshot UUID, time at which snapshot was created, and it lists down the snap-volume-name, number of snapshots already taken and number of snapshots still available for that particular volume, and the state of the snapshot. If snapname is specified then info of the mentioned snapshot is displayed. If volname is specified then info of all snapshots belonging to that volume is displayed. If both snapname and volname is not specified then info of all the snapshots present in the system are displayed.</p>
<dt><code>&nbsp;<wbr>snapshot status [snapname | (volume &lt;volname&gt;)] </code></p>
<dd>This command gives status of the snapshot. The details included are snapshot brick path, volume group(LVM details), status of the snapshot bricks, PID of the bricks, data percentage filled for that particular volume group to which the snapshots belong to, and total size of the logical volume. </p>
<p> If snapname is specified then status of the mentioned snapshot is displayed. If volname is specified then status of all snapshots belonging to that volume is displayed. If both snapname and volname is not specified then status of all the snapshots present in the system are displayed.</p>
<dt><code>&nbsp;<wbr>snapshot config [volname] ([snap-max-hard-limit &lt;count&gt;] [snap-max-soft-limit &lt;percent&gt;]) | ([auto-delete &lt;enable|disable&gt;]) | ([activate-on-create &lt;enable|disable&gt;])</p>
<dd>Displays and sets the snapshot config values. </p>
<p> snapshot config without any keywords displays the snapshot config values of all volumes in the system. If volname is provided, then the snapshot config values of that volume is displayed. </p>
<p> Snapshot config command along with keywords can be used to change the existing config values. If volname is provided then config value of that volume is changed, else it will set/change the system limit. </p>
<p> snap-max-soft-limit and auto-delete are global options, that will be inherited by all volumes in the system and cannot be set to individual volumes. </p>
<p> snap-max-hard-limit can be set globally, as well as per volume. The lowest limit between the global system limit and the volume specific limit, becomes the &quot;Effective snap-max-hard-limit&quot; for a volume. </p>
<p> snap-max-soft-limit is a percentage value, which is applied on the &quot;Effective snap-max-hard-limit&quot; to get the &quot;Effective snap-max-soft-limit&quot;. </p>
<p> When auto-delete feature is enabled, then upon reaching the &quot;Effective snap-max-soft-limit&quot;, with every successful snapshot creation, the oldest snapshot will be deleted. </p>
<p> When auto-delete feature is disabled, then upon reaching the &quot;Effective snap-max-soft-limit&quot;, the user gets a warning with every successful snapshot creation. </p>
<p> When auto-delete feature is disabled, then upon reaching the &quot;Effective snap-max-hard-limit&quot;, further snapshot creations will not be allowed. </p>
<p> activate-on-create is disabled by default. If you enable activate-on-create, then further snapshot will be activated during the time of snapshot creation.</p>
<dt>&nbsp;<wbr>snapshot activate &lt;snapname&gt; </code></p>
<dd>Activates the mentioned snapshot. </p>
<p> Note : By default the snapshot is activated during snapshot creation.</p>
<dt><code>&nbsp;<wbr>snapshot deactivate &lt;snapname&gt; </code></p>
<dd>Deactivates the mentioned snapshot.</p>
<dt><code>&nbsp;<wbr>snapshot help </code></p>
<dd>Display help for the snapshot commands.</dl>
<h3>Self-heal Commands</h3>
<dl>
<dt><code>&nbsp;<wbr>volume heal &lt;VOLNAME&gt;</code></p>
<dd>Triggers index self heal for the files that need healing. </p>
<dt><code>&nbsp;<wbr>volume heal &lt;VOLNAME&gt; [enable | disable]</code></p>
<dd>Enable/disable self-heal-daemon for volume &lt;VOLNAME&gt;. </p>
<dt><code>&nbsp;<wbr>volume heal &lt;VOLNAME&gt; full</code></p>
<dd>Triggers self heal on all the files. </p>
<dt><code>&nbsp;<wbr>volume heal &lt;VOLNAME&gt; info </code></p>
<dd>Lists the files that need healing. </p>
<dt><code>&nbsp;<wbr>volume heal &lt;VOLNAME&gt; info split-brain </code></p>
<dd>Lists the files which are in split-brain state. </p>
<dt><code>&nbsp;<wbr>volume heal &lt;VOLNAME&gt; statistics </code></p>
<dd>Lists the crawl statistics. </p>
<dt><code>&nbsp;<wbr>volume heal &lt;VOLNAME&gt; statistics heal-count </code></p>
<dd>Displays the count of files to be healed. </p>
<dt><code>&nbsp;<wbr>volume heal &lt;VOLNAME&gt; statistics heal-count replica &lt;HOSTNAME:BRICKNAME&gt; </code></p>
<dd>Displays the number of files to be healed from a particular replica subvolume to which the brick &lt;HOSTNAME:BRICKNAME&gt; belongs. </p>
<dt><code>&nbsp;<wbr>volume heal &lt;VOLNAME&gt; split-brain bigger-file &lt;FILE&gt; </code></p>
<dd>Performs healing of &lt;FILE&gt; which is in split-brain by choosing the bigger file in the replica as source. </p>
<dt><code>&nbsp;<wbr>volume heal &lt;VOLNAME&gt; split-brain source-brick &lt;HOSTNAME:BRICKNAME&gt; </code></p>
<dd>Selects &lt;HOSTNAME:BRICKNAME&gt; as the source for all the files that are in split-brain in that replica and heals them. </p>
<dt><code>&nbsp;<wbr>volume heal &lt;VOLNAME&gt; split-brain source-brick &lt;HOSTNAME:BRICKNAME&gt; &lt;FILE&gt; </code></p>
<dd>Selects the split-brained &lt;FILE&gt; present in &lt;HOSTNAME:BRICKNAME&gt; as source and completes heal.</dl>
<h3>Other Commands</h3>
<dl>
<dt><code>&nbsp;<wbr>get-state [&lt;daemon&gt;] [odir &lt;/path/to/output/dir/&gt;] [file &lt;filename&gt;] </code></p>
<dd>Get local state representation of mentioned daemon and store data in provided path information</p>
<dt><code>&nbsp;<wbr>help </code></p>
<dd>Display the command options.</p>
<dt><code>&nbsp;<wbr>quit </code></p>
<dd>Exit the gluster command line interface. </p>
</dl>
<h2>Files</h2>
<p>/var/lib/glusterd/*</p>
<h2>See Also</h2>
<pre><code><a href="//www.systutorials.com/docs/linux/man/1-fusermount/">fusermount</a></code>(1), <code><a href="//www.systutorials.com/docs/linux/man/8-mount.glusterfs/">mount.glusterfs</a></code>(8), <code><a href="//www.systutorials.com/docs/linux/man/8-glusterfs/">glusterfs</a></code>(8), <code><a href="//www.systutorials.com/docs/linux/man/8-glusterd/">glusterd</a></code>(8)</pre>
<h2>Copyright</h2>
<pre>Copyright(c) 2006-2011 Gluster, Inc. &lt;<a rel="nofollow" href="http://www.gluster.com">http://www.gluster.com</a>&gt;</pre>
