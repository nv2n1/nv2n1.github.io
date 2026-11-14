---
title: "path_resolution(7)"
name: "path_resolution"
section: "7"
letter: "p"
url: "/docs/linux/man/7-path_resolution/"
description: "path_resolution – how a pathname is resolved to a file"
---

<p>path_resolution &#8211; how a pathname is resolved to a file</p>
<h2>Description</h2>
<p>Some UNIX/Linux system calls have as parameter one or more filenames. A filename (or pathname) is resolved as follows.</p>
<h3>Step 1: start of the resolution process</h3>
<p>If the pathname starts with the &#8216;/&#8217; character, the starting lookup directory is the root directory of the calling process. A process inherits its root directory from its parent. Usually this will be the root directory of the file hierarchy. A process may get a different root directory by use of the <code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2) system call, or may temporarily use a different root directory by using <code><a href="/docs/linux/man/2-openat2/">openat2</a></code>(2) with the <code>RESOLVE_IN_ROOT</code> flag set. </p>
<p> A process may get an entirely private mount namespace in case it&#8212;or one of its ancestors&#8212;was started by an invocation of the <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) system call that had the <code>CLONE_NEWNS</code> flag set. This handles the &#8216;/&#8217; part of the pathname. </p>
<p> If the pathname does not start with the &#8216;/&#8217; character, the starting lookup directory of the resolution process is the current working directory of the process &#8212; or in the case of <code><a href="/docs/linux/man/2-openat/">openat</a></code>(2)-style system calls, the <i>dfd</i> argument (or the current working directory if <code>AT_FDCWD</code> is passed as the <i>dfd</i> argument). The current working directory is inherited from the parent, and can be changed by use of the <code><a href="/docs/linux/man/2-chdir/">chdir</a></code>(2) system call.) </p>
<p> Pathnames starting with a &#8216;/&#8217; character are called absolute pathnames. Pathnames not starting with a &#8216;/&#8217; are called relative pathnames.</p>
<h3>Step 2: walk along the path</h3>
<p>Set the current lookup directory to the starting lookup directory. Now, for each nonfinal component of the pathname, where a component is a substring delimited by &#8216;/&#8217; characters, this component is looked up in the current lookup directory. </p>
<p> If the process does not have search permission on the current lookup directory, an <code>EACCES</code> error is returned (&quot;Permission denied&quot;). </p>
<p> If the component is not found, an <code>ENOENT</code> error is returned (&quot;No such file or directory&quot;). </p>
<p> If the component is found, but is neither a directory nor a symbolic link, an <code>ENOTDIR</code> error is returned (&quot;Not a directory&quot;). </p>
<p> If the component is found and is a directory, we set the current lookup directory to that directory, and go to the next component. </p>
<p> If the component is found and is a symbolic link (symlink), we first resolve this symbolic link (with the current lookup directory as starting lookup directory). Upon error, that error is returned. If the result is not a directory, an <code>ENOTDIR</code> error is returned. If the resolution of the symbolic link is successful and returns a directory, we set the current lookup directory to that directory, and go to the next component. Note that the resolution process here can involve recursion if the prefix (&#8216;dirname&#8217;) component of a pathname contains a filename that is a symbolic link that resolves to a directory (where the prefix component of that directory may contain a symbolic link, and so on). In order to protect the kernel against stack overflow, and also to protect against denial of service, there are limits on the maximum recursion depth, and on the maximum number of symbolic links followed. An <code>ELOOP</code> error is returned when the maximum is exceeded (&quot;Too many levels of symbolic links&quot;). </p>
<p> As currently implemented on Linux, the maximum number of symbolic links that will be followed while resolving a pathname is 40. In kernels before 2.6.18, the limit on the recursion depth was 5. Starting with Linux 2.6.18, this limit was raised to 8. In Linux 4.2, the kernel&#8217;s pathname-resolution code was reworked to eliminate the use of recursion, so that the only limit that remains is the maximum of 40 resolutions for the entire pathname. </p>
<p> The resolution of symbolic links during this stage can be blocked by using <code><a href="/docs/linux/man/2-openat2/">openat2</a></code>(2), with the <code>RESOLVE_NO_SYMLINKS</code> flag set.</p>
<h3>Step 3: find the final entry</h3>
<p>The lookup of the final component of the pathname goes just like that of all other components, as described in the previous step, with two differences: (i) the final component need not be a directory (at least as far as the path resolution process is concerned&#8212;it may have to be a directory, or a nondirectory, because of the requirements of the specific system call), and (ii) it is not necessarily an error if the component is not found&#8212;maybe we are just creating it. The details on the treatment of the final entry are described in the manual pages of the specific system calls.</p>
<h3>. and ..</h3>
<p>By convention, every directory has the entries &quot;.&quot; and &quot;..&quot;, which refer to the directory itself and to its parent directory, respectively. </p>
<p> The path resolution process will assume that these entries have their conventional meanings, regardless of whether they are actually present in the physical filesystem. </p>
<p> One cannot walk up past the root: &quot;/..&quot; is the same as &quot;/&quot;.</p>
<h3>Mount points</h3>
<p>After a &quot;mount dev path&quot; command, the pathname &quot;path&quot; refers to the root of the filesystem hierarchy on the device &quot;dev&quot;, and no longer to whatever it referred to earlier. </p>
<p> One can walk out of a mounted filesystem: &quot;path/..&quot; refers to the parent directory of &quot;path&quot;, outside of the filesystem hierarchy on &quot;dev&quot;. </p>
<p> Traversal of mount points can be blocked by using <code><a href="/docs/linux/man/2-openat2/">openat2</a></code>(2), with the <code>RESOLVE_NO_XDEV</code> flag set (though note that this also restricts bind mount traversal).</p>
<h3>Trailing slashes</h3>
<p>If a pathname ends in a &#8216;/&#8217;, that forces resolution of the preceding component as in Step 2: it has to exist and resolve to a directory. Otherwise, a trailing &#8216;/&#8217; is ignored. (Or, equivalently, a pathname with a trailing &#8216;/&#8217; is equivalent to the pathname obtained by appending &#8216;.&#8217; to it.)</p>
<h3>Final symlink</h3>
<p>If the last component of a pathname is a symbolic link, then it depends on the system call whether the file referred to will be the symbolic link or the result of path resolution on its contents. For example, the system call <code><a href="/docs/linux/man/2-lstat/">lstat</a></code>(2) will operate on the symlink, while <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) operates on the file pointed to by the symlink.</p>
<h3>Length limit</h3>
<p>There is a maximum length for pathnames. If the pathname (or some intermediate pathname obtained while resolving symbolic links) is too long, an <code>ENAMETOOLONG</code> error is returned (&quot;Filename too long&quot;).</p>
<h3>Empty pathname</h3>
<p>In the original UNIX, the empty pathname referred to the current directory. Nowadays POSIX decrees that an empty pathname must not be resolved successfully. Linux returns <code>ENOENT</code> in this case.</p>
<h3>Permissions</h3>
<p>The permission bits of a file consist of three groups of three bits; see <code><a href="/docs/linux/man/1-chmod/">chmod</a></code>(1) and <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2). The first group of three is used when the effective user ID of the calling process equals the owner ID of the file. The second group of three is used when the group ID of the file either equals the effective group ID of the calling process, or is one of the supplementary group IDs of the calling process (as set by <code><a href="/docs/linux/man/2-setgroups/">setgroups</a></code>(2)). When neither holds, the third group is used. </p>
<p> Of the three bits used, the first bit determines read permission, the second write permission, and the last execute permission in case of ordinary files, or search permission in case of directories. </p>
<p> Linux uses the fsuid instead of the effective user ID in permission checks. Ordinarily the fsuid will equal the effective user ID, but the fsuid can be changed by the system call <code><a href="/docs/linux/man/2-setfsuid/">setfsuid</a></code>(2). </p>
<p> (Here &quot;fsuid&quot; stands for something like &quot;filesystem user ID&quot;. The concept was required for the implementation of a user space NFS server at a time when processes could send a signal to a process with the same effective user ID. It is obsolete now. Nobody should use <code><a href="/docs/linux/man/2-setfsuid/">setfsuid</a></code>(2).) </p>
<p> Similarly, Linux uses the fsgid (&quot;filesystem group ID&quot;) instead of the effective group ID. See <code><a href="/docs/linux/man/2-setfsgid/">setfsgid</a></code>(2).</p>
<h3>Bypassing permission checks: superuser and capabilities</h3>
<p>On a traditional UNIX system, the superuser (<i>root</i>, user ID 0) is all-powerful, and bypasses all permissions restrictions when accessing files. </p>
<p> On Linux, superuser privileges are divided into capabilities (see <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7)). Two capabilities are relevant for file permissions checks: <code>CAP_DAC_OVERRIDE</code> and <code>CAP_DAC_READ_SEARCH</code>. (A process has these capabilities if its fsuid is 0.) </p>
<p> The <code>CAP_DAC_OVERRIDE</code> capability overrides all permission checking, but grants execute permission only when at least one of the file&#8217;s three execute permission bits is set. </p>
<p> The <code>CAP_DAC_READ_SEARCH</code> capability grants read and search permission on directories, and read permission on ordinary files.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-readlink/">readlink</a></code>(2), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7), <code><a href="/docs/linux/man/7-symlink/">symlink</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
