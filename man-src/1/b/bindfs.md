---
title: "bindfs(1)"
name: "bindfs"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bindfs/"
description: "bindfs – mount –bind in user-space"
---

<h2 class="name">NAME</h2>
<p> bindfs &#8211; mount &#8211;bind in user-space </p>
<h2>SYNOPSIS</h2>
<p> <code>bindfs</code> [<i>options</i>]<i> dir mountpoint </p>
<p> </i></p>
<h2>DESCRIPTION</h2>
<p> A FUSE filesystem for mirroring the contents of a directory to another directory. Additionally, one can change the permissions of files in the mirrored directory. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Displays a help message and exits. </p>
<dt><code>-V, &#8211;version</code></p>
<dd> Displays version information and exits. </p>
<dt><code>-u, &#8211;user, &#8211;owner=</code><i>user</i>, -o owner=&#8230;</p>
<dd> Makes all files owned by the specified user. Also causes chown on the mounted filesystem to always fail. </p>
<dt><code>-g, &#8211;group=</code><i>group</i>, -o group=&#8230;</p>
<dd> Makes all files owned by the specified group. Also causes chgrp on the mounted filesystem to always fail. </p>
<dt><code>-p, &#8211;perms=</code><i>permissions</i>, -o perms=&#8230;</p>
<dd> Takes a comma- or colon-separated list of chmod-like permission specifications to be applied to the permission bits in order. See <code>PERMISSION SPECIFICATION</code> below for details. </p>
<p> This only affects how the permission bits of existing files are altered when shown in the mounted directory. You can use &#8211;create-with-perms to change the permissions newly created files get in the source directory. </p>
<dt><code>-m, &#8211;mirror=</code><i>users</i>, -o mirror=&#8230;</p>
<dd> Takes a comma- or colon-separated list of users who will see themselves as the owners of all files. Users who are not listed here will still be able to access the mount if the permissions otherwise allow them to. </p>
<p> You can also give a group name prefixed with an &#8216;@&#8217; to mirror all members of a group. This will not change which group the files are shown to have. </p>
<dt><code>-M, &#8211;mirror-only=</code><i>users</i>, -o mirror-only=&#8230;</p>
<dd> Like <code>&#8211;mirror</code> but disallows access for all other users (except root). </p>
<dt><code>-n, &#8211;no-allow-other, -o no-allow-other</code></p>
<dd> Does not add <code>-o allow_other</code> to FUSE options. This causes the mount to be accessible only by the current user. </p>
</dl>
<h2>FILE CREATION POLICY</h2>
<p> New files and directories are created so they are owned by the mounter. bindfs can let this happen (the default for normal users), or it can try to change the owner to the uid/gid of the process that wants to create the file (the default for root). It is also possible to have bindfs try to change the owner to a particular user or group. </p>
<dl>
<dt><code>&#8211;create-as-user, -o create-as-user</code></p>
<dd> Tries to change the owner and group of new files and directories to the uid and gid of the caller. This can work only if the mounter is root. It is also the default behavior (mimicing mount &#8211;bind) if the mounter is root. </p>
<dt><code>&#8211;create-as-mounter, -o create-as-mounter</code></p>
<dd> All new files and directories will be owned by the mounter. This is the default behavior for non-root mounters. </p>
<dt><code>&#8211;create-for-user=</code><i>user</i>, -o create-for-user=&#8230;</p>
<dd> Tries to change the owner of new files and directories to the user specified here. This can work only if the mounter is root. This option overrides the &#8211;create-as-user and &#8211;create-as-mounter options. </p>
<dt><code>&#8211;create-for-group=</code><i>group</i>, -o create-for-group=&#8230;</p>
<dd> Tries to change the owning group of new files and directories to the group specified here. This can work only if the mounter is root. This option overrides the &#8211;create-as-user and &#8211;create-as-mounter options. </p>
<dt><code>&#8211;create-with-perms=</code><i>permissions</i>, -o create-with-perms=&#8230;</p>
<dd> Works like &#8211;perms but is applied to the permission bits of new files get in the source directory. Normally the permissions of new files depend on the creating process&#8217;s preferences and umask. This option can be used to modify those permissions or override them completely. See <code>PERMISSION SPECIFICATION</code> below for details. </p>
</dl>
<h2>CHMOD POLICY</h2>
<p> Chmod calls are forwarded to the source directory by default. This may cause unexpected behaviour if bindfs is altering permission bits. Note that regardless of the options given below, if the <code>-u</code> and <code>-g</code> options are given then chown and chgrp respectively will always fail. </p>
<dl>
<dt><code>&#8211;chmod-normal, -o chmod-normal</code></p>
<dd> Tries to chmod the underlying file. This will succeed if the user has the appropriate mirrored permissions to chmod the mirrored file AND the mounter has enough permissions to chmod the real file. This is the default (in order to behave like mount &#8211;bind by default). </p>
<dt><code>&#8211;chmod-ignore, -o chmod-ignore</code></p>
<dd> Lets chmod succeed (if the user has enough mirrored permissions) but actually does nothing. </p>
<dt><code>&#8211;chmod-deny, -o chmod-deny</code></p>
<dd> Has chmod always fail with a &#8216;permission denied&#8217; error. </p>
<dt><code>&#8211;chmod-allow-x, -o chmod-allow-x</code></p>
<dd> Allows setting and clearing the executable attribute on files (but not directories). When used with &#8211;chmod-ignore, chmods will only affect execute bits on files and changes to other bits are discarded. With &#8211;chmod-deny, all chmods that would change any bits except excecute bits on files will still fail with a &#8216;permission denied&#8217;. This option does nothing with &#8211;chmod-normal. </p>
</dl>
<h2>XATTR POLICY</h2>
<p> Extended attributes are mirrored by default, though not all underlying file systems support xattrs. </p>
<dl>
<dt><code>&#8211;xattr-none, -o xattr-none</code></p>
<dd> Disable extended attributes altogether. All operations will return &#8216;Operation not supported&#8217;. </p>
<dt><code>&#8211;xattr-ro, -o xattr-ro</code></p>
<dd> Let extended attributes be read-only. </p>
<dt><code>&#8211;xattr-rw, -o xattr-rw</code></p>
<dd> Let extended attributes be read-write (the default). The read/write permissions are checked against the (possibly modified) file permissions inside the mount. </p>
</dl>
<h2>TIME-RELATED OPTIONS</h2>
<p> Recall that a unix file has three standard timestamps: <code>atime</code> (last access i.e. read time), <code>mtime</code> (last content modification time) <code>ctime</code> (last content or metadata (inode) change time) </p>
<p> It may sometimes be useful to alter these timestamps, but care should be taken not to cause programs (e.g. backup jobs) miss important changes. </p>
<dl>
<dt><code>&#8211;ctime-from-mtime, -o ctime-from-mtime</code></p>
<dd> Reads the ctime of each file and directory from its mtime. In other words, only content modifications (as opposed to metadata changes) will be reflected in a mirrored file&#8217;s ctime. (The underlying file&#8217;s ctime will still be updated normally.) </p>
</dl>
<h2>FUSE OPTIONS</h2>
<dl>
<dt><code>-o </code><i>options</i></p>
<dd> Fuse options. </p>
<dt><code>-d, -o debug</code></p>
<dd> Enable debug output (implies -f). </p>
<dt><code>-f</code></p>
<dd> Foreground operation. </p>
<dt><code>-s</code></p>
<dd> Disable multithreaded operation. </p>
</dl>
<h2>PERMISSION SPECIFICATION</h2>
<p> The <code>-p</code> option takes a comma- or colon-separated list of either octal numeric permission bits or symbolic representations of permission bit operations. The symbolic representation is based on that of the <code><a href="/docs/linux/man/1-chmod/">chmod</a></code>(1) command. setuid, setgid and sticky bits are ignored. </p>
<p> This program extends the chmod symbolic representation with the following operands: </p>
<p> `<code>D</code>&#8216; (right hand side)<br />
&nbsp;<wbr>Works like&nbsp;<wbr><code>X</code>&nbsp;<wbr>but applies only to directories&nbsp;<wbr>(not to executables). </p>
<p> `<code>d</code>&#8216; and `<code>f</code>&#8216; (left hand side)<br />
&nbsp;<wbr>Makes this directive only apply to directories&nbsp;<wbr>(d)&nbsp;<wbr>or files&nbsp;<wbr>(f).<br />
&nbsp;<wbr>e.g.&nbsp;<wbr><code>gd-w</code>&nbsp;<wbr>would remove the group write bit from all directories. </p>
<p> `<code>u</code>&#8216;, `<code>g</code>&#8216;, `<code>o</code>&#8216; (right hand side)<br />
&nbsp;<wbr>Uses the user&nbsp;<wbr>(u), group&nbsp;<wbr>(g)&nbsp;<wbr>or others&nbsp;<wbr>(o)&nbsp;<wbr>permission bits of<br />
&nbsp;<wbr>the original file.<br />
&nbsp;<wbr>e.g.&nbsp;<wbr><code>g=u</code>&nbsp;<wbr>would copy the user&#8217;s permission bits to the group.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>ug+o</code>&nbsp;<wbr>would add the others&#8217;&nbsp;<wbr>permissions to the owner and group. </p>
<p> <i>Examples</i></p>
<dl>
<dt><code>o-rwx</code></p>
<dd> Removes all permission bits from others. </p>
<dt><code>g=rD</code></p>
<dd> Allows group to read all files and enter all directories, but nothing else. </p>
<dt><code>0644,a+X</code></p>
<dd> Sets permission bits to 0644 and adds the execute bit for everyone to all directories and executables. </p>
<dt><code>og-x:og+rD:u=rwX:g+rw</code></p>
<dd> Removes execute bit for others and group, adds read and directory execute for others and group, sets user permissions to read, write and execute directory/executable, adds read and write for group. </p>
</dl>
<h2>EXAMPLES</h2>
<p> <code>.TP</code> <code>bindfs -u www -g nogroup -p 0000,u=rD ~/mywebsite ~/public_html/mysite</code> </p>
<p> Publishes a website in public_html so that only the &#8216;www&#8217; user can read the site. </p>
<dl>
<dt><code>bindfs -M foo,bar,1007,@mygroup -p 0600,u+X dir mnt</code></p>
<dd>
<p> Gives access to &#8216;foo&#8217;, &#8216;bar&#8217;, the user with the UID 1007 as well as everyone in the group &#8216;mygroup&#8217;. Sets the permission bits to 0600, thus giving the specified users read/write access, and adds the user execute bit for directories and executables. </p>
<dt><code>bindfs -ono-allow-other,perms=a-w somedir somedir</code></p>
<dd>
<p> Makes a directory read-only and accessable only by the current user. </p>
<dt><code>bindfs#/home/bob/shared /var/www/shared/bob fuse perms=0000:u+rD 0 0</code></p>
<dd>
<p> An example <i>/etc/fstab</i> entry. Note that the colon must be used to separate arguments to perms, because the comma is an option separator in <i>/etc/fstab</i>. </p>
</dl>
<h2>NOTES</h2>
<p> Setuid and setgid bits have no effect inside the mount. This is a necessary security feature of FUSE. </p>
<h2>BUGS</h2>
<p> Please report to the issue tracker on the project home page at <a rel="nofollow" href="http://code.google.com/p/bindfs/">http://code.google.com/p/bindfs/</a> </p>
<h2>AUTHOR</h2>
<p> Martin P[:a]rtel &lt;martin dot partel at gmail dot com&gt; </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-chmod/">chmod</a></code>(1), <code><a href="/docs/linux/man/1-fusermount/">fusermount</a></code>(1) </p>
<h2>Index</h2>
