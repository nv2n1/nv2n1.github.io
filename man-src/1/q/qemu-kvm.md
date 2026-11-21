---

title: "qemu-kvm(1)"
name: "qemu-kvm"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qemu-kvm/"
---

qemu-doc - QEMU Emulator User Documentation 

usage: qemu-kvm [options] [<i>disk_image</i>]

The <font SIZE="-1">QEMU PC</font> System emulator simulates the following peripherals:
<dl>
<dt>-
</dt><dd> i440FX host <font SIZE="-1">PCI</font> bridge and <font SIZE="-1">PIIX3 PCI</font> to <font SIZE="-1">ISA</font> bridge
</dd><dt>-
</dt><dd> Cirrus <font SIZE="-1">CLGD 5446 PCI VGA</font> card or dummy <font SIZE="-1">VGA</font> card with Bochs <font SIZE="-1">VESA</font> extensions (hardware level, including all non standard modes).
</dd><dt>-
</dt><dd> <font SIZE="-1">PS/2</font> mouse and keyboard
</dd><dt>-
</dt><dd> 2 <font SIZE="-1">PCI IDE</font> interfaces with hard disk and CD-ROM support
</dd><dt>-
</dt><dd> Floppy disk
</dd><dt>-
</dt><dd> <font SIZE="-1">PCI</font> and <font SIZE="-1">ISA</font> network adapters
</dd><dt>-
</dt><dd> Serial ports
</dd><dt>-
</dt><dd> Creative SoundBlaster 16 sound card
</dd><dt>-
</dt><dd> <font SIZE="-1">ENSONIQ</font> AudioPCI <font SIZE="-1">ES1370</font> sound card
</dd><dt>-
</dt><dd> Intel 82801AA <font SIZE="-1">AC97</font> Audio compatible sound card
</dd><dt>-
</dt><dd> Intel <font SIZE="-1">HD</font> Audio Controller and <font SIZE="-1">HDA</font> codec
</dd><dt>-
</dt><dd> Adlib (<font SIZE="-1">OPL2</font>) - Yamaha <font SIZE="-1">YM3812</font> compatible chip
</dd><dt>-
</dt><dd> Gravis Ultrasound <font SIZE="-1">GF1</font> sound card
</dd><dt>-
</dt><dd> <font SIZE="-1">CS4231A</font> compatible sound card
</dd><dt>-
</dt><dd> <font SIZE="-1">PCI UHCI USB</font> controller and a virtual <font SIZE="-1">USB</font> hub.</dd></dl>
 

 <font SIZE="-1">SMP</font> is supported with up to 255 CPUs. 

 <font SIZE="-1">QEMU</font> uses the <font SIZE="-1">PC BIOS</font> from the Bochs project and the Plex86/Bochs <font SIZE="-1">LGPL VGA BIOS.</font> 

 <font SIZE="-1">QEMU</font> uses <font SIZE="-1">YM3812</font> emulation by Tatsuyuki Satoh. 

 <font SIZE="-1">QEMU</font> uses <font SIZE="-1">GUS</font> emulation (<font SIZE="-1">GUSEMU32</font> &lt;<b><a rel="nofollow" HREF="http://www.deinmeister.de/gusemu/">http://www.deinmeister.de/gusemu/</a></b>&gt;) by Tibor ``<font SIZE="-1">TS''</font> Schütz. 

 Note that, by default, <font SIZE="-1">GUS</font> shares <font SIZE="-1"><i>IRQ</i></font><i></i>(7) with parallel ports and so <font SIZE="-1">QEMU</font> must be told to not have parallel ports to have working <font SIZE="-1">GUS.</font> 

 <pre>
        qemu-kvm dos.img -soundhw gus -parallel none
</pre> 

 Alternatively: 

 <pre>
        qemu-kvm dos.img -device gus,irq=5
</pre> 

 Or some other unclaimed <font SIZE="-1">IRQ.</font> 

 <font SIZE="-1">CS4231A</font> is the chip used in Windows Sound System and <font SIZE="-1">GUSMAX</font> products

<h2>OPTIONS</h2>

 <i>disk_image</i> is a raw hard disk image for <font SIZE="-1">IDE</font> hard disk 0. Some targets do not need a disk image. 

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
</dt><dd> Defines the size of the <font SIZE="-1">KVM</font> shadow <font SIZE="-1">MMU.</font>
</dd><dt><b>dump-guest-core=on|off</b>
</dt><dd> Include guest memory in a core dump. The default is on.
</dd><dt><b>mem-merge=on|off</b>
</dt><dd> Enables or disables memory merge support. This feature, when supported by the host, de-duplicates identical memory pages among VMs instances (enabled by default).</dd></dl>
</dl>

<dl>
</dl>

<dt><b>-cpu</b> <i>model</i>
</dt><dd> Select <font SIZE="-1">CPU</font> model (<tt>&quot;-cpu help&quot;</tt> for list and additional feature selection)
</dd><dt><b>-smp</b> <i>n</i><b>[,cores=</b><i>cores</i><b>][,threads=</b><i>threads</i><b>][,sockets=</b><i>sockets</i><b>][,maxcpus=</b><i>maxcpus</i><b>]</b>
</dt><dd> Simulate an <font SIZE="-1">SMP</font> system with <i>n</i> CPUs. On the <font SIZE="-1">PC</font> target, up to 255 CPUs are supported. On Sparc32 target, Linux limits the number of usable CPUs to 4. For the <font SIZE="-1">PC</font> target, the number of <i>cores</i> per socket, the number of <i>threads</i> per cores and the total number of <i>sockets</i> can be specified. Missing values will be computed. If any on the three values is given, the total number of CPUs <i>n</i> can be omitted. <i>maxcpus</i> specifies the maximum number of hotpluggable CPUs.
</dd><dt><b>-numa</b> <i>opts</i>
</dt><dd> Simulate a multi node <font SIZE="-1">NUMA</font> system. If mem and cpus are omitted, resources are split equally.
</dd><dt><b>-add-fd fd=</b><i>fd</i><b>,set=</b><i>set</i><b>[,opaque=</b><i>opaque</i><b>]</b>
</dt><dd> Add a file descriptor to an fd set. Valid options are:
</dd><dl>
<dl>
<dt><b>fd=</b><i>fd</i>
</dt><dd> This option defines the file descriptor of which a duplicate is added to fd set. The file descriptor cannot be stdin, stdout, or stderr.
</dd><dt><b>set=</b><i>set</i>
</dt><dd> This option defines the <font SIZE="-1">ID</font> of the fd set to add the file descriptor to.
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
</dt><dd> Specify boot order <i>drives</i> as a string of drive letters. Valid drive letters depend on the target achitecture. The x86 <font SIZE="-1">PC</font> uses: a, b (floppy 1 and 2), c (first hard disk), d (first CD-ROM), n-p (Etherboot from network adapter 1-4), hard disk boot is the default. To apply a particular boot order only on the first startup, specify it via <b>once</b>. 

 Interactive boot menus/prompts can be enabled via <b>menu=on</b> as far as firmware/BIOS supports them. The default is non-interactive boot. 

 A splash picture could be passed to bios, enabling user to show it as logo, when option splash=<i>sp_name</i> is given and menu=on, If firmware/BIOS supports them. Currently Seabios for X86 system support it. limitation: The splash file could be a jpeg file or a <font SIZE="-1">BMP</font> file in 24 <font SIZE="-1">BPP</font> format(true color). The resolution should be supported by the <font SIZE="-1">SVGA</font> mode, so the recommended is 320x240, 640x480, 800x640. 

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
</dt><dd> Set virtual <font SIZE="-1">RAM</font> size to <i>megs</i> megabytes. Default is 128 MiB. Optionally, a suffix of ``M'' or ``G'' can be used to signify a value in megabytes or gigabytes respectively.
</dd><dt><b>-mem-path</b> <i>path</i>
</dt><dd> Allocate guest <font SIZE="-1">RAM</font> from a temporarily created file in <i>path</i>.
</dd><dt><b>-mem-prealloc</b>
</dt><dd> Preallocate memory when using -mem-path.
</dd><dt><b>-k</b> <i>language</i>
</dt><dd> Use keyboard layout <i>language</i> (for example <tt>&quot;fr&quot;</tt> for French). This option is only needed where it is not easy to get raw <font SIZE="-1">PC</font> keycodes (e.g. on Macs, with some X11 servers or with a <font SIZE="-1">VNC</font> display). You don't normally need to use it on PC/Linux or PC/Windows hosts. 

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

 Note that Linux's i810_audio <font SIZE="-1">OSS</font> kernel (for <font SIZE="-1">AC97</font>) module might require manually specifying clocking. 

 <pre>
        modprobe i810_audio clocking=48000
</pre>
</dd><dt><b>-balloon none</b>
</dt><dd> Disable balloon device.
</dd><dt><b>-balloon virtio[,addr=</b><i>addr</i><b>]</b>
</dt><dd> Enable virtio balloon device (default), optionally with <font SIZE="-1">PCI</font> address <i>addr</i>.
</dd><dt><b>-device</b> <i>driver</i><b>[,</b><i>prop</i><b>[=</b><i>value</i><b>][,...]]</b>
</dt><dd> Add device <i>driver</i>. <i>prop</i>=<i>value</i> sets driver properties. Valid properties depend on the driver. To get help on possible drivers and properties, use <tt>&quot;-device help&quot;</tt> and <tt>&quot;-device </tt>driver<tt>,help&quot;</tt>.
</dd><dt><b>-name</b> <i>name</i>
</dt><dd> Sets the <i>name</i> of the guest. This name will be displayed in the <font SIZE="-1">SDL</font> window caption. The <i>name</i> will also be used for the <font SIZE="-1">VNC</font> server. Also optionally set the top visible process name in Linux.
</dd><dt><b>-uuid</b> <i>uuid</i>
</dt><dd> Set system <font SIZE="-1">UUID.</font></dd></dl>
 

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
 Special files such as iSCSI devices can be specified using protocol specific URLs. See the section for ``Device <font SIZE="-1">URL</font> Syntax'' for more information.
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
</dt><dd> <i>aio</i> is ``threads'', or ``native'' and selects between pthread based disk I/O and native Linux <font SIZE="-1">AIO.</font>
</dd><dt><b>discard=</b><i>discard</i>
</dt><dd> <i>discard</i> is one of ``ignore'' (or ``off'') or ``unmap'' (or ``on'') and controls whether <i>discard</i> (also known as <i>trim</i> or <i>unmap</i>) requests are ignored or passed to the filesystem. Some machine types may not support discard requests.
</dd><dt><b>format=</b><i>format</i>
</dt><dd> Specify which disk <i>format</i> will be used rather than detecting the format. Can be used to specifiy format=raw to avoid interpreting an untrusted format header.
</dd><dt><b>serial=</b><i>serial</i>
</dt><dd> This option specifies the serial number to assign to the device.
</dd><dt><b>addr=</b><i>addr</i>
</dt><dd> Specify the controller's <font SIZE="-1">PCI</font> address (if=virtio only).
</dd><dt><b>werror=</b><i>action</i><b>,rerror=</b><i>action</i>
</dt><dd> Specify which <i>action</i> to take on write and read errors. Valid actions are: ``ignore'' (ignore the error and try to continue), ``stop'' (pause <font SIZE="-1">QEMU</font>), ``report'' (report the error to the guest), ``enospc'' (pause <font SIZE="-1">QEMU</font> only if the host disk is full; report the error to the guest otherwise). The default setting is <b>werror=enospc</b> and <b>rerror=report</b>.
</dd><dt><b>readonly</b>
</dt><dd> Open drive <b>file</b> as read-only. Guest write attempts will fail.
</dd><dt><b>copy-on-read=</b><i>copy-on-read</i>
</dt><dd> <i>copy-on-read</i> is ``on'' or ``off'' and enables whether to copy read backing file sectors into the image file.</dd></dl>
</dl>

<dl>
<dt>
</dt><dd> 
 By default, the <b>cache=writeback</b> mode is used. It will report data writes as completed as soon as the data is present in the host page cache. This is safe as long as your guest <font SIZE="-1">OS</font> makes sure to correctly flush disk caches where needed. If your guest <font SIZE="-1">OS</font> does not handle volatile disk write caches correctly and your host crashes or loses power, then the guest may experience data corruption. 
 For such guests, you should consider using <b>cache=writethrough</b>. This means that the host page cache will be used to read and write data, but write notification will be sent to the guest only after <font SIZE="-1">QEMU</font> has made sure to flush each write to the disk. Be aware that this has a major impact on performance. 
 The host page cache can be avoided entirely with <b>cache=none</b>. This will attempt to do disk <font SIZE="-1">IO</font> directly to the guest's memory. <font SIZE="-1">QEMU</font> may still perform an internal copy of the data. Note that this is considered a writeback mode and the guest <font SIZE="-1">OS</font> must handle the disk write cache correctly in order to avoid data corruption on host crashes. 
 The host page cache can be avoided while only sending write notifications to the guest when the data has been flushed to the disk using <b>cache=directsync</b>. 
 In case you don't care about data integrity over host failures, use <b>cache=unsafe</b>. This option tells <font SIZE="-1">QEMU</font> that it never needs to write any data to the disk but can instead keep things in cache. If anything goes wrong, like your host losing power, the disk storage getting disconnected accidentally, etc. your image will most probably be rendered unusable. When using the <b>-snapshot</b> option, unsafe caching is always used. 
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
 You can connect a <font SIZE="-1">CDROM</font> to the slave of ide0: 
 <pre>
        qemu-kvm -drive file=file,if=ide,index=1,media=cdrom
</pre> 
 If you don't specify the ``file='' argument, you define an empty drive: 
 <pre>
        qemu-kvm -drive if=ide,index=1,media=cdrom
</pre> 
 You can connect a <font SIZE="-1">SCSI</font> disk with unit <font SIZE="-1">ID 6</font> on the bus #0: 
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
</dt><dd> Force hard disk 0 physical geometry (1 &lt;= <i>c</i> &lt;= 16383, 1 &lt;= <i>h</i> &lt;= 16, 1 &lt;= <i>s</i> &lt;= 63) and optionally force the <font SIZE="-1">BIOS</font> translation mode (<i>t</i>=none, lba or auto). Usually <font SIZE="-1">QEMU</font> can guess all those parameters. This option is useful for old MS-DOS disk images.
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
</dt><dd> Specifies the security model to be used for this export path. Supported security models are ``passthrough'', ``mapped-xattr'', ``mapped-file'' and ``none''. In ``passthrough'' security model, files are stored using the same credentials as they are created on the guest. This requires <font SIZE="-1">QEMU</font> to run as root. In ``mapped-xattr'' security model, some of the file attributes like uid, gid, mode bits and link target are stored as file attributes. For ``mapped-file'' these attributes are stored in the hidden .virtfs_metadata directory. Directories exported by this security model cannot interact with other unix tools. ``none'' security model is same as passthrough except the sever won't report failures if it fails to set file attributes like ownership. Security model is mandatory only for local fsdriver. Other fsdrivers (like handle, proxy) don't take security model as a parameter.
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
</dt><dd> Specifies the security model to be used for this export path. Supported security models are ``passthrough'', ``mapped-xattr'', ``mapped-file'' and ``none''. In ``passthrough'' security model, files are stored using the same credentials as they are created on the guest. This requires <font SIZE="-1">QEMU</font> to run as root. In ``mapped-xattr'' security model, some of the file attributes like uid, gid, mode bits and link target are stored as file attributes. For ``mapped-file'' these attributes are stored in the hidden .virtfs_metadata directory. Directories exported by this security model cannot interact with other unix tools. ``none'' security model is same as passthrough except the sever won't report failures if it fails to set file attributes like ownership. Security model is mandatory only for local fsdriver. Other fsdrivers (like handle, proxy) don't take security model as a parameter.
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
 

 <font SIZE="-1">USB</font> options:
<dl>
<dt><b>-usb</b>
</dt><dd> Enable the <font SIZE="-1">USB</font> driver (will be the default soon)
</dd><dt><b>-usbdevice</b> <i>devname</i>
</dt><dd> Add the <font SIZE="-1">USB</font> device <i>devname</i>.
</dd><dl>
<dl>
<dt><b>mouse</b>
</dt><dd> Virtual Mouse. This will override the <font SIZE="-1">PS/2</font> mouse emulation when activated.
</dd><dt><b>tablet</b>
</dt><dd> Pointer device that uses absolute coordinates (like a touchscreen). This means <font SIZE="-1">QEMU</font> is able to report the mouse position without having to grab the mouse. Also overrides the <font SIZE="-1">PS/2</font> mouse emulation when activated.
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
</dt><dd> Network adapter that supports <font SIZE="-1">CDC</font> ethernet and <font SIZE="-1">RNDIS</font> protocols.</dd></dl>
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
</dt><dd> Display video output via <font SIZE="-1">SDL </font>(usually in a separate graphics window; see the <font SIZE="-1">SDL</font> documentation for other possibilities).
</dd><dt><b>curses</b>
</dt><dd> Display video output via curses. For graphics device models which support a text mode, <font SIZE="-1">QEMU</font> can display this output using a curses/ncurses interface. Nothing is displayed when the graphics device is in graphical mode or if the graphics device does not support a text mode. Generally only the <font SIZE="-1">VGA</font> device models support text mode.
</dd><dt><b>none</b>
</dt><dd> Do not display video output. The guest will still see an emulated graphics card, but its output will not be displayed to the <font SIZE="-1">QEMU</font> user. This option differs from the -nographic option in that it only affects what is done with video output; -nographic also changes the destination of the serial and parallel port data.
</dd><dt><b>vnc</b>
</dt><dd> Start a <font SIZE="-1">VNC</font> server on display &lt;arg&gt;</dd></dl>
</dl>

<dl>
</dl>

<dt><b>-nographic</b>
</dt><dd> Normally, <font SIZE="-1">QEMU</font> uses <font SIZE="-1">SDL</font> to display the <font SIZE="-1">VGA</font> output. With this option, you can totally disable graphical output so that <font SIZE="-1">QEMU</font> is a simple command line application. The emulated serial port is redirected on the console. Therefore, you can still use <font SIZE="-1">QEMU</font> to debug a Linux kernel with a serial console.
</dd><dt><b>-curses</b>
</dt><dd> Normally, <font SIZE="-1">QEMU</font> uses <font SIZE="-1">SDL</font> to display the <font SIZE="-1">VGA</font> output. With this option, <font SIZE="-1">QEMU</font> can display the <font SIZE="-1">VGA</font> output when in text mode using a curses/ncurses interface. Nothing is displayed in graphical mode.
</dd><dt><b>-no-frame</b>
</dt><dd> Do not use decorations for <font SIZE="-1">SDL</font> windows and start them using the whole available screen space. This makes the using <font SIZE="-1">QEMU</font> in a dedicated desktop workspace more convenient.
</dd><dt><b>-alt-grab</b>
</dt><dd> Use Ctrl-Alt-Shift to grab mouse (instead of Ctrl-Alt). Note that this also affects the special keys (for fullscreen, monitor-mode switching, etc).
</dd><dt><b>-ctrl-grab</b>
</dt><dd> Use Right-Ctrl to grab mouse (instead of Ctrl-Alt). Note that this also affects the special keys (for fullscreen, monitor-mode switching, etc).
</dd><dt><b>-no-quit</b>
</dt><dd> Disable <font SIZE="-1">SDL</font> window close capability.
</dd><dt><b>-sdl</b>
</dt><dd> Enable <font SIZE="-1">SDL.</font>
</dd><dt><b>-spice</b> <i>option</i><b>[,</b><i>option</i><b>[,...]]</b>
</dt><dd> Enable the spice remote desktop protocol. Valid options are
</dd><dl>
<dl>
<dt><b>port=&lt;nr&gt;</b>
</dt><dd> Set the <font SIZE="-1">TCP</font> port spice is listening on for plaintext channels.
</dd><dt><b>addr=&lt;addr&gt;</b>
</dt><dd> Set the <font SIZE="-1">IP</font> address spice is listening on. Default is any address.
</dd><dt><b>ipv4</b>
</dt><dd>
</dd><dt><b>ipv6</b>
</dt><dd> Force using the specified <font SIZE="-1">IP</font> version.
</dd><dt><b>password=&lt;secret&gt;</b>
</dt><dd> Set the password you need to authenticate.
</dd><dt><b>sasl</b>
</dt><dd> Require that the client use <font SIZE="-1">SASL</font> to authenticate with the spice. The exact choice of authentication method used is controlled from the system / user's <font SIZE="-1">SASL</font> configuration file for the 'qemu' service. This is typically found in /etc/sasl2/qemu.conf. If running <font SIZE="-1">QEMU</font> as an unprivileged user, an environment variable <font SIZE="-1">SASL_CONF_PATH</font> can be used to make it search alternate locations for the service config. While some <font SIZE="-1">SASL</font> auth methods can also provide data encryption (eg <font SIZE="-1">GSSAPI</font>), it is recommended that <font SIZE="-1">SASL</font> always be combined with the 'tls' and 'x509' settings to enable use of <font SIZE="-1">SSL</font> and server certificates. This ensures a data encryption preventing compromise of authentication credentials.
</dd><dt><b>disable-ticketing</b>
</dt><dd> Allow client connects without authentication.
</dd><dt><b>disable-copy-paste</b>
</dt><dd> Disable copy paste between the client and the guest.
</dd><dt><b>tls-port=&lt;nr&gt;</b>
</dt><dd> Set the <font SIZE="-1">TCP</font> port spice is listening on for encrypted channels.
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
</dt><dd> Force specific channel to be used with or without <font SIZE="-1">TLS</font> encryption. The options can be specified multiple times to configure multiple channels. The special name ``default'' can be used to set the default mode. For channels which are not explicitly forced into one mode the spice client is allowed to pick tls/plaintext as he pleases.
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
</dt><dd> Rotate graphical output 90 deg left (only <font SIZE="-1">PXA LCD</font>).
</dd><dt><b>-rotate</b> <i>deg</i>
</dt><dd> Rotate graphical output some deg left (only <font SIZE="-1">PXA LCD</font>).
</dd><dt><b>-vga</b> <i>type</i>
</dt><dd> Select type of <font SIZE="-1">VGA</font> card to emulate. Valid values for <i>type</i> are
</dd><dl>
<dl>
<dt><b>cirrus</b>
</dt><dd> Cirrus Logic <font SIZE="-1">GD5446</font> Video card. All Windows versions starting from Windows 95 should recognize and use this graphic card. For optimal performances, use 16 bit color depth in the guest and the host <font SIZE="-1">OS. </font>(This one is the default)
</dd><dt><b>std</b>
</dt><dd> Standard <font SIZE="-1">VGA</font> card with Bochs <font SIZE="-1">VBE</font> extensions. If your guest <font SIZE="-1">OS</font> supports the <font SIZE="-1">VESA 2.0 VBE</font> extensions (e.g. Windows <font SIZE="-1">XP</font>) and if you want to use high resolution modes (&gt;= 1280x1024x16) then you should use this option.
</dd><dt><b>vmware</b>
</dt><dd> VMWare SVGA-II compatible adapter. Use it if you have sufficiently recent XFree86/XOrg server or Windows guest with a driver for this card.
</dd><dt><b>qxl</b>
</dt><dd> <font SIZE="-1">QXL</font> paravirtual graphic card. It is <font SIZE="-1">VGA</font> compatible (including <font SIZE="-1">VESA 2.0 VBE</font> support). Works best with qxl guest drivers installed though. Recommended choice when using the spice protocol.
</dd><dt><b>none</b>
</dt><dd> Disable <font SIZE="-1">VGA</font> card.</dd></dl>
</dl>

<dl>
</dl>

<dt><b>-full-screen</b>
</dt><dd> Start in full screen.
</dd><dt><b>-g</b> <i>width</i><b>x</b><i>height</i><b>[x</b><i>depth</i><b>]</b>
</dt><dd> Set the initial graphical resolution and depth (<font SIZE="-1">PPC, SPARC</font> only).
</dd><dt><b>-vnc</b> <i>display</i><b>[,</b><i>option</i><b>[,</b><i>option</i><b>[,...]]]</b>
</dt><dd> Normally, <font SIZE="-1">QEMU</font> uses <font SIZE="-1">SDL</font> to display the <font SIZE="-1">VGA</font> output. With this option, you can have <font SIZE="-1">QEMU</font> listen on <font SIZE="-1">VNC</font> display <i>display</i> and redirect the <font SIZE="-1">VGA</font> display over the <font SIZE="-1">VNC</font> session. It is very useful to enable the usb tablet device when using this option (option <b>-usbdevice tablet</b>). When using the <font SIZE="-1">VNC</font> display, you must use the <b>-k</b> parameter to set the keyboard layout if you are not using en-us. Valid syntax for the <i>display</i> is
</dd><dl>
<dl>
<dt><i>host</i><b>:</b><i>d</i>
</dt><dd> <font SIZE="-1">TCP</font> connections will only be allowed from <i>host</i> on display <i>d</i>. By convention the <font SIZE="-1">TCP</font> port is 5900+<i>d</i>. Optionally, <i>host</i> can be omitted in which case the server will accept connections from any host.
</dd><dt><b>unix:</b><i>path</i>
</dt><dd> Connections will be allowed over <font SIZE="-1">UNIX</font> domain sockets where <i>path</i> is the location of a unix socket to listen for connections on.
</dd><dt><b>none</b>
</dt><dd> <font SIZE="-1">VNC</font> is initialized but not started. The monitor <tt>&quot;change&quot;</tt> command can be used to later start the <font SIZE="-1">VNC</font> server.</dd></dl>
</dl>

<dl>
<dt>
</dt><dd> 
 Following the <i>display</i> value there may be one or more <i>option</i> flags separated by commas. Valid options are
</dd><dl>
<dt><b>reverse</b>
</dt><dd> Connect to a listening <font SIZE="-1">VNC</font> client via a ``reverse'' connection. The client is specified by the <i>display</i>. For reverse network connections (<i>host</i>:<i>d</i>,<tt>&quot;reverse&quot;</tt>), the <i>d</i> argument is a <font SIZE="-1">TCP</font> port number, not a display number.
</dd><dt><b>websocket</b>
</dt><dd> Opens an additional <font SIZE="-1">TCP</font> listening port dedicated to <font SIZE="-1">VNC</font> Websocket connections. By definition the Websocket port is 5700+<i>display</i>. If <i>host</i> is specified connections will only be allowed from this host. As an alternative the Websocket port could be specified by using <tt>&quot;websocket&quot;</tt>=<i>port</i>. <font SIZE="-1">TLS</font> encryption for the Websocket connection is supported if the required certificates are specified with the <font SIZE="-1">VNC</font> option <b>x509</b>.
</dd><dt><b>password</b>
</dt><dd> Require that password based authentication is used for client connections. 
 The password must be set separately using the <tt>&quot;set_password&quot;</tt> command in the <b>pcsys_monitor</b>. The syntax to change your password is: <tt>&quot;set_password &lt;protocol&gt; &lt;password&gt;&quot;</tt> where &lt;protocol&gt; could be either ``vnc'' or ``spice''. 
 If you would like to change &lt;protocol&gt; password expiration, you should use <tt>&quot;expire_password &lt;protocol&gt; &lt;expiration-time&gt;&quot;</tt> where expiration time could be one of the following options: now, never, +seconds or <font SIZE="-1">UNIX</font> time of expiration, e.g. +60 to make password expire in 60 seconds, or 1335196800 to make password expire on ``Mon Apr 23 12:00:00 <font SIZE="-1">EDT 2012'' </font>(<font SIZE="-1">UNIX</font> time for this date and time). 
 You can also use keywords ``now'' or ``never'' for the expiration time to allow &lt;protocol&gt; password to expire immediately or never expire.
</dd><dt><b>tls</b>
</dt><dd> Require that client use <font SIZE="-1">TLS</font> when communicating with the <font SIZE="-1">VNC</font> server. This uses anonymous <font SIZE="-1">TLS</font> credentials so is susceptible to a man-in-the-middle attack. It is recommended that this option be combined with either the <b>x509</b> or <b>x509verify</b> options.
</dd><dt><b>x509=</b><i>/path/to/certificate/dir</i>
</dt><dd> Valid if <b>tls</b> is specified. Require that x509 credentials are used for negotiating the <font SIZE="-1">TLS</font> session. The server will send its x509 certificate to the client. It is recommended that a password be set on the <font SIZE="-1">VNC</font> server to provide authentication of the client when this is used. The path following this option specifies where the x509 certificates are to be loaded from. See the <b>vnc_security</b> section for details on generating certificates.
</dd><dt><b>x509verify=</b><i>/path/to/certificate/dir</i>
</dt><dd> Valid if <b>tls</b> is specified. Require that x509 credentials are used for negotiating the <font SIZE="-1">TLS</font> session. The server will send its x509 certificate to the client, and request that the client send its own x509 certificate. The server will validate the client's certificate against the <font SIZE="-1">CA</font> certificate, and reject clients when validation fails. If the certificate authority is trusted, this is a sufficient authentication mechanism. You may still wish to set a password on the <font SIZE="-1">VNC</font> server as a second authentication layer. The path following this option specifies where the x509 certificates are to be loaded from. See the <b>vnc_security</b> section for details on generating certificates.
</dd><dt><b>sasl</b>
</dt><dd> Require that the client use <font SIZE="-1">SASL</font> to authenticate with the <font SIZE="-1">VNC</font> server. The exact choice of authentication method used is controlled from the system / user's <font SIZE="-1">SASL</font> configuration file for the 'qemu' service. This is typically found in /etc/sasl2/qemu.conf. If running <font SIZE="-1">QEMU</font> as an unprivileged user, an environment variable <font SIZE="-1">SASL_CONF_PATH</font> can be used to make it search alternate locations for the service config. While some <font SIZE="-1">SASL</font> auth methods can also provide data encryption (eg <font SIZE="-1">GSSAPI</font>), it is recommended that <font SIZE="-1">SASL</font> always be combined with the 'tls' and 'x509' settings to enable use of <font SIZE="-1">SSL</font> and server certificates. This ensures a data encryption preventing compromise of authentication credentials. See the <b>vnc_security</b> section for details on using <font SIZE="-1">SASL</font> authentication.
</dd><dt><b>acl</b>
</dt><dd> Turn on access control lists for checking of the x509 client certificate and <font SIZE="-1">SASL</font> party. For x509 certs, the <font SIZE="-1">ACL</font> check is made against the certificate's distinguished name. This is something that looks like <tt>&quot;C=GB,O=ACME,L=Boston,CN=bob&quot;</tt>. For <font SIZE="-1">SASL</font> party, the <font SIZE="-1">ACL</font> check is made against the username, which depending on the <font SIZE="-1">SASL</font> plugin, may include a realm component, eg <tt>&quot;bob&quot;</tt> or <tt>&quot;bob [at] EXAMPLE.COM&quot;</tt>. When the <b>acl</b> flag is set, the initial access list will be empty, with a <tt>&quot;deny&quot;</tt> policy. Thus no one will be allowed to use the <font SIZE="-1">VNC</font> server until the ACLs have been loaded. This can be achieved using the <tt>&quot;acl&quot;</tt> monitor command.
</dd><dt><b>lossy</b>
</dt><dd> Enable lossy compression methods (gradient, <font SIZE="-1">JPEG, ...</font>). If this option is set, <font SIZE="-1">VNC</font> client may receive lossy framebuffer updates depending on its encoding settings. Enabling this option can save a lot of bandwidth at the expense of quality.
</dd><dt><b>non-adaptive</b>
</dt><dd> Disable adaptive encodings. Adaptive encodings are enabled by default. An adaptive encoding will try to detect frequently updated screen regions, and send updates in these regions using a lossy encoding (like <font SIZE="-1">JPEG</font>). This can be really helpful to save bandwidth when playing videos. Disabling adaptive encodings allows to restore the original static behavior of encodings like Tight.
</dd><dt><b>share=[allow-exclusive|force-shared|ignore]</b>
</dt><dd> Set display sharing policy. 'allow-exclusive' allows clients to ask for exclusive access. As suggested by the rfb spec this is implemented by dropping other connections. Connecting multiple clients in parallel requires all clients asking for a shared session (vncviewer: -shared switch). This is the default. 'force-shared' disables exclusive client access. Useful for shared desktop sessions, where you don't want someone forgetting specify -shared disconnect everybody else. 'ignore' completely ignores the shared flag and allows everybody connect unconditionally. Doesn't conform to the rfb spec but is traditional <font SIZE="-1">QEMU</font> behavior.</dd></dl>
</dl>

<dl>
</dl>
</dl>
 

 i386 target only:
<dl>
<dt><b>-win2k-hack</b>
</dt><dd> Use it when installing Windows 2000 to avoid a disk full bug. After Windows 2000 is installed, you no longer need this option (this option slows down the <font SIZE="-1">IDE</font> transfers).
</dd><dt><b>-no-fd-bootchk</b>
</dt><dd> Disable boot signature checking for floppy disks in <font SIZE="-1">BIOS.</font> May be needed to boot from old floppy disks.
</dd><dt><b>-no-acpi</b>
</dt><dd> Disable <font SIZE="-1">ACPI </font>(Advanced Configuration and Power Interface) support. Use it if your guest <font SIZE="-1">OS</font> complains about <font SIZE="-1">ACPI</font> problems (<font SIZE="-1">PC</font> target machine only).
</dd><dt><b>-acpitable [sig=</b><i>str</i><b>][,rev=</b><i>n</i><b>][,oem_id=</b><i>str</i><b>][,oem_table_id=</b><i>str</i><b>][,oem_rev=</b><i>n</i><b>] [,asl_compiler_id=</b><i>str</i><b>][,asl_compiler_rev=</b><i>n</i><b>][,data=</b><i>file1</i><b>[:</b><i>file2</i><b>]...]</b>
</dt><dd> Add <font SIZE="-1">ACPI</font> table with specified header fields and context from specified files. For file=, take whole <font SIZE="-1">ACPI</font> table from the specified files, including all <font SIZE="-1">ACPI</font> headers (possible overridden by other options). For data=, only data portion of the table is used, all header information is specified in the command line. If a <font SIZE="-1">SLIC</font> table is supplied to <font SIZE="-1">QEMU,</font> then the <font SIZE="-1">SLIC</font>'s oem_id and oem_table_id fields will override the same in the <font SIZE="-1">RSDT</font> and the <font SIZE="-1">FADT </font>(a.k.a. <font SIZE="-1">FACP</font>), in order to ensure the field matches required by the Microsoft <font SIZE="-1">SLIC</font> spec and the <font SIZE="-1">ACPI</font> spec.
</dd><dt><b>-smbios file=</b><i>binary</i>
</dt><dd> Load <font SIZE="-1">SMBIOS</font> entry from binary file.
</dd><dt><b>-smbios type=0[,vendor=</b><i>str</i><b>][,version=</b><i>str</i><b>][,date=</b><i>str</i><b>][,release=</b><i>%d.%d</i><b>]</b>
</dt><dd> Specify <font SIZE="-1">SMBIOS</font> type 0 fields
</dd><dt><b>-smbios type=1[,manufacturer=</b><i>str</i><b>][,product=</b><i>str</i><b>] [,version=</b><i>str</i><b>][,serial=</b><i>str</i><b>][,uuid=</b><i>uuid</i><b>][,sku=</b><i>str</i><b>] [,family=</b><i>str</i><b>]</b>
</dt><dd> Specify <font SIZE="-1">SMBIOS</font> type 1 fields</dd></dl>
 

 Network options:
<dl>
<dt><b>-net nic[,vlan=</b><i>n</i><b>][,macaddr=</b><i>mac</i><b>][,model=</b><i>type</i><b>] [,name=</b><i>name</i><b>][,addr=</b><i>addr</i><b>][,vectors=</b><i>v</i><b>]</b>
</dt><dd> Create a new Network Interface Card and connect it to <font SIZE="-1">VLAN </font><i>n</i> (<i>n</i> = 0 is the default). The <font SIZE="-1">NIC</font> is an e1000 by default on the <font SIZE="-1">PC</font> target. Optionally, the <font SIZE="-1">MAC</font> address can be changed to <i>mac</i>, the device address set to <i>addr</i> (<font SIZE="-1">PCI</font> cards only), and a <i>name</i> can be assigned for use in monitor commands. Optionally, for <font SIZE="-1">PCI</font> cards, you can specify the number <i>v</i> of MSI-X vectors that the card should have; this option currently only affects virtio cards; set <i>v</i> = 0 to disable MSI-X. If no <b>-net</b> option is specified, a single <font SIZE="-1">NIC</font> is created. <font SIZE="-1">QEMU</font> can emulate several different models of network card. Valid values for <i>type</i> are <tt>&quot;virtio&quot;</tt>, <tt>&quot;i82551&quot;</tt>, <tt>&quot;i82557b&quot;</tt>, <tt>&quot;i82559er&quot;</tt>, <tt>&quot;ne2k_pci&quot;</tt>, <tt>&quot;ne2k_isa&quot;</tt>, <tt>&quot;pcnet&quot;</tt>, <tt>&quot;rtl8139&quot;</tt>, <tt>&quot;e1000&quot;</tt>, <tt>&quot;smc91c111&quot;</tt>, <tt>&quot;lance&quot;</tt> and <tt>&quot;mcf_fec&quot;</tt>. Not all devices are supported on all targets. Use <tt>&quot;-net nic,model=help&quot;</tt> for a list of available devices for your target.
</dd><dt><b>-netdev user,id=</b><i>id</i><b>[,</b><i>option</i><b>][,</b><i>option</i><b>][,...]</b>
</dt><dd>
</dd><dt><b>-net user[,</b><i>option</i><b>][,</b><i>option</i><b>][,...]</b>
</dt><dd> Use the user mode network stack which requires no administrator privilege to run. Valid options are:
</dd><dl>
<dl>
<dt><b>vlan=</b><i>n</i>
</dt><dd> Connect user mode stack to <font SIZE="-1">VLAN </font><i>n</i> (<i>n</i> = 0 is the default).
</dd><dt><b>id=</b><i>id</i>
</dt><dd>
</dd><dt><b>name=</b><i>name</i>
</dt><dd> Assign symbolic name for use in monitor commands.
</dd><dt><b>net=</b><i>addr</i><b>[/</b><i>mask</i><b>]</b>
</dt><dd> Set <font SIZE="-1">IP</font> network address the guest will see. Optionally specify the netmask, either in the form a.b.c.d or as number of valid top-most bits. Default is 10.0.2.0/24.
</dd><dt><b>host=</b><i>addr</i>
</dt><dd> Specify the guest-visible address of the host. Default is the 2nd <font SIZE="-1">IP</font> in the guest network, i.e. x.x.x.2.
</dd><dt><b>restrict=on|off</b>
</dt><dd> If this option is enabled, the guest will be isolated, i.e. it will not be able to contact the host and no guest <font SIZE="-1">IP</font> packets will be routed over the host to the outside. This option does not affect any explicitly set forwarding rules.
</dd><dt><b>hostname=</b><i>name</i>
</dt><dd> Specifies the client hostname reported by the built-in <font SIZE="-1">DHCP</font> server.
</dd><dt><b>dhcpstart=</b><i>addr</i>
</dt><dd> Specify the first of the 16 IPs the built-in <font SIZE="-1">DHCP</font> server can assign. Default is the 15th to 31st <font SIZE="-1">IP</font> in the guest network, i.e. x.x.x.15 to x.x.x.31.
</dd><dt><b>dns=</b><i>addr</i>
</dt><dd> Specify the guest-visible address of the virtual nameserver. The address must be different from the host address. Default is the 3rd <font SIZE="-1">IP</font> in the guest network, i.e. x.x.x.3.
</dd><dt><b>dnssearch=</b><i>domain</i>
</dt><dd> Provides an entry for the domain-search list sent by the built-in <font SIZE="-1">DHCP</font> server. More than one domain suffix can be transmitted by specifying this option multiple times. If supported, this will cause the guest to automatically try to append the given domain suffix(es) in case a domain name can not be resolved. 
 Example: 
 <pre>
        qemu-kvm -net user,dnssearch=mgmt.example.org,dnssearch=example.org [...]
</pre>
</dd><dt><b>tftp=</b><i>dir</i>
</dt><dd> When using the user mode network stack, activate a built-in <font SIZE="-1">TFTP</font> server. The files in <i>dir</i> will be exposed as the root of a <font SIZE="-1">TFTP</font> server. The <font SIZE="-1">TFTP</font> client on the guest must be configured in binary mode (use the command <tt>&quot;bin&quot;</tt> of the Unix <font SIZE="-1">TFTP</font> client).
</dd><dt><b>bootfile=</b><i>file</i>
</dt><dd> When using the user mode network stack, broadcast <i>file</i> as the <font SIZE="-1">BOOTP</font> filename. In conjunction with <b>tftp</b>, this can be used to network boot a guest from a local directory. 
 Example (using pxelinux): 
 <pre>
        qemu-kvm -hda linux.img -boot n -net user,tftp=/path/to/tftp/files,bootfile=/pxelinux.0
</pre>
</dd><dt><b>smb=</b><i>dir</i><b>[,smbserver=</b><i>addr</i><b>]</b>
</dt><dd> When using the user mode network stack, activate a built-in <font SIZE="-1">SMB</font> server so that Windows OSes can access to the host files in <i>dir</i> transparently. The <font SIZE="-1">IP</font> address of the <font SIZE="-1">SMB</font> server can be set to <i>addr</i>. By default the 4th <font SIZE="-1">IP</font> in the guest network is used, i.e. x.x.x.4. 
 In the guest Windows <font SIZE="-1">OS,</font> the line: 
 <pre>
        10.0.2.4 smbserver
</pre> 
 must be added in the file <i>C:\WINDOWS\LMHOSTS</i> (for windows 9x/Me) or <i>C:\WINNT\SYSTEM32\DRIVERS\ETC\LMHOSTS</i> (Windows <font SIZE="-1">NT/2000</font>). 
 Then <i>dir</i> can be accessed in <i>\\smbserver\qemu</i>. 
 Note that a <font SIZE="-1">SAMBA</font> server must be installed on the host <font SIZE="-1">OS. QEMU</font> was tested successfully with smbd versions from Red Hat 9, Fedora Core 3 and OpenSUSE 11.x.
</dd><dt><b>hostfwd=[tcp|udp]:[</b><i>hostaddr</i><b>]:</b><i>hostport</i><b>-[</b><i>guestaddr</i><b>]:</b><i>guestport</i>
</dt><dd> Redirect incoming <font SIZE="-1">TCP</font> or <font SIZE="-1">UDP</font> connections to the host port <i>hostport</i> to the guest <font SIZE="-1">IP</font> address <i>guestaddr</i> on guest port <i>guestport</i>. If <i>guestaddr</i> is not specified, its value is x.x.x.15 (default first address given by the built-in <font SIZE="-1">DHCP</font> server). By specifying <i>hostaddr</i>, the rule can be bound to a specific host interface. If no connection type is set, <font SIZE="-1">TCP</font> is used. This option can be given multiple times. 
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
</dt><dd> Forward guest <font SIZE="-1">TCP</font> connections to the <font SIZE="-1">IP</font> address <i>server</i> on port <i>port</i> to the character device <i>dev</i> or to a program executed by <i>cmd:command</i> which gets spawned for each connection. This option can be given multiple times. 
 You can either use a chardev directly and have that one used throughout <font SIZE="-1">QEMU</font>'s lifetime, like in the following example: 
 <pre>
        # open 10.10.1.1:4321 on bootup, connect 10.0.2.100:1234 to it whenever
        # the guest accesses it
        qemu-kvm -net user,guestfwd=tcp:10.0.2.100:1234-tcp:10.10.1.1:4321 [...]
</pre> 
 Or you can execute a command on every <font SIZE="-1">TCP</font> connection established by the guest, so that <font SIZE="-1">QEMU</font> behaves similar to an inetd process for that virtual server: 
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
</dt><dd> Connect the host <font SIZE="-1">TAP</font> network interface <i>name</i> to <font SIZE="-1">VLAN </font><i>n</i>. 

 Use the network script <i>file</i> to configure it and the network script <i>dfile</i> to deconfigure it. If <i>name</i> is not provided, the <font SIZE="-1">OS</font> automatically provides one. The default network configure script is <i>/etc/qemu-ifup</i> and the default network deconfigure script is <i>/etc/qemu-ifdown</i>. Use <b>script=no</b> or <b>downscript=no</b> to disable script execution. 

 If running <font SIZE="-1">QEMU</font> as an unprivileged user, use the network helper <i>helper</i> to configure the <font SIZE="-1">TAP</font> interface. The default network helper executable is <i>/path/to/qemu-bridge-helper</i>. 

 <b>fd</b>=<i>h</i> can be used to specify the handle of an already opened host <font SIZE="-1">TAP</font> interface. 

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
</dt><dd> Connect a host <font SIZE="-1">TAP</font> network interface to a host bridge device. 

 Use the network helper <i>helper</i> to configure the <font SIZE="-1">TAP</font> interface and attach it to the bridge. The default network helper executable is <i>/path/to/qemu-bridge-helper</i> and the default bridge device is <i>br0</i>. 

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
</dt><dd> Connect the <font SIZE="-1">VLAN </font><i>n</i> to a remote <font SIZE="-1">VLAN</font> in another <font SIZE="-1">QEMU</font> virtual machine using a <font SIZE="-1">TCP</font> socket connection. If <b>listen</b> is specified, <font SIZE="-1">QEMU</font> waits for incoming connections on <i>port</i> (<i>host</i> is optional). <b>connect</b> is used to connect to another <font SIZE="-1">QEMU</font> instance using the <b>listen</b> option. <b>fd</b>=<i>h</i> specifies an already opened <font SIZE="-1">TCP</font> socket. 

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
</dt><dd> Create a <font SIZE="-1">VLAN </font><i>n</i> shared with another <font SIZE="-1">QEMU</font> virtual machines using a <font SIZE="-1">UDP</font> multicast socket, effectively making a bus for every <font SIZE="-1">QEMU</font> with same multicast address <i>maddr</i> and <i>port</i>. <font SIZE="-1">NOTES:</font>
</dd><dl>
<dl>
<dt>1.
</dt><dd> Several <font SIZE="-1">QEMU</font> can be running on different hosts and share same bus (assuming correct multicast setup for these hosts).
</dd><dt>2.
</dt><dd> mcast support is compatible with User Mode Linux (argument <b>eth</b><i>N</i><b>=mcast</b>), see &lt;<b><a rel="nofollow" HREF="http://user-mode-linux.sf.net">http://user-mode-linux.sf.net</a></b>&gt;.
</dd><dt>3.
</dt><dd> Use <b>fd=h</b> to specify an already opened <font SIZE="-1">UDP</font> multicast socket.</dd></dl>
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
</dt><dd> Connect <font SIZE="-1">VLAN </font><i>n</i> to <font SIZE="-1">PORT </font><i>n</i> of a vde switch running on host and listening for incoming connections on <i>socketpath</i>. Use <font SIZE="-1">GROUP </font><i>groupname</i> and <font SIZE="-1">MODE </font><i>octalmode</i> to change default ownership and permissions for communication port. This option is only available if <font SIZE="-1">QEMU</font> has been compiled with vde support enabled. 

 Example: 

 <pre>
        # launch vde switch
        vde_switch -F -sock /tmp/myswitch
        # launch QEMU instance
        qemu-kvm linux.img -net nic -net vde,sock=/tmp/myswitch
</pre>
</dd><dt><b>-netdev hubport,id=</b><i>id</i><b>,hubid=</b><i>hubid</i>
</dt><dd> Create a hub port on <font SIZE="-1">QEMU </font>``vlan'' <i>hubid</i>. 

 The hubport netdev lets you connect a <font SIZE="-1">NIC</font> to a <font SIZE="-1">QEMU </font>``vlan'' instead of a single netdev. <tt>&quot;-net&quot;</tt> and <tt>&quot;-device&quot;</tt> with parameter <b>vlan</b> create the required hub automatically.
</dd><dt><b>-net dump[,vlan=</b><i>n</i><b>][,file=</b><i>file</i><b>][,len=</b><i>len</i><b>]</b>
</dt><dd> Dump network traffic on <font SIZE="-1">VLAN </font><i>n</i> to file <i>file</i> (<i>qemu-vlan0.pcap</i> by default). At most <i>len</i> bytes (64k by default) per packet are stored. The file format is libpcap, so it can be analyzed with tools such as tcpdump or Wireshark.
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
</dd><dt><b>-chardev socket ,id=</b><i>id</i> <b>[</b><i></i><font SIZE="-1"><i>TCP</i></font><i> options</i> <b>or</b> <i>unix options</i><b>] [,server] [,nowait] [,telnet]</b>
</dt><dd> Create a two-way stream socket, which can be either a <font SIZE="-1">TCP</font> or a unix socket. A unix socket will be created if <b>path</b> is specified. Behaviour is undefined if <font SIZE="-1">TCP</font> options are specified for a unix socket. 
 <b>server</b> specifies that the socket shall be a listening socket. 
 <b>nowait</b> specifies that <font SIZE="-1">QEMU</font> should not block waiting for a client to connect to a listening socket. 
 <b>telnet</b> specifies that traffic on the socket should interpret telnet escape sequences. 
 <font SIZE="-1">TCP</font> and unix socket options are given below:
</dd><dl>
<dl>
<dt><font SIZE="-1"><b>TCP</b></font><b> options: port=</b><i>port</i> <b>[,host=</b><i>host</i><b>] [,to=</b><i>to</i><b>] [,ipv4] [,ipv6] [,nodelay]</b>
</dt><dd> <b>host</b> for a listening socket specifies the local address to be bound. For a connecting socket species the remote host to connect to. <b>host</b> is optional for listening sockets. If not specified it defaults to <tt>0.0.0.0</tt>. 
 <b>port</b> for a listening socket specifies the local port to be bound. For a connecting socket specifies the port on the remote host to connect to. <b>port</b> can be given as either a port number or a service name. <b>port</b> is required. 
 <b>to</b> is only relevant to listening sockets. If it is specified, and <b>port</b> cannot be bound, <font SIZE="-1">QEMU</font> will attempt to bind to subsequent ports up to and including <b>to</b> until it succeeds. <b>to</b> must be specified as a port number. 
 <b>ipv4</b> and <b>ipv6</b> specify that either IPv4 or IPv6 must be used. If neither is specified the socket may use either protocol. 
 <b>nodelay</b> disables the Nagle algorithm.
</dd><dt><b>unix options: path=</b><i>path</i>
</dt><dd> <b>path</b> specifies the local path of the unix socket. <b>path</b> is required.</dd></dl>
</dl>

<dl>
</dl>

<dt><b>-chardev udp ,id=</b><i>id</i> <b>[,host=</b><i>host</i><b>] ,port=</b><i>port</i> <b>[,localaddr=</b><i>localaddr</i><b>] [,localport=</b><i>localport</i><b>] [,ipv4] [,ipv6]</b>
</dt><dd> Sends all traffic from the guest to a remote host over <font SIZE="-1">UDP.</font> 

 <b>host</b> specifies the remote host to connect to. If not specified it defaults to <tt>&quot;localhost&quot;</tt>. 

 <b>port</b> specifies the port on the remote host to connect to. <b>port</b> is required. 

 <b>localaddr</b> specifies the local address to bind to. If not specified it defaults to <tt>0.0.0.0</tt>. 

 <b>localport</b> specifies the local port to bind to. If not specified any available local port will be used. 

 <b>ipv4</b> and <b>ipv6</b> specify that either IPv4 or IPv6 must be used. If neither is specified the device may use either protocol.
</dd><dt><b>-chardev msmouse ,id=</b><i>id</i>
</dt><dd> Forward <font SIZE="-1">QEMU</font>'s emulated msmouse events to the guest. <b>msmouse</b> does not take any options.
</dd><dt><b>-chardev vc ,id=</b><i>id</i> <b>[[,width=</b><i>width</i><b>] [,height=</b><i>height</i><b>]] [[,cols=</b><i>cols</i><b>] [,rows=</b><i>rows</i><b>]]</b>
</dt><dd> Connect to a <font SIZE="-1">QEMU</font> text console. <b>vc</b> may optionally be given a specific size. 

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

 On other hosts, 2 pipes will be created called <i></i>path<i>.in</i> and <i></i>path<i>.out</i>. Data written to <i></i>path<i>.in</i> will be received by the guest. Data written by the guest can be read from <i></i>path<i>.out</i>. <font SIZE="-1">QEMU</font> will not create these fifos, and requires them to be present. 

 <b>path</b> forms part of the pipe path as described above. <b>path</b> is required.
</dd><dt><b>-chardev console ,id=</b><i>id</i>
</dt><dd> Send traffic from the guest to <font SIZE="-1">QEMU</font>'s standard output. <b>console</b> does not take any options. 

 <b>console</b> is only available on Windows hosts.
</dd><dt><b>-chardev serial ,id=</b><i>id</i> <b>,path=</b><b>path</b>
</dt><dd> Send traffic from the guest to a serial device on the host. 

 On Unix hosts serial will actually accept any tty device, not only serial lines. 

 <b>path</b> specifies the name of the serial device to open.
</dd><dt><b>-chardev pty ,id=</b><i>id</i>
</dt><dd> Create a new pseudo-terminal on the host and connect to it. <b>pty</b> does not take any options. 

 <b>pty</b> is not available on Windows hosts.
</dd><dt><b>-chardev stdio ,id=</b><i>id</i> <b>[,signal=on|off]</b>
</dt><dd> Connect to standard input and standard output of the <font SIZE="-1">QEMU</font> process. 

 <b>signal</b> controls if signals are enabled on the terminal, that includes exiting <font SIZE="-1">QEMU</font> with the key sequence <b>Control-c</b>. This option is enabled by default, use <b>signal=off</b> to disable it. 

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
 

 Device <font SIZE="-1">URL</font> Syntax: 

 In addition to using normal file images for the emulated storage devices, <font SIZE="-1">QEMU</font> can also use networked resources such as iSCSI devices. These are specified using a special <font SIZE="-1">URL</font> syntax.
<dl>
<dt><b>iSCSI</b>
</dt><dd> iSCSI support allows <font SIZE="-1">QEMU</font> to access iSCSI resources directly and use as images for the guest storage. Both disk and cdrom images are supported. 
 Syntax for specifying iSCSI LUNs is ``iscsi://&lt;target-ip&gt;[:&lt;port&gt;]/&lt;target-iqn&gt;/&lt;lun&gt;'' 
 By default qemu-kvm will use the iSCSI initiator-name 'iqn.2008-11.org.linux-kvm[:&lt;name&gt;]' but this can also be set from the command line or a configuration file. 
 Example (without authentication): 
 <pre>
        qemu-kvm -iscsi initiator-name=iqn.2001-04.com.example:my-initiator \
        -cdrom <a HREF="iscsi://192.0.2.1/iqn.2001-04.com.example/2">iscsi://192.0.2.1/iqn.2001-04.com.example/2</a> \
        -drive file=<a HREF="iscsi://192.0.2.1/iqn.2001-04.com.example/1">iscsi://192.0.2.1/iqn.2001-04.com.example/1</a>
</pre> 
 Example (<font SIZE="-1">CHAP</font> username/password via <font SIZE="-1">URL</font>): 
 <pre>
        qemu-kvm -drive file=<a HREF="iscsi://user%password@192.0.2.1/iqn.2001-04.com.example/1">iscsi://user%password@192.0.2.1/iqn.2001-04.com.example/1</a>
</pre> 
 Example (<font SIZE="-1">CHAP</font> username/password via environment variables): 
 <pre>
        LIBISCSI_CHAP_USERNAME=&quot;user&quot; \
        LIBISCSI_CHAP_PASSWORD=&quot;password&quot; \
        qemu-kvm -drive file=<a HREF="iscsi://192.0.2.1/iqn.2001-04.com.example/1">iscsi://192.0.2.1/iqn.2001-04.com.example/1</a>
</pre> 
 iSCSI support is an optional feature of <font SIZE="-1">QEMU</font> and only available when compiled and linked against libiscsi. 
 iSCSI parameters such as username and password can also be specified via a configuration file. See qemu-doc for more information and examples.
</dd><dt><font SIZE="-1"><b>NBD</b></font>
</dt><dd> <font SIZE="-1">QEMU</font> supports <font SIZE="-1">NBD </font>(Network Block Devices) both using <font SIZE="-1">TCP</font> protocol as well as Unix Domain Sockets. 
 Syntax for specifying a <font SIZE="-1">NBD</font> device using <font SIZE="-1">TCP </font>``nbd:&lt;server-ip&gt;:&lt;port&gt;[:exportname=&lt;export&gt;]'' 
 Syntax for specifying a <font SIZE="-1">NBD</font> device using Unix Domain Sockets ``nbd:unix:&lt;domain-socket&gt;[:exportname=&lt;export&gt;]'' 
 Example for <font SIZE="-1">TCP</font> 
 <pre>
        qemu-kvm --drive file=nbd:192.0.2.1:30000
</pre> 
 Example for Unix Domain Sockets 
 <pre>
        qemu-kvm --drive file=nbd:unix:/tmp/nbd-socket
</pre>
</dd><dt><font SIZE="-1"><b>SSH</b></font>
</dt><dd> <font SIZE="-1">QEMU</font> supports <font SIZE="-1">SSH </font>(Secure Shell) access to remote disks. 
 Examples: 
 <pre>
        qemu-kvm -drive file=<a HREF="ssh://user@host/path/to/disk.img">ssh://user@host/path/to/disk.img</a>
        qemu-kvm -drive file.driver=ssh,file.user=user,file.host=host,file.port=22,file.path=/path/to/disk.img
</pre> 
 Currently authentication must be done using ssh-agent. Other authentication methods may be supported in future.
</dd><dt><b>Sheepdog</b>
</dt><dd> Sheepdog is a distributed storage system for <font SIZE="-1">QEMU. QEMU</font> supports using either local sheepdog devices or remote networked devices. 
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
</dt><dd> GlusterFS is an user space distributed file system. <font SIZE="-1">QEMU</font> supports the use of GlusterFS volumes for hosting <font SIZE="-1">VM</font> disk images using <font SIZE="-1">TCP,</font> Unix Domain Sockets and <font SIZE="-1">RDMA</font> transport protocols. 
 Syntax for specifying a <font SIZE="-1">VM</font> disk image on GlusterFS volume is 
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
</dt><dd> Defines the function of the corresponding Bluetooth <font SIZE="-1">HCI. </font> -bt options are matched with the HCIs present in the chosen machine type. For example when emulating a machine with only one <font SIZE="-1">HCI</font> built into it, only the first <tt>&quot;-bt hci[...]&quot;</tt> option is valid and defines the <font SIZE="-1">HCI</font>'s logic. The Transport Layer is decided by the machine type. Currently the machines <tt>&quot;n800&quot;</tt> and <tt>&quot;n810&quot;</tt> have one <font SIZE="-1">HCI</font> and all other machines have none. 
 The following three types are recognized:
</dd><dl>
<dl>
<dt><b>-bt hci,null</b>
</dt><dd> (default) The corresponding Bluetooth <font SIZE="-1">HCI</font> assumes no internal logic and will not respond to any <font SIZE="-1">HCI</font> commands or emit events.
</dd><dt><b>-bt hci,host[:</b><i>id</i><b>]</b>
</dt><dd> (<tt>&quot;bluez&quot;</tt> only) The corresponding <font SIZE="-1">HCI</font> passes commands / events to / from the physical <font SIZE="-1">HCI</font> identified by the name <i>id</i> (default: <tt>&quot;hci0&quot;</tt>) on the computer running <font SIZE="-1">QEMU. </font> Only available on <tt>&quot;bluez&quot;</tt> capable systems like Linux.
</dd><dt><b>-bt hci[,vlan=</b><i>n</i><b>]</b>
</dt><dd> Add a virtual, standard <font SIZE="-1">HCI</font> that will participate in the Bluetooth scatternet <i>n</i> (default <tt>0</tt>). Similarly to <b>-net</b> VLANs, devices inside a bluetooth network <i>n</i> can only communicate with other devices in the same network (scatternet).</dd></dl>
</dl>

<dl>
</dl>

<dt><b>-bt vhci[,vlan=</b><i>n</i><b>]</b>
</dt><dd> (Linux-host only) Create a <font SIZE="-1">HCI</font> in scatternet <i>n</i> (default 0) attached to the host bluetooth stack instead of to the emulated target. This allows the host and target machines to participate in a common scatternet and communicate. Requires the Linux <tt>&quot;vhci&quot;</tt> driver installed. Can be used as following: 

 <pre>
        qemu-kvm [...OPTIONS...] -bt hci,vlan=5 -bt vhci,vlan=5
</pre>
</dd><dt><b>-bt device:</b><i>dev</i><b>[,vlan=</b><i>n</i><b>]</b>
</dt><dd> Emulate a bluetooth device <i>dev</i> and place it in network <i>n</i> (default <tt>0</tt>). <font SIZE="-1">QEMU</font> can only emulate one type of bluetooth devices currently:
</dd><dl>
<dl>
<dt><b>keyboard</b>
</dt><dd> Virtual wireless keyboard implementing the <font SIZE="-1">HIDP</font> bluetooth profile.</dd></dl>
</dl>

<dl>
</dl>
</dl>
 

 <font SIZE="-1">TPM</font> device options: 

 The general form of a <font SIZE="-1">TPM</font> device option is:
<dl>
<dt><b>-tpmdev</b> <i>backend</i> <b>,id=</b><i>id</i> <b>[,</b><i>options</i><b>]</b>
</dt><dd> Backend type must be: <b>passthrough</b>. 
 The specific backend type will determine the applicable options. The <tt>&quot;-tpmdev&quot;</tt> option creates the <font SIZE="-1">TPM</font> backend and requires a <tt>&quot;-device&quot;</tt> option that specifies the <font SIZE="-1">TPM</font> frontend interface model. 
 Options to each backend are described below. 
 Use 'help' to print all available <font SIZE="-1">TPM</font> backend types. 
 <pre>
        qemu-kvm -tpmdev help
</pre>
</dd><dt><b>-tpmdev passthrough, id=</b><i>id</i><b>, path=</b><i>path</i><b>, cancel-path=</b><i>cancel-path</i>
</dt><dd> (Linux-host only) Enable access to the host's <font SIZE="-1">TPM</font> using the passthrough driver. 
 <b>path</b> specifies the path to the host's <font SIZE="-1">TPM</font> device, i.e., on a Linux host this would be <tt>&quot;/dev/tpm0&quot;</tt>. <b>path</b> is optional and by default <tt>&quot;/dev/tpm0&quot;</tt> is used. 
 <b>cancel-path</b> specifies the path to the host <font SIZE="-1">TPM</font> device's sysfs entry allowing for cancellation of an ongoing <font SIZE="-1">TPM</font> command. <b>cancel-path</b> is optional and by default <font SIZE="-1">QEMU</font> will search for the sysfs entry to use. 
 Some notes about using the host's <font SIZE="-1">TPM</font> with the passthrough driver: 
 The <font SIZE="-1">TPM</font> device accessed by the passthrough driver must not be used by any other application on the host. 
 Since the host's firmware (<font SIZE="-1">BIOS/UEFI</font>) has already initialized the <font SIZE="-1">TPM,</font> the <font SIZE="-1">VM</font>'s firmware (<font SIZE="-1">BIOS/UEFI</font>) will not be able to initialize the <font SIZE="-1">TPM</font> again and may therefore not show a TPM-specific menu that would otherwise allow the user to configure the <font SIZE="-1">TPM,</font> e.g., allow the user to enable/disable or activate/deactivate the <font SIZE="-1">TPM.</font> Further, if <font SIZE="-1">TPM</font> ownership is released from within a <font SIZE="-1">VM</font> then the host's <font SIZE="-1">TPM</font> will get disabled and deactivated. To enable and activate the <font SIZE="-1">TPM</font> again afterwards, the host has to be rebooted and the user is required to enter the firmware's menu to enable and activate the <font SIZE="-1">TPM.</font> If the <font SIZE="-1">TPM</font> is left disabled and/or deactivated most <font SIZE="-1">TPM</font> commands will fail. 
 To create a passthrough <font SIZE="-1">TPM</font> use the following two options: 
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
</dt><dd> [Linux only] Pseudo <font SIZE="-1">TTY </font>(a new <font SIZE="-1">PTY</font> is automatically allocated)
</dd><dt><b>none</b>
</dt><dd> No device is allocated.
</dd><dt><b>null</b>
</dt><dd> void device
</dd><dt><b>/dev/XXX</b>
</dt><dd> [Linux only] Use host tty, e.g. <i>/dev/ttyS0</i>. The host serial port parameters are set according to the emulated ones.
</dd><dt><b>/dev/parport</b><i>N</i>
</dt><dd> [Linux only, parallel port only] Use host parallel port <i>N</i>. Currently <font SIZE="-1">SPP</font> and <font SIZE="-1">EPP</font> parallel port features can be used.
</dd><dt><b>file:</b><i>filename</i>
</dt><dd> Write output to <i>filename</i>. No character can be read.
</dd><dt><b>stdio</b>
</dt><dd> [Unix only] standard input/output
</dd><dt><b>pipe:</b><i>filename</i>
</dt><dd> name pipe <i>filename</i>
</dd><dt><font SIZE="-1"><b>COM</b></font><i>n</i>
</dt><dd> [Windows only] Use host serial port <i>n</i>
</dd><dt><b>udp:[</b><i>remote_host</i><b>]:</b><i>remote_port</i><b>[@[</b><i>src_ip</i><b>]:</b><i>src_port</i><b>]</b>
</dt><dd> This implements <font SIZE="-1">UDP</font> Net Console. When <i>remote_host</i> or <i>src_ip</i> are not specified they default to <tt>0.0.0.0</tt>. When not using a specified <i>src_port</i> a random port is automatically chosen. 
 If you just want a simple readonly console you can use <tt>&quot;netcat&quot;</tt> or <tt>&quot;nc&quot;</tt>, by starting <font SIZE="-1">QEMU</font> with: <tt>&quot;-serial udp::4555&quot;</tt> and nc as: <tt>&quot;nc -u -l -p 4555&quot;</tt>. Any time <font SIZE="-1">QEMU</font> writes something to that port it will appear in the netconsole session. 
 If you plan to send characters back via netconsole or you want to stop and start <font SIZE="-1">QEMU</font> a lot of times, you should have <font SIZE="-1">QEMU</font> use the same source port each time by using something like <tt>&quot;-serial udp::4555 [at] 4556&quot;</tt> to <font SIZE="-1">QEMU.</font> Another approach is to use a patched version of netcat which can listen to a <font SIZE="-1">TCP</font> port and send and receive characters via udp. If you have a patched version of netcat which activates telnet remote echo and single char transfer, then you can use the following options to step up a netcat redirector to allow telnet on port 5555 to access the <font SIZE="-1">QEMU</font> port.
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
</dt><dd> The <font SIZE="-1">TCP</font> Net Console has two modes of operation. It can send the serial I/O to a location or wait for a connection from a location. By default the <font SIZE="-1">TCP</font> Net Console is sent to <i>host</i> at the <i>port</i>. If you use the <i>server</i> option <font SIZE="-1">QEMU</font> will wait for a client socket application to connect to the port before continuing, unless the <tt>&quot;nowait&quot;</tt> option was specified. The <tt>&quot;nodelay&quot;</tt> option disables the Nagle buffering algorithm. If <i>host</i> is omitted, 0.0.0.0 is assumed. Only one <font SIZE="-1">TCP</font> connection at a time is accepted. You can use <tt>&quot;telnet&quot;</tt> to connect to the corresponding character device.
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
</dt><dd> The telnet protocol is used instead of raw tcp sockets. The options work the same as if you had specified <tt>&quot;-serial tcp&quot;</tt>. The difference is that the port acts like a telnet server or client using telnet option negotiation. This will also allow you to send the <font SIZE="-1">MAGIC_SYSRQ</font> sequence if you use a telnet that supports sending the break sequence. Typically in unix telnet you do it with Control-] and then type ``send break'' followed by pressing the enter key.
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
</dt><dd> Store the <font SIZE="-1">QEMU</font> process <font SIZE="-1">PID</font> in <i>file</i>. It is useful if you launch <font SIZE="-1">QEMU</font> from a script.
</dd><dt><b>-singlestep</b>
</dt><dd> Run the emulation in single step mode.
</dd><dt><b>-S</b>
</dt><dd> Do not start <font SIZE="-1">CPU</font> at startup (you must type 'c' in the monitor).
</dd><dt><b>-realtime mlock=on|off</b>
</dt><dd> Run qemu-kvm with realtime features. mlocking qemu-kvm and guest memory can be enabled via <b>mlock=on</b> (enabled by default).
</dd><dt><b>-gdb</b> <i>dev</i>
</dt><dd> Wait for gdb connection on device <i>dev</i>. Typical connections will likely be TCP-based, but also <font SIZE="-1">UDP,</font> pseudo <font SIZE="-1">TTY,</font> or even stdio are reasonable use case. The latter is allowing to start <font SIZE="-1">QEMU</font> from within gdb and establish the connection via a pipe: 

 <pre>
        (gdb) target remote | exec qemu-kvm -gdb stdio ...
