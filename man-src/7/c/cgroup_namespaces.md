---
title: "cgroup_namespaces(7)"
name: "cgroup_namespaces"
section: "7"
letter: "c"
url: "/docs/linux/man/7-cgroup_namespaces/"
description: "cgroup_namespaces – overview of Linux cgroup namespaces"
---

<p>cgroup_namespaces &#8211; overview of Linux cgroup namespaces</p>
<h2>Description</h2>
<p>For an overview of namespaces, see <code><a href="/docs/linux/man/7-namespaces/">namespaces</a></code>(7). </p>
<p> Cgroup namespaces virtualize the view of a process&#8217;s cgroups (see <code><a href="/docs/linux/man/7-cgroups/">cgroups</a></code>(7)) as seen via <i>/proc/[pid]/cgroup</i> and <i>/proc/[pid]/mountinfo</i>. </p>
<p> Each cgroup namespace has its own set of cgroup root directories. These root directories are the base points for the relative locations displayed in the corresponding records in the <i>/proc/[pid]/cgroup</i> file. When a process creates a new cgroup namespace using <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) or <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2) with the <code>CLONE_NEWCGROUP</code> flag, its current cgroups directories become the cgroup root directories of the new namespace. (This applies both for the cgroups version 1 hierarchies and the cgroups version 2 unified hierarchy.) </p>
<p> When reading the cgroup memberships of a &quot;target&quot; process from <i>/proc/[pid]/cgroup</i>, the pathname shown in the third field of each record will be relative to the reading process&#8217;s root directory for the corresponding cgroup hierarchy. If the cgroup directory of the target process lies outside the root directory of the reading process&#8217;s cgroup namespace, then the pathname will show <i>../</i> entries for each ancestor level in the cgroup hierarchy. </p>
<p> The following shell session demonstrates the effect of creating a new cgroup namespace. </p>
<p> First, (as superuser) in a shell in the initial cgroup namespace, we create a child cgroup in the <i>freezer</i> hierarchy, and place a process in that cgroup that we will use as part of the demonstration below: </p>
<p> # <code>mkdir -p /sys/fs/cgroup/freezer/sub2</code> # <code>sleep 10000 &amp;</code> # Create a process that lives for a while [1] 20124 # <code>echo 20124 &gt; /sys/fs/cgroup/freezer/sub2/cgroup.procs</code> </p>
<p> We then create another child cgroup in the <i>freezer</i> hierarchy and put the shell into that cgroup: </p>
<p> # <code>mkdir -p /sys/fs/cgroup/freezer/sub</code> # <code>echo $$</code> # Show PID of this shell 30655 # <code>echo 30655 &gt; /sys/fs/cgroup/freezer/sub/cgroup.procs</code> # <code>cat /proc/self/cgroup | grep freezer</code> 7:freezer:/sub </p>
<p> Next, we use <code><a href="/docs/linux/man/1-unshare/">unshare</a></code>(1) to create a process running a new shell in new cgroup and mount namespaces: </p>
<p> # <code>PS1=&quot;sh2# &quot; unshare -Cm bash</code> </p>
<p> From the new shell started by <code><a href="/docs/linux/man/1-unshare/">unshare</a></code>(1), we then inspect the <i>/proc/[pid]/cgroup</i> files of, respectively, the new shell, a process that is in the initial cgroup namespace (<i>init</i>, with PID 1), and the process in the sibling cgroup (<i>sub2</i>): </p>
<p> sh2# <code>cat /proc/self/cgroup | grep freezer</code> 7:freezer:/ sh2# <code>cat /proc/1/cgroup | grep freezer</code> 7:freezer:/.. sh2# <code>cat /proc/20124/cgroup | grep freezer</code> 7:freezer:/../sub2 </p>
<p> From the output of the first command, we see that the freezer cgroup membership of the new shell (which is in the same cgroup as the initial shell) is shown defined relative to the freezer cgroup root directory that was established when the new cgroup namespace was created. (In absolute terms, the new shell is in the <i>/sub</i> freezer cgroup, and the root directory of the freezer cgroup hierarchy in the new cgroup namespace is also <i>/sub</i>. Thus, the new shell&#8217;s cgroup membership is displayed as &#8216;/&#8217;.) </p>
<p> However, when we look in <i>/proc/self/mountinfo</i> we see the following anomaly: </p>
<p> sh2# <code>cat /proc/self/mountinfo | grep freezer</code> 155 145 0:32 /.. /sys/fs/cgroup/freezer &#8230; </p>
<p> The fourth field of this line (<i>/..</i>) should show the directory in the cgroup filesystem which forms the root of this mount. Since by the definition of cgroup namespaces, the process&#8217;s current freezer cgroup directory became its root freezer cgroup directory, we should see &#8216;/&#8217; in this field. The problem here is that we are seeing a mount entry for the cgroup filesystem corresponding to the initial cgroup namespace (whose cgroup filesystem is indeed rooted at the parent directory of <i>sub</i>). To fix this problem, we must remount the freezer cgroup filesystem from the new shell (i.e., perform the mount from a process that is in the new cgroup namespace), after which we see the expected results: </p>
<p> sh2# <code>mount &#8211;make-rslave /</code> # Don&#8217;t propagate mount events<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;to other namespaces sh2# <code>umount /sys/fs/cgroup/freezer</code> sh2# <code>mount -t cgroup -o freezer freezer /sys/fs/cgroup/freezer</code> sh2# <code>cat /proc/self/mountinfo | grep freezer</code> 155 145 0:32 / /sys/fs/cgroup/freezer rw,relatime &#8230;</p>
<h2>Conforming To</h2>
<p>Namespaces are a Linux-specific feature.</p>
<h2>Notes</h2>
<p>Use of cgroup namespaces requires a kernel that is configured with the <code>CONFIG_CGROUPS</code> option. </p>
<p> The virtualization provided by cgroup namespaces serves a number of purposes:</p>
<dl>
<dt>*</p>
<dd>It prevents information leaks whereby cgroup directory paths outside of a container would otherwise be visible to processes in the container. Such leakages could, for example, reveal information about the container framework to containerized applications.</p>
<dt>*</p>
<dd>It eases tasks such as container migration. The virtualization provided by cgroup namespaces allows containers to be isolated from knowledge of the pathnames of ancestor cgroups. Without such isolation, the full cgroup pathnames (displayed in <i>/proc/self/cgroups</i>) would need to be replicated on the target system when migrating a container; those pathnames would also need to be unique, so that they don&#8217;t conflict with other pathnames on the target system.</p>
<dt>*</p>
<dd>It allows better confinement of containerized processes, because it is possible to mount the container&#8217;s cgroup filesystems such that the container processes can&#8217;t gain access to ancestor cgroup directories. Consider, for example, the following scenario:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>We have a cgroup directory, <i>/cg/1</i>, that is owned by user ID 9000.</p>
<dt>&bull;</p>
<dd>We have a process, <i>X</i>, also owned by user ID 9000, that is namespaced under the cgroup <i>/cg/1/2</i> (i.e., <i>X</i> was placed in a new cgroup namespace via <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) or <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2) with the <code>CLONE_NEWCGROUP</code> flag).</dl>
</dl>
<dd>In the absence of cgroup namespacing, because the cgroup directory <i>/cg/1</i> is owned (and writable) by UID 9000 and process <i>X</i> is also owned by user ID 9000, process <i>X</i> would be able to modify the contents of cgroups files (i.e., change cgroup settings) not only in <i>/cg/1/2</i> but also in the ancestor cgroup directory <i>/cg/1</i>. Namespacing process <i>X</i> under the cgroup directory <i>/cg/1/2</i>, in combination with suitable mount operations for the cgroup filesystem (as shown above), prevents it modifying files in <i>/cg/1</i>, since it cannot even see the contents of that directory (or of further removed cgroup ancestor directories). Combined with correct enforcement of hierarchical limits, this prevents process <i>X</i> from escaping the limits imposed by ancestor cgroups.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-unshare/">unshare</a></code>(1), <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), <code><a href="/docs/linux/man/2-setns/">setns</a></code>(2), <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2), <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5), <code><a href="/docs/linux/man/7-cgroups/">cgroups</a></code>(7), <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7), <code><a href="/docs/linux/man/7-namespaces/">namespaces</a></code>(7), <code><a href="/docs/linux/man/7-user_namespaces/">user_namespaces</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
