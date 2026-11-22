---

title: "qemu-kvm(1)"
name: "qemu-kvm"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qemu-kvm/"
---

qemu-doc - QEMU Emulator User Documentation 

<h2>SYNOPSIS</h2>

 usage: qemu-kvm [options] [<i>disk_image</i>]

<h2>DESCRIPTION</h2>

 The QEMU PC System emulator simulates the following peripherals:
<dl>
<dt>-
</dt><dd> i440FX host PCI bridge and PIIX3 PCI to ISA bridge
</dd><dt>-
</dt><dd> Cirrus CLGD 5446 PCI VGA card or dummy VGA card with Bochs VESA extensions (hardware level, including all non standard modes).
</dd><dt>-
</dt><dd> PS/2 mouse and keyboard
</dd><dt>-
</dt><dd> 2 PCI IDE interfaces with hard disk and CD-ROM support
</dd><dt>-
</dt><dd> Floppy disk
</dd><dt>-
</dt><dd> PCI and ISA network adapters
</dd><dt>-
</dt><dd> Serial ports
</dd><dt>-
</dt><dd> Creative SoundBlaster 16 sound card
</dd><dt>-
</dt><dd> ENSONIQ AudioPCI ES1370 sound card
</dd><dt>-
</dt><dd> Intel 82801AA AC97 Audio compatible sound card
</dd><dt>-
</dt><dd> Intel HD Audio Controller and HDA codec
</dd><dt>-
</dt><dd> Adlib (OPL2) - Yamaha YM3812 compatible chip
</dd><dt>-
</dt><dd> Gravis Ultrasound GF1 sound card
</dd><dt>-
</dt><dd> CS4231A compatible sound card
</dd><dt>-
</dt><dd> PCI UHCI USB controller and a virtual USB hub.</dd></dl>
 

 SMP is supported with up to 255 CPUs. 

 QEMU uses the PC BIOS from the Bochs project and the Plex86/Bochs LGPL VGA BIOS. 

 QEMU uses YM3812 emulation by Tatsuyuki Satoh. 

 QEMU uses GUS emulation (GUSEMU32 &lt;<b><a rel="nofollow" HREF="http://www.deinmeister.de/gusemu/">http://www.deinmeister.de/gusemu/</a></b>&gt;) by Tibor ``TS'' Schütz. 

 Note that, by default, GUS shares <i>IRQ</i><i></i>(7) with parallel ports and so QEMU must be told to not have parallel ports to have working GUS. 

 <pre>
        qemu-kvm dos.img -soundhw gus -parallel none
</pre> 

 Alternatively: 

 <pre>
        qemu-kvm dos.img -device gus,irq=5
</pre> 

 Or some other unclaimed IRQ. 

 CS4231A is the chip used in Windows Sound System and GUSMAX products

<h2>OPTIONS</h2>

 <i>disk_image</i> is a raw hard disk image for IDE hard disk 0. Some targets do not need a disk image. 

 Standard options:
<dl>
<dt><b>-h</b>
</dt><dd> Display help and exit
</dd><dt><b>-version</b>
</dt><dd> Display version information and exit
</dd><dt><b>-machine [type=]</b><i>name</i><b>[,prop=</b><i>value</i><b>[,...]]</b>
</dt><dd> Select the emulated machine by <i>name</i>. Use <tt>&quot;-machine help&quot;</tt> to list available machines. Supported machine properties are:
</dd><dl>
<dl>
<dt><b>accel=</b><i>accels1</i><b>[:</b><i>accels2</i><b>[:...]]</b>
</dt><dd> This is used to enable an accelerator. Depending on the target architecture, kvm, xen, or tcg can be available. By default, tcg is used. If there is more than one accelerator specified, the next one is used if the previous one fails to initialize.
</dd><dt><b>kernel_irqchip=on|off</b>
</dt><dd> Enables in-kernel irqchip support for the chosen accelerator when available.
</dd><dt><b>kvm_shadow_mem=size</b>
</dt><dd> Defines the size of the KVM shadow MMU.
</dd><dt><b>dump-guest-core=on|off</b>
</dt><dd> Include guest memory in a core dump. The default is on.
</dd><dt><b>mem-merge=on|off</b>
</dt><dd> Enables or disables memory merge support. This feature, when supported by the host, de-duplicates identical memory pages among VMs instances (enabled by default).</dd></dl>
</dl>

<dl>
</dl>

<dt><b>-cpu</b> <i>model</i>
</dt><dd> Select CPU model (<tt>&quot;-cpu help&quot;</tt> for list and additional feature selection)
</dd><dt><b>-smp</b> <i>n</i><b>[,cores=</b><i>cores</i><b>][,threads=</b><i>threads</i><b>][,sockets=</b><i>sockets</i><b>][,maxcpus=</b><i>maxcpus</i><b>]</b>
</dt><dd> Simulate an SMP system with <i>n</i> CPUs. On the PC target, up to 255 CPUs are supported. On Sparc32 target, Linux limits the number of usable CPUs to 4. For the PC target, the number of <i>cores</i> per socket, the number of <i>threads</i> per cores and the total number of <i>sockets</i> can be specified. Missing values will be computed. If any on the three values is given, the total number of CPUs <i>n</i> can be omitted. <i>maxcpus</i> specifies the maximum number of hotpluggable CPUs.
</dd><dt><b>-numa</b> <i>opts</i>
</dt><dd> Simulate a multi node NUMA system. If mem and cpus are omitted, resources are split equally.
</dd><dt><b>-add-fd fd=</b><i>fd</i><b>,set=</b><i>set</i><b>[,opaque=</b><i>opaque</i><b>]</b>
</dt><dd> Add a file descriptor to an fd set. Valid options are:
</dd><dl>
<dl>
<dt><b>fd=</b><i>fd</i>
</dt><dd> This option defines the file descriptor of which a duplicate is added to fd set. The file descriptor cannot be stdin, stdout, or stderr.
</dd><dt><b>set=</b><i>set</i>
</dt><dd> This option defines the ID of the fd set to add the file descriptor to.
</dd><dt><b>opaque=</b><i>opaque</i>
</dt><dd> This option defines a free-form string that can be used to describe <i>fd</i>.</dd></dl>
</dl>

<dl>
<dt>
</dt><dd> 
 You can open an image using pre-opened file descriptors from an fd set: 
 <pre>
        qemu-kvm
        -add-fd fd=3,set=2,opaque=&quot;rdwr:/path/to/file&quot;
        -add-fd fd=4,set=2,opaque=&quot;rdonly:/path/to/file&quot;
        -drive file=/dev/fdset/2,index=0,media=disk
</pre></dd></dl>

<dt><b>-set</b> <i>group</i><b>.</b><i>id</i><b>.</b><i>arg</i><b>=</b><i>value</i>
</dt><dd> Set parameter <i>arg</i> for item <i>id</i> of type <i>group</i>\n&quot;
</dd><dt><b>-global</b> <i>driver</i><b>.</b><i>prop</i><b>=</b><i>value</i>
</dt><dd> Set default value of <i>driver</i>'s property <i>prop</i> to <i>value</i>, e.g.: 

 <pre>
        qemu-kvm -global ide-drive.physical_block_size=4096 -drive file=file,if=ide,index=0,media=disk
</pre> 

 In particular, you can use this to set driver properties for devices which are created automatically by the machine model. To create a device which is not created automatically and set properties on it, use -<b>device</b>.
</dd><dt><b>-boot [order=</b><i>drives</i><b>][,once=</b><i>drives</i><b>][,menu=on|off][,splash=</b><i>sp_name</i><b>][,splash-time=</b><i>sp_time</i><b>][,reboot-timeout=</b><i>rb_timeout</i><b>][,strict=on|off]</b>
</dt><dd> Specify boot order <i>drives</i> as a string of drive letters. Valid drive letters depend on the target achitecture. The x86 PC uses: a, b (floppy 1 and 2), c (first hard disk), d (first CD-ROM), n-p (Etherboot from network adapter 1-4), hard disk boot is the default. To apply a particular boot order only on the first startup, specify it via <b>once</b>. 

 Interactive boot menus/prompts can be enabled via <b>menu=on</b> as far as firmware/BIOS supports them. The default is non-interactive boot. 

 A splash picture could be passed to bios, enabling user to show it as logo, when option splash=<i>sp_name</i> is given and menu=on, If firmware/BIOS supports them. Currently Seabios for X86 system support it. limitation: The splash file could be a jpeg file or a BMP file in 24 BPP format(true color). The resolution should be supported by the SVGA mode, so the recommended is 320x240, 640x480, 800x640. 

 A timeout could be passed to bios, guest will pause for <i>rb_timeout</i> ms when boot failed, then reboot. If <i>rb_timeout</i> is '-1', guest will not reboot, qemu-kvm passes '-1' to bios by default. Currently Seabios for X86 system support it. 

 Do strict boot via <b>strict=on</b> as far as firmware/BIOS supports it. This only effects when boot priority is changed by bootindex options. The default is non-strict boot. 

 <pre>
        # try to boot from network first, then from hard disk
        qemu-kvm -boot order=nc
        # boot from CD-ROM first, switch back to default order after reboot
        qemu-kvm -boot once=d
        # boot with a splash picture for 5 seconds.
        qemu-kvm -boot menu=on,splash=/root/boot.bmp,splash-time=5000
</pre> 

 Note: The legacy format '-boot <i>drives</i>' is still supported but its use is discouraged as it may be removed from future versions.
</dd><dt><b>-m</b> <i>megs</i>
</dt><dd> Set virtual RAM size to <i>megs</i> megabytes. Default is 128 MiB. Optionally, a suffix of ``M'' or ``G'' can be used to signify a value in megabytes or gigabytes respectively.
</dd><dt><b>-mem-path</b> <i>path</i>
</dt><dd> Allocate guest RAM from a temporarily created file in <i>path</i>.
</dd><dt><b>-mem-prealloc</b>
</dt><dd> Preallocate memory when using -mem-path.
</dd><dt><b>-k</b> <i>language</i>
</dt><dd> Use keyboard layout <i>language</i> (for example <tt>&quot;fr&quot;</tt> for French). This option is only needed where it is not easy to get raw PC keycodes (e.g. on Macs, with some X11 servers or with a VNC display). You don't normally need to use it on PC/Linux or PC/Windows hosts. 

 The available layouts are: 

 <pre>
        ar  de-ch  es  fo     fr-ca  hu  ja  mk     no  pt-br  sv
        da  en-gb  et  fr     fr-ch  is  lt  nl     pl  ru     th
        de  en-us  fi  fr-be  hr     it  lv  nl-be  pt  sl     tr
</pre> 

 The default is <tt>&quot;en-us&quot;</tt>.
</dd><dt><b>-audio-help</b>
</dt><dd> Will show the audio subsystem help: list of drivers, tunable parameters.
</dd><dt><b>-soundhw</b> <i>card1</i><b>[,</b><i>card2</i><b>,...] or -soundhw all</b>
</dt><dd> Enable audio and selected sound hardware. Use 'help' to print all available sound hardware. 

 <pre>
        qemu-kvm -soundhw sb16,adlib disk.img
        qemu-kvm -soundhw es1370 disk.img
        qemu-kvm -soundhw ac97 disk.img
        qemu-kvm -soundhw hda disk.img
        qemu-kvm -soundhw all disk.img
        qemu-kvm -soundhw help
</pre> 

 Note that Linux's i810_audio OSS kernel (for AC97) module might require manually specifying clocking. 

 <pre>
        modprobe i810_audio clocking=48000
</pre>
</dd><dt><b>-balloon none</b>
</dt><dd> Disable balloon device.
</dd><dt><b>-balloon virtio[,addr=</b><i>addr</i><b>]</b>
</dt><dd> Enable virtio balloon device (default), optionally with PCI address <i>addr</i>.
</dd><dt><b>-device</b> <i>driver</i><b>[,</b><i>prop</i><b>[=</b><i>value</i><b>][,...]]</b>
</dt><dd> Add device <i>driver</i>. <i>prop</i>=<i>value</i> sets driver properties. Valid properties depend on the driver. To get help on possible drivers and properties, use <tt>&quot;-device help&quot;</tt> and <tt>&quot;-device </tt>driver<tt>,help&quot;</tt>.
</dd><dt><b>-name</b> <i>name</i>
</dt><dd> Sets the <i>name</i> of the guest. This name will be displayed in the SDL window caption. The <i>name</i> will also be used for the VNC server. Also optionally set the top visible process name in Linux.
</dd><dt><b>-uuid</b> <i>uuid</i>
</dt><dd> Set system UUID.</dd></dl>
 

 Block device options:
<dl>
<dt><b>-fda</b> <i>file</i>
</dt><dd>
</dd><dt><b>-fdb</b> <i>file</i>
</dt><dd> Use <i>file</i> as floppy disk 0/1 image. You can use the host floppy by using <i>/dev/fd0</i> as filename.
</dd><dt><b>-hda</b> <i>file</i>
</dt><dd>
</dd><dt><b>-hdb</b> <i>file</i>
</dt><dd>
</dd><dt><b>-hdc</b> <i>file</i>
</dt><dd>
</dd><dt><b>-hdd</b> <i>file</i>
</dt><dd> Use <i>file</i> as hard disk 0, 1, 2 or 3 image.
</dd><dt><b>-cdrom</b> <i>file</i>
</dt><dd> Use <i>file</i> as CD-ROM image (you cannot use <b>-hdc</b> and <b>-cdrom</b> at the same time). You can use the host CD-ROM by using <i>/dev/cdrom</i> as filename.
</dd><dt><b>-drive</b> <i>option</i><b>[,</b><i>option</i><b>[,</b><i>option</i><b>[,...]]]</b>
</dt><dd> Define a new drive. Valid options are:
</dd><dl>
<dl>
<dt><b>file=</b><i>file</i>
</dt><dd> This option defines which disk image to use with this drive. If the filename contains comma, you must double it (for instance, ``file=my,,file'' to use file ``my,file''). 
 Special files such as iSCSI devices can be specified using protocol specific URLs. See the section for ``Device URL Syntax'' for more information.
</dd><dt><b>if=</b><i>interface</i>
</dt><dd> This option defines on which type on interface the drive is connected. Available types are: ide, scsi, sd, mtd, floppy, pflash, virtio.
</dd><dt><b>bus=</b><i>bus</i><b>,unit=</b><i>unit</i>
</dt><dd> These options define where is connected the drive by defining the bus number and the unit id.
</dd><dt><b>index=</b><i>index</i>
</dt><dd> This option defines where is connected the drive by using an index in the list of available connectors of a given interface type.
</dd><dt><b>media=</b><i>media</i>
</dt><dd> This option defines the type of the media: disk or cdrom.
</dd><dt><b>cyls=</b><i>c</i><b>,heads=</b><i>h</i><b>,secs=</b><i>s</i><b>[,trans=</b><i>t</i><b>]</b>
</dt><dd> These options have the same definition as they have in <b>-hdachs</b>.
</dd><dt><b>snapshot=</b><i>snapshot</i>
</dt><dd> <i>snapshot</i> is ``on'' or ``off'' and allows to enable snapshot for given drive (see <b>-snapshot</b>).
</dd><dt><b>cache=</b><i>cache</i>
</dt><dd> <i>cache</i> is ``none'', ``writeback'', ``unsafe'', ``directsync'' or ``writethrough'' and controls how the host cache is used to access block data.
</dd><dt><b>aio=</b><i>aio</i>
</dt><dd> <i>aio</i> is ``threads'', or ``native'' and selects between pthread based disk I/O and native Linux AIO.
</dd><dt><b>discard=</b><i>discard</i>
</dt><dd> <i>discard</i> is one of ``ignore'' (or ``off'') or ``unmap'' (or ``on'') and controls whether <i>discard</i> (also known as <i>trim</i> or <i>unmap</i>) requests are ignored or passed to the filesystem. Some machine types may not support discard requests.
</dd><dt><b>format=</b><i>format</i>
</dt><dd> Specify which disk <i>format</i> will be used rather than detecting the format. Can be used to specifiy format=raw to avoid interpreting an untrusted format header.
</dd><dt><b>serial=</b><i>serial</i>
</dt><dd> This option specifies the serial number to assign to the device.
</dd><dt><b>addr=</b><i>addr</i>
</dt><dd> Specify the controller's PCI address (if=virtio only).
</dd><dt><b>werror=</b><i>action</i><b>,rerror=</b><i>action</i>
</dt><dd> Specify which <i>action</i> to take on write and read errors. Valid actions are: ``ignore'' (ignore the error and try to continue), ``stop'' (pause QEMU), ``report'' (report the error to the guest), ``enospc'' (pause QEMU only if the host disk is full; report the error to the guest otherwise). The default setting is <b>werror=enospc</b> and <b>rerror=report</b>.
</dd><dt><b>readonly</b>
</dt><dd> Open drive <b>file</b> as read-only. Guest write attempts will fail.
</dd><dt><b>copy-on-read=</b><i>copy-on-read</i>
</dt><dd> <i>copy-on-read</i> is ``on'' or ``off'' and enables whether to copy read backing file sectors into the image file.</dd></dl>
</dl>

<dl>
<dt>
</dt><dd> 
 By default, the <b>cache=writeback</b> mode is used. It will report data writes as completed as soon as the data is present in the host page cache. This is safe as long as your guest OS makes sure to correctly flush disk caches where needed. If your guest OS does not handle volatile disk write caches correctly and your host crashes or loses power, then the guest may experience data corruption. 
 For such guests, you should consider using <b>cache=writethrough</b>. This means that the host page cache will be used to read and write data, but write notification will be sent to the guest only after QEMU has made sure to flush each write to the disk. Be aware that this has a major impact on performance. 
 The host page cache can be avoided entirely with <b>cache=none</b>. This will attempt to do disk IO directly to the guest's memory. QEMU may still perform an internal copy of the data. Note that this is considered a writeback mode and the guest OS must handle the disk write cache correctly in order to avoid data corruption on host crashes. 
 The host page cache can be avoided while only sending write notifications to the guest when the data has been flushed to the disk using <b>cache=directsync</b>. 
 In case you don't care about data integrity over host failures, use <b>cache=unsafe</b>. This option tells QEMU that it never needs to write any data to the disk but can instead keep things in cache. If anything goes wrong, like your host losing power, the disk storage getting disconnected accidentally, etc. your image will most probably be rendered unusable. When using the <b>-snapshot</b> option, unsafe caching is always used. 
 Copy-on-read avoids accessing the same backing file sectors repeatedly and is useful when the backing file is over a slow network. By default copy-on-read is off. 
 Instead of <b>-cdrom</b> you can use: 
 <pre>
        qemu-kvm -drive file=file,index=2,media=cdrom
</pre> 
 Instead of <b>-hda</b>, <b>-hdb</b>, <b>-hdc</b>, <b>-hdd</b>, you can use: 
 <pre>
        qemu-kvm -drive file=file,index=0,media=disk
        qemu-kvm -drive file=file,index=1,media=disk
        qemu-kvm -drive file=file,index=2,media=disk
        qemu-kvm -drive file=file,index=3,media=disk
</pre> 
 You can open an image using pre-opened file descriptors from an fd set: 
 <pre>
        qemu-kvm
        -add-fd fd=3,set=2,opaque=&quot;rdwr:/path/to/file&quot;
        -add-fd fd=4,set=2,opaque=&quot;rdonly:/path/to/file&quot;
        -drive file=/dev/fdset/2,index=0,media=disk
</pre> 
 You can connect a CDROM to the slave of ide0: 
 <pre>
        qemu-kvm -drive file=file,if=ide,index=1,media=cdrom
</pre> 
 If you don't specify the ``file='' argument, you define an empty drive: 
 <pre>
        qemu-kvm -drive if=ide,index=1,media=cdrom
</pre> 
 You can connect a SCSI disk with unit ID 6 on the bus #0: 
 <pre>
        qemu-kvm -drive file=file,if=scsi,bus=0,unit=6
</pre> 
 Instead of <b>-fda</b>, <b>-fdb</b>, you can use: 
 <pre>
        qemu-kvm -drive file=file,index=0,if=floppy
        qemu-kvm -drive file=file,index=1,if=floppy
</pre> 
 By default, <i>interface</i> is ``ide'' and <i>index</i> is automatically incremented: 
 <pre>
        qemu-kvm -drive file=a -drive file=b&quot;
</pre> 
 is interpreted like: 
 <pre>
        qemu-kvm -hda a -hdb b
</pre></dd></dl>

<dt><b>-mtdblock</b> <i>file</i>
</dt><dd> Use <i>file</i> as on-board Flash memory image.
</dd><dt><b>-sd</b> <i>file</i>
</dt><dd> Use <i>file</i> as SecureDigital card image.
</dd><dt><b>-pflash</b> <i>file</i>
</dt><dd> Use <i>file</i> as a parallel flash image.
</dd><dt><b>-snapshot</b>
</dt><dd> Write to temporary files instead of disk image files. In this case, the raw disk image you use is not written back. You can however force the write back by pressing <b>C-a s</b>.
</dd><dt><b>-hdachs</b> <i>c</i><b>,</b><i>h</i><b>,</b><i>s</i><b>,[,</b><i>t</i><b>]</b>
</dt><dd> Force hard disk 0 physical geometry (1 &lt;= <i>c</i> &lt;= 16383, 1 &lt;= <i>h</i> &lt;= 16, 1 &lt;= <i>s</i> &lt;= 63) and optionally force the BIOS translation mode (<i>t</i>=none, lba or auto). Usually QEMU can guess all those parameters. This option is useful for old MS-DOS disk images.
</dd><dt><b>-fsdev</b> <i>fsdriver</i><b>,id=</b><i>id</i><b>,path=</b><i>path</i><b>,[security_model=</b><i>security_model</i><b>][,writeout=</b><i>writeout</i><b>][,readonly][,socket=</b><i>socket</i><b>|sock_fd=</b><i>sock_fd</i><b>]</b>
</dt><dd> Define a new file system device. Valid options are:
</dd><dl>
<dl>
<dt><i>fsdriver</i>
</dt><dd> This option specifies the fs driver backend to use. Currently ``local'', ``handle'' and ``proxy'' file system drivers are supported.
</dd><dt><b>id=</b><i>id</i>
</dt><dd> Specifies identifier for this device
</dd><dt><b>path=</b><i>path</i>
</dt><dd> Specifies the export path for the file system device. Files under this path will be available to the 9p client on the guest.
</dd><dt><b>security_model=</b><i>security_model</i>
</dt><dd> Specifies the security model to be used for this export path. Supported security models are ``passthrough'', ``mapped-xattr'', ``mapped-file'' and ``none''. In ``passthrough'' security model, files are stored using the same credentials as they are created on the guest. This requires QEMU to run as root. In ``mapped-xattr'' security model, some of the file attributes like uid, gid, mode bits and link target are stored as file attributes. For ``mapped-file'' these attributes are stored in the hidden .virtfs_metadata directory. Directories exported by this security model cannot interact with other unix tools. ``none'' security model is same as passthrough except the sever won't report failures if it fails to set file attributes like ownership. Security model is mandatory only for local fsdriver. Other fsdrivers (like handle, proxy) don't take security model as a parameter.
</dd><dt><b>writeout=</b><i>writeout</i>
</dt><dd> This is an optional argument. The only supported value is ``immediate''. This means that host page cache will be used to read and write data but write notification will be sent to the guest only when the data has been reported as written by the storage subsystem.
</dd><dt><b>readonly</b>
</dt><dd> Enables exporting 9p share as a readonly mount for guests. By default read-write access is given.
</dd><dt><b>socket=</b><i>socket</i>
</dt><dd> Enables proxy filesystem driver to use passed socket file for communicating with virtfs-proxy-helper
</dd><dt><b>sock_fd=</b><i>sock_fd</i>
</dt><dd> Enables proxy filesystem driver to use passed socket descriptor for communicating with virtfs-proxy-helper. Usually a helper like libvirt will create socketpair and pass one of the fds as sock_fd</dd></dl>
</dl>

<dl>
<dt>
</dt><dd> 
 -fsdev option is used along with -device driver ``virtio-9p-pci''.</dd></dl>

<dt><b>-device virtio-9p-pci,fsdev=</b><i>id</i><b>,mount_tag=</b><i>mount_tag</i>
</dt><dd> Options for virtio-9p-pci driver are:
</dd><dl>
<dl>
<dt><b>fsdev=</b><i>id</i>
</dt><dd> Specifies the id value specified along with -fsdev option
</dd><dt><b>mount_tag=</b><i>mount_tag</i>
</dt><dd> Specifies the tag name to be used by the guest to mount this export point</dd></dl>
</dl>

<dl>
</dl>

<dt><b>-virtfs</b> <i>fsdriver</i><b>[,path=</b><i>path</i><b>],mount_tag=</b><i>mount_tag</i><b>[,security_model=</b><i>security_model</i><b>][,writeout=</b><i>writeout</i><b>][,readonly][,socket=</b><i>socket</i><b>|sock_fd=</b><i>sock_fd</i><b>]</b>
</dt><dd> The general form of a Virtual File system pass-through options are:
</dd><dl>
<dl>
<dt><i>fsdriver</i>
</dt><dd> This option specifies the fs driver backend to use. Currently ``local'', ``handle'' and ``proxy'' file system drivers are supported.
</dd><dt><b>id=</b><i>id</i>
</dt><dd> Specifies identifier for this device
</dd><dt><b>path=</b><i>path</i>
</dt><dd> Specifies the export path for the file system device. Files under this path will be available to the 9p client on the guest.
</dd><dt><b>security_model=</b><i>security_model</i>
</dt><dd> Specifies the security model to be used for this export path. Supported security models are ``passthrough'', ``mapped-xattr'', ``mapped-file'' and ``none''. In ``passthrough'' security model, files are stored using the same credentials as they are created on the guest. This requires QEMU to run as root. In ``mapped-xattr'' security model, some of the file attributes like uid, gid, mode bits and link target are stored as file attributes. For ``mapped-file'' these attributes are stored in the hidden .virtfs_metadata directory. Directories exported by this security model cannot interact with other unix tools. ``none'' security model is same as passthrough except the sever won't report failures if it fails to set file attributes like ownership. Security model is mandatory only for local fsdriver. Other fsdrivers (like handle, proxy) don't take security model as a parameter.
</dd><dt><b>writeout=</b><i>writeout</i>
</dt><dd> This is an optional argument. The only supported value is ``immediate''. This means that host page cache will be used to read and write data but write notification will be sent to the guest only when the data has been reported as written by the storage subsystem.
</dd><dt><b>readonly</b>
</dt><dd> Enables exporting 9p share as a readonly mount for guests. By default read-write access is given.
</dd><dt><b>socket=</b><i>socket</i>
</dt><dd> Enables proxy filesystem driver to use passed socket file for communicating with virtfs-proxy-helper. Usually a helper like libvirt will create socketpair and pass one of the fds as sock_fd
</dd><dt><b>sock_fd</b>
</dt><dd> Enables proxy filesystem driver to use passed 'sock_fd' as the socket descriptor for interfacing with virtfs-proxy-helper</dd></dl>
</dl>

<dl>
</dl>

<dt><b>-virtfs_synth</b>
</dt><dd> Create synthetic file system image</dd></dl>
 

 USB options:
<dl>
<dt><b>-usb</b>
</dt><dd> Enable the USB driver (will be the default soon)
</dd><dt><b>-usbdevice</b> <i>devname</i>
</dt><dd> Add the USB device <i>devname</i>.
</dd><dl>
<dl>
<dt><b>mouse</b>
</dt><dd> Virtual Mouse. This will override the PS/2 mouse emulation when activated.
</dd><dt><b>tablet</b>
</dt><dd> Pointer device that uses absolute coordinates (like a touchscreen). This means QEMU is able to report the mouse position without having to grab the mouse. Also overrides the PS/2 mouse emulation when activated.
</dd><dt><b>disk:[format=</b><i>format</i><b>]:</b><i>file</i>
</dt><dd> Mass storage device based on file. The optional <i>format</i> argument will be used rather than detecting the format. Can be used to specifiy <tt>&quot;format=raw&quot;</tt> to avoid interpreting an untrusted format header.
</dd><dt><b>host:</b><i>bus</i><b>.</b><i>addr</i>
</dt><dd> Pass through the host device identified by <i>bus</i>.<i>addr</i> (Linux only).
</dd><dt><b>host:</b><i>vendor_id</i><b>:</b><i>product_id</i>
</dt><dd> Pass through the host device identified by <i>vendor_id</i>:<i>product_id</i> (Linux only).
</dd><dt><b>serial:[vendorid=</b><i>vendor_id</i><b>][,productid=</b><i>product_id</i><b>]:</b><i>dev</i>
</dt><dd> Serial converter to host character device <i>dev</i>, see <tt>&quot;-serial&quot;</tt> for the available devices.
</dd><dt><b>braille</b>
</dt><dd> Braille device. This will use BrlAPI to display the braille output on a real or fake device.
</dd><dt><b>net:</b><i>options</i>
</dt><dd> Network adapter that supports CDC ethernet and RNDIS protocols.</dd></dl>
</dl>

<dl>
</dl>
</dl>
 

 Display options:
<dl>
<dt><b>-display</b> <i>type</i>
</dt><dd> Select type of display to use. This option is a replacement for the old style -sdl/-curses/... options. Valid values for <i>type</i> are
</dd><dl>
<dl>
<dt><b>sdl</b>
</dt><dd> Display video output via SDL (usually in a separate graphics window; see the SDL documentation for other possibilities).
</dd><dt><b>curses</b>
</dt><dd> Display video output via curses. For graphics device models which support a text mode, QEMU can display this output using a curses/ncurses interface. Nothing is displayed when the graphics device is in graphical mode or if the graphics device does not support a text mode. Generally only the VGA device models support text mode.
</dd><dt><b>none</b>
</dt><dd> Do not display video output. The guest will still see an emulated graphics card, but its output will not be displayed to the QEMU user. This option differs from the -nographic option in that it only affects what is done with video output; -nographic also changes the destination of the serial and parallel port data.
</dd><dt><b>vnc</b>
</dt><dd> Start a VNC server on display &lt;arg&gt;</dd></dl>
</dl>

<dl>
</dl>

<dt><b>-nographic</b>
</dt><dd> Normally, QEMU uses SDL to display the VGA output. With this option, you can totally disable graphical output so that QEMU is a simple command line application. The emulated serial port is redirected on the console. Therefore, you can still use QEMU to debug a Linux kernel with a serial console.
</dd><dt><b>-curses</b>
</dt><dd> Normally, QEMU uses SDL to display the VGA output. With this option, QEMU can display the VGA output when in text mode using a curses/ncurses interface. Nothing is displayed in graphical mode.
</dd><dt><b>-no-frame</b>
</dt><dd> Do not use decorations for SDL windows and start them using the whole available screen space. This makes the using QEMU in a dedicated desktop workspace more convenient.
</dd><dt><b>-alt-grab</b>
</dt><dd> Use Ctrl-Alt-Shift to grab mouse (instead of Ctrl-Alt). Note that this also affects the special keys (for fullscreen, monitor-mode switching, etc).
</dd><dt><b>-ctrl-grab</b>
</dt><dd> Use Right-Ctrl to grab mouse (instead of Ctrl-Alt). Note that this also affects the special keys (for fullscreen, monitor-mode switching, etc).
</dd><dt><b>-no-quit</b>
</dt><dd> Disable SDL window close capability.
</dd><dt><b>-sdl</b>
</dt><dd> Enable SDL.
</dd><dt><b>-spice</b> <i>option</i><b>[,</b><i>option</i><b>[,...]]</b>
</dt><dd> Enable the spice remote desktop protocol. Valid options are
</dd><dl>
<dl>
<dt><b>port=&lt;nr&gt;</b>
</dt><dd> Set the TCP port spice is listening on for plaintext channels.
</dd><dt><b>addr=&lt;addr&gt;</b>
</dt><dd> Set the IP address spice is listening on. Default is any address.
</dd><dt><b>ipv4</b>
</dt><dd>
</dd><dt><b>ipv6</b>
</dt><dd> Force using the specified IP version.
</dd><dt><b>password=&lt;secret&gt;</b>
</dt><dd> Set the password you need to authenticate.
</dd><dt><b>sasl</b>
</dt><dd> Require that the client use SASL to authenticate with the spice. The exact choice of authentication method used is controlled from the system / user's SASL configuration file for the 'qemu' service. This is typically found in /etc/sasl2/qemu.conf. If running QEMU as an unprivileged user, an environment variable SASL_CONF_PATH can be used to make it search alternate locations for the service config. While some SASL auth methods can also provide data encryption (eg GSSAPI), it is recommended that SASL always be combined with the 'tls' and 'x509' settings to enable use of SSL and server certificates. This ensures a data encryption preventing compromise of authentication credentials.
</dd><dt><b>disable-ticketing</b>
</dt><dd> Allow client connects without authentication.
</dd><dt><b>disable-copy-paste</b>
</dt><dd> Disable copy paste between the client and the guest.
</dd><dt><b>tls-port=&lt;nr&gt;</b>
</dt><dd> Set the TCP port spice is listening on for encrypted channels.
</dd><dt><b>x509-dir=&lt;dir&gt;</b>
</dt><dd> Set the x509 file directory. Expects same filenames as -vnc <tt>$display</tt>,x509=$dir
</dd><dt><b>x509-key-file=&lt;file&gt;</b>
</dt><dd>
</dd><dt><b>x509-key-password=&lt;file&gt;</b>
</dt><dd>
</dd><dt><b>x509-cert-file=&lt;file&gt;</b>
</dt><dd>
</dd><dt><b>x509-cacert-file=&lt;file&gt;</b>
</dt><dd>
</dd><dt><b>x509-dh-key-file=&lt;file&gt;</b>
</dt><dd> The x509 file names can also be configured individually.
</dd><dt><b>tls-ciphers=&lt;list&gt;</b>
</dt><dd> Specify which ciphers to use.
</dd><dt><b>tls-channel=[main|display|cursor|inputs|record|playback]</b>
</dt><dd>
</dd><dt><b>plaintext-channel=[main|display|cursor|inputs|record|playback]</b>
</dt><dd> Force specific channel to be used with or without TLS encryption. The options can be specified multiple times to configure multiple channels. The special name ``default'' can be used to set the default mode. For channels which are not explicitly forced into one mode the spice client is allowed to pick tls/plaintext as he pleases.
</dd><dt><b>image-compression=[auto_glz|auto_lz|quic|glz|lz|off]</b>
</dt><dd> Configure image compression (lossless). Default is auto_glz.
</dd><dt><b>jpeg-wan-compression=[auto|never|always]</b>
</dt><dd>
</dd><dt><b>zlib-glz-wan-compression=[auto|never|always]</b>
</dt><dd> Configure wan image compression (lossy for slow links). Default is auto.
</dd><dt><b>streaming-video=[off|all|filter]</b>
</dt><dd> Configure video stream detection. Default is filter.
</dd><dt><b>agent-mouse=[on|off]</b>
</dt><dd> Enable/disable passing mouse events via vdagent. Default is on.
</dd><dt><b>playback-compression=[on|off]</b>
</dt><dd> Enable/disable audio stream compression (using celt 0.5.1). Default is on.
</dd><dt><b>seamless-migration=[on|off]</b>
</dt><dd> Enable/disable spice seamless migration. Default is off.</dd></dl>
</dl>

<dl>
</dl>

<dt><b>-portrait</b>
</dt><dd> Rotate graphical output 90 deg left (only PXA LCD).
</dd><dt><b>-rotate</b> <i>deg</i>
</dt><dd> Rotate graphical output some deg left (only PXA LCD).
</dd><dt><b>-vga</b> <i>type</i>
</dt><dd> Select type of VGA card to emulate. Valid values for <i>type</i> are
</dd><dl>
<dl>
<dt><b>cirrus</b>
</dt><dd> Cirrus Logic GD5446 Video card. All Windows versions starting from Windows 95 should recognize and use this graphic card. For optimal performances, use 16 bit color depth in the guest and the host OS. (This one is the default)
</dd><dt><b>std</b>
</dt><dd> Standard VGA card with Bochs VBE extensions. If your guest OS supports the VESA 2.0 VBE extensions (e.g. Windows XP) and if you want to use high resolution modes (&gt;= 1280x1024x16) then you should use this option.
</dd><dt><b>vmware</b>
</dt><dd> VMWare SVGA-II compatible adapter. Use it if you have sufficiently recent XFree86/XOrg server or Windows guest with a driver for this card.
</dd><dt><b>qxl</b>
</dt><dd> QXL paravirtual graphic card. It is VGA compatible (including VESA 2.0 VBE support). Works best with qxl guest drivers installed though. Recommended choice when using the spice protocol.
</dd><dt><b>none</b>
</dt><dd> Disable VGA card.</dd></dl>
</dl>

<dl>
</dl>

<dt><b>-full-screen</b>
</dt><dd> Start in full screen.
</dd><dt><b>-g</b> <i>width</i><b>x</b><i>height</i><b>[x</b><i>depth</i><b>]</b>
</dt><dd> Set the initial graphical resolution and depth (PPC, SPARC only).
</dd><dt><b>-vnc</b> <i>display</i><b>[,</b><i>option</i><b>[,</b><i>option</i><b>[,...]]]</b>
</dt><dd> Normally, QEMU uses SDL to display the VGA output. With this option, you can have QEMU listen on VNC display <i>display</i> and redirect the VGA display over the VNC session. It is very useful to enable the usb tablet device when using this option (option <b>-usbdevice tablet</b>). When using the VNC display, you must use the <b>-k</b> parameter to set the keyboard layout if you are not using en-us. Valid syntax for the <i>display</i> is
</dd><dl>
<dl>
<dt><i>host</i><b>:</b><i>d</i>
</dt><dd> TCP connections will only be allowed from <i>host</i> on display <i>d</i>. By convention the TCP port is 5900+<i>d</i>. Optionally, <i>host</i> can be omitted in which case the server will accept connections from any host.
</dd><dt><b>unix:</b><i>path</i>
</dt><dd> Connections will be allowed over UNIX domain sockets where <i>path</i> is the location of a unix socket to listen for connections on.
</dd><dt><b>none</b>
</dt><dd> VNC is initialized but not started. The monitor <tt>&quot;change&quot;</tt> command can be used to later start the VNC server.</dd></dl>
</dl>

<dl>
<dt>
</dt><dd> 
 Following the <i>display</i> value there may be one or more <i>option</i> flags separated by commas. Valid options are
</dd><dl>
<dt><b>reverse</b>
</dt><dd> Connect to a listening VNC client via a ``reverse'' connection. The client is specified by the <i>display</i>. For reverse network connections (<i>host</i>:<i>d</i>,<tt>&quot;reverse&quot;</tt>), the <i>d</i> argument is a TCP port number, not a display number.
</dd><dt><b>websocket</b>
</dt><dd> Opens an additional TCP listening port dedicated to VNC Websocket connections. By definition the Websocket port is 5700+<i>display</i>. If <i>host</i> is specified connections will only be allowed from this host. As an alternative the Websocket port could be specified by using <tt>&quot;websocket&quot;</tt>=<i>port</i>. TLS encryption for the Websocket connection is supported if the required certificates are specified with the VNC option <b>x509</b>.
</dd><dt><b>password</b>
</dt><dd> Require that password based authentication is used for client connections. 
 The password must be set separately using the <tt>&quot;set_password&quot;</tt> command in the <b>pcsys_monitor</b>. The syntax to change your password is: <tt>&quot;set_password &lt;protocol&gt; &lt;password&gt;&quot;</tt> where &lt;protocol&gt; could be either ``vnc'' or ``spice''. 
 If you would like to change &lt;protocol&gt; password expiration, you should use <tt>&quot;expire_password &lt;protocol&gt; &lt;expiration-time&gt;&quot;</tt> where expiration time could be one of the following options: now, never, +seconds or UNIX time of expiration, e.g. +60 to make password expire in 60 seconds, or 1335196800 to make password expire on ``Mon Apr 23 12:00:00 EDT 2012'' (UNIX time for this date and time). 
 You can also use keywords ``now'' or ``never'' for the expiration time to allow &lt;protocol&gt; password to expire immediately or never expire.
</dd><dt><b>tls</b>
</dt><dd> Require that client use TLS when communicating with the VNC server. This uses anonymous TLS credentials so is susceptible to a man-in-the-middle attack. It is recommended that this option be combined with either the <b>x509</b> or <b>x509verify</b> options.
</dd><dt><b>x509=</b><i>/path/to/certificate/dir</i>
</dt><dd> Valid if <b>tls</b> is specified. Require that x509 credentials are used for negotiating the TLS session. The server will send its x509 certificate to the client. It is recommended that a password be set on the VNC server to provide authentication of the client when this is used. The path following this option specifies where the x509 certificates are to be loaded from. See the <b>vnc_security</b> section for details on generating certificates.
</dd><dt><b>x509verify=</b><i>/path/to/certificate/dir</i>
</dt><dd> Valid if <b>tls</b> is specified. Require that x509 credentials are used for negotiating the TLS session. The server will send its x509 certificate to the client, and request that the client send its own x509 certificate. The server will validate the client's certificate against the CA certificate, and reject clients when validation fails. If the certificate authority is trusted, this is a sufficient authentication mechanism. You may still wish to set a password on the VNC server as a second authentication layer. The path following this option specifies where the x509 certificates are to be loaded from. See the <b>vnc_security</b> section for details on generating certificates.
</dd><dt><b>sasl</b>
</dt><dd> Require that the client use SASL to authenticate with the VNC server. The exact choice of authentication method used is controlled from the system / user's SASL configuration file for the 'qemu' service. This is typically found in /etc/sasl2/qemu.conf. If running QEMU as an unprivileged user, an environment variable SASL_CONF_PATH can be used to make it search alternate locations for the service config. While some SASL auth methods can also provide data encryption (eg GSSAPI), it is recommended that SASL always be combined with the 'tls' and 'x509' settings to enable use of SSL and server certificates. This ensures a data encryption preventing compromise of authentication credentials. See the <b>vnc_security</b> section for details on using SASL authentication.
</dd><dt><b>acl</b>
</dt><dd> Turn on access control lists for checking of the x509 client certificate and SASL party. For x509 certs, the ACL check is made against the certificate's distinguished name. This is something that looks like <tt>&quot;C=GB,O=ACME,L=Boston,CN=bob&quot;</tt>. For SASL party, the ACL check is made against the username, which depending on the SASL plugin, may include a realm component, eg <tt>&quot;bob&quot;</tt> or <tt>&quot;bob [at] EXAMPLE.COM&quot;</tt>. When the <b>acl</b> flag is set, the initial access list will be empty, with a <tt>&quot;deny&quot;</tt> policy. Thus no one will be allowed to use the VNC server until the ACLs have been loaded. This can be achieved using the <tt>&quot;acl&quot;</tt> monitor command.
</dd><dt><b>lossy</b>
</dt><dd> Enable lossy compression methods (gradient, JPEG, ...). If this option is set, VNC client may receive lossy framebuffer updates depending on its encoding settings. Enabling this option can save a lot of bandwidth at the expense of quality.
</dd><dt><b>non-adaptive</b>
</dt><dd> Disable adaptive encodings. Adaptive encodings are enabled by default. An adaptive encoding will try to detect frequently updated screen regions, and send updates in these regions using a lossy encoding (like JPEG). This can be really helpful to save bandwidth when playing videos. Disabling adaptive encodings allows to restore the original static behavior of encodings like Tight.
</dd><dt><b>share=[allow-exclusive|force-shared|ignore]</b>
</dt><dd> Set display sharing policy. 'allow-exclusive' allows clients to ask for exclusive access. As suggested by the rfb spec this is implemented by dropping other connections. Connecting multiple clients in parallel requires all clients asking for a shared session (vncviewer: -shared switch). This is the default. 'force-shared' disables exclusive client access. Useful for shared desktop sessions, where you don't want someone forgetting specify -shared disconnect everybody else. 'ignore' completely ignores the shared flag and allows everybody connect unconditionally. Doesn't conform to the rfb spec but is traditional QEMU behavior.</dd></dl>
</dl>

<dl>
</dl>
</dl>
 

 i386 target only:
<dl>
<dt><b>-win2k-hack</b>
</dt><dd> Use it when installing Windows 2000 to avoid a disk full bug. After Windows 2000 is installed, you no longer need this option (this option slows down the IDE transfers).
</dd><dt><b>-no-fd-bootchk</b>
</dt><dd> Disable boot signature checking for floppy disks in BIOS. May be needed to boot from old floppy disks.
</dd><dt><b>-no-acpi</b>
</dt><dd> Disable ACPI (Advanced Configuration and Power Interface) support. Use it if your guest OS complains about ACPI problems (PC target machine only).
</dd><dt><b>-acpitable [sig=</b><i>str</i><b>][,rev=</b><i>n</i><b>][,oem_id=</b><i>str</i><b>][,oem_table_id=</b><i>str</i><b>][,oem_rev=</b><i>n</i><b>] [,asl_compiler_id=</b><i>str</i><b>][,asl_compiler_rev=</b><i>n</i><b>][,data=</b><i>file1</i><b>[:</b><i>file2</i><b>]...]</b>
</dt><dd> Add ACPI table with specified header fields and context from specified files. For file=, take whole ACPI table from the specified files, including all ACPI headers (possible overridden by other options). For data=, only data portion of the table is used, all header information is specified in the command line. If a SLIC table is supplied to QEMU, then the SLIC's oem_id and oem_table_id fields will override the same in the RSDT and the FADT (a.k.a. FACP), in order to ensure the field matches required by the Microsoft SLIC spec and the ACPI spec.
</dd><dt><b>-smbios file=</b><i>binary</i>
</dt><dd> Load SMBIOS entry from binary file.
</dd><dt><b>-smbios type=0[,vendor=</b><i>str</i><b>][,version=</b><i>str</i><b>][,date=</b><i>str</i><b>][,release=</b><i>%d.%d</i><b>]</b>
</dt><dd> Specify SMBIOS type 0 fields
</dd><dt><b>-smbios type=1[,manufacturer=</b><i>str</i><b>][,product=</b><i>str</i><b>] [,version=</b><i>str</i><b>][,serial=</b><i>str</i><b>][,uuid=</b><i>uuid</i><b>][,sku=</b><i>str</i><b>] [,family=</b><i>str</i><b>]</b>
</dt><dd> Specify SMBIOS type 1 fields</dd></dl>
 

 Network options:
<dl>
<dt><b>-net nic[,vlan=</b><i>n</i><b>][,macaddr=</b><i>mac</i><b>][,model=</b><i>type</i><b>] [,name=</b><i>name</i><b>][,addr=</b><i>addr</i><b>][,vectors=</b><i>v</i><b>]</b>
</dt><dd> Create a new Network Interface Card and connect it to VLAN <i>n</i> (<i>n</i> = 0 is the default). The NIC is an e1000 by default on the PC target. Optionally, the MAC address can be changed to <i>mac</i>, the device address set to <i>addr</i> (PCI cards only), and a <i>name</i> can be assigned for use in monitor commands. Optionally, for PCI cards, you can specify the number <i>v</i> of MSI-X vectors that the card should have; this option currently only affects virtio cards; set <i>v</i> = 0 to disable MSI-X. If no <b>-net</b> option is specified, a single NIC is created. QEMU can emulate several different models of network card. Valid values for <i>type</i> are <tt>&quot;virtio&quot;</tt>, <tt>&quot;i82551&quot;</tt>, <tt>&quot;i82557b&quot;</tt>, <tt>&quot;i82559er&quot;</tt>, <tt>&quot;ne2k_pci&quot;</tt>, <tt>&quot;ne2k_isa&quot;</tt>, <tt>&quot;pcnet&quot;</tt>, <tt>&quot;rtl8139&quot;</tt>, <tt>&quot;e1000&quot;</tt>, <tt>&quot;smc91c111&quot;</tt>, <tt>&quot;lance&quot;</tt> and <tt>&quot;mcf_fec&quot;</tt>. Not all devices are supported on all targets. Use <tt>&quot;-net nic,model=help&quot;</tt> for a list of available devices for your target.
</dd><dt><b>-netdev user,id=</b><i>id</i><b>[,</b><i>option</i><b>][,</b><i>option</i><b>][,...]</b>
</dt><dd>
</dd><dt><b>-net user[,</b><i>option</i><b>][,</b><i>option</i><b>][,...]</b>
</dt><dd> Use the user mode network stack which requires no administrator privilege to run. Valid options are:
</dd><dl>
<dl>
<dt><b>vlan=</b><i>n</i>
</dt><dd> Connect user mode stack to VLAN <i>n</i> (<i>n</i> = 0 is the default).
</dd><dt><b>id=</b><i>id</i>
</dt><dd>
</dd><dt><b>name=</b><i>name</i>
</dt><dd> Assign symbolic name for use in monitor commands.
</dd><dt><b>net=</b><i>addr</i><b>[/</b><i>mask</i><b>]</b>
</dt><dd> Set IP network address the guest will see. Optionally specify the netmask, either in the form a.b.c.d or as number of valid top-most bits. Default is 10.0.2.0/24.
</dd><dt><b>host=</b><i>addr</i>
</dt><dd> Specify the guest-visible address of the host. Default is the 2nd IP in the guest network, i.e. x.x.x.2.
</dd><dt><b>restrict=on|off</b>
</dt><dd> If this option is enabled, the guest will be isolated, i.e. it will not be able to contact the host and no guest IP packets will be routed over the host to the outside. This option does not affect any explicitly set forwarding rules.
</dd><dt><b>hostname=</b><i>name</i>
</dt><dd> Specifies the client hostname reported by the built-in DHCP server.
</dd><dt><b>dhcpstart=</b><i>addr</i>
</dt><dd> Specify the first of the 16 IPs the built-in DHCP server can assign. Default is the 15th to 31st IP in the guest network, i.e. x.x.x.15 to x.x.x.31.
</dd><dt><b>dns=</b><i>addr</i>
</dt><dd> Specify the guest-visible address of the virtual nameserver. The address must be different from the host address. Default is the 3rd IP in the guest network, i.e. x.x.x.3.
</dd><dt><b>dnssearch=</b><i>domain</i>
</dt><dd> Provides an entry for the domain-search list sent by the built-in DHCP server. More than one domain suffix can be transmitted by specifying this option multiple times. If supported, this will cause the guest to automatically try to append the given domain suffix(es) in case a domain name can not be resolved. 
 Example: 
 <pre>
        qemu-kvm -net user,dnssearch=mgmt.example.org,dnssearch=example.org [...]
</pre>
</dd><dt><b>tftp=</b><i>dir</i>
</dt><dd> When using the user mode network stack, activate a built-in TFTP server. The files in <i>dir</i> will be exposed as the root of a TFTP server. The TFTP client on the guest must be configured in binary mode (use the command <tt>&quot;bin&quot;</tt> of the Unix TFTP client).
</dd><dt><b>bootfile=</b><i>file</i>
</dt><dd> When using the user mode network stack, broadcast <i>file</i> as the BOOTP filename. In conjunction with <b>tftp</b>, this can be used to network boot a guest from a local directory. 
 Example (using pxelinux): 
 <pre>
        qemu-kvm -hda linux.img -boot n -net user,tftp=/path/to/tftp/files,bootfile=/pxelinux.0
</pre>
</dd><dt><b>smb=</b><i>dir</i><b>[,smbserver=</b><i>addr</i><b>]</b>
</dt><dd> When using the user mode network stack, activate a built-in SMB server so that Windows OSes can access to the host files in <i>dir</i> transparently. The IP address of the SMB server can be set to <i>addr</i>. By default the 4th IP in the guest network is used, i.e. x.x.x.4. 
 In the guest Windows OS, the line: 
 <pre>
        10.0.2.4 smbserver
</pre> 
 must be added in the file <i>C:\WINDOWS\LMHOSTS</i> (for windows 9x/Me) or <i>C:\WINNT\SYSTEM32\DRIVERS\ETC\LMHOSTS</i> (Windows NT/2000). 
 Then <i>dir</i> can be accessed in <i>\\smbserver\qemu</i>. 
 Note that a SAMBA server must be installed on the host OS. QEMU was tested successfully with smbd versions from Red Hat 9, Fedora Core 3 and OpenSUSE 11.x.
</dd><dt><b>hostfwd=[tcp|udp]:[</b><i>hostaddr</i><b>]:</b><i>hostport</i><b>-[</b><i>guestaddr</i><b>]:</b><i>guestport</i>
</dt><dd> Redirect incoming TCP or UDP connections to the host port <i>hostport</i> to the guest IP address <i>guestaddr</i> on guest port <i>guestport</i>. If <i>guestaddr</i> is not specified, its value is x.x.x.15 (default first address given by the built-in DHCP server). By specifying <i>hostaddr</i>, the rule can be bound to a specific host interface. If no connection type is set, TCP is used. This option can be given multiple times. 
 For example, to redirect host X11 connection from screen 1 to guest screen 0, use the following: 
 <pre>
        # on the host
        qemu-kvm -net user,hostfwd=tcp:127.0.0.1:6001-:6000 [...]
        # this host xterm should open in the guest X11 server
        xterm -display :1
</pre> 
 To redirect telnet connections from host port 5555 to telnet port on the guest, use the following: 
 <pre>
        # on the host
        qemu-kvm -net user,hostfwd=tcp::5555-:23 [...]
        telnet localhost 5555
</pre> 
 Then when you use on the host <tt>&quot;telnet localhost 5555&quot;</tt>, you connect to the guest telnet server.
</dd><dt><b>guestfwd=[tcp]:</b><i>server</i><b>:</b><i>port</i><b>-</b><i>dev</i>
</dt><dd>
</dd><dt><b>guestfwd=[tcp]:</b><i>server</i><b>:</b><i>port</i><b>-</b><i>cmd:command</i>
</dt><dd> Forward guest TCP connections to the IP address <i>server</i> on port <i>port</i> to the character device <i>dev</i> or to a program executed by <i>cmd:command</i> which gets spawned for each connection. This option can be given multiple times. 
 You can either use a chardev directly and have that one used throughout QEMU's lifetime, like in the following example: 
 <pre>
        # open 10.10.1.1:4321 on bootup, connect 10.0.2.100:1234 to it whenever
        # the guest accesses it
        qemu-kvm -net user,guestfwd=tcp:10.0.2.100:1234-tcp:10.10.1.1:4321 [...]
</pre> 
 Or you can execute a command on every TCP connection established by the guest, so that QEMU behaves similar to an inetd process for that virtual server: 
 <pre>
        # call &quot;netcat 10.10.1.1 4321&quot; on every TCP connection to 10.0.2.100:1234
        # and connect the TCP stream to its stdin/stdout
        qemu-kvm -net 'user,guestfwd=tcp:10.0.2.100:1234-cmd:netcat 10.10.1.1 4321'
</pre></dd></dl>
</dl>

<dl>
<dt>
</dt><dd> 
 Note: Legacy stand-alone options -tftp, -bootp, -smb and -redir are still processed and applied to -net user. Mixing them with the new configuration syntax gives undefined results. Their use for new applications is discouraged as they will be removed from future versions.</dd></dl>

<dt><b>-netdev tap,id=</b><i>id</i><b>[,fd=</b><i>h</i><b>][,ifname=</b><i>name</i><b>][,script=</b><i>file</i><b>][,downscript=</b><i>dfile</i><b>][,helper=</b><i>helper</i><b>]</b>
</dt><dd>
</dd><dt><b>-net tap[,vlan=</b><i>n</i><b>][,name=</b><i>name</i><b>][,fd=</b><i>h</i><b>][,ifname=</b><i>name</i><b>][,script=</b><i>file</i><b>][,downscript=</b><i>dfile</i><b>][,helper=</b><i>helper</i><b>]</b>
</dt><dd> Connect the host TAP network interface <i>name</i> to VLAN <i>n</i>. 

 Use the network script <i>file</i> to configure it and the network script <i>dfile</i> to deconfigure it. If <i>name</i> is not provided, the OS automatically provides one. The default network configure script is <i>/etc/qemu-ifup</i> and the default network deconfigure script is <i>/etc/qemu-ifdown</i>. Use <b>script=no</b> or <b>downscript=no</b> to disable script execution. 

 If running QEMU as an unprivileged user, use the network helper <i>helper</i> to configure the TAP interface. The default network helper executable is <i>/path/to/qemu-bridge-helper</i>. 

 <b>fd</b>=<i>h</i> can be used to specify the handle of an already opened host TAP interface. 

 Examples: 

 <pre>
        #launch a QEMU instance with the default network script
        qemu-kvm linux.img -net nic -net tap
        #launch a QEMU instance with two NICs, each one connected
        #to a TAP device
        qemu-kvm linux.img \
        -net nic,vlan=0 -net tap,vlan=0,ifname=tap0 \
        -net nic,vlan=1 -net tap,vlan=1,ifname=tap1
        #launch a QEMU instance with the default network helper to
        #connect a TAP device to bridge br0
        qemu-kvm linux.img \
        -net nic -net tap,&quot;helper=/path/to/qemu-bridge-helper&quot;
</pre>
</dd><dt><b>-netdev bridge,id=</b><i>id</i><b>[,br=</b><i>bridge</i><b>][,helper=</b><i>helper</i><b>]</b>
</dt><dd>
</dd><dt><b>-net bridge[,vlan=</b><i>n</i><b>][,name=</b><i>name</i><b>][,br=</b><i>bridge</i><b>][,helper=</b><i>helper</i><b>]</b>
</dt><dd> Connect a host TAP network interface to a host bridge device. 

 Use the network helper <i>helper</i> to configure the TAP interface and attach it to the bridge. The default network helper executable is <i>/path/to/qemu-bridge-helper</i> and the default bridge device is <i>br0</i>. 

 Examples: 

 <pre>
        #launch a QEMU instance with the default network helper to
        #connect a TAP device to bridge br0
        qemu-kvm linux.img -net bridge -net nic,model=virtio
        #launch a QEMU instance with the default network helper to
        #connect a TAP device to bridge qemubr0
        qemu-kvm linux.img -net bridge,br=qemubr0 -net nic,model=virtio
</pre>
</dd><dt><b>-netdev socket,id=</b><i>id</i><b>[,fd=</b><i>h</i><b>][,listen=[</b><i>host</i><b>]:</b><i>port</i><b>][,connect=</b><i>host</i><b>:</b><i>port</i><b>]</b>
</dt><dd>
</dd><dt><b>-net socket[,vlan=</b><i>n</i><b>][,name=</b><i>name</i><b>][,fd=</b><i>h</i><b>] [,listen=[</b><i>host</i><b>]:</b><i>port</i><b>][,connect=</b><i>host</i><b>:</b><i>port</i><b>]</b>
</dt><dd> Connect the VLAN <i>n</i> to a remote VLAN in another QEMU virtual machine using a TCP socket connection. If <b>listen</b> is specified, QEMU waits for incoming connections on <i>port</i> (<i>host</i> is optional). <b>connect</b> is used to connect to another QEMU instance using the <b>listen</b> option. <b>fd</b>=<i>h</i> specifies an already opened TCP socket. 

 Example: 

 <pre>
        # launch a first QEMU instance
        qemu-kvm linux.img \
        -net nic,macaddr=52:54:00:12:34:56 \
        -net socket,listen=:1234
        # connect the VLAN 0 of this instance to the VLAN 0
        # of the first instance
        qemu-kvm linux.img \
        -net nic,macaddr=52:54:00:12:34:57 \
        -net socket,connect=127.0.0.1:1234
</pre>
</dd><dt><b>-netdev socket,id=</b><i>id</i><b>[,fd=</b><i>h</i><b>][,mcast=</b><i>maddr</i><b>:</b><i>port</i><b>[,localaddr=</b><i>addr</i><b>]]</b>
</dt><dd>
</dd><dt><b>-net socket[,vlan=</b><i>n</i><b>][,name=</b><i>name</i><b>][,fd=</b><i>h</i><b>][,mcast=</b><i>maddr</i><b>:</b><i>port</i><b>[,localaddr=</b><i>addr</i><b>]]</b>
</dt><dd> Create a VLAN <i>n</i> shared with another QEMU virtual machines using a UDP multicast socket, effectively making a bus for every QEMU with same multicast address <i>maddr</i> and <i>port</i>. NOTES:
</dd><dl>
<dl>
<dt>1.
</dt><dd> Several QEMU can be running on different hosts and share same bus (assuming correct multicast setup for these hosts).
</dd><dt>2.
</dt><dd> mcast support is compatible with User Mode Linux (argument <b>eth</b><i>N</i><b>=mcast</b>), see &lt;<b><a rel="nofollow" HREF="http://user-mode-linux.sf.net">http://user-mode-linux.sf.net</a></b>&gt;.
</dd><dt>3.
</dt><dd> Use <b>fd=h</b> to specify an already opened UDP multicast socket.</dd></dl>
</dl>

<dl>
<dt>
</dt><dd> 
 Example: 
 <pre>
        # launch one QEMU instance
        qemu-kvm linux.img \
        -net nic,macaddr=52:54:00:12:34:56 \
        -net socket,mcast=230.0.0.1:1234
        # launch another QEMU instance on same &quot;bus&quot;
        qemu-kvm linux.img \
        -net nic,macaddr=52:54:00:12:34:57 \
        -net socket,mcast=230.0.0.1:1234
        # launch yet another QEMU instance on same &quot;bus&quot;
        qemu-kvm linux.img \
        -net nic,macaddr=52:54:00:12:34:58 \
        -net socket,mcast=230.0.0.1:1234
</pre> 
 Example (User Mode Linux compat.): 
 <pre>
        # launch QEMU instance (note mcast address selected
        # is UML's default)
        qemu-kvm linux.img \
        -net nic,macaddr=52:54:00:12:34:56 \
        -net socket,mcast=239.192.168.1:1102
        # launch UML
        /path/to/linux ubd0=/path/to/root_fs eth0=mcast
</pre> 
 Example (send packets from host's 1.2.3.4): 
 <pre>
        qemu-kvm linux.img \
        -net nic,macaddr=52:54:00:12:34:56 \
        -net socket,mcast=239.192.168.1:1102,localaddr=1.2.3.4
</pre></dd></dl>

<dt><b>-netdev vde,id=</b><i>id</i><b>[,sock=</b><i>socketpath</i><b>][,port=</b><i>n</i><b>][,group=</b><i>groupname</i><b>][,mode=</b><i>octalmode</i><b>]</b>
</dt><dd>
</dd><dt><b>-net vde[,vlan=</b><i>n</i><b>][,name=</b><i>name</i><b>][,sock=</b><i>socketpath</i><b>] [,port=</b><i>n</i><b>][,group=</b><i>groupname</i><b>][,mode=</b><i>octalmode</i><b>]</b>
</dt><dd> Connect VLAN <i>n</i> to PORT <i>n</i> of a vde switch running on host and listening for incoming connections on <i>socketpath</i>. Use GROUP <i>groupname</i> and MODE <i>octalmode</i> to change default ownership and permissions for communication port. This option is only available if QEMU has been compiled with vde support enabled. 

 Example: 

 <pre>
        # launch vde switch
        vde_switch -F -sock /tmp/myswitch
        # launch QEMU instance
        qemu-kvm linux.img -net nic -net vde,sock=/tmp/myswitch
</pre>
</dd><dt><b>-netdev hubport,id=</b><i>id</i><b>,hubid=</b><i>hubid</i>
</dt><dd> Create a hub port on QEMU ``vlan'' <i>hubid</i>. 

 The hubport netdev lets you connect a NIC to a QEMU ``vlan'' instead of a single netdev. <tt>&quot;-net&quot;</tt> and <tt>&quot;-device&quot;</tt> with parameter <b>vlan</b> create the required hub automatically.
</dd><dt><b>-net dump[,vlan=</b><i>n</i><b>][,file=</b><i>file</i><b>][,len=</b><i>len</i><b>]</b>
</dt><dd> Dump network traffic on VLAN <i>n</i> to file <i>file</i> (<i>qemu-vlan0.pcap</i> by default). At most <i>len</i> bytes (64k by default) per packet are stored. The file format is libpcap, so it can be analyzed with tools such as tcpdump or Wireshark.
</dd><dt><b>-net none</b>
</dt><dd> Indicate that no network devices should be configured. It is used to override the default configuration (<b>-net nic -net user</b>) which is activated if no <b>-net</b> options are provided.</dd></dl>
 

 Character device options: 

 The general form of a character device option is:
<dl>
<dt><b>-chardev</b> <i>backend</i> <b>,id=</b><i>id</i> <b>[,mux=on|off] [,</b><i>options</i><b>]</b>
</dt><dd> Backend is one of: <b>null</b>, <b>socket</b>, <b>udp</b>, <b>msmouse</b>, <b>vc</b>, <b>ringbuf</b>, <b>file</b>, <b>pipe</b>, <b>console</b>, <b>serial</b>, <b>pty</b>, <b>stdio</b>, <b>braille</b>, <b>tty</b>, <b>parallel</b>, <b>parport</b>, <b>spicevmc</b>. <b>spiceport</b>. The specific backend will determine the applicable options. 
 All devices must have an id, which can be any string up to 127 characters long. It is used to uniquely identify this device in other command line directives. 
 A character device may be used in multiplexing mode by multiple front-ends. The key sequence of <b>Control-a</b> and <b>c</b> will rotate the input focus between attached front-ends. Specify <b>mux=on</b> to enable this mode. 
 Options to each backend are described below.
</dd><dt><b>-chardev null ,id=</b><i>id</i>
</dt><dd> A void device. This device will not emit any data, and will drop any data it receives. The null backend does not take any options.
</dd><dt><b>-chardev socket ,id=</b><i>id</i> <b>[</b><i></i><i>TCP</i><i> options</i> <b>or</b> <i>unix options</i><b>] [,server] [,nowait] [,telnet]</b>
</dt><dd> Create a two-way stream socket, which can be either a TCP or a unix socket. A unix socket will be created if <b>path</b> is specified. Behaviour is undefined if TCP options are specified for a unix socket. 
 <b>server</b> specifies that the socket shall be a listening socket. 
 <b>nowait</b> specifies that QEMU should not block waiting for a client to connect to a listening socket. 
 <b>telnet</b> specifies that traffic on the socket should interpret telnet escape sequences. 
 TCP and unix socket options are given below:
</dd><dl>
<dl>
<dt><b>TCP</b><b> options: port=</b><i>port</i> <b>[,host=</b><i>host</i><b>] [,to=</b><i>to</i><b>] [,ipv4] [,ipv6] [,nodelay]</b>
</dt><dd> <b>host</b> for a listening socket specifies the local address to be bound. For a connecting socket species the remote host to connect to. <b>host</b> is optional for listening sockets. If not specified it defaults to <tt>0.0.0.0</tt>. 
 <b>port</b> for a listening socket specifies the local port to be bound. For a connecting socket specifies the port on the remote host to connect to. <b>port</b> can be given as either a port number or a service name. <b>port</b> is required. 
 <b>to</b> is only relevant to listening sockets. If it is specified, and <b>port</b> cannot be bound, QEMU will attempt to bind to subsequent ports up to and including <b>to</b> until it succeeds. <b>to</b> must be specified as a port number. 
 <b>ipv4</b> and <b>ipv6</b> specify that either IPv4 or IPv6 must be used. If neither is specified the socket may use either protocol. 
 <b>nodelay</b> disables the Nagle algorithm.
</dd><dt><b>unix options: path=</b><i>path</i>
</dt><dd> <b>path</b> specifies the local path of the unix socket. <b>path</b> is required.</dd></dl>
</dl>

<dl>
</dl>

<dt><b>-chardev udp ,id=</b><i>id</i> <b>[,host=</b><i>host</i><b>] ,port=</b><i>port</i> <b>[,localaddr=</b><i>localaddr</i><b>] [,localport=</b><i>localport</i><b>] [,ipv4] [,ipv6]</b>
</dt><dd> Sends all traffic from the guest to a remote host over UDP. 

 <b>host</b> specifies the remote host to connect to. If not specified it defaults to <tt>&quot;localhost&quot;</tt>. 

 <b>port</b> specifies the port on the remote host to connect to. <b>port</b> is required. 

 <b>localaddr</b> specifies the local address to bind to. If not specified it defaults to <tt>0.0.0.0</tt>. 

 <b>localport</b> specifies the local port to bind to. If not specified any available local port will be used. 

 <b>ipv4</b> and <b>ipv6</b> specify that either IPv4 or IPv6 must be used. If neither is specified the device may use either protocol.
</dd><dt><b>-chardev msmouse ,id=</b><i>id</i>
</dt><dd> Forward QEMU's emulated msmouse events to the guest. <b>msmouse</b> does not take any options.
</dd><dt><b>-chardev vc ,id=</b><i>id</i> <b>[[,width=</b><i>width</i><b>] [,height=</b><i>height</i><b>]] [[,cols=</b><i>cols</i><b>] [,rows=</b><i>rows</i><b>]]</b>
</dt><dd> Connect to a QEMU text console. <b>vc</b> may optionally be given a specific size. 

 <b>width</b> and <b>height</b> specify the width and height respectively of the console, in pixels. 

 <b>cols</b> and <b>rows</b> specify that the console be sized to fit a text console with the given dimensions.
</dd><dt><b>-chardev ringbuf ,id=</b><i>id</i> <b>[,size=</b><i>size</i><b>]</b>
</dt><dd> Create a ring buffer with fixed size <b>size</b>. <i>size</i> must be a power of two, and defaults to <tt>&quot;64K&quot;</tt>).
</dd><dt><b>-chardev file ,id=</b><i>id</i> <b>,path=</b><i>path</i>
</dt><dd> Log all traffic received from the guest to a file. 

 <b>path</b> specifies the path of the file to be opened. This file will be created if it does not already exist, and overwritten if it does. <b>path</b> is required.
</dd><dt><b>-chardev pipe ,id=</b><i>id</i> <b>,path=</b><i>path</i>
</dt><dd> Create a two-way connection to the guest. The behaviour differs slightly between Windows hosts and other hosts: 

 On Windows, a single duplex pipe will be created at <i>\\.pipe\</i>path<i></i>. 

 On other hosts, 2 pipes will be created called <i></i>path<i>.in</i> and <i></i>path<i>.out</i>. Data written to <i></i>path<i>.in</i> will be received by the guest. Data written by the guest can be read from <i></i>path<i>.out</i>. QEMU will not create these fifos, and requires them to be present. 

 <b>path</b> forms part of the pipe path as described above. <b>path</b> is required.
</dd><dt><b>-chardev console ,id=</b><i>id</i>
</dt><dd> Send traffic from the guest to QEMU's standard output. <b>console</b> does not take any options. 

 <b>console</b> is only available on Windows hosts.
</dd><dt><b>-chardev serial ,id=</b><i>id</i> <b>,path=</b><b>path</b>
</dt><dd> Send traffic from the guest to a serial device on the host. 

 On Unix hosts serial will actually accept any tty device, not only serial lines. 

 <b>path</b> specifies the name of the serial device to open.
</dd><dt><b>-chardev pty ,id=</b><i>id</i>
</dt><dd> Create a new pseudo-terminal on the host and connect to it. <b>pty</b> does not take any options. 

 <b>pty</b> is not available on Windows hosts.
</dd><dt><b>-chardev stdio ,id=</b><i>id</i> <b>[,signal=on|off]</b>
</dt><dd> Connect to standard input and standard output of the QEMU process. 

 <b>signal</b> controls if signals are enabled on the terminal, that includes exiting QEMU with the key sequence <b>Control-c</b>. This option is enabled by default, use <b>signal=off</b> to disable it. 

 <b>stdio</b> is not available on Windows hosts.
</dd><dt><b>-chardev braille ,id=</b><i>id</i>
</dt><dd> Connect to a local BrlAPI server. <b>braille</b> does not take any options.
</dd><dt><b>-chardev tty ,id=</b><i>id</i> <b>,path=</b><i>path</i>
</dt><dd> <b>tty</b> is only available on Linux, Sun, FreeBSD, NetBSD, OpenBSD and DragonFlyBSD hosts. It is an alias for <b>serial</b>. 

 <b>path</b> specifies the path to the tty. <b>path</b> is required.
</dd><dt><b>-chardev parallel ,id=</b><i>id</i> <b>,path=</b><i>path</i>
</dt><dd>
</dd><dt><b>-chardev parport ,id=</b><i>id</i> <b>,path=</b><i>path</i>
</dt><dd> <b>parallel</b> is only available on Linux, FreeBSD and DragonFlyBSD hosts. 

 Connect to a local parallel port. 

 <b>path</b> specifies the path to the parallel port device. <b>path</b> is required.
</dd><dt><b>-chardev spicevmc ,id=</b><i>id</i> <b>,debug=</b><i>debug</i><b>, name=</b><i>name</i>
</dt><dd> <b>spicevmc</b> is only available when spice support is built in. 

 <b>debug</b> debug level for spicevmc 

 <b>name</b> name of spice channel to connect to 

 Connect to a spice virtual machine channel, such as vdiport.
</dd><dt><b>-chardev spiceport ,id=</b><i>id</i> <b>,debug=</b><i>debug</i><b>, name=</b><i>name</i>
</dt><dd> <b>spiceport</b> is only available when spice support is built in. 

 <b>debug</b> debug level for spicevmc 

 <b>name</b> name of spice port to connect to 

 Connect to a spice port, allowing a Spice client to handle the traffic identified by a name (preferably a fqdn).</dd></dl>
 

 Device URL Syntax: 

 In addition to using normal file images for the emulated storage devices, QEMU can also use networked resources such as iSCSI devices. These are specified using a special URL syntax.
<dl>
<dt><b>iSCSI</b>
</dt><dd> iSCSI support allows QEMU to access iSCSI resources directly and use as images for the guest storage. Both disk and cdrom images are supported. 
 Syntax for specifying iSCSI LUNs is ``iscsi://&lt;target-ip&gt;[:&lt;port&gt;]/&lt;target-iqn&gt;/&lt;lun&gt;'' 
 By default qemu-kvm will use the iSCSI initiator-name 'iqn.2008-11.org.linux-kvm[:&lt;name&gt;]' but this can also be set from the command line or a configuration file. 
 Example (without authentication): 
 <pre>
        qemu-kvm -iscsi initiator-name=iqn.2001-04.com.example:my-initiator \
        -cdrom <a HREF="iscsi://192.0.2.1/iqn.2001-04.com.example/2">iscsi://192.0.2.1/iqn.2001-04.com.example/2</a> \
        -drive file=<a HREF="iscsi://192.0.2.1/iqn.2001-04.com.example/1">iscsi://192.0.2.1/iqn.2001-04.com.example/1</a>
</pre> 
 Example (CHAP username/password via URL): 
 <pre>
        qemu-kvm -drive file=<a HREF="iscsi://user%password@192.0.2.1/iqn.2001-04.com.example/1">iscsi://user%password@192.0.2.1/iqn.2001-04.com.example/1</a>
</pre> 
 Example (CHAP username/password via environment variables): 
 <pre>
        LIBISCSI_CHAP_USERNAME=&quot;user&quot; \
        LIBISCSI_CHAP_PASSWORD=&quot;password&quot; \
        qemu-kvm -drive file=<a HREF="iscsi://192.0.2.1/iqn.2001-04.com.example/1">iscsi://192.0.2.1/iqn.2001-04.com.example/1</a>
</pre> 
 iSCSI support is an optional feature of QEMU and only available when compiled and linked against libiscsi. 
 iSCSI parameters such as username and password can also be specified via a configuration file. See qemu-doc for more information and examples.
</dd><dt><b>NBD</b>
</dt><dd> QEMU supports NBD (Network Block Devices) both using TCP protocol as well as Unix Domain Sockets. 
 Syntax for specifying a NBD device using TCP ``nbd:&lt;server-ip&gt;:&lt;port&gt;[:exportname=&lt;export&gt;]'' 
 Syntax for specifying a NBD device using Unix Domain Sockets ``nbd:unix:&lt;domain-socket&gt;[:exportname=&lt;export&gt;]'' 
 Example for TCP 
 <pre>
        qemu-kvm --drive file=nbd:192.0.2.1:30000
</pre> 
 Example for Unix Domain Sockets 
 <pre>
        qemu-kvm --drive file=nbd:unix:/tmp/nbd-socket
</pre>
</dd><dt><b>SSH</b>
</dt><dd> QEMU supports SSH (Secure Shell) access to remote disks. 
 Examples: 
 <pre>
        qemu-kvm -drive file=<a HREF="ssh://user@host/path/to/disk.img">ssh://user@host/path/to/disk.img</a>
        qemu-kvm -drive file.driver=ssh,file.user=user,file.host=host,file.port=22,file.path=/path/to/disk.img
</pre> 
 Currently authentication must be done using ssh-agent. Other authentication methods may be supported in future.
</dd><dt><b>Sheepdog</b>
</dt><dd> Sheepdog is a distributed storage system for QEMU. QEMU supports using either local sheepdog devices or remote networked devices. 
 Syntax for specifying a sheepdog device 
 <pre><code>
sheepdog[+tcp | +unix]: //[host:port]/vdiname[?socket=path][#snapid|#tag]
</code></pre> 
 Example 
 <pre>
        qemu-kvm --drive file=sheepdog://192.0.2.1:30000/MyVirtualMachine
</pre> 
 See also &lt;<b><a rel="nofollow" HREF="http://http://www.osrg.net/sheepdog/">http://http://www.osrg.net/sheepdog/</a></b>&gt;.
</dd><dt><b>GlusterFS</b>
</dt><dd> GlusterFS is an user space distributed file system. QEMU supports the use of GlusterFS volumes for hosting VM disk images using TCP, Unix Domain Sockets and RDMA transport protocols. 
 Syntax for specifying a VM disk image on GlusterFS volume is 
 <pre><code>
gluster[+transport]: //[server[:port]]/volname/image[?socket=...]
</code></pre> 
 Example 
 <pre>
        qemu-kvm --drive file=gluster://192.0.2.1/testvol/a.img
</pre> 
 See also &lt;<b><a rel="nofollow" HREF="http://www.gluster.org">http://www.gluster.org</a></b>&gt;.</dd></dl>
 

 Bluetooth(R) options:
<dl>
<dt><b>-bt hci[...]</b>
</dt><dd> Defines the function of the corresponding Bluetooth HCI.  -bt options are matched with the HCIs present in the chosen machine type. For example when emulating a machine with only one HCI built into it, only the first <tt>&quot;-bt hci[...]&quot;</tt> option is valid and defines the HCI's logic. The Transport Layer is decided by the machine type. Currently the machines <tt>&quot;n800&quot;</tt> and <tt>&quot;n810&quot;</tt> have one HCI and all other machines have none. 
 The following three types are recognized:
</dd><dl>
<dl>
<dt><b>-bt hci,null</b>
</dt><dd> (default) The corresponding Bluetooth HCI assumes no internal logic and will not respond to any HCI commands or emit events.
</dd><dt><b>-bt hci,host[:</b><i>id</i><b>]</b>
</dt><dd> (<tt>&quot;bluez&quot;</tt> only) The corresponding HCI passes commands / events to / from the physical HCI identified by the name <i>id</i> (default: <tt>&quot;hci0&quot;</tt>) on the computer running QEMU.  Only available on <tt>&quot;bluez&quot;</tt> capable systems like Linux.
</dd><dt><b>-bt hci[,vlan=</b><i>n</i><b>]</b>
</dt><dd> Add a virtual, standard HCI that will participate in the Bluetooth scatternet <i>n</i> (default <tt>0</tt>). Similarly to <b>-net</b> VLANs, devices inside a bluetooth network <i>n</i> can only communicate with other devices in the same network (scatternet).</dd></dl>
</dl>

<dl>
</dl>

<dt><b>-bt vhci[,vlan=</b><i>n</i><b>]</b>
</dt><dd> (Linux-host only) Create a HCI in scatternet <i>n</i> (default 0) attached to the host bluetooth stack instead of to the emulated target. This allows the host and target machines to participate in a common scatternet and communicate. Requires the Linux <tt>&quot;vhci&quot;</tt> driver installed. Can be used as following: 

 <pre>
        qemu-kvm [...OPTIONS...] -bt hci,vlan=5 -bt vhci,vlan=5
</pre>
</dd><dt><b>-bt device:</b><i>dev</i><b>[,vlan=</b><i>n</i><b>]</b>
</dt><dd> Emulate a bluetooth device <i>dev</i> and place it in network <i>n</i> (default <tt>0</tt>). QEMU can only emulate one type of bluetooth devices currently:
</dd><dl>
<dl>
<dt><b>keyboard</b>
</dt><dd> Virtual wireless keyboard implementing the HIDP bluetooth profile.</dd></dl>
</dl>

<dl>
</dl>
</dl>
 

 TPM device options: 

 The general form of a TPM device option is:
<dl>
<dt><b>-tpmdev</b> <i>backend</i> <b>,id=</b><i>id</i> <b>[,</b><i>options</i><b>]</b>
</dt><dd> Backend type must be: <b>passthrough</b>. 
 The specific backend type will determine the applicable options. The <tt>&quot;-tpmdev&quot;</tt> option creates the TPM backend and requires a <tt>&quot;-device&quot;</tt> option that specifies the TPM frontend interface model. 
 Options to each backend are described below. 
 Use 'help' to print all available TPM backend types. 
 <pre>
        qemu-kvm -tpmdev help
</pre>
</dd><dt><b>-tpmdev passthrough, id=</b><i>id</i><b>, path=</b><i>path</i><b>, cancel-path=</b><i>cancel-path</i>
</dt><dd> (Linux-host only) Enable access to the host's TPM using the passthrough driver. 
 <b>path</b> specifies the path to the host's TPM device, i.e., on a Linux host this would be <tt>&quot;/dev/tpm0&quot;</tt>. <b>path</b> is optional and by default <tt>&quot;/dev/tpm0&quot;</tt> is used. 
 <b>cancel-path</b> specifies the path to the host TPM device's sysfs entry allowing for cancellation of an ongoing TPM command. <b>cancel-path</b> is optional and by default QEMU will search for the sysfs entry to use. 
 Some notes about using the host's TPM with the passthrough driver: 
 The TPM device accessed by the passthrough driver must not be used by any other application on the host. 
 Since the host's firmware (BIOS/UEFI) has already initialized the TPM, the VM's firmware (BIOS/UEFI) will not be able to initialize the TPM again and may therefore not show a TPM-specific menu that would otherwise allow the user to configure the TPM, e.g., allow the user to enable/disable or activate/deactivate the TPM. Further, if TPM ownership is released from within a VM then the host's TPM will get disabled and deactivated. To enable and activate the TPM again afterwards, the host has to be rebooted and the user is required to enter the firmware's menu to enable and activate the TPM. If the TPM is left disabled and/or deactivated most TPM commands will fail. 
 To create a passthrough TPM use the following two options: 
 <pre>
        -tpmdev passthrough,id=tpm0 -device tpm-tis,tpmdev=tpm0
</pre> 
 Note that the <tt>&quot;-tpmdev&quot;</tt> id is <tt>&quot;tpm0&quot;</tt> and is referenced by <tt>&quot;tpmdev=tpm0&quot;</tt> in the device option.</dd></dl>
 

 Linux/Multiboot boot specific: 

 When using these options, you can use a given Linux or Multiboot kernel without installing it in the disk image. It can be useful for easier testing of various kernels.
<dl>
<dt><b>-kernel</b> <i>bzImage</i>
</dt><dd> Use <i>bzImage</i> as kernel image. The kernel can be either a Linux kernel or in multiboot format.
</dd><dt><b>-append</b> <i>cmdline</i>
</dt><dd> Use <i>cmdline</i> as kernel command line
</dd><dt><b>-initrd</b> <i>file</i>
</dt><dd> Use <i>file</i> as initial ram disk.
</dd><dt><b>-initrd &quot;</b><i>file1</i> <b>arg=foo,</b><i>file2</i><b>&quot;</b>
</dt><dd> This syntax is only available with multiboot. 
 Use <i>file1</i> and <i>file2</i> as modules and pass arg=foo as parameter to the first module.
</dd><dt><b>-dtb</b> <i>file</i>
</dt><dd> Use <i>file</i> as a device tree binary (dtb) image and pass it to the kernel on boot.</dd></dl>
 

 Debug/Expert options:
<dl>
<dt><b>-serial</b> <i>dev</i>
</dt><dd> Redirect the virtual serial port to host character device <i>dev</i>. The default device is <tt>&quot;vc&quot;</tt> in graphical mode and <tt>&quot;stdio&quot;</tt> in non graphical mode. 
 This option can be used several times to simulate up to 4 serial ports. 
 Use <tt>&quot;-serial none&quot;</tt> to disable all serial ports. 
 Available character devices are:
</dd><dl>
<dl>
<dt><b>vc[:</b><i>W</i><b>x</b><i>H</i><b>]</b>
</dt><dd> Virtual console. Optionally, a width and height can be given in pixel with 
 <pre>
        vc:800x600
</pre> 
 It is also possible to specify width or height in characters: 
 <pre>
        vc:80Cx24C
</pre>
</dd><dt><b>pty</b>
</dt><dd> [Linux only] Pseudo TTY (a new PTY is automatically allocated)
</dd><dt><b>none</b>
</dt><dd> No device is allocated.
</dd><dt><b>null</b>
</dt><dd> void device
</dd><dt><b>/dev/XXX</b>
</dt><dd> [Linux only] Use host tty, e.g. <i>/dev/ttyS0</i>. The host serial port parameters are set according to the emulated ones.
</dd><dt><b>/dev/parport</b><i>N</i>
</dt><dd> [Linux only, parallel port only] Use host parallel port <i>N</i>. Currently SPP and EPP parallel port features can be used.
</dd><dt><b>file:</b><i>filename</i>
</dt><dd> Write output to <i>filename</i>. No character can be read.
</dd><dt><b>stdio</b>
</dt><dd> [Unix only] standard input/output
</dd><dt><b>pipe:</b><i>filename</i>
</dt><dd> name pipe <i>filename</i>
</dd><dt><b>COM</b><i>n</i>
</dt><dd> [Windows only] Use host serial port <i>n</i>
</dd><dt><b>udp:[</b><i>remote_host</i><b>]:</b><i>remote_port</i><b>[@[</b><i>src_ip</i><b>]:</b><i>src_port</i><b>]</b>
</dt><dd> This implements UDP Net Console. When <i>remote_host</i> or <i>src_ip</i> are not specified they default to <tt>0.0.0.0</tt>. When not using a specified <i>src_port</i> a random port is automatically chosen. 
 If you just want a simple readonly console you can use <tt>&quot;netcat&quot;</tt> or <tt>&quot;nc&quot;</tt>, by starting QEMU with: <tt>&quot;-serial udp::4555&quot;</tt> and nc as: <tt>&quot;nc -u -l -p 4555&quot;</tt>. Any time QEMU writes something to that port it will appear in the netconsole session. 
 If you plan to send characters back via netconsole or you want to stop and start QEMU a lot of times, you should have QEMU use the same source port each time by using something like <tt>&quot;-serial udp::4555 [at] 4556&quot;</tt> to QEMU. Another approach is to use a patched version of netcat which can listen to a TCP port and send and receive characters via udp. If you have a patched version of netcat which activates telnet remote echo and single char transfer, then you can use the following options to step up a netcat redirector to allow telnet on port 5555 to access the QEMU port.
</dd><dl>
<dl>
<dt>&quot;QEMU Options:&quot;
</dt><dd> -serial udp::4555 [at] 4556
</dd><dt>&quot;netcat options:&quot;
</dt><dd> -u -P 4555 -L 0.0.0.0:4556 -t -p 5555 -I -T
</dd><dt>&quot;telnet options:&quot;
</dt><dd> localhost 5555</dd></dl>
</dl>

<dl>
</dl>

<dt><b>tcp:[</b><i>host</i><b>]:</b><i>port</i><b>[,</b><i>server</i><b>][,nowait][,nodelay]</b>
</dt><dd> The TCP Net Console has two modes of operation. It can send the serial I/O to a location or wait for a connection from a location. By default the TCP Net Console is sent to <i>host</i> at the <i>port</i>. If you use the <i>server</i> option QEMU will wait for a client socket application to connect to the port before continuing, unless the <tt>&quot;nowait&quot;</tt> option was specified. The <tt>&quot;nodelay&quot;</tt> option disables the Nagle buffering algorithm. If <i>host</i> is omitted, 0.0.0.0 is assumed. Only one TCP connection at a time is accepted. You can use <tt>&quot;telnet&quot;</tt> to connect to the corresponding character device.
</dd><dl>
<dl>
<dt>&quot;Example to send tcp console to 192.168.0.2 port 4444&quot;
</dt><dd> -serial tcp:192.168.0.2:4444
</dd><dt>&quot;Example to listen and wait on port 4444 for connection&quot;
</dt><dd> -serial tcp::4444,server
</dd><dt>&quot;Example to not wait and listen on ip 192.168.0.100 port 4444&quot;
</dt><dd> -serial tcp:192.168.0.100:4444,server,nowait</dd></dl>
</dl>

<dl>
</dl>

<dt><b>telnet:</b><i>host</i><b>:</b><i>port</i><b>[,server][,nowait][,nodelay]</b>
</dt><dd> The telnet protocol is used instead of raw tcp sockets. The options work the same as if you had specified <tt>&quot;-serial tcp&quot;</tt>. The difference is that the port acts like a telnet server or client using telnet option negotiation. This will also allow you to send the MAGIC_SYSRQ sequence if you use a telnet that supports sending the break sequence. Typically in unix telnet you do it with Control-] and then type ``send break'' followed by pressing the enter key.
</dd><dt><b>unix:</b><i>path</i><b>[,server][,nowait]</b>
</dt><dd> A unix domain socket is used instead of a tcp socket. The option works the same as if you had specified <tt>&quot;-serial tcp&quot;</tt> except the unix domain socket <i>path</i> is used for connections.
</dd><dt><b>mon:</b><i>dev_string</i>
</dt><dd> This is a special option to allow the monitor to be multiplexed onto another serial port. The monitor is accessed with key sequence of <b>Control-a</b> and then pressing <b>c</b>. See monitor access <b>pcsys_keys</b> in the -nographic section for more keys. <i>dev_string</i> should be any one of the serial devices specified above. An example to multiplex the monitor onto a telnet server listening on port 4444 would be:
</dd><dl>
<dl>
<dt>&quot;-serial mon:telnet::4444,server,nowait&quot;
</dt><dd></dd></dl>
</dl>

