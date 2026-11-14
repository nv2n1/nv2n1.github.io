---
title: "virt-v2v(1)"
name: "virt-v2v"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-v2v/"
description: "virt-v2v – Convert a guest to use KVM"
---

<h2 class="name">NAME</h2>
<p> virt-v2v &#8211; Convert a guest to use KVM </p>
<h2>SYNOPSIS</h2>
<pre>
 virt-v2v -ic <a href="vpx://vcenter.example.com/Datacenter/esxi">vpx://vcenter.example.com/Datacenter/esxi</a> vmware_guest
 virt-v2v -ic <a href="vpx://vcenter.example.com/Datacenter/esxi">vpx://vcenter.example.com/Datacenter/esxi</a> vmware_guest \
   -o rhev -os rhev.nfs:/export_domain --network rhevm
 virt-v2v -i libvirtxml guest-domain.xml -o local -os /var/tmp
 virt-v2v -i disk disk.img -o local -os /var/tmp
 virt-v2v -i disk disk.img -o glance
</pre>
<h2>DESCRIPTION</h2>
<p> Virt-v2v converts guests from a foreign hypervisor to run on <font SIZE="-1">KVM. </font> It can read Linux and Windows guests running on VMware, Xen, Hyper-V and some other hypervisors, and convert them to <font SIZE="-1">KVM</font> managed by libvirt, OpenStack, oVirt, Red Hat Enterprise Virtualisation (<font SIZE="-1">RHEV</font>) or several other targets. </p>
<p> There is also a companion front-end called <i><a href="/docs/linux/man/1-virt-p2v/">virt-p2v</a></i>(1) which comes as an <font SIZE="-1">ISO, CD</font> or <font SIZE="-1">PXE</font> image that can be booted on physical machines to virtualize those machines (physical to virtual, or p2v). </p>
<p> This manual page documents the rewritten virt-v2v included in libguestfs ≥ 1.28.</p>
<h2>INPUT AND OUTPUT MODES</h2>
<pre>
                          ┌────────────┐  ┌─────────&#x25b6; -o null
 -i disk ────────────┐    │            │ ─┘┌───────&#x25b6; -o local
 -i ova  ──────────┐ └──&#x25b6; │ virt-v2v   │ ──┘┌───────&#x25b6; -o qemu
                   └────&#x25b6; │ conversion │ ───┘┌────────────┐
 VMware─&#x25b6;┌────────────┐   │ server     │ ────&#x25b6; -o libvirt │─&#x25b6; KVM
 Xen ───&#x25b6;│ -i libvirt ──&#x25b6; │            │     │  (default) │
 ... ───&#x25b6;│  (default) │   │            │ ──┐ └────────────┘
         └────────────┘   │            │ ─┐└──────&#x25b6; -o glance
 -i libvirtxml ─────────&#x25b6; │            │ ┐└─────────&#x25b6; -o rhev
                          └────────────┘ └──────────&#x25b6; -o vdsm
</pre>
<p> Virt-v2v has a number of possible input and output modes, selected using the <i>-i</i> and <i>-o</i> options. Only one input and output mode can be selected for each run of virt-v2v. </p>
<p> <i>-i disk</i> is used for reading from local disk images (mainly for testing). </p>
<p> <i>-i libvirt</i> is used for reading from any libvirt source. Since libvirt can connect to many different hypervisors, it is used for reading guests from VMware, <font SIZE="-1">RHEL 5</font> Xen and more. The <i>-ic</i> option selects the precise libvirt source. </p>
<p> <i>-i libvirtxml</i> is used to read from libvirt <font SIZE="-1">XML</font> files. This is the method used by <i><a href="/docs/linux/man/1-virt-p2v/">virt-p2v</a></i>(1) behind the scenes. </p>
<p> <i>-i ova</i> is used for reading from a VMware ova source file. </p>
<p> <i>-o glance</i> is used for writing to OpenStack Glance. </p>
<p> <i>-o libvirt</i> is used for writing to any libvirt target. Libvirt can connect to local or remote <font SIZE="-1">KVM</font> hypervisors. The <i>-oc</i> option selects the precise libvirt target. </p>
<p> <i>-o local</i> is used to write to a local disk image with a local libvirt configuration file (mainly for testing). </p>
<p> <i>-o qemu</i> writes to a local disk image with a shell script for booting the guest directly in qemu (mainly for testing). </p>
<p> <i>-o rhev</i> is used to write to a RHEV-M / oVirt target. <i>-o vdsm</i> is only used when virt-v2v runs under <font SIZE="-1">VDSM</font> control.</p>
<h2>EXAMPLES</h2>
<h3>Convert from VMware vCenter server to local libvirt</h3>
<p> You have a VMware vCenter server called <tt>&quot;vcenter.example.com&quot;</tt>, a datacenter called <tt>&quot;Datacenter&quot;</tt>, and an ESXi hypervisor called <tt>&quot;esxi&quot;</tt>. You want to convert a guest called <tt>&quot;vmware_guest&quot;</tt> to run locally under libvirt. </p>
<pre>
 virt-v2v -ic <a href="vpx://vcenter.example.com/Datacenter/esxi">vpx://vcenter.example.com/Datacenter/esxi</a> vmware_guest
