---
title: "user_namespaces(7)"
name: "user_namespaces"
section: "7"
letter: "u"
url: "/docs/linux/man/7-user_namespaces/"
---


 </p>
<h2>DESCRIPTION</h2>
<p> For an overview of namespaces, see <code><a href="/docs/linux/man/7-namespaces/">namespaces</a></code>(7). </p>
<p> User namespaces isolate security-related identifiers and attributes, in particular, user IDs and group IDs (see <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7)), the root directory, keys (see <code><a href="/docs/linux/man/7-keyrings/">keyrings</a></code>(7)), and capabilities (see <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7)). A process&#8217;s user and group IDs can be different inside and outside a user namespace. In particular, a process can have a normal unprivileged user ID outside a user namespace while at the same time having a user ID of 0 inside the namespace; in other words, the process has full privileges for operations inside the user namespace, but is unprivileged for operations outside the namespace.  </p>
<h3>Nested namespaces, namespace membership</h3>
<p> User namespaces can be nested; that is, each user namespace---except the initial (&quot;root&quot;) namespace---has a parent user namespace, and can have zero or more child user namespaces. The parent user namespace is the user namespace of the process that creates the user namespace via a call to <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2) or <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) with the <code>CLONE_NEWUSER</code> flag. </p>
<p> The kernel imposes (since version 3.11) a limit of 32 nested levels of user namespaces. Calls to <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2) or <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) that would cause this limit to be exceeded fail with the error <code>EUSERS</code>. </p>
<p> Each process is a member of exactly one user namespace. A process created via <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) or <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) without the <code>CLONE_NEWUSER</code> flag is a member of the same user namespace as its parent. A single-threaded process can join another user namespace with <code><a href="/docs/linux/man/2-setns/">setns</a></code>(2) if it has the <code>CAP_SYS_ADMIN</code> in that namespace; upon doing so, it gains a full set of capabilities in that namespace. </p>
<p> A call to <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) or <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2) with the <code>CLONE_NEWUSER</code> flag makes the new child process (for <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2)) or the caller (for <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2)) a member of the new user namespace created by the call. </p>
<p> The <code>NS_GET_PARENT</code> <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operation can be used to discover the parental relationship between user namespaces; see <code><a href="/docs/linux/man/2-ioctl_ns/">ioctl_ns</a></code>(2).  </p>
<h3>Capabilities</h3>
<p> The child process created by <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) with the <code>CLONE_NEWUSER</code> flag starts out with a complete set of capabilities in the new user namespace. Likewise, a process that creates a new user namespace using <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2) or joins an existing user namespace using <code><a href="/docs/linux/man/2-setns/">setns</a></code>(2) gains a full set of capabilities in that namespace. On the other hand, that process has no capabilities in the parent (in the case of <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2)) or previous (in the case of <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2) and <code><a href="/docs/linux/man/2-setns/">setns</a></code>(2)) user namespace, even if the new namespace is created or joined by the root user (i.e., a process with user ID 0 in the root namespace). </p>
<p> Note that a call to <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) will cause a process&#8217;s capabilities to be recalculated in the usual way (see <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7)). Consequently, unless the process has a user ID of 0 within the namespace, or the executable file has a nonempty inheritable capabilities mask, the process will lose all capabilities. See the discussion of user and group ID mappings, below. </p>
<p> A call to <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) or <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2) using the <code>CLONE_NEWUSER</code> flag or a call to <code><a href="/docs/linux/man/2-setns/">setns</a></code>(2) that moves the caller into another user namespace sets the &quot;securebits&quot; flags (see <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7)) to their default values (all flags disabled) in the child (for <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2)) or caller (for <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2) or <code><a href="/docs/linux/man/2-setns/">setns</a></code>(2)). Note that because the caller no longer has capabilities in its original user namespace after a call to <code><a href="/docs/linux/man/2-setns/">setns</a></code>(2), it is not possible for a process to reset its &quot;securebits&quot; flags while retaining its user namespace membership by using a pair of <code><a href="/docs/linux/man/2-setns/">setns</a></code>(2) calls to move to another user namespace and then return to its original user namespace. </p>
<p> The rules for determining whether or not a process has a capability in a particular user namespace are as follows: </p>
<dl>
<dt>1.</dt>
<dd> <p> A process has a capability inside a user namespace if it is a member of that namespace and it has the capability in its effective capability set. A process can gain capabilities in its effective capability set in various ways. For example, it may execute a set-user-ID program or an executable with associated file capabilities. In addition, a process may gain capabilities via the effect of <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2), or <code><a href="/docs/linux/man/2-setns/">setns</a></code>(2), as already described. </p>
 </dd>
<dt>2.</dt>
<dd> <p> If a process has a capability in a user namespace, then it has that capability in all child (and further removed descendant) namespaces as well. </p>
 </dd>
<dt>3.</dt>
<dd> <p> When a user namespace is created, the kernel records the effective user ID of the creating process as being the &quot;owner&quot; of the namespace. A process that resides in the parent of the user namespace and whose effective user ID matches the owner of the namespace has all capabilities in the namespace. By virtue of the previous rule, this means that the process has all capabilities in all further removed descendant user namespaces as well. The <code>NS_GET_OWNER_UID</code> <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operation can be used to discover the user ID of the owner of the namespace; see <code><a href="/docs/linux/man/2-ioctl_ns/">ioctl_ns</a></code>(2). </p>
 </dd></dl>
