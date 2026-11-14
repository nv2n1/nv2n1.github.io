---
title: "virt-what(1)"
name: "virt-what"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-what/"
description: "virt-what – detect if we are running in a virtual machine"
---

<h2 class="name">NAME</h2>
<p> virt-what &#8211; detect if we are running in a virtual machine </p>
<h2>SUMMARY</h2>
<p> virt-what [options]</p>
<h2>DESCRIPTION</h2>
<p> <tt>&quot;virt-what&quot;</tt> is a shell script which can be used to detect if the program is running in a virtual machine. </p>
<p> The program prints out a list of &#8220;facts&#8221; about the virtual machine, derived from heuristics. One fact is printed per line. </p>
<p> If nothing is printed and the script exits with code 0 (no error), then it can mean <i>either</i> that the program is running on bare-metal <i>or</i> the program is running inside a type of virtual machine which we don&#8217;t know about or cannot detect.</p>
<h2>FACTS</h2>
<dl>
<dt><code>docker</code></p>
<dd> This is a Docker container. </p>
<p> Status: confirmed by Charles Nguyen</p>
<dt><code>hyperv</code></p>
<dd> This is Microsoft Hyper-V hypervisor. </p>
<p> Status: confirmed by <font SIZE="-1">RWMJ</font></p>
<dt><code>ibm_power-kvm</code></p>
<dd> This is an <font SIZE="-1">IBM POWER KVM</font> guest. </p>
<p> Status: contributed by Adrian Likins.</p>
<dt><code>ibm_power-lpar_shared</code></p>
<dd>
<dt><code>ibm_power-lpar_dedicated</code></p>
<dd> This is an <font SIZE="-1">IBM POWER LPAR </font>(hardware partition) in either shared or dedicated mode. </p>
<p> Status: contributed by Adrian Likins.</p>
<dt><code>ibm_systemz</code></p>
<dd> This is an <font SIZE="-1">IBM</font> SystemZ (or other S/390) hardware partitioning system. Additional facts listed below may also be printed.</p>
<dt><code>ibm_systemz-direct</code></p>
<dd> This is Linux running directly on a <font SIZE="-1">IBM</font> SystemZ hardware partitioning system. </p>
<p> This is expected to be a highly unusual configuration &#8211; if you see this result you should treat it with suspicion. </p>
<p> Status: not confirmed</p>
<dt><code>ibm_systemz-lpar</code></p>
<dd> This is Linux running directly on an <font SIZE="-1">LPAR</font> on an <font SIZE="-1">IBM</font> SystemZ hardware partitioning system. </p>
<p> Status: not confirmed</p>
<dt><code>ibm_systemz-zvm</code></p>
<dd> This is a z/VM guest running in an <font SIZE="-1">LPAR</font> on an <font SIZE="-1">IBM</font> SystemZ hardware partitioning system. </p>
<p> Status: confirmed by <font SIZE="-1">RWMJ</font> using a Fedora guest running in z/VM</p>
<dt><code>linux_vserver</code></p>
<dd> This is printed for backwards compatibility with older virt-what which could not distinguish between a Linux VServer container guest and host.</p>
<dt><code>linux_vserver-guest</code></p>
<dd> This process is running in a Linux VServer container. </p>
<p> Status: contributed by BarXX Metin</p>
<dt><code>linux_vserver-host</code></p>
<dd> This process is running as the Linux VServer host (VxID 0). </p>
<p> Status: contributed by BarXX Metin and Elan Ruusama.e</p>
<dt><code>lxc</code></p>
<dd> This process is running in a Linux <font SIZE="-1">LXC</font> container. </p>
<p> Status: contributed by Marc Fournier</p>
<dt><code>kvm</code></p>
<dd> This guest is running on the <font SIZE="-1">KVM</font> hypervisor using hardware acceleration. </p>
<p> Note that if the hypervisor is using software acceleration you should <i>not</i> see this, but should see the <tt>&quot;qemu&quot;</tt> fact instead. </p>
<p> Status: confirmed by <font SIZE="-1">RWMJ.</font></p>
<dt><code>lkvm</code></p>
<dd> This guest is running on the <font SIZE="-1">KVM</font> hypervisor using hardware acceleration, and the userspace component of the hypervisor is lkvm (a.k.a kvmtool). </p>
<p> Status: contributed by Andrew Jones</p>
<dt><code>openvz</code></p>
<dd> The guest appears to be running inside an OpenVZ or Virtuozzo container. </p>
<p> Status: contributed by Evgeniy Sokolov</p>
<dt><code>ovirt</code></p>
<dd> The guest is running on an oVirt node. (See also <tt>&quot;rhev&quot;</tt> below). </p>
<p> Status: contributed by <font SIZE="-1">RWMJ,</font> not confirmed</p>
<dt><code>parallels</code></p>
<dd> The guest is running inside Parallels Virtual Platform (Parallels Desktop, Parallels Server). </p>
<p> Status: contributed by Justin Clift</p>
<dt><code>powervm_lx86</code></p>
<dd> The guest is running inside <font SIZE="-1">IBM</font> PowerVM Lx86 Linux/x86 emulator. </p>
<p> Status: data originally supplied by Jeffrey Scheel, confirmed by Yufang Zhang and <font SIZE="-1">RWMJ</font></p>
<dt><code>qemu</code></p>
<dd> This is <font SIZE="-1">QEMU</font> hypervisor using software emulation. </p>
<p> Note that for <font SIZE="-1">KVM </font>(hardware accelerated) guests you should <i>not</i> see this. </p>
<p> Status: confirmed by <font SIZE="-1">RWMJ.</font></p>
<dt><code>rhev</code></p>
<dd> The guest is running on a Red Hat Enterprise Virtualization (<font SIZE="-1">RHEV</font>) node. </p>
<p> Status: confirmed by <font SIZE="-1">RWMJ</font></p>
<dt><code>uml</code></p>
<dd> This is a User-Mode Linux (<font SIZE="-1">UML</font>) guest. </p>
<p> Status: contributed by Laurent Leonard</p>
<dt><code>virt</code></p>
<dd> Some sort of virtualization appears to be present, but we are not sure what it is. In some very rare corner cases where we know that virtualization is hard to detect, we will try a timing attack to see if certain machine instructions are running much more slowly than they should be, which would indicate virtualization. In this case, the generic fact <tt>&quot;virt&quot;</tt> is printed.</p>
<dt><code>virtage</code></p>
<dd> This is Hitachi Virtualization Manager (<font SIZE="-1">HVM</font>) Virtage hardware partitioning system. </p>
<p> Status: data supplied by Bhavna Sarathy, not confirmed</p>
<dt><code>virtualbox</code></p>
<dd> This is a VirtualBox guest. </p>
<p> Status: contributed by Laurent Leonard</p>
<dt><code>virtualpc</code></p>
<dd> The guest appears to be running on Microsoft VirtualPC. </p>
<p> Status: not confirmed</p>
<dt><code>vmware</code></p>
<dd> The guest appears to be running on VMware hypervisor. </p>
<p> Status: confirmed by <font SIZE="-1">RWMJ</font></p>
<dt><code>xen</code></p>
<dd> The guest appears to be running on Xen hypervisor. </p>
<p> Status: confirmed by <font SIZE="-1">RWMJ</font></p>
<dt><code>xen-dom0</code></p>
<dd> This is the Xen dom0 (privileged domain). </p>
<p> Status: confirmed by <font SIZE="-1">RWMJ</font></p>
<dt><code>xen-domU</code></p>
<dd> This is a Xen domU (paravirtualized guest domain). </p>
<p> Status: confirmed by <font SIZE="-1">RWMJ</font></p>
<dt><code>xen-hvm</code></p>
<dd> This is a Xen guest fully virtualized (<font SIZE="-1">HVM</font>). </p>
<p> Status: confirmed by <font SIZE="-1">RWMJ</font></dl>
<h2>EXIT STATUS</h2>
<p> Programs that use or wrap <tt>&quot;virt-what&quot;</tt> should check that the exit status is 0 before they attempt to parse the output of the command. </p>
<p> A non-zero exit status indicates some error, for example, an unrecognized command line argument. If the exit status is non-zero then the output &#8220;facts&#8221; (if any were printed) cannot be guaranteed and should be ignored. </p>
<p> The exit status does <i>not</i> have anything to do with whether the program is running on baremetal or under virtualization, nor with whether <tt>&quot;virt-what&quot;</tt> managed detection &#8220;correctly&#8221; (which is basically unknowable given the large variety of virtualization systems out there and that some systems deliberately emulate others).</p>
<h2>RUNNING VIRT-WHAT FROM OTHER PROGRAMS</h2>
<p> <tt>&quot;virt-what&quot;</tt> is designed so that you can easily run it from other programs or wrap it up in a library. </p>
<p> Your program should check the exit status (see the section above). </p>
<p> Some programming languages (notably Python: issue 1652) erroneously mask the <tt>&quot;SIGPIPE&quot;</tt> signal and do not restore it when executing subprocesses. <tt>&quot;virt-what&quot;</tt> is a shell script and some shell commands do not work correctly when you do this. You may see warnings from <tt>&quot;virt-what&quot;</tt> similar to this: </p>
<pre>
 echo: write error: Broken pipe
