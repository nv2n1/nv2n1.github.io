---
title: "glocktop(8)"
name: "glocktop"
section: "8"
letter: "g"
url: "/docs/linux/man/8-glocktop/"
description: "glocktop – Display or print active GFS2 locks."
---

<p>glocktop &#8211; Display or print active GFS2 locks.</p>
<h2>Synopsis</h2>
<p><code>glocktop</code> [<i>OPTIONS</i>] </p>
<h2>Description</h2>
<p>The glocktop tool is used to display active GFS2 inter-node locks, also known as glocks. Simply put, it&#8217;s a tool to filter and interpret the contents of the glocks debugfs file. The glocks debugfs file shows all glocks known to GFS2, their holders, and technical data such as flags. The glocktop tool will only show the glocks that are important: glocks that are being held or for which there are waiters. It also interprets the debugfs file of DLM (Distributed Lock Manager). </p>
<h2>Options</h2>
<dl>
<dt><code>-d</code> <i>&lt;delay&gt;</i></p>
<dd>Specify a time delay (in seconds) between reports. (Default is 30 seconds)</p>
<dt><code>-h</code></p>
<dd>Print help information.</p>
<dt><code>-i</code></p>
<dd>Interactive mode. In this mode, glocktop acts more like the top command. It shows the pertinent glocks on the terminal session (as many as it can fit). The advantage is that it uses different colors to draw attention to what&#8217;s important. The disadvantage is that it&#8217;s limited by the size of your display, so you may not see all the glocks.</p>
<dt><code>-D</code></p>
<dd>Omit DLM status. This may be used to reduce the amount of output for interactive mode.</p>
<dt><code>-n</code> <i>&lt;iterations&gt;</i></p>
<dd>End the program after the specified number of iterations (reports). The default is to keep running until interrupted.</p>
<dt><code>-r</code></p>
<dd>Show resource group reservation information. Normally, glocktop omits resource group reservation information to condense the output. This information is only important when debugging information related to the GFS2 block allocator and file system fragmentation.</p>
<dt><code>-s</code> <i>&lt;freq&gt;</i></p>
<dd>Print glock summary information every <i>&lt;freq&gt;</i> reports. The glock summary information is bulky and often not needed, so it&#8217;s only printed once every 10 reports. You can eliminate it entirely from the output by specifying a value of 0. If you want the statistics to print after every report, specify freq as 1.</p>
<dt><code>-t</code></p>
<dd>Trace directory path. A lot of GFS2 glock performance problems are caused by an application&#8217;s contention for one or two directories. These show up as regular inodes in the output, but there&#8217;s no good way to tell from the output which directory is contended. Ordinarily, glocktop won&#8217;t try to look up the full pathname of a contended directory because it&#8217;s slow, especially if there are millions of glocks. This option instructs glocktop to try to determine the full directory path names when it can, so you can tell the full path (within the mount point) of contended directories.</p>
<dt><code>-H</code></p>
<dd>Don&#8217;t show Held glocks, unless there are also waiters for the lock. Ordinarily, glocktop will show glocks that are held (but not iopen glocks which are almost always held by the thousands) as well as glocks for which there are waiters. If it only showed glocks with waiters, you could see, for example, that a glock is being blocked on one node, but you couldn&#8217;t see the information for a different node currently holding the lock and thus, blocking the waiter. This option forces glocktop to stop printing information for glocks with no waiters (on that node). The advantage is that the output is smaller and easier to look at. The disadvantage is that you can&#8217;t see information from the node that&#8217;s blocking the waiter, unless both waiter and holder are on the same node.</dl>
<h2>Output Lines</h2>
<dl>
<dt><code>@ name</code></p>
<dd>This is the GFS2 file system name for which the information is printed. It also gives the time stamp of the report, and the cluster node name.</p>
<dt><code>G:</code></p>
<dd>This line represents a glock (internode GFS2 lock).<br />
&nbsp;<wbr>G:&nbsp;<wbr>&nbsp;<wbr>s:UN n:2/609b4 f:lIqob t:EX d:EX/0 a:0 v:0 r:3 m:200&nbsp;<wbr>(inode)</p>
<dt><code>D:</code></p>
<dd>This line gives you glocktop&#8217;s interpretation of the glock&#8217;s state as far as DLM (distributed lock manager) is concerned.<br />
&nbsp;<wbr>&nbsp;<wbr>D: Granted PR on node 2 to pid 17511&nbsp;<wbr>[python]</p>
<dt><code>H:</code></p>
<dd>This line represents a glock holder: a process that&#8217;s either holding the glock, or is waiting to hold it. The value after S: represents how this holder needs the lock: EX (Exclusive), SH (Shared), PR (Protected Read), or UN (Unlocked). The value after F: indicates the holder flags: a W indicates the holder is Waiting for the lock to be granted. An H indicates the holder is currently holding the lock.<br />
&nbsp;<wbr>&nbsp;<wbr>H: s:EX f:W e:0 p:17511&nbsp;<wbr>[python]&nbsp;<wbr>gfs2_unlink+0x7e/0x250&nbsp;<wbr>[gfs2]</p>
<dt><code>U:</code></p>
<dd>These lines represent glocktop&#8217;s user interpretation of the data, both glock and holder. Lines that begin with (N/A:&#8230;) can probably be ignored because they ought to be unimportant: system files such as journals, etc.<br />
&nbsp;<wbr>&nbsp;<wbr>U:&nbsp;<wbr>&nbsp;<wbr>W inode&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>183f5&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Is:Shared, Want:Exclusive&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[Demote pending, Reply pending, Queued, Blocking]<br />
&nbsp;<wbr>&nbsp;<wbr>U:&nbsp;<wbr>&nbsp;<wbr>W&nbsp;<wbr>&nbsp;<wbr>&#8212;&gt;&nbsp;<wbr>&nbsp;<wbr>waiting pid 17511&nbsp;<wbr>[python]&nbsp;<wbr>&nbsp;<wbr>(Granted PR on node 2 to pid 17511&nbsp;<wbr>[python])</p>
<dt><code>C:</code></p>
<dd>These lines give you the call trace (call stack) of the process that&#8217;s either holding or waiting to hold the glock.</p>
<dt><code>S</code></p>
<dd>These lines give you the summary of all glocks for this file system: How many of each category are unlocked, locked, how many are held in EX, SH, and DF, and how many are waiting. G Waiting is how many glocks have waiters. P Waiting is how many processes are waiting. Thus, you could have one glock that&#8217;s got ten processes waiting, or ten glocks that have ten processes waiting.</dl>
<h2>Example Output</h2>
<pre><dl><dt><dd># glocktop
@ nate_bob1 Wed Jan 27 07:24:14 2016 @host-050
 G: s:EX n:9/1 f:Iqb t:EX d:EX/0 a:0 v:0 r:2 m:200 (journal)
 D: Granted EX on node 2 to pid 17468 [ended]
 H: s:EX f:eH e:0 p:17468 [(ended)] gfs2_glock_nq_num+0x5b/0xa0 [gfs2]
 U: (N/A:Journl) H journal 1 Held:Exclusive [Queued, Blocking]
 U: (N/A:Journl) H ---&gt; held by pid 17468 [(ended)] (Granted EX on node 2 to pid 17468 [ended])
 G: s:SH n:1/1 f:Iqb t:SH d:EX/0 a:0 v:0 r:2 m:200 (non-disk)
 D: Granted PR on node 2 to pid 17468 [ended]
 H: s:SH f:eEH e:0 p:17468 [(ended)] gfs2_glock_nq_num+0x5b/0xa0 [gfs2]
 U: (N/A:Not EX) H non-disk 1 Held:Shared [Queued, Blocking]
 U: (N/A:Not EX) H ---&gt; held by pid 17468 [(ended)] (Granted PR on node 2 to pid 17468 [ended])
 G: s:EX n:2/181ec f:yIqob t:EX d:EX/0 a:1 v:0 r:3 m:200 (inode)
 D: Granted EX on this node to pid 17468 [ended]
 H: s:EX f:H e:0 p:17468 [(ended)] init_per_node+0x17d/0x280 [gfs2]
 I: n:12/98796 t:8 f:0x00 d:0x00000201 s:24
 U: (N/A:System) H inode 181ec Held:Exclusive [Dirty, Queued, Blocking]
 U: (N/A:System) H ---&gt; held by pid 17468 [(ended)] (Granted EX on this node to pid 17468 [ended])
 G: s:EX n:2/181ed f:Iqob t:EX d:EX/0 a:0 v:0 r:3 m:200 (inode)
 D: Granted EX on this node to pid 17468 [ended]
 H: s:EX f:H e:0 p:17468 [(ended)] init_per_node+0x1b0/0x280 [gfs2]
 I: n:13/98797 t:8 f:0x00 d:0x00000200 s:1048576
 U: (N/A:System) H inode 181ed Held:Exclusive [Queued, Blocking]
 U: (N/A:System) H ---&gt; held by pid 17468 [(ended)] (Granted EX on this node to pid 17468 [ended])
 G: s:SH n:2/183f5 f:ldrIqob t:EX d:UN/0 a:0 v:0 r:5 m:10 (inode)
 D: Granted PR on node 2 to pid 17511 [python]
 H: s:EX f:W e:0 p:17511 [python] gfs2_unlink+0x7e/0x250 [gfs2]
 I: n:1/99317 t:4 f:0x00 d:0x00000003 s:2048
 U: W inode 183f5 Is:Shared, Want:Exclusive [Demote pending, Reply pending, Queued, Blocking]
 U: W ---&gt; waiting pid 17511 [python] (Granted PR on node 2 to pid 17511 [python])
 C: gfs2_unlink+0xdc/0x250 [gfs2]
 C: vfs_unlink+0xa0/0xf0
 C: do_unlinkat+0x163/0x260
 C: sys_unlink+0x16/0x20
 G: s:SH n:2/805b f:Iqob t:SH d:EX/0 a:0 v:0 r:3 m:200 (inode)
 D: Granted PR on node 2 to pid 17468 [ended]
 H: s:SH f:eEcH e:0 p:17468 [(ended)] init_journal+0x185/0x500 [gfs2]
 I: n:5/32859 t:8 f:0x01 d:0x00000200 s:134217728
 U: (N/A:Not EX) H inode 805b Held:Shared [Queued, Blocking]
 U: (N/A:Not EX) H ---&gt; held by pid 17468 [(ended)] (Granted PR on node 2 to pid 17468 [ended])