<dl>
</dl>

<dt><b>braille</b>
</dt><dd> Braille device. This will use BrlAPI to display the braille output on a real or fake device.
</dd><dt><b>msmouse</b>
</dt><dd> Three button serial mouse. Configure the guest to use Microsoft protocol.</dd></dl>
</dl>

<dl>
</dl>

<dt><b>-parallel</b> <i>dev</i>
</dt><dd> Redirect the virtual parallel port to host device <i>dev</i> (same devices as the serial port). On Linux hosts, <i>/dev/parportN</i> can be used to use hardware devices connected on the corresponding host parallel port. 

 This option can be used several times to simulate up to 3 parallel ports. 

 Use <tt>&quot;-parallel none&quot;</tt> to disable all parallel ports.
</dd><dt><b>-monitor</b> <i>dev</i>
</dt><dd> Redirect the monitor to host device <i>dev</i> (same devices as the serial port). The default device is <tt>&quot;vc&quot;</tt> in graphical mode and <tt>&quot;stdio&quot;</tt> in non graphical mode.
</dd><dt><b>-qmp</b> <i>dev</i>
</dt><dd> Like -monitor but opens in 'control' mode.
</dd><dt><b>-mon chardev=[name][,mode=readline|control][,default]</b>
</dt><dd> Setup monitor on chardev <i>name</i>.
</dd><dt><b>-debugcon</b> <i>dev</i>
</dt><dd> Redirect the debug console to host device <i>dev</i> (same devices as the serial port). The debug console is an I/O port which is typically port 0xe9; writing to that I/O port sends output to this device. The default device is <tt>&quot;vc&quot;</tt> in graphical mode and <tt>&quot;stdio&quot;</tt> in non graphical mode.
</dd><dt><b>-pidfile</b> <i>file</i>
</dt><dd> Store the QEMU process PID in <i>file</i>. It is useful if you launch QEMU from a script.
</dd><dt><b>-singlestep</b>
</dt><dd> Run the emulation in single step mode.
</dd><dt><b>-S</b>
</dt><dd> Do not start CPU at startup (you must type 'c' in the monitor).
</dd><dt><b>-realtime mlock=on|off</b>
</dt><dd> Run qemu-kvm with realtime features. mlocking qemu-kvm and guest memory can be enabled via <b>mlock=on</b> (enabled by default).
</dd><dt><b>-gdb</b> <i>dev</i>
</dt><dd> Wait for gdb connection on device <i>dev</i>. Typical connections will likely be TCP-based, but also UDP, pseudo TTY, or even stdio are reasonable use case. The latter is allowing to start QEMU from within gdb and establish the connection via a pipe: 

 <pre>
        (gdb) target remote | exec qemu-kvm -gdb stdio ...
