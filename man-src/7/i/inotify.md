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
<dt>*</p>
<dd><code><a href="/docs/linux/man/2-inotify_init/">inotify_init</a></code>(2) creates an inotify instance and returns a file descriptor referring to the inotify instance. The more recent <code><a href="/docs/linux/man/2-inotify_init1/">inotify_init1</a></code>(2) is like <code><a href="/docs/linux/man/2-inotify_init/">inotify_init</a></code>(2), but has a <i>flags</i> argument that provides access to some extra functionality.</p>
<dt>*</p>
<dd><code><a href="/docs/linux/man/2-inotify_add_watch/">inotify_add_watch</a></code>(2) manipulates the &quot;watch list&quot; associated with an inotify instance. Each item (&quot;watch&quot;) in the watch list specifies the pathname of a file or directory, along with some set of events that the kernel should monitor for the file referred to by that pathname. <code><a href="/docs/linux/man/2-inotify_add_watch/">inotify_add_watch</a></code>(2) either creates a new watch item, or modifies an existing watch. Each watch has a unique &quot;watch descriptor&quot;, an integer returned by <code><a href="/docs/linux/man/2-inotify_add_watch/">inotify_add_watch</a></code>(2) when the watch is created.</p>
<dt>*</p>
<dd>When events occur for monitored files and directories, those events are made available to the application as structured data that can be read from the inotify file descriptor using <code><a href="/docs/linux/man/2-read/">read</a></code>(2) (see below).</p>
<dt>*</p>
<dd><code><a href="/docs/linux/man/2-inotify_rm_watch/">inotify_rm_watch</a></code>(2) removes an item from an inotify watch list.</p>
<dt>*</p>
<dd>When all file descriptors referring to an inotify instance have been closed (using <code><a href="/docs/linux/man/2-close/">close</a></code>(2)), the underlying object and its resources are freed for reuse by the kernel; all associated watches are automatically freed.</dl>
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
<p> <i>wd</i> identifies the watch for which this event occurs. It is one of the watch descriptors returned by a previous call to <code><a href="/docs/linux/man/2-inotify_add_watch/">inotify_add_watch</a></code>(2). <i>mask</i> contains bits that describe the event that occurred (see below). <i>cookie</i> is a unique integer that connects related events. Currently, this is used only for rename events, and allows the resulting pair of <code>IN_MOVED_FROM</code> and <code>IN_MOVED_TO</code> events to be connected by the application. For all other event types, <i>cookie</i> is set to 0. The <i>name</i> field is present only when an event is returned for a file inside a watched directory; it identifies the filename within the watched directory. This filename is null-terminated, and may include further null bytes (&#8216;
