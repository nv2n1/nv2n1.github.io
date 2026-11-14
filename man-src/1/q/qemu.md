---
title: "qemu(1)"
name: "qemu"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qemu/"
description: "qemu-doc – QEMU Emulator User Documentation"
---

<h2 class="name">NAME</h2>
<p> qemu-doc &#8211; QEMU Emulator User Documentation </p>
<h2>SYNOPSIS</h2>
<p> usage: qemu-system-i386 [options] [<i>disk_image</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <font SIZE="-1">QEMU PC</font> System emulator simulates the following peripherals:</p>
<dl>
<dt>&#8211;</p>
<dd> i440FX host <font SIZE="-1">PCI</font> bridge and <font SIZE="-1">PIIX3 PCI</font> to <font SIZE="-1">ISA</font> bridge</p>
<dt>&#8211;</p>
<dd> Cirrus <font SIZE="-1">CLGD 5446 PCI VGA</font> card or dummy <font SIZE="-1">VGA</font> card with Bochs <font SIZE="-1">VESA</font> extensions (hardware level, including all non standard modes).</p>
<dt>&#8211;</p>
<dd> <font SIZE="-1">PS/2</font> mouse and keyboard</p>
<dt>&#8211;</p>
<dd> 2 <font SIZE="-1">PCI IDE</font> interfaces with hard disk and CD-ROM support</p>
<dt>&#8211;</p>
<dd> Floppy disk</p>
<dt>&#8211;</p>
<dd> <font SIZE="-1">PCI</font> and <font SIZE="-1">ISA</font> network adapters</p>
<dt>&#8211;</p>
<dd> Serial ports</p>
<dt>&#8211;</p>
<dd> Creative SoundBlaster 16 sound card</p>
<dt>&#8211;</p>
<dd> <font SIZE="-1">ENSONIQ</font> AudioPCI <font SIZE="-1">ES1370</font> sound card</p>
<dt>&#8211;</p>
<dd> Intel 82801AA <font SIZE="-1">AC97</font> Audio compatible sound card</p>
<dt>&#8211;</p>
<dd> Intel <font SIZE="-1">HD</font> Audio Controller and <font SIZE="-1">HDA</font> codec</p>
<dt>&#8211;</p>
<dd> Adlib (<font SIZE="-1">OPL2</font>) &#8211; Yamaha <font SIZE="-1">YM3812</font> compatible chip</p>
<dt>&#8211;</p>
<dd> Gravis Ultrasound <font SIZE="-1">GF1</font> sound card</p>
<dt>&#8211;</p>
<dd> <font SIZE="-1">CS4231A</font> compatible sound card</p>
<dt>&#8211;</p>
<dd> <font SIZE="-1">PCI UHCI USB</font> controller and a virtual <font SIZE="-1">USB</font> hub.</dl>
<p> <font SIZE="-1">SMP</font> is supported with up to 255 CPUs. </p>
<p> <font SIZE="-1">QEMU</font> uses the <font SIZE="-1">PC BIOS</font> from the Seabios project and the Plex86/Bochs <font SIZE="-1">LGPL VGA BIOS.</font> </p>
<p> <font SIZE="-1">QEMU</font> uses <font SIZE="-1">YM3812</font> emulation by Tatsuyuki Satoh. </p>
<p> <font SIZE="-1">QEMU</font> uses <font SIZE="-1">GUS</font> emulation (<font SIZE="-1">GUSEMU32</font> &lt;<code><a rel="nofollow" href="http://www.deinmeister.de/gusemu/">http://www.deinmeister.de/gusemu/</a></code>&gt;) by Tibor &#8220;<font SIZE="-1">TS&#8221;</font> Schütz. </p>
<p> Note that, by default, <font SIZE="-1">GUS</font> shares <font SIZE="-1"><i><a href="/docs/linux/man/7-irq/">IRQ</a></i></font><i></i>(7) with parallel ports and so <font SIZE="-1">QEMU</font> must be told to not have parallel ports to have working <font SIZE="-1">GUS.</font> </p>
<pre>
        qemu-system-i386 dos.img -soundhw gus -parallel none
</pre>
<p> Alternatively: </p>
<pre>
        qemu-system-i386 dos.img -device gus,irq=5
</pre>
<p> Or some other unclaimed <font SIZE="-1">IRQ.</font> </p>
<p> <font SIZE="-1">CS4231A</font> is the chip used in Windows Sound System and <font SIZE="-1">GUSMAX</font> products</p>
<h2>OPTIONS</h2>
<p> <i>disk_image</i> is a raw hard disk image for <font SIZE="-1">IDE</font> hard disk 0. Some targets do not need a disk image. </p>
<p> Standard options:</p>
<dl>
<dt><code>-h</code></p>
<dd> Display help and exit</p>
<dt><code>-version</code></p>
<dd> Display version information and exit</p>
<dt><code>-machine [type=]</code><i>name</i><code>[,prop=</code><i>value</i><code>[,&#8230;]]</code></p>
<dd> Select the emulated machine by <i>name</i>. Use <tt>&quot;-machine help&quot;</tt> to list available machines. Supported machine properties are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>accel=</code><i>accels1</i><code>[:</code><i>accels2</i><code>[:&#8230;]]</code></p>
<dd> This is used to enable an accelerator. Depending on the target architecture, kvm, xen, or tcg can be available. By default, tcg is used. If there is more than one accelerator specified, the next one is used if the previous one fails to initialize.</p>
<dt><code>kernel_irqchip=on|off</code></p>
<dd> Enables in-kernel irqchip support for the chosen accelerator when available.</p>
<dt><code>kvm_shadow_mem=size</code></p>
<dd> Defines the size of the <font SIZE="-1">KVM</font> shadow <font SIZE="-1">MMU.</font></p>
<dt><code>dump-guest-core=on|off</code></p>
<dd> Include guest memory in a core dump. The default is on.</p>
<dt><code>mem-merge=on|off</code></p>
<dd> Enables or disables memory merge support. This feature, when supported by the host, de-duplicates identical memory pages among VMs instances (enabled by default).</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-cpu</code> <i>model</i></p>
<dd> Select <font SIZE="-1">CPU</font> model (<tt>&quot;-cpu help&quot;</tt> for list and additional feature selection)</p>
<dt><code>-smp [cpus=]</code><i>n</i><code>[,cores=</code><i>cores</i><code>][,threads=</code><i>threads</i><code>][,sockets=</code><i>sockets</i><code>][,maxcpus=</code><i>maxcpus</i><code>]</code></p>
<dd> Simulate an <font SIZE="-1">SMP</font> system with <i>n</i> CPUs. On the <font SIZE="-1">PC</font> target, up to 255 CPUs are supported. On Sparc32 target, Linux limits the number of usable CPUs to 4. For the <font SIZE="-1">PC</font> target, the number of <i>cores</i> per socket, the number of <i>threads</i> per cores and the total number of <i>sockets</i> can be specified. Missing values will be computed. If any on the three values is given, the total number of CPUs <i>n</i> can be omitted. <i>maxcpus</i> specifies the maximum number of hotpluggable CPUs.</p>
<dt><code>-numa</code> <i>opts</i></p>
<dd> Simulate a multi node <font SIZE="-1">NUMA</font> system. If mem and cpus are omitted, resources are split equally.</p>
<dt><code>-add-fd fd=</code><i>fd</i><code>,set=</code><i>set</i><code>[,opaque=</code><i>opaque</i><code>]</code></p>
<dd> Add a file descriptor to an fd set. Valid options are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>fd=</code><i>fd</i></p>
<dd> This option defines the file descriptor of which a duplicate is added to fd set. The file descriptor cannot be stdin, stdout, or stderr.</p>
<dt><code>set=</code><i>set</i></p>
<dd> This option defines the <font SIZE="-1">ID</font> of the fd set to add the file descriptor to.</p>
<dt><code>opaque=</code><i>opaque</i></p>
<dd> This option defines a free-form string that can be used to describe <i>fd</i>.</dl>
</dl>
<dl>
<dt>
<dd>
<p> You can open an image using pre-opened file descriptors from an fd set: </p>
<pre>
        qemu-system-i386
        -add-fd fd=3,set=2,opaque=&quot;rdwr:/path/to/file&quot;
        -add-fd fd=4,set=2,opaque=&quot;rdonly:/path/to/file&quot;
        -drive file=/dev/fdset/2,index=0,media=disk
</pre>
</dl>
<dt><code>-set</code> <i>group</i><code>.</code><i>id</i><code>.</code><i>arg</i><code>=</code><i>value</i></p>
<dd> Set parameter <i>arg</i> for item <i>id</i> of type <i>group</i>
&quot;</p>
<dt><code>-global</code> <i>driver</i><code>.</code><i>prop</i><code>=</code><i>value</i></p>
<dd> Set default value of <i>driver</i>&#8216;s property <i>prop</i> to <i>value</i>, e.g.: </p>
<pre>
        qemu-system-i386 -global ide-drive.physical_block_size=4096 -drive file=file,if=ide,index=0,media=disk
</pre>
<p> In particular, you can use this to set driver properties for devices which are created automatically by the machine model. To create a device which is not created automatically and set properties on it, use &#8211;<code>device</code>.</p>
<dt><code>-boot [order=</code><i>drives</i><code>][,once=</code><i>drives</i><code>][,menu=on|off][,splash=</code><i>sp_name</i><code>][,splash-time=</code><i>sp_time</i><code>][,reboot-timeout=</code><i>rb_timeout</i><code>][,strict=on|off]</code></p>
<dd> Specify boot order <i>drives</i> as a string of drive letters. Valid drive letters depend on the target achitecture. The x86 <font SIZE="-1">PC</font> uses: a, b (floppy 1 and 2), c (first hard disk), d (first CD-ROM), n-p (Etherboot from network adapter 1-4), hard disk boot is the default. To apply a particular boot order only on the first startup, specify it via <code>once</code>. </p>
<p> Interactive boot menus/prompts can be enabled via <code>menu=on</code> as far as firmware/BIOS supports them. The default is non-interactive boot. </p>
<p> A splash picture could be passed to bios, enabling user to show it as logo, when option splash=<i>sp_name</i> is given and menu=on, If firmware/BIOS supports them. Currently Seabios for X86 system support it. limitation: The splash file could be a jpeg file or a <font SIZE="-1">BMP</font> file in 24 <font SIZE="-1">BPP</font> format(true color). The resolution should be supported by the <font SIZE="-1">SVGA</font> mode, so the recommended is 320&#215;240, 640&#215;480, 800&#215;640. </p>
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
<dt><code>-m</code> <i>megs</i></p>
<dd> Set virtual <font SIZE="-1">RAM</font> size to <i>megs</i> megabytes. Default is 128 MiB. Optionally, a suffix of &#8220;M&#8221; or &#8220;G&#8221; can be used to signify a value in megabytes or gigabytes respectively.</p>
<dt><code>-mem-path</code> <i>path</i></p>
<dd> Allocate guest <font SIZE="-1">RAM</font> from a temporarily created file in <i>path</i>.</p>
<dt><code>-mem-prealloc</code></p>
<dd> Preallocate memory when using -mem-path.</p>
<dt><code>-k</code> <i>language</i></p>
<dd> Use keyboard layout <i>language</i> (for example <tt>&quot;fr&quot;</tt> for French). This option is only needed where it is not easy to get raw <font SIZE="-1">PC</font> keycodes (e.g. on Macs, with some X11 servers or with a <font SIZE="-1">VNC</font> display). You don&#8217;t normally need to use it on PC/Linux or PC/Windows hosts. </p>
<p> The available layouts are: </p>
<pre>
        ar  de-ch  es  fo     fr-ca  hu  ja  mk     no  pt-br  sv
        da  en-gb  et  fr     fr-ch  is  lt  nl     pl  ru     th
        de  en-us  fi  fr-be  hr     it  lv  nl-be  pt  sl     tr
</pre>
<p> The default is <tt>&quot;en-us&quot;</tt>.</p>
<dt><code>-audio-help</code></p>
<dd> Will show the audio subsystem help: list of drivers, tunable parameters.</p>
<dt><code>-soundhw</code> <i>card1</i><code>[,</code><i>card2</i><code>,&#8230;] or -soundhw all</code></p>
<dd> Enable audio and selected sound hardware. Use &#8216;help&#8217; to print all available sound hardware. </p>
<pre>
        qemu-system-i386 -soundhw sb16,adlib disk.img
        qemu-system-i386 -soundhw es1370 disk.img
        qemu-system-i386 -soundhw ac97 disk.img
        qemu-system-i386 -soundhw hda disk.img
        qemu-system-i386 -soundhw all disk.img
        qemu-system-i386 -soundhw help
</pre>
<p> Note that Linux&#8217;s i810_audio <font SIZE="-1">OSS</font> kernel (for <font SIZE="-1">AC97</font>) module might require manually specifying clocking. </p>
<pre>
        modprobe i810_audio clocking=48000
</pre>
<dt><code>-balloon none</code></p>
<dd> Disable balloon device.</p>
<dt><code>-balloon virtio[,addr=</code><i>addr</i><code>]</code></p>
<dd> Enable virtio balloon device (default), optionally with <font SIZE="-1">PCI</font> address <i>addr</i>.</p>
<dt><code>-device</code> <i>driver</i><code>[,</code><i>prop</i><code>[=</code><i>value</i><code>][,&#8230;]]</code></p>
<dd> Add device <i>driver</i>. <i>prop</i>=<i>value</i> sets driver properties. Valid properties depend on the driver. To get help on possible drivers and properties, use <tt>&quot;-device help&quot;</tt> and <tt>&quot;-device </tt>driver<tt>,help&quot;</tt>.</p>
<dt><code>-name</code> <i>name</i></p>
<dd> Sets the <i>name</i> of the guest. This name will be displayed in the <font SIZE="-1">SDL</font> window caption. The <i>name</i> will also be used for the <font SIZE="-1">VNC</font> server. Also optionally set the top visible process name in Linux. Naming of individual threads can also be enabled on Linux to aid debugging.</p>
<dt><code>-uuid</code> <i>uuid</i></p>
<dd> Set system <font SIZE="-1">UUID.</font></dl>
<p> Block device options:</p>
<dl>
<dt><code>-fda</code> <i>file</i></p>
<dd>
<dt><code>-fdb</code> <i>file</i></p>
<dd> Use <i>file</i> as floppy disk 0/1 image. You can use the host floppy by using <i>/dev/fd0</i> as filename.</p>
<dt><code>-hda</code> <i>file</i></p>
<dd>
<dt><code>-hdb</code> <i>file</i></p>
<dd>
<dt><code>-hdc</code> <i>file</i></p>
<dd>
<dt><code>-hdd</code> <i>file</i></p>
<dd> Use <i>file</i> as hard disk 0, 1, 2 or 3 image.</p>
<dt><code>-cdrom</code> <i>file</i></p>
<dd> Use <i>file</i> as CD-ROM image (you cannot use <code>-hdc</code> and <code>-cdrom</code> at the same time). You can use the host CD-ROM by using <i>/dev/cdrom</i> as filename.</p>
<dt><code>-drive</code> <i>option</i><code>[,</code><i>option</i><code>[,</code><i>option</i><code>[,&#8230;]]]</code></p>
<dd> Define a new drive. Valid options are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>file=</code><i>file</i></p>
<dd> This option defines which disk image to use with this drive. If the filename contains comma, you must double it (for instance, &#8220;file=my,,file&#8221; to use file &#8220;my,file&#8221;). </p>
<p> Special files such as iSCSI devices can be specified using protocol specific URLs. See the section for &#8220;Device <font SIZE="-1">URL</font> Syntax&#8221; for more information.</p>
<dt><code>if=</code><i>interface</i></p>
<dd> This option defines on which type on interface the drive is connected. Available types are: ide, scsi, sd, mtd, floppy, pflash, virtio.</p>
<dt><code>bus=</code><i>bus</i><code>,unit=</code><i>unit</i></p>
<dd> These options define where is connected the drive by defining the bus number and the unit id.</p>
<dt><code>index=</code><i>index</i></p>
<dd> This option defines where is connected the drive by using an index in the list of available connectors of a given interface type.</p>
<dt><code>media=</code><i>media</i></p>
<dd> This option defines the type of the media: disk or cdrom.</p>
<dt><code>cyls=</code><i>c</i><code>,heads=</code><i>h</i><code>,secs=</code><i>s</i><code>[,trans=</code><i>t</i><code>]</code></p>
<dd> These options have the same definition as they have in <code>-hdachs</code>.</p>
<dt><code>snapshot=</code><i>snapshot</i></p>
<dd> <i>snapshot</i> is &#8220;on&#8221; or &#8220;off&#8221; and allows to enable snapshot for given drive (see <code>-snapshot</code>).</p>
<dt><code>cache=</code><i>cache</i></p>
<dd> <i>cache</i> is &#8220;none&#8221;, &#8220;writeback&#8221;, &#8220;unsafe&#8221;, &#8220;directsync&#8221; or &#8220;writethrough&#8221; and controls how the host cache is used to access block data.</p>
<dt><code>aio=</code><i>aio</i></p>
<dd> <i>aio</i> is &#8220;threads&#8221;, or &#8220;native&#8221; and selects between pthread based disk I/O and native Linux <font SIZE="-1">AIO.</font></p>
<dt><code>discard=</code><i>discard</i></p>
<dd> <i>discard</i> is one of &#8220;ignore&#8221; (or &#8220;off&#8221;) or &#8220;unmap&#8221; (or &#8220;on&#8221;) and controls whether <i>discard</i> (also known as <i>trim</i> or <i>unmap</i>) requests are ignored or passed to the filesystem. Some machine types may not support discard requests.</p>
<dt><code>format=</code><i>format</i></p>
<dd> Specify which disk <i>format</i> will be used rather than detecting the format. Can be used to specifiy format=raw to avoid interpreting an untrusted format header.</p>
<dt><code>serial=</code><i>serial</i></p>
<dd> This option specifies the serial number to assign to the device.</p>
<dt><code>addr=</code><i>addr</i></p>
<dd> Specify the controller&#8217;s <font SIZE="-1">PCI</font> address (if=virtio only).</p>
<dt><code>werror=</code><i>action</i><code>,rerror=</code><i>action</i></p>
<dd> Specify which <i>action</i> to take on write and read errors. Valid actions are: &#8220;ignore&#8221; (ignore the error and try to continue), &#8220;stop&#8221; (pause <font SIZE="-1">QEMU</font>), &#8220;report&#8221; (report the error to the guest), &#8220;enospc&#8221; (pause <font SIZE="-1">QEMU</font> only if the host disk is full; report the error to the guest otherwise). The default setting is <code>werror=enospc</code> and <code>rerror=report</code>.</p>
<dt><code>readonly</code></p>
<dd> Open drive <code>file</code> as read-only. Guest write attempts will fail.</p>
<dt><code>copy-on-read=</code><i>copy-on-read</i></p>
<dd> <i>copy-on-read</i> is &#8220;on&#8221; or &#8220;off&#8221; and enables whether to copy read backing file sectors into the image file.</dl>
</dl>
<dl>
<dt>
<dd>
<p> By default, the <code>cache=writeback</code> mode is used. It will report data writes as completed as soon as the data is present in the host page cache. This is safe as long as your guest <font SIZE="-1">OS</font> makes sure to correctly flush disk caches where needed. If your guest <font SIZE="-1">OS</font> does not handle volatile disk write caches correctly and your host crashes or loses power, then the guest may experience data corruption. </p>
<p> For such guests, you should consider using <code>cache=writethrough</code>. This means that the host page cache will be used to read and write data, but write notification will be sent to the guest only after <font SIZE="-1">QEMU</font> has made sure to flush each write to the disk. Be aware that this has a major impact on performance. </p>
<p> The host page cache can be avoided entirely with <code>cache=none</code>. This will attempt to do disk <font SIZE="-1">IO</font> directly to the guest&#8217;s memory. <font SIZE="-1">QEMU</font> may still perform an internal copy of the data. Note that this is considered a writeback mode and the guest <font SIZE="-1">OS</font> must handle the disk write cache correctly in order to avoid data corruption on host crashes. </p>
<p> The host page cache can be avoided while only sending write notifications to the guest when the data has been flushed to the disk using <code>cache=directsync</code>. </p>
<p> In case you don&#8217;t care about data integrity over host failures, use <code>cache=unsafe</code>. This option tells <font SIZE="-1">QEMU</font> that it never needs to write any data to the disk but can instead keep things in cache. If anything goes wrong, like your host losing power, the disk storage getting disconnected accidentally, etc. your image will most probably be rendered unusable. When using the <code>-snapshot</code> option, unsafe caching is always used. </p>
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
<p> You can connect a <font SIZE="-1">CDROM</font> to the slave of ide0: </p>
<pre>
        qemu-system-i386 -drive file=file,if=ide,index=1,media=cdrom
</pre>
<p> If you don&#8217;t specify the &#8220;file=&#8221; argument, you define an empty drive: </p>
<pre>
        qemu-system-i386 -drive if=ide,index=1,media=cdrom
</pre>
<p> You can connect a <font SIZE="-1">SCSI</font> disk with unit <font SIZE="-1">ID 6</font> on the bus #0: </p>
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
</dl>
<dt><code>-mtdblock</code> <i>file</i></p>
<dd> Use <i>file</i> as on-board Flash memory image.</p>
<dt><code>-sd</code> <i>file</i></p>
<dd> Use <i>file</i> as SecureDigital card image.</p>
<dt><code>-pflash</code> <i>file</i></p>
<dd> Use <i>file</i> as a parallel flash image.</p>
<dt><code>-snapshot</code></p>
<dd> Write to temporary files instead of disk image files. In this case, the raw disk image you use is not written back. You can however force the write back by pressing <code>C-a s</code>.</p>
<dt><code>-hdachs</code> <i>c</i><code>,</code><i>h</i><code>,</code><i>s</i><code>,[,</code><i>t</i><code>]</code></p>
<dd> Force hard disk 0 physical geometry (1 &lt;= <i>c</i> &lt;= 16383, 1 &lt;= <i>h</i> &lt;= 16, 1 &lt;= <i>s</i> &lt;= 63) and optionally force the <font SIZE="-1">BIOS</font> translation mode (<i>t</i>=none, lba or auto). Usually <font SIZE="-1">QEMU</font> can guess all those parameters. This option is useful for old MS-DOS disk images.</p>
<dt><code>-fsdev</code> <i>fsdriver</i><code>,id=</code><i>id</i><code>,path=</code><i>path</i><code>,[security_model=</code><i>security_model</i><code>][,writeout=</code><i>writeout</i><code>][,readonly][,socket=</code><i>socket</i><code>|sock_fd=</code><i>sock_fd</i><code>]</code></p>
<dd> Define a new file system device. Valid options are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>fsdriver</i></p>
<dd> This option specifies the fs driver backend to use. Currently &#8220;local&#8221;, &#8220;handle&#8221; and &#8220;proxy&#8221; file system drivers are supported.</p>
<dt><code>id=</code><i>id</i></p>
<dd> Specifies identifier for this device</p>
<dt><code>path=</code><i>path</i></p>
<dd> Specifies the export path for the file system device. Files under this path will be available to the 9p client on the guest.</p>
<dt><code>security_model=</code><i>security_model</i></p>
<dd> Specifies the security model to be used for this export path. Supported security models are &#8220;passthrough&#8221;, &#8220;mapped-xattr&#8221;, &#8220;mapped-file&#8221; and &#8220;none&#8221;. In &#8220;passthrough&#8221; security model, files are stored using the same credentials as they are created on the guest. This requires <font SIZE="-1">QEMU</font> to run as root. In &#8220;mapped-xattr&#8221; security model, some of the file attributes like uid, gid, mode bits and link target are stored as file attributes. For &#8220;mapped-file&#8221; these attributes are stored in the hidden .virtfs_metadata directory. Directories exported by this security model cannot interact with other unix tools. &#8220;none&#8221; security model is same as passthrough except the sever won&#8217;t report failures if it fails to set file attributes like ownership. Security model is mandatory only for local fsdriver. Other fsdrivers (like handle, proxy) don&#8217;t take security model as a parameter.</p>
<dt><code>writeout=</code><i>writeout</i></p>
<dd> This is an optional argument. The only supported value is &#8220;immediate&#8221;. This means that host page cache will be used to read and write data but write notification will be sent to the guest only when the data has been reported as written by the storage subsystem.</p>
<dt><code>readonly</code></p>
<dd> Enables exporting 9p share as a readonly mount for guests. By default read-write access is given.</p>
<dt><code>socket=</code><i>socket</i></p>
<dd> Enables proxy filesystem driver to use passed socket file for communicating with virtfs-proxy-helper</p>
<dt><code>sock_fd=</code><i>sock_fd</i></p>
<dd> Enables proxy filesystem driver to use passed socket descriptor for communicating with virtfs-proxy-helper. Usually a helper like libvirt will create socketpair and pass one of the fds as sock_fd</dl>
</dl>
<dl>
<dt>
<dd>
<p> -fsdev option is used along with -device driver &#8220;virtio-9p-pci&#8221;.</dl>
<dt><code>-device virtio-9p-pci,fsdev=</code><i>id</i><code>,mount_tag=</code><i>mount_tag</i></p>
<dd> Options for virtio-9p-pci driver are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>fsdev=</code><i>id</i></p>
<dd> Specifies the id value specified along with -fsdev option</p>
<dt><code>mount_tag=</code><i>mount_tag</i></p>
<dd> Specifies the tag name to be used by the guest to mount this export point</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-virtfs</code> <i>fsdriver</i><code>[,path=</code><i>path</i><code>],mount_tag=</code><i>mount_tag</i><code>[,security_model=</code><i>security_model</i><code>][,writeout=</code><i>writeout</i><code>][,readonly][,socket=</code><i>socket</i><code>|sock_fd=</code><i>sock_fd</i><code>]</code></p>
<dd> The general form of a Virtual File system pass-through options are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>fsdriver</i></p>
<dd> This option specifies the fs driver backend to use. Currently &#8220;local&#8221;, &#8220;handle&#8221; and &#8220;proxy&#8221; file system drivers are supported.</p>
<dt><code>id=</code><i>id</i></p>
<dd> Specifies identifier for this device</p>
<dt><code>path=</code><i>path</i></p>
<dd> Specifies the export path for the file system device. Files under this path will be available to the 9p client on the guest.</p>
<dt><code>security_model=</code><i>security_model</i></p>
<dd> Specifies the security model to be used for this export path. Supported security models are &#8220;passthrough&#8221;, &#8220;mapped-xattr&#8221;, &#8220;mapped-file&#8221; and &#8220;none&#8221;. In &#8220;passthrough&#8221; security model, files are stored using the same credentials as they are created on the guest. This requires <font SIZE="-1">QEMU</font> to run as root. In &#8220;mapped-xattr&#8221; security model, some of the file attributes like uid, gid, mode bits and link target are stored as file attributes. For &#8220;mapped-file&#8221; these attributes are stored in the hidden .virtfs_metadata directory. Directories exported by this security model cannot interact with other unix tools. &#8220;none&#8221; security model is same as passthrough except the sever won&#8217;t report failures if it fails to set file attributes like ownership. Security model is mandatory only for local fsdriver. Other fsdrivers (like handle, proxy) don&#8217;t take security model as a parameter.</p>
<dt><code>writeout=</code><i>writeout</i></p>
<dd> This is an optional argument. The only supported value is &#8220;immediate&#8221;. This means that host page cache will be used to read and write data but write notification will be sent to the guest only when the data has been reported as written by the storage subsystem.</p>
<dt><code>readonly</code></p>
<dd> Enables exporting 9p share as a readonly mount for guests. By default read-write access is given.</p>
<dt><code>socket=</code><i>socket</i></p>
<dd> Enables proxy filesystem driver to use passed socket file for communicating with virtfs-proxy-helper. Usually a helper like libvirt will create socketpair and pass one of the fds as sock_fd</p>
<dt><code>sock_fd</code></p>
<dd> Enables proxy filesystem driver to use passed &#8216;sock_fd&#8217; as the socket descriptor for interfacing with virtfs-proxy-helper</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-virtfs_synth</code></p>
<dd> Create synthetic file system image</dl>
<p> <font SIZE="-1">USB</font> options:</p>
<dl>
<dt><code>-usb</code></p>
<dd> Enable the <font SIZE="-1">USB</font> driver (will be the default soon)</p>
<dt><code>-usbdevice</code> <i>devname</i></p>
<dd> Add the <font SIZE="-1">USB</font> device <i>devname</i>.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>mouse</code></p>
<dd> Virtual Mouse. This will override the <font SIZE="-1">PS/2</font> mouse emulation when activated.</p>
<dt><code>tablet</code></p>
<dd> Pointer device that uses absolute coordinates (like a touchscreen). This means <font SIZE="-1">QEMU</font> is able to report the mouse position without having to grab the mouse. Also overrides the <font SIZE="-1">PS/2</font> mouse emulation when activated.</p>
<dt><code>disk:[format=</code><i>format</i><code>]:</code><i>file</i></p>
<dd> Mass storage device based on file. The optional <i>format</i> argument will be used rather than detecting the format. Can be used to specifiy <tt>&quot;format=raw&quot;</tt> to avoid interpreting an untrusted format header.</p>
<dt><code>host:</code><i>bus</i><code>.</code><i>addr</i></p>
<dd> Pass through the host device identified by <i>bus</i>.<i>addr</i> (Linux only).</p>
<dt><code>host:</code><i>vendor_id</i><code>:</code><i>product_id</i></p>
<dd> Pass through the host device identified by <i>vendor_id</i>:<i>product_id</i> (Linux only).</p>
<dt><code>serial:[vendorid=</code><i>vendor_id</i><code>][,productid=</code><i>product_id</i><code>]:</code><i>dev</i></p>
<dd> Serial converter to host character device <i>dev</i>, see <tt>&quot;-serial&quot;</tt> for the available devices.</p>
<dt><code>braille</code></p>
<dd> Braille device. This will use BrlAPI to display the braille output on a real or fake device.</p>
<dt><code>net:</code><i>options</i></p>
<dd> Network adapter that supports <font SIZE="-1">CDC</font> ethernet and <font SIZE="-1">RNDIS</font> protocols.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<p> Display options:</p>
<dl>
<dt><code>-display</code> <i>type</i></p>
<dd> Select type of display to use. This option is a replacement for the old style -sdl/-curses/&#8230; options. Valid values for <i>type</i> are</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>sdl</code></p>
<dd> Display video output via <font SIZE="-1">SDL </font>(usually in a separate graphics window; see the <font SIZE="-1">SDL</font> documentation for other possibilities).</p>
<dt><code>curses</code></p>
<dd> Display video output via curses. For graphics device models which support a text mode, <font SIZE="-1">QEMU</font> can display this output using a curses/ncurses interface. Nothing is displayed when the graphics device is in graphical mode or if the graphics device does not support a text mode. Generally only the <font SIZE="-1">VGA</font> device models support text mode.</p>
<dt><code>none</code></p>
<dd> Do not display video output. The guest will still see an emulated graphics card, but its output will not be displayed to the <font SIZE="-1">QEMU</font> user. This option differs from the -nographic option in that it only affects what is done with video output; -nographic also changes the destination of the serial and parallel port data.</p>
<dt><code>gtk</code></p>
<dd> Display video output in a <font SIZE="-1">GTK</font> window. This interface provides drop-down menus and other <font SIZE="-1">UI</font> elements to configure and control the <font SIZE="-1">VM</font> during runtime.</p>
<dt><code>vnc</code></p>
<dd> Start a <font SIZE="-1">VNC</font> server on display &lt;arg&gt;</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-nographic</code></p>
<dd> Normally, <font SIZE="-1">QEMU</font> uses <font SIZE="-1">SDL</font> to display the <font SIZE="-1">VGA</font> output. With this option, you can totally disable graphical output so that <font SIZE="-1">QEMU</font> is a simple command line application. The emulated serial port is redirected on the console and muxed with the monitor (unless redirected elsewhere explicitly). Therefore, you can still use <font SIZE="-1">QEMU</font> to debug a Linux kernel with a serial console. Use <code>C-a h</code> for help on switching between the console and monitor.</p>
<dt><code>-curses</code></p>
<dd> Normally, <font SIZE="-1">QEMU</font> uses <font SIZE="-1">SDL</font> to display the <font SIZE="-1">VGA</font> output. With this option, <font SIZE="-1">QEMU</font> can display the <font SIZE="-1">VGA</font> output when in text mode using a curses/ncurses interface. Nothing is displayed in graphical mode.</p>
<dt><code>-no-frame</code></p>
<dd> Do not use decorations for <font SIZE="-1">SDL</font> windows and start them using the whole available screen space. This makes the using <font SIZE="-1">QEMU</font> in a dedicated desktop workspace more convenient.</p>
<dt><code>-alt-grab</code></p>
<dd> Use Ctrl-Alt-Shift to grab mouse (instead of Ctrl-Alt). Note that this also affects the special keys (for fullscreen, monitor-mode switching, etc).</p>
<dt><code>-ctrl-grab</code></p>
<dd> Use Right-Ctrl to grab mouse (instead of Ctrl-Alt). Note that this also affects the special keys (for fullscreen, monitor-mode switching, etc).</p>
<dt><code>-no-quit</code></p>
<dd> Disable <font SIZE="-1">SDL</font> window close capability.</p>
<dt><code>-sdl</code></p>
<dd> Enable <font SIZE="-1">SDL.</font></p>
<dt><code>-spice</code> <i>option</i><code>[,</code><i>option</i><code>[,&#8230;]]</code></p>
<dd> Enable the spice remote desktop protocol. Valid options are</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>port=&lt;nr&gt;</code></p>
<dd> Set the <font SIZE="-1">TCP</font> port spice is listening on for plaintext channels.</p>
<dt><code>addr=&lt;addr&gt;</code></p>
<dd> Set the <font SIZE="-1">IP</font> address spice is listening on. Default is any address.</p>
<dt><code>ipv4</code></p>
<dd>
<dt><code>ipv6</code></p>
<dd> Force using the specified <font SIZE="-1">IP</font> version.</p>
<dt><code>password=&lt;secret&gt;</code></p>
<dd> Set the password you need to authenticate.</p>
<dt><code>sasl</code></p>
<dd> Require that the client use <font SIZE="-1">SASL</font> to authenticate with the spice. The exact choice of authentication method used is controlled from the system / user&#8217;s <font SIZE="-1">SASL</font> configuration file for the &#8216;qemu&#8217; service. This is typically found in /etc/sasl2/qemu.conf. If running <font SIZE="-1">QEMU</font> as an unprivileged user, an environment variable <font SIZE="-1">SASL_CONF_PATH</font> can be used to make it search alternate locations for the service config. While some <font SIZE="-1">SASL</font> auth methods can also provide data encryption (eg <font SIZE="-1">GSSAPI</font>), it is recommended that <font SIZE="-1">SASL</font> always be combined with the &#8216;tls&#8217; and &#8216;x509&#8217; settings to enable use of <font SIZE="-1">SSL</font> and server certificates. This ensures a data encryption preventing compromise of authentication credentials.</p>
<dt><code>disable-ticketing</code></p>
<dd> Allow client connects without authentication.</p>
<dt><code>disable-copy-paste</code></p>
<dd> Disable copy paste between the client and the guest.</p>
<dt><code>disable-agent-file-xfer</code></p>
<dd> Disable spice-vdagent based file-xfer between the client and the guest.</p>
<dt><code>tls-port=&lt;nr&gt;</code></p>
<dd> Set the <font SIZE="-1">TCP</font> port spice is listening on for encrypted channels.</p>
<dt><code>x509-dir=&lt;dir&gt;</code></p>
<dd> Set the x509 file directory. Expects same filenames as -vnc <tt>$display</tt>,x509=$dir</p>
<dt><code>x509-key-file=&lt;file&gt;</code></p>
<dd>
<dt><code>x509-key-password=&lt;file&gt;</code></p>
<dd>
<dt><code>x509-cert-file=&lt;file&gt;</code></p>
<dd>
<dt><code>x509-cacert-file=&lt;file&gt;</code></p>
<dd>
<dt><code>x509-dh-key-file=&lt;file&gt;</code></p>
<dd> The x509 file names can also be configured individually.</p>
<dt><code>tls-ciphers=&lt;list&gt;</code></p>
<dd> Specify which ciphers to use.</p>
<dt><code>tls-channel=[main|display|cursor|inputs|record|playback]</code></p>
<dd>
<dt><code>plaintext-channel=[main|display|cursor|inputs|record|playback]</code></p>
<dd> Force specific channel to be used with or without <font SIZE="-1">TLS</font> encryption. The options can be specified multiple times to configure multiple channels. The special name &#8220;default&#8221; can be used to set the default mode. For channels which are not explicitly forced into one mode the spice client is allowed to pick tls/plaintext as he pleases.</p>
<dt><code>image-compression=[auto_glz|auto_lz|quic|glz|lz|off]</code></p>
<dd> Configure image compression (lossless). Default is auto_glz.</p>
<dt><code>jpeg-wan-compression=[auto|never|always]</code></p>
<dd>
<dt><code>zlib-glz-wan-compression=[auto|never|always]</code></p>
<dd> Configure wan image compression (lossy for slow links). Default is auto.</p>
<dt><code>streaming-video=[off|all|filter]</code></p>
<dd> Configure video stream detection. Default is filter.</p>
<dt><code>agent-mouse=[on|off]</code></p>
<dd> Enable/disable passing mouse events via vdagent. Default is on.</p>
<dt><code>playback-compression=[on|off]</code></p>
<dd> Enable/disable audio stream compression (using celt 0.5.1). Default is on.</p>
<dt><code>seamless-migration=[on|off]</code></p>
<dd> Enable/disable spice seamless migration. Default is off.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-portrait</code></p>
<dd> Rotate graphical output 90 deg left (only <font SIZE="-1">PXA LCD</font>).</p>
<dt><code>-rotate</code> <i>deg</i></p>
<dd> Rotate graphical output some deg left (only <font SIZE="-1">PXA LCD</font>).</p>
<dt><code>-vga</code> <i>type</i></p>
<dd> Select type of <font SIZE="-1">VGA</font> card to emulate. Valid values for <i>type</i> are</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>cirrus</code></p>
<dd> Cirrus Logic <font SIZE="-1">GD5446</font> Video card. All Windows versions starting from Windows 95 should recognize and use this graphic card. For optimal performances, use 16 bit color depth in the guest and the host <font SIZE="-1">OS. </font>(This one is the default)</p>
<dt><code>std</code></p>
<dd> Standard <font SIZE="-1">VGA</font> card with Bochs <font SIZE="-1">VBE</font> extensions. If your guest <font SIZE="-1">OS</font> supports the <font SIZE="-1">VESA 2.0 VBE</font> extensions (e.g. Windows <font SIZE="-1">XP</font>) and if you want to use high resolution modes (&gt;= 1280x1024x16) then you should use this option.</p>
<dt><code>vmware</code></p>
<dd> VMWare SVGA-II compatible adapter. Use it if you have sufficiently recent XFree86/XOrg server or Windows guest with a driver for this card.</p>
<dt><code>qxl</code></p>
<dd> <font SIZE="-1">QXL</font> paravirtual graphic card. It is <font SIZE="-1">VGA</font> compatible (including <font SIZE="-1">VESA 2.0 VBE</font> support). Works best with qxl guest drivers installed though. Recommended choice when using the spice protocol.</p>
<dt><code>tcx</code></p>
<dd> (sun4m only) Sun <font SIZE="-1">TCX</font> framebuffer. This is the default framebuffer for sun4m machines and offers both 8-bit and 24-bit colour depths at a fixed resolution of 1024&#215;768.</p>
<dt><code>cg3</code></p>
<dd> (sun4m only) Sun cgthree framebuffer. This is a simple 8-bit framebuffer for sun4m machines available in both 1024&#215;768 (OpenBIOS) and 1152&#215;900 (<font SIZE="-1">OBP</font>) resolutions aimed at people wishing to run older Solaris versions.</p>
<dt><code>none</code></p>
<dd> Disable <font SIZE="-1">VGA</font> card.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-full-screen</code></p>
<dd> Start in full screen.</p>
<dt><code>-g</code> <i>width</i><code>x</code><i>height</i><code>[x</code><i>depth</i><code>]</code></p>
<dd> Set the initial graphical resolution and depth (<font SIZE="-1">PPC, SPARC</font> only).</p>
<dt><code>-vnc</code> <i>display</i><code>[,</code><i>option</i><code>[,</code><i>option</i><code>[,&#8230;]]]</code></p>
<dd> Normally, <font SIZE="-1">QEMU</font> uses <font SIZE="-1">SDL</font> to display the <font SIZE="-1">VGA</font> output. With this option, you can have <font SIZE="-1">QEMU</font> listen on <font SIZE="-1">VNC</font> display <i>display</i> and redirect the <font SIZE="-1">VGA</font> display over the <font SIZE="-1">VNC</font> session. It is very useful to enable the usb tablet device when using this option (option <code>-usbdevice tablet</code>). When using the <font SIZE="-1">VNC</font> display, you must use the <code>-k</code> parameter to set the keyboard layout if you are not using en-us. Valid syntax for the <i>display</i> is</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>host</i><code>:</code><i>d</i></p>
<dd> <font SIZE="-1">TCP</font> connections will only be allowed from <i>host</i> on display <i>d</i>. By convention the <font SIZE="-1">TCP</font> port is 5900+<i>d</i>. Optionally, <i>host</i> can be omitted in which case the server will accept connections from any host.</p>
<dt><code>unix:</code><i>path</i></p>
<dd> Connections will be allowed over <font SIZE="-1">UNIX</font> domain sockets where <i>path</i> is the location of a unix socket to listen for connections on.</p>
<dt><code>none</code></p>
<dd> <font SIZE="-1">VNC</font> is initialized but not started. The monitor <tt>&quot;change&quot;</tt> command can be used to later start the <font SIZE="-1">VNC</font> server.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Following the <i>display</i> value there may be one or more <i>option</i> flags separated by commas. Valid options are</p>
<dl>
<dt><code>reverse</code></p>
<dd> Connect to a listening <font SIZE="-1">VNC</font> client via a &#8220;reverse&#8221; connection. The client is specified by the <i>display</i>. For reverse network connections (<i>host</i>:<i>d</i>,<tt>&quot;reverse&quot;</tt>), the <i>d</i> argument is a <font SIZE="-1">TCP</font> port number, not a display number.</p>
<dt><code>websocket</code></p>
<dd> Opens an additional <font SIZE="-1">TCP</font> listening port dedicated to <font SIZE="-1">VNC</font> Websocket connections. By definition the Websocket port is 5700+<i>display</i>. If <i>host</i> is specified connections will only be allowed from this host. As an alternative the Websocket port could be specified by using <tt>&quot;websocket&quot;</tt>=<i>port</i>. <font SIZE="-1">TLS</font> encryption for the Websocket connection is supported if the required certificates are specified with the <font SIZE="-1">VNC</font> option <code>x509</code>.</p>
<dt><code>password</code></p>
<dd> Require that password based authentication is used for client connections. </p>
<p> The password must be set separately using the <tt>&quot;set_password&quot;</tt> command in the <code>pcsys_monitor</code>. The syntax to change your password is: <tt>&quot;set_password &lt;protocol&gt; &lt;password&gt;&quot;</tt> where &lt;protocol&gt; could be either &#8220;vnc&#8221; or &#8220;spice&#8221;. </p>
<p> If you would like to change &lt;protocol&gt; password expiration, you should use <tt>&quot;expire_password &lt;protocol&gt; &lt;expiration-time&gt;&quot;</tt> where expiration time could be one of the following options: now, never, +seconds or <font SIZE="-1">UNIX</font> time of expiration, e.g. +60 to make password expire in 60 seconds, or 1335196800 to make password expire on &#8220;Mon Apr 23 12:00:00 <font SIZE="-1">EDT 2012&#8221; </font>(<font SIZE="-1">UNIX</font> time for this date and time). </p>
<p> You can also use keywords &#8220;now&#8221; or &#8220;never&#8221; for the expiration time to allow &lt;protocol&gt; password to expire immediately or never expire.</p>
<dt><code>tls</code></p>
<dd> Require that client use <font SIZE="-1">TLS</font> when communicating with the <font SIZE="-1">VNC</font> server. This uses anonymous <font SIZE="-1">TLS</font> credentials so is susceptible to a man-in-the-middle attack. It is recommended that this option be combined with either the <code>x509</code> or <code>x509verify</code> options.</p>
<dt><code>x509=</code><i>/path/to/certificate/dir</i></p>
<dd> Valid if <code>tls</code> is specified. Require that x509 credentials are used for negotiating the <font SIZE="-1">TLS</font> session. The server will send its x509 certificate to the client. It is recommended that a password be set on the <font SIZE="-1">VNC</font> server to provide authentication of the client when this is used. The path following this option specifies where the x509 certificates are to be loaded from. See the <code>vnc_security</code> section for details on generating certificates.</p>
<dt><code>x509verify=</code><i>/path/to/certificate/dir</i></p>
<dd> Valid if <code>tls</code> is specified. Require that x509 credentials are used for negotiating the <font SIZE="-1">TLS</font> session. The server will send its x509 certificate to the client, and request that the client send its own x509 certificate. The server will validate the client&#8217;s certificate against the <font SIZE="-1">CA</font> certificate, and reject clients when validation fails. If the certificate authority is trusted, this is a sufficient authentication mechanism. You may still wish to set a password on the <font SIZE="-1">VNC</font> server as a second authentication layer. The path following this option specifies where the x509 certificates are to be loaded from. See the <code>vnc_security</code> section for details on generating certificates.</p>
<dt><code>sasl</code></p>
<dd> Require that the client use <font SIZE="-1">SASL</font> to authenticate with the <font SIZE="-1">VNC</font> server. The exact choice of authentication method used is controlled from the system / user&#8217;s <font SIZE="-1">SASL</font> configuration file for the &#8216;qemu&#8217; service. This is typically found in /etc/sasl2/qemu.conf. If running <font SIZE="-1">QEMU</font> as an unprivileged user, an environment variable <font SIZE="-1">SASL_CONF_PATH</font> can be used to make it search alternate locations for the service config. While some <font SIZE="-1">SASL</font> auth methods can also provide data encryption (eg <font SIZE="-1">GSSAPI</font>), it is recommended that <font SIZE="-1">SASL</font> always be combined with the &#8216;tls&#8217; and &#8216;x509&#8217; settings to enable use of <font SIZE="-1">SSL</font> and server certificates. This ensures a data encryption preventing compromise of authentication credentials. See the <code>vnc_security</code> section for details on using <font SIZE="-1">SASL</font> authentication.</p>
<dt><code>acl</code></p>
<dd> Turn on access control lists for checking of the x509 client certificate and <font SIZE="-1">SASL</font> party. For x509 certs, the <font SIZE="-1">ACL</font> check is made against the certificate&#8217;s distinguished name. This is something that looks like <tt>&quot;C=GB,O=ACME,L=Boston,CN=bob&quot;</tt>. For <font SIZE="-1">SASL</font> party, the <font SIZE="-1">ACL</font> check is made against the username, which depending on the <font SIZE="-1">SASL</font> plugin, may include a realm component, eg <tt>&quot;bob&quot;</tt> or <tt>&quot;bob [at] EXAMPLE.COM&quot;</tt>. When the <code>acl</code> flag is set, the initial access list will be empty, with a <tt>&quot;deny&quot;</tt> policy. Thus no one will be allowed to use the <font SIZE="-1">VNC</font> server until the ACLs have been loaded. This can be achieved using the <tt>&quot;acl&quot;</tt> monitor command.</p>
<dt><code>lossy</code></p>
<dd> Enable lossy compression methods (gradient, <font SIZE="-1">JPEG, &#8230;</font>). If this option is set, <font SIZE="-1">VNC</font> client may receive lossy framebuffer updates depending on its encoding settings. Enabling this option can save a lot of bandwidth at the expense of quality.</p>
<dt><code>non-adaptive</code></p>
<dd> Disable adaptive encodings. Adaptive encodings are enabled by default. An adaptive encoding will try to detect frequently updated screen regions, and send updates in these regions using a lossy encoding (like <font SIZE="-1">JPEG</font>). This can be really helpful to save bandwidth when playing videos. Disabling adaptive encodings allows to restore the original static behavior of encodings like Tight.</p>
<dt><code>share=[allow-exclusive|force-shared|ignore]</code></p>
<dd> Set display sharing policy. &#8216;allow-exclusive&#8217; allows clients to ask for exclusive access. As suggested by the rfb spec this is implemented by dropping other connections. Connecting multiple clients in parallel requires all clients asking for a shared session (vncviewer: -shared switch). This is the default. &#8216;force-shared&#8217; disables exclusive client access. Useful for shared desktop sessions, where you don&#8217;t want someone forgetting specify -shared disconnect everybody else. &#8216;ignore&#8217; completely ignores the shared flag and allows everybody connect unconditionally. Doesn&#8217;t conform to the rfb spec but is traditional <font SIZE="-1">QEMU</font> behavior.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<p> i386 target only:</p>
<dl>
<dt><code>-win2k-hack</code></p>
<dd> Use it when installing Windows 2000 to avoid a disk full bug. After Windows 2000 is installed, you no longer need this option (this option slows down the <font SIZE="-1">IDE</font> transfers).</p>
<dt><code>-no-fd-bootchk</code></p>
<dd> Disable boot signature checking for floppy disks in <font SIZE="-1">BIOS.</font> May be needed to boot from old floppy disks.</p>
<dt><code>-no-acpi</code></p>
<dd> Disable <font SIZE="-1">ACPI </font>(Advanced Configuration and Power Interface) support. Use it if your guest <font SIZE="-1">OS</font> complains about <font SIZE="-1">ACPI</font> problems (<font SIZE="-1">PC</font> target machine only).</p>
<dt><code>-no-hpet</code></p>
<dd> Disable <font SIZE="-1">HPET</font> support.</p>
<dt><code>-acpitable [sig=</code><i>str</i><code>][,rev=</code><i>n</i><code>][,oem_id=</code><i>str</i><code>][,oem_table_id=</code><i>str</i><code>][,oem_rev=</code><i>n</i><code>] [,asl_compiler_id=</code><i>str</i><code>][,asl_compiler_rev=</code><i>n</i><code>][,data=</code><i>file1</i><code>[:</code><i>file2</i><code>]&#8230;]</code></p>
<dd> Add <font SIZE="-1">ACPI</font> table with specified header fields and context from specified files. For file=, take whole <font SIZE="-1">ACPI</font> table from the specified files, including all <font SIZE="-1">ACPI</font> headers (possible overridden by other options). For data=, only data portion of the table is used, all header information is specified in the command line.</p>
<dt><code>-smbios file=</code><i>binary</i></p>
<dd> Load <font SIZE="-1">SMBIOS</font> entry from binary file.</p>
<dt><code>-smbios type=0[,vendor=</code><i>str</i><code>][,version=</code><i>str</i><code>][,date=</code><i>str</i><code>][,release=</code><i>%d.%d</i><code>]</code></p>
<dd> Specify <font SIZE="-1">SMBIOS</font> type 0 fields</p>
<dt><code>-smbios type=1[,manufacturer=</code><i>str</i><code>][,product=</code><i>str</i><code>] [,version=</code><i>str</i><code>][,serial=</code><i>str</i><code>][,uuid=</code><i>uuid</i><code>][,sku=</code><i>str</i><code>] [,family=</code><i>str</i><code>]</code></p>
<dd> Specify <font SIZE="-1">SMBIOS</font> type 1 fields</dl>
<p> Network options:</p>
<dl>
<dt><code>-net nic[,vlan=</code><i>n</i><code>][,macaddr=</code><i>mac</i><code>][,model=</code><i>type</i><code>] [,name=</code><i>name</i><code>][,addr=</code><i>addr</i><code>][,vectors=</code><i>v</i><code>]</code></p>
<dd> Create a new Network Interface Card and connect it to <font SIZE="-1">VLAN </font><i>n</i> (<i>n</i> = 0 is the default). The <font SIZE="-1">NIC</font> is an e1000 by default on the <font SIZE="-1">PC</font> target. Optionally, the <font SIZE="-1">MAC</font> address can be changed to <i>mac</i>, the device address set to <i>addr</i> (<font SIZE="-1">PCI</font> cards only), and a <i>name</i> can be assigned for use in monitor commands. Optionally, for <font SIZE="-1">PCI</font> cards, you can specify the number <i>v</i> of MSI-X vectors that the card should have; this option currently only affects virtio cards; set <i>v</i> = 0 to disable MSI-X. If no <code>-net</code> option is specified, a single <font SIZE="-1">NIC</font> is created. <font SIZE="-1">QEMU</font> can emulate several different models of network card. Valid values for <i>type</i> are <tt>&quot;virtio&quot;</tt>, <tt>&quot;i82551&quot;</tt>, <tt>&quot;i82557b&quot;</tt>, <tt>&quot;i82559er&quot;</tt>, <tt>&quot;ne2k_pci&quot;</tt>, <tt>&quot;ne2k_isa&quot;</tt>, <tt>&quot;pcnet&quot;</tt>, <tt>&quot;rtl8139&quot;</tt>, <tt>&quot;e1000&quot;</tt>, <tt>&quot;smc91c111&quot;</tt>, <tt>&quot;lance&quot;</tt> and <tt>&quot;mcf_fec&quot;</tt>. Not all devices are supported on all targets. Use <tt>&quot;-net nic,model=help&quot;</tt> for a list of available devices for your target.</p>
<dt><code>-netdev user,id=</code><i>id</i><code>[,</code><i>option</i><code>][,</code><i>option</i><code>][,&#8230;]</code></p>
<dd>
<dt><code>-net user[,</code><i>option</i><code>][,</code><i>option</i><code>][,&#8230;]</code></p>
<dd> Use the user mode network stack which requires no administrator privilege to run. Valid options are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>vlan=</code><i>n</i></p>
<dd> Connect user mode stack to <font SIZE="-1">VLAN </font><i>n</i> (<i>n</i> = 0 is the default).</p>
<dt><code>id=</code><i>id</i></p>
<dd>
<dt><code>name=</code><i>name</i></p>
<dd> Assign symbolic name for use in monitor commands.</p>
<dt><code>net=</code><i>addr</i><code>[/</code><i>mask</i><code>]</code></p>
<dd> Set <font SIZE="-1">IP</font> network address the guest will see. Optionally specify the netmask, either in the form a.b.c.d or as number of valid top-most bits. Default is 10.0.2.0/24.</p>
<dt><code>host=</code><i>addr</i></p>
<dd> Specify the guest-visible address of the host. Default is the 2nd <font SIZE="-1">IP</font> in the guest network, i.e. x.x.x.2.</p>
<dt><code>restrict=on|off</code></p>
<dd> If this option is enabled, the guest will be isolated, i.e. it will not be able to contact the host and no guest <font SIZE="-1">IP</font> packets will be routed over the host to the outside. This option does not affect any explicitly set forwarding rules.</p>
<dt><code>hostname=</code><i>name</i></p>
<dd> Specifies the client hostname reported by the built-in <font SIZE="-1">DHCP</font> server.</p>
<dt><code>dhcpstart=</code><i>addr</i></p>
<dd> Specify the first of the 16 IPs the built-in <font SIZE="-1">DHCP</font> server can assign. Default is the 15th to 31st <font SIZE="-1">IP</font> in the guest network, i.e. x.x.x.15 to x.x.x.31.</p>
<dt><code>dns=</code><i>addr</i></p>
<dd> Specify the guest-visible address of the virtual nameserver. The address must be different from the host address. Default is the 3rd <font SIZE="-1">IP</font> in the guest network, i.e. x.x.x.3.</p>
<dt><code>dnssearch=</code><i>domain</i></p>
<dd> Provides an entry for the domain-search list sent by the built-in <font SIZE="-1">DHCP</font> server. More than one domain suffix can be transmitted by specifying this option multiple times. If supported, this will cause the guest to automatically try to append the given domain suffix(es) in case a domain name can not be resolved. </p>
<p> Example: </p>
<pre>
        qemu -net user,dnssearch=mgmt.example.org,dnssearch=example.org [...]
</pre>
<dt><code>tftp=</code><i>dir</i></p>
<dd> When using the user mode network stack, activate a built-in <font SIZE="-1">TFTP</font> server. The files in <i>dir</i> will be exposed as the root of a <font SIZE="-1">TFTP</font> server. The <font SIZE="-1">TFTP</font> client on the guest must be configured in binary mode (use the command <tt>&quot;bin&quot;</tt> of the Unix <font SIZE="-1">TFTP</font> client).</p>
<dt><code>bootfile=</code><i>file</i></p>
<dd> When using the user mode network stack, broadcast <i>file</i> as the <font SIZE="-1">BOOTP</font> filename. In conjunction with <code>tftp</code>, this can be used to network boot a guest from a local directory. </p>
<p> Example (using pxelinux): </p>
<pre>
        qemu-system-i386 -hda linux.img -boot n -net user,tftp=/path/to/tftp/files,bootfile=/pxelinux.0
</pre>
<dt><code>smb=</code><i>dir</i><code>[,smbserver=</code><i>addr</i><code>]</code></p>
<dd> When using the user mode network stack, activate a built-in <font SIZE="-1">SMB</font> server so that Windows OSes can access to the host files in <i>dir</i> transparently. The <font SIZE="-1">IP</font> address of the <font SIZE="-1">SMB</font> server can be set to <i>addr</i>. By default the 4th <font SIZE="-1">IP</font> in the guest network is used, i.e. x.x.x.4. </p>
<p> In the guest Windows <font SIZE="-1">OS,</font> the line: </p>
<pre>
        10.0.2.4 smbserver
</pre>
<p> must be added in the file <i>C:\WINDOWS\LMHOSTS</i> (for windows 9x/Me) or <i>C:\WINNT\SYSTEM32\DRIVERS\ETC\LMHOSTS</i> (Windows <font SIZE="-1">NT/2000</font>). </p>
<p> Then <i>dir</i> can be accessed in <i>\smbserver\qemu</i>. </p>
<p> Note that a <font SIZE="-1">SAMBA</font> server must be installed on the host <font SIZE="-1">OS. QEMU</font> was tested successfully with smbd versions from Red Hat 9, Fedora Core 3 and OpenSUSE 11.x.</p>
<dt><code>hostfwd=[tcp|udp]:[</code><i>hostaddr</i><code>]:</code><i>hostport</i><code>-[</code><i>guestaddr</i><code>]:</code><i>guestport</i></p>
<dd> Redirect incoming <font SIZE="-1">TCP</font> or <font SIZE="-1">UDP</font> connections to the host port <i>hostport</i> to the guest <font SIZE="-1">IP</font> address <i>guestaddr</i> on guest port <i>guestport</i>. If <i>guestaddr</i> is not specified, its value is x.x.x.15 (default first address given by the built-in <font SIZE="-1">DHCP</font> server). By specifying <i>hostaddr</i>, the rule can be bound to a specific host interface. If no connection type is set, <font SIZE="-1">TCP</font> is used. This option can be given multiple times. </p>
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
<dt><code>guestfwd=[tcp]:</code><i>server</i><code>:</code><i>port</i><code>&#8211;</code><i>dev</i></p>
<dd>
<dt><code>guestfwd=[tcp]:</code><i>server</i><code>:</code><i>port</i><code>&#8211;</code><i>cmd:command</i></p>
<dd> Forward guest <font SIZE="-1">TCP</font> connections to the <font SIZE="-1">IP</font> address <i>server</i> on port <i>port</i> to the character device <i>dev</i> or to a program executed by <i>cmd:command</i> which gets spawned for each connection. This option can be given multiple times. </p>
<p> You can either use a chardev directly and have that one used throughout <font SIZE="-1">QEMU</font>&#8216;s lifetime, like in the following example: </p>
<pre>
        # open 10.10.1.1:4321 on bootup, connect 10.0.2.100:1234 to it whenever
        # the guest accesses it
        qemu -net user,guestfwd=tcp:10.0.2.100:1234-tcp:10.10.1.1:4321 [...]
</pre>
<p> Or you can execute a command on every <font SIZE="-1">TCP</font> connection established by the guest, so that <font SIZE="-1">QEMU</font> behaves similar to an inetd process for that virtual server: </p>
<pre>
        # call &quot;netcat 10.10.1.1 4321&quot; on every TCP connection to 10.0.2.100:1234
        # and connect the TCP stream to its stdin/stdout
        qemu -net 'user,guestfwd=tcp:10.0.2.100:1234-cmd:netcat 10.10.1.1 4321'
</pre>
</dl>
</dl>
<dl>
<dt>
<dd>
<p> Note: Legacy stand-alone options -tftp, -bootp, -smb and -redir are still processed and applied to -net user. Mixing them with the new configuration syntax gives undefined results. Their use for new applications is discouraged as they will be removed from future versions.</dl>
<dt><code>-netdev tap,id=</code><i>id</i><code>[,fd=</code><i>h</i><code>][,ifname=</code><i>name</i><code>][,script=</code><i>file</i><code>][,downscript=</code><i>dfile</i><code>][,helper=</code><i>helper</i><code>]</code></p>
<dd>
<dt><code>-net tap[,vlan=</code><i>n</i><code>][,name=</code><i>name</i><code>][,fd=</code><i>h</i><code>][,ifname=</code><i>name</i><code>][,script=</code><i>file</i><code>][,downscript=</code><i>dfile</i><code>][,helper=</code><i>helper</i><code>]</code></p>
<dd> Connect the host <font SIZE="-1">TAP</font> network interface <i>name</i> to <font SIZE="-1">VLAN </font><i>n</i>. </p>
<p> Use the network script <i>file</i> to configure it and the network script <i>dfile</i> to deconfigure it. If <i>name</i> is not provided, the <font SIZE="-1">OS</font> automatically provides one. The default network configure script is <i>/etc/qemu-ifup</i> and the default network deconfigure script is <i>/etc/qemu-ifdown</i>. Use <code>script=no</code> or <code>downscript=no</code> to disable script execution. </p>
<p> If running <font SIZE="-1">QEMU</font> as an unprivileged user, use the network helper <i>helper</i> to configure the <font SIZE="-1">TAP</font> interface. The default network helper executable is <i>/path/to/qemu-bridge-helper</i>. </p>
<p> <code>fd</code>=<i>h</i> can be used to specify the handle of an already opened host <font SIZE="-1">TAP</font> interface. </p>
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
<dt><code>-netdev bridge,id=</code><i>id</i><code>[,br=</code><i>bridge</i><code>][,helper=</code><i>helper</i><code>]</code></p>
<dd>
<dt><code>-net bridge[,vlan=</code><i>n</i><code>][,name=</code><i>name</i><code>][,br=</code><i>bridge</i><code>][,helper=</code><i>helper</i><code>]</code></p>
<dd> Connect a host <font SIZE="-1">TAP</font> network interface to a host bridge device. </p>
<p> Use the network helper <i>helper</i> to configure the <font SIZE="-1">TAP</font> interface and attach it to the bridge. The default network helper executable is <i>/path/to/qemu-bridge-helper</i> and the default bridge device is <i>br0</i>. </p>
<p> Examples: </p>
<pre>
        #launch a QEMU instance with the default network helper to
        #connect a TAP device to bridge br0
        qemu-system-i386 linux.img -net bridge -net nic,model=virtio
        
        #launch a QEMU instance with the default network helper to
        #connect a TAP device to bridge qemubr0
        qemu-system-i386 linux.img -net bridge,br=qemubr0 -net nic,model=virtio
</pre>
<dt><code>-netdev socket,id=</code><i>id</i><code>[,fd=</code><i>h</i><code>][,listen=[</code><i>host</i><code>]:</code><i>port</i><code>][,connect=</code><i>host</i><code>:</code><i>port</i><code>]</code></p>
<dd>
<dt><code>-net socket[,vlan=</code><i>n</i><code>][,name=</code><i>name</i><code>][,fd=</code><i>h</i><code>] [,listen=[</code><i>host</i><code>]:</code><i>port</i><code>][,connect=</code><i>host</i><code>:</code><i>port</i><code>]</code></p>
<dd> Connect the <font SIZE="-1">VLAN </font><i>n</i> to a remote <font SIZE="-1">VLAN</font> in another <font SIZE="-1">QEMU</font> virtual machine using a <font SIZE="-1">TCP</font> socket connection. If <code>listen</code> is specified, <font SIZE="-1">QEMU</font> waits for incoming connections on <i>port</i> (<i>host</i> is optional). <code>connect</code> is used to connect to another <font SIZE="-1">QEMU</font> instance using the <code>listen</code> option. <code>fd</code>=<i>h</i> specifies an already opened <font SIZE="-1">TCP</font> socket. </p>
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
<dt><code>-netdev socket,id=</code><i>id</i><code>[,fd=</code><i>h</i><code>][,mcast=</code><i>maddr</i><code>:</code><i>port</i><code>[,localaddr=</code><i>addr</i><code>]]</code></p>
<dd>
<dt><code>-net socket[,vlan=</code><i>n</i><code>][,name=</code><i>name</i><code>][,fd=</code><i>h</i><code>][,mcast=</code><i>maddr</i><code>:</code><i>port</i><code>[,localaddr=</code><i>addr</i><code>]]</code></p>
<dd> Create a <font SIZE="-1">VLAN </font><i>n</i> shared with another <font SIZE="-1">QEMU</font> virtual machines using a <font SIZE="-1">UDP</font> multicast socket, effectively making a bus for every <font SIZE="-1">QEMU</font> with same multicast address <i>maddr</i> and <i>port</i>. <font SIZE="-1">NOTES:</font></p>
<dl>
<dt>
<dd>
<dl>
<dt>1.</p>
<dd> Several <font SIZE="-1">QEMU</font> can be running on different hosts and share same bus (assuming correct multicast setup for these hosts).</p>
<dt>2.</p>
<dd> mcast support is compatible with User Mode Linux (argument <code>eth</code><i>N</i><code>=mcast</code>), see &lt;<code><a rel="nofollow" href="http://user-mode-linux.sf.net">http://user-mode-linux.sf.net</a></code>&gt;.</p>
<dt>3.</p>
<dd> Use <code>fd=h</code> to specify an already opened <font SIZE="-1">UDP</font> multicast socket.</dl>
</dl>
<dl>
<dt>
<dd>
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
</dl>
<dt><code>-netdev vde,id=</code><i>id</i><code>[,sock=</code><i>socketpath</i><code>][,port=</code><i>n</i><code>][,group=</code><i>groupname</i><code>][,mode=</code><i>octalmode</i><code>]</code></p>
<dd>
<dt><code>-net vde[,vlan=</code><i>n</i><code>][,name=</code><i>name</i><code>][,sock=</code><i>socketpath</i><code>] [,port=</code><i>n</i><code>][,group=</code><i>groupname</i><code>][,mode=</code><i>octalmode</i><code>]</code></p>
<dd> Connect <font SIZE="-1">VLAN </font><i>n</i> to <font SIZE="-1">PORT </font><i>n</i> of a vde switch running on host and listening for incoming connections on <i>socketpath</i>. Use <font SIZE="-1">GROUP </font><i>groupname</i> and <font SIZE="-1">MODE </font><i>octalmode</i> to change default ownership and permissions for communication port. This option is only available if <font SIZE="-1">QEMU</font> has been compiled with vde support enabled. </p>
<p> Example: </p>
<pre>
        # launch vde switch
        vde_switch -F -sock /tmp/myswitch
        # launch QEMU instance
        qemu-system-i386 linux.img -net nic -net vde,sock=/tmp/myswitch
</pre>
<dt><code>-netdev hubport,id=</code><i>id</i><code>,hubid=</code><i>hubid</i></p>
<dd> Create a hub port on <font SIZE="-1">QEMU </font>&#8220;vlan&#8221; <i>hubid</i>. </p>
<p> The hubport netdev lets you connect a <font SIZE="-1">NIC</font> to a <font SIZE="-1">QEMU </font>&#8220;vlan&#8221; instead of a single netdev. <tt>&quot;-net&quot;</tt> and <tt>&quot;-device&quot;</tt> with parameter <code>vlan</code> create the required hub automatically.</p>
<dt><code>-net dump[,vlan=</code><i>n</i><code>][,file=</code><i>file</i><code>][,len=</code><i>len</i><code>]</code></p>
<dd> Dump network traffic on <font SIZE="-1">VLAN </font><i>n</i> to file <i>file</i> (<i>qemu-vlan0.pcap</i> by default). At most <i>len</i> bytes (64k by default) per packet are stored. The file format is libpcap, so it can be analyzed with tools such as tcpdump or Wireshark.</p>
<dt><code>-net none</code></p>
<dd> Indicate that no network devices should be configured. It is used to override the default configuration (<code>-net nic -net user</code>) which is activated if no <code>-net</code> options are provided.</dl>
<p> Character device options: </p>
<p> The general form of a character device option is:</p>
<dl>
<dt><code>-chardev</code> <i>backend</i> <code>,id=</code><i>id</i> <code>[,mux=on|off] [,</code><i>options</i><code>]</code></p>
<dd> Backend is one of: <code>null</code>, <code>socket</code>, <code>udp</code>, <code>msmouse</code>, <code>vc</code>, <code>ringbuf</code>, <code>file</code>, <code>pipe</code>, <code>console</code>, <code>serial</code>, <code>pty</code>, <code>stdio</code>, <code>braille</code>, <code>tty</code>, <code>parallel</code>, <code>parport</code>, <code>spicevmc</code>. <code>spiceport</code>. The specific backend will determine the applicable options. </p>
<p> All devices must have an id, which can be any string up to 127 characters long. It is used to uniquely identify this device in other command line directives. </p>
<p> A character device may be used in multiplexing mode by multiple front-ends. The key sequence of <code>Control-a</code> and <code>c</code> will rotate the input focus between attached front-ends. Specify <code>mux=on</code> to enable this mode. </p>
<p> Options to each backend are described below.</p>
<dt><code>-chardev null ,id=</code><i>id</i></p>
<dd> A void device. This device will not emit any data, and will drop any data it receives. The null backend does not take any options.</p>
<dt><code>-chardev socket ,id=</code><i>id</i> <code>[</code><i></i><font SIZE="-1"><i>TCP</i></font><i> options</i> <code>or</code> <i>unix options</i><code>] [,server] [,nowait] [,telnet]</code></p>
<dd> Create a two-way stream socket, which can be either a <font SIZE="-1">TCP</font> or a unix socket. A unix socket will be created if <code>path</code> is specified. Behaviour is undefined if <font SIZE="-1">TCP</font> options are specified for a unix socket. </p>
<p> <code>server</code> specifies that the socket shall be a listening socket. </p>
<p> <code>nowait</code> specifies that <font SIZE="-1">QEMU</font> should not block waiting for a client to connect to a listening socket. </p>
<p> <code>telnet</code> specifies that traffic on the socket should interpret telnet escape sequences. </p>
<p> <font SIZE="-1">TCP</font> and unix socket options are given below:</p>
<dl>
<dt>
<dd>
<dl>
<dt><font SIZE="-1"><code>TCP</code></font><code> options: port=</code><i>port</i> <code>[,host=</code><i>host</i><code>] [,to=</code><i>to</i><code>] [,ipv4] [,ipv6] [,nodelay]</code></p>
<dd> <code>host</code> for a listening socket specifies the local address to be bound. For a connecting socket species the remote host to connect to. <code>host</code> is optional for listening sockets. If not specified it defaults to <tt>0.0.0.0</tt>. </p>
<p> <code>port</code> for a listening socket specifies the local port to be bound. For a connecting socket specifies the port on the remote host to connect to. <code>port</code> can be given as either a port number or a service name. <code>port</code> is required. </p>
<p> <code>to</code> is only relevant to listening sockets. If it is specified, and <code>port</code> cannot be bound, <font SIZE="-1">QEMU</font> will attempt to bind to subsequent ports up to and including <code>to</code> until it succeeds. <code>to</code> must be specified as a port number. </p>
<p> <code>ipv4</code> and <code>ipv6</code> specify that either IPv4 or IPv6 must be used. If neither is specified the socket may use either protocol. </p>
<p> <code>nodelay</code> disables the Nagle algorithm.</p>
<dt><code>unix options: path=</code><i>path</i></p>
<dd> <code>path</code> specifies the local path of the unix socket. <code>path</code> is required.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-chardev udp ,id=</code><i>id</i> <code>[,host=</code><i>host</i><code>] ,port=</code><i>port</i> <code>[,localaddr=</code><i>localaddr</i><code>] [,localport=</code><i>localport</i><code>] [,ipv4] [,ipv6]</code></p>
<dd> Sends all traffic from the guest to a remote host over <font SIZE="-1">UDP.</font> </p>
<p> <code>host</code> specifies the remote host to connect to. If not specified it defaults to <tt>&quot;localhost&quot;</tt>. </p>
<p> <code>port</code> specifies the port on the remote host to connect to. <code>port</code> is required. </p>
<p> <code>localaddr</code> specifies the local address to bind to. If not specified it defaults to <tt>0.0.0.0</tt>. </p>
<p> <code>localport</code> specifies the local port to bind to. If not specified any available local port will be used. </p>
<p> <code>ipv4</code> and <code>ipv6</code> specify that either IPv4 or IPv6 must be used. If neither is specified the device may use either protocol.</p>
<dt><code>-chardev msmouse ,id=</code><i>id</i></p>
<dd> Forward <font SIZE="-1">QEMU</font>&#8216;s emulated msmouse events to the guest. <code>msmouse</code> does not take any options.</p>
<dt><code>-chardev vc ,id=</code><i>id</i> <code>[[,width=</code><i>width</i><code>] [,height=</code><i>height</i><code>]] [[,cols=</code><i>cols</i><code>] [,rows=</code><i>rows</i><code>]]</code></p>
<dd> Connect to a <font SIZE="-1">QEMU</font> text console. <code>vc</code> may optionally be given a specific size. </p>
<p> <code>width</code> and <code>height</code> specify the width and height respectively of the console, in pixels. </p>
<p> <code>cols</code> and <code>rows</code> specify that the console be sized to fit a text console with the given dimensions.</p>
<dt><code>-chardev ringbuf ,id=</code><i>id</i> <code>[,size=</code><i>size</i><code>]</code></p>
<dd> Create a ring buffer with fixed size <code>size</code>. <i>size</i> must be a power of two, and defaults to <tt>&quot;64K&quot;</tt>).</p>
<dt><code>-chardev file ,id=</code><i>id</i> <code>,path=</code><i>path</i></p>
<dd> Log all traffic received from the guest to a file. </p>
<p> <code>path</code> specifies the path of the file to be opened. This file will be created if it does not already exist, and overwritten if it does. <code>path</code> is required.</p>
<dt><code>-chardev pipe ,id=</code><i>id</i> <code>,path=</code><i>path</i></p>
<dd> Create a two-way connection to the guest. The behaviour differs slightly between Windows hosts and other hosts: </p>
<p> On Windows, a single duplex pipe will be created at <i>\.pipe\</i>path<i></i>. </p>
<p> On other hosts, 2 pipes will be created called <i></i>path<i>.in</i> and <i></i>path<i>.out</i>. Data written to <i></i>path<i>.in</i> will be received by the guest. Data written by the guest can be read from <i></i>path<i>.out</i>. <font SIZE="-1">QEMU</font> will not create these fifos, and requires them to be present. </p>
<p> <code>path</code> forms part of the pipe path as described above. <code>path</code> is required.</p>
<dt><code>-chardev console ,id=</code><i>id</i></p>
<dd> Send traffic from the guest to <font SIZE="-1">QEMU</font>&#8216;s standard output. <code>console</code> does not take any options. </p>
<p> <code>console</code> is only available on Windows hosts.</p>
<dt><code>-chardev serial ,id=</code><i>id</i> <code>,path=</code><code>path</code></p>
<dd> Send traffic from the guest to a serial device on the host. </p>
<p> On Unix hosts serial will actually accept any tty device, not only serial lines. </p>
<p> <code>path</code> specifies the name of the serial device to open.</p>
<dt><code>-chardev pty ,id=</code><i>id</i></p>
<dd> Create a new pseudo-terminal on the host and connect to it. <code>pty</code> does not take any options. </p>
<p> <code>pty</code> is not available on Windows hosts.</p>
<dt><code>-chardev stdio ,id=</code><i>id</i> <code>[,signal=on|off]</code></p>
<dd> Connect to standard input and standard output of the <font SIZE="-1">QEMU</font> process. </p>
<p> <code>signal</code> controls if signals are enabled on the terminal, that includes exiting <font SIZE="-1">QEMU</font> with the key sequence <code>Control-c</code>. This option is enabled by default, use <code>signal=off</code> to disable it. </p>
<p> <code>stdio</code> is not available on Windows hosts.</p>
<dt><code>-chardev braille ,id=</code><i>id</i></p>
<dd> Connect to a local BrlAPI server. <code>braille</code> does not take any options.</p>
<dt><code>-chardev tty ,id=</code><i>id</i> <code>,path=</code><i>path</i></p>
<dd> <code>tty</code> is only available on Linux, Sun, FreeBSD, NetBSD, OpenBSD and DragonFlyBSD hosts. It is an alias for <code>serial</code>. </p>
<p> <code>path</code> specifies the path to the tty. <code>path</code> is required.</p>
<dt><code>-chardev parallel ,id=</code><i>id</i> <code>,path=</code><i>path</i></p>
<dd>
<dt><code>-chardev parport ,id=</code><i>id</i> <code>,path=</code><i>path</i></p>
<dd> <code>parallel</code> is only available on Linux, FreeBSD and DragonFlyBSD hosts. </p>
<p> Connect to a local parallel port. </p>
<p> <code>path</code> specifies the path to the parallel port device. <code>path</code> is required.</p>
<dt><code>-chardev spicevmc ,id=</code><i>id</i> <code>,debug=</code><i>debug</i><code>, name=</code><i>name</i></p>
<dd> <code>spicevmc</code> is only available when spice support is built in. </p>
<p> <code>debug</code> debug level for spicevmc </p>
<p> <code>name</code> name of spice channel to connect to </p>
<p> Connect to a spice virtual machine channel, such as vdiport.</p>
<dt><code>-chardev spiceport ,id=</code><i>id</i> <code>,debug=</code><i>debug</i><code>, name=</code><i>name</i></p>
<dd> <code>spiceport</code> is only available when spice support is built in. </p>
<p> <code>debug</code> debug level for spicevmc </p>
<p> <code>name</code> name of spice port to connect to </p>
<p> Connect to a spice port, allowing a Spice client to handle the traffic identified by a name (preferably a fqdn).</dl>
<p> Device <font SIZE="-1">URL</font> Syntax: </p>
<p> In addition to using normal file images for the emulated storage devices, <font SIZE="-1">QEMU</font> can also use networked resources such as iSCSI devices. These are specified using a special <font SIZE="-1">URL</font> syntax.</p>
<dl>
<dt><code>iSCSI</code></p>
<dd> iSCSI support allows <font SIZE="-1">QEMU</font> to access iSCSI resources directly and use as images for the guest storage. Both disk and cdrom images are supported. </p>
<p> Syntax for specifying iSCSI LUNs is &#8220;iscsi://&lt;target-ip&gt;[:&lt;port&gt;]/&lt;target-iqn&gt;/&lt;lun&gt;&#8221; </p>
<p> By default qemu will use the iSCSI initiator-name &#8216;iqn.2008-11.org.linux-kvm[:&lt;name&gt;]&#8217; but this can also be set from the command line or a configuration file. </p>
<p> Example (without authentication): </p>
<pre>
        qemu-system-i386 -iscsi initiator-name=iqn.2001-04.com.example:my-initiator \
        -cdrom <a href="iscsi://192.0.2.1/iqn.2001-04.com.example/2">iscsi://192.0.2.1/iqn.2001-04.com.example/2</a> \
        -drive file=<a href="iscsi://192.0.2.1/iqn.2001-04.com.example/1">iscsi://192.0.2.1/iqn.2001-04.com.example/1</a>
</pre>
<p> Example (<font SIZE="-1">CHAP</font> username/password via <font SIZE="-1">URL</font>): </p>
<pre>
        qemu-system-i386 -drive file=<a href="iscsi://user%password@192.0.2.1/iqn.2001-04.com.example/1">iscsi://user%password@192.0.2.1/iqn.2001-04.com.example/1</a>
</pre>
<p> Example (<font SIZE="-1">CHAP</font> username/password via environment variables): </p>
<pre>
        LIBISCSI_CHAP_USERNAME=&quot;user&quot; \
        LIBISCSI_CHAP_PASSWORD=&quot;password&quot; \
        qemu-system-i386 -drive file=<a href="iscsi://192.0.2.1/iqn.2001-04.com.example/1">iscsi://192.0.2.1/iqn.2001-04.com.example/1</a>
</pre>
<p> iSCSI support is an optional feature of <font SIZE="-1">QEMU</font> and only available when compiled and linked against libiscsi. </p>
<p> iSCSI parameters such as username and password can also be specified via a configuration file. See qemu-doc for more information and examples.</p>
<dt><font SIZE="-1"><code>NBD</code></font></p>
<dd> <font SIZE="-1">QEMU</font> supports <font SIZE="-1">NBD </font>(Network Block Devices) both using <font SIZE="-1">TCP</font> protocol as well as Unix Domain Sockets. </p>
<p> Syntax for specifying a <font SIZE="-1">NBD</font> device using <font SIZE="-1">TCP </font>&#8220;nbd:&lt;server-ip&gt;:&lt;port&gt;[:exportname=&lt;export&gt;]&#8221; </p>
<p> Syntax for specifying a <font SIZE="-1">NBD</font> device using Unix Domain Sockets &#8220;nbd:unix:&lt;domain-socket&gt;[:exportname=&lt;export&gt;]&#8221; </p>
<p> Example for <font SIZE="-1">TCP</font> </p>
<pre>
        qemu-system-i386 --drive file=nbd:192.0.2.1:30000
</pre>
<p> Example for Unix Domain Sockets </p>
<pre>
        qemu-system-i386 --drive file=nbd:unix:/tmp/nbd-socket
</pre>
<dt><font SIZE="-1"><code>SSH</code></font></p>
<dd> <font SIZE="-1">QEMU</font> supports <font SIZE="-1">SSH </font>(Secure Shell) access to remote disks. </p>
<p> Examples: </p>
<pre>
        qemu-system-i386 -drive file=<a href="ssh://user@host/path/to/disk.img">ssh://user@host/path/to/disk.img</a>
        qemu-system-i386 -drive file.driver=ssh,file.user=user,file.host=host,file.port=22,file.path=/path/to/disk.img
</pre>
<p> Currently authentication must be done using ssh-agent. Other authentication methods may be supported in future.</p>
<dt><code>Sheepdog</code></p>
<dd> Sheepdog is a distributed storage system for <font SIZE="-1">QEMU. QEMU</font> supports using either local sheepdog devices or remote networked devices. </p>
<p> Syntax for specifying a sheepdog device </p>
<pre><code>
sheepdog[+tcp | +unix]: //[host:port]/vdiname[?socket=path][#snapid|#tag]
</code></pre>
<p> Example </p>
<pre>
        qemu-system-i386 --drive file=sheepdog://192.0.2.1:30000/MyVirtualMachine
</pre>
<p> See also &lt;<code><a rel="nofollow" href="http://http://www.osrg.net/sheepdog/">http://http://www.osrg.net/sheepdog/</a></code>&gt;.</p>
<dt><code>GlusterFS</code></p>
<dd> GlusterFS is an user space distributed file system. <font SIZE="-1">QEMU</font> supports the use of GlusterFS volumes for hosting <font SIZE="-1">VM</font> disk images using <font SIZE="-1">TCP,</font> Unix Domain Sockets and <font SIZE="-1">RDMA</font> transport protocols. </p>
<p> Syntax for specifying a <font SIZE="-1">VM</font> disk image on GlusterFS volume is </p>
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
<dt><code>-bt hci[&#8230;]</code></p>
<dd> Defines the function of the corresponding Bluetooth <font SIZE="-1">HCI. </font> -bt options are matched with the HCIs present in the chosen machine type. For example when emulating a machine with only one <font SIZE="-1">HCI</font> built into it, only the first <tt>&quot;-bt hci[...]&quot;</tt> option is valid and defines the <font SIZE="-1">HCI</font>&#8216;s logic. The Transport Layer is decided by the machine type. Currently the machines <tt>&quot;n800&quot;</tt> and <tt>&quot;n810&quot;</tt> have one <font SIZE="-1">HCI</font> and all other machines have none. </p>
<p> The following three types are recognized:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-bt hci,null</code></p>
<dd> (default) The corresponding Bluetooth <font SIZE="-1">HCI</font> assumes no internal logic and will not respond to any <font SIZE="-1">HCI</font> commands or emit events.</p>
<dt><code>-bt hci,host[:</code><i>id</i><code>]</code></p>
<dd> (<tt>&quot;bluez&quot;</tt> only) The corresponding <font SIZE="-1">HCI</font> passes commands / events to / from the physical <font SIZE="-1">HCI</font> identified by the name <i>id</i> (default: <tt>&quot;hci0&quot;</tt>) on the computer running <font SIZE="-1">QEMU. </font> Only available on <tt>&quot;bluez&quot;</tt> capable systems like Linux.</p>
<dt><code>-bt hci[,vlan=</code><i>n</i><code>]</code></p>
<dd> Add a virtual, standard <font SIZE="-1">HCI</font> that will participate in the Bluetooth scatternet <i>n</i> (default <tt>0</tt>). Similarly to <code>-net</code> VLANs, devices inside a bluetooth network <i>n</i> can only communicate with other devices in the same network (scatternet).</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-bt vhci[,vlan=</code><i>n</i><code>]</code></p>
<dd> (Linux-host only) Create a <font SIZE="-1">HCI</font> in scatternet <i>n</i> (default 0) attached to the host bluetooth stack instead of to the emulated target. This allows the host and target machines to participate in a common scatternet and communicate. Requires the Linux <tt>&quot;vhci&quot;</tt> driver installed. Can be used as following: </p>
<pre>
        qemu-system-i386 [...OPTIONS...] -bt hci,vlan=5 -bt vhci,vlan=5
</pre>
<dt><code>-bt device:</code><i>dev</i><code>[,vlan=</code><i>n</i><code>]</code></p>
<dd> Emulate a bluetooth device <i>dev</i> and place it in network <i>n</i> (default <tt>0</tt>). <font SIZE="-1">QEMU</font> can only emulate one type of bluetooth devices currently:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>keyboard</code></p>
<dd> Virtual wireless keyboard implementing the <font SIZE="-1">HIDP</font> bluetooth profile.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<p> <font SIZE="-1">TPM</font> device options: </p>
<p> The general form of a <font SIZE="-1">TPM</font> device option is:</p>
<dl>
<dt><code>-tpmdev</code> <i>backend</i> <code>,id=</code><i>id</i> <code>[,</code><i>options</i><code>]</code></p>
<dd> Backend type must be: <code>passthrough</code>. </p>
<p> The specific backend type will determine the applicable options. The <tt>&quot;-tpmdev&quot;</tt> option creates the <font SIZE="-1">TPM</font> backend and requires a <tt>&quot;-device&quot;</tt> option that specifies the <font SIZE="-1">TPM</font> frontend interface model. </p>
<p> Options to each backend are described below. </p>
<p> Use &#8216;help&#8217; to print all available <font SIZE="-1">TPM</font> backend types. </p>
<pre>
        qemu -tpmdev help
</pre>
<dt><code>-tpmdev passthrough, id=</code><i>id</i><code>, path=</code><i>path</i><code>, cancel-path=</code><i>cancel-path</i></p>
<dd> (Linux-host only) Enable access to the host&#8217;s <font SIZE="-1">TPM</font> using the passthrough driver. </p>
<p> <code>path</code> specifies the path to the host&#8217;s <font SIZE="-1">TPM</font> device, i.e., on a Linux host this would be <tt>&quot;/dev/tpm0&quot;</tt>. <code>path</code> is optional and by default <tt>&quot;/dev/tpm0&quot;</tt> is used. </p>
<p> <code>cancel-path</code> specifies the path to the host <font SIZE="-1">TPM</font> device&#8217;s sysfs entry allowing for cancellation of an ongoing <font SIZE="-1">TPM</font> command. <code>cancel-path</code> is optional and by default <font SIZE="-1">QEMU</font> will search for the sysfs entry to use. </p>
<p> Some notes about using the host&#8217;s <font SIZE="-1">TPM</font> with the passthrough driver: </p>
<p> The <font SIZE="-1">TPM</font> device accessed by the passthrough driver must not be used by any other application on the host. </p>
<p> Since the host&#8217;s firmware (<font SIZE="-1">BIOS/UEFI</font>) has already initialized the <font SIZE="-1">TPM,</font> the <font SIZE="-1">VM</font>&#8216;s firmware (<font SIZE="-1">BIOS/UEFI</font>) will not be able to initialize the <font SIZE="-1">TPM</font> again and may therefore not show a TPM-specific menu that would otherwise allow the user to configure the <font SIZE="-1">TPM,</font> e.g., allow the user to enable/disable or activate/deactivate the <font SIZE="-1">TPM.</font> Further, if <font SIZE="-1">TPM</font> ownership is released from within a <font SIZE="-1">VM</font> then the host&#8217;s <font SIZE="-1">TPM</font> will get disabled and deactivated. To enable and activate the <font SIZE="-1">TPM</font> again afterwards, the host has to be rebooted and the user is required to enter the firmware&#8217;s menu to enable and activate the <font SIZE="-1">TPM.</font> If the <font SIZE="-1">TPM</font> is left disabled and/or deactivated most <font SIZE="-1">TPM</font> commands will fail. </p>
<p> To create a passthrough <font SIZE="-1">TPM</font> use the following two options: </p>
<pre>
        -tpmdev passthrough,id=tpm0 -device tpm-tis,tpmdev=tpm0
</pre>
<p> Note that the <tt>&quot;-tpmdev&quot;</tt> id is <tt>&quot;tpm0&quot;</tt> and is referenced by <tt>&quot;tpmdev=tpm0&quot;</tt> in the device option.</dl>
<p> Linux/Multiboot boot specific: </p>
<p> When using these options, you can use a given Linux or Multiboot kernel without installing it in the disk image. It can be useful for easier testing of various kernels.</p>
<dl>
<dt><code>-kernel</code> <i>bzImage</i></p>
<dd> Use <i>bzImage</i> as kernel image. The kernel can be either a Linux kernel or in multiboot format.</p>
<dt><code>-append</code> <i>cmdline</i></p>
<dd> Use <i>cmdline</i> as kernel command line</p>
<dt><code>-initrd</code> <i>file</i></p>
<dd> Use <i>file</i> as initial ram disk.</p>
<dt><code>-initrd &quot;</code><i>file1</i> <code>arg=foo,</code><i>file2</i><code>&quot;</code></p>
<dd> This syntax is only available with multiboot. </p>
<p> Use <i>file1</i> and <i>file2</i> as modules and pass arg=foo as parameter to the first module.</p>
<dt><code>-dtb</code> <i>file</i></p>
<dd> Use <i>file</i> as a device tree binary (dtb) image and pass it to the kernel on boot.</dl>
<p> Debug/Expert options:</p>
<dl>
<dt><code>-serial</code> <i>dev</i></p>
<dd> Redirect the virtual serial port to host character device <i>dev</i>. The default device is <tt>&quot;vc&quot;</tt> in graphical mode and <tt>&quot;stdio&quot;</tt> in non graphical mode. </p>
<p> This option can be used several times to simulate up to 4 serial ports. </p>
<p> Use <tt>&quot;-serial none&quot;</tt> to disable all serial ports. </p>
<p> Available character devices are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>vc[:</code><i>W</i><code>x</code><i>H</i><code>]</code></p>
<dd> Virtual console. Optionally, a width and height can be given in pixel with </p>
<pre>
        vc:800x600
</pre>
<p> It is also possible to specify width or height in characters: </p>
<pre>
        vc:80Cx24C
</pre>
<dt><code>pty</code></p>
<dd> [Linux only] Pseudo <font SIZE="-1">TTY </font>(a new <font SIZE="-1">PTY</font> is automatically allocated)</p>
<dt><code>none</code></p>
<dd> No device is allocated.</p>
<dt><code>null</code></p>
<dd> void device</p>
<dt><code>chardev:</code><i>id</i></p>
<dd> Use a named character device defined with the <tt>&quot;-chardev&quot;</tt> option.</p>
<dt><code>/dev/XXX</code></p>
<dd> [Linux only] Use host tty, e.g. <i>/dev/ttyS0</i>. The host serial port parameters are set according to the emulated ones.</p>
<dt><code>/dev/parport</code><i>N</i></p>
<dd> [Linux only, parallel port only] Use host parallel port <i>N</i>. Currently <font SIZE="-1">SPP</font> and <font SIZE="-1">EPP</font> parallel port features can be used.</p>
<dt><code>file:</code><i>filename</i></p>
<dd> Write output to <i>filename</i>. No character can be read.</p>
<dt><code>stdio</code></p>
<dd> [Unix only] standard input/output</p>
<dt><code>pipe:</code><i>filename</i></p>
<dd> name pipe <i>filename</i></p>
<dt><font SIZE="-1"><code>COM</code></font><i>n</i></p>
<dd> [Windows only] Use host serial port <i>n</i></p>
<dt><code>udp:[</code><i>remote_host</i><code>]:</code><i>remote_port</i><code>[@[</code><i>src_ip</i><code>]:</code><i>src_port</i><code>]</code></p>
<dd> This implements <font SIZE="-1">UDP</font> Net Console. When <i>remote_host</i> or <i>src_ip</i> are not specified they default to <tt>0.0.0.0</tt>. When not using a specified <i>src_port</i> a random port is automatically chosen. </p>
<p> If you just want a simple readonly console you can use <tt>&quot;netcat&quot;</tt> or <tt>&quot;nc&quot;</tt>, by starting <font SIZE="-1">QEMU</font> with: <tt>&quot;-serial udp::4555&quot;</tt> and nc as: <tt>&quot;nc -u -l -p 4555&quot;</tt>. Any time <font SIZE="-1">QEMU</font> writes something to that port it will appear in the netconsole session. </p>
<p> If you plan to send characters back via netconsole or you want to stop and start <font SIZE="-1">QEMU</font> a lot of times, you should have <font SIZE="-1">QEMU</font> use the same source port each time by using something like <tt>&quot;-serial udp::4555 [at] 4556&quot;</tt> to <font SIZE="-1">QEMU.</font> Another approach is to use a patched version of netcat which can listen to a <font SIZE="-1">TCP</font> port and send and receive characters via udp. If you have a patched version of netcat which activates telnet remote echo and single char transfer, then you can use the following options to step up a netcat redirector to allow telnet on port 5555 to access the <font SIZE="-1">QEMU</font> port.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&quot;QEMU Options:&quot;</p>
<dd> -serial udp::4555 [at] 4556</p>
<dt>&quot;netcat options:&quot;</p>
<dd> -u -P 4555 -L 0.0.0.0:4556 -t -p 5555 -I -T</p>
<dt>&quot;telnet options:&quot;</p>
<dd> localhost 5555</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>tcp:[</code><i>host</i><code>]:</code><i>port</i><code>[,</code><i>server</i><code>][,nowait][,nodelay]</code></p>
<dd> The <font SIZE="-1">TCP</font> Net Console has two modes of operation. It can send the serial I/O to a location or wait for a connection from a location. By default the <font SIZE="-1">TCP</font> Net Console is sent to <i>host</i> at the <i>port</i>. If you use the <i>server</i> option <font SIZE="-1">QEMU</font> will wait for a client socket application to connect to the port before continuing, unless the <tt>&quot;nowait&quot;</tt> option was specified. The <tt>&quot;nodelay&quot;</tt> option disables the Nagle buffering algorithm. If <i>host</i> is omitted, 0.0.0.0 is assumed. Only one <font SIZE="-1">TCP</font> connection at a time is accepted. You can use <tt>&quot;telnet&quot;</tt> to connect to the corresponding character device.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&quot;Example to send tcp console to 192.168.0.2 port 4444&quot;</p>
<dd> -serial tcp:192.168.0.2:4444</p>
<dt>&quot;Example to listen and wait on port 4444 for connection&quot;</p>
<dd> -serial tcp::4444,server</p>
<dt>&quot;Example to not wait and listen on ip 192.168.0.100 port 4444&quot;</p>
<dd> -serial tcp:192.168.0.100:4444,server,nowait</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>telnet:</code><i>host</i><code>:</code><i>port</i><code>[,server][,nowait][,nodelay]</code></p>
<dd> The telnet protocol is used instead of raw tcp sockets. The options work the same as if you had specified <tt>&quot;-serial tcp&quot;</tt>. The difference is that the port acts like a telnet server or client using telnet option negotiation. This will also allow you to send the <font SIZE="-1">MAGIC_SYSRQ</font> sequence if you use a telnet that supports sending the break sequence. Typically in unix telnet you do it with Control-] and then type &#8220;send break&#8221; followed by pressing the enter key.</p>
<dt><code>unix:</code><i>path</i><code>[,server][,nowait]</code></p>
<dd> A unix domain socket is used instead of a tcp socket. The option works the same as if you had specified <tt>&quot;-serial tcp&quot;</tt> except the unix domain socket <i>path</i> is used for connections.</p>
<dt><code>mon:</code><i>dev_string</i></p>
<dd> This is a special option to allow the monitor to be multiplexed onto another serial port. The monitor is accessed with key sequence of <code>Control-a</code> and then pressing <code>c</code>. <i>dev_string</i> should be any one of the serial devices specified above. An example to multiplex the monitor onto a telnet server listening on port 4444 would be:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&quot;-serial mon:telnet::4444,server,nowait&quot;</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd>
<p> When the monitor is multiplexed to stdio in this way, Ctrl+C will not terminate <font SIZE="-1">QEMU</font> any more but will be passed to the guest instead.</dl>
<dt><code>braille</code></p>
<dd> Braille device. This will use BrlAPI to display the braille output on a real or fake device.</p>
<dt><code>msmouse</code></p>
<dd> Three button serial mouse. Configure the guest to use Microsoft protocol.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-parallel</code> <i>dev</i></p>
<dd> Redirect the virtual parallel port to host device <i>dev</i> (same devices as the serial port). On Linux hosts, <i>/dev/parportN</i> can be used to use hardware devices connected on the corresponding host parallel port. </p>
<p> This option can be used several times to simulate up to 3 parallel ports. </p>
<p> Use <tt>&quot;-parallel none&quot;</tt> to disable all parallel ports.</p>
<dt><code>-monitor</code> <i>dev</i></p>
<dd> Redirect the monitor to host device <i>dev</i> (same devices as the serial port). The default device is <tt>&quot;vc&quot;</tt> in graphical mode and <tt>&quot;stdio&quot;</tt> in non graphical mode. Use <tt>&quot;-monitor none&quot;</tt> to disable the default monitor.</p>
<dt><code>-qmp</code> <i>dev</i></p>
<dd> Like -monitor but opens in &#8216;control&#8217; mode.</p>
<dt><code>-mon [chardev=]name[,mode=readline|control][,default]</code></p>
<dd> Setup monitor on chardev <i>name</i>.</p>
<dt><code>-debugcon</code> <i>dev</i></p>
<dd> Redirect the debug console to host device <i>dev</i> (same devices as the serial port). The debug console is an I/O port which is typically port 0xe9; writing to that I/O port sends output to this device. The default device is <tt>&quot;vc&quot;</tt> in graphical mode and <tt>&quot;stdio&quot;</tt> in non graphical mode.</p>
<dt><code>-pidfile</code> <i>file</i></p>
<dd> Store the <font SIZE="-1">QEMU</font> process <font SIZE="-1">PID</font> in <i>file</i>. It is useful if you launch <font SIZE="-1">QEMU</font> from a script.</p>
<dt><code>-singlestep</code></p>
<dd> Run the emulation in single step mode.</p>
<dt><code>-S</code></p>
<dd> Do not start <font SIZE="-1">CPU</font> at startup (you must type &#8216;c&#8217; in the monitor).</p>
<dt><code>-realtime mlock=on|off</code></p>
<dd> Run qemu with realtime features. mlocking qemu and guest memory can be enabled via <code>mlock=on</code> (enabled by default).</p>
<dt><code>-gdb</code> <i>dev</i></p>
<dd> Wait for gdb connection on device <i>dev</i>. Typical connections will likely be TCP-based, but also <font SIZE="-1">UDP,</font> pseudo <font SIZE="-1">TTY,</font> or even stdio are reasonable use case. The latter is allowing to start <font SIZE="-1">QEMU</font> from within gdb and establish the connection via a pipe: </p>
<pre>
        (gdb) target remote | exec qemu-system-i386 -gdb stdio ...
</pre>
<dt><code>-s</code></p>
<dd> Shorthand for -gdb tcp::1234, i.e. open a gdbserver on <font SIZE="-1">TCP</font> port 1234.</p>
<dt><code>-d</code> <i>item1</i><code>[,&#8230;]</code></p>
<dd> Enable logging of specified items. Use &#8216;-d help&#8217; for a list of log items.</p>
<dt><code>-D</code> <i>logfile</i></p>
<dd> Output log in <i>logfile</i> instead of to stderr</p>
<dt><code>-L</code> <i>path</i></p>
<dd> Set the directory for the <font SIZE="-1">BIOS, VGA BIOS</font> and keymaps.</p>
<dt><code>-bios</code> <i>file</i></p>
<dd> Set the filename for the <font SIZE="-1">BIOS.</font></p>
<dt><code>-enable-kvm</code></p>
<dd> Enable <font SIZE="-1">KVM</font> full virtualization support. This option is only available if <font SIZE="-1">KVM</font> support is enabled when compiling.</p>
<dt><code>-xen-domid</code> <i>id</i></p>
<dd> Specify xen guest domain <i>id</i> (<font SIZE="-1">XEN</font> only).</p>
<dt><code>-xen-create</code></p>
<dd> Create domain using xen hypercalls, bypassing xend. Warning: should not be used when xend is in use (<font SIZE="-1">XEN</font> only).</p>
<dt><code>-xen-attach</code></p>
<dd> Attach to existing xen domain. xend will use this when starting <font SIZE="-1">QEMU </font>(<font SIZE="-1">XEN</font> only).</p>
<dt><code>-no-reboot</code></p>
<dd> Exit instead of rebooting.</p>
<dt><code>-no-shutdown</code></p>
<dd> Don&#8217;t exit <font SIZE="-1">QEMU</font> on guest shutdown, but instead only stop the emulation. This allows for instance switching to monitor to commit changes to the disk image.</p>
<dt><code>-loadvm</code> <i>file</i></p>
<dd> Start right away with a saved state (<tt>&quot;loadvm&quot;</tt> in monitor)</p>
<dt><code>-daemonize</code></p>
<dd> Daemonize the <font SIZE="-1">QEMU</font> process after initialization. <font SIZE="-1">QEMU</font> will not detach from standard <font SIZE="-1">IO</font> until it is ready to receive connections on any of its devices. This option is a useful way for external programs to launch <font SIZE="-1">QEMU</font> without having to cope with initialization race conditions.</p>
<dt><code>-option-rom</code> <i>file</i></p>
<dd> Load the contents of <i>file</i> as an option <font SIZE="-1">ROM.</font> This option is useful to load things like EtherBoot.</p>
<dt><code>-clock</code> <i>method</i></p>
<dd> Force the use of the given methods for timer alarm. To see what timers are available use <tt>&quot;-clock help&quot;</tt>.</p>
<dt><code>-rtc [base=utc|localtime|</code><i>date</i><code>][,clock=host|vm][,driftfix=none|slew]</code></p>
<dd> Specify <code>base</code> as <tt>&quot;utc&quot;</tt> or <tt>&quot;localtime&quot;</tt> to let the <font SIZE="-1">RTC</font> start at the current <font SIZE="-1">UTC</font> or local time, respectively. <tt>&quot;localtime&quot;</tt> is required for correct date in MS-DOS or Windows. To start at a specific point in time, provide <i>date</i> in the format <tt>&quot;2006-06-17T16:01:21&quot;</tt> or <tt>&quot;2006-06-17&quot;</tt>. The default base is <font SIZE="-1">UTC.</font> </p>
<p> By default the <font SIZE="-1">RTC</font> is driven by the host system time. This allows to use the <font SIZE="-1">RTC</font> as accurate reference clock inside the guest, specifically if the host time is smoothly following an accurate external reference clock, e.g. via <font SIZE="-1">NTP.</font> If you want to isolate the guest time from the host, you can set <code>clock</code> to <tt>&quot;rt&quot;</tt> instead. To even prevent it from progressing during suspension, you can set it to <tt>&quot;vm&quot;</tt>. </p>
<p> Enable <code>driftfix</code> (i386 targets only) if you experience time drift problems, specifically with Windows&#8217; <font SIZE="-1">ACPI HAL.</font> This option will try to figure out how many timer interrupts were not processed by the Windows guest and will re-inject them.</p>
<dt><code>-icount [</code><i>N</i><code>|auto]</code></p>
<dd> Enable virtual instruction counter. The virtual cpu will execute one instruction every 2^<i>N</i> ns of virtual time. If <tt>&quot;auto&quot;</tt> is specified then the virtual cpu speed will be automatically adjusted to keep virtual time within a few seconds of real time. </p>
<p> Note that while this option can give deterministic behavior, it does not provide cycle accurate emulation. Modern CPUs contain superscalar out of order cores with complex cache hierarchies. The number of instructions executed often has little or no correlation with actual performance.</p>
<dt><code>-watchdog</code> <i>model</i></p>
<dd> Create a virtual hardware watchdog device. Once enabled (by a guest action), the watchdog must be periodically polled by an agent inside the guest or else the guest will be restarted. </p>
<p> The <i>model</i> is the model of hardware watchdog to emulate. Choices for model are: <tt>&quot;ib700&quot;</tt> (iBASE 700) which is a very simple <font SIZE="-1">ISA</font> watchdog with a single timer, or <tt>&quot;i6300esb&quot;</tt> (Intel 6300ESB I/O controller hub) which is a much more featureful PCI-based dual-timer watchdog. Choose a model for which your guest has drivers. </p>
<p> Use <tt>&quot;-watchdog help&quot;</tt> to list available hardware models. Only one watchdog can be enabled for a guest.</p>
<dt><code>-watchdog-action</code> <i>action</i></p>
<dd> The <i>action</i> controls what <font SIZE="-1">QEMU</font> will do when the watchdog timer expires. The default is <tt>&quot;reset&quot;</tt> (forcefully reset the guest). Other possible actions are: <tt>&quot;shutdown&quot;</tt> (attempt to gracefully shutdown the guest), <tt>&quot;poweroff&quot;</tt> (forcefully poweroff the guest), <tt>&quot;pause&quot;</tt> (pause the guest), <tt>&quot;debug&quot;</tt> (print a debug message and continue), or <tt>&quot;none&quot;</tt> (do nothing). </p>
<p> Note that the <tt>&quot;shutdown&quot;</tt> action requires that the guest responds to <font SIZE="-1">ACPI</font> signals, which it may not be able to do in the sort of situations where the watchdog would have expired, and thus <tt>&quot;-watchdog-action shutdown&quot;</tt> is not recommended for production use. </p>
<p> Examples:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&quot;-watchdog i6300esb -watchdog-action pause&quot;</p>
<dd>
<dt>&quot;-watchdog ib700&quot;</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-echr</code> <i>numeric_ascii_value</i></p>
<dd> Change the escape character used for switching to the monitor when using monitor and serial sharing. The default is <tt>0x01</tt> when using the <tt>&quot;-nographic&quot;</tt> option. <tt>0x01</tt> is equal to pressing <tt>&quot;Control-a&quot;</tt>. You can select a different character from the ascii control keys where 1 through 26 map to Control-a through Control-z. For instance you could use the either of the following to change the escape character to Control-t.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&quot;-echr 0x14&quot;</p>
<dd>
<dt>&quot;-echr 20&quot;</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-virtioconsole</code> <i>c</i></p>
<dd> Set virtio console. </p>
<p> This option is maintained for backward compatibility. </p>
<p> Please use <tt>&quot;-device virtconsole&quot;</tt> for the new way of invocation.</p>
<dt><code>-show-cursor</code></p>
<dd> Show cursor.</p>
<dt><code>-tb-size</code> <i>n</i></p>
<dd> Set <font SIZE="-1">TB</font> size.</p>
<dt><code>-incoming</code> <i>port</i></p>
<dd> Prepare for incoming migration, listen on <i>port</i>.</p>
<dt><code>-nodefaults</code></p>
<dd> Don&#8217;t create default devices. Normally, <font SIZE="-1">QEMU</font> sets the default devices like serial port, parallel port, virtual console, monitor device, <font SIZE="-1">VGA</font> adapter, floppy and CD-ROM drive and others. The <tt>&quot;-nodefaults&quot;</tt> option will disable all those default devices.</p>
<dt><code>-chroot</code> <i>dir</i></p>
<dd> Immediately before starting guest execution, chroot to the specified directory. Especially useful in combination with -runas.</p>
<dt><code>-runas</code> <i>user</i></p>
<dd> Immediately before starting guest execution, drop root privileges, switching to the specified user.</p>
<dt><code>-prom-env</code> <i>variable</i><code>=</code><i>value</i></p>
<dd> Set OpenBIOS nvram <i>variable</i> to given <i>value</i> (<font SIZE="-1">PPC, SPARC</font> only).</p>
<dt><code>-semihosting</code></p>
<dd> Semihosting mode (<font SIZE="-1">ARM, M68K,</font> Xtensa only).</p>
<dt><code>-old-param</code></p>
<dd> Old param mode (<font SIZE="-1">ARM</font> only).</p>
<dt><code>-sandbox</code> <i>arg</i></p>
<dd> Enable Seccomp mode 2 system call filter. &#8216;on&#8217; will enable syscall filtering and &#8216;off&#8217; will disable it. The default is &#8216;off&#8217;.</p>
<dt><code>-readconfig</code> <i>file</i></p>
<dd> Read device configuration from <i>file</i>. This approach is useful when you want to spawn <font SIZE="-1">QEMU</font> process with many command line options but you don&#8217;t want to exceed the command line character limit.</p>
<dt><code>-writeconfig</code> <i>file</i></p>
<dd> Write device configuration to <i>file</i>. The <i>file</i> can be either filename to save command line and device configuration into file or dash <tt>&quot;-&quot;</tt>) character to print the output to stdout. This can be later used as input file for <tt>&quot;-readconfig&quot;</tt> option.</p>
<dt><code>-nodefconfig</code></p>
<dd> Normally <font SIZE="-1">QEMU</font> loads configuration files from <i>sysconfdir</i> and <i>datadir</i> at startup. The <tt>&quot;-nodefconfig&quot;</tt> option will prevent <font SIZE="-1">QEMU</font> from loading any of those config files.</p>
<dt><code>-no-user-config</code></p>
<dd> The <tt>&quot;-no-user-config&quot;</tt> option makes <font SIZE="-1">QEMU</font> not load any of the user-provided config files on <i>sysconfdir</i>, but won&#8217;t make it skip the QEMU-provided config files from <i>datadir</i>.</p>
<dt><code>-trace [events=</code><i>file</i><code>][,file=</code><i>file</i><code>]</code></p>
<dd> Specify tracing options.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>events=</code><i>file</i></p>
<dd> Immediately enable events listed in <i>file</i>. The file must contain one event name (as listed in the <i>trace-events</i> file) per line. This option is only available if <font SIZE="-1">QEMU</font> has been compiled with either <i>simple</i> or <i>stderr</i> tracing backend.</p>
<dt><code>file=</code><i>file</i></p>
<dd> Log output traces to <i>file</i>. </p>
<p> This option is only available if <font SIZE="-1">QEMU</font> has been compiled with the <i>simple</i> tracing backend.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-enable-fips</code></p>
<dd> Enable <font SIZE="-1">FIPS 140-2</font> compliance mode.</p>
<dt><code>-object</code> <i>typename</i><code>[,</code><i>prop1</i><code>=</code><i>value1</i><code>,&#8230;]</code></p>
<dd> Create an new object of type <i>typename</i> setting properties in the order they are specified. Note that the &#8216;id&#8217; property must be set. These objects are placed in the &#8216;/objects&#8217; path.</p>
<dt><code>-msg timestamp[=on|off]</code></p>
<dd> prepend a timestamp to each log message.(default:on)</dl>
<p> During the graphical emulation, you can use special key combinations to change modes. The default key mappings are shown below, but if you use <tt>&quot;-alt-grab&quot;</tt> then the modifier is Ctrl-Alt-Shift (instead of Ctrl-Alt) and if you use <tt>&quot;-ctrl-grab&quot;</tt> then the modifier is the right Ctrl key (instead of Ctrl-Alt):</p>
<dl>
<dt><code>Ctrl-Alt-f</code></p>
<dd> Toggle full screen</p>
<dt><code>Ctrl-Alt-+</code></p>
<dd> Enlarge the screen</p>
<dt><code>Ctrl-Alt&#8212;</code></p>
<dd> Shrink the screen</p>
<dt><code>Ctrl-Alt-u</code></p>
<dd> Restore the screen&#8217;s un-scaled dimensions</p>
<dt><code>Ctrl-Alt-n</code></p>
<dd> Switch to virtual console &#8216;n&#8217;. Standard console mappings are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>1</i></p>
<dd> Target system display</p>
<dt><i>2</i></p>
<dd> Monitor</p>
<dt><i>3</i></p>
<dd> Serial port</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>Ctrl-Alt</code></p>
<dd> Toggle mouse and keyboard grab.</dl>
<p> In the virtual consoles, you can use <code>Ctrl-Up</code>, <code>Ctrl-Down</code>, <code>Ctrl-PageUp</code> and <code>Ctrl-PageDown</code> to move in the back log. </p>
<p> During emulation, if you are using the <code>-nographic</code> option, use <code>Ctrl-a h</code> to get terminal commands:</p>
<dl>
<dt><code>Ctrl-a h</code></p>
<dd>
<dt><code>Ctrl-a ?</code></p>
<dd> Print this help</p>
<dt><code>Ctrl-a x</code></p>
<dd> Exit emulator</p>
<dt><code>Ctrl-a s</code></p>
<dd> Save disk data back to file (if -snapshot)</p>
<dt><code>Ctrl-a t</code></p>
<dd> Toggle console timestamps</p>
<dt><code>Ctrl-a b</code></p>
<dd> Send break (magic sysrq in Linux)</p>
<dt><code>Ctrl-a c</code></p>
<dd> Switch between console and monitor</p>
<dt><code>Ctrl-a Ctrl-a</code></p>
<dd> Send Ctrl-a</dl>
<p> The following options are specific to the PowerPC emulation:</p>
<dl>
<dt><code>-g</code> <i>W</i><code>x</code><i>H</i><code>[x</code><i></i><font SIZE="-1"><i>DEPTH</i></font><i></i><code>]</code></p>
<dd> Set the initial <font SIZE="-1">VGA</font> graphic mode. The default is 800x600x32.</p>
<dt><code>-prom-env</code> <i>string</i></p>
<dd> Set OpenBIOS variables in <font SIZE="-1">NVRAM,</font> for example: </p>
<pre>
        qemu-system-ppc -prom-env 'auto-boot?=false' \
         -prom-env 'boot-device=hd:2,\yaboot' \
         -prom-env 'boot-args=conf=hd:2,\yaboot.conf'
</pre>
<p> These variables are not used by Open Hack&#8217;Ware.</dl>
<p> The following options are specific to the Sparc32 emulation:</p>
<dl>
<dt><code>-g</code> <i>W</i><code>x</code><i>H</i><code>x[x</code><i></i><font SIZE="-1"><i>DEPTH</i></font><i></i><code>]</code></p>
<dd> Set the initial graphics mode. For <font SIZE="-1">TCX,</font> the default is 1024x768x8 with the option of 1024x768x24. For cgthree, the default is 1024x768x8 with the option of 1152x900x8 for people who wish to use <font SIZE="-1">OBP.</font></p>
<dt><code>-prom-env</code> <i>string</i></p>
<dd> Set OpenBIOS variables in <font SIZE="-1">NVRAM,</font> for example: </p>
<pre>
        qemu-system-sparc -prom-env 'auto-boot?=false' \
         -prom-env 'boot-device=sd(0,2,0):d' -prom-env 'boot-args=linux single'
</pre>
<dt><code>-M [SS-4|SS-5|SS-10|SS-20|SS-600MP|LX|Voyager|SPARCClassic] [|SPARCbook]</code></p>
<dd> Set the emulated machine type. Default is <font SIZE="-1">SS-5.</font></dl>
<p> The following options are specific to the Sparc64 emulation:</p>
<dl>
<dt><code>-prom-env</code> <i>string</i></p>
<dd> Set OpenBIOS variables in <font SIZE="-1">NVRAM,</font> for example: </p>
<pre>
        qemu-system-sparc64 -prom-env 'auto-boot?=false'
</pre>
<dt><code>-M [sun4u|sun4v|Niagara]</code></p>
<dd> Set the emulated machine type. The default is sun4u.</dl>
<h2>SEE ALSO</h2>
<p> The <font SIZE="-1">HTML</font> documentation of <font SIZE="-1">QEMU</font> for more precise information and Linux user mode emulator invocation.</p>
<h2>AUTHOR</h2>
<p> Fabrice Bellard </p>
<h2>Index</h2>