</pre>
</dd><dt><b>-s</b>
</dt><dd> Shorthand for -gdb tcp::1234, i.e. open a gdbserver on TCP port 1234.
</dd><dt><b>-d</b> <i>item1</i><b>[,...]</b>
</dt><dd> Enable logging of specified items. Use '-d help' for a list of log items.
</dd><dt><b>-D</b> <i>logfile</i>
</dt><dd> Output log in <i>logfile</i> instead of to stderr
</dd><dt><b>-L</b> <i>path</i>
</dt><dd> Set the directory for the BIOS, VGA BIOS and keymaps.
</dd><dt><b>-bios</b> <i>file</i>
</dt><dd> Set the filename for the BIOS.
</dd><dt><b>-enable-kvm</b>
</dt><dd> Enable KVM full virtualization support. This option is only available if KVM support is enabled when compiling.
</dd><dt><b>-xen-domid</b> <i>id</i>
</dt><dd> Specify xen guest domain <i>id</i> (XEN only).
</dd><dt><b>-xen-create</b>
</dt><dd> Create domain using xen hypercalls, bypassing xend. Warning: should not be used when xend is in use (XEN only).
</dd><dt><b>-xen-attach</b>
</dt><dd> Attach to existing xen domain. xend will use this when starting QEMU (XEN only).
</dd><dt><b>-no-reboot</b>
</dt><dd> Exit instead of rebooting.
</dd><dt><b>-no-shutdown</b>
</dt><dd> Don't exit QEMU on guest shutdown, but instead only stop the emulation. This allows for instance switching to monitor to commit changes to the disk image.
</dd><dt><b>-loadvm</b> <i>file</i>
</dt><dd> Start right away with a saved state (<tt>&quot;loadvm&quot;</tt> in monitor)
</dd><dt><b>-daemonize</b>
</dt><dd> Daemonize the QEMU process after initialization. QEMU will not detach from standard IO until it is ready to receive connections on any of its devices. This option is a useful way for external programs to launch QEMU without having to cope with initialization race conditions.
</dd><dt><b>-option-rom</b> <i>file</i>
</dt><dd> Load the contents of <i>file</i> as an option ROM. This option is useful to load things like EtherBoot.
</dd><dt><b>-clock</b> <i>method</i>
</dt><dd> Force the use of the given methods for timer alarm. To see what timers are available use <tt>&quot;-clock help&quot;</tt>.
</dd><dt><b>-rtc [base=utc|localtime|</b><i>date</i><b>][,clock=host|vm][,driftfix=none|slew]</b>
</dt><dd> Specify <b>base</b> as <tt>&quot;utc&quot;</tt> or <tt>&quot;localtime&quot;</tt> to let the RTC start at the current UTC or local time, respectively. <tt>&quot;localtime&quot;</tt> is required for correct date in MS-DOS or Windows. To start at a specific point in time, provide <i>date</i> in the format <tt>&quot;2006-06-17T16:01:21&quot;</tt> or <tt>&quot;2006-06-17&quot;</tt>. The default base is UTC. 

 By default the RTC is driven by the host system time. This allows to use the RTC as accurate reference clock inside the guest, specifically if the host time is smoothly following an accurate external reference clock, e.g. via NTP. If you want to isolate the guest time from the host, you can set <b>clock</b> to <tt>&quot;rt&quot;</tt> instead. To even prevent it from progressing during suspension, you can set it to <tt>&quot;vm&quot;</tt>. 

 Enable <b>driftfix</b> (i386 targets only) if you experience time drift problems, specifically with Windows' ACPI HAL. This option will try to figure out how many timer interrupts were not processed by the Windows guest and will re-inject them.
