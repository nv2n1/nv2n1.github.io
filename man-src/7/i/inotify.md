---
title: "inotify(7)"
name: "inotify"
section: "7"
letter: "i"
url: "/docs/linux/man/7-inotify/"
description: "inotify – monitoring filesystem events"
---

<p>inotify &#8211; monitoring filesystem events</p>
<h2>Description</h2>
<p>The <i>inotify</i> API provides a mechanism for monitoring filesystem events. Inotify can be used to monitor individual files, or to monitor directories. When a directory is monitored, inotify will return events for the directory itself, and for files inside the directory. The following system calls are used with this API:</p>
<dl>
<dt>*</dt>
<dd><code><a href="/docs/linux/man/2-inotify_init/">inotify_init</a></code>(2) creates an inotify instance and returns a file descriptor referring to the inotify instance. The more recent <code><a href="/docs/linux/man/2-inotify_init1/">inotify_init1</a></code>(2) is like <code><a href="/docs/linux/man/2-inotify_init/">inotify_init</a></code>(2), but has a <i>flags</i> argument that provides access to some extra functionality.</dd>
<dt>*</dt>
<dd><code><a href="/docs/linux/man/2-inotify_add_watch/">inotify_add_watch</a></code>(2) manipulates the &quot;watch list&quot; associated with an inotify instance. Each item (&quot;watch&quot;) in the watch list specifies the pathname of a file or directory, along with some set of events that the kernel should monitor for the file referred to by that pathname. <code><a href="/docs/linux/man/2-inotify_add_watch/">inotify_add_watch</a></code>(2) either creates a new watch item, or modifies an existing watch. Each watch has a unique &quot;watch descriptor&quot;, an integer returned by <code><a href="/docs/linux/man/2-inotify_add_watch/">inotify_add_watch</a></code>(2) when the watch is created.</dd>
<dt>*</dt>
<dd>When events occur for monitored files and directories, those events are made available to the application as structured data that can be read from the inotify file descriptor using <code><a href="/docs/linux/man/2-read/">read</a></code>(2) (see below).</dd>
<dt>*</dt>
<dd><code><a href="/docs/linux/man/2-inotify_rm_watch/">inotify_rm_watch</a></code>(2) removes an item from an inotify watch list.</dd>
<dt>*</dt>
<dd>When all file descriptors referring to an inotify instance have been closed (using <code><a href="/docs/linux/man/2-close/">close</a></code>(2)), the underlying object and its resources are freed for reuse by the kernel; all associated watches are automatically freed.</dd></dl>
<p> With careful programming, an application can use inotify to efficiently monitor and cache the state of a set of filesystem objects. However, robust applications should allow for the fact that bugs in the monitoring logic or races of the kind described below may leave the cache inconsistent with the filesystem state. It is probably wise to do some consistency checking, and rebuild the cache when inconsistencies are detected.</p>
<h3>Reading events from an inotify file descriptor</h3>
<p>To determine what events have occurred, an application <code><a href="/docs/linux/man/2-read/">read</a></code>(2)s from the inotify file descriptor. If no events have so far occurred, then, assuming a blocking file descriptor, <code><a href="/docs/linux/man/2-read/">read</a></code>(2) will block until at least one event occurs (unless interrupted by a signal, in which case the call fails with the error <code>EINTR</code>; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)). Each successful <code><a href="/docs/linux/man/2-read/">read</a></code>(2) returns a buffer containing one or more of the following structures: </p>
<pre><code>struct inotify_event {
    int wd; /* Watch descriptor */
    uint32_t mask;   /* Mask describing event */
    uint32_t cookie; /* Unique cookie associating related
                        events (for rename(2)) */
    uint32_t len;    /* Size of name field */
    char name[];     /* Optional null-terminated name */
};</code></pre>
<p> <i>wd</i> identifies the watch for which this event occurs. It is one of the watch descriptors returned by a previous call to <code><a href="/docs/linux/man/2-inotify_add_watch/">inotify_add_watch</a></code>(2). <i>mask</i> contains bits that describe the event that occurred (see below). <i>cookie</i> is a unique integer that connects related events. Currently, this is used only for rename events, and allows the resulting pair of <code>IN_MOVED_FROM</code> and <code>IN_MOVED_TO</code> events to be connected by the application. For all other event types, <i>cookie</i> is set to 0. The <i>name</i> field is present only when an event is returned for a file inside a watched directory; it identifies the filename within the watched directory. This filename is null-terminated, and may include further null bytes (&#8216;\0&#8217;) to align subsequent reads to a suitable address boundary. </p>
<p> The <i>len</i> field counts all of the bytes in <i>name</i>, including the null bytes; the length of each <i>inotify_event</i> structure is thus <i>sizeof(struct inotify_event)+len</i>. </p>
<p> The behavior when the buffer given to <code><a href="/docs/linux/man/2-read/">read</a></code>(2) is too small to return information about the next event depends on the kernel version: in kernels before 2.6.21, <code><a href="/docs/linux/man/2-read/">read</a></code>(2) returns 0; since kernel 2.6.21, <code><a href="/docs/linux/man/2-read/">read</a></code>(2) fails with the error <code>EINVAL</code>. Specifying a buffer of size </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sizeof(struct inotify_event)&nbsp;+&nbsp;NAME_MAX&nbsp;+&nbsp;1 </p>
<p> will be sufficient to read at least one event.  </p>
<h3>inotify events</h3>
<p> The <code><a href="/docs/linux/man/2-inotify_add_watch/">inotify_add_watch</a></code>(2) <i>mask</i> argument and the <i>mask</i> field of the <i>inotify_event</i> structure returned when <code><a href="/docs/linux/man/2-read/">read</a></code>(2)ing an inotify file descriptor are both bit masks identifying inotify events. The following bits can be specified in <i>mask</i> when calling <code><a href="/docs/linux/man/2-inotify_add_watch/">inotify_add_watch</a></code>(2) and may be returned in the <i>mask</i> field returned by <code><a href="/docs/linux/man/2-read/">read</a></code>(2): </p>
<dl>
<dd>  </dd>
<dl>
<dt><code>IN_ACCESS</code> (+) </dt>
<dd> <p> File was accessed (e.g., <code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2)). </p>
 </dd>
