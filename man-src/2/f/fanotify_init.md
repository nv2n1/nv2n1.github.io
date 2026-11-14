---
title: "fanotify_init(2)"
name: "fanotify_init"
section: "2"
letter: "f"
url: "/docs/linux/man/2-fanotify_init/"
description: "fanotify_init – create and initialize fanotify group"
---

<h2 class="name">NAME</h2>
<p> fanotify_init &#8211; create and initialize fanotify group </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;fcntl.h&gt;</code><br />
 <code>#include &lt;sys/fanotify.h&gt;</code> </p>
<p> <code>int fanotify_init(unsigned int </code><i>flags</i><code>, unsigned int </code><i>event_f_flags</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> For an overview of the fanotify API, see <code><a href="/docs/linux/man/7-fanotify/">fanotify</a></code>(7). </p>
<p> <code>fanotify_init</code>() initializes a new fanotify group and returns a file descriptor for the event queue associated with the group. </p>
<p> The file descriptor is used in calls to <code><a href="/docs/linux/man/2-fanotify_mark/">fanotify_mark</a></code>(2) to specify the files, directories, mounts or filesystems for which fanotify events shall be created. These events are received by reading from the file descriptor. Some events are only informative, indicating that a file has been accessed. Other events can be used to determine whether another application is permitted to access a file or directory. Permission to access filesystem objects is granted by writing to the file descriptor. </p>
<p> Multiple programs may be using the fanotify interface at the same time to monitor the same files. </p>
<p> In the current implementation, the number of fanotify groups per user is limited to 128. This limit cannot be overridden. </p>
<p> Calling <code>fanotify_init</code>() requires the <code>CAP_SYS_ADMIN</code> capability. This constraint might be relaxed in future versions of the API. Therefore, certain additional capability checks have been implemented as indicated below. </p>
<p> The <i>flags</i> argument contains a multi-bit field defining the notification class of the listening application and further single bit fields specifying the behavior of the file descriptor. </p>
<p> If multiple listeners for permission events exist, the notification class is used to establish the sequence in which the listeners receive the events. </p>
<p> Only one of the following notification classes may be specified in <i>flags</i>:</p>
<dl>
<dt><code>FAN_CLASS_PRE_CONTENT</code></p>
<dd> This value allows the receipt of events notifying that a file has been accessed and events for permission decisions if a file may be accessed. It is intended for event listeners that need to access files before they contain their final data. This notification class might be used by hierarchical storage managers, for example.</p>
<dt><code>FAN_CLASS_CONTENT</code></p>
<dd> This value allows the receipt of events notifying that a file has been accessed and events for permission decisions if a file may be accessed. It is intended for event listeners that need to access files when they already contain their final content. This notification class might be used by malware detection programs, for example.</p>
<dt><code>FAN_CLASS_NOTIF</code></p>
<dd> This is the default value. It does not need to be specified. This value only allows the receipt of events notifying that a file has been accessed. Permission decisions before the file is accessed are not possible.</dl>
<p> Listeners with different notification classes will receive events in the order <code>FAN_CLASS_PRE_CONTENT</code>, <code>FAN_CLASS_CONTENT</code>, <code>FAN_CLASS_NOTIF</code>. The order of notification for listeners in the same notification class is undefined. </p>
<p> The following bits can additionally be set in <i>flags</i>:</p>
<dl>
<dt><code>FAN_CLOEXEC</code></p>
<dd> Set the close-on-exec flag (<code>FD_CLOEXEC</code>) on the new file descriptor. See the description of the <code>O_CLOEXEC</code> flag in <code><a href="/docs/linux/man/2-open/">open</a></code>(2).</p>
<dt><code>FAN_NONBLOCK</code></p>
<dd> Enable the nonblocking flag (<code>O_NONBLOCK</code>) for the file descriptor. Reading from the file descriptor will not block. Instead, if no data is available, <code><a href="/docs/linux/man/2-read/">read</a></code>(2) fails with the error <code>EAGAIN</code>.</p>
<dt><code>FAN_UNLIMITED_QUEUE</code></p>
<dd> Remove the limit of 16384 events for the event queue. Use of this flag requires the <code>CAP_SYS_ADMIN</code> capability.</p>
<dt><code>FAN_UNLIMITED_MARKS</code></p>
<dd> Remove the limit of 8192 marks. Use of this flag requires the <code>CAP_SYS_ADMIN</code> capability.</p>
<dt><code>FAN_REPORT_TID</code> (since Linux 4.20)</p>
<dd> Report thread ID (TID) instead of process ID (PID) in the <i>pid</i> field of the <i>struct fanotify_event_metadata</i> supplied to <code><a href="/docs/linux/man/2-read/">read</a></code>(2) (see <code><a href="/docs/linux/man/7-fanotify/">fanotify</a></code>(7)).</p>
<dt><code>FAN_REPORT_FID</code> (since Linux 5.1)</p>
<dd> This value allows the receipt of events which contain additional information about the underlying filesystem object correlated to an event. An additional record of type <code>FAN_EVENT_INFO_TYPE_FID</code> encapsulates the information about the object and is included alongside the generic event metadata structure. The file descriptor that is used to represent the object correlated to an event is instead substituted with a file handle. It is intended for applications that may find the use of a file handle to identify an object more suitable than a file descriptor. Additionally, it may be used for applications monitoring a directory or a filesystem that are interested in the directory entry modification events <code>FAN_CREATE</code>, <code>FAN_DELETE</code>, and <code>FAN_MOVE</code>, or in events such as <code>FAN_ATTRIB</code>, <code>FAN_DELETE_SELF</code>, and <code>FAN_MOVE_SELF</code>. All the events above require an fanotify group that identifies filesystem objects by file handles. Note that for the directory entry modification events the reported file handle identifies the modified directory and not the created/deleted/moved child object. The use of <code>FAN_CLASS_CONTENT</code> or <code>FAN_CLASS_PRE_CONTENT</code> is not permitted with this flag and will result in the error <code>EINVAL</code>. See <code><a href="/docs/linux/man/7-fanotify/">fanotify</a></code>(7) for additional details.</p>
<dt><code>FAN_REPORT_DIR_FID</code> (since Linux 5.9)</p>
<dd> Events for fanotify groups initialized with this flag will contain (see exceptions below) additional information about a directory object correlated to an event. An additional record of type <code>FAN_EVENT_INFO_TYPE_DFID</code> encapsulates the information about the directory object and is included alongside the generic event metadata structure. For events that occur on a non-directory object, the additional structure includes a file handle that identifies the parent directory filesystem object. Note that there is no guarantee that the directory filesystem object will be found at the location described by the file handle information at the time the event is received. When combined with the flag <code>FAN_REPORT_FID</code>, two records may be reported with events that occur on a non-directory object, one to identify the non-directory object itself and one to identify the parent directory object. Note that in some cases, a filesystem object does not have a parent, for example, when an event occurs on an unlinked but open file. In that case, with the <code>FAN_REPORT_FID</code> flag, the event will be reported with only one record to identify the non-directory object itself, because there is no directory associated with the event. Without the <code>FAN_REPORT_FID</code> flag, no event will be reported. See <code><a href="/docs/linux/man/7-fanotify/">fanotify</a></code>(7) for additional details.</p>
<dt><code>FAN_REPORT_NAME</code> (since Linux 5.9)</p>
<dd> Events for fanotify groups initialized with this flag will contain additional information about the name of the directory entry correlated to an event. This flag must be provided in conjunction with the flag <code>FAN_REPORT_DIR_FID</code>. Providing this flag value without <code>FAN_REPORT_DIR_FID</code> will result in the error <code>EINVAL</code>. This flag may be combined with the flag <code>FAN_REPORT_FID</code>. An additional record of type <code>FAN_EVENT_INFO_TYPE_DFID_NAME</code>, which encapsulates the information about the directory entry, is included alongside the generic event metadata structure and substitutes the additional information record of type <code>FAN_EVENT_INFO_TYPE_DFID</code>. The additional record includes a file handle that identifies a directory filesystem object followed by a name that identifies an entry in that directory. For the directory entry modification events <code>FAN_CREATE</code>, <code>FAN_DELETE</code>, and <code>FAN_MOVE</code>, the reported name is that of the created/deleted/moved directory entry. For other events that occur on a directory object, the reported file handle is that of the directory object itself and the reported name is &#8216;.&#8217;. For other events that occur on a non-directory object, the reported file handle is that of the parent directory object and the reported name is the name of a directory entry where the object was located at the time of the event. The rationale behind this logic is that the reported directory file handle can be passed to <code><a href="/docs/linux/man/2-open_by_handle_at/">open_by_handle_at</a></code>(2) to get an open directory file descriptor and that file descriptor along with the reported name can be used to call <code><a href="/docs/linux/man/2-fstatat/">fstatat</a></code>(2). The same rule that applies to record type <code>FAN_EVENT_INFO_TYPE_DFID</code> also applies to record type <code>FAN_EVENT_INFO_TYPE_DFID_NAME</code>: if a non-directory object has no parent, either the event will not be reported or it will be reported without the directory entry information. Note that there is no guarantee that the filesystem object will be found at the location described by the directory entry information at the time the event is received. See <code><a href="/docs/linux/man/7-fanotify/">fanotify</a></code>(7) for additional details.</p>
<dt><code>FAN_REPORT_DFID_NAME</code></p>
<dd> This is a synonym for (<code>FAN_REPORT_DIR_FID</code>|<code>FAN_REPORT_NAME</code>).</dl>
<p> The <i>event_f_flags</i> argument defines the file status flags that will be set on the open file descriptions that are created for fanotify events. For details of these flags, see the description of the <i>flags</i> values in <code><a href="/docs/linux/man/2-open/">open</a></code>(2). <i>event_f_flags</i> includes a multi-bit field for the access mode. This field can take the following values:</p>
<dl>
<dt><code>O_RDONLY</code></p>
<dd> This value allows only read access.</p>
<dt><code>O_WRONLY</code></p>
<dd> This value allows only write access.</p>
<dt><code>O_RDWR</code></p>
<dd> This value allows read and write access.</dl>
<p> Additional bits can be set in <i>event_f_flags</i>. The most useful values are:</p>
<dl>
<dt><code>O_LARGEFILE</code></p>
<dd> Enable support for files exceeding 2 GB. Failing to set this flag will result in an <code>EOVERFLOW</code> error when trying to open a large file which is monitored by an fanotify group on a 32-bit system.</p>
<dt><code>O_CLOEXEC</code> (since Linux 3.18)</p>
<dd> Enable the close-on-exec flag for the file descriptor. See the description of the <code>O_CLOEXEC</code> flag in <code><a href="/docs/linux/man/2-open/">open</a></code>(2) for reasons why this may be useful.</dl>
<p> The following are also allowable: <code>O_APPEND</code>, <code>O_DSYNC</code>, <code>O_NOATIME</code>, <code>O_NONBLOCK</code>, and <code>O_SYNC</code>. Specifying any other flag in <i>event_f_flags</i> yields the error <code>EINVAL</code> (but see BUGS).</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>fanotify_init</code>() returns a new file descriptor. On error, -1 is returned, and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd> An invalid value was passed in <i>flags</i> or <i>event_f_flags</i>. <code>FAN_ALL_INIT_FLAGS</code> (deprecated since Linux kernel version 4.20) defines all allowable bits for <i>flags</i>.</p>
<dt><code>EMFILE</code></p>
<dd> The number of fanotify groups for this user exceeds 128.</p>
<dt><code>EMFILE</code></p>
<dd> The per-process limit on the number of open file descriptors has been reached.</p>
<dt><code>ENOMEM</code></p>
<dd> The allocation of memory for the notification group failed.</p>
<dt><code>ENOSYS</code></p>
<dd> This kernel does not implement <code>fanotify_init</code>(). The fanotify API is available only if the kernel was configured with <code>CONFIG_FANOTIFY</code>.</p>
<dt><code>EPERM</code></p>
<dd> The operation is not permitted because the caller lacks the <code>CAP_SYS_ADMIN</code> capability.</dl>
<h2>VERSIONS</h2>
<p> <code>fanotify_init</code>() was introduced in version 2.6.36 of the Linux kernel and enabled in version 2.6.37.</p>
<h2>CONFORMING TO</h2>
<p> This system call is Linux-specific.</p>
<h2>BUGS</h2>
<p> The following bug was present in Linux kernels before version 3.18:</p>
<dl>
<dt>*</p>
<dd> The <code>O_CLOEXEC</code> is ignored when passed in <i>event_f_flags</i>.</dl>
<p> The following bug was present in Linux kernels before version 3.14:</p>
<dl>
<dt>*</p>
<dd> The <i>event_f_flags</i> argument is not checked for invalid flags. Flags that are intended only for internal use, such as <code>FMODE_EXEC</code>, can be set, and will consequently be set for the file descriptors returned when reading from the fanotify file descriptor.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-fanotify_mark/">fanotify_mark</a></code>(2), <code><a href="/docs/linux/man/7-fanotify/">fanotify</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