</dd><dt><b>-icount [</b><i>N</i><b>|auto]</b>
</dt><dd> Enable virtual instruction counter. The virtual cpu will execute one instruction every 2^<i>N</i> ns of virtual time. If <tt>&quot;auto&quot;</tt> is specified then the virtual cpu speed will be automatically adjusted to keep virtual time within a few seconds of real time. 

 Note that while this option can give deterministic behavior, it does not provide cycle accurate emulation. Modern CPUs contain superscalar out of order cores with complex cache hierarchies. The number of instructions executed often has little or no correlation with actual performance.
</dd><dt><b>-watchdog</b> <i>model</i>
</dt><dd> Create a virtual hardware watchdog device. Once enabled (by a guest action), the watchdog must be periodically polled by an agent inside the guest or else the guest will be restarted. 

 The <i>model</i> is the model of hardware watchdog to emulate. Choices for model are: <tt>&quot;ib700&quot;</tt> (iBASE 700) which is a very simple ISA watchdog with a single timer, or <tt>&quot;i6300esb&quot;</tt> (Intel 6300ESB I/O controller hub) which is a much more featureful PCI-based dual-timer watchdog. Choose a model for which your guest has drivers. 

 Use <tt>&quot;-watchdog help&quot;</tt> to list available hardware models. Only one watchdog can be enabled for a guest.
