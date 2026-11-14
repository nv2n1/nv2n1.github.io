---
title: "virt-alignment-scan(1)"
name: "virt-alignment-scan"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-alignment-scan/"
description: "virt-alignment-scan – Check alignment of virtual machine partitions"
---

<h2 class="name">NAME</h2>
<p> virt-alignment-scan &#8211; Check alignment of virtual machine partitions </p>
<h2>SYNOPSIS</h2>
<pre><code>
virt - alignment - scan[--options] - d domname virt - alignment - scan[--options] - a disk.img[-a disk.img...] virt - alignment - scan[--options]
</code></pre>
<h2>DESCRIPTION</h2>
<p> When older operating systems install themselves, the partitioning tools place partitions at a sector misaligned with the underlying storage (commonly the first partition starts on sector <tt>63</tt>). Misaligned partitions can result in an operating system issuing more I/O than should be necessary. </p>
<p> The virt-alignment-scan tool checks the alignment of partitions in virtual machines and disk images and warns you if there are alignment problems. </p>
<p> Currently there is no virt tool for fixing alignment problems. You can only reinstall the guest operating system. The following NetApp document summarises the problem and possible solutions: <a rel="nofollow" href="http://media.netapp.com/documents/tr-3747.pdf">http://media.netapp.com/documents/tr-3747.pdf</a></p>
<h2>OUTPUT</h2>
<p> To run this tool on a disk image directly, use the <i>-a</i> option: </p>
<pre>
 $ virt-alignment-scan -a winxp.img
 /dev/sda1        32256          512    bad (alignment &lt; 4K)
 $ virt-alignment-scan -a fedora16.img
 /dev/sda1      1048576         1024K   ok
 /dev/sda2      2097152         2048K   ok
 /dev/sda3    526385152         2048K   ok
</pre>
<p> To run the tool on a guest known to libvirt, use the <i>-d</i> option and possibly the <i>-c</i> option: </p>
<pre>
 # virt-alignment-scan -d RHEL5
 /dev/sda1        32256          512    bad (alignment &lt; 4K)
 /dev/sda2    106928640          512    bad (alignment &lt; 4K)
 $ virt-alignment-scan -c <a href="qemu:///system">qemu:///system</a> -d Win7TwoDisks
 /dev/sda1      1048576         1024K   ok
 /dev/sda2    105906176         1024K   ok
 /dev/sdb1        65536           64K   ok
</pre>
<p> Run virt-alignment-scan without any <i>-a</i> or <i>-d</i> options to scan all libvirt domains. </p>
<pre>
 # virt-alignment-scan
 F16x64:/dev/sda1      1048576         1024K   ok
 F16x64:/dev/sda2      2097152         2048K   ok
 F16x64:/dev/sda3    526385152         2048K   ok