S glocks nondisk inode rgrp iopen flock quota jrnl Total
S --------- ------- -------- ------- ------- ------- ----- ---- --------
S Unlocked: 1 5 4 0 0 0 0 10
S Locked: 2 245 6 58 0 0 1 313
S Total: 3 250 10 58 0 0 1 323
S
S Held EX: 0 2 0 0 0 0 1 3
S Held SH: 1 1 0 57 0 0 0 59
S Held DF: 0 0 0 0 0 0 0 0
S G Waiting: 0 1 0 0 0 0 0 1
S P Waiting: 0 1 0 0 0 0 0 1
S DLM wait: 0
@ nate_bob0 Wed Jan 27 07:24:14 2016 @host-050
 G: s:EX n:2/180e9 f:yIqob t:EX d:EX/0 a:1 v:0 r:3 m:200 (inode)
 D: Granted EX on this node to pid 17465 [ended]
 H: s:EX f:H e:0 p:17465 [(ended)] init_per_node+0x17d/0x280 [gfs2]
 I: n:9/98537 t:8 f:0x00 d:0x00000201 s:24
 U: (N/A:System) H inode 180e9 Held:Exclusive [Dirty, Queued, Blocking]
 U: (N/A:System) H ---&gt; held by pid 17465 [(ended)] (Granted EX on this node to pid 17465 [ended])
 G: s:UN n:2/609b4 f:lIqob t:EX d:EX/0 a:0 v:0 r:3 m:200 (inode)
 D: Granted EX on node 2 to pid 14367 [ended]
 H: s:EX f:W e:0 p:16297 [delete_workqueu] gfs2_delete_inode+0x9d/0x450 [gfs2]
 U: W inode 609b4 Is:Unlocked, Want:Exclusive [Queued, Blocking]
 U: W ---&gt; waiting pid 16297 [delete_workqueu] (Granted EX on node 2 to pid 14367 [ended])
 C: gfs2_delete_inode+0xa5/0x450 [gfs2]
 C: generic_delete_inode+0xde/0x1d0
 C: generic_drop_inode+0x65/0x80
 C: gfs2_drop_inode+0x37/0x40 [gfs2]
 G: s:SH n:2/19 f:Iqob t:SH d:EX/0 a:0 v:0 r:3 m:200 (inode)
 D: Granted PR on this node to pid 17465 [ended]
 H: s:SH f:eEcH e:0 p:17465 [(ended)] init_journal+0x185/0x500 [gfs2]
 I: n:4/25 t:8 f:0x01 d:0x00000200 s:134217728
 U: (N/A:Not EX) H inode 19 Held:Shared [Queued, Blocking]
 U: (N/A:Not EX) H ---&gt; held by pid 17465 [(ended)] (Granted PR on this node to pid 17465 [ended])
 G: s:EX n:2/180ea f:Iqob t:EX d:EX/0 a:0 v:0 r:3 m:200 (inode)
 D: Granted EX on this node to pid 17465 [ended]
 H: s:EX f:H e:0 p:17465 [(ended)] init_per_node+0x1b0/0x280 [gfs2]
 I: n:10/98538 t:8 f:0x00 d:0x00000200 s:1048576
 U: (N/A:System) H inode 180ea Held:Exclusive [Queued, Blocking]
 U: (N/A:System) H ---&gt; held by pid 17465 [(ended)] (Granted EX on this node to pid 17465 [ended])
 G: s:EX n:9/0 f:Iqb t:EX d:EX/0 a:0 v:0 r:2 m:200 (journal)
 D: Granted EX on this node to pid 17465 [ended]
 H: s:EX f:eH e:0 p:17465 [(ended)] gfs2_glock_nq_num+0x5b/0xa0 [gfs2]
 U: (N/A:Journl) H journal 0 Held:Exclusive [Queued, Blocking]
 U: (N/A:Journl) H ---&gt; held by pid 17465 [(ended)] (Granted EX on this node to pid 17465 [ended])
 G: s:UN n:2/4fe12 f:ldIqob t:EX d:UN/0 a:0 v:0 r:4 m:10 (inode)
 H: s:EX f:W e:0 p:17523 [python] gfs2_rename+0x344/0x8b0 [gfs2]
 H: s:SH f:AW e:0 p:17527 [python] gfs2_permission+0x176/0x210 [gfs2]
 U: W inode 4fe12 Is:Unlocked, Want:Exclusive [Demote pending, Queued, Blocking]
 U: W ---&gt; waiting pid 17523 [python]
 C: gfs2_permission+0x17f/0x210 [gfs2]
 C: __link_path_walk+0xb3/0x1000
 C: path_walk+0x6a/0xe0
 C: filename_lookup+0x6b/0xc0
 U: W ---&gt; waiting pid 17527 [python]
 C: do_unlinkat+0x107/0x260
 C: sys_unlink+0x16/0x20
 C: system_call_fastpath+0x16/0x1b
 C: 0xffffffffffffffff
 G: s:SH n:1/1 f:Iqb t:SH d:EX/0 a:0 v:0 r:2 m:200 (non-disk)
 D: Granted PR on node 2 to pid 14285 [ended]
 D: Granted PR on this node to pid 17465 [ended]
 H: s:SH f:eEH e:0 p:17465 [(ended)] gfs2_glock_nq_num+0x5b/0xa0 [gfs2]
 U: (N/A:Not EX) H non-disk 1 Held:Shared [Queued, Blocking]
 U: (N/A:Not EX) H ---&gt; held by pid 17465 [(ended)] (Granted PR on node 2 to pid 14285 [ended]) (Granted PR on this node to pid 17465 [ended])