</dd><dt><b>-watchdog-action</b> <i>action</i>
</dt><dd> The <i>action</i> controls what QEMU will do when the watchdog timer expires. The default is <tt>&quot;reset&quot;</tt> (forcefully reset the guest). Other possible actions are: <tt>&quot;shutdown&quot;</tt> (attempt to gracefully shutdown the guest), <tt>&quot;poweroff&quot;</tt> (forcefully poweroff the guest), <tt>&quot;pause&quot;</tt> (pause the guest), <tt>&quot;debug&quot;</tt> (print a debug message and continue), or <tt>&quot;none&quot;</tt> (do nothing). 

 Note that the <tt>&quot;shutdown&quot;</tt> action requires that the guest responds to ACPI signals, which it may not be able to do in the sort of situations where the watchdog would have expired, and thus <tt>&quot;-watchdog-action shutdown&quot;</tt> is not recommended for production use. 

 Examples:
</dd><dl>
<dl>
<dt>&quot;-watchdog i6300esb -watchdog-action pause&quot;
</dt><dd>
</dd><dt>&quot;-watchdog ib700&quot;
</dt><dd></dd></dl>
</dl>

<dl>
</dl>

<dt><b>-echr</b> <i>numeric_ascii_value</i>
</dt><dd> Change the escape character used for switching to the monitor when using monitor and serial sharing. The default is <tt>0x01</tt> when using the <tt>&quot;-nographic&quot;</tt> option. <tt>0x01</tt> is equal to pressing <tt>&quot;Control-a&quot;</tt>. You can select a different character from the ascii control keys where 1 through 26 map to Control-a through Control-z. For instance you could use the either of the following to change the escape character to Control-t.
</dd><dl>
<dl>
<dt>&quot;-echr 0x14&quot;
</dt><dd>
</dd><dt>&quot;-echr 20&quot;
</dt><dd></dd></dl>
</dl>