</pre>
</dd><dt><b>-s</b>
</dt><dd> Shorthand for -gdb tcp::1234, i.e. open a gdbserver on <font SIZE="-1">TCP</font> port 1234.
</dd><dt><b>-d</b> <i>item1</i><b>[,...]</b>
</dt><dd> Enable logging of specified items. Use '-d help' for a list of log items.
</dd><dt><b>-D</b> <i>logfile</i>
</dt><dd> Output log in <i>logfile</i> instead of to stderr
</dd><dt><b>-L</b> <i>path</i>
</dt><dd> Set the directory for the <font SIZE="-1">BIOS, VGA BIOS</font> and keymaps.
</dd><dt><b>-bios</b> <i>file</i>
</dt><dd> Set the filename for the <font SIZE="-1">BIOS.</font>
</dd><dt><b>-enable-kvm</b>
</dt><dd> Enable <font SIZE="-1">KVM</font> full virtualization support. This option is only available if <font SIZE="-1">KVM</font> support is enabled when compiling.
</dd><dt><b>-xen-domid</b> <i>id</i>
</dt><dd> Specify xen guest domain <i>id</i> (<font SIZE="-1">XEN</font> only).
</dd><dt><b>-xen-create</b>
</dt><dd> Create domain using xen hypercalls, bypassing xend. Warning: should not be used when xend is in use (<font SIZE="-1">XEN</font> only).
</dd><dt><b>-xen-attach</b>
</dt><dd> Attach to existing xen domain. xend will use this when starting <font SIZE="-1">QEMU </font>(<font SIZE="-1">XEN</font> only).
</dd><dt><b>-no-reboot</b>
</dt><dd> Exit instead of rebooting.
</dd><dt><b>-no-shutdown</b>
</dt><dd> Don't exit <font SIZE="-1">QEMU</font> on guest shutdown, but instead only stop the emulation. This allows for instance switching to monitor to commit changes to the disk image.
</dd><dt><b>-loadvm</b> <i>file</i>
</dt><dd> Start right away with a saved state (<tt>&quot;loadvm&quot;</tt> in monitor)
</dd><dt><b>-daemonize</b>
</dt><dd> Daemonize the <font SIZE="-1">QEMU</font> process after initialization. <font SIZE="-1">QEMU</font> will not detach from standard <font SIZE="-1">IO</font> until it is ready to receive connections on any of its devices. This option is a useful way for external programs to launch <font SIZE="-1">QEMU</font> without having to cope with initialization race conditions.
</dd><dt><b>-option-rom</b> <i>file</i>
</dt><dd> Load the contents of <i>file</i> as an option <font SIZE="-1">ROM.</font> This option is useful to load things like EtherBoot.
</dd><dt><b>-clock</b> <i>method</i>
</dt><dd> Force the use of the given methods for timer alarm. To see what timers are available use <tt>&quot;-clock help&quot;</tt>.
</dd><dt><b>-rtc [base=utc|localtime|</b><i>date</i><b>][,clock=host|vm][,driftfix=none|slew]</b>
</dt><dd> Specify <b>base</b> as <tt>&quot;utc&quot;</tt> or <tt>&quot;localtime&quot;</tt> to let the <font SIZE="-1">RTC</font> start at the current <font SIZE="-1">UTC</font> or local time, respectively. <tt>&quot;localtime&quot;</tt> is required for correct date in MS-DOS or Windows. To start at a specific point in time, provide <i>date</i> in the format <tt>&quot;2006-06-17T16:01:21&quot;</tt> or <tt>&quot;2006-06-17&quot;</tt>. The default base is <font SIZE="-1">UTC.</font> 

 By default the <font SIZE="-1">RTC</font> is driven by the host system time. This allows to use the <font SIZE="-1">RTC</font> as accurate reference clock inside the guest, specifically if the host time is smoothly following an accurate external reference clock, e.g. via <font SIZE="-1">NTP.</font> If you want to isolate the guest time from the host, you can set <b>clock</b> to <tt>&quot;rt&quot;</tt> instead. To even prevent it from progressing during suspension, you can set it to <tt>&quot;vm&quot;</tt>. 

 Enable <b>driftfix</b> (i386 targets only) if you experience time drift problems, specifically with Windows' <font SIZE="-1">ACPI HAL.</font> This option will try to figure out how many timer interrupts were not processed by the Windows guest and will re-inject them.