<h3>Effect of capabilities within a user namespace</h3>
<p> Having a capability inside a user namespace permits a process to perform operations (that require privilege) only on resources governed by that namespace. In other words, having a capability in a user namespace permits a process to perform privileged operations on resources that are governed by (nonuser) namespaces owned by (associated with) the user namespace (see the next subsection). </p>
<p> On the other hand, there are many privileged operations that affect resources that are not associated with any namespace type, for example, changing the system (i.e., calendar) time (governed by <code>CAP_SYS_TIME</code>), loading a kernel module (governed by <code>CAP_SYS_MODULE</code>), and creating a device (governed by <code>CAP_MKNOD</code>). Only a process with privileges in the <i>initial</i> user namespace can perform such operations. </p>
<p> Holding <code>CAP_SYS_ADMIN</code> within the user namespace that owns a process&#8217;s mount namespace allows that process to create bind mounts and mount the following types of filesystems: </p>
<dl>
<dd>  </dd>
<dl>
<dt>*</dt>
<dd> <p> <i>/proc</i> (since Linux 3.8) </p>
 </dd>
<dt>*</dt>
<dd> <p> <i>/sys</i> (since Linux 3.8) </p>
 </dd>
<dt>*</dt>
<dd> <p> <i>devpts</i> (since Linux 3.9) </p>
 </dd>
<dt>*</dt>
<dd> <p> <code><a href="/docs/linux/man/5-tmpfs/">tmpfs</a></code>(5) (since Linux 3.9) </p>
 </dd>
<dt>*</dt>
<dd> <p> <i>ramfs</i> (since Linux 3.9) </p>
 </dd>
<dt>*</dt>
<dd> <p> <i>mqueue</i> (since Linux 3.9) </p>
 </dd>
<dt>*</dt>
<dd> <p> <i>bpf</i> (since Linux 4.4) </p>
 </dd></dl>
</dl>
<p> Holding <code>CAP_SYS_ADMIN</code> within the user namespace that owns a process&#8217;s cgroup namespace allows (since Linux 4.6) that process to the mount the cgroup version 2 filesystem and cgroup version 1 named hierarchies (i.e., cgroup filesystems mounted with the <i>&quot;none,name=&quot;</i> option). </p>
<p> Holding <code>CAP_SYS_ADMIN</code> within the user namespace that owns a process&#8217;s PID namespace allows (since Linux 3.8) that process to mount <i>/proc</i> filesystems. </p>
<p> Note however, that mounting block-based filesystems can be done only by a process that holds <code>CAP_SYS_ADMIN</code> in the initial user namespace.  </p>
<h3>Interaction of user namespaces and other types of namespaces</h3>
<p> Starting in Linux 3.8, unprivileged processes can create user namespaces, and the other types of namespaces can be created with just the <code>CAP_SYS_ADMIN</code> capability in the caller&#8217;s user namespace. </p>
<p> When a nonuser namespace is created, it is owned by the user namespace in which the creating process was a member at the time of the creation of the namespace. Privileged operations on resources governed by the nonuser namespace require that the process has the necessary capabilities in the user namespace that owns the nonuser namespace. </p>
<p> If <code>CLONE_NEWUSER</code> is specified along with other <code>CLONE_NEW*</code> flags in a single <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) or <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2) call, the user namespace is guaranteed to be created first, giving the child (<code><a href="/docs/linux/man/2-clone/">clone</a></code>(2)) or caller (<code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2)) privileges over the remaining namespaces created by the call. Thus, it is possible for an unprivileged caller to specify this combination of flags. </p>
<p> When a new namespace (other than a user namespace) is created via <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) or <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2), the kernel records the user namespace of the creating process as the owner of the new namespace. (This association can&#8217;t be changed.) When a process in the new namespace subsequently performs privileged operations that operate on global resources isolated by the namespace, the permission checks are performed according to the process&#8217;s capabilities in the user namespace that the kernel associated with the new namespace. For example, suppose that a process attempts to change the hostname (<code><a href="/docs/linux/man/2-sethostname/">sethostname</a></code>(2)), a resource governed by the UTS namespace. In this case, the kernel will determine which user namespace owns the process&#8217;s UTS namespace, and check whether the process has the required capability (<code>CAP_SYS_ADMIN</code>) in that user namespace. </p>
<p> The <code>NS_GET_USERNS</code> <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operation can be used to discover the user namespace that owns a nonuser namespace; see <code><a href="/docs/linux/man/2-ioctl_ns/">ioctl_ns</a></code>(2).  </p>
<h3>User and group ID mappings: uid_map and gid_map</h3>
<p> When a user namespace is created, it starts out without a mapping of user IDs (group IDs) to the parent user namespace. The <i>/proc/[pid]/uid_map</i> and <i>/proc/[pid]/gid_map</i> files (available since Linux 3.5) expose the mappings for user and group IDs inside the user namespace for the process <i>pid</i>. These files can be read to view the mappings in a user namespace and written to (once) to define the mappings. </p>
<p> The description in the following paragraphs explains the details for <i>uid_map</i>; <i>gid_map</i> is exactly the same, but each instance of &quot;user ID&quot; is replaced by &quot;group ID&quot;. </p>
<p> The <i>uid_map</i> file exposes the mapping of user IDs from the user namespace of the process <i>pid</i> to the user namespace of the process that opened <i>uid_map</i> (but see a qualification to this point below). In other words, processes that are in different user namespaces will potentially see different values when reading from a particular <i>uid_map</i> file, depending on the user ID mappings for the user namespaces of the reading processes. </p>
<p> Each line in the <i>uid_map</i> file specifies a 1-to-1 mapping of a range of contiguous user IDs between two user namespaces. (When a user namespace is first created, this file is empty.) The specification in each line takes the form of three numbers delimited by white space. The first two numbers specify the starting user ID in each of the two user namespaces. The third number specifies the length of the mapped range. In detail, the fields are interpreted as follows: </p>
<dl>
<dt>(1)</dt>
<dd> <p> The start of the range of user IDs in the user namespace of the process <i>pid</i>. </p>
 </dd>
<dt>(2)</dt>
<dd> <p> The start of the range of user IDs to which the user IDs specified by field one map. How field two is interpreted depends on whether the process that opened <i>uid_map</i> and the process <i>pid</i> are in the same user namespace, as follows: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>a)</dt>
<dd> <p> If the two processes are in different user namespaces: field two is the start of a range of user IDs in the user namespace of the process that opened <i>uid_map</i>. </p>
 </dd>
