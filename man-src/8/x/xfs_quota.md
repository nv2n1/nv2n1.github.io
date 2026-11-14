---
title: "xfs_quota(8)"
name: "xfs_quota"
section: "8"
letter: "x"
url: "/docs/linux/man/8-xfs_quota/"
description: "xfs_quota – manage use of quota on XFS filesystems"
---

<p>xfs_quota &#8211; manage use of quota on XFS filesystems</p>
<h2>Synopsis</h2>
<p><code>xfs_quota</code> [ <code>-x</code> ] [ <code>-f</code> ] [ <code>-p</code> <i>prog</i> ] [ <code>-c</code> <i>cmd</i> ] &#8230; [ <code>-d</code> <i>project</i> ] &#8230; [ <code>-D</code> <i>projects_file</i> ] [ <code>-P</code> <i>projid_file</i> ] [ <i>path</i> &#8230; ]<br />
 <code>xfs_quota -V</code></p>
<h2>Description</h2>
<p><code>xfs_quota</code> is a utility for reporting and editing various aspects of filesystem quota. </p>
<p> The options to <code>xfs_quota</code> are:</p>
<dl>
<dt><code>-c</code><i> cmd</i></p>
<dd><code>xfs_quota</code> commands may be run interactively (the default) or as arguments on the command line. Multiple <code>-c</code> arguments may be given. The commands are run in the sequence given, then the program exits.</p>
<dt><code>-p</code><i> prog</i></p>
<dd>Set the program name for prompts and some error messages, the default value is <code>xfs_quota</code>.</p>
<dt><code>-x</code></p>
<dd>Enable expert mode. All of the administrative commands (see the ADMINISTRATOR COMMANDS section below) which allow modifications to the quota system are available only in expert mode.</p>
<dt><code>-f</code></p>
<dd>Enable foreign filesystem mode. A limited number of user and administrative commands are available for use on some foreign (non-XFS) filesystems.</p>
<dt><code>-d</code><i> project</i></p>
<dd>Project names or numeric identifiers may be specified with this option, which restricts the output of the individual <code>xfs_quota</code> commands to the set of projects specified. Multiple <code>-d</code> arguments may be given.</p>
<dt><code>-D</code><i> projects_file</i></p>
<dd>Specify a file containing the mapping of numeric project identifiers to directory trees. <i>/etc/projects</i> as default, if this option is none.</p>
<dt><code>-P</code><i> projid_file</i></p>
<dd>Specify a file containing the mapping of numeric project identifiers to project names. <i>/etc/projid</i> as default, if this option is none.</p>
<dt><code>-V</code></p>
<dd>Prints the version number and exits.</dl>
<p> The optional <i>path</i> argument(s) can be used to specify mount points or device files which identify XFS filesystems. The output of the individual <code>xfs_quota</code> commands will then be restricted to the set of filesystems specified. </p>
<p> This manual page is divided into two sections &#8211; firstly, information for users of filesystems with quota enabled, and the <code>xfs_quota</code> commands of interest to such users; and then information which is useful only to administrators of XFS filesystems using quota and the quota commands which allow modifications to the quota system. </p>
<p> Note that common to almost all of the individual commands described below are the options for specifying which quota types are of interest &#8211; user quota (<code>-u</code>), group quota (<code>-g</code>), and/or project quota (<code>-p</code>). Also, several commands provide options to operate on &quot;blocks used&quot; (<code>-b</code>), &quot;inodes used&quot; (<code>-i</code>), and/or &quot;realtime blocks used&quot; (<code>-r</code>). </p>
<p> Many commands also have extensive online help. Use the <code>help</code> command for more details on any command.</p>
<h2>Quota Overview</h2>
<p>In most computing environments, disk space is not infinite. The quota subsystem provides a mechanism to control usage of disk space. Quotas can be set for each individual user on any/all of the local filesystems. The quota subsystem warns users when they exceed their allotted limit, but allows some extra space for current work (hard limit/soft limit). In addition, XFS filesystems with limit enforcement turned off can be used as an effective disk usage accounting system.</p>
<h3>Users&#8217; View of Disk Quotas</h3>
<p>To most users, disk quotas are either of no concern or a fact of life that cannot be avoided. There are two possible quotas that can be imposed &#8211; a limit can be set on the amount of space a user can occupy, and there may be a limit on the number of files (inodes) he can own. </p>
<p> The <code>quota</code> command provides information on the quotas that have been set by the system administrators and current usage. </p>
<p> There are four numbers for each limit: current usage, soft limit (quota), hard limit, and time limit. The soft limit is the number of 1K-blocks (or files) that the user is expected to remain below. The hard limit cannot be exceeded. If a user&#8217;s usage reaches the hard limit, further requests for space (or attempts to create a file) fail with the &quot;Quota exceeded&quot; (EDQUOT) error. </p>
<p> When a user exceeds the soft limit, the timer is enabled. Any time the quota drops below the soft limits, the timer is disabled. If the timer pops, the particular limit that has been exceeded is treated as if the hard limit has been reached, and no more resources are allocated to the user. The only way to reset this condition, short of turning off limit enforcement or increasing the limit, is to reduce usage below quota. Only the superuser (i.e. a sufficiently capable process) can set the time limits and this is done on a per filesystem basis.</p>
<h3>Surviving When the Quota Limit Is Reached</h3>
<p>In most cases, the only way for a user to recover from over-quota conditions is to abort whatever activity is in progress on the filesystem that has reached its limit, remove sufficient files to bring the limit back below quota, and retry the failed program.<br />
 However, if a user is in the editor and a write fails because of an over quota situation, that is not a suitable course of action. It is most likely that initially attempting to write the file has truncated its previous contents, so if the editor is aborted without correctly writing the file, not only are the recent changes lost, but possibly much, or even all, of the contents that previously existed.<br />
 There are several possible safe exits for a user caught in this situation. He can use the editor shell escape command to examine his file space and remove surplus files. Alternatively, using <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1), he can suspend the editor, remove some files, then resume it. A third possibility is to write the file to some other filesystem (perhaps to a file on <i>/tmp</i>) where the user&#8217;s quota has not been exceeded. Then after rectifying the quota situation, the file can be moved back to the filesystem it belongs on.</p>