</dd><dt><b>-icount [</b><i>N</i><b>|auto]</b>
</dt><dd> Enable virtual instruction counter. The virtual cpu will execute one instruction every 2^<i>N</i> ns of virtual time. If <tt>&quot;auto&quot;</tt> is specified then the virtual cpu speed will be automatically adjusted to keep virtual time within a few seconds of real time. 

 Note that while this option can give deterministic behavior, it does not provide cycle accurate emulation. Modern CPUs contain superscalar out of order cores with complex cache hierarchies. The number of instructions executed often has little or no correlation with actual performance.
</dd><dt><b>-watchdog</b> <i>model</i>
</dt><dd> Create a virtual hardware watchdog device. Once enabled (by a guest action), the watchdog must be periodically polled by an agent inside the guest or else the guest will be restarted. 

 The <i>model</i> is the model of hardware watchdog to emulate. Choices for model are: <tt>&quot;ib700&quot;</tt> (iBASE 700) which is a very simple <font SIZE="-1">ISA</font> watchdog with a single timer, or <tt>&quot;i6300esb&quot;</tt> (Intel 6300ESB I/O controller hub) which is a much more featureful PCI-based dual-timer watchdog. Choose a model for which your guest has drivers. 

 Use <tt>&quot;-watchdog help&quot;</tt> to list available hardware models. Only one watchdog can be enabled for a guest.