<dt>b)</dt>
<dd> <p> If the two processes are in the same user namespace: field two is the start of the range of user IDs in the parent user namespace of the process <i>pid</i>. This case enables the opener of <i>uid_map</i> (the common case here is opening <i>/proc/self/uid_map</i>) to see the mapping of user IDs into the user namespace of the process that created this user namespace. </p>
 </dd></dl>
</dl>
<dt>(3)</dt>
<dd> <p> The length of the range of user IDs that is mapped between the two user namespaces. </p>
 </dd></dl>
<p> System calls that return user IDs (group IDs)---for example, <code><a href="/docs/linux/man/2-getuid/">getuid</a></code>(2), <code><a href="/docs/linux/man/2-getgid/">getgid</a></code>(2), and the credential fields in the structure returned by <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2)---return the user ID (group ID) mapped into the caller&#8217;s user namespace. </p>
<p> When a process accesses a file, its user and group IDs are mapped into the initial user namespace for the purpose of permission checking and assigning IDs when creating a file. When a process retrieves file user and group IDs via <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2), the IDs are mapped in the opposite direction, to produce values relative to the process user and group ID mappings. </p>
<p> The initial user namespace has no parent namespace, but, for consistency, the kernel provides dummy user and group ID mapping files for this namespace. Looking at the <i>uid_map</i> file (<i>gid_map</i> is the same) from a shell in the initial namespace shows: </p>
<p> $ <code>cat /proc/$$/uid_map</code> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0 4294967295 </p>
<p> This mapping tells us that the range starting at user ID 0 in this namespace maps to a range starting at 0 in the (nonexistent) parent namespace, and the length of the range is the largest 32-bit unsigned integer. This leaves 4294967295 (the 32-bit signed -1 value) unmapped. This is deliberate: <i>(uid_t)&nbsp;-1</i> is used in several interfaces (e.g., <code><a href="/docs/linux/man/2-setreuid/">setreuid</a></code>(2)) as a way to specify &quot;no user ID&quot;. Leaving <i>(uid_t)&nbsp;-1</i> unmapped and unusable guarantees that there will be no confusion when using these interfaces.  </p>
<h3>Defining user and group ID mappings: writing to uid_map and gid_map</h3>
<p> After the creation of a new user namespace, the <i>uid_map</i> file of <i>one</i> of the processes in the namespace may be written to <i>once</i> to define the mapping of user IDs in the new user namespace. An attempt to write more than once to a <i>uid_map</i> file in a user namespace fails with the error <code>EPERM</code>. Similar rules apply for <i>gid_map</i> files. </p>
<p> The lines written to <i>uid_map</i> (<i>gid_map</i>) must conform to the following rules: </p>
<dl>
<dt>*</dt>
<dd> <p> The three fields must be valid numbers, and the last field must be greater than 0. </p>
 </dd>
<dt>*</dt>
<dd> <p> Lines are terminated by newline characters. </p>
 </dd>
<dt>*</dt>
<dd> <p> There is a limit on the number of lines in the file. In Linux 4.14 and earlier, this limit was (arbitrarily) set at 5 lines. Since Linux 4.15, the limit is 340 lines. In addition, the number of bytes written to the file must be less than the system page size, and the write must be performed at the start of the file (i.e., <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2) and <code><a href="/docs/linux/man/2-pwrite/">pwrite</a></code>(2) can&#8217;t be used to write to nonzero offsets in the file). </p>
 </dd>
<dt>*</dt>
<dd> <p> The range of user IDs (group IDs) specified in each line cannot overlap with the ranges in any other lines. In the initial implementation (Linux 3.8), this requirement was satisfied by a simplistic implementation that imposed the further requirement that the values in both field 1 and field 2 of successive lines must be in ascending numerical order, which prevented some otherwise valid maps from being created. Linux 3.9 and later fix this limitation, allowing any valid set of nonoverlapping maps. </p>
 </dd>
<dt>*</dt>
<dd> <p> At least one line must be written to the file. </p>
 </dd></dl>
<p> Writes that violate the above rules fail with the error <code>EINVAL</code>. </p>
<p> In order for a process to write to the <i>/proc/[pid]/uid_map</i> (<i>/proc/[pid]/gid_map</i>) file, all of the following requirements must be met: </p>
<dl>
<dt>1.</dt>
<dd> <p> The writing process must have the <code>CAP_SETUID</code> (<code>CAP_SETGID</code>) capability in the user namespace of the process <i>pid</i>. </p>
 </dd>
<dt>2.</dt>
<dd> <p> The writing process must either be in the user namespace of the process <i>pid</i> or be in the parent user namespace of the process <i>pid</i>. </p>
 </dd>
<dt>3.</dt>
<dd> <p> The mapped user IDs (group IDs) must in turn have a mapping in the parent user namespace. </p>
 </dd>
<dt>4.</dt>
<dd> <p> One of the following two cases applies: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>*</dt>
<dd> <p> <i>Either</i> the writing process has the <code>CAP_SETUID</code> (<code>CAP_SETGID</code>) capability in the <i>parent</i> user namespace. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>+</dt>
<dd> <p> No further restrictions apply: the process can make mappings to arbitrary user IDs (group IDs) in the parent user namespace. </p>
 </dd></dl>
</dl>
<dt>*</dt>
<dd> <p> <i>Or</i> otherwise all of the following restrictions apply: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>+</dt>
<dd> <p> The data written to <i>uid_map</i> (<i>gid_map</i>) must consist of a single line that maps the writing process&#8217;s effective user ID (group ID) in the parent user namespace to a user ID (group ID) in the user namespace. </p>
 </dd>
<dt>+</dt>
<dd> <p> The writing process must have the same effective user ID as the process that created the user namespace. </p>
 </dd>
