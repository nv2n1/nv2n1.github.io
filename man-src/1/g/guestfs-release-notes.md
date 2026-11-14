---
title: "guestfs-release-notes(1)"
name: "guestfs-release-notes"
section: "1"
letter: "g"
url: "/docs/linux/man/1-guestfs-release-notes/"
description: "guestfs-release-notes – libguestfs Release Notes"
---

<h2 class="name">NAME</h2>
<p> guestfs-release-notes &#8211; libguestfs Release Notes </p>
<h2>RELEASE NOTES FOR LIBGUESTFS 1.40</h2>
<p> These release notes only cover the differences from the previous stable/dev branch split (1.38.0). For detailed changelogs, please see the git repository, or the ChangeLog file distributed in the tarball.</p>
<h3>New features</h3>
<p> <i>New features in existing tools</i> </p>
<p> Virt-inspector now displays the libosinfo short <font SIZE="-1">ID</font> for guests (Pino Toscano). </p>
<p> Guestfish <i>-N</i> will now generate 1G disks instead of 100M disks by default. </p>
<p> Virt-resize supports f2fs filesystems (Pino Toscano). </p>
<p> libguestfs-test-tool now supports bash tab completion (Pino Toscano). </p>
<p> The <i>&#8211;machine-readable</i> option now supports sending output to files or stdout/stderr. This works uniformly across most OCaml-based virt tools, specifically: virt-builder, virt-builder-repository, virt-dib, virt-get-kernel, virt-resize, virt-sparsify, and virt-v2v (Pino Toscano). </p>
<p> Virt-builder <i>&#8211;uninstall</i> option now works on <font SIZE="-1">SUSE</font> (Sebastian Meyer). </p>
<p> Virt-builder now supports Windows. We are not able to ship Windows templates in the public respository for obvious licensing reasons, but if you are an <font SIZE="-1">MSDN</font> subscriber you may build your own. See <a rel="nofollow" href="https://rwmj.wordpress.com/2018/09/13/creating-windows-templates-for-virt-builder/">https://rwmj.wordpress.com/2018/09/13/creating-windows-templates-for-virt-builder/</a> </p>
<p> Many tools now support a <i>&#8211;key</i> option allowing you to pass in decryption keys for filesystems stored in local files on the host rather than having to feed them in over stdin (Pino Toscano). </p>
<p> <i>virt-v2v and virt-p2v</i> </p>
<p> New <i>-o rhv-upload</i> mode for directly uploading images to <font SIZE="-1">RHV,</font> bypassing the Export Storage Domain (Tomáš Golembiovský, Nir Soffer, Daniel Erez, Pino Toscano). </p>
<p> New <i>-o openstack</i> mode for directly uploading images to OpenStack and Cinder using OpenStack APIs. </p>
<p> Virt-v2v now has a general mechanism for input and output options: <i>-io</i> and <i>-oo</i>. </p>
<p> Virt-v2v can now install the <font SIZE="-1">RHV</font> tools or <font SIZE="-1">QEMU GA</font> in guests (Tomáš Golembiovský). </p>
<p> The huge manual has now been split into several smaller documents and is more focused on helping users to accomplish specific v2v tasks. </p>
<p> Multiple improvements to the <font SIZE="-1">OVF</font> metadata when converting to <font SIZE="-1">RHV</font> (Tomáš Golembiovský, Pino Toscano, Arik Hadas). </p>
<p> Virt-v2v can now convert Linux guests with split kernel packages, especially Ubuntu 18.04 (Pino Toscano). </p>
<p> Virt-v2v old <i>&#8211;password-file</i> option has been replaced by <i>-ip</i> (the old option remains for backwards compatibility). </p>
<p> Virt-v2v now preserves the <font SIZE="-1">VM</font> Generation <font SIZE="-1">ID.</font> </p>
<p> Virt-v2v has a new <i>&#8211;mac</i> option allowing specific NICs to be mapped precisely to networks or bridges on the target. </p>
<p> New virt-v2v <i>&#8211;print-estimate</i> option to estimate the size of data that virt-v2v will copy. </p>
<p> Virt-v2v is now usually able to remove open-vm-tools and VMware Tools from the Linux guest during conversion (Pino Toscano). </p>
<p> Virt-v2v can now support <font SIZE="-1">UEFI</font> conversions to <font SIZE="-1">RHV</font> (Tomáš Golembiovský). </p>
<p> Virt-p2v now prefers you to shut down instead of rebooting the machine after conversion has finished (Pino Toscano). </p>
<p> Virt-v2v now writes the libosinfo short <font SIZE="-1">ID</font> to the libvirt metadata when using <i>-o local</i> and <i>-o libvirt</i> output modes (Martin Kletzander). </p>
<p> <i>Language bindings</i> </p>
<p> OpenJDK 10+ is supported (Pino Toscano). </p>
<p> Java bindings fixed for Gentoo host (Martin Kletzander). </p>
<p> <i>Inspection</i> </p>
<p> Support Kali Linux (Pino Toscano). </p>
<p> When inspecting mountpoints, look for <i>/etc/mdadm/mdadm.conf</i> as well as <i>/etc/mdadm.conf</i> (Nikolay Ivanets). </p>
<p> Improved support for OpenSUSE Tumbleweed (Pino Toscano). </p>
<p> <i>Architectures and platforms</i> </p>
<p> Miscellaneous macOS build fixes (Adam Robinson). </p>
<p> <i>Other</i> </p>
<p> Multiple documentation typos fixed (Yuri Chornoivan).</p>
<h3>Security</h3>
<p> See also <code><a href="/docs/linux/man/1-guestfs-security/">guestfs-security</a></code>(1). </p>
<p> <i></i><font SIZE="-1"><i>CVE-2018-11806</i></font><i></i> </p>
<p> Qemu&#8217;s slirp (userspace networking) had several buffer overflows which could be triggered from the guest or network side.</p>
<h3><font SIZE="-1">API</font></h3>
<p> <i>New APIs</i></p>
<dl>
<dt>&quot;f2fs_expand&quot;</p>
<dd> Expand an f2fs filesystem (Pino Toscano).</p>
<dt>&quot;inspect_get_osinfo&quot;</p>
<dd> Get the libosinfo short <font SIZE="-1">ID</font> for the inspected guest (Pino Toscano).</p>
<dt>&quot;lvm_scan&quot;</p>
<dd> This rescans all PVs, VGs and LVs, optionally activating them.</dl>
<p> <i>Other </i><font SIZE="-1"><i>API</i></font><i> changes</i> </p>
<p> <tt>&quot;part_get_mbr_part_type&quot;</tt> was reimplemented in OCaml (Nikolay Ivanets). </p>
<p> <tt>&quot;list_filesystems&quot;</tt> now filters out <font SIZE="-1">MBR</font> extended partitions (Nikolay Ivanets). </p>
<p> <tt>&quot;vgscan&quot;</tt> has been deprecated. Use the new <tt>&quot;lvm_scan&quot;</tt> <font SIZE="-1">API</font> in preference.</p>
<h3>Build changes</h3>
<p> The <font SIZE="-1">JSON</font> library switched from yajl to Jansson ≥ 2.7 (Pino Toscano). </p>
<p> Support for The Sleuth Kit 4.5 (Pino Toscano). </p>
<p> Multiple improvements in the <tt>&quot;./configure&quot;</tt> script (Lin Ma). </p>
<p> More out-of-tree build fixes (Hilko Bengen). </p>
<p> Some work on reproducible builds (Bernhard M. Wiedemann).</p>
<h3>Internals</h3>
<p> lvmetad is now used unconditionally, and is started much earlier in the appliance boot process. This fixes support for certain <font SIZE="-1">PV</font> types. </p>
<p> On Debian, dash is installed inside the appliance and in virt-rescue (Pino Toscano). </p>
<p> The amount of <font SIZE="-1">RAM</font> assigned to the appliance has been increased from 500M to 768M (on x86_64, other architectures have different limits). This enables use of up to 255 disks when using recent Linux kernels. </p>
<p> Virt-v2v now models the source machine type (eg. i440FX, Q35 or virt). </p>
<p> Virt-p2v now generates configuration code automatically, also code for parsing the kernel command line. </p>
<p> Use <tt>&quot;LT_INIT&quot;</tt> instead of <tt>&quot;AC_PROG_LIBTOOL&quot;</tt>. </p>
<p> The OCaml <tt>&quot;JSON&quot;</tt> code for parsing and serializing has been unified into a single abstract data type. </p>
<p> Most OCaml tools are now built using the <font SIZE="-1">PIC</font> runtime. This has a performance penalty on i686, but is relatively free on other architectures and has security benefits. </p>
<p> The direct backend now queries the qemu binary for availability of <font SIZE="-1">KVM,</font> instead of using a heuristic based on <i>/dev/kvm</i> (Andrea Bolognani). </p>
<p> Our &#8220;clever&#8221; libxml2 writer macros are now used consistently across all parts of the code base. </p>
<p> Qemu dropped <i>-nodefconfig</i> without telling us. The equivalent <i>-no-user-config</i> option is now used instead. Qemu also moved the <tt>&quot;serial&quot;</tt> option from <i>-drive</i> to <i>-device</i>, again without any notice, and this is also fixed.</p>
<h3>Bugs fixed</h3>
<dl>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1664310">https://bugzilla.redhat.com/1664310</a></p>
<dd> [<font SIZE="-1">RHEL 7.6 LP</font>] openstack output leaks passwords</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1661038">https://bugzilla.redhat.com/1661038</a></p>
<dd> virt-inspector fails with &#8220;error: int_of_string&#8221; on a Linux image when /etc/fstab contains a partionless device</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1651432">https://bugzilla.redhat.com/1651432</a></p>
<dd> v2v &#8211; support for -insecure option to support <font SIZE="-1">OSP SSL</font> connection for <font SIZE="-1">VM</font> migrations</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1642044">https://bugzilla.redhat.com/1642044</a></p>
<dd> [<font SIZE="-1">RFE</font>] virt-p2v <font SIZE="-1">UI</font> should give the option to shutdown after conversion is finished</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1634248">https://bugzilla.redhat.com/1634248</a></p>
<dd> virt-v2v cannot convert opensuse15 guest</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1624902">https://bugzilla.redhat.com/1624902</a></p>
<dd> Fix rhev-apt command that virt-v2v runs in Windows guests on first boot</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1624878">https://bugzilla.redhat.com/1624878</a></p>
<dd> Update v2v docs to describe support for <font SIZE="-1">SHA 2</font> certs required for converting Windows 7 and 2008 R2 guests</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1615885">https://bugzilla.redhat.com/1615885</a></p>
<dd> Minor log issue of virt-v2v</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1614276">https://bugzilla.redhat.com/1614276</a></p>
<dd> VixDiskLib: VixDiskLib_Read: Read 4096 sectors at 57516160 failed. Error 2 (Memory allocation failed. Out of memory.) (DiskLib error 802: <font SIZE="-1">NBD_ERR_INSUFFICIENT_RESOURCES</font>) at 5240.</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1612785">https://bugzilla.redhat.com/1612785</a></p>
<dd> &#8220;warning: &lt;target dev=&#8217;sr0&#8242;&gt; was ignored because the device name could not be recognized&#8221; should be hidden since convert cdrom is supported by virt-v2v</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1611690">https://bugzilla.redhat.com/1611690</a></p>
<dd> part_to_dev &#8220;/dev/sdp1&#8221; returns &#8220;/dev/sd&#8221; instead of &#8220;/dev/sdp&#8221;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1608131">https://bugzilla.redhat.com/1608131</a></p>
<dd> inspection fails when swap partition in /etc/fstab has incorrect <font SIZE="-1">UUID</font> compared to actual swap partition</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1605071">https://bugzilla.redhat.com/1605071</a></p>
<dd> On machines where /dev/kvm exists but <font SIZE="-1">KVM</font> doesn&#8217;t work, libguestfs will not fall back to <font SIZE="-1">TCG</font></p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1602353">https://bugzilla.redhat.com/1602353</a></p>
<dd> virt-inspector can&#8217;t inspect LUKS-encrypted <font SIZE="-1">RHEL7</font> guest image</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1601943">https://bugzilla.redhat.com/1601943</a></p>
<dd> Improve error &#8220;No module named ovirtsdk4&#8221; in v2v rhv-upload conversion</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1598715">https://bugzilla.redhat.com/1598715</a></p>
<dd> Adding <font SIZE="-1">QXL</font> device in <font SIZE="-1">OVF</font> causes Cirrus Logic device to be added to guest</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1598350">https://bugzilla.redhat.com/1598350</a></p>
<dd> <font SIZE="-1">RFE:</font> virt-v2v should preserve &lt;genid&gt;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1596851">https://bugzilla.redhat.com/1596851</a></p>
<dd> Transfer fails if local host is in maintenance mode</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1596810">https://bugzilla.redhat.com/1596810</a></p>
<dd> Transfer fails if local host belongs to another <font SIZE="-1">DC</font></p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1592468">https://bugzilla.redhat.com/1592468</a></p>
<dd> v2v to <font SIZE="-1">RHV</font> transfer fails with: error: [empty name]: cannot read &#8216;//*/disksection&#8217; with value: null</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1592061">https://bugzilla.redhat.com/1592061</a></p>
<dd> virt-v2v convert rhel5.3 failure when executing rpm -ql kernel-2.6.18-128.el5 command</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1591789">https://bugzilla.redhat.com/1591789</a></p>
<dd> p2v: error: <font SIZE="-1">XML</font> error: <font SIZE="-1">CPU</font> vendor specified without <font SIZE="-1">CPU</font> model</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1590220">https://bugzilla.redhat.com/1590220</a></p>
<dd> Hide rhv-upload option in virt-p2v client</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1588451">https://bugzilla.redhat.com/1588451</a></p>
<dd> Don&#8217;t use relative socket paths for <font SIZE="-1">NBD</font></p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1588088">https://bugzilla.redhat.com/1588088</a></p>
<dd> <font SIZE="-1">RFE:</font> Support for -o rhv-upload via Unix domain socket</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1586198">https://bugzilla.redhat.com/1586198</a></p>
<dd> ovirt-imageio-daemon times out during migration</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1580309">https://bugzilla.redhat.com/1580309</a></p>
<dd> virt-v2v rhel7.6 build can&#8217;t convert guest to null with qemu-kvm rhel7.5.z build</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1580292">https://bugzilla.redhat.com/1580292</a></p>
<dd> Virt-v2v rhel7.6 build can&#8217;t convert guest with qemu-kvm rhel7.5.z build</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1579047">https://bugzilla.redhat.com/1579047</a></p>
<dd> virt-builder: ubuntu-18.04 template has stray <font SIZE="-1">HTTP</font> proxy configured for apt</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1575640">https://bugzilla.redhat.com/1575640</a></p>
<dd> virt-builder: error: host cpu (x86_64) and guest arch (unknown) are not compatible</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1570407">https://bugzilla.redhat.com/1570407</a></p>
<dd> virt-v2v -i ova gives checksum error when missing files are mentioned in .mf</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1567763">https://bugzilla.redhat.com/1567763</a></p>
<dd> guestfsd: error: /Windows/Drivers/VirtIO: Read-only file system</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1564983">https://bugzilla.redhat.com/1564983</a></p>
<dd> The mount-vfs failed to mount the logical volume</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1561828">https://bugzilla.redhat.com/1561828</a></p>
<dd> <font SIZE="-1">RHV</font> tools not properly installed in migrated Windows <font SIZE="-1">VM</font>&#8216;s causing boot failure</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1559027">https://bugzilla.redhat.com/1559027</a></p>
<dd> virt-v2v does not honor &#8211;network with -o rhv-upload</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1557273">https://bugzilla.redhat.com/1557273</a></p>
<dd> [<font SIZE="-1">RFE</font>] Upload images directly to oVirt (virt-v2v -o rhv-upload)</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1544842">https://bugzilla.redhat.com/1544842</a></p>
<dd> [<font SIZE="-1">RFE</font>] Add libosinfo short-id to virt-inspector output</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1544674">https://bugzilla.redhat.com/1544674</a></p>
<dd> virt-inspector &#8211;help differs from manpage</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1544227">https://bugzilla.redhat.com/1544227</a></p>
<dd> <font SIZE="-1">RFE:</font> recognize the Kali Linux distribution</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1532224">https://bugzilla.redhat.com/1532224</a></p>
<dd> Resume=/dev/sdaX can&#8217;t be updated to resume=/dev/vdaX in rhel7 guest&#8217;s grub file after v2v conversion</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1530967">https://bugzilla.redhat.com/1530967</a></p>
<dd> Change categories of &#8220;Guest Operating system management by <font SIZE="-1">VIX API&#8221;</font> in v2v man page</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1527334">https://bugzilla.redhat.com/1527334</a></p>
<dd> Various -it vddk -io vddk* options should be documented, removed or fixed</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1148012">https://bugzilla.redhat.com/1148012</a></p>
<dd> <code>Reverted:</code> <font SIZE="-1">RFE:</font> Allow qemu-bridge-helper to be used to implement guestfs_set_network</dl>
<h2>RELEASE NOTES FOR LIBGUESTFS 1.38</h2>
<p> These release notes only cover the differences from the previous stable/dev branch split (1.36.0). For detailed changelogs, please see the git repository, or the ChangeLog file distributed in the tarball.</p>
<h3>New features</h3>
<p> <i>New tools</i> </p>
<p> Virt-builder-repository is a new tool allowing end users to create and update virt-builder repositories (Cédric Bosdonnat). </p>
<p> Virt-rescue (while not a new tool) has been substantially rewritten, implementing job control, <i>-m</i> and <i>-i</i> options, escape keys, etc. </p>
<p> <i>New features in existing tools</i> </p>
<p> Virt-builder planner has been improved so that faster and more efficient build plans are chosen for complex cases, especially when either the tmpdir or output is on networked storage. </p>
<p> New virt-builder Fedora templates (starting with Fedora 26) will have plain partition layout and use <font SIZE="-1">GPT</font> for partitions. </p>
<p> Virt-customize &#8220;firstboot&#8221; scripts in guests using systemd are now installed under the <tt>&quot;multi-user.target&quot;</tt> instead of <tt>&quot;default.target&quot;</tt> so they will only run when the system is booted normally. </p>
<p> Virt-customize now sets a random <i>/etc/machine-id</i> for Linux guests, if one is not already set. </p>
<p> Virt-df now works correctly on filesystems with block sizes smaller than 1K (Nikolay Ivanets). </p>
<p> Virt-dib has further compatibility enhancements with diskimage-builder (Pino Toscano). </p>
<p> Virt-sysprep removes <tt>&quot;DHCP_HOSTNAME&quot;</tt> from <i>ifcfg-*</i> files. </p>
<p> Virt-sysprep now works on Oracle Linux (Jamie Iles). </p>
<p> Virt-resize now correctly copies <font SIZE="-1">GPT</font> partition attributes from the source to the destination (Cédric Bosdonnat). </p>
<p> Bash tab completion implemented or enhanced for: virt-win-reg, virt-v2v-copy-to-local. </p>
<p> <i>virt-v2v and virt-p2v</i> </p>
<p> Virt-v2v can now read VMware <font SIZE="-1">VMX</font> files directly, either from local disk, <font SIZE="-1">NFS</font> storage, or over <font SIZE="-1">SSH</font> from an ESXi hypervisor. </p>
<p> Virt-v2v can now use <font SIZE="-1">VDDK</font> as an input source. </p>
<p> Both virt-v2v and virt-p2v are now able to pass through the source <font SIZE="-1">CPU</font> vendor, model and topology. However unfortunately not all source and target hypervisors are able to provide or consume this data at present (Tomáš Golembiovský). </p>
<p> Virt-v2v now supports encrypted guests (Pino Toscano). </p>
<p> Virt-v2v can now handle VMware snapshots. Note that the snapshots are collapsed — it <i>does not</i> convert the chain of snapshots into a chain of snapshots. </p>
<p> Virt-v2v now installs Windows 10 / Windows Server 2016 virtio block drivers correctly (Pavel Butsykin, Kun Wei). </p>
<p> Virt-v2v now installs virtio-rng, balloon and pvpanic drivers, and correctly sets this in the target hypervisor metadata for hypervisors which support that (Tomáš Golembiovský). </p>
<p> Virt-v2v now installs both legacy and modern virtio keys in the Windows registry (Ladi Prosek). </p>
<p> Virt-p2v can now preserve (in some cases) the offset of the Real Time Clock from <font SIZE="-1">UTC.</font> </p>
<p> Virt-p2v now combines several scp commands to the conversion server into a single command, improving conversion times. </p>
<p> Virt-v2v now detects the special Linux Xen PV-only kernels correctly (Laszlo Ersek). </p>
<p> Virt-v2v <i>-o glance</i> now generates the right properties for <font SIZE="-1">UEFI</font> guests (Pino Toscano). </p>
<p> Virt-v2v <i>-o null</i> now avoids spooling the guest to a temporary file, instead it writes to the qemu &#8220;null block device&#8221;. This makes it faster and use almost no disk space. </p>
<p> Virt-v2v <i>-o rhv</i> now supports Windows 2016 Server guest type. </p>
<p> Virt-v2v <i>-i libvirtxml</i> can now open network disks over http or https. </p>
<p> Virt-v2v will now give a warning about host passthrough devices (Pino Toscano). </p>
<p> The virt-v2v <i>&#8211;machine-readable</i> output has been enhanced so it includes <tt>&quot;vcenter-https&quot;</tt>, <tt>&quot;xen-ssh&quot;</tt> and <tt>&quot;in-place&quot;</tt> facts (Pino Toscano). </p>
<p> <i>Language bindings</i> </p>
<p> Fix multiple memory leaks and other data corruption problems in the Java bindings (Pino Toscano). </p>
<p> Perl <tt>%guestfs_introspection</tt> has been dropped. </p>
<p> <i>Inspection</i> </p>
<p> Inspection support was rewritten in OCaml and included inside the daemon. This makes inspection considerably faster, more robust and more easily extensible in future. </p>
<p> Better icon support for <font SIZE="-1">ALT</font> Linux guests (Pino Toscano). </p>
<p> Better support for NeoKylin (Qingzheng Zhang). </p>
<p> Can handle OSes like Void Linux which do not include <tt>&quot;VERSION_ID&quot;</tt> in <i>/etc/os-release</i> (Pino Toscano). </p>
<p> Add support for Microsoft MS-DOS (Daniel Berrangé). </p>
<p> <i>Architectures and platforms</i> </p>
<p> Multiple fixes for S/390 architecture. Libguestfs and all the tools should now compile and run on this architecture. </p>
<p> <i>Other</i> </p>
<p> The libguestfs <font SIZE="-1">API</font> is now thread-safe (although not parallel). You can call APIs on the same handle from multiple threads without needing to take a lock.</p>
<h3>Security</h3>
<p> There were multiple vulnerabilities in the icoutils <tt>&quot;wrestool&quot;</tt> program which is run by libguestfs to create icons for Windows guests. Using the latest <tt>&quot;wrestool&quot;</tt> is recommended.</p>
<h3><font SIZE="-1">API</font></h3>
<p> <i>New APIs</i></p>
<dl>
<dt>&quot;hivex_value_string&quot;</p>
<dd> This replaces the deprecated <tt>&quot;hivex_value_utf8&quot;</tt> <font SIZE="-1">API,</font> but does the same thing.</p>
<dt>&quot;part_get_gpt_attributes&quot;</p>
<dd>
<dt>&quot;part_set_gpt_attributes&quot;</p>
<dd> Read and write <font SIZE="-1">GPT</font> partition attribute flags (Cédric Bosdonnat).</p>
<dt>&quot;part_resize&quot;</p>
<dd> Enlarge or shrink an existing partition (Nikos Skalkotos).</p>
<dt>&quot;yara_destroy&quot;</p>
<dd>
<dt>&quot;yara_load&quot;</p>
<dd>
<dt>&quot;yara_scan&quot;</p>
<dd> Support for the Yara malware scanning engine (Matteo Cafasso).</dl>
<p> <i>Other </i><font SIZE="-1"><i>API</i></font><i> changes</i> </p>
<p> APIs implemented in the daemon can now be written in either C or OCaml. Several APIs were rewritten in OCaml, although we are not planning to rewrite all of them. </p>
<p> You will now get a clear error message if you try to add too many disks to the appliance, instead of getting a peculiar failure from qemu. </p>
<p> Certain APIs accidentally allowed you to use <tt>&quot;/dev/urandom&quot;</tt> as an input &#8220;device&#8221;, eg. <tt>&quot;g.copy_device_to_device(&quot;/dev/urandom&quot;, &quot;/dev/sda&quot;)&quot;</tt>. The code has been modified to <i>forbid</i> this usage. </p>
<p> All APIs for inspecting installer CDs have been deprecated. Use libosinfo for this task.</p>
<h3>Build changes</h3>
<p> A working OCaml compiler ≥ 4.01 is now required for building libguestfs. The <tt>&quot;./configure --disable-ocaml&quot;</tt> option remains but is only used to disable the OCaml language bindings. </p>
<p> Add <tt>&quot;RELEASES&quot;</tt> file which lists release dates for each version of libguestfs. You must update this file when making a new release. </p>
<p> Documentation generated by <tt>&quot;gtk-doc&quot;</tt> has been removed. <tt>&quot;./configure --enable-gtk-doc&quot;</tt> now does nothing. </p>
<p> Libtirpc is now used for <font SIZE="-1">XDR</font> functions and rpcgen. Note that glibc has deprecated and in most Linux distros dropped these, so for most people this will be an extra dependency (Martin Kletzander). </p>
<p> Libxcrypt is now used for <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3). This is required if using glibc ≥ 2.27. </p>
<p> <tt>&quot;ocaml-hivex&quot;</tt> is now required. </p>
<p> Libvirt ≥ 1.2.20 is now required. </p>
<p> There is now a <tt>&quot;make check-root&quot;</tt> target for tests which need to be run as root (analogous to <tt>&quot;make check-slow&quot;</tt>). </p>
<p> <tt>&quot;./configure&quot;</tt>-time check for <tt>&quot;__attribute__((cleanup))&quot;</tt> now works in the cross-compilation case (Yann E. Morin). </p>
<p> The <tt>&quot;AUTHORS&quot;</tt> and <tt>&quot;p2v/about-authors.c&quot;</tt> files are now generated from a single place. </p>
<p> Either GnuPG v1 or v2 can be used. </p>
<p> <tt>&quot;./configure --with-guestfs-path&quot;</tt> may be used to set the default <tt>&quot;LIBGUESTFS_PATH&quot;</tt>. In addition the way that the path is searched has changed slightly so that all types of appliances are searched in each path element separately (Pavel Butsykin). </p>
<p> <tt>&quot;GUESTFSD_EXT_CMD&quot;</tt> which was used to mark external commands in the daemon has been removed. It was originally used by <font SIZE="-1">SUSE</font> builds, but they have not been using it for a while. </p>
<p> The output from <tt>&quot;./configure&quot;</tt> is now visually grouped under headings related to what it is doing, making it much easier to scan (Pino Toscano). </p>
<p> OCaml dependencies are now generated from a single script instead of multiple not-quite-the-same Makefile fragments. </p>
<p> <tt>&quot;./configure --with-distro=ID&quot;</tt> can be used to override automatic Linux distro detection at build time (Pino Toscano). </p>
<p> qemu ≥ 2.10 is supported (but not required). This adds mandatory locking to disks and libguestfs turns this off in certain circumstances when it is known to be safe (Lars Seipel, Peter Krempa, Daniel Berrangé, Pino Toscano, Fam Zheng, Yongkui Guo, Václav Kadlčík).</p>
<h3>Internals</h3>
<p> Most common code has been moved to the <i>common/</i> subdirectory, with OCaml common code being in <i>common/ml*</i> directories (eg. <i>common/visit</i> and <i>common/mlvisit</i> contain the visitor library in C and OCaml respectively). The <i>mllib</i> directory has been deleted and replaced by <i>common/mltools</i>. </p>
<p> There is now a lightweight OCaml binding for <font SIZE="-1">PCRE,</font> see <i>common/mlpcre</i>. Use of OCaml <tt>&quot;Str&quot;</tt> library has been mostly replaced with <font SIZE="-1">PCRE.</font> </p>
<p> Add more calls to <tt>&quot;udev_settle&quot;</tt> to improve stability of partition code (Dawid Zamirski). </p>
<p> Run <tt>&quot;udev_settle&quot;</tt> with <i>&#8211;exit-if-exists</i> option, which improves the speed of this command (Pavel Butsykin). </p>
<p> Detect new locations of <code><a href="/docs/linux/man/3-major/">major</a></code>(3), <code><a href="/docs/linux/man/3-minor/">minor</a></code>(3), <code><a href="/docs/linux/man/3-makedev/">makedev</a></code>(3). </p>
<p> Actions can now be deprecated with no suggested replacement, for APIs such as <tt>&quot;guestfs_wait_ready&quot;</tt> that should simply be removed from client code. </p>
<p> Use gnulib <tt>&quot;set_nonblocking_flag&quot;</tt> wrapper instead of calling <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) with <tt>&quot;O_NONBLOCK&quot;</tt> (Eric Blake). Similarly <tt>&quot;set_cloexec_flag&quot;</tt>. </p>
<p> Fix memory leak in <font SIZE="-1">XFS</font> version of <tt>&quot;guestfs_vfs_minimum_size&quot;</tt> (Pino Toscano). </p>
<p> Valgrind checks now run on the virt-p2v binary. </p>
<p> Unicode single quotes (<tt>&quot;‘’&quot;</tt>) and now used in place of <tt>''</tt> or <tt>`'</tt> throughout the code and documentation. Similarly for <tt>&quot;’s&quot;</tt> instead of <tt>&quot;'s&quot;</tt>. </p>
<p> The <tt>&quot;is_zero&quot;</tt> function has been reimplemented for greater speed (Eric Blake). </p>
<p> In the direct backend, virtio-blk support has been removed. Virtio-scsi is now the only supported way to add disks. </p>
<p> Generator string parameter and return types have been rationalised so there are only two types (<tt>&quot;String&quot;</tt>, <tt>&quot;StringList&quot;</tt>) with many subtypes eg. <tt>&quot;FileIn&quot;</tt> becomes <tt>&quot;String (FileIn, ...)&quot;</tt>. </p>
<p> The appliance disk image can now be in formats other than raw (Pavel Butsykin). </p>
<p> Multiple improvements to how we automatically build Debian templates for virt-builder (Pino Toscano). Enable serial console for these templates (Florian Klink). </p>
<p> In the daemon, instead of making a private copy of lvm.conf and modifying it (eg for filters), start with an empty file since <font SIZE="-1">LVM</font> understands that to mean &#8220;all defaults&#8221; (Alasdair Kergon, Zdenek Kabelac). </p>
<p> The <tt>&quot;direct&quot;</tt> backend can now run <font SIZE="-1">QMP</font> queries against the <font SIZE="-1">QEMU</font> binary, enhancing the kinds of information we can detect. In addition the code to query <font SIZE="-1">QEMU</font> has been made more robust for handling multiple parallel queries of different versions of <font SIZE="-1">QEMU.</font> </p>
<p> OCaml Augeas bindings are bundled under <i>common/mlaugeas</i>. The long term plan is to remove this and use system ocaml-augeas when it is more widely available in distros (Pino Toscano). </p>
<p> All OCaml modules (<tt>&quot;*.ml&quot;</tt> files) are now required to have an interface file (<tt>&quot;*.mli&quot;</tt>). If they don&#8217;t export anything then the interface will be empty except for comments. </p>
<p> Certain OCaml features in OCaml ≥ 4.01 are used throughout the code, including replacing ‘{ field = field }’ with ‘{ field }’. </p>
<p> Virt-builder <tt>&quot;make-template&quot;</tt> utility now uses the <tt>&quot;virt-install --transient&quot;</tt> option so that we should never need to clean up left over domains after a crash. It also saves kickstarts and virt-install commands, which are committed to git for future reference. </p>
<p> <i>/dev/shm</i> is now created in the appliance (Nicolas Hicher). </p>
<p> In verbose mode on Fedora guests, virt-customize will now use <tt>&quot;dnf --verbose&quot;</tt> enabling better debugging output. </p>
<p> Virt-v2v input and output classes now contain a <tt>&quot;#precheck&quot;</tt> method which is used to perform environmental checks before conversion starts. </p>
<p> Virt-p2v enables miniexpect debugging. It is written to stderr (of virt-p2v). </p>
<p> Virt-v2v free space checks are more liberal especially for smaller guests (Pino Toscano).</p>
<h3>Bugs fixed</h3>
<dl>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1540535">https://bugzilla.redhat.com/1540535</a></p>
<dd> Example <font SIZE="-1">URI</font> of &#8220;Convert from ESXi hypervisor over <font SIZE="-1">SSH</font> to local libvirt&#8221; is incorrect in v2v man page</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1539395">https://bugzilla.redhat.com/1539395</a></p>
<dd> virt-customize segfaults after upgrading to 1.37.35-3</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1536765">https://bugzilla.redhat.com/1536765</a></p>
<dd> Libguestfs Perl bindings can leak a small amount of memory on error</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1536763">https://bugzilla.redhat.com/1536763</a></p>
<dd> libguestfs Lua bindings use <code>strerror()</code>, which isn’t thread safe</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1536603">https://bugzilla.redhat.com/1536603</a></p>
<dd> man page makes no mention of using &#8216;&#8211;&#8216; when trying to change exit on error behavior</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1525241">https://bugzilla.redhat.com/1525241</a></p>
<dd> virt-df displays zeros for filesystems with block size =512</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1519204">https://bugzilla.redhat.com/1519204</a></p>
<dd> v2v should improve the result when convert a rhel7.4 guest with no available kernels found in the bootloader</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1518517">https://bugzilla.redhat.com/1518517</a></p>
<dd> virt-v2v fails with &#8220;unsupported configuration: shared access for disk &#8216;sdb&#8217; requires use of supported storage format&#8221;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1516094">https://bugzilla.redhat.com/1516094</a></p>
<dd> Mere presence of <font SIZE="-1">QEMU</font> file locking options breaks <font SIZE="-1">NBD</font> (Block protocol &#8216;nbd&#8217; doesn&#8217;t support the option &#8216;locking&#8217;)</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1514756">https://bugzilla.redhat.com/1514756</a></p>
<dd> ./configure &#8211;disable-ocaml breaks building common/mlpcre which breaks building daemon</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1513884">https://bugzilla.redhat.com/1513884</a></p>
<dd> [<font SIZE="-1">RFE</font>]Should update some vddk info in v2v man page</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1508874">https://bugzilla.redhat.com/1508874</a></p>
<dd> virt-v2v: warning: ova disk has an unknown VMware controller type (20)</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1506572">https://bugzilla.redhat.com/1506572</a></p>
<dd> virt-v2v &#8216;-i ova&#8217; is not parsing the <font SIZE="-1">MAC</font> address from the source <font SIZE="-1">OVF</font></p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1506511">https://bugzilla.redhat.com/1506511</a></p>
<dd> virt-builder fails to parse repo file if it has blank space after the repository identifier</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1503958">https://bugzilla.redhat.com/1503958</a></p>
<dd> Failed to convert the rhel5 guest with kmod-xenpv installed from xen server by virt-v2v</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1503497">https://bugzilla.redhat.com/1503497</a></p>
<dd> qemu-kvm fails to open qcow2 files in read-only mode with qemu-kvm 1.5.3</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1500673">https://bugzilla.redhat.com/1500673</a></p>
<dd> Error info shows wrong sometimes when ssh to conversion server using non-root user with sudo on p2v client</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1500537">https://bugzilla.redhat.com/1500537</a></p>
<dd> /dev/shm does not exist in the appliance environment</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1497475">https://bugzilla.redhat.com/1497475</a></p>
<dd> guestfish cannot list commands from interactive mode</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1493048">https://bugzilla.redhat.com/1493048</a></p>
<dd> Unbound constructor Hivex.OPEN_UNSAFE</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1484957">https://bugzilla.redhat.com/1484957</a></p>
<dd> bump debian images to use single-partition layout</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1482737">https://bugzilla.redhat.com/1482737</a></p>
<dd> virt-resize failed to expand swap partition for <font SIZE="-1">RHEL5.11</font> guest image with &#8220;parsing <font SIZE="-1">UUID</font> failed&#8221;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1477623">https://bugzilla.redhat.com/1477623</a></p>
<dd> Running file <font SIZE="-1">API</font> on a special chardev may hang forever</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1476081">https://bugzilla.redhat.com/1476081</a></p>
<dd> inspect-os report error: could not parse integer in version number: V7Update2</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1472719">https://bugzilla.redhat.com/1472719</a></p>
<dd> [<font SIZE="-1">RFE</font>]Add warning in process of v2v converting guest which has pci passthrough device</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1472208">https://bugzilla.redhat.com/1472208</a></p>
<dd> virt-v2v fails on opensuse 13.2 guest with error: statns: statns_stub: path must start with a / character</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1469655">https://bugzilla.redhat.com/1469655</a></p>
<dd> firstboot scripts are not correctly installed in Fedora 26</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1466563">https://bugzilla.redhat.com/1466563</a></p>
<dd> Libguestfs should pass copyonread flag through to the libvirt <font SIZE="-1">XML</font></p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1465665">https://bugzilla.redhat.com/1465665</a></p>
<dd> 1.36.x build failure: gtkdocize fails using newer autotools due to missing <font SIZE="-1">GTK_DOC_CHECK</font> in configure.ac</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1460338">https://bugzilla.redhat.com/1460338</a></p>
<dd> guestfs_shutdown hangs if main process sets signal handlers</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1459979">https://bugzilla.redhat.com/1459979</a></p>
<dd> guestfs_add_domain_argv fails with readonly option when vdi/vhd disk is attached to libvirt domain</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1451665">https://bugzilla.redhat.com/1451665</a></p>
<dd> <font SIZE="-1">RFE:</font> Virt-v2v can&#8217;t convert the guest which has encrypted partition</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1450325">https://bugzilla.redhat.com/1450325</a></p>
<dd> document <font SIZE="-1">URI</font> format for -a parameters of tools</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1448739">https://bugzilla.redhat.com/1448739</a></p>
<dd> <font SIZE="-1">RFE:</font> Support multicore decompression for <font SIZE="-1">OVA</font> files using pigz and pxz</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1447202">https://bugzilla.redhat.com/1447202</a></p>
<dd> Win 2016 guest is described as Win 10 after imported to <font SIZE="-1">RHEVM</font></p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1441197">https://bugzilla.redhat.com/1441197</a></p>
<dd> <font SIZE="-1">RFE:</font> ability to convert VMware virtual machines via vmx</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1438939">https://bugzilla.redhat.com/1438939</a></p>
<dd> Please drop or update GnuPG (1.4.x) dependency</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1438794">https://bugzilla.redhat.com/1438794</a></p>
<dd> [<font SIZE="-1">RFE</font>] Install Windows virtio-rng drivers on VMs imported</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1433937">https://bugzilla.redhat.com/1433937</a></p>
<dd> virt-inspector can&#8217;t get icon info from altlinux-centaurus</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1433577">https://bugzilla.redhat.com/1433577</a></p>
<dd> policycoreutils setfiles &gt;= 2.6 does .. nothing</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1431579">https://bugzilla.redhat.com/1431579</a></p>
<dd> Windows 8 <font SIZE="-1">UEFI</font> from VMware to <font SIZE="-1">KVM</font> fails to boot after conversion</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1430680">https://bugzilla.redhat.com/1430680</a></p>
<dd> There is error info about &#8220;No such file or directory&#8221; when convert a guest from ova file by v2v</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1430184">https://bugzilla.redhat.com/1430184</a></p>
<dd> virt-dib should generate sha256 checksum instead of sha512</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1429506">https://bugzilla.redhat.com/1429506</a></p>
<dd> <font SIZE="-1">RFE: OVMF</font> should be detected on conversion server to prevent failed conversion</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1429491">https://bugzilla.redhat.com/1429491</a></p>
<dd> Should rename network name of rhv in virt-v2v man page</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1427529">https://bugzilla.redhat.com/1427529</a></p>
<dd> virt-sysprep should remove <font SIZE="-1">DHCP_HOSTNAME</font></p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1417306">https://bugzilla.redhat.com/1417306</a></p>
<dd> <font SIZE="-1">QEMU</font> image file locking (libguestfs)</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1409024">https://bugzilla.redhat.com/1409024</a></p>
<dd> [Debian] Missing db_dump abort inspection</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1406906">https://bugzilla.redhat.com/1406906</a></p>
<dd> Segmentation fault when reading corrupted path with Python 3 bindings</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1379289">https://bugzilla.redhat.com/1379289</a></p>
<dd> <font SIZE="-1">RFE:</font> virt-p2v should support mnemonic operations</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1378022">https://bugzilla.redhat.com/1378022</a></p>
<dd> There is virt-v2v warning about &lt;listen type=&#8217;none&#8217;&gt; during converting a guest which has listen type=&#8217;none&#8217; in <font SIZE="-1">XML</font></p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1376547">https://bugzilla.redhat.com/1376547</a></p>
<dd> qemu-system-s390x: -device isa-serial,chardev=charserial0,id=serial0: &#8216;isa-serial&#8217; is not a valid device model name</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1374232">https://bugzilla.redhat.com/1374232</a></p>
<dd> selinux relabel fails on <font SIZE="-1">RHEL 6.2</font> guests with &#8220;libguestfs error: selinux_relabel: : Success&#8221;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1367738">https://bugzilla.redhat.com/1367738</a></p>
<dd> Missing bash completion scripts for: virt-diff guestunmount virt-copy-in virt-copy-out virt-customize virt-get-kernel virt-p2v-make-disk virt-p2v-make-kickstart virt-tar-in virt-tar-out virt-v2v-copy-to-local virt-win-reg</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1362649">https://bugzilla.redhat.com/1362649</a></p>
<dd> <font SIZE="-1">RFE:</font> virt-sysprep does not utilize libguestfs encryption support</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1172425">https://bugzilla.redhat.com/1172425</a></p>
<dd> [<font SIZE="-1">RFE</font>]virt-v2v failed to convert VMware <font SIZE="-1">ESX VM</font> with snapshot</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1171654">https://bugzilla.redhat.com/1171654</a></p>
<dd> Modify a file in virt-rescue with vi on some linux terminal such as yakuake, can lead to abnormal display in virt-rescue shell</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1167623">https://bugzilla.redhat.com/1167623</a></p>
<dd> Remove &#8220;If reporting bugs, run virt-v2v with debugging enabled ..&#8221; message when running virt-p2v</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1152819">https://bugzilla.redhat.com/1152819</a></p>
<dd> Can not end a running command in virt-rescue by press ^C or other keys, the only way is to exit virt-rescue</dl>
<h2>RELEASE NOTES FOR LIBGUESTFS 1.36</h2>
<p> These release notes only cover the differences from the previous stable/dev branch split (1.34.0). For detailed changelogs, please see the git repository, or the ChangeLog file distributed in the tarball.</p>
<h3>New features</h3>
<p> <i>New tools</i> </p>
<p> Virt-tail is a new tool for following (tailing) log files within a guest, similar to the regular <tt>&quot;tail -f&quot;</tt> command. </p>
<p> <i>New features in existing tools</i> </p>
<p> Virt-customize, virt-get-kernel, virt-sparsify and virt-sysprep can now handle encrypted guests (Pino Toscano). </p>
<p> Virt-builder and virt-customize now support <i>&#8211;append-line</i>, which is useful for adding lines to the end of configuration files. </p>
<p> Virt-resize can now shrink and expand swap partitions (Pino Toscano). </p>
<p> Virt-resize can now output to non-local disks (Pino Toscano). </p>
<p> Virt-sysprep has a new operation called <tt>&quot;backup-files&quot;</tt> for removing editor backups, and <tt>&quot;passwd-backups&quot;</tt> for removing <i>/etc/passwd-</i> and similar. </p>
<p> Virt-dib can now create checksums using the new <i>&#8211;checksum</i> option (Pino Toscano). </p>
<p> Virt-dib can now create tgz files. In addition, extended attributes and SELinux labels are preserved in the output tar file (Pino Toscano). </p>
<p> Virt-dib can now create squashfs files (Pino Toscano). </p>
<p> Bash tab-completion is now available in every command line tool that is shipped. </p>
<p> <i>virt-v2v and virt-p2v</i> </p>
<p> Conversions of Debian (6+) and Ubuntu (10.04+) guests are now supported (Tomáš Golembiovský, Pino Toscano). </p>
<p> Conversions from <font SIZE="-1">SUSE</font> Xen hypervisor have now been tested (Cédric Bosdonnat). </p>
<p> Windows conversions may now install a program <tt>&quot;pnp_wait.exe&quot;</tt> which prevents conflicts between the Windows Plug-and-Play Manager and our own scripts that install virtio device drivers. Enabling this requires the <tt>&quot;pnp_wait.exe&quot;</tt> program to be built separately (Roman Kagan). </p>
<p> <font SIZE="-1">OVA</font> files exported from <font SIZE="-1">AWS</font> can now be converted (Shahar Havivi). </p>
<p> When converting <font SIZE="-1">OVA</font> files, in some circumstances virt-v2v can now read disk images directly from the <font SIZE="-1">OVA</font> input file instead of needing to unpack the <font SIZE="-1">OVA</font> file to a temporary directory. This can save large amounts of disk space, and is quicker (Tomáš Golembiovský). </p>
<p> Virt-p2v can now be built on <font SIZE="-1">RHEL 5</font> (2007-era) Linux and <font SIZE="-1">RHEL 6,</font> which means that 32 bit and hardware with ancient fakeraid disks can be virtualized. Binaries of virt-p2v based on these old versions of <font SIZE="-1">RHEL</font> can be found at <a rel="nofollow" href="http://oirase.annexia.org/virt-p2v/">http://oirase.annexia.org/virt-p2v/</a> </p>
<p> Virt-p2v can now use nbdkit (an <font SIZE="-1">NBD</font> server) as an alternative to qemu-nbd. In addition, virt-p2v can use &#8220;socket activation&#8221; which is a more robust method for opening the <font SIZE="-1">NBD</font> listening socket. Socket activation works with qemu-nbd or nbdkit, but requires the most up to date versions. </p>
<p> To prevent timeouts during P2V conversions, virt-p2v inhibits power saving on the physical machine, and also sends ping packets over the ssh control and data connections. </p>
<p> Virt-v2v no longer removes the <tt>&quot;Processor&quot;</tt> and <tt>&quot;Intelppm&quot;</tt> nodes from the Windows Registry. </p>
<p> Xen and vCenter conversions can now be done using the libvirt backend, provided libvirt ≥ 2.1.0 is used. </p>
<p> <i>/dev/srX</i> (<font SIZE="-1">SCSI</font> CD-ROM) devices are ignored (Tomáš Golembiovský). </p>
<p> When converting <font SIZE="-1">SUSE</font> Linux guests, use <i>/etc/modprobe.conf.local</i> if it exists. </p>
<p> Removing VMware tools from Linux guests should now work reliably (Pino Toscano). </p>
<p> When converting <font SIZE="-1">OVA</font> files, virt-v2v now checks the disk image hash contained in the manifest file, whereas previously it was ignored because of a mistake in the code. In addition, <font SIZE="-1">SHA256</font> hashes are now supported (Tomáš Golembiovský). </p>
<p> When converting <font SIZE="-1">OVA</font> files that contain compressed disk images, we now trust the <tt>&quot;ovf:compression&quot;</tt> attribute from the metadata instead of using content sniffing on the disk image (Tomáš Golembiovský). </p>
<p> A new flag <i>&#8211;vdsm-compat</i> has been added to <i>-o vdsm</i> mode, allowing more efficient qcow2 images to be generated. </p>
<p> Since the <font SIZE="-1">RHEV</font> product [commercially supported version of oVirt] has now been renamed to <font SIZE="-1">RHV, &#8220;RHEV&#8221;</font> was changed to &#8220;<font SIZE="-1">RHV&#8221;</font> throughout the tooling. In particular, <i>-o rhev</i> becomes <i>-o rhv</i>, although the old name can be used for backwards compatibility. </p>
<p> The <tt>&quot;RHEV-APT&quot;</tt> utility is only installed when the output hypervisor is oVirt or <font SIZE="-1">RHV.</font> </p>
<p> A problem with virt-v2v running out of memory when doing an SELinux relabel of the guest filesystem should now be resolved. </p>
<p> <i>Language bindings</i> </p>
<p> Setting <tt>&quot;EXTRA_JAVAC_FLAGS&quot;</tt> before <i>./configure</i> allows you to add arbitrary flags to <tt>&quot;javac&quot;</tt> when compiling the Java bindings. </p>
<p> Use of any libguestfs <font SIZE="-1">API</font> which returned a single struct, from Perl or Java bindings, would have leaked memory. This has now been fixed (Pino Toscano). </p>
<p> <i>Inspection</i> </p>
<p> Inspection of Windows guests with mildly corrupted Windows Registry hives should now work instead of failing with an error. This feature requires hivex ≥ 1.3.14 (Dawid Zamirski). </p>
<p> For Debian guests, we can now read the <font SIZE="-1">URL,</font> source name, summary and full description of installed packages. For RPM-based guests we can read the <font SIZE="-1">URL,</font> summary and description (Pino Toscano). </p>
<p> Inspection of guest operating systems that use a separate <i>/usr</i> partition should now work more reliably (Pino Toscano). </p>
<p> When parsing guest <i>/etc/fstab</i>, paths are reduced to a canonical form (eg. <tt>&quot;///usr//local//&quot;</tt> → <tt>&quot;/usr/local&quot;</tt>). </p>
<p> Inspection of btrfs subvolumes now works where the <i>/etc/fstab</i> options field contains commas. </p>
<p> <i>/dev/cdN</i> devices in guest <i>/etc/fstab</i> are ignored (Pino Toscano). </p>
<p> <i>Architectures and platforms</i> </p>
<p> Stable releases are now tested on aarch64, ppc64 and ppc64le architectures. </p>
<p> The RISC-V architecture is now handled as a guest, and libguestfs will now at least compile on RISC-V (but probably not work as there is no usable qemu at the time of writing). </p>
<p> Detection of S/390 and S/390x binaries and guests is now supported. </p>
<p> <i>Other</i> </p>
<p> ExFAT filesystems are now supported (Miles Wolbe).</p>
<h3>Security</h3>
<p> See also <code><a href="/docs/linux/man/1-guestfs-security/">guestfs-security</a></code>(1). </p>
<p> There were no CVEs reported in this development cycle. However some security-related hardening was carried out as described below. </p>
<p> Temporary filenames are now always generated using randomness from <i>/dev/urandom</i> (previously the C function <code><a href="/docs/linux/man/3-random/">random</a></code>(3) was used in one case). </p>
<p> The <tt>$TERM</tt> environment variable is now validated before passing it through to the appliance kernel command line.</p>
<h3><font SIZE="-1">API</font></h3>
<p> <i>New APIs</i></p>
<dl>
<dt>&quot;guestfs_aug_transform&quot;</p>
<dd> Exposes the Augeas <tt>&quot;aug_transform&quot;</tt> <font SIZE="-1">API</font> (Pino Toscano).</p>
<dt>&quot;guestfs_find_inode&quot;</p>
<dd> Find files by inode number (Matteo Cafasso).</p>
<dt>&quot;guestfs_inspect_get_windows_software_hive&quot;</p>
<dd>
<dt>&quot;guestfs_inspect_get_windows_system_hive&quot;</p>
<dd> Return the path to the Windows <tt>&quot;HKLM\SYSTEM&quot;</tt> and <tt>&quot;HKLM\SOFTWARE&quot;</tt> hives computed during inspection.</p>
<dt>&quot;guestfs_mksquashfs&quot;</p>
<dd> Create a squashfs filesystem from a path (Pino Toscano).</dl>
<p> <i>Other </i><font SIZE="-1"><i>API</i></font><i> changes</i></p>
<dl>
<dt>&quot;guestfs_add_domain&quot;</p>
<dd> This call now handles libvirt file-based volumes correctly, where previously these would have been ignored. Also handled are disks which require libvirt authentication secrets to open (Pino Toscano).</p>
<dt>&quot;guestfs_canonical_device_name&quot;</p>
<dd> This call will no longer incorrectly modify Linux software <font SIZE="-1">RAID</font> device names (like <i>/dev/mdX</i>).</p>
<dt>&quot;guestfs_file_architecture&quot;</p>
<dd> Previously the <tt>&quot;file_architecture&quot;</tt> <font SIZE="-1">API</font> could return either of the strings <tt>&quot;i386&quot;</tt> or <tt>&quot;i486&quot;</tt> for 32 bit x86 binaries. It now only returns <tt>&quot;i386&quot;</tt> (as documented). </p>
<p> This <font SIZE="-1">API</font> can now return the following new values: <tt>&quot;riscv32&quot;</tt>, <tt>&quot;riscv64&quot;</tt>, <tt>&quot;riscv128&quot;</tt>, <tt>&quot;s390&quot;</tt>, <tt>&quot;s390x&quot;</tt>.</p>
<dt>&quot;guestfs_hivex_open&quot;</p>
<dd> This now has an optional <tt>&quot;GUESTFS_HIVEX_OPEN_UNSAFE&quot;</tt> flag which allows certain corrupted Windows Registry hives to be opened. This feature requires hivex ≥ 1.3.14 (Dawid Zamirski).</p>
<dt>&quot;guestfs_list_partitions&quot;</p>
<dd> This call now returns Linux software <font SIZE="-1">RAID</font> partitions.</p>
<dt>&quot;guestfs_part_to_dev&quot;</p>
<dd> This call now correctly handles partition names which include <tt>&quot;p&lt;N&gt;&quot;</tt> (Pino Toscano).</p>
<dt>&quot;guestfs_set_label&quot;</p>
<dd> This call can now change the labels of swap partitions (Pino Toscano).</dl>
<h3>Build changes</h3>
<p> libmagic, the library part of the <tt>&quot;file&quot;</tt> command, is now required at build time (previously optional). </p>
<p> <font SIZE="-1">GCC 7</font> is now supported. </p>
<p> &#8220;Silent rules&#8221; are now used for OCaml programs, Java bindings. To show the full command line executed, add <tt>&quot;V=1&quot;</tt> on the make command line (Pino Toscano). </p>
<p> Slow testing (<tt>&quot;make check-slow&quot;</tt>) now covers: firstboot scripts in Linux guests; v2v conversion of a selection of real Linux guests; the virt-customize <i>&#8211;hostname</i> and <i>&#8211;timezone</i> settings; the <i>&#8211;root-password</i> parameter; that the serial console works in virt-builder guests. </p>
<p> Large generated C source files, eg. the list of commands found in <i>fish/cmds.c</i> (and many more), have been split into smaller files to speed parallel compilation. </p>
<p> <tt>&quot;make maintainer-check-extra-dist&quot;</tt> now checks that all generated files are included in the tarball. </p>
<p> The tests no longer assume that <tt>&quot;.&quot;</tt> is in Perl&#8217;s <tt>@INC</tt>, as it is going to be removed soon (Pino Toscano). </p>
<p> Debian hosts using UsrMerge are now supported (Pino Toscano). </p>
<p> Header files and C structs can now have internal documentation using the special <tt>&quot;/** ... */&quot;</tt> comments. </p>
<p> <tt>&quot;@VAR@&quot;</tt> subtitutions in <tt>&quot;./run&quot;</tt> are now fully quoted. This is necessary so that (eg) <tt>&quot;./configure PYTHON=/some/path&quot;</tt> works robustly if <tt>&quot;/some/path&quot;</tt> contains characters that need to be quoted (Hilko Bengen). </p>
<p> gperf ≥ 3.1 is now supported. </p>
<p> Kraxel&#8217;s old edk2 builds can no longer be used for <font SIZE="-1">UEFI</font> support. <font SIZE="-1">UEFI</font> code is now fully free software, so use the versions bundled with your Linux distro instead. </p>
<p> Virt-p2v can now be compiled on <font SIZE="-1">RHEL 5</font> (2007-era) Linux with Gtk 2.10.</p>
<h3>Internals</h3>
<p> The generator and mllib <tt>&quot;Common_utils&quot;</tt> modules are now shared from the same source file. </p>
<p> A considerable amount of common code has been moved into the <i>common</i> directory in the source and is now compiled only once. The mini-libraries located under here are: <i>common/edit</i>, <i>common/errnostring</i>, <i>common/miniexpect</i>, <i>common/options</i>, <i>common/parallel</i>, <i>common/progress</i>, <i>common/protocol</i>, <i>common/utils</i>, <i>common/visit</i>, <i>common/windows</i>. </p>
<p> The directory containing the main library code has moved from <i>src</i> → <i>lib</i>. </p>
<p> All tests written in shell script now use a common file of utility functions (<i>tests/test-functions.sh</i>). There are several new utility functions, mainly for skipping tests. Also these test scripts can now use autoconf-like path variables like <tt>$abs_top_srcdir</tt>. </p>
<p> <font SIZE="-1">UEFI</font> paths are now stored in the generator (<i>generator/uefi.ml</i>). </p>
<p> The way the generator handles actions and procedure numbers was changed quite substantially. See <i>generator/actions_*.ml</i> and <i>generator/proc_nr.ml</i>. </p>
<p> The gnulib <tt>&quot;getprogname&quot;</tt> module is now used everywhere when needing/printing the program name (Pino Toscano). </p>
<p> <i>perl/Guestfs.c</i> is not translatable (Nikos Skalkotos). </p>
<p> Virt-builder templates moved from <i>builder/website</i> to <i>builder/templates</i> and there is now a single unified program which can build any template. </p>
<p> All Windows registry utilities used by virt-customize and virt-v2v have been moved to a common module called <tt>&quot;Registry&quot;</tt> under <i>mllib</i>. </p>
<p> All <font SIZE="-1">POSIX</font> bindings have been moved to a new module called <tt>&quot;Unix_utils&quot;</tt> under <i>mllib</i>. </p>
<p> Inspection, virt-customize and virt-v2v no longer recompute the Windows <tt>&quot;%systemroot%&quot;</tt>, <tt>&quot;CurrentControlSet&quot;</tt> or paths to the <tt>&quot;HKLM\SYSTEM&quot;</tt> and <tt>&quot;HKLM\SOFTWARE&quot;</tt> hives in multiple places. Instead these are all computed once (during inspection) and passed to the other tools through various <tt>&quot;guestfs_inspect_get_windows_*&quot;</tt> APIs. </p>
<p> <tt>&quot;/dev/pts&quot;</tt> is now available inside the appliance, so any tools we run which require a pty will now work (Pino Toscano). </p>
<p> Most OCaml warnings have been fixed. </p>
<p> There is now a single common function for creating temporary files (<tt>&quot;guestfs_int_make_temp_path&quot;</tt>) (Matteo Cafasso). </p>
<p> The <tt>$TERM</tt> environment variable is now validated before passing it through to the appliance kernel command line. </p>
<p> Useless <font SIZE="-1">USB</font> and memballoon devices are no longer created in the appliance (Laine Stump). </p>
<p> On aarch64 we now use virtio-pci for the appliance. This is somewhat faster than virtio-mmio. </p>
<p> Use of <code><a href="/docs/linux/man/3-srandom/">srandom</a></code>(3) and <code><a href="/docs/linux/man/3-random/">random</a></code>(3) has been minimized. In particular, temporary filenames are no longer created based on randomness returned by <code><a href="/docs/linux/man/3-random/">random</a></code>(3), but <i>/dev/urandom</i> is used instead.</p>
<h3>Bugs fixed</h3>
<dl>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1425306">https://bugzilla.redhat.com/1425306</a></p>
<dd> typo error in virt-tail man page</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1418283">https://bugzilla.redhat.com/1418283</a></p>
<dd> virt-v2v: appliance runs out of memory running setfiles command</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1417549">https://bugzilla.redhat.com/1417549</a></p>
<dd> /usr/bin/x86_64-linux-gnu-ld.bfd.real: ../common/progress/.libs/libprogress.a(libprogress_la-progress.o): undefined reference to symbol &#8216;UP@@NCURSES_TINFO_5.0.19991023&#8217;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1417444">https://bugzilla.redhat.com/1417444</a></p>
<dd> *** No rule to make target &#8216;../perl/lib/Sys/Guestfs.c&#8217;, needed by &#8216;libguestfs.pot&#8217;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1416941">https://bugzilla.redhat.com/1416941</a></p>
<dd> compile of 1.34.3 fails with gperf 3.1</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1414682">https://bugzilla.redhat.com/1414682</a></p>
<dd> guestfs_canonical_device_name incorrectly returns /dev/sd0 for <font SIZE="-1">MD</font> devices (/dev/md0)</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1414510">https://bugzilla.redhat.com/1414510</a></p>
<dd> guestfs_list_filesystems does not recognize ddf partitions</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1409023">https://bugzilla.redhat.com/1409023</a></p>
<dd> [Debian] ldmtool not installed in the appliance</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1404287">https://bugzilla.redhat.com/1404287</a></p>
<dd> qemu-kvm cannot boot <font SIZE="-1">RHEL 7</font> kernel with <font SIZE="-1">TCG,</font> hangs at &#8220;Probing <font SIZE="-1">EDD</font> (edd=off to disable)&#8230;&#8221;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1404182">https://bugzilla.redhat.com/1404182</a></p>
<dd> <font SIZE="-1">RFE:</font> virt-resize should support a <font SIZE="-1">URL</font> as the outdisk</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1401474">https://bugzilla.redhat.com/1401474</a></p>
<dd> Importing VMs from VMware is failing with error &#8220;Inspection field &#8216;i_arch&#8217; was &#8216;unknown&#8221;&#8217;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1401320">https://bugzilla.redhat.com/1401320</a></p>
<dd> <font SIZE="-1">RFE:</font> Increate virt-sysprep coverage a bit</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1400205">https://bugzilla.redhat.com/1400205</a></p>
<dd> Add &#8211;vdsm-compat=1.1 flag for <font SIZE="-1">VDSM</font></p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1398070">https://bugzilla.redhat.com/1398070</a></p>
<dd> typo error in man page</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1392798">https://bugzilla.redhat.com/1392798</a></p>
<dd> secrets from libvirt domains are not read</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1390876">https://bugzilla.redhat.com/1390876</a></p>
<dd> &#8220;&#8211;machine-readable&#8221; info should be updated in virt-v2v manual page</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1379289">https://bugzilla.redhat.com/1379289</a></p>
<dd> <font SIZE="-1">RFE:</font> virt-p2v should support mnemonic operations</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1378022">https://bugzilla.redhat.com/1378022</a></p>
<dd> There is virt-v2v warning about &lt;listen type=&#8217;none&#8217;&gt; during converting a guest which has listen type=&#8217;none&#8217; in <font SIZE="-1">XML</font></p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1377081">https://bugzilla.redhat.com/1377081</a></p>
<dd> virt-p2v manual should update the new dialog information</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1375157">https://bugzilla.redhat.com/1375157</a></p>
<dd> virt-v2v: -i ova: Permission denied when using libvirt and running as root</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1374651">https://bugzilla.redhat.com/1374651</a></p>
<dd> Can&#8217;t install qxl driver for display device in win7 guest after converting to glance by virt-v2v</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1374405">https://bugzilla.redhat.com/1374405</a></p>
<dd> There is <font SIZE="-1">HTTP 404</font> error info when convert guest to glance by virt-v2v</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1374232">https://bugzilla.redhat.com/1374232</a></p>
<dd> selinux relabel fails on <font SIZE="-1">RHEL 6.2</font> guests with &#8220;libguestfs error: selinux_relabel: : Success&#8221;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1372668">https://bugzilla.redhat.com/1372668</a></p>
<dd> Process status is not normal in windows guest after converted from kvm to rhev by virt-v2v</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1372269">https://bugzilla.redhat.com/1372269</a></p>
<dd> Builder does not set hostname properly for Debian 8 (Jessie)</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1371843">https://bugzilla.redhat.com/1371843</a></p>
<dd> Improve <font SIZE="-1">OVA</font> import compatibility</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1370424">https://bugzilla.redhat.com/1370424</a></p>
<dd> virt-manager coredump when vm with gluster image exists</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1367839">https://bugzilla.redhat.com/1367839</a></p>
<dd> Cannot import VMs from Xen and VMware when using <font SIZE="-1">RHEL7.3</font> host.</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1367738">https://bugzilla.redhat.com/1367738</a></p>
<dd> Missing bash completion scripts for: virt-diff guestunmount virt-copy-in virt-copy-out virt-customize virt-get-kernel virt-p2v-make-disk virt-p2v-make-kickstart virt-tar-in virt-tar-out virt-v2v-copy-to-local virt-win-reg</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1367615">https://bugzilla.redhat.com/1367615</a></p>
<dd> <font SIZE="-1">OVMF</font> file which is built for rhel7.3 can&#8217;t be used for virt-v2v uefi conversion</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1366456">https://bugzilla.redhat.com/1366456</a></p>
<dd> Converting rhel7 host installed on RAID:warning: fstrim: fstrim: /sysroot/: the discard operation is not supported</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1366049">https://bugzilla.redhat.com/1366049</a></p>
<dd> <font SIZE="-1">RFE:</font> libvirt backend: support handling disks stored as volume name in a pool</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1365005">https://bugzilla.redhat.com/1365005</a></p>
<dd> Guest name is incorrect if convert guest from disk image by virt-v2v</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1362649">https://bugzilla.redhat.com/1362649</a></p>
<dd> <font SIZE="-1">RFE:</font> virt-sysprep does not utilize libguestfs encryption support</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1354507">https://bugzilla.redhat.com/1354507</a></p>
<dd> virt-v2v conversions from vCenter do not consistently obey the proxy environment variables</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1168144">https://bugzilla.redhat.com/1168144</a></p>
<dd> warning: fstrim: fstrim: /sysroot/: <font SIZE="-1">FITRIM</font> ioctl failed: Operation not supported (ignored) when convert win2003 guest from xen server</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1161019">https://bugzilla.redhat.com/1161019</a></p>
<dd> <font SIZE="-1">RFE:</font> Only install RHEV-APT if virt-v2v -o rhev/-o vdsm option is used</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1152369">https://bugzilla.redhat.com/1152369</a></p>
<dd> virt-v2v failed to convert <font SIZE="-1">RHEL 6.7 UEFI</font> guest: no grub1/grub-legacy or grub2 configuration file was found</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1141631">https://bugzilla.redhat.com/1141631</a></p>
<dd> [<font SIZE="-1">RFE</font>] virt-v2v should support convert a guest to a dir-pool with using pool&#8217;s uuid</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1134878">https://bugzilla.redhat.com/1134878</a></p>
<dd> libvirt reports json &#8220;backing file&#8221; is missing</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1019388">https://bugzilla.redhat.com/1019388</a></p>
<dd> firstboot scripts (virt-builder, virt-sysprep) don&#8217;t work for Debian 6 &amp; 7 guests</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/737600">https://bugzilla.redhat.com/737600</a></p>
<dd> virt-v2v windows xp &#8211; machine dies <font SIZE="-1">BSOD</font> &#8211; processr,sys &#8211; workaround provided</dl>
<h2>RELEASE NOTES FOR LIBGUESTFS 1.34</h2>
<p> These release notes only cover the differences from the previous stable/dev branch split (1.32.0). For detailed changelogs, please see the git repository, or the ChangeLog file distributed in the tarball.</p>
<h3>New features</h3>
<p> Multiple performance enhancements were made in libguestfs. The &#8220;hot cache&#8221; time to launch to appliance should be under 1 second assuming recent qemu and kernel are installed. There are also new utilities for precisely benchmarking libguestfs (<i>utils/boot-benchmark</i> and <i>utils/boot-analysis</i> in the source tree). </p>
<p> The virt-p2v tool for converting physical machines to virtual machines was substantially improved. This includes: clearer, coloured output during conversions, support for Gtk 3, more detailed information about hardware, click to identify network interfaces, more debugging tools included with the <font SIZE="-1">ISO,</font> and many bug fixes. </p>
<p> f2fs (Flash Friendly File System) is now supported (Pino Toscano). </p>
<p> <i>New tools</i> </p>
<p> <code><a href="/docs/linux/man/1-virt-p2v-make-kiwi/">virt-p2v-make-kiwi</a></code>(1) can be used to build the virt-p2v <font SIZE="-1">ISO</font> based on <font SIZE="-1">SLES</font> and openSUSE, using the kiwi utility (Cédric Bosdonnat). </p>
<p> <i>New features in existing tools</i> </p>
<p> virt-resize will now preserve the <font SIZE="-1">GPT GUID.</font> This was required for Windows Server 2012 R2, where the bootloader would become confused if the <font SIZE="-1">GUID</font> changed (Maxim Perevedentsev). </p>
<p> virt-resize will use sparse copying for (old MBR-style) extended partitions. This makes resizing of guests that use extended partitions much faster (Maxim Perevedentsev). </p>
<p> virt-p2v kernel command line options can now be used to set defaults for <font SIZE="-1">GUI</font> configuration. </p>
<p> The virt-p2v debugging options have been completely removed, simplifying the interface and documentation. Debugging information is now captured fully automatically. </p>
<p> virt-p2v-make-disk lets you specify an <i>&#8211;arch</i> option, allowing you to build a 32 bit virt-p2v, for compatibility with older systems. </p>
<p> virt-p2v-make-disk no longer requires that you specify an <tt>&quot;os-version&quot;</tt> for the virt-p2v disk. If omitted it will try to choose a suitable <tt>&quot;os-version&quot;</tt> depending on your host system. </p>
<p> virt-p2v-make-disk and virt-p2v-make-kickstart both gain a new <i>&#8211;install</i> option that allows you to add arbitrary extra packages to the virt-p2v <font SIZE="-1">ISO,</font> for customization, additional debugging tools and so on. </p>
<p> virt-v2v will now uninstall Parallels Tools (or the equivalent Virtuozzo Tools) from Linux guests. Also stop the Windows drivers from loading at boot. (Roman Kagan and Pavel Butsykin) </p>
<p> virt-v2v <i>&#8211;in-place</i> mode has been enhanced to allow the caller to choose whether or not to install certain virtio drivers in the guest (Roman Kagan). </p>
<p> virt-v2v conversion of Windows guests was substantially rewritten and simplified (Roman Kagan). </p>
<p> virt-v2v <i>&#8211;in-place</i> mode now supports installing virtio-scsi drivers in guests (Roman Kagan). </p>
<p> virt-v2v can now convert <font SIZE="-1">SUSE</font> guests and <font SIZE="-1">SUSE</font> guests using <font SIZE="-1">UEFI</font> (Cédric Bosdonnat and Jim Fehlig). </p>
<p> virt-v2v can now convert guests to Glance that have multiple disks. Previously it would fail on such guests. </p>
<p> The virt-v2v <i>&#8211;no-trim</i> and <i>&#8211;vmtype</i> options are now no-ops. They will print a warning but are otherwise ignored. virt-v2v can now generate the <font SIZE="-1">OVF</font> vmtype correctly without user intervention. </p>
<p> virt-v2v has now been tested against <font SIZE="-1">SUSE</font> Xen as a source hypervisor (Cédric Bosdonnat). </p>
<p> virt-v2v adds support for <font SIZE="-1">SUSE VMDP</font> drivers (Cédric Bosdonnat). </p>
<p> virt-v2v can convert <font SIZE="-1">OVA</font> files containing subfolders, as produced by <font SIZE="-1">SUSE</font> Studio (Cédric Bosdonnat). </p>
<p> virt-v2v sets the <font SIZE="-1">OVF</font> <tt>&quot;&lt;Origin&gt;&quot;</tt> element correctly. oVirt has been extended to support more source hypervisors (Shahar Havivi). </p>
<p> virt-v2v now supports Windows Server 2016 (Tomáš Golembiovský). </p>
<p> The virt-builder <i>&#8211;list</i> option can now be used to show all templates or a single template (Pino Toscano). </p>
<p> All OCaml-based tools now use <code><a href="/docs/linux/man/3-getopt_long/">getopt_long</a></code>(3) for option parsing, and <i>&#8211;help</i> output has been improved (Pino Toscano). </p>
<p> virt-builder and virt-customize <i>&#8211;selinux-relabel</i> option can now fully relabel the guest filesystem at build time, without requiring a lengthy autorelabel at first boot. </p>
<p> virt-customize <i>&#8211;delete</i> now accepts globs. </p>
<p> New virt-customize <i>&#8211;uninstall</i> option lets you uninstall packages. </p>
<p> virt-customize can now use <tt>&quot;pvvxsvc&quot;</tt> as an alternative to <tt>&quot;rhsrvany&quot;</tt> for running firstboot scripts in Windows guests (Cédric Bosdonnat). </p>
<p> virt-customize now uses the strongest hashing scheme for passwords on Arch and Void Linux (Pino Toscano). </p>
<p> virt-customize <i>&#8211;install</i> now works correctly on Arch (Pino Toscano). </p>
<p> virt-inspector has new options <i>&#8211;no-applications</i> and <i>&#8211;no-icon</i> to prevent the list of applications and icon from being included in the <font SIZE="-1">XML</font> output (Pino Toscano). </p>
<p> New virt-sysprep <i>&#8211;network</i> option has been added, allowing you to actually use the <i>&#8211;install</i> etc options which were present in virt-sysprep before but did not usually work. Note that the network is still disabled by default. </p>
<p> virt-sysprep <tt>&quot;fs-uuids&quot;</tt> operation no longer fails on btrfs guests (Maxim Perevedentsev). </p>
<p> virt-dib can output Docker images (Pino Toscano). </p>
<p> virt-dib has a new <i>&#8211;drive-format</i> option to allow the user to specify the format of the helper drive (Pino Toscano). </p>
<p> All OCaml virt tools now have a <i>&#8211;colors</i>/<i>&#8211;colours</i> option which enables coloured output (using <font SIZE="-1">ANSI</font> escape sequences) even if the output is not a tty. The default is to check if the output is a tty and disable coloured output if not. This allows coloured output to be consumed by other tools. </p>
<p> <i>Language bindings</i> </p>
<p> <font SIZE="-1">PHP</font> test coverage has been enhanced (Pino Toscano). </p>
<p> <font SIZE="-1">PHP 7</font> is now supported (Pino Toscano). </p>
<p> Python bindings are now compliant with <font SIZE="-1">PEP 8</font> (Pino Toscano). </p>
<p> A Python pip package is available in <a rel="nofollow" href="http://libguestfs.org/download/python/">http://libguestfs.org/download/python/</a> </p>
<p> The Ruby bindings now print the full exception if one is thrown by the event callback. Note this is still incorrect behaviour as event callbacks should not throw exceptions, but it aids debugging. </p>
<p> All OCaml libraries and programs are now compiled with <i>-safe-string</i>, if supported by the OCaml compiler. </p>
<p> <i>Inspection</i> </p>
<p> Alpine Linux using busybox can now be inspected. Also the <font SIZE="-1">APK</font> package manager is supported in virt-customize (Pino Toscano). </p>
<p> We now handle inspection of Mageia 4 (Pino Toscano). </p>
<p> Void Linux and the Void Linux xbps package manager are fully supported (Pino Toscano). </p>
<p> Parsing of CoreOS version information has been enhanced (Pino Toscano). </p>
<p> It is now possible to get an icon from <font SIZE="-1">ALT</font> Linux (Pino Toscano). </p>
<p> <font SIZE="-1">PLD</font> Linux versions &lt; 3 are now recognized (Pino Toscano). </p>
<p> Windows drive letters are now returned for guests using <font SIZE="-1">GPT</font> partitions (Dawid Zamirski). </p>
<p> We can now correctly inspect Unix guests that do not have an <i>/etc/fstab</i> file (Pino Toscano). </p>
<p> Added another source for the Ubuntu icon which doesn&#8217;t rely on <font SIZE="-1">GNOME</font> having been installed in the guest. </p>
<p> We can now get an icon for Windows 7 64 bit guests. </p>
<p> Libosinfo integration was rewritten to deal with the new database format used by osinfo (Pino Toscano). </p>
<p> <i>Documentation</i> </p>
<p> New manual page <code><a href="/docs/linux/man/1-guestfs-building/">guestfs-building</a></code>(1) describes how to build libguestfs from source. </p>
<p> The man pages, tools and tool <i>&#8211;help</i> output is now automatically checked to ensure that all tool options are properly documented, that warning sections are included where necessary, and that every page has a description section. </p>
<p> The <code><a href="/docs/linux/man/1-guestfs-testing/">guestfs-testing</a></code>(1) man page has been refreshed and based on a newer libguestfs. </p>
<p> <i>Architectures and platforms</i> </p>
<p> virt-customize now works on <font SIZE="-1">POWER7</font> and <font SIZE="-1">POWER8</font> platforms, both big endian and little endian (Xianghua Chen and Hu Zhang).</p>
<h3>Security</h3>
<p> See also <code><a href="/docs/linux/man/1-guestfs-security/">guestfs-security</a></code>(1). </p>
<p> <i></i><font SIZE="-1"><i>CVE-2015-8869</i></font><i></i> </p>
<p> <a rel="nofollow" href="https://bugzilla.redhat.com/CVE-2015-8869">https://bugzilla.redhat.com/CVE-2015-8869</a> </p>
<p> This vulnerability in OCaml might affect virt tools written in the OCaml programming language. It affects only 64 bit platforms. Because this bug affects code generation it is difficult to predict which precise software could be affected, and therefore our recommendation is that you recompile libguestfs using a version of the OCaml compiler where this bug has been fixed (or ask your Linux distro to do the same). </p>
<p> <i>virt-customize ownership of .ssh, .ssh/authorized_keys</i> </p>
<p> <a rel="nofollow" href="https://bugzilla.redhat.com/1337561">https://bugzilla.redhat.com/1337561</a> </p>
<p> Previously when virt-customize injected an <font SIZE="-1">SSH</font> key into a guest, when it created the <i>~/.ssh</i> and <i>~/.ssh/authorized_keys</i> directory and file (in case they were missing) it created them with owner and group <tt>&quot;root.root&quot;</tt>. This has been fixed so the correct user is used. This is not thought to have been exploitable. </p>
<p> <i>Windows </i>&quot;%systemroot%&quot;<i></i> </p>
<p> The inspection code has been made more robust against guests which might use very long <tt>&quot;%systemroot%&quot;</tt> (derived from the guest-controlled Windows Registry). This is not thought to have been exploitable. </p>
<p> <i>Virtio-rng is now available in the appliance</i> </p>
<p> virtio-rng (the virtual Random Number Generator device) is now passed to the appliance, which should improve the quality random numbers generated for GUIDs and cryptographic key generation.</p>
<h3><font SIZE="-1">API</font></h3>
<p> <i>New APIs</i></p>
<dl>
<dt>&quot;btrfs_filesystem_show&quot;</p>
<dd> List all devices where a btrfs filesystem is spanned (Pino Toscano).</p>
<dt>&quot;download_blocks&quot;</p>
<dd>
<dt>&quot;download_inode&quot;</p>
<dd>
<dt>&quot;filesystem_walk&quot;</p>
<dd> Download filesystem data blocks from a given partition. Download arbitrary files by inode number. Retrieve all files from a filesystem including deleted files. </p>
<p> Note these require optional dependency The Sleuth Kit. (Matteo Cafasso)</p>
<dt>&quot;get_sockdir&quot;</p>
<dd> Read the path where temporary sockets are stored (Pino Toscano).</p>
<dt>&quot;mountable_device&quot;</p>
<dd>
<dt>&quot;mountable_subvolume&quot;</p>
<dd> Split a Mountable into device name and subvolume (Cédric Bosdonnat).</p>
<dt>&quot;ntfscat_i&quot;</p>
<dd> Download <font SIZE="-1">NTFS</font> file by inode number (Matteo Cafasso).</p>
<dt>&quot;part_expand_gpt&quot;</p>
<dd> Allow in-place expanding of <font SIZE="-1">GPT</font> partitions by moving the second (backup) partition table to the end of the disk (Maxim Perevedentsev).</p>
<dt>&quot;part_get_disk_guid&quot;</p>
<dd>
<dt>&quot;part_set_disk_guid&quot;</p>
<dd>
<dt>&quot;part_set_disk_guid_random&quot;</p>
<dd> Get and set the <font SIZE="-1">GPT</font> disk <font SIZE="-1">GUID,</font> or set it to a fresh random value (Maxim Perevedentsev).</p>
<dt>&quot;selinux_relabel&quot;</p>
<dd> SELinux-relabel part or all of the guest filesystem.</dl>
<p> <i>Other </i><font SIZE="-1"><i>API</i></font><i> changes</i> </p>
<p> <tt>&quot;guestfs_set_selinux&quot;</tt>, <tt>&quot;guestfs_get_selinux&quot;</tt>, <tt>&quot;guestfs_setcon&quot;</tt>, <tt>&quot;guestfs_getcon&quot;</tt> and <tt>&quot;guestfs_llz&quot;</tt> have been deprecated. Use the new <font SIZE="-1">API</font> <tt>&quot;guestfs_selinux_relabel&quot;</tt> to relabel filesystems. Use <tt>&quot;guestfs_lgetxattrs&quot;</tt> to list the <tt>&quot;security.selinux&quot;</tt> extended attributes of existing files. </p>
<p> <tt>&quot;guestfs_vfs_minimum_size&quot;</tt> can now be used on dirty filesystems (Maxim Perevedentsev). </p>
<p> <tt>&quot;guestfs_ll&quot;</tt> now works on paths which contain absolute symlinks (Pino Toscano). </p>
<p> <tt>&quot;guestfs_glob_expand&quot;</tt> now has an optional <tt>&quot;directoryslash&quot;</tt> boolean parameter which controls whether trailing slashes are returned for directory names (Pino Toscano). </p>
<p> <tt>&quot;guestfs_lvs&quot;</tt> will no longer return LVs which have the <tt>&quot;activationskip&quot;</tt> flag set. The reason is that such LVs have no <tt>&quot;/dev/VG/LV&quot;</tt> device node and so code which read the list of LVs and then probed the devices themselves would immediately fail. You can use <tt>&quot;guestfs_lvs_full&quot;</tt> if you want to read all LVs. (Pino Toscano). </p>
<p> <tt>&quot;guestfs_list_disk_labels&quot;</tt> now no longer fails if no disks with labels were added. Instead it now returns an empty list (Pino Toscano). </p>
<p> <tt>&quot;guestfs_is_lv&quot;</tt> no longer fails if passed a btrfs subvolume, it returns false instead (Maxim Perevedentsev).</p>
<h3>Build changes</h3>
<p> qemu ≥ 1.3.0 is required. </p>
<p> yajl (a <font SIZE="-1">JSON</font> parsing library) is required to build libguestfs. </p>
<p> You can now build with <font SIZE="-1">GCC 6.</font> </p>
<p> <tt>&quot;make check-valgrind&quot;</tt> now has substantially better coverage. </p>
<p> <tt>&quot;make check-slow&quot;</tt> now works again. </p>
<p> Use <tt>&quot;make -C appliance clean-supermin-appliance&quot;</tt> to clean the supermin appliance (it will be rebuilt on next <tt>&quot;make&quot;</tt>). </p>
<p> There are a variety of new rules for running virt-p2v from the source directory: <tt>&quot;make -C p2v run-virt-p2v-directly&quot;</tt> | <tt>&quot;run-virt-p2v-in-a-vm&quot;</tt> | <tt>&quot;run-virt-p2v-non-gui-conversion&quot;</tt>. These are documented further in <code><a href="/docs/linux/man/1-guestfs-hacking/">guestfs-hacking</a></code>(1). </p>
<p> virt-p2v may be built using either Gtk 2 or Gtk 3. To force a particular version of Gtk to be used, <tt>&quot;./configure --with-gtk=2|3&quot;</tt> </p>
<p> The <tt>&quot;./configure&quot;</tt> options are now mostly documented in <code><a href="/docs/linux/man/1-guestfs-building/">guestfs-building</a></code>(1).</p>
<h3>Internals</h3>
<p> In git, versions are now tagged with <tt>&quot;v1.XX.YY&quot;</tt> (previously they were tagged with <tt>&quot;1.XX.YY&quot;</tt>). Using the <tt>&quot;v-&quot;</tt> prefix is more common in git repositories. </p>
<p> When using the libvirt backend, we now wait for qemu to exit gracefully instead of killing it after 15 seconds. This helps when writing to slow devices (especially cheap <font SIZE="-1">USB</font> keys). </p>
<p> Error messages from libvirt now include the <tt>&quot;err-&gt;int1&quot;</tt> field which usually contains the <tt>&quot;errno&quot;</tt>. </p>
<p> On <font SIZE="-1">ARM,</font> all <font SIZE="-1">DTB</font> (device tree) code has been removed. qemu creates the right device tree on the fly, we do not need to specify one. </p>
<p> The C <font SIZE="-1">API</font> tests now use larger test disks, allowing <font SIZE="-1">BTRFS</font> to be tested properly (Pino Toscano). </p>
<p> The tests should now work on a pure Python 3 host (Pino Toscano). </p>
<p> In C bindings, internal functions are now (mostly) consistently named <tt>&quot;guestfs_int_*&quot;</tt> whereas previously there was no consistent scheme. </p>
<p> The old <tt>&quot;safe_malloc&quot;</tt> etc functions are now no longer exported by the library, nor used in language bindings. </p>
<p> Setting <font SIZE="-1">TMPDIR</font> to a path longer than ~ 100 characters will no longer cause libguestfs to fail silently and randomly when creating Unix domain sockets (Pino Toscano). </p>
<p> The <tt>&quot;COMPILE_REGEXP&quot;</tt> macro can now be used in the daemon. </p>
<p> When tracing, results containing structs are now printed in full (Pino Toscano). </p>
<p> The Perl <tt>&quot;Sys::Guestfs&quot;</tt> module now no longer embeds an incrementing <font SIZE="-1">API</font> &#8220;version number&#8221;. This module is now always at phony version &#8220;1.0&#8221;. To find the real version of libguestfs from Perl you must call <tt>&quot;$g-&gt;version&quot;</tt>. </p>
<p> All code is compiled with <tt>&quot;-Wstack-usage=10000&quot;</tt> and multiple changes have been made to remove stack allocation of large strings and buffers. </p>
<p> The <code><a href="/docs/linux/man/3-error/">error</a></code>(3) function is now used everywhere, replacing most previous uses of <code><a href="/docs/linux/man/3-perror/">perror</a></code>(3) + <code><a href="/docs/linux/man/3-exit/">exit</a></code>(3), and <code><a href="/docs/linux/man/3-fprintf/">fprintf</a></code>(3) + exit. </p>
<p> In C code, <tt>&quot;/**&quot;</tt> comments are turned into documentation which is automatically added to the <code><a href="/docs/linux/man/1-guestfs-hacking/">guestfs-hacking</a></code>(1) manual page. </p>
<p> A safe &#8220;getumask&#8221; function has been added. For recent Linux kernels this uses the newly added <tt>&quot;Umask&quot;</tt> field in <i>/proc/self/status</i>. For older Linux and other Unix, this uses a thread-safe technique involving <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) (thanks: Josh Stone, Jiri Jaburek, Eric Blake). </p>
<p> Safe <code><a href="/docs/linux/man/2-posix_fadvise/">posix_fadvise</a></code>(2) wrappers have been added, and more hints have been added to the code which may make a minor difference to performance. </p>
<p> A safe wrapper around <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2) has been added which handles <tt>&quot;INTR&quot;</tt> properly. </p>
<p> <tt>&quot;podwrapper.pl&quot;</tt> (used to generate the manual pages) now stops if any <font SIZE="-1">POD</font> error is found. A new script called <tt>&quot;podcheck.pl&quot;</tt> does cross-checking of <i>&#8211;help</i> output, tool options and manual pages. </p>
<p> All version numbers in the library (eg. versions of qemu, versions of libvirt, versions of guest operating systems) are unified in a single file <i>src/version.c</i> (Pino Toscano). </p>
<p> On Windows guests, virt-customize will use the vendor-neutral path <tt>&quot;C:\Program Files\Guestfs\Firstboot&quot;</tt> to store firstboot scripts. Previously it used <tt>&quot;C:\Program Files\Red Hat\Firstboot&quot;</tt>. This change should be invisible to the scripts themselves. (Cédric Bosdonnat) </p>
<p> On Linux guests, the firstboot services generated by virt-builder <i>&#8211;firstboot</i> etc have been renamed to <tt>&quot;guestfs-firstboot&quot;</tt> (Pino Toscano). </p>
<p> There is now a common <tt>&quot;debug&quot;</tt> function used by all OCaml tools, replacing previous code which did <tt>&quot;if verbose () then printf ...&quot;</tt>. </p>
<p> virt-p2v copies files it needs over to the virt-v2v conversion server using <code><a href="/docs/linux/man/1-scp/">scp</a></code>(1), instead of trying to send them via the shell session. This should improve reliability and should be a completely transparent to end users. </p>
<p> All code in <i>mllib</i> is now built into a single <tt>&quot;mllib.cma&quot;</tt> or <tt>&quot;mllib.cmxa&quot;</tt> library. All code in <i>customize</i> is now built into a single <tt>&quot;customize.cma&quot;</tt> or <tt>&quot;customize.cmxa&quot;</tt> library. This simplifies the build of the OCaml tools. </p>
<p> <code><a href="/docs/linux/man/8-lvmetad/">lvmetad</a></code>(8) is now used in the appliance when available (Pino Toscano). </p>
<p> &#8220;Silent rules&#8221; are used for OCaml, Java, Erlang and <font SIZE="-1">POD.</font> Use <tt>&quot;make V=1&quot;</tt> to see the full command lines again (Pino Toscano).</p>
<h3>Bugs fixed</h3>
<dl>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1364347">https://bugzilla.redhat.com/1364347</a></p>
<dd> virt-sparsify &#8211;in-place failed with <font SIZE="-1">UEFI</font> system</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1362357">https://bugzilla.redhat.com/1362357</a></p>
<dd> run_command runs exit handlers when execve fails (e.g. due to missing executable)</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1362354">https://bugzilla.redhat.com/1362354</a></p>
<dd> virt-dib failed to create image using <font SIZE="-1">DIB_YUM_REPO_CONF</font></p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1359652">https://bugzilla.redhat.com/1359652</a></p>
<dd> Fail to inspect Windows <font SIZE="-1">ISO</font> file</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1358142">https://bugzilla.redhat.com/1358142</a></p>
<dd> Some info will show when convert guest to libvirt by virt-v2v with parameter &#8211;quiet</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1354335">https://bugzilla.redhat.com/1354335</a></p>
<dd> overlay of disk images does not specify the format of the backing file</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1352761">https://bugzilla.redhat.com/1352761</a></p>
<dd> Virt-manager can&#8217;t show <font SIZE="-1">OS</font> icons of win7/win8/ubuntu guest.</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1350363">https://bugzilla.redhat.com/1350363</a></p>
<dd> Improve error info &#8220;remote server timeout unexpectedly waiting for password prompt&#8221; when connect to a bogus server at p2v client</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1348900">https://bugzilla.redhat.com/1348900</a></p>
<dd> virt-p2v should update error prompt when &#8216;Test connection&#8217; with a non-existing user in conversion server</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1345813">https://bugzilla.redhat.com/1345813</a></p>
<dd> virt-sysprep &#8211;install always failed to install the packages specified</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1345809">https://bugzilla.redhat.com/1345809</a></p>
<dd> virt-customize &#8211;truncate-recursive should give an error message when specifying a no-existing path</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1343423">https://bugzilla.redhat.com/1343423</a></p>
<dd> [<font SIZE="-1">RFE</font>]Should give a better description about &#8216;curl error 22&#8217; when failed using ssh identity http url at p2v client</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1343414">https://bugzilla.redhat.com/1343414</a></p>
<dd> Failed <font SIZE="-1">SSH</font> to conversion server by ssh identity http url at p2v client</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1343375">https://bugzilla.redhat.com/1343375</a></p>
<dd> [<font SIZE="-1">RFE</font>] uninstall packages inside the <font SIZE="-1">VM</font></p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1342447">https://bugzilla.redhat.com/1342447</a></p>
<dd> Ifconfig command is not supported on p2v client</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1342398">https://bugzilla.redhat.com/1342398</a></p>
<dd> Convert a guest from <font SIZE="-1">RHEL</font> by virt-v2v but its origin info shows <font SIZE="-1">RHEV</font> at rhevm</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1342337">https://bugzilla.redhat.com/1342337</a></p>
<dd> Should remind a warning about disk image has a partition when using virt-p2v-make-disk</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1341984">https://bugzilla.redhat.com/1341984</a></p>
<dd> virt-get-kernel prompts an &#8216;invalid value&#8217; error when using &#8211;format auto</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1341564">https://bugzilla.redhat.com/1341564</a></p>
<dd> virt-p2v spinner should be hidden when it stops spinning</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1340809">https://bugzilla.redhat.com/1340809</a></p>
<dd> Testing connection timeout when input regular user of conversion server with checked &#8220;use sudo&#8230;&#8230;&#8221;button</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1340464">https://bugzilla.redhat.com/1340464</a></p>
<dd> [<font SIZE="-1">RFE</font>] Suggestion give user a reminder for &#8220;Cancel conversion&#8221; button</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1340407">https://bugzilla.redhat.com/1340407</a></p>
<dd> Multiple network ports will not be aligned at p2v client</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1338083">https://bugzilla.redhat.com/1338083</a></p>
<dd> Update <font SIZE="-1">UEFI</font> whitelist for official fedora packages</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1337561">https://bugzilla.redhat.com/1337561</a></p>
<dd> virt-customize &#8211;ssh-inject not applying correct file permission</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1335671">https://bugzilla.redhat.com/1335671</a></p>
<dd> extra quotes around <font SIZE="-1">UUID</font> confuses findfs in <font SIZE="-1">RHEL</font> (but not in Fedora)</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1332025">https://bugzilla.redhat.com/1332025</a></p>
<dd> Inspection does not parse /etc/redhat-release containing &#8220;Derived from Red Hat Enterprise Linux 7.1 (Source)&#8221;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1327488">https://bugzilla.redhat.com/1327488</a></p>
<dd> <font SIZE="-1">RFE:</font> Allow p2v kernel options without p2v.server to set defaults</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1325825">https://bugzilla.redhat.com/1325825</a></p>
<dd> virt-v2v should prevent using multiple &#8216;-b&#8217; and &#8216;-n&#8217; option appears on the command line</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1321620">https://bugzilla.redhat.com/1321620</a></p>
<dd> libguestfs: error: could not parse integer in version number: 7&quot;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1321338">https://bugzilla.redhat.com/1321338</a></p>
<dd> [1.33.16] Compilation Error: Unbound value List.sort_uniq in v2v.ml line 988, characters 10-24:</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1317843">https://bugzilla.redhat.com/1317843</a></p>
<dd> `virt-builder &#8211;update` fails with: &#8220;dnf -y &#8211;best upgrade: command exited with an error&#8221;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1316479">https://bugzilla.redhat.com/1316479</a></p>
<dd> v2v cmd cannot exit and &#8220;block I/O error in device &#8216;appliance&#8217;: No space left on device (28)&#8221; is printed when specified &#8220;-v -x&#8221;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1316041">https://bugzilla.redhat.com/1316041</a></p>
<dd> virt-rescue fails, but missing error message</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1314244">https://bugzilla.redhat.com/1314244</a></p>
<dd> <font SIZE="-1">RFE:</font> virt-p2v log window should process colour escapes and backspaces</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1312254">https://bugzilla.redhat.com/1312254</a></p>
<dd> virt-v2v -o libvirt doesn&#8217;t preserve or use correct &lt;graphics type=&#8220;vnc|spice&#8221;&gt;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1309706">https://bugzilla.redhat.com/1309706</a></p>
<dd> error: internal error: Invalid floppy device name: hdb</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1309619">https://bugzilla.redhat.com/1309619</a></p>
<dd> Wrong warning info &#8220;use standard <font SIZE="-1">VGA&#8221;</font> shows when converting windows &gt; 7 by virt-v2v</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1309580">https://bugzilla.redhat.com/1309580</a></p>
<dd> <font SIZE="-1">OS</font> name of win8.1 x64 guest shows incorrect in rhevm3.6 general info</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1308769">https://bugzilla.redhat.com/1308769</a></p>
<dd> virt-v2v does not copy additional disks to Glance</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1306666">https://bugzilla.redhat.com/1306666</a></p>
<dd> Failure when disk contains an <font SIZE="-1">LV</font> with activationskip=y</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1296606">https://bugzilla.redhat.com/1296606</a></p>
<dd> virt-v2v doesn&#8217;t remove VirtualBox additions correctly because of file quoting</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1293527">https://bugzilla.redhat.com/1293527</a></p>
<dd> There should be a reminder to avoid user to edit a guest image by multiple tools at the same time in guestfish man page</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1293276">https://bugzilla.redhat.com/1293276</a></p>
<dd> guestfish can not ll a symbolic link dir or edit a file in it</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1278878">https://bugzilla.redhat.com/1278878</a></p>
<dd> guestfish should be able to handle <font SIZE="-1">LVM</font> thin layouts</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1264835">https://bugzilla.redhat.com/1264835</a></p>
<dd> ppc64le: virt-customize &#8211;install fail to detect the guest arch</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1264332">https://bugzilla.redhat.com/1264332</a></p>
<dd> Test that trimming in virt-v2v doesn&#8217;t regress</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1232192">https://bugzilla.redhat.com/1232192</a></p>
<dd> Virt-v2v gives an error on a blank disk: part_get_parttype: unknown signature, of the output: <font SIZE="-1">BYT</font>;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1229386">https://bugzilla.redhat.com/1229386</a></p>
<dd> virt-p2v in non-GUI mode doesn&#8217;t show any conversion progress or status</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1227599">https://bugzilla.redhat.com/1227599</a></p>
<dd> P2V invalid password prints unexpected end of file waiting for command prompt.</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1224795">https://bugzilla.redhat.com/1224795</a></p>
<dd> On Ubuntu, virt-builder &#8211;install and &#8211;update cannot use the network</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1213324">https://bugzilla.redhat.com/1213324</a></p>
<dd> virt-v2v: warning: unknown guest operating system: windows windows 6.3 when converting win8,win8.1,win2012,win2012R2,win10 to rhev</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1203898">https://bugzilla.redhat.com/1203898</a></p>
<dd> Support inspecting docker images without /etc/fstab</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1186935">https://bugzilla.redhat.com/1186935</a></p>
<dd> libguestfs cannot inspect recent Fedora / <font SIZE="-1">RHEL</font> &gt;= 7 when /usr is a separate partition</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1167916">https://bugzilla.redhat.com/1167916</a></p>
<dd> P2V: invalid conversion server prints unexpected end of file waiting for password prompt.</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1152825">https://bugzilla.redhat.com/1152825</a></p>
<dd> virt-rescue &#8211;selinux can not work well, when enable selinux in the command line the value of &#8216;getenforce&#8217; is still Disabled in virt-rescue appliance</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1150298">https://bugzilla.redhat.com/1150298</a></p>
<dd> <font SIZE="-1">ARM 32</font> bit on Ubuntu: warning: cast to pointer from integer of different size [-Wint-to-pointer-cast]</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1089100">https://bugzilla.redhat.com/1089100</a></p>
<dd> NetworkManager avc unlink denied for resolv.conf after using &#8211;selinux-relabel</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/983969">https://bugzilla.redhat.com/983969</a></p>
<dd> <font SIZE="-1">RFE:</font> virt-sysprep should be SELinux-aware</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/855058">https://bugzilla.redhat.com/855058</a></p>
<dd> <font SIZE="-1">RFE:</font> virt-p2v: display more information about storage devices</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/554829">https://bugzilla.redhat.com/554829</a></p>
<dd> SELinux handling could be done better.</dl>
<h2>RELEASE NOTES FOR LIBGUESTFS 1.32</h2>
<p> These release notes only cover the differences from the previous stable/dev branch split (1.30.0). For detailed changelogs, please see the git repository, or the ChangeLog file distributed in the tarball.</p>
<h3>New features</h3>
<p> <i>New tools</i> </p>
<p> The new <code><a href="/docs/linux/man/1-virt-v2v-copy-to-local/">virt-v2v-copy-to-local</a></code>(1) tool is an ancillary tool for <code><a href="/docs/linux/man/1-virt-v2v/">virt-v2v</a></code>(1) allowing you to convert source guests that virt-v2v is unable to access directly. </p>
<p> <i>New features in existing tools</i> </p>
<p> Virt-customize knows how to write a random seed to CirrOS (Pino Toscano). </p>
<p> On Fedora, virt-customize runs <code><a href="/docs/linux/man/8-dnf/">dnf</a></code>(8) with the <i>&#8211;best</i> flag, ensuring it always updates to the latest available packages. </p>
<p> Virt-builder now provides 32 bit Fedora templates. </p>
<p> Virt-builder and virt-customize <i>&#8211;install</i> option now works on 32 bit Fedora guests. Previously it would try to install 64 bit packages (Jan Sedlák). </p>
<p> Virt-builder can now fetch cloud images using Simple Streams v1.0 metadata (Pino Toscano). </p>
<p> Virt-builder can now fetch openSUSE cloud images out of the box (Cédric Bosdonnat). </p>
<p> Virt-customize will now use stronger (<font SIZE="-1">SHA-512</font>) encrypted passwords by default on openSUSE ≥ 11 (Pino Toscano). </p>
<p> Virt-builder will now correctly handle output filenames containing colon characters (<tt>&quot;:&quot;</tt>), and will create temporary files in the libguestfs cache directory instead of defaulting to <i>/tmp</i> (Pino Toscano). </p>
<p> Virt-resize has a new <i>&#8211;unknown-filesystems</i> option to control what to do when asked to resize a filesystem that libguestfs doesn&#8217;t know how to resize. </p>
<p> Virt-v2v now has an <i>&#8211;in-place</i> flag/mode, allowing in-place conversion of guests (Roman Kagan). </p>
<p> Virt-v2v has a <i>&#8211;compressed</i> option for creating compressed qcow2 output files. </p>
<p> Virt-v2v can now correctly get the VMware datacenter path (dcPath) from libvirt, instead of having to calculate it using an algorithm that occasionally got the wrong answer (Matthias Bolte, Tingting Zheng). </p>
<p> Virt-v2v now processes <font SIZE="-1">RAM</font> sizes correctly for 64 bit guests when running on a 32 bit host. </p>
<p> <i>Language bindings</i> </p>
<p> In Perl and Python programs, the <tt>&quot;get_program_name&quot;</tt> <font SIZE="-1">API</font> now returns the true program name, instead of the incorrect string <tt>&quot;perl&quot;</tt> or <tt>&quot;python&quot;</tt>. </p>
<p> The Python bindings can now be compiled against a different version of libguestfs, allowing the pip module to be built against any version of libguestfs (instead of requiring the pip module and libguestfs to have exactly the same version). </p>
<p> The quality of the Ruby rdoc (documentation) has been improved (Pino Toscano). </p>
<p> Perl scripts no longer hard-code the location of perl in the shebang line, but use <code><a href="/docs/linux/man/1-env/">env</a></code>(1) to locate it instead (Pino Toscano). </p>
<p> In OCaml programs, the guestfs handle was incorrectly made into a global root, meaning it could never be garbage collected. If you didn&#8217;t call the <tt>&quot;close&quot;</tt> function explicitly, the handle would not be closed until the whole program exited. This has now been fixed so handles will be garbage collected in the usual way. This changes the <font SIZE="-1">API</font> of the OCaml function <tt>&quot;Guestfs.event_callback&quot;</tt>. Note that non-C language bindings are not covered by the libguestfs <font SIZE="-1">API/ABI</font> guarantee, although we try hard not to change them, but in this case it was essential in order to fix this very serious bug. </p>
<p> <i>Inspection</i> </p>
<p> Alpine Linux and the <font SIZE="-1">APK</font> package manager, <font SIZE="-1">ALT</font> Linux, Frugalware, and <font SIZE="-1">PLD</font> Linux are now recognized (Pino Toscano). </p>
<p> If it exists, <i>/etc/os-release</i> will be preferred for inspecting Linux guests (Pino Toscano). </p>
<p> The correct kernel version is returned for Windows guests ≥ 10. </p>
<p> <i>Documentation</i> </p>
<p> The large <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3) man page has been split into several separate man pages: <code><a href="/docs/linux/man/1-guestfs-hacking/">guestfs-hacking</a></code>(1) <code><a href="/docs/linux/man/1-guestfs-internals/">guestfs-internals</a></code>(1) <code><a href="/docs/linux/man/1-guestfs-security/">guestfs-security</a></code>(1). In the source tree, a new <i>docs</i> directory contains this documentation. </p>
<p> <i>Architectures and platforms</i> </p>
<p> Libguestfs now supports <font SIZE="-1">ARM 64</font> bit platforms with vGICv3.</p>
<h3>Security</h3>
<p> See also <code><a href="/docs/linux/man/1-guestfs-security/">guestfs-security</a></code>(1).</p>
<dl>
<dt>&quot;CVE-2015-5745&quot;</p>
<dd> <a rel="nofollow" href="https://bugzilla.redhat.com/1251157">https://bugzilla.redhat.com/1251157</a> </p>
<p> This is not a vulnerability in libguestfs, but because we always give a virtio-serial port to each guest (since that is how guest-host communication happens), an escalation from the appliance to the host qemu process is possible. This could affect you if:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> your libguestfs program runs untrusted programs out of the guest (using &#8220;guestfs_sh&#8221; etc), or</p>
<dt>&bull;</p>
<dd> another exploit was found in (for example) kernel filesystem code that allowed a malformed filesystem to take over the appliance.</dl>
</dl>
<dl>
<dt>
<dd>
<p> If you use sVirt to confine qemu, that would thwart some attacks.</dl>
<dt>Virt-customize permissions on <i>.ssh</i>, <i>.ssh/authorized_keys</i></p>
<dd> <a rel="nofollow" href="https://bugzilla.redhat.com/1260778.">https://bugzilla.redhat.com/1260778.</a> </p>
<p> Previously when asked to inject an <font SIZE="-1">SSH</font> key into a guest, virt-customize (hence virt-builder too) would create the <i>.ssh</i> directory and <i>.ssh/authorized_keys</i> file with too broad permissions, allowing other users to read. They are now created as <tt>0700</tt> and <tt>0600</tt> respectively, which is the same as the <code><a href="/docs/linux/man/1-ssh-copy-id/">ssh-copy-id</a></code>(1) utility.</dl>
<h3><font SIZE="-1">API</font></h3>
<p> <i>New APIs</i></p>
<dl>
<dt>&quot;guestfs_get_identifier&quot;</p>
<dd>
<dt>&quot;guestfs_set_identifier&quot;</p>
<dd> Get/set a per-handle identifier. The main effect of this is to change trace output from: </p>
<pre>
 libguestfs: trace: foo
</pre>
<p> to: </p>
<pre>
 libguestfs: trace: ID: foo
</pre>
<p> making it easier to follow traces in multi-threaded programs, or where a program uses multiple handles (especially virt-v2v).</p>
<dt>&quot;guestfs_vfs_minimum_size&quot;</p>
<dd> Return the minimum size of a filesystem (when shrunk). This supports ext2/3/4, <font SIZE="-1">XFS</font> and btrfs, and can support other filesystem types in future (Maxim Perevedentsev).</dl>
<p> <i>Other </i><font SIZE="-1"><i>API</i></font><i> changes</i></p>
<dl>
<dt>&quot;guestfs_disk_create&quot;: add &quot;preallocation&quot; = &quot;off&quot;/&quot;metadata&quot;/&quot;full&quot;.</p>
<dd> For raw, this allows <tt>&quot;off&quot;</tt> as a synonym for <tt>&quot;sparse&quot;</tt> (making it consistent with qcow2). For qcow2, this allows <tt>&quot;sparse&quot;</tt> as a synonym for <tt>&quot;off&quot;</tt>. </p>
<p> It also adds <tt>&quot;full&quot;</tt>, which corresponds to fully allocated, but uses <code><a href="/docs/linux/man/3-posix_fallocate/">posix_fallocate</a></code>(3) for efficiency.</p>
<dt>&quot;guestfs_tar_in&quot;: new &quot;xattrs&quot;, &quot;selinux&quot;, &quot;acl&quot; parameters.</p>
<dd>
<dt>&quot;guestfs_tar_out&quot;: new &quot;xattrs&quot;, &quot;selinux&quot;, &quot;acl&quot; parameters.</p>
<dd> These extra parameters control whether extended attributes, SELinux contexts and/or <font SIZE="-1">POSIX</font> ACLs are restored from / saved to tarballs.</p>
<dt>&quot;guestfs_add_drive&quot;</p>
<dd> The existing <tt>&quot;username&quot;</tt> and <tt>&quot;secret&quot;</tt> parameters can be used to supply authentication for iSCSI (Pino Toscano).</dl>
<h3>Build changes</h3>
<p> The <tt>&quot;./configure --enable-valgrind-daemon&quot;</tt> option has been removed. </p>
<p> You can no longer build libguestfs on <font SIZE="-1">RHEL</font> 5-era (c.2007) machines. See the <tt>&quot;oldlinux&quot;</tt> branch if you need (limited) <font SIZE="-1">RHEL 5</font> support. </p>
<p> Virt-p2v can now be built on <font SIZE="-1">RHEL</font> 6-era (c.2010) Linux distros. </p>
<p> OCaml ≥ 3.11 (released in 2008) is now required to build from git. </p>
<p> Building the Perl bindings now requires <tt>&quot;Module::Build&quot;</tt> (instead of <tt>&quot;ExtUtils::MakeMaker&quot;</tt>). </p>
<p> Builds should be faster (especially when incrementally rebuilding), because work was done to reduce build times. </p>
<p> Both OCaml and the OCaml findlib module are required if you need to run the generator at build time. Previously the build would have failed if findlib was not installed. </p>
<p> <tt>&quot;make check&quot;</tt> tests now run in parallel (within each test directory). </p>
<p> <tt>&quot;make install&quot;</tt> no longer installs OCaml <i>bindtests.*</i> files incorrectly. </p>
<p> <tt>&quot;make install&quot;</tt> can now be run twice. Previously it would fail on the second run. </p>
<p> <tt>&quot;make clean&quot;</tt> should now remove nearly every file that <tt>&quot;make&quot;</tt> creates. </p>
<p> A new <tt>&quot;make installcheck&quot;</tt> rule has been added, allowing the installed copy of libguestfs to be tested.</p>
<h3>Internals</h3>
<p> Some effort was put into minimizing the size of the appliance, which reduces temporary disk space and time needed by libguestfs handles. </p>
<p> The appliance now passes the <font SIZE="-1">NIC</font> name to dhcpd, fixing hangs when running the appliance on some distros (Cédric Bosdonnat). </p>
<p> OCaml <tt>&quot;Guestfs.Errno&quot;</tt> is now generated (Pino Toscano). </p>
<p> In OCaml tools, common code now handles <i>&#8211;debug-gc</i>, <i>&#8211;verbose</i> and other common options (Roman Kagan, Pino Toscano). </p>
<p> The virt-v2v test harness allows us to boot the test guests at fixed dates in the past, ensuring that Windows reactivation doesn&#8217;t kick in. </p>
<p> There is a new internal <font SIZE="-1">API</font> for reading/writing a subprocess via a pipe from library code. </p>
<p> Used <tt>&quot;deheader&quot;</tt> program to remove unused <tt>&quot;#include&quot;</tt> directives. </p>
<p> In OCaml tools, the <tt>&quot;Char&quot;</tt> and <tt>&quot;String&quot;</tt> modules now implicitly reference the <tt>&quot;Common_utils.Char&quot;</tt> and <tt>&quot;Common_utils.String&quot;</tt> modules (instead of the ones from stdlib). The <tt>&quot;Common_utils&quot;</tt> modules contain a number of extra char/string utility functions, and also hide some unsafe functions in stdlib. </p>
<p> Many more virt-v2v tests will now be run even if you don&#8217;t have rhsrvany and virtio-win installed (Roman Kagan). </p>
<p> The huge <i>configure.ac</i> file has been split into several smaller files called <i>m4/guestfs_*.m4</i>. </p>
<p> The old <i>tests/data</i> and <i>tests/guests</i> directories have been moved to <i>test-data/</i>. This new top level directory carries all test data which is common, large and/or shared between multiple tests. </p>
<p> There is a new top level <i>website/</i> directory containing the public <a rel="nofollow" href="http://libguestfs.org">http://libguestfs.org</a> website (or most of it). </p>
<p> The fuzz testing of inspection (<i>tests/fuzz</i>) has been removed. </p>
<p> Virt-p2v now saves the source physical machine dmesg output into the conversion server debug directory, making it simpler to debug cases of missing drivers, firmware etc.</p>
<h3>Bugs fixed</h3>
<dl>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1294956">https://bugzilla.redhat.com/1294956</a></p>
<dd> set-label returns wrong error message when set the ext3/ext4 filesystem label</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1288733">https://bugzilla.redhat.com/1288733</a></p>
<dd> Add a Fedora 23 32-bit base image for virt-builder</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1288201">https://bugzilla.redhat.com/1288201</a></p>
<dd> virt-builder writes temporary files to /tmp</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1285847">https://bugzilla.redhat.com/1285847</a></p>
<dd> virt-resize does not copy logical partitions</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1281578">https://bugzilla.redhat.com/1281578</a></p>
<dd> virt-inspector returns version 6.3 for win10 images (should return 10.0)</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1281577">https://bugzilla.redhat.com/1281577</a></p>
<dd> virt-inspector &#8211;xpath segfault on attribute get</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1280029">https://bugzilla.redhat.com/1280029</a></p>
<dd> libguestfs can run commands with stdin not open (or worse still, connected to arbitrary guest-chosen random devices)</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1279273">https://bugzilla.redhat.com/1279273</a></p>
<dd> About compression option for qcow2</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1278878">https://bugzilla.redhat.com/1278878</a></p>
<dd> guestfish should be able to handle <font SIZE="-1">LVM</font> thin layouts</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1278382">https://bugzilla.redhat.com/1278382</a></p>
<dd> <font SIZE="-1">DNF</font> python programming error when run from virt-builder</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1278371">https://bugzilla.redhat.com/1278371</a></p>
<dd> inspection returns arch=&#8220;unknown&#8221; for Windows guest if file command is not installed</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1277274">https://bugzilla.redhat.com/1277274</a></p>
<dd> Document permissions needed for non-admin users to use virt-v2v</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1277122">https://bugzilla.redhat.com/1277122</a></p>
<dd> <font SIZE="-1">RFE:</font> virt-sparsify: make &#8216;&#8211;in-place&#8217; sparsification safe to abort (gracefully or ungracefully)</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1277074">https://bugzilla.redhat.com/1277074</a></p>
<dd> Virt-p2v client shouldn&#8217;t present the vdsm option because it&#8217;s not usable</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1276540">https://bugzilla.redhat.com/1276540</a></p>
<dd> virt-v2v fails to convert Windows raw image: error &#8220;device name is not a partition&#8221;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1275806">https://bugzilla.redhat.com/1275806</a></p>
<dd> virt-builder: error: [file] is not a regular file in the guest</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1270011">https://bugzilla.redhat.com/1270011</a></p>
<dd> Simplestreams test fails: virt-builder: error: the value for the key &#8216;size&#8217; is not an integer</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1267032">https://bugzilla.redhat.com/1267032</a></p>
<dd> guestfish copy-in command behaves oddly/unexpectedly with wildcards</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1262983">https://bugzilla.redhat.com/1262983</a></p>
<dd> python: Cannot compile pip module if installed libguestfs != pip guestfs version</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1262127">https://bugzilla.redhat.com/1262127</a></p>
<dd> Better diagnostic message when virbr0 doesn&#8217;t exist</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1261436">https://bugzilla.redhat.com/1261436</a></p>
<dd> No warning shows when convert a win7 guest with <font SIZE="-1">AVG</font> AntiVirus installed</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1260778">https://bugzilla.redhat.com/1260778</a></p>
<dd> virt-builder &#8211;ssh-inject doesn&#8217;t set proper permissions on created files</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1260689">https://bugzilla.redhat.com/1260689</a></p>
<dd> <font SIZE="-1">RFE: V2V</font> to check and warn user to disable group policy and anti virus on Windows guests</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1260590">https://bugzilla.redhat.com/1260590</a></p>
<dd> Wrong graphics protocal and video type set for guest after convert to rhev 3.6 by virt-v2v</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1258342">https://bugzilla.redhat.com/1258342</a></p>
<dd> extra slashes in vcenter <font SIZE="-1">URL</font> confuses virt-v2v</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1257895">https://bugzilla.redhat.com/1257895</a></p>
<dd> [<font SIZE="-1">RHEV</font>][V2V] virt-v2v ignores <font SIZE="-1">NIC</font> if interface source/@network or source/@bridge is an empty string</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1256405">https://bugzilla.redhat.com/1256405</a></p>
<dd> virt-builder created Fedora 22 32bit disk image cannot be updated</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1256222">https://bugzilla.redhat.com/1256222</a></p>
<dd> virt-p2v no <font SIZE="-1">GUI</font> mode:error opening control connection to <tt>$ip:22:unexpected</tt> …rompt</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1251909">https://bugzilla.redhat.com/1251909</a></p>
<dd> Option -oa preallocated -of qcow2 of virt-v2v didn&#8217;t work efficiently</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1250715">https://bugzilla.redhat.com/1250715</a></p>
<dd> v2v: spaces need to be escaped as <tt>%20</tt> in paths</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1248678">https://bugzilla.redhat.com/1248678</a></p>
<dd> Close all incoming ports on virt-p2v <font SIZE="-1">ISO</font></p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1246882">https://bugzilla.redhat.com/1246882</a></p>
<dd> man virt-customize shows synopsis twice</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1242853">https://bugzilla.redhat.com/1242853</a></p>
<dd> mount-loop failed to setup loop device: No such file or directory</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1237136">https://bugzilla.redhat.com/1237136</a></p>
<dd> <font SIZE="-1">BUG:</font> unable to handle kernel <font SIZE="-1">NULL</font> pointer dereference at &lt;addr&gt; in function __blkg_lookup</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1230412">https://bugzilla.redhat.com/1230412</a></p>
<dd> virt-v2v should ignore bogus kernel entries in grub config</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1229119">https://bugzilla.redhat.com/1229119</a></p>
<dd> Unrelated info in fstab makes virt-v2v fail with unclear error info</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1227609">https://bugzilla.redhat.com/1227609</a></p>
<dd> virt-p2v: Using &#8220;Back&#8221; button causes output list to be repopulated multiple times</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1225789">https://bugzilla.redhat.com/1225789</a></p>
<dd> Wrong video driver is installed for rhel5.11 guest after conversion to libvirt</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1204131">https://bugzilla.redhat.com/1204131</a></p>
<dd> <font SIZE="-1">RFE:</font> virt-builder creates qcow v3 images, add build option for qcow v2</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1176801">https://bugzilla.redhat.com/1176801</a></p>
<dd> File /etc/sysconfig/kernel isn&#8217;t updated when convert XenPV guest with regular kernel installed</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1174551">https://bugzilla.redhat.com/1174551</a></p>
<dd> &#8220;lstatnslist&#8221; and &#8220;lstatlist&#8221; don&#8217;t give an error if the <font SIZE="-1">API</font> is used wrongly</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1168223">https://bugzilla.redhat.com/1168223</a></p>
<dd> koji spin-livecd cannot build a working live <font SIZE="-1">CD</font></p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1165785">https://bugzilla.redhat.com/1165785</a></p>
<dd> mount-loop command fails: mount failed: Unknown error -1</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1164708">https://bugzilla.redhat.com/1164708</a></p>
<dd> set-label can only set &lt;=127 bytes for btrfs and &lt;=126 bytes for ntfs filesystem which not meet the help message. Also for ntfs it should give a warning message when the length &gt;128 bytes</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1020216">https://bugzilla.redhat.com/1020216</a></p>
<dd> libvirt fails to shut down domain: could not destroy libvirt domain: Requested operation is not valid: domain is not running</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1011907">https://bugzilla.redhat.com/1011907</a></p>
<dd> mount-loop failed to setup loop device: No such file or directory</dl>
<h2>RELEASE NOTES FOR LIBGUESTFS 1.30</h2>
<p> These release notes only cover the differences from the previous stable/dev branch split (1.28.0). For detailed changelogs, please see the git repository, or the ChangeLog file distributed in the tarball.</p>
<h3>New features</h3>
<p> <i>New tools</i> </p>
<p> <code><a href="/docs/linux/man/1-virt-dib/">virt-dib</a></code>(1) is a secure and safe alternative to the OpenStack &#8220;diskimage-builder&#8221; tool. It is compatible with diskimage-builder elements. (Pino Toscano) </p>
<p> <code><a href="/docs/linux/man/1-virt-get-kernel/">virt-get-kernel</a></code>(1) extracts the kernel and ramdisk from a disk image. Previously this functionality was part of <code><a href="/docs/linux/man/1-virt-builder/">virt-builder</a></code>(1), but the new tool is more featureful. (Pino Toscano) </p>
<p> <i>New features in existing tools</i> </p>
<p> <code><a href="/docs/linux/man/1-virt-v2v/">virt-v2v</a></code>(1) <i>-i ova</i> mode can now read a wider range of <font SIZE="-1">OVA</font> files, and also unpacked files (directories). </p>
<p> virt-v2v now securely passes options to curl, so passwords, cookies and so on cannot be seen by users with shell access on the same machine. </p>
<p> virt-v2v has a new <i>&#8211;password-file</i> option to allow you to securely pass in a password, and to avoid an interactive prompt. </p>
<p> virt-v2v disables Windows autoreboot, making debugging conversion failures on Windows easier. </p>
<p> virt-v2v now comes with an extensive external test suite. See <code><a href="/docs/linux/man/1-virt-v2v-test-harness/">virt-v2v-test-harness</a></code>(1). </p>
<p> virt-v2v allows virtio drivers to come from any location (Roman Kagan), and drivers can be read directly from the virtio <font SIZE="-1">ISO.</font> </p>
<p> virt-v2v supports conversion of Windows ≥ 8. Note this is experimental, and possibly broken. Use with caution. </p>
<p> virt-v2v can now convert <font SIZE="-1">UEFI</font> guests. </p>
<p> <code><a href="/docs/linux/man/1-virt-p2v/">virt-p2v</a></code>(1) adds a network configuration dialog. </p>
<p> virt-p2v now has <tt>&quot;p2v.pre&quot;</tt>, <tt>&quot;p2v.post&quot;</tt> and <tt>&quot;p2v.fail&quot;</tt> triggers, allowing arbitrary scripts for preparing the host for conversion and tidying up post-conversion. </p>
<p> virt-p2v now uses the more advanced metacity window manager (instead of matchbox). </p>
<p> <code><a href="/docs/linux/man/1-virt-sysprep/">virt-sysprep</a></code>(1) will remove <tt>&quot;/var/spool/mail/username&quot;</tt> for non-root accounts (Hu Tao). </p>
<p> <code><a href="/docs/linux/man/1-virt-customize/">virt-customize</a></code>(1), <code><a href="/docs/linux/man/1-virt-builder/">virt-builder</a></code>(1) and virt-sysprep have the following new options:</p>
<dl>
<dt><i>&#8211;commands-from-file</i></p>
<dd> allow long lists of commands to be read from a file instead of from the command line (Pino Toscano)</p>
<dt><i>&#8211;copy</i></p>
<dd> copy files inside the guest (Maros Zatko)</p>
<dt><i>&#8211;copy-in</i></p>
<dd> copy host files recursively into the guest (Pino Toscano)</p>
<dt><i>&#8211;move</i></p>
<dd> move files inside the guest (Maros Zatko)</p>
<dt><i>&#8211;ssh-inject</i></p>
<dd> inject <font SIZE="-1">SSH</font> keys into a guest (Pino Toscano)</p>
<dt><i>&#8211;sm-attach</i></p>
<dd>
<dt><i>&#8211;sm-credentials</i></p>
<dd>
<dt><i>&#8211;sm-register</i></p>
<dd>
<dt><i>&#8211;sm-remove</i></p>
<dd>
<dt><i>&#8211;sm-unregister</i></p>
<dd> register and unregister a guest from subscription-manager (Pino Toscano)</p>
<dt><i>&#8211;touch</i></p>
<dd> touch a file in the guest (Pino Toscano)</p>
<dt><i>&#8211;truncate</i></p>
<dd>
<dt><i>&#8211;truncate-recursive</i></p>
<dd> truncate files (Maros Zatko)</dl>
<p> Improvements to virt-customize firstboot support. In particular, Windows firstboot should work as well as Linux (Roman Kagan). </p>
<p> <code><a href="/docs/linux/man/1-virt-df/">virt-df</a></code>(1) can now use PolicyKit, <font SIZE="-1">SASL</font> and other authentication methods when getting the list of domains from libvirt. </p>
<p> Improvements to guestfish bash completion (Pino Toscano). </p>
<p> Bash completion now completes short options as well as long options (Pino Toscano). </p>
<p> <code><a href="/docs/linux/man/1-guestfish/">guestfish</a></code>(1) now displays a command synopsis if the number of parameters given to a command is wrong (Hu Tao). </p>
<p> virt-builder now supports Red Hat Enterprise Linux versions back to <font SIZE="-1">RHEL 3.</font> </p>
<p> virt-builder supports <font SIZE="-1">SUSE</font> guests using zypper (Cédric Bosdonnat). </p>
<p> <i>Language bindings</i> </p>
<p> The Java bindings now include validated Javadoc, and other improvements (Pino Toscano). </p>
<p> Multiple fixes and improvements to the <font SIZE="-1">PHP</font> bindings (Pino Toscano). </p>
<p> <i>Inspection</i> </p>
<p> Inspection can now get icons from <font SIZE="-1">RHEL 7</font> and CentOS 7. </p>
<p> <i>/etc/favicon.png</i> is now allowed to be a symbolic link. </p>
<p> For RPM-based guests, inspection now returns <font SIZE="-1">RPM</font> Epoch fields. </p>
<p> Debian packages now have separate Epoch and Version fields (Nikos Skalkotos). </p>
<p> OpenBSD detection added, FreeBSD and NetBSD added as separate &#8220;distros&#8221;, and other <font SIZE="-1">BSD</font> inspection improvements and bug fixes (Nikos Skalkotos). </p>
<p> CoreOS detection added (Nikos Skalkotos). </p>
<p> The package manager in Fedora ≥ 22 is <tt>&quot;dnf&quot;</tt>. </p>
<p> ReactOS guests can be inspected (Maros Zatko). </p>
<p> Add support for <font SIZE="-1">UEFI</font> guests. </p>
<p> Inspection now works when kernel modules are gzip or xz compressed (Pino Toscano). </p>
<p> Inspection now recognizes ppc64 and ppc64le guests (Maros Zatko). </p>
<p> Inspection lists the installed applications on Archlinux guests (Nikos Skalkotos). </p>
<p> <i>Architectures and platforms</i> </p>
<p> <font SIZE="-1">PPC64</font> (<font SIZE="-1">POWER7</font>) and <font SIZE="-1">PPC64LE</font> (<font SIZE="-1">POWER8</font>) architectures are now much better supported, and should work out of the box. </p>
<p> For aarch64, we use <font SIZE="-1">AAVMF</font> (an open source <font SIZE="-1">UEFI</font> implementation based on <font SIZE="-1">OVMF</font>) if available to run the appliance. </p>
<p> For armv7, we now use the <i>-M virt</i> machine type by default. </p>
<p> There is better support for compiling on non-Linux platforms (Pino Toscano, Margaret Lewicka). </p>
<p> Libguestfs should now work on <font SIZE="-1">MIPS 32</font> bit little endian (&#8220;mipsel&#8221;). I have not been able to try 64 bit or big endian.</p>
<h3>Security</h3>
<dl>
<dt><font SIZE="-1">CVE-2014-8484</font></p>
<dd>
<dt><font SIZE="-1">CVE-2014-8485</font></p>
<dd> Libguestfs previously ran the <code><a href="/docs/linux/man/1-strings/">strings</a></code>(1) utility on untrusted files. Strings could parse <font SIZE="-1">BFD</font> headers in an unsafe way, leading to possible arbitrary code execution. Libguestfs now runs strings with a flag to ensure it does not try to parse <font SIZE="-1">BFD</font> headers. This could have led to exploitation of the libguestfs appliance, but since libguestfs further constrains the appliance through virtualization, SELinux and other techniques, it was unlikely to have caused any privilege escalation on the host.</p>
<dt>XPath injection in virt-v2v</p>
<dd> One possible XPath injection vulnerability was fixed in virt-v2v. This might have allowed a malicious guest which was being converted by virt-v2v to construct an arbitrary XPath expression which would have been evaluated on the host (by the libxml2 library linked to the virt-v2v binary). It is not clear what the effects of this might be. </p>
<p> For further information, see upstream commit <a rel="nofollow" href="https://github.com/libguestfs/libguestfs/commit/6c6ce85f94c36803fe2db35a98db436bff0c14b0">https://github.com/libguestfs/libguestfs/commit/6c6ce85f94c36803fe2db35a98db436bff0c14b0</a></p>
<dt>Denial of service problems when using &quot;qemu-img info&quot;</p>
<dd> When using the American Fuzzy Lop fuzzer (<tt>&quot;afl-fuzz&quot;</tt>) on the <tt>&quot;qemu-img info&quot;</tt> command, Richard W.M. Jones found that certain files can cause the <tt>&quot;qemu-img&quot;</tt> program to use lots of memory and time (for example 6GB of heap and 14 seconds of <font SIZE="-1">CPU</font> time on a fast Intel processor), and in some cases to crash. Since libguestfs may run <tt>&quot;qemu-img info&quot;</tt> on disk images to find out what they contain, this transitively could cause libguestfs to hang or consume lots of memory. </p>
<p> Libguestfs was modified so that it uses resource limits to limit the space and time used by <tt>&quot;qemu-img info&quot;</tt>, to avoid this problem. If a malicious user tries to pass one of these disk images to libguestfs, <tt>&quot;qemu-img&quot;</tt> will crash and the crash is reported back to libguestfs callers as an error message.</dl>
<h3><font SIZE="-1">API</font></h3>
<p> <i>New APIs</i></p>
<dl>
<dt>&quot;guestfs_add_libvirt_dom&quot;</p>
<dd> This exposes a previously private <font SIZE="-1">API</font> that allows you to pass a <tt>&quot;virDomainPtr&quot;</tt> object directly from libvirt to libguestfs.</p>
<dt>&quot;guestfs_blockdev_setra&quot;</p>
<dd> Adjust readahead parameter for devices. See <tt>&quot;blockdev --setra&quot;</tt> command.</p>
<dt>&quot;guestfs_btrfs_balance&quot;</p>
<dd>
<dt>&quot;guestfs_btrfs_balance_cancel&quot;</p>
<dd>
<dt>&quot;guestfs_btrfs_balance_pause&quot;</p>
<dd>
<dt>&quot;guestfs_btrfs_balance_resume&quot;</p>
<dd>
<dt>&quot;guestfs_btrfs_balance_status&quot;</p>
<dd> Balance support for Btrfs filesystems (Hu Tao).</p>
<dt>&quot;guestfs_btrfs_filesystem_defragment&quot;</p>
<dd> Filesystem defragmentation support for Btrfs filesystems (Hu Tao).</p>
<dt>&quot;guestfs_btrfs_image&quot;</p>
<dd> Create an image of a Btrfs filesystem (Chen Hanxiao)</p>
<dt>&quot;guestfs_btrfs_qgroup_assign&quot;</p>
<dd>
<dt>&quot;guestfs_btrfs_qgroup_create&quot;</p>
<dd>
<dt>&quot;guestfs_btrfs_qgroup_destroy&quot;</p>
<dd>
<dt>&quot;guestfs_btrfs_qgroup_limit&quot;</p>
<dd>
<dt>&quot;guestfs_btrfs_qgroup_remove&quot;</p>
<dd>
<dt>&quot;guestfs_btrfs_qgroup_show&quot;</p>
<dd>
<dt>&quot;guestfs_btrfs_quota_enable&quot;</p>
<dd>
<dt>&quot;guestfs_btrfs_quota_rescan&quot;</p>
<dd> Quote support for Btrfs filesystems (Hu Tao).</p>
<dt>&quot;guestfs_btrfs_rescue_chunk_recover&quot;</p>
<dd> Scan and recover the chunk tree in Btrfs filesystems (Hu Tao).</p>
<dt>&quot;guestfs_btrfs_rescue_super_recover&quot;</p>
<dd> Restore superblocks in Btrfs filesystems (Hu Tao).</p>
<dt>&quot;guestfs_btrfs_replace&quot;</p>
<dd> Replace a device in a Btrfs filesystem (Cao Jin).</p>
<dt>&quot;guestfs_btrfs_scrub&quot;</p>
<dd>
<dt>&quot;guestfs_btrfs_scrub_cancel&quot;</p>
<dd>
<dt>&quot;guestfs_btrfs_scrub_resume&quot;</p>
<dd>
<dt>&quot;guestfs_btrfs_scrub_status&quot;</p>
<dd> Scrub a Btrfs filesystem (Hu Tao).</p>
<dt>&quot;guestfs_btrfs_subvolume_get_default&quot;</p>
<dd> Get the default subvolume of a Btrfs filesystem (Hu Tao).</p>
<dt>&quot;guestfs_btrfs_subvolume_show&quot;</p>
<dd> List detailed information about the subvolume of a Btrfs filesystem (Hu Tao).</p>
<dt>&quot;guestfs_btrfstune_enable_extended_inode_refs&quot;</p>
<dd>
<dt>&quot;guestfs_btrfstune_enable_skinny_metadata_extent_refs&quot;</p>
<dd>
<dt>&quot;guestfs_btrfstune_seeding&quot;</p>
<dd> Various tuning parameters for Btrfs filesystems (Chen Hanxiao).</p>
<dt>&quot;guestfs_c_pointer&quot;</p>
<dd> Return the C pointer to the underlying <tt>&quot;guestfs_h *&quot;</tt>. This allows interworking of libguestfs bindings with bindings from other libraries. For further information see <a rel="nofollow" href="https://bugzilla.redhat.com/1075164">https://bugzilla.redhat.com/1075164</a></p>
<dt>&quot;guestfs_copy_in&quot;</p>
<dd>
<dt>&quot;guestfs_copy_out&quot;</p>
<dd> Flexible APIs for recursively copying directories of files between the host and guest filesystem. Previously these were available only as guestfish commands, but now any <font SIZE="-1">API</font> users can call them (Pino Toscano).</p>
<dt>&quot;guestfs_part_get_gpt_guid&quot;</p>
<dd>
<dt>&quot;guestfs_part_set_gpt_guid&quot;</p>
<dd> Get and set the <font SIZE="-1">GPT</font> per-partition <font SIZE="-1">GUID.</font></p>
<dt>&quot;guestfs_part_get_mbr_part_type&quot;</p>
<dd> Get <font SIZE="-1">MBR</font> partition type (Chen Hanxiao).</p>
<dt>&quot;guestfs_set_uuid_random&quot;</p>
<dd> Set the <font SIZE="-1">UUID</font> of a filesystem to a randomly generated value; supported filesystems currently are ext2/3/4, <font SIZE="-1">XFS,</font> Btrfs, and swap partitions. (Chen Hanxiao).</dl>
<p> <i>Other </i><font SIZE="-1"><i>API</i></font><i> changes</i> </p>
<p> <tt>&quot;guestfs_disk_create&quot;</tt> can now use <font SIZE="-1">VMDK</font> files as backing files. </p>
<p> <tt>&quot;guestfs_btrfs_subvolume_snapshot&quot;</tt> takes extra optional parameters (all added by Hu Tao):</p>
<dl>
<dt>&quot;ro&quot;</p>
<dd> for creating a read-only Btrfs snapshot</p>
<dt>&quot;qgroupid&quot;</p>
<dd> for adding the snapshot to a qgroup</dl>
<p> <tt>&quot;guestfs_btrfs_subvolume_create&quot;</tt> can also take the optional <tt>&quot;qgroupid&quot;</tt> parameter (Hu Tao). </p>
<p> <tt>&quot;guestfs_set_uuid&quot;</tt> can set <font SIZE="-1">UUID</font> of swap partitions, Btrfs (Hu Tao, Chen Hanxiao). </p>
<p> <tt>&quot;guestfs_copy_device_to_file&quot;</tt> and <tt>&quot;guestfs_copy_file_to_file&quot;</tt> have a new optional <tt>&quot;append&quot;</tt> parameter, allowing you to append to the output file instead of truncating it. </p>
<p> <tt>&quot;guestfs_mkfs&quot;</tt> has a new optional <tt>&quot;label&quot;</tt> parameter to set the initial label of the new filesystem (Pino Toscano). </p>
<p> <tt>&quot;guestfs_set_label&quot;</tt> and <tt>&quot;guestfs_set_uuid&quot;</tt> now set <tt>&quot;ENOTSUP&quot;</tt> as errno when there is no implemented support for the filesystem of the specified mountable (Chen Hanxiao). </p>
<p> Environment variables now let you write <tt>&quot;LIBGUESTFS_DEBUG=true&quot;</tt>, <tt>&quot;LIBGUESTFS_DEBUG=0&quot;</tt> and so on. </p>
<p> All <tt>&quot;guestfs_sfdisk*&quot;</tt> APIs have been deprecated. Because <code><a href="/docs/linux/man/8-sfdisk/">sfdisk</a></code>(8) was rewritten, incompatibly, upstream, we don&#8217;t recommend using these APIs in future code. Use the <tt>&quot;guestfs_part*&quot;</tt> APIs as replacements. </p>
<p> APIs such as <tt>&quot;guestfs_download&quot;</tt> do not truncate <i>/dev/stdout</i> or <i>/dev/stderr</i> when writing to them, meaning that if you redirect stdout or stderr to a file, the file is no longer truncated.</p>
<h3>Build changes</h3>
<p> The daemon no longer uses its own separate copy of gnulib. Instead it shares a single copy with the library. </p>
<p> OCaml <i>.annot</i> files are now created, so IDEs and editors like emacs and vi can browse OCaml types in the source code. </p>
<p> Various fixes to allow different host/appliance architecture builds (Pino Toscano). </p>
<p> Automake is now used directly to build all the OCaml programs, instead of ad hoc Makefile rules. One side effect of this is to enable warnings in all the C code used by OCaml programs. </p>
<p> <tt>&quot;-fno-strict-overflow&quot;</tt> is used throughout the build to avoid dubious <font SIZE="-1">GCC</font> optimizations. </p>
<p> Multiple cleanups to support <font SIZE="-1">GCC 5.</font> </p>
<p> OCaml OUnit2 is needed to run some OCaml tests. </p>
<p> Creating a statically linked <i>libguestfs.a</i> should work again. </p>
<p> The <i>src/api-support</i> subdirectory and its scripts are no longer used. Instead we store in the <i>generator/actions.ml</i> when the <font SIZE="-1">API</font> was added to libguestfs.</p>
<h3>Internationalization</h3>
<p> The translation service has changed from Transifex to Zanata. </p>
<p> Many more translations are available now, for both library and tools messages and documentation.</p>
<h3>Internals</h3>
<p> In all OCaml tools, there are now common <tt>&quot;error&quot;</tt>, <tt>&quot;warning&quot;</tt>, <tt>&quot;info&quot;</tt> functions, and common way to set and get the <i>&#8211;quiet</i>, <i>-x</i> (trace) and <i>-v</i> (verbose) flags, and colour highlighting used consistently. </p>
<p> <tt>&quot;COMPILE_REGEXP&quot;</tt> macros are used to simplify <font SIZE="-1">PCRE</font> constructors and destructors. </p>
<p> In the generator, <tt>&quot;Pointer&quot;</tt> arguments have finally been implemented. </p>
<p> Internal identifiers no longer use double and triple underscores (eg. <tt>&quot;guestfs___program_name&quot;</tt>). These identifiers are invalid for C99 and C<font SIZE="-2">++</font> programs, although compilers would accept them. </p>
<p> The daemon no longer parses <tt>&quot;guestfs_*&quot;</tt> options from <i>/proc/cmdline</i>. Instead it only takes ordinary command line options. The appliance init script turns <i>/proc/cmdline</i> into daemon command line options. </p>
<p> The tests can now run the daemon as a &#8220;captive process&#8221;, allowing it to be run directly on the host. The main advantage of this is we can run valgrind directly on the daemon during testing.</p>
<h3>Bugs fixed</h3>
<dl>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1239053">https://bugzilla.redhat.com/1239053</a></p>
<dd> virt-v2v error reporting when grub.conf cannot be parsed by Augeas</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1238053">https://bugzilla.redhat.com/1238053</a></p>
<dd> v2v:Duplicate disk target set when convert guest with cdrom attached</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1237869">https://bugzilla.redhat.com/1237869</a></p>
<dd> Virtio drivers are not installed for windows 2008 guests by virt-v2v</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1234351">https://bugzilla.redhat.com/1234351</a></p>
<dd> virt-v2v Support for Fedora virtio-win drivers</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1232192">https://bugzilla.redhat.com/1232192</a></p>
<dd> Virt-v2v gives an error on a blank disk: part_get_parttype: unknown signature, of the output: <font SIZE="-1">BYT</font>;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1229385">https://bugzilla.redhat.com/1229385</a></p>
<dd> virt-p2v in kernel command line mode should power off the machine after conversion</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1229340">https://bugzilla.redhat.com/1229340</a></p>
<dd> virt-p2v no <font SIZE="-1">GUI</font> mode appends 
 to the final command line parameter</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1229305">https://bugzilla.redhat.com/1229305</a></p>
<dd> virt-sysprep at cleanup deletes /var/spool/at/.SEQ which results in failing at</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1226794">https://bugzilla.redhat.com/1226794</a></p>
<dd> &#8220;Doing conversion……&#8221; still shows after cancel the conversion from virt-p2v client</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1215042">https://bugzilla.redhat.com/1215042</a></p>
<dd> Memory leak in virNetSocketNewConnectUNIX</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1213324">https://bugzilla.redhat.com/1213324</a></p>
<dd> virt-v2v: warning: unknown guest operating system: windows windows 6.3 when converting win8,win8.1,win2012,win2012R2 to rhev</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1213247">https://bugzilla.redhat.com/1213247</a></p>
<dd> virt tools should print the same format of version string</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1212808">https://bugzilla.redhat.com/1212808</a></p>
<dd> <font SIZE="-1">RFE:</font> virt-builder &#8211;touch</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1212807">https://bugzilla.redhat.com/1212807</a></p>
<dd> virt-builder &#8211;selinux-relabel flag fails on cross-architecture builds</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1212680">https://bugzilla.redhat.com/1212680</a></p>
<dd> <font SIZE="-1">RFE:</font> virt-inspector xpath query should output a neat format of the query element</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1212152">https://bugzilla.redhat.com/1212152</a></p>
<dd> virt-builder firstboot-command fails: File name too long</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1211996">https://bugzilla.redhat.com/1211996</a></p>
<dd> virt-inspector gives incorrect arch (ppc64) for ppc64le guest</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1203817">https://bugzilla.redhat.com/1203817</a></p>
<dd> <font SIZE="-1">RFE:</font> virt-customize &#8211;move and &#8211;copy</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1201526">https://bugzilla.redhat.com/1201526</a></p>
<dd> index-parser can&#8217;t parse systemd mount files properly</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1196101">https://bugzilla.redhat.com/1196101</a></p>
<dd> virt-builder &#8211;upload option doesn&#8217;t work to a <font SIZE="-1">FAT</font> partition</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1196100">https://bugzilla.redhat.com/1196100</a></p>
<dd> virt-builder -x option on its own does not enable tracing</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1195204">https://bugzilla.redhat.com/1195204</a></p>
<dd> `virt-builder` should create <tt>$HOME</tt>/.cache directory if it already doesn&#8217;t exist</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1193237">https://bugzilla.redhat.com/1193237</a></p>
<dd> Virt-builder fingerprint is required even when no check desired</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1189284">https://bugzilla.redhat.com/1189284</a></p>
<dd> virt-resize should preserve <font SIZE="-1">GPT</font> partition UUIDs, else <font SIZE="-1">EFI</font> guests become unbootable</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1188866">https://bugzilla.redhat.com/1188866</a></p>
<dd> Performance regression in virt-builder when uncompressing image</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1186800">https://bugzilla.redhat.com/1186800</a></p>
<dd> virt-v2v should support gzip format ova as input</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1185561">https://bugzilla.redhat.com/1185561</a></p>
<dd> virt-sparsify should ignore read-only LVs</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1182463">https://bugzilla.redhat.com/1182463</a></p>
<dd> &#8220;mknod-b&#8221;, &#8220;mknod-c&#8221;, and &#8220;mkfifo&#8221; do not strip non-permissions bits from &#8220;mode&#8221;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1176493">https://bugzilla.redhat.com/1176493</a></p>
<dd> virt-v2v ignores sound device when convert xen guest to local kvm</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1175676">https://bugzilla.redhat.com/1175676</a></p>
<dd> Typo error in &#8216;help ping-daemon&#8217;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1175196">https://bugzilla.redhat.com/1175196</a></p>
<dd> &#8220;parse-environment&#8221; and &#8220;parse-environment-list&#8221; fail to parse &#8220;<font SIZE="-1">LIBGUESTFS_TRACE</font> = 0&#8221;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1175035">https://bugzilla.redhat.com/1175035</a></p>
<dd> &#8220;is-blockdev&#8221;/&#8220;is-blockdev-opts&#8221; fail to detect &#8220;/dev/sda&#8221;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1174280">https://bugzilla.redhat.com/1174280</a></p>
<dd> <font SIZE="-1">RFE:</font> Allow v2v conversion of Oracle Linux 5.8 VMware <font SIZE="-1">VM</font></p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1174200">https://bugzilla.redhat.com/1174200</a></p>
<dd> New virt-v2v failure: <font SIZE="-1">CURL:</font> Error opening file: <font SIZE="-1">NSS:</font> client certificate not found (nickname not specified): Invalid argument</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1174123">https://bugzilla.redhat.com/1174123</a></p>
<dd> Graphics password disappear after conversion of virt-v2v</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1174073">https://bugzilla.redhat.com/1174073</a></p>
<dd> The listen address for vnc is changed after conversion by virt-v2v</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1171666">https://bugzilla.redhat.com/1171666</a></p>
<dd> inspection thinks <font SIZE="-1">EFI</font> partition is a separate operating system</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1171130">https://bugzilla.redhat.com/1171130</a></p>
<dd> virt-v2v conversion of <font SIZE="-1">RHEL 3</font> guest fails with: All of your loopback devices are in use</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1170685">https://bugzilla.redhat.com/1170685</a></p>
<dd> Conversion of <font SIZE="-1">RHEL 4</font> guest fails: rpm -ql 1:kernel-utils-2.4-23.el4: virt-v2v: error: libguestfs error: command_lines:</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1170073">https://bugzilla.redhat.com/1170073</a></p>
<dd> virt-v2v picks debug kernels over non-debug kernels when versions are equal</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1169045">https://bugzilla.redhat.com/1169045</a></p>
<dd> virt-sparsify: libguestfs error: qemu-img info: &#8216;virtual-size&#8217; is not representable as a 64 bit integer</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1169015">https://bugzilla.redhat.com/1169015</a></p>
<dd> virt-resize &#8211;expand fails on ubuntu-14.04.img image (regression)</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1168144">https://bugzilla.redhat.com/1168144</a></p>
<dd> warning: fstrim: fstrim: /sysroot/: <font SIZE="-1">FITRIM</font> ioctl failed: Operation not supported (ignored) when convert win2003 guest from xen server</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1167921">https://bugzilla.redhat.com/1167921</a></p>
<dd> p2v: No Network Connection dialog</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1167774">https://bugzilla.redhat.com/1167774</a></p>
<dd> virt-p2v fails with error:&#8220;nbd.<code>c:nbd_receive_negotiate()</code>:L501: read failed&#8221;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1167623">https://bugzilla.redhat.com/1167623</a></p>
<dd> Remove &#8220;If reporting bugs, run virt-v2v with debugging enabled ..&#8221; message when running virt-p2v</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1167601">https://bugzilla.redhat.com/1167601</a></p>
<dd> &#8220;Conversion was successful&#8221; pop out even virt-p2v fails</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1167302">https://bugzilla.redhat.com/1167302</a></p>
<dd> virt-v2v: warning: ova hard disk has no parent controller when convert from a ova file</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1166618">https://bugzilla.redhat.com/1166618</a></p>
<dd> virt-resize should give out the detail warning info to let customers know what&#8217;s going wrong</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1165975">https://bugzilla.redhat.com/1165975</a></p>
<dd> File &#8220;/boot/grub2/device.map&#8221; showing is not right after converting a rhel7 guest from esx server</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1165785">https://bugzilla.redhat.com/1165785</a></p>
<dd> mount-loop command fails: mount failed: Unknown error -1</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1165569">https://bugzilla.redhat.com/1165569</a></p>
<dd> Disable &#8220;cancel conversion&#8221; button after virt-p2v conversion finished</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1165564">https://bugzilla.redhat.com/1165564</a></p>
<dd> Provide Reboot/Shutdown button after virt-p2v</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1164853">https://bugzilla.redhat.com/1164853</a></p>
<dd> Booting in qemu found no volume groups and failed checking the filesystems</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1164732">https://bugzilla.redhat.com/1164732</a></p>
<dd> The description of &#8216;help append&#8217; is not accurately, it add the kernel options to libguestfs appliance not the guest kernel</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1164697">https://bugzilla.redhat.com/1164697</a></p>
<dd> typo errors in man pages</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1164619">https://bugzilla.redhat.com/1164619</a></p>
<dd> Inspect-get-icon failed on <font SIZE="-1">RHEL7</font> guest</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1162966">https://bugzilla.redhat.com/1162966</a></p>
<dd> xfs should also give a warning out to let customer know the limitation</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1161575">https://bugzilla.redhat.com/1161575</a></p>
<dd> Failed to import guest with &#8220;rtl8139&#8221; nic to openstack server after converted by v2v</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1159651">https://bugzilla.redhat.com/1159651</a></p>
<dd> virt-sysprep firstboot script is not deleted if it reboot a <font SIZE="-1">RHEL 7</font> guest</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1159258">https://bugzilla.redhat.com/1159258</a></p>
<dd> esx win2008 32 bit guest fail to load after conversion because the firmware isn&#8217;t <font SIZE="-1">ACPI</font> compatible</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1159016">https://bugzilla.redhat.com/1159016</a></p>
<dd> libvirt backend does not set <font SIZE="-1">RBD</font> password</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1158526">https://bugzilla.redhat.com/1158526</a></p>
<dd> Use password file instead of process interaction</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1157679">https://bugzilla.redhat.com/1157679</a></p>
<dd> virt-p2v-make-disk should add firmwares</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1156449">https://bugzilla.redhat.com/1156449</a></p>
<dd> libguestfs <font SIZE="-1">FTBFS</font> on f21 ppc64le</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1156301">https://bugzilla.redhat.com/1156301</a></p>
<dd> virt-inspector support adding a remote disk, but in its man page -a <font SIZE="-1">URI /</font> &#8211;add <font SIZE="-1">URI</font> is missing</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1155121">https://bugzilla.redhat.com/1155121</a></p>
<dd> Virt-v2v will fail when using relative path for -i ova</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1153844">https://bugzilla.redhat.com/1153844</a></p>
<dd> Redundancy whitespace at the end of directory name when use &lt;<font SIZE="-1">TAB</font>&gt; to complete the directory name in guestfish with a xfs filesystem in guest</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1153589">https://bugzilla.redhat.com/1153589</a></p>
<dd> virt-v2v will hang when converting esx guest before disk copy phase</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1152998">https://bugzilla.redhat.com/1152998</a></p>
<dd> virt-v2v / qemu-img fails on ova image</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1151910">https://bugzilla.redhat.com/1151910</a></p>
<dd> virt-ls should remove &#8216;/&#8217; in the output when specify the directory name as /etc/</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1151900">https://bugzilla.redhat.com/1151900</a></p>
<dd> Should also add a field for directory files when run virt-ls with &#8211;csv option</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1151033">https://bugzilla.redhat.com/1151033</a></p>
<dd> virt-v2v conversions from VMware vCenter server run slowly</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1146832">https://bugzilla.redhat.com/1146832</a></p>
<dd> virt-v2v fail to convert guest with disk type volume</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1146007">https://bugzilla.redhat.com/1146007</a></p>
<dd> Input/output error during conversion of esx guest.</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1135585">https://bugzilla.redhat.com/1135585</a></p>
<dd> [<font SIZE="-1">RFE</font>] virt-builder should support copying in a directory/list of files</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1089566">https://bugzilla.redhat.com/1089566</a></p>
<dd> [abrt] livecd-tools: kickstart.py:276:apply:IOError: [Errno 2] No such file or directory: &#8216;/run/media/jones/2tp001data/createlive/temp/imgcreate-_dX8Us/install_root/etc/rpm/macros.imgcreate&#8217;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1079625">https://bugzilla.redhat.com/1079625</a></p>
<dd> virt-sparsify fails if a btrfs filesystem contains readonly snapshots</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1075164">https://bugzilla.redhat.com/1075164</a></p>
<dd> <font SIZE="-1">RFE:</font> allow passing in a pre-opened libvirt connection from python</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/912499">https://bugzilla.redhat.com/912499</a></p>
<dd> Security context on image file gets reset</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/889082">https://bugzilla.redhat.com/889082</a></p>
<dd> [<font SIZE="-1">RFE</font>] virt-v2v should check whether guest with same name exist on target first then transfer the disk</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/855059">https://bugzilla.redhat.com/855059</a></p>
<dd> <font SIZE="-1">RFE:</font> virt-p2v: display more information about network devices such as topology, bonding, etc.</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/823758">https://bugzilla.redhat.com/823758</a></p>
<dd> p2v client should have largest number restrictions for <font SIZE="-1">CPU</font> and Memory settings</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/709327">https://bugzilla.redhat.com/709327</a></p>
<dd> hivex cannot read registry hives from ReactOS</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/709326">https://bugzilla.redhat.com/709326</a></p>
<dd> virt-inspector cannot detect ReactOS</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/119673">https://bugzilla.redhat.com/119673</a></p>
<dd> installation via <font SIZE="-1">NFS</font> doesn&#8217;t seem to work</dl>
<h2>RELEASE NOTES FOR LIBGUESTFS 1.28</h2>
<p> These release notes only cover the differences from the previous stable/dev branch split (1.26.0). For detailed changelogs, please see the git repository, or the ChangeLog file distributed in the tarball.</p>
<h3>New features</h3>
<p> <i>Tools</i> </p>
<p> <code><a href="/docs/linux/man/1-virt-v2v/">virt-v2v</a></code>(1) and <code><a href="/docs/linux/man/1-virt-p2v/">virt-p2v</a></code>(1) are tools for converting from foreign hypervisors (such as VMware or Xen) or physical machines, to <font SIZE="-1">KVM.</font> These tools were previously a separate project. The code for both tools has been integrated into the libguestfs tree. As part of the refactoring, virt-p2v has been rewritten (from Ruby, now C), and virt-v2v now uses several modern features of qemu which make it run many times faster than before. <code><a href="/docs/linux/man/1-virt-v2v/">virt-v2v</a></code>(1) can import from: VMware vCenter, VMware <font SIZE="-1">OVA</font> files, local disk files, libvirt, <font SIZE="-1">RHEL 5</font> Xen. It can output to: oVirt or Red Hat Enterprise Virtualization (RHEV-M), OpenStack Glance, libvirt, qemu, local disk files. </p>
<p> <code><a href="/docs/linux/man/1-virt-log/">virt-log</a></code>(1) is a new tool for listing log files from guests. It supports a variety of guests including Linux traditional, Linux using journal, and Windows event log. </p>
<p> <code><a href="/docs/linux/man/1-virt-builder/">virt-builder</a></code>(1) has a new <tt>&quot;--machine-readable&quot;</tt> option to make it simpler to consume virt-builder from other programs. </p>
<p> New <code><a href="/docs/linux/man/1-virt-builder/">virt-builder</a></code>(1) and <code><a href="/docs/linux/man/1-virt-customize/">virt-customize</a></code>(1) <i>&#8211;chmod</i> option. </p>
<p> <code><a href="/docs/linux/man/1-virt-sysprep/">virt-sysprep</a></code>(1) will now remove: systemd journals, anaconda logs, lightdm logs, debian-installer files, apt logs, exim logs, ConsoleKit logs, firewalld logs, grubby logs, proftpd logs, libvirt/libxml logs, and several other log files. The virt-sysprep <tt>&quot;user-account&quot;</tt> operation is now able to remove or keep particular user accounts. (Pino Toscano). </p>
<p> New <code><a href="/docs/linux/man/1-guestmount/">guestmount</a></code>(1) <i>&#8211;fd</i> option, allowing you to run guestmount captive under another process. </p>
<p> <code><a href="/docs/linux/man/1-virt-sparsify/">virt-sparsify</a></code>(1) has a new <i>&#8211;tmp</i> option allowing you to precisely control where temporary files are stored. </p>
<p> <code><a href="/docs/linux/man/1-virt-sparsify/">virt-sparsify</a></code>(1) can now write to a block device. </p>
<p> <code><a href="/docs/linux/man/1-virt-customize/">virt-customize</a></code>(1) and <code><a href="/docs/linux/man/1-virt-sysprep/">virt-sysprep</a></code>(1) now support adding firstboot scripts to Windows guests. </p>
<p> <code><a href="/docs/linux/man/1-virt-cat/">virt-cat</a></code>(1), <code><a href="/docs/linux/man/1-virt-edit/">virt-edit</a></code>(1), <code><a href="/docs/linux/man/1-virt-ls/">virt-ls</a></code>(1) now support the <i>-m</i> option, allowing you to override automatic inspection of guests and instead specify where to mount partitions (Pino Toscano). </p>
<p> The virt tools now have coloured output: green for <font SIZE="-1">OK,</font> red for errors, blue for warnings. </p>
<p> <i>Language bindings</i> </p>
<p> You can build a Python distribution using <tt>&quot;make -C python sdist&quot;</tt> </p>
<p> Ruby bindings have switched from <tt>&quot;Test::Unit&quot;</tt> to <tt>&quot;MiniTest&quot;</tt>. </p>
<p> The Java bindings are now compatible with OpenJDK 8 (Pino Toscano). </p>
<p> <i>Inspection</i> </p>
<p> Oracle Linux is returned as <tt>&quot;oraclelinux&quot;</tt> (Nikos Skalkotos). </p>
<p> Linux guests which do not have <i>/etc/fstab</i> can now be handled (Pino Toscano). </p>
<p> Minix is returned as <tt>&quot;minix&quot;</tt> (Pino Toscano). </p>
<p> <i>Architectures</i> </p>
<p> Aarch64 (64 bit <font SIZE="-1">ARM</font>) support has been added. </p>
<p> Inspection and the <tt>&quot;guestfs_file_architecture&quot;</tt> call can now recognize arm (32 bit) and aarch64 guests.</p>
<h3>Security</h3>
<dl>
<dt><font SIZE="-1">CVE-2014-0191</font> Network usage and entity resolution in <font SIZE="-1">XML</font> parsing</p>
<dd> Libguestfs previously used unsafe libxml2 APIs for parsing libvirt <font SIZE="-1">XML.</font> These APIs defaulted to allowing network connections to be made when certain <font SIZE="-1">XML</font> documents were presented. Using a malformed <font SIZE="-1">XML</font> document it was also possible to exhaust all <font SIZE="-1">CPU,</font> memory or file descriptors on the machine. </p>
<p> Since the libvirt <font SIZE="-1">XML</font> comes from a trusted source (the libvirt daemon) it is not thought that this could have been exploitable. </p>
<p> This was fixed in libguestfs ≥ 1.27.9 and the fix was backported to stable versions ≥ 1.26.2, ≥ 1.24.9, ≥ 1.22.10 and ≥ 1.20.13. (Thanks: Dan Berrange, Pino Toscano).</p>
<dt>Shellshock (bash <font SIZE="-1">CVE-2014-6271</font>)</p>
<dd> This bash bug indirectly affects libguestfs. For more information see: <a rel="nofollow" href="https://www.redhat.com/archives/libguestfs/2014-September/msg00252.html">https://www.redhat.com/archives/libguestfs/2014-September/msg00252.html</a></dl>
<h3><font SIZE="-1">API</font></h3>
<p> <i>New APIs</i></p>
<dl>
<dt>&quot;guestfs_clear_backend_setting&quot;</p>
<dd>
<dt>&quot;guestfs_get_backend_setting&quot;</p>
<dd>
<dt>&quot;guestfs_set_backend_setting&quot;</p>
<dd> Use these APIs to set individual backend settings.</p>
<dt>&quot;guestfs_cpio_out&quot;</p>
<dd> Convert a directory within the disk image to cpio format.</p>
<dt>&quot;guestfs_journal_get_realtime_usec&quot;</p>
<dd> Fetch precise journal times, see <code><a href="/docs/linux/man/3-sd_journal_get_realtime_usec/">sd_journal_get_realtime_usec</a></code>(3).</p>
<dt>&quot;guestfs_lstatns&quot;</p>
<dd>
<dt>&quot;guestfs_lstatnslist&quot;</p>
<dd>
<dt>&quot;guestfs_statns&quot;</p>
<dd> Enhanced versions of <tt>&quot;guestfs_lstat&quot;</tt>, <tt>&quot;guestfs_lstatlist&quot;</tt>, <tt>&quot;guestfs_stat&quot;</tt> which return nanosecond timestamps.</dl>
<h3>Build changes</h3>
<p> Libguestfs can now be built with qemu 2.x. </p>
<p> Add support for packaging the appliance on Mageia (Joseph Wang, Thierry Vignaud). </p>
<p> Augeas is now a required dependency. </p>
<p> Flex and bison are now required dependencies.</p>
<h3>Internals</h3>
<p> User-Mode Linux (<font SIZE="-1">UML</font>) is no longer a supported backend (although still available). It will be supported again once someone steps in and fixes various regressions and brokenness in the <font SIZE="-1">UML</font> (Linux) kernel. </p>
<p> You can now connect gdb to qemu by specifying <tt>&quot;LIBGUESTFS_BACKEND_SETTINGS=gdb&quot;</tt> </p>
<p> Serial <font SIZE="-1">BIOS</font> (sgabios) is now used by the libvirt backend (on x86 only) so that we see early <font SIZE="-1">BIOS</font> messages. </p>
<p> For the OCaml virt tools, exceptions are now handled and printed by a common function. </p>
<p> A <font SIZE="-1">GCC</font> warning about large stack frames is now enabled by default. Several places that used large arrays and structures on the stack have been fixed. </p>
<p> There is now a test for booting the appliance repeatedly. Useful for finding kernel leaks. See: <i>tests/qemu/qemu-boot.c</i> </p>
<p> There is a test for testing the speed of various qemu features such as virtio-serial uploads and block device writes. See: <i>tests/qemu/qemu-speed-test.c</i> </p>
<p> <font SIZE="-1">GCC</font> warnings are now enabled for OCaml-C bindings in the OCaml virt tools. </p>
<p> The code for editing files used by <code><a href="/docs/linux/man/1-virt-edit/">virt-edit</a></code>(1), <code><a href="/docs/linux/man/1-guestfish/">guestfish</a></code>(1) <tt>&quot;edit&quot;</tt> command, <code><a href="/docs/linux/man/1-virt-customize/">virt-customize</a></code>(1) <i>&#8211;edit</i> option and more is now shared between all these utilities (thanks Pino Toscano). </p>
<p> The <font SIZE="-1">FUSE</font> tests were rewritten in C to ensure finer control over how system calls are tested. </p>
<p> The <i>update-bugs.sh</i> script has been fixed so it should no longer create an empty <tt>&quot;BUGS&quot;</tt> file if the Bugzilla server is unavailable. </p>
<p> The <code><a href="/docs/linux/man/1-virt-resize/">virt-resize</a></code>(1) tests now use a stochastic method to ensure much deeper and broader testing. </p>
<p> When the network is enabled, the appliance now uses <font SIZE="-1">DHCP</font> to acquire an <font SIZE="-1">IP</font> address. </p>
<p> If libvirt is being used then the appliance will connect to <tt>&quot;virbr0&quot;</tt> (can be overridden by setting <tt>&quot;LIBGUESTFS_BACKEND_SETTINGS=network_bridge=&lt;some_bridge&gt;&quot;</tt>). This enables full-featured network connections, with working <font SIZE="-1">ICMP,</font> ping and so on.</p>
<h3>Bugs fixed</h3>
<dl>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1153515">https://bugzilla.redhat.com/1153515</a></p>
<dd> empty (but set) <font SIZE="-1">LIBGUESTFS_BACKEND</font> prints libguestfs: error: invalid backend:</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1151766">https://bugzilla.redhat.com/1151766</a></p>
<dd> libguestfs-bash-completion package contains file /usr/share/bash-completion/completions/virt-log, but no <code>_virt_log()</code> function in that file</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1151738">https://bugzilla.redhat.com/1151738</a></p>
<dd> typo error in man page of virt-edit</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1151033">https://bugzilla.redhat.com/1151033</a></p>
<dd> virt-v2v conversions from VMware vCenter server run slowly</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1150880">https://bugzilla.redhat.com/1150880</a></p>
<dd> virt-v2v: warning: display &lt;graphics type=&#8217;sdl&#8217;&gt; was ignored when converting rhel5 guest with sdl graphics</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1150867">https://bugzilla.redhat.com/1150867</a></p>
<dd> &#8216;copy-file-to-file /src /dest&#8217; create file /dest even if command &#8216;copy-file-to-file /src /dest&#8217; failed</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1150815">https://bugzilla.redhat.com/1150815</a></p>
<dd> Can not find &#8220;<font SIZE="-1">RECURSIVE LONG LISTING&#8221;</font> in &#8216;man virt-diff&#8217;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1150701">https://bugzilla.redhat.com/1150701</a></p>
<dd> virt-v2v does not fstrim data disks and non-mounted filesystems</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1150475">https://bugzilla.redhat.com/1150475</a></p>
<dd> Exporting 2+ disk guest to <font SIZE="-1">RHEV,</font> only one disk shows after import</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1148355">https://bugzilla.redhat.com/1148355</a></p>
<dd> virt-filesystems: incorrect <font SIZE="-1">LVM</font> vg name when listing Fedora 21 Alpha Atomic image filesystems</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1148072">https://bugzilla.redhat.com/1148072</a></p>
<dd> Option missing &#8211;no-selinux-relabel</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1148012">https://bugzilla.redhat.com/1148012</a></p>
<dd> <font SIZE="-1">RFE:</font> Allow qemu-bridge-helper to be used to implement guestfs_set_network</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1146815">https://bugzilla.redhat.com/1146815</a></p>
<dd> virt-v2v prints warning: /files/etc/fstab/8/spec references unknown device &#8220;cdrom&#8221;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1146275">https://bugzilla.redhat.com/1146275</a></p>
<dd> regression setting root password with virt-builder/virt-customize</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1146017">https://bugzilla.redhat.com/1146017</a></p>
<dd> virt-v2v -v -x during windows guest conversion will hang at hivex: hivex_open: used block id ……</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1145995">https://bugzilla.redhat.com/1145995</a></p>
<dd> Improve the error info when converting windows guest with unclean file system</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1145916">https://bugzilla.redhat.com/1145916</a></p>
<dd> virt-v2v fails to convert win7 guest</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1144891">https://bugzilla.redhat.com/1144891</a></p>
<dd> <font SIZE="-1">RFE:</font> stat calls do not return nanosecond timestamps</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1144766">https://bugzilla.redhat.com/1144766</a></p>
<dd> <code>futimens()</code> is a no-op via guestmount</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1144201">https://bugzilla.redhat.com/1144201</a></p>
<dd> guestfish can not restore terminal&#8217;s output colour when exit guestfish, if the terminal&#8217;s background colour is black then it will make a inconvenient</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1143949">https://bugzilla.redhat.com/1143949</a></p>
<dd> virt-customize option &#8216;&#8211;password-crypto&#8217; do not work</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1143887">https://bugzilla.redhat.com/1143887</a></p>
<dd> Warning shows when converting guests to rhev:chown: changing ownership of ‘/tmp/v2v.u48xag/*.ovf’: Invalid argument</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1143883">https://bugzilla.redhat.com/1143883</a></p>
<dd> warning shows when converting rhel7 guest:virt-v2v:could not update grub2 console: aug_get: no matching node (ignored)</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1143866">https://bugzilla.redhat.com/1143866</a></p>
<dd> virt-v2v fails with error: cannot open Packages index using db5</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1142416">https://bugzilla.redhat.com/1142416</a></p>
<dd> part-get-name give &#8216;libguestfs: error: part_get_name: parted does not support the machine output (-m)&#8217; error message when run &#8216;part-get-name /dev/sda 1&#8217;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1142186">https://bugzilla.redhat.com/1142186</a></p>
<dd> virt-sysprep option &#8216;&#8211;mount-options&#8217; don&#8217;t work well</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1142158">https://bugzilla.redhat.com/1142158</a></p>
<dd> Illegal command &#8216;part-get-name /dev/sda1 1&#8217; cause libguestfs appliance crashed</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1142004">https://bugzilla.redhat.com/1142004</a></p>
<dd> virt-v2v prints warning:WARNING:/files/boot/grub/device.map references unknown device &#8220;xvda&#8221;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1141723">https://bugzilla.redhat.com/1141723</a></p>
<dd> virt-v2v: error: disk sda has no defined format shows when converting xen hvm guest</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1141680">https://bugzilla.redhat.com/1141680</a></p>
<dd> [<font SIZE="-1">RFE</font>] virt-v2 should support convert a domain with using domain&#8217;s <font SIZE="-1">UUID</font> instead of domain name</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1141631">https://bugzilla.redhat.com/1141631</a></p>
<dd> [<font SIZE="-1">RFE</font>] virt-v2 should support convert a guest to a dir-pool with using pool&#8217;s uuid</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1141157">https://bugzilla.redhat.com/1141157</a></p>
<dd> virt-sysprep option &#8216;&#8211;user-accounts&#8217; don&#8217;t work well</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1141145">https://bugzilla.redhat.com/1141145</a></p>
<dd> virt-v2v fails to convert xen pv guests.</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1141113">https://bugzilla.redhat.com/1141113</a></p>
<dd> virt-v2v fails to convert esx guests</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1140946">https://bugzilla.redhat.com/1140946</a></p>
<dd> qemu-img shows error message for backing file twice</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1140894">https://bugzilla.redhat.com/1140894</a></p>
<dd> No error messages output if append &#8216;&#8211;format qcow2&#8217; after &#8216;-a guest.img&#8217;, guest.img is a raw format image file</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1140547">https://bugzilla.redhat.com/1140547</a></p>
<dd> virt-builder option &#8216;&#8211;format&#8217; don&#8217;t work well</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1140156">https://bugzilla.redhat.com/1140156</a></p>
<dd> <font SIZE="-1">RFE:</font> Export to <font SIZE="-1">RHEV</font> data domain</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1140050">https://bugzilla.redhat.com/1140050</a></p>
<dd> No error shows when multiple conflicting options used with virt-v2v</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1139973">https://bugzilla.redhat.com/1139973</a></p>
<dd> Improve the error info when converting xen guest with no passwordless <font SIZE="-1">SSH</font> access configured</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1139543">https://bugzilla.redhat.com/1139543</a></p>
<dd> Improve the error info when converting guest with no space left</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1138586">https://bugzilla.redhat.com/1138586</a></p>
<dd> No error shows when converting running guest with virt-v2v</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1138184">https://bugzilla.redhat.com/1138184</a></p>
<dd> virt-v2v will fail when converting guests with initramfs-*kdump.img under /boot</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1138182">https://bugzilla.redhat.com/1138182</a></p>
<dd> xen guest will be kernel panic after converted by virt-v2v</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1130189">https://bugzilla.redhat.com/1130189</a></p>
<dd> Annoying message about permissions of /dev/kvm</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1123007">https://bugzilla.redhat.com/1123007</a></p>
<dd> libguestfs &#8216;direct&#8217; backend should close file descriptors before exec-ing qemu to avoid leaking !O_CLOEXEC fds</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1122557">https://bugzilla.redhat.com/1122557</a></p>
<dd> virt-sparsify overwrites block devices if used as output files</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1113156">https://bugzilla.redhat.com/1113156</a></p>
<dd> Empty fstab breaks libguestfs inspection</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1111662">https://bugzilla.redhat.com/1111662</a></p>
<dd> Guestfs.Error(&#8220;vgchange_uuid_all: Volume group has active logical volumes&#8221;)</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1109174">https://bugzilla.redhat.com/1109174</a></p>
<dd> virt-win-reg manual page is corrupted</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1106548">https://bugzilla.redhat.com/1106548</a></p>
<dd> root gets an error accessing to a non-root dir on a snapshot guestmount <font SIZE="-1">VMDK</font> img</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1103877">https://bugzilla.redhat.com/1103877</a></p>
<dd> These APIs also need to add to `guestfish -h` command list</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1102448">https://bugzilla.redhat.com/1102448</a></p>
<dd> mageia package list is incorrect</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1102447">https://bugzilla.redhat.com/1102447</a></p>
<dd> libguestfs 1.27.13 does not build due to libxml library order</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1100498">https://bugzilla.redhat.com/1100498</a></p>
<dd> <font SIZE="-1">RFE:</font> non-polling mechanism to detect guestmount &#8211;no-fork readiness</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1099490">https://bugzilla.redhat.com/1099490</a></p>
<dd> scrub-file can&#8217;t handle link file</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1099284">https://bugzilla.redhat.com/1099284</a></p>
<dd> typo errors in man pages</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1098718">https://bugzilla.redhat.com/1098718</a></p>
<dd> <font SIZE="-1">RFE:</font> virt-builder aliases</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1096465">https://bugzilla.redhat.com/1096465</a></p>
<dd> virt-builder &#8220;proxy=off&#8221; setting doesn&#8217;t turn off the proxy for downloads</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1094746">https://bugzilla.redhat.com/1094746</a></p>
<dd> virt-sparsify man failes to mention what happens to snapshots within a qcow2 image (they are discarded)</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1092753">https://bugzilla.redhat.com/1092753</a></p>
<dd> virt-builder: If several repos contain the same os-version images, then they are duplicated in -l output</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1091803">https://bugzilla.redhat.com/1091803</a></p>
<dd> tar-in-opts execute failed that cause libguestfs appliance crashed</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1088424">https://bugzilla.redhat.com/1088424</a></p>
<dd> virt-resize: libguestfs error: part_set_name: parted: /dev/sdb: Error during translation: Invalid or incomplete multibyte or wide character</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1088262">https://bugzilla.redhat.com/1088262</a></p>
<dd> virt-builder cannot write to a block device</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1085029">https://bugzilla.redhat.com/1085029</a></p>
<dd> Ruby tests fail with latest Ruby</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1079210">https://bugzilla.redhat.com/1079210</a></p>
<dd> virt-sparsify &#8211;in-place cannot sparsify as much as it should</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1079182">https://bugzilla.redhat.com/1079182</a></p>
<dd> virt-df cannot report used disk space of windows guest when updated to 6.5</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1077817">https://bugzilla.redhat.com/1077817</a></p>
<dd> virt-builder error: &#8220;syntax error at line 3: syntax error&#8221;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1056290">https://bugzilla.redhat.com/1056290</a></p>
<dd> virt-sparsify overwrites block devices if used as output files</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/812970">https://bugzilla.redhat.com/812970</a></p>
<dd> virt-rescue cannot set ≥&lt;rescue&gt; prompt, on Ubuntu 12.04</dl>
<h2>RELEASE NOTES FOR LIBGUESTFS 1.26</h2>
<p> These release notes only cover the differences from the previous stable/dev branch split (1.24.0). For detailed changelogs, please see the git repository, or the ChangeLog file distributed in the tarball.</p>
<h3>New features</h3>
<p> <i>Tools</i> </p>
<p> <code><a href="/docs/linux/man/1-virt-customize/">virt-customize</a></code>(1) is a new tool for customizing virtual machine disk images. It lets you install packages, edit configuration files, run scripts, set passwords and so on. <code><a href="/docs/linux/man/1-virt-builder/">virt-builder</a></code>(1) and <code><a href="/docs/linux/man/1-virt-sysprep/">virt-sysprep</a></code>(1) use virt-customize, and command line options across all these tools are now identical. </p>
<p> <code><a href="/docs/linux/man/1-virt-diff/">virt-diff</a></code>(1) is a new tool for showing the differences between the filesystems of two virtual machines. It is mainly useful when showing what files have been changed between snapshots. </p>
<p> <code><a href="/docs/linux/man/1-virt-builder/">virt-builder</a></code>(1) has been greatly enhanced. There are many more ways to customize the virtual machine. It can pull templates from multiple repositories. A parallelized internal xzcat implementation speeds up template decompression. Virt-builder uses an optimizing planner to choose the fastest way to build the <font SIZE="-1">VM.</font> It is now easier to use virt-builder from other programs. Internationalization support has been added to metadata. More efficient SELinux relabelling of files. Can build guests for multiple architectures. Error messages have been improved. (Pino Toscano) </p>
<p> <code><a href="/docs/linux/man/1-virt-sparsify/">virt-sparsify</a></code>(1) has a new <i>&#8211;in-place</i> option. This sparsifies an image in place (without copying it) and is also much faster. (Lots of help provided by Paolo Bonzini) </p>
<p> <code><a href="/docs/linux/man/1-virt-sysprep/">virt-sysprep</a></code>(1) can delete and scrub files under user control. You can lock user accounts or set random passwords on accounts. Can remove more log files. Can unsubscribe a guest from Red Hat Subscription Manager. New flexible way to enable and disable operations. (Wanlong Gao, Pino Toscano) </p>
<p> <code><a href="/docs/linux/man/1-virt-win-reg/">virt-win-reg</a></code>(1) allows you to use URIs to specify remote disk images. </p>
<p> <code><a href="/docs/linux/man/1-virt-format/">virt-format</a></code>(1) can now pass the extra space that it recovers back to the host. </p>
<p> <code><a href="/docs/linux/man/1-guestfish/">guestfish</a></code>(1) has additional environment variables to give fine control over the <tt>&quot;&gt;&lt;fs&gt;&quot;</tt> prompt. Guestfish reads its (rarely used) configuration file in a different order now so that local settings override global settings. (Pino Toscano) </p>
<p> <code><a href="/docs/linux/man/1-virt-make-fs/">virt-make-fs</a></code>(1) was rewritten in C, but is unchanged in terms of functionality and command line usage. </p>
<p> <i>Language bindings</i> </p>
<p> The OCaml bindings have a new <tt>&quot;Guestfs.Errno&quot;</tt> module, used to check the error number returned by <tt>&quot;Guestfs.last_errno&quot;</tt>. </p>
<p> <font SIZE="-1">PHP</font> tests now work. (Pino Toscano) </p>
<p> <i>Inspection</i> </p>
<p> Inspection can recognize Debian live images. </p>
<p> <i>Architectures</i> </p>
<p> ARMv7 (32 bit) now supports <font SIZE="-1">KVM</font> acceleration. </p>
<p> Aarch64 (<font SIZE="-1">ARM 64</font> bit) is supported, but the appliance part does not work yet. </p>
<p> <font SIZE="-1">PPC64</font> support has been fixed and enhanced.</p>
<h3>Security</h3>
<dl>
<dt>Denial of service when inspecting disk images with corrupt btrfs volumes</p>
<dd> It was possible to crash libguestfs (and programs that use libguestfs as a library) by presenting a disk image containing a corrupt btrfs volume. </p>
<p> This was caused by a <font SIZE="-1">NULL</font> pointer dereference causing a denial of service, and is not thought to be exploitable any further. </p>
<p> See commit d70ceb4cbea165c960710576efac5a5716055486 for the fix. This fix is included in libguestfs stable branches ≥ 1.26.0, ≥ 1.24.6 and ≥ 1.22.8, and also in <font SIZE="-1">RHEL</font> ≥ 7.0. Earlier versions of libguestfs are not vulnerable.</p>
<dt>Better generation of random root passwords and random seeds</p>
<dd> When generating random root passwords and random seeds, two bugs were fixed which are possibly security related. Firstly we no longer read excessive bytes from <i>/dev/urandom</i> (most of which were just thrown away). Secondly we changed the code to avoid modulo bias. These issues were not thought to be exploitable. (Both changes suggested by Edwin Török)</dl>
<h3><font SIZE="-1">API</font></h3>
<p> <font SIZE="-1">GUID</font> parameters are now validated when they are passed to <font SIZE="-1">API</font> calls, whereas previously you could have passed any string. (Pino Toscano) </p>
<p> <i>New APIs</i></p>
<dl>
<dt>&quot;guestfs_add_drive_opts&quot;: new &quot;discard&quot; parameter</p>
<dd> The new <tt>&quot;discard&quot;</tt> parameter allows fine-grained control over discard/trim support for a particular disk. This allows the host file to become more sparse (or thin-provisioned) when you delete files or issue the <tt>&quot;guestfs_fstrim&quot;</tt> <font SIZE="-1">API</font> call.</p>
<dt>&quot;guestfs_add_domain&quot;: new parameters: &quot;cachemode&quot;, &quot;discard&quot;</p>
<dd> These parameters are passed through when adding the domain&#8217;s disks.</p>
<dt>&quot;guestfs_blkdiscard&quot;</p>
<dd> Discard all blocks on a guestfs device. Combined with the <tt>&quot;discard&quot;</tt> parameter above, this makes the host file sparse.</p>
<dt>&quot;guestfs_blkdiscardzeroes&quot;</p>
<dd> Test if discarded blocks read back as zeroes.</p>
<dt>&quot;guestfs_compare_*&quot;</p>
<dd>
<dt>&quot;guestfs_copy_*&quot;</p>
<dd> For each struct returned through the <font SIZE="-1">API,</font> libguestfs now generates <tt>&quot;guestfs_compare_*&quot;</tt> and <tt>&quot;guestfs_copy_*&quot;</tt> functions to allow you to compare and copy structs.</p>
<dt>&quot;guestfs_copy_attributes&quot;</p>
<dd> Copy attributes (like permissions, xattrs, ownership) from one file to another. (Pino Toscano)</p>
<dt>&quot;guestfs_disk_create&quot;</p>
<dd> A flexible <font SIZE="-1">API</font> for creating empty disk images from scratch. This avoids the need to call out to external programs like <code><a href="/docs/linux/man/1-qemu-img/">qemu-img</a></code>(1).</p>
<dt>&quot;guestfs_get_backend_settings&quot;</p>
<dd>
<dt>&quot;guestfs_set_backend_settings&quot;</p>
<dd> Per-backend settings (can also be set via the environment variable <tt>&quot;LIBGUESTFS_BACKEND_SETTINGS&quot;</tt>). The main use for this is forcing <font SIZE="-1">TCG</font> mode in the qemu-based backends, for example: </p>
<pre>
 export LIBGUESTFS_BACKEND=direct
 export LIBGUESTFS_BACKEND_SETTINGS=force_tcg
</pre>
<dt>&quot;guestfs_part_get_name&quot;</p>
<dd> Get the label or name of a partition (for <font SIZE="-1">GPT</font> disk images).</dl>
<h3>Build changes</h3>
<p> The following extra packages are required to build libguestfs 1.26:</p>
<dl>
<dt>supermin ≥ 5</p>
<dd> Supermin version 5 is required to build this version of libguestfs.</p>
<dt>flex, bison</p>
<dd> Virt-builder now uses a real parser to parse its metadata file, so these tools are required.</p>
<dt>xz</p>
<dd> This is now a required build dependency, where previously it was (in theory) optional.</dl>
<h3>Internals</h3>
<p> <font SIZE="-1">PO</font> message extraction rewritten to be more robust. (Pino Toscano) </p>
<p> <tt>&quot;podwrapper&quot;</tt> gives an error if the <i>&#8211;insert</i> or <i>&#8211;verbatim</i> argument pattern is not found. </p>
<p> Libguestfs now passes the qemu <i>-enable-fips</i> option to enable <font SIZE="-1">FIPS,</font> if qemu supports it. </p>
<p> <tt>&quot;./configure --without-qemu&quot;</tt> can be used if you don&#8217;t want to specify a default hypervisor. </p>
<p> Copy-on-write [<font SIZE="-1">COW</font>] overlays, used for example for read-only drives, are now created through an internal backend <font SIZE="-1">API</font> (<tt>&quot;.create_cow_overlay&quot;</tt>). </p>
<p> Libvirt backend uses some funky C macros to generate <font SIZE="-1">XML.</font> These are simpler and safer. </p>
<p> The ChangeLog file format has changed. It is now just the same as <tt>&quot;git log&quot;</tt>, instead of using a custom format. </p>
<p> Appliance start-up has changed:</p>
<dl>
<dt>&bull;</p>
<dd> The libguestfs appliance now initializes <font SIZE="-1">LVM</font> the same way as it is done on physical machines.</p>
<dt>&bull;</p>
<dd> The libguestfs appliance does not write an empty string to <i>/proc/sys/kernel/hotplug</i> when starting up. </p>
<p> Note that you <code>must</code> configure your kernel to have <tt>&quot;CONFIG_UEVENT_HELPER_PATH=&quot;&quot;&quot;</tt> otherwise you will get strange <font SIZE="-1">LVM</font> errors (this applies as much to any Linux machine, not just libguestfs). (Peter Rajnoha)</dl>
<p> Libguestfs can now be built on arches that have <code><a href="/docs/linux/man/1-ocamlc/">ocamlc</a></code>(1) but not <code><a href="/docs/linux/man/1-ocamlopt/">ocamlopt</a></code>(1). (Hilko Bengen, Olaf Hering) </p>
<p> You cannot use <tt>&quot;./configure --disable-daemon --enable-appliance&quot;</tt>. It made no sense anyway. Now it is expressly forbidden by the configure script. </p>
<p> The packagelist file uses <tt>&quot;m4&quot;</tt> for macro expansion instead of <tt>&quot;cpp&quot;</tt>.</p>
<h3>Bugs fixed</h3>
<dl>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1073906">https://bugzilla.redhat.com/1073906</a></p>
<dd> java bindings inspect_list_applications2 throws java.lang.ArrayIndexOutOfBoundsException:</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1063374">https://bugzilla.redhat.com/1063374</a></p>
<dd> [<font SIZE="-1">RFE</font>] enable subscription manager clean or unregister operation to sysprep</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1060404">https://bugzilla.redhat.com/1060404</a></p>
<dd> virt-resize does not preserve <font SIZE="-1">GPT</font> partition names</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1057504">https://bugzilla.redhat.com/1057504</a></p>
<dd> mount-local should give a clearer error if root is not mounted</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1056290">https://bugzilla.redhat.com/1056290</a></p>
<dd> virt-sparsify overwrites block devices if used as output files</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1055452">https://bugzilla.redhat.com/1055452</a></p>
<dd> libguestfs: error: invalid backend: appliance</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1054761">https://bugzilla.redhat.com/1054761</a></p>
<dd> guestfs_pvs prints &#8220;unknown device&#8221; if a physical volume is missing</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1053847">https://bugzilla.redhat.com/1053847</a></p>
<dd> Recommended default clock/timer settings</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1046509">https://bugzilla.redhat.com/1046509</a></p>
<dd> ruby-libguestfs throws &#8220;expecting 0 or 1 arguments&#8221; on Guestfs::Guestfs.new</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1045450">https://bugzilla.redhat.com/1045450</a></p>
<dd> Cannot inspect cirros 0.3.1 disk image fully</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1045033">https://bugzilla.redhat.com/1045033</a></p>
<dd> LIBVIRT_DEFAULT_URI=<a href="qemu:///system">qemu:///system</a> breaks libguestfs</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1044585">https://bugzilla.redhat.com/1044585</a></p>
<dd> virt-builder network (eg. &#8211;install) doesn&#8217;t work if resolv.conf sets nameserver 127.0.0.1</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1044014">https://bugzilla.redhat.com/1044014</a></p>
<dd> When <font SIZE="-1">SSSD</font> is installed, libvirt configuration requires authentication, but not clear to user</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1039995">https://bugzilla.redhat.com/1039995</a></p>
<dd> virt-make-fs fails making fat/vfat whole disk: Device partition expected, not making filesystem on entire device &#8216;/dev/sda&#8217; (use -I to override)</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1039540">https://bugzilla.redhat.com/1039540</a></p>
<dd> virt-sysprep to delete more logfiles</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1033207">https://bugzilla.redhat.com/1033207</a></p>
<dd> <font SIZE="-1">RFE:</font> libguestfs inspection does not recognize Free4NAS live <font SIZE="-1">CD</font></p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1028660">https://bugzilla.redhat.com/1028660</a></p>
<dd> <font SIZE="-1">RFE:</font> virt-sysprep/virt-builder should have an option to lock a user account</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1026688">https://bugzilla.redhat.com/1026688</a></p>
<dd> libguestfs fails examining libvirt guest with ceph drives: rbd: image name must begin with a &#8216;/&#8217;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1022431">https://bugzilla.redhat.com/1022431</a></p>
<dd> virt-builder fails if <tt>$HOME</tt>/.cache doesn&#8217;t exist</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1022184">https://bugzilla.redhat.com/1022184</a></p>
<dd> libguestfs: do not use versioned jar file</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1020806">https://bugzilla.redhat.com/1020806</a></p>
<dd> All libguestfs <font SIZE="-1">LVM</font> operations fail on Debian/Ubuntu</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1008417">https://bugzilla.redhat.com/1008417</a></p>
<dd> Need update helpout of part-set-gpt-type</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/953907">https://bugzilla.redhat.com/953907</a></p>
<dd> virt-sysprep does not correctly set the hostname on Debian/Ubuntu</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/923355">https://bugzilla.redhat.com/923355</a></p>
<dd> guestfish prints literal &#8220;
&#8221; in error messages</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/660687">https://bugzilla.redhat.com/660687</a></p>
<dd> guestmount: &#8220;touch&#8221; command fails: touch: setting times of `timestamp&#8217;: Invalid argument</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/593511">https://bugzilla.redhat.com/593511</a></p>
<dd> [<font SIZE="-1">RFE</font>] function to get partition name</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/563450">https://bugzilla.redhat.com/563450</a></p>
<dd> list-devices returns devices of different types out of order</dl>
<h2>RELEASE NOTES FOR LIBGUESTFS 1.24</h2>
<p> These release notes only cover the differences from the previous stable/dev branch split (1.22.0). For detailed changelogs, please see the git repository, or the ChangeLog file distributed in the tarball.</p>
<h3>New features</h3>
<p> User-Mode Linux (<font SIZE="-1">UML</font>) can be used as an alternative backend (ie. instead of <font SIZE="-1">KVM</font>). This improves performance especially when using libguestfs inside a <font SIZE="-1">VM</font> (eg. in the cloud). <font SIZE="-1">UML</font> is supported as a first-class backend. See &#8220;USER-MODE <font SIZE="-1">LINUX BACKEND&#8221;</font> in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3) for how to use this. </p>
<p> <font SIZE="-1">ARM</font> (32 bit) and <font SIZE="-1">PPC64</font> are now fully supported. </p>
<p> <i>Tools</i> </p>
<p> <code><a href="/docs/linux/man/1-virt-builder/">virt-builder</a></code>(1) is a new tool for building virtual machine images. It lets you rapidly and securely create guests and customize them. </p>
<p> New <code><a href="/docs/linux/man/1-virt-sysprep/">virt-sysprep</a></code>(1) operations: Remove files in <i>/tmp</i> and <i>/var/tmp</i>. Remove <font SIZE="-1">RPM</font> database files. Change root and user passwords. More log files are removed. New operations which are not enabled by default: Create random UUIDs for filesystems. Reset firewall rules. (Wanlong Gao) </p>
<p> <code><a href="/docs/linux/man/1-virt-resize/">virt-resize</a></code>(1) and virt-sysprep can now use URIs to specify a remote disk. </p>
<p> Use <tt>&quot;guestfish -N filename=type&quot;</tt> to create a named disk image (instead of the default <i>test1.img</i> etc). </p>
<p> <code><a href="/docs/linux/man/1-virt-sparsify/">virt-sparsify</a></code>(1) now tests if there is enough disk space to complete the operation, instead of possibly running out of space half way through. </p>
<p> <code><a href="/docs/linux/man/1-virt-format/">virt-format</a></code>(1) and <code><a href="/docs/linux/man/1-virt-make-fs/">virt-make-fs</a></code>(1): new <i>&#8211;label</i> option for setting filesystem label. </p>
<p> virt-resize <i>&#8211;no-sparse</i> flag can be used to resize on to partitions and other targets that are not zeroed. </p>
<p> <i>Language bindings</i> </p>
<p> New bindings for the Go programming language. </p>
<p> <i></i><font SIZE="-1"><i>API</i></font><i></i> </p>
<p> Support for the systemd journal. </p>
<p> <tt>&quot;guestfs_add_drive_opts&quot;</tt> can now control the qemu caching mode through a new <tt>&quot;cachemode&quot;</tt> parameter. You can select improved performance for temporary drives, or safety. </p>
<p> <tt>&quot;guestfs_set_label&quot;</tt> now works for <font SIZE="-1">XFS</font> and btrfs. </p>
<p> New <font SIZE="-1">GUESTFS_EVENT_WARNING</font> event for warning messages. </p>
<p> <i>Inspection</i> </p>
<p> Better inspection of <font SIZE="-1">SUSE</font> guests (Olaf Hering). </p>
<p> Better support for non-standard Windows <tt>%systemroot</tt>% (Matthew Booth). </p>
<p> Enhanced error reporting for Augeas errors.</p>
<h3>Security</h3>
<dl>
<dt><font SIZE="-1">CVE-2013-2124</font></p>
<dd> <a rel="nofollow" href="https://bugzilla.redhat.com/show_bug.cgi?id=968306">https://bugzilla.redhat.com/show_bug.cgi?id=968306</a> </p>
<p> A denial of service was possible when inspecting certain guests. The fix has been backported to 1.20 and 1.22 branches.</p>
<dt><font SIZE="-1">CVE-2013-4419</font></p>
<dd> <a rel="nofollow" href="https://www.redhat.com/archives/libguestfs/2013-October/msg00031.html">https://www.redhat.com/archives/libguestfs/2013-October/msg00031.html</a> </p>
<p> Fix insecure temporary directory handling for remote guestfish. The fix has been backported to 1.20 and 1.22 branches.</dl>
<h3>New APIs</h3>
<pre>
 add-drive-scratch: Add a temporary scratch drive
 aug-label
 aug-setm
 journal-open: Systemd journal support
 journal-close
 journal-next
 journal-skip
 journal-get
 journal-get-data-threshold
 journal-set-data-threshold
 remount: Allow rw flag to be adjusted on mounted filesystems
 set-uuid: Set UUID of filesystem
</pre>
<p> <tt>&quot;is-file&quot;</tt>, <tt>&quot;is-dir&quot;</tt>, <tt>&quot;is-blockdev&quot;</tt>, <tt>&quot;is-chardev&quot;</tt>, <tt>&quot;is-fifo&quot;</tt>, <tt>&quot;is-socket&quot;</tt> APIs now have an extra <tt>&quot;followsymlinks&quot;</tt> flag. </p>
<p> <tt>&quot;add-drive&quot;</tt> has a new <tt>&quot;cachemode&quot;</tt> parameter.</p>
<h3>Build changes</h3>
<p> The following packages are required to build libguestfs 1.24:</p>
<dl>
<dt>Augeas ≥ 1.0.0</p>
<dd></dl>
<p> The following optional packages may be added to enhance functionality but are not required:</p>
<dl>
<dt>sd-journal</p>
<dd> To read journal files from guests which use that.</p>
<dt>url_mkcow</p>
<dd> For <font SIZE="-1">UML</font> backend.</p>
<dt>curl</p>
<dd>
<dt>gpg</p>
<dd>
<dt>xz</p>
<dd> For virt-builder.</p>
<dt>golang ≥ 1.1.1</p>
<dd> For Go language bindings.</dl>
<h3>Internals</h3>
<p> New <tt>&quot;make check-*&quot;</tt> rules replace <tt>&quot;make extra-tests&quot;</tt>. See <tt>&quot;make help&quot;</tt> and <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3) for details. </p>
<p> Perl code can now be valgrinded. </p>
<p> Inspection code is now fuzz-tested. </p>
<p> <tt>&quot;make&quot;</tt> no longer recurses into the generator directory in every other directory. This reduces the overhead of builds considerably. </p>
<p> Additional tests for Augeas, hivex. </p>
<p> Add a launch timeout of 20 minutes waiting for the appliance to start up. </p>
<p> Add a timeout (4 hours) to all tests so we can catch the case where qemu or other components hang. </p>
<p> Use kvmclock and <tt>&quot;-cpu host&quot;</tt>. This improves clock stability and overall performance. </p>
<p> <tt>&quot;./configure --enable-packet-dump&quot;</tt> mode is fixed. </p>
<p> <tt>&quot;./configure --enable-valgrind-daemon&quot;</tt> mode has been rewritten. It is now feasible for developers to keep this flag enabled at all times. </p>
<p> Backends have been refactored to be modular (although they are not actually loadable modules). </p>
<p> When enabled, the network now uses resolver configuration (ie. /etc/resolv.conf) from the host.</p>
<h3>Bugs fixed</h3>
<dl>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1019889">https://bugzilla.redhat.com/1019889</a></p>
<dd> libguestfs-tools.conf should have a man page</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1018149">https://bugzilla.redhat.com/1018149</a></p>
<dd> valgrind errors in btrfs_subvolume_list</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1002032">https://bugzilla.redhat.com/1002032</a></p>
<dd> mke2fs can&#8217;t return the correct filesystem type when blockscount is less than 2048 for ext3</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1001876">https://bugzilla.redhat.com/1001876</a></p>
<dd> Update &#8220;rsync-out&#8221; helpout for using wildcard</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1001875">https://bugzilla.redhat.com/1001875</a></p>
<dd> Argument &#8216;excludes&#8217; of tar-out does not work</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1000428">https://bugzilla.redhat.com/1000428</a></p>
<dd> virt-format uses wrong partition type for vfat filesystems</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/1000121">https://bugzilla.redhat.com/1000121</a></p>
<dd> &#8216;sh&#8217; command before mount causes daemon to segfault</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/998513">https://bugzilla.redhat.com/998513</a></p>
<dd> guestfish does not work when you mix &#8211;remote and &#8211;add options</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/998482">https://bugzilla.redhat.com/998482</a></p>
<dd> guestfish remote prints &#8220;libguestfs: error: waitpid (qemu): No child processes&#8221;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/995711">https://bugzilla.redhat.com/995711</a></p>
<dd> list-filesystems command fails if there are no block devices</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/994517">https://bugzilla.redhat.com/994517</a></p>
<dd> cache=none/O_DIRECT workaround doesn&#8217;t work for images with backing files</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/989356">https://bugzilla.redhat.com/989356</a></p>
<dd> cap-get-file will return error if the file has not be set capabilities</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/986877">https://bugzilla.redhat.com/986877</a></p>
<dd> <font SIZE="-1">RFE:</font> Implement set-uuid command</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/986875">https://bugzilla.redhat.com/986875</a></p>
<dd> <font SIZE="-1">RFE:</font> Implement set-label for xfs</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/985269">https://bugzilla.redhat.com/985269</a></p>
<dd> Can&#8217;t set acl value for a specified user with &#8216;acl-set-file&#8217;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/983218">https://bugzilla.redhat.com/983218</a></p>
<dd> libguestfs double free when kernel link fails during launch</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/981715">https://bugzilla.redhat.com/981715</a></p>
<dd> Make xfs filesystem failed with specified blocksize, gives &#8220;unknown option -b&#8221; error</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/981683">https://bugzilla.redhat.com/981683</a></p>
<dd> &#8220;hivex-commit&#8221; should fail with a relative path</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/981663">https://bugzilla.redhat.com/981663</a></p>
<dd> disk-format &#8220;qemu-img info: <font SIZE="-1">JSON</font> parse error&#8221; when target file does not exist</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/978302">https://bugzilla.redhat.com/978302</a></p>
<dd> mke2fs-J should give a meaningful error when specified type is anything except &#8216;ext{2,3,4}&#8217;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/975797">https://bugzilla.redhat.com/975797</a></p>
<dd> Specifying virtio interface (&#8216;iface&#8217; parameter) breaks the direct backend &#8211; libguestfs hangs</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/975753">https://bugzilla.redhat.com/975753</a></p>
<dd> &#8220;virt-resize &#8211;expand&#8221; and &#8220;virt-resize &#8211;resize&#8221; outputs error message for Win2008 32bit <font SIZE="-1">OS</font></p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/975412">https://bugzilla.redhat.com/975412</a></p>
<dd> inspection: Augeas expressions are broken with augeas &gt;= 0.10</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/974904">https://bugzilla.redhat.com/974904</a></p>
<dd> virt-resize &#8211;expand fails on Ubuntu Cloud Image</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/974489">https://bugzilla.redhat.com/974489</a></p>
<dd> Regression: Fedora inspection broken by change from guestfs_exists to guestfs_is_file</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/972775">https://bugzilla.redhat.com/972775</a></p>
<dd> txz-out command produces a bzip2-compressed file (should be xz-compressed)</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/969845">https://bugzilla.redhat.com/969845</a></p>
<dd> upload to a directory occasionally hangs instead of failing</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/968875">https://bugzilla.redhat.com/968875</a></p>
<dd> virt-sysprep should support URL-type arguments</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/624334">https://bugzilla.redhat.com/624334</a></p>
<dd> blockdev-setbsz succeeds, but does not affect blockdev-getbsz</dl>
<h2>RELEASE NOTES FOR LIBGUESTFS 1.22</h2>
<p> These release notes only cover the differences from the previous stable/dev branch split (1.20.0). For detailed changelogs, please see the git repository, or the ChangeLog file distributed in the tarball.</p>
<h3>New features</h3>
<p> <i></i><font SIZE="-1"><i>API</i></font><i></i> </p>
<p> Remote access to disks:</p>
<dl>
<dt>&bull;</p>
<dd> Network Block Device (nbd)</p>
<dt>&bull;</p>
<dd> Secure Shell (ssh)</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">HTTP</font> and <font SIZE="-1">HTTPS</font></p>
<dt>&bull;</p>
<dd> <font SIZE="-1">FTP</font> and <font SIZE="-1">FTPS</font></p>
<dt>&bull;</p>
<dd> iSCSI</p>
<dt>&bull;</p>
<dd> Gluster</p>
<dt>&bull;</p>
<dd> Ceph/rbd (Mike Kelly)</p>
<dt>&bull;</p>
<dd> Sheepdog</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">TFTP</font></dl>
<p> The <font SIZE="-1">SYSLINUX</font> and <font SIZE="-1">EXTLINUX</font> bootloaders can now be installed in disk images using the <font SIZE="-1">API.</font> </p>
<p> Inspection can now handle filesystems such as btrfs where subvolumes are separately mountable (Matthew Booth). </p>
<p> &#8220;Attach methods&#8221; are now known as &#8220;backends&#8221;. Compatibility with existing code is preserved. </p>
<p> Filenames can contain &#8216;:&#8217;, as long as newer <font SIZE="-1">QEMU</font> is being used. </p>
<p> <i>Tools</i> </p>
<p> Virt-alignment-scan and virt-df scan multiple guests in parallel. </p>
<p> Guestmount now passes errno accurately back to userspace in almost all cases. </p>
<p> Guestfish and other tools can now use a URI-like syntax to access remote disks, eg: </p>
<pre>
 guestfish -a <a href="ssh://example.com/path/to/disk.img">ssh://example.com/path/to/disk.img</a>
</pre>
<p> Guestfish and guestmount now allow you to specify the filesystem type when mounting, which is more secure (Dave Vasilevsky). </p>
<p> Guestfish is now the &#8220;guest filesystem shell&#8221;. </p>
<p> Guestfish allows only <tt>1</tt> <tt>&quot;true&quot;</tt> <tt>&quot;t&quot;</tt> <tt>&quot;yes&quot;</tt> <tt>&quot;y&quot;</tt> <tt>&quot;on&quot;</tt> <tt>0</tt> <tt>&quot;false&quot;</tt> <tt>&quot;f&quot;</tt> <tt>&quot;no&quot;</tt> <tt>&quot;n&quot;</tt> <tt>&quot;off&quot;</tt> for boolean values (case insensitive), and gives an error for all other strings. </p>
<p> New tool <tt>&quot;guestunmount&quot;</tt> for unmounting <font SIZE="-1">FUSE</font> filesystems safely. </p>
<p> <tt>&quot;guestmount --no-fork&quot;</tt> flag prevents guestmount from daemonizing. </p>
<p> Virt-resize now uses sparse copies by default, saving considerable space for guests which are mostly empty. </p>
<p> Bash tab completion has been rewritten and can now handle most tools, and correctly tab-complete <tt>&quot;--long&quot;</tt> options. In addition, bash completion scripts are loaded on demand. </p>
<p> <i>Language bindings</i> </p>
<p> The Java <font SIZE="-1">API</font> now supports events. </p>
<p> The Python object now inherits from the <tt>&quot;object&quot;</tt> base class. </p>
<p> Python methods which previously returned lists of tuples can now be made to return a Python dict. For backwards compatibility, you have to enable this by using the constructor option <tt>&quot;guestfs.GuestFS (python_return_dict=True)&quot;</tt>. </p>
<p> The <font SIZE="-1">PHP</font> bindings are now tested properly, and have had multiple fixes. </p>
<p> The long-deprecated Perl <tt>&quot;Sys::Guestfs::Lib&quot;</tt> library has been removed. <a rel="nofollow" href="https://www.redhat.com/archives/libguestfs/2013-April/msg00001.html">https://www.redhat.com/archives/libguestfs/2013-April/msg00001.html</a> </p>
<p> <i>Examples</i> </p>
<p> New example program showing how to enable debugging and capture log messages. </p>
<p> <i>Other</i> </p>
<p> Distributors can add arbitrary extra packages to the appliance by doing: </p>
<pre>
 ./configure --with-extra-packages=&quot;list of package names&quot;
</pre>
<p> Distributors can use: </p>
<pre>
 ./configure --with-supermin-extra-options=&quot;...&quot;
</pre>
<p> to add arbitrary extra options to supermin.</p>
<h3>Security</h3>
<p> No security issues were found in this release.</p>
<h3>New APIs</h3>
<pre>
 cp-r
 extlinux
 feature-available
 get-program
 is-whole-device
 part-get-gpt-type
 part-set-gpt-type
 rename
 set-program
 syslinux
</pre>
<p> C only: </p>
<pre>
 guestfs_event_to_string
</pre>
<h3>Internals</h3>
<p> The febootstrap tool has now been renamed to &#8220;supermin&#8221;. Libguestfs can use either, but now prefers &#8220;supermin&#8221;. <a rel="nofollow" href="http://people.redhat.com/~rjones/supermin/">http://people.redhat.com/~rjones/supermin/</a> </p>
<p> libxml2 is required to build libguestfs. </p>
<p> The hivexregedit program (from hivex) is required to build from git. </p>
<p> Internal functions can no longer be used unless the caller defines <tt>&quot;-DGUESTFS_PRIVATE=1&quot;</tt>. </p>
<p> Enable C compiler warnings in Python, Ruby bindings. </p>
<p> Fail early and clearly if libvirt does not support qemu/KVM (eg. if default libvirt connection is to Xen). </p>
<p> <tt>&quot;make print-subdirs&quot;</tt> rule, useful for selectively running tests. </p>
<p> Multiple fixes to allow separated (sourcedir != builddir) builds. </p>
<p> Multiple fixes to Haskell bindings. </p>
<p> <tt>&quot;ln&quot;</tt> and <tt>&quot;ln-f&quot;</tt> APIs now capture <tt>&quot;errno&quot;</tt> correctly. </p>
<p> Language binding tests use (mostly) a standard numbering scheme and aim to test the same range of features in each language. Also the number of launches required has been reduced so these tests should run much more quickly. </p>
<p> Library code internally uses <font SIZE="-1">GCC</font> <tt>&quot;__attribute__((cleanup))&quot;</tt> (if available) to simplify memory allocation. </p>
<p> Internal header files have been reorganized. See the comments in <i>src/guestfs-internal*.h</i> </p>
<p> Internal code shared between the library and certain tools is now located in a static <tt>&quot;libutils&quot;</tt> library. </p>
<p> Almost all subdirectories can now use parallel builds, although note that the top-level directories still build in series. </p>
<p> Use of <tt>&quot;PATH_MAX&quot;</tt> and <tt>&quot;NAME_MAX&quot;</tt> has been eliminated from the code. </p>
<p> The Java <font SIZE="-1">API</font> now requires <font SIZE="-1">JVM</font> ≥ 1.6. </p>
<p> Force use of <tt>&quot;serial-tests&quot;</tt> with automake ≥ 1.12. </p>
<p> Use of sockets in the library protocol layer is abstracted, allowing other non-POSIX layers to be added in future (see <i>src/conn-socket.c</i>). </p>
<p> <tt>&quot;qemu-img info --output json&quot;</tt> is used if available, for more secure parsing of the output of this command. </p>
<p> Distros can now use <tt>&quot;make INSTALLDIRS=vendor install&quot;</tt> to place Ruby bindings in vendordir. This eliminates a non-upstream patch carried by both Fedora and Debian. </p>
<p> Valgrind log files are now written to <i>tmp/valgrind-</i><font SIZE="-1"><i>DATE</i></font><i>&#8211;</i><font SIZE="-1"><i>PID</i></font><i>.log</i> </p>
<p> <tt>&quot;make clean&quot;</tt> cleans the local <tt>&quot;tmp/&quot;</tt> directory. </p>
<p> The C <font SIZE="-1">API</font> tests have been rewritten using a more flexible generator language that allows arbitrary C code to be executing during tests.</p>
<h3>Bugs fixed</h3>
<dl>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/961812">https://bugzilla.redhat.com/961812</a></p>
<dd> Segfault in inspect-fs.c in mountable code</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/957772">https://bugzilla.redhat.com/957772</a></p>
<dd> tar-out and base64-out quoting error</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/957380">https://bugzilla.redhat.com/957380</a></p>
<dd> libguestfs: error: btrfsvol:/dev/sda2/root: root device not found: only call this function with a root device previously returned by guestfs_inspect_os</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/948324">https://bugzilla.redhat.com/948324</a></p>
<dd> inspection fails if libosinfo is not installed</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/928995">https://bugzilla.redhat.com/928995</a></p>
<dd> file on zero-sized file now produces &#8220;empty &#8221; instead of &#8220;empty&#8221;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/921292">https://bugzilla.redhat.com/921292</a></p>
<dd> qemu: could not open disk image /tmp/&#8230;/snapshot1: Permission denied</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/921040">https://bugzilla.redhat.com/921040</a></p>
<dd> &#8220;error: external command failed, see earlier error messages&#8221; message needs to change</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/920225">https://bugzilla.redhat.com/920225</a></p>
<dd> libguestfs should use &#8211;output json (if supported) to safely parse the output of qemu-img command</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/916780">https://bugzilla.redhat.com/916780</a></p>
<dd> feature request: guestmount &#8211;with-cleanup-pipefd</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/914934">https://bugzilla.redhat.com/914934</a></p>
<dd> oom-killer kills guestfsd when tar-in a lot of data</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/914931">https://bugzilla.redhat.com/914931</a></p>
<dd> FileIn commands cause segfault if appliance dies during the file copy in</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/913145">https://bugzilla.redhat.com/913145</a></p>
<dd> Misc leaks in virNetClientProgramCall in libvirt 1.0.2</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/912499">https://bugzilla.redhat.com/912499</a></p>
<dd> Security context on image file gets reset</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/909836">https://bugzilla.redhat.com/909836</a></p>
<dd> libguestfs-test-tool &#8211;qemu segfaults</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/909624">https://bugzilla.redhat.com/909624</a></p>
<dd> Unexpected non-tail recursion in recv_from_daemon results in stack overflow in very long-running <font SIZE="-1">API</font> calls that send progress messages</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/908322">https://bugzilla.redhat.com/908322</a></p>
<dd> virt-tar fails on non-existent directory names &#8220;error in chunked encoding at /home/rjones/d/libguestfs/tools/virt-tar line 272.&#8221;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/908321">https://bugzilla.redhat.com/908321</a></p>
<dd> virt-cat fails on directory names &#8220;/dev/stdout: error in chunked encoding&#8221;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/907554">https://bugzilla.redhat.com/907554</a></p>
<dd> btrfs causes subsequent ntfs-3g filesystem to fail</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/905341">https://bugzilla.redhat.com/905341</a></p>
<dd> &#8220;No such file or directory&#8221; when execute &#8220;hivex-commit&#8221;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/903620">https://bugzilla.redhat.com/903620</a></p>
<dd> btrfs_subvolume_list broken due to change in subvolume list output</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/895910">https://bugzilla.redhat.com/895910</a></p>
<dd> guestmount: <code>rename()</code> incorrectly follows symbolic links</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/895905">https://bugzilla.redhat.com/895905</a></p>
<dd> guestmount: <code>link()</code> incorrectly returns <font SIZE="-1">ENOENT,</font> when it should be <font SIZE="-1">EXDEV</font></p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/895904">https://bugzilla.redhat.com/895904</a></p>
<dd> checksums-out fail to compute the checksums of all regular files in directory</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/894545">https://bugzilla.redhat.com/894545</a></p>
<dd> libguestfs <font SIZE="-1">FTBFS</font> on Fedora 19 because of new ruby</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/890027">https://bugzilla.redhat.com/890027</a></p>
<dd> virt-sysprep: Setting hostname, domain name and pretty name on Fedora 18 correctly</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/887971">https://bugzilla.redhat.com/887971</a></p>
<dd> pvcreate fails if partition contains a swap signature</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/887520">https://bugzilla.redhat.com/887520</a></p>
<dd> zero_free_space: open: /sysroot//ujqqq135.rd3: Cannot allocate memory</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/886915">https://bugzilla.redhat.com/886915</a></p>
<dd> libguestfs with libvirt attach-method fails with odd error if default hypervisor is Xen</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/847549">https://bugzilla.redhat.com/847549</a></p>
<dd> Adding a zero-length virtio-scsi disk causes: qemu-kvm: hw/scsi-bus.c:1568: scsi_req_complete: Assertion `req-&gt;status == -1&#8242; failed.</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/811649">https://bugzilla.redhat.com/811649</a></p>
<dd> libguestfs cannot open disk images which are symlinks to files that contain &#8216;:&#8217; (colon) character</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/664558">https://bugzilla.redhat.com/664558</a></p>
<dd> <font SIZE="-1">RFE:</font> Allow to set log callback in Ruby bindings</dl>
<h2>RELEASE NOTES FOR LIBGUESTFS 1.20</h2>
<p> These release notes only cover the differences from the previous stable/dev branch split (1.18.0). For detailed changelogs, please see the git repository, or the ChangeLog file distributed in the tarball.</p>
<h3>New features</h3>
<p> <i>libvirt and sVirt (SELinux confinement)</i> </p>
<p> You can <i>optionally</i> use libvirt to launch and manage the backend appliance by:</p>
<dl>
<dt>&bull;</p>
<dd> setting <tt>&quot;LIBGUESTFS_ATTACH_METHOD=libvirt[:URI]&quot;</tt></p>
<dt>&bull;</p>
<dd> using <tt>&quot;./configure --with-default-attach-method=libvirt[:URI]&quot;</tt></p>
<dt>&bull;</p>
<dd> or calling the <font SIZE="-1">API</font> method <tt>&quot;guestfs_set_attach_method&quot;</tt></dl>
<p> SVirt (SELinux confinement) is used to secure the libguestfs appliance, if the libvirt backend is selected. </p>
<p> <i>virtio-scsi, larger number of drives, hotplugging</i> </p>
<p> Virtio-scsi is now used by default, if it is available. This greatly increases the number of drives that can be added to a single libguestfs handle (up to 255). </p>
<p> You can now hotplug drives (add and remove drives after launch). </p>
<p> Libguestfs can now handle &gt; 25 disks, in all APIs, tools and tests. </p>
<p> You can label drives when adding them, then refer to them by label (<i>/dev/disk/guestfs/LABEL</i>) instead of having to use device names (<i>/dev/sda</i>). </p>
<p> <i>new library features</i> </p>
<p> <font SIZE="-1">POSIX</font> Access Control Lists (ACLs) and Linux filesystem capabilities can now be read and written through the <font SIZE="-1">API.</font> </p>
<p> Windows Dynamic Disks are now supported. The metadata can only be read (volumes cannot be modified or created). However the data/filesystems in the volumes themselves can be mounted, read and written (Matthew Booth). </p>
<p> Hivex (Windows Registry editing) is now directly supported through the <font SIZE="-1">API,</font> making reading or editing the Windows Registry much more efficient. </p>
<p> Several libguestfs APIs were reimplemented so they no longer have any limits on output. The reimplemented APIs are: <tt>&quot;guestfs_cat&quot;</tt>, <tt>&quot;guestfs_find&quot;</tt>, <tt>&quot;guestfs_read_file&quot;</tt>, <tt>&quot;guestfs_read_lines&quot;</tt>, <tt>&quot;guestfs_write&quot;</tt>, <tt>&quot;guestfs_write_append&quot;</tt>, <tt>&quot;guestfs_lstatlist&quot;</tt>, <tt>&quot;guestfs_lxattrlist&quot;</tt>, <tt>&quot;guestfs_readlinklist&quot;</tt>, <tt>&quot;guestfs_ls&quot;</tt>. </p>
<p> <i>virt tools</i> </p>
<p> <tt>&quot;guestfish touch 'win:c:
ew_file'&quot;</tt> now works as expected. </p>
<p> <tt>&quot;guestfish&quot;</tt> has a new <i>&#8211;network</i> option, which enables the user network in libguestfs. </p>
<p> You can set <tt>&quot;GUESTFISH_PS1&quot;</tt> to use fancy prompts in <tt>&quot;guestfish&quot;</tt>. </p>
<p> <tt>&quot;rsync&quot;</tt>, <tt>&quot;ssh&quot;</tt>, <tt>&quot;less&quot;</tt> and <tt>&quot;lrzip&quot;</tt> commands are now available in virt-rescue. In addition, <tt>&quot;rsync&quot;</tt> can be used through the <font SIZE="-1">API</font> for doing incremental copies. </p>
<p> <tt>&quot;virt-sparsify&quot;</tt> uses qcow2 v3 for increased efficiency. </p>
<p> <tt>&quot;virt-sysprep&quot;</tt> enhancements:</p>
<dl>
<dt>&bull;</p>
<dd> generate new UUIDs for PVs and VGs</p>
<dt>&bull;</p>
<dd> remove the local machine <font SIZE="-1">ID</font> (Wanlong Gao)</p>
<dt>&bull;</p>
<dd> remove <font SIZE="-1">ABRT</font> data (Wanlong Gao)</p>
<dt>&bull;</p>
<dd> remove puppet keys and log files (Wanlong Gao)</p>
<dt>&bull;</p>
<dd> remove process accounting files (Wanlong Gao)</p>
<dt>&bull;</p>
<dd> new <i>&#8211;firstboot</i> parameter allowing firstboot scripts for customizing guests</p>
<dt>&bull;</p>
<dd> remove <font SIZE="-1">HOSTNAME</font> field from <tt>&quot;ifcfg-eth*&quot;</tt> files (Wanlong Gao)</p>
<dt>&bull;</p>
<dd> miscellaneous improvements for SuSE (Olaf Hering)</p>
<dt>&bull;</p>
<dd> remove man pages cache (Wanlong Gao)</p>
<dt>&bull;</p>
<dd> remove crash data generated by kexec-tools (Wanlong Gao)</dl>
<p> <tt>&quot;virt-make-fs&quot;</tt> can now create virtual floppy disks (VFDs). </p>
<p> <tt>&quot;guestmount&quot;</tt> has a <i>&#8211;pid-file</i> option, which can be used to avoid a race condition between unmounting the filesystem and using the underlying disk image. </p>
<p> <i>language bindings</i> </p>
<p> Full-featured Lua bindings have been added in this release (thanks to Jerome Vuarand for many suggestions). </p>
<p> In Ruby, optional arguments hash is optional. </p>
<p> In Python, optional arguments now don&#8217;t use special &#8220;sentinel&#8221; values, so any integer can be passed as an optional argument. </p>
<p> Erlang bindings now come with examples and tests. </p>
<p> Erlang bindings now handle 64 bit integer parameters correctly. </p>
<p> The automated &#8216;bindtests&#8217; now test for 64 bit cleanliness in parameter passing. Several bugs in the bindings were found and fixed as a result. </p>
<p> Better handling of blocking and non-blocking functions should make libguestfs calls more efficient. </p>
<p> <i>inspection</i> </p>
<p> Windows guests with unlimited-sized Registries are now supported. By adding the hivex <font SIZE="-1">API</font> to the libguestfs <font SIZE="-1">API,</font> it is much more efficient and easier to inspect and modify the Windows Registry in guests. </p>
<p> Better support for SuSE guests (Olaf Hering). </p>
<p> Return the architecture of installed applications (John Eckersberg). </p>
<p> Windows 8 is now supported. </p>
<p> Fedora 18 is now supported. </p>
<p> Inspection of ISOs/CDs/DVDs can now use the libosinfo database. </p>
<p> <i>ports</i> </p>
<p> Libguestfs without the appliance can be compiled on Mac <font SIZE="-1">OS X</font> (Masami <font SIZE="-1">HIRATA</font>). </p>
<p> <font SIZE="-1">RHEL 5</font> is now explicitly supported through the &#8216;oldlinux&#8217; branch in upstream git. </p>
<p> PowerPC 64 bit is now supported. Also libguestfs has been examined for endianness bugs and these have been fixed. </p>
<p> <i>daemon</i> </p>
<p> A man page for the daemon (<code><a href="/docs/linux/man/8-guestfsd/">guestfsd</a></code>(8)) is included.</p>
<h3>Security</h3>
<p> <i>guestfish history file</i> </p>
<p> The <i></i>$HOME<i>/.guestfish</i> history file is now created with 0600 permissions (instead of 0644 before) so it is no longer world readable. </p>
<p> <i></i><font SIZE="-1"><i>CVE-2012-2690</i></font><i></i> </p>
<p> Old versions of both <tt>&quot;virt-edit&quot;</tt> and the <tt>&quot;guestfish&quot;</tt> <tt>&quot;edit&quot;</tt> command created a new file containing the changes but did not set the permissions, etc of the new file to match the old one. The result of this was that if you edited a security sensitive file such as <i>/etc/shadow</i> then it would be left world-readable after the edit. </p>
<p> This issue was assigned <font SIZE="-1">CVE-2012-2690,</font> and is fixed in libguestfs ≥ 1.16. </p>
<p> For further information, see <a rel="nofollow" href="https://bugzilla.redhat.com/show_bug.cgi?id=788642">https://bugzilla.redhat.com/show_bug.cgi?id=788642</a></p>
<h3>New APIs</h3>
<pre><code>
acl - delete - def - file acl - get - file acl - set - file canonical - device - name cap - get - file cap - set - file create - flags device - index disk - has - backing - file disk - format disk - virtual - size filesystem - available fill - dir fstrim get - cachedir get - libvirt - requested - credentials get - libvirt - requested - credential - prompt get - libvirt - requested - credential - challenge get - libvirt - requested - credential - defresult get - tmpdir hivex - close hivex - commit hivex - node - add - child hivex - node - children hivex - node - delete - child hivex - node - get - child hivex - node - get - value hivex - node - name hivex - node - parent hivex - node - set - value hivex - node - values hivex - open hivex - root hivex - value - key hivex - value - type hivex - value - utf8 hivex - value - value inspect - list - applications2(John Eckersberg) list - ldm - volumes list - ldm - partitions ldmtool - create - all ldmtool - diskgroup - disks ldmtool - diskgroup - name ldmtool - diskgroup - volumes ldmtool - remove - all ldmtool - scan ldmtool - scan - devices ldmtool - volume - hint ldmtool - volume - partitions ldmtool - volume - type ls0 max - disks mke2fs(Wanlong Gao) mklost - and-found mkswap[added label and uuid optional arguments] mktemp(Wanlong Gao) nr - devices parse - environment parse - environment - list rm - f rsync rsync - in rsync - out set - cachedir set - libvirt - supported - credentials set - libvirt - requested - credential set - tmpdir shutdown[backported to 1.16 and 1.18] tar - in[added compress flag] tar - out[added compress, numericowner, excludes flags] umount[added force and lazy optional arguments] utsname xfs - admin(Wanlong Gao) xfs - growfs(Wanlong Gao) xfs - info(Wanlong Gao) xfs - repair(Wanlong Gao)
</code></pre>
<p> In the C <font SIZE="-1">API</font> only: </p>
<pre>
 guestfs_push_error_handler
 guestfs_pop_error_handler
</pre>
<h3>Internals</h3>
<p> qemu ≥ 1.1 is required (≥ 1.2 preferred). </p>
<p> febootstrap ≥ 3.20 is required. </p>
<p> libvirt is optional, but if you want to use the new libvirt backend for launching the appliance then libvirt ≥ 0.10.2 would be required. </p>
<p> Coverity has been run over the complete codebase, and many issues fixed (thanks Ondrej Vasik, Kamil Dudka). </p>
<p> Functions which previously had no optargs can now be converted to ones with optargs, making extending the <font SIZE="-1">API</font> much more flexible. Source and binary backwards compatibility is preserved for users of the <font SIZE="-1">API.</font> </p>
<p> The way that libguestfs APIs and structures are represented in the generator has changed to use an OCaml struct instead of a tuple. This makes generator descriptions more flexible and easier to understand. For details see commits 39d1a7db and eb185eef. </p>
<p> Separation of the library code into more files:</p>
<dl>
<dt>&bull;</p>
<dd> Launch backends are now located in separate files eg. <i>src/launch-appliance.c</i>, <tt>&quot;src/launch-libvirt.c&quot;</tt>.</p>
<dt>&bull;</p>
<dd> Generated action code is now split over several <i>src/action*.c</i> files, for faster compilation.</p>
<dt>&bull;</p>
<dd> The huge <i>src/guestfs.c</i> file is now split into smaller logical units.</dl>
<p> <font SIZE="-1">POD</font> (documentation) is now generated using a rewritten Perl program instead of pod2* + shell scripts. </p>
<p> Man pages now contain stable dates (Hilko Bengen). </p>
<p> Skipped tests now exit with code 77, so they appear as <tt>&quot;SKIP:&quot;</tt> in <tt>&quot;make check&quot;</tt> output. </p>
<p> The parallel mount-local test has been rewritten in C (RHBZ#838081). </p>
<p> Ruby 1.8.5 is now supported (though Ruby ≥ 1.9 is preferred). </p>
<p> Perl bindings can be disabled via <tt>&quot;./configure --disable-perl&quot;</tt> (Wulf C. Krueger). Note that Perl is still required in order to build libguestfs. </p>
<p> Java bindings are now enabled/disabled using <tt>&quot;./configure --with-java&quot;</tt> or <tt>&quot;./configure --without-java&quot;</tt> (Wulf C. Krueger). </p>
<p> New configure options <tt>&quot;./configure --enable-code-profiling&quot;</tt> and <tt>&quot;./configure --enable-code-coverage&quot;</tt>. </p>
<p> Multiple fixes to use of 64 bit integers in language bindings. </p>
<p> The appliance backend now uses sgabios instead of vgabios (Dan Berrange). </p>
<p> The <tt>&quot;./run&quot;</tt> script now sets enough environment variables that you can run OCaml, Python, Ruby, Java, <font SIZE="-1">GJS,</font> Erlang, Lua programs. </p>
<p> <tt>&quot;./run --test&quot;</tt> flag for running tests with minimal output. It also prints the time taken to run each test. </p>
<p> The <tt>&quot;./run&quot;</tt> script now builds up paths cumulatively, meaning that you can use <tt>&quot;./run&quot;</tt> twice, or use the libguestfs and libvirt <tt>&quot;./run&quot;</tt> scripts together. </p>
<p> You can extract a list of external commands required by the daemon, making building the appliance on certain distros easier (Olaf Hering). </p>
<p> The <tt>&quot;virt-rescue&quot;</tt> command is now tested during <tt>&quot;make check&quot;</tt>. </p>
<p> The generator now removes unused generated files. This helps when going back and forth with git rebase, git bisect, etc. </p>
<p> Tests now run in a separate toplevel <tt>&quot;tmp/&quot;</tt> directory in the source. This allows the directory to be labelled for SELinux (sVirt), and also makes it easier to clean up. </p>
<p> <tt>&quot;make syntax-check&quot;</tt> now works to a greater extent, and many problems in the main code that were found by syntax-check have been fixed (thanks Jim Meyering). </p>
<p> Emacs mode (-*- foo -*-) has been added to generated files. </p>
<p> Progress bar output is now sent to <i>/dev/tty</i> so it doesn&#8217;t end up in the regular output of the program. virt-resize and virt-sparsify now suppress progress bars if stdout is not a tty. </p>
<p> There is now a <tt>&quot;./configure --without-libvirt&quot;</tt> option. This is useful for testing that the code still compiles without libvirt. </p>
<p> There is now an internal mini-library for running commands. This allows us to redirect errors from external commands into events. </p>
<p> Code for handling temporary directories and the appliance cache was completely overhauled. </p>
<p> Code for temporarily ignoring/disabling errors now looks like this: </p>
<p>guestfs_push_error_handler(g, NULL, NULL);<br />
guestfs_mkdir(g, &#8220;/foo&#8221;); /* We don&#8217;t care if this fails. */<br />
guestfs_pop_error_handler(g);</p>
<p> The <tt>&quot;tests/extra&quot;</tt> directory has gone. The &#8220;extra tests&#8221; are now split into separately runnable targets, such as <tt>&quot;make check-valgrind&quot;</tt>. Use <tt>&quot;make help&quot;</tt> to get a summary of the targets. </p>
<p> The <tt>&quot;lpj&quot;</tt> option is passed to the appliance kernel when using <font SIZE="-1">TCG.</font> This should improve clock stability (thanks Marcelo Tosatti, Olaf Hering).</p>
<h3>Bugs fixed</h3>
<dl>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/882417">https://bugzilla.redhat.com/882417</a></p>
<dd> libguestfs tools fail with odd error messages if <font SIZE="-1">TMPDIR</font> is not an absolute path</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/882299">https://bugzilla.redhat.com/882299</a></p>
<dd> Windows 8 guest disks can&#8217;t be mounted: &#8220;The <font SIZE="-1">NTFS</font> partition is in an unsafe state. Please resume and shutdown Windows fully (no hibernation or fast restarting), or mount the volume read-only with the &#8216;ro&#8217; mount option.&#8221;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/881953">https://bugzilla.redhat.com/881953</a></p>
<dd> libguestfs: migration to /etc/hostname, /etc/vconsole.conf, /etc/locale.conf</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/880801">https://bugzilla.redhat.com/880801</a></p>
<dd> virt-df with two -a options displays incorrect disk image name</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/879416">https://bugzilla.redhat.com/879416</a></p>
<dd> libguestfs-test-tool pauses when you use &#8211;help option</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/876579">https://bugzilla.redhat.com/876579</a></p>
<dd> mke2fs <font SIZE="-1">API</font> does not apply block device naming translation to journaldevice optarg</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/860235">https://bugzilla.redhat.com/860235</a></p>
<dd> SELinux policy ought to allow qemu to write to unconfined_u:object_r:user_tmp_t:s0</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/859949">https://bugzilla.redhat.com/859949</a></p>
<dd> <font SIZE="-1">RFE:</font> inspect-list-applications does not return the architecture of <font SIZE="-1">RPM</font> packages</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/859885">https://bugzilla.redhat.com/859885</a></p>
<dd> inspect-list-applications does not list all installed <font SIZE="-1">RPM</font> packages with same name and different versions</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/859876">https://bugzilla.redhat.com/859876</a></p>
<dd> guestfish printed paths are not canonicalized</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/859875">https://bugzilla.redhat.com/859875</a></p>
<dd> Progress bar output should go to tty(?) stderr(?)</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/858696">https://bugzilla.redhat.com/858696</a></p>
<dd> virt-sysprep reports Guestfs.Error(&#8220;read_lines: fopen: /etc/sysconfig/network: No such file or directory&#8221;) on some Fedora guests</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/858128">https://bugzilla.redhat.com/858128</a></p>
<dd> libguestfs fail to list devices added by add-drive-ro-with-if twice</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/858126">https://bugzilla.redhat.com/858126</a></p>
<dd> virt-inspector fail to work with some windows guests</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/853762">https://bugzilla.redhat.com/853762</a></p>
<dd> virt-sparsify should use a more robust method to detect the input format</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/853393">https://bugzilla.redhat.com/853393</a></p>
<dd> libvirt doesn&#8217;t label console, serial sockets</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/853159">https://bugzilla.redhat.com/853159</a></p>
<dd> virt-rescue in Fedora 18 is completely broken</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/852394">https://bugzilla.redhat.com/852394</a></p>
<dd> libguestfs inspection limits registries to 100 MiB</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/852194">https://bugzilla.redhat.com/852194</a></p>
<dd> virt-sparsify &#8211;compress fails if output is raw format</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/847881">https://bugzilla.redhat.com/847881</a></p>
<dd> <font SIZE="-1">RFE:</font> allow extra arguments (like &#8211;exclude) to tar-out</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/847880">https://bugzilla.redhat.com/847880</a></p>
<dd> tar-out should allow (or force) &#8211;numeric-owner</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/845522">https://bugzilla.redhat.com/845522</a></p>
<dd> guestfish &#8220;copy-out / localdir&#8221; command fails with &#8220;No such file or directory&#8221;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/845488">https://bugzilla.redhat.com/845488</a></p>
<dd> Long filenames on <font SIZE="-1">NTFS</font> cause tar-out, copy-out etc to fail with error &#8220;Cannot open: File name too long&#8221;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/842307">https://bugzilla.redhat.com/842307</a></p>
<dd> <font SIZE="-1">RFE:</font> Need help designing and implementing selinux policy for libguestfs/sVirt</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/840572">https://bugzilla.redhat.com/840572</a></p>
<dd> virt-make-fs / tar-in should support vfat properly</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/840115">https://bugzilla.redhat.com/840115</a></p>
<dd> guestfish touch problem &#8211; case_sensitive_path <font SIZE="-1">API</font> expects the file to exist</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/836710">https://bugzilla.redhat.com/836710</a></p>
<dd> Data loss when writing to qcow2-format disk files</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/834712">https://bugzilla.redhat.com/834712</a></p>
<dd> lvresize, lvresize-free fail unnecessarily if you don&#8217;t change the size of the <font SIZE="-1">LV:</font> &#8220;New size (nn extents) matches existing size (nn extents)&#8221;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/824716">https://bugzilla.redhat.com/824716</a></p>
<dd> compress-device-out didn&#8217;t support bzip2</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/824043">https://bugzilla.redhat.com/824043</a></p>
<dd> guestfish unrecognized mount option gives confusing error message</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/823887">https://bugzilla.redhat.com/823887</a></p>
<dd> Filenames containing Chinese characters can&#8217;t be created on vfat filesystems</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/823885">https://bugzilla.redhat.com/823885</a></p>
<dd> virt-make-fs cannot create vfat filesystem containing filesystems with Chinese characters</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/823883">https://bugzilla.redhat.com/823883</a></p>
<dd> virt-make-fs -t fat fails with an obscure error message</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/823821">https://bugzilla.redhat.com/823821</a></p>
<dd> Inspection fails when /etc/HOSTNAME is empty</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/801117">https://bugzilla.redhat.com/801117</a></p>
<dd> libguestfs cannot get icon for Windows 8</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/798979">https://bugzilla.redhat.com/798979</a></p>
<dd> Ubuntu install CDs from oneiric onwards are not recognized: &#8220;multi-boot operating systems are not supported&#8221;</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/782167">https://bugzilla.redhat.com/782167</a></p>
<dd> libguestfs doesn&#8217;t recognize Windows Dynamic disks in some configurations, eg. spanned</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/713678">https://bugzilla.redhat.com/713678</a></p>
<dd> Not all febootstrap messages are redirected to log callbacks</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/627675">https://bugzilla.redhat.com/627675</a></p>
<dd> libguestfs inspector code cannot handle /dev/disk/by-id/* paths</p>
<dt><a rel="nofollow" href="https://bugzilla.redhat.com/602997">https://bugzilla.redhat.com/602997</a></p>
<dd> part-get-bootable gives wrong result with an unordered part layout</dl>
<h2>RELEASE NOTES FOR LIBGUESTFS 1.18</h2>
<p> These release notes only cover the differences from the previous stable/dev branch split (1.16.0). For detailed changelogs, please see the git repository, or the ChangeLog file distributed in the tarball.</p>
<h3>New features</h3>
<p> <i>virt tools</i> </p>
<p>&#8211; virt &#8211; sysprep has been rewritten and expanded(thanks Wanlong Gao)<br />
    http: // libguestfs.org/virt-sysprep.1.html<br />
        -virt &#8211; sparsify&#8211; zero is a new option that zeroes the named<br />
            partition<br />
        or filesystem<br />
                   &#8211; virt &#8211; sparsify can now safely sparsify Linux swap partitions<br />
                   &#8211; virt &#8211; sparsify fixed so it cleans up after<br />
               ^ C<br />
    http: // libguestfs.org/virt-sparsify.1.html<br />
        -a new tool &#8216;libguestfs-make-fixed-appliance&#8217; is provided to build<br />
        fixed appliances that can be copied to other machines that don&#8217;t have febootstrap support<br />
    http: // libguestfs.org/libguestfs-make-fixed-appliance.1.html<br />
        -virt &#8211; filesystems now displays the parents(containers) of MD<br />
     devices and volume groups<br />
   &#8211; virt-alignment-scan, run with no args, displays alignment information<br />
     for all libvirt domains<br />
   &#8211; virt-df and virt-alignment-scan will display information from all<br />
     guests even when a disk is inaccessible<br />
   &#8211; virt-rescue new &#8211;scratch option to make scratch disks</p>
<blockquote class="wp-embedded-content" data-secret="PAz0vsR6xK"><p><a href="https://rwmj.wordpress.com/2012/04/26/virt-rescue-scratch/" rel="nofollow noopener" target="_blank">virt-rescue &#8211;scratch</a></p></blockquote>
<p><iframe loading="lazy" class="wp-embedded-content" sandbox="allow-scripts" security="restricted" style="position: absolute; visibility: hidden;" title="&#8220;virt-rescue &#8211;scratch&#8221; &#8212; Richard WM Jones" src="https://rwmj.wordpress.com/2012/04/26/virt-rescue-scratch/embed/#?secret=pJKIpTylRu#?secret=PAz0vsR6xK" data-secret="PAz0vsR6xK" width="600" height="338" frameborder="0" marginwidth="0" marginheight="0" scrolling="no"></iframe><br />
   &#8211; virt-make-fs can now be used to create btrfs<br />
   &#8211; virt-edit preserves permissions, UID, GID and SELinux context<br />
     when editing files<br />
   &#8211; guestfish passes the close event over stdout and remote correctly<br />
   &#8211; guestfish new &#8216;&#8211;pipe-error&#8217; option lets you detect errors in pipe<br />
     commands<br />
   &#8211; guestfish globs now expand device names<br />
   &#8211; comma and colon characters in filenames now handled correctly by<br />
     all virt tools</p>
<p> <i>inspection</i> </p>
<pre>
   - added support for Fedora 17+
   - added support for FreeDOS
   - added support for Buildroot and Cirros
   - inspection is now compatible with Windows guests that have been
     sysprepped (thanks Grant Williamson).
</pre>
<p> <i></i><font SIZE="-1"><i>API</i></font><i></i> </p>
<pre>
   - broad support for btrfs added, including adding multiple devices,
     fsck, snapshots (thanks Wanlong Gao)
   - the new 'mount-local' API brings FUSE support directly into the
     core libguestfs API
     <a rel="nofollow" href="https://rwmj.wordpress.com/2012/05/14/tip-using-mount-local-api-from-c/#content">https://rwmj.wordpress.com/2012/05/14/tip-using-mount-local-api-from-c/#content</a>
   - new man page: <a href="//www.systutorials.com/docs/linux/man/1-guestfs-performance/">guestfs-performance</a>(1), which contains performance
     tuning tips
     <a rel="nofollow" href="http://libguestfs.org/guestfs-performance.1.html">http://libguestfs.org/guestfs-performance.1.html</a>
   - new man page: <a href="//www.systutorials.com/docs/linux/man/1-guestfs-faq/">guestfs-faq</a>(1), Frequently Asked Questions
     <a rel="nofollow" href="http://libguestfs.org/guestfs-faq.1.html">http://libguestfs.org/guestfs-faq.1.html</a>
   - ENOTSUP (from guestfs_last_errno) is now returned for APIs that
     are not supported
</pre>
<p> <i>examples</i> </p>
<pre>
   - 'copy_over' example showing how to copy between two handles
   - 'display_icon' program displays the icon associated with a guest
   - 'mount_local.c' example shows how to use the mount-local API
</pre>
<h3>Security</h3>
<pre>
  (no security problems were found or fixed in this release)
</pre>
<h3>New APIs</h3>
<pre>
  btrfs-device-add: Add devices to a btrfs filesystem.
  btrfs-device-delete: Remove devices from a btrfs filesystem.
  btrfs-filesystem-sync: Sync a btrfs filesystem.
  btrfs-filesystem-balance: Balance a btrfs filesystem.
  btrfs-fsck: Check btrfs filesystem.
  btrfs-set-seeding: Enable or disable seeding.
  btrfs-subvolume-create: Create a btrfs snapshot.
  btrfs-subvolume-delete: Delete a btrfs snapshot.
  btrfs-subvolume-list: List btrfs snapshots and subvolumes.
  btrfs-subvolume-set-default: Set default btrfs subvolume.
  btrfs-subvolume-snapshot: Create a writable btrfs snapshot.
  get-e2attrs: List ext2 file attributes of a file.
  get-e2generation: Get ext2 file generation of a file.
  isoinfo, isoinfo-device: Get information from the header of ISO files.
  llz: List files with SELinux information.
  lvcreate-free: Create an LVM logical volume in % remaining free space.
  md-stat: Return underlying devices from an MD device.
  mkfs-brtfs: Make btrfs filesystem, with all tunables.
  mount-local, mount-local-run, umount-local: FUSE support in the API.
  ntfsclone-in, ntfsclone-out: Save, restore NTFS from backup.
  ntfsfix: Fix common errors and force Windows to check NTFS.
  set-e2attrs: Set or clear ext2 file attributes of a file.
  set-e2generation: Set ext2 file generation of a file.
  set-label: Unified interface for setting filesystem label.
  vgmeta: Get volume group metadata.
  wipefs: Wipe filesystem signatures from a device.
  zero-free-space: Zero free space in a filesystem.
</pre>
<h3>Internals</h3>
<p> &#8211; The debian/ subdirectory has been removed.  We recommend you use<br />
   the official Debian packages made by Hilko Bengen.<br />
   http://people.debian.org/~bengen/libguestfs/<br />
   http://packages.debian.org/search?keywords=libguestfs<br />
 &#8211; O_CLOEXEC / SOCK_CLOEXEC is now used for almost all file<br />
   descriptors that the library opens.<br />
 &#8211; posix_fadvise is called when sequentially reading or writing large<br />
   files.<br />
 &#8211; close all file descriptors and remove all signal handlers in the<br />
   recovery process<br />
 &#8211; multiple gcc warnings and Coverity bugs have been fixed;<br />
 many<br />
         strict &#8211;<br />
     overflow bugs have also been fixed &#8211; use./ configure&#8211; enable &#8211; valgrind &#8211; daemon to use valgrind on the daemon;  many errors have been fixed<br />
 &#8211; use ./configure &#8211;with-qemu-options to pass extra options to qemu<br />
 &#8211; the daemon now has a growable strings buffer type (DECLARE_STRINGSBUF)<br />
 &#8211; the &lt;guestfs.h&gt; header file works with C++ and we have a regression<br />
   test for this<br />
 &#8211; multiple APIs which should only be called in the CONFIG state now<br />
   give an error if they are not<br />
 &#8211; .gitignore fixed to use absolute paths<br />
 &#8211; gobject bindings have been expanded, including mapping libguestfs<br />
   events to gobject signals (thanks Matt Booth)<br />
 &#8211; gobject documentation is generated properly (thanks Matt Booth)<br />
 &#8211; gobject header files now live in a subdirectory<br />
 &#8211; CompareWithString test in the generator now works<br />
 &#8211; FUInt32, FUInt64 struct field types now use the correct XDR type<br />
 &#8211; OCaml tests are now run on bytecode and native code.<br />
 &#8211; java -Xlint:all is used, and all warnings have been fixed<br />
 &#8211; bmptopng, wrestool (etc) missing or failure no longer prints<br />
   warning messages<br />
 &#8211; ruby: Use RbConfig instead of Config.<br />
 &#8211; PYTHONPATH is set by the ./run script.<br />
 &#8211; appliance building is now thread-safe.<br />
 &#8211; appliance now uses &#8216;ip&#8217; instead of &#8216;ifconfig&#8217; and &#8216;netstat&#8217;<br />
   commands<br />
 &#8211; several fixes to make parallel builds work properly<br />
 &#8211; guestfish &#8211;listen now cleans up properly<br />
 &#8211; the BUSY state has been removed<br />
 &#8211; gettextize has been removed, replaced by a simple Makefile.am<br />
 &#8211; gettext support now covers virt-resize, virt-sparsify and virt-sysprep<br />
 &#8211; better support for the arm architecture</p>
<h3>Bugs fixed</h3>
<p> &#8211; 822490 virt-ls error: &#8220;libguestfs: error: checksum: path: parameter cannot be NULL&#8221;<br />
 &#8211; 816839 data overflow error when debug progress -1<br />
 &#8211; 816098 virt-make-fs fails to make a btrfs filesystem because it doesn&#8217;t allocate enough space<br />
 &#8211; 811872 inspection fails on ubuntu 10.04 guest with encrypted swap<br />
 &#8211; 811650 guestfs_last_error not set when qemu fails early during launch<br />
 &#8211; 811649 libguestfs cannot open disk images which are symlinks to files that contain &#8216;:&#8217; (colon) character<br />
 &#8211; 811117 [RFE][virt-sysprep] net-hwaddr not removed from &#8220;ifcfg-*&#8221; files on rhel<br />
 &#8211; 811112 [RFE][virt-sysprep] hostname can not be changed on rhel system<br />
 &#8211; 809361 inspection doesn&#8217;t recognize Fedora 18 (grub2 + GPT)<br />
 &#8211; 807905 mkfs blocksize option breaks when creating btrfs<br />
 &#8211; 805070 virt-filesystems should show &#8216;parents&#8217; of LV and RAID devices<br />
 &#8211; 804464 libguestfs cannot be built when LINGUAS is different then ja or uk<br />
 &#8211; 803664 libguestfs inspection fails on Windows XP: libguestfs: error: hivex: could not locate HKLM\SYSTEM\MountedDevices<br />
 &#8211; 803533 guestfish: write error<br />
 &#8211; 802389 event handlers for &#8216;close&#8217; event doesn&#8217;t work in remote mode<br />
 &#8211; 802109 libguestfs uses putc on stderr, results in many individual 1 byte writes of debug messages<br />
 &#8211; 801640 [RFE] the error reported by resize2fs-M need to be more clear<br />
 &#8211; 801298 Possible null dereference and resource leaks<br />
 &#8211; 801273 Document for set-pgroup need to be updated<br />
 &#8211; 798196 virt-resize confuses format and output_format variables; using &#8211;output-format sets the input format<br />
 &#8211; 797986 virt-resize on Windows XP in sysprep state causes &#8220;UNMOUNTABLE_BOOT_VOLUME&#8221; BSOD<br />
 &#8211; 796520 [RFE] Prevent user from running some appliance configure commands after appliance boot up<br />
 &#8211; 790721 multiprovider build error: RuntimeError: link: /tmp/.guestfs-0/kernel /tmp/.guestfs-0/kernel.10139: File exists<br />
 &#8211; 789960 guestfsd crash when try to mount non-exist disk<br />
 &#8211; 789504 virt-df (other tools?) should not give up if a guest disk is missing<br />
 &#8211; 788641 virt-edit doesn&#8217;t preserve file permissions<br />
 &#8211; 786215 libguestfs inspection does not recognize FreeDOS operating system<br />
 &#8211; 786188 libguestfs inspection does not recognize FreeDOS install CD<br />
 &#8211; 785668 aug-defnode: daemon crash<br />
 &#8211; 784647 Libguestfs uses deprecated net-tools<br />
 &#8211; 769304 virt-resize on RHEL 6 kernel fails to re-read the partition table<br />
 &#8211; 755729 Error message for resize2fs-M needs tweaking<br />
 &#8211; 701814 virt-win-reg fails on a libvirt guest that has no defined disk format: &#8220;format parameter is empty or contains disallowed characters&#8221;<br />
 &#8211; 679737 libguestfs: improve error message when zerofree is not available in the appliance<br />
 &#8211; 635971 glob mkfs ext2 /dev/vd[b-t]1 does not expand</p>
<h2>RELEASE NOTES FOR LIBGUESTFS 1.16</h2>
<p> These release notes only cover the differences from the previous stable/dev branch split (1.14.0). For detailed changelogs, please see the git repository, or the ChangeLog file distributed in the tarball.</p>
<h3>New features</h3>
<p> <i>libguestfs</i> </p>
<p>   &#8211; allow XFS filesystems to be created over an existing filesystem<br />
     (Wanlong Gao)<br />
   &#8211; the (unspecified) default alignment for part-disk has been<br />
     changed to 64K for better support of high-end network-attached<br />
     storage<br />
   &#8211; new guestfs-testing(1) man page<br />
   &#8211; list-filesystems returns MD devices containing filesystems<br />
     (Matthew Booth)<br />
   &#8211; support for GCC &gt;= 4.7 (Jim Meyering)<br />
   &#8211; check user does not add the same drive twice (Wanlong Gao).</p>
<p> <i>language bindings</i> </p>
<p>   &#8211; Experimental GObject bindings, with support for GObject<br />
     Introspection.  You can now use libguestfs from Javascript.<br />
     Please note these are not stable and final in this release.<br />
     (Matthew Booth).<br />
   &#8211; support for Ruby &gt;= 1.9<br />
   &#8211; Ruby bindings can be disabled individually (Hilko Bengen)<br />
   &#8211; support for Python 2.6, 3.x (Richard Jones, Hilko Bengen)<br />
   &#8211; support for PHP &gt;= 5.4<br />
   &#8211; new %guestfs_introspection hash is available in Perl bindings so<br />
     you can query which optional arguments are available</p>
<p> <i>inspection</i> </p>
<pre>
   - guests with MD devices can be inspected (Matthew Booth)
   - support for GNU/Hurd guests
</pre>
<p> <i>guestfish</i> </p>
<pre>
   - libguestfs events (such as progress bar events and log messages) can
     be trapped and processed by user-defined shell scripts.
   - MD devices are tab-completed (Matthew Booth)
</pre>
<p> <i>virt tools</i> </p>
<p>   &#8211; New tool virt-format for erasing and making blank disks<br />
   &#8211; virt-sparsify new &#8211;compress and -o options to allow for compressed<br />
     and different format output<br />
   &#8211; virt-sparsify can now detect and sparsify .vdi files<br />
   &#8211; virt-sysprep no longer requires xmlstarlet; a new virt-inspector &#8211;xpath<br />
     option has been added to replace this functionality<br />
   &#8211; virt-rescue has a new &#8211;suggest option which suggests mount commands<br />
     for the guest<br />
   &#8211; virt-resize no longer requires OCaml pcre library</p>
<p> <i>libguestfs live</i> </p>
<pre>
   - daemon will no longer try to edit your live /etc/lvm configuration
   - fix a potential security problem with predictable /tmp names (Steve Kemp)
</pre>
<h3>Security</h3>
<pre>
  CVE-2011-4127, RHBZ#757071
  Mitigate possible privilege escalation via SG_IO ioctl
  For more information, see: <a rel="nofollow" href="https://github.com/libguestfs/libguestfs/commit/9a5f784d511a8f00a8386f316eab41fe660430db">https://github.com/libguestfs/libguestfs/commit/9a5f784d511a8f00a8386f316eab41fe660430db</a>
</pre>
<h3>New APIs</h3>
<pre>
  blkid: print all attributes of a device known to blkid (Wanlong Gao)
  e2fsck: access to more features of e2fsck (Wanlong Gao)
  list-md-devices: list of Linux MD devices (Matthew Booth)
  md-create: create an MD device
  md-detail: returns metadata for an MD device (Matthew Booth)
  md-stop: stop an MD device (Wanlong Gao)
  tune2fs: allow ext2/3/4 filesystems to be tuned
</pre>
<h3>Internals</h3>
<p>  Git hosting has moved to http://github.com/libguestfs<br />
  The various test directories have been rearranged logically, and now<br />
  all appear under &#8216;tests/&#8217;.<br />
  There is a &#8216;make extra-tests&#8217; rule which runs ordinary tests and<br />
  additional tests, using valgrind to check for memory problems.<br />
  Multiple memory leaks and other problems found by valgrind and fixed.<br />
  Support for optional arguments in the generator has been rewritten<br />
  to provide more features and safety (Matthew Booth).<br />
  With gcc -fvisibility=hidden is used for internal symbols, avoiding<br />
  call indirection via the PLT.<br />
  RHashtable functions can be tested in the generator.<br />
  ADD_ARG macro in daemon allows arg lists to be constructed without<br />
  risk of stack smashing.<br />
  Fix generation of OCaml functions that have more than 10 arguments.<br />
  psmisc has been added to the appliance, allowing use of &#8216;fuser&#8217;,<br />
  &#8216;killall&#8217; and &#8216;pstree&#8217; for debugging.<br />
  bindtests now cover RBufferOut and optional arguments (Matthew Booth).</p>
<h3>Bugs fixed</h3>
<pre>
 - 769680 temporary directories created during appliance builds are not cleaned up on error
 - 761460 guestfs_utimens hangs on named pipes
 - 761451 guestfs_utimens cannot set times on a directory
 - 760775 &quot;guestfish: multi-boot operating systems are not supported by the -i option&quot; should be more explanatory
 - 760669 guestfish copy-in and &lt;! (inline execution) don't mix well: pclose: No child processes
 - 760000 libguestfs fails to compile with Ruby &gt;= 1.9
 - 755729 Error message for resize2fs-M needs tweaking
 - 750889 Python code incompatible with Python v3.
 - 596761 Ctrl-\ causes guestfish to abort
</pre>
<h2>RELEASE NOTES FOR LIBGUESTFS 1.14</h2>
<p> These release notes only cover the differences from the previous stable/dev branch split (1.12.0). For detailed changelogs, please see the git repository, or the ChangeLog file distributed in the tarball.</p>
<h3>New features</h3>
<pre>
  Erlang bindings.
  virt-alignment-scan is a new tool to check the alignment of
  partitions within virtual machines or disk images.
  virt-sparsify is a new tool to make virtual machine disk images
  sparse.
  virt-sysprep is a new tool to make cloning guests from a template
  simpler.
</pre>
<p> <i>guestfish</i> </p>
<pre>
   - New commands setenv, unsetenv, to set environment variables.
   - The input file and line number is printed in error messages.
   - guestfish progress bars are now a &quot;mini-library&quot; used by other
     tools too.
</pre>
<p> <i>guestmount</i> </p>
<pre>
   - the --live option (for access to live VMs) now works.
</pre>
<p> <i>virt-cat</i> </p>
<pre>
   - virt-cat can now handle Windows paths and drive letters (RHBZ#693359).
</pre>
<p> <i>virt-filesystems</i> </p>
<pre>
   - the MBR partition type byte is displayed in --long output.
</pre>
<p> <i>virt-make-fs</i> </p>
<pre>
   - virt-make-fs now sets the MBR partition type byte correctly,
     improving compatibility with Windows (RHBZ#746295).
</pre>
<p> <i>virt-resize</i> </p>
<pre>
   - virt-resize can now work with guests using extended and logical
     partitions, in particular Ubuntu guests.
   - virt-resize can now align the first partition of Windows guests,
     improving performance.  The new virt-resize --align-first option
     controls this behaviour.
   - The virt-resize --machine-readable flag makes it possible to use
     virt-resize from other programs.
   - Partitions are now aligned to 128 sectors (usually 64K) by
     default.  This improves efficiency on high-end storage.  The new
     virt-resize --alignment option allows the alignment to be
     adjusted.
</pre>
<p> <i>virt-win-reg</i> </p>
<pre>
   - The syntax for deleting registry keys and values is documented
     in the man page (RHBZ#737944).
</pre>
<p> <i>library</i> </p>
<pre>
   - non-printing characters are escaped correctly in debug output.
   - GUESTFS_EVENT_ENTER is a new event type generated whenever a
     libguestfs function is called.
   - the library contains systemtap/DTrace probes.
   - the library can now be compiled without hivex (RHBZ#723474).
</pre>
<p> <i>inspection</i> </p>
<pre>
   - Improve detection of Windows disks.
   - Adds support for:
         ttylinux - a minimal Linux
         Mageia (thanks Michael Scherer)
         OpenSUSE and zypper (thanks Michael Scherer, Vincent Untz)
         Ubuntu logos (thanks Michael Scherer)
         NetBSD and pkgsrc (thanks Michael Scherer)
   - Handle some guest types that use /dev/root in /etc/fstab.
   - Fix handling of guests with &gt; 26 disks (thanks Matthew Booth)
   - Add support for guests with HP Smart Array disks (thanks Matthew Booth)
</pre>
<p> <i>febootstrap</i> </p>
<pre>
   - FEBOOTSTRAP_KERNEL, FEBOOTSTRAP_MODULES environment variables can
     be set in order to choose which kernel to use for the appliance.
</pre>
<p> <i>misc</i> </p>
<pre>
   - ArchLinux support now working with Linux 3.0 (thanks Erik Nolte)
   - libvirt disks marked &lt;readonly/&gt; are now added readonly when
     using the virt-tools '-d' option.
</pre>
<h3>Security</h3>
<pre>
  (no security problems were found or fixed in this release)
</pre>
<h3>New APIs</h3>
<pre>
  compress-out, compress-device-out, copy-device-to-device,
  copy-device-to-file, copy-file-to-device, copy-file-to-file,
  get-smp, part-to-partnum, set-smp.
  The mount API no longer implicitly adds -o sync,noatime options.
  add-domain has a new 'readonlydisk' optional parameter to control
  how &lt;readonly/&gt; disks are handled.
</pre>
<h3>Internals</h3>
<pre>
 - Coverity was run on the source and more bugs were identified and
   fixed.
 - PCRE library is now required to build libguestfs.
 - APIC is now the default for the appliance.  You can also enable
   SMP support in the appliance.
 - OCaml bindings now correctly acquire GC lock during callbacks.
 - Out of tree builds should now work correctly (thanks Hilko Bengen).
 - ./configure --with-extra=&quot;...&quot; can be used by packagers to set
   the extra version string.
 - zero, zero-device APIs: if the blocks already contain zeroes,
   don't write zeroes, so that we don't unnecessarily make the
   underlying storage non-sparse.
 - is-zero, is-zero-device APIs: optimize these so zero detection is
   faster.
</pre>
<h3>Bugs fixed</h3>
<pre>
 - 748266 libguestfs should detect versions of qemu which require -machine pc option
 - 747290 libguestfs ignores &lt;readonly/&gt; in libvirt XML
 - 747287 Misleading error message when permission denied opening a disk image
 - 746295 virt-make-fs doesn't set partition ID
 - 744795 guestmount --live is not usable
 - 737944 virt-win-reg hyphen (delete key) syntax may be wrong, and is not documented
 - 733297 ruby event handlers fail with &quot;exception in callback: wrong argument type Proc (expected Data)&quot;
 - 731744 libguestfs should escape special/non-printing characters in debug output
 - 729887 appliance crashes running aug_init with flags=4
 - 729075 libguestfs confuses Hp_recovery partition with Windows root filesystem
 - 727178 error: luks_open: cryptsetup: error while loading shared libraries: libfipscheck.so.1: cannot open shared object file: No such file or directory
 - 726739 libguestfs: error: aug_get: no matching node, trying to find hostname
 - 723474 If hivex and/or pcre not installed, libguestfs fails to compile
 - 693359 virt-cat and virt-edit don't handle case sensitive NTFS paths properly
 - 678231 virt-inspector reports unknown filesystem UUID
 - 671082 libguestfs does not work with kernel-rt
 - 666578 libguestfs: unknown filesystem label SWAP-sda2
 - 642821 virt-resize falls over on a disk image with a logical swap partition
</pre>
<h2>RELEASE NOTES FOR LIBGUESTFS 1.12</h2>
<p> These release notes only cover the differences from the previous stable/dev branch split (1.10.0). For detailed changelogs, please see the git repository, or the ChangeLog file distributed in the tarball.</p>
<h3>New features</h3>
<p> <i>guestfish</i> </p>
<pre>
   - guestfish strings can use escapes,
     eg. &gt;&lt;fs&gt; write /foo &quot;line 1
line 2
&quot;
   - guestfish write-append command can be used to append to files.
   - Long-running file uploads and downloads can be cancelled through the
     API or by hitting ^C in guestfish.
   - New guestfish &quot;display&quot; command for displaying graphical files
     inside guests.
   - In guestfish, tab completion now works on /dev/mapper devices.
</pre>
<p> <i>virt-inspector</i> </p>
<pre>
   - Inspection API can get an icon or logo for certain guests.
   - virt-inspector includes the logo and hostname for certain guests.
   - virt-inspector can now get the version and release numbers for RPM
     packages.
   - CentOS and Scientific Linux are now treated as separate distros by
     the inspection API.
</pre>
<p> <i>virt-resize</i> </p>
<pre>
   - virt-resize can now handle btrfs.
   - New virt-resize --ntfsresize-force option allows Windows VMs to be
     resized multiple times.
</pre>
<p> <i>other virt tools</i> </p>
<pre>
   - guestfish, guestmount, virt-cat, virt-df, virt-edit, virt-filesystems,
     virt-inspector, virt-ls and virt-rescue now allow you to use
     &quot;-d UUID&quot; option to specify a guest by UUID.  This makes them more
     robust to use from other programs.
   - virt-ls -lR option allows complex file iteration and guest analysis.
   - virt-win-reg supports HKEY_USERS\&lt;SID&gt; and HKEY_USERS\&lt;username&gt;.
   - virt-win-reg new option --unsafe-printable-strings allows printable
     strings to be displayed in the output (unsafely: read the documentation
     before using).
   - virt-edit has been rewritten in C.
</pre>
<p> <i></i><font SIZE="-1"><i>API</i></font><i> and language bindings</i> </p>
<pre>
   - Java is now completely supported.
     See <a rel="nofollow" href="http://libguestfs.org/guestfs-java.3.html">http://libguestfs.org/guestfs-java.3.html</a>
   - JRuby is supported via the Java bindings.
   - guestfs_close now appears in trace messages.
   - Python binding adds explicit g.close() method.
   - Python programs can now use the new event API.
   - Python GIL is released during libguestfs calls, allowing multithreaded
     Python programs to work properly.
   - 9pfs (Plan 9 filesystems exported from the host) are now supported.
   - Add -DGUESTFS_WARN_DEPRECATED=1 to warn about use of deprecated API
     functions in C programs.
   - New manual page <a href="//www.systutorials.com/docs/linux/man/1-guestfs-recipes/">guestfs-recipes</a>(1) with recipes.
   - mkfs-opts can now set inode size and sector size on created filesystems
     (thanks Nikita Menkovich).
   - guestfs_last_errno is now accessible from OCaml (as g#last_errno ()).
</pre>
<h3>Security</h3>
<pre>
 - optargs_bitmask is checked even for calls that have no optional
   arguments.  This closes a possible exploit in the daemon from
   untrusted callers.
</pre>
<h3>New APIs</h3>
<pre>
  btrfs-filesystem-resize, get-pgroup, inspect-get-icon, is-zero,
  is-zero-device, list-9p, list-dm-devices, mount-9p, ntfsresize-opts,
  set-pgroup, write-append
</pre>
<h3>Internals</h3>
<pre>
 - Coverity (a static analysis tool) was run across the codebase and
   many fixes were made.
 - Generator can handle functions that return RBufferOut and have
   optional arguments.
 - Compatible with Perl 5.14.
 - Compatible with gcc 4.6.
 - Perform safety checks on QEMU.
 - C API tests can now fully test calls that have optional arguments.
 - Use ./configure --enable-install-daemon to install /usr/sbin/guestfsd.
 - po-docs directory now covers all man pages.
 - stderr from qemu process is now captured by the event subsystem.
</pre>
<h3>Bugs fixed</h3>
<pre>
 - 602997 part-get-bootable gives wrong result with an unordered part layout
 - 661280 virt-rescue: panic when shutting down: &quot;/sbin/reboot: No such file or directory&quot;
 - 700369 qemu-system-x86_64 says 'KVM not supported for this target'
 - 705200 guestmount attempt results in access denied
 - 714981 'list-filesystems' does not know about virtio 9p filesystems or detect existing mounts
 - 717786 libguestfs python bindings should have an explicit close call
 - 721275 virt-resize in F16 should support btrfs
</pre>
<h2>Release notes for libguestfs 1.10.0</h2>
<p> These release notes only cover the differences from the previous stable/dev branch split (1.8.0). For detailed changelogs, please see the git repository, or the ChangeLog file distributed in the tarball.</p>
<h3>New features</h3>
<p> &#8211; libguestfs and tools can be used against live virtual machines.<br />
   See the &#8216;guestfish &#8211;live&#8217; and &#8216;guestmount &#8211;live&#8217; options, and (for<br />
   the low-level interface) the new APIs set-attach-method and<br />
   get-attach-method.<br />
 &#8211; New virt tools:<br />
   virt-copy-in, virt-copy-out, virt-tar-in, virt-tar-out.<br />
 &#8211; libguestfs can get the drive letter mappings for Windows guests.<br />
 &#8211; virt-inspector displays drive letter mappings for Windows guests.<br />
 &#8211; Drive letters can now be used in virt-edit and guestfish programs<br />
   when operating on Windows guests.<br />
 &#8211; virt-resize now works on 32 bit hosts.<br />
 &#8211; You can now inspect the install disks and live CDs of many different<br />
   operating systems.<br />
 &#8211; guestfish &lt;! cmd which executes a shell cmd and inlines the result.<br />
 &#8211; guestfish, guestmount, virt-rescue now all support &#8211;ro and &#8211;rw<br />
   options, and the default for this can be chosen via a configuration<br />
   file (/etc/libguestfs-tools.conf).<br />
 &#8211; New event API allows more than one callback to be registered for<br />
   each event, makes it possible to call the API from other languages,<br />
   and allows nearly all log, debug and trace messages to be rerouted<br />
   from stderr.<br />
 &#8211; Greater FHS compliance for temporary files, including using /var/tmp<br />
   for large cached files that should survive reboot (instead of /tmp).<br />
 &#8211; guestfish, guestmount -m option allows mount options to be passed<br />
   through to the underlying filesystem.<br />
 &#8211; mkfs-opts allows filesystem features to be specified.<br />
 &#8211; More intelligent handling of mountpoints, allowing mkmountpoint, mount<br />
   and umount-all commands to work together properly.<br />
 &#8211; Trace messages are prefixed with a distinct string, allowing them to<br />
   be easily &#8216;grepped&#8217; out from debug output.<br />
 &#8211; guestfs_launch (guestfish &#8216;run&#8217; command) now produces progress<br />
   messages (a guestfish progress bar) if it takes longer than 5<br />
   seconds to run.<br />
 &#8211; Several long-running commands where we are unable to estimate time<br />
   to completion generate &#8220;pulse mode&#8221; progress events.  Progress bar<br />
   in guestfish has been updated to display these.<br />
 &#8211; Publish new example code in: C, Perl, Python, OCaml, Ruby.<br />
 &#8211; New virt-dhcp-address example program.<br />
 &#8211; The Java and Ruby bindings have been improved greatly.<br />
 &#8211; Perl includes a way to get the errno of the last error.<br />
 &#8211; Python bindings now compatible with rpyc (thanks Erez Shinan).<br />
 &#8211; Transifex is now being used to manage translations.<br />
   http://www.transifex.net/projects/p/libguestfs/<br />
 &#8211; Inspection now supports Red Hat Desktop, Slackware distributions.<br />
 &#8211; Inspection no longer fails for Windows guests that have two or<br />
   more disks.<br />
 &#8211; Inspection can now tell the difference between Windows 2008 Server<br />
   and Windows 7.<br />
 &#8211; Inspection can detect 32 bit applications installed in 64 bit<br />
   Windows, running on the WOW64 emulator.<br />
 &#8211; A series of protocol fixes has fixed the old bug RHBZ#576879<br />
   which used to cause errors during the upload command to lose<br />
   protocol synchronization.<br />
 &#8211; New logo!</p>
<h3>Security</h3>
<pre>
  [none]
</pre>
<h3>New APIs</h3>
<pre>
  first-private, get-attach-method, inspect-get-drive-mappings,
  inspect-get-product-variant,
  inspect-get-windows-current-control-set, next-private, resize2fs-M,
  set-attach-method.
</pre>
<h3>Internals</h3>
<pre>
 - The 'HACKING' file is obsolete.  The contents have been moved into
   a section of the <a href="//www.systutorials.com/docs/linux/man/3-guestfs/">guestfs</a>(3) manual page.
 - libguestfs-test-tool simplified.  It no longer needs the static
   binary or tries to construct an ISO.
 - rpcgen-generated files are compiled with -fno-strict-aliasing
   which should be safer (thanks Matt Booth).
 - virt-resize was rewritten in OCaml.
 - guestfish and other tools tested with valgrind; some memory leaks
   were fixed.
</pre>
<h3>Bugs fixed</h3>
<pre>
 - 502533 Updated Polish translation of libguestfs
 - 576879 libguestfs protocol loses synchronization if you 'upload' before mounting disks
 - 599503 document that mkmountpoint and umount-all cannot be mixed
 - 617440 guestfish: fails to tilde expand '~' when the $HOME env is unset
 - 664558 RFE: Allow to set log callback in Ruby bindings
 - 665358 Punjabi Translation Completed (pa_IN)
 - 666577 libguestfs: unknown filesystem /dev/fd0
 - 667610 Multiple bugs, memory leaks in libguestfs ruby bindings
 - 668112 virt-filesystems command fails on guest with corrupt filesystem label
 - 668574 guestfish -i is trying to mount all mounts from /etc/fstab and fails with an error when device doesn't exists
 - 673479 Add a grep-friendly string to LIBGUESTFS_TRACE output
 - 674130 Inspection code fails for Windows guest with two disks
 - 682756 libguestfs trace segfaults when list-filesystems returns error
 - 682979 libguestfs incorrectly detects Red Hat desktop as 'redhat-based' instead of 'redhat'
 - 690819 mkfs fails creating a filesystem on a disk device when using a disk with 'ide' interface
 - 691389 Extended attributes don't work over guestmount (FUSE)
 - 691724 virt-inspector reports unknown filesystem /dev/vda1
 - 692545 inspect-list-applications fails to detect 32 bit apps installed under WOW64 emulator on 64 bit Windows
 - 693324 sfdisk's python interface only accepts lists of type 'list' for the lines parameter
</pre>
<h2>Release notes for libguestfs 1.8</h2>
<p> These release notes only cover the differences from the previous stable/dev branch split (1.6.0). For detailed changelogs, please see the git repository, or the ChangeLog file distributed in the tarball.</p>
<h3>New features</h3>
<p> &#8211; Support and packages for Debian and Ubuntu.<br />
 &#8211; Daily builds from git repository on Debian and Ubuntu to reduce risk<br />
   of regressions.<br />
 &#8211; Port to ArchLinux &#8216;pacman&#8217; (thanks Thomas S Hatch).<br />
 &#8211; The following tools have been rewritten in C (originally in Perl):<br />
     . virt-cat<br />
     . virt-df<br />
     . virt-inspector<br />
     . virt-ls<br />
     . virt-rescue<br />
 &#8211; Some C tools support encrypted guests automatically.  This is<br />
   supported in: guestfish, guestmount, virt-cat, virt-inspector,<br />
   virt-ls.<br />
 &#8211; New tool virt-filesystems (in C) which is a replacement for<br />
   virt-list-filesystems and virt-list-partitions, and has a superset<br />
   of the functionality of those tools.<br />
 &#8211; guestfish, guestmount and the C tools use unified command line option<br />
   parsing, so they support many common options such as &#8216;-a disk.img&#8217;,<br />
   &#8216;-d libvirt-domain&#8217;, &#8216;-x&#8217;, &#8216;-v&#8217;.  The old command line option<br />
   parsing is preserved for compatibility in scripts etc.<br />
 &#8211; guestfish no longer has any dependencies on Perl<br />
 &#8211; New man pages containing programming examples: guestfs-examples(3) (C/C++),<br />
   guestfs-ocaml(3), guestfs-python(3), guestfs-ruby(3).<br />
 &#8211; Trace mode prints return values from API functions.<br />
 &#8211; virt-inspector can list applications installed in Windows guests, along<br />
   with a great deal of information about those applications.<br />
 &#8211; Add support for inspecting: Linux Mint, Mandriva, FreeBSD.<br />
 &#8211; guestfish &#8211;rw option (with no effect currently) to make potentially<br />
   dangerous write access explicit.<br />
 &#8211; guestfish &#8211;listen &#8211;csh for compatibility with csh, tcsh (thanks<br />
   Eric Blake).<br />
 &#8211; The first upstream version that introduced each API function is now<br />
   documented in guestfs(3).<br />
 &#8211; guestfs_last_errno allows you to retrieve the errno from the<br />
   daemon, correctly translated to the local operating system.<br />
 &#8211; Functions can now have optional parameters.<br />
 &#8211; Progress bars and progress notifications can now happen for upload<br />
   commands.<br />
 &#8211; Appliance builder more careful about not leaving temporary files<br />
   around in /tmp.<br />
 &#8211; getfattr/setfattr commands added to virt-rescue.<br />
 &#8211; ROADMAP file covers roadmap and goals for future releases.</p>
<h3>Security</h3>
<pre>
 - New SECURITY section in <a href="//www.systutorials.com/docs/linux/man/3-guestfs/">guestfs</a>(3) API documentation.
 - virt-inspector no longer runs any guest commands.
 - Inspection code is more careful about avoiding very large files
   from guests which might previously have caused a denial of service.
 - FUSE calls into guestmount are now traced when using guestmount -x.
</pre>
<h3>New APIs</h3>
<pre>
 - add-domain
 - add-drive-opts
 - getxattr
 - inspect-get-hostname
 - inspect-get-package-format
 - inspect-get-package-management
 - inspect-get-roots
 - inspect-list-applications
 - lgetxattr
 - mkfs-opts
</pre>
<h3>Internals</h3>
<p> &#8211; C programs now only link precisely with the libraries that they use.<br />
 &#8211; PCRE, libmagic, hivex and libvirt libraries are now completely<br />
   optional for building.<br />
 &#8211; Multiple memory leaks and file descriptor leaks fixed.<br />
 &#8211; Add a POD wrapper to unify generation of man pages and HTML files<br />
   across all programs.<br />
 &#8211; Source includes phony images of Fedora, Debian, Ubuntu and<br />
   Windows guests.<br />
 &#8211; Ruby bindings have &#8216;make install&#8217; rule.<br />
 &#8211; &lt;guestfs.h&gt; is now a single file.<br />
 &#8211; &lt;guestfs.h&gt; does not require XDR headers.<br />
 &#8211; ocaml xml-light library is no longer required to build (thanks<br />
   Maxim Koltsov).<br />
 &#8211; ./configure &#8211;disable-[&#8230;] for each language binding (thanks<br />
   Maxim Koltsov).<br />
 &#8211; Old ocaml-viewer program removed (use guestfs-browser instead).<br />
 &#8211; New C API test type &#8216;InitScratchFS&#8217; makes the tests run a little<br />
   more quickly.<br />
 &#8211; Excluded packages in the appliance are now listed in a separate<br />
   file appliance/excludelist.in, and can be customized per-distro.</p>
<h3>Bugs fixed</h3>
<pre>
 - 663407 readlink and readlinklist returns /sysroot/ in some paths
 - 661280 virt-rescue: panic when shutting down: &quot;/sbin/reboot: No such file or directory&quot;
 - 657499 checksum: wrong check sum type causes umount to fail
 - 655554 Whole disk paths are not made canonical by virt-inspector
 - 654638 openssl updated to 1.0.0b libguestfs depends on exact file names
 - 652796 ruby bindings not installed by 'make install', hence omitted from the binary distribution
</pre>
<h2>RELEASE NOTES FOR LIBGUESTFS 1.6</h2>
<p> These release notes only cover the differences from the previous stable/dev branch split (1.4.0). For detailed changelogs, please see the git repository, or the ChangeLog file distributed in the tarball.</p>
<h3>New features</h3>
<p> &#8211; Use a new method for creating and caching the appliance.  This<br />
   greatly improves the performance of libguestfs, often by a factor<br />
   of x 4 to x 5.<br />
 &#8211; Support for guest inspection (like virt-inspector) via the ordinary<br />
   API and all language bindings.  &#8216;guestfish -i&#8217; option is as a side-<br />
   effect much quicker.<br />
 &#8211; virt-inspector and core inspection API can now detect guests running:<br />
   Fedora, Debian, Ubuntu, Windows, Red Hat Enterprise Linux, CentOS,<br />
   Scientific Linux, Gentoo, Pardus, Arch Linux, MeeGo.<br />
 &#8211; Support for LUKS whole-disk encryption in guests.<br />
 &#8211; PHP bindings.<br />
 &#8211; Progress messages (and progress bars in guestfish and virt-resize)<br />
   for certain long-running operations.<br />
 &#8211; virt-df is now much more efficient.  Use &#8216;&#8211;one-per-guest&#8217; to restore<br />
   the old per-guest isolation behaviour.<br />
 &#8211; guestfish &#8216;copy-in&#8217; and &#8216;copy-out&#8217; commands for copying files and<br />
   directories recursively in and out of the guest.<br />
 &#8211; guestfish &#8216;hexedit&#8217; command for doing binary edits to devices and<br />
   files.<br />
 &#8211; Change guestfish -i syntax to allow commands to be specified on the<br />
   command line (retaining backwards compatibility).<br />
 &#8211; guestfish &#8216;-d &lt;domain&gt;&#8217; for adding disks from libvirt domains.<br />
 &#8211; guestfish &#8216;-N&#8217; option supports several new prepared disk image types:<br />
         lvfs : disk with LV formatted with filesystem<br />
           lv : disk with LV<br />
     bootroot : boot+root<br />
   bootrootlv : boot and root on LV<br />
 &#8211; guestfish &#8216;more&#8217; and &#8216;edit&#8217; commands now work with arbitrary files.<br />
 &#8211; guestfish &#8216;&#8211;echo-keys&#8217; option allows you to echo keys/passphrases<br />
   while typing them.<br />
 &#8211; guestmount now supports -a / -d / -i options, like guestfish.<br />
 &#8211; Use virtio-serial for communications with the appliance.  This<br />
   also has a major performance benefit.<br />
 &#8211; virt-edit &#8216;-b&#8217; option to create a backup of edited files.<br />
 &#8211; virt-edit &#8216;-e&#8217; option for non-interactive edits to files.<br />
 &#8211; Ability to capture core dumps from the appliance (thanks Matthew Booth).<br />
 &#8211; virt-rescue now shuts down cleanly (thanks Matthew Booth).<br />
 &#8211; virt-rescue now has a &#8211;network option to enable network access.<br />
 &#8211; virt-resize can now handle guests which use GPT partition table format.<br />
 &#8211; virt-resize has better support for shrinking guests.<br />
 &#8211; virt-resize supports qcow2-format guests.<br />
 &#8211; $TMPDIR can be used to override almost all temporary directory usage.<br />
 &#8211; OCaml users can use an alternate OO-style of coding, eg. g#launch ()<br />
 &#8211; The API supports calls which take optional parameters, eg.<br />
     $g-&gt;add_drive_opts (&#8220;disk&#8221;, readonly =&gt; 1);<br />
 &#8211; Trace output now escapes and shortens large strings(thanks<br />
                                                           Matthew Booth)<br />
         .-<br />
     Autosync is now on by default,<br />
     resulting in more reliable behaviour<br />
         when the handle is closed.-<br />
         virt &#8211; df&#8211; uuid option allows you to follow a domain across migration and renaming.- Translations of manual pages.</p>
<h3>Security</h3>
<pre>
 - CVE-2010-3851 libguestfs: missing disk format specifier when adding a disk
   <a rel="nofollow" href="https://www.redhat.com/archives/libguestfs/2010-October/msg00036.html">https://www.redhat.com/archives/libguestfs/2010-October/msg00036.html</a>
   This is comprehensively fixed in this release, and the fix will be
   backported to the other stable branches after more testing.
 - virt-inspector no longer relies on untrusted guest code to list
   applications in some guests.
</pre>
<h3>New APIs</h3>
<pre>
  download-offset, file-architecture, findfs-label, findfs-uuid,
  inspect-os, inspect-get-arch, inspect-get-distro,
  inspect-get-filesystems, inspect-get-major-version,
  inspect-get-minor-version, inspect-get-mountpoints,
  inspect-get-product-name, inspect-get-type, is-blockdev, is-chardev,
  is-fifo, is-lv, is-socket, is-symlink, list-filesystems, luks-add-key,
  luks-close, luks-format, luks-format-cipher, luks-kill-slot,
  luks-open, luks-open-ro, lvm-clear-filter, lvm-canonical-lv-name,
  lvm-set-filter, part-to-dev, pread-device, pwrite-device,
  upload-offset
</pre>
<h3>Internals</h3>
<pre>
 - Use size_t for loop iterators.
 - Refactor the library code into separate files.
 - Refactor the generator code into separate files.
 - Generate guestfish commands.
 - guestfish &amp; guestmount options processing is unified.
 - Protocol changes:
     error message size increased to 64K
     send errno to library
 - Add 'make bindist' to make a binary distribution.
 - Cleaner behaviour under valgrind.
 - More testing of the guestfish command line options and libvirt
   integration.
 - The Perl inspection code is no longer used by any of the tools.
</pre>
<h3>Bugs fixed</h3>
<p> &#8211; 646822 libguestfs trace mode should not print long binary strings<br />
 &#8211; 646821 virt-df should have &#8211;uuid option<br />
 &#8211; 646432 /dev/mapper paths should not be returned from guestfs_mountpoints<br />
 &#8211; 643624 libguestfs tools documentation should describe how to quote guest domain names from shell<br />
 &#8211; 642934 No way to specify disk format when adding a disk to libguestfs<br />
 &#8211; 642933 guestfs_list_filesystems should be used in all possible places<br />
 &#8211; 642932 guestmount options should match guestfish options<br />
 &#8211; 642930 virt-inspector (Sys::Guestfs::Lib) should use C inspection APIs<br />
 &#8211; 642929 C inspection code should ignore /dev/fd* in /etc/fstab<br />
 &#8211; 642826 virt-resize converts any other image format to raw without notifying user, instructions do not account for this<br />
 &#8211; 640961 Document that grub-install might be needed for old Linux guests after virt-resize<br />
 &#8211; 639986 virt-df &#8211;csv does not properly quote &#8221; in libvirt domain names<br />
 &#8211; 639405 Interrupted cached appliance creation leaves libguestfs unusable<br />
 &#8211; 638901 Appliance filename should not contain repository name<br />
 &#8211; 638899 /dev/mapper paths should not be returned from C inspection APIs<br />
 &#8211; 636918 Updates to Spanish translation<br />
 &#8211; 636061 [abrt] guestfish-1.2.11-1.fc12: malloc_consolidate: Process /usr/bin/guestfish was killed by signal 11 (SIGSEGV)<br />
 &#8211; 635969 glob echo mkfs ext2 /dev/vd[b-t]1 prints garbage<br />
 &#8211; 634246 guestfs_part_get_parttype returns &#8220;loop&#8221; when run against a partition, LV or filesystem<br />
 &#8211; 633766 virt-resize &#8211;shrink fails<br />
 &#8211; 633357 Updates to Spanish translation<br />
 &#8211; 633096 virt-resize calculates block device size incorrectly, doesn&#8217;t work with qcow2 target<br />
 &#8211; 629593 Dutch translation added<br />
 &#8211; 627556 Updates to Spanish translations of libguestfs<br />
 &#8211; 626843 Updates to Spanish translations<br />
 &#8211; 619793 [RFE] Need a way to determine if a particular block device is a logical volume<br />
 &#8211; 618556 virt-rescue return none zero value when exit<br />
 &#8211; 617200 mount operation failed and hung on some images which running in read-only mode<br />
 &#8211; 610880 libguestfs should set broader read perms on tmpdir, so works in some situations when executed with umask 077<br />
 &#8211; 599503 document that mkmountpoint and umount-all cannot be mixed<br />
 &#8211; 571714 Running virt-df on disk image relabels it, so qemu can no longer write to it.<br />
 &#8211; 502533 Updated Polish translation of libguestfs</p>
<h2>RELEASE NOTES FOR LIBGUESTFS 1.4</h2>
<p> These release notes only cover the differences from the previous stable/dev branch split (1.2.0). For detailed changelogs, please see the git repository, or the ChangeLog file distributed in the tarball.</p>
<h3>New features</h3>
<p> &#8211; guestfish lets you choose a prepared disk image, eg:<br />
     guestfish -N fs:ext4<br />
 &#8211; Add write support to guestmount (FUSE) module.<br />
 &#8211; virt-resize can now resize the content of partitions and logical<br />
   volumes in the guest, and we have better support for shrinking guests.<br />
 &#8211; Bash tab-completion script for guestfish.<br />
 &#8211; Add ZFS support to virt-rescue.<br />
 &#8211; New tool &#8216;virt-make-fs&#8217; for creating filesystems with content.<br />
 &#8211; Allow suffixes on any guestfish number parameter, eg. &#8220;1M&#8221;.<br />
 &#8211; guestfish &#8216;man&#8217; command opens the manual page.<br />
 &#8211; guestfish supports a &#8220;heredoc&#8221; syntax for uploading files:<br />
     upload -&lt;&lt;_end_ /foo<br />
     content<br />
     _end_<br />
 &#8211; Some guestfish commands now print their output in octal or hex<br />
   where appropriate (RHBZ#583242).<br />
 &#8211; Allow dash prefix on guestfish command line.  This ignores any<br />
   error from the second command:                   (RHBZ#578407)<br />
     guestfish &#8212; cmd1 : -cmd2 : cmd3<br />
 &#8211; guestfish -h / help command now returns an error for non-existent<br />
   commands (RHBZ#597145).<br />
 &#8211; New &#8216;supported&#8217; command in guestfish to list optional groups of<br />
   commands which are supported by the daemon / configuration.<br />
 &#8211; virt-inspector and guestfish -i now work for filenames which<br />
   contain spaces (RHBZ#507810).<br />
 &#8211; Change the protocol to use link-local addresses, to avoid<br />
   conflicting with any address that the host might be using<br />
   (RHBZ#588763).<br />
 &#8211; libguestfs now sets the correct time and timezone on filesystem<br />
   modifications.<br />
 &#8211; Sort the domains into alphabetical order in virt-df.<br />
 &#8211; Make mkfs-b command work for FAT and NTFS by mapping the blocksize<br />
   parameter to the cluster size (RHBZ#599464).<br />
 &#8211; Add version numbers to Perl modules (RHBZ#521674).<br />
 &#8211; Localization now works for all the libguestfs tools (RHBZ#559963).<br />
 &#8211; Tools now support filesystem-on-image VMs (RHBZ#590167).<br />
 &#8211; virt-list-partitions has a &#8216;-t&#8217; option to show the total size of disks.<br />
 &#8211; Include extra Augeas lenses in the supermin appliance (Matthew Booth).<br />
 &#8211; Add error and close callbacks.<br />
 &#8211; Add explicit close method in the Perl API.<br />
 &#8211; Multiple fixes for RHEL 5 compatibility.<br />
 &#8211; Multiple fixes for Debian/Ubuntu compatibility.<br />
 &#8211; Multiple revisions to improve the documentation.</p>
<h3>Security</h3>
<pre>
 - Fix a potential DoS in virt-inspector and virt-v2v if a specially
   crafted disk image contained a char device in place of one of the
   configuration files that we read under /etc (RHBZ#582484).
</pre>
<h3>New APIs</h3>
<pre>
 - aug-clear - clear Augeas path
 - available-all-groups - return a list of all optional groups
 - base64-in - upload base64-encoded data to file
 - base64-out - download file and encode as base64
 - checksum-device - compute checksums on the contents of a device
 - checksums-out - compute checksums of multiple files in a directory
 - debug-upload - upload a file to the appliance
 - fallocate64 - preallocate a file in the guest filesystem
 - fill-pattern - fill a file with a repeating pattern of bytes
 - get-umask - get the current umask
 - lvresize-free - expand an LV to fill free space
 - ntfsresize - resize an NTFS filesystem
 - ntfsresize-size - resize an NTFS filesystem (with size)
 - part-del - delete a partition
 - part-get-bootable - get the bootable flag of a partition
 - part-get-mbr-id - get the MBR type byte of a partition
 - part-set-mbr-id - set the MBR type byte of a partition
 - pvresize-size - resize a physical volume (with size)
 - pwrite - write to part of a file
 - resize2fs-size - resize an ext2/3/4 filesystem (with size)
 - txz-in - unpack compressed tarball to directory (RHBZ#580556)
 - txz-out - pack directory into compressed tarball (RHBZ#580556)
 - vfs-label - get the filesystem label
 - vfs-uuid - get the filesystem UUID
 - vgscan - rescan for LVM physical volumes, volume groups and logical volumes
 - write - create a new file
 - zero-device - write zeroes to an entire device
</pre>
<h3>Internals</h3>
<pre>
 - Extend the generator to support testing optional features.
 - Stricter checks on input parameters to many calls (RHBZ#501893 RHBZ#501894)
 - Extend the protocol to support sending arbitrary 8 bit data buffers.
 - Ship 'BUGS' file with releases.  This is a summary of the bugs in
   the Red Hat Bugzilla database.
 - Ship 'RELEASE-NOTES' file with releases, containing release notes.
 - Unify supermin appliance building into one place, in febootstrap 2.7.
 - Fix the protocol code to handle the case where both ends send cancel
   messages at the same time.
</pre>
<h3>Bugs fixed</h3>
<pre><code>
 - 612178 guestfish: using -m option in conjunction with --listen option causes appliance to die
 - 610880 libguestfs should set broader read perms on tmpdir, so works in some situations when executed with umask 077
 - 604691 OCaml bindings are not thread safe
 - 603870 Updates to Spanish translation
 - 602592 [RFE] expose guestfs_close in perl bindings
 - 600977 virt-df -h --csv "Argument .. isn't numeric in printf"
 - 599464 mkfs-b does not support vfat/ntfs
 - 598807 add_cdrom does not work in RHEL 6
 - 598309 part-list and several other cmd failed on libguestfs on RHEL5
 - 597145 guestfish 'help' command should indicate error in exit status with an unknown command
 - 597135 guestfish write-file cmd does not check "size" parameter
 - 597118 A warning should be given in the help of mke2journal-L for the length of label
 - 597112 get-e2uuid should use blkid instead of "tune2fs -l" to get filesystem UUID
 - 596776 virt-inspector doesn't discover modprobe aliases on RHEL 3 guests
 - 596763 Updates to Spanish translation
 - 593292 Updates to Spanish translation
 - 592883 can not edit files on  images mounted with guestmount cmd
 - 592360 Updates to Spanish translation
 - 591250 virt-tar prints "tar_in: tar subcommand failed on directory" if the archive is compressed or not in the right format
 - 591155 virt-tar prints "tar_in: tar subcommand failed on directory" if a disk image is not writable
 - 591142 virt-inspector should give an error for unrecognized disk images
 - 590167 virt-inspector and other virt tools should be able to handle filesystem-on-image VMs
 - 589039 guestfish read-file cmd will cause daemon hang when read large files
 - 588851 guestfs_launch() returns -1, but guestfs_last_error() == NULL
 - 588763 libguestfs should use non-public or link-local addresses for appliance network
 - 588733 Updates to Spanish translation
 - 588651 guestfish 'strings-e' cmd does not give proper error message or hint
 - 587484 lvresize can't reduce size of a volumn
 - 585961 Updates to Spanish translation
 - 585223 ntfsresize should support shrinking filesystems
 - 585222 pvresize should support shrinking PVs
 - 585221 resize2fs should support shrinking filesystems
 - 584038 Updates to Spanish translation
 - 583554 [FEAT] mknod-mode command is needed to set mode explicitly
 - 583242 [RFE] guestfish should print outputs in a suitable base (eg. octal for modes)
 - 582993 guestfish eats words when tab completing case (in)sensitive paths
 - 582953 Misleading help information about lvcreate command
 - 582948 mknod command doesn't make block, character or FIFO devices
 - 582929 mknod doesn't check for invalid mode
 - 582901 guestfish chmod/umask commands do not check invalid mode value
 - 582899 guestfish:sparse is missed from command autocomplete list
 - 582891 [Feature Request] behavior and return value of guestfish umask cmd should be changed
 - 582548 [mknod] umask shouldn't take effect when mode is set explicitly
 - 582484 some guestfish sub commands can not handle special files properly
 - 582252 Updates to Spanish translation
 - 581501 Updates to Spanish translation
 - 580650 virt-inspector warns "No grub default specified at /usr/lib/perl5/Sys/Guestfs/Lib.pm at [...]"
 - 580556 request for libguestfs to support .txz tarballs
 - 580246 tar-in command hangs if uploading more than available space
 - 580016 aug-ls in guestfish does not take augeas variable as argument
 - 579664 guestfish doesn't report error when there is not enough space for image allocation
 - 579608 multiple commands in guestfish can not work for symbol links
 - 579155 libguestfs hangs if qemu doesn't start (in null vmchannel mode)
 - 578407 the prefix '-' in sub-command isn't handled by guestfish in remote control mode
 - 576879 libguestfs protocol loses synchronization if you 'upload' before mounting disks
 - 559963 libguestfs Perl programs do set locale, but still localization doesn't work
 - 521674 Perl modules are unversioned, but should carry version numbers
 - 516096 Race condition in test_swapon_label_0: /sbin/blockdev: BLKRRPART: Device or resource busy
 - 507810 guestfish -i / virt-inspector cannot handle spaces in filenames
 - 502533 Updated Polish translation of libguestfs
 - 501894 Some String parameters should be OptString
 - 501893 String parameters should be checked for != NULL
 - 501889 write-file does not support strings containing ASCII NUL
 - 484986 grub-install fails on virtio disk
</code></pre>
<h2>RELEASE NOTES FOR HISTORICAL VERSIONS OF LIBGUESTFS</h2>
<p> Before 2010 libguestfs did not have official release notes or a formalized version numbering system. However these are links to historically significant versions.</p>
<dl>
<dt>2009-11-10 (1.0.78)</p>
<dd> <a rel="nofollow" href="https://www.redhat.com/archives/libguestfs/2009-November/msg00095.html">https://www.redhat.com/archives/libguestfs/2009-November/msg00095.html</a></p>
<dt>2009-09-13 (1.0.67)</p>
<dd> <a rel="nofollow" href="https://www.redhat.com/archives/libguestfs/2009-August/msg00281.html">https://www.redhat.com/archives/libguestfs/2009-August/msg00281.html</a></p>
<dt>2009-07-23 (1.0.64)</p>
<dd> <a rel="nofollow" href="https://www.redhat.com/archives/libguestfs/2009-July/msg00059.html">https://www.redhat.com/archives/libguestfs/2009-July/msg00059.html</a></p>
<dt>2009-07-14 (1.0.59)</p>
<dd> <a rel="nofollow" href="https://www.redhat.com/archives/libguestfs/2009-July/msg00023.html">https://www.redhat.com/archives/libguestfs/2009-July/msg00023.html</a></p>
<dt>2009-04-01 (the initial announcement)</p>
<dd> <a rel="nofollow" href="http://rwmj.wordpress.com/2009/04/01/libguestfs-access-and-modify-virtual-machine-disk-images/">http://rwmj.wordpress.com/2009/04/01/libguestfs-access-and-modify-virtual-machine-disk-images/</a></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-guestfs-examples/">guestfs-examples</a></code>(1), <code><a href="/docs/linux/man/1-guestfs-faq/">guestfs-faq</a></code>(1), <code><a href="/docs/linux/man/1-guestfs-performance/">guestfs-performance</a></code>(1), <code><a href="/docs/linux/man/1-guestfs-recipes/">guestfs-recipes</a></code>(1), <code><a href="/docs/linux/man/1-guestfs-testing/">guestfs-testing</a></code>(1), <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3), <code><a href="/docs/linux/man/1-guestfish/">guestfish</a></code>(1), <a rel="nofollow" href="http://libguestfs.org/">http://libguestfs.org/</a></p>
<h2>AUTHOR</h2>
<p> Richard W.M. Jones</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2009-2019 Red Hat Inc.</p>
<h2>LICENSE</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE.</font> See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
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
<dd> Run <code><a href="/docs/linux/man/1-libguestfs-test-tool/">libguestfs-test-tool</a></code>(1) and paste the <code>complete, unedited</code> output into the bug report. </p>
</dl>
<h2>Index</h2>
<dt><a href="#lbAJ">RELEASE NOTES FOR LIBGUESTFS 1.38</a></p>
<dd>
<dt><a href="#lbAQ">RELEASE NOTES FOR LIBGUESTFS 1.36</a></p>
<dd>
<dt><a href="#lbAX">RELEASE NOTES FOR LIBGUESTFS 1.34</a></p>
<dd>
<dt><a href="#lbBE">RELEASE NOTES FOR LIBGUESTFS 1.32</a></p>
<dd>
<dt><a href="#lbBL">RELEASE NOTES FOR LIBGUESTFS 1.30</a></p>
<dd>
<dt><a href="#lbBT">RELEASE NOTES FOR LIBGUESTFS 1.28</a></p>
<dd>
<dt><a href="#lbCA">RELEASE NOTES FOR LIBGUESTFS 1.26</a></p>
<dd>
<dt><a href="#lbCH">RELEASE NOTES FOR LIBGUESTFS 1.24</a></p>
<dd>
<dt><a href="#lbCO">RELEASE NOTES FOR LIBGUESTFS 1.22</a></p>
<dd>
<dt><a href="#lbCU">RELEASE NOTES FOR LIBGUESTFS 1.20</a></p>
<dd>
<dt><a href="#lbDA">RELEASE NOTES FOR LIBGUESTFS 1.18</a></p>
<dd>
<dt><a href="#lbDG">RELEASE NOTES FOR LIBGUESTFS 1.16</a></p>
<dd>
<dt><a href="#lbDM">RELEASE NOTES FOR LIBGUESTFS 1.14</a></p>
<dd>
<dt><a href="#lbDS">RELEASE NOTES FOR LIBGUESTFS 1.12</a></p>
<dd>
<dt><a href="#lbDY">Release notes for libguestfs 1.10.0</a></p>
<dd>
<dt><a href="#lbEE">Release notes for libguestfs 1.8</a></p>
<dd>
<dt><a href="#lbEK">RELEASE NOTES FOR LIBGUESTFS 1.6</a></p>
<dd>
<dt><a href="#lbEQ">RELEASE NOTES FOR LIBGUESTFS 1.4</a></p>
<dd>
<dt><a href="#lbEW">RELEASE NOTES FOR HISTORICAL VERSIONS OF LIBGUESTFS</a></p>
<dd>
<dt><a href="#lbEX">SEE ALSO</a></p>
<dd>
<dt><a href="#lbEY">AUTHOR</a></p>
<dd>
<dt><a href="#lbEZ">COPYRIGHT</a></p>
<dd>
<dt><a href="#lbFA">LICENSE</a></p>
<dd>
<dt><a href="#lbFB">BUGS</a></p>
<dd></dl>