<h2>User Commands</h2>
<dl>
<dt><code>print</code></p>
<dd>Lists all paths with devices/project identifiers. The path list can come from several places &#8211; the command line, the mount table, and the <i>/etc/projects</i> file.</p>
<dt><code>df</code></p>
<dd>See the <code>free</code> command.</p>
<dt> <code>quota</code> [ <code>-g</code> | <code>-p</code> | <code>-u</code> ] [ <code>-bir</code> ] [ <code>-hnNv</code> ] [ <code>-f</code> <i>file</i> ] [ <i>ID</i> | <i>name</i> ] &#8230;</p>
<dd>
<dd>Show individual usage and limits, for a single user <i>name</i> or numeric user <i>ID</i>. The <code>-h</code> option reports in a &quot;human-readable&quot; format similar to the <code><a href="/docs/linux/man/1-df/">df</a></code>(1) command. The <code>-n</code> option reports the numeric IDs rather than the name. The <code>-N</code> option omits the header. The <code>-v</code> option outputs verbose information. The <code>-f</code> option sends the output to <i>file</i> instead of stdout.</p>
<dt> <code></p>
<dd>free</code> [ <code>-bir</code> ] [ <code>-hN</code> ] [ <code>-f</code> <i>file</i> ]<br />
 Reports filesystem usage, much like the <code><a href="/docs/linux/man/1-df/">df</a></code>(1) utility. It can show usage for <code>b</code>locks, <code>i</code>node, and/or <code>r</code>ealtime block space, and shows used, free, and total available. If project quota are in use (see the DIRECTORY TREE QUOTA section below), it will also report utilisation for those projects (directory trees). The <code>-h</code> option reports in a &quot;human-readable&quot; format. The <code>-N</code> option omits the header. The <code>-f</code> option outputs the report to <i>file</i> instead of stdout.</p>
