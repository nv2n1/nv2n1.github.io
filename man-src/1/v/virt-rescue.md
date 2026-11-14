---
title: "virt-rescue(1)"
name: "virt-rescue"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-rescue/"
description: "virt-rescue – Run a rescue shell on a virtual machine"
---

<h2 class="name">NAME</h2>
<p> virt-rescue &#8211; Run a rescue shell on a virtual machine </p>
<h2>SYNOPSIS</h2>
<pre><code>
virt - rescue[--options] - d domname virt - rescue[--options] - a disk.img[-a disk.img...] virt - rescue-- suggest(-d domname | -a disk.img...)
</code></pre>
<p> Old style: </p>
<p>virt &#8211; rescue[&#8211;options] domname virt &#8211; rescue[&#8211;options] disk.img[disk.img&#8230;]</p>
<h2>WARNING</h2>
<p> Using <tt>&quot;virt-rescue&quot;</tt> in write mode on live virtual machines, or concurrently with other disk editing tools, can be dangerous, potentially causing disk corruption. The virtual machine must be shut down before you use this command, and disk images must not be edited concurrently. </p>
<p> Use the <i>&#8211;ro</i> (read-only) option to use <tt>&quot;virt-rescue&quot;</tt> safely if the disk image or virtual machine might be live. You may see strange or inconsistent results if running concurrently with other changes, but with this option you won&#8217;t risk disk corruption.</p>
<h2>DESCRIPTION</h2>
<p> virt-rescue is like a Rescue <font SIZE="-1">CD,</font> but for virtual machines, and without the need for a <font SIZE="-1">CD. </font> virt-rescue gives you a rescue shell and some simple recovery tools which you can use to examine or rescue a virtual machine or disk image. </p>
<p> You can run virt-rescue on any virtual machine known to libvirt, or directly on disk image(s): </p>
<pre>
 virt-rescue -d GuestName
 virt-rescue --ro -a /path/to/disk.img
 virt-rescue -a /dev/sdc
</pre>
<p> For live VMs you <i>must</i> use the &#8211;ro option. </p>
<p> When you run virt-rescue on a virtual machine or disk image, you are placed in an interactive bash shell where you can use many ordinary Linux commands. What you see in <i>/</i> (<i>/bin</i>, <i>/lib</i> etc) is the rescue appliance. You must mount the virtual machine&#8217;s filesystems by hand. There is an empty directory called <i>/sysroot</i> where you can mount filesystems. </p>
<p> You can get virt-rescue to suggest mount commands for you by using the <i>&#8211;suggest</i> option (in another terminal): </p>
<p>$ virt &#8211; rescue&#8211; suggest &#8211; d Fedora15 Inspecting the virtual machine or disk image&#8230;</p>
<p>    This disk contains one or<br />
    more operating systems.You can use these<br />
            mount commands in virt &#8211;<br />
        rescue(at the &gt; &lt;rescue&gt; prompt) to mount the<br />
            filesystems.</p>
<p>#/ dev / vg_f15x32 / lv_root is the root of a linux operating system<br />
#type : linux, distro : fedora, version : 15.0<br />
#Fedora release 15(Lovelock)</p>
<p>            mount<br />
            / dev / vg_f15x32 / lv_root / sysroot /<br />
            mount / dev / vda1 / sysroot / boot mount&#8211; bind / dev / sysroot / dev mount&#8211; bind / dev / pts / sysroot / dev / pts mount&#8211; bind / proc / sysroot / proc mount&#8211; bind / sys / sysroot / sys</p>
<p> Another way is to list the logical volumes (with <i><a href="/docs/linux/man/8-lvs/">lvs</a></i>(8)) and partitions (with <i><a href="/docs/linux/man/8-parted/">parted</a></i>(8)) and mount them by hand: </p>
<pre>
 &gt;&lt;rescue&gt; lvs
 LV      VG        Attr   LSize   Origin Snap%  Move Log Copy%  Convert
 lv_root vg_f15x32 -wi-a-   8.83G
 lv_swap vg_f15x32 -wi-a- 992.00M
 &gt;&lt;rescue&gt; mount /dev/vg_f15x32/lv_root /sysroot
 &gt;&lt;rescue&gt; mount /dev/vda1 /sysroot/boot
 &gt;&lt;rescue&gt; ls /sysroot
</pre>
<p> Another command to list available filesystems is <i><a href="/docs/linux/man/1-virt-filesystems/">virt-filesystems</a></i>(1). </p>
<p> To run commands in a Linux guest (for example, grub), you should chroot into the /sysroot directory first: </p>
<pre>
 &gt;&lt;rescue&gt; chroot /sysroot