</pre>
<p> In this case you will most likely have to run virt-v2v as <tt>&quot;root&quot;</tt>, since it needs to talk to the system libvirt daemon and copy the guest disks to <i>/var/lib/libvirt/images</i>. </p>
<p> For more information see &#8220;<font SIZE="-1">INPUT FROM VMWARE VCENTER SERVER&#8221;</font> below.</p>
<h3>Convert from VMware to RHEV-M/oVirt</h3>
<p> This is the same as the previous example, except you want to send the guest to a RHEV-M Export Storage Domain which is located remotely (over <font SIZE="-1">NFS</font>) at <tt>&quot;rhev.nfs:/export_domain&quot;</tt>. If you are unclear about the location of the Export Storage Domain you should check the settings on your RHEV-M management console. Guest network interface(s) are connected to the target network called <tt>&quot;rhevm&quot;</tt>. </p>
<pre>
 virt-v2v -ic <a href="vpx://vcenter.example.com/Datacenter/esxi">vpx://vcenter.example.com/Datacenter/esxi</a> vmware_guest \
   -o rhev -os rhev.nfs:/export_domain --network rhevm
</pre>
<p> In this case the host running virt-v2v acts as a <code>conversion server</code>. </p>
<p> Note that after conversion, the guest will appear in the RHEV-M Export Storage Domain, from where you will need to import it using the RHEV-M user interface. (See &#8220;<font SIZE="-1">OUTPUT TO RHEV&#8221;</font>).</p>
<h3>Convert disk image to OpenStack glance</h3>
<p> Given a disk image from another hypervisor that you want to convert to run on OpenStack (only KVM-based OpenStack is supported), you can do: </p>
<pre>
 virt-v2v -i disk disk.img -o glance
</pre>
<p> See &#8220;<font SIZE="-1">OUTPUT TO GLANCE&#8221;</font> below.</p>
<h3>Convert disk image to disk image</h3>
<p> Given a disk image from another hypervisor that you want to convert to run on <font SIZE="-1">KVM,</font> you have two options. The simplest way is to try: </p>
<pre>
 virt-v2v -i disk disk.img -o local -os /var/tmp
</pre>
<p> where virt-v2v guesses everything about the input <i>disk.img</i> and (in this case) writes the converted result to <i>/var/tmp</i>. </p>
<p> A more complex method is to write some libvirt <font SIZE="-1">XML</font> describing the input guest (if you can get the source hypervisor to provide you with libvirt <font SIZE="-1">XML,</font> then so much the better). You can then do: </p>
<pre>
 virt-v2v -i libvirtxml guest-domain.xml -o local -os /var/tmp
</pre>
<p> Since <i>guest-domain.xml</i> contains the path(s) to the guest disk image(s) you do not need to specify the name of the disk image on the command line.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Display help.</p>
<dt><code>-b</code> &#8230;</p>
<dd>
<dt><code>&#8211;bridge</code> &#8230;</p>
<dd> See <i>&#8211;network</i> below.</p>
<dt><code>&#8211;colors</code></p>
<dd>
<dt><code>&#8211;colours</code></p>
<dd> Use <font SIZE="-1">ANSI</font> colour sequences to colourize messages. This is the default when the output is a tty. If the output of the program is redirected to a file, <font SIZE="-1">ANSI</font> colour sequences are disabled unless you use this option.</p>
<dt><code>&#8211;compressed</code></p>
<dd> Write a compressed output file. This is only allowed if the output format is qcow2 (see <i>-of</i> below), and is equivalent to the <i>-c</i> option of <i><a href="/docs/linux/man/1-qemu-img/">qemu-img</a></i>(1).</p>
<dt><code>&#8211;debug-gc</code></p>
<dd> Debug garbage collection and memory allocation. This is only useful when debugging memory problems in virt-v2v or the OCaml libguestfs bindings.</p>
<dt><code>&#8211;debug-overlays</code></p>
<dd> Save the overlay file(s) created during conversion. This option is only used for debugging virt-v2v and may be removed in a future version.</p>
<dt><code>-i disk</code></p>
<dd> Set the input method to <i>disk</i>. </p>
<p> In this mode you can read a virtual machine disk image with no metadata. virt-v2v tries to guess the best default metadata. This is usually adequate but you can get finer control (eg. of memory and vCPUs) by using <i>-i libvirtxml</i> instead. Only guests that use a single disk can be imported this way.</p>
<dt><code>-i libvirt</code></p>
<dd> Set the input method to <i>libvirt</i>. This is the default. </p>
<p> In this mode you have to specify a libvirt guest name or <font SIZE="-1">UUID</font> on the command line. You may also specify a libvirt connection <font SIZE="-1">URI </font>(see <i>-ic</i>).</p>
<dt><code>-i libvirtxml</code></p>
<dd> Set the input method to <i>libvirtxml</i>. </p>
<p> In this mode you have to pass a libvirt <font SIZE="-1">XML</font> file on the command line. This file is read in order to get metadata about the source guest (such as its name, amount of memory), and also to locate the input disks. See &#8220;<font SIZE="-1">MINIMAL XML FOR</font> -i libvirtxml <font SIZE="-1">OPTION&#8221;</font> below.</p>
<dt><code>-i local</code></p>
<dd> This is the same as <i>-i disk</i>.</p>
<dt><code>-i ova</code></p>
<dd> Set the input method to <i>ova</i>. </p>
<p> In this mode you can read a VMware ova file. Virt-v2v will read the ova manifest file and check the vmdk volumes for validity (checksums) as well as analyzing the ovf file, and then convert the guest. See &#8220;<font SIZE="-1">INPUT FROM VMWARE OVA&#8221;</font> below</p>
<dt><code>-ic</code> libvirtURI</p>
<dd> Specify a libvirt connection <font SIZE="-1">URI</font> to use when reading the guest. This is only used when <i>-i libvirt</i>. </p>
<p> Only local libvirt connections, VMware vCenter connections, or <font SIZE="-1">RHEL 5</font> Xen remote connections can be used. Other remote libvirt connections will not work in general. </p>
<p> See also &#8220;<font SIZE="-1">INPUT FROM VMWARE VCENTER SERVER&#8221;</font>, &#8220;<font SIZE="-1">INPUT FROM RHEL 5 XEN&#8221;</font> below.</p>
<dt><code>-if</code> format</p>
<dd> For <i>-i disk</i> only, this specifies the format of the input disk image. For other input methods you should specify the input format in the metadata.</p>
<dt><code>&#8211;machine-readable</code></p>
<dd> This option is used to make the output more machine friendly when being parsed by other programs. See &#8220;<font SIZE="-1">MACHINE READABLE OUTPUT&#8221;</font> below.</p>
<dt><code>-n</code> in:out</p>
<dd>
<dt><code>-n</code> out</p>
<dd>
<dt><code>&#8211;network</code> in:out</p>
<dd>
<dt><code>&#8211;network</code> out</p>
<dd>
<dt><code>-b</code> in:out</p>
<dd>
<dt><code>-b</code> out</p>
<dd>
<dt><code>&#8211;bridge</code> in:out</p>
<dd>
<dt><code>&#8211;bridge</code> out</p>
<dd> Map network (or bridge) called <tt>&quot;in&quot;</tt> to network (or bridge) called <tt>&quot;out&quot;</tt>. If no <tt>&quot;in:&quot;</tt> prefix is given, all other networks (or bridges) are mapped to <tt>&quot;out&quot;</tt>. </p>
<p> See &#8220;<font SIZE="-1">NETWORKS AND BRIDGES&#8221;</font> below.</p>
<dt><code>&#8211;no-copy</code></p>
<dd> Don&#8217;t copy the disks. Instead, conversion is performed (and thrown away), and metadata is written, but no disks are created. See also discussion of <i>-o null</i> below. </p>
<p> This is useful in two cases: Either you want to test if conversion is likely to succeed, without the long copying process. Or you are only interested in looking at the metadata. </p>
<p> This option is not compatible with <i>-o libvirt</i> since it would create a faulty guest (one with no disks). </p>
<p> This option is not compatible with <i>-o glance</i> for technical reasons.</p>
<dt><code>&#8211;no-trim all</code></p>
<dd>
<dt><code>&#8211;no-trim</code> mp[,mp&#8230;]</p>
<dd> By default virt-v2v runs <i><a href="/docs/linux/man/8-fstrim/">fstrim</a></i>(8) to reduce the amount of data that needs to be copied. This is known to break some buggy bootloaders causing boot failures after conversion (see for example <a rel="nofollow" href="https://bugzilla.redhat.com/show_bug.cgi?id=1141145#c27">https://bugzilla.redhat.com/show_bug.cgi?id=1141145#c27</a>). </p>
<p> You can use <i>&#8211;no-trim all</i> to disable all trimming. Note this will greatly increase the amount of data that has to be copied and can make virt-v2v run much more slowly. </p>
<p> You can also disable trimming on selected filesystems only (specified by a comma-separated list of their mount point(s) in the guest). Typically you would use <i>&#8211;no-trim /boot</i> to work around the grub bug mentioned above. </p>
<p> You can also disable trimming on partitions using the libguestfs naming scheme for devices, eg: <i>&#8211;no-trim /dev/sdb2</i> means do not trim the second partition on the second block device. Use <i><a href="/docs/linux/man/1-virt-filesystems/">virt-filesystems</a></i>(1) to list filesystem names in a guest.</p>
<dt><code>-o disk</code></p>
<dd> This is the same as <i>-o local</i>.</p>
<dt><code>-o glance</code></p>
<dd> Set the output method to OpenStack Glance. In this mode the converted guest is uploaded to Glance. See &#8220;<font SIZE="-1">OUTPUT TO GLANCE&#8221;</font> below.</p>
<dt><code>-o libvirt</code></p>
<dd> Set the output method to <i>libvirt</i>. This is the default. </p>
<p> In this mode, the converted guest is created as a libvirt guest. You may also specify a libvirt connection <font SIZE="-1">URI </font>(see <i>-oc</i>). </p>
<p> See &#8220;<font SIZE="-1">OUTPUT TO LIBVIRT&#8221;</font> below.</p>
<dt><code>-o local</code></p>
<dd> Set the output method to <i>local</i>. </p>
<p> In this mode, the converted guest is written to a local directory specified by <i>-os /dir</i> (the directory must exist). The converted guest&#8217;s disks are written as: </p>
<pre>
 /dir/name-sda
 /dir/name-sdb
 [etc]
</pre>
<p> and a libvirt <font SIZE="-1">XML</font> file is created containing guest metadata: </p>
<pre>
 /dir/name.xml
</pre>
<p> where <tt>&quot;name&quot;</tt> is the guest name.</p>
<dt><code>-o null</code></p>
<dd> Set the output method to <i>null</i>. </p>
<p> The guest is converted and copied (unless you also specify <i>&#8211;no-copy</i>), but the results are thrown away and no metadata is written.</p>
<dt><code>-o ovirt</code></p>
<dd> This is the same as <i>-o rhev</i>.</p>
<dt><code>-o qemu</code></p>
<dd> Set the output method to <i>qemu</i>. </p>
<p> This is similar to <i>-o local</i>, except that a shell script is written which you can use to boot the guest in qemu. The converted disks and shell script are written to the directory specified by <i>-os</i>.</p>
<dt><code>-o rhev</code></p>
<dd> Set the output method to <i>rhev</i>. </p>
<p> The converted guest is written to a <font SIZE="-1">RHEV</font> Export Storage Domain. The <i>-os</i> parameter must also be used to specify the location of the Export Storage Domain. Note this does not actually import the guest into <font SIZE="-1">RHEV. </font> You have to do that manually later using the <font SIZE="-1">UI.</font> </p>
<p> See &#8220;<font SIZE="-1">OUTPUT TO RHEV&#8221;</font> below.</p>
<dt><code>-o vdsm</code></p>
<dd> Set the output method to <i>vdsm</i>. </p>
<p> This mode is similar to <i>-o rhev</i>, but the full path to the data domain must be given: <i>/rhev/data-center/&lt;data-center-uuid&gt;/&lt;data-domain-uuid&gt;</i>. This mode is only used when virt-v2v runs under <font SIZE="-1">VDSM</font> control.</p>
<dt><code>-oa sparse</code></p>
<dd>
<dt><code>-oa preallocated</code></p>
<dd> Set the output file allocation mode. The default is <tt>&quot;sparse&quot;</tt>.</p>
<dt><code>-oc</code> libvirtURI</p>
<dd> Specify a libvirt connection to use when writing the converted guest. This is only used when <i>-o libvirt</i>. See &#8220;<font SIZE="-1">OUTPUT TO LIBVIRT&#8221;</font> below. </p>
<p> Only local libvirt connections can be used. Remote libvirt connections will not work.</p>
<dt><code>-of</code> format</p>
<dd> When converting the guest, convert the disks to the given format. </p>
<p> If not specified, then the input format is used.</p>
<dt><code>-on</code> name</p>
<dd> Rename the guest when converting it. If this option is not used then the output name is the same as the input name.</p>
<dt><code>-os</code> storage</p>
<dd> The location of the storage for the converted guest. </p>
<p> For <i>-o libvirt</i>, this is a libvirt directory pool (see <tt>&quot;virsh pool-list&quot;</tt>) or pool <font SIZE="-1">UUID.</font> </p>
<p> For <i>-o local</i> and <i>-o qemu</i>, this is a directory name. The directory must exist. </p>
<p> For <i>-o rhev</i>, this can be an <font SIZE="-1">NFS</font> path of the Export Storage Domain of the form <tt>&quot;&lt;host&gt;:&lt;path&gt;&quot;</tt>, eg: </p>
<pre>
 rhev-storage.example.com:/rhev/export
</pre>
<p> The <font SIZE="-1">NFS</font> export must be mountable and writable by the user and host running virt-v2v, since the virt-v2v program has to actually mount it when it runs. So you probably have to run virt-v2v as <tt>&quot;root&quot;</tt>. </p>
<p> <code>Or:</code> You can mount the Export Storage Domain yourself, and point <i>-os</i> to the mountpoint. Note that virt-v2v will still need to write to this remote directory, so virt-v2v will still need to run as <tt>&quot;root&quot;</tt>. </p>
<p> You will get an error if virt-v2v is unable to mount/write to the Export Storage Domain.</p>
<dt><code>&#8211;password-file</code> file</p>
<dd> Instead of asking for password(s) interactively, pass the password through a file. Note the file should contain the whole password, <code>without any trailing newline</code>, and for security the file should have mode <tt>0600</tt> so that others cannot read it.</p>
<dt><code>&#8211;print-source</code></p>
<dd> Print information about the source guest and stop. This option is useful when you are setting up network and bridge maps. See &#8220;<font SIZE="-1">NETWORKS AND BRIDGES&#8221;</font>.</p>
<dt><code>-q</code></p>
<dd>
<dt><code>&#8211;quiet</code></p>
<dd> This disables progress bars and other unnecessary output.</p>
<dt><code>&#8211;root ask</code></p>
<dd>
<dt><code>&#8211;root single</code></p>
<dd>
<dt><code>&#8211;root first</code></p>
<dd>
<dt><code>&#8211;root</code> /dev/sdX</p>
<dd>
<dt><code>&#8211;root</code> /dev/VG/LV</p>
<dd> Choose the root filesystem to be converted. </p>
<p> In the case where the virtual machine is dual-boot or multi-boot, or where the <font SIZE="-1">VM</font> has other filesystems that look like operating systems, this option can be used to select the root filesystem (a.k.a. <tt>&quot;C:&quot;</tt> drive or <i>/</i>) of the operating system that is to be converted. The Windows Recovery Console, certain attached <font SIZE="-1">DVD</font> drives, and bugs in libguestfs inspection heuristics, can make a guest look like a multi-boot operating system. </p>
<p> The default in virt-v2v ≤ 0.7.1 was <i>&#8211;root single</i>, which causes virt-v2v to die if a multi-boot operating system is found. </p>
<p> Since virt-v2v ≥ 0.7.2 the default is now <i>&#8211;root ask</i>: If the <font SIZE="-1">VM</font> is found to be multi-boot, then virt-v2v will stop and list the possible root filesystems and ask the user which to use. This requires that virt-v2v is run interactively. </p>
<p> <i>&#8211;root first</i> means to choose the first root device in the case of a multi-boot operating system. Since this is a heuristic, it may sometimes choose the wrong one. </p>
<p> You can also name a specific root device, eg. <i>&#8211;root /dev/sda2</i> would mean to use the second partition on the first hard drive. If the named root device does not exist or was not detected as a root device, then virt-v2v will fail. </p>
<p> Note that there is a bug in grub which prevents it from successfully booting a multiboot system if VirtIO is enabled. Grub is only able to boot an operating system from the first VirtIO disk. Specifically, <i>/boot</i> must be on the first VirtIO disk, and it cannot chainload an <font SIZE="-1">OS</font> which is not in the first VirtIO disk.</p>
<dt><code>&#8211;vdsm-compat=0.10</code></p>
<dd>
<dt><code>&#8211;vdsm-compat=1.1</code></p>
<dd> If <i>-o vdsm</i> and the output format is qcow2, then we add the qcow2 <i>compat=0.10</i> option to the output file for compatibility with <font SIZE="-1">RHEL 6 </font>(see <a rel="nofollow" href="https://bugzilla.redhat.com/1145582">https://bugzilla.redhat.com/1145582</a>). </p>
<p> If <i>&#8211;vdsm-compat=1.1</i> is used then modern qcow2 (<i>compat=1.1</i>) files are generated instead. </p>
<p> Currently <i>&#8211;vdsm-compat=0.10</i> is the default, but this will change to <i>&#8211;vdsm-compat=1.1</i> in a future version of virt-v2v (when we can assume that everyone is using a modern version of qemu). </p>
<p> <code>Note this option only affects </code>-o vdsm<code> output</code>. All other output modes (including <i>-o rhev</i>) generate modern qcow2 <i>compat=1.1</i> files, always.</p>
<dt><code>&#8211;vdsm-image-uuid</code> <font SIZE="-1">UUID</font></p>
<dd>
<dt><code>&#8211;vdsm-vol-uuid</code> <font SIZE="-1">UUID</font></p>
<dd>
<dt><code>&#8211;vdsm-vm-uuid</code> <font SIZE="-1">UUID</font></p>
<dd>
<dt><code>&#8211;vdsm-ovf-output</code></p>
<dd> Normally the <font SIZE="-1">RHEV</font> output mode chooses random UUIDs for the target guest. However <font SIZE="-1">VDSM</font> needs to control the UUIDs and passes these parameters when virt-v2v runs under <font SIZE="-1">VDSM</font> control. The parameters control:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> the image directory of each guest disk (<i>&#8211;vdsm-image-uuid</i>) (this option is passed once for each guest disk)</p>
<dt>&bull;</p>
<dd> UUIDs for each guest disk (<i>&#8211;vdsm-vol-uuid</i>) (this option is passed once for each guest disk)</p>
<dt>&bull;</p>
<dd> the <font SIZE="-1">OVF</font> file name (<i>&#8211;vdsm-vm-uuid</i>).</p>
<dt>&bull;</p>
<dd> the <font SIZE="-1">OVF</font> output directory (default current directory) (<i>&#8211;vdsm-ovf-output</i>).</dl>
</dl>
<dl>
<dt>
<dd>
<p> The format of UUIDs is: <tt>&quot;12345678-1234-1234-1234-123456789abc&quot;</tt> (each hex digit can be <tt>&quot;0-9&quot;</tt> or <tt>&quot;a-f&quot;</tt>), conforming to <font SIZE="-1">OSF DCE 1.1.</font> </p>
<p> These options can only be used with <i>-o vdsm</i>.</dl>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd> Enable verbose messages for debugging.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Display version number and exit.</p>
<dt><code>&#8211;vmtype desktop</code></p>
<dd>
<dt><code>&#8211;vmtype server</code></p>
<dd> For the <i>-o rhev</i> or <i>-o vdsm</i> targets only, specify the type of guest. You can set this to <tt>&quot;desktop&quot;</tt> or <tt>&quot;server&quot;</tt>. If the option is not given, then a suitable default is chosen based on the detected guest operating system.</p>
<dt><code>-x</code></p>
<dd> Enable tracing of libguestfs <font SIZE="-1">API</font> calls.</dl>
<h2>XEN PARAVIRTUALIZED GUESTS</h2>
<p> Older versions of virt-v2v could turn a Xen paravirtualized (<font SIZE="-1">PV</font>) guest into a <font SIZE="-1">KVM</font> guest by installing a new kernel. This version of virt-v2v does <i>not</i> attempt to install any new kernels. Instead it will give you an error if there are <i>only</i> Xen <font SIZE="-1">PV</font> kernels available. </p>
<p> Therefore before conversion you should check that a regular kernel is installed. For some older Linux distributions, this means installing a kernel from the table below: </p>
<pre>
 RHEL 3         (Does not apply, as there was no Xen PV kernel)
 
 RHEL 4         i686 with &gt; 10GB of RAM: install 'kernel-hugemem'
                i686 SMP: install 'kernel-smp'
                other i686: install 'kernel'
                x86-64 SMP with &gt; 8 CPUs: install 'kernel-largesmp'
                x86-64 SMP: install 'kernel-smp'
                other x86-64: install 'kernel'
 
 RHEL 5         i686: install 'kernel-PAE'
                x86-64: install 'kernel'
 
 SLES 10        i586 with &gt; 10GB of RAM: install 'kernel-bigsmp'
                i586 SMP: install 'kernel-smp'
                other i586: install 'kernel-default'
                x86-64 SMP: install 'kernel-smp'
                other x86-64: install 'kernel-default'
 
 SLES 11+       i586: install 'kernel-pae'
                x86-64: install 'kernel-default'
 Windows        (Does not apply, as there is no Xen PV Windows kernel)
</pre>
<h2>ENABLING VIRTIO</h2>
<p> &#8220;Virtio&#8221; is the name for a set of drivers which make disk (block device), network and other guest operations work much faster on <font SIZE="-1">KVM.</font> </p>
<p> Older versions of virt-v2v could install these drivers for certain Linux guests. This version of virt-v2v does <i>not</i> attempt to install new Linux kernels or drivers, but will warn you if they are not installed already. </p>
<p> In order to enable virtio, and hence improve performance of the guest after conversion, you should ensure that the <code>minimum</code> versions of packages are installed <i>before</i> conversion, by consulting the table below. </p>
<pre><code>
RHEL 3 No virtio drivers are available

        RHEL 4 kernel &gt;= 2.5.9 - 89.EL lvm2 &gt;=
    2.02.42 - 5.el4 device - mapper &gt;= 1.02.28 - 2.el4 selinux - policy - targeted &gt;= 1.17.30 - 2.152.el4 policycoreutils &gt;= 1.18.1 - 4.13

                                                                                                                                 RHEL 5 kernel &gt;=
    2.6.18 - 128.el5 lvm2 &gt;= 2.02.40 - 6.el5 selinux - policy - targeted &gt;= 2.4.6 - 203.el5

                                                                                RHEL 6 +
                                                                                All versions support virtio

                                                                                    Fedora All versions support virtio

                                                                                        SLES 11 +
                                                                                All versions support virtio

                                                                                    SLES 10 kernel &gt;=
    2.6.16.60 - 0.85.1

        OpenSUSE 11 +
        All versions support virtio

            OpenSUSE 10 kernel &gt;=
    2.6.25.5 - 1.1 Windows Drivers are installed from the directory pointed to by
        "VIRTIO_WIN" environment
        variable(/ usr / share / virtio - win by default) if present
</code></pre>
<h2>RHEL 4</h2>
<h3>SELinux relabel appears to hang forever</h3>
<p> In <font SIZE="-1">RHEL</font> ≤ 4.7 there was a bug which causes SELinux relabelling to appear to hang forever at: </p>
<pre>
 *** Warning -- SELinux relabel is required. ***
 *** Disabling security enforcement.         ***
 *** Relabeling could take a very long time, ***
 *** depending on file system size.          ***
</pre>
<p> In reality it is waiting for you to press a key (but there is no visual indication of this). You can either hit the <tt>&quot;[Return]&quot;</tt> key, at which point the guest will finish relabelling and reboot, or you can install policycoreutils ≥ 1.18.1-4.13 before starting the v2v conversion. See also <a rel="nofollow" href="https://bugzilla.redhat.com/show_bug.cgi?id=244636">https://bugzilla.redhat.com/show_bug.cgi?id=244636</a></p>
<h2>WINDOWS</h2>
<h3>Windows ≥ 8 Fast Startup is incompatible with virt-v2v</h3>
<p> Guests which use the Windows ≥ 8 &#8220;Fast Startup&#8221; feature (or guests which are hibernated) cannot be converted with virt-v2v. You will see an error: </p>
<pre>
 virt-v2v: error: unable to mount the disk image for writing. This has
 probably happened because Windows Hibernation or Fast Restart is being
 used in this guest. You have to disable this (in the guest) in order
 to use virt-v2v.
</pre>
<p> As the message says, you need to boot the guest and disable the &#8220;Fast Startup&#8221; feature (Control Panel → Power Options → Choose what the power buttons do → Change settings that are currently unavailable → Turn on fast startup), and shut down the guest, and then you will be able to convert it. </p>
<p> For more information, see: &#8220;<font SIZE="-1">WINDOWS HIBERNATION AND WINDOWS 8 FAST STARTUP&#8221;</font> in <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3).</p>
<h3>Boot failure: 0x0000007B</h3>
<p> This boot failure is caused by Windows being unable to find or load the right disk driver (eg. <i>viostor.sys</i>). If you experience this error, here are some things to check:</p>
<dl>
<dt>&bull;</p>
<dd> First ensure that the guest boots on the source hypervisor before conversion.</p>
<dt>&bull;</p>
<dd> Check you have the Windows virtio drivers available in <i>/usr/share/virtio-win</i>, and that virt-v2v did not print any warning about not being able to install virtio drivers. </p>
<p> On Red Hat Enterprise Linux 7, you will need to install the signed drivers available in the <tt>&quot;virtio-win&quot;</tt> package. If you do not have access to the signed drivers, then you will probably need to disable driver signing in the boot menus.</p>
<dt>&bull;</p>
<dd> Check that you are presenting a virtio-blk interface (<code>not</code> virtio-scsi and <code>not</code> ide) to the guest. On the qemu/KVM command line you should see something similar to this: </p>
<pre>
 ... -drive file=windows-sda,if=virtio ...
</pre>
<p> In libvirt <font SIZE="-1">XML,</font> you should see: </p>
<pre>
 &lt;target dev='vda' bus='virtio'/&gt;
</pre>
<dt>&bull;</p>
<dd> Check that Windows Group Policy does not prevent the driver from being installed or used. Try deleting Windows Group Policy before conversion.</p>
<dt>&bull;</p>
<dd> Check there is no anti-virus or other software which implements Group Policy-like prohibitions on installing or using new drivers.</p>
<dt>&bull;</p>
<dd> Enable boot debugging and check the <i>viostor.sys</i> driver is being loaded.</dl>
<h3>OpenStack and Windows reactivation</h3>
<p> OpenStack does not offer stable device / <font SIZE="-1">PCI</font> addresses to guests. Every time it creates or starts a guest, it regenerates the libvirt <font SIZE="-1">XML</font> for that guest from scratch. The libvirt <font SIZE="-1">XML</font> will have no &lt;address&gt; fields. Libvirt will then assign addresses to devices, in a predictable manner. Addresses may change if any of the following are true:</p>
<dl>
<dt>&bull;</p>
<dd> A new disk or network device has been added or removed from the guest.</p>
<dt>&bull;</p>
<dd> The version of OpenStack or (possibly) libvirt has changed.</dl>
<p> Because Windows does not like &#8220;hardware&#8221; changes of this kind, it may trigger Windows reactivation. </p>
<p> This can also prevent booting with a 7B error [see previous section] if the guest has group policy containing <tt>&quot;Device Installation Restrictions&quot;</tt>.</p>
<h2>UEFI</h2>
<p> VMware allows you to present <font SIZE="-1">UEFI</font> firmware to guests (instead of the ordinary <font SIZE="-1">PC BIOS</font>). Virt-v2v can convert these guests, but requires that <font SIZE="-1">UEFI</font> is supported by the target hypervisor. </p>
<p> Currently <font SIZE="-1">KVM</font> supports <font SIZE="-1">OVMF,</font> an open source <font SIZE="-1">UEFI</font> firmware, and can run these guests. </p>
<p> Since <font SIZE="-1">OVMF</font> support was only recently added to <font SIZE="-1">KVM </font>(in 2014/2015), not all target environments support <font SIZE="-1">UEFI</font> guests yet:</p>
<dl>
<dt><font SIZE="-1">UEFI</font> on libvirt, qemu</p>
<dd> Supported. Virt-v2v will generate the correct libvirt <font SIZE="-1">XML </font>(metadata) automatically, but note that the same version of <font SIZE="-1">OVMF</font> must be installed on the conversion host as is installed on the target hypervisor, else you will have to adjust paths in the metadata. </p>
<p> On <font SIZE="-1">RHEL</font> ≥ 7.3, only qemu-kvm-rhev (not qemu-kvm) is supported.</p>
<dt><font SIZE="-1">UEFI</font> on OpenStack</p>
<dd> Not supported.</p>
<dt><font SIZE="-1">UEFI</font> on <font SIZE="-1">RHEV</font></p>
<dd> Not supported.</dl>
<h2>NETWORKS AND BRIDGES</h2>
<p> Guests are usually connected to one or more networks, and when converted to the target hypervisor you usually want to reconnect those networks at the destination. The options <i>&#8211;network</i> and <i>&#8211;bridge</i> allow you to do that. </p>
<p> If you are unsure of what networks and bridges are in use on the source hypervisor, then you can examine the source metadata (libvirt <font SIZE="-1">XML,</font> vCenter information, etc.). Or you can run virt-v2v with the <i>&#8211;print-source</i> option which causes virt-v2v to print out the information it has about the guest on the source and then exit. </p>
<p> In the <i>&#8211;print-source</i> output you will see a section showing the guest&#8217;s Network Interface Cards (NICs): </p>
<p>$ virt &#8211; v2v[-i&#8230;]&#8211; print &#8211; source name[&#8230;] NICs : Network &#8220;default&#8221; mac : 52 : 54 : 00 : d0 : cf : 0e</p>
<p> This is typical of a libvirt guest: It has a single network interface connected to a network called <tt>&quot;default&quot;</tt>. </p>
<p> To map a specific network to a target network, for example <tt>&quot;default&quot;</tt> on the source to <tt>&quot;rhevm&quot;</tt> on the target, use: </p>
<pre>
 virt-v2v [...] --network default:rhevm
</pre>
<p> To map every network to a target network, use: </p>
<pre>
 virt-v2v [...] --network rhevm
</pre>
<p> Bridges are handled in the same way, but you have to use the <i>&#8211;bridge</i> option instead. For example: </p>
<p>$ virt &#8211; v2v[-i&#8230;]&#8211; print &#8211; source name[&#8230;] NICs : Bridge &#8220;br0&#8221;</p>
<p>                                                      $ virt &#8211;<br />
                                                      v2v[&#8230;]&#8211; bridge br0 : targetbr</p>
<h2>INPUT FROM VMWARE VCENTER SERVER</h2>
<p> Virt-v2v is able to import guests from VMware vCenter Server. </p>
<p> vCenter ≥ 5.0 is required. If you don&#8217;t have vCenter, using <font SIZE="-1">OVA</font> is recommended instead (see &#8220;<font SIZE="-1">INPUT FROM VMWARE OVA&#8221;</font> below), or if that is not possible then see &#8220;<font SIZE="-1">INPUT FROM VMWARE</font> ESXi <font SIZE="-1">HYPERVISOR&#8221;</font>. </p>
<p> Virt-v2v uses libvirt for access to vCenter, and therefore the input mode should be <i>-i libvirt</i>. As this is the default, you don&#8217;t need to specify it on the command line.</p>
<h3><font SIZE="-1">VCENTER: REMOVE VMWARE TOOLS FROM WINDOWS GUESTS</font></h3>
<p> For Windows guests, you should remove VMware tools before conversion. Although this is not strictly necessary, and the guest will still be able to run, if you don&#8217;t do this then the converted guest will complain on every boot. The tools cannot be removed after conversion because the uninstaller checks if it is running on VMware and refuses to start (which is also the reason that virt-v2v cannot remove them). </p>
<p> This is not necessary for Linux guests, as virt-v2v is able to remove VMware tools.</p>
<h3><font SIZE="-1">VCENTER: URI</font></h3>
<p> The libvirt <font SIZE="-1">URI</font> of a vCenter server looks something like this: </p>
<pre>
 <a href="vpx://user@server/Datacenter/esxi">vpx://user@server/Datacenter/esxi</a>
</pre>
<p> where:</p>
<dl>
<dt>&quot;user@&quot;</p>
<dd> is the (optional, but recommended) user to connect as. </p>
<p> If the username contains a backslash (eg. <tt>&quot;DOMAIN