</pre>
<p> The output consists of 4 or more whitespace-separated columns. Only the first 4 columns are significant if you want to parse this from a program. The columns are:</p>
<dl>
<dt>col 1</p>
<dd> The device and partition name (eg. <i>/dev/sda1</i> meaning the first partition on the first block device). </p>
<p> When listing all libvirt domains (no <i>-a</i> or <i>-d</i> option given) this column is prefixed by the libvirt name or <font SIZE="-1">UUID </font>(if <i>&#8211;uuid</i> is given). eg: <tt>&quot;WinXP:/dev/sda1&quot;</tt></p>
<dt>col 2</p>
<dd> the start of the partition in bytes</p>
<dt>col 3</p>
<dd> the alignment in bytes or Kbytes (eg. <tt>512</tt> or <tt>&quot;4K&quot;</tt>)</p>
<dt>col 4</p>
<dd> <tt>&quot;ok&quot;</tt> if the alignment is best for performance, or <tt>&quot;bad&quot;</tt> if the alignment can cause performance problems</p>
<dt>cols 5+</p>
<dd> optional free-text explanation.</dl>
<p> The exit code from the program changes depending on whether poorly aligned partitions were found. See &#8220;<font SIZE="-1">EXIT STATUS&#8221;</font> below. </p>
<p> If you just want the exit code with no output, use the <i>-q</i> option.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Display brief help.</p>
<dt><code>-a</code> file</p>
<dd>
<dt><code>&#8211;add</code> file</p>
<dd> Add <i>file</i> which should be a disk image from a virtual machine. </p>
<p> The format of the disk image is auto-detected. To override this and force a particular format use the <i>&#8211;format=..</i> option.</p>
<dt><code>-a </code><font SIZE="-1"><code>URI</code></font></p>
<dd>
<dt><code>&#8211;add </code><font SIZE="-1"><code>URI</code></font></p>
<dd> Add a remote disk. See &#8220;<font SIZE="-1">ADDING REMOTE STORAGE&#8221;</font> in <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1).</p>
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
 virt-alignment-scan --format=raw -a disk.img
</pre>
<p> forces raw format (no auto-detection) for <i>disk.img</i>. </p>
<pre>
 virt-alignment-scan --format=raw -a disk.img --format -a another.img
</pre>
<p> forces raw format (no auto-detection) for <i>disk.img</i> and reverts to auto-detection for <i>another.img</i>. </p>
<p> If you have untrusted raw-format guest disk images, you should use this option to specify the disk format. This avoids a possible security problem with malicious guests (<font SIZE="-1">CVE-2010-3851</font>).</p>
<dt><code>-P</code> nr_threads</p>
<dd> Since libguestfs 1.22, virt-alignment-scan is multithreaded and examines guests in parallel. By default the number of threads to use is chosen based on the amount of free memory available at the time that virt-alignment-scan is started. You can force virt-alignment-scan to use at most <tt>&quot;nr_threads&quot;</tt> by using the <i>-P</i> option. </p>
<p> Note that <i>-P 0</i> means to autodetect, and <i>-P 1</i> means to use a single thread.</p>
<dt><code>-q</code></p>
<dd>
<dt><code>&#8211;quiet</code></p>
<dd> Don&#8217;t produce any output. Just set the exit code (see &#8220;<font SIZE="-1">EXIT STATUS&#8221;</font> below).</p>
<dt><code>&#8211;uuid</code></p>
<dd> Print UUIDs instead of names. This is useful for following a guest even when the guest is migrated or renamed, or when two guests happen to have the same name. </p>
<p> This option only applies when listing all libvirt domains (when no <i>-a</i> or <i>-d</i> options are specified).</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd> Enable verbose messages for debugging.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Display version number and exit.</p>
<dt><code>-x</code></p>
<dd> Enable tracing of libguestfs <font SIZE="-1">API</font> calls.</dl>
<h2>RECOMMENDED ALIGNMENT</h2>
<p> Operating systems older than Windows 2008 and Linux before ca.2010 place the first sector of the first partition at sector 63, with a 512 byte sector size. This happens because of a historical accident. Drives have to report a cylinder / head / sector (<font SIZE="-1">CHS</font>) geometry to the <font SIZE="-1">BIOS. </font> The geometry is completely meaningless on modern drives, but it happens that the geometry reported always has 63 sectors per track. The operating system therefore places the first partition at the start of the second &#8220;track&#8221;, at sector 63. </p>
<p> When the guest <font SIZE="-1">OS</font> is virtualized, the host operating system and hypervisor may prefer accesses aligned to one of:</p>
<dl>
<dt>&bull;</p>
<dd> 512 bytes </p>
<p> if the host <font SIZE="-1">OS</font> uses local storage directly on hard drive partitions, and the hard drive has 512 byte physical sectors.</p>
<dt>&bull;</p>
<dd> 4 Kbytes </p>
<p> for local storage on new hard drives with 4Kbyte physical sectors; for file-backed storage on filesystems with 4Kbyte block size; or for some types of network-attached storage.</p>
<dt>&bull;</p>
<dd> 64 Kbytes </p>
<p> for high-end network-attached storage. This is the optimal block size for some NetApp hardware.</p>
<dt>&bull;</p>
<dd> 1 Mbyte </p>
<p> see &#8220;1 <font SIZE="-1">MB PARTITION ALIGNMENT&#8221;</font> below.</dl>
<p> Partitions which are not aligned correctly to the underlying storage cause extra I/O. For example: </p>
<pre>
                       sect#63
                       ┌──────────────────────────┬ ─ ─ ─ ─
                       │         guest            │
                       │    filesystem block      │
  ─ ┬──────────────────┴──────┬───────────────────┴─────┬ ─ ─
    │  host block             │  host block             │
    │                         │                         │
  ─ ┴─────────────────────────┴─────────────────────────┴ ─ ─
</pre>
<p> In this example, each time a 4K guest block is read, two blocks on the host must be accessed (so twice as much I/O is done). When a 4K guest block is written, two host blocks must first be read, the old and new data combined, and the two blocks written back (4x I/O).</p>
<h3><font SIZE="-1">LINUX HOST BLOCK AND I/O SIZE</font></h3>
<p> New versions of the Linux kernel expose the physical and logical block size, and minimum and recommended I/O size. </p>
<p> For a typical consumer hard drive with 512 byte sectors: </p>
<pre>
 $ cat /sys/block/sda/queue/hw_sector_size
 512
 $ cat /sys/block/sda/queue/physical_block_size
 512
 $ cat /sys/block/sda/queue/logical_block_size
 512
 $ cat /sys/block/sda/queue/minimum_io_size
 512
 $ cat /sys/block/sda/queue/optimal_io_size
 0
</pre>
<p> For a new consumer hard drive with 4Kbyte sectors: </p>
<pre>
 $ cat /sys/block/sda/queue/hw_sector_size
 4096
 $ cat /sys/block/sda/queue/physical_block_size
 4096
 $ cat /sys/block/sda/queue/logical_block_size
 4096
 $ cat /sys/block/sda/queue/minimum_io_size
 4096
 $ cat /sys/block/sda/queue/optimal_io_size
 0
</pre>
<p> For a NetApp <font SIZE="-1">LUN:</font> </p>
<pre>
 $ cat /sys/block/sdc/queue/logical_block_size
 512
 $ cat /sys/block/sdc/queue/physical_block_size
 512
 $ cat /sys/block/sdc/queue/minimum_io_size
 4096
 $ cat /sys/block/sdc/queue/optimal_io_size
 65536
</pre>
<p> The NetApp allows 512 byte accesses (but they will be very inefficient), prefers a minimum 4K I/O size, but the optimal I/O size is 64K. </p>
<p> For detailed information about what these numbers mean, see <a rel="nofollow" href="http://docs.redhat.com/docs/en-US/Red_Hat_Enterprise_Linux/6/html/Storage_Administration_Guide/newstorage-iolimits.html">http://docs.redhat.com/docs/en-US/Red_Hat_Enterprise_Linux/6/html/Storage_Administration_Guide/newstorage-iolimits.html</a> </p>
<p> [Thanks to Matt Booth for providing 4K drive data. Thanks to Mike Snitzer for providing NetApp data and additional information.]</p>
<h3>1 <font SIZE="-1">MB PARTITION ALIGNMENT</font></h3>
<p> Microsoft picked 1 <font SIZE="-1">MB</font> as the default alignment for all partitions starting with Windows 2008 Server, and Linux has followed this. </p>
<p> Assuming 512 byte sectors in the guest, you will now see the first partition starting at sector 2048, and subsequent partitions (if any) will start at a multiple of 2048 sectors. </p>
<p> 1 <font SIZE="-1">MB</font> alignment is compatible with all current alignment requirements (4K, 64K) and provides room for future growth in physical block sizes.</p>
<h3><font SIZE="-1">SETTING ALIGNMENT</font></h3>
<p> <i><a href="/docs/linux/man/1-virt-resize/">virt-resize</a></i>(1) can change the alignment of the partitions of some guests. Currently it can fully align all the partitions of all Windows guests, and it will fix the bootloader where necessary. For Linux guests, it can align the second and subsequent partitions, so the majority of <font SIZE="-1">OS</font> accesses except at boot will be aligned. </p>
<p> Another way to correct partition alignment problems is to reinstall your guest operating systems. If you install operating systems from templates, ensure these have correct partition alignment too. </p>
<p> For older versions of Windows, the following NetApp document contains useful information: <a rel="nofollow" href="http://media.netapp.com/documents/tr-3747.pdf">http://media.netapp.com/documents/tr-3747.pdf</a> </p>
<p> For Red Hat Enterprise Linux ≤ 5, use a Kickstart script that contains an explicit <tt>%pre</tt> section that creates aligned partitions using <i><a href="/docs/linux/man/8-parted/">parted</a></i>(8). Do not use the Kickstart <tt>&quot;part&quot;</tt> command. The NetApp document above contains an example.</p>
<h2>EXIT STATUS</h2>
<p> This program returns:</p>
<dl>
<dt>&bull;</p>
<dd> 0 </p>
<p> successful exit, all partitions are aligned ≥ 64K for best performance</p>
<dt>&bull;</p>
<dd> 1 </p>
<p> an error scanning the disk image or guest</p>
<dt>&bull;</p>
<dd> 2 </p>
<p> successful exit, some partitions have alignment &lt; 64K which can result in poor performance on high end network storage</p>
<dt>&bull;</p>
<dd> 3 </p>
<p> successful exit, some partitions have alignment &lt; 4K which can result in poor performance on most hypervisors</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3), <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1), <i><a href="/docs/linux/man/1-virt-filesystems/">virt-filesystems</a></i>(1), <i><a href="/docs/linux/man/1-virt-rescue/">virt-rescue</a></i>(1), <i><a href="/docs/linux/man/1-virt-resize/">virt-resize</a></i>(1), <a rel="nofollow" href="http://libguestfs.org/.">http://libguestfs.org/.</a></p>
<h2>AUTHOR</h2>
<p> Richard W.M. Jones <a rel="nofollow" href="http://people.redhat.com/~rjones/">http://people.redhat.com/~rjones/</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2011 Red Hat Inc.</p>
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
<dt><a href="#lbAK">EXIT STATUS</a></p>
<dd>
<dt><a href="#lbAL">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAM">AUTHOR</a></p>
<dd>
<dt><a href="#lbAN">COPYRIGHT</a></p>
<dd>
<dt><a href="#lbAO">LICENSE</a></p>
<dd>
<dt><a href="#lbAP">BUGS</a></p>
<dd></dl>