</pre>
<h3><font SIZE="-1">NOTES</font></h3>
<p> Virt-rescue can be used on <i>any</i> disk image file or device, not just a virtual machine. For example you can use it on a blank file if you want to partition that file (although we would recommend using <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1) instead as it is more suitable for this purpose). You can even use virt-rescue on things like <font SIZE="-1">SD</font> cards. </p>
<p> You can get virt-rescue to give you scratch disk(s) to play with. This is useful for testing out Linux utilities (see <i>&#8211;scratch</i>). </p>
<p> Virt-rescue does not require root. You only need to run it as root if you need root to open the disk image. </p>
<p> This tool is just designed for quick interactive hacking on a virtual machine. For more structured access to a virtual machine disk image, you should use <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3). To get a structured shell that you can use to make scripted changes to guests, use <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Display brief help.</p>
<dt><code>-a</code> file</p>
<dd>
<dt><code>&#8211;add</code> file</p>
<dd> Add <i>file</i> which should be a disk image from a virtual machine. If the virtual machine has multiple block devices, you must supply all of them with separate <i>-a</i> options. </p>
<p> The format of the disk image is auto-detected. To override this and force a particular format use the <i>&#8211;format=..</i> option.</p>
<dt><code>-a </code><font SIZE="-1"><code>URI</code></font></p>
<dd>
<dt><code>&#8211;add </code><font SIZE="-1"><code>URI</code></font></p>
<dd> Add a remote disk. See &#8220;<font SIZE="-1">ADDING REMOTE STORAGE&#8221;</font> in <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1).</p>
<dt><code>&#8211;append kernelopts</code></p>
<dd> Pass additional options to the rescue kernel.</p>
<dt><code>-c</code> <font SIZE="-1">URI</font></p>
<dd>
<dt><code>&#8211;connect</code> <font SIZE="-1">URI</font></p>
<dd> If using libvirt, connect to the given <i></i><font SIZE="-1"><i>URI</i></font><i></i>. If omitted, then we connect to the default libvirt hypervisor. </p>
<p> If you specify guest block devices directly (<i>-a</i>), then libvirt is not used at all.</p>
<dt><code>-d</code> guest</p>
<dd>
<dt><code>&#8211;domain</code> guest</p>
<dd> Add all the disks from the named libvirt guest. Domain UUIDs can be used instead of names.</p>
<dt><code>&#8211;format=raw|qcow2|..</code></p>
<dd>
<dt><code>&#8211;format</code></p>
<dd> The default for the <i>-a</i> option is to auto-detect the format of the disk image. Using this forces the disk format for <i>-a</i> options which follow on the command line. Using <i>&#8211;format</i> with no argument switches back to auto-detection for subsequent <i>-a</i> options. </p>
<p> For example: </p>
<pre>
 virt-rescue --format=raw -a disk.img
</pre>
<p> forces raw format (no auto-detection) for <i>disk.img</i>. </p>
<pre>
 virt-rescue --format=raw -a disk.img --format -a another.img
</pre>
<p> forces raw format (no auto-detection) for <i>disk.img</i> and reverts to auto-detection for <i>another.img</i>. </p>
<p> If you have untrusted raw-format guest disk images, you should use this option to specify the disk format. This avoids a possible security problem with malicious guests (<font SIZE="-1">CVE-2010-3851</font>).</p>
<dt><code>-m </code><font SIZE="-1"><code>MB</code></font></p>
<dd>
<dt><code>&#8211;memsize </code><font SIZE="-1"><code>MB</code></font></p>
<dd> Change the amount of memory allocated to the rescue system. The default is set by libguestfs and is small but adequate for running system tools. The occasional program might need more memory. The parameter is specified in megabytes.</p>
<dt><code>&#8211;network</code></p>
<dd> Enable <font SIZE="-1">QEMU</font> user networking in the guest. See &#8220;<font SIZE="-1">NETWORK&#8221;</font>.</p>
<dt><code>-r</code></p>
<dd>
<dt><code>&#8211;ro</code></p>
<dd> Open the image read-only. </p>
<p> The option must always be used if the disk image or virtual machine might be running, and is generally recommended in cases where you don&#8217;t need write access to the disk. </p>
<p> See also &#8220;<font SIZE="-1">OPENING DISKS FOR READ AND WRITE&#8221;</font> in <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1).</p>
<dt><code>&#8211;scratch</code></p>
<dd>
<dt><code>&#8211;scratch=N</code></p>
<dd> The <i>&#8211;scratch</i> option adds a large scratch disk to the rescue appliance. <i>&#8211;scratch=N</i> adds <tt>&quot;N&quot;</tt> scratch disks. The scratch disk(s) are deleted automatically when virt-rescue exits. </p>
<p> You can also mix <i>-a</i>, <i>-d</i> and <i>&#8211;scratch</i> options. The scratch disk(s) are added to the appliance in the order they appear on the command line.</p>
<dt><code>&#8211;selinux</code></p>
<dd> This option is provided for backwards compatibility and does nothing.</p>
<dt><code>&#8211;smp</code> N</p>
<dd> Enable N ≥ 2 virtual CPUs in the rescue appliance.</p>
<dt><code>&#8211;suggest</code></p>
<dd> Inspect the disk image and suggest what mount commands should be used to mount the disks. You should use the <i>&#8211;suggest</i> option in a second terminal, then paste the commands into another virt-rescue. </p>
<p> This option implies <i>&#8211;ro</i> and is safe to use even if the guest is up or if another virt-rescue is running.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd> Enable verbose messages for debugging.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Display version number and exit.</p>
<dt><code>-w</code></p>
<dd>
<dt><code>&#8211;rw</code></p>
<dd> This changes the <i>-a</i> and <i>-d</i> options so that disks are added and mounts are done read-write. </p>
<p> See &#8220;<font SIZE="-1">OPENING DISKS FOR READ AND WRITE&#8221;</font> in <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1).</p>
<dt><code>-x</code></p>
<dd> Enable tracing of libguestfs <font SIZE="-1">API</font> calls.</dl>
<h2>OLD-STYLE COMMAND LINE ARGUMENTS</h2>
<p> Previous versions of virt-rescue allowed you to write either: </p>
<pre>
 virt-rescue disk.img [disk.img ...]
