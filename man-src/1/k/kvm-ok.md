---
title: "kvm-ok(1)"
name: "kvm-ok"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kvm-ok/"
description: "kvm-ok – determine if this system is capable of running hardware accelerated KVM virtual machines (ie, possesses Virtualization Technology)"
---

<h2 class="name">NAME</h2>
<p> <code>kvm-ok</code> &#8211; determine if this system is capable of running hardware accelerated KVM virtual machines (ie, possesses Virtualization Technology)</p>
<h2>DESCRIPTION</h2>
<p> <code>kvm-ok</code> is a program that will determine if the locate system can host hardware accelerated KVM virtual machines. </p>
<p> The program will first determine if <i>/proc/cpuinfo</i> contains the flags indicating that the CPU has the Virtualization Technology (VT) capability. </p>
<p> Next, it will check if the <i>/dev/kvm</i> device exists. </p>
<p> If running as root, it will check your CPU&#8217;s MSRs to see if VT is disabled in the BIOS. </p>
<p> In some failure cases, <code>kvm-ok</code> provides hints on how you might go about enabling KVM on a system where it is arbitrarily disabled. </p>
<p> If KVM can be used, this script will exit 0, otherwise it will exit non-zero. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-kvm/">kvm</a></code>(1), <code><a href="/docs/linux/man/1-dmesg/">dmesg</a></code>(1) </p>
<h2>FILES</h2>
<p> <i>/proc/cpuinfo</i>, <i>/dev/kvm</i> </p>
<h2>BUGS</h2>
<p> The disabled-by-bios check currently scans <code><a href="/docs/linux/man/1-dmesg/">dmesg</a></code>(1) for a message displayed by the kernel. This is not ideal, in that a long-running system will eventually roll the dmesg logs. The kernel should expose the disabled-by-bios flag in <i>/proc/cpuinfo</i>. </p>
<p> <i><a rel="nofollow" href="https://bugs.launchpad.net/ubuntu/+source/linux/+bug/535373">https://bugs.launchpad.net/ubuntu/+source/linux/+bug/535373</a></i> </p>
<h2>MORE INFORMATION</h2>
<p> <i><a rel="nofollow" href="http://launchpad.net/cpu-checker">http://launchpad.net/cpu-checker</a></i> </p>
<h2>AUTHOR</h2>
<p> This manpage and the utility was written by Dustin Kirkland &lt;kirkland [at] canonical.com&gt; for Ubuntu systems (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 3 published by the Free Software Foundation. </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL-3. </p>
<h2>Index</h2>