<dt><code>IN_ATTRIB</code> (*) </dt>
<dd> <p> Metadata changed---for example, permissions (e.g., <code><a href="/docs/linux/man/2-chmod/">chmod</a></code>(2)), timestamps (e.g., <code><a href="/docs/linux/man/2-utimensat/">utimensat</a></code>(2)), extended attributes (<code><a href="/docs/linux/man/2-setxattr/">setxattr</a></code>(2)), link count (since Linux 2.6.25; e.g., for the target of <code><a href="/docs/linux/man/2-link/">link</a></code>(2) and for <code><a href="/docs/linux/man/2-unlink/">unlink</a></code>(2)), and user/group ID (e.g., <code><a href="/docs/linux/man/2-chown/">chown</a></code>(2)). </p>
 </dd>
<dt><code>IN_CLOSE_WRITE</code> (+) </dt>
<dd> <p> File opened for writing was closed. </p>
 </dd>
<dt><code>IN_CLOSE_NOWRITE</code> (*) </dt>
<dd> <p> File or directory not opened for writing was closed. </p>
 </dd>
<dt><code>IN_CREATE</code> (+) </dt>
<dd> <p> File/directory created in watched directory (e.g., <code><a href="/docs/linux/man/2-open/">open</a></code>(2) <code>O_CREAT</code>, <code><a href="/docs/linux/man/2-mkdir/">mkdir</a></code>(2), <code><a href="/docs/linux/man/2-link/">link</a></code>(2), <code><a href="/docs/linux/man/2-symlink/">symlink</a></code>(2), <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2) on a UNIX domain socket). </p>
 </dd>
<dt><code>IN_DELETE</code> (+) </dt>
<dd> <p> File/directory deleted from watched directory. </p>
 </dd>
<dt><code>IN_DELETE_SELF</code></dt>
<dd> <p> Watched file/directory was itself deleted. (This event also occurs if an object is moved to another filesystem, since <code><a href="/docs/linux/man/1-mv/">mv</a></code>(1) in effect copies the file to the other filesystem and then deletes it from the original filesystem.) In addition, an <code>IN_IGNORED</code> event will subsequently be generated for the watch descriptor. </p>
 </dd>
<dt><code>IN_MODIFY</code> (+) </dt>
<dd> <p> File was modified (e.g., <code><a href="/docs/linux/man/2-write/">write</a></code>(2), <code><a href="/docs/linux/man/2-truncate/">truncate</a></code>(2)). </p>
 </dd>
<dt><code>IN_MOVE_SELF</code></dt>
<dd> <p> Watched file/directory was itself moved. </p>
 </dd>
<dt><code>IN_MOVED_FROM</code> (+) </dt>
<dd> <p> Generated for the directory containing the old filename when a file is renamed. </p>
 </dd>