<dt> <code>help</code> [ <i>command</i> ]</p>
<dd>
<dd>Online help for all commands, or one specific <i>command</i>.</p>
<dt><code>quit</code></p>
<dd>Exit <code>xfs_quota</code>.</p>
<dt><code>q</code></p>
<dd>See the <code>quit</code> command.</dl>
<h2>Quota Administration</h2>
<p>The XFS quota system differs to that of other filesystems in a number of ways. Most importantly, XFS considers quota information as filesystem metadata and uses journaling to provide a higher level guarantee of consistency. As such, it is administered differently, in particular:</p>
<dl>
<dt>1.</p>
<dd>The <code>quotacheck</code> command has no effect on XFS filesystems. The first time quota accounting is turned on (at mount time), XFS does an automatic quotacheck internally; afterwards, the quota system will always be completely consistent until quotas are manually turned off.</p>
<dt>2.</p>
<dd>There is no need for quota file(s) in the root of the XFS filesystem.</p>
<dt>3.</p>
<dd>XFS distinguishes between quota accounting and limit enforcement. Quota accounting must be turned on at the time of mounting the XFS filesystem. However, it is possible to turn on/off limit enforcement any time quota accounting is turned on. The &quot;quota&quot; option to the <code>mount</code> command turns on both (user) quota accounting and enforcement. The &quot;uqnoenforce&quot; option must be used to turn on user accounting with limit enforcement disabled.</p>
<dt>4.</p>
<dd>Turning on quotas on the root filesystem is slightly different from the above. For IRIX XFS, refer to <code><a href="//www.systutorials.com/docs/linux/man/1M-quotaon/">quotaon</a></code>(1M). For Linux XFS, the quota mount flags must be passed in with the &quot;rootflags=&quot; boot parameter.</p>
<dt>5.</p>
<dd>It is useful to use the <code>state</code> to monitor the XFS quota subsystem at various stages &#8211; it can be used to see if quotas are turned on, and also to monitor the space occupied by the quota system itself..</p>
<dt>6.</p>
<dd>There is a mechanism built into <code>xfsdump</code> that allows quota limit information to be backed up for later restoration, should the need arise.</p>
<dt>7.</p>
<dd>Quota limits cannot be set before turning on quotas on.</p>
<dt>8.</p>
<dd>XFS filesystems keep quota accounting on the superuser (user ID zero), and the tool will display the superuser&#8217;s usage information. However, limits are never enforced on the superuser (nor are they enforced for group and project ID zero).</p>
<dt>9.</p>
<dd>XFS filesystems perform quota accounting whether the user has quota limits or not.</p>
<dt>10.</p>
<dd>XFS supports the notion of project quota, which can be used to implement a form of directory tree quota (i.e. to restrict a directory tree to only being able to use up a component of the filesystems available space; or simply to keep track of the amount of space used, or number of inodes, within the tree).</dl>
<h2>Administrator Commands</h2>
<dl>
<dt> <code>path</code> [ <i>N</i> ]</p>
<dd>
<dd>Lists all paths with devices/project identifiers or set the current path to the <i>N</i>th list entry (the current path is used by many of the commands described here, it identifies the filesystem toward which a command is directed). The path list can come from several places &#8211; the command line, the mount table, and the <i>/etc/projects</i> file.</p>
<dt> <code>report</code> [ <code>-gpu</code> ] [ <code>-bir</code> ] [ <code>-ahntlLNU</code> ] [ <code>-f</code> <i>file</i> ]</p>
<dd>
<dd>Report filesystem quota information. This reports all quota usage for a filesystem, for the specified quota type (<code>u</code>/<code>g</code>/<code>p</code> and/or <code>b</code>locks/<code>i</code>nodes/<code>r</code>ealtime). It reports blocks in 1KB units by default. The <code>-h</code> option reports in a &quot;human-readable&quot; format similar to the <code><a href="/docs/linux/man/1-df/">df</a></code>(1) command. The <code>-f</code> option outputs the report to <i>file</i> instead of stdout. The <code>-a</code> option reports on all filesystems. By default, outputs the name of the user/group/project. If no name is defined for a given ID, outputs the numeric ID instead. The <code>-n</code> option outputs the numeric ID instead of the name. The <code>-L</code> and <code>-U</code> options specify lower and upper ID bounds to report on. If upper/lower bounds are specified, then by default only the IDs will be displayed in output; with the <code>-l</code> option, a lookup will be performed to translate these IDs to names. The <code>-N</code> option reports information without the header line. The <code>-t</code> option performs a terse report.</p>
<dt> <code></p>
<dd>state</code> [ <code>-gpu</code> ] [ <code>-av</code> ] [ <code>-f</code> <i>file</i> ]<br />
 Report overall quota state information. This reports on the state of quota accounting, quota enforcement, and the number of extents being used by quota metadata within the filesystem. The <code>-f</code> option outputs state information to <i>file</i> instead of stdout. The <code>-a</code> option reports state on all filesystems and not just the current path.</p>
