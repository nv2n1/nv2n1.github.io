---
title: "gfs_tool(8)"
name: "gfs_tool"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gfs_tool/"
description: "gfs_tool – interface to gfs ioctl calls"
---

<p>gfs_tool &#8211; interface to gfs ioctl calls</p>
<h2>Synopsis</h2>
<p><code>gfs_tool</code> <i>COMMAND</i> [<i>OPTION</i>] [<i>PARAMETERS &#8230;</i>] </p>
<h2>Description</h2>
<p>gfs_tool is an interface to a variety of the GFS ioctl calls.</p>
<dl>
<dt>Specifying gfs_tool -h prints gfs_tool command line usage (help).</p>
<dd>
<dt>Specifying gfs_tool -V prints the gfs_tool version information.</p>
<dd></dl>
<h2>Commands</h2>
<dl>
<dt><code>clearflag</code> <i>Flag</i> <i>File1</i> <i>File2</i> <i>&#8230;</i></p>
<dd>Clear an attribute flag on a file.</p>
<dt><code>counters</code> <i>MountPoint</i> [-c] [-i <i>interval</i>]</p>
<dd>Print out statistics about a filesystem. If -c is specified, gfs_tool keeps running printing out the statistics once per second or, if specified, the interval given with the -i option, in seconds.</p>
<dt><code>df</code> <i>MountPoint</i> [-k]|[-H]</p>
<dd>Print out a space usage summary of a given filesystem. The information printed is more detailed than a standard &quot;df&quot;. If -k is specified, the output is given in kilobytes (KB). If -H is specified, the output is given in human readable format (similar to df -h). If neither -k nor -H are specified, the output is given in file system blocks. </p>
<dt><code>freeze</code> <i>MountPoint</i></p>
<dd>Freeze (quiesce) a GFS cluster.</p>
<dt><code>getsb</code> <i>MountPoint</i></p>
<dd>Print out the superblock of a mounted filesystem.</p>
<dt><code>gettune</code> <i>MountPoint</i></p>
<dd>Print out the current values of the tuning parameters in a running filesystem.</p>
<dt><code>jindex</code> <i>MountPoint</i></p>
<dd>Print out the journal index of a mounted filesystem.</p>
<dt><code>layout</code> <i>File</i> <i>[buffersize]</i></p>
<dd>Print out on-disk layout information about a file or directory. Buffersize is the size of the buffer (in bytes) that gfs_tool allocates to store the file&#8217;s metadata during processing. It defaults to 4194304 bytes. If you are printing a very big directory you may need to specify a bigger size.</p>
<dt><code>list</code></p>
<dd>List the currently mounted GFS filesystems. Each line represents a filesystem. The columns represent (in order): 1) A number that is a cookie that represents the mounted filesystem. 2) The name of the device that holds the filesystem (well, the name as the Linux kernel knows it). 3) The lock table field that the filesystem was mounted with.</p>
<dt><code>lockdump</code> <i>MountPoint</i> <i>[buffersize]</i></p>
<dd>Print out information about the locks this machine holds for a given filesystem. Buffersize is the size of the buffer (in bytes) that gfs_tool allocates to store the lock data during processing. It defaults to 4194304 bytes.</p>
<dt><code>margs</code> <i>arguments</i></p>
<dd>This loads arguments into the module what will override the mount options passed with the -o field on the next mount. See <a href="/docs/linux/man/8-mount-gfs/">mount.gfs</a>(8).</p>
<dt><code>reclaim</code> <i>File</i></p>
<dd>Returns unused on-disk metadata blocks to free blocks.</p>
<dt><code>rindex</code> <i>MountPoint</i></p>
<dd>Print out the resource group index of a mounted filesystem.</p>
<dt><code>quota</code> <i>MountPoint</i></p>
<dd>Print out the quota file of a mounted filesystem. Also see the &quot;gfs_quota list&quot; command.</p>
<dt><code>sb</code> <i>device</i> <code>proto</code> <i>[newvalue]</i></p>
<dd>View (and possibly replace) the name of the locking protocol in the file system superblock. The file system shouldn&#8217;t be mounted by any client when you do this.</p>
<dt><code>sb</code> <i>device</i> <code>table</code> <i>[newvalue]</i></p>
<dd>View (and possibly replace) the name of the locking table in the file system superblock. The file system shouldn&#8217;t be mounted by any client when you do this.</p>
<dt><code>sb</code> <i>device</i> <code>ondisk</code> <i>[newvalue]</i></p>
<dd>View (and possibly replace) the ondisk format number in the file system superblock. The file system shouldn&#8217;t be mounted by any client when you do this. No one should have to use this.</p>
<dt><code>sb</code> <i>device</i> <code>multihost</code> <i>[newvalue]</i></p>
<dd>View (and possibly replace) the multihost format number in the file system superblock. The file system shouldn&#8217;t be mounted by any client when you do this. No one should have to use this.</p>
<dt><code>sb</code> <i>device</i> <code>all</code></p>
<dd>Print out the superblock.</p>
<dt><code>setflag</code> <i>Flag</i> <i>File1</i> <i>File2</i> <i>&#8230;</i></p>
<dd>Set an attribute flag on a file. There are four currently supported flags. They are jdata, directio, inherit_jdata, and inherit_directio.<br />
&nbsp;<wbr>&nbsp;<wbr> The <i>jdata</i> flag causes all the data written to a regular file to be journaled. The jdata flag can only be set (or cleared) if the file is zero length. </p>
<p> The <i>directio</i> flag causes all I/O to a regular file to be Direct I/O, even if the O_DIRECT flag isn&#8217;t used on the open() command. </p>
<p> The <i>inherit_jdata</i> flag is set on a directory. It causes all new regular files created in that directory automatically inherit the <i>jdata</i> flag. The <i>inherit_jdata</i> is also inherited by any new subdirectories created in that directory. </p>
<p> The <i>inherit_directio</i> flag is set on a directory. It causes all new regular files created in that directory automatically inherit the <i>directio</i> flag. The <i>inherit_directio</i> is also inherited by any new subdirectories created in that directory.</p>
<dt><code>settune</code> <i>MountPoint</i> <i>parameter</i> <i>newvalue</i></p>
<dd>Set the value of tuning parameter. Use <code>gettune</code> for a listing of tunable parameters.</p>
<dt><code>shrink</code> <i>MountPoint</i></p>
<dd>Causes any unused inodes to be thrown out of memory.</p>
<dt><code>stat</code> <i>File</i></p>
<dd>Print out extended stat information about a file.</p>
<dt><code>unfreeze</code> <i>MountPoint</i></p>
<dd>Unfreeze a GFS cluster.</p>
<dt><code>version</code></p>
<dd>Print out the version of GFS that this program goes with.</p>
<dt><code>withdraw</code> <i>MountPoint</i></p>
<dd>Cause GFS to abnormally shutdown a given filesystem on this node. </p>
</dl>