<dt><code>IN_MOVED_TO</code> (+) </dt>
<dd> <p> Generated for the directory containing the new filename when a file is renamed. </p>
 </dd>
<dt><code>IN_OPEN</code> (*) </dt>
<dd> <p> File or directory was opened. </p>
 </dd></dl>
</dl>
<p> Inotify monitoring is inode-based: when monitoring a file (but not when monitoring the directory containing a file), an event can be generated for activity on any link to the file (in the same or a different directory). </p>
<p> When monitoring a directory: </p>
<dl>
<dt>*</dt>
<dd> <p> the events marked above with an asterisk (*) can occur both for the directory itself and for objects inside the directory; and </p>
 </dd>
<dt>*</dt>
<dd> <p> the events marked with a plus sign (+) occur only for objects inside the directory (not for the directory itself). </p>
 </dd></dl>
<p> <i>Note</i>: when monitoring a directory, events are not generated for the files inside the directory when the events are performed via a pathname (i.e., a link) that lies outside the monitored directory. </p>
<p> When events are generated for objects inside a watched directory, the <i>name</i> field in the returned <i>inotify_event</i> structure identifies the name of the file within the directory. </p>
<p> The <code>IN_ALL_EVENTS</code> macro is defined as a bit mask of all of the above events. This macro can be used as the <i>mask</i> argument when calling <code><a href="/docs/linux/man/2-inotify_add_watch/">inotify_add_watch</a></code>(2). </p>
<p> Two additional convenience macros are defined: </p>
<dl>
<dd>  </dd>
<dl>
<dt><code>IN_MOVE</code></dt>
<dd> <p> Equates to <code>IN_MOVED_FROM | IN_MOVED_TO</code>. </p>
 </dd>
<dt><code>IN_CLOSE</code></dt>
<dd> <p> Equates to <code>IN_CLOSE_WRITE | IN_CLOSE_NOWRITE</code>. </p>
 </dd></dl>
</dl>
<p> The following further bits can be specified in <i>mask</i> when calling <code><a href="/docs/linux/man/2-inotify_add_watch/">inotify_add_watch</a></code>(2): </p>
<dl>
<dd>  </dd>
<dl>
<dt><code>IN_DONT_FOLLOW</code> (since Linux 2.6.15) </dt>
<dd> <p> Don&#8217;t dereference <i>pathname</i> if it is a symbolic link. </p>
 </dd>
<dt><code>IN_EXCL_UNLINK</code> (since Linux 2.6.36) </dt>
<dd> <p> By default, when watching events on the children of a directory, events are generated for children even after they have been unlinked from the directory. This can result in large numbers of uninteresting events for some applications (e.g., if watching <i>/tmp</i>, in which many applications create temporary files whose names are immediately unlinked). Specifying <code>IN_EXCL_UNLINK</code> changes the default behavior, so that events are not generated for children after they have been unlinked from the watched directory. </p>
 </dd>
<dt><code>IN_MASK_ADD</code></dt>
<dd> <p> If a watch instance already exists for the filesystem object corresponding to <i>pathname</i>, add (OR) the events in <i>mask</i> to the watch mask (instead of replacing the mask); the error <code>EINVAL</code> results if <code>IN_MASK_CREATE</code> is also specified. </p>
 </dd>
<dt><code>IN_ONESHOT</code></dt>
<dd> <p> Monitor the filesystem object corresponding to <i>pathname</i> for one event, then remove from watch list. </p>
 </dd>
<dt><code>IN_ONLYDIR</code> (since Linux 2.6.15) </dt>
<dd> <p> Watch <i>pathname</i> only if it is a directory; the error <code>ENOTDIR</code> results if <i>pathname</i> is not a directory. Using this flag provides an application with a race-free way of ensuring that the monitored object is a directory. </p>
 </dd>
<dt><code>IN_MASK_CREATE</code> (since Linux 4.18) </dt>
<dd> <p> Watch <i>pathname</i> only if it does not already have a watch associated with it; the error <code>EEXIST</code> results if <i>pathname</i> is already being watched. </p>
 </dd>
<dd> <p> Using this flag provides an application with a way of ensuring that new watches do not modify existing ones. This is useful because multiple paths may refer to the same inode, and multiple calls to <code><a href="/docs/linux/man/2-inotify_add_watch/">inotify_add_watch</a></code>(2) without this flag may clobber existing watch masks. </p>
 </dd></dl>
