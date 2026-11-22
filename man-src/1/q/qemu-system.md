---

title: "qemu-system(1)"
name: "qemu-system"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qemu-system/"
description: "qemu-doc – QEMU version 4.2.0 User Documentation"
---

<p> qemu-doc &#8211; QEMU version 4.2.0 User Documentation </p>
<h2>SYNOPSIS</h2>
<p> <code>qemu-system-x86_64</code> [<i>options</i>] [<i>disk_image</i>]</p>
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
<dd> IPMI BMC, either and internal or external one</dd>
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
<dd> PCI UHCI, OHCI, EHCI or XHCI USB controller and a virtual USB-1.1 hub.</dd></dl>
<p> SMP is supported with up to 255 CPUs. </p>
<p> QEMU uses the PC BIOS from the Seabios project and the Plex86/Bochs LGPL VGA BIOS. </p>
<p> QEMU uses YM3812 emulation by Tatsuyuki Satoh. </p>
<p> QEMU uses GUS emulation (GUSEMU32 &lt;<code><a rel="nofollow" href="http://www.deinmeister.de/gusemu/">http://www.deinmeister.de/gusemu/</a></code>&gt;) by Tibor &#8220;TS&#8221; Schütz. </p>
<p> Note that, by default, GUS shares <code>IRQ</code>(7) with parallel ports and so QEMU must be told to not have parallel ports to have working GUS. </p>
<pre>
        qemu-system-x86_64 dos.img -soundhw gus -parallel none
</pre>
<p> Alternatively: </p>
<pre>
        qemu-system-x86_64 dos.img -device gus,irq=5
</pre>
<p> Or some other unclaimed IRQ. </p>
<p> CS4231A is the chip used in Windows Sound System and GUSMAX products</p>
<h2>OPTIONS</h2>
<p> <i>disk_image</i> is a raw hard disk image for IDE hard disk 0. Some targets do not need a disk image. </p>
<p> <i>Standard options</i></p>
<dl>
<dt><code>-h</code></dt>
<dd> Display help and exit</dd>
<dt><code>-version</code></dt>
<dd> Display version information and exit</dd>
<dt><code>-machine [type=]</code><i>name</i><code>[,prop=</code><i>value</i><code>[,&#8230;]]</code></dt>
<dd> Select the emulated machine by <i>name</i>. Use <tt>&quot;-machine help&quot;</tt> to list available machines. </dd>
<p> For architectures which aim to support live migration compatibility across releases, each release will introduce a new versioned machine type. For example, the 2.8.0 release introduced machine types &#8220;pc-i440fx-2.8&#8221; and &#8220;pc-q35-2.8&#8221; for the x86_64/i686 architectures. </p>
<p> To allow live migration of guests from QEMU version 2.8.0, to QEMU version 2.9.0, the 2.9.0 version must support the &#8220;pc-i440fx-2.8&#8221; and &#8220;pc-q35-2.8&#8221; machines too. To allow users live migrating VMs to skip multiple intermediate releases when upgrading, new releases of QEMU will support machine types from many previous versions. </p>
<p> Supported machine properties are:</p>
<dl>
<dl>
<dt><code>accel=</code><i>accels1</i><code>[:</code><i>accels2</i><code>[:&#8230;]]</code></dt>
<dd> This is used to enable an accelerator. Depending on the target architecture, kvm, xen, hax, hvf, whpx or tcg can be available. By default, tcg is used. If there is more than one accelerator specified, the next one is used if the previous one fails to initialize.</dd>
<dt><code>kernel_irqchip=on|off</code></dt>
<dd> Controls in-kernel irqchip support for the chosen accelerator when available.</dd>
<dt><code>gfx_passthru=on|off</code></dt>
<dd> Enables IGD GFX passthrough support for the chosen machine when available.</dd>
<dt><code>vmport=on|off|auto</code></dt>
<dd> Enables emulation of VMWare IO port, for vmmouse etc. auto says to select the value based on accel. For accel=xen the default is off otherwise the default is on.</dd>
<dt><code>kvm_shadow_mem=size</code></dt>
<dd> Defines the size of the KVM shadow MMU.</dd>
<dt><code>dump-guest-core=on|off</code></dt>
<dd> Include guest memory in a core dump. The default is on.</dd>
<dt><code>mem-merge=on|off</code></dt>
<dd> Enables or disables memory merge support. This feature, when supported by the host, de-duplicates identical memory pages among VMs instances (enabled by default).</dd>
<dt><code>aes-key-wrap=on|off</code></dt>
<dd> Enables or disables AES key wrapping support on s390-ccw hosts. This feature controls whether AES wrapping keys will be created to allow execution of AES cryptographic functions. The default is on.</dd>
<dt><code>dea-key-wrap=on|off</code></dt>
<dd> Enables or disables DEA key wrapping support on s390-ccw hosts. This feature controls whether DEA wrapping keys will be created to allow execution of DEA cryptographic functions. The default is on.</dd>
<dt><code>nvdimm=on|off</code></dt>
<dd> Enables or disables NVDIMM support. The default is off.</dd>
<dt><code>enforce-config-section=on|off</code></dt>
<dd> If <code>enforce-config-section</code> is set to <i>on</i>, force migration code to send configuration section even if the machine-type sets the <code>migration.send-configuration</code> property to <i>off</i>. NOTE: this parameter is deprecated. Please use <code>-global</code> <code>migration.send-configuration</code>=<i>on|off</i> instead.</dd>
<dt><code>memory-encryption=</code></dt>
<dd> Memory encryption object to use. The default is none.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-cpu</code> <i>model</i></dt>
<dd> Select CPU model (<tt>&quot;-cpu help&quot;</tt> for list and additional feature selection)</dd>
<dt><code>-accel</code> <i>name</i><code>[,prop=</code><i>value</i><code>[,&#8230;]]</code></dt>
<dd> This is used to enable an accelerator. Depending on the target architecture, kvm, xen, hax, hvf, whpx or tcg can be available. By default, tcg is used. If there is more than one accelerator specified, the next one is used if the previous one fails to initialize.</dd>
<dl>
<dl>
<dt><code>thread=single|multi</code></dt>
<dd> Controls number of TCG threads. When the TCG is multi-threaded there will be one thread per vCPU therefor taking advantage of additional host cores. The default is to enable multi-threading where both the back-end and front-ends support it and no incompatible TCG features have been enabled (e.g. icount/replay).</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-smp [cpus=]</code><i>n</i><code>[,cores=</code><i>cores</i><code>][,threads=</code><i>threads</i><code>][,dies=dies][,sockets=</code><i>sockets</i><code>][,maxcpus=</code><i>maxcpus</i><code>]</code></dt>
<dd> Simulate an SMP system with <i>n</i> CPUs. On the PC target, up to 255 CPUs are supported. On Sparc32 target, Linux limits the number of usable CPUs to 4. For the PC target, the number of <i>cores</i> per die, the number of <i>threads</i> per cores, the number of <i>dies</i> per packages and the total number of <i>sockets</i> can be specified. Missing values will be computed. If any on the three values is given, the total number of CPUs <i>n</i> can be omitted. <i>maxcpus</i> specifies the maximum number of hotpluggable CPUs.</dd>
<dt><code>-numa node[,mem=</code><i>size</i><code>][,cpus=</code><i>firstcpu</i><code>[-</code><i>lastcpu</i><code>]][,nodeid=</code><i>node</i><code>]</code></dt>
<dd>
</dd><dt><code>-numa node[,memdev=</code><i>id</i><code>][,cpus=</code><i>firstcpu</i><code>[-</code><i>lastcpu</i><code>]][,nodeid=</code><i>node</i><code>]</code></dt>
<dd>
</dd><dt><code>-numa dist,src=</code><i>source</i><code>,dst=</code><i>destination</i><code>,val=</code><i>distance</i></dt>
<dd>
</dd><dt><code>-numa cpu,node-id=</code><i>node</i><code>[,socket-id=</code><i>x</i><code>][,core-id=</code><i>y</i><code>][,thread-id=</code><i>z</i><code>]</code></dt>
<dd> Define a NUMA node and assign RAM and VCPUs to it. Set the NUMA distance from a source node to a destination node. </dd>
<p> Legacy VCPU assignment uses <code>cpus</code> option where <i>firstcpu</i> and <i>lastcpu</i> are CPU indexes. Each <code>cpus</code> option represent a contiguous range of CPU indexes (or a single VCPU if <i>lastcpu</i> is omitted). A non-contiguous set of VCPUs can be represented by providing multiple <code>cpus</code> options. If <code>cpus</code> is omitted on all nodes, VCPUs are automatically split between them. </p>
<p> For example, the following option assigns VCPUs 0, 1, 2 and 5 to a NUMA node: </p>
<pre>
        -numa node,cpus=0-2,cpus=5
</pre>
<p> <code>cpu</code> option is a new alternative to <code>cpus</code> option which uses <code>socket-id|core-id|thread-id</code> properties to assign CPU objects to a <i>node</i> using topology layout properties of CPU. The set of properties is machine specific, and depends on used machine type/<code>smp</code> options. It could be queried with <code>hotpluggable-cpus</code> monitor command. <code>node-id</code> property specifies <i>node</i> to which CPU object will be assigned, it&#8217;s required for <i>node</i> to be declared with <code>node</code> option before it&#8217;s used with <code>cpu</code> option. </p>
<p> For example: </p>
<pre>
        -M pc \
        -smp 1,sockets=2,maxcpus=2 \
        -numa node,nodeid=0 -numa node,nodeid=1 \
        -numa cpu,node-id=0,socket-id=0 -numa cpu,node-id=1,socket-id=1
</pre>
<p> <code>mem</code> assigns a given RAM amount to a node. <code>memdev</code> assigns RAM from a given memory backend device to a node. If <code>mem</code> and <code>memdev</code> are omitted in all nodes, RAM is split equally between them. </p>
<p> <code>mem</code> and <code>memdev</code> are mutually exclusive. Furthermore, if one node uses <code>memdev</code>, all of them have to use it. </p>
<p> <i>source</i> and <i>destination</i> are NUMA node IDs. <i>distance</i> is the NUMA distance from <i>source</i> to <i>destination</i>. The distance from a node to itself is always 10. If any pair of nodes is given a distance, then all pairs must be given distances. Although, when distances are only given in one direction for each pair of nodes, then the distances in the opposite directions are assumed to be the same. If, however, an asymmetrical pair of distances is given for even one node pair, then all node pairs must be provided distance values for both directions, even when they are symmetrical. When a node is unreachable from another node, set the pair&#8217;s distance to 255. </p>
<p> Note that the &#8211;<code>numa</code> option doesn&#8217;t allocate any of the specified resources, it just assigns existing resources to NUMA nodes. This means that one still has to use the <code>-m</code>, <code>-smp</code> options to allocate RAM and VCPUs respectively.</p>
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
        qemu-system-x86_64 \
        -add-fd fd=3,set=2,opaque=&quot;rdwr:/path/to/file&quot; \
        -add-fd fd=4,set=2,opaque=&quot;rdonly:/path/to/file&quot; \
        -drive file=/dev/fdset/2,index=0,media=disk
</pre>
</dd></dl>
<dt><code>-set</code> <i>group</i><code>.</code><i>id</i><code>.</code><i>arg</i><code>=</code><i>value</i></dt>
<dd> Set parameter <i>arg</i> for item <i>id</i> of type <i>group</i></dd>
<dt><code>-global</code> <i>driver</i><code>.</code><i>prop</i><code>=</code><i>value</i></dt>
<dd>
</dd><dt><code>-global driver=</code><i>driver</i><code>,property=</code><i>property</i><code>,value=</code><i>value</i></dt>
<dd> Set default value of <i>driver</i>&#8216;s property <i>prop</i> to <i>value</i>, e.g.: </dd>
<pre>
        qemu-system-x86_64 -global ide-hd.physical_block_size=4096 disk-image.img
</pre>
<p> In particular, you can use this to set driver properties for devices which are created automatically by the machine model. To create a device which is not created automatically and set properties on it, use &#8211;<code>device</code>. </p>
<p> -global <i>driver</i>.<i>prop</i>=<i>value</i> is shorthand for -global driver=<i>driver</i>,property=<i>prop</i>,value=<i>value</i>. The longhand syntax works even when <i>driver</i> contains a dot.</p>
<dt><code>-boot [order=</code><i>drives</i><code>][,once=</code><i>drives</i><code>][,menu=on|off][,splash=</code><i>sp_name</i><code>][,splash-time=</code><i>sp_time</i><code>][,reboot-timeout=</code><i>rb_timeout</i><code>][,strict=on|off]</code></dt>
<dd> Specify boot order <i>drives</i> as a string of drive letters. Valid drive letters depend on the target architecture. The x86 PC uses: a, b (floppy 1 and 2), c (first hard disk), d (first CD-ROM), n-p (Etherboot from network adapter 1-4), hard disk boot is the default. To apply a particular boot order only on the first startup, specify it via <code>once</code>. Note that the <code>order</code> or <code>once</code> parameter should not be used together with the <code>bootindex</code> property of devices, since the firmware implementations normally do not support both at the same time. </dd>
<p> Interactive boot menus/prompts can be enabled via <code>menu=on</code> as far as firmware/BIOS supports them. The default is non-interactive boot. </p>
<p> A splash picture could be passed to bios, enabling user to show it as logo, when option splash=<i>sp_name</i> is given and menu=on, If firmware/BIOS supports them. Currently Seabios for X86 system support it. limitation: The splash file could be a jpeg file or a BMP file in 24 BPP format(true color). The resolution should be supported by the SVGA mode, so the recommended is 320&#215;240, 640&#215;480, 800&#215;640. </p>
<p> A timeout could be passed to bios, guest will pause for <i>rb_timeout</i> ms when boot failed, then reboot. If <code>reboot-timeout</code> is not set, guest will not reboot by default. Currently Seabios for X86 system support it. </p>
<p> Do strict boot via <code>strict=on</code> as far as firmware/BIOS supports it. This only effects when boot priority is changed by bootindex options. The default is non-strict boot. </p>
<pre>
        # try to boot from network first, then from hard disk
        qemu-system-x86_64 -boot order=nc
        # boot from CD-ROM first, switch back to default order after reboot
        qemu-system-x86_64 -boot once=d
        # boot with a splash picture for 5 seconds.
        qemu-system-x86_64 -boot menu=on,splash=/root/boot.bmp,splash-time=5000
</pre>
<p> Note: The legacy format &#8216;-boot <i>drives</i>&#8216; is still supported but its use is discouraged as it may be removed from future versions.</p>
<dt><code>-m [size=]</code><i>megs</i><code>[,slots=n,maxmem=size]</code></dt>
<dd> Sets guest startup RAM size to <i>megs</i> megabytes. Default is 128 MiB. Optionally, a suffix of &#8220;M&#8221; or &#8220;G&#8221; can be used to signify a value in megabytes or gigabytes respectively. Optional pair <i>slots</i>, <i>maxmem</i> could be used to set amount of hotpluggable memory slots and maximum amount of memory. Note that <i>maxmem</i> must be aligned to the page size. </dd>
<p> For example, the following command-line sets the guest startup RAM size to 1GB, creates 3 slots to hotplug additional memory and sets the maximum memory the guest can reach to 4GB: </p>
<pre>
        qemu-system-x86_64 -m 1G,slots=3,maxmem=4G
</pre>
<p> If <i>slots</i> and <i>maxmem</i> are not specified, memory hotplug won&#8217;t be enabled and the guest startup RAM will never increase.</p>
<dt><code>-mem-path</code> <i>path</i></dt>
<dd> Allocate guest RAM from a temporarily created file in <i>path</i>.</dd>
<dt><code>-mem-prealloc</code></dt>
<dd> Preallocate memory when using -mem-path.</dd>
<dt><code>-k</code> <i>language</i></dt>
<dd> Use keyboard layout <i>language</i> (for example <tt>&quot;fr&quot;</tt> for French). This option is only needed where it is not easy to get raw PC keycodes (e.g. on Macs, with some X11 servers or with a VNC or curses display). You don&#8217;t normally need to use it on PC/Linux or PC/Windows hosts. </dd>
<p> The available layouts are: </p>
<pre>
        ar  de-ch  es  fo     fr-ca  hu  ja  mk     no  pt-br  sv
        da  en-gb  et  fr     fr-ch  is  lt  nl     pl  ru     th
        de  en-us  fi  fr-be  hr     it  lv  nl-be  pt  sl     tr
</pre>
<p> The default is <tt>&quot;en-us&quot;</tt>.</p>
<dt><code>-audio-help</code></dt>
<dd> Will show the -audiodev equivalent of the currently specified (deprecated) environment variables.</dd>
<dt><code>-audiodev [driver=]</code><i>driver</i><code>,id=</code><i>id</i><code>[,</code><i>prop</i><code>[=</code><i>value</i><code>][,&#8230;]]</code></dt>
<dd> Adds a new audio backend <i>driver</i> identified by <i>id</i>. There are global and driver specific properties. Some values can be set differently for input and output, they&#8217;re marked with <tt>&quot;in|out.&quot;</tt>. You can set the input&#8217;s property with <tt>&quot;in.</tt>prop<tt>&quot;</tt> and the output&#8217;s property with <tt>&quot;out.</tt>prop<tt>&quot;</tt>. For example: </dd>
<pre>
        -audiodev alsa,id=example,in.frequency=44110,out.frequency=8000
        -audiodev alsa,id=example,out.channels=1 # leaves in.channels unspecified
</pre>
<p> NOTE: parameter validation is known to be incomplete, in many cases specifying an invalid option causes QEMU to print an error message and continue emulation without sound. </p>
<p> Valid global options are:</p>
<dl>
<dl>
<dt><code>id=</code><i>identifier</i></dt>
<dd> Identifies the audio backend.</dd>
<dt><code>timer-period=</code><i>period</i></dt>
<dd> Sets the timer <i>period</i> used by the audio subsystem in microseconds. Default is 10000 (10 ms).</dd>
<dt><code>in|out.mixing-engine=on|off</code></dt>
<dd> Use QEMU&#8216;s mixing engine to mix all streams inside QEMU and convert audio formats when not supported by the backend. When off, <i>fixed-settings</i> must be off too. Note that disabling this option means that the selected backend must support multiple streams and the audio formats used by the virtual cards, otherwise you&#8217;ll get no sound. It&#8217;s not recommended to disable this option unless you want to use 5.1 or 7.1 audio, as mixing engine only supports mono and stereo audio. Default is on.</dd>
<dt><code>in|out.fixed-settings=on|off</code></dt>
<dd> Use fixed settings for host audio. When off, it will change based on how the guest opens the sound card. In this case you must not specify <i>frequency</i>, <i>channels</i> or <i>format</i>. Default is on.</dd>
<dt><code>in|out.frequency=</code><i>frequency</i></dt>
<dd> Specify the <i>frequency</i> to use when using <i>fixed-settings</i>. Default is 44100Hz.</dd>
<dt><code>in|out.channels=</code><i>channels</i></dt>
<dd> Specify the number of <i>channels</i> to use when using <i>fixed-settings</i>. Default is 2 (stereo).</dd>
<dt><code>in|out.format=</code><i>format</i></dt>
<dd> Specify the sample <i>format</i> to use when using <i>fixed-settings</i>. Valid values are: <tt>&quot;s8&quot;</tt>, <tt>&quot;s16&quot;</tt>, <tt>&quot;s32&quot;</tt>, <tt>&quot;u8&quot;</tt>, <tt>&quot;u16&quot;</tt>, <tt>&quot;u32&quot;</tt>. Default is <tt>&quot;s16&quot;</tt>.</dd>
<dt><code>in|out.voices=</code><i>voices</i></dt>
<dd> Specify the number of <i>voices</i> to use. Default is 1.</dd>
<dt><code>in|out.buffer-length=</code><i>usecs</i></dt>
<dd> Sets the size of the buffer in microseconds.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-audiodev none,id=</code><i>id</i><code>[,</code><i>prop</i><code>[=</code><i>value</i><code>][,&#8230;]]</code></dt>
<dd> Creates a dummy backend that discards all outputs. This backend has no backend specific properties.</dd>
<dt><code>-audiodev alsa,id=</code><i>id</i><code>[,</code><i>prop</i><code>[=</code><i>value</i><code>][,&#8230;]]</code></dt>
<dd> Creates backend using the ALSA. This backend is only available on Linux. </dd>
<p> ALSA specific options are:</p>
<dl>
<dl>
<dt><code>in|out.dev=</code><i>device</i></dt>
<dd> Specify the ALSA <i>device</i> to use for input and/or output. Default is <tt>&quot;default&quot;</tt>.</dd>
<dt><code>in|out.period-length=</code><i>usecs</i></dt>
<dd> Sets the period length in microseconds.</dd>
<dt><code>in|out.try-poll=on|off</code></dt>
<dd> Attempt to use poll mode with the device. Default is on.</dd>
<dt><code>threshold=</code><i>threshold</i></dt>
<dd> Threshold (in microseconds) when playback starts. Default is 0.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-audiodev coreaudio,id=</code><i>id</i><code>[,</code><i>prop</i><code>[=</code><i>value</i><code>][,&#8230;]]</code></dt>
<dd> Creates a backend using Apple&#8217;s Core Audio. This backend is only available on Mac OS and only supports playback. </dd>
<p> Core Audio specific options are:</p>
<dl>
<dl>
<dt><code>in|out.buffer-count=</code><i>count</i></dt>
<dd> Sets the <i>count</i> of the buffers.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-audiodev dsound,id=</code><i>id</i><code>[,</code><i>prop</i><code>[=</code><i>value</i><code>][,&#8230;]]</code></dt>
<dd> Creates a backend using Microsoft&#8217;s DirectSound. This backend is only available on Windows and only supports playback. </dd>
<p> DirectSound specific options are:</p>
<dl>
<dl>
<dt><code>latency=</code><i>usecs</i></dt>
<dd> Add extra <i>usecs</i> microseconds latency to playback. Default is 10000 (10 ms).</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-audiodev oss,id=</code><i>id</i><code>[,</code><i>prop</i><code>[=</code><i>value</i><code>][,&#8230;]]</code></dt>
<dd> Creates a backend using OSS. This backend is available on most Unix-like systems. </dd>
<p> OSS specific options are:</p>
<dl>
<dl>
<dt><code>in|out.dev=</code><i>device</i></dt>
<dd> Specify the file name of the OSS <i>device</i> to use. Default is <tt>&quot;/dev/dsp&quot;</tt>.</dd>
<dt><code>in|out.buffer-count=</code><i>count</i></dt>
<dd> Sets the <i>count</i> of the buffers.</dd>
<dt><code>in|out.try-poll=on|of</code></dt>
<dd> Attempt to use poll mode with the device. Default is on.</dd>
<dt><code>try-mmap=on|off</code></dt>
<dd> Try using memory mapped device access. Default is off.</dd>
<dt><code>exclusive=on|off</code></dt>
<dd> Open the device in exclusive mode (vmix won&#8217;t work in this case). Default is off.</dd>
<dt><code>dsp-policy=</code><i>policy</i></dt>
<dd> Sets the timing policy (between 0 and 10, where smaller number means smaller latency but higher CPU usage). Use -1 to use buffer sizes specified by <tt>&quot;buffer&quot;</tt> and <tt>&quot;buffer-count&quot;</tt>. This option is ignored if you do not have OSS 4. Default is 5.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-audiodev pa,id=</code><i>id</i><code>[,</code><i>prop</i><code>[=</code><i>value</i><code>][,&#8230;]]</code></dt>
<dd> Creates a backend using PulseAudio. This backend is available on most systems. </dd>
<p> PulseAudio specific options are:</p>
<dl>
<dl>
<dt><code>server=</code><i>server</i></dt>
<dd> Sets the PulseAudio <i>server</i> to connect to.</dd>
<dt><code>in|out.name=</code><i>sink</i></dt>
<dd> Use the specified source/sink for recording/playback.</dd>
<dt><code>in|out.latency=</code><i>usecs</i></dt>
<dd> Desired latency in microseconds. The PulseAudio server will try to honor this value but actual latencies may be lower or higher.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-audiodev sdl,id=</code><i>id</i><code>[,</code><i>prop</i><code>[=</code><i>value</i><code>][,&#8230;]]</code></dt>
<dd> Creates a backend using SDL. This backend is available on most systems, but you should use your platform&#8217;s native backend if possible. This backend has no backend specific properties.</dd>
<dt><code>-audiodev spice,id=</code><i>id</i><code>[,</code><i>prop</i><code>[=</code><i>value</i><code>][,&#8230;]]</code></dt>
<dd> Creates a backend that sends audio through SPICE. This backend requires <tt>&quot;-spice&quot;</tt> and automatically selected in that case, so usually you can ignore this option. This backend has no backend specific properties.</dd>
<dt><code>-audiodev wav,id=</code><i>id</i><code>[,</code><i>prop</i><code>[=</code><i>value</i><code>][,&#8230;]]</code></dt>
<dd> Creates a backend that writes audio to a WAV file. </dd>
<p> Backend specific options are:</p>
<dl>
<dl>
<dt><code>path=</code><i>path</i></dt>
<dd> Write recorded audio into the specified file. Default is <tt>&quot;qemu.wav&quot;</tt>.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-soundhw</code> <i>card1</i><code>[,</code><i>card2</i><code>,&#8230;] or -soundhw all</code></dt>
<dd> Enable audio and selected sound hardware. Use &#8216;help&#8217; to print all available sound hardware. For example: </dd>
<pre>
        qemu-system-x86_64 -soundhw sb16,adlib disk.img
        qemu-system-x86_64 -soundhw es1370 disk.img
        qemu-system-x86_64 -soundhw ac97 disk.img
        qemu-system-x86_64 -soundhw hda disk.img
        qemu-system-x86_64 -soundhw all disk.img
        qemu-system-x86_64 -soundhw help
</pre>
<p> Note that Linux&#8217;s i810_audio OSS kernel (for AC97) module might require manually specifying clocking. </p>
<pre>
        modprobe i810_audio clocking=48000
</pre>
<dt><code>-device</code> <i>driver</i><code>[,</code><i>prop</i><code>[=</code><i>value</i><code>][,&#8230;]]</code></dt>
<dd> Add device <i>driver</i>. <i>prop</i>=<i>value</i> sets driver properties. Valid properties depend on the driver. To get help on possible drivers and properties, use <tt>&quot;-device help&quot;</tt> and <tt>&quot;-device </tt>driver<tt>,help&quot;</tt>. </dd>
<p> Some drivers are:</p>
<dt><code>-device ipmi-bmc-sim,id=</code><i>id</i><code>[,slave_addr=</code><i>val</i><code>][,sdrfile=</code><i>file</i><code>][,furareasize=</code><i>val</i><code>][,furdatafile=</code><i>file</i><code>][,guid=</code><i>uuid</i><code>]</code></dt>
<dd> Add an IPMI BMC. This is a simulation of a hardware management interface processor that normally sits on a system. It provides a watchdog and the ability to reset and power control the system. You need to connect this to an IPMI interface to make it useful </dd>
<p> The IPMI slave address to use for the BMC. The default is 0x20. This address is the BMC&#8216;s address on the I2C network of management controllers. If you don&#8217;t know what this means, it is safe to ignore it.</p>
<dl>
<dl>
<dt><code>id=</code><i>id</i></dt>
<dd> The BMC id for interfaces to use this device.</dd>
<dt><code>slave_addr=</code><i>val</i></dt>
<dd> Define slave address to use for the BMC. The default is 0x20.</dd>
<dt><code>sdrfile=</code><i>file</i></dt>
<dd> file containing raw Sensor Data Records (SDR) data. The default is none.</dd>
<dt><code>fruareasize=</code><i>val</i></dt>
<dd> size of a Field Replaceable Unit (FRU) area. The default is 1024.</dd>
<dt><code>frudatafile=</code><i>file</i></dt>
<dd> file containing raw Field Replaceable Unit (FRU) inventory data. The default is none.</dd>
<dt><code>guid=</code><i>uuid</i></dt>
<dd> value for the GUID for the BMC, in standard UUID format. If this is set, get &#8220;Get GUID&#8221; command to the BMC will return it. Otherwise &#8220;Get GUID&#8221; will return an error.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-device ipmi-bmc-extern,id=</code><i>id</i><code>,chardev=</code><i>id</i><code>[,slave_addr=</code><i>val</i><code>]</code></dt>
<dd> Add a connection to an external IPMI BMC simulator. Instead of locally emulating the BMC like the above item, instead connect to an external entity that provides the IPMI services. </dd>
<p> A connection is made to an external BMC simulator. If you do this, it is strongly recommended that you use the &#8220;reconnect=&#8221; chardev option to reconnect to the simulator if the connection is lost. Note that if this is not used carefully, it can be a security issue, as the interface has the ability to send resets, NMIs, and power off the VM. It&#8217;s best if QEMU makes a connection to an external simulator running on a secure port on localhost, so neither the simulator nor QEMU is exposed to any outside network. </p>
<p> See the &#8220;lanserv/README.vm&#8221; file in the OpenIPMI library for more details on the external interface.</p>
<dt><code>-device isa-ipmi-kcs,bmc=</code><i>id</i><code>[,ioport=</code><i>val</i><code>][,irq=</code><i>val</i><code>]</code></dt>
<dd> Add a KCS IPMI interafce on the ISA bus. This also adds a corresponding ACPI and SMBIOS entries, if appropriate.</dd>
<dl>
<dl>
<dt><code>bmc=</code><i>id</i></dt>
<dd> The BMC to connect to, one of ipmi-bmc-sim or ipmi-bmc-extern above.</dd>
<dt><code>ioport=</code><i>val</i></dt>
<dd> Define the I/O address of the interface. The default is 0xca0 for KCS.</dd>
<dt><code>irq=</code><i>val</i></dt>
<dd> Define the interrupt to use. The default is 5. To disable interrupts, set this to 0.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-device isa-ipmi-bt,bmc=</code><i>id</i><code>[,ioport=</code><i>val</i><code>][,irq=</code><i>val</i><code>]</code></dt>
<dd> Like the KCS interface, but defines a BT interface. The default port is 0xe4 and the default interrupt is 5.</dd>
<dt><code>-name</code> <i>name</i></dt>
<dd> Sets the <i>name</i> of the guest. This name will be displayed in the SDL window caption. The <i>name</i> will also be used for the VNC server. Also optionally set the top visible process name in Linux. Naming of individual threads can also be enabled on Linux to aid debugging.</dd>
<dt><code>-uuid</code> <i>uuid</i></dt>
<dd> Set system UUID.</dd></dl>
<p> <i>Block device options</i></p>
<dl>
<dt><code>-fda</code> <i>file</i></dt>
<dd>
</dd><dt><code>-fdb</code> <i>file</i></dt>
<dd> Use <i>file</i> as floppy disk 0/1 image.</dd>
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
<dt><code>-blockdev</code> <i>option</i><code>[,</code><i>option</i><code>[,</code><i>option</i><code>[,&#8230;]]]</code></dt>
<dd> Define a new block driver node. Some of the options apply to all block drivers, other options are only accepted for a specific block driver. See below for a list of generic options and options for the most common block drivers. </dd>
<p> Options that expect a reference to another node (e.g. <tt>&quot;file&quot;</tt>) can be given in two ways. Either you specify the node name of an already existing node (file=<i>node-name</i>), or you define a new node inline, adding options for the referenced node after a dot (file.filename=<i>path</i>,file.aio=native). </p>
<p> A block driver node created with <code>-blockdev</code> can be used for a guest device by specifying its node name for the <tt>&quot;drive&quot;</tt> property in a <code>-device</code> argument that defines a block device.</p>
<dl>
<dl>
<dt><code>Valid options for any block driver node:</code></dt>
<dd>
</dd><dl>
<dl>
<dt>&quot;driver&quot;</dt>
<dd> Specifies the block driver to use for the given node.</dd>
<dt>&quot;node-name&quot;</dt>
<dd> This defines the name of the block driver node by which it will be referenced later. The name must be unique, i.e. it must not match the name of a different block driver node, or (if you use <code>-drive</code> as well) the ID of a drive. </dd>
<p> If no node name is specified, it is automatically generated. The generated node name is not intended to be predictable and changes between QEMU invocations. For the top level, an explicit node name must be specified.</p>
<dt>&quot;read-only&quot;</dt>
<dd> Open the node read-only. Guest write attempts will fail. </dd>
<p> Note that some block drivers support only read-only access, either generally or in certain configurations. In this case, the default value <code>read-only=off</code> does not work and the option must be specified explicitly.</p>
<dt>&quot;auto-read-only&quot;</dt>
<dd> If <code>auto-read-only=on</code> is set, QEMU may fall back to read-only usage even when <code>read-only=off</code> is requested, or even switch between modes as needed, e.g. depending on whether the image file is writable or whether a writing user is attached to the node.</dd>
<dt>&quot;force-share&quot;</dt>
<dd> Override the image locking system of QEMU by forcing the node to utilize weaker shared access for permissions where it would normally request exclusive access. When there is the potential for multiple instances to have the same file open (whether this invocation of QEMU is the first or the second instance), both instances must permit shared access for the second instance to succeed at opening the file. </dd>
<p> Enabling <code>force-share=on</code> requires <code>read-only=on</code>.</p>
<dt>&quot;cache.direct&quot;</dt>
<dd> The host page cache can be avoided with <code>cache.direct=on</code>. This will attempt to do disk IO directly to the guest&#8217;s memory. QEMU may still perform an internal copy of the data.</dd>
<dt>&quot;cache.no-flush&quot;</dt>
<dd> In case you don&#8217;t care about data integrity over host failures, you can use <code>cache.no-flush=on</code>. This option tells QEMU that it never needs to write any data to the disk but can instead keep things in cache. If anything goes wrong, like your host losing power, the disk storage getting disconnected accidentally, etc. your image will most probably be rendered unusable.</dd>
<dt>&quot;discard=<i>discard</i>&quot;</dt>
<dd> <i>discard</i> is one of &#8220;ignore&#8221; (or &#8220;off&#8221;) or &#8220;unmap&#8221; (or &#8220;on&#8221;) and controls whether <tt>&quot;discard&quot;</tt> (also known as <tt>&quot;trim&quot;</tt> or <tt>&quot;unmap&quot;</tt>) requests are ignored or passed to the filesystem. Some machine types may not support discard requests.</dd>
<dt>&quot;detect-zeroes=<i>detect-zeroes</i>&quot;</dt>
<dd> <i>detect-zeroes</i> is &#8220;off&#8221;, &#8220;on&#8221; or &#8220;unmap&#8221; and enables the automatic conversion of plain zero writes by the OS to driver specific optimized zero write commands. You may even choose &#8220;unmap&#8221; if <i>discard</i> is set to &#8220;unmap&#8221; to allow a zero write to be converted to an <tt>&quot;unmap&quot;</tt> operation.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>Driver-specific options for </code>&quot;file&quot;</dt>
<dd> This is the protocol-level block driver for accessing regular files.</dd>
<dl>
<dl>
<dt>&quot;filename&quot;</dt>
<dd> The path to the image file in the local filesystem</dd>
<dt>&quot;aio&quot;</dt>
<dd> Specifies the AIO backend (threads/native, default: threads)</dd>
<dt>&quot;locking&quot;</dt>
<dd> Specifies whether the image file is protected with Linux OFD / POSIX locks. The default is to use the Linux Open File Descriptor API if available, otherwise no lock is applied. (auto/on/off, default: auto)</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> Example: </p>
<pre>
        -blockdev driver=file,node-name=disk,filename=disk.img
</pre>
</dd></dl>
<dt><code>Driver-specific options for </code>&quot;raw&quot;</dt>
<dd> This is the image format block driver for raw images. It is usually stacked on top of a protocol level block driver such as <tt>&quot;file&quot;</tt>.</dd>
<dl>
<dl>
<dt>&quot;file&quot;</dt>
<dd> Reference to or definition of the data source block driver node (e.g. a <tt>&quot;file&quot;</tt> driver node)</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> Example 1: </p>
<pre>
        -blockdev driver=file,node-name=disk_file,filename=disk.img
        -blockdev driver=raw,node-name=disk,file=disk_file
</pre>
<p> Example 2: </p>
<pre>
        -blockdev driver=raw,node-name=disk,file.driver=file,file.filename=disk.img
</pre>
</dd></dl>
<dt><code>Driver-specific options for </code>&quot;qcow2&quot;</dt>
<dd> This is the image format block driver for qcow2 images. It is usually stacked on top of a protocol level block driver such as <tt>&quot;file&quot;</tt>.</dd>
<dl>
<dl>
<dt>&quot;file&quot;</dt>
<dd> Reference to or definition of the data source block driver node (e.g. a <tt>&quot;file&quot;</tt> driver node)</dd>
<dt>&quot;backing&quot;</dt>
<dd> Reference to or definition of the backing file block device (default is taken from the image file). It is allowed to pass <tt>&quot;null&quot;</tt> here in order to disable the default backing file.</dd>
<dt>&quot;lazy-refcounts&quot;</dt>
<dd> Whether to enable the lazy refcounts feature (on/off; default is taken from the image file)</dd>
<dt>&quot;cache-size&quot;</dt>
<dd> The maximum total size of the L2 table and refcount block caches in bytes (default: the sum of l2-cache-size and refcount-cache-size)</dd>
<dt>&quot;l2-cache-size&quot;</dt>
<dd> The maximum size of the L2 table cache in bytes (default: if cache-size is not specified &#8211; 32M on Linux platforms, and 8M on non-Linux platforms; otherwise, as large as possible within the cache-size, while permitting the requested or the minimal refcount cache size)</dd>
<dt>&quot;refcount-cache-size&quot;</dt>
<dd> The maximum size of the refcount block cache in bytes (default: 4 times the cluster size; or if cache-size is specified, the part of it which is not used for the L2 cache)</dd>
<dt>&quot;cache-clean-interval&quot;</dt>
<dd> Clean unused entries in the L2 and refcount caches. The interval is in seconds. The default value is 600 on supporting platforms, and 0 on other platforms. Setting it to 0 disables this feature.</dd>
<dt>&quot;pass-discard-request&quot;</dt>
<dd> Whether discard requests to the qcow2 device should be forwarded to the data source (on/off; default: on if discard=unmap is specified, off otherwise)</dd>
<dt>&quot;pass-discard-snapshot&quot;</dt>
<dd> Whether discard requests for the data source should be issued when a snapshot operation (e.g. deleting a snapshot) frees clusters in the qcow2 file (on/off; default: on)</dd>
<dt>&quot;pass-discard-other&quot;</dt>
<dd> Whether discard requests for the data source should be issued on other occasions where a cluster gets freed (on/off; default: off)</dd>
<dt>&quot;overlap-check&quot;</dt>
<dd> Which overlap checks to perform for writes to the image (none/constant/cached/all; default: cached). For details or finer granularity control refer to the QAPI documentation of <tt>&quot;blockdev-add&quot;</tt>.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> Example 1: </p>
<pre>
        -blockdev driver=file,node-name=my_file,filename=/tmp/disk.qcow2
        -blockdev driver=qcow2,node-name=hda,file=my_file,overlap-check=none,cache-size=16777216
</pre>
<p> Example 2: </p>
<pre>
        -blockdev driver=qcow2,node-name=disk,file.driver=http,file.filename=<a rel="nofollow" href="http://example.com/image.qcow2">http://example.com/image.qcow2</a>
</pre>
</dd></dl>
<dt><code>Driver-specific options for other drivers</code></dt>
<dd> Please refer to the QAPI documentation of the <tt>&quot;blockdev-add&quot;</tt> QMP command.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-drive</code> <i>option</i><code>[,</code><i>option</i><code>[,</code><i>option</i><code>[,&#8230;]]]</code></dt>
<dd> Define a new drive. This includes creating a block driver node (the backend) as well as a guest device, and is mostly a shortcut for defining the corresponding <code>-blockdev</code> and <code>-device</code> options. </dd>
<p> <code>-drive</code> accepts all options that are accepted by <code>-blockdev</code>. In addition, it knows the following options:</p>
<dl>
<dl>
<dt><code>file=</code><i>file</i></dt>
<dd> This option defines which disk image to use with this drive. If the filename contains comma, you must double it (for instance, &#8220;file=my,,file&#8221; to use file &#8220;my,file&#8221;). </dd>
<p> Special files such as iSCSI devices can be specified using protocol specific URLs. See the section for &#8220;Device URL Syntax&#8221; for more information.</p>
<dt><code>if=</code><i>interface</i></dt>
<dd> This option defines on which type on interface the drive is connected. Available types are: ide, scsi, sd, mtd, floppy, pflash, virtio, none.</dd>
<dt><code>bus=</code><i>bus</i><code>,unit=</code><i>unit</i></dt>
<dd> These options define where is connected the drive by defining the bus number and the unit id.</dd>
<dt><code>index=</code><i>index</i></dt>
<dd> This option defines where is connected the drive by using an index in the list of available connectors of a given interface type.</dd>
<dt><code>media=</code><i>media</i></dt>
<dd> This option defines the type of the media: disk or cdrom.</dd>
<dt><code>snapshot=</code><i>snapshot</i></dt>
<dd> <i>snapshot</i> is &#8220;on&#8221; or &#8220;off&#8221; and controls snapshot mode for the given drive (see <code>-snapshot</code>).</dd>
<dt><code>cache=</code><i>cache</i></dt>
<dd> <i>cache</i> is &#8220;none&#8221;, &#8220;writeback&#8221;, &#8220;unsafe&#8221;, &#8220;directsync&#8221; or &#8220;writethrough&#8221; and controls how the host cache is used to access block data. This is a shortcut that sets the <code>cache.direct</code> and <code>cache.no-flush</code> options (as in <code>-blockdev</code>), and additionally <code>cache.writeback</code>, which provides a default for the <code>write-cache</code> option of block guest devices (as in <code>-device</code>). The modes correspond to the following settings: </dd>
<pre>
                     │ cache.writeback   cache.direct   cache.no-flush
        ─────────────┼─────────────────────────────────────────────────
        writeback    │ on                off            off
        none         │ on                on             off
        writethrough │ off               off            off
        directsync   │ off               on             off
        unsafe       │ on                off            on
</pre>
<p> The default mode is <code>cache=writeback</code>.</p>
<dt><code>aio=</code><i>aio</i></dt>
<dd> <i>aio</i> is &#8220;threads&#8221;, or &#8220;native&#8221; and selects between pthread based disk I/O and native Linux AIO.</dd>
<dt><code>format=</code><i>format</i></dt>
<dd> Specify which disk <i>format</i> will be used rather than detecting the format. Can be used to specify format=raw to avoid interpreting an untrusted format header.</dd>
<dt><code>werror=</code><i>action</i><code>,rerror=</code><i>action</i></dt>
<dd> Specify which <i>action</i> to take on write and read errors. Valid actions are: &#8220;ignore&#8221; (ignore the error and try to continue), &#8220;stop&#8221; (pause QEMU), &#8220;report&#8221; (report the error to the guest), &#8220;enospc&#8221; (pause QEMU only if the host disk is full; report the error to the guest otherwise). The default setting is <code>werror=enospc</code> and <code>rerror=report</code>.</dd>
<dt><code>copy-on-read=</code><i>copy-on-read</i></dt>
<dd> <i>copy-on-read</i> is &#8220;on&#8221; or &#8220;off&#8221; and enables whether to copy read backing file sectors into the image file.</dd>
<dt><code>bps=</code><i>b</i><code>,bps_rd=</code><i>r</i><code>,bps_wr=</code><i>w</i></dt>
<dd> Specify bandwidth throttling limits in bytes per second, either for all request types or for reads or writes only. Small values can lead to timeouts or hangs inside the guest. A safe minimum for disks is 2 MB/s.</dd>
<dt><code>bps_max=</code><i>bm</i><code>,bps_rd_max=</code><i>rm</i><code>,bps_wr_max=</code><i>wm</i></dt>
<dd> Specify bursts in bytes per second, either for all request types or for reads or writes only. Bursts allow the guest I/O to spike above the limit temporarily.</dd>
<dt><code>iops=</code><i>i</i><code>,iops_rd=</code><i>r</i><code>,iops_wr=</code><i>w</i></dt>
<dd> Specify request rate limits in requests per second, either for all request types or for reads or writes only.</dd>
<dt><code>iops_max=</code><i>bm</i><code>,iops_rd_max=</code><i>rm</i><code>,iops_wr_max=</code><i>wm</i></dt>
<dd> Specify bursts in requests per second, either for all request types or for reads or writes only. Bursts allow the guest I/O to spike above the limit temporarily.</dd>
<dt><code>iops_size=</code><i>is</i></dt>
<dd> Let every <i>is</i> bytes of a request count as a new request for iops throttling purposes. Use this option to prevent guests from circumventing iops limits by sending fewer but larger requests.</dd>
<dt><code>group=</code><i>g</i></dt>
<dd> Join a throttling quota group with given name <i>g</i>. All drives that are members of the same group are accounted for together. Use this option to prevent guests from circumventing throttling limits by using many small disks instead of a single larger disk.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> By default, the <code>cache.writeback=on</code> mode is used. It will report data writes as completed as soon as the data is present in the host page cache. This is safe as long as your guest OS makes sure to correctly flush disk caches where needed. If your guest OS does not handle volatile disk write caches correctly and your host crashes or loses power, then the guest may experience data corruption. </p>
<p> For such guests, you should consider using <code>cache.writeback=off</code>. This means that the host page cache will be used to read and write data, but write notification will be sent to the guest only after QEMU has made sure to flush each write to the disk. Be aware that this has a major impact on performance. </p>
<p> When using the <code>-snapshot</code> option, unsafe caching is always used. </p>
<p> Copy-on-read avoids accessing the same backing file sectors repeatedly and is useful when the backing file is over a slow network. By default copy-on-read is off. </p>
<p> Instead of <code>-cdrom</code> you can use: </p>
<pre>
        qemu-system-x86_64 -drive file=file,index=2,media=cdrom
</pre>
<p> Instead of <code>-hda</code>, <code>-hdb</code>, <code>-hdc</code>, <code>-hdd</code>, you can use: </p>
<pre>
        qemu-system-x86_64 -drive file=file,index=0,media=disk
        qemu-system-x86_64 -drive file=file,index=1,media=disk
        qemu-system-x86_64 -drive file=file,index=2,media=disk
        qemu-system-x86_64 -drive file=file,index=3,media=disk
</pre>
<p> You can open an image using pre-opened file descriptors from an fd set: </p>
<pre>
        qemu-system-x86_64 \
        -add-fd fd=3,set=2,opaque=&quot;rdwr:/path/to/file&quot; \
        -add-fd fd=4,set=2,opaque=&quot;rdonly:/path/to/file&quot; \
        -drive file=/dev/fdset/2,index=0,media=disk
</pre>
<p> You can connect a CDROM to the slave of ide0: </p>
<pre>
        qemu-system-x86_64 -drive file=file,if=ide,index=1,media=cdrom
</pre>
<p> If you don&#8217;t specify the &#8220;file=&#8221; argument, you define an empty drive: </p>
<pre>
        qemu-system-x86_64 -drive if=ide,index=1,media=cdrom
</pre>
<p> Instead of <code>-fda</code>, <code>-fdb</code>, you can use: </p>
<pre>
        qemu-system-x86_64 -drive file=file,index=0,if=floppy
        qemu-system-x86_64 -drive file=file,index=1,if=floppy
</pre>
<p> By default, <i>interface</i> is &#8220;ide&#8221; and <i>index</i> is automatically incremented: </p>
<pre>
        qemu-system-x86_64 -drive file=a -drive file=b&quot;
</pre>
<p> is interpreted like: </p>
<pre>
        qemu-system-x86_64 -hda a -hdb b
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
<dt><code>-fsdev local,id=</code><i>id</i><code>,path=</code><i>path</i><code>,security_model=</code><i>security_model</i> <code>[,writeout=</code><i>writeout</i><code>][,readonly][,fmode=</code><i>fmode</i><code>][,dmode=</code><i>dmode</i><code>] [,throttling.</code><i>option</i><code>=</code><i>value</i><code>[,throttling.</code><i>option</i><code>=</code><i>value</i><code>[,&#8230;]]]</code></dt>
<dd>
</dd><dt><code>-fsdev proxy,id=</code><i>id</i><code>,socket=</code><i>socket</i><code>[,writeout=</code><i>writeout</i><code>][,readonly]</code></dt>
<dd>
</dd><dt><code>-fsdev proxy,id=</code><i>id</i><code>,sock_fd=</code><i>sock_fd</i><code>[,writeout=</code><i>writeout</i><code>][,readonly]</code></dt>
<dd>
</dd><dt><code>-fsdev synth,id=</code><i>id</i><code>[,readonly]</code></dt>
<dd> Define a new file system device. Valid options are:</dd>
<dl>
<dl>
<dt><code>local</code></dt>
<dd> Accesses to the filesystem are done by QEMU.</dd>
<dt><code>proxy</code></dt>
<dd> Accesses to the filesystem are done by <code><a href="/docs/linux/man/1-virtfs-proxy-helper/">virtfs-proxy-helper</a></code>(1).</dd>
<dt><code>synth</code></dt>
<dd> Synthetic filesystem, only used by QTests.</dd>
<dt><code>id=</code><i>id</i></dt>
<dd> Specifies identifier for this device.</dd>
<dt><code>path=</code><i>path</i></dt>
<dd> Specifies the export path for the file system device. Files under this path will be available to the 9p client on the guest.</dd>
<dt><code>security_model=</code><i>security_model</i></dt>
<dd> Specifies the security model to be used for this export path. Supported security models are &#8220;passthrough&#8221;, &#8220;mapped-xattr&#8221;, &#8220;mapped-file&#8221; and &#8220;none&#8221;. In &#8220;passthrough&#8221; security model, files are stored using the same credentials as they are created on the guest. This requires QEMU to run as root. In &#8220;mapped-xattr&#8221; security model, some of the file attributes like uid, gid, mode bits and link target are stored as file attributes. For &#8220;mapped-file&#8221; these attributes are stored in the hidden .virtfs_metadata directory. Directories exported by this security model cannot interact with other unix tools. &#8220;none&#8221; security model is same as passthrough except the sever won&#8217;t report failures if it fails to set file attributes like ownership. Security model is mandatory only for local fsdriver. Other fsdrivers (like proxy) don&#8217;t take security model as a parameter.</dd>
<dt><code>writeout=</code><i>writeout</i></dt>
<dd> This is an optional argument. The only supported value is &#8220;immediate&#8221;. This means that host page cache will be used to read and write data but write notification will be sent to the guest only when the data has been reported as written by the storage subsystem.</dd>
<dt><code>readonly</code></dt>
<dd> Enables exporting 9p share as a readonly mount for guests. By default read-write access is given.</dd>
<dt><code>socket=</code><i>socket</i></dt>
<dd> Enables proxy filesystem driver to use passed socket file for communicating with <code><a href="/docs/linux/man/1-virtfs-proxy-helper/">virtfs-proxy-helper</a></code>(1).</dd>
<dt><code>sock_fd=</code><i>sock_fd</i></dt>
<dd> Enables proxy filesystem driver to use passed socket descriptor for communicating with <code><a href="/docs/linux/man/1-virtfs-proxy-helper/">virtfs-proxy-helper</a></code>(1). Usually a helper like libvirt will create socketpair and pass one of the fds as sock_fd.</dd>
<dt><code>fmode=</code><i>fmode</i></dt>
<dd> Specifies the default mode for newly created files on the host. Works only with security models &#8220;mapped-xattr&#8221; and &#8220;mapped-file&#8221;.</dd>
<dt><code>dmode=</code><i>dmode</i></dt>
<dd> Specifies the default mode for newly created directories on the host. Works only with security models &#8220;mapped-xattr&#8221; and &#8220;mapped-file&#8221;.</dd>
<dt><code>throttling.bps-total=</code><i>b</i><code>,throttling.bps-read=</code><i>r</i><code>,throttling.bps-write=</code><i>w</i></dt>
<dd> Specify bandwidth throttling limits in bytes per second, either for all request types or for reads or writes only.</dd>
<dt><code>throttling.bps-total-max=</code><i>bm</i><code>,bps-read-max=</code><i>rm</i><code>,bps-write-max=</code><i>wm</i></dt>
<dd> Specify bursts in bytes per second, either for all request types or for reads or writes only. Bursts allow the guest I/O to spike above the limit temporarily.</dd>
<dt><code>throttling.iops-total=</code><i>i</i><code>,throttling.iops-read=</code><i>r</i><code>, throttling.iops-write=</code><i>w</i></dt>
<dd> Specify request rate limits in requests per second, either for all request types or for reads or writes only.</dd>
<dt><code>throttling.iops-total-max=</code><i>im</i><code>,throttling.iops-read-max=</code><i>irm</i><code>, throttling.iops-write-max=</code><i>iwm</i></dt>
<dd> Specify bursts in requests per second, either for all request types or for reads or writes only. Bursts allow the guest I/O to spike above the limit temporarily.</dd>
<dt><code>throttling.iops-size=</code><i>is</i></dt>
<dd> Let every <i>is</i> bytes of a request count as a new request for iops throttling purposes.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> -fsdev option is used along with -device driver &#8220;virtio-9p-&#8230;&#8221;.</dd></dl>
<dt><code>-device virtio-9p-</code><i>type</i><code>,fsdev=</code><i>id</i><code>,mount_tag=</code><i>mount_tag</i></dt>
<dd> Options for virtio-9p-&#8230; driver are:</dd>
<dl>
<dl>
<dt><i>type</i></dt>
<dd> Specifies the variant to be used. Supported values are &#8220;pci&#8221;, &#8220;ccw&#8221; or &#8220;device&#8221;, depending on the machine type.</dd>
<dt><code>fsdev=</code><i>id</i></dt>
<dd> Specifies the id value specified along with -fsdev option.</dd>
<dt><code>mount_tag=</code><i>mount_tag</i></dt>
<dd> Specifies the tag name to be used by the guest to mount this export point.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-virtfs local,path=</code><i>path</i><code>,mount_tag=</code><i>mount_tag</i> <code>,security_model=</code><i>security_model</i><code>[,writeout=</code><i>writeout</i><code>][,readonly] [,fmode=</code><i>fmode</i><code>][,dmode=</code><i>dmode</i><code>][,multidevs=</code><i>multidevs</i><code>]</code></dt>
<dd>
</dd><dt><code>-virtfs proxy,socket=</code><i>socket</i><code>,mount_tag=</code><i>mount_tag</i> <code>[,writeout=</code><i>writeout</i><code>][,readonly]</code></dt>
<dd>
</dd><dt><code>-virtfs proxy,sock_fd=</code><i>sock_fd</i><code>,mount_tag=</code><i>mount_tag</i> <code>[,writeout=</code><i>writeout</i><code>][,readonly]</code></dt>
<dd>
</dd><dt><code>-virtfs synth,mount_tag=</code><i>mount_tag</i></dt>
<dd> Define a new filesystem device and expose it to the guest using a virtio-9p-device. The general form of a Virtual File system pass-through options are:</dd>
<dl>
<dl>
<dt><code>local</code></dt>
<dd> Accesses to the filesystem are done by QEMU.</dd>
<dt><code>proxy</code></dt>
<dd> Accesses to the filesystem are done by <code><a href="/docs/linux/man/1-virtfs-proxy-helper/">virtfs-proxy-helper</a></code>(1).</dd>
<dt><code>synth</code></dt>
<dd> Synthetic filesystem, only used by QTests.</dd>
<dt><code>id=</code><i>id</i></dt>
<dd> Specifies identifier for the filesystem device</dd>
<dt><code>path=</code><i>path</i></dt>
<dd> Specifies the export path for the file system device. Files under this path will be available to the 9p client on the guest.</dd>
<dt><code>security_model=</code><i>security_model</i></dt>
<dd> Specifies the security model to be used for this export path. Supported security models are &#8220;passthrough&#8221;, &#8220;mapped-xattr&#8221;, &#8220;mapped-file&#8221; and &#8220;none&#8221;. In &#8220;passthrough&#8221; security model, files are stored using the same credentials as they are created on the guest. This requires QEMU to run as root. In &#8220;mapped-xattr&#8221; security model, some of the file attributes like uid, gid, mode bits and link target are stored as file attributes. For &#8220;mapped-file&#8221; these attributes are stored in the hidden .virtfs_metadata directory. Directories exported by this security model cannot interact with other unix tools. &#8220;none&#8221; security model is same as passthrough except the sever won&#8217;t report failures if it fails to set file attributes like ownership. Security model is mandatory only for local fsdriver. Other fsdrivers (like proxy) don&#8217;t take security model as a parameter.</dd>
<dt><code>writeout=</code><i>writeout</i></dt>
<dd> This is an optional argument. The only supported value is &#8220;immediate&#8221;. This means that host page cache will be used to read and write data but write notification will be sent to the guest only when the data has been reported as written by the storage subsystem.</dd>
<dt><code>readonly</code></dt>
<dd> Enables exporting 9p share as a readonly mount for guests. By default read-write access is given.</dd>
<dt><code>socket=</code><i>socket</i></dt>
<dd> Enables proxy filesystem driver to use passed socket file for communicating with <code><a href="/docs/linux/man/1-virtfs-proxy-helper/">virtfs-proxy-helper</a></code>(1). Usually a helper like libvirt will create socketpair and pass one of the fds as sock_fd.</dd>
<dt><code>sock_fd</code></dt>
<dd> Enables proxy filesystem driver to use passed &#8216;sock_fd&#8217; as the socket descriptor for interfacing with <code><a href="/docs/linux/man/1-virtfs-proxy-helper/">virtfs-proxy-helper</a></code>(1).</dd>
<dt><code>fmode=</code><i>fmode</i></dt>
<dd> Specifies the default mode for newly created files on the host. Works only with security models &#8220;mapped-xattr&#8221; and &#8220;mapped-file&#8221;.</dd>
<dt><code>dmode=</code><i>dmode</i></dt>
<dd> Specifies the default mode for newly created directories on the host. Works only with security models &#8220;mapped-xattr&#8221; and &#8220;mapped-file&#8221;.</dd>
<dt><code>mount_tag=</code><i>mount_tag</i></dt>
<dd> Specifies the tag name to be used by the guest to mount this export point.</dd>
<dt><code>multidevs=</code><i>multidevs</i></dt>
<dd> Specifies how to deal with multiple devices being shared with a 9p export. Supported behaviours are either &#8220;remap&#8221;, &#8220;forbid&#8221; or &#8220;warn&#8221;. The latter is the default behaviour on which virtfs 9p expects only one device to be shared with the same export, and if more than one device is shared and accessed via the same 9p export then only a warning message is logged (once) by qemu on host side. In order to avoid file ID collisions on guest you should either create a separate virtfs export for each device to be shared with guests (recommended way) or you might use &#8220;remap&#8221; instead which allows you to share multiple devices with only one export instead, which is achieved by remapping the original inode numbers from host to guest in a way that would prevent such collisions. Remapping inodes in such use cases is required because the original device IDs from host are never passed and exposed on guest. Instead all files of an export shared with virtfs always share the same device id on guest. So two files with identical inode numbers but from actually different devices on host would otherwise cause a file ID collision and hence potential misbehaviours on guest. &#8220;forbid&#8221; on the other hand assumes like &#8220;warn&#8221; that only one device is shared by the same export, however it will not only log a warning message but also deny access to additional devices on guest. Note though that &#8220;forbid&#8221; does currently not block all possible file access operations (e.g. <code>readdir()</code> would still return entries from other devices).</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-virtfs_synth</code></dt>
<dd> Create synthetic file system image. Note that this option is now deprecated. Please use <tt>&quot;-fsdev synth&quot;</tt> and <tt>&quot;-device virtio-9p-...&quot;</tt> instead.</dd>
<dt><code>-iscsi</code></dt>
<dd> Configure iSCSI session parameters.</dd></dl>
<p> <i></i><i>USB</i><i> options</i></p>
<dl>
<dt><code>-usb</code></dt>
<dd> Enable USB emulation on machine types with an on-board USB host controller (if not enabled by default). Note that on-board USB host controllers may not support USB 3.0. In this case <code>-device qemu-xhci</code> can be used instead on machines with PCI.</dd>
<dt><code>-usbdevice</code> <i>devname</i></dt>
<dd> Add the USB device <i>devname</i>. Note that this option is deprecated, please use <tt>&quot;-device usb-...&quot;</tt> instead.</dd>
<dl>
<dl>
<dt><code>mouse</code></dt>
<dd> Virtual Mouse. This will override the PS/2 mouse emulation when activated.</dd>
<dt><code>tablet</code></dt>
<dd> Pointer device that uses absolute coordinates (like a touchscreen). This means QEMU is able to report the mouse position without having to grab the mouse. Also overrides the PS/2 mouse emulation when activated.</dd>
<dt><code>braille</code></dt>
<dd> Braille device. This will use BrlAPI to display the braille output on a real or fake device.</dd></dl>
</dl>
<dl>
</dl>
</dl>
<p> <i>Display options</i></p>
<dl>
<dt><code>-display</code> <i>type</i></dt>
<dd> Select type of display to use. This option is a replacement for the old style -sdl/-curses/&#8230; options. Valid values for <i>type</i> are</dd>
<dl>
<dl>
<dt><code>sdl</code></dt>
<dd> Display video output via SDL (usually in a separate graphics window; see the SDL documentation for other possibilities).</dd>
<dt><code>curses</code></dt>
<dd> Display video output via curses. For graphics device models which support a text mode, QEMU can display this output using a curses/ncurses interface. Nothing is displayed when the graphics device is in graphical mode or if the graphics device does not support a text mode. Generally only the VGA device models support text mode. The font charset used by the guest can be specified with the <tt>&quot;charset&quot;</tt> option, for example <tt>&quot;charset=CP850&quot;</tt> for IBM CP850 encoding. The default is <tt>&quot;CP437&quot;</tt>.</dd>
<dt><code>none</code></dt>
<dd> Do not display video output. The guest will still see an emulated graphics card, but its output will not be displayed to the QEMU user. This option differs from the -nographic option in that it only affects what is done with video output; -nographic also changes the destination of the serial and parallel port data.</dd>
<dt><code>gtk</code></dt>
<dd> Display video output in a GTK window. This interface provides drop-down menus and other UI elements to configure and control the VM during runtime.</dd>
<dt><code>vnc</code></dt>
<dd> Start a VNC server on display &lt;arg&gt;</dd>
<dt><code>egl-headless</code></dt>
<dd> Offload all OpenGL operations to a local DRI device. For any graphical display, this display needs to be paired with either VNC or SPICE displays.</dd>
<dt><code>spice-app</code></dt>
<dd> Start QEMU as a Spice server and launch the default Spice client application. The Spice server will redirect the serial consoles and QEMU monitors. (Since 4.0)</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-nographic</code></dt>
<dd> Normally, if QEMU is compiled with graphical window support, it displays output such as guest graphics, guest console, and the QEMU monitor in a window. With this option, you can totally disable graphical output so that QEMU is a simple command line application. The emulated serial port is redirected on the console and muxed with the monitor (unless redirected elsewhere explicitly). Therefore, you can still use QEMU to debug a Linux kernel with a serial console. Use <code>C-a h</code> for help on switching between the console and monitor.</dd>
<dt><code>-curses</code></dt>
<dd> Normally, if QEMU is compiled with graphical window support, it displays output such as guest graphics, guest console, and the QEMU monitor in a window. With this option, QEMU can display the VGA output when in text mode using a curses/ncurses interface. Nothing is displayed in graphical mode.</dd>
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
<dd>
</dd><dt><code>unix</code></dt>
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
<dd> Configure video stream detection. Default is off.</dd>
<dt><code>agent-mouse=[on|off]</code></dt>
<dd> Enable/disable passing mouse events via vdagent. Default is on.</dd>
<dt><code>playback-compression=[on|off]</code></dt>
<dd> Enable/disable audio stream compression (using celt 0.5.1). Default is on.</dd>
<dt><code>seamless-migration=[on|off]</code></dt>
<dd> Enable/disable spice seamless migration. Default is off.</dd>
<dt><code>gl=[on|off]</code></dt>
<dd> Enable/disable OpenGL context. Default is off.</dd>
<dt><code>rendernode=&lt;file&gt;</code></dt>
<dd> DRM render node for OpenGL rendering. If not specified, it will pick the first available. (Since 2.9)</dd></dl>
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
<dd> Cirrus Logic GD5446 Video card. All Windows versions starting from Windows 95 should recognize and use this graphic card. For optimal performances, use 16 bit color depth in the guest and the host OS. (This card was the default before QEMU 2.2)</dd>
<dt><code>std</code></dt>
<dd> Standard VGA card with Bochs VBE extensions. If your guest OS supports the VESA 2.0 VBE extensions (e.g. Windows XP) and if you want to use high resolution modes (&gt;= 1280x1024x16) then you should use this option. (This card is the default since QEMU 2.2)</dd>
<dt><code>vmware</code></dt>
<dd> VMWare SVGA-II compatible adapter. Use it if you have sufficiently recent XFree86/XOrg server or Windows guest with a driver for this card.</dd>
<dt><code>qxl</code></dt>
<dd> QXL paravirtual graphic card. It is VGA compatible (including VESA 2.0 VBE support). Works best with qxl guest drivers installed though. Recommended choice when using the spice protocol.</dd>
<dt><code>tcx</code></dt>
<dd> (sun4m only) Sun TCX framebuffer. This is the default framebuffer for sun4m machines and offers both 8-bit and 24-bit colour depths at a fixed resolution of 1024&#215;768.</dd>
<dt><code>cg3</code></dt>
<dd> (sun4m only) Sun cgthree framebuffer. This is a simple 8-bit framebuffer for sun4m machines available in both 1024&#215;768 (OpenBIOS) and 1152&#215;900 (OBP) resolutions aimed at people wishing to run older Solaris versions.</dd>
<dt><code>virtio</code></dt>
<dd> Virtio VGA card.</dd>
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
<dd> Normally, if QEMU is compiled with graphical window support, it displays output such as guest graphics, guest console, and the QEMU monitor in a window. With this option, you can have QEMU listen on VNC display <i>display</i> and redirect the VGA display over the VNC session. It is very useful to enable the usb tablet device when using this option (option <code>-device usb-tablet</code>). When using the VNC display, you must use the <code>-k</code> parameter to set the keyboard layout if you are not using en-us. Valid syntax for the <i>display</i> is</dd>
<dl>
<dl>
<dt><code>to=</code><i>L</i></dt>
<dd> With this option, QEMU will try next available VNC <i>display</i>s, until the number <i>L</i>, if the origianlly defined &quot;-vnc <i>display</i>&quot; is not available, e.g. port 5900+<i>display</i> is already used by another application. By default, to=0.</dd>
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
<dd> Opens an additional TCP listening port dedicated to VNC Websocket connections. If a bare <i>websocket</i> option is given, the Websocket port is 5700+<i>display</i>. An alternative port can be specified with the syntax <tt>&quot;websocket&quot;</tt>=<i>port</i>. </dd>
<p> If <i>host</i> is specified connections will only be allowed from this host. It is possible to control the websocket listen address independently, using the syntax <tt>&quot;websocket&quot;</tt>=<i>host</i>:<i>port</i>. </p>
<p> If no TLS credentials are provided, the websocket connection runs in unencrypted mode. If TLS credentials are provided, the websocket connection requires encrypted client connections.</p>
<dt><code>password</code></dt>
<dd> Require that password based authentication is used for client connections. </dd>
<p> The password must be set separately using the <tt>&quot;set_password&quot;</tt> command in the <code>pcsys_monitor</code>. The syntax to change your password is: <tt>&quot;set_password &lt;protocol&gt; &lt;password&gt;&quot;</tt> where &lt;protocol&gt; could be either &#8220;vnc&#8221; or &#8220;spice&#8221;. </p>
<p> If you would like to change &lt;protocol&gt; password expiration, you should use <tt>&quot;expire_password &lt;protocol&gt; &lt;expiration-time&gt;&quot;</tt> where expiration time could be one of the following options: now, never, +seconds or UNIX time of expiration, e.g. +60 to make password expire in 60 seconds, or 1335196800 to make password expire on &#8220;Mon Apr 23 12:00:00 EDT 2012&#8221; (UNIX time for this date and time). </p>
<p> You can also use keywords &#8220;now&#8221; or &#8220;never&#8221; for the expiration time to allow &lt;protocol&gt; password to expire immediately or never expire.</p>
<dt><code>tls-creds=</code><i></i><i>ID</i><i></i></dt>
<dd> Provides the ID of a set of TLS credentials to use to secure the VNC server. They will apply to both the normal VNC server socket and the websocket socket (if enabled). Setting TLS credentials will cause the VNC server socket to enable the VeNCrypt auth mechanism. The credentials should have been previously created using the <code>-object tls-creds</code> argument.</dd>
<dt><code>tls-authz=</code><i></i><i>ID</i><i></i></dt>
<dd> Provides the ID of the QAuthZ authorization object against which the client&#8217;s x509 distinguished name will validated. This object is only resolved at time of use, so can be deleted and recreated on the fly while the VNC server is active. If missing, it will default to denying access.</dd>
<dt><code>sasl</code></dt>
<dd> Require that the client use SASL to authenticate with the VNC server. The exact choice of authentication method used is controlled from the system / user&#8217;s SASL configuration file for the &#8216;qemu&#8217; service. This is typically found in /etc/sasl2/qemu.conf. If running QEMU as an unprivileged user, an environment variable SASL_CONF_PATH can be used to make it search alternate locations for the service config. While some SASL auth methods can also provide data encryption (eg GSSAPI), it is recommended that SASL always be combined with the &#8216;tls&#8217; and &#8216;x509&#8217; settings to enable use of SSL and server certificates. This ensures a data encryption preventing compromise of authentication credentials. See the <code>vnc_security</code> section for details on using SASL authentication.</dd>
<dt><code>sasl-authz=</code><i></i><i>ID</i><i></i></dt>
<dd> Provides the ID of the QAuthZ authorization object against which the client&#8217;s SASL username will validated. This object is only resolved at time of use, so can be deleted and recreated on the fly while the VNC server is active. If missing, it will default to denying access.</dd>
<dt><code>acl</code></dt>
<dd> Legacy method for enabling authorization of clients against the x509 distinguished name and SASL username. It results in the creation of two <tt>&quot;authz-list&quot;</tt> objects with IDs of <tt>&quot;vnc.username&quot;</tt> and <tt>&quot;vnc.x509dname&quot;</tt>. The rules for these objects must be configured with the HMP ACL commands. </dd>
<p> This option is deprecated and should no longer be used. The new <code>sasl-authz</code> and <code>tls-authz</code> options are a replacement.</p>
<dt><code>lossy</code></dt>
<dd> Enable lossy compression methods (gradient, JPEG, &#8230;). If this option is set, VNC client may receive lossy framebuffer updates depending on its encoding settings. Enabling this option can save a lot of bandwidth at the expense of quality.</dd>
<dt><code>non-adaptive</code></dt>
<dd> Disable adaptive encodings. Adaptive encodings are enabled by default. An adaptive encoding will try to detect frequently updated screen regions, and send updates in these regions using a lossy encoding (like JPEG). This can be really helpful to save bandwidth when playing videos. Disabling adaptive encodings restores the original static behavior of encodings like Tight.</dd>
<dt><code>share=[allow-exclusive|force-shared|ignore]</code></dt>
<dd> Set display sharing policy. &#8216;allow-exclusive&#8217; allows clients to ask for exclusive access. As suggested by the rfb spec this is implemented by dropping other connections. Connecting multiple clients in parallel requires all clients asking for a shared session (vncviewer: -shared switch). This is the default. &#8216;force-shared&#8217; disables exclusive client access. Useful for shared desktop sessions, where you don&#8217;t want someone forgetting specify -shared disconnect everybody else. &#8216;ignore&#8217; completely ignores the shared flag and allows everybody connect unconditionally. Doesn&#8217;t conform to the rfb spec but is traditional QEMU behavior.</dd>
<dt><code>key-delay-ms</code></dt>
<dd> Set keyboard delay, for key down and key up events, in milliseconds. Default is 10. Keyboards are low-bandwidth devices, so this slowdown can help the device and guest to keep up and not lose events in case events are arriving in bulk. Possible causes for the latter are flaky network connections, or scripts for automated testing.</dd>
<dt><code>audiodev=</code><i>audiodev</i></dt>
<dd> Use the specified <i>audiodev</i> when the VNC client requests audio transmission. When not using an -audiodev argument, this option must be omitted, otherwise is must be present and specify a valid audiodev.</dd></dl>
</dl>
<dl>
</dl>
</dl>
<p> <i>i386 target only</i></p>
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
<dd> Add ACPI table with specified header fields and context from specified files. For file=, take whole ACPI table from the specified files, including all ACPI headers (possible overridden by other options). For data=, only data portion of the table is used, all header information is specified in the command line. If a SLIC table is supplied to QEMU, then the SLIC&#8216;s oem_id and oem_table_id fields will override the same in the RSDT and the FADT (a.k.a. FACP), in order to ensure the field matches required by the Microsoft SLIC spec and the ACPI spec.</dd>
<dt><code>-smbios file=</code><i>binary</i></dt>
<dd> Load SMBIOS entry from binary file.</dd>
<dt><code>-smbios type=0[,vendor=</code><i>str</i><code>][,version=</code><i>str</i><code>][,date=</code><i>str</i><code>][,release=</code><i></i>%d<i>.%d</i><code>][,uefi=on|off]</code></dt>
<dd> Specify SMBIOS type 0 fields</dd>
<dt><code>-smbios type=1[,manufacturer=</code><i>str</i><code>][,product=</code><i>str</i><code>][,version=</code><i>str</i><code>][,serial=</code><i>str</i><code>][,uuid=</code><i>uuid</i><code>][,sku=</code><i>str</i><code>][,family=</code><i>str</i><code>]</code></dt>
<dd> Specify SMBIOS type 1 fields</dd>
<dt><code>-smbios type=2[,manufacturer=</code><i>str</i><code>][,product=</code><i>str</i><code>][,version=</code><i>str</i><code>][,serial=</code><i>str</i><code>][,asset=</code><i>str</i><code>][,location=</code><i>str</i><code>]</code></dt>
<dd> Specify SMBIOS type 2 fields</dd>
<dt><code>-smbios type=3[,manufacturer=</code><i>str</i><code>][,version=</code><i>str</i><code>][,serial=</code><i>str</i><code>][,asset=</code><i>str</i><code>][,sku=</code><i>str</i><code>]</code></dt>
<dd> Specify SMBIOS type 3 fields</dd>
<dt><code>-smbios type=4[,sock_pfx=</code><i>str</i><code>][,manufacturer=</code><i>str</i><code>][,version=</code><i>str</i><code>][,serial=</code><i>str</i><code>][,asset=</code><i>str</i><code>][,part=</code><i>str</i><code>]</code></dt>
<dd> Specify SMBIOS type 4 fields</dd>
<dt><code>-smbios type=17[,loc_pfx=</code><i>str</i><code>][,bank=</code><i>str</i><code>][,manufacturer=</code><i>str</i><code>][,serial=</code><i>str</i><code>][,asset=</code><i>str</i><code>][,part=</code><i>str</i><code>][,speed=</code><i></i>%d<i></i><code>]</code></dt>
<dd> Specify SMBIOS type 17 fields</dd></dl>
<p> <i>Network options</i></p>
<dl>
<dt><code>-nic [tap|bridge|user|l2tpv3|vde|netmap|vhost-user|socket][,&#8230;][,mac=macaddr][,model=mn]</code></dt>
<dd> This option is a shortcut for configuring both the on-board (default) guest NIC hardware and the host network backend in one go. The host backend options are the same as with the corresponding <code>-netdev</code> options below. The guest NIC model can be set with <code>model=</code><i>modelname</i>. Use <code>model=help</code> to list the available device types. The hardware MAC address can be set with <code>mac=</code><i>macaddr</i>. </dd>
<p> The following two example do exactly the same, to show how <code>-nic</code> can be used to shorten the command line length (note that the e1000 is the default on i386, so the <code>model=e1000</code> parameter could even be omitted here, too): </p>
<pre>
        qemu-system-x86_64 -netdev user,id=n1,ipv6=off -device e1000,netdev=n1,mac=52:54:98:76:54:32
        qemu-system-x86_64 -nic user,ipv6=off,model=e1000,mac=52:54:98:76:54:32
</pre>
<dt><code>-nic none</code></dt>
<dd> Indicate that no network devices should be configured. It is used to override the default configuration (default NIC with &#8220;user&#8221; host network backend) which is activated if no other networking options are provided.</dd>
<dt><code>-netdev user,id=</code><i>id</i><code>[,</code><i>option</i><code>][,</code><i>option</i><code>][,&#8230;]</code></dt>
<dd> Configure user mode host network backend which requires no administrator privilege to run. Valid options are:</dd>
<dl>
<dl>
<dt><code>id=</code><i>id</i></dt>
<dd> Assign symbolic name for use in monitor commands.</dd>
<dt><code>ipv4=on|off and ipv6=on|off</code></dt>
<dd> Specify that either IPv4 or IPv6 must be enabled. If neither is specified both protocols are enabled.</dd>
<dt><code>net=</code><i>addr</i><code>[/</code><i>mask</i><code>]</code></dt>
<dd> Set IP network address the guest will see. Optionally specify the netmask, either in the form a.b.c.d or as number of valid top-most bits. Default is 10.0.2.0/24.</dd>
<dt><code>host=</code><i>addr</i></dt>
<dd> Specify the guest-visible address of the host. Default is the 2nd IP in the guest network, i.e. x.x.x.2.</dd>
<dt><code>ipv6-net=</code><i>addr</i><code>[/</code><i>int</i><code>]</code></dt>
<dd> Set IPv6 network address the guest will see (default is fec0::/64). The network prefix is given in the usual hexadecimal IPv6 address notation. The prefix size is optional, and is given as the number of valid top-most bits (default is 64).</dd>
<dt><code>ipv6-host=</code><i>addr</i></dt>
<dd> Specify the guest-visible IPv6 address of the host. Default is the 2nd IPv6 in the guest network, i.e. xxxx::2.</dd>
<dt><code>restrict=on|off</code></dt>
<dd> If this option is enabled, the guest will be isolated, i.e. it will not be able to contact the host and no guest IP packets will be routed over the host to the outside. This option does not affect any explicitly set forwarding rules.</dd>
<dt><code>hostname=</code><i>name</i></dt>
<dd> Specifies the client hostname reported by the built-in DHCP server.</dd>
<dt><code>dhcpstart=</code><i>addr</i></dt>
<dd> Specify the first of the 16 IPs the built-in DHCP server can assign. Default is the 15th to 31st IP in the guest network, i.e. x.x.x.15 to x.x.x.31.</dd>
<dt><code>dns=</code><i>addr</i></dt>
<dd> Specify the guest-visible address of the virtual nameserver. The address must be different from the host address. Default is the 3rd IP in the guest network, i.e. x.x.x.3.</dd>
<dt><code>ipv6-dns=</code><i>addr</i></dt>
<dd> Specify the guest-visible address of the IPv6 virtual nameserver. The address must be different from the host address. Default is the 3rd IP in the guest network, i.e. xxxx::3.</dd>
<dt><code>dnssearch=</code><i>domain</i></dt>
<dd> Provides an entry for the domain-search list sent by the built-in DHCP server. More than one domain suffix can be transmitted by specifying this option multiple times. If supported, this will cause the guest to automatically try to append the given domain suffix(es) in case a domain name can not be resolved. </dd>
<p> Example: </p>
<pre>
        qemu-system-x86_64 -nic user,dnssearch=mgmt.example.org,dnssearch=example.org
</pre>
<dt><code>domainname=</code><i>domain</i></dt>
<dd> Specifies the client domain name reported by the built-in DHCP server.</dd>
<dt><code>tftp=</code><i>dir</i></dt>
<dd> When using the user mode network stack, activate a built-in TFTP server. The files in <i>dir</i> will be exposed as the root of a TFTP server. The TFTP client on the guest must be configured in binary mode (use the command <tt>&quot;bin&quot;</tt> of the Unix TFTP client).</dd>
<dt><code>tftp-server-name=</code><i>name</i></dt>
<dd> In BOOTP reply, broadcast <i>name</i> as the &#8220;TFTP server name&#8221; (RFC2132 option 66). This can be used to advise the guest to load boot files or configurations from a different server than the host address.</dd>
<dt><code>bootfile=</code><i>file</i></dt>
<dd> When using the user mode network stack, broadcast <i>file</i> as the BOOTP filename. In conjunction with <code>tftp</code>, this can be used to network boot a guest from a local directory. </dd>
<p> Example (using pxelinux): </p>
<pre>
        qemu-system-x86_64 -hda linux.img -boot n -device e1000,netdev=n1 \
        -netdev user,id=n1,tftp=/path/to/tftp/files,bootfile=/pxelinux.0
</pre>
<dt><code>smb=</code><i>dir</i><code>[,smbserver=</code><i>addr</i><code>]</code></dt>
<dd> When using the user mode network stack, activate a built-in SMB server so that Windows OSes can access to the host files in <i>dir</i> transparently. The IP address of the SMB server can be set to <i>addr</i>. By default the 4th IP in the guest network is used, i.e. x.x.x.4. </dd>
<p> In the guest Windows OS, the line: </p>
<pre>
        10.0.2.4 smbserver
</pre>
<p> must be added in the file <i>C:\WINDOWS\LMHOSTS</i> (for windows 9x/Me) or <i>C:\WINNT\SYSTEM32\DRIVERS\ETC\LMHOSTS</i> (Windows NT/2000). </p>
<p> Then <i>dir</i> can be accessed in <i>\smbserver\qemu</i>. </p>
<p> Note that a SAMBA server must be installed on the host OS.</p>
<dt><code>hostfwd=[tcp|udp]:[</code><i>hostaddr</i><code>]:</code><i>hostport</i><code>-[</code><i>guestaddr</i><code>]:</code><i>guestport</i></dt>
<dd> Redirect incoming TCP or UDP connections to the host port <i>hostport</i> to the guest IP address <i>guestaddr</i> on guest port <i>guestport</i>. If <i>guestaddr</i> is not specified, its value is x.x.x.15 (default first address given by the built-in DHCP server). By specifying <i>hostaddr</i>, the rule can be bound to a specific host interface. If no connection type is set, TCP is used. This option can be given multiple times. </dd>
<p> For example, to redirect host X11 connection from screen 1 to guest screen 0, use the following: </p>
<pre>
        # on the host
        qemu-system-x86_64 -nic user,hostfwd=tcp:127.0.0.1:6001-:6000
        # this host xterm should open in the guest X11 server
        xterm -display :1
</pre>
<p> To redirect telnet connections from host port 5555 to telnet port on the guest, use the following: </p>
<pre>
        # on the host
        qemu-system-x86_64 -nic user,hostfwd=tcp::5555-:23
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
        qemu-system-x86_64 -nic user,guestfwd=tcp:10.0.2.100:1234-tcp:10.10.1.1:4321
</pre>
<p> Or you can execute a command on every TCP connection established by the guest, so that QEMU behaves similar to an inetd process for that virtual server: </p>
<pre>
        # call &quot;netcat 10.10.1.1 4321&quot; on every TCP connection to 10.0.2.100:1234
        # and connect the TCP stream to its stdin/stdout
        qemu-system-x86_64 -nic  'user,id=n1,guestfwd=tcp:10.0.2.100:1234-cmd:netcat 10.10.1.1 4321'
</pre>
</dl>
</dl>
<dl>
</dl>
<dt><code>-netdev tap,id=</code><i>id</i><code>[,fd=</code><i>h</i><code>][,ifname=</code><i>name</i><code>][,script=</code><i>file</i><code>][,downscript=</code><i>dfile</i><code>][,br=</code><i>bridge</i><code>][,helper=</code><i>helper</i><code>]</code></dt>
<dd> Configure a host TAP network backend with ID <i>id</i>. </dd>
<p> Use the network script <i>file</i> to configure it and the network script <i>dfile</i> to deconfigure it. If <i>name</i> is not provided, the OS automatically provides one. The default network configure script is <i>/etc/qemu-ifup</i> and the default network deconfigure script is <i>/etc/qemu-ifdown</i>. Use <code>script=no</code> or <code>downscript=no</code> to disable script execution. </p>
<p> If running QEMU as an unprivileged user, use the network helper <i>helper</i> to configure the TAP interface and attach it to the bridge. The default network helper executable is <i>/path/to/qemu-bridge-helper</i> and the default bridge device is <i>br0</i>. </p>
<p> <code>fd</code>=<i>h</i> can be used to specify the handle of an already opened host TAP interface. </p>
<p> Examples: </p>
<pre>
        #launch a QEMU instance with the default network script
        qemu-system-x86_64 linux.img -nic tap
        #launch a QEMU instance with two NICs, each one connected
        #to a TAP device
        qemu-system-x86_64 linux.img \
        -netdev tap,id=nd0,ifname=tap0 -device e1000,netdev=nd0 \
        -netdev tap,id=nd1,ifname=tap1 -device rtl8139,netdev=nd1
        #launch a QEMU instance with the default network helper to
        #connect a TAP device to bridge br0
        qemu-system-x86_64 linux.img -device virtio-net-pci,netdev=n1 \
        -netdev tap,id=n1,&quot;helper=/path/to/qemu-bridge-helper&quot;
</pre>
<dt><code>-netdev bridge,id=</code><i>id</i><code>[,br=</code><i>bridge</i><code>][,helper=</code><i>helper</i><code>]</code></dt>
<dd> Connect a host TAP network interface to a host bridge device. </dd>
<p> Use the network helper <i>helper</i> to configure the TAP interface and attach it to the bridge. The default network helper executable is <i>/path/to/qemu-bridge-helper</i> and the default bridge device is <i>br0</i>. </p>
<p> Examples: </p>
<pre>
        #launch a QEMU instance with the default network helper to
        #connect a TAP device to bridge br0
        qemu-system-x86_64 linux.img -netdev bridge,id=n1 -device virtio-net,netdev=n1
        #launch a QEMU instance with the default network helper to
        #connect a TAP device to bridge qemubr0
        qemu-system-x86_64 linux.img -netdev bridge,br=qemubr0,id=n1 -device virtio-net,netdev=n1
</pre>
<dt><code>-netdev socket,id=</code><i>id</i><code>[,fd=</code><i>h</i><code>][,listen=[</code><i>host</i><code>]:</code><i>port</i><code>][,connect=</code><i>host</i><code>:</code><i>port</i><code>]</code></dt>
<dd> This host network backend can be used to connect the guest&#8217;s network to another QEMU virtual machine using a TCP socket connection. If <code>listen</code> is specified, QEMU waits for incoming connections on <i>port</i> (<i>host</i> is optional). <code>connect</code> is used to connect to another QEMU instance using the <code>listen</code> option. <code>fd</code>=<i>h</i> specifies an already opened TCP socket. </dd>
<p> Example: </p>
<pre>
        # launch a first QEMU instance
        qemu-system-x86_64 linux.img \
        -device e1000,netdev=n1,mac=52:54:00:12:34:56 \
        -netdev socket,id=n1,listen=:1234
        # connect the network of this instance to the network of the first instance
        qemu-system-x86_64 linux.img \
        -device e1000,netdev=n2,mac=52:54:00:12:34:57 \
        -netdev socket,id=n2,connect=127.0.0.1:1234
</pre>
<dt><code>-netdev socket,id=</code><i>id</i><code>[,fd=</code><i>h</i><code>][,mcast=</code><i>maddr</i><code>:</code><i>port</i><code>[,localaddr=</code><i>addr</i><code>]]</code></dt>
<dd> Configure a socket host network backend to share the guest&#8217;s network traffic with another QEMU virtual machines using a UDP multicast socket, effectively making a bus for every QEMU with same multicast address <i>maddr</i> and <i>port</i>. NOTES:</dd>
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
        qemu-system-x86_64 linux.img \
        -device e1000,netdev=n1,mac=52:54:00:12:34:56 \
        -netdev socket,id=n1,mcast=230.0.0.1:1234
        # launch another QEMU instance on same &quot;bus&quot;
        qemu-system-x86_64 linux.img \
        -device e1000,netdev=n2,mac=52:54:00:12:34:57 \
        -netdev socket,id=n2,mcast=230.0.0.1:1234
        # launch yet another QEMU instance on same &quot;bus&quot;
        qemu-system-x86_64 linux.img \
        -device e1000,netdev=n3,mac=52:54:00:12:34:58 \
        -netdev socket,id=n3,mcast=230.0.0.1:1234
</pre>
<p> Example (User Mode Linux compat.): </p>
<pre>
        # launch QEMU instance (note mcast address selected is UML's default)
        qemu-system-x86_64 linux.img \
        -device e1000,netdev=n1,mac=52:54:00:12:34:56 \
        -netdev socket,id=n1,mcast=239.192.168.1:1102
        # launch UML
        /path/to/linux ubd0=/path/to/root_fs eth0=mcast
</pre>
<p> Example (send packets from host&#8217;s 1.2.3.4): </p>
<pre>
        qemu-system-x86_64 linux.img \
        -device e1000,netdev=n1,mac=52:54:00:12:34:56 \
        -netdev socket,id=n1,mcast=239.192.168.1:1102,localaddr=1.2.3.4
</pre>
</dd></dl>
<dt><code>-netdev l2tpv3,id=</code><i>id</i><code>,src=</code><i>srcaddr</i><code>,dst=</code><i>dstaddr</i><code>[,srcport=</code><i>srcport</i><code>][,dstport=</code><i>dstport</i><code>],txsession=</code><i>txsession</i><code>[,rxsession=</code><i>rxsession</i><code>][,ipv6][,udp][,cookie64][,counter][,pincounter][,txcookie=</code><i>txcookie</i><code>][,rxcookie=</code><i>rxcookie</i><code>][,offset=</code><i>offset</i><code>]</code></dt>
<dd> Configure a L2TPv3 pseudowire host network backend. L2TPv3 (RFC3391) is a popular protocol to transport Ethernet (and other Layer 2) data frames between two systems. It is present in routers, firewalls and the Linux kernel (from version 3.3 onwards). </dd>
<p> This transport allows a VM to communicate to another VM, router or firewall directly.</p>
<dl>
<dl>
<dt><code>src=</code><i>srcaddr</i></dt>
<dd> source address (mandatory)</dd>
<dt><code>dst=</code><i>dstaddr</i></dt>
<dd> destination address (mandatory)</dd>
<dt><code>udp</code></dt>
<dd> select udp encapsulation (default is ip).</dd>
<dt><code>srcport=</code><i>srcport</i></dt>
<dd> source udp port.</dd>
<dt><code>dstport=</code><i>dstport</i></dt>
<dd> destination udp port.</dd>
<dt><code>ipv6</code></dt>
<dd> force v6, otherwise defaults to v4.</dd>
<dt><code>rxcookie=</code><i>rxcookie</i></dt>
<dd>
</dd><dt><code>txcookie=</code><i>txcookie</i></dt>
<dd> Cookies are a weak form of security in the l2tpv3 specification. Their function is mostly to prevent misconfiguration. By default they are 32 bit.</dd>
<dt><code>cookie64</code></dt>
<dd> Set cookie size to 64 bit instead of the default 32</dd>
<dt><code>counter=off</code></dt>
<dd> Force a &#8216;cut-down&#8217; L2TPv3 with no counter as in draft-mkonstan-l2tpext-keyed-ipv6-tunnel-00</dd>
<dt><code>pincounter=on</code></dt>
<dd> Work around broken counter handling in peer. This may also help on networks which have packet reorder.</dd>
<dt><code>offset=</code><i>offset</i></dt>
<dd> Add an extra offset between header and data</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> For example, to attach a VM running on host 4.3.2.1 via L2TPv3 to the bridge br-lan on the remote Linux host 1.2.3.4: </p>
<pre>
        # Setup tunnel on linux host using raw ip as encapsulation
        # on 1.2.3.4
        ip l2tp add tunnel remote 4.3.2.1 local 1.2.3.4 tunnel_id 1 peer_tunnel_id 1 \
        encap udp udp_sport 16384 udp_dport 16384
        ip l2tp add session tunnel_id 1 name vmtunnel0 session_id \
        0xFFFFFFFF peer_session_id 0xFFFFFFFF
        ifconfig vmtunnel0 mtu 1500
        ifconfig vmtunnel0 up
        brctl addif br-lan vmtunnel0
        # on 4.3.2.1
        # launch QEMU instance - if your network has reorder or is very lossy add ,pincounter
        qemu-system-x86_64 linux.img -device e1000,netdev=n1 \
        -netdev l2tpv3,id=n1,src=4.2.3.1,dst=1.2.3.4,udp,srcport=16384,dstport=16384,rxsession=0xffffffff,txsession=0xffffffff,counter
</pre>
</dd></dl>
<dt><code>-netdev vde,id=</code><i>id</i><code>[,sock=</code><i>socketpath</i><code>][,port=</code><i>n</i><code>][,group=</code><i>groupname</i><code>][,mode=</code><i>octalmode</i><code>]</code></dt>
<dd> Configure VDE backend to connect to PORT <i>n</i> of a vde switch running on host and listening for incoming connections on <i>socketpath</i>. Use GROUP <i>groupname</i> and MODE <i>octalmode</i> to change default ownership and permissions for communication port. This option is only available if QEMU has been compiled with vde support enabled. </dd>
<p> Example: </p>
<pre>
        # launch vde switch
        vde_switch -F -sock /tmp/myswitch
        # launch QEMU instance
        qemu-system-x86_64 linux.img -nic vde,sock=/tmp/myswitch
</pre>
<dt><code>-netdev vhost-user,chardev=</code><i>id</i><code>[,vhostforce=on|off][,queues=n]</code></dt>
<dd> Establish a vhost-user netdev, backed by a chardev <i>id</i>. The chardev should be a unix domain socket backed one. The vhost-user uses a specifically defined protocol to pass vhost ioctl replacement messages to an application on the other end of the socket. On non-MSIX guests, the feature can be forced with <i>vhostforce</i>. Use &#8216;queues=<i>n</i>&#8216; to specify the number of queues to be created for multiqueue vhost-user. </dd>
<p> Example: </p>
<pre>
        qemu -m 512 -object memory-backend-file,id=mem,size=512M,mem-path=/hugetlbfs,share=on \
        -numa node,memdev=mem \
        -chardev socket,id=chr0,path=/path/to/socket \
        -netdev type=vhost-user,id=net0,chardev=chr0 \
        -device virtio-net-pci,netdev=net0
</pre>
<dt><code>-netdev hubport,id=</code><i>id</i><code>,hubid=</code><i>hubid</i><code>[,netdev=</code><i>nd</i><code>]</code></dt>
<dd> Create a hub port on the emulated hub with ID <i>hubid</i>. </dd>
<p> The hubport netdev lets you connect a NIC to a QEMU emulated hub instead of a single netdev. Alternatively, you can also connect the hubport to another netdev with ID <i>nd</i> by using the <code>netdev=</code><i>nd</i> option.</p>
<dt><code>-net nic[,netdev=</code><i>nd</i><code>][,macaddr=</code><i>mac</i><code>][,model=</code><i>type</i><code>] [,name=</code><i>name</i><code>][,addr=</code><i>addr</i><code>][,vectors=</code><i>v</i><code>]</code></dt>
<dd> Legacy option to configure or create an on-board (or machine default) Network Interface Card(NIC) and connect it either to the emulated hub with ID 0 (i.e. the default hub), or to the netdev <i>nd</i>. The NIC is an e1000 by default on the PC target. Optionally, the MAC address can be changed to <i>mac</i>, the device address set to <i>addr</i> (PCI cards only), and a <i>name</i> can be assigned for use in monitor commands. Optionally, for PCI cards, you can specify the number <i>v</i> of MSI-X vectors that the card should have; this option currently only affects virtio cards; set <i>v</i> = 0 to disable MSI-X. If no <code>-net</code> option is specified, a single NIC is created. QEMU can emulate several different models of network card. Use <tt>&quot;-net nic,model=help&quot;</tt> for a list of available devices for your target.</dd>
<dt><code>-net user|tap|bridge|socket|l2tpv3|vde[,&#8230;][,name=</code><i>name</i><code>]</code></dt>
<dd> Configure a host network backend (with the options corresponding to the same <code>-netdev</code> option) and connect it to the emulated hub 0 (the default hub). Use <i>name</i> to specify the name of the hub port.</dd></dl>
<p> <i>Character device options</i> </p>
<p> The general form of a character device option is:</p>
<dl>
<dt><code>-chardev</code> <i>backend</i><code>,id=</code><i>id</i><code>[,mux=on|off][,</code><i>options</i><code>]</code></dt>
<dd> Backend is one of: <code>null</code>, <code>socket</code>, <code>udp</code>, <code>msmouse</code>, <code>vc</code>, <code>ringbuf</code>, <code>file</code>, <code>pipe</code>, <code>console</code>, <code>serial</code>, <code>pty</code>, <code>stdio</code>, <code>braille</code>, <code>tty</code>, <code>parallel</code>, <code>parport</code>, <code>spicevmc</code>, <code>spiceport</code>. The specific backend will determine the applicable options. </dd>
<p> Use <tt>&quot;-chardev help&quot;</tt> to print all available chardev backend types. </p>
<p> All devices must have an id, which can be any string up to 127 characters long. It is used to uniquely identify this device in other command line directives. </p>
<p> A character device may be used in multiplexing mode by multiple front-ends. Specify <code>mux=on</code> to enable this mode. A multiplexer is a &#8220;1:N&#8221; device, and here the &#8220;1&#8221; end is your specified chardev backend, and the &#8220;N&#8221; end is the various parts of QEMU that can talk to a chardev. If you create a chardev with <code>id=myid</code> and <code>mux=on</code>, QEMU will create a multiplexer with your specified ID, and you can then configure multiple front ends to use that chardev ID for their input/output. Up to four different front ends can be connected to a single multiplexed chardev. (Without multiplexing enabled, a chardev can only be used by a single front end.) For instance you could use this to allow a single stdio chardev to be used by two serial ports and the QEMU monitor: </p>
<pre>
        -chardev stdio,mux=on,id=char0 \
        -mon chardev=char0,mode=readline \
        -serial chardev:char0 \
        -serial chardev:char0
</pre>
<p> You can have more than one multiplexer in a system configuration; for instance you could have a TCP port multiplexed between UART 0 and UART 1, and stdio multiplexed between the QEMU monitor and a parallel port: </p>
<pre>
        -chardev stdio,mux=on,id=char0 \
        -mon chardev=char0,mode=readline \
        -parallel chardev:char0 \
        -chardev tcp,...,mux=on,id=char1 \
        -serial chardev:char1 \
        -serial chardev:char1
</pre>
<p> When you&#8217;re using a multiplexed character device, some escape sequences are interpreted in the input. </p>
<p> Note that some other command line options may implicitly create multiplexed character backends; for instance <code>-serial mon:stdio</code> creates a multiplexed stdio backend connected to the serial port and the QEMU monitor, and <code>-nographic</code> also multiplexes the console and the monitor to stdio. </p>
<p> There is currently no support for multiplexing in the other direction (where a single QEMU front end takes input and output from multiple chardevs). </p>
<p> Every backend supports the <code>logfile</code> option, which supplies the path to a file to record all data transmitted via the backend. The <code>logappend</code> option controls whether the log file will be truncated or appended to when opened.</dl>
<p> The available backends are:</p>
<dl>
<dt><code>-chardev null,id=</code><i>id</i></dt>
<dd> A void device. This device will not emit any data, and will drop any data it receives. The null backend does not take any options.</dd>
<dt><code>-chardev socket,id=</code><i>id</i><code>[,</code><i></i><i>TCP</i><i> options</i> <code>or</code> <i>unix options</i><code>][,server][,nowait][,telnet][,websocket][,reconnect=</code><i>seconds</i><code>][,tls-creds=</code><i>id</i><code>][,tls-authz=</code><i>id</i><code>]</code></dt>
<dd> Create a two-way stream socket, which can be either a TCP or a unix socket. A unix socket will be created if <code>path</code> is specified. Behaviour is undefined if TCP options are specified for a unix socket. </dd>
<p> <code>server</code> specifies that the socket shall be a listening socket. </p>
<p> <code>nowait</code> specifies that QEMU should not block waiting for a client to connect to a listening socket. </p>
<p> <code>telnet</code> specifies that traffic on the socket should interpret telnet escape sequences. </p>
<p> <code>websocket</code> specifies that the socket uses WebSocket protocol for communication. </p>
<p> <code>reconnect</code> sets the timeout for reconnecting on non-server sockets when the remote end goes away. qemu will delay this many seconds and then attempt to reconnect. Zero disables reconnecting, and is the default. </p>
<p> <code>tls-creds</code> requests enablement of the TLS protocol for encryption, and specifies the id of the TLS credentials to use for the handshake. The credentials must be previously created with the <code>-object tls-creds</code> argument. </p>
<p> <code>tls-auth</code> provides the ID of the QAuthZ authorization object against which the client&#8217;s x509 distinguished name will be validated. This object is only resolved at time of use, so can be deleted and recreated on the fly while the chardev server is active. If missing, it will default to denying access. </p>
<p> TCP and unix socket options are given below:</p>
<dl>
<dl>
<dt><code>TCP</code><code> options: port=</code><i>port</i><code>[,host=</code><i>host</i><code>][,to=</code><i>to</i><code>][,ipv4][,ipv6][,nodelay]</code></dt>
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
<dt><code>-chardev udp,id=</code><i>id</i><code>[,host=</code><i>host</i><code>],port=</code><i>port</i><code>[,localaddr=</code><i>localaddr</i><code>][,localport=</code><i>localport</i><code>][,ipv4][,ipv6]</code></dt>
<dd> Sends all traffic from the guest to a remote host over UDP. </dd>
<p> <code>host</code> specifies the remote host to connect to. If not specified it defaults to <tt>&quot;localhost&quot;</tt>. </p>
<p> <code>port</code> specifies the port on the remote host to connect to. <code>port</code> is required. </p>
<p> <code>localaddr</code> specifies the local address to bind to. If not specified it defaults to <tt>0.0.0.0</tt>. </p>
<p> <code>localport</code> specifies the local port to bind to. If not specified any available local port will be used. </p>
<p> <code>ipv4</code> and <code>ipv6</code> specify that either IPv4 or IPv6 must be used. If neither is specified the device may use either protocol.</p>
<dt><code>-chardev msmouse,id=</code><i>id</i></dt>
<dd> Forward QEMU&#8216;s emulated msmouse events to the guest. <code>msmouse</code> does not take any options.</dd>
<dt><code>-chardev vc,id=</code><i>id</i><code>[[,width=</code><i>width</i><code>][,height=</code><i>height</i><code>]][[,cols=</code><i>cols</i><code>][,rows=</code><i>rows</i><code>]]</code></dt>
<dd> Connect to a QEMU text console. <code>vc</code> may optionally be given a specific size. </dd>
<p> <code>width</code> and <code>height</code> specify the width and height respectively of the console, in pixels. </p>
<p> <code>cols</code> and <code>rows</code> specify that the console be sized to fit a text console with the given dimensions.</p>
<dt><code>-chardev ringbuf,id=</code><i>id</i><code>[,size=</code><i>size</i><code>]</code></dt>
<dd> Create a ring buffer with fixed size <code>size</code>. <i>size</i> must be a power of two and defaults to <tt>&quot;64K&quot;</tt>.</dd>
<dt><code>-chardev file,id=</code><i>id</i><code>,path=</code><i>path</i></dt>
<dd> Log all traffic received from the guest to a file. </dd>
<p> <code>path</code> specifies the path of the file to be opened. This file will be created if it does not already exist, and overwritten if it does. <code>path</code> is required.</p>
<dt><code>-chardev pipe,id=</code><i>id</i><code>,path=</code><i>path</i></dt>
<dd> Create a two-way connection to the guest. The behaviour differs slightly between Windows hosts and other hosts: </dd>
<p> On Windows, a single duplex pipe will be created at <i>\.pipe\</i>path<i></i>. </p>
<p> On other hosts, 2 pipes will be created called <i></i>path<i>.in</i> and <i></i>path<i>.out</i>. Data written to <i></i>path<i>.in</i> will be received by the guest. Data written by the guest can be read from <i></i>path<i>.out</i>. QEMU will not create these fifos, and requires them to be present. </p>
<p> <code>path</code> forms part of the pipe path as described above. <code>path</code> is required.</p>
<dt><code>-chardev console,id=</code><i>id</i></dt>
<dd> Send traffic from the guest to QEMU&#8216;s standard output. <code>console</code> does not take any options. </dd>
<p> <code>console</code> is only available on Windows hosts.</p>
<dt><code>-chardev serial,id=</code><i>id</i><code>,path=</code><code>path</code></dt>
<dd> Send traffic from the guest to a serial device on the host. </dd>
<p> On Unix hosts serial will actually accept any tty device, not only serial lines. </p>
<p> <code>path</code> specifies the name of the serial device to open.</p>
<dt><code>-chardev pty,id=</code><i>id</i></dt>
<dd> Create a new pseudo-terminal on the host and connect to it. <code>pty</code> does not take any options. </dd>
<p> <code>pty</code> is not available on Windows hosts.</p>
<dt><code>-chardev stdio,id=</code><i>id</i><code>[,signal=on|off]</code></dt>
<dd> Connect to standard input and standard output of the QEMU process. </dd>
<p> <code>signal</code> controls if signals are enabled on the terminal, that includes exiting QEMU with the key sequence <code>Control-c</code>. This option is enabled by default, use <code>signal=off</code> to disable it.</p>
<dt><code>-chardev braille,id=</code><i>id</i></dt>
<dd> Connect to a local BrlAPI server. <code>braille</code> does not take any options.</dd>
<dt><code>-chardev tty,id=</code><i>id</i><code>,path=</code><i>path</i></dt>
<dd> <code>tty</code> is only available on Linux, Sun, FreeBSD, NetBSD, OpenBSD and DragonFlyBSD hosts. It is an alias for <code>serial</code>. </dd>
<p> <code>path</code> specifies the path to the tty. <code>path</code> is required.</p>
<dt><code>-chardev parallel,id=</code><i>id</i><code>,path=</code><i>path</i></dt>
<dd>
</dd><dt><code>-chardev parport,id=</code><i>id</i><code>,path=</code><i>path</i></dt>
<dd> <code>parallel</code> is only available on Linux, FreeBSD and DragonFlyBSD hosts. </dd>
<p> Connect to a local parallel port. </p>
<p> <code>path</code> specifies the path to the parallel port device. <code>path</code> is required.</p>
<dt><code>-chardev spicevmc,id=</code><i>id</i><code>,debug=</code><i>debug</i><code>,name=</code><i>name</i></dt>
<dd> <code>spicevmc</code> is only available when spice support is built in. </dd>
<p> <code>debug</code> debug level for spicevmc </p>
<p> <code>name</code> name of spice channel to connect to </p>
<p> Connect to a spice virtual machine channel, such as vdiport.</p>
<dt><code>-chardev spiceport,id=</code><i>id</i><code>,debug=</code><i>debug</i><code>,name=</code><i>name</i></dt>
<dd> <code>spiceport</code> is only available when spice support is built in. </dd>
<p> <code>debug</code> debug level for spicevmc </p>
<p> <code>name</code> name of spice port to connect to </p>
<p> Connect to a spice port, allowing a Spice client to handle the traffic identified by a name (preferably a fqdn).</dl>
<p> <i>Bluetooth(R) options</i></p>
<dl>
<dt><code>-bt hci[&#8230;]</code></dt>
<dd> Defines the function of the corresponding Bluetooth HCI. -bt options are matched with the HCIs present in the chosen machine type. For example when emulating a machine with only one HCI built into it, only the first <tt>&quot;-bt hci[...]&quot;</tt> option is valid and defines the HCI&#8216;s logic. The Transport Layer is decided by the machine type. Currently the machines <tt>&quot;n800&quot;</tt> and <tt>&quot;n810&quot;</tt> have one HCI and all other machines have none. </dd>
<p> Note: This option and the whole bluetooth subsystem is considered as deprecated. If you still use it, please send a mail to &lt;<code>qemu-devel [at] nongnu.org</code>&gt; where you describe your usecase. </p>
<p> The following three types are recognized:</p>
<dl>
<dl>
<dt><code>-bt hci,null</code></dt>
<dd> (default) The corresponding Bluetooth HCI assumes no internal logic and will not respond to any HCI commands or emit events.</dd>
<dt><code>-bt hci,host[:</code><i>id</i><code>]</code></dt>
<dd> (<tt>&quot;bluez&quot;</tt> only) The corresponding HCI passes commands / events to / from the physical HCI identified by the name <i>id</i> (default: <tt>&quot;hci0&quot;</tt>) on the computer running QEMU. Only available on <tt>&quot;bluez&quot;</tt> capable systems like Linux.</dd>
<dt><code>-bt hci[,vlan=</code><i>n</i><code>]</code></dt>
<dd> Add a virtual, standard HCI that will participate in the Bluetooth scatternet <i>n</i> (default <tt>0</tt>). Similarly to <code>-net</code> VLANs, devices inside a bluetooth network <i>n</i> can only communicate with other devices in the same network (scatternet).</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-bt vhci[,vlan=</code><i>n</i><code>]</code></dt>
<dd> (Linux-host only) Create a HCI in scatternet <i>n</i> (default 0) attached to the host bluetooth stack instead of to the emulated target. This allows the host and target machines to participate in a common scatternet and communicate. Requires the Linux <tt>&quot;vhci&quot;</tt> driver installed. Can be used as following: </dd>
<pre>
        qemu-system-x86_64 [...OPTIONS...] -bt hci,vlan=5 -bt vhci,vlan=5
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
<p> <i></i><i>TPM</i><i> device options</i> </p>
<p> The general form of a TPM device option is:</p>
<dl>
<dt><code>-tpmdev</code> <i>backend</i><code>,id=</code><i>id</i><code>[,</code><i>options</i><code>]</code></dt>
<dd> The specific backend type will determine the applicable options. The <tt>&quot;-tpmdev&quot;</tt> option creates the TPM backend and requires a <tt>&quot;-device&quot;</tt> option that specifies the TPM frontend interface model. </dd>
<p> Use <tt>&quot;-tpmdev help&quot;</tt> to print all available TPM backend types.</dl>
<p> The available backends are:</p>
<dl>
<dt><code>-tpmdev passthrough,id=</code><i>id</i><code>,path=</code><i>path</i><code>,cancel-path=</code><i>cancel-path</i></dt>
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
<p> Note that the <tt>&quot;-tpmdev&quot;</tt> id is <tt>&quot;tpm0&quot;</tt> and is referenced by <tt>&quot;tpmdev=tpm0&quot;</tt> in the device option.</p>
<dt><code>-tpmdev emulator,id=</code><i>id</i><code>,chardev=</code><i>dev</i></dt>
<dd> (Linux-host only) Enable access to a TPM emulator using Unix domain socket based chardev backend. </dd>
<p> <code>chardev</code> specifies the unique ID of a character device backend that provides connection to the software TPM server. </p>
<p> To create a TPM emulator backend device with chardev socket backend: </p>
<pre>
        -chardev socket,id=chrtpm,path=/tmp/swtpm-sock -tpmdev emulator,id=tpm0,chardev=chrtpm -device tpm-tis,tpmdev=tpm0
</pre>
</dl>
<p> <i>Linux/Multiboot boot specific</i> </p>
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
<p> <i>Debug/Expert options</i></p>
<dl>
<dt><code>-fw_cfg [name=]</code><i>name</i><code>,file=</code><i>file</i></dt>
<dd> Add named fw_cfg entry with contents from file <i>file</i>.</dd>
<dt><code>-fw_cfg [name=]</code><i>name</i><code>,string=</code><i>str</i></dt>
<dd> Add named fw_cfg entry with contents from string <i>str</i>. </dd>
<p> The terminating NUL character of the contents of <i>str</i> will not be included as part of the fw_cfg item data. To insert contents with embedded NUL characters, you have to use the <i>file</i> parameter. </p>
<p> The fw_cfg entries are passed by QEMU through to the guest. </p>
<p> Example: </p>
<pre>
        -fw_cfg name=opt/com.mycompany/blob,file=./my_blob.bin
</pre>
<p> creates an fw_cfg entry named opt/com.mycompany/blob with contents from ./my_blob.bin.</p>
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
<p> If you plan to send characters back via netconsole or you want to stop and start QEMU a lot of times, you should have QEMU use the same source port each time by using something like <tt>&quot;-serial udp::4555 [at] 4556&quot;</tt> to QEMU. Another approach is to use a patched version of netcat which can listen to a TCP port and send and receive characters via udp. If you have a patched version of netcat which activates telnet remote echo and single char transfer, then you can use the following options to set up a netcat redirector to allow telnet on port 5555 to access the QEMU port.</p>
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
<dt><code>tcp:[</code><i>host</i><code>]:</code><i>port</i><code>[,</code><i>server</i><code>][,nowait][,nodelay][,reconnect=</code><i>seconds</i><code>]</code></dt>
<dd> The TCP Net Console has two modes of operation. It can send the serial I/O to a location or wait for a connection from a location. By default the TCP Net Console is sent to <i>host</i> at the <i>port</i>. If you use the <i>server</i> option QEMU will wait for a client socket application to connect to the port before continuing, unless the <tt>&quot;nowait&quot;</tt> option was specified. The <tt>&quot;nodelay&quot;</tt> option disables the Nagle buffering algorithm. The <tt>&quot;reconnect&quot;</tt> option only applies if <i>noserver</i> is set, if the connection goes down it will attempt to reconnect at the given interval. If <i>host</i> is omitted, 0.0.0.0 is assumed. Only one TCP connection at a time is accepted. You can use <tt>&quot;telnet&quot;</tt> to connect to the corresponding character device.</dd>
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
<dt><code>websocket:</code><i>host</i><code>:</code><i>port</i><code>,server[,nowait][,nodelay]</code></dt>
<dd> The WebSocket protocol is used instead of raw tcp socket. The port acts as a WebSocket server. Client mode is not supported.</dd>
<dt><code>unix:</code><i>path</i><code>[,server][,nowait][,reconnect=</code><i>seconds</i><code>]</code></dt>
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
<dt><code>-qmp-pretty</code> <i>dev</i></dt>
<dd> Like -qmp but uses pretty JSON formatting.</dd>
<dt><code>-mon [chardev=]name[,mode=readline|control][,pretty[=on|off]]</code></dt>
<dd> Setup monitor on chardev <i>name</i>. <tt>&quot;pretty&quot;</tt> turns on JSON pretty printing easing human reading and debugging.</dd>
<dt><code>-debugcon</code> <i>dev</i></dt>
<dd> Redirect the debug console to host device <i>dev</i> (same devices as the serial port). The debug console is an I/O port which is typically port 0xe9; writing to that I/O port sends output to this device. The default device is <tt>&quot;vc&quot;</tt> in graphical mode and <tt>&quot;stdio&quot;</tt> in non graphical mode.</dd>
<dt><code>-pidfile</code> <i>file</i></dt>
<dd> Store the QEMU process PID in <i>file</i>. It is useful if you launch QEMU from a script.</dd>
<dt><code>-singlestep</code></dt>
<dd> Run the emulation in single step mode.</dd>
<dt><code>&#8211;preconfig</code></dt>
<dd> Pause QEMU for interactive configuration before the machine is created, which allows querying and configuring properties that will affect machine initialization. Use QMP command &#8216;x-exit-preconfig&#8217; to exit the preconfig state and move to the next state (i.e. run guest if -S isn&#8217;t used or pause the second time if -S is used). This option is experimental.</dd>
<dt><code>-S</code></dt>
<dd> Do not start CPU at startup (you must type &#8216;c&#8217; in the monitor).</dd>
<dt><code>-realtime mlock=on|off</code></dt>
<dd> Run qemu with realtime features. mlocking qemu and guest memory can be enabled via <code>mlock=on</code> (enabled by default).</dd>
<dt><code>-overcommit mem-lock=on|off</code></dt>
<dd>
</dd><dt><code>-overcommit cpu-pm=on|off</code></dt>
<dd> Run qemu with hints about host resource overcommit. The default is to assume that host overcommits all resources. </dd>
<p> Locking qemu and guest memory can be enabled via <code>mem-lock=on</code> (disabled by default). This works when host memory is not overcommitted and reduces the worst-case latency for guest. This is equivalent to <code>realtime</code>. </p>
<p> Guest ability to manage power state of host cpus (increasing latency for other processes on the same host cpu, but decreasing latency for guest) can be enabled via <code>cpu-pm=on</code> (disabled by default). This works best when host CPU is not overcommitted. When used, host estimates of CPU cycle and power utilization will be incorrect, not taking into account guest idle time.</p>
<dt><code>-gdb</code> <i>dev</i></dt>
<dd> Wait for gdb connection on device <i>dev</i>. Typical connections will likely be TCP-based, but also UDP, pseudo TTY, or even stdio are reasonable use case. The latter is allowing to start QEMU from within gdb and establish the connection via a pipe: </dd>
<pre>
        (gdb) target remote | exec qemu-system-x86_64 -gdb stdio ...
</pre>
<dt><code>-s</code></dt>
<dd> Shorthand for -gdb tcp::1234, i.e. open a gdbserver on TCP port 1234.</dd>
<dt><code>-d</code> <i>item1</i><code>[,&#8230;]</code></dt>
<dd> Enable logging of specified items. Use &#8216;-d help&#8217; for a list of log items.</dd>
<dt><code>-D</code> <i>logfile</i></dt>
<dd> Output log in <i>logfile</i> instead of to stderr</dd>
<dt><code>-dfilter</code> <i>range1</i><code>[,&#8230;]</code></dt>
<dd> Filter debug output to that relevant to a range of target addresses. The filter spec can be either <i>start</i>+<i>size</i>, <i>start</i>&#8211;<i>size</i> or <i>start</i>..<i>end</i> where <i>start</i> <i>end</i> and <i>size</i> are the addresses and sizes required. For example: </dd>
<pre>
        -dfilter 0x8000..0x8fff,0xffffffc000080000+0x200,0xffffffc000060000-0x1000
</pre>
<p> Will dump output for any code in the 0x1000 sized block starting at 0x8000 and the 0x200 sized block starting at 0xffffffc000080000 and another 0x1000 sized block starting at 0xffffffc00005f000.</p>
<dt><code>-seed</code> <i>number</i></dt>
<dd> Force the guest to use a deterministic pseudo-random number generator, seeded with <i>number</i>. This does not affect crypto routines within the host.</dd>
<dt><code>-L</code> <i>path</i></dt>
<dd> Set the directory for the BIOS, VGA BIOS and keymaps. </dd>
<p> To list all the data directories, use <tt>&quot;-L help&quot;</tt>.</p>
<dt><code>-bios</code> <i>file</i></dt>
<dd> Set the filename for the BIOS.</dd>
<dt><code>-enable-kvm</code></dt>
<dd> Enable KVM full virtualization support. This option is only available if KVM support is enabled when compiling.</dd>
<dt><code>-xen-domid</code> <i>id</i></dt>
<dd> Specify xen guest domain <i>id</i> (XEN only).</dd>
<dt><code>-xen-attach</code></dt>
<dd> Attach to existing xen domain. libxl will use this when starting QEMU (XEN only). Restrict set of available xen operations to specified domain id (XEN only).</dd>
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
<dt><code>-rtc [base=utc|localtime|</code><i>datetime</i><code>][,clock=host|rt|vm][,driftfix=none|slew]</code></dt>
<dd> Specify <code>base</code> as <tt>&quot;utc&quot;</tt> or <tt>&quot;localtime&quot;</tt> to let the RTC start at the current UTC or local time, respectively. <tt>&quot;localtime&quot;</tt> is required for correct date in MS-DOS or Windows. To start at a specific point in time, provide <i>datetime</i> in the format <tt>&quot;2006-06-17T16:01:21&quot;</tt> or <tt>&quot;2006-06-17&quot;</tt>. The default base is UTC. </dd>
<p> By default the RTC is driven by the host system time. This allows using of the RTC as accurate reference clock inside the guest, specifically if the host time is smoothly following an accurate external reference clock, e.g. via NTP. If you want to isolate the guest time from the host, you can set <code>clock</code> to <tt>&quot;rt&quot;</tt> instead, which provides a host monotonic clock if host support it. To even prevent the RTC from progressing during suspension, you can set <code>clock</code> to <tt>&quot;vm&quot;</tt> (virtual clock). <code>clock=vm</code> is recommended especially in icount mode in order to preserve determinism; however, note that in icount mode the speed of the virtual clock is variable and can in general differ from the host clock. </p>
<p> Enable <code>driftfix</code> (i386 targets only) if you experience time drift problems, specifically with Windows&#8217; ACPI HAL. This option will try to figure out how many timer interrupts were not processed by the Windows guest and will re-inject them.</p>
<dt><code>-icount [shift=</code><i>N</i><code>|auto][,rr=record|replay,rrfile=</code><i>filename</i><code>,rrsnapshot=</code><i>snapshot</i><code>]</code></dt>
<dd> Enable virtual instruction counter. The virtual cpu will execute one instruction every 2^<i>N</i> ns of virtual time. If <tt>&quot;auto&quot;</tt> is specified then the virtual cpu speed will be automatically adjusted to keep virtual time within a few seconds of real time. </dd>
<p> When the virtual cpu is sleeping, the virtual time will advance at default speed unless <code>sleep=on|off</code> is specified. With <code>sleep=on|off</code>, the virtual time will jump to the next timer deadline instantly whenever the virtual cpu goes to sleep mode and will not advance if no timer is enabled. This behavior give deterministic execution times from the guest point of view. </p>
<p> Note that while this option can give deterministic behavior, it does not provide cycle accurate emulation. Modern CPUs contain superscalar out of order cores with complex cache hierarchies. The number of instructions executed often has little or no correlation with actual performance. </p>
<p> <code>align=on</code> will activate the delay algorithm which will try to synchronise the host clock and the virtual clock. The goal is to have a guest running at the real frequency imposed by the shift option. Whenever the guest clock is behind the host clock and if <code>align=on</code> is specified then we print a message to the user to inform about the delay. Currently this option does not work when <code>shift</code> is <tt>&quot;auto&quot;</tt>. Note: The sync algorithm will work for those shift values for which the guest clock runs ahead of the host clock. Typically this happens when the shift value is high (how high depends on the host machine). </p>
<p> When <code>rr</code> option is specified deterministic record/replay is enabled. Replay log is written into <i>filename</i> file in record mode and read from this file in replay mode. </p>
<p> Option rrsnapshot is used to create new vm snapshot named <i>snapshot</i> at the start of execution recording. In replay mode this option is used to load the initial VM state.</p>
<dt><code>-watchdog</code> <i>model</i></dt>
<dd> Create a virtual hardware watchdog device. Once enabled (by a guest action), the watchdog must be periodically polled by an agent inside the guest or else the guest will be restarted. Choose a model for which your guest has drivers. </dd>
<p> The <i>model</i> is the model of hardware watchdog to emulate. Use <tt>&quot;-watchdog help&quot;</tt> to list available hardware models. Only one watchdog can be enabled for a guest. </p>
<p> The following models may be available:</p>
<dl>
<dl>
<dt><code>ib700</code></dt>
<dd> iBASE 700 is a very simple ISA watchdog with a single timer.</dd>
<dt><code>i6300esb</code></dt>
<dd> Intel 6300ESB I/O controller hub is a much more featureful PCI-based dual-timer watchdog.</dd>
<dt><code>diag288</code></dt>
<dd> A virtual watchdog for s390x backed by the diagnose 288 hypercall (currently KVM only).</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-watchdog-action</code> <i>action</i></dt>
<dd> The <i>action</i> controls what QEMU will do when the watchdog timer expires. The default is <tt>&quot;reset&quot;</tt> (forcefully reset the guest). Other possible actions are: <tt>&quot;shutdown&quot;</tt> (attempt to gracefully shutdown the guest), <tt>&quot;poweroff&quot;</tt> (forcefully poweroff the guest), <tt>&quot;inject-nmi&quot;</tt> (inject a NMI into the guest), <tt>&quot;pause&quot;</tt> (pause the guest), <tt>&quot;debug&quot;</tt> (print a debug message and continue), or <tt>&quot;none&quot;</tt> (do nothing). </dd>
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
<dt><code>-show-cursor</code></dt>
<dd> Show cursor.</dd>
<dt><code>-tb-size</code> <i>n</i></dt>
<dd> Set TB size.</dd>
<dt><code>-incoming tcp:[</code><i>host</i><code>]:</code><i>port</i><code>[,to=</code><i>maxport</i><code>][,ipv4][,ipv6]</code></dt>
<dd>
</dd><dt><code>-incoming rdma:</code><i>host</i><code>:</code><i>port</i><code>[,ipv4][,ipv6]</code></dt>
<dd> Prepare for incoming migration, listen on a given tcp port.</dd>
<dt><code>-incoming unix:</code><i>socketpath</i></dt>
<dd> Prepare for incoming migration, listen on a given unix socket.</dd>
<dt><code>-incoming fd:</code><i>fd</i></dt>
<dd> Accept incoming migration from a given filedescriptor.</dd>
<dt><code>-incoming exec:</code><i>cmdline</i></dt>
<dd> Accept incoming migration as an output from specified external command.</dd>
<dt><code>-incoming defer</code></dt>
<dd> Wait for the URI to be specified via migrate_incoming. The monitor can be used to change settings (such as migration parameters) prior to issuing the migrate_incoming to allow the migration to begin.</dd>
<dt><code>-only-migratable</code></dt>
<dd> Only allow migratable devices. Devices will not be allowed to enter an unmigratable state.</dd>
<dt><code>-nodefaults</code></dt>
<dd> Don&#8217;t create default devices. Normally, QEMU sets the default devices like serial port, parallel port, virtual console, monitor device, VGA adapter, floppy and CD-ROM drive and others. The <tt>&quot;-nodefaults&quot;</tt> option will disable all those default devices.</dd>
<dt><code>-chroot</code> <i>dir</i></dt>
<dd> Immediately before starting guest execution, chroot to the specified directory. Especially useful in combination with -runas.</dd>
<dt><code>-runas</code> <i>user</i></dt>
<dd> Immediately before starting guest execution, drop root privileges, switching to the specified user.</dd>
<dt><code>-prom-env</code> <i>variable</i><code>=</code><i>value</i></dt>
<dd> Set OpenBIOS nvram <i>variable</i> to given <i>value</i> (PPC, SPARC only).</dd>
<dt><code>-semihosting</code></dt>
<dd> Enable semihosting mode (ARM, M68K, Xtensa, MIPS, Nios II only).</dd>
<dt><code>-semihosting-config [enable=on|off][,target=native|gdb|auto][,chardev=id][,arg=str[,&#8230;]]</code></dt>
<dd> Enable and configure semihosting (ARM, M68K, Xtensa, MIPS, Nios II only).</dd>
<dl>
<dl>
<dt><code>target=</code>&quot;native|gdb|auto&quot;</dt>
<dd> Defines where the semihosting calls will be addressed, to QEMU (<tt>&quot;native&quot;</tt>) or to GDB (<tt>&quot;gdb&quot;</tt>). The default is <tt>&quot;auto&quot;</tt>, which means <tt>&quot;gdb&quot;</tt> during debug sessions and <tt>&quot;native&quot;</tt> otherwise.</dd>
<dt><code>chardev=</code><i>str1</i></dt>
<dd> Send the output to a chardev backend output for native or auto output when not in gdb</dd>
<dt><code>arg=</code><i>str1</i><code>,arg=</code><i>str2</i><code>,&#8230;</code></dt>
<dd> Allows the user to pass input arguments, and can be used multiple times to build up a list. The old-style <tt>&quot;-kernel&quot;</tt>/<tt>&quot;-append&quot;</tt> method of passing a command line is still supported for backward compatibility. If both the <tt>&quot;--semihosting-config arg&quot;</tt> and the <tt>&quot;-kernel&quot;</tt>/<tt>&quot;-append&quot;</tt> are specified, the former is passed to semihosting as it always takes precedence.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-old-param</code></dt>
<dd> Old param mode (ARM only).</dd>
<dt><code>-sandbox</code> <i>arg</i><code>[,obsolete=</code><i>string</i><code>][,elevateprivileges=</code><i>string</i><code>][,spawn=</code><i>string</i><code>][,resourcecontrol=</code><i>string</i><code>]</code></dt>
<dd> Enable Seccomp mode 2 system call filter. &#8216;on&#8217; will enable syscall filtering and &#8216;off&#8217; will disable it. The default is &#8216;off&#8217;.</dd>
<dl>
<dl>
<dt><code>obsolete=</code><i>string</i></dt>
<dd> Enable Obsolete system calls</dd>
<dt><code>elevateprivileges=</code><i>string</i></dt>
<dd> Disable set*uid|gid system calls</dd>
<dt><code>spawn=</code><i>string</i></dt>
<dd> Disable *fork and execve</dd>
<dt><code>resourcecontrol=</code><i>string</i></dt>
<dd> Disable process affinity and schedular priority</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-readconfig</code> <i>file</i></dt>
<dd> Read device configuration from <i>file</i>. This approach is useful when you want to spawn QEMU process with many command line options but you don&#8217;t want to exceed the command line character limit.</dd>
<dt><code>-writeconfig</code> <i>file</i></dt>
<dd> Write device configuration to <i>file</i>. The <i>file</i> can be either filename to save command line and device configuration into file or dash <tt>&quot;-&quot;</tt>) character to print the output to stdout. This can be later used as input file for <tt>&quot;-readconfig&quot;</tt> option.</dd>
<dt><code>-no-user-config</code></dt>
<dd> The <tt>&quot;-no-user-config&quot;</tt> option makes QEMU not load any of the user-provided config files on <i>sysconfdir</i>.</dd>
<dt><code>-trace [[enable=]</code><i>pattern</i><code>][,events=</code><i>file</i><code>][,file=</code><i>file</i><code>]</code></dt>
<dd> Specify tracing options.</dd>
<dl>
<dl>
<dt><code>[enable=]</code><i>pattern</i></dt>
<dd> Immediately enable events matching <i>pattern</i> (either event name or a globbing pattern). This option is only available if QEMU has been compiled with the <i>simple</i>, <i>log</i> or <i>ftrace</i> tracing backend. To specify multiple events or patterns, specify the <code>-trace</code> option multiple times. </dd>
<p> Use <tt>&quot;-trace help&quot;</tt> to print a list of names of trace points.</p>
<dt><code>events=</code><i>file</i></dt>
<dd> Immediately enable events listed in <i>file</i>. The file must contain one event name (as listed in the <i>trace-events-all</i> file) per line; globbing patterns are accepted too. This option is only available if QEMU has been compiled with the <i>simple</i>, <i>log</i> or <i>ftrace</i> tracing backend.</dd>
<dt><code>file=</code><i>file</i></dt>
<dd> Log output traces to <i>file</i>. This option is only available if QEMU has been compiled with the <i>simple</i> tracing backend.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-plugin file=</code><i>file</i><code>[,arg=</code><i>string</i><code>]</code></dt>
<dd> Load a plugin.</dd>
<dl>
<dl>
<dt><code>file=</code><i>file</i></dt>
<dd> Load the given plugin from a shared library file.</dd>
<dt><code>arg=</code><i>string</i></dt>
<dd> Argument string passed to the plugin. (Can be given multiple times.)</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-enable-fips</code></dt>
<dd> Enable FIPS 140-2 compliance mode.</dd>
<dt><code>-msg timestamp[=on|off]</code></dt>
<dd> prepend a timestamp to each log message.(default:on)</dd>
<dt><code>-dump-vmstate</code> <i>file</i></dt>
<dd> Dump json-encoded vmstate information for current machine type to file in <i>file</i></dd>
<dt><code>-enable-sync-profile</code></dt>
<dd> Enable synchronization profiling.</dd></dl>
<p> <i>Generic object creation</i></p>
<dl>
<dt><code>-object</code> <i>typename</i><code>[,</code><i>prop1</i><code>=</code><i>value1</i><code>,&#8230;]</code></dt>
<dd> Create a new object of type <i>typename</i> setting properties in the order they are specified. Note that the &#8216;id&#8217; property must be set. These objects are placed in the &#8216;/objects&#8217; path.</dd>
<dl>
<dl>
<dt><code>-object memory-backend-file,id=</code><i>id</i><code>,size=</code><i>size</i><code>,mem-path=</code><i>dir</i><code>,share=</code><i>on|off</i><code>,discard-data=</code><i>on|off</i><code>,merge=</code><i>on|off</i><code>,dump=</code><i>on|off</i><code>,prealloc=</code><i>on|off</i><code>,host-nodes=</code><i>host-nodes</i><code>,policy=</code><i>default|preferred|bind|interleave</i><code>,align=</code><i>align</i></dt>
<dd> Creates a memory file backend object, which can be used to back the guest RAM with huge pages. </dd>
<p> The <code>id</code> parameter is a unique ID that will be used to reference this memory region when configuring the <code>-numa</code> argument. </p>
<p> The <code>size</code> option provides the size of the memory region, and accepts common suffixes, eg <code>500M</code>. </p>
<p> The <code>mem-path</code> provides the path to either a shared memory or huge page filesystem mount. </p>
<p> The <code>share</code> boolean option determines whether the memory region is marked as private to QEMU, or shared. The latter allows a co-operating external process to access the QEMU memory region. </p>
<p> The <code>share</code> is also required for pvrdma devices due to limitations in the RDMA API provided by Linux. </p>
<p> Setting share=on might affect the ability to configure NUMA bindings for the memory backend under some circumstances, see Documentation/vm/numa_memory_policy.txt on the Linux kernel source tree for additional details. </p>
<p> Setting the <code>discard-data</code> boolean option to <i>on</i> indicates that file contents can be destroyed when QEMU exits, to avoid unnecessarily flushing data to the backing file. Note that <code>discard-data</code> is only an optimization, and QEMU might not discard file contents if it aborts unexpectedly or is terminated using SIGKILL. </p>
<p> The <code>merge</code> boolean option enables memory merge, also known as MADV_MERGEABLE, so that Kernel Samepage Merging will consider the pages for memory deduplication. </p>
<p> Setting the <code>dump</code> boolean option to <i>off</i> excludes the memory from core dumps. This feature is also known as MADV_DONTDUMP. </p>
<p> The <code>prealloc</code> boolean option enables memory preallocation. </p>
<p> The <code>host-nodes</code> option binds the memory range to a list of NUMA host nodes. </p>
<p> The <code>policy</code> option sets the NUMA policy to one of the following values:</p>
<dl>
<dl>
<dt><i>default</i></dt>
<dd> default host policy</dd>
<dt><i>preferred</i></dt>
<dd> prefer the given host node list for allocation</dd>
<dt><i>bind</i></dt>
<dd> restrict memory allocation to the given host node list</dd>
<dt><i>interleave</i></dt>
<dd> interleave memory allocations across the given host node list</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> The <code>align</code> option specifies the base address alignment when QEMU <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) <code>mem-path</code>, and accepts common suffixes, eg <code>2M</code>. Some backend store specified by <code>mem-path</code> requires an alignment different than the default one used by QEMU, eg the device DAX /dev/dax0.0 requires 2M alignment rather than 4K. In such cases, users can specify the required alignment via this option. </p>
<p> The <code>pmem</code> option specifies whether the backing file specified by <code>mem-path</code> is in host persistent memory that can be accessed using the SNIA NVM programming model (e.g. Intel NVDIMM). If <code>pmem</code> is set to &#8216;on&#8217;, QEMU will take necessary operations to guarantee the persistence of its own writes to <code>mem-path</code> (e.g. in vNVDIMM label emulation and live migration). Also, we will map the backend-file with MAP_SYNC flag, which ensures the file metadata is in sync for <code>mem-path</code> in case of host crash or a power failure. MAP_SYNC requires support from both the host kernel (since Linux kernel 4.15) and the filesystem of <code>mem-path</code> mounted with DAX option.</dd></dl>
<dt><code>-object memory-backend-ram,id=</code><i>id</i><code>,merge=</code><i>on|off</i><code>,dump=</code><i>on|off</i><code>,share=</code><i>on|off</i><code>,prealloc=</code><i>on|off</i><code>,size=</code><i>size</i><code>,host-nodes=</code><i>host-nodes</i><code>,policy=</code><i>default|preferred|bind|interleave</i></dt>
<dd> Creates a memory backend object, which can be used to back the guest RAM. Memory backend objects offer more control than the <code>-m</code> option that is traditionally used to define guest RAM. Please refer to <code>memory-backend-file</code> for a description of the options.</dd>
<dt><code>-object memory-backend-memfd,id=</code><i>id</i><code>,merge=</code><i>on|off</i><code>,dump=</code><i>on|off</i><code>,share=</code><i>on|off</i><code>,prealloc=</code><i>on|off</i><code>,size=</code><i>size</i><code>,host-nodes=</code><i>host-nodes</i><code>,policy=</code><i>default|preferred|bind|interleave</i><code>,seal=</code><i>on|off</i><code>,hugetlb=</code><i>on|off</i><code>,hugetlbsize=</code><i>size</i></dt>
<dd> Creates an anonymous memory file backend object, which allows QEMU to share the memory with an external process (e.g. when using vhost-user). The memory is allocated with memfd and optional sealing. (Linux only) </dd>
<p> The <code>seal</code> option creates a sealed-file, that will block further resizing the memory (&#8216;on&#8217; by default). </p>
<p> The <code>hugetlb</code> option specify the file to be created resides in the hugetlbfs filesystem (since Linux 4.14). Used in conjunction with the <code>hugetlb</code> option, the <code>hugetlbsize</code> option specify the hugetlb page size on systems that support multiple hugetlb page sizes (it must be a power of 2 value supported by the system). </p>
<p> In some versions of Linux, the <code>hugetlb</code> option is incompatible with the <code>seal</code> option (requires at least Linux 4.16). </p>
<p> Please refer to <code>memory-backend-file</code> for a description of the other options. </p>
<p> The <code>share</code> boolean option is <i>on</i> by default with memfd.</p>
<dt><code>-object rng-builtin,id=</code><i>id</i></dt>
<dd> Creates a random number generator backend which obtains entropy from QEMU builtin functions. The <code>id</code> parameter is a unique ID that will be used to reference this entropy backend from the <code>virtio-rng</code> device. By default, the <code>virtio-rng</code> device uses this RNG backend.</dd>
<dt><code>-object rng-random,id=</code><i>id</i><code>,filename=</code><i>/dev/random</i></dt>
<dd> Creates a random number generator backend which obtains entropy from a device on the host. The <code>id</code> parameter is a unique ID that will be used to reference this entropy backend from the <code>virtio-rng</code> device. The <code>filename</code> parameter specifies which file to obtain entropy from and if omitted defaults to <code>/dev/urandom</code>.</dd>
<dt><code>-object rng-egd,id=</code><i>id</i><code>,chardev=</code><i>chardevid</i></dt>
<dd> Creates a random number generator backend which obtains entropy from an external daemon running on the host. The <code>id</code> parameter is a unique ID that will be used to reference this entropy backend from the <code>virtio-rng</code> device. The <code>chardev</code> parameter is the unique ID of a character device backend that provides the connection to the RNG daemon.</dd>
<dt><code>-object tls-creds-anon,id=</code><i>id</i><code>,endpoint=</code><i>endpoint</i><code>,dir=</code><i>/path/to/cred/dir</i><code>,verify-peer=</code><i>on|off</i></dt>
<dd> Creates a TLS anonymous credentials object, which can be used to provide TLS support on network backends. The <code>id</code> parameter is a unique ID which network backends will use to access the credentials. The <code>endpoint</code> is either <code>server</code> or <code>client</code> depending on whether the QEMU network backend that uses the credentials will be acting as a client or as a server. If <code>verify-peer</code> is enabled (the default) then once the handshake is completed, the peer credentials will be verified, though this is a no-op for anonymous credentials. </dd>
<p> The <i>dir</i> parameter tells QEMU where to find the credential files. For server endpoints, this directory may contain a file <i>dh-params.pem</i> providing diffie-hellman parameters to use for the TLS server. If the file is missing, QEMU will generate a set of DH parameters at startup. This is a computationally expensive operation that consumes random pool entropy, so it is recommended that a persistent set of parameters be generated upfront and saved.</p>
<dt><code>-object tls-creds-psk,id=</code><i>id</i><code>,endpoint=</code><i>endpoint</i><code>,dir=</code><i>/path/to/keys/dir</i><code>[,username=</code><i>username</i><code>]</code></dt>
<dd> Creates a TLS Pre-Shared Keys (PSK) credentials object, which can be used to provide TLS support on network backends. The <code>id</code> parameter is a unique ID which network backends will use to access the credentials. The <code>endpoint</code> is either <code>server</code> or <code>client</code> depending on whether the QEMU network backend that uses the credentials will be acting as a client or as a server. For clients only, <code>username</code> is the username which will be sent to the server. If omitted it defaults to &#8220;qemu&#8221;. </dd>
<p> The <i>dir</i> parameter tells QEMU where to find the keys file. It is called &quot;<i>dir</i>/keys.psk&#8220; and contains &#8221;username:key&quot; pairs. This file can most easily be created using the GnuTLS <tt>&quot;psktool&quot;</tt> program. </p>
<p> For server endpoints, <i>dir</i> may also contain a file <i>dh-params.pem</i> providing diffie-hellman parameters to use for the TLS server. If the file is missing, QEMU will generate a set of DH parameters at startup. This is a computationally expensive operation that consumes random pool entropy, so it is recommended that a persistent set of parameters be generated up front and saved.</p>
<dt><code>-object tls-creds-x509,id=</code><i>id</i><code>,endpoint=</code><i>endpoint</i><code>,dir=</code><i>/path/to/cred/dir</i><code>,priority=</code><i>priority</i><code>,verify-peer=</code><i>on|off</i><code>,passwordid=</code><i>id</i></dt>
<dd> Creates a TLS anonymous credentials object, which can be used to provide TLS support on network backends. The <code>id</code> parameter is a unique ID which network backends will use to access the credentials. The <code>endpoint</code> is either <code>server</code> or <code>client</code> depending on whether the QEMU network backend that uses the credentials will be acting as a client or as a server. If <code>verify-peer</code> is enabled (the default) then once the handshake is completed, the peer credentials will be verified. With x509 certificates, this implies that the clients must be provided with valid client certificates too. </dd>
<p> The <i>dir</i> parameter tells QEMU where to find the credential files. For server endpoints, this directory may contain a file <i>dh-params.pem</i> providing diffie-hellman parameters to use for the TLS server. If the file is missing, QEMU will generate a set of DH parameters at startup. This is a computationally expensive operation that consumes random pool entropy, so it is recommended that a persistent set of parameters be generated upfront and saved. </p>
<p> For x509 certificate credentials the directory will contain further files providing the x509 certificates. The certificates must be stored in PEM format, in filenames <i>ca-cert.pem</i>, <i>ca-crl.pem</i> (optional), <i>server-cert.pem</i> (only servers), <i>server-key.pem</i> (only servers), <i>client-cert.pem</i> (only clients), and <i>client-key.pem</i> (only clients). </p>
<p> For the <i>server-key.pem</i> and <i>client-key.pem</i> files which contain sensitive private keys, it is possible to use an encrypted version by providing the <i>passwordid</i> parameter. This provides the ID of a previously created <tt>&quot;secret&quot;</tt> object containing the password for decryption. </p>
<p> The <i>priority</i> parameter allows to override the global default priority used by gnutls. This can be useful if the system administrator needs to use a weaker set of crypto priorities for QEMU without potentially forcing the weakness onto all applications. Or conversely if one wants wants a stronger default for QEMU than for all other applications, they can do this through this parameter. Its format is a gnutls priority string as described at &lt;<code><a rel="nofollow" href="https://gnutls.org/manual/html_node/Priority-Strings.html">https://gnutls.org/manual/html_node/Priority-Strings.html</a></code>&gt;.</p>
<dt><code>-object filter-buffer,id=</code><i>id</i><code>,netdev=</code><i>netdevid</i><code>,interval=</code><i>t</i><code>[,queue=</code><i>all|rx|tx</i><code>][,status=</code><i>on|off</i><code>]</code></dt>
<dd> Interval <i>t</i> can&#8217;t be 0, this filter batches the packet delivery: all packets arriving in a given interval on netdev <i>netdevid</i> are delayed until the end of the interval. Interval is in microseconds. <code>status</code> is optional that indicate whether the netfilter is on (enabled) or off (disabled), the default status for netfilter will be &#8216;on&#8217;. </dd>
<p> queue <i>all|rx|tx</i> is an option that can be applied to any netfilter. </p>
<p> <code>all</code>: the filter is attached both to the receive and the transmit queue of the netdev (default). </p>
<p> <code>rx</code>: the filter is attached to the receive queue of the netdev, where it will receive packets sent to the netdev. </p>
<p> <code>tx</code>: the filter is attached to the transmit queue of the netdev, where it will receive packets sent by the netdev.</p>
<dt><code>-object filter-mirror,id=</code><i>id</i><code>,netdev=</code><i>netdevid</i><code>,outdev=</code><i>chardevid</i><code>,queue=</code><i>all|rx|tx</i><code>[,vnet_hdr_support]</code></dt>
<dd> filter-mirror on netdev <i>netdevid</i>,mirror net packet to chardev<i>chardevid</i>, if it has the vnet_hdr_support flag, filter-mirror will mirror packet with vnet_hdr_len.</dd>
<dt><code>-object filter-redirector,id=</code><i>id</i><code>,netdev=</code><i>netdevid</i><code>,indev=</code><i>chardevid</i><code>,outdev=</code><i>chardevid</i><code>,queue=</code><i>all|rx|tx</i><code>[,vnet_hdr_support]</code></dt>
<dd> filter-redirector on netdev <i>netdevid</i>,redirect filter&#8217;s net packet to chardev <i>chardevid</i>,and redirect indev&#8217;s packet to filter.if it has the vnet_hdr_support flag, filter-redirector will redirect packet with vnet_hdr_len. Create a filter-redirector we need to differ outdev id from indev id, id can not be the same. we can just use indev or outdev, but at least one of indev or outdev need to be specified.</dd>
<dt><code>-object filter-rewriter,id=</code><i>id</i><code>,netdev=</code><i>netdevid</i><code>,queue=</code><i>all|rx|tx</i><code>,[vnet_hdr_support]</code></dt>
<dd> Filter-rewriter is a part of COLO project.It will rewrite tcp packet to secondary from primary to keep secondary tcp connection,and rewrite tcp packet to primary from secondary make tcp packet can be handled by client.if it has the vnet_hdr_support flag, we can parse packet with vnet header. </dd>
<p> usage: colo secondary: -object filter-redirector,id=f1,netdev=hn0,queue=tx,indev=red0 -object filter-redirector,id=f2,netdev=hn0,queue=rx,outdev=red1 -object filter-rewriter,id=rew0,netdev=hn0,queue=all</p>
<dt><code>-object filter-dump,id=</code><i>id</i><code>,netdev=</code><i>dev</i><code>[,file=</code><i>filename</i><code>][,maxlen=</code><i>len</i><code>]</code></dt>
<dd> Dump the network traffic on netdev <i>dev</i> to the file specified by <i>filename</i>. At most <i>len</i> bytes (64k by default) per packet are stored. The file format is libpcap, so it can be analyzed with tools such as tcpdump or Wireshark.</dd>
<dt><code>-object colo-compare,id=</code><i>id</i><code>,primary_in=</code><i>chardevid</i><code>,secondary_in=</code><i>chardevid</i><code>,outdev=</code><i>chardevid</i><code>,iothread=</code><i>id</i><code>[,vnet_hdr_support][,notify_dev=</code><i>id</i><code>]</code></dt>
<dd> Colo-compare gets packet from primary_in<i>chardevid</i> and secondary_in<i>chardevid</i>, than compare primary packet with secondary packet. If the packets are same, we will output primary packet to outdev<i>chardevid</i>, else we will notify colo-frame do checkpoint and send primary packet to outdev<i>chardevid</i>. In order to improve efficiency, we need to put the task of comparison in another thread. If it has the vnet_hdr_support flag, colo compare will send/recv packet with vnet_hdr_len. If you want to use Xen COLO, will need the notify_dev to notify Xen colo-frame to do checkpoint. </dd>
<p> we must use it with the help of filter-mirror and filter-redirector. </p>
<pre>
        KVM COLO
        primary:
        -netdev tap,id=hn0,vhost=off,script=/etc/qemu-ifup,downscript=/etc/qemu-ifdown
        -device e1000,id=e0,netdev=hn0,mac=52:a4:00:12:78:66
        -chardev socket,id=mirror0,host=3.3.3.3,port=9003,server,nowait
        -chardev socket,id=compare1,host=3.3.3.3,port=9004,server,nowait
        -chardev socket,id=compare0,host=3.3.3.3,port=9001,server,nowait
        -chardev socket,id=compare0-0,host=3.3.3.3,port=9001
        -chardev socket,id=compare_out,host=3.3.3.3,port=9005,server,nowait
        -chardev socket,id=compare_out0,host=3.3.3.3,port=9005
        -object iothread,id=iothread1
        -object filter-mirror,id=m0,netdev=hn0,queue=tx,outdev=mirror0
        -object filter-redirector,netdev=hn0,id=redire0,queue=rx,indev=compare_out
        -object filter-redirector,netdev=hn0,id=redire1,queue=rx,outdev=compare0
        -object colo-compare,id=comp0,primary_in=compare0-0,secondary_in=compare1,outdev=compare_out0,iothread=iothread1
        secondary:
        -netdev tap,id=hn0,vhost=off,script=/etc/qemu-ifup,down script=/etc/qemu-ifdown
        -device e1000,netdev=hn0,mac=52:a4:00:12:78:66
        -chardev socket,id=red0,host=3.3.3.3,port=9003
        -chardev socket,id=red1,host=3.3.3.3,port=9004
        -object filter-redirector,id=f1,netdev=hn0,queue=tx,indev=red0
        -object filter-redirector,id=f2,netdev=hn0,queue=rx,outdev=red1
        Xen COLO
        primary:
        -netdev tap,id=hn0,vhost=off,script=/etc/qemu-ifup,downscript=/etc/qemu-ifdown
        -device e1000,id=e0,netdev=hn0,mac=52:a4:00:12:78:66
        -chardev socket,id=mirror0,host=3.3.3.3,port=9003,server,nowait
        -chardev socket,id=compare1,host=3.3.3.3,port=9004,server,nowait
        -chardev socket,id=compare0,host=3.3.3.3,port=9001,server,nowait
        -chardev socket,id=compare0-0,host=3.3.3.3,port=9001
        -chardev socket,id=compare_out,host=3.3.3.3,port=9005,server,nowait
        -chardev socket,id=compare_out0,host=3.3.3.3,port=9005
        -chardev socket,id=notify_way,host=3.3.3.3,port=9009,server,nowait
        -object filter-mirror,id=m0,netdev=hn0,queue=tx,outdev=mirror0
        -object filter-redirector,netdev=hn0,id=redire0,queue=rx,indev=compare_out
        -object filter-redirector,netdev=hn0,id=redire1,queue=rx,outdev=compare0
        -object iothread,id=iothread1
        -object colo-compare,id=comp0,primary_in=compare0-0,secondary_in=compare1,outdev=compare_out0,notify_dev=nofity_way,iothread=iothread1
        secondary:
        -netdev tap,id=hn0,vhost=off,script=/etc/qemu-ifup,down script=/etc/qemu-ifdown
        -device e1000,netdev=hn0,mac=52:a4:00:12:78:66
        -chardev socket,id=red0,host=3.3.3.3,port=9003
        -chardev socket,id=red1,host=3.3.3.3,port=9004
        -object filter-redirector,id=f1,netdev=hn0,queue=tx,indev=red0
        -object filter-redirector,id=f2,netdev=hn0,queue=rx,outdev=red1
</pre>
<p> If you want to know the detail of above command line, you can read the colo-compare git log.</p>
<dt><code>-object cryptodev-backend-builtin,id=</code><i>id</i><code>[,queues=</code><i>queues</i><code>]</code></dt>
<dd> Creates a cryptodev backend which executes crypto opreation from the QEMU cipher APIS. The <i>id</i> parameter is a unique ID that will be used to reference this cryptodev backend from the <code>virtio-crypto</code> device. The <i>queues</i> parameter is optional, which specify the queue number of cryptodev backend, the default of <i>queues</i> is 1. </dd>
<pre><code>
#qemu - system - x86_64[...] - object cryptodev - backend - builtin, id = cryptodev0 - device virtio - crypto - pci, id = crypto0, cryptodev = cryptodev0[...]
</code></pre>
<dt><code>-object cryptodev-vhost-user,id=</code><i>id</i><code>,chardev=</code><i>chardevid</i><code>[,queues=</code><i>queues</i><code>]</code></dt>
<dd> Creates a vhost-user cryptodev backend, backed by a chardev <i>chardevid</i>. The <i>id</i> parameter is a unique ID that will be used to reference this cryptodev backend from the <code>virtio-crypto</code> device. The chardev should be a unix domain socket backed one. The vhost-user uses a specifically defined protocol to pass vhost ioctl replacement messages to an application on the other end of the socket. The <i>queues</i> parameter is optional, which specify the queue number of cryptodev backend for multiqueue vhost-user, the default of <i>queues</i> is 1. </dd>
<p>#qemu &#8211; system &#8211; x86_64[&#8230;] &#8211; chardev socket, id = chardev0, path = / path / to / socket &#8211; object cryptodev &#8211; vhost &#8211; user, id = cryptodev0, chardev = chardev0 &#8211; device virtio &#8211; crypto &#8211; pci, id = crypto0, cryptodev = cryptodev0[&#8230;]</p>
<dt><code>-object secret,id=</code><i>id</i><code>,data=</code><i>string</i><code>,format=</code><i>raw|base64</i><code>[,keyid=</code><i>secretid</i><code>,iv=</code><i>string</i><code>]</code></dt>
<dd>
</dd><dt><code>-object secret,id=</code><i>id</i><code>,file=</code><i>filename</i><code>,format=</code><i>raw|base64</i><code>[,keyid=</code><i>secretid</i><code>,iv=</code><i>string</i><code>]</code></dt>
<dd> Defines a secret to store a password, encryption key, or some other sensitive data. The sensitive data can either be passed directly via the <i>data</i> parameter, or indirectly via the <i>file</i> parameter. Using the <i>data</i> parameter is insecure unless the sensitive data is encrypted. </dd>
<p> The sensitive data can be provided in raw format (the default), or base64. When encoded as JSON, the raw format only supports valid UTF-8 characters, so base64 is recommended for sending binary data. QEMU will convert from which ever format is provided to the format it needs internally. eg, an RBD password can be provided in raw format, even though it will be base64 encoded when passed onto the RBD sever. </p>
<p> For added protection, it is possible to encrypt the data associated with a secret using the AES-256-CBC cipher. Use of encryption is indicated by providing the <i>keyid</i> and <i>iv</i> parameters. The <i>keyid</i> parameter provides the ID of a previously defined secret that contains the AES-256 decryption key. This key should be 32-bytes long and be base64 encoded. The <i>iv</i> parameter provides the random initialization vector used for encryption of this particular secret and should be a base64 encrypted string of the 16-byte IV. </p>
<p> The simplest (insecure) usage is to provide the secret inline </p>
<pre>
        # qemu-system-x86_64 -object secret,id=sec0,data=letmein,format=raw
</pre>
<p> The simplest secure usage is to provide the secret via a file </p>
<p> # printf &#8220;letmein&#8221; &gt; mypasswd.txt # qemu-system-x86_64 -object secret,id=sec0,file=mypasswd.txt,format=raw </p>
<p> For greater security, AES-256-CBC should be used. To illustrate usage, consider the openssl command line tool which can encrypt the data. Note that when encrypting, the plaintext must be padded to the cipher block size (32 bytes) using the standard PKCS#5/6 compatible padding algorithm. </p>
<p> First a master key needs to be created in base64 encoding: </p>
<pre>
        # openssl rand -base64 32 &gt; key.b64
        # KEY=$(base64 -d key.b64 | hexdump  -v -e '/1 &quot;%02X&quot;')
</pre>
<p> Each secret to be encrypted needs to have a random initialization vector generated. These do not need to be kept secret </p>
<pre>
        # openssl rand -base64 16 &gt; iv.b64
        # IV=$(base64 -d iv.b64 | hexdump  -v -e '/1 &quot;%02X&quot;')
</pre>
<p> The secret to be defined can now be encrypted, in this case we&#8217;re telling openssl to base64 encode the result, but it could be left as raw bytes if desired. </p>
<pre>
        # SECRET=$(printf &quot;letmein&quot; |
        openssl enc -aes-256-cbc -a -K $KEY -iv $IV)
</pre>
<p> When launching QEMU, create a master secret pointing to <tt>&quot;key.b64&quot;</tt> and specify that to be used to decrypt the user password. Pass the contents of <tt>&quot;iv.b64&quot;</tt> to the second secret </p>
<pre>
        # qemu-system-x86_64 \
        -object secret,id=secmaster0,format=base64,file=key.b64 \
        -object secret,id=sec0,keyid=secmaster0,format=base64,\
        data=$SECRET,iv=$(&lt;iv.b64)
</pre>
<dt><code>-object sev-guest,id=</code><i>id</i><code>,cbitpos=</code><i>cbitpos</i><code>,reduced-phys-bits=</code><i>val</i><code>,[sev-device=</code><i>string</i><code>,policy=</code><i>policy</i><code>,handle=</code><i>handle</i><code>,dh-cert-file=</code><i>file</i><code>,session-file=</code><i>file</i><code>]</code></dt>
<dd> Create a Secure Encrypted Virtualization (SEV) guest object, which can be used to provide the guest memory encryption support on AMD processors. </dd>
<p> When memory encryption is enabled, one of the physical address bit (aka the C-bit) is utilized to mark if a memory page is protected. The <code>cbitpos</code> is used to provide the C-bit position. The C-bit position is Host family dependent hence user must provide this value. On EPYC, the value should be 47. </p>
<p> When memory encryption is enabled, we loose certain bits in physical address space. The <code>reduced-phys-bits</code> is used to provide the number of bits we loose in physical address space. Similar to C-bit, the value is Host family dependent. On EPYC, the value should be 5. </p>
<p> The <code>sev-device</code> provides the device file to use for communicating with the SEV firmware running inside AMD Secure Processor. The default device is &#8216;/dev/sev&#8217;. If hardware supports memory encryption then /dev/sev devices are created by CCP driver. </p>
<p> The <code>policy</code> provides the guest policy to be enforced by the SEV firmware and restrict what configuration and operational commands can be performed on this guest by the hypervisor. The policy should be provided by the guest owner and is bound to the guest and cannot be changed throughout the lifetime of the guest. The default is 0. </p>
<p> If guest <code>policy</code> allows sharing the key with another SEV guest then <code>handle</code> can be use to provide handle of the guest from which to share the key. </p>
<p> The <code>dh-cert-file</code> and <code>session-file</code> provides the guest owner&#8217;s Public Diffie-Hillman key defined in SEV spec. The PDH and session parameters are used for establishing a cryptographic session with the guest owner to negotiate keys used for attestation. The file must be encoded in base64. </p>
<p> e.g to launch a SEV guest </p>
<pre>
        # qemu-system-x86_64 \
        ......
        -object sev-guest,id=sev0,cbitpos=47,reduced-phys-bits=5 \
        -machine ...,memory-encryption=sev0
        .....
</pre>
<dt><code>-object authz-simple,id=</code><i>id</i><code>,identity=</code><i>string</i></dt>
<dd> Create an authorization object that will control access to network services. </dd>
<p> The <code>identity</code> parameter is identifies the user and its format depends on the network service that authorization object is associated with. For authorizing based on TLS x509 certificates, the identity must be the x509 distinguished name. Note that care must be taken to escape any commas in the distinguished name. </p>
<p> An example authorization object to validate a x509 distinguished name would look like: </p>
<pre>
        # qemu-system-x86_64 \
        ...
        -object 'authz-simple,id=auth0,identity=CN=laptop.example.com,,O=Example Org,,L=London,,ST=London,,C=GB' \
        ...
</pre>
<p> Note the use of quotes due to the x509 distinguished name containing whitespace, and escaping of &#8216;,&#8217;.</p>
<dt><code>-object authz-listfile,id=</code><i>id</i><code>,filename=</code><i>path</i><code>,refresh=</code><i>yes|no</i></dt>
<dd> Create an authorization object that will control access to network services. </dd>
<p> The <code>filename</code> parameter is the fully qualified path to a file containing the access control list rules in JSON format. </p>
<p> An example set of rules that match against SASL usernames might look like: </p>
<p>{<br/>
    &#8220;rules&#8221; : [<br/>
        {&#8220;match&#8221; : &#8220;fred&#8221;, &#8220;policy&#8221; : &#8220;allow&#8221;, &#8220;format&#8221; : &#8220;exact&#8221;},<br/>
        {&#8220;match&#8221; : &#8220;bob&#8221;, &#8220;policy&#8221; : &#8220;allow&#8221;, &#8220;format&#8221; : &#8220;exact&#8221;},<br/>
        {&#8220;match&#8221; : &#8220;danb&#8221;, &#8220;policy&#8221; : &#8220;deny&#8221;, &#8220;format&#8221; : &#8220;glob&#8221;},<br/>
        {&#8220;match&#8221; : &#8220;dan*&#8221;, &#8220;policy&#8221; : &#8220;allow&#8221;, &#8220;format&#8221; : &#8220;exact&#8221;},<br/>
    ],<br/>
              &#8220;policy&#8221; : &#8220;deny&#8221;<br/>
}</p>
<p> When checking access the object will iterate over all the rules and the first rule to match will have its <code>policy</code> value returned as the result. If no rules match, then the default <code>policy</code> value is returned. </p>
<p> The rules can either be an exact string match, or they can use the simple UNIX glob pattern matching to allow wildcards to be used. </p>
<p> If <code>refresh</code> is set to true the file will be monitored and automatically reloaded whenever its content changes. </p>
<p> As with the <tt>&quot;authz-simple&quot;</tt> object, the format of the identity strings being matched depends on the network service, but is usually a TLS x509 distinguished name, or a SASL username. </p>
<p> An example authorization object to validate a SASL username would look like: </p>
<pre>
        # qemu-system-x86_64 \
        ...
        -object authz-simple,id=auth0,filename=/etc/qemu/vnc-sasl.acl,refresh=yes
        ...
</pre>
<dt><code>-object authz-pam,id=</code><i>id</i><code>,service=</code><i>string</i></dt>
<dd> Create an authorization object that will control access to network services. </dd>
<p> The <code>service</code> parameter provides the name of a PAM service to use for authorization. It requires that a file <tt>&quot;/etc/pam.d/</tt>service<tt>&quot;</tt> exist to provide the configuration for the <tt>&quot;account&quot;</tt> subsystem. </p>
<p> An example authorization object to validate a TLS x509 distinguished name would look like: </p>
<pre>
        # qemu-system-x86_64 \
        ...
        -object authz-pam,id=auth0,service=qemu-vnc
        ...
</pre>
<p> There would then be a corresponding config file for PAM at <tt>&quot;/etc/pam.d/qemu-vnc&quot;</tt> that contains: </p>
<pre>
        account requisite  pam_listfile.so item=user sense=allow \
        file=/etc/qemu/vnc.allow
</pre>
<p> Finally the <tt>&quot;/etc/qemu/vnc.allow&quot;</tt> file would contain the list of x509 distingished names that are permitted access </p>
<pre>
        CN=laptop.example.com,O=Example Home,L=London,ST=London,C=GB
</pre>
</dl>
</dl>
<dl>
</dl>
</dl>
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
<p> During emulation, if you are using a character backend multiplexer (which is the default if you are using <code>-nographic</code>) then several commands are available via an escape sequence. These key sequences all start with an escape character, which is <code>Ctrl-a</code> by default, but can be changed with <code>-echr</code>. The list below assumes you&#8217;re using the default.</p>
<dl>
<dt><code>Ctrl-a h</code></dt>
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
<dd> Rotate between the frontends connected to the multiplexer (usually this switches between the monitor and the console)</dd>
<dt><code>Ctrl-a Ctrl-a</code></dt>
<dd> Send the escape character to the frontend</dd></dl>
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
<dt><code>-M [sun4u|sun4v|niagara]</code></dt>
<dd> Set the emulated machine type. The default is sun4u.</dd></dl>
<p> The following options are specific to the ARM emulation:</p>
<dl>
<dt><code>-semihosting</code></dt>
<dd> Enable semihosting syscall emulation. </dd>
<p> On ARM this implements the &#8220;Angel&#8221; interface. </p>
<p> Note that this allows guest direct access to the host filesystem, so should only be used with trusted guest OS.</dl>
<p> The following options are specific to the ColdFire emulation:</p>
<dl>
<dt><code>-semihosting</code></dt>
<dd> Enable semihosting syscall emulation. </dd>
<p> On M68K this implements the &#8220;ColdFire GDB&#8221; interface used by libgloss. </p>
<p> Note that this allows guest direct access to the host filesystem, so should only be used with trusted guest OS.</dl>
<p> The following options are specific to the Xtensa emulation:</p>
<dl>
<dt><code>-semihosting</code></dt>
<dd> Enable semihosting syscall emulation. </dd>
<p> Xtensa semihosting provides basic file IO calls, such as open/read/write/seek/select. Tensilica baremetal libc for ISS and linux platform &#8220;sim&#8221; use this interface. </p>
<p> Note that this allows guest direct access to the host filesystem, so should only be used with trusted guest OS.</dl>
<h2>NOTES</h2>
<p> In addition to using normal file images for the emulated storage devices, QEMU can also use networked resources such as iSCSI devices. These are specified using a special URL syntax.</p>
<dl>
<dt><code>iSCSI</code></dt>
<dd> iSCSI support allows QEMU to access iSCSI resources directly and use as images for the guest storage. Both disk and cdrom images are supported. </dd>
<p> Syntax for specifying iSCSI LUNs is &#8220;iscsi://&lt;target-ip&gt;[:&lt;port&gt;]/&lt;target-iqn&gt;/&lt;lun&gt;&#8221; </p>
<p> By default qemu will use the iSCSI initiator-name &#8216;iqn.2008-11.org.linux-kvm[:&lt;name&gt;]&#8217; but this can also be set from the command line or a configuration file. </p>
<p> Since version Qemu 2.4 it is possible to specify a iSCSI request timeout to detect stalled requests and force a reestablishment of the session. The timeout is specified in seconds. The default is 0 which means no timeout. Libiscsi 1.15.0 or greater is required for this feature. </p>
<p> Example (without authentication): </p>
<pre>
        qemu-system-x86_64 -iscsi initiator-name=iqn.2001-04.com.example:my-initiator \
                         -cdrom <a href="iscsi://192.0.2.1/iqn.2001-04.com.example/2">iscsi://192.0.2.1/iqn.2001-04.com.example/2</a> \
                         -drive file=<a href="iscsi://192.0.2.1/iqn.2001-04.com.example/1">iscsi://192.0.2.1/iqn.2001-04.com.example/1</a>
</pre>
<p> Example (CHAP username/password via URL): </p>
<pre>
        qemu-system-x86_64 -drive file=<a href="iscsi://user%password@192.0.2.1/iqn.2001-04.com.example/1">iscsi://user%password@192.0.2.1/iqn.2001-04.com.example/1</a>
</pre>
<p> Example (CHAP username/password via environment variables): </p>
<pre>
        LIBISCSI_CHAP_USERNAME=&quot;user&quot; \
        LIBISCSI_CHAP_PASSWORD=&quot;password&quot; \
        qemu-system-x86_64 -drive file=<a href="iscsi://192.0.2.1/iqn.2001-04.com.example/1">iscsi://192.0.2.1/iqn.2001-04.com.example/1</a>
</pre>
<dt><code>NBD</code></dt>
<dd> QEMU supports NBD (Network Block Devices) both using TCP protocol as well as Unix Domain Sockets. With TCP, the default port is 10809. </dd>
<p> Syntax for specifying a NBD device using TCP, in preferred URI form: &#8220;nbd://&lt;server-ip&gt;[:&lt;port&gt;]/[&lt;export&gt;]&#8221; </p>
<p> Syntax for specifying a NBD device using Unix Domain Sockets; remember that &#8216;?&#8217; is a shell glob character and may need quoting: &#8220;nbd+<a href="unix:///[">unix:///[</a>&lt;export&gt;]?socket=&lt;domain-socket&gt;&#8221; </p>
<p> Older syntax that is also recognized: &#8220;nbd:&lt;server-ip&gt;:&lt;port&gt;[:exportname=&lt;export&gt;]&#8221; </p>
<p> Syntax for specifying a NBD device using Unix Domain Sockets &#8220;nbd:unix:&lt;domain-socket&gt;[:exportname=&lt;export&gt;]&#8221; </p>
<p> Example for TCP </p>
<pre>
        qemu-system-x86_64 --drive file=nbd:192.0.2.1:30000
</pre>
<p> Example for Unix Domain Sockets </p>
<pre>
        qemu-system-x86_64 --drive file=nbd:unix:/tmp/nbd-socket
</pre>
<dt><code>SSH</code></dt>
<dd> QEMU supports SSH (Secure Shell) access to remote disks. </dd>
<p> Examples: </p>
<pre>
        qemu-system-x86_64 -drive file=<a href="ssh://user@host/path/to/disk.img">ssh://user@host/path/to/disk.img</a>
        qemu-system-x86_64 -drive file.driver=ssh,file.user=user,file.host=host,file.port=22,file.path=/path/to/disk.img
</pre>
<p> Currently authentication must be done using ssh-agent. Other authentication methods may be supported in future.</p>
<dt><code>Sheepdog</code></dt>
<dd> Sheepdog is a distributed storage system for QEMU. QEMU supports using either local sheepdog devices or remote networked devices. </dd>
<p> Syntax for specifying a sheepdog device </p>
<p>sheepdog[+tcp | +unix]: //[host:port]/vdiname[?socket=path][#snapid|#tag]</p>
<p> Example </p>
<pre>
        qemu-system-x86_64 --drive file=sheepdog://192.0.2.1:30000/MyVirtualMachine
</pre>
<p> See also &lt;<code><a rel="nofollow" href="https://sheepdog.github.io/sheepdog/">https://sheepdog.github.io/sheepdog/</a></code>&gt;.</p>
<dt><code>GlusterFS</code></dt>
<dd> GlusterFS is a user space distributed file system. QEMU supports the use of GlusterFS volumes for hosting VM disk images using TCP, Unix Domain Sockets and RDMA transport protocols. </dd>
<p> Syntax for specifying a VM disk image on GlusterFS volume is </p>
<p>URI : gluster[+type] : //[host[:port]]/volume/path[?socket=&#8230;][,debug=N][,logfile=&#8230;]</p>
<p>                       JSON :<br/>
        &#8216;json:{&#8220;driver&#8221;:&#8221;qcow2&#8243;,&#8221;file&#8221;:{&#8220;driver&#8221;:&#8221;gluster&#8221;,&#8221;volume&#8221;:&#8221;testvol&#8221;,&#8221;path&#8221;:&#8221;a.img&#8221;,&#8221;debug&#8221;:N,&#8221;logfile&#8221;:&#8221;&#8230;&#8221;, &#8220;server&#8221; : [ {&#8220;type&#8221; : &#8220;tcp&#8221;, &#8220;host&#8221; : &#8220;&#8230;&#8221;, &#8220;port&#8221; : &#8220;&#8230;&#8221;},<br/>
                                                                                                                                      {&#8220;type&#8221; : &#8220;unix&#8221;, &#8220;socket&#8221; : &#8220;&#8230;&#8221;} ]<br/>
}<br/>
}<br/>
&#8216;</p>
<p> Example </p>
<p>URI : qemu &#8211; system &#8211; x86_64&#8211; drive file = gluster : // 192.0.2.1/testvol/a.img,<br/>
                                                      file.debug = 9,<br/>
                                     file.logfile = / var / log / qemu &#8211; gluster.log</p>
<p>                                                                             JSON : qemu &#8211;<br/>
                                                    system &#8211; x86_64 &#8216;json:{&#8220;driver&#8221;:&#8221;qcow2&#8243;, &#8220;file&#8221;:<br/>
{<br/>
    &#8220;driver&#8221; : &#8220;gluster&#8221;,<br/>
               &#8220;volume&#8221; : &#8220;testvol&#8221;,<br/>
                          &#8220;path&#8221; : &#8220;a.img&#8221;,<br/>
                                   &#8220;debug&#8221; : 9,<br/>
                                   &#8220;logfile&#8221; : &#8220;/var/log/qemu-gluster.log&#8221;,<br/>
                                               &#8220;server&#8221; : [ {&#8220;type&#8221; : &#8220;tcp&#8221;, &#8220;host&#8221; : &#8220;1.2.3.4&#8221;, &#8220;port&#8221; : 24007},<br/>
                                                            {&#8220;type&#8221; : &#8220;unix&#8221;, &#8220;socket&#8221; : &#8220;/var/run/glusterd.socket&#8221;} ]<br/>
}<br/>
}<br/>
&#8216; qemu &#8211; system &#8211; x86_64 &#8211; drive driver = qcow2, file.driver = gluster, file.volume = testvol, file.path = / path / a.img,<br/>
                                 file.debug = 9, file.logfile = / var / log / qemu &#8211; gluster.log,<br/>
                                 file.server .0.type = tcp, file.server .0.host = 1.2.3.4, file.server .0.port = 24007,<br/>
                                 file.server .1.type = unix, file.server .1.socket = / var / run / glusterd.socket</p>
<p> See also &lt;<code><a rel="nofollow" href="http://www.gluster.org">http://www.gluster.org</a></code>&gt;.</p>
<dt><code>HTTP/HTTPS/FTP/FTPS</code></dt>
<dd> QEMU supports read-only access to files accessed over http(s) and ftp(s). </dd>
<p> Syntax using a single filename: </p>
<pre><code>
        &lt;protocol&gt;://[&lt;username&gt;[:&lt;password&gt;]@]&lt;host&gt;/&lt;path&gt;
</code></pre>
<p> where:</p>
<dl>
<dl>
<dt><code>protocol</code></dt>
<dd> &#8216;http&#8217;, &#8216;https&#8217;, &#8216;ftp&#8217;, or &#8216;ftps&#8217;.</dd>
<dt><code>username</code></dt>
<dd> Optional username for authentication to the remote server.</dd>
<dt><code>password</code></dt>
<dd> Optional password for authentication to the remote server.</dd>
<dt><code>host</code></dt>
<dd> Address of the remote server.</dd>
<dt><code>path</code></dt>
<dd> Path on the remote server, including any query string.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> The following options are also supported:</p>
</dd><dl>
<dt><code>url</code></dt>
<dd> The full URL when passing options to the driver explicitly.</dd>
<dt><code>readahead</code></dt>
<dd> The amount of data to read ahead with each range request to the remote server. This value may optionally have the suffix &#8216;T&#8217;, &#8216;G&#8217;, &#8216;M&#8217;, &#8216;K&#8217;, &#8216;k&#8217; or &#8216;b&#8217;. If it does not have a suffix, it will be assumed to be in bytes. The value must be a multiple of 512 bytes. It defaults to 256k.</dd>
<dt><code>sslverify</code></dt>
<dd> Whether to verify the remote server&#8217;s certificate when connecting over SSL. It can have the value &#8216;on&#8217; or &#8216;off&#8217;. It defaults to &#8216;on&#8217;.</dd>
<dt><code>cookie</code></dt>
<dd> Send this cookie (it can also be a list of cookies separated by &#8216;;&#8217;) with each outgoing request. Only supported when using protocols such as HTTP which support cookies, otherwise ignored.</dd>
<dt><code>timeout</code></dt>
<dd> Set the timeout in seconds of the CURL connection. This timeout is the time that CURL waits for a response from the remote server to get the size of the image to be downloaded. If not set, the default timeout of 5 seconds is used.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> Note that when passing options to qemu explicitly, <code>driver</code> is the value of &lt;protocol&gt;. </p>
<p> Example: boot from a remote Fedora 20 live ISO image </p>
<pre>
        qemu-system-x86_64 --drive media=cdrom,file=<a rel="nofollow" href="https://archives.fedoraproject.org/pub/archive/fedora/linux/releases/20/Live/x86_64/Fedora-Live-Desktop-x86_64-20-1.iso,readonly">https://archives.fedoraproject.org/pub/archive/fedora/linux/releases/20/Live/x86_64/Fedora-Live-Desktop-x86_64-20-1.iso,readonly</a>
        qemu-system-x86_64 --drive media=cdrom,file.driver=http,file.url=<a rel="nofollow" href="http://archives.fedoraproject.org/pub/fedora/linux/releases/20/Live/x86_64/Fedora-Live-Desktop-x86_64-20-1.iso,readonly">http://archives.fedoraproject.org/pub/fedora/linux/releases/20/Live/x86_64/Fedora-Live-Desktop-x86_64-20-1.iso,readonly</a>
</pre>
<p> Example: boot from a remote Fedora 20 cloud image using a local overlay for writes, copy-on-read, and a readahead of 64k </p>
<pre>
        qemu-img create -f qcow2 -o backing_file='json:{&quot;file.driver&quot;:&quot;http&quot;,, &quot;file.url&quot;:&quot;<a rel="nofollow" href="http://archives.fedoraproject.org/pub/archive/fedora/linux/releases/20/Images/x86_64/Fedora-x86_64-20-20131211.1-sda.qcow2">http://archives.fedoraproject.org/pub/archive/fedora/linux/releases/20/Images/x86_64/Fedora-x86_64-20-20131211.1-sda.qcow2</a>&quot;,, &quot;file.readahead&quot;:&quot;64k&quot;}' /tmp/Fedora-x86_64-20-20131211.1-sda.qcow2
        qemu-system-x86_64 -drive file=/tmp/Fedora-x86_64-20-20131211.1-sda.qcow2,copy-on-read=on
</pre>
<p> Example: boot from an image stored on a VMware vSphere server with a self-signed certificate using a local overlay for writes, a readahead of 64k and a timeout of 10 seconds. </p>
<pre>
        qemu-img create -f qcow2 -o backing_file='json:{&quot;file.driver&quot;:&quot;https&quot;,, &quot;file.url&quot;:&quot;<a rel="nofollow" href="https://user:password@vsphere.example.com/folder/test/test-flat.vmdk?dcPath=Datacenter">https://user:password@vsphere.example.com/folder/test/test-flat.vmdk?dcPath=Datacenter</a>&amp;dsName=datastore1&quot;,, &quot;file.sslverify&quot;:&quot;off&quot;,, &quot;file.readahead&quot;:&quot;64k&quot;,, &quot;file.timeout&quot;:10}' /tmp/test.qcow2
        qemu-system-x86_64 -drive file=/tmp/test.qcow2
</pre>
</dd></dl>
</dl>
<h2>SEE ALSO</h2>
<p> The HTML documentation of QEMU for more precise information and Linux user mode emulator invocation.</p>
<h2>AUTHOR</h2>
<p> Fabrice Bellard </p>