<dl>
</dl>

<dt><b>-virtioconsole</b> <i>c</i>
</dt><dd> Set virtio console. 

 This option is maintained for backward compatibility. 

 Please use <tt>&quot;-device virtconsole&quot;</tt> for the new way of invocation.
</dd><dt><b>-show-cursor</b>
</dt><dd> Show cursor.
</dd><dt><b>-tb-size</b> <i>n</i>
</dt><dd> Set TB size.
</dd><dt><b>-incoming</b> <i>port</i>
</dt><dd> Prepare for incoming migration, listen on <i>port</i>.
</dd><dt><b>-nodefaults</b>
</dt><dd> Don't create default devices. Normally, QEMU sets the default devices like serial port, parallel port, virtual console, monitor device, VGA adapter, floppy and CD-ROM drive and others. The <tt>&quot;-nodefaults&quot;</tt> option will disable all those default devices.
</dd><dt><b>-chroot</b> <i>dir</i>
</dt><dd> Immediately before starting guest execution, chroot to the specified directory. Especially useful in combination with -runas.
</dd><dt><b>-runas</b> <i>user</i>
</dt><dd> Immediately before starting guest execution, drop root privileges, switching to the specified user.
</dd><dt><b>-prom-env</b> <i>variable</i><b>=</b><i>value</i>
</dt><dd> Set OpenBIOS nvram <i>variable</i> to given <i>value</i> (PPC, SPARC only).
</dd><dt><b>-semihosting</b>
</dt><dd> Semihosting mode (ARM, M68K, Xtensa only).
</dd><dt><b>-old-param</b>
</dt><dd> Old param mode (ARM only).
</dd><dt><b>-sandbox</b> <i>arg</i>
</dt><dd> Enable Seccomp mode 2 system call filter. 'on' will enable syscall filtering and 'off' will disable it. The default is 'off'.
</dd><dt><b>-readconfig</b> <i>file</i>
</dt><dd> Read device configuration from <i>file</i>. This approach is useful when you want to spawn QEMU process with many command line options but you don't want to exceed the command line character limit.
</dd><dt><b>-writeconfig</b> <i>file</i>
</dt><dd> Write device configuration to <i>file</i>. The <i>file</i> can be either filename to save command line and device configuration into file or dash <tt>&quot;-&quot;</tt>) character to print the output to stdout. This can be later used as input file for <tt>&quot;-readconfig&quot;</tt> option.
</dd><dt><b>-nodefconfig</b>
</dt><dd> Normally QEMU loads configuration files from <i>sysconfdir</i> and <i>datadir</i> at startup. The <tt>&quot;-nodefconfig&quot;</tt> option will prevent QEMU from loading any of those config files.
</dd><dt><b>-no-user-config</b>
</dt><dd> The <tt>&quot;-no-user-config&quot;</tt> option makes QEMU not load any of the user-provided config files on <i>sysconfdir</i>, but won't make it skip the QEMU-provided config files from <i>datadir</i>.
</dd><dt><b>-trace [events=</b><i>file</i><b>][,file=</b><i>file</i><b>]</b>
</dt><dd> Specify tracing options.
</dd><dl>
<dl>
<dt><b>events=</b><i>file</i>
</dt><dd> Immediately enable events listed in <i>file</i>. The file must contain one event name (as listed in the <i>trace-events</i> file) per line. This option is only available if QEMU has been compiled with either <i>simple</i> or <i>stderr</i> tracing backend.
</dd><dt><b>file=</b><i>file</i>
</dt><dd> Log output traces to <i>file</i>. 
 This option is only available if QEMU has been compiled with the <i>simple</i> tracing backend.</dd></dl>