</dl>
<p> The following bits may be set in the <i>mask</i> field returned by <code><a href="/docs/linux/man/2-read/">read</a></code>(2): </p>
<dl>
<dd>  </dd>
<dl>
<dt><code>IN_IGNORED</code></dt>
<dd> <p> Watch was removed explicitly (<code><a href="/docs/linux/man/2-inotify_rm_watch/">inotify_rm_watch</a></code>(2)) or automatically (file was deleted, or filesystem was unmounted). See also BUGS. </p>
 </dd>
<dt><code>IN_ISDIR</code></dt>
<dd> <p> Subject of this event is a directory. </p>
 </dd>
<dt><code>IN_Q_OVERFLOW</code></dt>
<dd> <p> Event queue overflowed (<i>wd</i> is -1 for this event). </p>
 </dd>
<dt><code>IN_UNMOUNT</code></dt>
<dd> <p> Filesystem containing watched object was unmounted. In addition, an <code>IN_IGNORED</code> event will subsequently be generated for the watch descriptor. </p>
 </dd></dl>
</dl>
<h3>Examples</h3>
<p> Suppose an application is watching the directory <i>dir</i> and the file <i>dir/myfile</i> for all events. The examples below show some events that will be generated for these two objects. </p>
<dl>
<dd>  </dd>
<dl>
<dt>fd = open(&quot;dir/myfile&quot;, O_RDWR);</dt>
<dd> <p> Generates <code>IN_OPEN</code> events for both <i>dir</i> and <i>dir/myfile</i>. </p>
 </dd>
<dt>read(fd, buf, count);</dt>
<dd> <p> Generates <code>IN_ACCESS</code> events for both <i>dir</i> and <i>dir/myfile</i>. </p>
 </dd>
<dt>write(fd, buf, count);</dt>
<dd> <p> Generates <code>IN_MODIFY</code> events for both <i>dir</i> and <i>dir/myfile</i>. </p>
 </dd>
<dt>fchmod(fd, mode);</dt>
<dd> <p> Generates <code>IN_ATTRIB</code> events for both <i>dir</i> and <i>dir/myfile</i>. </p>
 </dd>
<dt>close(fd);</dt>
<dd> <p> Generates <code>IN_CLOSE_WRITE</code> events for both <i>dir</i> and <i>dir/myfile</i>. </p>
 </dd></dl>
</dl>
<p> Suppose an application is watching the directories <i>dir1</i> and <i>dir2</i>, and the file <i>dir1/myfile</i>. The following examples show some events that may be generated. </p>
<dl>
<dd>  </dd>
<dl>
<dt>link(&quot;dir1/myfile&quot;, &quot;dir2/new&quot;);</dt>
<dd> <p> Generates an <code>IN_ATTRIB</code> event for <i>myfile</i> and an <code>IN_CREATE</code> event for <i>dir2</i>. </p>
 </dd>
<dt>rename(&quot;dir1/myfile&quot;, &quot;dir2/myfile&quot;);</dt>
<dd> <p> Generates an <code>IN_MOVED_FROM</code> event for <i>dir1</i>, an <code>IN_MOVED_TO</code> event for <i>dir2</i>, and an <code>IN_MOVE_SELF</code> event for <i>myfile</i>. The <code>IN_MOVED_FROM</code> and <code>IN_MOVED_TO</code> events will have the same <i>cookie</i> value. </p>
 </dd></dl>
</dl>
<p> Suppose that <i>dir1/xx</i> and <i>dir2/yy</i> are (the only) links to the same file, and an application is watching <i>dir1</i>, <i>dir2</i>, <i>dir1/xx</i>, and <i>dir2/yy</i>. Executing the following calls in the order given below will generate the following events: </p>
<dl>
<dd>  </dd>
<dl>
<dt>unlink(&quot;dir2/yy&quot;);</dt>
<dd> <p> Generates an <code>IN_ATTRIB</code> event for <i>xx</i> (because its link count changes) and an <code>IN_DELETE</code> event for <i>dir2</i>. </p>
 </dd>
<dt>unlink(&quot;dir1/xx&quot;);</dt>
<dd> <p> Generates <code>IN_ATTRIB</code>, <code>IN_DELETE_SELF</code>, and <code>IN_IGNORED</code> events for <i>xx</i>, and an <code>IN_DELETE</code> event for <i>dir1</i>. </p>
 </dd></dl>
</dl>
<p> Suppose an application is watching the directory <i>dir</i> and (the empty) directory <i>dir/subdir</i>. The following examples show some events that may be generated. </p>
<dl>
<dd>  </dd>
<dl>
<dt>mkdir(&quot;dir/new&quot;, mode);</dt>
<dd> <p> Generates an <code>IN_CREATE | IN_ISDIR</code> event for <i>dir</i>. </p>
 </dd>