</pre>
<p> or </p>
<pre>
 virt-rescue guestname
</pre>
<p> whereas in this version you should use <i>-a</i> or <i>-d</i> respectively to avoid the confusing case where a disk image might have the same name as a guest. </p>
<p> For compatibility the old style is still supported.</p>
<h2>NETWORK</h2>
<p> Adding the <i>&#8211;network</i> option enables <font SIZE="-1">QEMU</font> user networking in the rescue appliance. There are some differences between user networking and ordinary networking:</p>
<dl>
<dt>ping does not work</p>
<dd> Because the <font SIZE="-1">ICMP ECHO_REQUEST</font> protocol generally requires root in order to send the ping packets, and because virt-rescue must be able to run as non-root, <font SIZE="-1">QEMU</font> user networking is not able to emulate the <i><a href="/docs/linux/man/8-ping/">ping</a></i>(8) command. The ping command will appear to resolve addresses but will not be able to send or receive any packets. This does not mean that the network is not working.</p>
<dt>cannot receive connections</p>
<dd> <font SIZE="-1">QEMU</font> user networking cannot receive incoming connections.</p>
<dt>making <font SIZE="-1">TCP</font> connections</p>
<dd> The virt-rescue appliance needs to be small and so does not include many network tools. In particular there is no <i><a href="/docs/linux/man/1-telnet/">telnet</a></i>(1) command. You can make <font SIZE="-1">TCP</font> connections from the shell using the magical <i>/dev/tcp/&lt;hostname&gt;/&lt;port&gt;</i> syntax: </p>
<pre>
 exec 3&lt;&gt;/dev/tcp/redhat.com/80
 echo &quot;GET /&quot; &gt;&amp;3
 cat &lt;&amp;3
</pre>
<p> See <i><a href="/docs/linux/man/1-bash/">bash</a></i>(1) for more details.</dl>
<h2>CAPTURING CORE DUMPS</h2>
<p> If you are testing a tool inside virt-rescue and the tool (<code>not</code> virt-rescue) segfaults, it can be tricky to capture the core dump outside virt-rescue for later analysis. This section describes one way to do this.</p>
<dl>
<dt>1.</p>
<dd> Create a scratch disk for core dumps: </p>
<p>truncate &#8211; s 4G / tmp / corefiles virt &#8211; format&#8211; partition = mbr&#8211; filesystem = ext2 &#8211; a / tmp / corefiles virt &#8211; filesystems &#8211; a / tmp / corefiles&#8211; all&#8211; long &#8211; h</p>
<dt>2.</p>
<dd> When starting virt-rescue, attach the core files disk last: </p>
<pre>
 virt-rescue --rw [-a ...] -a /tmp/corefiles
</pre>
<p> <font SIZE="-1"><code>NB.</code></font> If you use the <i>&#8211;ro</i> option, then virt-rescue will silently not write any core files to <i>/tmp/corefiles</i>.</p>
<dt>3.</p>
<dd> Inside virt-rescue, mount the core files disk. Note replace <i>/dev/sdb1</i> with the last disk index. For example if the core files disk is the last of four disks, you would use <i>/dev/sdd1</i>. </p>
<pre>
 &gt;&lt;rescue&gt; mkdir /tmp/mnt
 &gt;&lt;rescue&gt; mount /dev/sdb1 /tmp/mnt
</pre>
<dt>4.</p>
<dd> Enable core dumps in the rescue kernel: </p>
<pre>
 &gt;&lt;rescue&gt; echo '/tmp/mnt/core.%p' &gt; /proc/sys/kernel/core_pattern
 &gt;&lt;rescue&gt; ulimit -Hc unlimited
 &gt;&lt;rescue&gt; ulimit -Sc unlimited