<dt> <code></p>
<dd>limit</code> [ <code>-g</code> | <code>-p</code> | <code>-u</code> ] <code>bsoft=</code><i>N</i> | <code>bhard=</code><i>N</i> | <code>isoft=</code><i>N</i> | <code>ihard=</code><i>N</i> | <code>rtbsoft=</code><i>N</i> | <code>rtbhard=</code><i>N</i> <code>-d</code> | <i>id</i> | <i>name</i><br />
 Set quota block limits (bhard/bsoft), inode count limits (ihard/isoft) and/or realtime block limits (rtbhard/rtbsoft). The <code>-d</code> option (defaults) can be used to set the default value that will be used, otherwise a specific <code>u</code>ser/<code>g</code>roup/<code>p</code>roject <i>name</i> or numeric <i>id</i>entifier must be specified.</p>
<dt> <code>timer</code> [ <code>-g</code> | <code>-p</code> | <code>-u</code> ] [ <code>-bir</code> ] <i>value</i></p>
<dd>
<dd>Allows the quota enforcement timeout (i.e. the amount of time allowed to pass before the soft limits are enforced as the hard limits) to be modified. The current timeout setting can be displayed using the <code>state</code> command. The value argument is a number of seconds, but units of &#8216;minutes&#8217;, &#8216;hours&#8217;, &#8216;days&#8217;, and &#8216;weeks&#8217; are also understood (as are their abbreviations &#8216;m&#8217;, &#8216;h&#8217;, &#8216;d&#8217;, and &#8216;w&#8217;).</p>
<dt> <code>warn</code> [ <code>-g</code> | <code>-p</code> | <code>-u</code> ] [ <code>-bir</code> ] <i>value</i> <code>-d</code> | <i>id</i> | <i>name</i></p>
<dd>
<dd>Allows the quota warnings limit (i.e. the number of times a warning will be send to someone over quota) to be viewed and modified. The <code>-d</code> option (defaults) can be used to set the default time that will be used, otherwise a specific <code>u</code>ser/<code>g</code>roup/<code>p</code>roject <i>name</i> or numeric <i>id</i>entifier must be specified. <code>NOTE: this feature is not currently implemented.</code></p>
<dt><code>enable</code> [ <code>-gpu</code> ] [ <code>-v</code> ]</p>
<dd>Switches on quota enforcement for the filesystem identified by the current path. This requires the filesystem to have been mounted with quota enabled, and for accounting to be currently active. The <code>-v</code> option (verbose) displays the state after the operation has completed.</p>
<dt><code>disable</code> [ <code>-gpu</code> ] [ <code>-v</code> ]</p>
<dd>Disables quota enforcement, while leaving quota accounting active. The <code>-v</code> option (verbose) displays the state after the operation has completed.</p>
<dt><code>off</code> [ <code>-gpu</code> ] [ <code>-v</code> ]</p>
<dd>Permanently switches quota off for the filesystem identified by the current path. Quota can only be switched back on subsequently by unmounting and then mounting again.</p>
<dt><code>remove</code> [ <code>-gpu</code> ] [ <code>-v</code> ]</p>
<dd>Remove any space allocated to quota metadata from the filesystem identified by the current path. Quota must not be enabled on the filesystem, else this operation will report an error.</p>
<dt> <code></p>
<dd>dump</code> [ <code>-g</code> | <code>-p</code> | <code>-u</code> ] [ <code>-f</code> <i>file</i> ]<br />
 Dump out quota limit information for backup utilities, either to standard output (default) or to a <i>file</i>. This is only the limits, not the usage information, of course.</p>