<dt>rmdir(&quot;dir/subdir&quot;);</dt>
<dd> <p> Generates <code>IN_DELETE_SELF</code> and <code>IN_IGNORED</code> events for <i>subdir</i>, and an <code>IN_DELETE | IN_ISDIR</code> event for <i>dir</i>. </p>
 </dd></dl>
</dl>
<h3>/proc interfaces</h3>
<p> The following interfaces can be used to limit the amount of kernel memory consumed by inotify: </p>
<dl>
<dt><i>/proc/sys/fs/inotify/max_queued_events</i></dt>
<dd> <p> The value in this file is used when an application calls <code><a href="/docs/linux/man/2-inotify_init/">inotify_init</a></code>(2) to set an upper limit on the number of events that can be queued to the corresponding inotify instance. Events in excess of this limit are dropped, but an <code>IN_Q_OVERFLOW</code> event is always generated. </p>
 </dd>
<dt><i>/proc/sys/fs/inotify/max_user_instances</i></dt>
<dd> <p> This specifies an upper limit on the number of inotify instances that can be created per real user ID. </p>
 </dd>
<dt><i>/proc/sys/fs/inotify/max_user_watches</i></dt>
<dd> <p> This specifies an upper limit on the number of watches that can be created per real user ID. </p>
 </dd></dl>
