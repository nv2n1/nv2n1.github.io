---
title: "openat2(2)"
name: "openat2"
section: "2"
letter: "o"
url: "/docs/linux/man/2-openat2/"
description: "openat2 – open and possibly create a file (extended)"
---

<h2 class="name">NAME</h2>
<p> openat2 &#8211; open and possibly create a file (extended) </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;fcntl.h&gt;
#include &lt;linux/openat2.h&gt;
#include &lt;sys/stat.h&gt;
#include &lt;sys/types.h&gt;
long openat2(int dirfd, const char *pathname,
             struct open_how *how, size_t size);
</code></pre>
<p> <i>Note</i>: There is no glibc wrapper for this system call; see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> The <code>openat2</code>() system call is an extension of <code><a href="/docs/linux/man/2-openat/">openat</a></code>(2) and provides a superset of its functionality. </p>
<p> The <code>openat2</code>() system call opens the file specified by <i>pathname</i>. If the specified file does not exist, it may optionally (if <code>O_CREAT</code> is specified in <i>how.flags</i>) be created. </p>
<p> As with <code><a href="/docs/linux/man/2-openat/">openat</a></code>(2), if <i>pathname</i> is a relative pathname, then it is interpreted relative to the directory referred to by the file descriptor <i>dirfd</i> (or the current working directory of the calling process, if <i>dirfd</i> is the special value <code>AT_FDCWD</code>). If <i>pathname</i> is an absolute pathname, then <i>dirfd</i> is ignored (unless <i>how.resolve</i> contains <code>RESOLVE_IN_ROOT</code>, in which case <i>pathname</i> is resolved relative to <i>dirfd</i>). </p>
<p> Rather than taking a single <i>flags</i> argument, an extensible structure (<i>how</i>) is passed to allow for future extensions. The <i>size</i> argument must be specified as <i>sizeof(struct open_how)</i>.</p>
<h3>The open_how structure</h3>
<p> The <i>how</i> argument specifies how <i>pathname</i> should be opened, and acts as a superset of the <i>flags</i> and <i>mode</i> arguments to <code><a href="/docs/linux/man/2-openat/">openat</a></code>(2). This argument is a pointer to a structure of the following form: </p>
<p> struct open_how {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 flags;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;O_*&nbsp;flags&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 mode;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Mode for O_{CREAT,TMPFILE}&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 resolve;&nbsp;<wbr>&nbsp;/*&nbsp;RESOLVE_*&nbsp;flags&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;&#8230;&nbsp;*/ }; </p>
<p> Any future extensions to <code>openat2</code>() will be implemented as new fields appended to the above structure, with a zero value in a new field resulting in the kernel behaving as though that extension field was not present. Therefore, the caller <i>must</i> zero-fill this structure on initialization. (See the &quot;Extensibility&quot; section of the <code>NOTES</code> for more detail on why this is necessary.) </p>
<p> The fields of the <i>open_how</i> structure are as follows:</p>
<dl>
<dt><i>flags</i></p>
<dd> This field specifies the file creation and file status flags to use when opening the file. All of the <code>O_*</code> flags defined for <code><a href="/docs/linux/man/2-openat/">openat</a></code>(2) are valid <code>openat2</code>() flag values.</p>
<dt>
<dd> Whereas <code><a href="/docs/linux/man/2-openat/">openat</a></code>(2) ignores unknown bits in its <i>flags</i> argument, <code>openat2</code>() returns an error if unknown or conflicting flags are specified in <i>how.flags</i>.</p>
<dt><i>mode</i></p>
<dd> This field specifies the mode for the new file, with identical semantics to the <i>mode</i> argument of <code><a href="/docs/linux/man/2-openat/">openat</a></code>(2).</p>
<dt>
<dd> Whereas <code><a href="/docs/linux/man/2-openat/">openat</a></code>(2) ignores bits other than those in the range <i>07777</i> in its <i>mode</i> argument, <code>openat2</code>() returns an error if <i>how.mode</i> contains bits other than <i>07777</i>. Similarly, an error is returned if <code>openat2</code>() is called with a nonzero <i>how.mode</i> and <i>how.flags</i> does not contain <code>O_CREAT</code> or <code>O_TMPFILE</code>.</p>
<dt><i>resolve</i></p>
<dd> This is a bit-mask of flags that modify the way in which <code>all</code> components of <i>pathname</i> will be resolved. (See <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7) for background information.)</p>
<dt>
<dd> The primary use case for these flags is to allow trusted programs to restrict how untrusted paths (or paths inside untrusted directories) are resolved. The full list of <i>resolve</i> flags is as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>RESOLVE_BENEATH</code></p>
<dd> Do not permit the path resolution to succeed if any component of the resolution is not a descendant of the directory indicated by <i>dirfd</i>. This causes absolute symbolic links (and absolute values of <i>pathname</i>) to be rejected.</p>
<dt>
<dd> Currently, this flag also disables magic-link resolution (see below). However, this may change in the future. Therefore, to ensure that magic links are not resolved, the caller should explicitly specify <code>RESOLVE_NO_MAGICLINKS</code>.</p>
<dt><code>RESOLVE_IN_ROOT</code></p>
<dd> Treat the directory referred to by <i>dirfd</i> as the root directory while resolving <i>pathname</i>. Absolute symbolic links are interpreted relative to <i>dirfd</i>. If a prefix component of <i>pathname</i> equates to <i>dirfd</i>, then an immediately following <i>..</i> component likewise equates to <i>dirfd</i> (just as <i>/..</i> is traditionally equivalent to <i>/</i>). If <i>pathname</i> is an absolute path, it is also interpreted relative to <i>dirfd</i>.</p>
<dt>
<dd> The effect of this flag is as though the calling process had used <code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2) to (temporarily) modify its root directory (to the directory referred to by <i>dirfd</i>). However, unlike <code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2) (which changes the filesystem root permanently for a process), <code>RESOLVE_IN_ROOT</code> allows a program to efficiently restrict path resolution on a per-open basis.</p>
<dt>
<dd> Currently, this flag also disables magic-link resolution. However, this may change in the future. Therefore, to ensure that magic links are not resolved, the caller should explicitly specify <code>RESOLVE_NO_MAGICLINKS</code>.</p>
<dt><code>RESOLVE_NO_MAGICLINKS</code></p>
<dd> Disallow all magic-link resolution during path resolution.</p>
<dt>
<dd> Magic links are symbolic link-like objects that are most notably found in <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5); examples include <i>/proc/[pid]/exe</i> and <i>/proc/[pid]/fd/*</i>. (See <code><a href="/docs/linux/man/7-symlink/">symlink</a></code>(7) for more details.)</p>
<dt>
<dd> Unknowingly opening magic links can be risky for some applications. Examples of such risks include the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> If the process opening a pathname is a controlling process that currently has no controlling terminal (see <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7)), then opening a magic link inside <i>/proc/[pid]/fd</i> that happens to refer to a terminal would cause the process to acquire a controlling terminal.</p>
<dt>&bull;</p>
<dd> In a containerized environment, a magic link inside <i>/proc</i> may refer to an object outside the container, and thus may provide a means to escape from the container.</dl>
</dl>
<dt>
<dd> Because of such risks, an application may prefer to disable magic link resolution using the <code>RESOLVE_NO_MAGICLINKS</code> flag.</p>
<dt>
<dd> If the trailing component (i.e., basename) of <i>pathname</i> is a magic link, <i>how.resolve</i> contains <code>RESOLVE_NO_MAGICLINKS</code>, and <i>how.flags</i> contains both <code>O_PATH</code> and <code>O_NOFOLLOW</code>, then an <code>O_PATH</code> file descriptor referencing the magic link will be returned.</p>
<dt><code>RESOLVE_NO_SYMLINKS</code></p>
<dd> Disallow resolution of symbolic links during path resolution. This option implies <code>RESOLVE_NO_MAGICLINKS</code>.</p>
<dt>
<dd> If the trailing component (i.e., basename) of <i>pathname</i> is a symbolic link, <i>how.resolve</i> contains <code>RESOLVE_NO_SYMLINKS</code>, and <i>how.flags</i> contains both <code>O_PATH</code> and <code>O_NOFOLLOW</code>, then an <code>O_PATH</code> file descriptor referencing the symbolic link will be returned.</p>
<dt>
<dd> Note that the effect of the <code>RESOLVE_NO_SYMLINKS</code> flag, which affects the treatment of symbolic links in all of the components of <i>pathname</i>, differs from the effect of the <code>O_NOFOLLOW</code> file creation flag (in <i>how.flags</i>), which affects the handling of symbolic links only in the final component of <i>pathname</i>.</p>
<dt>
<dd> Applications that employ the <code>RESOLVE_NO_SYMLINKS</code> flag are encouraged to make its use configurable (unless it is used for a specific security purpose), as symbolic links are very widely used by end-users. Setting this flag indiscriminately&#8212;i.e., for purposes not specifically related to security&#8212;for all uses of <code>openat2</code>() may result in spurious errors on previously functional systems. This may occur if, for example, a system pathname that is used by an application is modified (e.g., in a new distribution release) so that a pathname component (now) contains a symbolic link.</p>
<dt><code>RESOLVE_NO_XDEV</code></p>
<dd> Disallow traversal of mount points during path resolution (including all bind mounts). Consequently, <i>pathname</i> must either be on the same mount as the directory referred to by <i>dirfd</i>, or on the same mount as the current working directory if <i>dirfd</i> is specified as <code>AT_FDCWD</code>.</p>
<dt>
<dd> Applications that employ the <code>RESOLVE_NO_XDEV</code> flag are encouraged to make its use configurable (unless it is used for a specific security purpose), as bind mounts are widely used by end-users. Setting this flag indiscriminately&#8212;i.e., for purposes not specifically related to security&#8212;for all uses of <code>openat2</code>() may result in spurious errors on previously functional systems. This may occur if, for example, a system pathname that is used by an application is modified (e.g., in a new distribution release) so that a pathname component (now) contains a bind mount.</dl>
</dl>
<dt>
<dd> If any bits other than those listed above are set in <i>how.resolve</i>, an error is returned.</dl>
<h2>RETURN VALUE</h2>
<p> On success, a new file descriptor is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<p> The set of errors returned by <code>openat2</code>() includes all of the errors returned by <code><a href="/docs/linux/man/2-openat/">openat</a></code>(2), as well as the following additional errors:</p>
<dl>
<dt><code>E2BIG</code></p>
<dd> An extension that this kernel does not support was specified in <i>how</i>. (See the &quot;Extensibility&quot; section of <code>NOTES</code> for more detail on how extensions are handled.)</p>
<dt><code>EAGAIN</code></p>
<dd> <i>how.resolve</i> contains either <code>RESOLVE_IN_ROOT</code> or <code>RESOLVE_BENEATH</code>, and the kernel could not ensure that a &quot;..&quot; component didn&#8217;t escape (due to a race condition or potential attack). The caller may choose to retry the <code>openat2</code>() call.</p>
<dt><code>EINVAL</code></p>
<dd> An unknown flag or invalid value was specified in <i>how</i>.</p>
<dt><code>EINVAL</code></p>
<dd> <i>mode</i> is nonzero, but <i>how.flags</i> does not contain <code>O_CREAT</code> or <code>O_TMPFILE</code>.</p>
<dt><code>EINVAL</code></p>
<dd> <i>size</i> was smaller than any known version of <i>struct open_how</i>.</p>
<dt><code>ELOOP</code></p>
<dd> <i>how.resolve</i> contains <code>RESOLVE_NO_SYMLINKS</code>, and one of the path components was a symbolic link (or magic link).</p>
<dt><code>ELOOP</code></p>
<dd> <i>how.resolve</i> contains <code>RESOLVE_NO_MAGICLINKS</code>, and one of the path components was a magic link.</p>
<dt><code>EXDEV</code></p>
<dd> <i>how.resolve</i> contains either <code>RESOLVE_IN_ROOT</code> or <code>RESOLVE_BENEATH</code>, and an escape from the root during path resolution was detected.</p>
<dt><code>EXDEV</code></p>
<dd> <i>how.resolve</i> contains <code>RESOLVE_NO_XDEV</code>, and a path component crosses a mount point.</dl>
<h2>VERSIONS</h2>
<p> <code>openat2</code>() first appeared in Linux 5.6.</p>
<h2>CONFORMING TO</h2>
<p> This system call is Linux-specific. </p>
<p> The semantics of <code>RESOLVE_BENEATH</code> were modeled after FreeBSD&#8217;s <code>O_BENEATH</code>.</p>
<h2>NOTES</h2>
<p> Glibc does not provide a wrapper for this system call; call it using <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2).</p>
<h3>Extensibility</h3>
<p> In order to allow for future extensibility, <code>openat2</code>() requires the user-space application to specify the size of the <i>open_how</i> structure that it is passing. By providing this information, it is possible for <code>openat2</code>() to provide both forwards- and backwards-compatibility, with <i>size</i> acting as an implicit version number. (Because new extension fields will always be appended, the structure size will always increase.) This extensibility design is very similar to other system calls such as <code><a href="/docs/linux/man/2-sched_setattr/">sched_setattr</a></code>(2), <code><a href="/docs/linux/man/2-perf_event_open/">perf_event_open</a></code>(2), and <code><a href="/docs/linux/man/2-clone3/">clone3</a></code>(2). </p>
<p> If we let <i>usize</i> be the size of the structure as specified by the user-space application, and <i>ksize</i> be the size of the structure which the kernel supports, then there are three cases to consider:</p>
<dl>
<dt>&bull;</p>
<dd> If <i>ksize</i> equals <i>usize</i>, then there is no version mismatch and <i>how</i> can be used verbatim.</p>
<dt>&bull;</p>
<dd> If <i>ksize</i> is larger than <i>usize</i>, then there are some extension fields that the kernel supports which the user-space application is unaware of. Because a zero value in any added extension field signifies a no-op, the kernel treats all of the extension fields not provided by the user-space application as having zero values. This provides backwards-compatibility.</p>
<dt>&bull;</p>
<dd> If <i>ksize</i> is smaller than <i>usize</i>, then there are some extension fields which the user-space application is aware of but which the kernel does not support. Because any extension field must have its zero values signify a no-op, the kernel can safely ignore the unsupported extension fields if they are all-zero. If any unsupported extension fields are nonzero, then -1 is returned and <i>errno</i> is set to <code>E2BIG</code>. This provides forwards-compatibility.</dl>
<p> Because the definition of <i>struct open_how</i> may change in the future (with new fields being added when system headers are updated), user-space applications should zero-fill <i>struct open_how</i> to ensure that recompiling the program with new headers will not result in spurious errors at runtime. The simplest way is to use a designated initializer: </p>
<p> struct open_how how = { .flags = O_RDWR,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.resolve&nbsp;=&nbsp;RESOLVE_IN_ROOT&nbsp;}; </p>
<p> or explicitly using <code><a href="/docs/linux/man/3-memset/">memset</a></code>(3) or similar: </p>
<p> struct open_how how; memset(&amp;how, 0, sizeof(how)); how.flags = O_RDWR; how.resolve = RESOLVE_IN_ROOT; </p>
<p> A user-space application that wishes to determine which extensions the running kernel supports can do so by conducting a binary search on <i>size</i> with a structure which has every byte nonzero (to find the largest value which doesn&#8217;t produce an error of <code>E2BIG</code>).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-openat/">openat</a></code>(2), <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7), <code><a href="/docs/linux/man/7-symlink/">symlink</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