</pre>
<dt>5.</p>
<dd> Run the tool that caused the core dump. The core dump will be written to <i>/tmp/mnt/core.</i><font SIZE="-1"><i>PID</i></font><i></i>. </p>
<pre><code>
&gt; &lt;rescue&gt; ls - l / tmp / mnt total 1628 - rw-- -- -- -1 root root 1941504 Dec 7 13 : 13 core .130 drwx-- -- --2 root root 16384 Dec 7 13 : 00 lost + found
</code></pre>
<dt>6.</p>
<dd> Before exiting virt-rescue, unmount (or at least sync) the disks: </p>
<pre>
 &gt;&lt;rescue&gt; umount /tmp/mnt
 &gt;&lt;rescue&gt; exit
</pre>
<dt>7.</p>
<dd> Outside virt-rescue, the core dump(s) can be removed from the disk using <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1). For example: </p>
<pre>
 guestfish --ro -a /tmp/corefiles -m /dev/sda1
 &gt;&lt;fs&gt; ll /
 &gt;&lt;fs&gt; download /core.NNN /tmp/core.NNN
</pre>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> Several environment variables affect virt-rescue. See &#8220;<font SIZE="-1">ENVIRONMENT VARIABLES&#8221;</font> in <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3) for the complete list.</p>
<h2>FILES</h2>
<dl>
<dt>$XDG_CONFIG_HOME/libguestfs/libguestfs-tools.conf</p>
<dd>
<dt>$HOME/.libguestfs-tools.rc</p>
<dd>
<dt>$XDG_CONFIG_DIRS/libguestfs/libguestfs-tools.conf</p>
<dd>
<dt>/etc/libguestfs-tools.conf</p>
<dd> This configuration file controls the default read-only or read-write mode (<i>&#8211;ro</i> or <i>&#8211;rw</i>). </p>
<p> See <i><a href="/docs/linux/man/5-libguestfs-tools-conf/">libguestfs-tools.conf</a></i>(5).</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3), <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1), <i><a href="/docs/linux/man/1-virt-cat/">virt-cat</a></i>(1), <i><a href="/docs/linux/man/1-virt-edit/">virt-edit</a></i>(1), <i><a href="/docs/linux/man/1-virt-filesystems/">virt-filesystems</a></i>(1), <i><a href="/docs/linux/man/5-libguestfs-tools-conf/">libguestfs-tools.conf</a></i>(5), <a rel="nofollow" href="http://libguestfs.org/.">http://libguestfs.org/.</a></p>
<h2>AUTHOR</h2>
<p> Richard W.M. Jones <a rel="nofollow" href="http://people.redhat.com/~rjones/">http://people.redhat.com/~rjones/</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2009-2016 Red Hat Inc.</p>
<h2>LICENSE</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, <font SIZE="-1">MA 02110-1301 USA.</font></p>
<h2>BUGS</h2>
<p> To get a list of bugs against libguestfs, use this link: <a rel="nofollow" href="https://bugzilla.redhat.com/buglist.cgi?component=libguestfs">https://bugzilla.redhat.com/buglist.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools </p>
<p> To report a new bug against libguestfs, use this link: <a rel="nofollow" href="https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs">https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools </p>
<p> When reporting a bug, please supply:</p>
<dl>
<dt>&bull;</p>
<dd> The version of libguestfs.</p>
<dt>&bull;</p>
<dd> Where you got libguestfs (eg. which Linux distro, compiled from source, etc)</p>
<dt>&bull;</p>
<dd> Describe the bug accurately and give a way to reproduce it.</p>
<dt>&bull;</p>
<dd> Run <i><a href="/docs/linux/man/1-libguestfs-test-tool/">libguestfs-test-tool</a></i>(1) and paste the <code>complete, unedited</code> output into the bug report. </p>
</dl>
<h2>Index</h2>
<dt><a href="#lbAG">OPTIONS</a></p>
<dd>
<dt><a href="#lbAH">OLD-STYLE COMMAND LINE ARGUMENTS</a></p>
<dd>
<dt><a href="#lbAI">NETWORK</a></p>
<dd>
<dt><a href="#lbAJ">CAPTURING CORE DUMPS</a></p>
<dd>
<dt><a href="#lbAK">ENVIRONMENT VARIABLES</a></p>
<dd>
<dt><a href="#lbAL">FILES</a></p>
<dd>
<dt><a href="#lbAM">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAN">AUTHOR</a></p>
<dd>
<dt><a href="#lbAO">COPYRIGHT</a></p>
<dd>
<dt><a href="#lbAP">LICENSE</a></p>
<dd>
<dt><a href="#lbAQ">BUGS</a></p>
<dd></dl>
