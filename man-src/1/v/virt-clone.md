---
title: "virt-clone(1)"
name: "virt-clone"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-clone/"
description: "virt-clone – clone existing virtual machine images"
---

<h2 class="name">NAME</h2>
<p> virt-clone &#8211; clone existing virtual machine images </p>
<h2>SYNOPSIS</h2>
<p> <code>virt-clone</code> [<font SIZE="-1">OPTION</font>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>virt-clone</code> is a command line tool for cloning existing virtual machine images using the <tt>&quot;libvirt&quot;</tt> hypervisor management library. It will copy the disk images of any existing virtual machine, and define a new guest with an identical virtual hardware configuration. Elements which require uniqueness will be updated to avoid a clash between old and new guests. </p>
<p> By default, virt-clone will show an error if the necessary information to clone the guest is not provided. The &#8211;auto-clone option will generate all needed input, aside from the source guest to clone. </p>
<p> Please note, virt-clone does not change anything _inside_ the guest <font SIZE="-1">OS,</font> it only duplicates disks and does host side changes. So things like changing passwords, changing static <font SIZE="-1">IP</font> address, etc are outside the scope of this tool. For these types of changes, please see <code>virt-sysprep</code>.</p>
<h2>GENERAL OPTIONS</h2>
<p> Most options are not required. Minimum requirements are &#8211;original or &#8211;original-xml (to specify the guest to clone), &#8211;name, and appropriate storage options via -file.</p>
<dl>
<dt><code>&#8211;connect</code> <font SIZE="-1">URI</font></p>
<dd> Connect to a non-default hypervisor. See <i><a href="/docs/linux/man/1-virt-install/">virt-install</a></i>(1) for details</p>
<dt><code>-o</code> <font SIZE="-1">ORIGINAL_GUEST</font></p>
<dd>
<dt><code>&#8211;original</code> <font SIZE="-1">ORIGINAL_GUEST</font></p>
<dd> Name of the original guest to be cloned. This guest must be shut off or paused since it is not possible to safely clone active guests at this time.</p>
<dt><code>&#8211;original-xml</code> <font SIZE="-1">ORIGINAL_XML</font></p>
<dd> Libvirt guest xml file to use as the original guest. The guest does not need to be defined on the libvirt connection. This takes the place of the <tt>&quot;--original&quot;</tt> parameter.</p>
<dt><code>&#8211;auto-clone</code></p>
<dd> Generate a new guest name, and paths for new storage. </p>
<p> An example or possible generated output: </p>
<pre>
  Original name        : MyVM
  Generated clone name : MyVM-clone
  Original disk path   : /home/user/foobar.img
  Generated disk path  : /home/user/foobar-clone.img
</pre>
<p> If generated names collide with existing VMs or storage, a number is appended, such as foobar-clone-1.img, or MyVM-clone-3.</p>
<dt><code>-n</code> <font SIZE="-1">NAME</font></p>
<dd>
<dt><code>&#8211;name</code> <font SIZE="-1">NAME</font></p>
<dd> Name of the new guest virtual machine instance. This must be unique amongst all guests known to the hypervisor connection, including those not currently active.</p>
<dt><code>-u</code> <font SIZE="-1">UUID</font></p>
<dd>
<dt><code>&#8211;uuid</code> <font SIZE="-1">UUID</font></p>
<dd> <font SIZE="-1">UUID</font> for the guest; if none is given a random <font SIZE="-1">UUID</font> will be generated. If you specify <font SIZE="-1">UUID,</font> you should use a 32-digit hexadecimal number. <font SIZE="-1">UUID</font> are intended to be unique across the entire data center, and indeed world. Bear this in mind if manually specifying a <font SIZE="-1">UUID</font></p>
<dt><code>-f</code> <font SIZE="-1">DISKFILE</font></p>
<dd>
<dt><code>&#8211;file</code> <font SIZE="-1">DISKFILE</font></p>
<dd> Path to the file, disk partition, or logical volume to use as the backing store for the new guest&#8217;s virtual disk. If the original guest has multiple disks, this parameter must be repeated multiple times, once per disk in the original virtual machine.</p>
<dt><code>&#8211;force-copy</code> <font SIZE="-1">TARGET</font></p>
<dd> Force cloning the passed disk target (&#8216;hdc&#8217;, &#8216;sda&#8217;, etc.). By default, <tt>&quot;virt-clone&quot;</tt> will skip certain disks, such as those marked &#8216;readonly&#8217; or &#8216;shareable&#8217;.</p>
<dt><code>&#8211;nonsparse</code></p>
<dd> Fully allocate the new storage if the path being cloned is a sparse file. See <i><a href="/docs/linux/man/1-virt-install/">virt-install</a></i>(1) for more details on sparse vs. nonsparse.</p>
<dt><code>&#8211;preserve-data</code></p>
<dd> No storage is cloned: disk images specific by &#8211;file are preserved as is, and referenced in the new clone <font SIZE="-1">XML.</font> This is useful if you want to clone a <font SIZE="-1">VM XML</font> template, but not the storage contents.</p>
<dt><code>&#8211;reflink</code></p>
<dd> When &#8211;reflink is specified, perform a lightweight copy. This is much faster if source images and destination images are all on the same btrfs filesystem. If <font SIZE="-1">COW</font> copy is not possible, then virt-clone fails.</p>
<dt><code>-m</code> <font SIZE="-1">MAC</font></p>
<dd>
<dt><code>&#8211;mac</code> <font SIZE="-1">MAC</font></p>
<dd> Fixed <font SIZE="-1">MAC</font> address for the guest; If this parameter is omitted, or the value <tt>&quot;RANDOM&quot;</tt> is specified a suitable address will be randomly generated. Addresses are applied sequentially to the networks as they are listed in the original guest <font SIZE="-1">XML.</font></p>
<dt><code>&#8211;print-xml</code></p>
<dd> Print the generated clone <font SIZE="-1">XML</font> and exit without cloning.</p>
<dt><code>&#8211;replace</code></p>
<dd> Shutdown and remove any existing guest with the passed <tt>&quot;--name&quot;</tt> before cloning the original guest.</p>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8211;help</code></p>
<dd> Show the help message and exit</p>
<dt><code>&#8211;version</code></p>
<dd> Show program&#8217;s version number and exit</p>
<dt><code>&#8211;check</code></p>
<dd> Enable or disable some validation checks. See <i><a href="/docs/linux/man/1-virt-install/">virt-install</a></i>(1) for more details.</p>
<dt><code>-q</code></p>
<dd>
<dt><code>&#8211;quiet</code></p>
<dd> Suppress non-error output.</p>
<dt><code>-d</code></p>
<dd>
<dt><code>&#8211;debug</code></p>
<dd> Print debugging information to the terminal when running the install process. The debugging information is also stored in <tt>&quot;~/.cache/virt-manager/virt-clone.log&quot;</tt> even if this parameter is omitted.</dl>
<h2>EXAMPLES</h2>
<p> Clone the guest called <tt>&quot;demo&quot;</tt> on the default connection, auto generating a new name and disk clone path. </p>
<pre>
  # virt-clone \
       --original demo \
       --auto-clone
</pre>
<p> Clone the guest called <tt>&quot;demo&quot;</tt> which has a single disk to copy </p>
<pre>
  # virt-clone \
       --original demo \
       --name newdemo \
       --file /var/lib/xen/images/newdemo.img
</pre>
<p> Clone a <font SIZE="-1">QEMU</font> guest with multiple disks </p>
<pre><code>
#virt - clone-- connect qemu: ///system \
       --original demo \
       --name newdemo \
       --file /var/lib/xen/images/newdemo.img \
       --file /var/lib/xen/images/newdata.img
</code></pre>
<p> Clone a guest to a physical device which is at least as big as the original guests disks. If the destination device is bigger, the new guest can do a filesystem resize when it boots. </p>
<pre><code>
#virt - clone-- connect qemu: ///system \
       --original demo \
       --name newdemo \
       --file /dev/HostVG/DemoVM \
       --mac 52:54:00:34:11:54
</code></pre>
<h2>BUGS</h2>
<p> Please see <a rel="nofollow" href="http://virt-manager.org/page/BugReporting">http://virt-manager.org/page/BugReporting</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) Fujitsu Limited, Copyright (C) Red Hat, Inc, and various contributors. This is free software. You may redistribute copies of it under the terms of the <font SIZE="-1">GNU</font> General Public License <tt>&quot;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a>&quot;</tt>. There is <font SIZE="-1">NO WARRANTY,</font> to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <tt>&quot;<a href="/docs/linux/man/1-virt-sysprep/">virt-sysprep</a>(1)&quot;</tt>, <tt><a href="/docs/linux/man/1-virsh/">virsh</a>(1)</tt>, <tt>&quot;<a href="/docs/linux/man/1-virt-install/">virt-install</a>(1)&quot;</tt>, <tt>&quot;<a href="/docs/linux/man/1-virt-manager/">virt-manager</a>(1)&quot;</tt>, the project website <tt>&quot;<a rel="nofollow" href="http://virt-manager.org">http://virt-manager.org</a>&quot;</tt> </p>
<h2>Index</h2>
