---

title: "virt-v2v(1)"
name: "virt-v2v"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-v2v/"
description: "virt-v2v – Convert a guest to use KVM"
---

<pre>
 virt-v2v -ic <a href="vpx://vcenter.example.com/Datacenter/esxi">vpx://vcenter.example.com/Datacenter/esxi</a> vmware_guest
 virt-v2v -ic <a href="vpx://vcenter.example.com/Datacenter/esxi">vpx://vcenter.example.com/Datacenter/esxi</a> vmware_guest \
   -o rhev -os rhev.nfs:/export_domain --network rhevm
 virt-v2v -i libvirtxml guest-domain.xml -o local -os /var/tmp
 virt-v2v -i disk disk.img -o local -os /var/tmp
 virt-v2v -i disk disk.img -o glance
</pre>
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
<dt><code>&#8211;help</code></dt>
<dd> Display help.</dd>
<dt><code>-b</code> &#8230;</dt>
<dd>
</dd><dt><code>&#8211;bridge</code> &#8230;</dt>
<dd> See <i>&#8211;network</i> below.</dd>
<dt><code>&#8211;colors</code></dt>
<dd>
</dd><dt><code>&#8211;colours</code></dt>
<dd> Use <font SIZE="-1">ANSI</font> colour sequences to colourize messages. This is the default when the output is a tty. If the output of the program is redirected to a file, <font SIZE="-1">ANSI</font> colour sequences are disabled unless you use this option.</dd>
<dt><code>&#8211;compressed</code></dt>
<dd> Write a compressed output file. This is only allowed if the output format is qcow2 (see <i>-of</i> below), and is equivalent to the <i>-c</i> option of <i><a href="/docs/linux/man/1-qemu-img/">qemu-img</a></i>(1).</dd>
<dt><code>&#8211;debug-gc</code></dt>
<dd> Debug garbage collection and memory allocation. This is only useful when debugging memory problems in virt-v2v or the OCaml libguestfs bindings.</dd>
<dt><code>&#8211;debug-overlays</code></dt>
<dd> Save the overlay file(s) created during conversion. This option is only used for debugging virt-v2v and may be removed in a future version.</dd>
<dt><code>-i disk</code></dt>
<dd> Set the input method to <i>disk</i>. </dd>
<p> In this mode you can read a virtual machine disk image with no metadata. virt-v2v tries to guess the best default metadata. This is usually adequate but you can get finer control (eg. of memory and vCPUs) by using <i>-i libvirtxml</i> instead. Only guests that use a single disk can be imported this way.</p>
<dt><code>-i libvirt</code></dt>
<dd> Set the input method to <i>libvirt</i>. This is the default. </dd>
<p> In this mode you have to specify a libvirt guest name or <font SIZE="-1">UUID</font> on the command line. You may also specify a libvirt connection <font SIZE="-1">URI </font>(see <i>-ic</i>).</p>
<dt><code>-i libvirtxml</code></dt>
<dd> Set the input method to <i>libvirtxml</i>. </dd>
<p> In this mode you have to pass a libvirt <font SIZE="-1">XML</font> file on the command line. This file is read in order to get metadata about the source guest (such as its name, amount of memory), and also to locate the input disks. See &#8220;<font SIZE="-1">MINIMAL XML FOR</font> -i libvirtxml <font SIZE="-1">OPTION&#8221;</font> below.</p>
<dt><code>-i local</code></dt>
<dd> This is the same as <i>-i disk</i>.</dd>
<dt><code>-i ova</code></dt>
<dd> Set the input method to <i>ova</i>. </dd>
<p> In this mode you can read a VMware ova file. Virt-v2v will read the ova manifest file and check the vmdk volumes for validity (checksums) as well as analyzing the ovf file, and then convert the guest. See &#8220;<font SIZE="-1">INPUT FROM VMWARE OVA&#8221;</font> below</p>
<dt><code>-ic</code> libvirtURI</dt>
<dd> Specify a libvirt connection <font SIZE="-1">URI</font> to use when reading the guest. This is only used when <i>-i libvirt</i>. </dd>
<p> Only local libvirt connections, VMware vCenter connections, or <font SIZE="-1">RHEL 5</font> Xen remote connections can be used. Other remote libvirt connections will not work in general. </p>
<p> See also &#8220;<font SIZE="-1">INPUT FROM VMWARE VCENTER SERVER&#8221;</font>, &#8220;<font SIZE="-1">INPUT FROM RHEL 5 XEN&#8221;</font> below.</p>
<dt><code>-if</code> format</dt>
<dd> For <i>-i disk</i> only, this specifies the format of the input disk image. For other input methods you should specify the input format in the metadata.</dd>
<dt><code>&#8211;machine-readable</code></dt>
<dd> This option is used to make the output more machine friendly when being parsed by other programs. See &#8220;<font SIZE="-1">MACHINE READABLE OUTPUT&#8221;</font> below.</dd>
<dt><code>-n</code> in:out</dt>
<dd>
</dd><dt><code>-n</code> out</dt>
<dd>
</dd><dt><code>&#8211;network</code> in:out</dt>
<dd>
</dd><dt><code>&#8211;network</code> out</dt>
<dd>
</dd><dt><code>-b</code> in:out</dt>
<dd>
</dd><dt><code>-b</code> out</dt>
<dd>
</dd><dt><code>&#8211;bridge</code> in:out</dt>
<dd>
</dd><dt><code>&#8211;bridge</code> out</dt>
<dd> Map network (or bridge) called <tt>&quot;in&quot;</tt> to network (or bridge) called <tt>&quot;out&quot;</tt>. If no <tt>&quot;in:&quot;</tt> prefix is given, all other networks (or bridges) are mapped to <tt>&quot;out&quot;</tt>. </dd>
<p> See &#8220;<font SIZE="-1">NETWORKS AND BRIDGES&#8221;</font> below.</p>
<dt><code>&#8211;no-copy</code></dt>
<dd> Don&#8217;t copy the disks. Instead, conversion is performed (and thrown away), and metadata is written, but no disks are created. See also discussion of <i>-o null</i> below. </dd>
<p> This is useful in two cases: Either you want to test if conversion is likely to succeed, without the long copying process. Or you are only interested in looking at the metadata. </p>
<p> This option is not compatible with <i>-o libvirt</i> since it would create a faulty guest (one with no disks). </p>
<p> This option is not compatible with <i>-o glance</i> for technical reasons.</p>
<dt><code>&#8211;no-trim all</code></dt>
<dd>
</dd><dt><code>&#8211;no-trim</code> mp[,mp&#8230;]</dt>
<dd> By default virt-v2v runs <i><a href="/docs/linux/man/8-fstrim/">fstrim</a></i>(8) to reduce the amount of data that needs to be copied. This is known to break some buggy bootloaders causing boot failures after conversion (see for example <a rel="nofollow" href="https://bugzilla.redhat.com/show_bug.cgi?id=1141145#c27">https://bugzilla.redhat.com/show_bug.cgi?id=1141145#c27</a>). </dd>
<p> You can use <i>&#8211;no-trim all</i> to disable all trimming. Note this will greatly increase the amount of data that has to be copied and can make virt-v2v run much more slowly. </p>
<p> You can also disable trimming on selected filesystems only (specified by a comma-separated list of their mount point(s) in the guest). Typically you would use <i>&#8211;no-trim /boot</i> to work around the grub bug mentioned above. </p>
<p> You can also disable trimming on partitions using the libguestfs naming scheme for devices, eg: <i>&#8211;no-trim /dev/sdb2</i> means do not trim the second partition on the second block device. Use <i><a href="/docs/linux/man/1-virt-filesystems/">virt-filesystems</a></i>(1) to list filesystem names in a guest.</p>
<dt><code>-o disk</code></dt>
<dd> This is the same as <i>-o local</i>.</dd>
<dt><code>-o glance</code></dt>
<dd> Set the output method to OpenStack Glance. In this mode the converted guest is uploaded to Glance. See &#8220;<font SIZE="-1">OUTPUT TO GLANCE&#8221;</font> below.</dd>
<dt><code>-o libvirt</code></dt>
<dd> Set the output method to <i>libvirt</i>. This is the default. </dd>
<p> In this mode, the converted guest is created as a libvirt guest. You may also specify a libvirt connection <font SIZE="-1">URI </font>(see <i>-oc</i>). </p>
<p> See &#8220;<font SIZE="-1">OUTPUT TO LIBVIRT&#8221;</font> below.</p>
<dt><code>-o local</code></dt>
<dd> Set the output method to <i>local</i>. </dd>
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
<dt><code>-o null</code></dt>
<dd> Set the output method to <i>null</i>. </dd>
<p> The guest is converted and copied (unless you also specify <i>&#8211;no-copy</i>), but the results are thrown away and no metadata is written.</p>
<dt><code>-o ovirt</code></dt>
<dd> This is the same as <i>-o rhev</i>.</dd>
<dt><code>-o qemu</code></dt>
<dd> Set the output method to <i>qemu</i>. </dd>
<p> This is similar to <i>-o local</i>, except that a shell script is written which you can use to boot the guest in qemu. The converted disks and shell script are written to the directory specified by <i>-os</i>.</p>
<dt><code>-o rhev</code></dt>
<dd> Set the output method to <i>rhev</i>. </dd>
<p> The converted guest is written to a <font SIZE="-1">RHEV</font> Export Storage Domain. The <i>-os</i> parameter must also be used to specify the location of the Export Storage Domain. Note this does not actually import the guest into <font SIZE="-1">RHEV. </font> You have to do that manually later using the <font SIZE="-1">UI.</font> </p>
<p> See &#8220;<font SIZE="-1">OUTPUT TO RHEV&#8221;</font> below.</p>
<dt><code>-o vdsm</code></dt>
<dd> Set the output method to <i>vdsm</i>. </dd>
<p> This mode is similar to <i>-o rhev</i>, but the full path to the data domain must be given: <i>/rhev/data-center/&lt;data-center-uuid&gt;/&lt;data-domain-uuid&gt;</i>. This mode is only used when virt-v2v runs under <font SIZE="-1">VDSM</font> control.</p>
<dt><code>-oa sparse</code></dt>
<dd>
</dd><dt><code>-oa preallocated</code></dt>
<dd> Set the output file allocation mode. The default is <tt>&quot;sparse&quot;</tt>.</dd>
<dt><code>-oc</code> libvirtURI</dt>
<dd> Specify a libvirt connection to use when writing the converted guest. This is only used when <i>-o libvirt</i>. See &#8220;<font SIZE="-1">OUTPUT TO LIBVIRT&#8221;</font> below. </dd>
<p> Only local libvirt connections can be used. Remote libvirt connections will not work.</p>
<dt><code>-of</code> format</dt>
<dd> When converting the guest, convert the disks to the given format. </dd>
<p> If not specified, then the input format is used.</p>
<dt><code>-on</code> name</dt>
<dd> Rename the guest when converting it. If this option is not used then the output name is the same as the input name.</dd>
<dt><code>-os</code> storage</dt>
<dd> The location of the storage for the converted guest. </dd>
<p> For <i>-o libvirt</i>, this is a libvirt directory pool (see <tt>&quot;virsh pool-list&quot;</tt>) or pool <font SIZE="-1">UUID.</font> </p>
<p> For <i>-o local</i> and <i>-o qemu</i>, this is a directory name. The directory must exist. </p>
<p> For <i>-o rhev</i>, this can be an <font SIZE="-1">NFS</font> path of the Export Storage Domain of the form <tt>&quot;&lt;host&gt;:&lt;path&gt;&quot;</tt>, eg: </p>
<pre>
 rhev-storage.example.com:/rhev/export
</pre>
<p> The <font SIZE="-1">NFS</font> export must be mountable and writable by the user and host running virt-v2v, since the virt-v2v program has to actually mount it when it runs. So you probably have to run virt-v2v as <tt>&quot;root&quot;</tt>. </p>
<p> <code>Or:</code> You can mount the Export Storage Domain yourself, and point <i>-os</i> to the mountpoint. Note that virt-v2v will still need to write to this remote directory, so virt-v2v will still need to run as <tt>&quot;root&quot;</tt>. </p>
<p> You will get an error if virt-v2v is unable to mount/write to the Export Storage Domain.</p>
<dt><code>&#8211;password-file</code> file</dt>
<dd> Instead of asking for password(s) interactively, pass the password through a file. Note the file should contain the whole password, <code>without any trailing newline</code>, and for security the file should have mode <tt>0600</tt> so that others cannot read it.</dd>
<dt><code>&#8211;print-source</code></dt>
<dd> Print information about the source guest and stop. This option is useful when you are setting up network and bridge maps. See &#8220;<font SIZE="-1">NETWORKS AND BRIDGES&#8221;</font>.</dd>
<dt><code>-q</code></dt>
<dd>
</dd><dt><code>&#8211;quiet</code></dt>
<dd> This disables progress bars and other unnecessary output.</dd>
<dt><code>&#8211;root ask</code></dt>
<dd>
</dd><dt><code>&#8211;root single</code></dt>
<dd>
</dd><dt><code>&#8211;root first</code></dt>
<dd>
</dd><dt><code>&#8211;root</code> /dev/sdX</dt>
<dd>
</dd><dt><code>&#8211;root</code> /dev/VG/LV</dt>
<dd> Choose the root filesystem to be converted. </dd>
<p> In the case where the virtual machine is dual-boot or multi-boot, or where the <font SIZE="-1">VM</font> has other filesystems that look like operating systems, this option can be used to select the root filesystem (a.k.a. <tt>&quot;C:&quot;</tt> drive or <i>/</i>) of the operating system that is to be converted. The Windows Recovery Console, certain attached <font SIZE="-1">DVD</font> drives, and bugs in libguestfs inspection heuristics, can make a guest look like a multi-boot operating system. </p>
<p> The default in virt-v2v ≤ 0.7.1 was <i>&#8211;root single</i>, which causes virt-v2v to die if a multi-boot operating system is found. </p>
<p> Since virt-v2v ≥ 0.7.2 the default is now <i>&#8211;root ask</i>: If the <font SIZE="-1">VM</font> is found to be multi-boot, then virt-v2v will stop and list the possible root filesystems and ask the user which to use. This requires that virt-v2v is run interactively. </p>
<p> <i>&#8211;root first</i> means to choose the first root device in the case of a multi-boot operating system. Since this is a heuristic, it may sometimes choose the wrong one. </p>
<p> You can also name a specific root device, eg. <i>&#8211;root /dev/sda2</i> would mean to use the second partition on the first hard drive. If the named root device does not exist or was not detected as a root device, then virt-v2v will fail. </p>
<p> Note that there is a bug in grub which prevents it from successfully booting a multiboot system if VirtIO is enabled. Grub is only able to boot an operating system from the first VirtIO disk. Specifically, <i>/boot</i> must be on the first VirtIO disk, and it cannot chainload an <font SIZE="-1">OS</font> which is not in the first VirtIO disk.</p>
<dt><code>&#8211;vdsm-compat=0.10</code></dt>
<dd>
</dd><dt><code>&#8211;vdsm-compat=1.1</code></dt>
<dd> If <i>-o vdsm</i> and the output format is qcow2, then we add the qcow2 <i>compat=0.10</i> option to the output file for compatibility with <font SIZE="-1">RHEL 6 </font>(see <a rel="nofollow" href="https://bugzilla.redhat.com/1145582">https://bugzilla.redhat.com/1145582</a>). </dd>
<p> If <i>&#8211;vdsm-compat=1.1</i> is used then modern qcow2 (<i>compat=1.1</i>) files are generated instead. </p>
<p> Currently <i>&#8211;vdsm-compat=0.10</i> is the default, but this will change to <i>&#8211;vdsm-compat=1.1</i> in a future version of virt-v2v (when we can assume that everyone is using a modern version of qemu). </p>
<p> <code>Note this option only affects </code>-o vdsm<code> output</code>. All other output modes (including <i>-o rhev</i>) generate modern qcow2 <i>compat=1.1</i> files, always.</p>
<dt><code>&#8211;vdsm-image-uuid</code> <font SIZE="-1">UUID</font></dt>
<dd>
</dd><dt><code>&#8211;vdsm-vol-uuid</code> <font SIZE="-1">UUID</font></dt>
<dd>
</dd><dt><code>&#8211;vdsm-vm-uuid</code> <font SIZE="-1">UUID</font></dt>
<dd>
</dd><dt><code>&#8211;vdsm-ovf-output</code></dt>
<dd> Normally the <font SIZE="-1">RHEV</font> output mode chooses random UUIDs for the target guest. However <font SIZE="-1">VDSM</font> needs to control the UUIDs and passes these parameters when virt-v2v runs under <font SIZE="-1">VDSM</font> control. The parameters control:</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> the image directory of each guest disk (<i>&#8211;vdsm-image-uuid</i>) (this option is passed once for each guest disk)</dd>
<dt>&bull;</dt>
<dd> UUIDs for each guest disk (<i>&#8211;vdsm-vol-uuid</i>) (this option is passed once for each guest disk)</dd>
<dt>&bull;</dt>
<dd> the <font SIZE="-1">OVF</font> file name (<i>&#8211;vdsm-vm-uuid</i>).</dd>
<dt>&bull;</dt>
<dd> the <font SIZE="-1">OVF</font> output directory (default current directory) (<i>&#8211;vdsm-ovf-output</i>).</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> The format of UUIDs is: <tt>&quot;12345678-1234-1234-1234-123456789abc&quot;</tt> (each hex digit can be <tt>&quot;0-9&quot;</tt> or <tt>&quot;a-f&quot;</tt>), conforming to <font SIZE="-1">OSF DCE 1.1.</font> </p>
<p> These options can only be used with <i>-o vdsm</i>.</dd></dl>
<dt><code>-v</code></dt>
<dd>
</dd><dt><code>&#8211;verbose</code></dt>
<dd> Enable verbose messages for debugging.</dd>
<dt><code>-V</code></dt>
<dd>
</dd><dt><code>&#8211;version</code></dt>
<dd> Display version number and exit.</dd>
<dt><code>&#8211;vmtype desktop</code></dt>
<dd>
</dd><dt><code>&#8211;vmtype server</code></dt>
<dd> For the <i>-o rhev</i> or <i>-o vdsm</i> targets only, specify the type of guest. You can set this to <tt>&quot;desktop&quot;</tt> or <tt>&quot;server&quot;</tt>. If the option is not given, then a suitable default is chosen based on the detected guest operating system.</dd>
<dt><code>-x</code></dt>
<dd> Enable tracing of libguestfs <font SIZE="-1">API</font> calls.</dd></dl>
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
<p> For more information, see: &#8220;<font SIZE="-1">WINDOWS HIBERNATION AND WINDOWS 8 FAST STARTUP&#8221;</font> in <i>guestfs</i>(3).</p>
<h3>Boot failure: 0x0000007B</h3>
<p> This boot failure is caused by Windows being unable to find or load the right disk driver (eg. <i>viostor.sys</i>). If you experience this error, here are some things to check:</p>
<dl>
<dt>&bull;</dt>
<dd> First ensure that the guest boots on the source hypervisor before conversion.</dd>
<dt>&bull;</dt>
<dd> Check you have the Windows virtio drivers available in <i>/usr/share/virtio-win</i>, and that virt-v2v did not print any warning about not being able to install virtio drivers. </dd>
<p> On Red Hat Enterprise Linux 7, you will need to install the signed drivers available in the <tt>&quot;virtio-win&quot;</tt> package. If you do not have access to the signed drivers, then you will probably need to disable driver signing in the boot menus.</p>
<dt>&bull;</dt>
<dd> Check that you are presenting a virtio-blk interface (<code>not</code> virtio-scsi and <code>not</code> ide) to the guest. On the qemu/KVM command line you should see something similar to this: </dd>
<pre>
 ... -drive file=windows-sda,if=virtio ...
</pre>
<p> In libvirt <font SIZE="-1">XML,</font> you should see: </p>
<pre>
 &lt;target dev='vda' bus='virtio'/&gt;
</pre>
<dt>&bull;</dt>
<dd> Check that Windows Group Policy does not prevent the driver from being installed or used. Try deleting Windows Group Policy before conversion.</dd>
<dt>&bull;</dt>
<dd> Check there is no anti-virus or other software which implements Group Policy-like prohibitions on installing or using new drivers.</dd>
<dt>&bull;</dt>
<dd> Enable boot debugging and check the <i>viostor.sys</i> driver is being loaded.</dd></dl>
<h3>OpenStack and Windows reactivation</h3>
<p> OpenStack does not offer stable device / <font SIZE="-1">PCI</font> addresses to guests. Every time it creates or starts a guest, it regenerates the libvirt <font SIZE="-1">XML</font> for that guest from scratch. The libvirt <font SIZE="-1">XML</font> will have no &lt;address&gt; fields. Libvirt will then assign addresses to devices, in a predictable manner. Addresses may change if any of the following are true:</p>
<dl>
<dt>&bull;</dt>
<dd> A new disk or network device has been added or removed from the guest.</dd>
<dt>&bull;</dt>
<dd> The version of OpenStack or (possibly) libvirt has changed.</dd></dl>
<p> Because Windows does not like &#8220;hardware&#8221; changes of this kind, it may trigger Windows reactivation. </p>
<p> This can also prevent booting with a 7B error [see previous section] if the guest has group policy containing <tt>&quot;Device Installation Restrictions&quot;</tt>.</p>
<h2>UEFI</h2>
<p> VMware allows you to present <font SIZE="-1">UEFI</font> firmware to guests (instead of the ordinary <font SIZE="-1">PC BIOS</font>). Virt-v2v can convert these guests, but requires that <font SIZE="-1">UEFI</font> is supported by the target hypervisor. </p>
<p> Currently <font SIZE="-1">KVM</font> supports <font SIZE="-1">OVMF,</font> an open source <font SIZE="-1">UEFI</font> firmware, and can run these guests. </p>
<p> Since <font SIZE="-1">OVMF</font> support was only recently added to <font SIZE="-1">KVM </font>(in 2014/2015), not all target environments support <font SIZE="-1">UEFI</font> guests yet:</p>
<dl>
<dt><font SIZE="-1">UEFI</font> on libvirt, qemu</dt>
<dd> Supported. Virt-v2v will generate the correct libvirt <font SIZE="-1">XML </font>(metadata) automatically, but note that the same version of <font SIZE="-1">OVMF</font> must be installed on the conversion host as is installed on the target hypervisor, else you will have to adjust paths in the metadata. </dd>
<p> On <font SIZE="-1">RHEL</font> ≥ 7.3, only qemu-kvm-rhev (not qemu-kvm) is supported.</p>
<dt><font SIZE="-1">UEFI</font> on OpenStack</dt>
<dd> Not supported.</dd>
<dt><font SIZE="-1">UEFI</font> on <font SIZE="-1">RHEV</font></dt>
<dd> Not supported.</dd></dl>
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
<dt>&quot;user@&quot;</dt>
<dd> is the (optional, but recommended) user to connect as. </dd>
<p> If the username contains a backslash (eg. <tt>&quot;DOMAIN</tt>\USER&quot;</code>) then you will need to URI-escape that character using <code>%5c</code>: <code>&quot;DOMAIN%5cUSER&quot;</code> (5c is the hexadecimal <font SIZE="-1">ASCII</font> code for backslash.) Other punctuation may also have to be escaped. </p>
<dt>&quot;server&quot;</dt>
<dd> <p> is the vCenter Server (<i>not</i> hypervisor). </p>
 </dd>
<dt>&quot;Datacenter&quot;</dt>
<dd> <p> is the name of the datacenter. </p>
<p> If the name contains a space, replace it with the URI-escape code <code>%20</code>. </p>
 </dd>
<dt>&quot;esxi&quot;</dt>
<dd> <p> is the name of the ESXi hypervisor running the guest. </p>
 </dd></dl>
<p> If the VMware deployment is using folders, then these may need to be added to the <font SIZE="-1">URI,</font> eg: </p>
<pre><code>vpx://user@server/Folder/Datacenter/esxi
</code></pre>
<p> For full details of libvirt URIs, see: <a rel="nofollow" href="http://libvirt.org/drvesx.html">http://libvirt.org/drvesx.html</a> </p>
<p> Typical errors from libvirt / virsh when the <font SIZE="-1">URI</font> is wrong include: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Could not find datacenter specified in [...] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Could not find compute resource specified in [...] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Path [...] does not specify a compute resource </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Path [...] does not specify a host system </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Could not find host system specified in [...] </p>
 </dd></dl>
<font SIZE="-1"></font><h3>VCENTER: TEST LIBVIRT CONNECTION TO VCENTER</h3>
<p> Use the <i><a href="/docs/linux/man/1-virsh/">virsh</a></i>(1) command to list the guests on the vCenter Server like this: </p>
<pre><code> $ virsh -c 'vpx://root@vcenter.example.com/Datacenter/esxi' list --all
 Enter root's password for vcenter.example.com: ***
  Id Name State
 ----------------------------------------------------
  - Fedora 20 shut off
  - Windows 2003 shut off
</code></pre>
<p> If you get an error ``Peer certificate cannot be authenticated with given <font SIZE="-1">CA</font> certificates&#8217;&#8216; or similar, then you can either import the vCenter host&#8217;s certificate, or bypass signature verification by adding the <code>&quot;?no_verify=1&quot;</code> flag: </p>
<pre><code> $ virsh -c 'vpx://root@vcenter.example.com/Datacenter/esxi?no_verify=1' list --all
</code></pre>
<p> You should also try dumping the metadata from any guest on your server, like this: </p>
<pre><code> $ virsh -c 'vpx://root@vcenter.example.com/Datacenter/esxi' dumpxml &quot;Windows 2003&quot;
 &lt;domain type='vmware'&gt;
   &lt;name&gt;Windows 2003&lt;/name&gt;
   [...]
 &lt;/domain&gt;
</code></pre>
<p> <code>If the above commands do not work, then virt-v2v is not going to work either</code>. Fix your libvirt configuration and/or your VMware vCenter Server before continuing.  </p>
<font SIZE="-1"></font><h3>VCENTER: IMPORTING A GUEST</h3>
<p> To import a particular guest from vCenter Server, do: </p>
<pre><code> $ virt-v2v -ic 'vpx://root@vcenter.example.com/Datacenter/esxi?no_verify=1' \
   &quot;Windows 2003&quot; \
   -o local -os /var/tmp
</code></pre>
<p> where <code>&quot;Windows 2003&quot;</code> is the name of the guest (which must be shut down). </p>
<p> Note that you may be asked for the vCenter password <i>twice</i>. This happens once because libvirt needs it, and a second time because virt-v2v itself connects directly to the server. Use <i>--password-file</i> to supply a password via a file. </p>
<p> In this case the output flags are set to write the converted guest to a temporary directory as this is just an example, but you can also write to libvirt or any other supported target.  </p>
<font SIZE="-1"></font><font SIZE="-1"></font><h3>VCENTER: NON-ADMINISTRATOR ROLE</h3>
<p> Instead of using the vCenter Administrator role, you can create a custom non-administrator role to perform the conversion. You will however need to give it a minimum set of permissions as follows: </p>
<dl>
<dt>1.</dt>
<dd> <p> Create a custom role in vCenter. </p>
 </dd>
<dt>2.</dt>
<dd> <p> Enable (check) the following objects: </p>
<pre><code> Datastore:
  - Browse datastore
  - Low level file operations
 Sessions:
  - Validate session
 Virtual Machine:
   Provisioning:
     - Allow disk access
     - Allow read-only disk access
     - Guest Operating system management by VIX API
</code></pre>
 </dd></dl>
<font SIZE="-1"></font><h3>VCENTER: FIREWALL AND PROXY SETTINGS</h3>
<p> <i>vCenter: Ports</i> </p>
<p> If there is a firewall between the virt-v2v conversion server and the vCenter server, then you will need to open port 443 (https) and port 5480. </p>
<p> Port 443 is used to copy the guest disk image(s). Port 5480 is used to query vCenter for guest metadata. </p>
<p> These port numbers are only the defaults. It is possible to reconfigure vCenter to use other port numbers. In that case you would need to specify those ports in the <code>&quot;vpx://&quot;</code> <font SIZE="-1">URI.</font> See ``<font SIZE="-1">VCENTER: URI&#8217;&#8216;</font> above. </p>
<p> These ports only apply to virt-v2v conversions. You may have to open other ports for other vCenter functionality, for example the web user interface. VMware documents the required ports for vCenter in their online documentation. </p>
<pre><code> ┌────────────┐ port 443 ┌────────────┐ ┌────────────┐
 │ virt-v2v │────────────▶ vCenter │────────▶ ESXi │
 │ conversion │────────────▶ server │ │ hypervisor │
 │ server │ port 5480 │ │ │ ┌─────┐ │
 └────────────┘ └────────────┘ │ │guest│ │
                                                 └───┴─────┴──┘
</code></pre>
<p> (In the diagram above the arrows show the direction in which the <font SIZE="-1">TCP</font> connection is initiated, <i>not</i> necessarily the direction of data transfer.) </p>
<p> Virt-v2v itself does not connect directly to the ESXi hypervisor containing the guest. However vCenter connects to the hypervisor and forwards the information, so if you have a firewall between vCenter and its hypervisors you may need to open additional ports (consult VMware documentation). </p>
<p> <i>vCenter: Proxy settings</i> </p>
<p> To copy the disks, virt-v2v uses <i><a href="/docs/linux/man/3-libcurl/">libcurl</a></i>(3). The Curl library obeys the proxy environment variables, in particular <code>&quot;https_proxy&quot;</code>, <code>&quot;all_proxy&quot;</code> and <code>&quot;no_proxy&quot;</code> (<code>&quot;HTTPS_PROXY&quot;</code>, <code>&quot;ALL_PROXY&quot;</code> and <code>&quot;NO_PROXY&quot;</code> can also be used, but the lowercase named environment variables take precedence). </p>
<p> If these environment variables are set then copying may happen via the proxy, and so a different set of ports may need to be opened in the firewall. </p>
<p> The port 5480 connection never uses a proxy.  </p>
<h2>INPUT FROM VMWARE OVA</h2>
<p> Virt-v2v is able to import guests from VMware&#8217;s <font SIZE="-1">OVA </font>(Open Virtualization Appliance) files. Only OVAs exported from VMware vSphere will work.  </p>
<font SIZE="-1"></font><h3>OVA: REMOVE VMWARE TOOLS FROM WINDOWS GUESTS</h3>
<p> For Windows guests, you should remove VMware tools before conversion. Although this is not strictly necessary, and the guest will still be able to run, if you don&#8217;t do this then the converted guest will complain on every boot. The tools cannot be removed after conversion because the uninstaller checks if it is running on VMware and refuses to start (which is also the reason that virt-v2v cannot remove them). </p>
<p> This is not necessary for Linux guests, as virt-v2v is able to remove VMware tools.  </p>
<font SIZE="-1"></font><h3>OVA: CREATE OVA</h3>
<p> To create an <font SIZE="-1">OVA</font> in vSphere, use the ``Export <font SIZE="-1">OVF</font> Template&#8217;&#8216; option (from the <font SIZE="-1">VM</font> context menu, or from the File menu). Either ``Folder of files&#8217;&#8216; (<font SIZE="-1">OVF</font>) or ``Single file&#8217;&#8216; (<font SIZE="-1">OVA</font>) will work, but <font SIZE="-1">OVA</font> is probably easier to deal with. <font SIZE="-1">OVA</font> files are really just uncompressed tar files, so you can use commands like <code>&quot;tar tf VM.ova&quot;</code> to view their contents. </p>
<p> <i>Create </i><font SIZE="-1"><i>OVA</i></font><i> with ovftool</i> </p>
<p> You can also use VMware&#8217;s proprietary <code>&quot;ovftool&quot;</code>: </p>
<pre><code> ovftool --noSSLVerify \
   vi://USER:PASSWORD [at] esxi.example.com/VM \
   VM.ova
</code></pre>
<p> To connect to vCenter: </p>
<pre><code> ovftool --noSSLVerify \
   vi://USER:PASSWORD [at] vcenter.example.com/DATACENTER-NAME/vm/VM \
   VM.ova
</code></pre>
<p> For Active Directory-aware authentication, you have to express the <code>&quot;@&quot;</code> character in the form of its ascii hex-code (<code>%5c</code>): </p>
<pre><code> vi://DOMAIN%5cUSER:PASSWORD@...
</code></pre>
<font SIZE="-1"></font><h3>OVA: IMPORTING A GUEST</h3>
<p> To import an <font SIZE="-1">OVA</font> file called <i></i><font SIZE="-1"><i>VM</i></font><i>.ova</i>, do; </p>
<pre><code> $ virt-v2v -i ova VM.ova -o local -os /var/tmp
</code></pre>
<p> If you exported the guest as a ``Folder of files&#8217;&#8216;, <i>or</i> if you unpacked the <font SIZE="-1">OVA</font> tarball yourself, then you can point virt-v2v at the directory containing the files: </p>
<pre><code> $ virt-v2v -i ova /path/to/files -o local -os /var/tmp
</code></pre>
<h2>INPUT FROM VMWARE ESXi HYPERVISOR</h2>
<p> Virt-v2v cannot access an ESXi hypervisor directly. You should use the <font SIZE="-1">OVA</font> method above (see ``<font SIZE="-1">INPUT FROM VMWARE OVA&#8217;&#8216;</font>) if possible, as it is much faster and requires much less disk space than the method described in this section. </p>
<p> You can use the <i><a href="/docs/linux/man/1-virt-v2v-copy-to-local/">virt-v2v-copy-to-local</a></i>(1) tool to copy the guest off the hypervisor into a local file, and then convert it.  </p>
<font SIZE="-1"></font><h3>ESXi: REMOVE VMWARE TOOLS FROM WINDOWS GUESTS</h3>
<p> For Windows guests, you should remove VMware tools before conversion. Although this is not strictly necessary, and the guest will still be able to run, if you don&#8217;t do this then the converted guest will complain on every boot. The tools cannot be removed after conversion because the uninstaller checks if it is running on VMware and refuses to start (which is also the reason that virt-v2v cannot remove them). </p>
<p> This is not necessary for Linux guests, as virt-v2v is able to remove VMware tools.  </p>
<font SIZE="-1"></font><h3>ESXi: URI</h3>
<p> The libvirt <font SIZE="-1">URI</font> for VMware ESXi hypervisors will look something like this: </p>
<pre><code>esx://root@esxi.example.com?no_verify=1
</code></pre>
<p> The <code>&quot;?no_verify=1&quot;</code> parameter disables <font SIZE="-1">TLS</font> certificate checking.  </p>
<font SIZE="-1"></font><font SIZE="-1"></font><h3>ESXi: TEST LIBVIRT CONNECTION TO ESXi HYPERVISOR</h3>
<p> Use the <i><a href="/docs/linux/man/1-virsh/">virsh</a></i>(1) command to test the <font SIZE="-1">URI</font> and list the remote guests available: </p>
<pre><code> $ virsh -cesx://root@esxi.example.com?no_verify=1 list --all
 Enter root's password for esxi.example.com: ***
  Id Name State
 ----------------------------------------------------
  - guest shut off
</code></pre>
<font SIZE="-1"></font><h3>ESXi: COPY THE GUEST TO THE LOCAL MACHINE</h3>
<p> Using the libvirt <font SIZE="-1">URI</font> as the <i>-ic</i> option, copy one of the guests to the local machine: </p>
<pre><code> $ virt-v2v-copy-to-local -icesx://root@esxi.example.com?no_verify=1 guest
</code></pre>
<p> This creates <i>guest.xml</i>, <i>guest-disk1</i>, ...  </p>
<font SIZE="-1"></font><h3>ESXi: DO THE VIRT-V2V CONVERSION</h3>
<p> Perform the conversion of the guest using virt-v2v: </p>
<pre><code> $ virt-v2v -i libvirtxml guest.xml -o local -os /var/tmp
</code></pre>
<font SIZE="-1"></font><h3>ESXi: CLEAN UP</h3>
<p> Remove the <i>guest.xml</i> and <i>guest-disk*</i> files.  </p>
<h2>INPUT FROM RHEL 5 XEN</h2>
<p> Virt-v2v is able to import Xen guests from <font SIZE="-1">RHEL 5</font> Xen hosts. </p>
<p> Virt-v2v uses libvirt for access to the remote Xen host, and therefore the input mode should be <i>-i libvirt</i>. As this is the default, you don&#8217;t need to specify it on the command line.  </p>
<font SIZE="-1"></font><font SIZE="-1"></font><h3>XEN: SET UP SSH-AGENT ACCESS TO XEN HOST</h3>
<p> Currently you must enable passwordless <font SIZE="-1">SSH</font> access to the remote Xen host from the virt-v2v conversion server. </p>
<p> You must also use ssh-agent, and add your ssh public key to <i>/root/.ssh/authorized_keys</i> (on the Xen host). </p>
<p> After doing this, you should check that passwordless access works from the virt-v2v server to the Xen host. For example: </p>
<pre><code> $ ssh root [at] xen.example.com
 [ logs straight into the shell, no password is requested ]
</code></pre>
<p> Note that password-interactive and Kerberos access are <code>not</code> supported. You <code>have</code> to set up ssh access using ssh-agent and authorized_keys.  </p>
<font SIZE="-1"></font><h3>XEN: TEST LIBVIRT CONNECTION TO REMOTE XEN HOST</h3>
<p> Use the <i><a href="/docs/linux/man/1-virsh/">virsh</a></i>(1) command to list the guests on the remote Xen host: </p>
<pre><code> $ virsh -c xen+ssh://root@xen.example.com list --all
  Id Name State
 ----------------------------------------------------
  0 Domain-0 running
  - rhel49-x86_64-pv shut off
</code></pre>
<p> You should also try dumping the metadata from any guest on your server, like this: </p>
<pre><code> $ virsh -c xen+ssh://root@xen.example.com dumpxml rhel49-x86_64-pv
 &lt;domain type='xen'&gt;
   &lt;name&gt;rhel49-x86_64-pv&lt;/name&gt;
   [...]
 &lt;/domain&gt;
</code></pre>
<p> <code>If the above commands do not work, then virt-v2v is not going to work either</code>. Fix your libvirt configuration or the remote server before continuing. </p>
<p> <code>If the guest disks are located on a host block device</code>, then the conversion will fail. See ``<font SIZE="-1">XEN OR SSH CONVERSIONS FROM BLOCK DEVICES&#8217;&#8216;</font> below for a workaround.  </p>
<font SIZE="-1"></font><h3>XEN: IMPORTING A GUEST</h3>
<p> To import a particular guest from a Xen server, do: </p>
<pre><code> $ virt-v2v -ic 'xen+ssh://root@xen.example.com' \
   rhel49-x86_64-pv \
   -o local -os /var/tmp
</code></pre>
<p> where <code>&quot;rhel49-x86_64-pv&quot;</code> is the name of the guest (which must be shut down). </p>
<p> In this case the output flags are set to write the converted guest to a temporary directory as this is just an example, but you can also write to libvirt or any other supported target.  </p>
<font SIZE="-1"></font><h3>XEN OR SSH CONVERSIONS FROM BLOCK DEVICES</h3>
<p> Currently virt-v2v cannot directly access a Xen guest (or any guest located remotely over ssh) if that guest&#8217;s disks are located on host block devices. </p>
<p> To tell if a Xen guest uses host block devices, look at the guest <font SIZE="-1">XML.</font> You will see: </p>
<pre><code>  &lt;disk type='block' device='disk'&gt;
    ...
    &lt;source dev='/dev/VG/guest'/&gt;
</code></pre>
<p> where <code>&quot;type=&#8216;block&#8217;&quot;</code>, <code>&quot;source dev=&quot;</code> and <code>&quot;/dev/...&quot;</code> are all indications that the disk is located on a host block device. </p>
<p> This happens because the qemu ssh block driver that we use to access remote disks uses the ssh sftp protocol, and this protocol cannot correctly detect the size of host block devices. </p>
<p> The workaround is to copy the guest over to the conversion server, using the separate <i><a href="/docs/linux/man/1-virt-v2v-copy-to-local/">virt-v2v-copy-to-local</a></i>(1) tool, followed by running virt-v2v. You will need sufficient space on the conversion server to store a full copy of the guest. </p>
<pre><code> virt-v2v-copy-to-local -ic xen+ssh://root@xen.example.com guest
 virt-v2v -i libvirtxml guest.xml -o local -os /var/tmp
 rm guest.xml guest-disk*
</code></pre>
<h2>OUTPUT TO LIBVIRT</h2>
<p> The <i>-o libvirt</i> option lets you upload the converted guest to a libvirt-managed host. There are several limitations: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> You can only use a local libvirt connection [see below for how to workaround this]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <i>-os pool</i> option must specify a directory pool, not anything more exotic such as iSCSI [but see below]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> You can only upload to a <font SIZE="-1">KVM</font> hypervisor. </p>
 </dd></dl>
<p> <code>To output to a remote libvirt instance and/or a non-directory storage pool</code> you have to use the following workaround: </p>
<dl>
<dt>1.</dt>
<dd> <p> Use virt-v2v in <i>-o local</i> mode to convert the guest disks and metadata into a local temporary directory: </p>
<pre><code> virt-v2v [...] -o local -os /var/tmp
</code></pre>
<p> This creates two (or more) files in <i>/var/tmp</i> called: </p>
<pre><code> /var/tmp/NAME.xml # the libvirt XML (metadata)
 /var/tmp/NAME-sda # the guest's first disk
</code></pre>
<p> (for <code>&quot;NAME&quot;</code> substitute the guest&#8217;s name). </p>
 </dd>
<dt>2.</dt>
<dd> <p> Upload the converted disk(s) into the storage pool called <code>&quot;POOL&quot;</code>: </p>
<pre><code> size=$(stat -c%s /var/tmp/NAME-sda)
 virsh vol-create-as POOL NAME-sda $size --format raw
 virsh vol-upload --pool POOL NAME-sda /var/tmp/NAME-sda
</code></pre>
 </dd>
<dt>3.</dt>
<dd> <p> Edit <i>/var/tmp/NAME.xml</i> to change <i>/var/tmp/NAME-sda</i> to the pool name. In other words, locate the following bit of <font SIZE="-1">XML:</font> </p>
<pre><code> &lt;disk type='file' device='disk'&gt;
   &lt;driver name='qemu' type='raw' cache='none' /&gt;
   &lt;source file='/var/tmp/NAME-sda' /&gt;
   &lt;target dev='hda' bus='ide' /&gt;
 &lt;/disk&gt;
</code></pre>
<p> and change two things: The <code>&quot;type=&#8216;file&#8217;&quot;</code> attribute must be changed to <code>&quot;type=&#8216;volume&#8217;&quot;</code>, and the <code>&quot;&lt;source&gt;&quot;</code> element must be changed to include <code>&quot;pool&quot;</code> and <code>&quot;volume&quot;</code> attributes: </p>
<pre><code> &lt;disk type='volume' device='disk'&gt;
   ...
   &lt;source pool='POOL' volume='NAME-sda' /&gt;
   ...
 &lt;/disk&gt;
</code></pre>
 </dd>
<dt>4.</dt>
<dd> <p> Define the final guest in libvirt: </p>
<pre><code> virsh define /var/tmp/NAME.xml
</code></pre>
 </dd></dl>
<h2>OUTPUT TO RHEV</h2>
<p> This section only applies to the <i>-o rhev</i> output mode. If you use virt-v2v from the RHEV-M user interface, then behind the scenes the import is managed by <font SIZE="-1">VDSM</font> using the <i>-o vdsm</i> output mode (which end users should not try to use directly). </p>
<p> You have to specify <i>-o rhev</i> and an <i>-os</i> option that points to the RHEV-M Export Storage Domain. You can either specify the <font SIZE="-1">NFS</font> server and mountpoint, eg. <code>&quot;-os rhev-storage:/rhev/export&quot;</code>, or you can mount that first and point to the directory where it is mounted, eg. <code>&quot;-os /tmp/mnt&quot;</code>. Be careful not to point to the Data Storage Domain by accident as that will not work. </p>
<p> On successful completion virt-v2v will have written the new guest to the Export Storage Domain, but it will not yet be ready to run. It must be imported into <font SIZE="-1">RHEV</font> using the <font SIZE="-1">UI</font> before it can be used. </p>
<p> In <font SIZE="-1">RHEV</font> ≥ 2.2 this is done from the Storage tab. Select the export domain the guest was written to. A pane will appear underneath the storage domain list displaying several tabs, one of which is ``<font SIZE="-1">VM</font> Import&#8217;&#8216;. The converted guest will be listed here. Select the appropriate guest an click ``Import&#8217;&#8216;. See the <font SIZE="-1">RHEV</font> documentation for additional details. </p>
<p> If you export several guests, then you can import them all at the same time through the <font SIZE="-1">UI.</font>  </p>
<h2>OUTPUT TO GLANCE</h2>
<p> To output to OpenStack Glance, use the <i>-o glance</i> option. </p>
<p> This runs the <i><a href="/docs/linux/man/1-glance/">glance</a></i>(1) <font SIZE="-1">CLI</font> program which must be installed on the virt-v2v conversion host. For authentication to work, you will need to set <code>&quot;OS_*&quot;</code> environment variables. In most cases you can do this by sourcing a file called something like <i>keystonerc_admin</i>. </p>
<p> Virt-v2v adds metadata for the guest to Glance, describing such things as the guest operating system and what drivers it requires. The command <code>&quot;glance image-show&quot;</code> will display the metadata as ``Property&#8217;&#8216; fields such as <code>&quot;os_type&quot;</code> and <code>&quot;hw_disk_bus&quot;</code>.  </p>
<h3>Glance and sparseness</h3>
<p> Glance image upload doesn&#8217;t appear to correctly handle sparseness. For this reason, using qcow2 will be faster and use less space on the Glance server. Use the virt-v2v <i>-of qcow2</i> option.  </p>
<h3>Glance and multiple disks</h3>
<p> If the guest has a single disk, then the name of the disk in Glance will be the name of the guest. You can control this using the <i>-on</i> option. </p>
<p> Glance doesn&#8217;t have a concept of associating multiple disks with a single guest, and Nova doesn&#8217;t allow you to boot a guest from multiple Glance disks either. If the guest has multiple disks, then the first (assumed to be the system disk) will have the name of the guest, and the second and subsequent data disks will be called <code>&quot;</code>guestname <code>-disk2&quot;</code>, <code>&quot;</code>guestname <code>-disk3&quot;</code> etc. It may be best to leave the system disk in Glance, and import the data disks to Cinder (see next section).  </p>
<h3>Importing disks into Cinder</h3>
<p> Since most virt-v2v guests are ``pets&#8217;&#8216;, Glance is perhaps not the best place to store them. There is no way for virt-v2v to upload directly to Cinder (<a rel="nofollow" href="https://bugzilla.redhat.com/1155229">https://bugzilla.redhat.com/1155229</a>). There are two ways to upload to Cinder: </p>
<dl>
<dt>1.</dt>
<dd> <p> Import the image to Glance first (ie. <i>-o glance</i>) and then copy it to Cinder: </p>
<pre><code> cinder create --image-id &lt;GLANCE-IMAGE-UUID&gt; &lt;SIZE&gt;
</code></pre>
 </dd>
<dt>2.</dt>
<dd> <p> Create (through some other means) a new volume / <font SIZE="-1">LUN</font> in your Cinder backing store. Migrate the guest to this volume (using <i>-o local</i>). Then ask Cinder to take over management of the volume using: </p>
<pre><code> cinder manage &lt;VOLUMEREF&gt;
</code></pre>
 </dd></dl>
<h2>RESOURCE REQUIREMENTS</h2>
<h3>Network</h3>
<p> The most important resource for virt-v2v appears to be network bandwidth. Virt-v2v should be able to copy guest data at gigabit ethernet speeds or greater. </p>
<p> Ensure that the network connections between servers (conversion server, <font SIZE="-1">NFS</font> server, vCenter, Xen) are as fast and as low latency as possible.  </p>
<h3>Disk space</h3>
<p> Virt-v2v places potentially large temporary files in <code>$TMPDIR</code> (which is <i>/var/tmp</i> if you don&#8217;t set it). Using tmpfs is a bad idea. </p>
<p> For each guest disk, an overlay is stored temporarily. This stores the changes made during conversion, and is used as a cache. The overlays are not particularly large &#8211; tens or low hundreds of megabytes per disk is typical. In addition to the overlay(s), input and output methods may use disk space, as outlined in the table below. </p>
<dl>
<dt><i>-i ova</i></dt>
<dd> <p> This temporarily places a full copy of the uncompressed source disks in <code>$TMPDIR</code>. </p>
 </dd>
<dt><i>-o glance</i></dt>
<dd> <p> This temporarily places a full copy of the output disks in <code>$TMPDIR</code>. </p>
 </dd>
<dt><i>-o local</i></dt>
<dd>  </dd>
<dt><i>-o qemu</i></dt>
<dd> <p> You must ensure there is sufficient space in the output directory for the converted guest. </p>
 </dd>
<dt><i>-o null</i></dt>
<dd> <p> This temporarily places a full copy of the output disks in <code>$TMPDIR</code>. </p>
 </dd></dl>
<p> See also ``Minimum free space check in the host&#8217;&#8216; below.  </p>
<h3>VMware vCenter resources</h3>
<p> Copying from VMware vCenter is currently quite slow, but we believe this to be an issue with VMware. Ensuring the VMware ESXi hypervisor and vCenter are running on fast hardware with plenty of memory should alleviate this.  </p>
<font SIZE="-1"></font><h3>Compute power and RAM</h3>
<p> Virt-v2v is not especially compute or <font SIZE="-1">RAM</font> intensive. If you are running many parallel conversions, then you may consider allocating one <font SIZE="-1">CPU</font> core and between 512 <font SIZE="-1">MB</font> and 1 <font SIZE="-1">GB</font> of <font SIZE="-1">RAM</font> per running instance. </p>
<p> Virt-v2v can be run in a virtual machine.  </p>
<h3>Trimming</h3>
<p> Virt-v2v attempts to optimize the speed of conversion by ignoring guest filesystem data which is not used. This would include unused filesystem blocks, blocks containing zeroes, and deleted files. </p>
<p> To do this, virt-v2v issues a non-destructive <i><a href="/docs/linux/man/8-fstrim/">fstrim</a></i>(8) operation. As this happens to an overlay placed over the guest data, it does <code>not</code> affect the source in any way. </p>
<p> If this fstrim operation fails, you will see a warning, but virt-v2v will continue anyway. It may run more slowly (in some cases much more slowly), because it is copying the unused parts of the disk. </p>
<p> Unfortunately support for fstrim is not universal, and it also depends on specific details of the filesystem, partition alignment, and backing storage. As an example, <font SIZE="-1">NTFS</font> filesystems cannot be fstrimmed if they occupy a partition which is not aligned to the underlying storage. That was the default on Windows before Vista. As another example, <font SIZE="-1">VFAT</font> filesystems (used by <font SIZE="-1">UEFI</font> guests) cannot be trimmed at all. </p>
<p> fstrim support in the Linux kernel is improving gradually, so over time some of these restrictions will be lifted and virt-v2v will work faster.  </p>
<h2>POST-CONVERSION TASKS</h2>
<h3>Guest network configuration</h3>
<p> Virt-v2v cannot currently reconfigure a guest&#8217;s network configuration. If the converted guest is not connected to the same subnet as the source, its network configuration may have to be updated. See also <i><a href="/docs/linux/man/1-virt-customize/">virt-customize</a></i>(1).  </p>
<h3>Converting a Windows guest</h3>
<p> When converting a Windows guests, the conversion process is split into two stages: </p>
<dl>
<dt>1.</dt>
<dd> <p> Offline conversion. </p>
 </dd>
<dt>2.</dt>
<dd> <p> First boot. </p>
 </dd></dl>
<p> The guest will be bootable after the offline conversion stage, but will not yet have all necessary drivers installed to work correctly. These will be installed automatically the first time the guest boots. </p>
<p> <code>N.B.</code> Take care not to interrupt the automatic driver installation process when logging in to the guest for the first time, as this may prevent the guest from subsequently booting correctly.  </p>
<h2>FREE SPACE FOR CONVERSION</h2>
<h3>Free space in the guest</h3>
<p> Virt-v2v checks there is sufficient free space in the guest filesystem to perform the conversion. Currently it checks: </p>
<dl>
<dt>Linux root filesystem or Windows &quot;C:&quot; drive</dt>
<dd> <p> Minimum free space: 20 <font SIZE="-1">MB</font> </p>
 </dd>
<dt>Linux <i>/boot</i></dt>
<dd> <p> Minimum free space: 50 <font SIZE="-1">MB</font> </p>
<p> This is because we need to build a new initramfs for some Enterprise Linux conversions. </p>
 </dd>
<dt>Any other mountable filesystem</dt>
<dd> <p> Minimum free space: 10 <font SIZE="-1">MB</font> </p>
 </dd></dl>
<h3>Minimum free space check in the host</h3>
<p> You must have sufficient free space in the host directory used to store temporary overlays (except in <i>--in-place</i> mode). To find out which directory this is, use: </p>
<pre><code> $ df -h &quot;`guestfish get-cachedir`&quot;
 Filesystem Size Used Avail Use% Mounted on
 /dev/mapper/root 50G 40G 6.8G 86% /
</code></pre>
<p> and look under the <code>&quot;Avail&quot;</code> column. Virt-v2v will refuse to do the conversion at all unless at least 1GB is available there. </p>
<p> See also ``<font SIZE="-1">RESOURCE REQUIREMENTS&#8217;&#8216;</font> above.  </p>
<h2>RUNNING VIRT-V2V AS ROOT OR NON-ROOT</h2>
<p> Nothing in virt-v2v inherently needs root access, and it will run just fine as a non-root user. However, certain external features may require either root or a special user: </p>
<dl>
<dt>Mounting the Export Storage Domain</dt>
<dd> <p> When using <i>-o rhev -os server:/esd</i> virt-v2v has to have sufficient privileges to <font SIZE="-1">NFS</font> mount the Export Storage Domain from <code>&quot;server&quot;</code>. </p>
<p> You can avoid needing root here by mounting it yourself before running virt-v2v, and passing <i>-os /mountpoint</i> instead, but first of all read the next section ... </p>
 </dd>
<dt>Writing to the Export Storage Domain as 36:36</dt>
<dd> <p> RHEV-M cannot read files and directories from the Export Storage Domain unless they have <font SIZE="-1">UID:GID 36:36. </font> You will see <font SIZE="-1">VM</font> import problems if the <font SIZE="-1">UID:GID</font> is not correct. </p>
<p> When you run virt-v2v <i>-o rhev</i> as root, virt-v2v attempts to create files and directories with the correct ownership. If you run virt-v2v as non-root, it will probably still work, but you will need to manually change ownership after virt-v2v has finished. </p>
 </dd>
<dt>Writing to libvirt</dt>
<dd> <p> When using <i>-o libvirt</i>, you may need to run virt-v2v as root so that it can write to the libvirt system instance (ie. <code>&quot;<a href="qemu:///system">qemu:///system</a>&quot;</code>) and to the default location for disk images (usually <i>/var/lib/libvirt/images</i>). </p>
<p> You can avoid this by setting up libvirt connection authentication, see <a rel="nofollow" href="http://libvirt.org/auth.html.">http://libvirt.org/auth.html.</a> Alternatively, use <i>-oc <a href="qemu:///session">qemu:///session</a></i>, which will write to your per-user libvirt instance. </p>
 </dd>
<dt>Writing to Glance</dt>
<dd> <p> This does <i>not</i> need root (in fact it probably won&#8217;t work), but may require either a special user and/or for you to source a script that sets authentication environment variables. Consult the Glance documentation. </p>
 </dd></dl>
<h2>DEBUGGING RHEV-M IMPORT FAILURES</h2>
<p> When you export to the RHEV-M Export Storage Domain, and then import that guest through the RHEV-M <font SIZE="-1">UI,</font> you may encounter an import failure. Diagnosing these failures is infuriatingly difficult as the <font SIZE="-1">UI</font> generally hides the true reason for the failure. </p>
<p> There are two log files of interest. The first is stored on the RHEV-M server itself, and is called <i>/var/log/ovirt-engine/engine.log</i> </p>
<p> The second file, which is the most useful, is found on the <font SIZE="-1">SPM</font> host (<font SIZE="-1">SPM</font> stands for ``Storage Pool Manager&#8217;&#8216;). This is a <font SIZE="-1">RHEV</font> node that is elected to do all metadata modifications in the data center, such as image or snapshot creation. You can find out which host is the current <font SIZE="-1">SPM</font> from the ``Hosts&#8217;&#8216; tab ``Spm Status&#8217;&#8216; column. Once you have located the <font SIZE="-1">SPM,</font> log into it and grab the file <i>/var/log/vdsm/vdsm.log</i> which will contain detailed error messages from low-level commands.  </p>
<h2>MINIMAL XML FOR -i libvirtxml OPTION</h2>
<p> When using the <i>-i libvirtxml</i> option, you have to supply some libvirt <font SIZE="-1">XML. </font> Writing this from scratch is hard, so the template below is helpful. </p>
<p> <code>Note this should only be used for testing and/or where you know what you&#8217;re doing!</code> If you have libvirt metadata for the guest, always use that instead. </p>
<pre><code> &lt;domain type='kvm'&gt;
   &lt;name&gt;NAME&lt;/name&gt;
   &lt;memory&gt;1048576&lt;/memory&gt;
   &lt;vcpu&gt;2&lt;/vcpu&gt;
   &lt;os&gt;
     &lt;type&gt;hvm&lt;/type&gt;
     &lt;boot dev='hd'/&gt;
   &lt;/os&gt;
   &lt;features&gt;
     &lt;acpi/&gt;
     &lt;apic/&gt;
     &lt;pae/&gt;
   &lt;/features&gt;
   &lt;devices&gt;
     &lt;disk type='file' device='disk'&gt;
       &lt;driver name='qemu' type='raw'/&gt;
       &lt;source file='/path/to/disk/image'/&gt;
       &lt;target dev='hda' bus='ide'/&gt;
     &lt;/disk&gt;
     &lt;interface type='network'&gt;
       &lt;mac address='52:54:00:01:02:03'/&gt;
       &lt;source network='default'/&gt;
       &lt;model type='rtl8139'/&gt;
     &lt;/interface&gt;
   &lt;/devices&gt;
 &lt;/domain&gt;
</code></pre>
<h2>MACHINE READABLE OUTPUT</h2>
<p> The <i>--machine-readable</i> option can be used to make the output more machine friendly, which is useful when calling virt-v2v from other programs, GUIs etc. </p>
<p> There are two ways to use this option. </p>
<p> Firstly use the option on its own to query the capabilities of the virt-v2v binary. Typical output looks like this: </p>
<pre><code> $ virt-v2v --machine-readable
 virt-v2v
 libguestfs-rewrite
 input:disk
 [...]
 output:local
 [...]
 convert:enterprise-linux
 convert:windows
</code></pre>
<p> A list of features is printed, one per line, and the program exits with status 0. </p>
<p> The <code>&quot;input:&quot;</code> and <code>&quot;output:&quot;</code> features refer to <i>-i</i> and <i>-o</i> (input and output mode) options supported by this binary. The <code>&quot;convert:&quot;</code> features refer to guest types that this binary knows how to convert. </p>
<p> Secondly use the option in conjunction with other options to make the regular program output more machine friendly. </p>
<p> At the moment this means: </p>
<dl>
<dt>1.</dt>
<dd> <p> Progress bar messages can be parsed from stdout by looking for this regular expression: </p>
<pre><code> ^[0-9]+/[0-9]+$
</code></pre>
 </dd>
<dt>2.</dt>
<dd> <p> The calling program should treat messages sent to stdout (except for progress bar messages) as status messages. They can be logged and/or displayed to the user. </p>
 </dd>
<dt>3.</dt>
<dd> <p> The calling program should treat messages sent to stderr as error messages. In addition, virt-v2v exits with a non-zero status code if there was a fatal error. </p>
 </dd></dl>
<p> Virt-v2v ≤ 0.9.1 did not support the <i>--machine-readable</i> option at all. The option was added when virt-v2v was rewritten in 2014.  </p>
<h2>FILES</h2>
<dl>
<dt><i>/usr/share/virtio-win</i></dt>
<dd> <p> (Optional) </p>
<p> If this directory is present, then virtio drivers for Windows guests will be found from this directory and installed in the guest during conversion. </p>
 </dd></dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt>&quot;TMPDIR&quot;</dt>
<dd> <p> Location of the temporary directory used for the potentially large temporary overlay file. </p>
<p> See the ``Disk space&#8217;&#8216; section above. </p>
 </dd>
<dt>&quot;VIRT_TOOLS_DATA_DIR&quot;</dt>
<dd> <p> This can point to the directory containing data files used for Windows conversion. </p>
<p> Normally you do not need to set this. If not set, a compiled-in default will be used (something like <i>/usr/share/virt-tools</i>). </p>
<p> This directory may contain the following files: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><i>rhsrvany.exe</i></dt>
<dd> <p> (Required when doing conversions of Windows guests) </p>
<p> This is the RHSrvAny Windows binary, used to install a ``firstboot&#8217;&#8216; script in the guest during conversion of Windows guests. </p>
<p> See also: <code>&quot;<a rel="nofollow" href="https://github.com/rwmjones/rhsrvany">https://github.com/rwmjones/rhsrvany</a>&quot;</code> </p>
 </dd>
<dt><i>rhev-apt.exe</i></dt>
<dd> <p> (Optional) </p>
<p> The <font SIZE="-1">RHEV</font> Application Provisioning Tool (<font SIZE="-1">RHEV APT</font>). If this file is present, then <font SIZE="-1">RHEV APT</font> will be installed in the Windows guest during conversion. This tool is a guest agent which ensures that the virtio drivers remain up to date when the guest is running on Red Hat Enterprise Virtualization (<font SIZE="-1">RHEV</font>). </p>
<p> This file comes from Red Hat Enterprise Virtualization (<font SIZE="-1">RHEV</font>), and is not distributed with virt-v2v. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>&quot;VIRTIO_WIN&quot;</dt>
<dd> <p> This is where VirtIO drivers for Windows are searched for (<i>/usr/share/virtio-win</i> if unset). It can be a directory <i>or</i> point to <i>virtio-win.iso</i> (<font SIZE="-1">CD ROM</font> image containing drivers). </p>
<p> See ``<font SIZE="-1">ENABLING VIRTIO&#8217;&#8216;</font>. </p>
 </dd></dl>
<p> For other environment variables, see ``<font SIZE="-1">ENVIRONMENT VARIABLES&#8217;&#8216;</font> in <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3).  </p>
<h2>OTHER TOOLS</h2>
<dl>
<dt><i><a href="/docs/linux/man/1-virt-v2v-copy-to-local/">virt-v2v-copy-to-local</a></i>(1)</dt>
<dd> <p> There are some special cases where virt-v2v cannot directly access the remote hypervisor. In that case you have to use <i><a href="/docs/linux/man/1-virt-v2v-copy-to-local/">virt-v2v-copy-to-local</a></i>(1) to make a local copy of the guest first, followed by running <code>&quot;virt-v2v -i libvirtxml&quot;</code> to perform the conversion. </p>
 </dd>
<dt><i><a href="/docs/linux/man/8-engine-image-uploader/">engine-image-uploader</a></i>(8)</dt>
<dd> <p> Variously called <code>&quot;engine-image-uploader&quot;</code>, <code>&quot;ovirt-image-uploader&quot;</code> or <code>&quot;rhevm-image-uploader&quot;</code>, this tool allows you to copy a guest from one oVirt or <font SIZE="-1">RHEV</font> Export Storage Domain to another. It only permits importing a guest that was previously exported from another oVirt/RHEV instance. </p>
 </dd>
<dt>import-to-ovirt.pl</dt>
<dd> <p> This script can be used to import guests that already run on <font SIZE="-1">KVM</font> to oVirt or <font SIZE="-1">RHEV. </font> For more information, see this blog posting by the author of virt-v2v: </p>
<p> <a rel="nofollow" href="https://rwmj.wordpress.com/2015/09/18/importing-kvm-guests-to-ovirt-or-rhev/#content">https://rwmj.wordpress.com/2015/09/18/importing-kvm-guests-to-ovirt-or-rhev/#content</a> </p>
 </dd></dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-virt-p2v/">virt-p2v</a></i>(1), <i><a href="/docs/linux/man/1-virt-customize/">virt-customize</a></i>(1), <i><a href="/docs/linux/man/1-virt-df/">virt-df</a></i>(1), <i><a href="/docs/linux/man/1-virt-filesystems/">virt-filesystems</a></i>(1), <i><a href="/docs/linux/man/1-virt-sparsify/">virt-sparsify</a></i>(1), <i><a href="/docs/linux/man/1-virt-sysprep/">virt-sysprep</a></i>(1), <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3), <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1), <i><a href="/docs/linux/man/1-qemu-img/">qemu-img</a></i>(1), <i><a href="/docs/linux/man/8-fstrim/">fstrim</a></i>(8), <i><a href="/docs/linux/man/1-virt-v2v-copy-to-local/">virt-v2v-copy-to-local</a></i>(1), <i><a href="/docs/linux/man/1-virt-v2v-test-harness/">virt-v2v-test-harness</a></i>(1), <i><a href="/docs/linux/man/8-engine-image-uploader/">engine-image-uploader</a></i>(8), import-to-ovirt.pl, <a rel="nofollow" href="http://libguestfs.org/.">http://libguestfs.org/.</a>  </p>
<h2>AUTHORS</h2>
<p> Richard W.M. Jones <a rel="nofollow" href="http://people.redhat.com/~rjones/">http://people.redhat.com/~rjones/</a> </p>
<p> Matthew Booth </p>
<p> Mike Latimer </p>
<p> Pino Toscano </p>
<p> Shahar Havivi </p>
<p> Tingting Zheng  </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2009-2016 Red Hat Inc.  </p>
<h2>LICENSE</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, <font SIZE="-1">MA 02110-1301 USA.</font>  </p>
<h2>BUGS</h2>
<p> To get a list of bugs against libguestfs, use this link: <a rel="nofollow" href="https://bugzilla.redhat.com/buglist.cgi?component=libguestfs">https://bugzilla.redhat.com/buglist.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools </p>
<p> To report a new bug against libguestfs, use this link: <a rel="nofollow" href="https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs">https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools </p>
<p> When reporting a bug, please supply: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The version of libguestfs. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Where you got libguestfs (eg. which Linux distro, compiled from source, etc) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Describe the bug accurately and give a way to reproduce it. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Run <i><a href="/docs/linux/man/1-libguestfs-test-tool/">libguestfs-test-tool</a></i>(1) and paste the <code>complete, unedited</code> output into the bug report. </p>
 </dd></dl>