</pre>
<p> The solution is to set the <tt>&quot;SIGPIPE&quot;</tt> signal handler back to <tt>&quot;SIG_DFL&quot;</tt> before running <tt>&quot;virt-what&quot;</tt>.</p>
<h2>IMPORTANT NOTE</h2>
<p> Most of the time, using this program is the <i>wrong</i> thing to do. Instead you should detect the specific features you actually want to use. (As an example, if you wanted to issue Xen hypervisor commands you would look for the <tt>&quot;/proc/xen/privcmd&quot;</tt> file). </p>
<p> However people keep asking for this, so we provide it. There are a few legitimate uses:</p>
<dl>
<dt>Bug reporting tool</p>
<dd> If you think that virtualization could affect how your program runs, then you might use <tt>&quot;virt-what&quot;</tt> to report this in a bug reporting tool.</p>
<dt>Status display and monitoring tools</p>
<dd> You might include this information in status and monitoring programs.</p>
<dt>System tuning (sometimes)</p>
<dd> You might use this program to tune an operating system so it runs better as a virtual machine of a particular hypervisor. However if installing paravirtualized drivers, it&#8217;s better to check for the specific features your drivers need (eg. for the presence of <font SIZE="-1">PCI</font> devices).</dl>
<h2>SEE ALSO</h2>
<p> &lt;<a rel="nofollow" href="http://people.redhat.com/~rjones/virt-what/">http://people.redhat.com/~rjones/virt-what/</a>&gt;, &lt;<a rel="nofollow" href="http://www.vmware.com/">http://www.vmware.com/</a>&gt;, &lt;<a rel="nofollow" href="http://www.microsoft.com/windows/products/winfamily/virtualpc">http://www.microsoft.com/windows/products/winfamily/virtualpc</a>&gt;, &lt;<a rel="nofollow" href="http://xensource.com/">http://xensource.com/</a>&gt;, &lt;<a rel="nofollow" href="http://bellard.org/qemu/">http://bellard.org/qemu/</a>&gt;, &lt;<a rel="nofollow" href="http://kvm.qumranet.com/">http://kvm.qumranet.com/</a>&gt;, &lt;<a rel="nofollow" href="http://openvz.org/">http://openvz.org/</a>&gt;</p>
<h2>AUTHORS</h2>
<p> Richard W.M. Jones &lt;rjones @ redhat . com&gt;</p>
<h2>COPYRIGHT</h2>
<p> (C) Copyright 2008-2015 Red Hat Inc., &lt;<a rel="nofollow" href="http://people.redhat.com/~rjones/virt-what/">http://people.redhat.com/~rjones/virt-what/</a>&gt; </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, <font SIZE="-1">MA 02139, USA.</font></p>
<h2>REPORTING BUGS</h2>
<p> Bugs can be viewed on the Red Hat Bugzilla page: &lt;<a rel="nofollow" href="https://bugzilla.redhat.com/">https://bugzilla.redhat.com/</a>&gt;. </p>
<p> If you find a bug in virt-what, please follow these steps to report it:</p>
<dl>
<dt>1. Check for existing bug reports</p>
<dd> Go to &lt;<a rel="nofollow" href="https://bugzilla.redhat.com/">https://bugzilla.redhat.com/</a>&gt; and search for similar bugs. Someone may already have reported the same bug, and they may even have fixed it.</p>
<dt>2. Capture debug and error messages</p>
<dd> Run </p>
<pre>
 virt-what &gt; virt-what.log 2&gt;&amp;1
</pre>
<p> and keep <i>virt-what.log</i>. It may contain error messages which you should submit with your bug report.</p>
<dt>3. Get version of virt-what.</p>
<dd> Run </p>
<pre>
 virt-what --version
</pre>
<dt>4. Submit a bug report.</p>
<dd> Go to &lt;<a rel="nofollow" href="https://bugzilla.redhat.com/">https://bugzilla.redhat.com/</a>&gt; and enter a new bug. Please describe the problem in as much detail as possible. </p>
<p> Remember to include the version numbers (step 3) and the debug messages file (step 2) and as much other detail as possible.</p>
<dt>5. Assign the bug to rjones @ redhat.com</p>
<dd> Assign or reassign the bug to <code>rjones @ redhat.com</code> (without the spaces). You can also send me an email with the bug number if you want a faster response. </p>
</dl>
<h2>Index</h2>