</dl>

<dl>
</dl>

<dt><b>-enable-fips</b>
</dt><dd> Enable FIPS 140-2 compliance mode.
</dd><dt><b>-object</b> <i>typename</i><b>[,</b><i>prop1</i><b>=</b><i>value1</i><b>,...]</b>
</dt><dd> Create an new object of type <i>typename</i> setting properties in the order they are specified. Note that the 'id' property must be set. These objects are placed in the '/objects' path.
</dd><dt><b>-msg timestamp[=on|off]</b>
</dt><dd> prepend a timestamp to each log message.(default:on)
</dd><dt><b>-dump-vmstate</b> <i>file</i>
</dt><dd> Dump json-encoded vmstate information for current machine type to file in <i>file</i></dd></dl>
 

 During the graphical emulation, you can use special key combinations to change modes. The default key mappings are shown below, but if you use <tt>&quot;-alt-grab&quot;</tt> then the modifier is Ctrl-Alt-Shift (instead of Ctrl-Alt) and if you use <tt>&quot;-ctrl-grab&quot;</tt> then the modifier is the right Ctrl key (instead of Ctrl-Alt):
<dl>
<dt><b>Ctrl-Alt-f</b>
</dt><dd> Toggle full screen
</dd><dt><b>Ctrl-Alt-+</b>
</dt><dd> Enlarge the screen
</dd><dt><b>Ctrl-Alt---</b>
</dt><dd> Shrink the screen
</dd><dt><b>Ctrl-Alt-u</b>
</dt><dd> Restore the screen's un-scaled dimensions
</dd><dt><b>Ctrl-Alt-n</b>
</dt><dd> Switch to virtual console 'n'. Standard console mappings are:
</dd><dl>
<dl>
<dt><i>1</i>
</dt><dd> Target system display
</dd><dt><i>2</i>
</dt><dd> Monitor
</dd><dt><i>3</i>
</dt><dd> Serial port</dd></dl>
</dl>

