---
title: "vfs_shadow_copy2(8)"
name: "vfs_shadow_copy2"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_shadow_copy2/"
description: "vfs_shadow_copy2 – Expose snapshots to Windows clients as shadow copies."
---

<p>vfs_shadow_copy2 &#8211; Expose snapshots to Windows clients as shadow copies.</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = shadow_copy2</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The vfs_shadow_copy2 VFS module offers a functionality similar to Microsoft Shadow Copy services. When set up properly, this module allows Microsoft Shadow Copy clients to browse through file system snapshots as &quot;shadow copies&quot; on Samba shares. </p>
<p> This is a second implementation of a shadow copy module which has the following additional features (compared to the original <code><a href="/docs/linux/man/8-shadow_copy/">shadow_copy</a></code>(8) module): </p>
<dl>
<dd>1. There is no need any more to populate your share&#8217;s root directory with symlinks to the snapshots if the file system stores the snapshots elsewhere. Instead, you can flexibly configure the module where to look for the file system snapshots. This can be very important when you have thousands of shares, or use [homes].</dl>
<dl>
<dd>2. Snapshot directories need not be in one fixed central place but can be located anywhere in the directory tree. This mode helps to support file systems that offer snapshotting of particular subtrees, for example the GPFS independent file sets.</dl>
<dl>
<dd>3. Vanity naming for snapshots: snapshots can be named in any format compatible with str[fp]time conversions.</dl>
<dl>
<dd>4. Timestamps can be represented in localtime rather than UTC.</dl>
<dl>
<dd>5. The inode number of the files can optionally be altered to be different from the original. This fixes the &#8216;restore&#8217; button in the Windows GUI to work without a sharing violation when serving from file systems, like GPFS, that return the same device and inode number for the snapshot file and the original.</dl>
<dl>
<dd>6. Shadow copy results are by default sorted before being sent to the client. This is beneficial for filesystems that don&#8217;t read directories alphabetically (the default unix). Sort ordering can be configured and sorting can be turned off completely if the file system sorts its directory listing.</dl>
<p> This module is stackable.</p>
<h2>Configuration</h2>
<p>vfs_shadow_copy2 relies on a filesystem snapshot implementation. Many common filesystems have native support for this. </p>
<p> Filesystem snapshots must be available under specially named directories in order to be recognized by vfs_shadow_copy2. These snapshot directory is typically a direct subdirectory of the share root&#8217;s mountpoint but there are other modes that can be configured with the parameters described in detail below. </p>
<p> The snapshot at a given point in time is expected in a subdirectory of the snapshot directory where the snapshot&#8217;s directory is expected to be a formatted version of the snapshot time. The default format which can be changed with the shadow:format option is @GMT-YYYY.MM.DD-hh.mm.ss, where: </p>
<dl>
<dd>&bull; YYYY is the 4 digit year</dl>
<dl>
<dd>&bull; MM is the 2 digit month</dl>
<dl>
<dd>&bull; DD is the 2 digit day</dl>
<dl>
<dd>&bull; hh is the 2 digit hour</dl>
<dl>
<dd>&bull; mm is the 2 digit minute</dl>
<dl>
<dd>&bull; ss is the 2 digit second.</dl>
<p> The vfs_shadow_copy2 snapshot naming convention can be produced with the following <code><a href="/docs/linux/man/1-date/">date</a></code>(1) command: </p>
<dl>
<dd>
<pre> TZ=GMT date +@GMT-%Y.%m.%d-%H.%M.%S</pre>
</dl>
<h2>Options</h2>
<p>shadow:mountpoint = MOUNTPOINT</p>
<dl>
<dd>With this parameter, one can specify the mount point of the filesystem that contains the share path. Usually this mount point is automatically detected. But for some constellations, in particular tests, it can be convenient to be able to specify it. </p>
<p> Example: shadow:mountpoint = /path/to/filesystem </p>
<p> Default: shadow:mountpoint = NOT SPECIFIED</dl>
<p> shadow:snapdir = SNAPDIR</p>
<dl>
<dd>Path to the directory where the file system of the share keeps its snapshots. If an absolute path is specified, it is used as-is. If a relative path is specified, then it is taken relative to the mount point of the filesystem of the share root. (See shadow:mountpoint.) </p>
<p> Note that shadow:snapdirseverywhere depends on this parameter and needs a relative path. Setting an absolute path disables shadow:snapdirseverywhere. </p>
<p> Note that the shadow:crossmountpoints option also requires a relative snapdir. Setting an absolute path disables shadow:crossmountpoints. </p>
<p> Example: shadow:snapdir = /some/absolute/path </p>
<p> Default: shadow:snapdir = .snapshots</dl>
<p> shadow:basedir = BASEDIR</p>
<dl>
<dd>The basedir option allows one to specify a directory between the share&#8217;s mount point and the share root, relative to which the file system&#8217;s snapshots are taken. </p>
<p> For example, if </p>
<dl>
<dd>&bull; basedir = mountpoint/rel_basedir</dl>
<dl>
<dd>&bull; share_root = basedir/rel_share_root</dl>
<dl>
<dd>&bull; snapshot_path = mountpoint/snapdir </p>
<p> or snapshot_path = snapdir if snapdir is absolute</dl>
</dl>
<p> then the snapshot of a file = mountpoint/rel_basedir/rel_share_root/rel_file at a time TIME will be found under snapshot_path/FS_GMT_TOKEN(TIME)/rel_share_root/rel_file, where FS_GMT_TOKEN(TIME) is the timestamp string belonging to TIME in the format required by the file system. (See shadow:format.) </p>
<p> The default for the basedir is the mount point of the file system of the share root (see shadow:mountpoint). </p>
<p> Note that the shadow:snapdirseverywhere and shadow:crossmountpoints options are incompatible with shadow:basedir and disable the basedir setting. </p>
<p> shadow:snapsharepath = SNAPSHAREPATH</p>
<dl>
<dd>With this parameter, one can specify the path of the share&#8217;s root directory in snapshots, relative to the snapshot&#8217;s root directory. It is an alternative method to shadow:basedir, allowing greater control. </p>
<p> For example, if within each snapshot the files of the share have a path/to/share/ prefix, then shadow:snapsharepath can be set to path/to/share. </p>
<p> With this parameter, it is no longer assumed that a snapshot represents an image of the original file system or a portion of it. For example, a system could perform backups of only files contained in shares, and then expose the backup files in a logical structure: </p>
<dl>
<dd>&bull; share1/</dl>
<dl>
<dd>&bull; share2/</dl>
<dl>
<dd>&bull; &#8230;/</dl>
</dl>
<p> Note that the shadow:snapdirseverywhere and the shadow:basedir options are incompatible with shadow:snapsharepath and disable shadow:snapsharepath setting. </p>
<p> Example: shadow:snapsharepath = path/to/share </p>
<p> Default: shadow:snapsharepath = NOT SPECIFIED </p>
<p> shadow:sort = asc/desc</p>
<dl>
<dd>By default, this module sorts the shadow copy data alphabetically before sending it to the client. With this parameter, one can specify the sort order. Possible known values are desc (descending, the default) and asc (ascending). If the file system lists directories alphabetically sorted, one can turn off sorting in this module by specifying any other value. </p>
<p> Example: shadow:sort = asc </p>
<p> Example: shadow:sort = none </p>
<p> Default: shadow:sort = desc</dl>
<p> shadow:localtime = yes/no</p>
<dl>
<dd>This is an optional parameter that indicates whether the snapshot names are in UTC/GMT or in local time. If it is disabled then UTC/GMT is expected. </p>
<p> shadow:localtime = no</dl>
<p> shadow:format = format specification for snapshot names</p>
<dl>
<dd>This is an optional parameter that specifies the format specification for the naming of snapshots in the file system. The format must be compatible with the conversion specifications recognized by str[fp]time. </p>
<p> Default: shadow:format = &quot;@GMT-%Y.%m.%d-%H.%M.%S&quot;</dl>
<p> shadow:sscanf = yes/no</p>
<dl>
<dd>This parameter can be used to specify that the time in format string is given as an unsigned long integer (%lu) rather than a time strptime() can parse. The result must be a unix time_t time. </p>
<p> Default: shadow:sscanf = no</dl>
<p> shadow:fixinodes = yes/no</p>
<dl>
<dd>If you enable shadow:fixinodes then this module will modify the apparent inode number of files in the snapshot directories using a hash of the files path. This is needed for snapshot systems where the snapshots have the same device:inode number as the original files (such as happens with GPFS snapshots). If you don&#8217;t set this option then the &#8216;restore&#8217; button in the shadow copy UI will fail with a sharing violation. </p>
<p> Default: shadow:fixinodes = no</dl>
<p> shadow:snapdirseverywhere = yes/no</p>
<dl>
<dd>If you enable shadow:snapdirseverywhere then this module will look out for snapshot directories in the current working directory and all parent directories, stopping at the mount point by default. But see shadow:crossmountpoints how to change that behaviour. </p>
<p> An example where this is needed are independent filesets in IBM&#8217;s GPFS, but other filesystems might support snapshotting only particular subtrees of the filesystem as well. </p>
<p> Note that shadow:snapdirseverywhere depends on shadow:snapdir and needs it to be a relative path. Setting an absolute snapdir path disables shadow:snapdirseverywhere. </p>
<p> Note that this option is incompatible with the shadow:basedir option and removes the shadow:basedir setting by itself. </p>
<p> Example: shadow:snapdirseverywhere = yes </p>
<p> Default: shadow:snapdirseverywhere = no</dl>
<p> shadow:crossmountpoints = yes/no</p>
<dl>
<dd>This option is effective in the case of shadow:snapdirseverywhere = yes. Setting this option makes the module not stop at the first mount point encountered when looking for snapdirs, but lets it search potentially all through the path instead. </p>
<p> An example where this is needed are independent filesets in IBM&#8217;s GPFS, but other filesystems might support snapshotting only particular subtrees of the filesystem as well. </p>
<p> Note that shadow:crossmountpoints depends on shadow:snapdir and needs it to be a relative path. Setting an absolute snapdir path disables shadow:crossmountpoints. </p>
<p> Note that this option is incompatible with the shadow:basedir option and removes the shadow:basedir setting by itself. </p>
<p> Example: shadow:crossmountpoints = yes </p>
<p> Default: shadow:crossmountpoints = no</dl>
<p> shadow:snapprefix</p>
<dl>
<dd>With growing number of snapshots file-systems need some mechanism to differentiate one set of snapshots from other, e.g. monthly, weekly, manual, special events, etc. Therefore these file-systems provide different ways to tag snapshots, e.g. provide a configurable way to name snapshots, which is not just based on time. With only shadow:format it is very difficult to filter these snapshots. With this optional parameter, one can specify a variable prefix component for names of the snapshot directories in the file-system. If this parameter is set, together with the shadow:format and shadow:delimiter parameters it determines the possible names of snapshot directories in the file-system. The option only supports Basic Regular Expression (BRE).</dl>
<p> shadow:delimiter</p>
<dl>
<dd>This optional parameter is used as a delimiter between shadow:snapprefix and shadow:format. This parameter is used only when shadow:snapprefix is set. </p>
<p> Default: shadow:delimiter = &quot;_GMT&quot;</dl>
<h2>Examples</h2>
<p>Add shadow copy support to user home directories: </p>
<dl>
<dd>
<pre> <i>[homes]</i>
 m[blue]<code>vfs objects = shadow_copy2</code>m[]
 m[blue]<code>shadow:snapdir = /data/snapshots</code>m[]
 m[blue]<code>shadow:basedir = /data/home</code>m[]
 m[blue]<code>shadow:sort = desc</code>m[]</pre>
</dl>
<h2>Caveats</h2>
<p>This is not a backup, archival, or version control solution. </p>
<p> With Samba or Windows servers, vfs_shadow_copy2 is designed to be an end-user tool only. It does not replace or enhance your backup and archival solutions and should in no way be considered as such. Additionally, if you need version control, implement a version control system.</p>
<h2>Version</h2>
<p>This man page is correct for version 4.0 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