</dd><dt><b>-watchdog-action</b> <i>action</i>
</dt><dd> The <i>action</i> controls what <font SIZE="-1">QEMU</font> will do when the watchdog timer expires. The default is <tt>&quot;reset&quot;</tt> (forcefully reset the guest). Other possible actions are: <tt>&quot;shutdown&quot;</tt> (attempt to gracefully shutdown the guest), <tt>&quot;poweroff&quot;</tt> (forcefully poweroff the guest), <tt>&quot;pause&quot;</tt> (pause the guest), <tt>&quot;debug&quot;</tt> (print a debug message and continue), or <tt>&quot;none&quot;</tt> (do nothing). 

 Note that the <tt>&quot;shutdown&quot;</tt> action requires that the guest responds to <font SIZE="-1">ACPI</font> signals, which it may not be able to do in the sort of situations where the watchdog would have expired, and thus <tt>&quot;-watchdog-action shutdown&quot;</tt> is not recommended for production use. 

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
</dt><dd> Set <font SIZE="-1">TB</font> size.
</dd><dt><b>-incoming</b> <i>port</i>
</dt><dd> Prepare for incoming migration, listen on <i>port</i>.
</dd><dt><b>-nodefaults</b>
</dt><dd> Don't create default devices. Normally, <font SIZE="-1">QEMU</font> sets the default devices like serial port, parallel port, virtual console, monitor device, <font SIZE="-1">VGA</font> adapter, floppy and CD-ROM drive and others. The <tt>&quot;-nodefaults&quot;</tt> option will disable all those default devices.
</dd><dt><b>-chroot</b> <i>dir</i>
</dt><dd> Immediately before starting guest execution, chroot to the specified directory. Especially useful in combination with -runas.
</dd><dt><b>-runas</b> <i>user</i>
</dt><dd> Immediately before starting guest execution, drop root privileges, switching to the specified user.
</dd><dt><b>-prom-env</b> <i>variable</i><b>=</b><i>value</i>
</dt><dd> Set OpenBIOS nvram <i>variable</i> to given <i>value</i> (<font SIZE="-1">PPC, SPARC</font> only).
</dd><dt><b>-semihosting</b>
</dt><dd> Semihosting mode (<font SIZE="-1">ARM, M68K,</font> Xtensa only).
</dd><dt><b>-old-param</b>
</dt><dd> Old param mode (<font SIZE="-1">ARM</font> only).
</dd><dt><b>-sandbox</b> <i>arg</i>
</dt><dd> Enable Seccomp mode 2 system call filter. 'on' will enable syscall filtering and 'off' will disable it. The default is 'off'.
</dd><dt><b>-readconfig</b> <i>file</i>
</dt><dd> Read device configuration from <i>file</i>. This approach is useful when you want to spawn <font SIZE="-1">QEMU</font> process with many command line options but you don't want to exceed the command line character limit.
</dd><dt><b>-writeconfig</b> <i>file</i>
</dt><dd> Write device configuration to <i>file</i>. The <i>file</i> can be either filename to save command line and device configuration into file or dash <tt>&quot;-&quot;</tt>) character to print the output to stdout. This can be later used as input file for <tt>&quot;-readconfig&quot;</tt> option.
</dd><dt><b>-nodefconfig</b>
</dt><dd> Normally <font SIZE="-1">QEMU</font> loads configuration files from <i>sysconfdir</i> and <i>datadir</i> at startup. The <tt>&quot;-nodefconfig&quot;</tt> option will prevent <font SIZE="-1">QEMU</font> from loading any of those config files.
</dd><dt><b>-no-user-config</b>
</dt><dd> The <tt>&quot;-no-user-config&quot;</tt> option makes <font SIZE="-1">QEMU</font> not load any of the user-provided config files on <i>sysconfdir</i>, but won't make it skip the QEMU-provided config files from <i>datadir</i>.
</dd><dt><b>-trace [events=</b><i>file</i><b>][,file=</b><i>file</i><b>]</b>
</dt><dd> Specify tracing options.
</dd><dl>
<dl>
<dt><b>events=</b><i>file</i>
</dt><dd> Immediately enable events listed in <i>file</i>. The file must contain one event name (as listed in the <i>trace-events</i> file) per line. This option is only available if <font SIZE="-1">QEMU</font> has been compiled with either <i>simple</i> or <i>stderr</i> tracing backend.
</dd><dt><b>file=</b><i>file</i>
</dt><dd> Log output traces to <i>file</i>. 
 This option is only available if <font SIZE="-1">QEMU</font> has been compiled with the <i>simple</i> tracing backend.</dd></dl>
