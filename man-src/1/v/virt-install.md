---
title: "virt-install(1)"
name: "virt-install"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-install/"
description: "virt-install – provision new virtual machines"
---

<h2 class="name">NAME</h2>
<p> virt-install &#8211; provision new virtual machines </p>
<h2>SYNOPSIS</h2>
<p> <code>virt-install</code> [<font SIZE="-1">OPTION</font>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>virt-install</code> is a command line tool for creating new <font SIZE="-1">KVM,</font> Xen, or Linux container guests using the <tt>&quot;libvirt&quot;</tt> hypervisor management library. See the <font SIZE="-1">EXAMPLES</font> section at the end of this document to quickly get started. </p>
<p> <code>virt-install</code> tool supports graphical installations using (for example) <font SIZE="-1">VNC</font> or <font SIZE="-1">SPICE,</font> as well as text mode installs over serial console. The guest can be configured to use one or more virtual disks, network interfaces, audio devices, physical <font SIZE="-1">USB</font> or <font SIZE="-1">PCI</font> devices, among others. </p>
<p> The installation media can be held locally or remotely on <font SIZE="-1">NFS, HTTP, FTP</font> servers. In the latter case <tt>&quot;virt-install&quot;</tt> will fetch the minimal files necessary to kick off the installation process, allowing the guest to fetch the rest of the <font SIZE="-1">OS</font> distribution as needed. <font SIZE="-1">PXE</font> booting, and importing an existing disk image (thus skipping the install phase) are also supported. </p>
<p> Given suitable command line arguments, <tt>&quot;virt-install&quot;</tt> is capable of running completely unattended, with the guest &#8216;kickstarting&#8217; itself too. This allows for easy automation of guest installs. </p>
<p> Many arguments have sub options, specified like opt1=foo,opt2=bar, etc. Try &#8211;option=? to see a complete list of sub options associated with that argument, example: virt-install &#8211;disk=? </p>
<p> Most options are not required. Minimum requirements are &#8211;name, &#8211;memory, guest storage (&#8211;disk or &#8211;filesystem), and an install option.</p>
<h2>CONNECTING TO LIBVIRT</h2>
<dl>
<dt><code>-c</code> <font SIZE="-1">URI</font></p>
<dd>
<dt><code>&#8211;connect</code> <font SIZE="-1">URI</font></p>
<dd> Connect to a non-default hypervisor. If this isn&#8217;t specified, libvirt will try and choose the most suitable default. </p>
<p> Some valid options here are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><a href="qemu:///system">qemu:///system</a></p>
<dd> For creating <font SIZE="-1">KVM</font> and <font SIZE="-1">QEMU</font> guests to be run by the system libvirtd instance. This is the default mode that virt-manager uses, and what most <font SIZE="-1">KVM</font> users want.</p>
<dt><a href="qemu:///session">qemu:///session</a></p>
<dd> For creating <font SIZE="-1">KVM</font> and <font SIZE="-1">QEMU</font> guests for libvirtd running as the regular user.</p>
<dt><a href="xen:///">xen:///</a></p>
<dd> For connecting to Xen.</p>
<dt><a href="lxc:///">lxc:///</a></p>
<dd> For creating linux containers</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h2>GENERAL OPTIONS</h2>
<p> General configuration parameters that apply to all types of guest installs.</p>
<dl>
<dt><code>-n</code> <font SIZE="-1">NAME</font></p>
<dd>
<dt><code>&#8211;name</code> <font SIZE="-1">NAME</font></p>
<dd> Name of the new guest virtual machine instance. This must be unique amongst all guests known to the hypervisor on the connection, including those not currently active. To re-define an existing guest, use the <tt><a href="/docs/linux/man/1-virsh/">virsh</a>(1)</tt> tool to shut it down (&#8216;virsh shutdown&#8217;) &amp; delete (&#8216;virsh undefine&#8217;) it prior to running <tt>&quot;virt-install&quot;</tt>.</p>
<dt><code>&#8211;memory</code> <font SIZE="-1">OPTIONS</font></p>
<dd> Memory to allocate for the guest, in MiB. Sub options are available, like &#8216;maxmemory&#8217; and &#8216;hugepages&#8217;. This deprecates the -r/&#8211;ram option. </p>
<p> Use &#8211;memory=? to see a list of all available sub options. Complete details at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsMemoryAllocation">http://libvirt.org/formatdomain.html#elementsMemoryAllocation</a>&gt;</p>
<dt><code>&#8211;memorybacking</code> <font SIZE="-1">OPTIONS</font></p>
<dd> This option will influence how virtual memory pages are backed by host pages. </p>
<p> Use &#8211;memorybacking=? to see a list of all available sub options. Complete details at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsMemoryBacking">http://libvirt.org/formatdomain.html#elementsMemoryBacking</a>&gt;</p>
<dt><code>&#8211;arch</code> <font SIZE="-1">ARCH</font></p>
<dd> Request a non-native <font SIZE="-1">CPU</font> architecture for the guest virtual machine. If omitted, the host <font SIZE="-1">CPU</font> architecture will be used in the guest.</p>
<dt><code>&#8211;machine</code> <font SIZE="-1">MACHINE</font></p>
<dd> The machine type to emulate. This will typically not need to be specified for Xen or <font SIZE="-1">KVM,</font> but is useful for choosing machine types of more exotic architectures.</p>
<dt><code>&#8211;metadata</code> OPT=VAL,[&#8230;]</p>
<dd> Specify metadata values for the guest. Possible options include name, uuid, title, and description. This option deprecates -u/&#8211;uuid and &#8211;description. </p>
<p> Use &#8211;metadata=? to see a list of all available sub options. Complete details at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsMetadata">http://libvirt.org/formatdomain.html#elementsMetadata</a>&gt;</p>
<dt><code>&#8211;events</code> OPT=VAL,[&#8230;]</p>
<dd> Specify events values for the guest. Possible options include on_poweroff, on_reboot, and on_crash. </p>
<p> Use &#8211;events=? to see a list of all available sub options. Complete details at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsEvents">http://libvirt.org/formatdomain.html#elementsEvents</a>&gt;</p>
<dt><code>&#8211;resource</code> OPT=VAL,[&#8230;]</p>
<dd> Specify resource partitioning for the guest. </p>
<p> Use &#8211;resource=? to see a list of all available sub options. Complete details at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#resPartition">http://libvirt.org/formatdomain.html#resPartition</a>&gt;</p>
<dt><code>&#8211;vcpus</code> <font SIZE="-1">OPTIONS</font></p>
<dd> Number of virtual cpus to configure for the guest. If &#8216;maxvcpus&#8217; is specified, the guest will be able to hotplug up to <font SIZE="-1">MAX</font> vcpus while the guest is running, but will startup with <font SIZE="-1">VCPUS.</font> </p>
<p> <font SIZE="-1">CPU</font> topology can additionally be specified with sockets, cores, and threads. If values are omitted, the rest will be autofilled preferring sockets over cores over threads. </p>
<p> &#8216;cpuset&#8217; sets which physical cpus the guest can use. <tt>&quot;CPUSET&quot;</tt> is a comma separated list of numbers, which can also be specified in ranges or cpus to exclude. Example: </p>
<pre>
    0,2,3,5     : Use processors 0,2,3 and 5
    1-5,^3,8    : Use processors 1,2,4,5 and 8
</pre>
<p> If the value &#8216;auto&#8217; is passed, virt-install attempts to automatically determine an optimal cpu pinning using <font SIZE="-1">NUMA</font> data, if available. </p>
<p> Use &#8211;vcpus=? to see a list of all available sub options. Complete details at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsCPUAllocation">http://libvirt.org/formatdomain.html#elementsCPUAllocation</a>&gt;</p>
<dt><code>&#8211;numatune</code> <font SIZE="-1">OPTIONS</font></p>
<dd> Tune <font SIZE="-1">NUMA</font> policy for the domain process. Example invocations </p>
<pre>
    --numatune 1,2,3,4-7
    --numatune 1-3,5,mode=preferred
</pre>
<p> Specifies the numa nodes to allocate memory from. This has the same syntax as <tt>&quot;--cpuset&quot;</tt> option. mode can be one of &#8216;interleave&#8217;, &#8216;preferred&#8217;, or &#8216;strict&#8217; (the default). See &#8216;man 8 numactl&#8217; for information about each mode. </p>
<p> Use &#8211;numatune=? to see a list of all available sub options. Complete details at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsNUMATuning">http://libvirt.org/formatdomain.html#elementsNUMATuning</a>&gt;</p>
<dt><code>&#8211;memtune</code> <font SIZE="-1">OPTIONS</font></p>
<dd> Tune memory policy for the domain process. Example invocations </p>
<pre>
    --memtune 1000
    --memtune hard_limit=100,soft_limit=60,swap_hard_limit=150,min_guarantee=80
</pre>
<p> Use &#8211;memtune=? to see a list of all available sub options. Complete details at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsMemoryTuning">http://libvirt.org/formatdomain.html#elementsMemoryTuning</a>&gt;</p>
<dt><code>&#8211;blkiotune</code> <font SIZE="-1">OPTIONS</font></p>
<dd> Tune blkio policy for the domain process. Example invocations </p>
<pre>
    --blkiotune 100
    --blkiotune weight=100,device_path=/dev/sdc,device_weight=200
</pre>
<p> Use &#8211;blkiotune=? to see a list of all available sub options. Complete details at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsBlockTuning">http://libvirt.org/formatdomain.html#elementsBlockTuning</a>&gt;</p>
<dt><code>&#8211;cpu</code> MODEL[,+feature][,-feature][,match=MATCH][,vendor=VENDOR]</p>
<dd> Configure the <font SIZE="-1">CPU</font> model and <font SIZE="-1">CPU</font> features exposed to the guest. The only required value is <font SIZE="-1">MODEL,</font> which is a valid <font SIZE="-1">CPU</font> model as known to libvirt. </p>
<p> Libvirt&#8217;s feature policy values force, require, optional, disable, or forbid, or with the shorthand &#8216;+feature&#8217; and &#8216;-feature&#8217;, which equal &#8216;force=feature&#8217; and &#8216;disable=feature&#8217; respectively </p>
<p> Some examples:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;cpu core2duo,+x2apic,disable=vmx</code></p>
<dd> Expose the core2duo <font SIZE="-1">CPU</font> model, force enable x2apic, but do not expose vmx</p>
<dt><code>&#8211;cpu host</code></p>
<dd> Expose the host CPUs configuration to the guest. This enables the guest to take advantage of many of the host CPUs features (better performance), but may cause issues if migrating the guest to a host without an identical <font SIZE="-1">CPU.</font></p>
<dt><code>&#8211;cpu host-model-only</code></p>
<dd> Expose the nearest host <font SIZE="-1">CPU</font> model configuration to the guest. It is the best <font SIZE="-1">CPU</font> which can be used for a guest on any of the hosts.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Use &#8211;cpu=? to see a list of all available sub options. Complete details at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsCPU">http://libvirt.org/formatdomain.html#elementsCPU</a>&gt;</dl>
<dt><code>&#8211;security</code> type=TYPE[,label=LABEL][,relabel=yes|no]</p>
<dd> Configure domain security driver settings. Type can be either &#8216;static&#8217; or &#8216;dynamic&#8217;. &#8216;static&#8217; configuration requires a security <font SIZE="-1">LABEL.</font> Specifying <font SIZE="-1">LABEL</font> without <font SIZE="-1">TYPE</font> implies static configuration. </p>
<p> To have libvirt automatically apply your static label, you must specify relabel=yes. Otherwise disk images must be manually labeled by the admin, including images that virt-install is asked to create. </p>
<p> Use &#8211;security=? to see a list of all available sub options. Complete details at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#seclabel">http://libvirt.org/formatdomain.html#seclabel</a>&gt;</p>
<dt><code>&#8211;features</code> FEAT=on|off,&#8230;</p>
<dd> Set elements in the guests &lt;features&gt; <font SIZE="-1">XML</font> on or off. Examples include acpi, apic, eoi, privnet, and hyperv features. Some examples:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;features eoi=on</code></p>
<dd> Enable <font SIZE="-1">APIC PV EOI</font></p>
<dt><code>&#8211;features hyperv_vapic=on,hyperv_spinlocks=off</code></p>
<dd> Enable hypver <font SIZE="-1">VAPIC,</font> but disable spinlocks</p>
<dt><code>&#8211;features kvm_hidden=on</code></p>
<dd> Allow the <font SIZE="-1">KVM</font> hypervisor signature to be hidden from the guest</p>
<dt><code>&#8211;features pvspinlock=on</code></p>
<dd> Notify the guest that the host supports paravirtual spinlocks for example by exposing the pvticketlocks mechanism.</p>
<dt><code>&#8211;features gic_version=2</code></p>
<dd> This is relevant only for <font SIZE="-1">ARM</font> architectures. Possible values are &#8220;host&#8221; or version number.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Use &#8211;features=? to see a list of all available sub options. Complete details at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsFeatures">http://libvirt.org/formatdomain.html#elementsFeatures</a>&gt;</dl>
<dt><code>&#8211;clock</code> offset=OFFSET,TIMER_OPT=VAL,&#8230;</p>
<dd> Configure the guest&#8217;s &lt;clock&gt; <font SIZE="-1">XML.</font> Some supported options:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;clock offset=OFFSET</code></p>
<dd> Set the clock offset, ex. &#8216;utc&#8217; or &#8216;localtime&#8217;</p>
<dt><code>&#8211;clock TIMER_present=no</code></p>
<dd> Disable a boolean timer. <font SIZE="-1">TIMER</font> here might be hpet, kvmclock, etc.</p>
<dt><code>&#8211;clock TIMER_tickpolicy=VAL</code></p>
<dd> Set a timer&#8217;s tickpolicy value. <font SIZE="-1">TIMER</font> here might be rtc, pit, etc. <font SIZE="-1">VAL</font> might be catchup, delay, etc. Refer to the libvirt docs for all values.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Use &#8211;clock=? to see a list of all available sub options. Complete details at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsTime">http://libvirt.org/formatdomain.html#elementsTime</a>&gt;</dl>
<dt><code>&#8211;pm</code> <font SIZE="-1">OPTIONS</font></p>
<dd> Configure guest power management features. Example suboptions include suspend_to_mem=on|off and suspend_to_disk=on|off </p>
<p> Use &#8211;pm=? to see a list of all available sub options. Complete details at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsPowerManagement">http://libvirt.org/formatdomain.html#elementsPowerManagement</a>&gt;</dl>
<h2>INSTALLATION OPTIONS</h2>
<dl>
<dt><code>&#8211;cdrom</code> <font SIZE="-1">OPTIONS</font></p>
<dd> File or device used as a virtual CD-ROM device. It can be path to an <font SIZE="-1">ISO</font> image or a <font SIZE="-1">URL</font> from which to fetch/access a minimal boot <font SIZE="-1">ISO</font> image. The URLs take the same format as described for the <tt>&quot;--location&quot;</tt> argument. If a cdrom has been specified via the <tt>&quot;--disk&quot;</tt> option, and neither <tt>&quot;--cdrom&quot;</tt> nor any other install option is specified, the <tt>&quot;--disk&quot;</tt> cdrom is used as the install media.</p>
<dt><code>-l</code> <font SIZE="-1">LOCATION</font></p>
<dd>
<dt><code>&#8211;location</code> <font SIZE="-1">OPTIONS</font></p>
<dd> Distribution tree installation source. virt-install can recognize certain distribution trees and fetches a bootable kernel/initrd pair to launch the install. </p>
<p> With libvirt 0.9.4 or later, network <font SIZE="-1">URL</font> installs work for remote connections. virt-install will download kernel/initrd to the local machine, and then upload the media to the remote host. This option requires the <font SIZE="-1">URL</font> to be accessible by both the local and remote host. </p>
<p> &#8211;location allows things like &#8211;extra-args for kernel arguments, and using &#8211;initrd-inject. If you want to use those options with <font SIZE="-1">CDROM</font> media, you have a few options: </p>
<p> * Run virt-install as root and do &#8211;location <font SIZE="-1">ISO</font> </p>
<p> * Mount the <font SIZE="-1">ISO</font> at a local directory, and do &#8211;location <font SIZE="-1">DIRECTORY</font> </p>
<p> * Mount the <font SIZE="-1">ISO</font> at a local directory, export that directory over local http, and do &#8211;location <a rel="nofollow" href="http://localhost/DIRECTORY">http://localhost/DIRECTORY</a> </p>
<p> The <tt>&quot;LOCATION&quot;</tt> can take one of the following forms:</p>
<dl>
<dt>
<dd>
<dl>
<dt><a rel="nofollow" href="http://host/path">http://host/path</a></p>
<dd> An <font SIZE="-1">HTTP</font> server location containing an installable distribution image.</p>
<dt><a href="ftp://host/path">ftp://host/path</a></p>
<dd> An <font SIZE="-1">FTP</font> server location containing an installable distribution image.</p>
<dt>nfs:host:/path or <a href="nfs://host/path">nfs://host/path</a></p>
<dd> An <font SIZE="-1">NFS</font> server location containing an installable distribution image. This requires running virt-install as root.</p>
<dt><font SIZE="-1">DIRECTORY</font></p>
<dd> Path to a local directory containing an installable distribution image. Note that the directory will not be accessible by the guest after initial boot, so the <font SIZE="-1">OS</font> installer will need another way to access the rest of the install media.</p>
<dt><font SIZE="-1">ISO</font></p>
<dd> Mount the <font SIZE="-1">ISO</font> and probe the directory. This requires running virt-install as root, and has the same <font SIZE="-1">VM</font> access caveat as <font SIZE="-1">DIRECTORY.</font></dl>
</dl>
<dl>
<dt>
<dd>
<p> Some distro specific url samples:</p>
<dl>
<dt>Fedora/Red Hat Based</p>
<dd> <a rel="nofollow" href="http://download.fedoraproject.org/pub/fedora/linux/releases/21/Server/x86_64/os">http://download.fedoraproject.org/pub/fedora/linux/releases/21/Server/x86_64/os</a></p>
<dt>Debian</p>
<dd> <a rel="nofollow" href="http://ftp.us.debian.org/debian/dists/stable/main/installer-amd64/">http://ftp.us.debian.org/debian/dists/stable/main/installer-amd64/</a></p>
<dt>Ubuntu</p>
<dd> <a rel="nofollow" href="http://us.archive.ubuntu.com/ubuntu/dists/wily/main/installer-amd64/">http://us.archive.ubuntu.com/ubuntu/dists/wily/main/installer-amd64/</a></p>
<dt>Suse</p>
<dd> <a rel="nofollow" href="http://download.opensuse.org/distribution/11.0/repo/oss/">http://download.opensuse.org/distribution/11.0/repo/oss/</a></p>
<dt>Mandriva</p>
<dd> <a href="ftp://ftp.uwsg.indiana.edu/linux/mandrake/official/2009.0/i586/">ftp://ftp.uwsg.indiana.edu/linux/mandrake/official/2009.0/i586/</a></p>
<dt>Mageia</p>
<dd> <a href="ftp://distrib-coffee.ipsl.jussieu.fr/pub/linux/Mageia/distrib/1">ftp://distrib-coffee.ipsl.jussieu.fr/pub/linux/Mageia/distrib/1</a></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;pxe</code></p>
<dd> Use the <font SIZE="-1">PXE</font> boot protocol to load the initial ramdisk and kernel for starting the guest installation process.</p>
<dt><code>&#8211;import</code></p>
<dd> Skip the <font SIZE="-1">OS</font> installation process, and build a guest around an existing disk image. The device used for booting is the first device specified via <tt>&quot;--disk&quot;</tt> or <tt>&quot;--filesystem&quot;</tt>.</p>
<dt><code>&#8211;livecd</code></p>
<dd> Specify that the installation media is a live <font SIZE="-1">CD</font> and thus the guest needs to be configured to boot off the <font SIZE="-1">CDROM</font> device permanently. It may be desirable to also use the <tt>&quot;--disk none&quot;</tt> flag in combination.</p>
<dt><code>-x</code> <font SIZE="-1">EXTRA</font></p>
<dd>
<dt><code>&#8211;extra-args</code> <font SIZE="-1">OPTIONS</font></p>
<dd> Additional kernel command line arguments to pass to the installer when performing a guest install from <tt>&quot;--location&quot;</tt>. One common usage is specifying an anaconda kickstart file for automated installs, such as &#8211;extra-args &#8220;ks=<a rel="nofollow" href="http://myserver/my.ks''">http://myserver/my.ks&#8221;</a></p>
<dt><code>&#8211;initrd-inject</code> <font SIZE="-1">PATH</font></p>
<dd> Add <font SIZE="-1">PATH</font> to the root of the initrd fetched with <tt>&quot;--location&quot;</tt>. This can be used to run an automated install without requiring a network hosted kickstart file: </p>
<p> &#8211;initrd-inject=/path/to/my.ks &#8211;extra-args &#8220;ks=file:/my.ks&#8221;</p>
<dt><code>&#8211;os-variant</code> <font SIZE="-1">OS_VARIANT</font></p>
<dd> Optimize the guest configuration for a specific operating system (ex. &#8216;fedora18&#8217;, &#8216;rhel7&#8217;, &#8216;winxp&#8217;). While not required, specifying this options is <font SIZE="-1">HIGHLY RECOMMENDED,</font> as it can greatly increase performance by specifying virtio among other guest tweaks. </p>
<p> By default, virt-install will attempt to auto detect this value from the install media (currently only supported for <font SIZE="-1">URL</font> installs). Autodetection can be disabled with the special value &#8216;none&#8217;. Autodetection can be forced with the special value &#8216;auto&#8217;. </p>
<p> Use the command &#8220;osinfo-query os&#8221; to get the list of the accepted <font SIZE="-1">OS</font> variants.</p>
<dt><code>&#8211;boot</code> <font SIZE="-1">BOOTOPTS</font></p>
<dd> Optionally specify the post-install <font SIZE="-1">VM</font> boot configuration. This option allows specifying a boot device order, permanently booting off kernel/initrd with option kernel arguments, and enabling a <font SIZE="-1">BIOS</font> boot menu (requires libvirt 0.8.3 or later) </p>
<p> &#8211;boot can be specified in addition to other install options (such as &#8211;location, &#8211;cdrom, etc.) or can be specified on its own. In the latter case, behavior is similar to the &#8211;import install option: there is no &#8216;install&#8217; phase, the guest is just created and launched as specified. </p>
<p> Some examples:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;boot cdrom,fd,hd,network,menu=on</code></p>
<dd> Set the boot device priority as first cdrom, first floppy, first harddisk, network <font SIZE="-1">PXE</font> boot. Additionally enable <font SIZE="-1">BIOS</font> boot menu prompt.</p>
<dt><code>&#8211;boot kernel=KERNEL,initrd=INITRD,kernel_args=&quot;console=/dev/ttyS0&quot;</code></p>
<dd> Have guest permanently boot off a local kernel/initrd pair, with the specified kernel options.</p>
<dt><code>&#8211;boot kernel=KERNEL,initrd=INITRD,dtb=DTB</code></p>
<dd> Have guest permanently boot off a local kernel/initrd pair with an external device tree binary. <font SIZE="-1">DTB</font> can be required for some non-x86 configurations like <font SIZE="-1">ARM</font> or <font SIZE="-1">PPC</font></p>
<dt><code>&#8211;boot loader=BIOSPATH</code></p>
<dd> Use <font SIZE="-1">BIOSPATH</font> as the virtual machine <font SIZE="-1">BIOS.</font></p>
<dt><code>&#8211;boot menu=on,useserial=on</code></p>
<dd> Enable the bios boot menu, and enable sending bios text output over serial console.</p>
<dt><code>&#8211;boot init=INITPATH</code></p>
<dd> Path to a binary that the container guest will init. If a root <tt>&quot;--filesystem&quot;</tt> has been specified, virt-install will default to /sbin/init, otherwise will default to /bin/sh.</p>
<dt><code>&#8211;boot uefi</code></p>
<dd> Configure the <font SIZE="-1">VM</font> to boot from <font SIZE="-1">UEFI.</font> In order for virt-install to know the correct <font SIZE="-1">UEFI</font> parameters, libvirt needs to be advertising known <font SIZE="-1">UEFI</font> binaries via domcapabilities <font SIZE="-1">XML,</font> so this will likely only work if using properly configured distro packages.</p>
<dt><code>&#8211;boot loader=/&#8230;/OVMF_CODE.fd,loader_ro=yes,loader_type=pflash,nvram_template=/&#8230;/OVMF_VARS.fd</code></p>
<dd> Specify that the virtual machine use the custom <font SIZE="-1">OVMF</font> binary as boot firmware, mapped as a virtual flash chip. In addition, request that libvirt instantiate the VM-specific <font SIZE="-1">UEFI</font> varstore from the custom &#8220;/&#8230;/OVMF_VARS.fd&#8221; varstore template. This is the recommended <font SIZE="-1">UEFI</font> setup, and should be used if &#8211;boot uefi doesn&#8217;t know about your <font SIZE="-1">UEFI</font> binaries.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Use &#8211;boot=? to see a list of all available sub options. Complete details at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsOS">http://libvirt.org/formatdomain.html#elementsOS</a>&gt;</dl>
<dt><code>&#8211;idmap</code> <font SIZE="-1">OPTIONS</font></p>
<dd> If the guest configuration declares a <font SIZE="-1">UID</font> or <font SIZE="-1">GID</font> mapping, the &#8216;user&#8217; namespace will be enabled to apply these. A suitably configured <font SIZE="-1">UID/GID</font> mapping is a pre-requisite to make containers secure, in the absence of sVirt confinement. </p>
<p> &#8211;idmap can be specified to enable user namespace for <font SIZE="-1">LXC</font> containers </p>
<p> Example:<br />
&nbsp;<wbr>&#8211;idmap uid_start=0,uid_target=1000,uid_count=10,gid_start=0,gid_target=1000,gid_count=10 </p>
<p> Use &#8211;idmap=? to see a list of all available sub options. Complete details at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsOSContainer">http://libvirt.org/formatdomain.html#elementsOSContainer</a>&gt;</dl>
<h2>STORAGE OPTIONS</h2>
<dl>
<dt><code>&#8211;disk</code> <font SIZE="-1">OPTIONS</font></p>
<dd> Specifies media to use as storage for the guest, with various options. The general format of a disk string is </p>
<pre>
    --disk opt1=val1,opt2=val2,...
</pre>
<p> The simplest invocation to create a new 10G disk image and associated disk device: </p>
<pre>
    --disk size=10
</pre>
<p> virt-install will generate a path name, and place it in the default image location for the hypervisor. To specify media, the command can either be: </p>
<pre>
    --disk /some/storage/path[,opt1=val1]...
</pre>
<p> or explicitly specify one of the following arguments:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>path</code></p>
<dd> A path to some storage media to use, existing or not. Existing media can be a file or block device. </p>
<p> Specifying a non-existent path implies attempting to create the new storage, and will require specifying a &#8216;size&#8217; value. Even for remote hosts, virt-install will try to use libvirt storage APIs to automatically create the given path. </p>
<p> If the hypervisor supports it, <code>path</code> can also be a network <font SIZE="-1">URL,</font> like <a rel="nofollow" href="http://example.com/some-disk.img">http://example.com/some-disk.img</a> . For network paths, they hypervisor will directly access the storage, nothing is downloaded locally.</p>
<dt><code>pool</code></p>
<dd> An existing libvirt storage pool name to create new storage on. Requires specifying a &#8216;size&#8217; value.</p>
<dt><code>vol</code></p>
<dd> An existing libvirt storage volume to use. This is specified as &#8216;poolname/volname&#8217;.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Other available options:</p>
<dl>
<dt><code>device</code></p>
<dd> Disk device type. Value can be &#8216;cdrom&#8217;, &#8216;disk&#8217;, &#8216;lun&#8217; or &#8216;floppy&#8217;. Default is &#8216;disk&#8217;. If a &#8216;cdrom&#8217; is specified, and no install method is chosen, the cdrom is used as the install media.</p>
<dt><code>boot_order</code></p>
<dd> Guest installation with multiple disks will need this parameter to boot correctly after being installed. A boot_order parameter will take values 1,2,3,&#8230; Devices with lower value has higher priority.</p>
<dt><code>bus</code></p>
<dd> Disk bus type. Value can be &#8216;ide&#8217;, &#8216;sata&#8217;, &#8216;scsi&#8217;, &#8216;usb&#8217;, &#8216;virtio&#8217; or &#8216;xen&#8217;. The default is hypervisor dependent since not all hypervisors support all bus types.</p>
<dt><code>removable</code></p>
<dd> Sets the removable flag (/sys/block/$dev/removable on Linux). Only used with <font SIZE="-1">QEMU</font> and bus=usb. Value can be &#8216;on&#8217; or &#8216;off&#8217;.</p>
<dt><code>readonly</code></p>
<dd> Set drive as readonly (takes &#8216;on&#8217; or &#8216;off&#8217;)</p>
<dt><code>shareable</code></p>
<dd> Set drive as shareable (takes &#8216;on&#8217; or &#8216;off&#8217;)</p>
<dt><code>size</code></p>
<dd> size (in GiB) to use if creating new storage</p>
<dt><code>sparse</code></p>
<dd> whether to skip fully allocating newly created storage. Value is &#8216;yes&#8217; or &#8216;no&#8217;. Default is &#8216;yes&#8217; (do not fully allocate) unless it isn&#8217;t supported by the underlying storage type. </p>
<p> The initial time taken to fully-allocate the guest virtual disk (sparse=no) will be usually balanced by faster install times inside the guest. Thus use of this option is recommended to ensure consistently high performance and to avoid I/O errors in the guest should the host filesystem fill up.</p>
<dt><code>backing_store</code></p>
<dd> Path to a disk to use as the backing store for the newly created image.</p>
<dt><code>backing_format</code></p>
<dd> Disk image format of <code>backing_store</code></p>
<dt><code>cache</code></p>
<dd> The cache mode to be used. The host pagecache provides cache memory. The cache value can be &#8216;none&#8217;, &#8216;writethrough&#8217;, &#8216;directsync&#8217;, &#8216;unsafe&#8217; or &#8216;writeback&#8217;. &#8216;writethrough&#8217; provides read caching. &#8216;writeback&#8217; provides read and write caching. &#8216;directsync&#8217; bypasses the host page cache. &#8216;unsafe&#8217; may cache all content and ignore flush requests from the guest.</p>
<dt><code>discard</code></p>
<dd> Whether discard (also known as &#8220;trim&#8221; or &#8220;unmap&#8221;) requests are ignored or passed to the filesystem. The value can be either &#8220;unmap&#8221; (allow the discard request to be passed) or &#8220;ignore&#8221; (ignore the discard request). Since 1.0.6 (<font SIZE="-1">QEMU</font> and <font SIZE="-1">KVM</font> only)</p>
<dt><code>format</code></p>
<dd> Disk image format. For file volumes, this can be &#8216;raw&#8217;, &#8216;qcow2&#8217;, &#8216;vmdk&#8217;, etc. See format types in &lt;<a rel="nofollow" href="http://libvirt.org/storage.html">http://libvirt.org/storage.html</a>&gt; for possible values. This is often mapped to the <code>driver_type</code> value as well. </p>
<p> If not specified when creating file images, this will default to &#8216;qcow2&#8217;. </p>
<p> If creating storage, this will be the format of the new image. If using an existing image, this overrides libvirt&#8217;s format auto-detection.</p>
<dt><code>driver_name</code></p>
<dd> Driver name the hypervisor should use when accessing the specified storage. Typically does not need to be set by the user.</p>
<dt><code>driver_type</code></p>
<dd> Driver format/type the hypervisor should use when accessing the specified storage. Typically does not need to be set by the user.</p>
<dt><code>io</code></p>
<dd> Disk <font SIZE="-1">IO</font> backend. Can be either &#8220;threads&#8221; or &#8220;native&#8221;.</p>
<dt><code>error_policy</code></p>
<dd> How guest should react if a write error is encountered. Can be one of &#8220;stop&#8221;, &#8220;ignore&#8221;, or &#8220;enospace&#8221;</p>
<dt><code>serial</code></p>
<dd> Serial number of the emulated disk device. This is used in linux guests to set /dev/disk/by-id symlinks. An example serial number might be: <font SIZE="-1">WD-WMAP9A966149</font></p>
<dt><code>startup_policy</code></p>
<dd> It defines what to do with the disk if the source file is not accessible. See possible values in &lt;<a rel="nofollow" href="http://www.libvirt.org/formatdomain.html#elementsDisks">http://www.libvirt.org/formatdomain.html#elementsDisks</a>&gt;</dl>
</dl>
<dl>
<dt>
<dd>
<p> See the examples section for some uses. This option deprecates -f/&#8211;file, -s/&#8211;file-size, &#8211;nonsparse, and &#8211;nodisks. </p>
<p> Use &#8211;disk=? to see a list of all available sub options. Complete details at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsDisks">http://libvirt.org/formatdomain.html#elementsDisks</a>&gt;</dl>
<dt><code>&#8211;filesystem</code></p>
<dd> Specifies a directory on the host to export to the guest. The most simple invocation is: </p>
<pre>
    --filesystem /source/on/host,/target/point/in/guest
</pre>
<p> Which will work for recent <font SIZE="-1">QEMU</font> and linux guest <font SIZE="-1">OS</font> or <font SIZE="-1">LXC</font> containers. For <font SIZE="-1">QEMU,</font> the target point is just a mounting hint in sysfs, so will not be automatically mounted. </p>
<p> The following explicit options can be specified:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>type</code></p>
<dd> The type or the source directory. Valid values are &#8216;mount&#8217; (the default) or &#8216;template&#8217; for OpenVZ templates.</p>
<dt><code>mode</code></p>
<dd> The access mode for the source directory from the guest <font SIZE="-1">OS.</font> Only used with <font SIZE="-1">QEMU</font> and type=mount. Valid modes are &#8216;passthrough&#8217; (the default), &#8216;mapped&#8217;, or &#8216;squash&#8217;. See libvirt domain <font SIZE="-1">XML</font> documentation for more info.</p>
<dt><code>source</code></p>
<dd> The directory on the host to share.</p>
<dt><code>target</code></p>
<dd> The mount location to use in the guest.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Use &#8211;filesystem=? to see a list of all available sub options. Complete details at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsFilesystems">http://libvirt.org/formatdomain.html#elementsFilesystems</a>&gt;</dl>
</dl>
<h2>NETWORKING OPTIONS</h2>
<dl>
<dt><code>-w</code> <font SIZE="-1">OPTIONS</font></p>
<dd>
<dt><code>&#8211;network</code> <font SIZE="-1">OPTIONS</font></p>
<dd> Connect the guest to the host network. The value for <tt>&quot;NETWORK&quot;</tt> can take one of 4 formats:</p>
<dl>
<dt>
<dd>
<dl>
<dt>bridge=BRIDGE</p>
<dd> Connect to a bridge device in the host called <tt>&quot;BRIDGE&quot;</tt>. Use this option if the host has static networking config &amp; the guest requires full outbound and inbound connectivity to/from the <font SIZE="-1">LAN.</font> Also use this if live migration will be used with this guest.</p>
<dt>network=NAME</p>
<dd> Connect to a virtual network in the host called <tt>&quot;NAME&quot;</tt>. Virtual networks can be listed, created, deleted using the <tt>&quot;virsh&quot;</tt> command line tool. In an unmodified install of <tt>&quot;libvirt&quot;</tt> there is usually a virtual network with a name of <tt>&quot;default&quot;</tt>. Use a virtual network if the host has dynamic networking (eg NetworkManager), or using wireless. The guest will be NATed to the <font SIZE="-1">LAN</font> by whichever connection is active.</p>
<dt>type=direct,source=IFACE[,source_mode=MODE]</p>
<dd> Direct connect to host interface <font SIZE="-1">IFACE</font> using macvtap.</p>
<dt>user</p>
<dd> Connect to the <font SIZE="-1">LAN</font> using <font SIZE="-1">SLIRP.</font> Only use this if running a <font SIZE="-1">QEMU</font> guest as an unprivileged user. This provides a very limited form of <font SIZE="-1">NAT.</font></p>
<dt>none</p>
<dd> Tell virt-install not to add any default network interface.</dl>
</dl>
<dl>
<dt>
<dd>
<p> If this option is omitted a single <font SIZE="-1">NIC</font> will be created in the guest. If there is a bridge device in the host with a physical interface enslaved, that will be used for connectivity. Failing that, the virtual network called <tt>&quot;default&quot;</tt> will be used. This option can be specified multiple times to setup more than one <font SIZE="-1">NIC.</font> </p>
<p> Other available options are:</p>
<dl>
<dt><code>model</code></p>
<dd> Network device model as seen by the guest. Value can be any nic model supported by the hypervisor, e.g.: &#8216;e1000&#8217;, &#8216;rtl8139&#8217;, &#8216;virtio&#8217;, &#8230;</p>
<dt><code>mac</code></p>
<dd> Fixed <font SIZE="-1">MAC</font> address for the guest; If this parameter is omitted, or the value <tt>&quot;RANDOM&quot;</tt> is specified a suitable address will be randomly generated. For Xen virtual machines it is required that the first 3 pairs in the <font SIZE="-1">MAC</font> address be the sequence &#8217;00:16:3e&#8217;, while for <font SIZE="-1">QEMU</font> or <font SIZE="-1">KVM</font> virtual machines it must be &#8217;52:54:00&#8242;.</p>
<dt><code>filterref</code></p>
<dd> Controlling firewall and network filtering in libvirt. Value can be any nwfilter defined by the <tt>&quot;virsh&quot;</tt> &#8216;nwfilter&#8217; subcommands. Available filters can be listed by running &#8216;virsh nwfilter-list&#8217;, e.g.: &#8216;clean-traffic&#8217;, &#8216;no-mac-spoofing&#8217;, &#8230;</p>
<dt><code>virtualport_type</code></p>
<dd> The type of virtual port profile, one the following values</p>
<dl>
<dt>
<dd>
<dl>
<dt>&quot;802.Qbg&quot;</p>
<dd> The following additional parameters are accepted</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>virtualport_managerid</code></p>
<dd> The <font SIZE="-1">VSI</font> Manager <font SIZE="-1">ID</font> identifies the database containing the <font SIZE="-1">VSI</font> type and instance definitions. This is an integer value and the value 0 is reserved.</p>
<dt><code>virtualport_typeid</code></p>
<dd> The <font SIZE="-1">VSI</font> Type <font SIZE="-1">ID</font> identifies a <font SIZE="-1">VSI</font> type characterizing the network access. <font SIZE="-1">VSI</font> types are typically managed by network administrator. This is an integer value.</p>
<dt><code>virtualport_typeidversion</code></p>
<dd> The <font SIZE="-1">VSI</font> Type Version allows multiple versions of a <font SIZE="-1">VSI</font> Type. This is an integer value.</p>
<dt><code>virtualport_instanceid</code></p>
<dd> The <font SIZE="-1">VSI</font> Instance <font SIZE="-1">ID</font> Identifier is generated when a <font SIZE="-1">VSI</font> instance (i.e. a virtual interface of a virtual machine) is created. This is a globally unique identifier.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&quot;802.Qbh&quot;</p>
<dd> The following additional parameters are accepted</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>virtualport_profileid</code></p>
<dd> The profile <font SIZE="-1">ID</font> contains the name of the port profile that is to be applied to this interface. This name is resolved by the port profile database into the network parameters from the port profile, and those network parameters will be applied to this interface.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&quot;openvswitch&quot;</p>
<dd> The following additional parameters are accepted</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>virtualport_profileid</code></p>
<dd> The OpenVSwitch port profile for the interface</p>
<dt><code>virtualport_interfaceid</code></p>
<dd> A <font SIZE="-1">UUID</font> to uniquely identify the interface. If omitted one will be generated automatically</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&quot;midonet&quot;</p>
<dd> The following additional parameters are accepted</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>virtualport_interfaceid</code></p>
<dd> A <font SIZE="-1">UUID</font> identifying the port in the network to which the interface will be bound</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
</dl>
<dl>
<dt>
<dd>
<p> Use &#8211;network=? to see a list of all available sub options. Complete details at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsNICS">http://libvirt.org/formatdomain.html#elementsNICS</a>&gt; </p>
<p> This option deprecates -m/&#8211;mac, -b/&#8211;bridge, and &#8211;nonetworks</dl>
</dl>
<h2>GRAPHICS OPTIONS</h2>
<p> If no graphics option is specified, <tt>&quot;virt-install&quot;</tt> will try to select the appropriate graphics if the <font SIZE="-1">DISPLAY</font> environment variable is set, otherwise &#8216;&#8211;graphics none&#8217; is used.</p>
<dl>
<dt><code>&#8211;graphics</code> <font SIZE="-1">TYPE</font>,opt1=arg1,opt2=arg2,&#8230;</p>
<dd> Specifies the graphical display configuration. This does not configure any virtual hardware, just how the guest&#8217;s graphical display can be accessed. Typically the user does not need to specify this option, virt-install will try and choose a useful default, and launch a suitable connection. </p>
<p> General format of a graphical string is </p>
<pre>
    --graphics TYPE,opt1=arg1,opt2=arg2,...
</pre>
<p> For example: </p>
<pre>
    --graphics vnc,password=foobar
</pre>
<p> The supported options are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>type</code></p>
<dd> The display type. This is one of: </p>
<p> vnc </p>
<p> Setup a virtual console in the guest and export it as a <font SIZE="-1">VNC</font> server in the host. Unless the <tt>&quot;port&quot;</tt> parameter is also provided, the <font SIZE="-1">VNC</font> server will run on the first free port number at 5900 or above. The actual <font SIZE="-1">VNC</font> display allocated can be obtained using the <tt>&quot;vncdisplay&quot;</tt> command to <tt>&quot;virsh&quot;</tt> (or <i><a href="/docs/linux/man/1-virt-viewer/">virt-viewer</a></i>(1) can be used which handles this detail for the use). </p>
<p> spice </p>
<p> Export the guest&#8217;s console using the Spice protocol. Spice allows advanced features like audio and <font SIZE="-1">USB</font> device streaming, as well as improved graphical performance. </p>
<p> Using spice graphic type will work as if those arguments were given: </p>
<pre>
    --video qxl --channel spicevmc
</pre>
<p> none </p>
<p> No graphical console will be allocated for the guest. Guests will likely need to have a text console configured on the first serial port in the guest (this can be done via the &#8211;extra-args option). The command &#8216;virsh console <font SIZE="-1">NAME</font>&#8216; can be used to connect to the serial device.</p>
<dt><code>port</code></p>
<dd> Request a permanent, statically assigned port number for the guest console. This is used by &#8216;vnc&#8217; and &#8216;spice&#8217;</p>
<dt><code>tlsport</code></p>
<dd> Specify the spice tlsport.</p>
<dt><code>listen</code></p>
<dd> Address to listen on for VNC/Spice connections. Default is typically 127.0.0.1 (localhost only), but some hypervisors allow changing this globally (for example, the qemu driver default can be changed in /etc/libvirt/qemu.conf). Use 0.0.0.0 to allow access from other machines. </p>
<p> Use &#8216;none&#8217; to specify that the display server should not listen on any port. The display server can be accessed only locally through libvirt unix socket (virt-viewer with &#8211;attach for instance). </p>
<p> Use &#8216;socket&#8217; to have the <font SIZE="-1">VM</font> listen on a libvirt generated unix socket path on the host filesystem. </p>
<p> This is used by &#8216;vnc&#8217; and &#8216;spice&#8217;</p>
<dt><code>keymap</code></p>
<dd> Request that the virtual <font SIZE="-1">VNC</font> console be configured to run with a specific keyboard layout. If the special value &#8216;local&#8217; is specified, virt-install will attempt to configure to use the same keymap as the local system. A value of &#8216;none&#8217; specifically defers to the hypervisor. Default behavior is hypervisor specific, but typically is the same as &#8216;local&#8217;. This is used by &#8216;vnc&#8217;</p>
<dt><code>password</code></p>
<dd> Request a <font SIZE="-1">VNC</font> password, required at connection time. Beware, this info may end up in virt-install log files, so don&#8217;t use an important password. This is used by &#8216;vnc&#8217; and &#8216;spice&#8217;</p>
<dt><code>gl</code></p>
<dd> Whether to use OpenGl accelerated rendering. Value is &#8216;yes&#8217; or &#8216;no&#8217;. This is used by &#8216;spice&#8217;.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Use &#8211;graphics=? to see a list of all available sub options. Complete details at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsGraphics">http://libvirt.org/formatdomain.html#elementsGraphics</a>&gt; </p>
<p> This deprecates the following options: &#8211;vnc, &#8211;vncport, &#8211;vnclisten, -k/&#8211;keymap, &#8211;sdl, &#8211;nographics</dl>
<dt><code>&#8211;noautoconsole</code></p>
<dd> Don&#8217;t automatically try to connect to the guest console. The default behaviour is to launch <i><a href="/docs/linux/man/1-virt-viewer/">virt-viewer</a></i>(1) to display the graphical console, or to run the <tt>&quot;virsh&quot;</tt> <tt>&quot;console&quot;</tt> command to display the text console. Use of this parameter will disable this behaviour.</dl>
<h2>VIRTUALIZATION OPTIONS</h2>
<p> Options to override the default virtualization type choices.</p>
<dl>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;hvm</code></p>
<dd> Request the use of full virtualization, if both para &amp; full virtualization are available on the host. This parameter may not be available if connecting to a Xen hypervisor on a machine without hardware virtualization support. This parameter is implied if connecting to a <font SIZE="-1">QEMU</font> based hypervisor.</p>
<dt><code>-p</code></p>
<dd>
<dt><code>&#8211;paravirt</code></p>
<dd> This guest should be a paravirtualized guest. If the host supports both para &amp; full virtualization, and neither this parameter nor the <tt>&quot;--hvm&quot;</tt> are specified, this will be assumed.</p>
<dt><code>&#8211;container</code></p>
<dd> This guest should be a container type guest. This option is only required if the hypervisor supports other guest types as well (so for example this option is the default behavior for <font SIZE="-1">LXC</font> and OpenVZ, but is provided for completeness).</p>
<dt><code>&#8211;virt-type</code></p>
<dd> The hypervisor to install on. Example choices are kvm, qemu, or xen. Available options are listed via &#8216;virsh capabilities&#8217; in the &lt;domain&gt; tags. </p>
<p> This deprecates the &#8211;accelerate option, which is now the default behavior. To install a plain <font SIZE="-1">QEMU</font> guest, use &#8216;&#8211;virt-type qemu&#8217;</dl>
<h2>DEVICE OPTIONS</h2>
<p> All devices have a set of <code>address.*</code> options for configuring the particulars of the device&#8217;s address on its parent controller or bus. See <tt>&quot;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsAddress">http://libvirt.org/formatdomain.html#elementsAddress</a>&quot;</tt> for details.</p>
<dl>
<dt><code>&#8211;controller</code> <font SIZE="-1">OPTIONS</font></p>
<dd> Attach a controller device to the guest. <font SIZE="-1">TYPE</font> is one of: <code>ide</code>, <code>fdc</code>, <code>scsi</code>, <code>sata</code>, <code>virtio-serial</code>, or <code>usb</code>. </p>
<p> Controller also supports the special values <code>usb2</code> and <code>usb3</code> to specify which version of the <font SIZE="-1">USB</font> controller should be used (version 2 or 3).</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>model</code></p>
<dd> Controller model. These may vary according to the hypervisor and its version. Most commonly used models are e.g. <code>auto</code>, <code>virtio-scsi</code> for the <code>scsi</code> controller, <code>ehci</code> or <code>none</code> for the <code>usb</code> controller. For full list and further details on controllers/models, see <tt>&quot;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsControllers">http://libvirt.org/formatdomain.html#elementsControllers</a>&quot;</tt>.</p>
<dt><code>address</code></p>
<dd> Shorthand for setting a manual <font SIZE="-1">PCI</font> address from an lscpi style string. The preferred method for setting this is using the address.* parameters.</p>
<dt><code>index</code></p>
<dd> A decimal integer describing in which order the bus controller is encountered, and to reference the controller bus.</p>
<dt><code>master</code></p>
<dd> Applicable to <font SIZE="-1">USB</font> companion controllers, to define the master bus startport.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Examples:</p>
<dl>
<dt><code>&#8211;controller usb,model=ich9-ehci1,address=0:0:4.0,index=0</code></p>
<dd> Adds a <font SIZE="-1">ICH9 EHCI1 USB</font> controller on <font SIZE="-1">PCI</font> address 0:0:4.0</p>
<dt><code>&#8211;controller usb,model=ich9-uhci2,address=0:0:4.7,index=0,master=2</code></p>
<dd> Adds a <font SIZE="-1">ICH9 UHCI2 USB</font> companion controller for the previous master controller, ports start from port number 2. </p>
<p> The parameter multifunction=&#8217;on&#8217; will be added automatically to the proper device (if needed). This applies to all <font SIZE="-1">PCI</font> devices.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Use &#8211;controller=? to see a list of all available sub options. Complete details at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsControllers">http://libvirt.org/formatdomain.html#elementsControllers</a>&gt;</dl>
<dt><code>&#8211;input</code> <font SIZE="-1">OPTIONS</font></p>
<dd> Attach an input device to the guest. Example input device types are mouse, tablet, or keyboard. </p>
<p> Use &#8211;input=? to see a list of all available sub options. Complete details at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsInput">http://libvirt.org/formatdomain.html#elementsInput</a>&gt;</p>
<dt><code>&#8211;hostdev</code> <font SIZE="-1">OPTIONS</font></p>
<dd>
<dt><code>&#8211;host-device</code> <font SIZE="-1">OPTIONS</font></p>
<dd> Attach a physical host device to the guest. Some example values for <font SIZE="-1">HOSTDEV:</font></p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;hostdev pci_0000_00_1b_0</code></p>
<dd> A node device name via libvirt, as shown by &#8216;virsh nodedev-list&#8217;</p>
<dt><code>&#8211;hostdev 001.003</code></p>
<dd> <font SIZE="-1">USB</font> by bus, device (via lsusb).</p>
<dt><code>&#8211;hostdev 0x1234:0x5678</code></p>
<dd> <font SIZE="-1">USB</font> by vendor, product (via lsusb).</p>
<dt><code>&#8211;hostdev 1f.01.02</code></p>
<dd> <font SIZE="-1">PCI</font> device (via lspci).</dl>
</dl>
<dl>
<dt>
<dd>
<p> Use &#8211;hostdev=? to see a list of all available sub options. Complete details at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsHostDev">http://libvirt.org/formatdomain.html#elementsHostDev</a>&gt;</dl>
<dt><code>&#8211;sound</code> <font SIZE="-1">MODEL</font></p>
<dd> Attach a virtual audio device to the guest. <font SIZE="-1">MODEL</font> specifies the emulated sound card model. Possible values are ich6, ich9, ac97, es1370, sb16, pcspk, or default. &#8216;default&#8217; will try to pick the best model that the specified <font SIZE="-1">OS</font> supports. </p>
<p> This deprecates the old &#8211;soundhw option. </p>
<p> Use &#8211;sound=? to see a list of all available sub options. Complete details at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsSound">http://libvirt.org/formatdomain.html#elementsSound</a>&gt;</p>
<dt><code>&#8211;watchdog</code> MODEL[,action=ACTION]</p>
<dd> Attach a virtual hardware watchdog device to the guest. This requires a daemon and device driver in the guest. The watchdog fires a signal when the virtual machine appears to hung. <font SIZE="-1">ACTION</font> specifies what libvirt will do when the watchdog fires. Values are</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>reset</code></p>
<dd> Forcefully reset the guest (the default)</p>
<dt><code>poweroff</code></p>
<dd> Forcefully power off the guest</p>
<dt><code>pause</code></p>
<dd> Pause the guest</p>
<dt><code>none</code></p>
<dd> Do nothing</p>
<dt><code>shutdown</code></p>
<dd> Gracefully shutdown the guest (not recommended, since a hung guest probably won&#8217;t respond to a graceful shutdown)</dl>
</dl>
<dl>
<dt>
<dd>
<p> <font SIZE="-1">MODEL</font> is the emulated device model: either i6300esb (the default) or ib700. Some examples: </p>
<p> Use the recommended settings: </p>
<p> &#8211;watchdog default </p>
<p> Use the i6300esb with the &#8216;poweroff&#8217; action </p>
<p> &#8211;watchdog i6300esb,action=poweroff </p>
<p> Use &#8211;watchdog=? to see a list of all available sub options. Complete details at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsWatchdog">http://libvirt.org/formatdomain.html#elementsWatchdog</a>&gt;</dl>
<dt><code>&#8211;parallel</code> <font SIZE="-1">OPTIONS</font></p>
<dd>
<dt><code>&#8211;serial</code> <font SIZE="-1">OPTIONS</font></p>
<dd> Specifies a serial device to attach to the guest, with various options. The general format of a serial string is </p>
<pre>
    --serial type,opt1=val1,opt2=val2,...
</pre>
<p> &#8211;serial and &#8211;parallel devices share all the same options, unless otherwise noted. Some of the types of character device redirection are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;serial pty</code></p>
<dd> Pseudo <font SIZE="-1">TTY.</font> The allocated pty will be listed in the running guests <font SIZE="-1">XML</font> description.</p>
<dt><code>&#8211;serial dev,path=HOSTPATH</code></p>
<dd> Host device. For serial devices, this could be /dev/ttyS0. For parallel devices, this could be /dev/parport0.</p>
<dt><code>&#8211;serial file,path=FILENAME</code></p>
<dd> Write output to <font SIZE="-1">FILENAME.</font></p>
<dt><code>&#8211;serial pipe,path=PIPEPATH</code></p>
<dd> Named pipe (see <i><a href="/docs/linux/man/7-pipe/">pipe</a></i>(7))</p>
<dt><code>&#8211;serial tcp,host=HOST:PORT,mode=MODE,protocol=PROTOCOL</code></p>
<dd> <font SIZE="-1">TCP</font> net console. <font SIZE="-1">MODE</font> is either &#8216;bind&#8217; (wait for connections on <font SIZE="-1">HOST:PORT</font>) or &#8216;connect&#8217; (send output to <font SIZE="-1">HOST:PORT</font>), default is &#8216;bind&#8217;. <font SIZE="-1">HOST</font> defaults to &#8216;127.0.0.1&#8217;, but <font SIZE="-1">PORT</font> is required. <font SIZE="-1">PROTOCOL</font> can be either &#8216;raw&#8217; or &#8216;telnet&#8217; (default &#8216;raw&#8217;). If &#8216;telnet&#8217;, the port acts like a telnet server or client. Some examples: </p>
<p> Wait for connections on any address, port 4567: </p>
<p> &#8211;serial tcp,host=0.0.0.0:4567 </p>
<p> Connect to localhost, port 1234: </p>
<p> &#8211;serial tcp,host=:1234,mode=connect </p>
<p> Wait for telnet connection on localhost, port 2222. The user could then connect interactively to this console via &#8216;telnet localhost 2222&#8217;: </p>
<p> &#8211;serial tcp,host=:2222,mode=bind,protocol=telnet</p>
<dt><code>&#8211;serial udp,host=CONNECT_HOST:PORT,bind_host=BIND_HOST:BIND_PORT</code></p>
<dd> <font SIZE="-1">UDP</font> net console. <font SIZE="-1">HOST:PORT</font> is the destination to send output to (default <font SIZE="-1">HOST</font> is &#8216;127.0.0.1&#8217;, <font SIZE="-1">PORT</font> is required). <font SIZE="-1">BIND_HOST:BIND_PORT</font> is the optional local address to bind to (default <font SIZE="-1">BIND_HOST</font> is 127.0.0.1, but is only set if <font SIZE="-1">BIND_PORT</font> is specified). Some examples: </p>
<p> Send output to default syslog port (may need to edit /etc/rsyslog.conf accordingly): </p>
<p> &#8211;serial udp,host=:514 </p>
<p> Send output to remote host 192.168.10.20, port 4444 (this output can be read on the remote host using &#8216;nc -u -l 4444&#8217;): </p>
<p> &#8211;serial udp,host=192.168.10.20:4444</p>
<dt><code>&#8211;serial unix,path=UNIXPATH,mode=MODE</code></p>
<dd> Unix socket, see <i><a href="/docs/linux/man/7-unix/">unix</a></i>(7). <font SIZE="-1">MODE</font> has similar behavior and defaults as &#8211;serial tcp,mode=MODE</dl>
</dl>
<dl>
<dt>
<dd>
<p> Use &#8211;serial=? or &#8211;parallel=? to see a list of all available sub options. Complete details at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsCharSerial">http://libvirt.org/formatdomain.html#elementsCharSerial</a>&gt; and &lt;<a href="http://libvirt.org/formatdomain.html#elementsCharParallel">http://libvirt.org/formatdomain.html#elementsCharParallel</a>&gt;</dl>
<dt><code>&#8211;channel</code></p>
<dd> Specifies a communication channel device to connect the guest and host machine. This option uses the same options as &#8211;serial and &#8211;parallel for specifying the host/source end of the channel. Extra &#8216;target&#8217; options are used to specify how the guest machine sees the channel. </p>
<p> Some of the types of character device redirection are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;channel </code><font SIZE="-1"><code>SOURCE</code></font><code>,target_type=guestfwd,target_address=HOST:PORT</code></p>
<dd> Communication channel using <font SIZE="-1">QEMU</font> usermode networking stack. The guest can connect to the channel using the specified <font SIZE="-1">HOST:PORT</font> combination.</p>
<dt><code>&#8211;channel </code><font SIZE="-1"><code>SOURCE</code></font><code>,target_type=virtio[,name=NAME]</code></p>
<dd> Communication channel using virtio serial (requires 2.6.34 or later host and guest). Each instance of a virtio &#8211;channel line is exposed in the guest as /dev/vport0p1, /dev/vport0p2, etc. <font SIZE="-1">NAME</font> is optional metadata, and can be any string, such as org.linux-kvm.virtioport1. If specified, this will be exposed in the guest at /sys/class/virtio-ports/vport0p1/NAME</p>
<dt><code>&#8211;channel spicevmc,target_type=virtio[,name=NAME]</code></p>
<dd> Communication channel for <font SIZE="-1">QEMU</font> spice agent, using virtio serial (requires 2.6.34 or later host and guest). <font SIZE="-1">NAME</font> is optional metadata, and can be any string, such as the default com.redhat.spice.0 that specifies how the guest will see the channel.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Use &#8211;channel=? to see a list of all available sub options. Complete details at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsCharChannel">http://libvirt.org/formatdomain.html#elementsCharChannel</a>&gt;</dl>
<dt><code>&#8211;console</code></p>
<dd> Connect a text console between the guest and host. Certain guest and hypervisor combinations can automatically set up a getty in the guest, so an out of the box text login can be provided (target_type=xen for xen paravirt guests, and possibly target_type=virtio in the future). </p>
<p> Example:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;console pty,target_type=virtio</code></p>
<dd> Connect a virtio console to the guest, redirected to a <font SIZE="-1">PTY</font> on the host. For supported guests, this exposes /dev/hvc0 in the guest. See <a rel="nofollow" href="http://fedoraproject.org/wiki/Features/VirtioSerial">http://fedoraproject.org/wiki/Features/VirtioSerial</a> for more info. virtio console requires libvirt 0.8.3 or later.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Use &#8211;console=? to see a list of all available sub options. Complete details at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsCharConsole">http://libvirt.org/formatdomain.html#elementsCharConsole</a>&gt;</dl>
<dt><code>&#8211;video</code> <font SIZE="-1">OPTIONS</font></p>
<dd> Specify what video device model will be attached to the guest. Valid values for <font SIZE="-1">VIDEO</font> are hypervisor specific, but some options for recent kvm are cirrus, vga, qxl, virtio, or vmvga (vmware). </p>
<p> Use &#8211;video=? to see a list of all available sub options. Complete details at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsVideo">http://libvirt.org/formatdomain.html#elementsVideo</a>&gt;</p>
<dt><code>&#8211;smartcard</code> MODE[,OPTIONS]</p>
<dd> Configure a virtual smartcard device. </p>
<p> Mode is one of <code>host</code>, <code>host-certificates</code>, or <code>passthrough</code>. Additional options are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>type</code></p>
<dd> Character device type to connect to on the host. This is only applicable for <code>passthrough</code> mode.</dl>
</dl>
<dl>
<dt>
<dd>
<p> An example invocation:</p>
<dl>
<dt><code>&#8211;smartcard passthrough,type=spicevmc</code></p>
<dd> Use the smartcard channel of a <font SIZE="-1">SPICE</font> graphics device to pass smartcard info to the guest</dl>
</dl>
<dl>
<dt>
<dd>
<p> Use &#8211;smartcard=? to see a list of all available sub options. Complete details at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsSmartcard">http://libvirt.org/formatdomain.html#elementsSmartcard</a>&gt;</dl>
<dt><code>&#8211;redirdev</code> BUS[,OPTIONS]</p>
<dd> Add a redirected device.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>type</code></p>
<dd> The redirection type, currently supported is <code>tcp</code> or <code>spicevmc</code>.</p>
<dt><code>server</code></p>
<dd> The <font SIZE="-1">TCP</font> server connection details, of the form &#8216;server:port&#8217;.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Examples of invocation:</p>
<dl>
<dt><code>&#8211;redirdev usb,type=tcp,server=localhost:4000</code></p>
<dd> Add a <font SIZE="-1">USB</font> redirected device provided by the <font SIZE="-1">TCP</font> server on &#8216;localhost&#8217; port 4000.</p>
<dt><code>&#8211;redirdev usb,type=spicevmc</code></p>
<dd> Add a <font SIZE="-1">USB</font> device redirected via a dedicated Spice channel.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Use &#8211;redirdev=? to see a list of all available sub options. Complete details at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsRedir">http://libvirt.org/formatdomain.html#elementsRedir</a>&gt;</dl>
<dt><code>&#8211;memballoon</code> <font SIZE="-1">MODEL</font></p>
<dd> Attach a virtual memory balloon device to the guest. If the memballoon device needs to be explicitly disabled, MODEL=&#8217;none&#8217; is used. </p>
<p> <font SIZE="-1">MODEL</font> is the type of memballoon device provided. The value can be &#8216;virtio&#8217;, &#8216;xen&#8217; or &#8216;none&#8217;. Some examples: </p>
<p> Use the recommended settings: </p>
<p> &#8211;memballoon virtio </p>
<p> Do not use memballoon device: </p>
<p> &#8211;memballoon none </p>
<p> Use &#8211;memballoon=? to see a list of all available sub options. Complete details at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsMemBalloon">http://libvirt.org/formatdomain.html#elementsMemBalloon</a>&gt;</p>
<dt><code>&#8211;tpm</code> TYPE[,OPTIONS]</p>
<dd> Configure a virtual <font SIZE="-1">TPM</font> device. </p>
<p> Type must be <code>passthrough</code>. Additional options are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>model</code></p>
<dd> The device model to present to the guest operating system. Model must be <code>tpm-tis</code>.</dl>
</dl>
<dl>
<dt>
<dd>
<p> An example invocation:</p>
<dl>
<dt><code>&#8211;tpm passthrough,model=tpm-tis</code></p>
<dd> Make the host&#8217;s <font SIZE="-1">TPM</font> accessible to a single guest.</p>
<dt><code>&#8211;tpm /dev/tpm</code></p>
<dd> Convenience option for passing through the hosts <font SIZE="-1">TPM.</font></dl>
</dl>
<dl>
<dt>
<dd>
<p> Use &#8211;tpm=? to see a list of all available sub options. Complete details at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsTpm">http://libvirt.org/formatdomain.html#elementsTpm</a>&gt;</dl>
<dt><code>&#8211;rng</code> TYPE[,OPTIONS]</p>
<dd> Configure a virtual <font SIZE="-1">RNG</font> device. </p>
<p> Type can be <code>random</code> or <code>egd</code>. </p>
<p> If the specified type is <code>random</code> then these values must be specified:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>backend_device</code></p>
<dd> The device to use as a source of entropy.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Whereas, when the type is <code>egd</code>, these values must be provided:</p>
<dl>
<dt><code>backend_host</code></p>
<dd> Specify the host of the Entropy Gathering Daemon to connect to.</p>
<dt><code>backend_service</code></p>
<dd> Specify the port of the Entropy Gathering Daemon to connect to.</p>
<dt><code>backend_type</code></p>
<dd> Specify the type of the connection: <code>tcp</code> or <code>udp</code>.</p>
<dt><code>backend_mode</code></p>
<dd> Specify the mode of the connection. It is either &#8216;bind&#8217; (wait for connections on <font SIZE="-1">HOST:PORT</font>) or &#8216;connect&#8217; (send output to <font SIZE="-1">HOST:PORT</font>).</p>
<dt><code>backend_connect_host</code></p>
<dd> Specify the remote host to connect to when the specified backend_type is <code>udp</code> and backend_mode is <code>bind</code>.</p>
<dt><code>backend_connect_service</code></p>
<dd> Specify the remote service to connect to when the specified backend_type is <code>udp</code> and backend_mode is <code>bind</code>.</dl>
</dl>
<dl>
<dt>
<dd>
<p> An example invocation:</p>
<dl>
<dt><code>&#8211;rng egd,backend_host=localhost,backend_service=8000,backend_type=tcp</code></p>
<dd> Connect to localhost to the <font SIZE="-1">TCP</font> port 8000 to get entropy data.</p>
<dt><code>&#8211;rng /dev/random</code></p>
<dd> Use the /dev/random device to get entropy data, this form implicitly uses the &#8220;random&#8221; model. </p>
<p> Use &#8211;rng=? to see a list of all available sub options. Complete details at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsRng">http://libvirt.org/formatdomain.html#elementsRng</a>&gt;</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;panic</code> <font SIZE="-1">OPTS</font></p>
<dd> Attach a panic notifier device to the guest. For the recommended settings, use: </p>
<p> &#8211;panic default </p>
<p> Use &#8211;panic=? to see a list of all available sub options. Complete details at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html#elementsPanic">http://libvirt.org/formatdomain.html#elementsPanic</a>&gt;</dl>
<h2>MISCELLANEOUS OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8211;help</code></p>
<dd> Show the help message and exit</p>
<dt><code>&#8211;version</code></p>
<dd> Show program&#8217;s version number and exit</p>
<dt><code>&#8211;autostart</code></p>
<dd> Set the autostart flag for a domain. This causes the domain to be started on host boot up.</p>
<dt><code>&#8211;transient</code></p>
<dd> Use &#8211;import or &#8211;boot and &#8211;transient if you want a transient libvirt <font SIZE="-1">VM. </font> These VMs exist only until the domain is shut down or the host server is restarted. Libvirt forgets the <font SIZE="-1">XML</font> configuration of the <font SIZE="-1">VM</font> after either of these events. Note that the <font SIZE="-1">VM</font>&#8216;s disks will not be deleted. See: &lt;<a rel="nofollow" href="http://wiki.libvirt.org/page/VM_lifecycle#Transient_guest_domains_vs_Persistent_guest_domains">http://wiki.libvirt.org/page/VM_lifecycle#Transient_guest_domains_vs_Persistent_guest_domains</a>&gt;</p>
<dt><code>&#8211;print-xml</code> [<font SIZE="-1">STEP</font>]</p>
<dd> Print the generated <font SIZE="-1">XML</font> of the guest, instead of defining it. By default this <font SIZE="-1">WILL</font> do storage creation (can be disabled with &#8211;dry-run). This option implies &#8211;quiet. </p>
<p> If the <font SIZE="-1">VM</font> install has multiple phases, by default this will print all generated <font SIZE="-1">XML.</font> If you want to print a particular step, use &#8211;print-xml 2 (for the second phase <font SIZE="-1">XML</font>).</p>
<dt><code>&#8211;noreboot</code></p>
<dd> Prevent the domain from automatically rebooting after the install has completed.</p>
<dt><code>&#8211;wait</code> <font SIZE="-1">WAIT</font></p>
<dd> Amount of time to wait (in minutes) for a <font SIZE="-1">VM</font> to complete its install. Without this option, virt-install will wait for the console to close (not necessarily indicating the guest has shutdown), or in the case of &#8211;noautoconsole, simply kick off the install and exit. Any negative value will make virt-install wait indefinitely, a value of 0 triggers the same results as noautoconsole. If the time limit is exceeded, virt-install simply exits, leaving the virtual machine in its current state.</p>
<dt><code>&#8211;dry-run</code></p>
<dd> Proceed through the guest creation process, but do <font SIZE="-1">NOT</font> create storage devices, change host device configuration, or actually teach libvirt about the guest. virt-install may still fetch install media, since this is required to properly detect the <font SIZE="-1">OS</font> to install.</p>
<dt><code>&#8211;check</code></p>
<dd> Enable or disable some validation checks. Some examples are warning about using a disk that&#8217;s already assigned to another <font SIZE="-1">VM </font>(&#8211;check path_in_use=on|off), or warning about potentially running out of space during disk allocation (&#8211;check disk_size=on|off). Most checks are performed by default.</p>
<dt><code>-q</code></p>
<dd>
<dt><code>&#8211;quiet</code></p>
<dd> Only print fatal error messages.</p>
<dt><code>-d</code></p>
<dd>
<dt><code>&#8211;debug</code></p>
<dd> Print debugging information to the terminal when running the install process. The debugging information is also stored in <tt>&quot;~/.cache/virt-manager/virt-install.log&quot;</tt> even if this parameter is omitted.</dl>
<h2>EXAMPLES</h2>
<p> Install a Fedora 9 plain <font SIZE="-1">QEMU</font> guest, using <font SIZE="-1">LVM</font> partition, virtual networking, booting from <font SIZE="-1">PXE,</font> using <font SIZE="-1">VNC</font> server/viewer, with virtio-scsi disk </p>
<pre><code>
#virt - install-- connect qemu: ///system \
       --name demo \
       --memory 500 \
       --disk path=/dev/HostVG/DemoVM,bus=scsi \
       --controller virtio-scsi \
       --network network=default \
       --virt-type qemu
--graphics vnc-- os - variant fedora9
</code></pre>
<p> Run a Live <font SIZE="-1">CD</font> image under Xen fullyvirt, in diskless environment </p>
<p>#virt &#8211; install&#8211; hvm&#8211; name demo&#8211; memory 500 &#8211;disk none&#8211; livecd&#8211; graphics vnc&#8211; cdrom / root / fedora7live.iso</p>
<p> Run /usr/bin/httpd in a linux container guest (<font SIZE="-1">LXC</font>). Resource usage is capped at 512 MiB of ram and 2 host cpus: </p>
<p>#virt &#8211; install&#8211; connect lxc: /// \<br />
        &#8211;name httpd_guest \<br />
        &#8211;memory 512 \<br />
        &#8211;vcpus 2 \<br />
        &#8211;init /usr/bin/httpd</p>
<p> Start a linux container guest(<font SIZE="-1">LXC</font>) with a private root filesystem, using /bin/sh as init. Container&#8217;s root will be under host dir /home/LXC. The host dir &#8220;/home/test&#8221; will be mounted at &#8220;/mnt&#8221; dir inside container: </p>
<p>#virt &#8211; install&#8211; connect lxc: /// \<br />
        &#8211;name container \<br />
        &#8211;memory 128 \<br />
        &#8211;filesystem /home/LXC,/ \<br />
        &#8211;filesystem /home/test,/mnt \<br />
        &#8211;init /bin/sh</p>
<p> Install a paravirtualized Xen guest, 500 MiB of <font SIZE="-1">RAM,</font> a 5 GiB of disk, and Fedora Core 6 from a web server, in text-only mode, with old style &#8211;file options: </p>
<p>#virt &#8211; install&#8211; paravirt&#8211; name demo&#8211; memory 500 &#8211;disk / var / lib / xen / images / demo.img, size = 6 &#8211;graphics none&#8211; location http: // download.fedora.redhat.com/pub/fedora/linux/core/6/x86_64/os/</p>
<p> Create a guest from an existing disk image &#8216;mydisk.img&#8217; using defaults for the rest of the options. </p>
<p>#virt &#8211; install&#8211; name demo&#8211; memory 512 &#8211;disk / home / user / VMs / mydisk.img&#8211; import</p>
<p> Start serial <font SIZE="-1">QEMU ARM VM,</font> which requires specifying a manual kernel. </p>
<pre><code>
#virt - install-- name armtest-- memory 1024 --arch armv7l-- machine vexpress - a9-- disk / home / user / VMs / myarmdisk.img-- boot kernel = / tmp / my - arm - kernel, initrd = / tmp / my - arm - initrd, dtb = / tmp / my - arm - dtb, kernel_args = "console=ttyAMA0 rw root=/dev/mmcblk0p3" --graphics none
</code></pre>
<h2>BUGS</h2>
<p> Please see <a rel="nofollow" href="http://virt-manager.org/page/BugReporting">http://virt-manager.org/page/BugReporting</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) Red Hat, Inc, and various contributors. This is free software. You may redistribute copies of it under the terms of the <font SIZE="-1">GNU</font> General Public License <tt>&quot;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a>&quot;</tt>. There is <font SIZE="-1">NO WARRANTY,</font> to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <tt><a href="/docs/linux/man/1-virsh/">virsh</a>(1)</tt>, <tt>&quot;<a href="/docs/linux/man/1-virt-clone/">virt-clone</a>(1)&quot;</tt>, <tt>&quot;<a href="/docs/linux/man/1-virt-manager/">virt-manager</a>(1)&quot;</tt>, the project website <tt>&quot;<a rel="nofollow" href="http://virt-manager.org">http://virt-manager.org</a>&quot;</tt> </p>
<h2>Index</h2>
