---
title: "fanotify(7)"
name: "fanotify"
section: "7"
letter: "f"
url: "/docs/linux/man/7-fanotify/"
description: "fanotify – monitoring filesystem events"
---

<p>fanotify &#8211; monitoring filesystem events</p>
<h2>Description</h2>
<p>The fanotify API provides notification and interception of filesystem events. Use cases include virus scanning and hierarchical storage management. In the original fanotify API, only a limited set of events was supported. In particular, there was no support for create, delete, and move events. The support for those events was added in Linux 5.1. (See <code><a href="/docs/linux/man/7-inotify/">inotify</a></code>(7) for details of an API that did notify those events pre Linux 5.1.) Additional capabilities compared to the <code><a href="/docs/linux/man/7-inotify/">inotify</a></code>(7) API include the ability to monitor all of the objects in a mounted filesystem, the ability to make access permission decisions, and the possibility to read or modify files before access by other applications. The following system calls are used with this API: <code><a href="/docs/linux/man/2-fanotify_init/">fanotify_init</a></code>(2), <code><a href="/docs/linux/man/2-fanotify_mark/">fanotify_mark</a></code>(2), <code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-write/">write</a></code>(2), and <code><a href="/docs/linux/man/2-close/">close</a></code>(2).</p>
<h3>fanotify_init(), fanotify_mark(), and notification groups</h3>
<p>The <code><a href="/docs/linux/man/2-fanotify_init/">fanotify_init</a></code>(2) system call creates and initializes an fanotify notification group and returns a file descriptor referring to it. An fanotify notification group is a kernel-internal object that holds a list of files, directories, filesystems, and mount points for which events shall be created. For each entry in an fanotify notification group, two bit masks exist: the <i>mark</i> mask and the <i>ignore</i> mask. The mark mask defines file activities for which an event shall be created. The ignore mask defines activities for which no event shall be generated. Having these two types of masks permits a filesystem, mount point, or directory to be marked for receiving events, while at the same time ignoring events for specific objects under a mount point or directory. The <code><a href="/docs/linux/man/2-fanotify_mark/">fanotify_mark</a></code>(2) system call adds a file, directory, filesystem or mount point to a notification group and specifies which events shall be reported (or ignored), or removes or modifies such an entry. A possible usage of the ignore mask is for a file cache. Events of interest for a file cache are modification of a file and closing of the same. Hence, the cached directory or mount point is to be marked to receive these events. After receiving the first event informing that a file has been modified, the corresponding cache entry will be invalidated. No further modification events for this file are of interest until the file is closed. Hence, the modify event can be added to the ignore mask. Upon receiving the close event, the modify event can be removed from the ignore mask and the file cache entry can be updated. The entries in the fanotify notification groups refer to files and directories via their inode number and to mounts via their mount ID. If files or directories are renamed or moved within the same mount, the respective entries survive. If files or directories are deleted or moved to another mount or if filesystems or mounts are unmounted, the corresponding entries are deleted.</p>
<h3>The event queue</h3>
<p>As events occur on the filesystem objects monitored by a notification group, the fanotify system generates events that are collected in a queue. These events can then be read (using <code><a href="/docs/linux/man/2-read/">read</a></code>(2) or similar) from the fanotify file descriptor returned by <code><a href="/docs/linux/man/2-fanotify_init/">fanotify_init</a></code>(2). Two types of events are generated: <i>notification</i> events and <i>permission</i> events. Notification events are merely informative and require no action to be taken by the receiving application with one exception: if a valid file descriptor is provided within a generic event, the file descriptor must be closed. Permission events are requests to the receiving application to decide whether permission for a file access shall be granted. For these events, the recipient must write a response which decides whether access is granted or not. An event is removed from the event queue of the fanotify group when it has been read. Permission events that have been read are kept in an internal list of the fanotify group until either a permission decision has been taken by writing to the fanotify file descriptor or the fanotify file descriptor is closed.</p>
<h3>Reading fanotify events</h3>
<p>Calling <code><a href="/docs/linux/man/2-read/">read</a></code>(2) for the file descriptor returned by <code><a href="/docs/linux/man/2-fanotify_init/">fanotify_init</a></code>(2) blocks (if the flag <code>FAN_NONBLOCK</code> is not specified in the call to <code><a href="/docs/linux/man/2-fanotify_init/">fanotify_init</a></code>(2)) until either a file event occurs or the call is interrupted by a signal (see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)). The use of one of the flags <code>FAN_REPORT_FID</code>, <code>FAN_REPORT_DIR_FID</code> in <code><a href="/docs/linux/man/2-fanotify_init/">fanotify_init</a></code>(2) influences what data structures are returned to the event listener for each event. Events reported to a group initialized with one of these flags will use file handles to identify filesystem objects instead of file descriptors.</p>
<dl>
<dt>After a successful</p>
<dd><code><a href="/docs/linux/man/2-read/">read</a></code>(2), the read buffer contains one or more of the following structures:</dl>
<pre><code>struct fanotify_event_metadata {
    __u32 event_len;
    __u8 vers;
    __u8 reserved;
    __u16 metadata_len;
    __aligned_u64 mask;
    __s32 fd;
    __s32 pid;
};</code></pre>
<p> In case of an fanotify group that identifies filesystem objects by file handles, you should also expect to receive one or more additional information records of the structure detailed below following the generic <i>fanotify_event_metadata</i> structure within the read buffer: struct fanotify_event_info_header {<br />
    __u8 info_type;<br />
    __u8 pad;<br />
    __u16 len;<br />
};<br />
struct fanotify_event_info_fid {<br />
    struct fanotify_event_info_header hdr;<br />
    __kernel_fsid_t fsid;<br />
    unsigned char file_handle[0];<br />
}; For performance reasons, it is recommended to use a large buffer size (for example, 4096 bytes), so that multiple events can be retrieved by a single <code><a href="/docs/linux/man/2-read/">read</a></code>(2). The return value of <code><a href="/docs/linux/man/2-read/">read</a></code>(2) is the number of bytes placed in the buffer, or -1 in case of an error (but see BUGS). The fields of the <i>fanotify_event_metadata</i> structure are as follows:</p>
<dl>
<dt><i>event_len</i></p>
<dd>This is the length of the data for the current event and the offset to the next event in the buffer. Unless the group identifies filesystem objects by file handles, the value of <i>event_len</i> is always <code>FAN_EVENT_METADATA_LEN</code>. For a group that identifies filesystem objects by file handles, <i>event_len</i> also includes the variable length file identifier records.</p>
<dt><i>vers</i></p>
<dd>This field holds a version number for the structure. It must be compared to <code>FANOTIFY_METADATA_VERSION</code> to verify that the structures returned at run time match the structures defined at compile time. In case of a mismatch, the application should abandon trying to use the fanotify file descriptor.</p>
<dt><i>reserved</i></p>
<dd>This field is not used.</p>
<dt><i>metadata_len</i></p>
<dd>This is the length of the structure. The field was introduced to facilitate the implementation of optional headers per event type. No such optional headers exist in the current implementation.</p>
<dt><i>mask</i></p>
<dd>This is a bit mask describing the event (see below).</p>
<dt><i>fd</i></p>
<dd>This is an open file descriptor for the object being accessed, or <code>FAN_NOFD</code> if a queue overflow occurred. With an fanotify group that identifies filesystem objects by file handles, applications should expect this value to be set to <code>FAN_NOFD</code> for each event that is received. The file descriptor can be used to access the contents of the monitored file or directory. The reading application is responsible for closing this file descriptor.</p>
<dd>When calling <code><a href="/docs/linux/man/2-fanotify_init/">fanotify_init</a></code>(2), the caller may specify (via the <i>event_f_flags</i> argument) various file status flags that are to be set on the open file description that corresponds to this file descriptor. In addition, the (kernel-internal) <code>FMODE_NONOTIFY</code> file status flag is set on the open file description. This flag suppresses fanotify event generation. Hence, when the receiver of the fanotify event accesses the notified file or directory using this file descriptor, no additional events will be created.</p>
<dt><i>pid</i></p>
<dd>If flag <code>FAN_REPORT_TID</code> was set in <code><a href="/docs/linux/man/2-fanotify_init/">fanotify_init</a></code>(2), this is the TID of the thread that caused the event. Otherwise, this the PID of the process that caused the event.</dl>
<p> A program listening to fanotify events can compare this PID to the PID returned by <code><a href="/docs/linux/man/2-getpid/">getpid</a></code>(2), to determine whether the event is caused by the listener itself, or is due to a file access by another process. The bit mask in <i>mask</i> indicates which events have occurred for a single filesystem object. Multiple bits may be set in this mask, if more than one event occurred for the monitored filesystem object. In particular, consecutive events for the same filesystem object and originating from the same process may be merged into a single event, with the exception that two permission events are never merged into one queue entry. The bits that may appear in <i>mask</i> are as follows:</p>
<dl>
<dt><code>FAN_ACCESS</code></p>
<dd>A file or a directory (but see BUGS) was accessed (read).</p>
<dt><code>FAN_OPEN</code></p>
<dd>A file or a directory was opened.</p>
<dt><code>FAN_OPEN_EXEC</code></p>
<dd>A file was opened with the intent to be executed. See NOTES in <code><a href="/docs/linux/man/2-fanotify_mark/">fanotify_mark</a></code>(2) for additional details.</p>
<dt><code>FAN_ATTRIB</code></p>
<dd>A file or directory metadata was changed.</p>
<dt><code>FAN_CREATE</code></p>
<dd>A child file or directory was created in a watched parent.</p>
<dt><code>FAN_DELETE</code></p>
<dd>A child file or directory was deleted in a watched parent.</p>
<dt><code>FAN_DELETE_SELF</code></p>
<dd>A watched file or directory was deleted.</p>
<dt><code>FAN_MOVED_FROM</code></p>
<dd>A file or directory has been moved from a watched parent directory.</p>
<dt><code>FAN_MOVED_TO</code></p>
<dd>A file or directory has been moved to a watched parent directory.</p>
<dt><code>FAN_MOVE_SELF</code></p>
<dd>A watched file or directory was moved.</p>
<dt><code>FAN_MODIFY</code></p>
<dd>A file was modified.</p>
<dt><code>FAN_CLOSE_WRITE</code></p>
<dd>A file that was opened for writing (<code>O_WRONLY</code> or <code>O_RDWR</code>) was closed.</p>
<dt><code>FAN_CLOSE_NOWRITE</code></p>
<dd>A file or directory that was opened read-only (<code>O_RDONLY</code>) was closed.</p>
<dt><code>FAN_Q_OVERFLOW</code></p>
<dd>The event queue exceeded the limit of 16384 entries. This limit can be overridden by specifying the <code>FAN_UNLIMITED_QUEUE</code> flag when calling <code><a href="/docs/linux/man/2-fanotify_init/">fanotify_init</a></code>(2).</p>
<dt><code>FAN_ACCESS_PERM</code></p>
<dd>An application wants to read a file or directory, for example using <code><a href="/docs/linux/man/2-read/">read</a></code>(2) or <code><a href="/docs/linux/man/2-readdir/">readdir</a></code>(2). The reader must write a response (as described below) that determines whether the permission to access the filesystem object shall be granted.</p>
<dt><code>FAN_OPEN_PERM</code></p>
<dd>An application wants to open a file or directory. The reader must write a response that determines whether the permission to open the filesystem object shall be granted.</p>
<dt><code>FAN_OPEN_EXEC_PERM</code></p>
<dd>An application wants to open a file for execution. The reader must write a response that determines whether the permission to open the filesystem object for execution shall be granted. See NOTES in <code><a href="/docs/linux/man/2-fanotify_mark/">fanotify_mark</a></code>(2) for additional details.</dl>
<p> To check for any close event, the following bit mask may be used:</p>
<dl>
<dt><code>FAN_CLOSE</code></p>
<dd>A file was closed. This is a synonym for:</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FAN_CLOSE_WRITE | FAN_CLOSE_NOWRITE</dl>
<p> To check for any move event, the following bit mask may be used:</p>
<dl>
<dt><code>FAN_MOVE</code></p>
<dd>A file or directory was moved. This is a synonym for:</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FAN_MOVED_FROM | FAN_MOVED_TO</dl>
<p> The following bits may appear in <i>mask</i> only in conjunction with other event type bits:</p>
<dl>
<dt><code>FAN_ONDIR</code></p>
<dd>The events described in the <i>mask</i> have occurred on a directory object. Reporting events on directories requires setting this flag in the mark mask. See <code><a href="/docs/linux/man/2-fanotify_mark/">fanotify_mark</a></code>(2) for additional details. The <code>FAN_ONDIR</code> flag is reported in an event mask only if the fanotify group identifies filesystem objects by file handles.</dl>
<p> The fields of the <i>fanotify_event_info_fid</i> structure are as follows:</p>
<dl>
<dt><i>hdr</i></p>
<dd>This is a structure of type <i>fanotify_event_info_header</i>. It is a generic header that contains information used to describe an additional information record attached to the event. For example, when an fanotify file descriptor is created using <code>FAN_REPORT_FID</code>, a single information record is expected to be attached to the event with <i>info_type</i> field value of <code>FAN_EVENT_INFO_TYPE_FID</code>. When an fanotify file descriptor is created using the combination of <code>FAN_REPORT_FID</code> and <code>FAN_REPORT_DIR_FID</code>, there may be two information records attached to the event: one with <i>info_type</i> field value of <code>FAN_EVENT_INFO_TYPE_DFID</code>, identifying a parent directory object, and one with <i>info_type</i> field value of <code>FAN_EVENT_INFO_TYPE_FID</code>, identifying a non-directory object. The <i>fanotify_event_info_header</i> contains a <i>len</i> field. The value of <i>len</i> is the size of the additional information record including the <i>fanotify_event_info_header</i> itself. The total size of all additional information records is not expected to be bigger than ( <i>event_len</i> &#8211; <i>metadata_len</i> ).</p>
<dt><i>fsid</i></p>
<dd>This is a unique identifier of the filesystem containing the object associated with the event. It is a structure of type <i>__kernel_fsid_t</i> and contains the same value as <i>f_fsid</i> when calling <code><a href="/docs/linux/man/2-statfs/">statfs</a></code>(2).</p>
<dt><i>file_handle</i></p>
<dd>This is a variable length structure of type struct file_handle. It is an opaque handle that corresponds to a specified object on a filesystem as returned by <code><a href="/docs/linux/man/2-name_to_handle_at/">name_to_handle_at</a></code>(2). It can be used to uniquely identify a file on a filesystem and can be passed as an argument to <code><a href="/docs/linux/man/2-open_by_handle_at/">open_by_handle_at</a></code>(2). Note that for the directory entry modification events <code>FAN_CREATE</code>, <code>FAN_DELETE</code>, and <code>FAN_MOVE</code>, the <i>file_handle</i> identifies the modified directory and not the created/deleted/moved child object. If the value of <i>info_type</i> field is <code>FAN_EVENT_INFO_TYPE_DFID_NAME</code>, the file handle is followed by a null terminated string that identifies the created/deleted/moved directory entry name. For other events such as <code>FAN_OPEN</code>, <code>FAN_ATTRIB</code>, <code>FAN_DELETE_SELF</code>, and <code>FAN_MOVE_SELF</code>, if the value of <i>info_type</i> field is <code>FAN_EVENT_INFO_TYPE_FID</code>, the <i>file_handle</i> identifies the object correlated to the event. If the value of <i>info_type</i> field is <code>FAN_EVENT_INFO_TYPE_DFID</code>, the <i>file_handle</i> identifies the directory object correlated to the event or the parent directory of a non-directory object correlated to the event. If the value of <i>info_type</i> field is <code>FAN_EVENT_INFO_TYPE_DFID_NAME</code>, the <i>file_handle</i> identifies the same directory object that would be reported with <code>FAN_EVENT_INFO_TYPE_DFID</code> and the file handle is followed by a null terminated string that identifies the name of a directory entry in that directory, or &#8216;.&#8217; to identify the directory object itself.</dl>
<p> The following macros are provided to iterate over a buffer containing fanotify event metadata returned by a <code><a href="/docs/linux/man/2-read/">read</a></code>(2) from an fanotify file descriptor:</p>
<dl>
<dt><code>FAN_EVENT_OK(meta, len)</code></p>
<dd>This macro checks the remaining length <i>len</i> of the buffer <i>meta</i> against the length of the metadata structure and the <i>event_len</i> field of the first metadata structure in the buffer.</p>
<dt><code>FAN_EVENT_NEXT(meta, len)</code></p>
<dd>This macro uses the length indicated in the <i>event_len</i> field of the metadata structure pointed to by <i>meta</i> to calculate the address of the next metadata structure that follows <i>meta</i>. <i>len</i> is the number of bytes of metadata that currently remain in the buffer. The macro returns a pointer to the next metadata structure that follows <i>meta</i>, and reduces <i>len</i> by the number of bytes in the metadata structure that has been skipped over (i.e., it subtracts <i>meta-&gt;event_len</i> from <i>len</i>).</dl>
<p> In addition, there is:</p>
<dl>
<dt><code>FAN_EVENT_METADATA_LEN</code></p>
<dd>This macro returns the size (in bytes) of the structure <i>fanotify_event_metadata</i>. This is the minimum size (and currently the only size) of any event metadata.</dl>
<h3>Monitoring an fanotify file descriptor for events</h3>
<p>When an fanotify event occurs, the fanotify file descriptor indicates as readable when passed to <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7), <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), or <code><a href="/docs/linux/man/2-select/">select</a></code>(2).</p>
<h3>Dealing with permission events</h3>
<p>For permission events, the application must <code><a href="/docs/linux/man/2-write/">write</a></code>(2) a structure of the following form to the fanotify file descriptor: struct fanotify_response {<br />
    __s32 fd;<br />
    __u32 response;<br />
}; The fields of this structure are as follows:</p>
<dl>
<dt><i>fd</i></p>
<dd>This is the file descriptor from the structure <i>fanotify_event_metadata</i>.</p>
<dt><i>response</i></p>
<dd>This field indicates whether or not the permission is to be granted. Its value must be either <code>FAN_ALLOW</code> to allow the file operation or <code>FAN_DENY</code> to deny the file operation.</dl>
<p> If access is denied, the requesting application call will receive an <code>EPERM</code> error.</p>
<h3>Closing the fanotify file descriptor</h3>
<p>When all file descriptors referring to the fanotify notification group are closed, the fanotify group is released and its resources are freed for reuse by the kernel. Upon <code><a href="/docs/linux/man/2-close/">close</a></code>(2), outstanding permission events will be set to allowed.</p>
<h3>/proc/[pid]/fdinfo</h3>
<p>The file <i>/proc/[pid]/fdinfo/[fd]</i> contains information about fanotify marks for file descriptor <i>fd</i> of process <i>pid</i>. See <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5) for details.</p>
<h2>Errors</h2>
<p>In addition to the usual errors for <code><a href="/docs/linux/man/2-read/">read</a></code>(2), the following errors can occur when reading from the fanotify file descriptor:</p>
<dl>
<dt><code>EINVAL</code></p>
<dd>The buffer is too small to hold the event.</p>
<dt><code>EMFILE</code></p>
<dd>The per-process limit on the number of open files has been reached. See the description of <code>RLIMIT_NOFILE</code> in <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2).</p>
<dt><code>ENFILE</code></p>
<dd>The system-wide limit on the total number of open files has been reached. See <i>/proc/sys/fs/file-max</i> in <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5).</p>
<dt><code>ETXTBSY</code></p>
<dd>This error is returned by <code><a href="/docs/linux/man/2-read/">read</a></code>(2) if <code>O_RDWR</code> or <code>O_WRONLY</code> was specified in the <i>event_f_flags</i> argument when calling <code><a href="/docs/linux/man/2-fanotify_init/">fanotify_init</a></code>(2) and an event occurred for a monitored file that is currently being executed.</dl>
<p> In addition to the usual errors for <code><a href="/docs/linux/man/2-write/">write</a></code>(2), the following errors can occur when writing to the fanotify file descriptor:</p>
<dl>
<dt><code>EINVAL</code></p>
<dd>Fanotify access permissions are not enabled in the kernel configuration or the value of <i>response</i> in the response structure is not valid.</p>
<dt><code>ENOENT</code></p>
<dd>The file descriptor <i>fd</i> in the response structure is not valid. This may occur when a response for the permission event has already been written.</dl>
<h2>Versions</h2>
<p>The fanotify API was introduced in version 2.6.36 of the Linux kernel and enabled in version 2.6.37. Fdinfo support was added in version 3.8.</p>
<h2>Conforming To</h2>
<p>The fanotify API is Linux-specific.</p>
<h2>Notes</h2>
<p>The fanotify API is available only if the kernel was built with the <code>CONFIG_FANOTIFY</code> configuration option enabled. In addition, fanotify permission handling is available only if the <code>CONFIG_FANOTIFY_ACCESS_PERMISSIONS</code> configuration option is enabled.</p>
<h3>Limitations and caveats</h3>
<p>Fanotify reports only events that a user-space program triggers through the filesystem API. As a result, it does not catch remote events that occur on network filesystems. </p>
<p> The fanotify API does not report file accesses and modifications that may occur because of <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-msync/">msync</a></code>(2), and <code><a href="/docs/linux/man/2-munmap/">munmap</a></code>(2). </p>
<p> Events for directories are created only if the directory itself is opened, read, and closed. Adding, removing, or changing children of a marked directory does not create events for the monitored directory itself. </p>
<p> Fanotify monitoring of directories is not recursive: to monitor subdirectories under a directory, additional marks must be created. The <code>FAN_CREATE</code> event can be used for detecting when a subdirectory has been created under a marked directory. An additional mark must then be set on the newly created subdirectory. This approach is racy, because it can lose events that occurred inside the newly created subdirectory, before a mark is added on that subdirectory. Monitoring mounts offers the capability to monitor a whole directory tree in a race-free manner. Monitoring filesystems offers the capability to monitor changes made from any mount of a filesystem instance in a race-free manner. </p>
<p> The event queue can overflow. In this case, events are lost.</p>
<h2>Bugs</h2>
<p>Before Linux 3.19, <code><a href="/docs/linux/man/2-fallocate/">fallocate</a></code>(2) did not generate fanotify events. Since Linux 3.19, calls to <code><a href="/docs/linux/man/2-fallocate/">fallocate</a></code>(2) generate <code>FAN_MODIFY</code> events. </p>
<p> As of Linux 3.17, the following bugs exist:</p>
<dl>
<dt>*</p>
<dd>On Linux, a filesystem object may be accessible through multiple paths, for example, a part of a filesystem may be remounted using the <i>&#8211;bind</i> option of <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8). A listener that marked a mount will be notified only of events that were triggered for a filesystem object using the same mount. Any other event will pass unnoticed.</p>
<dt>*</p>
<dd>When an event is generated, no check is made to see whether the user ID of the receiving process has authorization to read or write the file before passing a file descriptor for that file. This poses a security risk, when the <code>CAP_SYS_ADMIN</code> capability is set for programs executed by unprivileged users.</p>
<dt>*</p>
<dd>If a call to <code><a href="/docs/linux/man/2-read/">read</a></code>(2) processes multiple events from the fanotify queue and an error occurs, the return value will be the total length of the events successfully copied to the user-space buffer before the error occurred. The return value will not be -1, and <i>errno</i> will not be set. Thus, the reading application has no way to detect the error.</dl>
<h2>Examples</h2>
<p>The two example programs below demonstrate the usage of the fanotify API.</p>
<h3>Example program: fanotify_example.c</h3>
<p>The first program is an example of fanotify being used with its event object information passed in the form of a file descriptor. The program marks the mount point passed as a command-line argument and waits for events of type <code>FAN_OPEN_PERM</code> and <code>FAN_CLOSE_WRITE</code>. When a permission event occurs, a <code>FAN_ALLOW</code> response is given. The following shell session shows an example of running this program. This session involved editing the file <i>/home/user/temp/notes</i>. Before the file was opened, a <code>FAN_OPEN_PERM</code> event occurred. After the file was closed, a <code>FAN_CLOSE_WRITE</code> event occurred. Execution of the program ends when the user presses the ENTER key. # <code>./fanotify_example /home</code> Press enter key to terminate. Listening for events. FAN_OPEN_PERM: File /home/user/temp/notes FAN_CLOSE_WRITE: File /home/user/temp/notes Listening for events stopped.</p>
<p>Program source: fanotify_example.c</p>
<p>#define _GNU_SOURCE /* Needed to get O_LARGEFILE definition */<br />
#include &lt;errno.h&gt;<br />
#include &lt;fcntl.h&gt;<br />
#include &lt;limits.h&gt;<br />
#include &lt;poll.h&gt;<br />
#include &lt;stdio.h&gt;<br />
#include &lt;stdlib.h&gt;<br />
#include &lt;sys/fanotify.h&gt;<br />
#include &lt;unistd.h&gt;<br />
/* Read all available fanotify events from the file descriptor &#8216;fd&#8217; */<br />
static void<br />
handle_events(int fd)<br />
{<br />
    const struct fanotify_event_metadata *metadata;<br />
    struct fanotify_event_metadata buf[200];<br />
    ssize_t len;<br />
    char path[PATH_MAX];<br />
    ssize_t path_len;<br />
    char procfd_path[PATH_MAX];<br />
    struct fanotify_response response;<br />
    /* Loop while events can be read from fanotify file descriptor */<br />
    for (;;) {<br />
        /* Read some events */<br />
        len = read(fd, buf, sizeof(buf));<br />
        if (len == -1 &amp;&amp; errno != EAGAIN) {<br />
            perror(&quot;read&quot;);<br />
            exit(EXIT_FAILURE);<br />
        }<br />
        /* Check if end of available data reached */<br />
        if (len &lt;= 0)<br />
            break;<br />
        /* Point to the first event in the buffer */<br />
        metadata = buf;<br />
        /* Loop over all events in the buffer */<br />
        while (FAN_EVENT_OK(metadata, len)) {<br />
            /* Check that run-time and compile-time structures match */<br />
            if (metadata-&gt;vers != FANOTIFY_METADATA_VERSION) {<br />
                fprintf(stderr,<br />
                        &quot;Mismatch of fanotify metadata version.
&quot;);<br />
                exit(EXIT_FAILURE);<br />
            }<br />
            /* metadata-&gt;fd contains either FAN_NOFD, indicating a<br />
                           queue overflow, or a file descriptor (a nonnegative<br />
                           integer). Here, we simply ignore queue overflow. */<br />
            if (metadata-&gt;fd &gt;= 0) {<br />
                /* Handle open permission event */<br />
                if (metadata-&gt;mask &amp; FAN_OPEN_PERM) {<br />
                    printf(&quot;FAN_OPEN_PERM: &quot;);<br />
                    /* Allow file to be opened */<br />
                    response.fd = metadata-&gt;fd;<br />
                    response.response = FAN_ALLOW;<br />
                    write(fd, &amp;response, sizeof(response));<br />
                }<br />
                /* Handle closing of writable file event */<br />
                if (metadata-&gt;mask &amp; FAN_CLOSE_WRITE)<br />
                    printf(&quot;FAN_CLOSE_WRITE: &quot;);<br />
                /* Retrieve and print pathname of the accessed file */<br />
                snprintf(procfd_path, sizeof(procfd_path),<br />
                         &quot;/proc/self/fd/%d&quot;, metadata-&gt;fd);<br />
                path_len = readlink(procfd_path, path,<br />
                                    sizeof(path) &#8211; 1);<br />
                if (path_len == -1) {<br />
                    perror(&quot;readlink&quot;);<br />
                    exit(EXIT_FAILURE);<br />
                }<br />
                path[path_len] = &#8216;