S glocks nondisk inode rgrp iopen flock quota jrnl Total
S --------- ------- -------- ------- ------- ------- ----- ---- --------
S Unlocked: 1 8 7 0 0 0 0 16
S Locked: 2 208 3 41 0 0 1 256
S Total: 3 216 10 41 0 0 1 272
S
S Held EX: 0 2 0 0 0 0 1 3
S Held SH: 1 1 0 41 0 0 0 43
S Held DF: 0 0 0 0 0 0 0 0
S G Waiting: 0 2 0 0 0 0 0 2
S P Waiting: 0 3 0 0 0 0 0 3
S DLM wait: 0
</dl></pre>
<p>From this example output, we can see there are two GFS2 file systems mounted on system host-050: nate_bob1 and nate_bob0. In nate_bob1, we can see six glocks, but we can ignore all of them marked (N/A:&#8230;) because they are system files or held in SHared mode, and therefore other nodes should be able to hold the lock in SHared as well. </p>
<p> There is one glock, for inode 183f5, which is has a process waiting to hold it. The lock is currently in SHared mode (s:SH on the G: line) but process 17511 (python) wants to hold the lock in EXclusive mode (S:EX on the H: line). That process has a call stack that indicates it is trying to hold the glock from gfs2_unlink. The DLM says the lock is currently granted on node 2 in PR (Protected Read) mode. </p>
<p> For file system nate_bob0, there are 7 glocks listed. All but two are uninteresting. Locks 2/609b4 and 2/4fe12 have processes waiting to hold them. </p>
<p> In the summary data for nate_bob0, you can see there are 3 processes waiting for 2 inode glocks (so one of those glocks has multiple processes waiting). </p>
<p> Since DLM wait is 0 in the summary data for both GFS2 mount points, nobody is waiting for DLM to grant the lock.</p>
<h2>Known Bugs And Limitations</h2>
<p>Since the GFS2 debugfs files are completely separate from the DLM debugfs files, and locks can change status in a few nanoseconds time, there will always be a lag between the GFS2 view of a lock and the DLM view of a lock. If there is some kind of long-term hang, they are more likely to match. However, under ordinary conditions, by the time glocktop gets around to fetching the DLM status of a lock, the information has changed. Therefore, don&#8217;t be surprised if the DLM&#8217;s view of a lock is at odds with its glock. </p>
<p> Since iopen glocks are held by the thousands, glocktop skips most of the information related to them unless there&#8217;s a waiter. For that reason, iopen lock problems may be difficult to debug with glocktop. </p>
<p> It doesn&#8217;t handle very large numbers (millions) of glocks.</p>
