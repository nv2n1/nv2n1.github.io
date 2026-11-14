---
title: "capabilities(7)"
name: "capabilities"
section: "7"
letter: "c"
url: "/docs/linux/man/7-capabilities/"
description: "capabilities – overview of Linux capabilities"
---

<p>capabilities &#8211; overview of Linux capabilities</p>
<h2>Description</h2>
<p>For the purpose of performing permission checks, traditional UNIX implementations distinguish two categories of processes: <i>privileged</i> processes (whose effective user ID is 0, referred to as superuser or root), and <i>unprivileged</i> processes (whose effective UID is nonzero). Privileged processes bypass all kernel permission checks, while unprivileged processes are subject to full permission checking based on the process&#8217;s credentials (usually: effective UID, effective GID, and supplementary group list). </p>
<p> Starting with kernel 2.2, Linux divides the privileges traditionally associated with superuser into distinct units, known as <i>capabilities</i>, which can be independently enabled and disabled. Capabilities are a per-thread attribute.</p>
<h3>Capabilities list</h3>
<p>The following list shows the capabilities implemented on Linux, and the operations or behaviors that each capability permits:</p>
<dl>
<dt><code>CAP_AUDIT_CONTROL</code> (since Linux 2.6.11)</p>
<dd>Enable and disable kernel auditing; change auditing filter rules; retrieve auditing status and filtering rules.</p>
<dt><code>CAP_AUDIT_READ</code> (since Linux 3.16)</p>
<dd>Allow reading the audit log via a multicast netlink socket.</p>
<dt><code>CAP_AUDIT_WRITE</code> (since Linux 2.6.11)</p>
<dd>Write records to kernel auditing log.</p>
<dt><code>CAP_BLOCK_SUSPEND</code> (since Linux 3.5)</p>
<dd>Employ features that can block system suspend (<code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7) <code>EPOLLWAKEUP</code>, <i>/proc/sys/wake_lock</i>).</p>
<dt><code>CAP_BPF</code> (since Linux 5.8)</p>
<dd>Employ privileged BPF operations; see <code><a href="/docs/linux/man/2-bpf/">bpf</a></code>(2) and <code><a href="/docs/linux/man/7-bpf-helpers/">bpf-helpers</a></code>(7).</p>
<dd>This capability was added in Linux 5.8 to separate out BPF functionality from the overloaded <code>CAP_SYS_ADMIN</code> capability.</p>
<dt><code>CAP_CHECKPOINT_RESTORE</code> (since Linux 5.9)</p>
<dd>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>Update <i>/proc/sys/kernel/ns_last_pid</i> (see <code><a href="/docs/linux/man/7-pid_namespaces/">pid_namespaces</a></code>(7));</p>
<dt>*</p>
<dd>employ the <i>set_tid</i> feature of <code><a href="/docs/linux/man/2-clone3/">clone3</a></code>(2);</p>
<dt>*</p>
<dd>read the contents of the symbolic links in <i>/proc/[pid]/map_files</i> for other processes.</dl>
</dl>
<dd>This capability was added in Linux 5.9 to separate out checkpoint/restore functionality from the overloaded <code>CAP_SYS_ADMIN</code> capability.</p>
<dt><code>CAP_CHOWN</code></p>
<dd>Make arbitrary changes to file UIDs and GIDs (see <code><a href="/docs/linux/man/2-chown/">chown</a></code>(2)).</p>
<dt><code>CAP_DAC_OVERRIDE</code></p>
<dd>Bypass file read, write, and execute permission checks. (DAC is an abbreviation of &quot;discretionary access control&quot;.)</p>
<dt><code>CAP_DAC_READ_SEARCH</code></p>
<dd>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>Bypass file read permission checks and directory read and execute permission checks;</p>
<dt>*</p>
<dd>invoke <code><a href="/docs/linux/man/2-open_by_handle_at/">open_by_handle_at</a></code>(2);</p>
<dt>*</p>
<dd>use the <code><a href="/docs/linux/man/2-linkat/">linkat</a></code>(2) <code>AT_EMPTY_PATH</code> flag to create a link to a file referred to by a file descriptor.</dl>
</dl>
<dt><code>CAP_FOWNER</code></p>
<dd>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>Bypass permission checks on operations that normally require the filesystem UID of the process to match the UID of the file (e.g., <code><a href="/docs/linux/man/2-chmod/">chmod</a></code>(2), <code><a href="/docs/linux/man/2-utime/">utime</a></code>(2)), excluding those operations covered by <code>CAP_DAC_OVERRIDE</code> and <code>CAP_DAC_READ_SEARCH</code>;</p>
<dt>*</p>
<dd>set inode flags (see <code><a href="/docs/linux/man/2-ioctl_iflags/">ioctl_iflags</a></code>(2)) on arbitrary files;</p>
<dt>*</p>
<dd>set Access Control Lists (ACLs) on arbitrary files;</p>
<dt>*</p>
<dd>ignore directory sticky bit on file deletion;</p>
<dt>*</p>
<dd>modify <i>user</i> extended attributes on sticky directory owned by any user;</p>
<dt>*</p>
<dd>specify <code>O_NOATIME</code> for arbitrary files in <code><a href="/docs/linux/man/2-open/">open</a></code>(2) and <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2).</dl>
</dl>
<dt><code>CAP_FSETID</code></p>
<dd>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>Don&#8217;t clear set-user-ID and set-group-ID mode bits when a file is modified;</p>
<dt>*</p>
<dd>set the set-group-ID bit for a file whose GID does not match the filesystem or any of the supplementary GIDs of the calling process.</dl>
</dl>
<dt><code>CAP_IPC_LOCK</code></p>
<dd>Lock memory (<code><a href="/docs/linux/man/2-mlock/">mlock</a></code>(2), <code><a href="/docs/linux/man/2-mlockall/">mlockall</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-shmctl/">shmctl</a></code>(2)).</p>
<dt><code>CAP_IPC_OWNER</code></p>
<dd>Bypass permission checks for operations on System V IPC objects.</p>
<dt><code>CAP_KILL</code></p>
<dd>Bypass permission checks for sending signals (see <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2)). This includes use of the <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) <code>KDSIGACCEPT</code> operation.</p>
<dt><code>CAP_LEASE</code> (since Linux 2.4)</p>
<dd>Establish leases on arbitrary files (see <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2)).</p>
<dt><code>CAP_LINUX_IMMUTABLE</code></p>
<dd>Set the <code>FS_APPEND_FL</code> and <code>FS_IMMUTABLE_FL</code> inode flags (see <code><a href="/docs/linux/man/2-ioctl_iflags/">ioctl_iflags</a></code>(2)).</p>
<dt><code>CAP_MAC_ADMIN</code> (since Linux 2.6.25)</p>
<dd>Allow MAC configuration or state changes. Implemented for the Smack Linux Security Module (LSM).</p>
<dt><code>CAP_MAC_OVERRIDE</code> (since Linux 2.6.25)</p>
<dd>Override Mandatory Access Control (MAC). Implemented for the Smack LSM.</p>
<dt><code>CAP_MKNOD</code> (since Linux 2.4)</p>
<dd>Create special files using <code><a href="/docs/linux/man/2-mknod/">mknod</a></code>(2).</p>
<dt><code>CAP_NET_ADMIN</code></p>
<dd>Perform various network-related operations:</p>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>interface configuration;</p>
<dt>*</p>
<dd>administration of IP firewall, masquerading, and accounting;</p>
<dt>*</p>
<dd>modify routing tables;</p>
<dt>*</p>
<dd>bind to any address for transparent proxying;</p>
<dt>*</p>
<dd>set type-of-service (TOS);</p>
<dt>*</p>
<dd>clear driver statistics;</p>
<dt>*</p>
<dd>set promiscuous mode;</p>
<dt>*</p>
<dd>enabling multicasting;</p>
<dt>*</p>
<dd>use <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2) to set the following socket options: <code>SO_DEBUG</code>, <code>SO_MARK</code>, <code>SO_PRIORITY</code> (for a priority outside the range 0 to 6), <code>SO_RCVBUFFORCE</code>, and <code>SO_SNDBUFFORCE</code>.</dl>
</dl>
<dt><code>CAP_NET_BIND_SERVICE</code></p>
<dd>Bind a socket to Internet domain privileged ports (port numbers less than 1024).</p>
<dt><code>CAP_NET_BROADCAST</code></p>
<dd>(Unused) Make socket broadcasts, and listen to multicasts.</p>
<dt><code>CAP_NET_RAW</code></p>
<dd>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>Use RAW and PACKET sockets;</p>
<dt>*</p>
<dd>bind to any address for transparent proxying.</dl>
</dl>
<dt><code>CAP_PERFMON</code> (since Linux 5.8)</p>
<dd>Employ various performance-monitoring mechanisms, including:</p>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>call <code><a href="/docs/linux/man/2-perf_event_open/">perf_event_open</a></code>(2);</p>
<dt>*</p>
<dd>employ various BPF operations that have performance implications.</dl>
</dl>
<dd>This capability was added in Linux 5.8 to separate out performance monitoring functionality from the overloaded <code>CAP_SYS_ADMIN</code> capability. See also the kernel source file <i>Documentation/admin-guide/perf-security.rst</i>.</p>
<dt><code>CAP_SETGID</code></p>
<dd>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>Make arbitrary manipulations of process GIDs and supplementary GID list;</p>
<dt>*</p>
<dd>forge GID when passing socket credentials via UNIX domain sockets;</p>
<dt>*</p>
<dd>write a group ID mapping in a user namespace (see <code><a href="/docs/linux/man/7-user_namespaces/">user_namespaces</a></code>(7)).</dl>
</dl>
<dt><code>CAP_SETFCAP</code> (since Linux 2.6.24)</p>
<dd>Set arbitrary capabilities on a file.</p>
<dt><code>CAP_SETPCAP</code></p>
<dd>If file capabilities are supported (i.e., since Linux 2.6.24): add any capability from the calling thread&#8217;s bounding set to its inheritable set; drop capabilities from the bounding set (via <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2) <code>PR_CAPBSET_DROP</code>); make changes to the <i>securebits</i> flags.</p>
<dd>If file capabilities are not supported (i.e., kernels before Linux 2.6.24): grant or remove any capability in the caller&#8217;s permitted capability set to or from any other process. (This property of <code>CAP_SETPCAP</code> is not available when the kernel is configured to support file capabilities, since <code>CAP_SETPCAP</code> has entirely different semantics for such kernels.)</p>
<dt><code>CAP_SETUID</code></p>
<dd>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>Make arbitrary manipulations of process UIDs (<code><a href="/docs/linux/man/2-setuid/">setuid</a></code>(2), <code><a href="/docs/linux/man/2-setreuid/">setreuid</a></code>(2), <code><a href="/docs/linux/man/2-setresuid/">setresuid</a></code>(2), <code><a href="/docs/linux/man/2-setfsuid/">setfsuid</a></code>(2));</p>
<dt>*</p>
<dd>forge UID when passing socket credentials via UNIX domain sockets;</p>
<dt>*</p>
<dd>write a user ID mapping in a user namespace (see <code><a href="/docs/linux/man/7-user_namespaces/">user_namespaces</a></code>(7)).</dl>
</dl>
<dt><code>CAP_SYS_ADMIN</code></p>
<dd><i>Note</i>: this capability is overloaded; see <i>Notes to kernel developers</i>, below.</p>
<dd>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>Perform a range of system administration operations including: <code><a href="/docs/linux/man/2-quotactl/">quotactl</a></code>(2), <code><a href="/docs/linux/man/2-mount/">mount</a></code>(2), <code><a href="/docs/linux/man/2-umount/">umount</a></code>(2), <code><a href="/docs/linux/man/2-pivot_root/">pivot_root</a></code>(2), <code><a href="/docs/linux/man/2-swapon/">swapon</a></code>(2), <code><a href="/docs/linux/man/2-swapoff/">swapoff</a></code>(2), <code><a href="/docs/linux/man/2-sethostname/">sethostname</a></code>(2), and <code><a href="/docs/linux/man/2-setdomainname/">setdomainname</a></code>(2);</p>
<dt>*</p>
<dd>perform privileged <code><a href="/docs/linux/man/2-syslog/">syslog</a></code>(2) operations (since Linux 2.6.37, <code>CAP_SYSLOG</code> should be used to permit such operations);</p>
<dt>*</p>
<dd>perform <code>VM86_REQUEST_IRQ</code> <code><a href="/docs/linux/man/2-vm86/">vm86</a></code>(2) command;</p>
<dt>*</p>
<dd>access the same checkpoint/restore functionality that is governed by <code>CAP_CHECKPOINT_RESTORE</code> (but the latter, weaker capability is preferred for accessing that functionality).</p>
<dt>*</p>
<dd>perform the same BPF operations as are governed by <code>CAP_BPF</code> (but the latter, weaker capability is preferred for accessing that functionality).</p>
<dt>*</p>
<dd>employ the same performance monitoring mechanisms as are governed by <code>CAP_PERFMON</code> (but the latter, weaker capability is preferred for accessing that functionality).</p>
<dt>*</p>
<dd>perform <code>IPC_SET</code> and <code>IPC_RMID</code> operations on arbitrary System V IPC objects;</p>
<dt>*</p>
<dd>override <code>RLIMIT_NPROC</code> resource limit;</p>
<dt>*</p>
<dd>perform operations on <i>trusted</i> and <i>security</i> extended attributes (see <code><a href="/docs/linux/man/7-xattr/">xattr</a></code>(7));</p>
<dt>*</p>
<dd>use <code><a href="/docs/linux/man/2-lookup_dcookie/">lookup_dcookie</a></code>(2);</p>
<dt>*</p>
<dd>use <code><a href="/docs/linux/man/2-ioprio_set/">ioprio_set</a></code>(2) to assign <code>IOPRIO_CLASS_RT</code> and (before Linux 2.6.25) <code>IOPRIO_CLASS_IDLE</code> I/O scheduling classes;</p>
<dt>*</p>
<dd>forge PID when passing socket credentials via UNIX domain sockets;</p>
<dt>*</p>
<dd>exceed <i>/proc/sys/fs/file-max</i>, the system-wide limit on the number of open files, in system calls that open files (e.g., <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2), <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-pipe/">pipe</a></code>(2));</p>
<dt>*</p>
<dd>employ <code>CLONE_*</code> flags that create new namespaces with <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) and <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2) (but, since Linux 3.8, creating user namespaces does not require any capability);</p>
<dt>*</p>
<dd>access privileged <i>perf</i> event information;</p>
<dt>*</p>
<dd>call <code><a href="/docs/linux/man/2-setns/">setns</a></code>(2) (requires <code>CAP_SYS_ADMIN</code> in the <i>target</i> namespace);</p>
<dt>*</p>
<dd>call <code><a href="/docs/linux/man/2-fanotify_init/">fanotify_init</a></code>(2);</p>
<dt>*</p>
<dd>perform privileged <code>KEYCTL_CHOWN</code> and <code>KEYCTL_SETPERM</code> <code><a href="/docs/linux/man/2-keyctl/">keyctl</a></code>(2) operations;</p>
<dt>*</p>
<dd>perform <code><a href="/docs/linux/man/2-madvise/">madvise</a></code>(2) <code>MADV_HWPOISON</code> operation;</p>
<dt>*</p>
<dd>employ the <code>TIOCSTI</code> <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) to insert characters into the input queue of a terminal other than the caller&#8217;s controlling terminal;</p>
<dt>*</p>
<dd>employ the obsolete <code><a href="/docs/linux/man/2-nfsservctl/">nfsservctl</a></code>(2) system call;</p>
<dt>*</p>
<dd>employ the obsolete <code><a href="/docs/linux/man/2-bdflush/">bdflush</a></code>(2) system call;</p>
<dt>*</p>
<dd>perform various privileged block-device <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operations;</p>
<dt>*</p>
<dd>perform various privileged filesystem <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operations;</p>
<dt>*</p>
<dd>perform privileged <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operations on the <i>/dev/random</i> device (see <code><a href="/docs/linux/man/4-random/">random</a></code>(4));</p>
<dt>*</p>
<dd>install a <code><a href="/docs/linux/man/2-seccomp/">seccomp</a></code>(2) filter without first having to set the <i>no_new_privs</i> thread attribute;</p>
<dt>*</p>
<dd>modify allow/deny rules for device control groups;</p>
<dt>*</p>
<dd>employ the <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2) <code>PTRACE_SECCOMP_GET_FILTER</code> operation to dump tracee&#8217;s seccomp filters;</p>
<dt>*</p>
<dd>employ the <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2) <code>PTRACE_SETOPTIONS</code> operation to suspend the tracee&#8217;s seccomp protections (i.e., the <code>PTRACE_O_SUSPEND_SECCOMP</code> flag);</p>
<dt>*</p>
<dd>perform administrative operations on many device drivers;</p>
<dt>*</p>
<dd>modify autogroup nice values by writing to <i>/proc/[pid]/autogroup</i> (see <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7)).</dl>
</dl>
<dt><code>CAP_SYS_BOOT</code></p>
<dd>Use <code><a href="/docs/linux/man/2-reboot/">reboot</a></code>(2) and <code><a href="/docs/linux/man/2-kexec_load/">kexec_load</a></code>(2).</p>
<dt><code>CAP_SYS_CHROOT</code></p>
<dd>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>Use <code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2);</p>
<dt>*</p>
<dd>change mount namespaces using <code><a href="/docs/linux/man/2-setns/">setns</a></code>(2).</dl>
</dl>
<dt><code>CAP_SYS_MODULE</code></p>
<dd>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>Load and unload kernel modules (see <code><a href="/docs/linux/man/2-init_module/">init_module</a></code>(2) and <code><a href="/docs/linux/man/2-delete_module/">delete_module</a></code>(2));</p>
<dt>*</p>
<dd>in kernels before 2.6.25: drop capabilities from the system-wide capability bounding set.</dl>
</dl>
<dt><code>CAP_SYS_NICE</code></p>
<dd>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>Lower the process nice value (<code><a href="/docs/linux/man/2-nice/">nice</a></code>(2), <code><a href="/docs/linux/man/2-setpriority/">setpriority</a></code>(2)) and change the nice value for arbitrary processes;</p>
<dt>*</p>
<dd>set real-time scheduling policies for calling process, and set scheduling policies and priorities for arbitrary processes (<code><a href="/docs/linux/man/2-sched_setscheduler/">sched_setscheduler</a></code>(2), <code><a href="/docs/linux/man/2-sched_setparam/">sched_setparam</a></code>(2), <code><a href="/docs/linux/man/2-sched_setattr/">sched_setattr</a></code>(2));</p>
<dt>*</p>
<dd>set CPU affinity for arbitrary processes (<code><a href="/docs/linux/man/2-sched_setaffinity/">sched_setaffinity</a></code>(2));</p>
<dt>*</p>
<dd>set I/O scheduling class and priority for arbitrary processes (<code><a href="/docs/linux/man/2-ioprio_set/">ioprio_set</a></code>(2));</p>
<dt>*</p>
<dd>apply <code><a href="/docs/linux/man/2-migrate_pages/">migrate_pages</a></code>(2) to arbitrary processes and allow processes to be migrated to arbitrary nodes;</p>
<dt>*</p>
<dd>apply <code><a href="/docs/linux/man/2-move_pages/">move_pages</a></code>(2) to arbitrary processes;</p>
<dt>*</p>
<dd>use the <code>MPOL_MF_MOVE_ALL</code> flag with <code><a href="/docs/linux/man/2-mbind/">mbind</a></code>(2) and <code><a href="/docs/linux/man/2-move_pages/">move_pages</a></code>(2).</dl>
</dl>
<dt><code>CAP_SYS_PACCT</code></p>
<dd>Use <code><a href="/docs/linux/man/2-acct/">acct</a></code>(2).</p>
<dt><code>CAP_SYS_PTRACE</code></p>
<dd>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>Trace arbitrary processes using <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2);</p>
<dt>*</p>
<dd>apply <code><a href="/docs/linux/man/2-get_robust_list/">get_robust_list</a></code>(2) to arbitrary processes;</p>
<dt>*</p>
<dd>transfer data to or from the memory of arbitrary processes using <code><a href="/docs/linux/man/2-process_vm_readv/">process_vm_readv</a></code>(2) and <code><a href="/docs/linux/man/2-process_vm_writev/">process_vm_writev</a></code>(2);</p>
<dt>*</p>
<dd>inspect processes using <code><a href="/docs/linux/man/2-kcmp/">kcmp</a></code>(2).</dl>
</dl>
<dt><code>CAP_SYS_RAWIO</code></p>
<dd>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>Perform I/O port operations (<code><a href="/docs/linux/man/2-iopl/">iopl</a></code>(2) and <code><a href="/docs/linux/man/2-ioperm/">ioperm</a></code>(2));</p>
<dt>*</p>
<dd>access <i>/proc/kcore</i>;</p>
<dt>*</p>
<dd>employ the <code>FIBMAP</code> <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operation;</p>
<dt>*</p>
<dd>open devices for accessing x86 model-specific registers (MSRs, see <code><a href="/docs/linux/man/4-msr/">msr</a></code>(4));</p>
<dt>*</p>
<dd>update <i>/proc/sys/vm/mmap_min_addr</i>;</p>
<dt>*</p>
<dd>create memory mappings at addresses below the value specified by <i>/proc/sys/vm/mmap_min_addr</i>;</p>
<dt>*</p>
<dd>map files in <i>/proc/bus/pci</i>;</p>
<dt>*</p>
<dd>open <i>/dev/mem</i> and <i>/dev/kmem</i>;</p>
<dt>*</p>
<dd>perform various SCSI device commands;</p>
<dt>*</p>
<dd>perform certain operations on <code><a href="/docs/linux/man/4-hpsa/">hpsa</a></code>(4) and <code><a href="/docs/linux/man/4-cciss/">cciss</a></code>(4) devices;</p>
<dt>*</p>
<dd>perform a range of device-specific operations on other devices.</dl>
</dl>
<dt><code>CAP_SYS_RESOURCE</code></p>
<dd>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>Use reserved space on ext2 filesystems;</p>
<dt>*</p>
<dd>make <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) calls controlling ext3 journaling;</p>
<dt>*</p>
<dd>override disk quota limits;</p>
<dt>*</p>
<dd>increase resource limits (see <code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></code>(2));</p>
<dt>*</p>
<dd>override <code>RLIMIT_NPROC</code> resource limit;</p>
<dt>*</p>
<dd>override maximum number of consoles on console allocation;</p>
<dt>*</p>
<dd>override maximum number of keymaps;</p>
<dt>*</p>
<dd>allow more than 64hz interrupts from the real-time clock;</p>
<dt>*</p>
<dd>raise <i>msg_qbytes</i> limit for a System V message queue above the limit in <i>/proc/sys/kernel/msgmnb</i> (see <code><a href="/docs/linux/man/2-msgop/">msgop</a></code>(2) and <code><a href="/docs/linux/man/2-msgctl/">msgctl</a></code>(2));</p>
<dt>*</p>
<dd>allow the <code>RLIMIT_NOFILE</code> resource limit on the number of &quot;in-flight&quot; file descriptors to be bypassed when passing file descriptors to another process via a UNIX domain socket (see <code><a href="/docs/linux/man/7-unix/">unix</a></code>(7));</p>
<dt>*</p>
<dd>override the <i>/proc/sys/fs/pipe-size-max</i> limit when setting the capacity of a pipe using the <code>F_SETPIPE_SZ</code> <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) command;</p>
<dt>*</p>
<dd>use <code>F_SETPIPE_SZ</code> to increase the capacity of a pipe above the limit specified by <i>/proc/sys/fs/pipe-max-size</i>;</p>
<dt>*</p>
<dd>override <i>/proc/sys/fs/mqueue/queues_max,</i> <i>/proc/sys/fs/mqueue/msg_max,</i> and <i>/proc/sys/fs/mqueue/msgsize_max</i> limits when creating POSIX message queues (see <code><a href="/docs/linux/man/7-mq_overview/">mq_overview</a></code>(7));</p>
<dt>*</p>
<dd>employ the <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2) <code>PR_SET_MM</code> operation;</p>
<dt>*</p>
<dd>set <i>/proc/[pid]/oom_score_adj</i> to a value lower than the value last set by a process with <code>CAP_SYS_RESOURCE</code>.</dl>
</dl>
<dt><code>CAP_SYS_TIME</code></p>
<dd>Set system clock (<code><a href="/docs/linux/man/2-settimeofday/">settimeofday</a></code>(2), <code><a href="/docs/linux/man/2-stime/">stime</a></code>(2), <code><a href="/docs/linux/man/2-adjtimex/">adjtimex</a></code>(2)); set real-time (hardware) clock.</p>
<dt><code>CAP_SYS_TTY_CONFIG</code></p>
<dd>Use <code><a href="/docs/linux/man/2-vhangup/">vhangup</a></code>(2); employ various privileged <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operations on virtual terminals.</p>
<dt><code>CAP_SYSLOG</code> (since Linux 2.6.37)</p>
<dd>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>Perform privileged <code><a href="/docs/linux/man/2-syslog/">syslog</a></code>(2) operations. See <code><a href="/docs/linux/man/2-syslog/">syslog</a></code>(2) for information on which operations require privilege.</p>
<dt>*</p>
<dd>View kernel addresses exposed via <i>/proc</i> and other interfaces when <i>/proc/sys/kernel/kptr_restrict</i> has the value 1. (See the discussion of the <i>kptr_restrict</i> in <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5).)</dl>
</dl>
<dt><code>CAP_WAKE_ALARM</code> (since Linux 3.0)</p>
<dd>Trigger something that will wake up the system (set <code>CLOCK_REALTIME_ALARM</code> and <code>CLOCK_BOOTTIME_ALARM</code> timers).</dl>
<h3>Past and current implementation</h3>
<p>A full implementation of capabilities requires that:</p>
<dl>
<dt>1.</p>
<dd>For all privileged operations, the kernel must check whether the thread has the required capability in its effective set.</p>
<dt>2.</p>
<dd>The kernel must provide system calls allowing a thread&#8217;s capability sets to be changed and retrieved.</p>
<dt>3.</p>
<dd>The filesystem must support attaching capabilities to an executable file, so that a process gains those capabilities when the file is executed.</dl>
<p> Before kernel 2.6.24, only the first two of these requirements are met; since kernel 2.6.24, all three requirements are met.</p>
<h3>Notes to kernel developers</h3>
<p>When adding a new kernel feature that should be governed by a capability, consider the following points.</p>
<dl>
<dt>*</p>
<dd>The goal of capabilities is divide the power of superuser into pieces, such that if a program that has one or more capabilities is compromised, its power to do damage to the system would be less than the same program running with root privilege.</p>
<dt>*</p>
<dd>You have the choice of either creating a new capability for your new feature, or associating the feature with one of the existing capabilities. In order to keep the set of capabilities to a manageable size, the latter option is preferable, unless there are compelling reasons to take the former option. (There is also a technical limit: the size of capability sets is currently limited to 64 bits.)</p>
<dt>*</p>
<dd>To determine which existing capability might best be associated with your new feature, review the list of capabilities above in order to find a &quot;silo&quot; into which your new feature best fits. One approach to take is to determine if there are other features requiring capabilities that will always be used along with the new feature. If the new feature is useless without these other features, you should use the same capability as the other features.</p>
<dt>*</p>
<dd><i>Don&#8217;t</i> choose <code>CAP_SYS_ADMIN</code> if you can possibly avoid it! A vast proportion of existing capability checks are associated with this capability (see the partial list above). It can plausibly be called &quot;the new root&quot;, since on the one hand, it confers a wide range of powers, and on the other hand, its broad scope means that this is the capability that is required by many privileged programs. Don&#8217;t make the problem worse. The only new features that should be associated with <code>CAP_SYS_ADMIN</code> are ones that <i>closely</i> match existing uses in that silo.</p>
<dt>*</p>
<dd>If you have determined that it really is necessary to create a new capability for your feature, don&#8217;t make or name it as a &quot;single-use&quot; capability. Thus, for example, the addition of the highly specific <code>CAP_SYS_PACCT</code> was probably a mistake. Instead, try to identify and name your new capability as a broader silo into which other related future use cases might fit.</dl>
<h3>Thread capability sets</h3>
<p>Each thread has the following capability sets containing zero or more of the above capabilities:</p>
<dl>
<dt><i>Permitted</i></p>
<dd>This is a limiting superset for the effective capabilities that the thread may assume. It is also a limiting superset for the capabilities that may be added to the inheritable set by a thread that does not have the <code>CAP_SETPCAP</code> capability in its effective set.</p>
<dd>If a thread drops a capability from its permitted set, it can never reacquire that capability (unless it <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2)s either a set-user-ID-root program, or a program whose associated file capabilities grant that capability).</p>
<dt><i>Inheritable</i></p>
<dd>This is a set of capabilities preserved across an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). Inheritable capabilities remain inheritable when executing any program, and inheritable capabilities are added to the permitted set when executing a program that has the corresponding bits set in the file inheritable set.</p>
<dd>Because inheritable capabilities are not generally preserved across <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) when running as a non-root user, applications that wish to run helper programs with elevated capabilities should consider using ambient capabilities, described below.</p>
<dt><i>Effective</i></p>
<dd>This is the set of capabilities used by the kernel to perform permission checks for the thread.</p>
<dt><i>Bounding</i> (per-thread since Linux 2.6.25)</p>
<dd>The capability bounding set is a mechanism that can be used to limit the capabilities that are gained during <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).</p>
<dd>Since Linux 2.6.25, this is a per-thread capability set. In older kernels, the capability bounding set was a system wide attribute shared by all threads on the system.</p>
<dd>For more details on the capability bounding set, see below.</p>
<dt><i>Ambient</i> (since Linux 4.3)</p>
<dd>This is a set of capabilities that are preserved across an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) of a program that is not privileged. The ambient capability set obeys the invariant that no capability can ever be ambient if it is not both permitted and inheritable.</p>
<dd>The ambient capability set can be directly modified using <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2). Ambient capabilities are automatically lowered if either of the corresponding permitted or inheritable capabilities is lowered.</p>
<dd>Executing a program that changes UID or GID due to the set-user-ID or set-group-ID bits or executing a program that has any file capabilities set will clear the ambient set. Ambient capabilities are added to the permitted set and assigned to the effective set when <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) is called. If ambient capabilities cause a process&#8217;s permitted and effective capabilities to increase during an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), this does not trigger the secure-execution mode described in <code><a href="/docs/linux/man/8-ld-so/">ld.so</a></code>(8).</dl>
<p> A child created via <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) inherits copies of its parent&#8217;s capability sets. See below for a discussion of the treatment of capabilities during <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). </p>
<p> Using <code><a href="/docs/linux/man/2-capset/">capset</a></code>(2), a thread may manipulate its own capability sets (see below). </p>
<p> Since Linux 3.2, the file <i>/proc/sys/kernel/cap_last_cap</i> exposes the numerical value of the highest capability supported by the running kernel; this can be used to determine the highest bit that may be set in a capability set.</p>
<h3>File capabilities</h3>
<p>Since kernel 2.6.24, the kernel supports associating capability sets with an executable file using <code><a href="/docs/linux/man/8-setcap/">setcap</a></code>(8). The file capability sets are stored in an extended attribute (see <code><a href="/docs/linux/man/2-setxattr/">setxattr</a></code>(2) and <code><a href="/docs/linux/man/7-xattr/">xattr</a></code>(7)) named <i>security.capability</i>. Writing to this extended attribute requires the <code>CAP_SETFCAP</code> capability. The file capability sets, in conjunction with the capability sets of the thread, determine the capabilities of a thread after an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). </p>
<p> The three file capability sets are:</p>
<dl>
<dt><i>Permitted</i> (formerly known as <i>forced</i>):</p>
<dd>These capabilities are automatically permitted to the thread, regardless of the thread&#8217;s inheritable capabilities.</p>
<dt><i>Inheritable</i> (formerly known as <i>allowed</i>):</p>
<dd>This set is ANDed with the thread&#8217;s inheritable set to determine which inheritable capabilities are enabled in the permitted set of the thread after the <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).</p>
<dt><i>Effective</i>:</p>
<dd>This is not a set, but rather just a single bit. If this bit is set, then during an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) all of the new permitted capabilities for the thread are also raised in the effective set. If this bit is not set, then after an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), none of the new permitted capabilities is in the new effective set.</p>
<dd>Enabling the file effective capability bit implies that any file permitted or inheritable capability that causes a thread to acquire the corresponding permitted capability during an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) (see the transformation rules described below) will also acquire that capability in its effective set. Therefore, when assigning capabilities to a file (<code><a href="/docs/linux/man/8-setcap/">setcap</a></code>(8), <code><a href="/docs/linux/man/3-cap_set_file/">cap_set_file</a></code>(3), <code><a href="/docs/linux/man/3-cap_set_fd/">cap_set_fd</a></code>(3)), if we specify the effective flag as being enabled for any capability, then the effective flag must also be specified as enabled for all other capabilities for which the corresponding permitted or inheritable flags is enabled.</dl>
<h3>File capability extended attribute versioning</h3>
<p>To allow extensibility, the kernel supports a scheme to encode a version number inside the <i>security.capability</i> extended attribute that is used to implement file capabilities. These version numbers are internal to the implementation, and not directly visible to user-space applications. To date, the following versions are supported:</p>
<dl>
<dt><code>VFS_CAP_REVISION_1</code></p>
<dd>This was the original file capability implementation, which supported 32-bit masks for file capabilities.</p>
<dt><code>VFS_CAP_REVISION_2</code> (since Linux 2.6.25)</p>
<dd>This version allows for file capability masks that are 64 bits in size, and was necessary as the number of supported capabilities grew beyond 32. The kernel transparently continues to support the execution of files that have 32-bit version 1 capability masks, but when adding capabilities to files that did not previously have capabilities, or modifying the capabilities of existing files, it automatically uses the version 2 scheme (or possibly the version 3 scheme, as described below).</p>
<dt><code>VFS_CAP_REVISION_3</code> (since Linux 4.14)</p>
<dd>Version 3 file capabilities are provided to support namespaced file capabilities (described below).</p>
<dd>As with version 2 file capabilities, version 3 capability masks are 64 bits in size. But in addition, the root user ID of namespace is encoded in the <i>security.capability</i> extended attribute. (A namespace&#8217;s root user ID is the value that user ID 0 inside that namespace maps to in the initial user namespace.)</p>
<dd>Version 3 file capabilities are designed to coexist with version 2 capabilities; that is, on a modern Linux system, there may be some files with version 2 capabilities while others have version 3 capabilities.</dl>
<p> Before Linux 4.14, the only kind of file capability extended attribute that could be attached to a file was a <code>VFS_CAP_REVISION_2</code> attribute. Since Linux 4.14, the version of the <i>security.capability</i> extended attribute that is attached to a file depends on the circumstances in which the attribute was created. </p>
<p> Starting with Linux 4.14, a <i>security.capability</i> extended attribute is automatically created as (or converted to) a version 3 (<code>VFS_CAP_REVISION_3</code>) attribute if both of the following are true:</p>
<dl>
<dt>(1)</p>
<dd>The thread writing the attribute resides in a noninitial user namespace. (More precisely: the thread resides in a user namespace other than the one from which the underlying filesystem was mounted.)</p>
<dt>(2)</p>
<dd>The thread has the <code>CAP_SETFCAP</code> capability over the file inode, meaning that (a) the thread has the <code>CAP_SETFCAP</code> capability in its own user namespace; and (b) the UID and GID of the file inode have mappings in the writer&#8217;s user namespace.</dl>
<p> When a <code>VFS_CAP_REVISION_3</code> <i>security.capability</i> extended attribute is created, the root user ID of the creating thread&#8217;s user namespace is saved in the extended attribute. </p>
<p> By contrast, creating or modifying a <i>security.capability</i> extended attribute from a privileged (<code>CAP_SETFCAP</code>) thread that resides in the namespace where the underlying filesystem was mounted (this normally means the initial user namespace) automatically results in the creation of a version 2 (<code>VFS_CAP_REVISION_2</code>) attribute. </p>
<p> Note that the creation of a version 3 <i>security.capability</i> extended attribute is automatic. That is to say, when a user-space application writes (<code><a href="/docs/linux/man/2-setxattr/">setxattr</a></code>(2)) a <i>security.capability</i> attribute in the version 2 format, the kernel will automatically create a version 3 attribute if the attribute is created in the circumstances described above. Correspondingly, when a version 3 <i>security.capability</i> attribute is retrieved (<code><a href="/docs/linux/man/2-getxattr/">getxattr</a></code>(2)) by a process that resides inside a user namespace that was created by the root user ID (or a descendant of that user namespace), the returned attribute is (automatically) simplified to appear as a version 2 attribute (i.e., the returned value is the size of a version 2 attribute and does not include the root user ID). These automatic translations mean that no changes are required to user-space tools (e.g., <code><a href="/docs/linux/man/1-setcap/">setcap</a></code>(1) and <code><a href="/docs/linux/man/1-getcap/">getcap</a></code>(1)) in order for those tools to be used to create and retrieve version 3 <i>security.capability</i> attributes. </p>
<p> Note that a file can have either a version 2 or a version 3 <i>security.capability</i> extended attribute associated with it, but not both: creation or modification of the <i>security.capability</i> extended attribute will automatically modify the version according to the circumstances in which the extended attribute is created or modified.</p>
<h3>Transformation of capabilities during execve()</h3>
<p>During an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), the kernel calculates the new capabilities of the process using the following algorithm: </p>
<p> P'(ambient) = (file is privileged) ? 0 : P(ambient) </p>
<p> P'(permitted) = (P(inheritable) &amp; F(inheritable)) |<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(F(permitted)&nbsp;&amp;&nbsp;P(bounding))&nbsp;| P'(ambient) </p>
<p> P'(effective) = F(effective) ? P'(permitted) : P'(ambient) </p>
<p> P'(inheritable) = P(inheritable) [i.e., unchanged] </p>
<p> P'(bounding) = P(bounding) [i.e., unchanged] </p>
<p> where:</p>
<dl>
<dd>
<dl>
<dt>P()</p>
<dd>denotes the value of a thread capability set before the <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2)</p>
<dt>P'()</p>
<dd>denotes the value of a thread capability set after the <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2)</p>
<dt>F()</p>
<dd>denotes a file capability set</dl>
</dl>
<p> Note the following details relating to the above capability transformation rules:</p>
<dl>
<dt>*</p>
<dd>The ambient capability set is present only since Linux 4.3. When determining the transformation of the ambient set during <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), a privileged file is one that has capabilities or has the set-user-ID or set-group-ID bit set.</p>
<dt>*</p>
<dd>Prior to Linux 2.6.25, the bounding set was a system-wide attribute shared by all threads. That system-wide value was employed to calculate the new permitted set during <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) in the same manner as shown above for <i>P(bounding)</i>.</dl>
<p> <i>Note</i>: during the capability transitions described above, file capabilities may be ignored (treated as empty) for the same reasons that the set-user-ID and set-group-ID bits are ignored; see <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). File capabilities are similarly ignored if the kernel was booted with the <i>no_file_caps</i> option. </p>
<p> <i>Note</i>: according to the rules above, if a process with nonzero user IDs performs an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) then any capabilities that are present in its permitted and effective sets will be cleared. For the treatment of capabilities when a process with a user ID of zero performs an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), see below under <i>Capabilities and execution of programs by root</i>.</p>
<h3>Safety checking for capability-dumb binaries</h3>
<p>A capability-dumb binary is an application that has been marked to have file capabilities, but has not been converted to use the <code><a href="/docs/linux/man/3-libcap/">libcap</a></code>(3) API to manipulate its capabilities. (In other words, this is a traditional set-user-ID-root program that has been switched to use file capabilities, but whose code has not been modified to understand capabilities.) For such applications, the effective capability bit is set on the file, so that the file permitted capabilities are automatically enabled in the process effective set when executing the file. The kernel recognizes a file which has the effective capability bit set as capability-dumb for the purpose of the check described here. </p>
<p> When executing a capability-dumb binary, the kernel checks if the process obtained all permitted capabilities that were specified in the file permitted set, after the capability transformations described above have been performed. (The typical reason why this might <i>not</i> occur is that the capability bounding set masked out some of the capabilities in the file permitted set.) If the process did not obtain the full set of file permitted capabilities, then <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) fails with the error <code>EPERM</code>. This prevents possible security risks that could arise when a capability-dumb application is executed with less privilege that it needs. Note that, by definition, the application could not itself recognize this problem, since it does not employ the <code><a href="/docs/linux/man/3-libcap/">libcap</a></code>(3) API.</p>
<h3>Capabilities and execution of programs by root</h3>
<p>In order to mirror traditional UNIX semantics, the kernel performs special treatment of file capabilities when a process with UID 0 (root) executes a program and when a set-user-ID-root program is executed. </p>
<p> After having performed any changes to the process effective ID that were triggered by the set-user-ID mode bit of the binary&#8212;e.g., switching the effective user ID to 0 (root) because a set-user-ID-root program was executed&#8212;the kernel calculates the file capability sets as follows:</p>
<dl>
<dt>1.</p>
<dd>If the real or effective user ID of the process is 0 (root), then the file inheritable and permitted sets are ignored; instead they are notionally considered to be all ones (i.e., all capabilities enabled). (There is one exception to this behavior, described below in <i>Set-user-ID-root programs that have file capabilities</i>.)</p>
<dt>2.</p>
<dd>If the effective user ID of the process is 0 (root) or the file effective bit is in fact enabled, then the file effective bit is notionally defined to be one (enabled).</dl>
<p> These notional values for the file&#8217;s capability sets are then used as described above to calculate the transformation of the process&#8217;s capabilities during <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). </p>
<p> Thus, when a process with nonzero UIDs <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2)s a set-user-ID-root program that does not have capabilities attached, or when a process whose real and effective UIDs are zero <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2)s a program, the calculation of the process&#8217;s new permitted capabilities simplifies to: </p>
<p> P'(permitted) = P(inheritable) | P(bounding) </p>
<p> P'(effective) = P'(permitted) </p>
<p> Consequently, the process gains all capabilities in its permitted and effective capability sets, except those masked out by the capability bounding set. (In the calculation of P'(permitted), the P'(ambient) term can be simplified away because it is by definition a proper subset of P(inheritable).) </p>
<p> The special treatments of user ID 0 (root) described in this subsection can be disabled using the securebits mechanism described below.</p>
<h3>Set-user-ID-root programs that have file capabilities</h3>
<p>There is one exception to the behavior described under <i>Capabilities and execution of programs by root</i>. If (a) the binary that is being executed has capabilities attached and (b) the real user ID of the process is <i>not</i> 0 (root) and (c) the effective user ID of the process <i>is</i> 0 (root), then the file capability bits are honored (i.e., they are not notionally considered to be all ones). The usual way in which this situation can arise is when executing a set-UID-root program that also has file capabilities. When such a program is executed, the process gains just the capabilities granted by the program (i.e., not all capabilities, as would occur when executing a set-user-ID-root program that does not have any associated file capabilities). </p>
<p> Note that one can assign empty capability sets to a program file, and thus it is possible to create a set-user-ID-root program that changes the effective and saved set-user-ID of the process that executes the program to 0, but confers no capabilities to that process.</p>
<h3>Capability bounding set</h3>
<p>The capability bounding set is a security mechanism that can be used to limit the capabilities that can be gained during an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). The bounding set is used in the following ways:</p>
<dl>
<dt>*</p>
<dd>During an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), the capability bounding set is ANDed with the file permitted capability set, and the result of this operation is assigned to the thread&#8217;s permitted capability set. The capability bounding set thus places a limit on the permitted capabilities that may be granted by an executable file.</p>
<dt>*</p>
<dd>(Since Linux 2.6.25) The capability bounding set acts as a limiting superset for the capabilities that a thread can add to its inheritable set using <code><a href="/docs/linux/man/2-capset/">capset</a></code>(2). This means that if a capability is not in the bounding set, then a thread can&#8217;t add this capability to its inheritable set, even if it was in its permitted capabilities, and thereby cannot have this capability preserved in its permitted set when it <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2)s a file that has the capability in its inheritable set.</dl>
<p> Note that the bounding set masks the file permitted capabilities, but not the inheritable capabilities. If a thread maintains a capability in its inheritable set that is not in its bounding set, then it can still gain that capability in its permitted set by executing a file that has the capability in its inheritable set. </p>
<p> Depending on the kernel version, the capability bounding set is either a system-wide attribute, or a per-process attribute. </p>
<p> <code>Capability bounding set from Linux 2.6.25 onward</code> </p>
<p> From Linux 2.6.25, the <i>capability bounding set</i> is a per-thread attribute. (The system-wide capability bounding set described below no longer exists.) </p>
<p> The bounding set is inherited at <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) from the thread&#8217;s parent, and is preserved across an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). </p>
<p> A thread may remove capabilities from its capability bounding set using the <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2) <code>PR_CAPBSET_DROP</code> operation, provided it has the <code>CAP_SETPCAP</code> capability. Once a capability has been dropped from the bounding set, it cannot be restored to that set. A thread can determine if a capability is in its bounding set using the <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2) <code>PR_CAPBSET_READ</code> operation. </p>
<p> Removing capabilities from the bounding set is supported only if file capabilities are compiled into the kernel. In kernels before Linux 2.6.33, file capabilities were an optional feature configurable via the <code>CONFIG_SECURITY_FILE_CAPABILITIES</code> option. Since Linux 2.6.33, the configuration option has been removed and file capabilities are always part of the kernel. When file capabilities are compiled into the kernel, the <code>init</code> process (the ancestor of all processes) begins with a full bounding set. If file capabilities are not compiled into the kernel, then <code>init</code> begins with a full bounding set minus <code>CAP_SETPCAP</code>, because this capability has a different meaning when there are no file capabilities. </p>
<p> Removing a capability from the bounding set does not remove it from the thread&#8217;s inheritable set. However it does prevent the capability from being added back into the thread&#8217;s inheritable set in the future. </p>
<p> <code>Capability bounding set prior to Linux 2.6.25</code> </p>
<p> In kernels before 2.6.25, the capability bounding set is a system-wide attribute that affects all threads on the system. The bounding set is accessible via the file <i>/proc/sys/kernel/cap-bound</i>. (Confusingly, this bit mask parameter is expressed as a signed decimal number in <i>/proc/sys/kernel/cap-bound</i>.) </p>
<p> Only the <code>init</code> process may set capabilities in the capability bounding set; other than that, the superuser (more precisely: a process with the <code>CAP_SYS_MODULE</code> capability) may only clear capabilities from this set. </p>
<p> On a standard system the capability bounding set always masks out the <code>CAP_SETPCAP</code> capability. To remove this restriction (dangerous!), modify the definition of <code>CAP_INIT_EFF_SET</code> in <i>include/linux/capability.h</i> and rebuild the kernel. </p>
<p> The system-wide capability bounding set feature was added to Linux starting with kernel version 2.2.11.</p>
<h3>Effect of user ID changes on capabilities</h3>
<p>To preserve the traditional semantics for transitions between 0 and nonzero user IDs, the kernel makes the following changes to a thread&#8217;s capability sets on changes to the thread&#8217;s real, effective, saved set, and filesystem user IDs (using <code><a href="/docs/linux/man/2-setuid/">setuid</a></code>(2), <code><a href="/docs/linux/man/2-setresuid/">setresuid</a></code>(2), or similar):</p>
<dl>
<dt>1.</p>
<dd>If one or more of the real, effective or saved set user IDs was previously 0, and as a result of the UID changes all of these IDs have a nonzero value, then all capabilities are cleared from the permitted, effective, and ambient capability sets.</p>
<dt>2.</p>
<dd>If the effective user ID is changed from 0 to nonzero, then all capabilities are cleared from the effective set.</p>
<dt>3.</p>
<dd>If the effective user ID is changed from nonzero to 0, then the permitted set is copied to the effective set.</p>
<dt>4.</p>
<dd>If the filesystem user ID is changed from 0 to nonzero (see <code><a href="/docs/linux/man/2-setfsuid/">setfsuid</a></code>(2)), then the following capabilities are cleared from the effective set: <code>CAP_CHOWN</code>, <code>CAP_DAC_OVERRIDE</code>, <code>CAP_DAC_READ_SEARCH</code>, <code>CAP_FOWNER</code>, <code>CAP_FSETID</code>, <code>CAP_LINUX_IMMUTABLE</code> (since Linux 2.6.30), <code>CAP_MAC_OVERRIDE</code>, and <code>CAP_MKNOD</code> (since Linux 2.6.30). If the filesystem UID is changed from nonzero to 0, then any of these capabilities that are enabled in the permitted set are enabled in the effective set.</dl>
<p> If a thread that has a 0 value for one or more of its user IDs wants to prevent its permitted capability set being cleared when it resets all of its user IDs to nonzero values, it can do so using the <code>SECBIT_KEEP_CAPS</code> securebits flag described below.</p>
<h3>Programmatically adjusting capability sets</h3>
<p>A thread can retrieve and change its permitted, effective, and inheritable capability sets using the <code><a href="/docs/linux/man/2-capget/">capget</a></code>(2) and <code><a href="/docs/linux/man/2-capset/">capset</a></code>(2) system calls. However, the use of <code><a href="/docs/linux/man/3-cap_get_proc/">cap_get_proc</a></code>(3) and <code><a href="/docs/linux/man/3-cap_set_proc/">cap_set_proc</a></code>(3), both provided in the <i>libcap</i> package, is preferred for this purpose. The following rules govern changes to the thread capability sets:</p>
<dl>
<dt>1.</p>
<dd>If the caller does not have the <code>CAP_SETPCAP</code> capability, the new inheritable set must be a subset of the combination of the existing inheritable and permitted sets.</p>
<dt>2.</p>
<dd>(Since Linux 2.6.25) The new inheritable set must be a subset of the combination of the existing inheritable set and the capability bounding set.</p>
<dt>3.</p>
<dd>The new permitted set must be a subset of the existing permitted set (i.e., it is not possible to acquire permitted capabilities that the thread does not currently have).</p>
<dt>4.</p>
<dd>The new effective set must be a subset of the new permitted set.</dl>
<h3>The securebits flags: establishing a capabilities-only environment</h3>
<p>Starting with kernel 2.6.26, and with a kernel in which file capabilities are enabled, Linux implements a set of per-thread <i>securebits</i> flags that can be used to disable special handling of capabilities for UID 0 (<i>root</i>). These flags are as follows:</p>
<dl>
<dt><code>SECBIT_KEEP_CAPS</code></p>
<dd>Setting this flag allows a thread that has one or more 0 UIDs to retain capabilities in its permitted set when it switches all of its UIDs to nonzero values. If this flag is not set, then such a UID switch causes the thread to lose all permitted capabilities. This flag is always cleared on an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).</p>
<dd>Note that even with the <code>SECBIT_KEEP_CAPS</code> flag set, the effective capabilities of a thread are cleared when it switches its effective UID to a nonzero value. However, if the thread has set this flag and its effective UID is already nonzero, and the thread subsequently switches all other UIDs to nonzero values, then the effective capabilities will not be cleared.</p>
<dd>The setting of the <code>SECBIT_KEEP_CAPS</code> flag is ignored if the <code>SECBIT_NO_SETUID_FIXUP</code> flag is set. (The latter flag provides a superset of the effect of the former flag.)</p>
<dd>This flag provides the same functionality as the older <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2) <code>PR_SET_KEEPCAPS</code> operation.</p>
<dt><code>SECBIT_NO_SETUID_FIXUP</code></p>
<dd>Setting this flag stops the kernel from adjusting the process&#8217;s permitted, effective, and ambient capability sets when the thread&#8217;s effective and filesystem UIDs are switched between zero and nonzero values. (See the subsection <i>Effect of user ID changes on capabilities</i>.)</p>
<dt><code>SECBIT_NOROOT</code></p>
<dd>If this bit is set, then the kernel does not grant capabilities when a set-user-ID-root program is executed, or when a process with an effective or real UID of 0 calls <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). (See the subsection <i>Capabilities and execution of programs by root</i>.)</p>
<dt><code>SECBIT_NO_CAP_AMBIENT_RAISE</code></p>
<dd>Setting this flag disallows raising ambient capabilities via the <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2) <code>PR_CAP_AMBIENT_RAISE</code> operation.</dl>
<p> Each of the above &quot;base&quot; flags has a companion &quot;locked&quot; flag. Setting any of the &quot;locked&quot; flags is irreversible, and has the effect of preventing further changes to the corresponding &quot;base&quot; flag. The locked flags are: <code>SECBIT_KEEP_CAPS_LOCKED</code>, <code>SECBIT_NO_SETUID_FIXUP_LOCKED</code>, <code>SECBIT_NOROOT_LOCKED</code>, and <code>SECBIT_NO_CAP_AMBIENT_RAISE_LOCKED</code>. </p>
<p> The <i>securebits</i> flags can be modified and retrieved using the <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2) <code>PR_SET_SECUREBITS</code> and <code>PR_GET_SECUREBITS</code> operations. The <code>CAP_SETPCAP</code> capability is required to modify the flags. Note that the <code>SECBIT_*</code> constants are available only after including the <i>&lt;linux/securebits.h&gt;</i> header file. </p>
<p> The <i>securebits</i> flags are inherited by child processes. During an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), all of the flags are preserved, except <code>SECBIT_KEEP_CAPS</code> which is always cleared. </p>
<p> An application can use the following call to lock itself, and all of its descendants, into an environment where the only way of gaining capabilities is by executing a program with associated file capabilities: </p>
<p> prctl(PR_SET_SECUREBITS,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;SECBIT_KEEP_CAPS off&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;SECBIT_KEEP_CAPS_LOCKED |<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;SECBIT_NO_SETUID_FIXUP |<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;SECBIT_NO_SETUID_FIXUP_LOCKED |<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;SECBIT_NOROOT |<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;SECBIT_NOROOT_LOCKED);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Setting/locking SECBIT_NO_CAP_AMBIENT_RAISE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;is not required&nbsp;*/</p>
<h3>Per-user-namespace set-user-ID-root programs</h3>
<p>A set-user-ID program whose UID matches the UID that created a user namespace will confer capabilities in the process&#8217;s permitted and effective sets when executed by any process inside that namespace or any descendant user namespace. </p>
<p> The rules about the transformation of the process&#8217;s capabilities during the <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) are exactly as described in the subsections <i>Transformation of capabilities during execve()</i> and <i>Capabilities and execution of programs by root</i>, with the difference that, in the latter subsection, &quot;root&quot; is the UID of the creator of the user namespace.</p>
<h3>Namespaced file capabilities</h3>
<p>Traditional (i.e., version 2) file capabilities associate only a set of capability masks with a binary executable file. When a process executes a binary with such capabilities, it gains the associated capabilities (within its user namespace) as per the rules described above in &quot;Transformation of capabilities during execve()&quot;. </p>
<p> Because version 2 file capabilities confer capabilities to the executing process regardless of which user namespace it resides in, only privileged processes are permitted to associate capabilities with a file. Here, &quot;privileged&quot; means a process that has the <code>CAP_SETFCAP</code> capability in the user namespace where the filesystem was mounted (normally the initial user namespace). This limitation renders file capabilities useless for certain use cases. For example, in user-namespaced containers, it can be desirable to be able to create a binary that confers capabilities only to processes executed inside that container, but not to processes that are executed outside the container. </p>
<p> Linux 4.14 added so-called namespaced file capabilities to support such use cases. Namespaced file capabilities are recorded as version 3 (i.e., <code>VFS_CAP_REVISION_3</code>) <i>security.capability</i> extended attributes. Such an attribute is automatically created in the circumstances described above under &quot;File capability extended attribute versioning&quot;. When a version 3 <i>security.capability</i> extended attribute is created, the kernel records not just the capability masks in the extended attribute, but also the namespace root user ID. </p>
<p> As with a binary that has <code>VFS_CAP_REVISION_2</code> file capabilities, a binary with <code>VFS_CAP_REVISION_3</code> file capabilities confers capabilities to a process during <code>execve</code>(). However, capabilities are conferred only if the binary is executed by a process that resides in a user namespace whose UID 0 maps to the root user ID that is saved in the extended attribute, or when executed by a process that resides in a descendant of such a namespace.</p>
<h3>Interaction with user namespaces</h3>
<p>For further information on the interaction of capabilities and user namespaces, see <code><a href="/docs/linux/man/7-user_namespaces/">user_namespaces</a></code>(7).</p>
<h2>Conforming To</h2>
<p>No standards govern capabilities, but the Linux capability implementation is based on the withdrawn POSIX.1e draft standard; see</p>
<h2>Notes</h2>
<p>When attempting to <code><a href="/docs/linux/man/1-strace/">strace</a></code>(1) binaries that have capabilities (or set-user-ID-root binaries), you may find the <i>-u &lt;username&gt;</i> option useful. Something like: </p>
<p> $ <code>sudo strace -o trace.log -u ceci ./myprivprog</code> </p>
<p> From kernel 2.5.27 to kernel 2.6.26, capabilities were an optional kernel component, and could be enabled/disabled via the <code>CONFIG_SECURITY_CAPABILITIES</code> kernel configuration option. </p>
<p> The <i>/proc/[pid]/task/TID/status</i> file can be used to view the capability sets of a thread. The <i>/proc/[pid]/status</i> file shows the capability sets of a process&#8217;s main thread. Before Linux 3.8, nonexistent capabilities were shown as being enabled (1) in these sets. Since Linux 3.8, all nonexistent capabilities (above <code>CAP_LAST_CAP</code>) are shown as disabled (0). </p>
<p> The <i>libcap</i> package provides a suite of routines for setting and getting capabilities that is more comfortable and less likely to change than the interface provided by <code><a href="/docs/linux/man/2-capset/">capset</a></code>(2) and <code><a href="/docs/linux/man/2-capget/">capget</a></code>(2). This package also provides the <code><a href="/docs/linux/man/8-setcap/">setcap</a></code>(8) and <code><a href="/docs/linux/man/8-getcap/">getcap</a></code>(8) programs. It can be found at </p>
<p> Before kernel 2.6.24, and from kernel 2.6.24 to kernel 2.6.32 if file capabilities are not enabled, a thread with the <code>CAP_SETPCAP</code> capability can manipulate the capabilities of threads other than itself. However, this is only theoretically possible, since no thread ever has <code>CAP_SETPCAP</code> in either of these cases:</p>
<dl>
<dt>*</p>
<dd>In the pre-2.6.25 implementation the system-wide capability bounding set, <i>/proc/sys/kernel/cap-bound</i>, always masks out the <code>CAP_SETPCAP</code> capability, and this can not be changed without modifying the kernel source and rebuilding the kernel.</p>
<dt>*</p>
<dd>If file capabilities are disabled (i.e., the kernel <code>CONFIG_SECURITY_FILE_CAPABILITIES</code> option is disabled), then <code>init</code> starts out with the <code>CAP_SETPCAP</code> capability removed from its per-process bounding set, and that bounding set is inherited by all other processes created on the system.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-capsh/">capsh</a></code>(1), <code><a href="/docs/linux/man/1-setpriv/">setpriv</a></code>(1), <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2), <code><a href="/docs/linux/man/2-setfsuid/">setfsuid</a></code>(2), <code><a href="/docs/linux/man/3-cap_clear/">cap_clear</a></code>(3), <code><a href="/docs/linux/man/3-cap_copy_ext/">cap_copy_ext</a></code>(3), <code><a href="/docs/linux/man/3-cap_from_text/">cap_from_text</a></code>(3), <code><a href="/docs/linux/man/3-cap_get_file/">cap_get_file</a></code>(3), <code><a href="/docs/linux/man/3-cap_get_proc/">cap_get_proc</a></code>(3), <code><a href="/docs/linux/man/3-cap_init/">cap_init</a></code>(3), <code><a href="/docs/linux/man/3-capgetp/">capgetp</a></code>(3), <code><a href="/docs/linux/man/3-capsetp/">capsetp</a></code>(3), <code><a href="/docs/linux/man/3-libcap/">libcap</a></code>(3), <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5), <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7), <code><a href="/docs/linux/man/7-user_namespaces/">user_namespaces</a></code>(7), <code><a href="/docs/linux/man/8-captest/">captest</a></code>(8), <code><a href="/docs/linux/man/8-filecap/">filecap</a></code>(8), <code><a href="/docs/linux/man/8-getcap/">getcap</a></code>(8), <code><a href="/docs/linux/man/8-getpcaps/">getpcaps</a></code>(8), <code><a href="/docs/linux/man/8-netcap/">netcap</a></code>(8), <code><a href="/docs/linux/man/8-pscap/">pscap</a></code>(8), <code><a href="/docs/linux/man/8-setcap/">setcap</a></code>(8) </p>
<p> <i>include/linux/capability.h</i> in the Linux kernel source tree</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
