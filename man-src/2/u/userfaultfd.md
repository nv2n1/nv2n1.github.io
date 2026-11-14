---
title: "userfaultfd(2)"
name: "userfaultfd"
section: "2"
letter: "u"
url: "/docs/linux/man/2-userfaultfd/"
description: "userfaultfd – create a file descriptor for handling page faults in user space"
---

<h2 class="name">NAME</h2>
<p> userfaultfd &#8211; create a file descriptor for handling page faults in user space </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;linux/userfaultfd.h&gt;
#include &lt;sys/types.h&gt;
int userfaultfd(int flags);
</code></pre>
<p> <i>Note</i>: There is no glibc wrapper for this system call; see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> <code>userfaultfd</code>() creates a new userfaultfd object that can be used for delegation of page-fault handling to a user-space application, and returns a file descriptor that refers to the new object. The new userfaultfd object is configured using <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2). </p>
<p> Once the userfaultfd object is configured, the application can use <code><a href="/docs/linux/man/2-read/">read</a></code>(2) to receive userfaultfd notifications. The reads from userfaultfd may be blocking or non-blocking, depending on the value of <i>flags</i> used for the creation of the userfaultfd or subsequent calls to <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2). </p>
<p> The following values may be bitwise ORed in <i>flags</i> to change the behavior of <code>userfaultfd</code>():</p>
<dl>
<dt><code>O_CLOEXEC</code></p>
<dd> Enable the close-on-exec flag for the new userfaultfd file descriptor. See the description of the <code>O_CLOEXEC</code> flag in <code><a href="/docs/linux/man/2-open/">open</a></code>(2).</p>
<dt><code>O_NONBLOCK</code></p>
<dd> Enables non-blocking operation for the userfaultfd object. See the description of the <code>O_NONBLOCK</code> flag in <code><a href="/docs/linux/man/2-open/">open</a></code>(2).</dl>
<p> When the last file descriptor referring to a userfaultfd object is closed, all memory ranges that were registered with the object are unregistered and unread events are flushed.</p>
<h3>Usage</h3>
<p> The userfaultfd mechanism is designed to allow a thread in a multithreaded program to perform user-space paging for the other threads in the process. When a page fault occurs for one of the regions registered to the userfaultfd object, the faulting thread is put to sleep and an event is generated that can be read via the userfaultfd file descriptor. The fault-handling thread reads events from this file descriptor and services them using the operations described in <code><a href="/docs/linux/man/2-ioctl_userfaultfd/">ioctl_userfaultfd</a></code>(2). When servicing the page fault events, the fault-handling thread can trigger a wake-up for the sleeping thread. </p>
<p> It is possible for the faulting threads and the fault-handling threads to run in the context of different processes. In this case, these threads may belong to different programs, and the program that executes the faulting threads will not necessarily cooperate with the program that handles the page faults. In such non-cooperative mode, the process that monitors userfaultfd and handles page faults needs to be aware of the changes in the virtual memory layout of the faulting process to avoid memory corruption. </p>
<p> Starting from Linux 4.11, userfaultfd can also notify the fault-handling threads about changes in the virtual memory layout of the faulting process. In addition, if the faulting process invokes <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), the userfaultfd objects associated with the parent may be duplicated into the child process and the userfaultfd monitor will be notified (via the <code>UFFD_EVENT_FORK</code> described below) about the file descriptor associated with the userfault objects created for the child process, which allows the userfaultfd monitor to perform user-space paging for the child process. Unlike page faults which have to be synchronous and require an explicit or implicit wakeup, all other events are delivered asynchronously and the non-cooperative process resumes execution as soon as the userfaultfd manager executes <code><a href="/docs/linux/man/2-read/">read</a></code>(2). The userfaultfd manager should carefully synchronize calls to <code>UFFDIO_COPY</code> with the processing of events. </p>
<p> The current asynchronous model of the event delivery is optimal for single threaded non-cooperative userfaultfd manager implementations.</p>
<h3>Userfaultfd operation</h3>
<p> After the userfaultfd object is created with <code>userfaultfd</code>(), the application must enable it using the <code>UFFDIO_API</code> <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operation. This operation allows a handshake between the kernel and user space to determine the API version and supported features. This operation must be performed before any of the other <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operations described below (or those operations fail with the <code>EINVAL</code> error). </p>
<p> After a successful <code>UFFDIO_API</code> operation, the application then registers memory address ranges using the <code>UFFDIO_REGISTER</code> <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operation. After successful completion of a <code>UFFDIO_REGISTER</code> operation, a page fault occurring in the requested memory range, and satisfying the mode defined at the registration time, will be forwarded by the kernel to the user-space application. The application can then use the <code>UFFDIO_COPY</code> or <code>UFFDIO_ZEROPAGE</code> <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operations to resolve the page fault. </p>
<p> Starting from Linux 4.14, if the application sets the <code>UFFD_FEATURE_SIGBUS</code> feature bit using the <code>UFFDIO_API</code> <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2), no page-fault notification will be forwarded to user space. Instead a <code>SIGBUS</code> signal is delivered to the faulting process. With this feature, userfaultfd can be used for robustness purposes to simply catch any access to areas within the registered address range that do not have pages allocated, without having to listen to userfaultfd events. No userfaultfd monitor will be required for dealing with such memory accesses. For example, this feature can be useful for applications that want to prevent the kernel from automatically allocating pages and filling holes in sparse files when the hole is accessed through a memory mapping. </p>
<p> The <code>UFFD_FEATURE_SIGBUS</code> feature is implicitly inherited through <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) if used in combination with <code>UFFD_FEATURE_FORK</code>. </p>
<p> Details of the various <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operations can be found in <code><a href="/docs/linux/man/2-ioctl_userfaultfd/">ioctl_userfaultfd</a></code>(2). </p>
<p> Since Linux 4.11, events other than page-fault may enabled during <code>UFFDIO_API</code> operation. </p>
<p> Up to Linux 4.11, userfaultfd can be used only with anonymous private memory mappings. Since Linux 4.11, userfaultfd can be also used with hugetlbfs and shared memory mappings. </p>
<h3>Reading from the userfaultfd structure</h3>
<p> Each <code><a href="/docs/linux/man/2-read/">read</a></code>(2) from the userfaultfd file descriptor returns one or more <i>uffd_msg</i> structures, each of which describes a page-fault event or an event required for the non-cooperative userfaultfd usage: </p>
<p> struct uffd_msg {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u8&nbsp;<wbr>&nbsp;event;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Type of event&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8230;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;union&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 flags;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Flags describing fault&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 address;&nbsp;<wbr>&nbsp;/*&nbsp;Faulting address&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;pagefault; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct&nbsp;{&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Since Linux 4.11&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 ufd;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Userfault file descriptor<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;of the child process&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;fork; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct&nbsp;{&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Since Linux 4.11&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 from;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Old address of remapped area&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 to;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;New address of remapped area&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 len;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Original mapping length&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;remap; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct&nbsp;{&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Since Linux 4.11&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 start;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Start address of removed area&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 end;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;End address of removed area&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;remove;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8230;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;arg; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Padding fields omitted&nbsp;*/ } __packed; </p>
<p> If multiple events are available and the supplied buffer is large enough, <code><a href="/docs/linux/man/2-read/">read</a></code>(2) returns as many events as will fit in the supplied buffer. If the buffer supplied to <code><a href="/docs/linux/man/2-read/">read</a></code>(2) is smaller than the size of the <i>uffd_msg</i> structure, the <code><a href="/docs/linux/man/2-read/">read</a></code>(2) fails with the error <code>EINVAL</code>. </p>
<p> The fields set in the <i>uffd_msg</i> structure are as follows:</p>
<dl>
<dt><i>event</i></p>
<dd> The type of event. Depending of the event type, different fields of the <i>arg</i> union represent details required for the event processing. The non-page-fault events are generated only when appropriate feature is enabled during API handshake with <code>UFFDIO_API</code> <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2).</p>
<dt>
<dd> The following values can appear in the <i>event</i> field:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>UFFD_EVENT_PAGEFAULT</code> (since Linux 4.3)</p>
<dd> A page-fault event. The page-fault details are available in the <i>pagefault</i> field.</p>
<dt><code>UFFD_EVENT_FORK</code> (since Linux 4.11)</p>
<dd> Generated when the faulting process invokes <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) (or <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) without the <code>CLONE_VM</code> flag). The event details are available in the <i>fork</i> field.</p>
<dt><code>UFFD_EVENT_REMAP</code> (since Linux 4.11)</p>
<dd> Generated when the faulting process invokes <code><a href="/docs/linux/man/2-mremap/">mremap</a></code>(2). The event details are available in the <i>remap</i> field.</p>
<dt><code>UFFD_EVENT_REMOVE</code> (since Linux 4.11)</p>
<dd> Generated when the faulting process invokes <code><a href="/docs/linux/man/2-madvise/">madvise</a></code>(2) with <code>MADV_DONTNEED</code> or <code>MADV_REMOVE</code> advice. The event details are available in the <i>remove</i> field.</p>
<dt><code>UFFD_EVENT_UNMAP</code> (since Linux 4.11)</p>
<dd> Generated when the faulting process unmaps a memory range, either explicitly using <code><a href="/docs/linux/man/2-munmap/">munmap</a></code>(2) or implicitly during <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) or <code><a href="/docs/linux/man/2-mremap/">mremap</a></code>(2). The event details are available in the <i>remove</i> field.</dl>
</dl>
<dt><i>pagefault.address</i></p>
<dd> The address that triggered the page fault.</p>
<dt><i>pagefault.flags</i></p>
<dd> A bit mask of flags that describe the event. For <code>UFFD_EVENT_PAGEFAULT</code>, the following flag may appear:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>UFFD_PAGEFAULT_FLAG_WRITE</code></p>
<dd> If the address is in a range that was registered with the <code>UFFDIO_REGISTER_MODE_MISSING</code> flag (see <code><a href="/docs/linux/man/2-ioctl_userfaultfd/">ioctl_userfaultfd</a></code>(2)) and this flag is set, this a write fault; otherwise it is a read fault.</dl>
</dl>
<dt><i>fork.ufd</i></p>
<dd> The file descriptor associated with the userfault object created for the child created by <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2).</p>
<dt><i>remap.from</i></p>
<dd> The original address of the memory range that was remapped using <code><a href="/docs/linux/man/2-mremap/">mremap</a></code>(2).</p>
<dt><i>remap.to</i></p>
<dd> The new address of the memory range that was remapped using <code><a href="/docs/linux/man/2-mremap/">mremap</a></code>(2).</p>
<dt><i>remap.len</i></p>
<dd> The original length of the memory range that was remapped using <code><a href="/docs/linux/man/2-mremap/">mremap</a></code>(2).</p>
<dt><i>remove.start</i></p>
<dd> The start address of the memory range that was freed using <code><a href="/docs/linux/man/2-madvise/">madvise</a></code>(2) or unmapped</p>
<dt><i>remove.end</i></p>
<dd> The end address of the memory range that was freed using <code><a href="/docs/linux/man/2-madvise/">madvise</a></code>(2) or unmapped</dl>
<p> A <code><a href="/docs/linux/man/2-read/">read</a></code>(2) on a userfaultfd file descriptor can fail with the following errors:</p>
<dl>
<dt><code>EINVAL</code></p>
<dd> The userfaultfd object has not yet been enabled using the <code>UFFDIO_API</code> <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operation</dl>
<p> If the <code>O_NONBLOCK</code> flag is enabled in the associated open file description, the userfaultfd file descriptor can be monitored with <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), <code><a href="/docs/linux/man/2-select/">select</a></code>(2), and <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7). When events are available, the file descriptor indicates as readable. If the <code>O_NONBLOCK</code> flag is not enabled, then <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2) (always) indicates the file as having a <code>POLLERR</code> condition, and <code><a href="/docs/linux/man/2-select/">select</a></code>(2) indicates the file descriptor as both readable and writable.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>userfaultfd</code>() returns a new file descriptor that refers to the userfaultfd object. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd> An unsupported value was specified in <i>flags</i>.</p>
<dt><code>EMFILE</code></p>
<dd> The per-process limit on the number of open file descriptors has been reached</p>
<dt><code>ENFILE</code></p>
<dd> The system-wide limit on the total number of open files has been reached.</p>
<dt><code>ENOMEM</code></p>
<dd> Insufficient kernel memory was available.</p>
<dt><code>EPERM</code> (since Linux 5.2)</p>
<dd> The caller is not privileged (does not have the <code>CAP_SYS_PTRACE</code> capability in the initial user namespace), and <i>/proc/sys/vm/unprivileged_userfaultfd</i> has the value 0.</dl>
<h2>VERSIONS</h2>
<p> The <code>userfaultfd</code>() system call first appeared in Linux 4.3. </p>
<p> The support for hugetlbfs and shared memory areas and non-page-fault events was added in Linux 4.11</p>
<h2>CONFORMING TO</h2>
<p> <code>userfaultfd</code>() is Linux-specific and should not be used in programs intended to be portable.</p>
<h2>NOTES</h2>
<p> Glibc does not provide a wrapper for this system call; call it using <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2). </p>
<p> The userfaultfd mechanism can be used as an alternative to traditional user-space paging techniques based on the use of the <code>SIGSEGV</code> signal and <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2). It can also be used to implement lazy restore for checkpoint/restore mechanisms, as well as post-copy migration to allow (nearly) uninterrupted execution when transferring virtual machines and Linux containers from one host to another.</p>
<h2>BUGS</h2>
<p> If the <code>UFFD_FEATURE_EVENT_FORK</code> is enabled and a system call from the <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) family is interrupted by a signal or failed, a stale userfaultfd descriptor might be created. In this case, a spurious <code>UFFD_EVENT_FORK</code> will be delivered to the userfaultfd monitor.</p>
<h2>EXAMPLES</h2>
<p> The program below demonstrates the use of the userfaultfd mechanism. The program creates two threads, one of which acts as the page-fault handler for the process, for the pages in a demand-page zero region created using <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2). </p>
<p> The program takes one command-line argument, which is the number of pages that will be created in a mapping whose page faults will be handled via userfaultfd. After creating a userfaultfd object, the program then creates an anonymous private mapping of the specified size and registers the address range of that mapping using the <code>UFFDIO_REGISTER</code> <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operation. The program then creates a second thread that will perform the task of handling page faults. </p>
<p> The main thread then walks through the pages of the mapping fetching bytes from successive pages. Because the pages have not yet been accessed, the first access of a byte in each page will trigger a page-fault event on the userfaultfd file descriptor. </p>
<p> Each of the page-fault events is handled by the second thread, which sits in a loop processing input from the userfaultfd file descriptor. In each loop iteration, the second thread first calls <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2) to check the state of the file descriptor, and then reads an event from the file descriptor. All such events should be <code>UFFD_EVENT_PAGEFAULT</code> events, which the thread handles by copying a page of data into the faulting region using the <code>UFFDIO_COPY</code> <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operation. </p>
<p> The following is an example of what we see when running the program: </p>
<p> $ <code>./userfaultfd_demo 3</code> Address returned by mmap() = 0x7fd30106c000 </p>
<p> fault_handler_thread():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;poll()&nbsp;returns: nready&nbsp;=&nbsp;1;&nbsp;POLLIN&nbsp;=&nbsp;1;&nbsp;POLLERR&nbsp;=&nbsp;0<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;UFFD_EVENT_PAGEFAULT event: flags&nbsp;=&nbsp;0;&nbsp;address&nbsp;=&nbsp;7fd30106c00f<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(uffdio_copy.copy returned 4096) Read address 0x7fd30106c00f in main(): A Read address 0x7fd30106c40f in main(): A Read address 0x7fd30106c80f in main(): A Read address 0x7fd30106cc0f in main(): A </p>
<p> fault_handler_thread():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;poll()&nbsp;returns: nready&nbsp;=&nbsp;1;&nbsp;POLLIN&nbsp;=&nbsp;1;&nbsp;POLLERR&nbsp;=&nbsp;0<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;UFFD_EVENT_PAGEFAULT event: flags&nbsp;=&nbsp;0;&nbsp;address&nbsp;=&nbsp;7fd30106d00f<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(uffdio_copy.copy returned 4096) Read address 0x7fd30106d00f in main(): B Read address 0x7fd30106d40f in main(): B Read address 0x7fd30106d80f in main(): B Read address 0x7fd30106dc0f in main(): B </p>
<p> fault_handler_thread():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;poll()&nbsp;returns: nready&nbsp;=&nbsp;1;&nbsp;POLLIN&nbsp;=&nbsp;1;&nbsp;POLLERR&nbsp;=&nbsp;0<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;UFFD_EVENT_PAGEFAULT event: flags&nbsp;=&nbsp;0;&nbsp;address&nbsp;=&nbsp;7fd30106e00f<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(uffdio_copy.copy returned 4096) Read address 0x7fd30106e00f in main(): C Read address 0x7fd30106e40f in main(): C Read address 0x7fd30106e80f in main(): C Read address 0x7fd30106ec0f in main(): C</p>
<h3>Program source</h3>
<p> /* userfaultfd_demo.c </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Licensed under the GNU General Public License version 2 or later. */ #define _GNU_SOURCE #include &lt;inttypes.h&gt; #include &lt;sys/types.h&gt; #include &lt;stdio.h&gt; #include &lt;linux/userfaultfd.h&gt; #include &lt;pthread.h&gt; #include &lt;errno.h&gt; #include &lt;unistd.h&gt; #include &lt;stdlib.h&gt; #include &lt;fcntl.h&gt; #include &lt;signal.h&gt; #include &lt;poll.h&gt; #include &lt;string.h&gt; #include &lt;sys/mman.h&gt; #include &lt;sys/syscall.h&gt; #include &lt;sys/ioctl.h&gt; #include &lt;poll.h&gt; </p>
<p> #define errExit(msg) do { perror(msg); exit(EXIT_FAILURE); \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;while&nbsp;(0) </p>
<p> static int page_size; </p>
<p> static void * fault_handler_thread(void *arg) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;static struct uffd_msg msg;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Data read from userfaultfd&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;static int fault_cnt&nbsp;=&nbsp;0;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Number of faults so far handled&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long uffd;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;userfaultfd file descriptor&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;static char&nbsp;*page&nbsp;=&nbsp;NULL;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct uffdio_copy uffdio_copy;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ssize_t nread; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uffd&nbsp;=&nbsp;(long)&nbsp;arg; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Create a page that will be copied into the faulting region&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(page&nbsp;==&nbsp;NULL)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;page&nbsp;=&nbsp;mmap(NULL, page_size, PROT_READ | PROT_WRITE,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(page&nbsp;==&nbsp;MAP_FAILED)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;mmap&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Loop, handling incoming events on the userfaultfd<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;file descriptor&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(;;)&nbsp;{ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;See what poll()&nbsp;tells us about the userfaultfd&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct pollfd pollfd;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int nready;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pollfd.fd&nbsp;=&nbsp;uffd;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pollfd.events&nbsp;=&nbsp;POLLIN;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nready&nbsp;=&nbsp;poll(&amp;pollfd, 1, -1);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(nready&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;poll&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;
fault_handler_thread():
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;poll()&nbsp;returns: nready&nbsp;=&nbsp;%d;&nbsp;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;POLLIN&nbsp;=&nbsp;%d;&nbsp;POLLERR&nbsp;=&nbsp;%d
&quot;, nready,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(pollfd.revents&nbsp;&amp;&nbsp;POLLIN)&nbsp;!=&nbsp;0,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(pollfd.revents&nbsp;&amp;&nbsp;POLLERR)&nbsp;!=&nbsp;0); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Read an event from the userfaultfd&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nread&nbsp;=&nbsp;read(uffd,&nbsp;&amp;msg, sizeof(msg));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(nread&nbsp;==&nbsp;0)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;EOF on userfaultfd!
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(nread&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;read&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;We expect only one kind of event;&nbsp;verify that assumption&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(msg.event&nbsp;!=&nbsp;UFFD_EVENT_PAGEFAULT)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Unexpected event on userfaultfd
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Display info about the page-fault event&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;UFFD_EVENT_PAGEFAULT event:&nbsp;&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;flags&nbsp;=&nbsp;%&quot;PRIx64&quot;;&nbsp;&quot;, msg.arg.pagefault.flags);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;address&nbsp;=&nbsp;%&quot;PRIx64&quot;
&quot;, msg.arg.pagefault.address); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Copy the page pointed to by&nbsp;&#8216;page&#8217;&nbsp;into the faulting<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;region. Vary the contents that are copied in, so that it<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;is more obvious that each fault is handled separately.&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;memset(page,&nbsp;&#8216;A&#8217;&nbsp;+&nbsp;fault_cnt&nbsp;%&nbsp;20, page_size);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fault_cnt++; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uffdio_copy.src&nbsp;=&nbsp;(unsigned long)&nbsp;page; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;We need to handle page faults in units of pages(!).<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;So, round faulting address down to page boundary&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uffdio_copy.dst&nbsp;=&nbsp;(unsigned long)&nbsp;msg.arg.pagefault.address&nbsp;&amp;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;~(page_size &#8211; 1);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uffdio_copy.len&nbsp;=&nbsp;page_size;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uffdio_copy.mode&nbsp;=&nbsp;0;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uffdio_copy.copy&nbsp;=&nbsp;0;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(ioctl(uffd, UFFDIO_COPY,&nbsp;&amp;uffdio_copy)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;ioctl-UFFDIO_COPY&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(uffdio_copy.copy returned&nbsp;%&quot;PRId64&quot;)
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uffdio_copy.copy);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} } </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long uffd;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;userfaultfd file descriptor&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*addr;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Start of region handled by userfaultfd&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t len;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Length of region handled by userfaultfd&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pthread_t thr;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;ID of thread that handles page faults&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct uffdio_api uffdio_api;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct uffdio_register uffdio_register;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int s; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;!=&nbsp;2)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s num-pages
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;page_size&nbsp;=&nbsp;sysconf(_SC_PAGE_SIZE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;len&nbsp;=&nbsp;strtoull(argv[1], NULL, 0)&nbsp;*&nbsp;page_size; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Create and enable userfaultfd object&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uffd&nbsp;=&nbsp;syscall(__NR_userfaultfd, O_CLOEXEC | O_NONBLOCK);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(uffd&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;userfaultfd&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uffdio_api.api&nbsp;=&nbsp;UFFD_API;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uffdio_api.features&nbsp;=&nbsp;0;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(ioctl(uffd, UFFDIO_API,&nbsp;&amp;uffdio_api)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;ioctl-UFFDIO_API&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Create a private anonymous mapping. The memory will be<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;demand-zero paged&#8211;that is, not yet allocated. When we<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;actually touch the memory, it will be allocated via<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the userfaultfd.&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;addr&nbsp;=&nbsp;mmap(NULL, len, PROT_READ | PROT_WRITE,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(addr&nbsp;==&nbsp;MAP_FAILED)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;mmap&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Address returned by mmap()&nbsp;=&nbsp;%p
&quot;, addr); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Register the memory range of the mapping we just created for<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handling by the userfaultfd object. In mode, we request to track<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;missing pages&nbsp;(i.e., pages that have not yet been faulted in).&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uffdio_register.range.start&nbsp;=&nbsp;(unsigned long)&nbsp;addr;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uffdio_register.range.len&nbsp;=&nbsp;len;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uffdio_register.mode&nbsp;=&nbsp;UFFDIO_REGISTER_MODE_MISSING;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(ioctl(uffd, UFFDIO_REGISTER,&nbsp;&amp;uffdio_register)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;ioctl-UFFDIO_REGISTER&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Create a thread that will process the userfaultfd events&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;s&nbsp;=&nbsp;pthread_create(&amp;thr, NULL, fault_handler_thread,&nbsp;(void&nbsp;*)&nbsp;uffd);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(s&nbsp;!=&nbsp;0)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errno&nbsp;=&nbsp;s;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;pthread_create&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Main thread now touches memory in the mapping, touching<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;locations 1024 bytes apart. This will trigger userfaultfd<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;events for all pages in the region.&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int l;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;l&nbsp;=&nbsp;0xf;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Ensure that faulting address is not on a page<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;boundary, in order to test that we correctly<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle that case in fault_handling_thread()&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while&nbsp;(l&nbsp;&lt;&nbsp;len)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char c&nbsp;=&nbsp;addr[l];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Read address&nbsp;%p in main():&nbsp;&quot;, addr&nbsp;+&nbsp;l);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%c
&quot;, c);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;l&nbsp;+=&nbsp;1024;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;usleep(100000);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Slow things down a little&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2), <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2), <code><a href="/docs/linux/man/2-ioctl_userfaultfd/">ioctl_userfaultfd</a></code>(2), <code><a href="/docs/linux/man/2-madvise/">madvise</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) </p>
<p> <i>Documentation/admin-guide/mm/userfaultfd.rst</i> in the Linux kernel source tree</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
