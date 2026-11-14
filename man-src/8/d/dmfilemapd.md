---
title: "dmfilemapd(8)"
name: "dmfilemapd"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dmfilemapd/"
description: "dmfilemapd — device-mapper filemap monitoring daemon"
---

<p>dmfilemapd &#8212; device-mapper filemap monitoring daemon</p>
<h2>Synopsis</h2>
<p><i>dmfilemapd</i> [<code>file_descriptor</code>] [<code>group_id</code>] [<code>abs_path</code>] [<code>mode</code>] [<code>foreground</code>[<code>verbose</code>]<code>]</code></p>
<h2>Description</h2>
<p>The dmfilemapd daemon monitors groups of <i>dmstats</i> regions that correspond to the extents of a file, adding and removing regions to reflect the changing state of the file on-disk. </p>
<p> The daemon is normally launched automatically by the dmstats create command, but can be run manually, either to create a new daemon where one did not previously exist, or to change the options previously used, by killing the existing daemon and starting a new one.</p>
<h2>Options</h2>
<dl>
<dt> <code>file_descriptor</code></p>
<dd>
<dd>Specify the file descriptor number for the file to be monitored. The file descriptor must reference a regular file, open for reading, in a local file system that supports the FIEMAP ioctl, and that returns data describing the physical location of extents. </p>
<p> The process that executes <code>dmfilemapd</code> is responsible for opening the file descriptor that is handed to the daemon.</p>
<dt> <code>group_id</code></p>
<dd>
<dd>The <code>dmstats</code> group identifier of the group that <code>dmfilemapd</code> should update. The group must exist and it should correspond to a set of regions created by a previous filemap operation.</p>
<dt> <code>abs_path</code></p>
<dd>
<dd>The absolute path to the file being monitored, at the time that it was opened. The use of <code>path</code> by the daemon differs, depending on the filemap following mode in use; see <code>MODES</code> and the <code>mode</code> option for more information. </p>
<dt> <code>mode</code></p>
<dd>
<dd>The filemap monitoring mode the daemon should use: either &quot;inode&quot; (<code>DM_FILEMAP_FOLLOW_INODE</code>), or &quot;path&quot; (<code>DM_FILEMAP_FOLLOW_PATH</code>), to enable follow-inode or follow-path mode respectively.</p>
<dt> <code>[foreground]</code></p>
<dd>
<dd>If set to 1, disable forking and allow the daemon to run in the foreground.</p>
<dt> <code>[verbose]</code></p>
<dd>Control daemon logging. If set to zero, the daemon will close all stdio streams and run silently. If <code>verbose</code> is a number between 1 and 3, stdio will be retained and the daemon will log messages to stdout and stderr that match the specified verbosity level.</dl>
<h2>Modes</h2>
<p>The file map monitoring daemon can monitor files in two distinct ways: the mode affects the behaviour of the daemon when a file under monitoring is renamed or unlinked, and the conditions which cause the daemon to terminate. </p>
<p> In both modes, the daemon will always shut down when the group being monitored is deleted. </p>
<p> <code>Follow inode</code> </p>
<p> The daemon follows the inode of the file, as it was at the time the daemon started. The file descriptor referencing the file is kept open at all times, and the daemon will exit when it detects that the file has been unlinked and it is the last holder of a reference to the file. </p>
<p> This mode is useful if the file is expected to be renamed, or moved within the file system, while it is being monitored. </p>
<p> <code>Follow path</code> </p>
<p> The daemon follows the path that was given on the daemon command line. The file descriptor referencing the file is re-opened on each iteration of the daemon, and the daemon will exit if no file exists at this location (a tolerance is allowed so that a brief delay between removal and replacement is permitted). </p>
<p> This mode is useful if the file is updated by unlinking the original and placing a new file at the same path.</p>
<h2>Limitations</h2>
<p>The daemon attempts to maintain good synchronisation between the file extents and the regions contained in the group, however, since the daemon can only react to new allocations once they have been written, there are inevitably some IO events that cannot be counted when a file is growing, particularly if the file is being extended by a single thread writing beyond EOF (for example, the <code>dd</code> program). </p>
<p> There is a further loss of events in that there is currently no way to atomically resize a <code>dmstats</code> region and preserve its current counter values. This affects files when they grow by extending the final extent, rather than allocating a new extent: any events that had accumulated in the region between any prior operation and the resize are lost. </p>
<p> File mapping is currently most effective in cases where the majority of IO does not trigger extent allocation. Future updates may address these limitations when kernel support is available.</p>
<h2>Examples</h2>
<p>Normally the daemon is started automatically by the <code>dmstats</code> <code>create</code> or <code>update_filemap</code> commands but it can be run manually for debugging or testing purposes. Start the daemon in the background, in follow-path mode<br />
 # <code>dmfilemapd 3 0 /srv/images/vm.img path 0 0 3&lt; /srv/images/vm.img</code><br />
 Start the daemon in follow-inode mode, disable forking and enable verbose logging<br />
 # <code>dmfilemapd 3 0 /var/tmp/data inode 1 3 3&lt; /var/tmp/data</code><br />
 Starting dmfilemapd with fd=3, group_id=0 mode=inode, path=/var/tmp/data<br />
 dm version [ opencount flush ] [16384] (*1)<br />
 dm info (253:0) [ opencount flush ] [16384] (*1)<br />
 dm message (253:0) [ opencount flush ] @stats_list dmstats [16384] (*1)<br />
 Read alias &#8216;data&#8217; from aux_data<br />
 Found group_id 0: alias=&quot;data&quot;<br />
 dm_stats_walk_init: initialised flags to 4000000000000<br />
 starting stats walk with GROUP<br />
 exiting _filemap_monitor_get_events() with deleted=0, check=0<br />
 Waiting for check interval </p>
<h2>Authors</h2>
<p>Bryn M. Reeves &lt;bmr [at] redhat.com&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-dmstats/">dmstats</a></code>(8) LVM2 resource page: <a rel="nofollow" href="https://www.sourceware.org/lvm2/">https://www.sourceware.org/lvm2/</a><br />
 Device-mapper resource page: <a rel="nofollow" href="http://sources.redhat.com/dm/">http://sources.redhat.com/dm/</a> </p>