</dl>

<dl>
</dl>

<dt><b>-enable-fips</b>
</dt><dd> Enable <font SIZE="-1">FIPS 140-2</font> compliance mode.
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
<dt><b>-g</b> <i>W</i><b>x</b><i>H</i><b>[x</b><i></i><font SIZE="-1"><i>DEPTH</i></font><i></i><b>]</b>
</dt><dd> Set the initial <font SIZE="-1">VGA</font> graphic mode. The default is 800x600x15.
</dd><dt><b>-prom-env</b> <i>string</i>
</dt><dd> Set OpenBIOS variables in <font SIZE="-1">NVRAM,</font> for example: 
 <pre>
        qemu-system-ppc -prom-env 'auto-boot?=false' \
         -prom-env 'boot-device=hd:2,\yaboot' \
         -prom-env 'boot-args=conf=hd:2,\yaboot.conf'
</pre> 
 These variables are not used by Open Hack'Ware.</dd></dl>
 

 The following options are specific to the Sparc32 emulation:
<dl>
<dt><b>-g</b> <i>W</i><b>x</b><i>H</i><b>x[x</b><i></i><font SIZE="-1"><i>DEPTH</i></font><i></i><b>]</b>
</dt><dd> Set the initial <font SIZE="-1">TCX</font> graphic mode. The default is 1024x768x8, currently the only other possible mode is 1024x768x24.
</dd><dt><b>-prom-env</b> <i>string</i>
</dt><dd> Set OpenBIOS variables in <font SIZE="-1">NVRAM,</font> for example: 
 <pre>
        qemu-system-sparc -prom-env 'auto-boot?=false' \
         -prom-env 'boot-device=sd(0,2,0):d' -prom-env 'boot-args=linux single'
</pre>
</dd><dt><b>-M [SS-4|SS-5|SS-10|SS-20|SS-600MP|LX|Voyager|SPARCClassic] [|SPARCbook|SS-2|SS-1000|SS-2000]</b>
</dt><dd> Set the emulated machine type. Default is <font SIZE="-1">SS-5.</font></dd></dl>
 

 The following options are specific to the Sparc64 emulation:
<dl>
<dt><b>-prom-env</b> <i>string</i>
</dt><dd> Set OpenBIOS variables in <font SIZE="-1">NVRAM,</font> for example: 
 <pre>
        qemu-system-sparc64 -prom-env 'auto-boot?=false'
</pre>
</dd><dt><b>-M [sun4u|sun4v|Niagara]</b>
</dt><dd> Set the emulated machine type. The default is sun4u.</dd></dl>

<h2>SEE ALSO</h2>

 The <font SIZE="-1">HTML</font> documentation of <font SIZE="-1">QEMU</font> for more precise information and Linux user mode emulator invocation.

<h2>AUTHOR</h2>

 Fabrice Bellard
