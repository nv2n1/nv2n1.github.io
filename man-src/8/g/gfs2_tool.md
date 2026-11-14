---
title: "gfs2_tool(8)"
name: "gfs2_tool"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gfs2_tool/"
description: "gfs2_tool – interface to gfs2 ioctl/sysfs calls"
---

<p>gfs2_tool &#8211; interface to gfs2 ioctl/sysfs calls</p>
<h2>Synopsis</h2>
<p><code>gfs2_tool</code> <i>COMMAND</i> [<i>OPTION</i>]&#8230; </p>
<h2>Description</h2>
<p>gfs2_tool is an interface to a variety of the GFS2 ioctl/sysfs calls. Some of the functions of gfs_tool have been replaced by standard system tools such as mount and chattr, so gfs2_tool doesn&#8217;t have as many options as gfs_tool used to. </p>
<h2>Commands</h2>
<dl>
<dt><code>clearflag</code> <i>Flag</i> <i>File1</i> <i>File2</i> <i>&#8230;</i></p>
<dd>Clear an attribute flag on a file. This is now obsolete and kept only for backward compatibility, chattr is the preferred way to clear attribute flags. See <code>setflag</code> for available flags. This option will probably be removed at a future date.</p>
<dt><code>freeze</code> <i>MountPoint</i></p>
<dd>Freeze (quiesce) a GFS2 cluster.</p>
<dt><code>gettune</code> <i>MountPoint</i></p>
<dd>Print out the current values of the tuning parameters in a running filesystem. A better source of similar (more comprehensive) information is that in the /proc/mounts file. Running the mount command with no arguments will also provide the same information. This option is considered obsolete and will probably be removed at some future date.</p>
<dt><code>journals</code> <i>MountPoint</i></p>
<dd>Print out information about the journals in a mounted filesystem.</p>
<dt><code>lockdump</code> <i>MountPoint</i></p>
<dd>Print out information about the locks this machine holds for a given filesystem. This information is also available via the debugfs glock dump file, and accessing that file is the preferred method of obtaining a dump of the glock state.</p>
<dt><code>sb</code> <i>device</i> <code>proto</code> <i>[newvalue]</i></p>
<dd>View (and possibly replace) the name of the locking protocol in the file system superblock. The file system shouldn&#8217;t be mounted by any client when you do this.</p>
<dt><code>sb</code> <i>device</i> <code>table</code> <i>[newvalue]</i></p>
<dd>View (and possibly replace) the name of the locking table in the file system superblock. The file system shouldn&#8217;t be mounted by any client when you do this.</p>
<dt><code>sb</code> <i>device</i> <code>ondisk</code> <i>[newvalue]</i></p>
<dd>View (and possibly replace) the ondisk format number in the file system superblock. The file system shouldn&#8217;t be mounted by any client when you do this. No one should have to use this.</p>
<dt><code>sb</code> <i>device</i> <code>multihost</code> <i>[newvalue]</i></p>
<dd>View (and possibly replace) the multihost format number in the file system superblock. The file system shouldn&#8217;t be mounted by any client when you do this. No one should have to use this.</p>
<dt><code>sb</code> <i>device</i> <code>uuid</code> <i>[newvalue]</i></p>
<dd>View (and possibly replace) the uuid in the file system superblock. The file system shouldn&#8217;t be mounted by any client when you do this. The new uuid value should be in the standard uuid format. For example: 1AEA8269-15C5-72BD-6D83-8720B17AA4EE</p>
<dt><code>sb</code> <i>device</i> <code>all</code></p>
<dd>Print out the superblock.</p>
<dt><code>setflag</code> <i>Flag</i> <i>File1</i> <i>File2</i> <i>&#8230;</i></p>
<dd>Set an attribute flag on a file. The currently supported flags are jdata, immutable, appendonly, noatime, and sync. The chattr command is the preferred way to set attributes on files. This option will probably be removed at a future date. </p>
<p> The <i>jdata</i> flag causes all the data written to a file to be journaled. If the <i>jdata</i> flag is set for a directory, all files and directories subsequently created within that directory are also journaled. This behavior replaces the old <i>inherit_jdata</i> flag from gfs. Same as chattr +j. </p>
<p> The <i>immutable</i> flag marks the file immutable. The behavior is similar to the immutable flag in the ext2/3 filesystems. All write access is denied. Same as chattr +i. </p>
<p> The <i>appendonly</i> flag causes all data to be written at the end of the file. Same as chattr +a. </p>
<p> The <i>noatime</i> flag disables updates to the file&#8217;s access time. Same as chattr +A. </p>
<p> The <i>sync</i> flag causes data written to the file to be sync&#8217;ed to stable storage immediately. Same as chattr +S.</p>
<dt><code>settune</code> <i>MountPoint</i> <i>parameter</i> <i>newvalue</i></p>
<dd>Set the value of tuning parameter. Use <code>gettune</code> for a listing of tunable parameters. The mount -oremount command is the preferred way to set the values of tunable parameters. At some future stage, when all parameters can be set via mount, this option will be removed.</p>
<dt><code>unfreeze</code> <i>MountPoint</i></p>
<dd>Unfreeze a GFS2 cluster.</p>
<dt><code>version</code></p>
<dd>Print out the version of GFS2 that this program goes with.</p>
<dt><code>withdraw</code> <i>MountPoint</i></p>
<dd>Cause GFS2 to abnormally shutdown a given filesystem on this node. This feature is only useful for testing and should not be used during normal filesystem operation. </p>
</dl>