<dl>
</dl>

<dt><b>Ctrl-Alt</b>
</dt><dd> Toggle mouse and keyboard grab.</dd></dl>
 

 In the virtual consoles, you can use <b>Ctrl-Up</b>, <b>Ctrl-Down</b>, <b>Ctrl-PageUp</b> and <b>Ctrl-PageDown</b> to move in the back log. 

 During emulation, if you are using the <b>-nographic</b> option, use <b>Ctrl-a h</b> to get terminal commands:
<dl>
<dt><b>Ctrl-a h</b>
</dt><dd>
</dd><dt><b>Ctrl-a ?</b>
</dt><dd> Print this help
</dd><dt><b>Ctrl-a x</b>
</dt><dd> Exit emulator
</dd><dt><b>Ctrl-a s</b>
</dt><dd> Save disk data back to file (if -snapshot)
</dd><dt><b>Ctrl-a t</b>
</dt><dd> Toggle console timestamps
</dd><dt><b>Ctrl-a b</b>
</dt><dd> Send break (magic sysrq in Linux)
</dd><dt><b>Ctrl-a c</b>
</dt><dd> Switch between console and monitor
</dd><dt><b>Ctrl-a Ctrl-a</b>
</dt><dd> Send Ctrl-a</dd></dl>
 

 The following options are specific to the PowerPC emulation:
<dl>
<dt><b>-g</b> <i>W</i><b>x</b><i>H</i><b>[x</b><i></i><i>DEPTH</i><i></i><b>]</b>
</dt><dd> Set the initial VGA graphic mode. The default is 800x600x15.
</dd><dt><b>-prom-env</b> <i>string</i>
</dt><dd> Set OpenBIOS variables in NVRAM, for example: 
 <pre>
        qemu-system-ppc -prom-env 'auto-boot?=false' \
         -prom-env 'boot-device=hd:2,\yaboot' \
         -prom-env 'boot-args=conf=hd:2,\yaboot.conf'
</pre> 
 These variables are not used by Open Hack'Ware.</dd></dl>
 

 The following options are specific to the Sparc32 emulation:
<dl>
<dt><b>-g</b> <i>W</i><b>x</b><i>H</i><b>x[x</b><i></i><i>DEPTH</i><i></i><b>]</b>
</dt><dd> Set the initial TCX graphic mode. The default is 1024x768x8, currently the only other possible mode is 1024x768x24.
</dd><dt><b>-prom-env</b> <i>string</i>
</dt><dd> Set OpenBIOS variables in NVRAM, for example: 
 <pre>
        qemu-system-sparc -prom-env 'auto-boot?=false' \
         -prom-env 'boot-device=sd(0,2,0):d' -prom-env 'boot-args=linux single'
</pre>
</dd><dt><b>-M [SS-4|SS-5|SS-10|SS-20|SS-600MP|LX|Voyager|SPARCClassic] [|SPARCbook|SS-2|SS-1000|SS-2000]</b>
</dt><dd> Set the emulated machine type. Default is SS-5.</dd></dl>
 

 The following options are specific to the Sparc64 emulation:
<dl>
<dt><b>-prom-env</b> <i>string</i>
</dt><dd> Set OpenBIOS variables in NVRAM, for example: 
 <pre>
        qemu-system-sparc64 -prom-env 'auto-boot?=false'
</pre>
</dd><dt><b>-M [sun4u|sun4v|Niagara]</b>
</dt><dd> Set the emulated machine type. The default is sun4u.</dd></dl>

<h2>SEE ALSO</h2>

 The HTML documentation of QEMU for more precise information and Linux user mode emulator invocation.

<h2>AUTHOR</h2>

 Fabrice Bellard