<h2>VERSIONS</h2>
<p> Inotify was merged into the 2.6.13 Linux kernel. The required library interfaces were added to glibc in version 2.4. (<code>IN_DONT_FOLLOW</code>, <code>IN_MASK_ADD</code>, and <code>IN_ONLYDIR</code> were added in glibc version 2.5.)  </p>
<h2>CONFORMING TO</h2>
<p> The inotify API is Linux-specific.  </p>
<h2>NOTES</h2>
<p> Inotify file descriptors can be monitored using <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), and <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7). When an event is available, the file descriptor indicates as readable. </p>
<p> Since Linux 2.6.25, signal-driven I/O notification is available for inotify file descriptors; see the discussion of <code>F_SETFL</code> (for setting the <code>O_ASYNC</code> flag), <code>F_SETOWN</code>, and <code>F_SETSIG</code> in <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2). The <i>siginfo_t</i> structure (described in <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2)) that is passed to the signal handler has the following fields set: <i>si_fd</i> is set to the inotify file descriptor number; <i>si_signo</i> is set to the signal number; <i>si_code</i> is set to <code>POLL_IN</code>; and <code>POLLIN</code> is set in <i>si_band</i>. </p>
<p> If successive output inotify events produced on the inotify file descriptor are identical (same <i>wd</i>, <i>mask</i>, <i>cookie</i>, and <i>name</i>), then they are coalesced into a single event if the older event has not yet been read (but see BUGS). This reduces the amount of kernel memory required for the event queue, but also means that an application can&#8217;t use inotify to reliably count file events. </p>
<p> The events returned by reading from an inotify file descriptor form an ordered queue. Thus, for example, it is guaranteed that when renaming from one directory to another, events will be produced in the correct order on the inotify file descriptor. </p>
<p> The set of watch descriptors that is being monitored via an inotify file descriptor can be viewed via the entry for the inotify file descriptor in the process&#8217;s <i>/proc/[pid]/fdinfo</i> directory. See <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5) for further details. The <code>FIONREAD</code> <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) returns the number of bytes available to read from an inotify file descriptor.  </p>
<h3>Limitations and caveats</h3>
<p> The inotify API provides no information about the user or process that triggered the inotify event. In particular, there is no easy way for a process that is monitoring events via inotify to distinguish events that it triggers itself from those that are triggered by other processes. </p>
<p> Inotify reports only events that a user-space program triggers through the filesystem API. As a result, it does not catch remote events that occur on network filesystems. (Applications must fall back to polling the filesystem to catch such events.) Furthermore, various pseudo-filesystems such as <i>/proc</i>, <i>/sys</i>, and <i>/dev/pts</i> are not monitorable with inotify. </p>
<p> The inotify API does not report file accesses and modifications that may occur because of <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-msync/">msync</a></code>(2), and <code><a href="/docs/linux/man/2-munmap/">munmap</a></code>(2). </p>
<p> The inotify API identifies affected files by filename. However, by the time an application processes an inotify event, the filename may already have been deleted or renamed. </p>
<p> The inotify API identifies events via watch descriptors. It is the application&#8217;s responsibility to cache a mapping (if one is needed) between watch descriptors and pathnames. Be aware that directory renamings may affect multiple cached pathnames. </p>
<p> Inotify monitoring of directories is not recursive: to monitor subdirectories under a directory, additional watches must be created. This can take a significant amount time for large directory trees. </p>
<p> If monitoring an entire directory subtree, and a new subdirectory is created in that tree or an existing directory is renamed into that tree, be aware that by the time you create a watch for the new subdirectory, new files (and subdirectories) may already exist inside the subdirectory. Therefore, you may want to scan the contents of the subdirectory immediately after adding the watch (and, if desired, recursively add watches for any subdirectories that it contains). </p>
<p> Note that the event queue can overflow. In this case, events are lost. Robust applications should handle the possibility of lost events gracefully. For example, it may be necessary to rebuild part or all of the application cache. (One simple, but possibly expensive, approach is to close the inotify file descriptor, empty the cache, create a new inotify file descriptor, and then re-create watches and cache entries for the objects to be monitored.) </p>
<p> If a filesystem is mounted on top of a monitored directory, no event is generated, and no events are generated for objects immediately under the new mount point. If the filesystem is subsequently unmounted, events will subsequently be generated for the directory and the objects it contains.  </p>
<h3>Dealing with rename() events</h3>
<p> As noted above, the <code>IN_MOVED_FROM</code> and <code>IN_MOVED_TO</code> event pair that is generated by <code><a href="/docs/linux/man/2-rename/">rename</a></code>(2) can be matched up via their shared cookie value. However, the task of matching has some challenges. </p>
<p> These two events are usually consecutive in the event stream available when reading from the inotify file descriptor. However, this is not guaranteed. If multiple processes are triggering events for monitored objects, then (on rare occasions) an arbitrary number of other events may appear between the <code>IN_MOVED_FROM</code> and <code>IN_MOVED_TO</code> events. Furthermore, it is not guaranteed that the event pair is atomically inserted into the queue: there may be a brief interval where the <code>IN_MOVED_FROM</code> has appeared, but the <code>IN_MOVED_TO</code> has not. </p>
<p> Matching up the <code>IN_MOVED_FROM</code> and <code>IN_MOVED_TO</code> event pair generated by <code><a href="/docs/linux/man/2-rename/">rename</a></code>(2) is thus inherently racy. (Don&#8217;t forget that if an object is renamed outside of a monitored directory, there may not even be an <code>IN_MOVED_TO</code> event.) Heuristic approaches (e.g., assume the events are always consecutive) can be used to ensure a match in most cases, but will inevitably miss some cases, causing the application to perceive the <code>IN_MOVED_FROM</code> and <code>IN_MOVED_TO</code> events as being unrelated. If watch descriptors are destroyed and re-created as a result, then those watch descriptors will be inconsistent with the watch descriptors in any pending events. (Re-creating the inotify file descriptor and rebuilding the cache may be useful to deal with this scenario.) </p>
<p> Applications should also allow for the possibility that the <code>IN_MOVED_FROM</code> event was the last event that could fit in the buffer returned by the current call to <code><a href="/docs/linux/man/2-read/">read</a></code>(2), and the accompanying <code>IN_MOVED_TO</code> event might be fetched only on the next <code><a href="/docs/linux/man/2-read/">read</a></code>(2), which should be done with a (small) timeout to allow for the fact that insertion of the <code>IN_MOVED_FROM</code>-<code>IN_MOVED_TO</code> event pair is not atomic, and also the possibility that there may not be any <code>IN_MOVED_TO</code> event.  </p>
<h2>BUGS</h2>
<p> Before Linux 3.19, <code><a href="/docs/linux/man/2-fallocate/">fallocate</a></code>(2) did not create any inotify events. Since Linux 3.19, calls to <code><a href="/docs/linux/man/2-fallocate/">fallocate</a></code>(2) generate <code>IN_MODIFY</code> events. </p>
<p> In kernels before 2.6.16, the <code>IN_ONESHOT</code> <i>mask</i> flag does not work. </p>
<p> As originally designed and implemented, the <code>IN_ONESHOT</code> flag did not cause an <code>IN_IGNORED</code> event to be generated when the watch was dropped after one event. However, as an unintended effect of other changes, since Linux 2.6.36, an <code>IN_IGNORED</code> event is generated in this case. </p>
<p> Before kernel 2.6.25, the kernel code that was intended to coalesce successive identical events (i.e., the two most recent events could potentially be coalesced if the older had not yet been read) instead checked if the most recent event could be coalesced with the <i>oldest</i> unread event. </p>
<p> When a watch descriptor is removed by calling <code><a href="/docs/linux/man/2-inotify_rm_watch/">inotify_rm_watch</a></code>(2) (or because a watch file is deleted or the filesystem that contains it is unmounted), any pending unread events for that watch descriptor remain available to read. As watch descriptors are subsequently allocated with <code><a href="/docs/linux/man/2-inotify_add_watch/">inotify_add_watch</a></code>(2), the kernel cycles through the range of possible watch descriptors (0 to <code>INT_MAX</code>) incrementally. When allocating a free watch descriptor, no check is made to see whether that watch descriptor number has any pending unread events in the inotify queue. Thus, it can happen that a watch descriptor is reallocated even when pending unread events exist for a previous incarnation of that watch descriptor number, with the result that the application might then read those events and interpret them as belonging to the file associated with the newly recycled watch descriptor. In practice, the likelihood of hitting this bug may be extremely low, since it requires that an application cycle through <code>INT_MAX</code> watch descriptors, release a watch descriptor while leaving unread events for that watch descriptor in the queue, and then recycle that watch descriptor. For this reason, and because there have been no reports of the bug occurring in real-world applications, as of Linux 3.15, no kernel changes have yet been made to eliminate this possible bug.  </p>
<h2>EXAMPLES</h2>
<p> The following program demonstrates the usage of the inotify API. It marks the directories passed as a command-line arguments and waits for events of type <code>IN_OPEN</code>, <code>IN_CLOSE_NOWRITE</code>, and <code>IN_CLOSE_WRITE</code>. </p>
<p> The following output was recorded while editing the file <i>/home/user/temp/foo</i> and listing directory <i>/tmp</i>. Before the file and the directory were opened, <code>IN_OPEN</code> events occurred. After the file was closed, an <code>IN_CLOSE_WRITE</code> event occurred. After the directory was closed, an <code>IN_CLOSE_NOWRITE</code> event occurred. Execution of the program ended when the user pressed the ENTER key.  </p>
<h3>Example output</h3>
<p> $ <code>./a.out /tmp /home/user/temp</code> Press enter key to terminate. Listening for events. IN_OPEN: /home/user/temp/foo [file] IN_CLOSE_WRITE: /home/user/temp/foo [file] IN_OPEN: /tmp/ [directory] IN_CLOSE_NOWRITE: /tmp/ [directory] </p>
<p> Listening for events stopped.  </p>
<h3>Program source</h3>
<p> #include &lt;errno.h&gt; #include &lt;poll.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;sys/inotify.h&gt; #include &lt;unistd.h&gt; #include &lt;string.h&gt; </p>
<p> /* Read all available inotify events from the file descriptor &#8216;fd&#8217;. <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;wd is the table of watch descriptors for the directories in argv. <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;argc is the length of wd and argv. <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;argv is the list of watched directories. <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Entry 0 of wd and argv is unused.&nbsp;*/ </p>
<p> static void handle_events(int fd, int *wd, int argc, char* argv[]) { <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Some systems cannot read integer variables if they are not <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;properly aligned. On other systems, incorrect alignment may <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;decrease performance. Hence, the buffer used for reading from <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the inotify file descriptor should have the same alignment as <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct inotify_event.&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char buf[4096] <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__attribute__&nbsp;((aligned(__alignof__(struct inotify_event)))); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;const struct inotify_event&nbsp;*event; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ssize_t len; </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Loop while events can be read from inotify file descriptor.&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(;;)&nbsp;{ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Read some events.&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;len&nbsp;=&nbsp;read(fd, buf, sizeof(buf)); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(len&nbsp;==&nbsp;-1&nbsp;&amp;&amp;&nbsp;errno&nbsp;!=&nbsp;EAGAIN)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;read&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;If the nonblocking read()&nbsp;found no events to read, then <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;it returns -1 with errno set to EAGAIN. In that case, <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;we exit the loop.&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(len&nbsp;&lt;=&nbsp;0) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break; </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Loop over all events in the buffer&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(char&nbsp;*ptr&nbsp;=&nbsp;buf;&nbsp;ptr&nbsp;&lt;&nbsp;buf&nbsp;+&nbsp;len; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ptr&nbsp;+=&nbsp;sizeof(struct inotify_event)&nbsp;+&nbsp;event-&gt;len)&nbsp;{ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;event&nbsp;=&nbsp;(const struct inotify_event&nbsp;*)&nbsp;ptr; </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Print event type&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(event-&gt;mask&nbsp;&amp;&nbsp;IN_OPEN) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;IN_OPEN:&nbsp;&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(event-&gt;mask&nbsp;&amp;&nbsp;IN_CLOSE_NOWRITE) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;IN_CLOSE_NOWRITE:&nbsp;&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(event-&gt;mask&nbsp;&amp;&nbsp;IN_CLOSE_WRITE) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;IN_CLOSE_WRITE:&nbsp;&quot;); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Print the name of the watched directory&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int i&nbsp;=&nbsp;1;&nbsp;i&nbsp;&lt;&nbsp;argc;&nbsp;++i)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(wd[i]&nbsp;==&nbsp;event-&gt;wd)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%s/&quot;, argv[i]); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Print the name of the file&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(event-&gt;len) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%s&quot;, event-&gt;name); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Print type of filesystem object&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(event-&gt;mask&nbsp;&amp;&nbsp;IN_ISDIR) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&nbsp;[directory]\n&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;else <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&nbsp;[file]\n&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} } </p>
<p> int main(int argc, char* argv[]) { <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char buf; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int fd, i, poll_num; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;*wd; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nfds_t nfds; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct pollfd fds[2]; </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;&lt;&nbsp;2)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Usage:&nbsp;%s PATH&nbsp;[PATH ...]\n&quot;, argv[0]); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Press ENTER key to terminate.\n&quot;); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Create the file descriptor for accessing the inotify API&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fd&nbsp;=&nbsp;inotify_init1(IN_NONBLOCK); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(fd&nbsp;==&nbsp;-1)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;inotify_init1&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Allocate memory for watch descriptors&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;wd&nbsp;=&nbsp;calloc(argc, sizeof(int)); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(wd&nbsp;==&nbsp;NULL)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;calloc&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Mark directories for events <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;- file was opened <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;- file was closed&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(i&nbsp;=&nbsp;1;&nbsp;i&nbsp;&lt;&nbsp;argc;&nbsp;i++)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;wd[i]&nbsp;=&nbsp;inotify_add_watch(fd, argv[i], <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;IN_OPEN | IN_CLOSE); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(wd[i]&nbsp;==&nbsp;-1)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Cannot watch&nbsp;&#8216;%s&#8217;:&nbsp;%s\n&quot;, <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;argv[i], strerror(errno)); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Prepare for polling&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nfds&nbsp;=&nbsp;2; </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Console input&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fds[0].fd&nbsp;=&nbsp;STDIN_FILENO; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fds[0].events&nbsp;=&nbsp;POLLIN; </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Inotify input&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fds[1].fd&nbsp;=&nbsp;fd; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fds[1].events&nbsp;=&nbsp;POLLIN; </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Wait for events and/or terminal input&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Listening for events.\n&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while&nbsp;(1)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;poll_num&nbsp;=&nbsp;poll(fds, nfds, -1); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(poll_num&nbsp;==&nbsp;-1)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(errno&nbsp;==&nbsp;EINTR) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;continue; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;poll&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(poll_num&nbsp;&gt;&nbsp;0)&nbsp;{ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(fds[0].revents&nbsp;&amp;&nbsp;POLLIN)&nbsp;{ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Console input is available. Empty stdin and quit&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while&nbsp;(read(STDIN_FILENO,&nbsp;&amp;buf, 1)&nbsp;&gt;&nbsp;0&nbsp;&amp;&amp;&nbsp;buf&nbsp;!=&nbsp;&#8216;\n&#8217;) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;continue; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(fds[1].revents&nbsp;&amp;&nbsp;POLLIN)&nbsp;{ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Inotify events are available&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_events(fd, wd, argc, argv); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Listening for events stopped.\n&quot;); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Close inotify file descriptor&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;close(fd); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;free(wd); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-inotifywait/">inotifywait</a></code>(1), <code><a href="/docs/linux/man/1-inotifywatch/">inotifywatch</a></code>(1), <code><a href="/docs/linux/man/2-inotify_add_watch/">inotify_add_watch</a></code>(2), <code><a href="/docs/linux/man/2-inotify_init/">inotify_init</a></code>(2), <code><a href="/docs/linux/man/2-inotify_init1/">inotify_init1</a></code>(2), <code><a href="/docs/linux/man/2-inotify_rm_watch/">inotify_rm_watch</a></code>(2), <code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2), <code><a href="/docs/linux/man/7-fanotify/">fanotify</a></code>(7) </p>
<p> <i>Documentation/filesystems/inotify.txt</i> in the Linux kernel source tree  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