<dt>+</dt>
<dd> <p> In the case of <i>gid_map</i>, use of the <code><a href="/docs/linux/man/2-setgroups/">setgroups</a></code>(2) system call must first be denied by writing &quot;<i>deny</i>&quot; to the <i>/proc/[pid]/setgroups</i> file (see below) before writing to <i>gid_map</i>. </p>
 </dd></dl>
</dl>
</dl>
</dl>
</dl>
<p> Writes that violate the above rules fail with the error <code>EPERM</code>.  </p>
<h3>Interaction with system calls that change process UIDs or GIDs</h3>
<p> In a user namespace where the <i>uid_map</i> file has not been written, the system calls that change user IDs will fail. Similarly, if the <i>gid_map</i> file has not been written, the system calls that change group IDs will fail. After the <i>uid_map</i> and <i>gid_map</i> files have been written, only the mapped values may be used in system calls that change user and group IDs. </p>
<p> For user IDs, the relevant system calls include <code><a href="/docs/linux/man/2-setuid/">setuid</a></code>(2), <code><a href="/docs/linux/man/2-setfsuid/">setfsuid</a></code>(2), <code><a href="/docs/linux/man/2-setreuid/">setreuid</a></code>(2), and <code><a href="/docs/linux/man/2-setresuid/">setresuid</a></code>(2). For group IDs, the relevant system calls include <code><a href="/docs/linux/man/2-setgid/">setgid</a></code>(2), <code><a href="/docs/linux/man/2-setfsgid/">setfsgid</a></code>(2), <code><a href="/docs/linux/man/2-setregid/">setregid</a></code>(2), <code><a href="/docs/linux/man/2-setresgid/">setresgid</a></code>(2), and <code><a href="/docs/linux/man/2-setgroups/">setgroups</a></code>(2). </p>
<p> Writing &quot;<i>deny</i>&quot; to the <i>/proc/[pid]/setgroups</i> file before writing to <i>/proc/[pid]/gid_map</i> will permanently disable <code><a href="/docs/linux/man/2-setgroups/">setgroups</a></code>(2) in a user namespace and allow writing to <i>/proc/[pid]/gid_map</i> without having the <code>CAP_SETGID</code> capability in the parent user namespace.  </p>
<h3>The /proc/[pid]/setgroups file</h3>
<p> The <i>/proc/[pid]/setgroups</i> file displays the string &quot;<i>allow</i>&quot; if processes in the user namespace that contains the process <i>pid</i> are permitted to employ the <code><a href="/docs/linux/man/2-setgroups/">setgroups</a></code>(2) system call; it displays &quot;<i>deny</i>&quot; if <code><a href="/docs/linux/man/2-setgroups/">setgroups</a></code>(2) is not permitted in that user namespace. Note that regardless of the value in the <i>/proc/[pid]/setgroups</i> file (and regardless of the process&#8217;s capabilities), calls to <code><a href="/docs/linux/man/2-setgroups/">setgroups</a></code>(2) are also not permitted if <i>/proc/[pid]/gid_map</i> has not yet been set. </p>
<p> A privileged process (one with the <code>CAP_SYS_ADMIN</code> capability in the namespace) may write either of the strings &quot;<i>allow</i>&quot; or &quot;<i>deny</i>&quot; to this file <i>before</i> writing a group ID mapping for this user namespace to the file <i>/proc/[pid]/gid_map</i>. Writing the string &quot;<i>deny</i>&quot; prevents any process in the user namespace from employing <code><a href="/docs/linux/man/2-setgroups/">setgroups</a></code>(2). </p>
<p> The essence of the restrictions described in the preceding paragraph is that it is permitted to write to <i>/proc/[pid]/setgroups</i> only so long as calling <code><a href="/docs/linux/man/2-setgroups/">setgroups</a></code>(2) is disallowed because <i>/proc/[pid]/gid_map</i> has not been set. This ensures that a process cannot transition from a state where <code><a href="/docs/linux/man/2-setgroups/">setgroups</a></code>(2) is allowed to a state where <code><a href="/docs/linux/man/2-setgroups/">setgroups</a></code>(2) is denied; a process can transition only from <code><a href="/docs/linux/man/2-setgroups/">setgroups</a></code>(2) being disallowed to <code><a href="/docs/linux/man/2-setgroups/">setgroups</a></code>(2) being allowed. </p>
<p> The default value of this file in the initial user namespace is &quot;<i>allow</i>&quot;. </p>
<p> Once <i>/proc/[pid]/gid_map</i> has been written to (which has the effect of enabling <code><a href="/docs/linux/man/2-setgroups/">setgroups</a></code>(2) in the user namespace), it is no longer possible to disallow <code><a href="/docs/linux/man/2-setgroups/">setgroups</a></code>(2) by writing &quot;<i>deny</i>&quot; to <i>/proc/[pid]/setgroups</i> (the write fails with the error <code>EPERM</code>). </p>
<p> A child user namespace inherits the <i>/proc/[pid]/setgroups</i> setting from its parent. </p>
<p> If the <i>setgroups</i> file has the value &quot;<i>deny</i>&quot;, then the <code><a href="/docs/linux/man/2-setgroups/">setgroups</a></code>(2) system call can&#8217;t subsequently be reenabled (by writing &quot;<i>allow</i>&quot; to the file) in this user namespace. (Attempts to do so fail with the error <code>EPERM</code>.) This restriction also propagates down to all child user namespaces of this user namespace. </p>
<p> The <i>/proc/[pid]/setgroups</i> file was added in Linux 3.19, but was backported to many earlier stable kernel series, because it addresses a security issue. The issue concerned files with permissions such as &quot;rwx---rwx&quot;. Such files give fewer permissions to &quot;group&quot; than they do to &quot;other&quot;. This means that dropping groups using <code><a href="/docs/linux/man/2-setgroups/">setgroups</a></code>(2) might allow a process file access that it did not formerly have. Before the existence of user namespaces this was not a concern, since only a privileged process (one with the <code>CAP_SETGID</code> capability) could call <code><a href="/docs/linux/man/2-setgroups/">setgroups</a></code>(2). However, with the introduction of user namespaces, it became possible for an unprivileged process to create a new namespace in which the user had all privileges. This then allowed formerly unprivileged users to drop groups and thus gain file access that they did not previously have. The <i>/proc/[pid]/setgroups</i> file was added to address this security issue, by denying any pathway for an unprivileged process to drop groups with <code><a href="/docs/linux/man/2-setgroups/">setgroups</a></code>(2).  </p>
<h3>Unmapped user and group IDs</h3>
<p> There are various places where an unmapped user ID (group ID) may be exposed to user space. For example, the first process in a new user namespace may call <code><a href="/docs/linux/man/2-getuid/">getuid</a></code>(2) before a user ID mapping has been defined for the namespace. In most such cases, an unmapped user ID is converted to the overflow user ID (group ID); the default value for the overflow user ID (group ID) is 65534. See the descriptions of <i>/proc/sys/kernel/overflowuid</i> and <i>/proc/sys/kernel/overflowgid</i> in <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5). </p>
<p> The cases where unmapped IDs are mapped in this fashion include system calls that return user IDs (<code><a href="/docs/linux/man/2-getuid/">getuid</a></code>(2), <code><a href="/docs/linux/man/2-getgid/">getgid</a></code>(2), and similar), credentials passed over a UNIX domain socket, credentials returned by <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2), <code><a href="/docs/linux/man/2-waitid/">waitid</a></code>(2), and the System V IPC &quot;ctl&quot; <code>IPC_STAT</code> operations, credentials exposed by <i>/proc/[pid]/status</i> and the files in <i>/proc/sysvipc/*</i>, credentials returned via the <i>si_uid</i> field in the <i>siginfo_t</i> received with a signal (see <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2)), credentials written to the process accounting file (see <code><a href="/docs/linux/man/5-acct/">acct</a></code>(5)), and credentials returned with POSIX message queue notifications (see <code><a href="/docs/linux/man/3-mq_notify/">mq_notify</a></code>(3)). </p>
<p> There is one notable case where unmapped user and group IDs are <i>not</i> converted to the corresponding overflow ID value. When viewing a <i>uid_map</i> or <i>gid_map</i> file in which there is no mapping for the second field, that field is displayed as 4294967295 (-1 as an unsigned integer).  </p>
<h3>Accessing files</h3>
<p> In order to determine permissions when an unprivileged process accesses a file, the process credentials (UID, GID) and the file credentials are in effect mapped back to what they would be in the initial user namespace and then compared to determine the permissions that the process has on the file. The same is also of other objects that employ the credentials plus permissions mask accessibility model, such as System V IPC objects  </p>
<h3>Operation of file-related capabilities</h3>
<p> Certain capabilities allow a process to bypass various kernel-enforced restrictions when performing operations on files owned by other users or groups. These capabilities are: <code>CAP_CHOWN</code>, <code>CAP_DAC_OVERRIDE</code>, <code>CAP_DAC_READ_SEARCH</code>, <code>CAP_FOWNER</code>, and <code>CAP_FSETID</code>. </p>
<p> Within a user namespace, these capabilities allow a process to bypass the rules if the process has the relevant capability over the file, meaning that: </p>
<dl>
<dt>*</dt>
<dd> <p> the process has the relevant effective capability in its user namespace; and </p>
 </dd>
<dt>*</dt>
<dd> <p> the file&#8217;s user ID and group ID both have valid mappings in the user namespace. </p>
 </dd></dl>
<p> The <code>CAP_FOWNER</code> capability is treated somewhat exceptionally: it allows a process to bypass the corresponding rules so long as at least the file&#8217;s user ID has a mapping in the user namespace (i.e., the file&#8217;s group ID does not need to have a valid mapping).  </p>
<h3>Set-user-ID and set-group-ID programs</h3>
<p> When a process inside a user namespace executes a set-user-ID (set-group-ID) program, the process&#8217;s effective user (group) ID inside the namespace is changed to whatever value is mapped for the user (group) ID of the file. However, if either the user <i>or</i> the group ID of the file has no mapping inside the namespace, the set-user-ID (set-group-ID) bit is silently ignored: the new program is executed, but the process&#8217;s effective user (group) ID is left unchanged. (This mirrors the semantics of executing a set-user-ID or set-group-ID program that resides on a filesystem that was mounted with the <code>MS_NOSUID</code> flag, as described in <code><a href="/docs/linux/man/2-mount/">mount</a></code>(2).)  </p>
<h3>Miscellaneous</h3>
<p> When a process&#8217;s user and group IDs are passed over a UNIX domain socket to a process in a different user namespace (see the description of <code>SCM_CREDENTIALS</code> in <code><a href="/docs/linux/man/7-unix/">unix</a></code>(7)), they are translated into the corresponding values as per the receiving process&#8217;s user and group ID mappings.  </p>
<h2>CONFORMING TO</h2>
<p> Namespaces are a Linux-specific feature.  </p>
<h2>NOTES</h2>
<p> Over the years, there have been a lot of features that have been added to the Linux kernel that have been made available only to privileged users because of their potential to confuse set-user-ID-root applications. In general, it becomes safe to allow the root user in a user namespace to use those features because it is impossible, while in a user namespace, to gain more privilege than the root user of a user namespace has.  </p>
<h3>Availability</h3>
<p> Use of user namespaces requires a kernel that is configured with the <code>CONFIG_USER_NS</code> option. User namespaces require support in a range of subsystems across the kernel. When an unsupported subsystem is configured into the kernel, it is not possible to configure user namespaces support. </p>
<p> As at Linux 3.8, most relevant subsystems supported user namespaces, but a number of filesystems did not have the infrastructure needed to map user and group IDs between user namespaces. Linux 3.9 added the required infrastructure support for many of the remaining unsupported filesystems (Plan 9 (9P), Andrew File System (AFS), Ceph, CIFS, CODA, NFS, and OCFS2). Linux 3.12 added support for the last of the unsupported major filesystems, XFS.  </p>
<h2>EXAMPLES</h2>
<p> The program below is designed to allow experimenting with user namespaces, as well as other types of namespaces. It creates namespaces as specified by command-line options and then executes a command inside those namespaces. The comments and <i>usage()</i> function inside the program provide a full explanation of the program. The following shell session demonstrates its use. </p>
<p> First, we look at the run-time environment: </p>
<p> $ <code>uname -rs</code> # Need Linux 3.8 or later Linux 3.8.0 $ <code>id -u</code> # Running as unprivileged user 1000 $ <code>id -g</code> 1000 </p>
<p> Now start a new shell in new user (<i>-U</i>), mount (<i>-m</i>), and PID (<i>-p</i>) namespaces, with user ID (<i>-M</i>) and group ID (<i>-G</i>) 1000 mapped to 0 inside the user namespace: </p>
<p> $ <code>./userns_child_exec -p -m -U -M &#8216;0 1000 1&#8217; -G &#8216;0 1000 1&#8217; bash</code> </p>
<p> The shell has PID 1, because it is the first process in the new PID namespace: </p>
<p> bash$ <code>echo $$</code> 1 </p>
<p> Mounting a new <i>/proc</i> filesystem and listing all of the processes visible in the new PID namespace shows that the shell can&#8217;t see any processes outside the PID namespace: </p>
<p> bash$ <code>mount -t proc proc /proc</code> bash$ <code>ps ax</code> <br />
&nbsp;<wbr>&nbsp;PID TTY&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;STAT&nbsp;<wbr>&nbsp;<wbr>&nbsp;TIME COMMAND <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1 pts/3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;S&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0:00 bash <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;22 pts/3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;R+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0:00 ps ax </p>
<p> Inside the user namespace, the shell has user and group ID 0, and a full set of permitted and effective capabilities: </p>
<p> bash$ <code>cat /proc/$$/status | egrep &#8216;ha[UG]id&#8217;</code> Uid:<code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>0 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>0 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>0 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>0<br />
 Gid:<code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>0 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>0 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>0 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>0<br />
 bash$ <code>cat /proc/$$/status | egrep &#8216;haCap(Prm|Inh|Eff)&#8216;</code> CapInh:<code>&nbsp;</code>0000000000000000<br />
 CapPrm:<code>&nbsp;</code>0000001fffffffff<br />
 CapEff:<code>&nbsp;</code>0000001fffffffff<br />
  </p>
<h3>Program source</h3>
<p> /* userns_child_exec.c </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Licensed under GNU General Public License v2 or later </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Create a child process that executes a shell command in new <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;namespace(s);&nbsp;allow UID and GID mappings to be specified when <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;creating a user namespace. */ #define _GNU_SOURCE #include &lt;sched.h&gt; #include &lt;unistd.h&gt; #include &lt;stdint.h&gt; #include &lt;stdlib.h&gt; #include &lt;sys/wait.h&gt; #include &lt;signal.h&gt; #include &lt;fcntl.h&gt; #include &lt;stdio.h&gt; #include &lt;string.h&gt; #include &lt;limits.h&gt; #include &lt;errno.h&gt; </p>
<p> /* A simple error-handling function: print an error message based <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;on the value in&nbsp;&#8216;errno&#8217;&nbsp;and terminate the calling process&nbsp;*/ </p>
<p> #define errExit(msg) do { perror(msg); exit(EXIT_FAILURE); \ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;while&nbsp;(0) </p>
<p> struct child_args { <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;**argv;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Command to be executed by child, with args&nbsp;*/ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pipe_fd[2];&nbsp;<wbr>&nbsp;/*&nbsp;Pipe used to synchronize parent and child&nbsp;*/ }; </p>
<p> static int verbose; </p>
<p> static void usage(char *pname) { <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s&nbsp;[options]&nbsp;cmd&nbsp;[arg...]\n\n&quot;, pname); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Create a child process that executes a shell&nbsp;&quot; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;command in a new user namespace,\n&quot; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;and possibly also other new namespace(s).\n\n&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Options can be:\n\n&quot;); #define fpe(str) fprintf(stderr, &quot; %s&quot;, str); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fpe(&quot;-i&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;New IPC namespace\n&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fpe(&quot;-m&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;New mount namespace\n&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fpe(&quot;-n&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;New network namespace\n&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fpe(&quot;-p&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;New PID namespace\n&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fpe(&quot;-u&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;New UTS namespace\n&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fpe(&quot;-U&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;New user namespace\n&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fpe(&quot;-M uid_map&nbsp;<wbr>&nbsp;Specify UID map for user namespace\n&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fpe(&quot;-G gid_map&nbsp;<wbr>&nbsp;Specify GID map for user namespace\n&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fpe(&quot;-z&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Map user&#8217;s UID and GID to 0 in user namespace\n&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fpe(&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(equivalent to: -M&nbsp;&#8216;0&nbsp;&lt;uid&gt;&nbsp;1&#8217;&nbsp;-G&nbsp;&#8216;0&nbsp;&lt;gid&gt;&nbsp;1&#8217;)\n&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fpe(&quot;-v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Display verbose messages\n&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fpe(&quot;\n&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fpe(&quot;If -z, -M, or -G is specified, -U is required.\n&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fpe(&quot;It is not permitted to specify both -z and either -M or -G.\n&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fpe(&quot;\n&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fpe(&quot;Map strings for -M and -G consist of records of the form:\n&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fpe(&quot;\n&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fpe(&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ID-inside-ns&nbsp;<wbr>&nbsp;<wbr>&nbsp;ID-outside-ns&nbsp;<wbr>&nbsp;<wbr>&nbsp;len\n&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fpe(&quot;\n&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fpe(&quot;A map string can contain multiple records, separated&quot; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;&nbsp;by commas;\n&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fpe(&quot;the commas are replaced by newlines before writing&quot; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;&nbsp;to map files.\n&quot;); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); } </p>
<p> /* Update the mapping file &#8216;map_file&#8217;, with the value provided in <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8216;mapping&#8217;, a string that defines a UID or GID mapping. A UID or <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;GID mapping consists of one or more newline-delimited records <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;of the form: </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ID_inside-ns&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ID-outside-ns&nbsp;<wbr>&nbsp;<wbr>&nbsp;length </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Requiring the user to supply a string that contains newlines is <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;of course inconvenient for command-line use. Thus, we permit the <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;use of commas to delimit records in this string, and replace them <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;with newlines before writing the string to the file.&nbsp;*/ </p>
<p> static void update_map(char *mapping, char *map_file) { <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int fd; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t map_len;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Length of&nbsp;&#8216;mapping&#8217;&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Replace commas in mapping string with newlines&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;map_len&nbsp;=&nbsp;strlen(mapping); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int j&nbsp;=&nbsp;0;&nbsp;j&nbsp;&lt;&nbsp;map_len;&nbsp;j++) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(mapping[j]&nbsp;==&nbsp;&#8216;,&#8216;) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mapping[j]&nbsp;=&nbsp;&#8216;\n&#8217;; </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fd&nbsp;=&nbsp;open(map_file, O_RDWR); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(fd&nbsp;==&nbsp;-1)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;ERROR: open&nbsp;%s:&nbsp;%s\n&quot;, map_file, <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;strerror(errno)); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(write(fd, mapping, map_len)&nbsp;!=&nbsp;map_len)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;ERROR: write&nbsp;%s:&nbsp;%s\n&quot;, map_file, <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;strerror(errno)); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;close(fd); } </p>
<p> /* Linux 3.19 made a change in the handling of <a href="/docs/linux/man/2-setgroups/">setgroups</a>(2) and the <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8216;gid_map&#8217;&nbsp;file to address a security issue. The issue allowed <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;*unprivileged*&nbsp;users to employ user namespaces in order to drop <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;The upshot of the 3.19 changes is that in order to update the <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8216;gid_maps&#8217;&nbsp;file, use of the setgroups()&nbsp;system call in this <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;user namespace must first be disabled by writing&nbsp;&quot;deny&quot;&nbsp;to one of <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;the&nbsp;/proc/PID/setgroups files for this namespace.&nbsp;<wbr>&nbsp;That is the <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;purpose of the following function.&nbsp;*/ </p>
<p> static void proc_setgroups_write(pid_t child_pid, char *str) { <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char setgroups_path[PATH_MAX]; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int fd; </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;snprintf(setgroups_path, PATH_MAX,&nbsp;&quot;/proc/%jd/setgroups&quot;, <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(intmax_t)&nbsp;child_pid); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fd&nbsp;=&nbsp;open(setgroups_path, O_RDWR); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(fd&nbsp;==&nbsp;-1)&nbsp;{ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;We may be on a system that doesn&#8217;t support <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/proc/PID/setgroups. In that case, the file won&#8217;t exist, <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;and the system won&#8217;t impose the restrictions that Linux 3.19 <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;added. That&#8217;s fine: we don&#8217;t need to do anything in order <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;to permit&nbsp;&#8216;gid_map&#8217;&nbsp;to be updated. </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;However, if the error from open()&nbsp;was something other than <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the ENOENT error that is expected for that case,&nbsp;<wbr>&nbsp;let the <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;user know.&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(errno&nbsp;!=&nbsp;ENOENT) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;ERROR: open&nbsp;%s:&nbsp;%s\n&quot;, setgroups_path, <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;strerror(errno)); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(write(fd, str, strlen(str))&nbsp;==&nbsp;-1) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;ERROR: write&nbsp;%s:&nbsp;%s\n&quot;, setgroups_path, <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;strerror(errno)); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;close(fd); } </p>
<p> static int /* Start function for cloned child */ childFunc(void *arg) { <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct child_args&nbsp;*args&nbsp;=&nbsp;arg; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char ch; </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Wait until the parent has updated the UID and GID mappings. <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;See the comment in main(). We wait for end of file on a <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pipe that will be closed by the parent process once it has <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;updated the mappings.&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;close(args-&gt;pipe_fd[1]);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Close our descriptor for the write <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;end of the pipe so that we see EOF <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;when parent closes its descriptor&nbsp;*/ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(read(args-&gt;pipe_fd[0],&nbsp;&amp;ch, 1)&nbsp;!=&nbsp;0)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr, <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;Failure in child: read from pipe returned&nbsp;!=&nbsp;0\n&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;close(args-&gt;pipe_fd[0]); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Execute a shell command&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;About to exec&nbsp;%s\n&quot;, args-&gt;argv[0]); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;execvp(args-&gt;argv[0], args-&gt;argv); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;execvp&quot;); } </p>
<p> #define STACK_SIZE (1024 * 1024) </p>
<p> static char child_stack[STACK_SIZE]; /* Space for child&#8217;s stack */ </p>
<p> int main(int argc, char *argv[]) { <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int flags, opt, map_zero; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pid_t child_pid; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct child_args args; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*uid_map,&nbsp;*gid_map; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;const int MAP_BUF_SIZE&nbsp;=&nbsp;100; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char map_buf[MAP_BUF_SIZE]; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char map_path[PATH_MAX]; </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Parse command-line options. The initial&nbsp;&#8216;+&#8216;&nbsp;character in <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the final getopt()&nbsp;argument prevents GNU-style permutation <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;of command-line options. That&#8217;s useful, since sometimes <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the&nbsp;&#8216;command&#8217;&nbsp;to be executed by this program itself <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;has command-line options. We don&#8217;t want getopt()&nbsp;to treat <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;those as options to this program.&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;flags&nbsp;=&nbsp;0; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;verbose&nbsp;=&nbsp;0; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gid_map&nbsp;=&nbsp;NULL; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uid_map&nbsp;=&nbsp;NULL; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;map_zero&nbsp;=&nbsp;0; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while&nbsp;((opt&nbsp;=&nbsp;getopt(argc, argv,&nbsp;&quot;+imnpuUM:G:zv&quot;))&nbsp;!=&nbsp;-1)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;switch&nbsp;(opt)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case&nbsp;&#8216;i&#8217;: flags |=&nbsp;CLONE_NEWIPC;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case&nbsp;&#8216;m&#8217;: flags |=&nbsp;CLONE_NEWNS;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case&nbsp;&#8216;n&#8217;: flags |=&nbsp;CLONE_NEWNET;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case&nbsp;&#8216;p&#8217;: flags |=&nbsp;CLONE_NEWPID;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case&nbsp;&#8216;u&#8217;: flags |=&nbsp;CLONE_NEWUTS;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case&nbsp;&#8216;v&#8217;: verbose&nbsp;=&nbsp;1;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case&nbsp;&#8216;z&#8217;: map_zero&nbsp;=&nbsp;1;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case&nbsp;&#8216;M&#8217;: uid_map&nbsp;=&nbsp;optarg;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case&nbsp;&#8216;G&#8217;: gid_map&nbsp;=&nbsp;optarg;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case&nbsp;&#8216;U&#8217;: flags |=&nbsp;CLONE_NEWUSER;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;default:&nbsp;<wbr>&nbsp;usage(argv[0]); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;-M or -G without -U is nonsensical&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(((uid_map&nbsp;!=&nbsp;NULL || gid_map&nbsp;!=&nbsp;NULL || map_zero)&nbsp;&amp;&amp; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;!(flags&nbsp;&amp;&nbsp;CLONE_NEWUSER))&nbsp;|| <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(map_zero&nbsp;&amp;&amp;&nbsp;(uid_map&nbsp;!=&nbsp;NULL || gid_map&nbsp;!=&nbsp;NULL))) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;usage(argv[0]); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;args.argv&nbsp;=&nbsp;&amp;argv[optind]; </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;We use a pipe to synchronize the parent and child, in order to <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ensure that the parent sets the UID and GID maps before the child <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;calls execve(). This ensures that the child maintains its <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;capabilities during the execve()&nbsp;in the common case where we <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;want to map the child&#8217;s effective user ID to 0 in the new user <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;namespace. Without this synchronization, the child would lose <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;its capabilities if it performed an execve()&nbsp;with nonzero <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;user IDs&nbsp;(see the&nbsp;<a href="/docs/linux/man/7-capabilities/">capabilities</a>(7)&nbsp;man page for details of the <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;transformation of a process&#8217;s capabilities during execve()).&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(pipe(args.pipe_fd)&nbsp;==&nbsp;-1) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;pipe&quot;); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Create the child in new namespace(s)&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;child_pid&nbsp;=&nbsp;clone(childFunc, child_stack&nbsp;+&nbsp;STACK_SIZE, <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;flags | SIGCHLD,&nbsp;&amp;args); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(child_pid&nbsp;==&nbsp;-1) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;clone&quot;); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Parent falls through to here&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(verbose) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%s: PID of child created by clone()&nbsp;is&nbsp;%jd\n&quot;, <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;argv[0],&nbsp;(intmax_t)&nbsp;child_pid); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Update the UID and GID maps in the child&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(uid_map&nbsp;!=&nbsp;NULL || map_zero)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;snprintf(map_path, PATH_MAX,&nbsp;&quot;/proc/%jd/uid_map&quot;, <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(intmax_t)&nbsp;child_pid); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(map_zero)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;snprintf(map_buf, MAP_BUF_SIZE,&nbsp;&quot;0&nbsp;%jd 1&quot;, <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(intmax_t)&nbsp;getuid()); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uid_map&nbsp;=&nbsp;map_buf; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;update_map(uid_map, map_path); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(gid_map&nbsp;!=&nbsp;NULL || map_zero)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;proc_setgroups_write(child_pid,&nbsp;&quot;deny&quot;); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;snprintf(map_path, PATH_MAX,&nbsp;&quot;/proc/%jd/gid_map&quot;, <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(intmax_t)&nbsp;child_pid); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(map_zero)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;snprintf(map_buf, MAP_BUF_SIZE,&nbsp;&quot;0&nbsp;%ld 1&quot;, <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(intmax_t)&nbsp;getgid()); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gid_map&nbsp;=&nbsp;map_buf; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;update_map(gid_map, map_path); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Close the write end of the pipe, to signal to the child that we <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;have updated the UID and GID maps&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;close(args.pipe_fd[1]); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(waitpid(child_pid, NULL, 0)&nbsp;==&nbsp;-1)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Wait for child&nbsp;*/ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;waitpid&quot;); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(verbose) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%s: terminating\n&quot;, argv[0]); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-newgidmap/">newgidmap</a></code>(1), <code><a href="/docs/linux/man/1-newuidmap/">newuidmap</a></code>(1), <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2), <code><a href="/docs/linux/man/2-setns/">setns</a></code>(2), <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2), <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5), <code><a href="/docs/linux/man/5-subgid/">subgid</a></code>(5), <code><a href="/docs/linux/man/5-subuid/">subuid</a></code>(5), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-cgroup_namespaces/">cgroup_namespaces</a></code>(7), <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7), <code><a href="/docs/linux/man/7-namespaces/">namespaces</a></code>(7), <code><a href="/docs/linux/man/7-pid_namespaces/">pid_namespaces</a></code>(7) </p>
<p> The kernel source file <i>Documentation/namespaces/resource-control.txt</i>.  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
