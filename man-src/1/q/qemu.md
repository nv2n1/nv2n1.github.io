---

title: "qemu(1)"
name: "qemu"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qemu/"
description: "qemu-doc – QEMU Emulator User Documentation"
---

<p> qemu-doc &#8211; QEMU Emulator User Documentation </p>
<h2>SYNOPSIS</h2>
<p> usage: qemu-system-i386 [options] [<i>disk_image</i>]</p>
<h2>DESCRIPTION</h2>
<p> The QEMU PC System emulator simulates the following peripherals:</p>
<dl>
<dt>&#8211;</dt>
<dd> i440FX host PCI bridge and PIIX3 PCI to ISA bridge</dd>
<dt>&#8211;</dt>
<dd> Cirrus CLGD 5446 PCI VGA card or dummy VGA card with Bochs VESA extensions (hardware level, including all non standard modes).</dd>
<dt>&#8211;</dt>
<dd> PS/2 mouse and keyboard</dd>
<dt>&#8211;</dt>
<dd> 2 PCI IDE interfaces with hard disk and CD-ROM support</dd>
<dt>&#8211;</dt>
<dd> Floppy disk</dd>
<dt>&#8211;</dt>
<dd> PCI and ISA network adapters</dd>
<dt>&#8211;</dt>
<dd> Serial ports</dd>
<dt>&#8211;</dt>
<dd> Creative SoundBlaster 16 sound card</dd>
<dt>&#8211;</dt>
<dd> ENSONIQ AudioPCI ES1370 sound card</dd>
<dt>&#8211;</dt>
<dd> Intel 82801AA AC97 Audio compatible sound card</dd>
<dt>&#8211;</dt>
<dd> Intel HD Audio Controller and HDA codec</dd>
<dt>&#8211;</dt>
<dd> Adlib (OPL2) &#8211; Yamaha YM3812 compatible chip</dd>
<dt>&#8211;</dt>
<dd> Gravis Ultrasound GF1 sound card</dd>
<dt>&#8211;</dt>
<dd> CS4231A compatible sound card</dd>
<dt>&#8211;</dt>
<dd> PCI UHCI USB controller and a virtual USB hub.</dd></dl>
<p> SMP is supported with up to 255 CPUs. </p>
<p> QEMU uses the PC BIOS from the Seabios project and the Plex86/Bochs LGPL VGA BIOS. </p>
<p> QEMU uses YM3812 emulation by Tatsuyuki Satoh. </p>
<p> QEMU uses GUS emulation (GUSEMU32 &lt;<code><a rel="nofollow" href="http://www.deinmeister.de/gusemu/">http://www.deinmeister.de/gusemu/</a></code>&gt;) by Tibor &#8220;TS&#8221; Schütz. </p>
<p> Note that, by default, GUS shares <i>IRQ</i><i></i>(7) with parallel ports and so QEMU must be told to not have parallel ports to have working GUS. </p>
<pre>
        qemu-system-i386 dos.img -soundhw gus -parallel none
</pre>
<p> Alternatively: </p>
<pre>
        qemu-system-i386 dos.img -device gus,irq=5
</pre>
<p> Or some other unclaimed IRQ. </p>
<p> CS4231A is the chip used in Windows Sound System and GUSMAX products</p>
<h2>OPTIONS</h2>
<p> <i>disk_image</i> is a raw hard disk image for IDE hard disk 0. Some targets do not need a disk image. </p>
<p> Standard options:</p>
<dl>
<dt><code>-h</code></dt>
<dd> Display help and exit</dd>
<dt><code>-version</code></dt>
<dd> Display version information and exit</dd>
<dt><code>-machine [type=]</code><i>name</i><code>[,prop=</code><i>value</i><code>[,&#8230;]]</code></dt>
<dd> Select the emulated machine by <i>name</i>. Use <tt>&quot;-machine help&quot;</tt> to list available machines. Supported machine properties are:</dd>
<dl>
<dl>
<dt><code>accel=</code><i>accels1</i><code>[:</code><i>accels2</i><code>[:&#8230;]]</code></dt>
<dd> This is used to enable an accelerator. Depending on the target architecture, kvm, xen, or tcg can be available. By default, tcg is used. If there is more than one accelerator specified, the next one is used if the previous one fails to initialize.</dd>
<dt><code>kernel_irqchip=on|off</code></dt>
<dd> Enables in-kernel irqchip support for the chosen accelerator when available.</dd>
<dt><code>kvm_shadow_mem=size</code></dt>
<dd> Defines the size of the KVM shadow MMU.</dd>
<dt><code>dump-guest-core=on|off</code></dt>
<dd> Include guest memory in a core dump. The default is on.</dd>
<dt><code>mem-merge=on|off</code></dt>
<dd> Enables or disables memory merge support. This feature, when supported by the host, de-duplicates identical memory pages among VMs instances (enabled by default).</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-cpu</code> <i>model</i></dt>
<dd> Select CPU model (<tt>&quot;-cpu help&quot;</tt> for list and additional feature selection)</dd>
<dt><code>-smp [cpus=]</code><i>n</i><code>[,cores=</code><i>cores</i><code>][,threads=</code><i>threads</i><code>][,sockets=</code><i>sockets</i><code>][,maxcpus=</code><i>maxcpus</i><code>]</code></dt>
<dd> Simulate an SMP system with <i>n</i> CPUs. On the PC target, up to 255 CPUs are supported. On Sparc32 target, Linux limits the number of usable CPUs to 4. For the PC target, the number of <i>cores</i> per socket, the number of <i>threads</i> per cores and the total number of <i>sockets</i> can be specified. Missing values will be computed. If any on the three values is given, the total number of CPUs <i>n</i> can be omitted. <i>maxcpus</i> specifies the maximum number of hotpluggable CPUs.</dd>
<dt><code>-numa</code> <i>opts</i></dt>
<dd> Simulate a multi node NUMA system. If mem and cpus are omitted, resources are split equally.</dd>
<dt><code>-add-fd fd=</code><i>fd</i><code>,set=</code><i>set</i><code>[,opaque=</code><i>opaque</i><code>]</code></dt>
<dd> Add a file descriptor to an fd set. Valid options are:</dd>
<dl>
<dl>
<dt><code>fd=</code><i>fd</i></dt>
<dd> This option defines the file descriptor of which a duplicate is added to fd set. The file descriptor cannot be stdin, stdout, or stderr.</dd>
<dt><code>set=</code><i>set</i></dt>
<dd> This option defines the ID of the fd set to add the file descriptor to.</dd>
<dt><code>opaque=</code><i>opaque</i></dt>
<dd> This option defines a free-form string that can be used to describe <i>fd</i>.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> You can open an image using pre-opened file descriptors from an fd set: </p>
<pre>
        qemu-system-i386
        -add-fd fd=3,set=2,opaque=&quot;rdwr:/path/to/file&quot;
        -add-fd fd=4,set=2,opaque=&quot;rdonly:/path/to/file&quot;
        -drive file=/dev/fdset/2,index=0,media=disk
</pre>
</dd></dl>
<dt><code>-set</code> <i>group</i><code>.</code><i>id</i><code>.</code><i>arg</i><code>=</code><i>value</i></dt>
<dd> Set parameter <i>arg</i> for item <i>id</i> of type <i>group</i>
&quot;</dd>
<dt><code>-global</code> <i>driver</i><code>.</code><i>prop</i><code>=</code><i>value</i></dt>
<dd> Set default value of <i>driver</i>&#8216;s property <i>prop</i> to <i>value</i>, e.g.: </dd>
<pre>
        qemu-system-i386 -global ide-drive.physical_block_size=4096 -drive file=file,if=ide,index=0,media=disk
</pre>
<p> In particular, you can use this to set driver properties for devices which are created automatically by the machine model. To create a device which is not created automatically and set properties on it, use &#8211;<code>device</code>.</p>
<dt><code>-boot [order=</code><i>drives</i><code>][,once=</code><i>drives</i><code>][,menu=on|off][,splash=</code><i>sp_name</i><code>][,splash-time=</code><i>sp_time</i><code>][,reboot-timeout=</code><i>rb_timeout</i><code>][,strict=on|off]</code></dt>
<dd> Specify boot order <i>drives</i> as a string of drive letters. Valid drive letters depend on the target achitecture. The x86 PC uses: a, b (floppy 1 and 2), c (first hard disk), d (first CD-ROM), n-p (Etherboot from network adapter 1-4), hard disk boot is the default. To apply a particular boot order only on the first startup, specify it via <code>once</code>. </dd>
<p> Interactive boot menus/prompts can be enabled via <code>menu=on</code> as far as firmware/BIOS supports them. The default is non-interactive boot. </p>
<p> A splash picture could be passed to bios, enabling user to show it as logo, when option splash=<i>sp_name</i> is given and menu=on, If firmware/BIOS supports them. Currently Seabios for X86 system support it. limitation: The splash file could be a jpeg file or a BMP file in 24 BPP format(true color). The resolution should be supported by the SVGA mode, so the recommended is 320&#215;240, 640&#215;480, 800&#215;640. </p>
<p> A timeout could be passed to bios, guest will pause for <i>rb_timeout</i> ms when boot failed, then reboot. If <i>rb_timeout</i> is &#8216;-1&#8217;, guest will not reboot, qemu passes &#8216;-1&#8217; to bios by default. Currently Seabios for X86 system support it. </p>
<p> Do strict boot via <code>strict=on</code> as far as firmware/BIOS supports it. This only effects when boot priority is changed by bootindex options. The default is non-strict boot. </p>
<pre>
        # try to boot from network first, then from hard disk
        qemu-system-i386 -boot order=nc
        # boot from CD-ROM first, switch back to default order after reboot
        qemu-system-i386 -boot once=d
        # boot with a splash picture for 5 seconds.
        qemu-system-i386 -boot menu=on,splash=/root/boot.bmp,splash-time=5000
</pre>
<p> Note: The legacy format &#8216;-boot <i>drives</i>&#8216; is still supported but its use is discouraged as it may be removed from future versions.</p>
<dt><code>-m</code> <i>megs</i></dt>
<dd> Set virtual RAM size to <i>megs</i> megabytes. Default is 128 MiB. Optionally, a suffix of &#8220;M&#8221; or &#8220;G&#8221; can be used to signify a value in megabytes or gigabytes respectively.</dd>
<dt><code>-mem-path</code> <i>path</i></dt>
<dd> Allocate guest RAM from a temporarily created file in <i>path</i>.</dd>
<dt><code>-mem-prealloc</code></dt>
<dd> Preallocate memory when using -mem-path.</dd>
<dt><code>-k</code> <i>language</i></dt>
<dd> Use keyboard layout <i>language</i> (for example <tt>&quot;fr&quot;</tt> for French). This option is only needed where it is not easy to get raw PC keycodes (e.g. on Macs, with some X11 servers or with a VNC display). You don&#8217;t normally need to use it on PC/Linux or PC/Windows hosts. </dd>
<p> The available layouts are: </p>
<pre>
        ar  de-ch  es  fo     fr-ca  hu  ja  mk     no  pt-br  sv
        da  en-gb  et  fr     fr-ch  is  lt  nl     pl  ru     th
        de  en-us  fi  fr-be  hr     it  lv  nl-be  pt  sl     tr
</pre>
<p> The default is <tt>&quot;en-us&quot;</tt>.</p>
<dt><code>-audio-help</code></dt>
<dd> Will show the audio subsystem help: list of drivers, tunable parameters.</dd>
<dt><code>-soundhw</code> <i>card1</i><code>[,</code><i>card2</i><code>,&#8230;] or -soundhw all</code></dt>
<dd> Enable audio and selected sound hardware. Use &#8216;help&#8217; to print all available sound hardware. </dd>
<pre>
        qemu-system-i386 -soundhw sb16,adlib disk.img
        qemu-system-i386 -soundhw es1370 disk.img
        qemu-system-i386 -soundhw ac97 disk.img
        qemu-system-i386 -soundhw hda disk.img
        qemu-system-i386 -soundhw all disk.img
        qemu-system-i386 -soundhw help
</pre>
<p> Note that Linux&#8217;s i810_audio OSS kernel (for AC97) module might require manually specifying clocking. </p>
<pre>
        modprobe i810_audio clocking=48000
</pre>
<dt><code>-balloon none</code></dt>
<dd> Disable balloon device.</dd>
<dt><code>-balloon virtio[,addr=</code><i>addr</i><code>]</code></dt>
<dd> Enable virtio balloon device (default), optionally with PCI address <i>addr</i>.</dd>
<dt><code>-device</code> <i>driver</i><code>[,</code><i>prop</i><code>[=</code><i>value</i><code>][,&#8230;]]</code></dt>
<dd> Add device <i>driver</i>. <i>prop</i>=<i>value</i> sets driver properties. Valid properties depend on the driver. To get help on possible drivers and properties, use <tt>&quot;-device help&quot;</tt> and <tt>&quot;-device </tt>driver<tt>,help&quot;</tt>.</dd>
<dt><code>-name</code> <i>name</i></dt>
<dd> Sets the <i>name</i> of the guest. This name will be displayed in the SDL window caption. The <i>name</i> will also be used for the VNC server. Also optionally set the top visible process name in Linux. Naming of individual threads can also be enabled on Linux to aid debugging.</dd>
<dt><code>-uuid</code> <i>uuid</i></dt>
<dd> Set system UUID.</dd></dl>
<p> Block device options:</p>
<dl>
<dt><code>-fda</code> <i>file</i></dt>
<dd>
</dd><dt><code>-fdb</code> <i>file</i></dt>
<dd> Use <i>file</i> as floppy disk 0/1 image. You can use the host floppy by using <i>/dev/fd0</i> as filename.</dd>
<dt><code>-hda</code> <i>file</i></dt>
<dd>
</dd><dt><code>-hdb</code> <i>file</i></dt>
<dd>
</dd><dt><code>-hdc</code> <i>file</i></dt>
<dd>
</dd><dt><code>-hdd</code> <i>file</i></dt>
<dd> Use <i>file</i> as hard disk 0, 1, 2 or 3 image.</dd>
<dt><code>-cdrom</code> <i>file</i></dt>
<dd> Use <i>file</i> as CD-ROM image (you cannot use <code>-hdc</code> and <code>-cdrom</code> at the same time). You can use the host CD-ROM by using <i>/dev/cdrom</i> as filename.</dd>
<dt><code>-drive</code> <i>option</i><code>[,</code><i>option</i><code>[,</code><i>option</i><code>[,&#8230;]]]</code></dt>
<dd> Define a new drive. Valid options are:</dd>
<dl>
<dl>
<dt><code>file=</code><i>file</i></dt>
<dd> This option defines which disk image to use with this drive. If the filename contains comma, you must double it (for instance, &#8220;file=my,,file&#8221; to use file &#8220;my,file&#8221;). </dd>
<p> Special files such as iSCSI devices can be specified using protocol specific URLs. See the section for &#8220;Device URL Syntax&#8221; for more information.</p>
<dt><code>if=</code><i>interface</i></dt>
<dd> This option defines on which type on interface the drive is connected. Available types are: ide, scsi, sd, mtd, floppy, pflash, virtio.</dd>
<dt><code>bus=</code><i>bus</i><code>,unit=</code><i>unit</i></dt>
<dd> These options define where is connected the drive by defining the bus number and the unit id.</dd>
<dt><code>index=</code><i>index</i></dt>
<dd> This option defines where is connected the drive by using an index in the list of available connectors of a given interface type.</dd>
<dt><code>media=</code><i>media</i></dt>
<dd> This option defines the type of the media: disk or cdrom.</dd>
<dt><code>cyls=</code><i>c</i><code>,heads=</code><i>h</i><code>,secs=</code><i>s</i><code>[,trans=</code><i>t</i><code>]</code></dt>
<dd> These options have the same definition as they have in <code>-hdachs</code>.</dd>
<dt><code>snapshot=</code><i>snapshot</i></dt>
<dd> <i>snapshot</i> is &#8220;on&#8221; or &#8220;off&#8221; and allows to enable snapshot for given drive (see <code>-snapshot</code>).</dd>
<dt><code>cache=</code><i>cache</i></dt>
<dd> <i>cache</i> is &#8220;none&#8221;, &#8220;writeback&#8221;, &#8220;unsafe&#8221;, &#8220;directsync&#8221; or &#8220;writethrough&#8221; and controls how the host cache is used to access block data.</dd>
<dt><code>aio=</code><i>aio</i></dt>
<dd> <i>aio</i> is &#8220;threads&#8221;, or &#8220;native&#8221; and selects between pthread based disk I/O and native Linux AIO.</dd>
<dt><code>discard=</code><i>discard</i></dt>
<dd> <i>discard</i> is one of &#8220;ignore&#8221; (or &#8220;off&#8221;) or &#8220;unmap&#8221; (or &#8220;on&#8221;) and controls whether <i>discard</i> (also known as <i>trim</i> or <i>unmap</i>) requests are ignored or passed to the filesystem. Some machine types may not support discard requests.</dd>
<dt><code>format=</code><i>format</i></dt>
<dd> Specify which disk <i>format</i> will be used rather than detecting the format. Can be used to specifiy format=raw to avoid interpreting an untrusted format header.</dd>
<dt><code>serial=</code><i>serial</i></dt>
<dd> This option specifies the serial number to assign to the device.</dd>
<dt><code>addr=</code><i>addr</i></dt>
<dd> Specify the controller&#8217;s PCI address (if=virtio only).</dd>
<dt><code>werror=</code><i>action</i><code>,rerror=</code><i>action</i></dt>
<dd> Specify which <i>action</i> to take on write and read errors. Valid actions are: &#8220;ignore&#8221; (ignore the error and try to continue), &#8220;stop&#8221; (pause QEMU), &#8220;report&#8221; (report the error to the guest), &#8220;enospc&#8221; (pause QEMU only if the host disk is full; report the error to the guest otherwise). The default setting is <code>werror=enospc</code> and <code>rerror=report</code>.</dd>
<dt><code>readonly</code></dt>
<dd> Open drive <code>file</code> as read-only. Guest write attempts will fail.</dd>
<dt><code>copy-on-read=</code><i>copy-on-read</i></dt>
<dd> <i>copy-on-read</i> is &#8220;on&#8221; or &#8220;off&#8221; and enables whether to copy read backing file sectors into the image file.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> By default, the <code>cache=writeback</code> mode is used. It will report data writes as completed as soon as the data is present in the host page cache. This is safe as long as your guest OS makes sure to correctly flush disk caches where needed. If your guest OS does not handle volatile disk write caches correctly and your host crashes or loses power, then the guest may experience data corruption. </p>
<p> For such guests, you should consider using <code>cache=writethrough</code>. This means that the host page cache will be used to read and write data, but write notification will be sent to the guest only after QEMU has made sure to flush each write to the disk. Be aware that this has a major impact on performance. </p>
<p> The host page cache can be avoided entirely with <code>cache=none</code>. This will attempt to do disk IO directly to the guest&#8217;s memory. QEMU may still perform an internal copy of the data. Note that this is considered a writeback mode and the guest OS must handle the disk write cache correctly in order to avoid data corruption on host crashes. </p>
<p> The host page cache can be avoided while only sending write notifications to the guest when the data has been flushed to the disk using <code>cache=directsync</code>. </p>
<p> In case you don&#8217;t care about data integrity over host failures, use <code>cache=unsafe</code>. This option tells QEMU that it never needs to write any data to the disk but can instead keep things in cache. If anything goes wrong, like your host losing power, the disk storage getting disconnected accidentally, etc. your image will most probably be rendered unusable. When using the <code>-snapshot</code> option, unsafe caching is always used. </p>
<p> Copy-on-read avoids accessing the same backing file sectors repeatedly and is useful when the backing file is over a slow network. By default copy-on-read is off. </p>
<p> Instead of <code>-cdrom</code> you can use: </p>
<pre>
        qemu-system-i386 -drive file=file,index=2,media=cdrom
</pre>
<p> Instead of <code>-hda</code>, <code>-hdb</code>, <code>-hdc</code>, <code>-hdd</code>, you can use: </p>
<pre>
        qemu-system-i386 -drive file=file,index=0,media=disk
        qemu-system-i386 -drive file=file,index=1,media=disk
        qemu-system-i386 -drive file=file,index=2,media=disk
        qemu-system-i386 -drive file=file,index=3,media=disk
</pre>
<p> You can open an image using pre-opened file descriptors from an fd set: </p>
<pre>
        qemu-system-i386
        -add-fd fd=3,set=2,opaque=&quot;rdwr:/path/to/file&quot;
        -add-fd fd=4,set=2,opaque=&quot;rdonly:/path/to/file&quot;
        -drive file=/dev/fdset/2,index=0,media=disk
</pre>
<p> You can connect a CDROM to the slave of ide0: </p>
<pre>
        qemu-system-i386 -drive file=file,if=ide,index=1,media=cdrom
</pre>
<p> If you don&#8217;t specify the &#8220;file=&#8221; argument, you define an empty drive: </p>
<pre>
        qemu-system-i386 -drive if=ide,index=1,media=cdrom
</pre>
<p> You can connect a SCSI disk with unit ID 6 on the bus #0: </p>
<pre>
        qemu-system-i386 -drive file=file,if=scsi,bus=0,unit=6
</pre>
<p> Instead of <code>-fda</code>, <code>-fdb</code>, you can use: </p>
<pre>
        qemu-system-i386 -drive file=file,index=0,if=floppy
        qemu-system-i386 -drive file=file,index=1,if=floppy
</pre>
<p> By default, <i>interface</i> is &#8220;ide&#8221; and <i>index</i> is automatically incremented: </p>
<pre>
        qemu-system-i386 -drive file=a -drive file=b&quot;
</pre>
<p> is interpreted like: </p>
<pre>
        qemu-system-i386 -hda a -hdb b
</pre>
</dd></dl>
<dt><code>-mtdblock</code> <i>file</i></dt>
<dd> Use <i>file</i> as on-board Flash memory image.</dd>
<dt><code>-sd</code> <i>file</i></dt>
<dd> Use <i>file</i> as SecureDigital card image.</dd>
<dt><code>-pflash</code> <i>file</i></dt>
<dd> Use <i>file</i> as a parallel flash image.</dd>
<dt><code>-snapshot</code></dt>
<dd> Write to temporary files instead of disk image files. In this case, the raw disk image you use is not written back. You can however force the write back by pressing <code>C-a s</code>.</dd>
<dt><code>-hdachs</code> <i>c</i><code>,</code><i>h</i><code>,</code><i>s</i><code>,[,</code><i>t</i><code>]</code></dt>
<dd> Force hard disk 0 physical geometry (1 &lt;= <i>c</i> &lt;= 16383, 1 &lt;= <i>h</i> &lt;= 16, 1 &lt;= <i>s</i> &lt;= 63) and optionally force the BIOS translation mode (<i>t</i>=none, lba or auto). Usually QEMU can guess all those parameters. This option is useful for old MS-DOS disk images.</dd>
<dt><code>-fsdev</code> <i>fsdriver</i><code>,id=</code><i>id</i><code>,path=</code><i>path</i><code>,[security_model=</code><i>security_model</i><code>][,writeout=</code><i>writeout</i><code>][,readonly][,socket=</code><i>socket</i><code>|sock_fd=</code><i>sock_fd</i><code>]</code></dt>
<dd> Define a new file system device. Valid options are:</dd>
<dl>
<dl>
<dt><i>fsdriver</i></dt>
<dd> This option specifies the fs driver backend to use. Currently &#8220;local&#8221;, &#8220;handle&#8221; and &#8220;proxy&#8221; file system drivers are supported.</dd>
<dt><code>id=</code><i>id</i></dt>
<dd> Specifies identifier for this device</dd>
<dt><code>path=</code><i>path</i></dt>
<dd> Specifies the export path for the file system device. Files under this path will be available to the 9p client on the guest.</dd>
<dt><code>security_model=</code><i>security_model</i></dt>
<dd> Specifies the security model to be used for this export path. Supported security models are &#8220;passthrough&#8221;, &#8220;mapped-xattr&#8221;, &#8220;mapped-file&#8221; and &#8220;none&#8221;. In &#8220;passthrough&#8221; security model, files are stored using the same credentials as they are created on the guest. This requires QEMU to run as root. In &#8220;mapped-xattr&#8221; security model, some of the file attributes like uid, gid, mode bits and link target are stored as file attributes. For &#8220;mapped-file&#8221; these attributes are stored in the hidden .virtfs_metadata directory. Directories exported by this security model cannot interact with other unix tools. &#8220;none&#8221; security model is same as passthrough except the sever won&#8217;t report failures if it fails to set file attributes like ownership. Security model is mandatory only for local fsdriver. Other fsdrivers (like handle, proxy) don&#8217;t take security model as a parameter.</dd>
<dt><code>writeout=</code><i>writeout</i></dt>
<dd> This is an optional argument. The only supported value is &#8220;immediate&#8221;. This means that host page cache will be used to read and write data but write notification will be sent to the guest only when the data has been reported as written by the storage subsystem.</dd>
<dt><code>readonly</code></dt>
<dd> Enables exporting 9p share as a readonly mount for guests. By default read-write access is given.</dd>
<dt><code>socket=</code><i>socket</i></dt>
<dd> Enables proxy filesystem driver to use passed socket file for communicating with virtfs-proxy-helper</dd>
<dt><code>sock_fd=</code><i>sock_fd</i></dt>
<dd> Enables proxy filesystem driver to use passed socket descriptor for communicating with virtfs-proxy-helper. Usually a helper like libvirt will create socketpair and pass one of the fds as sock_fd</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> -fsdev option is used along with -device driver &#8220;virtio-9p-pci&#8221;.</dd></dl>
<dt><code>-device virtio-9p-pci,fsdev=</code><i>id</i><code>,mount_tag=</code><i>mount_tag</i></dt>
<dd> Options for virtio-9p-pci driver are:</dd>
<dl>
<dl>
<dt><code>fsdev=</code><i>id</i></dt>
<dd> Specifies the id value specified along with -fsdev option</dd>
<dt><code>mount_tag=</code><i>mount_tag</i></dt>
<dd> Specifies the tag name to be used by the guest to mount this export point</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-virtfs</code> <i>fsdriver</i><code>[,path=</code><i>path</i><code>],mount_tag=</code><i>mount_tag</i><code>[,security_model=</code><i>security_model</i><code>][,writeout=</code><i>writeout</i><code>][,readonly][,socket=</code><i>socket</i><code>|sock_fd=</code><i>sock_fd</i><code>]</code></dt>
<dd> The general form of a Virtual File system pass-through options are:</dd>
<dl>
<dl>
<dt><i>fsdriver</i></dt>
<dd> This option specifies the fs driver backend to use. Currently &#8220;local&#8221;, &#8220;handle&#8221; and &#8220;proxy&#8221; file system drivers are supported.</dd>
<dt><code>id=</code><i>id</i></dt>
<dd> Specifies identifier for this device</dd>
<dt><code>path=</code><i>path</i></dt>
<dd> Specifies the export path for the file system device. Files under this path will be available to the 9p client on the guest.</dd>
<dt><code>security_model=</code><i>security_model</i></dt>
<dd> Specifies the security model to be used for this export path. Supported security models are &#8220;passthrough&#8221;, &#8220;mapped-xattr&#8221;, &#8220;mapped-file&#8221; and &#8220;none&#8221;. In &#8220;passthrough&#8221; security model, files are stored using the same credentials as they are created on the guest. This requires QEMU to run as root. In &#8220;mapped-xattr&#8221; security model, some of the file attributes like uid, gid, mode bits and link target are stored as file attributes. For &#8220;mapped-file&#8221; these attributes are stored in the hidden .virtfs_metadata directory. Directories exported by this security model cannot interact with other unix tools. &#8220;none&#8221; security model is same as passthrough except the sever won&#8217;t report failures if it fails to set file attributes like ownership. Security model is mandatory only for local fsdriver. Other fsdrivers (like handle, proxy) don&#8217;t take security model as a parameter.</dd>
<dt><code>writeout=</code><i>writeout</i></dt>
<dd> This is an optional argument. The only supported value is &#8220;immediate&#8221;. This means that host page cache will be used to read and write data but write notification will be sent to the guest only when the data has been reported as written by the storage subsystem.</dd>
<dt><code>readonly</code></dt>
<dd> Enables exporting 9p share as a readonly mount for guests. By default read-write access is given.</dd>
<dt><code>socket=</code><i>socket</i></dt>
<dd> Enables proxy filesystem driver to use passed socket file for communicating with virtfs-proxy-helper. Usually a helper like libvirt will create socketpair and pass one of the fds as sock_fd</dd>
<dt><code>sock_fd</code></dt>
<dd> Enables proxy filesystem driver to use passed &#8216;sock_fd&#8217; as the socket descriptor for interfacing with virtfs-proxy-helper</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-virtfs_synth</code></dt>
<dd> Create synthetic file system image</dd></dl>
<p> USB options:</p>
<dl>
<dt><code>-usb</code></dt>
<dd> Enable the USB driver (will be the default soon)</dd>
<dt><code>-usbdevice</code> <i>devname</i></dt>
<dd> Add the USB device <i>devname</i>.</dd>
<dl>
<dl>
<dt><code>mouse</code></dt>
<dd> Virtual Mouse. This will override the PS/2 mouse emulation when activated.</dd>
<dt><code>tablet</code></dt>
<dd> Pointer device that uses absolute coordinates (like a touchscreen). This means QEMU is able to report the mouse position without having to grab the mouse. Also overrides the PS/2 mouse emulation when activated.</dd>
<dt><code>disk:[format=</code><i>format</i><code>]:</code><i>file</i></dt>
<dd> Mass storage device based on file. The optional <i>format</i> argument will be used rather than detecting the format. Can be used to specifiy <tt>&quot;format=raw&quot;</tt> to avoid interpreting an untrusted format header.</dd>
<dt><code>host:</code><i>bus</i><code>.</code><i>addr</i></dt>
<dd> Pass through the host device identified by <i>bus</i>.<i>addr</i> (Linux only).</dd>
<dt><code>host:</code><i>vendor_id</i><code>:</code><i>product_id</i></dt>
<dd> Pass through the host device identified by <i>vendor_id</i>:<i>product_id</i> (Linux only).</dd>
<dt><code>serial:[vendorid=</code><i>vendor_id</i><code>][,productid=</code><i>product_id</i><code>]:</code><i>dev</i></dt>
<dd> Serial converter to host character device <i>dev</i>, see <tt>&quot;-serial&quot;</tt> for the available devices.</dd>
<dt><code>braille</code></dt>
<dd> Braille device. This will use BrlAPI to display the braille output on a real or fake device.</dd>
<dt><code>net:</code><i>options</i></dt>
<dd> Network adapter that supports CDC ethernet and RNDIS protocols.</dd></dl>
</dl>
<dl>
</dl>
</dl>
<p> Display options:</p>
<dl>
<dt><code>-display</code> <i>type</i></dt>
<dd> Select type of display to use. This option is a replacement for the old style -sdl/-curses/&#8230; options. Valid values for <i>type</i> are</dd>
<dl>
<dl>
<dt><code>sdl</code></dt>
<dd> Display video output via SDL (usually in a separate graphics window; see the SDL documentation for other possibilities).</dd>
<dt><code>curses</code></dt>
<dd> Display video output via curses. For graphics device models which support a text mode, QEMU can display this output using a curses/ncurses interface. Nothing is displayed when the graphics device is in graphical mode or if the graphics device does not support a text mode. Generally only the VGA device models support text mode.</dd>
<dt><code>none</code></dt>
<dd> Do not display video output. The guest will still see an emulated graphics card, but its output will not be displayed to the QEMU user. This option differs from the -nographic option in that it only affects what is done with video output; -nographic also changes the destination of the serial and parallel port data.</dd>
<dt><code>gtk</code></dt>
<dd> Display video output in a GTK window. This interface provides drop-down menus and other UI elements to configure and control the VM during runtime.</dd>
<dt><code>vnc</code></dt>
<dd> Start a VNC server on display &lt;arg&gt;</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-nographic</code></dt>
<dd> Normally, QEMU uses SDL to display the VGA output. With this option, you can totally disable graphical output so that QEMU is a simple command line application. The emulated serial port is redirected on the console and muxed with the monitor (unless redirected elsewhere explicitly). Therefore, you can still use QEMU to debug a Linux kernel with a serial console. Use <code>C-a h</code> for help on switching between the console and monitor.</dd>
<dt><code>-curses</code></dt>
<dd> Normally, QEMU uses SDL to display the VGA output. With this option, QEMU can display the VGA output when in text mode using a curses/ncurses interface. Nothing is displayed in graphical mode.</dd>
<dt><code>-no-frame</code></dt>
<dd> Do not use decorations for SDL windows and start them using the whole available screen space. This makes the using QEMU in a dedicated desktop workspace more convenient.</dd>
<dt><code>-alt-grab</code></dt>
<dd> Use Ctrl-Alt-Shift to grab mouse (instead of Ctrl-Alt). Note that this also affects the special keys (for fullscreen, monitor-mode switching, etc).</dd>
<dt><code>-ctrl-grab</code></dt>
<dd> Use Right-Ctrl to grab mouse (instead of Ctrl-Alt). Note that this also affects the special keys (for fullscreen, monitor-mode switching, etc).</dd>
<dt><code>-no-quit</code></dt>
<dd> Disable SDL window close capability.</dd>
<dt><code>-sdl</code></dt>
<dd> Enable SDL.</dd>
<dt><code>-spice</code> <i>option</i><code>[,</code><i>option</i><code>[,&#8230;]]</code></dt>
<dd> Enable the spice remote desktop protocol. Valid options are</dd>
<dl>
<dl>
<dt><code>port=&lt;nr&gt;</code></dt>
<dd> Set the TCP port spice is listening on for plaintext channels.</dd>
<dt><code>addr=&lt;addr&gt;</code></dt>
<dd> Set the IP address spice is listening on. Default is any address.</dd>
<dt><code>ipv4</code></dt>
<dd>
</dd><dt><code>ipv6</code></dt>
<dd> Force using the specified IP version.</dd>
<dt><code>password=&lt;secret&gt;</code></dt>
<dd> Set the password you need to authenticate.</dd>
<dt><code>sasl</code></dt>
<dd> Require that the client use SASL to authenticate with the spice. The exact choice of authentication method used is controlled from the system / user&#8217;s SASL configuration file for the &#8216;qemu&#8217; service. This is typically found in /etc/sasl2/qemu.conf. If running QEMU as an unprivileged user, an environment variable SASL_CONF_PATH can be used to make it search alternate locations for the service config. While some SASL auth methods can also provide data encryption (eg GSSAPI), it is recommended that SASL always be combined with the &#8216;tls&#8217; and &#8216;x509&#8217; settings to enable use of SSL and server certificates. This ensures a data encryption preventing compromise of authentication credentials.</dd>
<dt><code>disable-ticketing</code></dt>
<dd> Allow client connects without authentication.</dd>
<dt><code>disable-copy-paste</code></dt>
<dd> Disable copy paste between the client and the guest.</dd>
<dt><code>disable-agent-file-xfer</code></dt>
<dd> Disable spice-vdagent based file-xfer between the client and the guest.</dd>
<dt><code>tls-port=&lt;nr&gt;</code></dt>
<dd> Set the TCP port spice is listening on for encrypted channels.</dd>
<dt><code>x509-dir=&lt;dir&gt;</code></dt>
<dd> Set the x509 file directory. Expects same filenames as -vnc <tt>$display</tt>,x509=$dir</dd>
<dt><code>x509-key-file=&lt;file&gt;</code></dt>
<dd>
</dd><dt><code>x509-key-password=&lt;file&gt;</code></dt>
<dd>
</dd><dt><code>x509-cert-file=&lt;file&gt;</code></dt>
<dd>
</dd><dt><code>x509-cacert-file=&lt;file&gt;</code></dt>
<dd>
</dd><dt><code>x509-dh-key-file=&lt;file&gt;</code></dt>
<dd> The x509 file names can also be configured individually.</dd>
<dt><code>tls-ciphers=&lt;list&gt;</code></dt>
<dd> Specify which ciphers to use.</dd>
<dt><code>tls-channel=[main|display|cursor|inputs|record|playback]</code></dt>
<dd>
</dd><dt><code>plaintext-channel=[main|display|cursor|inputs|record|playback]</code></dt>
<dd> Force specific channel to be used with or without TLS encryption. The options can be specified multiple times to configure multiple channels. The special name &#8220;default&#8221; can be used to set the default mode. For channels which are not explicitly forced into one mode the spice client is allowed to pick tls/plaintext as he pleases.</dd>
<dt><code>image-compression=[auto_glz|auto_lz|quic|glz|lz|off]</code></dt>
<dd> Configure image compression (lossless). Default is auto_glz.</dd>
<dt><code>jpeg-wan-compression=[auto|never|always]</code></dt>
<dd>
</dd><dt><code>zlib-glz-wan-compression=[auto|never|always]</code></dt>
<dd> Configure wan image compression (lossy for slow links). Default is auto.</dd>
<dt><code>streaming-video=[off|all|filter]</code></dt>
<dd> Configure video stream detection. Default is filter.</dd>
<dt><code>agent-mouse=[on|off]</code></dt>
<dd> Enable/disable passing mouse events via vdagent. Default is on.</dd>
<dt><code>playback-compression=[on|off]</code></dt>
<dd> Enable/disable audio stream compression (using celt 0.5.1). Default is on.</dd>
<dt><code>seamless-migration=[on|off]</code></dt>
<dd> Enable/disable spice seamless migration. Default is off.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-portrait</code></dt>
<dd> Rotate graphical output 90 deg left (only PXA LCD).</dd>
<dt><code>-rotate</code> <i>deg</i></dt>
<dd> Rotate graphical output some deg left (only PXA LCD).</dd>
<dt><code>-vga</code> <i>type</i></dt>
<dd> Select type of VGA card to emulate. Valid values for <i>type</i> are</dd>
<dl>
<dl>
<dt><code>cirrus</code></dt>
<dd> Cirrus Logic GD5446 Video card. All Windows versions starting from Windows 95 should recognize and use this graphic card. For optimal performances, use 16 bit color depth in the guest and the host OS. (This one is the default)</dd>
<dt><code>std</code></dt>
<dd> Standard VGA card with Bochs VBE extensions. If your guest OS supports the VESA 2.0 VBE extensions (e.g. Windows XP) and if you want to use high resolution modes (&gt;= 1280x1024x16) then you should use this option.</dd>
<dt><code>vmware</code></dt>
<dd> VMWare SVGA-II compatible adapter. Use it if you have sufficiently recent XFree86/XOrg server or Windows guest with a driver for this card.</dd>
<dt><code>qxl</code></dt>
<dd> QXL paravirtual graphic card. It is VGA compatible (including VESA 2.0 VBE support). Works best with qxl guest drivers installed though. Recommended choice when using the spice protocol.</dd>
<dt><code>tcx</code></dt>
<dd> (sun4m only) Sun TCX framebuffer. This is the default framebuffer for sun4m machines and offers both 8-bit and 24-bit colour depths at a fixed resolution of 1024&#215;768.</dd>
<dt><code>cg3</code></dt>
<dd> (sun4m only) Sun cgthree framebuffer. This is a simple 8-bit framebuffer for sun4m machines available in both 1024&#215;768 (OpenBIOS) and 1152&#215;900 (OBP) resolutions aimed at people wishing to run older Solaris versions.</dd>
<dt><code>none</code></dt>
<dd> Disable VGA card.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-full-screen</code></dt>
<dd> Start in full screen.</dd>
<dt><code>-g</code> <i>width</i><code>x</code><i>height</i><code>[x</code><i>depth</i><code>]</code></dt>
<dd> Set the initial graphical resolution and depth (PPC, SPARC only).</dd>
<dt><code>-vnc</code> <i>display</i><code>[,</code><i>option</i><code>[,</code><i>option</i><code>[,&#8230;]]]</code></dt>
<dd> Normally, QEMU uses SDL to display the VGA output. With this option, you can have QEMU listen on VNC display <i>display</i> and redirect the VGA display over the VNC session. It is very useful to enable the usb tablet device when using this option (option <code>-usbdevice tablet</code>). When using the VNC display, you must use the <code>-k</code> parameter to set the keyboard layout if you are not using en-us. Valid syntax for the <i>display</i> is</dd>
<dl>
<dl>
<dt><i>host</i><code>:</code><i>d</i></dt>
<dd> TCP connections will only be allowed from <i>host</i> on display <i>d</i>. By convention the TCP port is 5900+<i>d</i>. Optionally, <i>host</i> can be omitted in which case the server will accept connections from any host.</dd>
<dt><code>unix:</code><i>path</i></dt>
<dd> Connections will be allowed over UNIX domain sockets where <i>path</i> is the location of a unix socket to listen for connections on.</dd>
<dt><code>none</code></dt>
<dd> VNC is initialized but not started. The monitor <tt>&quot;change&quot;</tt> command can be used to later start the VNC server.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> Following the <i>display</i> value there may be one or more <i>option</i> flags separated by commas. Valid options are</p>
</dd><dl>
<dt><code>reverse</code></dt>
<dd> Connect to a listening VNC client via a &#8220;reverse&#8221; connection. The client is specified by the <i>display</i>. For reverse network connections (<i>host</i>:<i>d</i>,<tt>&quot;reverse&quot;</tt>), the <i>d</i> argument is a TCP port number, not a display number.</dd>
<dt><code>websocket</code></dt>
<dd> Opens an additional TCP listening port dedicated to VNC Websocket connections. By definition the Websocket port is 5700+<i>display</i>. If <i>host</i> is specified connections will only be allowed from this host. As an alternative the Websocket port could be specified by using <tt>&quot;websocket&quot;</tt>=<i>port</i>. TLS encryption for the Websocket connection is supported if the required certificates are specified with the VNC option <code>x509</code>.</dd>
<dt><code>password</code></dt>
<dd> Require that password based authentication is used for client connections. </dd>
<p> The password must be set separately using the <tt>&quot;set_password&quot;</tt> command in the <code>pcsys_monitor</code>. The syntax to change your password is: <tt>&quot;set_password &lt;protocol&gt; &lt;password&gt;&quot;</tt> where &lt;protocol&gt; could be either &#8220;vnc&#8221; or &#8220;spice&#8221;. </p>
<p> If you would like to change &lt;protocol&gt; password expiration, you should use <tt>&quot;expire_password &lt;protocol&gt; &lt;expiration-time&gt;&quot;</tt> where expiration time could be one of the following options: now, never, +seconds or UNIX time of expiration, e.g. +60 to make password expire in 60 seconds, or 1335196800 to make password expire on &#8220;Mon Apr 23 12:00:00 EDT 2012&#8221; (UNIX time for this date and time). </p>
<p> You can also use keywords &#8220;now&#8221; or &#8220;never&#8221; for the expiration time to allow &lt;protocol&gt; password to expire immediately or never expire.</p>
<dt><code>tls</code></dt>
<dd> Require that client use TLS when communicating with the VNC server. This uses anonymous TLS credentials so is susceptible to a man-in-the-middle attack. It is recommended that this option be combined with either the <code>x509</code> or <code>x509verify</code> options.</dd>
<dt><code>x509=</code><i>/path/to/certificate/dir</i></dt>
<dd> Valid if <code>tls</code> is specified. Require that x509 credentials are used for negotiating the TLS session. The server will send its x509 certificate to the client. It is recommended that a password be set on the VNC server to provide authentication of the client when this is used. The path following this option specifies where the x509 certificates are to be loaded from. See the <code>vnc_security</code> section for details on generating certificates.</dd>
<dt><code>x509verify=</code><i>/path/to/certificate/dir</i></dt>
<dd> Valid if <code>tls</code> is specified. Require that x509 credentials are used for negotiating the TLS session. The server will send its x509 certificate to the client, and request that the client send its own x509 certificate. The server will validate the client&#8217;s certificate against the CA certificate, and reject clients when validation fails. If the certificate authority is trusted, this is a sufficient authentication mechanism. You may still wish to set a password on the VNC server as a second authentication layer. The path following this option specifies where the x509 certificates are to be loaded from. See the <code>vnc_security</code> section for details on generating certificates.</dd>
<dt><code>sasl</code></dt>
<dd> Require that the client use SASL to authenticate with the VNC server. The exact choice of authentication method used is controlled from the system / user&#8217;s SASL configuration file for the &#8216;qemu&#8217; service. This is typically found in /etc/sasl2/qemu.conf. If running QEMU as an unprivileged user, an environment variable SASL_CONF_PATH can be used to make it search alternate locations for the service config. While some SASL auth methods can also provide data encryption (eg GSSAPI), it is recommended that SASL always be combined with the &#8216;tls&#8217; and &#8216;x509&#8217; settings to enable use of SSL and server certificates. This ensures a data encryption preventing compromise of authentication credentials. See the <code>vnc_security</code> section for details on using SASL authentication.</dd>
<dt><code>acl</code></dt>
<dd> Turn on access control lists for checking of the x509 client certificate and SASL party. For x509 certs, the ACL check is made against the certificate&#8217;s distinguished name. This is something that looks like <tt>&quot;C=GB,O=ACME,L=Boston,CN=bob&quot;</tt>. For SASL party, the ACL check is made against the username, which depending on the SASL plugin, may include a realm component, eg <tt>&quot;bob&quot;</tt> or <tt>&quot;bob [at] EXAMPLE.COM&quot;</tt>. When the <code>acl</code> flag is set, the initial access list will be empty, with a <tt>&quot;deny&quot;</tt> policy. Thus no one will be allowed to use the VNC server until the ACLs have been loaded. This can be achieved using the <tt>&quot;acl&quot;</tt> monitor command.</dd>
<dt><code>lossy</code></dt>
<dd> Enable lossy compression methods (gradient, JPEG, &#8230;). If this option is set, VNC client may receive lossy framebuffer updates depending on its encoding settings. Enabling this option can save a lot of bandwidth at the expense of quality.</dd>
<dt><code>non-adaptive</code></dt>
<dd> Disable adaptive encodings. Adaptive encodings are enabled by default. An adaptive encoding will try to detect frequently updated screen regions, and send updates in these regions using a lossy encoding (like JPEG). This can be really helpful to save bandwidth when playing videos. Disabling adaptive encodings allows to restore the original static behavior of encodings like Tight.</dd>
<dt><code>share=[allow-exclusive|force-shared|ignore]</code></dt>
<dd> Set display sharing policy. &#8216;allow-exclusive&#8217; allows clients to ask for exclusive access. As suggested by the rfb spec this is implemented by dropping other connections. Connecting multiple clients in parallel requires all clients asking for a shared session (vncviewer: -shared switch). This is the default. &#8216;force-shared&#8217; disables exclusive client access. Useful for shared desktop sessions, where you don&#8217;t want someone forgetting specify -shared disconnect everybody else. &#8216;ignore&#8217; completely ignores the shared flag and allows everybody connect unconditionally. Doesn&#8217;t conform to the rfb spec but is traditional QEMU behavior.</dd></dl>
</dl>
<dl>
</dl>
</dl>
<p> i386 target only:</p>
<dl>
<dt><code>-win2k-hack</code></dt>
<dd> Use it when installing Windows 2000 to avoid a disk full bug. After Windows 2000 is installed, you no longer need this option (this option slows down the IDE transfers).</dd>
<dt><code>-no-fd-bootchk</code></dt>
<dd> Disable boot signature checking for floppy disks in BIOS. May be needed to boot from old floppy disks.</dd>
<dt><code>-no-acpi</code></dt>
<dd> Disable ACPI (Advanced Configuration and Power Interface) support. Use it if your guest OS complains about ACPI problems (PC target machine only).</dd>
<dt><code>-no-hpet</code></dt>
<dd> Disable HPET support.</dd>
<dt><code>-acpitable [sig=</code><i>str</i><code>][,rev=</code><i>n</i><code>][,oem_id=</code><i>str</i><code>][,oem_table_id=</code><i>str</i><code>][,oem_rev=</code><i>n</i><code>] [,asl_compiler_id=</code><i>str</i><code>][,asl_compiler_rev=</code><i>n</i><code>][,data=</code><i>file1</i><code>[:</code><i>file2</i><code>]&#8230;]</code></dt>
<dd> Add ACPI table with specified header fields and context from specified files. For file=, take whole ACPI table from the specified files, including all ACPI headers (possible overridden by other options). For data=, only data portion of the table is used, all header information is specified in the command line.</dd>
<dt><code>-smbios file=</code><i>binary</i></dt>
<dd> Load SMBIOS entry from binary file.</dd>
<dt><code>-smbios type=0[,vendor=</code><i>str</i><code>][,version=</code><i>str</i><code>][,date=</code><i>str</i><code>][,release=</code><i>%d.%d</i><code>]</code></dt>
<dd> Specify SMBIOS type 0 fields</dd>
<dt><code>-smbios type=1[,manufacturer=</code><i>str</i><code>][,product=</code><i>str</i><code>] [,version=</code><i>str</i><code>][,serial=</code><i>str</i><code>][,uuid=</code><i>uuid</i><code>][,sku=</code><i>str</i><code>] [,family=</code><i>str</i><code>]</code></dt>
<dd> Specify SMBIOS type 1 fields</dd></dl>
<p> Network options:</p>
<dl>
<dt><code>-net nic[,vlan=</code><i>n</i><code>][,macaddr=</code><i>mac</i><code>][,model=</code><i>type</i><code>] [,name=</code><i>name</i><code>][,addr=</code><i>addr</i><code>][,vectors=</code><i>v</i><code>]</code></dt>
<dd> Create a new Network Interface Card and connect it to VLAN <i>n</i> (<i>n</i> = 0 is the default). The NIC is an e1000 by default on the PC target. Optionally, the MAC address can be changed to <i>mac</i>, the device address set to <i>addr</i> (PCI cards only), and a <i>name</i> can be assigned for use in monitor commands. Optionally, for PCI cards, you can specify the number <i>v</i> of MSI-X vectors that the card should have; this option currently only affects virtio cards; set <i>v</i> = 0 to disable MSI-X. If no <code>-net</code> option is specified, a single NIC is created. QEMU can emulate several different models of network card. Valid values for <i>type</i> are <tt>&quot;virtio&quot;</tt>, <tt>&quot;i82551&quot;</tt>, <tt>&quot;i82557b&quot;</tt>, <tt>&quot;i82559er&quot;</tt>, <tt>&quot;ne2k_pci&quot;</tt>, <tt>&quot;ne2k_isa&quot;</tt>, <tt>&quot;pcnet&quot;</tt>, <tt>&quot;rtl8139&quot;</tt>, <tt>&quot;e1000&quot;</tt>, <tt>&quot;smc91c111&quot;</tt>, <tt>&quot;lance&quot;</tt> and <tt>&quot;mcf_fec&quot;</tt>. Not all devices are supported on all targets. Use <tt>&quot;-net nic,model=help&quot;</tt> for a list of available devices for your target.</dd>
<dt><code>-netdev user,id=</code><i>id</i><code>[,</code><i>option</i><code>][,</code><i>option</i><code>][,&#8230;]</code></dt>
<dd>
</dd><dt><code>-net user[,</code><i>option</i><code>][,</code><i>option</i><code>][,&#8230;]</code></dt>
<dd> Use the user mode network stack which requires no administrator privilege to run. Valid options are:</dd>
<dl>
<dl>
<dt><code>vlan=</code><i>n</i></dt>
<dd> Connect user mode stack to VLAN <i>n</i> (<i>n</i> = 0 is the default).</dd>
<dt><code>id=</code><i>id</i></dt>
<dd>
</dd><dt><code>name=</code><i>name</i></dt>
<dd> Assign symbolic name for use in monitor commands.</dd>
<dt><code>net=</code><i>addr</i><code>[/</code><i>mask</i><code>]</code></dt>
<dd> Set IP network address the guest will see. Optionally specify the netmask, either in the form a.b.c.d or as number of valid top-most bits. Default is 10.0.2.0/24.</dd>
<dt><code>host=</code><i>addr</i></dt>
<dd> Specify the guest-visible address of the host. Default is the 2nd IP in the guest network, i.e. x.x.x.2.</dd>
<dt><code>restrict=on|off</code></dt>
<dd> If this option is enabled, the guest will be isolated, i.e. it will not be able to contact the host and no guest IP packets will be routed over the host to the outside. This option does not affect any explicitly set forwarding rules.</dd>
<dt><code>hostname=</code><i>name</i></dt>
<dd> Specifies the client hostname reported by the built-in DHCP server.</dd>
<dt><code>dhcpstart=</code><i>addr</i></dt>
<dd> Specify the first of the 16 IPs the built-in DHCP server can assign. Default is the 15th to 31st IP in the guest network, i.e. x.x.x.15 to x.x.x.31.</dd>
<dt><code>dns=</code><i>addr</i></dt>
<dd> Specify the guest-visible address of the virtual nameserver. The address must be different from the host address. Default is the 3rd IP in the guest network, i.e. x.x.x.3.</dd>
<dt><code>dnssearch=</code><i>domain</i></dt>
<dd> Provides an entry for the domain-search list sent by the built-in DHCP server. More than one domain suffix can be transmitted by specifying this option multiple times. If supported, this will cause the guest to automatically try to append the given domain suffix(es) in case a domain name can not be resolved. </dd>
<p> Example: </p>
<pre>
        qemu -net user,dnssearch=mgmt.example.org,dnssearch=example.org [...]
</pre>
<dt><code>tftp=</code><i>dir</i></dt>
<dd> When using the user mode network stack, activate a built-in TFTP server. The files in <i>dir</i> will be exposed as the root of a TFTP server. The TFTP client on the guest must be configured in binary mode (use the command <tt>&quot;bin&quot;</tt> of the Unix TFTP client).</dd>
<dt><code>bootfile=</code><i>file</i></dt>
<dd> When using the user mode network stack, broadcast <i>file</i> as the BOOTP filename. In conjunction with <code>tftp</code>, this can be used to network boot a guest from a local directory. </dd>
<p> Example (using pxelinux): </p>
<pre>
        qemu-system-i386 -hda linux.img -boot n -net user,tftp=/path/to/tftp/files,bootfile=/pxelinux.0
</pre>
<dt><code>smb=</code><i>dir</i><code>[,smbserver=</code><i>addr</i><code>]</code></dt>
<dd> When using the user mode network stack, activate a built-in SMB server so that Windows OSes can access to the host files in <i>dir</i> transparently. The IP address of the SMB server can be set to <i>addr</i>. By default the 4th IP in the guest network is used, i.e. x.x.x.4. </dd>
<p> In the guest Windows OS, the line: </p>
<pre>
        10.0.2.4 smbserver
</pre>
<p> must be added in the file <i>C:\WINDOWS\LMHOSTS</i> (for windows 9x/Me) or <i>C:\WINNT\SYSTEM32\DRIVERS\ETC\LMHOSTS</i> (Windows NT/2000). </p>
<p> Then <i>dir</i> can be accessed in <i>\smbserver\qemu</i>. </p>
<p> Note that a SAMBA server must be installed on the host OS. QEMU was tested successfully with smbd versions from Red Hat 9, Fedora Core 3 and OpenSUSE 11.x.</p>
<dt><code>hostfwd=[tcp|udp]:[</code><i>hostaddr</i><code>]:</code><i>hostport</i><code>-[</code><i>guestaddr</i><code>]:</code><i>guestport</i></dt>
<dd> Redirect incoming TCP or UDP connections to the host port <i>hostport</i> to the guest IP address <i>guestaddr</i> on guest port <i>guestport</i>. If <i>guestaddr</i> is not specified, its value is x.x.x.15 (default first address given by the built-in DHCP server). By specifying <i>hostaddr</i>, the rule can be bound to a specific host interface. If no connection type is set, TCP is used. This option can be given multiple times. </dd>
<p> For example, to redirect host X11 connection from screen 1 to guest screen 0, use the following: </p>
<pre>
        # on the host
        qemu-system-i386 -net user,hostfwd=tcp:127.0.0.1:6001-:6000 [...]
        # this host xterm should open in the guest X11 server
        xterm -display :1
</pre>
<p> To redirect telnet connections from host port 5555 to telnet port on the guest, use the following: </p>
<pre>
        # on the host
        qemu-system-i386 -net user,hostfwd=tcp::5555-:23 [...]
        telnet localhost 5555
</pre>
<p> Then when you use on the host <tt>&quot;telnet localhost 5555&quot;</tt>, you connect to the guest telnet server.</p>
<dt><code>guestfwd=[tcp]:</code><i>server</i><code>:</code><i>port</i><code>&#8211;</code><i>dev</i></dt>
<dd>
</dd><dt><code>guestfwd=[tcp]:</code><i>server</i><code>:</code><i>port</i><code>&#8211;</code><i>cmd:command</i></dt>
<dd> Forward guest TCP connections to the IP address <i>server</i> on port <i>port</i> to the character device <i>dev</i> or to a program executed by <i>cmd:command</i> which gets spawned for each connection. This option can be given multiple times. </dd>
<p> You can either use a chardev directly and have that one used throughout QEMU&#8216;s lifetime, like in the following example: </p>
<pre>
        # open 10.10.1.1:4321 on bootup, connect 10.0.2.100:1234 to it whenever
        # the guest accesses it
        qemu -net user,guestfwd=tcp:10.0.2.100:1234-tcp:10.10.1.1:4321 [...]
</pre>
<p> Or you can execute a command on every TCP connection established by the guest, so that QEMU behaves similar to an inetd process for that virtual server: </p>
<pre>
        # call &quot;netcat 10.10.1.1 4321&quot; on every TCP connection to 10.0.2.100:1234
        # and connect the TCP stream to its stdin/stdout
        qemu -net 'user,guestfwd=tcp:10.0.2.100:1234-cmd:netcat 10.10.1.1 4321'
</pre>
</dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> Note: Legacy stand-alone options -tftp, -bootp, -smb and -redir are still processed and applied to -net user. Mixing them with the new configuration syntax gives undefined results. Their use for new applications is discouraged as they will be removed from future versions.</dd></dl>
<dt><code>-netdev tap,id=</code><i>id</i><code>[,fd=</code><i>h</i><code>][,ifname=</code><i>name</i><code>][,script=</code><i>file</i><code>][,downscript=</code><i>dfile</i><code>][,helper=</code><i>helper</i><code>]</code></dt>
<dd>
</dd><dt><code>-net tap[,vlan=</code><i>n</i><code>][,name=</code><i>name</i><code>][,fd=</code><i>h</i><code>][,ifname=</code><i>name</i><code>][,script=</code><i>file</i><code>][,downscript=</code><i>dfile</i><code>][,helper=</code><i>helper</i><code>]</code></dt>
<dd> Connect the host TAP network interface <i>name</i> to VLAN <i>n</i>. </dd>
<p> Use the network script <i>file</i> to configure it and the network script <i>dfile</i> to deconfigure it. If <i>name</i> is not provided, the OS automatically provides one. The default network configure script is <i>/etc/qemu-ifup</i> and the default network deconfigure script is <i>/etc/qemu-ifdown</i>. Use <code>script=no</code> or <code>downscript=no</code> to disable script execution. </p>
<p> If running QEMU as an unprivileged user, use the network helper <i>helper</i> to configure the TAP interface. The default network helper executable is <i>/path/to/qemu-bridge-helper</i>. </p>
<p> <code>fd</code>=<i>h</i> can be used to specify the handle of an already opened host TAP interface. </p>
<p> Examples: </p>
<pre>
        #launch a QEMU instance with the default network script
        qemu-system-i386 linux.img -net nic -net tap
        #launch a QEMU instance with two NICs, each one connected
        #to a TAP device
        qemu-system-i386 linux.img \
        -net nic,vlan=0 -net tap,vlan=0,ifname=tap0 \
        -net nic,vlan=1 -net tap,vlan=1,ifname=tap1
        #launch a QEMU instance with the default network helper to
        #connect a TAP device to bridge br0
        qemu-system-i386 linux.img \
        -net nic -net tap,&quot;helper=/path/to/qemu-bridge-helper&quot;
</pre>
<dt><code>-netdev bridge,id=</code><i>id</i><code>[,br=</code><i>bridge</i><code>][,helper=</code><i>helper</i><code>]</code></dt>
<dd>
</dd><dt><code>-net bridge[,vlan=</code><i>n</i><code>][,name=</code><i>name</i><code>][,br=</code><i>bridge</i><code>][,helper=</code><i>helper</i><code>]</code></dt>
<dd> Connect a host TAP network interface to a host bridge device. </dd>
<p> Use the network helper <i>helper</i> to configure the TAP interface and attach it to the bridge. The default network helper executable is <i>/path/to/qemu-bridge-helper</i> and the default bridge device is <i>br0</i>. </p>
<p> Examples: </p>
<pre>
        #launch a QEMU instance with the default network helper to
        #connect a TAP device to bridge br0
        qemu-system-i386 linux.img -net bridge -net nic,model=virtio
        #launch a QEMU instance with the default network helper to
        #connect a TAP device to bridge qemubr0
        qemu-system-i386 linux.img -net bridge,br=qemubr0 -net nic,model=virtio
</pre>
<dt><code>-netdev socket,id=</code><i>id</i><code>[,fd=</code><i>h</i><code>][,listen=[</code><i>host</i><code>]:</code><i>port</i><code>][,connect=</code><i>host</i><code>:</code><i>port</i><code>]</code></dt>
<dd>
</dd><dt><code>-net socket[,vlan=</code><i>n</i><code>][,name=</code><i>name</i><code>][,fd=</code><i>h</i><code>] [,listen=[</code><i>host</i><code>]:</code><i>port</i><code>][,connect=</code><i>host</i><code>:</code><i>port</i><code>]</code></dt>
<dd> Connect the VLAN <i>n</i> to a remote VLAN in another QEMU virtual machine using a TCP socket connection. If <code>listen</code> is specified, QEMU waits for incoming connections on <i>port</i> (<i>host</i> is optional). <code>connect</code> is used to connect to another QEMU instance using the <code>listen</code> option. <code>fd</code>=<i>h</i> specifies an already opened TCP socket. </dd>
<p> Example: </p>
<pre>
        # launch a first QEMU instance
        qemu-system-i386 linux.img \
        -net nic,macaddr=52:54:00:12:34:56 \
        -net socket,listen=:1234
        # connect the VLAN 0 of this instance to the VLAN 0
        # of the first instance
        qemu-system-i386 linux.img \
        -net nic,macaddr=52:54:00:12:34:57 \
        -net socket,connect=127.0.0.1:1234
</pre>
<dt><code>-netdev socket,id=</code><i>id</i><code>[,fd=</code><i>h</i><code>][,mcast=</code><i>maddr</i><code>:</code><i>port</i><code>[,localaddr=</code><i>addr</i><code>]]</code></dt>
<dd>
</dd><dt><code>-net socket[,vlan=</code><i>n</i><code>][,name=</code><i>name</i><code>][,fd=</code><i>h</i><code>][,mcast=</code><i>maddr</i><code>:</code><i>port</i><code>[,localaddr=</code><i>addr</i><code>]]</code></dt>
<dd> Create a VLAN <i>n</i> shared with another QEMU virtual machines using a UDP multicast socket, effectively making a bus for every QEMU with same multicast address <i>maddr</i> and <i>port</i>. NOTES:</dd>
<dl>
<dl>
<dt>1.</dt>
<dd> Several QEMU can be running on different hosts and share same bus (assuming correct multicast setup for these hosts).</dd>
<dt>2.</dt>
<dd> mcast support is compatible with User Mode Linux (argument <code>eth</code><i>N</i><code>=mcast</code>), see &lt;<code><a rel="nofollow" href="http://user-mode-linux.sf.net">http://user-mode-linux.sf.net</a></code>&gt;.</dd>
<dt>3.</dt>
<dd> Use <code>fd=h</code> to specify an already opened UDP multicast socket.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> Example: </p>
<pre>
        # launch one QEMU instance
        qemu-system-i386 linux.img \
        -net nic,macaddr=52:54:00:12:34:56 \
        -net socket,mcast=230.0.0.1:1234
        # launch another QEMU instance on same &quot;bus&quot;
        qemu-system-i386 linux.img \
        -net nic,macaddr=52:54:00:12:34:57 \
        -net socket,mcast=230.0.0.1:1234
        # launch yet another QEMU instance on same &quot;bus&quot;
        qemu-system-i386 linux.img \
        -net nic,macaddr=52:54:00:12:34:58 \
        -net socket,mcast=230.0.0.1:1234
</pre>
<p> Example (User Mode Linux compat.): </p>
<pre>
        # launch QEMU instance (note mcast address selected
        # is UML's default)
        qemu-system-i386 linux.img \
        -net nic,macaddr=52:54:00:12:34:56 \
        -net socket,mcast=239.192.168.1:1102
        # launch UML
        /path/to/linux ubd0=/path/to/root_fs eth0=mcast
</pre>
<p> Example (send packets from host&#8217;s 1.2.3.4): </p>
<pre>
        qemu-system-i386 linux.img \
        -net nic,macaddr=52:54:00:12:34:56 \
        -net socket,mcast=239.192.168.1:1102,localaddr=1.2.3.4
</pre>
</dd></dl>
<dt><code>-netdev vde,id=</code><i>id</i><code>[,sock=</code><i>socketpath</i><code>][,port=</code><i>n</i><code>][,group=</code><i>groupname</i><code>][,mode=</code><i>octalmode</i><code>]</code></dt>
<dd>
</dd><dt><code>-net vde[,vlan=</code><i>n</i><code>][,name=</code><i>name</i><code>][,sock=</code><i>socketpath</i><code>] [,port=</code><i>n</i><code>][,group=</code><i>groupname</i><code>][,mode=</code><i>octalmode</i><code>]</code></dt>
<dd> Connect VLAN <i>n</i> to PORT <i>n</i> of a vde switch running on host and listening for incoming connections on <i>socketpath</i>. Use GROUP <i>groupname</i> and MODE <i>octalmode</i> to change default ownership and permissions for communication port. This option is only available if QEMU has been compiled with vde support enabled. </dd>
<p> Example: </p>
<pre>
        # launch vde switch
        vde_switch -F -sock /tmp/myswitch
        # launch QEMU instance
        qemu-system-i386 linux.img -net nic -net vde,sock=/tmp/myswitch
</pre>
<dt><code>-netdev hubport,id=</code><i>id</i><code>,hubid=</code><i>hubid</i></dt>
<dd> Create a hub port on QEMU &#8220;vlan&#8221; <i>hubid</i>. </dd>
<p> The hubport netdev lets you connect a NIC to a QEMU &#8220;vlan&#8221; instead of a single netdev. <tt>&quot;-net&quot;</tt> and <tt>&quot;-device&quot;</tt> with parameter <code>vlan</code> create the required hub automatically.</p>
<dt><code>-net dump[,vlan=</code><i>n</i><code>][,file=</code><i>file</i><code>][,len=</code><i>len</i><code>]</code></dt>
<dd> Dump network traffic on VLAN <i>n</i> to file <i>file</i> (<i>qemu-vlan0.pcap</i> by default). At most <i>len</i> bytes (64k by default) per packet are stored. The file format is libpcap, so it can be analyzed with tools such as tcpdump or Wireshark.</dd>
<dt><code>-net none</code></dt>
<dd> Indicate that no network devices should be configured. It is used to override the default configuration (<code>-net nic -net user</code>) which is activated if no <code>-net</code> options are provided.</dd></dl>
<p> Character device options: </p>
<p> The general form of a character device option is:</p>
<dl>
<dt><code>-chardev</code> <i>backend</i> <code>,id=</code><i>id</i> <code>[,mux=on|off] [,</code><i>options</i><code>]</code></dt>
<dd> Backend is one of: <code>null</code>, <code>socket</code>, <code>udp</code>, <code>msmouse</code>, <code>vc</code>, <code>ringbuf</code>, <code>file</code>, <code>pipe</code>, <code>console</code>, <code>serial</code>, <code>pty</code>, <code>stdio</code>, <code>braille</code>, <code>tty</code>, <code>parallel</code>, <code>parport</code>, <code>spicevmc</code>. <code>spiceport</code>. The specific backend will determine the applicable options. </dd>
<p> All devices must have an id, which can be any string up to 127 characters long. It is used to uniquely identify this device in other command line directives. </p>
<p> A character device may be used in multiplexing mode by multiple front-ends. The key sequence of <code>Control-a</code> and <code>c</code> will rotate the input focus between attached front-ends. Specify <code>mux=on</code> to enable this mode. </p>
<p> Options to each backend are described below.</p>
<dt><code>-chardev null ,id=</code><i>id</i></dt>
<dd> A void device. This device will not emit any data, and will drop any data it receives. The null backend does not take any options.</dd>
<dt><code>-chardev socket ,id=</code><i>id</i> <code>[</code><i></i><i>TCP</i><i> options</i> <code>or</code> <i>unix options</i><code>] [,server] [,nowait] [,telnet]</code></dt>
<dd> Create a two-way stream socket, which can be either a TCP or a unix socket. A unix socket will be created if <code>path</code> is specified. Behaviour is undefined if TCP options are specified for a unix socket. </dd>
<p> <code>server</code> specifies that the socket shall be a listening socket. </p>
<p> <code>nowait</code> specifies that QEMU should not block waiting for a client to connect to a listening socket. </p>
<p> <code>telnet</code> specifies that traffic on the socket should interpret telnet escape sequences. </p>
<p> TCP and unix socket options are given below:</p>
<dl>
<dl>
<dt><code>TCP</code><code> options: port=</code><i>port</i> <code>[,host=</code><i>host</i><code>] [,to=</code><i>to</i><code>] [,ipv4] [,ipv6] [,nodelay]</code></dt>
<dd> <code>host</code> for a listening socket specifies the local address to be bound. For a connecting socket species the remote host to connect to. <code>host</code> is optional for listening sockets. If not specified it defaults to <tt>0.0.0.0</tt>. </dd>
<p> <code>port</code> for a listening socket specifies the local port to be bound. For a connecting socket specifies the port on the remote host to connect to. <code>port</code> can be given as either a port number or a service name. <code>port</code> is required. </p>
<p> <code>to</code> is only relevant to listening sockets. If it is specified, and <code>port</code> cannot be bound, QEMU will attempt to bind to subsequent ports up to and including <code>to</code> until it succeeds. <code>to</code> must be specified as a port number. </p>
<p> <code>ipv4</code> and <code>ipv6</code> specify that either IPv4 or IPv6 must be used. If neither is specified the socket may use either protocol. </p>
<p> <code>nodelay</code> disables the Nagle algorithm.</p>
<dt><code>unix options: path=</code><i>path</i></dt>
<dd> <code>path</code> specifies the local path of the unix socket. <code>path</code> is required.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-chardev udp ,id=</code><i>id</i> <code>[,host=</code><i>host</i><code>] ,port=</code><i>port</i> <code>[,localaddr=</code><i>localaddr</i><code>] [,localport=</code><i>localport</i><code>] [,ipv4] [,ipv6]</code></dt>
<dd> Sends all traffic from the guest to a remote host over UDP. </dd>
<p> <code>host</code> specifies the remote host to connect to. If not specified it defaults to <tt>&quot;localhost&quot;</tt>. </p>
<p> <code>port</code> specifies the port on the remote host to connect to. <code>port</code> is required. </p>
<p> <code>localaddr</code> specifies the local address to bind to. If not specified it defaults to <tt>0.0.0.0</tt>. </p>
<p> <code>localport</code> specifies the local port to bind to. If not specified any available local port will be used. </p>
<p> <code>ipv4</code> and <code>ipv6</code> specify that either IPv4 or IPv6 must be used. If neither is specified the device may use either protocol.</p>
<dt><code>-chardev msmouse ,id=</code><i>id</i></dt>
<dd> Forward QEMU&#8216;s emulated msmouse events to the guest. <code>msmouse</code> does not take any options.</dd>
<dt><code>-chardev vc ,id=</code><i>id</i> <code>[[,width=</code><i>width</i><code>] [,height=</code><i>height</i><code>]] [[,cols=</code><i>cols</i><code>] [,rows=</code><i>rows</i><code>]]</code></dt>
<dd> Connect to a QEMU text console. <code>vc</code> may optionally be given a specific size. </dd>
<p> <code>width</code> and <code>height</code> specify the width and height respectively of the console, in pixels. </p>
<p> <code>cols</code> and <code>rows</code> specify that the console be sized to fit a text console with the given dimensions.</p>
<dt><code>-chardev ringbuf ,id=</code><i>id</i> <code>[,size=</code><i>size</i><code>]</code></dt>
<dd> Create a ring buffer with fixed size <code>size</code>. <i>size</i> must be a power of two, and defaults to <tt>&quot;64K&quot;</tt>).</dd>
<dt><code>-chardev file ,id=</code><i>id</i> <code>,path=</code><i>path</i></dt>
<dd> Log all traffic received from the guest to a file. </dd>
<p> <code>path</code> specifies the path of the file to be opened. This file will be created if it does not already exist, and overwritten if it does. <code>path</code> is required.</p>
<dt><code>-chardev pipe ,id=</code><i>id</i> <code>,path=</code><i>path</i></dt>
<dd> Create a two-way connection to the guest. The behaviour differs slightly between Windows hosts and other hosts: </dd>
<p> On Windows, a single duplex pipe will be created at <i>\.pipe\</i>path<i></i>. </p>
<p> On other hosts, 2 pipes will be created called <i></i>path<i>.in</i> and <i></i>path<i>.out</i>. Data written to <i></i>path<i>.in</i> will be received by the guest. Data written by the guest can be read from <i></i>path<i>.out</i>. QEMU will not create these fifos, and requires them to be present. </p>
<p> <code>path</code> forms part of the pipe path as described above. <code>path</code> is required.</p>
<dt><code>-chardev console ,id=</code><i>id</i></dt>
<dd> Send traffic from the guest to QEMU&#8216;s standard output. <code>console</code> does not take any options. </dd>
<p> <code>console</code> is only available on Windows hosts.</p>
<dt><code>-chardev serial ,id=</code><i>id</i> <code>,path=</code><code>path</code></dt>
<dd> Send traffic from the guest to a serial device on the host. </dd>
<p> On Unix hosts serial will actually accept any tty device, not only serial lines. </p>
<p> <code>path</code> specifies the name of the serial device to open.</p>
<dt><code>-chardev pty ,id=</code><i>id</i></dt>
<dd> Create a new pseudo-terminal on the host and connect to it. <code>pty</code> does not take any options. </dd>
<p> <code>pty</code> is not available on Windows hosts.</p>
<dt><code>-chardev stdio ,id=</code><i>id</i> <code>[,signal=on|off]</code></dt>
<dd> Connect to standard input and standard output of the QEMU process. </dd>
<p> <code>signal</code> controls if signals are enabled on the terminal, that includes exiting QEMU with the key sequence <code>Control-c</code>. This option is enabled by default, use <code>signal=off</code> to disable it. </p>
<p> <code>stdio</code> is not available on Windows hosts.</p>
<dt><code>-chardev braille ,id=</code><i>id</i></dt>
<dd> Connect to a local BrlAPI server. <code>braille</code> does not take any options.</dd>
<dt><code>-chardev tty ,id=</code><i>id</i> <code>,path=</code><i>path</i></dt>
<dd> <code>tty</code> is only available on Linux, Sun, FreeBSD, NetBSD, OpenBSD and DragonFlyBSD hosts. It is an alias for <code>serial</code>. </dd>
<p> <code>path</code> specifies the path to the tty. <code>path</code> is required.</p>
<dt><code>-chardev parallel ,id=</code><i>id</i> <code>,path=</code><i>path</i></dt>
<dd>
</dd><dt><code>-chardev parport ,id=</code><i>id</i> <code>,path=</code><i>path</i></dt>
<dd> <code>parallel</code> is only available on Linux, FreeBSD and DragonFlyBSD hosts. </dd>
<p> Connect to a local parallel port. </p>
<p> <code>path</code> specifies the path to the parallel port device. <code>path</code> is required.</p>
<dt><code>-chardev spicevmc ,id=</code><i>id</i> <code>,debug=</code><i>debug</i><code>, name=</code><i>name</i></dt>
<dd> <code>spicevmc</code> is only available when spice support is built in. </dd>
<p> <code>debug</code> debug level for spicevmc </p>
<p> <code>name</code> name of spice channel to connect to </p>
<p> Connect to a spice virtual machine channel, such as vdiport.</p>
<dt><code>-chardev spiceport ,id=</code><i>id</i> <code>,debug=</code><i>debug</i><code>, name=</code><i>name</i></dt>
<dd> <code>spiceport</code> is only available when spice support is built in. </dd>
<p> <code>debug</code> debug level for spicevmc </p>
<p> <code>name</code> name of spice port to connect to </p>
<p> Connect to a spice port, allowing a Spice client to handle the traffic identified by a name (preferably a fqdn).</dl>
<p> Device URL Syntax: </p>
<p> In addition to using normal file images for the emulated storage devices, QEMU can also use networked resources such as iSCSI devices. These are specified using a special URL syntax.</p>
<dl>
<dt><code>iSCSI</code></dt>
<dd> iSCSI support allows QEMU to access iSCSI resources directly and use as images for the guest storage. Both disk and cdrom images are supported. </dd>
<p> Syntax for specifying iSCSI LUNs is &#8220;iscsi://&lt;target-ip&gt;[:&lt;port&gt;]/&lt;target-iqn&gt;/&lt;lun&gt;&#8221; </p>
<p> By default qemu will use the iSCSI initiator-name &#8216;iqn.2008-11.org.linux-kvm[:&lt;name&gt;]&#8217; but this can also be set from the command line or a configuration file. </p>
<p> Example (without authentication): </p>
<pre>
        qemu-system-i386 -iscsi initiator-name=iqn.2001-04.com.example:my-initiator \
        -cdrom <a href="iscsi://192.0.2.1/iqn.2001-04.com.example/2">iscsi://192.0.2.1/iqn.2001-04.com.example/2</a> \
        -drive file=<a href="iscsi://192.0.2.1/iqn.2001-04.com.example/1">iscsi://192.0.2.1/iqn.2001-04.com.example/1</a>
</pre>
<p> Example (CHAP username/password via URL): </p>
<pre>
        qemu-system-i386 -drive file=<a href="iscsi://user%password@192.0.2.1/iqn.2001-04.com.example/1">iscsi://user%password@192.0.2.1/iqn.2001-04.com.example/1</a>
</pre>
<p> Example (CHAP username/password via environment variables): </p>
<pre>
        LIBISCSI_CHAP_USERNAME=&quot;user&quot; \
        LIBISCSI_CHAP_PASSWORD=&quot;password&quot; \
        qemu-system-i386 -drive file=<a href="iscsi://192.0.2.1/iqn.2001-04.com.example/1">iscsi://192.0.2.1/iqn.2001-04.com.example/1</a>
</pre>
<p> iSCSI support is an optional feature of QEMU and only available when compiled and linked against libiscsi. </p>
<p> iSCSI parameters such as username and password can also be specified via a configuration file. See qemu-doc for more information and examples.</p>
<dt><code>NBD</code></dt>
<dd> QEMU supports NBD (Network Block Devices) both using TCP protocol as well as Unix Domain Sockets. </dd>
<p> Syntax for specifying a NBD device using TCP &#8220;nbd:&lt;server-ip&gt;:&lt;port&gt;[:exportname=&lt;export&gt;]&#8221; </p>
<p> Syntax for specifying a NBD device using Unix Domain Sockets &#8220;nbd:unix:&lt;domain-socket&gt;[:exportname=&lt;export&gt;]&#8221; </p>
<p> Example for TCP </p>
<pre>
        qemu-system-i386 --drive file=nbd:192.0.2.1:30000
</pre>
<p> Example for Unix Domain Sockets </p>
<pre>
        qemu-system-i386 --drive file=nbd:unix:/tmp/nbd-socket
</pre>
<dt><code>SSH</code></dt>
<dd> QEMU supports SSH (Secure Shell) access to remote disks. </dd>
<p> Examples: </p>
<pre>
        qemu-system-i386 -drive file=<a href="ssh://user@host/path/to/disk.img">ssh://user@host/path/to/disk.img</a>
        qemu-system-i386 -drive file.driver=ssh,file.user=user,file.host=host,file.port=22,file.path=/path/to/disk.img
</pre>
<p> Currently authentication must be done using ssh-agent. Other authentication methods may be supported in future.</p>
<dt><code>Sheepdog</code></dt>
<dd> Sheepdog is a distributed storage system for QEMU. QEMU supports using either local sheepdog devices or remote networked devices. </dd>
<p> Syntax for specifying a sheepdog device </p>
<pre><code>
sheepdog[+tcp | +unix]: //[host:port]/vdiname[?socket=path][#snapid|#tag]
</code></pre>
<p> Example </p>
<pre>
        qemu-system-i386 --drive file=sheepdog://192.0.2.1:30000/MyVirtualMachine
</pre>
<p> See also &lt;<code><a rel="nofollow" href="http://http://www.osrg.net/sheepdog/">http://http://www.osrg.net/sheepdog/</a></code>&gt;.</p>
<dt><code>GlusterFS</code></dt>
<dd> GlusterFS is an user space distributed file system. QEMU supports the use of GlusterFS volumes for hosting VM disk images using TCP, Unix Domain Sockets and RDMA transport protocols. </dd>
<p> Syntax for specifying a VM disk image on GlusterFS volume is </p>
<pre><code>
gluster[+transport]: //[server[:port]]/volname/image[?socket=...]
</code></pre>
<p> Example </p>
<pre>
        qemu-system-x86_64 --drive file=gluster://192.0.2.1/testvol/a.img
</pre>
<p> See also &lt;<code><a rel="nofollow" href="http://www.gluster.org">http://www.gluster.org</a></code>&gt;.</dl>
<p> Bluetooth(R) options:</p>
<dl>
<dt><code>-bt hci[&#8230;]</code></dt>
<dd> Defines the function of the corresponding Bluetooth HCI.  -bt options are matched with the HCIs present in the chosen machine type. For example when emulating a machine with only one HCI built into it, only the first <tt>&quot;-bt hci[...]&quot;</tt> option is valid and defines the HCI&#8216;s logic. The Transport Layer is decided by the machine type. Currently the machines <tt>&quot;n800&quot;</tt> and <tt>&quot;n810&quot;</tt> have one HCI and all other machines have none. </dd>
<p> The following three types are recognized:</p>
<dl>
<dl>
<dt><code>-bt hci,null</code></dt>
<dd> (default) The corresponding Bluetooth HCI assumes no internal logic and will not respond to any HCI commands or emit events.</dd>
<dt><code>-bt hci,host[:</code><i>id</i><code>]</code></dt>
<dd> (<tt>&quot;bluez&quot;</tt> only) The corresponding HCI passes commands / events to / from the physical HCI identified by the name <i>id</i> (default: <tt>&quot;hci0&quot;</tt>) on the computer running QEMU.  Only available on <tt>&quot;bluez&quot;</tt> capable systems like Linux.</dd>
<dt><code>-bt hci[,vlan=</code><i>n</i><code>]</code></dt>
<dd> Add a virtual, standard HCI that will participate in the Bluetooth scatternet <i>n</i> (default <tt>0</tt>). Similarly to <code>-net</code> VLANs, devices inside a bluetooth network <i>n</i> can only communicate with other devices in the same network (scatternet).</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-bt vhci[,vlan=</code><i>n</i><code>]</code></dt>
<dd> (Linux-host only) Create a HCI in scatternet <i>n</i> (default 0) attached to the host bluetooth stack instead of to the emulated target. This allows the host and target machines to participate in a common scatternet and communicate. Requires the Linux <tt>&quot;vhci&quot;</tt> driver installed. Can be used as following: </dd>
<pre>
        qemu-system-i386 [...OPTIONS...] -bt hci,vlan=5 -bt vhci,vlan=5
</pre>
<dt><code>-bt device:</code><i>dev</i><code>[,vlan=</code><i>n</i><code>]</code></dt>
<dd> Emulate a bluetooth device <i>dev</i> and place it in network <i>n</i> (default <tt>0</tt>). QEMU can only emulate one type of bluetooth devices currently:</dd>
<dl>
<dl>
<dt><code>keyboard</code></dt>
<dd> Virtual wireless keyboard implementing the HIDP bluetooth profile.</dd></dl>
</dl>
<dl>
</dl>
</dl>
<p> TPM device options: </p>
<p> The general form of a TPM device option is:</p>
<dl>
<dt><code>-tpmdev</code> <i>backend</i> <code>,id=</code><i>id</i> <code>[,</code><i>options</i><code>]</code></dt>
<dd> Backend type must be: <code>passthrough</code>. </dd>
<p> The specific backend type will determine the applicable options. The <tt>&quot;-tpmdev&quot;</tt> option creates the TPM backend and requires a <tt>&quot;-device&quot;</tt> option that specifies the TPM frontend interface model. </p>
<p> Options to each backend are described below. </p>
<p> Use &#8216;help&#8217; to print all available TPM backend types. </p>
<pre>
        qemu -tpmdev help
</pre>
<dt><code>-tpmdev passthrough, id=</code><i>id</i><code>, path=</code><i>path</i><code>, cancel-path=</code><i>cancel-path</i></dt>
<dd> (Linux-host only) Enable access to the host&#8217;s TPM using the passthrough driver. </dd>
<p> <code>path</code> specifies the path to the host&#8217;s TPM device, i.e., on a Linux host this would be <tt>&quot;/dev/tpm0&quot;</tt>. <code>path</code> is optional and by default <tt>&quot;/dev/tpm0&quot;</tt> is used. </p>
<p> <code>cancel-path</code> specifies the path to the host TPM device&#8217;s sysfs entry allowing for cancellation of an ongoing TPM command. <code>cancel-path</code> is optional and by default QEMU will search for the sysfs entry to use. </p>
<p> Some notes about using the host&#8217;s TPM with the passthrough driver: </p>
<p> The TPM device accessed by the passthrough driver must not be used by any other application on the host. </p>
<p> Since the host&#8217;s firmware (BIOS/UEFI) has already initialized the TPM, the VM&#8216;s firmware (BIOS/UEFI) will not be able to initialize the TPM again and may therefore not show a TPM-specific menu that would otherwise allow the user to configure the TPM, e.g., allow the user to enable/disable or activate/deactivate the TPM. Further, if TPM ownership is released from within a VM then the host&#8217;s TPM will get disabled and deactivated. To enable and activate the TPM again afterwards, the host has to be rebooted and the user is required to enter the firmware&#8217;s menu to enable and activate the TPM. If the TPM is left disabled and/or deactivated most TPM commands will fail. </p>
<p> To create a passthrough TPM use the following two options: </p>
<pre>
        -tpmdev passthrough,id=tpm0 -device tpm-tis,tpmdev=tpm0
</pre>
<p> Note that the <tt>&quot;-tpmdev&quot;</tt> id is <tt>&quot;tpm0&quot;</tt> and is referenced by <tt>&quot;tpmdev=tpm0&quot;</tt> in the device option.</dl>
<p> Linux/Multiboot boot specific: </p>
<p> When using these options, you can use a given Linux or Multiboot kernel without installing it in the disk image. It can be useful for easier testing of various kernels.</p>
<dl>
<dt><code>-kernel</code> <i>bzImage</i></dt>
<dd> Use <i>bzImage</i> as kernel image. The kernel can be either a Linux kernel or in multiboot format.</dd>
<dt><code>-append</code> <i>cmdline</i></dt>
<dd> Use <i>cmdline</i> as kernel command line</dd>
<dt><code>-initrd</code> <i>file</i></dt>
<dd> Use <i>file</i> as initial ram disk.</dd>
<dt><code>-initrd &quot;</code><i>file1</i> <code>arg=foo,</code><i>file2</i><code>&quot;</code></dt>
<dd> This syntax is only available with multiboot. </dd>
<p> Use <i>file1</i> and <i>file2</i> as modules and pass arg=foo as parameter to the first module.</p>
<dt><code>-dtb</code> <i>file</i></dt>
<dd> Use <i>file</i> as a device tree binary (dtb) image and pass it to the kernel on boot.</dd></dl>
<p> Debug/Expert options:</p>
<dl>
<dt><code>-serial</code> <i>dev</i></dt>
<dd> Redirect the virtual serial port to host character device <i>dev</i>. The default device is <tt>&quot;vc&quot;</tt> in graphical mode and <tt>&quot;stdio&quot;</tt> in non graphical mode. </dd>
<p> This option can be used several times to simulate up to 4 serial ports. </p>
<p> Use <tt>&quot;-serial none&quot;</tt> to disable all serial ports. </p>
<p> Available character devices are:</p>
<dl>
<dl>
<dt><code>vc[:</code><i>W</i><code>x</code><i>H</i><code>]</code></dt>
<dd> Virtual console. Optionally, a width and height can be given in pixel with </dd>
<pre>
        vc:800x600
</pre>
<p> It is also possible to specify width or height in characters: </p>
<pre>
        vc:80Cx24C
</pre>
<dt><code>pty</code></dt>
<dd> [Linux only] Pseudo TTY (a new PTY is automatically allocated)</dd>
<dt><code>none</code></dt>
<dd> No device is allocated.</dd>
<dt><code>null</code></dt>
<dd> void device</dd>
<dt><code>chardev:</code><i>id</i></dt>
<dd> Use a named character device defined with the <tt>&quot;-chardev&quot;</tt> option.</dd>
<dt><code>/dev/XXX</code></dt>
<dd> [Linux only] Use host tty, e.g. <i>/dev/ttyS0</i>. The host serial port parameters are set according to the emulated ones.</dd>
<dt><code>/dev/parport</code><i>N</i></dt>
<dd> [Linux only, parallel port only] Use host parallel port <i>N</i>. Currently SPP and EPP parallel port features can be used.</dd>
<dt><code>file:</code><i>filename</i></dt>
<dd> Write output to <i>filename</i>. No character can be read.</dd>
<dt><code>stdio</code></dt>
<dd> [Unix only] standard input/output</dd>
<dt><code>pipe:</code><i>filename</i></dt>
<dd> name pipe <i>filename</i></dd>
<dt><code>COM</code><i>n</i></dt>
<dd> [Windows only] Use host serial port <i>n</i></dd>
<dt><code>udp:[</code><i>remote_host</i><code>]:</code><i>remote_port</i><code>[@[</code><i>src_ip</i><code>]:</code><i>src_port</i><code>]</code></dt>
<dd> This implements UDP Net Console. When <i>remote_host</i> or <i>src_ip</i> are not specified they default to <tt>0.0.0.0</tt>. When not using a specified <i>src_port</i> a random port is automatically chosen. </dd>
<p> If you just want a simple readonly console you can use <tt>&quot;netcat&quot;</tt> or <tt>&quot;nc&quot;</tt>, by starting QEMU with: <tt>&quot;-serial udp::4555&quot;</tt> and nc as: <tt>&quot;nc -u -l -p 4555&quot;</tt>. Any time QEMU writes something to that port it will appear in the netconsole session. </p>
<p> If you plan to send characters back via netconsole or you want to stop and start QEMU a lot of times, you should have QEMU use the same source port each time by using something like <tt>&quot;-serial udp::4555 [at] 4556&quot;</tt> to QEMU. Another approach is to use a patched version of netcat which can listen to a TCP port and send and receive characters via udp. If you have a patched version of netcat which activates telnet remote echo and single char transfer, then you can use the following options to step up a netcat redirector to allow telnet on port 5555 to access the QEMU port.</p>
<dl>
<dl>
<dt>&quot;QEMU Options:&quot;</dt>
<dd> -serial udp::4555 [at] 4556</dd>
<dt>&quot;netcat options:&quot;</dt>
<dd> -u -P 4555 -L 0.0.0.0:4556 -t -p 5555 -I -T</dd>
<dt>&quot;telnet options:&quot;</dt>
<dd> localhost 5555</dd></dl>
</dl>
<dl>
</dl>
<dt><code>tcp:[</code><i>host</i><code>]:</code><i>port</i><code>[,</code><i>server</i><code>][,nowait][,nodelay]</code></dt>
<dd> The TCP Net Console has two modes of operation. It can send the serial I/O to a location or wait for a connection from a location. By default the TCP Net Console is sent to <i>host</i> at the <i>port</i>. If you use the <i>server</i> option QEMU will wait for a client socket application to connect to the port before continuing, unless the <tt>&quot;nowait&quot;</tt> option was specified. The <tt>&quot;nodelay&quot;</tt> option disables the Nagle buffering algorithm. If <i>host</i> is omitted, 0.0.0.0 is assumed. Only one TCP connection at a time is accepted. You can use <tt>&quot;telnet&quot;</tt> to connect to the corresponding character device.</dd>
<dl>
<dl>
<dt>&quot;Example to send tcp console to 192.168.0.2 port 4444&quot;</dt>
<dd> -serial tcp:192.168.0.2:4444</dd>
<dt>&quot;Example to listen and wait on port 4444 for connection&quot;</dt>
<dd> -serial tcp::4444,server</dd>
<dt>&quot;Example to not wait and listen on ip 192.168.0.100 port 4444&quot;</dt>
<dd> -serial tcp:192.168.0.100:4444,server,nowait</dd></dl>
</dl>
<dl>
</dl>
<dt><code>telnet:</code><i>host</i><code>:</code><i>port</i><code>[,server][,nowait][,nodelay]</code></dt>
<dd> The telnet protocol is used instead of raw tcp sockets. The options work the same as if you had specified <tt>&quot;-serial tcp&quot;</tt>. The difference is that the port acts like a telnet server or client using telnet option negotiation. This will also allow you to send the MAGIC_SYSRQ sequence if you use a telnet that supports sending the break sequence. Typically in unix telnet you do it with Control-] and then type &#8220;send break&#8221; followed by pressing the enter key.</dd>
<dt><code>unix:</code><i>path</i><code>[,server][,nowait]</code></dt>
<dd> A unix domain socket is used instead of a tcp socket. The option works the same as if you had specified <tt>&quot;-serial tcp&quot;</tt> except the unix domain socket <i>path</i> is used for connections.</dd>
<dt><code>mon:</code><i>dev_string</i></dt>
<dd> This is a special option to allow the monitor to be multiplexed onto another serial port. The monitor is accessed with key sequence of <code>Control-a</code> and then pressing <code>c</code>. <i>dev_string</i> should be any one of the serial devices specified above. An example to multiplex the monitor onto a telnet server listening on port 4444 would be:</dd>
<dl>
<dl>
<dt>&quot;-serial mon:telnet::4444,server,nowait&quot;</dt>
<dd></dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> When the monitor is multiplexed to stdio in this way, Ctrl+C will not terminate QEMU any more but will be passed to the guest instead.</dd></dl>
<dt><code>braille</code></dt>
<dd> Braille device. This will use BrlAPI to display the braille output on a real or fake device.</dd>
<dt><code>msmouse</code></dt>
<dd> Three button serial mouse. Configure the guest to use Microsoft protocol.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-parallel</code> <i>dev</i></dt>
<dd> Redirect the virtual parallel port to host device <i>dev</i> (same devices as the serial port). On Linux hosts, <i>/dev/parportN</i> can be used to use hardware devices connected on the corresponding host parallel port. </dd>
<p> This option can be used several times to simulate up to 3 parallel ports. </p>
<p> Use <tt>&quot;-parallel none&quot;</tt> to disable all parallel ports.</p>
<dt><code>-monitor</code> <i>dev</i></dt>
<dd> Redirect the monitor to host device <i>dev</i> (same devices as the serial port). The default device is <tt>&quot;vc&quot;</tt> in graphical mode and <tt>&quot;stdio&quot;</tt> in non graphical mode. Use <tt>&quot;-monitor none&quot;</tt> to disable the default monitor.</dd>
<dt><code>-qmp</code> <i>dev</i></dt>
<dd> Like -monitor but opens in &#8216;control&#8217; mode.</dd>
<dt><code>-mon [chardev=]name[,mode=readline|control][,default]</code></dt>
<dd> Setup monitor on chardev <i>name</i>.</dd>
<dt><code>-debugcon</code> <i>dev</i></dt>
<dd> Redirect the debug console to host device <i>dev</i> (same devices as the serial port). The debug console is an I/O port which is typically port 0xe9; writing to that I/O port sends output to this device. The default device is <tt>&quot;vc&quot;</tt> in graphical mode and <tt>&quot;stdio&quot;</tt> in non graphical mode.</dd>
<dt><code>-pidfile</code> <i>file</i></dt>
<dd> Store the QEMU process PID in <i>file</i>. It is useful if you launch QEMU from a script.</dd>
<dt><code>-singlestep</code></dt>
<dd> Run the emulation in single step mode.</dd>
<dt><code>-S</code></dt>
<dd> Do not start CPU at startup (you must type &#8216;c&#8217; in the monitor).</dd>
<dt><code>-realtime mlock=on|off</code></dt>
<dd> Run qemu with realtime features. mlocking qemu and guest memory can be enabled via <code>mlock=on</code> (enabled by default).</dd>
<dt><code>-gdb</code> <i>dev</i></dt>
<dd> Wait for gdb connection on device <i>dev</i>. Typical connections will likely be TCP-based, but also UDP, pseudo TTY, or even stdio are reasonable use case. The latter is allowing to start QEMU from within gdb and establish the connection via a pipe: </dd>
<pre>
        (gdb) target remote | exec qemu-system-i386 -gdb stdio ...
</pre>
<dt><code>-s</code></dt>
<dd> Shorthand for -gdb tcp::1234, i.e. open a gdbserver on TCP port 1234.</dd>
<dt><code>-d</code> <i>item1</i><code>[,&#8230;]</code></dt>
<dd> Enable logging of specified items. Use &#8216;-d help&#8217; for a list of log items.</dd>
<dt><code>-D</code> <i>logfile</i></dt>
<dd> Output log in <i>logfile</i> instead of to stderr</dd>
<dt><code>-L</code> <i>path</i></dt>
<dd> Set the directory for the BIOS, VGA BIOS and keymaps.</dd>
<dt><code>-bios</code> <i>file</i></dt>
<dd> Set the filename for the BIOS.</dd>
<dt><code>-enable-kvm</code></dt>
<dd> Enable KVM full virtualization support. This option is only available if KVM support is enabled when compiling.</dd>
<dt><code>-xen-domid</code> <i>id</i></dt>
<dd> Specify xen guest domain <i>id</i> (XEN only).</dd>
<dt><code>-xen-create</code></dt>
<dd> Create domain using xen hypercalls, bypassing xend. Warning: should not be used when xend is in use (XEN only).</dd>
<dt><code>-xen-attach</code></dt>
<dd> Attach to existing xen domain. xend will use this when starting QEMU (XEN only).</dd>
<dt><code>-no-reboot</code></dt>
<dd> Exit instead of rebooting.</dd>
<dt><code>-no-shutdown</code></dt>
<dd> Don&#8217;t exit QEMU on guest shutdown, but instead only stop the emulation. This allows for instance switching to monitor to commit changes to the disk image.</dd>
<dt><code>-loadvm</code> <i>file</i></dt>
<dd> Start right away with a saved state (<tt>&quot;loadvm&quot;</tt> in monitor)</dd>
<dt><code>-daemonize</code></dt>
<dd> Daemonize the QEMU process after initialization. QEMU will not detach from standard IO until it is ready to receive connections on any of its devices. This option is a useful way for external programs to launch QEMU without having to cope with initialization race conditions.</dd>
<dt><code>-option-rom</code> <i>file</i></dt>
<dd> Load the contents of <i>file</i> as an option ROM. This option is useful to load things like EtherBoot.</dd>
<dt><code>-clock</code> <i>method</i></dt>
<dd> Force the use of the given methods for timer alarm. To see what timers are available use <tt>&quot;-clock help&quot;</tt>.</dd>
<dt><code>-rtc [base=utc|localtime|</code><i>date</i><code>][,clock=host|vm][,driftfix=none|slew]</code></dt>
<dd> Specify <code>base</code> as <tt>&quot;utc&quot;</tt> or <tt>&quot;localtime&quot;</tt> to let the RTC start at the current UTC or local time, respectively. <tt>&quot;localtime&quot;</tt> is required for correct date in MS-DOS or Windows. To start at a specific point in time, provide <i>date</i> in the format <tt>&quot;2006-06-17T16:01:21&quot;</tt> or <tt>&quot;2006-06-17&quot;</tt>. The default base is UTC. </dd>
<p> By default the RTC is driven by the host system time. This allows to use the RTC as accurate reference clock inside the guest, specifically if the host time is smoothly following an accurate external reference clock, e.g. via NTP. If you want to isolate the guest time from the host, you can set <code>clock</code> to <tt>&quot;rt&quot;</tt> instead. To even prevent it from progressing during suspension, you can set it to <tt>&quot;vm&quot;</tt>. </p>
<p> Enable <code>driftfix</code> (i386 targets only) if you experience time drift problems, specifically with Windows&#8217; ACPI HAL. This option will try to figure out how many timer interrupts were not processed by the Windows guest and will re-inject them.</p>
<dt><code>-icount [</code><i>N</i><code>|auto]</code></dt>
<dd> Enable virtual instruction counter. The virtual cpu will execute one instruction every 2^<i>N</i> ns of virtual time. If <tt>&quot;auto&quot;</tt> is specified then the virtual cpu speed will be automatically adjusted to keep virtual time within a few seconds of real time. </dd>
<p> Note that while this option can give deterministic behavior, it does not provide cycle accurate emulation. Modern CPUs contain superscalar out of order cores with complex cache hierarchies. The number of instructions executed often has little or no correlation with actual performance.</p>
<dt><code>-watchdog</code> <i>model</i></dt>
<dd> Create a virtual hardware watchdog device. Once enabled (by a guest action), the watchdog must be periodically polled by an agent inside the guest or else the guest will be restarted. </dd>
<p> The <i>model</i> is the model of hardware watchdog to emulate. Choices for model are: <tt>&quot;ib700&quot;</tt> (iBASE 700) which is a very simple ISA watchdog with a single timer, or <tt>&quot;i6300esb&quot;</tt> (Intel 6300ESB I/O controller hub) which is a much more featureful PCI-based dual-timer watchdog. Choose a model for which your guest has drivers. </p>
<p> Use <tt>&quot;-watchdog help&quot;</tt> to list available hardware models. Only one watchdog can be enabled for a guest.</p>
<dt><code>-watchdog-action</code> <i>action</i></dt>
<dd> The <i>action</i> controls what QEMU will do when the watchdog timer expires. The default is <tt>&quot;reset&quot;</tt> (forcefully reset the guest). Other possible actions are: <tt>&quot;shutdown&quot;</tt> (attempt to gracefully shutdown the guest), <tt>&quot;poweroff&quot;</tt> (forcefully poweroff the guest), <tt>&quot;pause&quot;</tt> (pause the guest), <tt>&quot;debug&quot;</tt> (print a debug message and continue), or <tt>&quot;none&quot;</tt> (do nothing). </dd>
<p> Note that the <tt>&quot;shutdown&quot;</tt> action requires that the guest responds to ACPI signals, which it may not be able to do in the sort of situations where the watchdog would have expired, and thus <tt>&quot;-watchdog-action shutdown&quot;</tt> is not recommended for production use. </p>
<p> Examples:</p>
<dl>
<dl>
<dt>&quot;-watchdog i6300esb -watchdog-action pause&quot;</dt>
<dd>
</dd><dt>&quot;-watchdog ib700&quot;</dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>-echr</code> <i>numeric_ascii_value</i></dt>
<dd> Change the escape character used for switching to the monitor when using monitor and serial sharing. The default is <tt>0x01</tt> when using the <tt>&quot;-nographic&quot;</tt> option. <tt>0x01</tt> is equal to pressing <tt>&quot;Control-a&quot;</tt>. You can select a different character from the ascii control keys where 1 through 26 map to Control-a through Control-z. For instance you could use the either of the following to change the escape character to Control-t.</dd>
<dl>
<dl>
<dt>&quot;-echr 0x14&quot;</dt>
<dd>
</dd><dt>&quot;-echr 20&quot;</dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>-virtioconsole</code> <i>c</i></dt>
<dd> Set virtio console. </dd>
<p> This option is maintained for backward compatibility. </p>
<p> Please use <tt>&quot;-device virtconsole&quot;</tt> for the new way of invocation.</p>
<dt><code>-show-cursor</code></dt>
<dd> Show cursor.</dd>
<dt><code>-tb-size</code> <i>n</i></dt>
<dd> Set TB size.</dd>
<dt><code>-incoming</code> <i>port</i></dt>
<dd> Prepare for incoming migration, listen on <i>port</i>.</dd>
<dt><code>-nodefaults</code></dt>
<dd> Don&#8217;t create default devices. Normally, QEMU sets the default devices like serial port, parallel port, virtual console, monitor device, VGA adapter, floppy and CD-ROM drive and others. The <tt>&quot;-nodefaults&quot;</tt> option will disable all those default devices.</dd>
<dt><code>-chroot</code> <i>dir</i></dt>
<dd> Immediately before starting guest execution, chroot to the specified directory. Especially useful in combination with -runas.</dd>
<dt><code>-runas</code> <i>user</i></dt>
<dd> Immediately before starting guest execution, drop root privileges, switching to the specified user.</dd>
<dt><code>-prom-env</code> <i>variable</i><code>=</code><i>value</i></dt>
<dd> Set OpenBIOS nvram <i>variable</i> to given <i>value</i> (PPC, SPARC only).</dd>
<dt><code>-semihosting</code></dt>
<dd> Semihosting mode (ARM, M68K, Xtensa only).</dd>
<dt><code>-old-param</code></dt>
<dd> Old param mode (ARM only).</dd>
<dt><code>-sandbox</code> <i>arg</i></dt>
<dd> Enable Seccomp mode 2 system call filter. &#8216;on&#8217; will enable syscall filtering and &#8216;off&#8217; will disable it. The default is &#8216;off&#8217;.</dd>
<dt><code>-readconfig</code> <i>file</i></dt>
<dd> Read device configuration from <i>file</i>. This approach is useful when you want to spawn QEMU process with many command line options but you don&#8217;t want to exceed the command line character limit.</dd>
<dt><code>-writeconfig</code> <i>file</i></dt>
<dd> Write device configuration to <i>file</i>. The <i>file</i> can be either filename to save command line and device configuration into file or dash <tt>&quot;-&quot;</tt>) character to print the output to stdout. This can be later used as input file for <tt>&quot;-readconfig&quot;</tt> option.</dd>
<dt><code>-nodefconfig</code></dt>
<dd> Normally QEMU loads configuration files from <i>sysconfdir</i> and <i>datadir</i> at startup. The <tt>&quot;-nodefconfig&quot;</tt> option will prevent QEMU from loading any of those config files.</dd>
<dt><code>-no-user-config</code></dt>
<dd> The <tt>&quot;-no-user-config&quot;</tt> option makes QEMU not load any of the user-provided config files on <i>sysconfdir</i>, but won&#8217;t make it skip the QEMU-provided config files from <i>datadir</i>.</dd>
<dt><code>-trace [events=</code><i>file</i><code>][,file=</code><i>file</i><code>]</code></dt>
<dd> Specify tracing options.</dd>
<dl>
<dl>
<dt><code>events=</code><i>file</i></dt>
<dd> Immediately enable events listed in <i>file</i>. The file must contain one event name (as listed in the <i>trace-events</i> file) per line. This option is only available if QEMU has been compiled with either <i>simple</i> or <i>stderr</i> tracing backend.</dd>
<dt><code>file=</code><i>file</i></dt>
<dd> Log output traces to <i>file</i>. </dd>
<p> This option is only available if QEMU has been compiled with the <i>simple</i> tracing backend.</dl>
</dl>
<dl>
</dl>
<dt><code>-enable-fips</code></dt>
<dd> Enable FIPS 140-2 compliance mode.</dd>
<dt><code>-object</code> <i>typename</i><code>[,</code><i>prop1</i><code>=</code><i>value1</i><code>,&#8230;]</code></dt>
<dd> Create an new object of type <i>typename</i> setting properties in the order they are specified. Note that the &#8216;id&#8217; property must be set. These objects are placed in the &#8216;/objects&#8217; path.</dd>
<dt><code>-msg timestamp[=on|off]</code></dt>
<dd> prepend a timestamp to each log message.(default:on)</dd></dl>
<p> During the graphical emulation, you can use special key combinations to change modes. The default key mappings are shown below, but if you use <tt>&quot;-alt-grab&quot;</tt> then the modifier is Ctrl-Alt-Shift (instead of Ctrl-Alt) and if you use <tt>&quot;-ctrl-grab&quot;</tt> then the modifier is the right Ctrl key (instead of Ctrl-Alt):</p>
<dl>
<dt><code>Ctrl-Alt-f</code></dt>
<dd> Toggle full screen</dd>
<dt><code>Ctrl-Alt-+</code></dt>
<dd> Enlarge the screen</dd>
<dt><code>Ctrl-Alt&#8212;</code></dt>
<dd> Shrink the screen</dd>
<dt><code>Ctrl-Alt-u</code></dt>
<dd> Restore the screen&#8217;s un-scaled dimensions</dd>
<dt><code>Ctrl-Alt-n</code></dt>
<dd> Switch to virtual console &#8216;n&#8217;. Standard console mappings are:</dd>
<dl>
<dl>
<dt><i>1</i></dt>
<dd> Target system display</dd>
<dt><i>2</i></dt>
<dd> Monitor</dd>
<dt><i>3</i></dt>
<dd> Serial port</dd></dl>
</dl>
<dl>
</dl>
<dt><code>Ctrl-Alt</code></dt>
<dd> Toggle mouse and keyboard grab.</dd></dl>
<p> In the virtual consoles, you can use <code>Ctrl-Up</code>, <code>Ctrl-Down</code>, <code>Ctrl-PageUp</code> and <code>Ctrl-PageDown</code> to move in the back log. </p>
<p> During emulation, if you are using the <code>-nographic</code> option, use <code>Ctrl-a h</code> to get terminal commands:</p>
<dl>
<dt><code>Ctrl-a h</code></dt>
<dd>
</dd><dt><code>Ctrl-a ?</code></dt>
<dd> Print this help</dd>
<dt><code>Ctrl-a x</code></dt>
<dd> Exit emulator</dd>
<dt><code>Ctrl-a s</code></dt>
<dd> Save disk data back to file (if -snapshot)</dd>
<dt><code>Ctrl-a t</code></dt>
<dd> Toggle console timestamps</dd>
<dt><code>Ctrl-a b</code></dt>
<dd> Send break (magic sysrq in Linux)</dd>
<dt><code>Ctrl-a c</code></dt>
<dd> Switch between console and monitor</dd>
<dt><code>Ctrl-a Ctrl-a</code></dt>
<dd> Send Ctrl-a</dd></dl>
<p> The following options are specific to the PowerPC emulation:</p>
<dl>
<dt><code>-g</code> <i>W</i><code>x</code><i>H</i><code>[x</code><i></i><i>DEPTH</i><i></i><code>]</code></dt>
<dd> Set the initial VGA graphic mode. The default is 800x600x32.</dd>
<dt><code>-prom-env</code> <i>string</i></dt>
<dd> Set OpenBIOS variables in NVRAM, for example: </dd>
<pre>
        qemu-system-ppc -prom-env 'auto-boot?=false' \
         -prom-env 'boot-device=hd:2,\yaboot' \
         -prom-env 'boot-args=conf=hd:2,\yaboot.conf'
</pre>
<p> These variables are not used by Open Hack&#8217;Ware.</dl>
<p> The following options are specific to the Sparc32 emulation:</p>
<dl>
<dt><code>-g</code> <i>W</i><code>x</code><i>H</i><code>x[x</code><i></i><i>DEPTH</i><i></i><code>]</code></dt>
<dd> Set the initial graphics mode. For TCX, the default is 1024x768x8 with the option of 1024x768x24. For cgthree, the default is 1024x768x8 with the option of 1152x900x8 for people who wish to use OBP.</dd>
<dt><code>-prom-env</code> <i>string</i></dt>
<dd> Set OpenBIOS variables in NVRAM, for example: </dd>
<pre>
        qemu-system-sparc -prom-env 'auto-boot?=false' \
         -prom-env 'boot-device=sd(0,2,0):d' -prom-env 'boot-args=linux single'
</pre>
<dt><code>-M [SS-4|SS-5|SS-10|SS-20|SS-600MP|LX|Voyager|SPARCClassic] [|SPARCbook]</code></dt>
<dd> Set the emulated machine type. Default is SS-5.</dd></dl>
<p> The following options are specific to the Sparc64 emulation:</p>
<dl>
<dt><code>-prom-env</code> <i>string</i></dt>
<dd> Set OpenBIOS variables in NVRAM, for example: </dd>
<pre>
        qemu-system-sparc64 -prom-env 'auto-boot?=false'
</pre>
<dt><code>-M [sun4u|sun4v|Niagara]</code></dt>
<dd> Set the emulated machine type. The default is sun4u.</dd></dl>
<h2>SEE ALSO</h2>
<p> The HTML documentation of QEMU for more precise information and Linux user mode emulator invocation.</p>
<h2>AUTHOR</h2>
<p> Fabrice Bellard </p>