<dt> <code>restore</code> [ <code>-g</code> | <code>-p</code> | <code>-u</code> ] [ <code>-f</code> <i>file</i> ]</p>
<dd>
<dd>Restore quota limits from a backup <i>file</i>. The file must be in the format produced by the <code>dump</code> command.</p>
<dt> <code></p>
<dd>quot</code> [ <code>-g</code> | <code>-p</code> | <code>-u</code> ] [ <code>-bir</code> ] [ <code>-acnv</code> ] [ <code>-f</code> <i>file</i> ]<br />
 Summarize filesystem ownership, by user, group or project. This command uses a special XFS &quot;bulkstat&quot; interface to quickly scan an entire filesystem and report usage information. This command can be used even when filesystem quota are not enabled, as it is a full-filesystem scan (it may also take a long time&#8230;). The <code>-a</code> option displays information on all filesystems. The <code>-c</code> option displays a histogram instead of a report. The <code>-n</code> option displays numeric IDs rather than names. The <code>-v</code> option displays verbose information. The <code>-f</code> option send the output to <i>file</i> instead of stdout.</p>
<dt> <code>project</code> [ <code>-cCs</code> [ <code>-d</code> <i>depth</i> ] [ <code>-p</code> <i>path</i> ] <i>id</i> | <i>name</i> ]</p>
<dd>
<dd>The <code>-c</code>, <code>-C</code>, and <code>-s</code> options allow the directory tree quota mechanism to be maintained. <code>-d</code> allows to limit recursion level when processing project directories and <code>-p</code> allows to specify project paths at command line ( instead of <i>/etc/projects</i> ). All options are discussed in detail below.</dl>
<h2>Directory Tree Quota</h2>
<p>The project quota mechanism in XFS can be used to implement a form of directory tree quota, where a specified directory and all of the files and subdirectories below it (i.e. a tree) can be restricted to using a subset of the available space in the filesystem. </p>
<p> A managed tree must be setup initially using the <code>-s</code> option to the <code>project</code> command. The specified project name or identifier is matched to one or more trees defined in <i>/etc/projects</i>, and these trees are then recursively descended to mark the affected inodes as being part of that tree. This process sets an inode flag and the project identifier on every file in the affected tree. Once this has been done, new files created in the tree will automatically be accounted to the tree based on their project identifier. An attempt to create a hard link to a file in the tree will only succeed if the project identifier matches the project identifier for the tree. The <code>xfs_io</code> utility can be used to set the project ID for an arbitrary file, but this can only be done by a privileged user. </p>
<p> A previously setup tree can be cleared from project quota control through use of the <code>project -C</code> option, which will recursively descend the tree, clearing the affected inodes from project quota control. </p>
<p> Finally, the <code>project -c</code> option can be used to check whether a tree is setup, it reports nothing if the tree is correct, otherwise it reports the paths of inodes which do not have the project ID of the rest of the tree, or if the inode flag is not set. </p>
<p> Option <code>-d</code> can be used to limit recursion level (-1 is infinite, 0 is top level only, 1 is first level &#8230; ). Option <code>-p</code> adds possibility to specify project paths in command line without a need for <i>/etc/projects</i> to exist. Note that if projects file exists then it is also used.</p>
<h2>Examples</h2>
<p>Enabling quota enforcement on an XFS filesystem (restrict a user to a set amount of space). </p>
<pre># mount -o uquota /dev/xvm/home /home
# xfs_quota -x -c 'limit bsoft=500m bhard=550m tanya' /home
# xfs_quota -x -c report /home</pre>
<p>Enabling project quota on an XFS filesystem (restrict files in log file directories to only using 1 gigabyte of space). </p>
<pre># mount -o prjquota /dev/xvm/var /var
# echo 42:/var/log &gt;&gt; /etc/projects
# echo logfiles:42 &gt;&gt; /etc/projid
# xfs_quota -x -c 'project -s logfiles' /var
# xfs_quota -x -c 'limit -p bhard=1g logfiles' /var</pre>
<p>Same as above without a need for configuration files. </p>
<pre># rm -f /etc/projects /etc/projid
# mount -o prjquota /dev/xvm/var /var
# xfs_quota -x -c 'project -s -p /var/log 42' /var
# xfs_quota -x -c 'limit -p bhard=1g 42' /var</pre>
<h2>Caveats</h2>
<p>XFS implements delayed allocation (aka. allocate-on-flush) and this has implications for the quota subsystem. Since quota accounting can only be done when blocks are actually allocated, it is possible to issue (buffered) writes into a file and not see the usage immediately updated. Only when the data is actually written out, either via one of the kernels flushing mechanisms, or via a manual <code><a href="/docs/linux/man/2-sync/">sync</a></code>(2), will the usage reported reflect what has actually been written. </p>
<p> In addition, the XFS allocation mechanism will always reserve the maximum amount of space required before proceeding with an allocation. If insufficient space for this reservation is available, due to the block quota limit being reached for example, this may result in the allocation failing even though there is sufficient space. Quota enforcement can thus sometimes happen in situations where the user is under quota and the end result of some operation would still have left the user under quota had the operation been allowed to run its course. This additional overhead is typically in the range of tens of blocks. </p>
<p> Both of these properties are unavoidable side effects of the way XFS operates, so should be kept in mind when assigning block limits.</p>
<h2>Bugs</h2>
<p>Quota support for filesystems with realtime subvolumes is not yet implemented, nor is the quota warning mechanism (the Linux <code><a href="/docs/linux/man/8-warnquota/">warnquota</a></code>(8) tool can be used to provide similar functionality on that platform).</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/projects</i></p>
<dd>Mapping of numeric project identifiers to directories trees.</p>
<dt><i>/etc/projid</i></p>
<dd>Mapping of numeric project identifiers to project names.</dl>
<h2>Irix See Also</h2>
<p><code><a href="//www.systutorials.com/docs/linux/man/1M-quotaon/">quotaon</a></code>(1M), <code><a href="/docs/linux/man/4-xfs/">xfs</a></code>(4).</p>
<h2>Linux See Also</h2>
<p><code><a href="/docs/linux/man/8-warnquota/">warnquota</a></code>(8), <code><a href="/docs/linux/man/5-xfs/">xfs</a></code>(5).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-df/">df</a></code>(1), <code><a href="/docs/linux/man/1-mount/">mount</a></code>(1), <code><a href="/docs/linux/man/2-sync/">sync</a></code>(2), <code><a href="/docs/linux/man/5-projid/">projid</a></code>(5), <code><a href="/docs/linux/man/5-projects/">projects</a></code>(5). </p>
