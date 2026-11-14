---
title: "qemu-system-x86_64(1)"
name: "qemu-system-x86_64"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qemu-system-x86_64/"
description: "qemu-doc – QEMU version 4.2.0 User Documentation"
---

<h2 class="name">NAME</h2>
<p> qemu-doc &#8211; QEMU version 4.2.0 User Documentation </p>
<h2>SYNOPSIS</h2>
<p> <code>qemu-system-x86_64</code> [<i>options</i>] [<i>disk_image</i>]</p>
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
<dd> <font SIZE="-1">IPMI BMC,</font> either and internal or external one</p>
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
<dd> <font SIZE="-1">PCI UHCI, OHCI, EHCI</font> or <font SIZE="-1">XHCI USB</font> controller and a virtual <font SIZE="-1">USB-1.1</font> hub.</dl>
<p> <font SIZE="-1">SMP</font> is supported with up to 255 CPUs. </p>
<p> <font SIZE="-1">QEMU</font> uses the <font SIZE="-1">PC BIOS</font> from the Seabios project and the Plex86/Bochs <font SIZE="-1">LGPL VGA BIOS.</font> </p>
<p> <font SIZE="-1">QEMU</font> uses <font SIZE="-1">YM3812</font> emulation by Tatsuyuki Satoh. </p>
<p> <font SIZE="-1">QEMU</font> uses <font SIZE="-1">GUS</font> emulation (<font SIZE="-1">GUSEMU32</font> &lt;<code><a rel="nofollow" href="http://www.deinmeister.de/gusemu/">http://www.deinmeister.de/gusemu/</a></code>&gt;) by Tibor &#8220;<font SIZE="-1">TS&#8221;</font> Schütz. </p>
<p> Note that, by default, <font SIZE="-1">GUS</font> shares <font SIZE="-1"><code><a href="/docs/linux/man/7-irq/">IRQ</a></code></font>(7) with parallel ports and so <font SIZE="-1">QEMU</font> must be told to not have parallel ports to have working <font SIZE="-1">GUS.</font> </p>
<pre>
        qemu-system-x86_64 dos.img -soundhw gus -parallel none
</pre>
<p> Alternatively: </p>
<pre>
        qemu-system-x86_64 dos.img -device gus,irq=5
</pre>
<p> Or some other unclaimed <font SIZE="-1">IRQ.</font> </p>
<p> <font SIZE="-1">CS4231A</font> is the chip used in Windows Sound System and <font SIZE="-1">GUSMAX</font> products</p>
<h2>OPTIONS</h2>
<p> <i>disk_image</i> is a raw hard disk image for <font SIZE="-1">IDE</font> hard disk 0. Some targets do not need a disk image. </p>
<p> <i>Standard options</i></p>
<dl>
<dt><code>-h</code></p>
<dd> Display help and exit</p>
<dt><code>-version</code></p>
<dd> Display version information and exit</p>
<dt><code>-machine [type=]</code><i>name</i><code>[,prop=</code><i>value</i><code>[,&#8230;]]</code></p>
<dd> Select the emulated machine by <i>name</i>. Use <tt>&quot;-machine help&quot;</tt> to list available machines. </p>
<p> For architectures which aim to support live migration compatibility across releases, each release will introduce a new versioned machine type. For example, the 2.8.0 release introduced machine types &#8220;pc-i440fx-2.8&#8221; and &#8220;pc-q35-2.8&#8221; for the x86_64/i686 architectures. </p>
<p> To allow live migration of guests from <font SIZE="-1">QEMU</font> version 2.8.0, to <font SIZE="-1">QEMU</font> version 2.9.0, the 2.9.0 version must support the &#8220;pc-i440fx-2.8&#8221; and &#8220;pc-q35-2.8&#8221; machines too. To allow users live migrating VMs to skip multiple intermediate releases when upgrading, new releases of <font SIZE="-1">QEMU</font> will support machine types from many previous versions. </p>
<p> Supported machine properties are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>accel=</code><i>accels1</i><code>[:</code><i>accels2</i><code>[:&#8230;]]</code></p>
<dd> This is used to enable an accelerator. Depending on the target architecture, kvm, xen, hax, hvf, whpx or tcg can be available. By default, tcg is used. If there is more than one accelerator specified, the next one is used if the previous one fails to initialize.</p>
<dt><code>kernel_irqchip=on|off</code></p>
<dd> Controls in-kernel irqchip support for the chosen accelerator when available.</p>
<dt><code>gfx_passthru=on|off</code></p>
<dd> Enables <font SIZE="-1">IGD GFX</font> passthrough support for the chosen machine when available.</p>
<dt><code>vmport=on|off|auto</code></p>
<dd> Enables emulation of VMWare <font SIZE="-1">IO</font> port, for vmmouse etc. auto says to select the value based on accel. For accel=xen the default is off otherwise the default is on.</p>
<dt><code>kvm_shadow_mem=size</code></p>
<dd> Defines the size of the <font SIZE="-1">KVM</font> shadow <font SIZE="-1">MMU.</font></p>
<dt><code>dump-guest-core=on|off</code></p>
<dd> Include guest memory in a core dump. The default is on.</p>
<dt><code>mem-merge=on|off</code></p>
<dd> Enables or disables memory merge support. This feature, when supported by the host, de-duplicates identical memory pages among VMs instances (enabled by default).</p>
<dt><code>aes-key-wrap=on|off</code></p>
<dd> Enables or disables <font SIZE="-1">AES</font> key wrapping support on s390-ccw hosts. This feature controls whether <font SIZE="-1">AES</font> wrapping keys will be created to allow execution of <font SIZE="-1">AES</font> cryptographic functions. The default is on.</p>
<dt><code>dea-key-wrap=on|off</code></p>
<dd> Enables or disables <font SIZE="-1">DEA</font> key wrapping support on s390-ccw hosts. This feature controls whether <font SIZE="-1">DEA</font> wrapping keys will be created to allow execution of <font SIZE="-1">DEA</font> cryptographic functions. The default is on.</p>
<dt><code>nvdimm=on|off</code></p>
<dd> Enables or disables <font SIZE="-1">NVDIMM</font> support. The default is off.</p>
<dt><code>enforce-config-section=on|off</code></p>
<dd> If <code>enforce-config-section</code> is set to <i>on</i>, force migration code to send configuration section even if the machine-type sets the <code>migration.send-configuration</code> property to <i>off</i>. <font SIZE="-1">NOTE:</font> this parameter is deprecated. Please use <code>-global</code> <code>migration.send-configuration</code>=<i>on|off</i> instead.</p>
<dt><code>memory-encryption=</code></p>
<dd> Memory encryption object to use. The default is none.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-cpu</code> <i>model</i></p>
<dd> Select <font SIZE="-1">CPU</font> model (<tt>&quot;-cpu help&quot;</tt> for list and additional feature selection)</p>
<dt><code>-accel</code> <i>name</i><code>[,prop=</code><i>value</i><code>[,&#8230;]]</code></p>
<dd> This is used to enable an accelerator. Depending on the target architecture, kvm, xen, hax, hvf, whpx or tcg can be available. By default, tcg is used. If there is more than one accelerator specified, the next one is used if the previous one fails to initialize.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>thread=single|multi</code></p>
<dd> Controls number of <font SIZE="-1">TCG</font> threads. When the <font SIZE="-1">TCG</font> is multi-threaded there will be one thread per vCPU therefor taking advantage of additional host cores. The default is to enable multi-threading where both the back-end and front-ends support it and no incompatible <font SIZE="-1">TCG</font> features have been enabled (e.g. icount/replay).</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-smp [cpus=]</code><i>n</i><code>[,cores=</code><i>cores</i><code>][,threads=</code><i>threads</i><code>][,dies=dies][,sockets=</code><i>sockets</i><code>][,maxcpus=</code><i>maxcpus</i><code>]</code></p>
<dd> Simulate an <font SIZE="-1">SMP</font> system with <i>n</i> CPUs. On the <font SIZE="-1">PC</font> target, up to 255 CPUs are supported. On Sparc32 target, Linux limits the number of usable CPUs to 4. For the <font SIZE="-1">PC</font> target, the number of <i>cores</i> per die, the number of <i>threads</i> per cores, the number of <i>dies</i> per packages and the total number of <i>sockets</i> can be specified. Missing values will be computed. If any on the three values is given, the total number of CPUs <i>n</i> can be omitted. <i>maxcpus</i> specifies the maximum number of hotpluggable CPUs.</p>
<dt><code>-numa node[,mem=</code><i>size</i><code>][,cpus=</code><i>firstcpu</i><code>[-</code><i>lastcpu</i><code>]][,nodeid=</code><i>node</i><code>]</code></p>
<dd>
<dt><code>-numa node[,memdev=</code><i>id</i><code>][,cpus=</code><i>firstcpu</i><code>[-</code><i>lastcpu</i><code>]][,nodeid=</code><i>node</i><code>]</code></p>
<dd>
<dt><code>-numa dist,src=</code><i>source</i><code>,dst=</code><i>destination</i><code>,val=</code><i>distance</i></p>
<dd>
<dt><code>-numa cpu,node-id=</code><i>node</i><code>[,socket-id=</code><i>x</i><code>][,core-id=</code><i>y</i><code>][,thread-id=</code><i>z</i><code>]</code></p>
<dd> Define a <font SIZE="-1">NUMA</font> node and assign <font SIZE="-1">RAM</font> and VCPUs to it. Set the <font SIZE="-1">NUMA</font> distance from a source node to a destination node. </p>
<p> Legacy <font SIZE="-1">VCPU</font> assignment uses <code>cpus</code> option where <i>firstcpu</i> and <i>lastcpu</i> are <font SIZE="-1">CPU</font> indexes. Each <code>cpus</code> option represent a contiguous range of <font SIZE="-1">CPU</font> indexes (or a single <font SIZE="-1">VCPU</font> if <i>lastcpu</i> is omitted). A non-contiguous set of VCPUs can be represented by providing multiple <code>cpus</code> options. If <code>cpus</code> is omitted on all nodes, VCPUs are automatically split between them. </p>
<p> For example, the following option assigns VCPUs 0, 1, 2 and 5 to a <font SIZE="-1">NUMA</font> node: </p>
<pre>
        -numa node,cpus=0-2,cpus=5
</pre>
<p> <code>cpu</code> option is a new alternative to <code>cpus</code> option which uses <code>socket-id|core-id|thread-id</code> properties to assign <font SIZE="-1">CPU</font> objects to a <i>node</i> using topology layout properties of <font SIZE="-1">CPU.</font> The set of properties is machine specific, and depends on used machine type/<code>smp</code> options. It could be queried with <code>hotpluggable-cpus</code> monitor command. <code>node-id</code> property specifies <i>node</i> to which <font SIZE="-1">CPU</font> object will be assigned, it&#8217;s required for <i>node</i> to be declared with <code>node</code> option before it&#8217;s used with <code>cpu</code> option. </p>
<p> For example: </p>
<pre>
        -M pc \
        -smp 1,sockets=2,maxcpus=2 \
        -numa node,nodeid=0 -numa node,nodeid=1 \
        -numa cpu,node-id=0,socket-id=0 -numa cpu,node-id=1,socket-id=1
</pre>
<p> <code>mem</code> assigns a given <font SIZE="-1">RAM</font> amount to a node. <code>memdev</code> assigns <font SIZE="-1">RAM</font> from a given memory backend device to a node. If <code>mem</code> and <code>memdev</code> are omitted in all nodes, <font SIZE="-1">RAM</font> is split equally between them. </p>
<p> <code>mem</code> and <code>memdev</code> are mutually exclusive. Furthermore, if one node uses <code>memdev</code>, all of them have to use it. </p>
<p> <i>source</i> and <i>destination</i> are <font SIZE="-1">NUMA</font> node IDs. <i>distance</i> is the <font SIZE="-1">NUMA</font> distance from <i>source</i> to <i>destination</i>. The distance from a node to itself is always 10. If any pair of nodes is given a distance, then all pairs must be given distances. Although, when distances are only given in one direction for each pair of nodes, then the distances in the opposite directions are assumed to be the same. If, however, an asymmetrical pair of distances is given for even one node pair, then all node pairs must be provided distance values for both directions, even when they are symmetrical. When a node is unreachable from another node, set the pair&#8217;s distance to 255. </p>
<p> Note that the &#8211;<code>numa</code> option doesn&#8217;t allocate any of the specified resources, it just assigns existing resources to <font SIZE="-1">NUMA</font> nodes. This means that one still has to use the <code>-m</code>, <code>-smp</code> options to allocate <font SIZE="-1">RAM</font> and VCPUs respectively.</p>
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
        qemu-system-x86_64 \
        -add-fd fd=3,set=2,opaque=&quot;rdwr:/path/to/file&quot; \
        -add-fd fd=4,set=2,opaque=&quot;rdonly:/path/to/file&quot; \
        -drive file=/dev/fdset/2,index=0,media=disk
</pre>
</dl>
<dt><code>-set</code> <i>group</i><code>.</code><i>id</i><code>.</code><i>arg</i><code>=</code><i>value</i></p>
<dd> Set parameter <i>arg</i> for item <i>id</i> of type <i>group</i></p>
<dt><code>-global</code> <i>driver</i><code>.</code><i>prop</i><code>=</code><i>value</i></p>
<dd>
<dt><code>-global driver=</code><i>driver</i><code>,property=</code><i>property</i><code>,value=</code><i>value</i></p>
<dd> Set default value of <i>driver</i>&#8216;s property <i>prop</i> to <i>value</i>, e.g.: </p>
<pre>
        qemu-system-x86_64 -global ide-hd.physical_block_size=4096 disk-image.img
</pre>
<p> In particular, you can use this to set driver properties for devices which are created automatically by the machine model. To create a device which is not created automatically and set properties on it, use &#8211;<code>device</code>. </p>
<p> -global <i>driver</i>.<i>prop</i>=<i>value</i> is shorthand for -global driver=<i>driver</i>,property=<i>prop</i>,value=<i>value</i>. The longhand syntax works even when <i>driver</i> contains a dot.</p>
<dt><code>-boot [order=</code><i>drives</i><code>][,once=</code><i>drives</i><code>][,menu=on|off][,splash=</code><i>sp_name</i><code>][,splash-time=</code><i>sp_time</i><code>][,reboot-timeout=</code><i>rb_timeout</i><code>][,strict=on|off]</code></p>
<dd> Specify boot order <i>drives</i> as a string of drive letters. Valid drive letters depend on the target architecture. The x86 <font SIZE="-1">PC</font> uses: a, b (floppy 1 and 2), c (first hard disk), d (first CD-ROM), n-p (Etherboot from network adapter 1-4), hard disk boot is the default. To apply a particular boot order only on the first startup, specify it via <code>once</code>. Note that the <code>order</code> or <code>once</code> parameter should not be used together with the <code>bootindex</code> property of devices, since the firmware implementations normally do not support both at the same time. </p>
<p> Interactive boot menus/prompts can be enabled via <code>menu=on</code> as far as firmware/BIOS supports them. The default is non-interactive boot. </p>
<p> A splash picture could be passed to bios, enabling user to show it as logo, when option splash=<i>sp_name</i> is given and menu=on, If firmware/BIOS supports them. Currently Seabios for X86 system support it. limitation: The splash file could be a jpeg file or a <font SIZE="-1">BMP</font> file in 24 <font SIZE="-1">BPP</font> format(true color). The resolution should be supported by the <font SIZE="-1">SVGA</font> mode, so the recommended is 320&#215;240, 640&#215;480, 800&#215;640. </p>
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
<dt><code>-m [size=]</code><i>megs</i><code>[,slots=n,maxmem=size]</code></p>
<dd> Sets guest startup <font SIZE="-1">RAM</font> size to <i>megs</i> megabytes. Default is 128 MiB. Optionally, a suffix of &#8220;M&#8221; or &#8220;G&#8221; can be used to signify a value in megabytes or gigabytes respectively. Optional pair <i>slots</i>, <i>maxmem</i> could be used to set amount of hotpluggable memory slots and maximum amount of memory. Note that <i>maxmem</i> must be aligned to the page size. </p>
<p> For example, the following command-line sets the guest startup <font SIZE="-1">RAM</font> size to 1GB, creates 3 slots to hotplug additional memory and sets the maximum memory the guest can reach to 4GB: </p>
<pre>
        qemu-system-x86_64 -m 1G,slots=3,maxmem=4G
</pre>
<p> If <i>slots</i> and <i>maxmem</i> are not specified, memory hotplug won&#8217;t be enabled and the guest startup <font SIZE="-1">RAM</font> will never increase.</p>
<dt><code>-mem-path</code> <i>path</i></p>
<dd> Allocate guest <font SIZE="-1">RAM</font> from a temporarily created file in <i>path</i>.</p>
<dt><code>-mem-prealloc</code></p>
<dd> Preallocate memory when using -mem-path.</p>
<dt><code>-k</code> <i>language</i></p>
<dd> Use keyboard layout <i>language</i> (for example <tt>&quot;fr&quot;</tt> for French). This option is only needed where it is not easy to get raw <font SIZE="-1">PC</font> keycodes (e.g. on Macs, with some X11 servers or with a <font SIZE="-1">VNC</font> or curses display). You don&#8217;t normally need to use it on PC/Linux or PC/Windows hosts. </p>
<p> The available layouts are: </p>
<pre>
        ar  de-ch  es  fo     fr-ca  hu  ja  mk     no  pt-br  sv
        da  en-gb  et  fr     fr-ch  is  lt  nl     pl  ru     th
        de  en-us  fi  fr-be  hr     it  lv  nl-be  pt  sl     tr
</pre>
<p> The default is <tt>&quot;en-us&quot;</tt>.</p>
<dt><code>-audio-help</code></p>
<dd> Will show the -audiodev equivalent of the currently specified (deprecated) environment variables.</p>
<dt><code>-audiodev [driver=]</code><i>driver</i><code>,id=</code><i>id</i><code>[,</code><i>prop</i><code>[=</code><i>value</i><code>][,&#8230;]]</code></p>
<dd> Adds a new audio backend <i>driver</i> identified by <i>id</i>. There are global and driver specific properties. Some values can be set differently for input and output, they&#8217;re marked with <tt>&quot;in|out.&quot;</tt>. You can set the input&#8217;s property with <tt>&quot;in.</tt>prop<tt>&quot;</tt> and the output&#8217;s property with <tt>&quot;out.</tt>prop<tt>&quot;</tt>. For example: </p>
<pre>
        -audiodev alsa,id=example,in.frequency=44110,out.frequency=8000
        -audiodev alsa,id=example,out.channels=1 # leaves in.channels unspecified
</pre>
<p> <font SIZE="-1">NOTE:</font> parameter validation is known to be incomplete, in many cases specifying an invalid option causes <font SIZE="-1">QEMU</font> to print an error message and continue emulation without sound. </p>
<p> Valid global options are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>id=</code><i>identifier</i></p>
<dd> Identifies the audio backend.</p>
<dt><code>timer-period=</code><i>period</i></p>
<dd> Sets the timer <i>period</i> used by the audio subsystem in microseconds. Default is 10000 (10 ms).</p>
<dt><code>in|out.mixing-engine=on|off</code></p>
<dd> Use <font SIZE="-1">QEMU</font>&#8216;s mixing engine to mix all streams inside <font SIZE="-1">QEMU</font> and convert audio formats when not supported by the backend. When off, <i>fixed-settings</i> must be off too. Note that disabling this option means that the selected backend must support multiple streams and the audio formats used by the virtual cards, otherwise you&#8217;ll get no sound. It&#8217;s not recommended to disable this option unless you want to use 5.1 or 7.1 audio, as mixing engine only supports mono and stereo audio. Default is on.</p>
<dt><code>in|out.fixed-settings=on|off</code></p>
<dd> Use fixed settings for host audio. When off, it will change based on how the guest opens the sound card. In this case you must not specify <i>frequency</i>, <i>channels</i> or <i>format</i>. Default is on.</p>
<dt><code>in|out.frequency=</code><i>frequency</i></p>
<dd> Specify the <i>frequency</i> to use when using <i>fixed-settings</i>. Default is 44100Hz.</p>
<dt><code>in|out.channels=</code><i>channels</i></p>
<dd> Specify the number of <i>channels</i> to use when using <i>fixed-settings</i>. Default is 2 (stereo).</p>
<dt><code>in|out.format=</code><i>format</i></p>
<dd> Specify the sample <i>format</i> to use when using <i>fixed-settings</i>. Valid values are: <tt>&quot;s8&quot;</tt>, <tt>&quot;s16&quot;</tt>, <tt>&quot;s32&quot;</tt>, <tt>&quot;u8&quot;</tt>, <tt>&quot;u16&quot;</tt>, <tt>&quot;u32&quot;</tt>. Default is <tt>&quot;s16&quot;</tt>.</p>
<dt><code>in|out.voices=</code><i>voices</i></p>
<dd> Specify the number of <i>voices</i> to use. Default is 1.</p>
<dt><code>in|out.buffer-length=</code><i>usecs</i></p>
<dd> Sets the size of the buffer in microseconds.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-audiodev none,id=</code><i>id</i><code>[,</code><i>prop</i><code>[=</code><i>value</i><code>][,&#8230;]]</code></p>
<dd> Creates a dummy backend that discards all outputs. This backend has no backend specific properties.</p>
<dt><code>-audiodev alsa,id=</code><i>id</i><code>[,</code><i>prop</i><code>[=</code><i>value</i><code>][,&#8230;]]</code></p>
<dd> Creates backend using the <font SIZE="-1">ALSA.</font> This backend is only available on Linux. </p>
<p> <font SIZE="-1">ALSA</font> specific options are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>in|out.dev=</code><i>device</i></p>
<dd> Specify the <font SIZE="-1">ALSA</font> <i>device</i> to use for input and/or output. Default is <tt>&quot;default&quot;</tt>.</p>
<dt><code>in|out.period-length=</code><i>usecs</i></p>
<dd> Sets the period length in microseconds.</p>
<dt><code>in|out.try-poll=on|off</code></p>
<dd> Attempt to use poll mode with the device. Default is on.</p>
<dt><code>threshold=</code><i>threshold</i></p>
<dd> Threshold (in microseconds) when playback starts. Default is 0.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-audiodev coreaudio,id=</code><i>id</i><code>[,</code><i>prop</i><code>[=</code><i>value</i><code>][,&#8230;]]</code></p>
<dd> Creates a backend using Apple&#8217;s Core Audio. This backend is only available on Mac <font SIZE="-1">OS</font> and only supports playback. </p>
<p> Core Audio specific options are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>in|out.buffer-count=</code><i>count</i></p>
<dd> Sets the <i>count</i> of the buffers.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-audiodev dsound,id=</code><i>id</i><code>[,</code><i>prop</i><code>[=</code><i>value</i><code>][,&#8230;]]</code></p>
<dd> Creates a backend using Microsoft&#8217;s DirectSound. This backend is only available on Windows and only supports playback. </p>
<p> DirectSound specific options are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>latency=</code><i>usecs</i></p>
<dd> Add extra <i>usecs</i> microseconds latency to playback. Default is 10000 (10 ms).</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-audiodev oss,id=</code><i>id</i><code>[,</code><i>prop</i><code>[=</code><i>value</i><code>][,&#8230;]]</code></p>
<dd> Creates a backend using <font SIZE="-1">OSS.</font> This backend is available on most Unix-like systems. </p>
<p> <font SIZE="-1">OSS</font> specific options are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>in|out.dev=</code><i>device</i></p>
<dd> Specify the file name of the <font SIZE="-1">OSS</font> <i>device</i> to use. Default is <tt>&quot;/dev/dsp&quot;</tt>.</p>
<dt><code>in|out.buffer-count=</code><i>count</i></p>
<dd> Sets the <i>count</i> of the buffers.</p>
<dt><code>in|out.try-poll=on|of</code></p>
<dd> Attempt to use poll mode with the device. Default is on.</p>
<dt><code>try-mmap=on|off</code></p>
<dd> Try using memory mapped device access. Default is off.</p>
<dt><code>exclusive=on|off</code></p>
<dd> Open the device in exclusive mode (vmix won&#8217;t work in this case). Default is off.</p>
<dt><code>dsp-policy=</code><i>policy</i></p>
<dd> Sets the timing policy (between 0 and 10, where smaller number means smaller latency but higher <font SIZE="-1">CPU</font> usage). Use -1 to use buffer sizes specified by <tt>&quot;buffer&quot;</tt> and <tt>&quot;buffer-count&quot;</tt>. This option is ignored if you do not have <font SIZE="-1">OSS 4.</font> Default is 5.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-audiodev pa,id=</code><i>id</i><code>[,</code><i>prop</i><code>[=</code><i>value</i><code>][,&#8230;]]</code></p>
<dd> Creates a backend using PulseAudio. This backend is available on most systems. </p>
<p> PulseAudio specific options are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>server=</code><i>server</i></p>
<dd> Sets the PulseAudio <i>server</i> to connect to.</p>
<dt><code>in|out.name=</code><i>sink</i></p>
<dd> Use the specified source/sink for recording/playback.</p>
<dt><code>in|out.latency=</code><i>usecs</i></p>
<dd> Desired latency in microseconds. The PulseAudio server will try to honor this value but actual latencies may be lower or higher.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-audiodev sdl,id=</code><i>id</i><code>[,</code><i>prop</i><code>[=</code><i>value</i><code>][,&#8230;]]</code></p>
<dd> Creates a backend using <font SIZE="-1">SDL.</font> This backend is available on most systems, but you should use your platform&#8217;s native backend if possible. This backend has no backend specific properties.</p>
<dt><code>-audiodev spice,id=</code><i>id</i><code>[,</code><i>prop</i><code>[=</code><i>value</i><code>][,&#8230;]]</code></p>
<dd> Creates a backend that sends audio through <font SIZE="-1">SPICE.</font> This backend requires <tt>&quot;-spice&quot;</tt> and automatically selected in that case, so usually you can ignore this option. This backend has no backend specific properties.</p>
<dt><code>-audiodev wav,id=</code><i>id</i><code>[,</code><i>prop</i><code>[=</code><i>value</i><code>][,&#8230;]]</code></p>
<dd> Creates a backend that writes audio to a <font SIZE="-1">WAV</font> file. </p>
<p> Backend specific options are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>path=</code><i>path</i></p>
<dd> Write recorded audio into the specified file. Default is <tt>&quot;qemu.wav&quot;</tt>.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-soundhw</code> <i>card1</i><code>[,</code><i>card2</i><code>,&#8230;] or -soundhw all</code></p>
<dd> Enable audio and selected sound hardware. Use &#8216;help&#8217; to print all available sound hardware. For example: </p>
<pre>
        qemu-system-x86_64 -soundhw sb16,adlib disk.img
        qemu-system-x86_64 -soundhw es1370 disk.img
        qemu-system-x86_64 -soundhw ac97 disk.img
        qemu-system-x86_64 -soundhw hda disk.img
        qemu-system-x86_64 -soundhw all disk.img
        qemu-system-x86_64 -soundhw help
</pre>
<p> Note that Linux&#8217;s i810_audio <font SIZE="-1">OSS</font> kernel (for <font SIZE="-1">AC97</font>) module might require manually specifying clocking. </p>
<pre>
        modprobe i810_audio clocking=48000
</pre>
<dt><code>-device</code> <i>driver</i><code>[,</code><i>prop</i><code>[=</code><i>value</i><code>][,&#8230;]]</code></p>
<dd> Add device <i>driver</i>. <i>prop</i>=<i>value</i> sets driver properties. Valid properties depend on the driver. To get help on possible drivers and properties, use <tt>&quot;-device help&quot;</tt> and <tt>&quot;-device </tt>driver<tt>,help&quot;</tt>. </p>
<p> Some drivers are:</p>
<dt><code>-device ipmi-bmc-sim,id=</code><i>id</i><code>[,slave_addr=</code><i>val</i><code>][,sdrfile=</code><i>file</i><code>][,furareasize=</code><i>val</i><code>][,furdatafile=</code><i>file</i><code>][,guid=</code><i>uuid</i><code>]</code></p>
<dd> Add an <font SIZE="-1">IPMI BMC.</font> This is a simulation of a hardware management interface processor that normally sits on a system. It provides a watchdog and the ability to reset and power control the system. You need to connect this to an <font SIZE="-1">IPMI</font> interface to make it useful </p>
<p> The <font SIZE="-1">IPMI</font> slave address to use for the <font SIZE="-1">BMC.</font> The default is 0x20. This address is the <font SIZE="-1">BMC</font>&#8216;s address on the I2C network of management controllers. If you don&#8217;t know what this means, it is safe to ignore it.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>id=</code><i>id</i></p>
<dd> The <font SIZE="-1">BMC</font> id for interfaces to use this device.</p>
<dt><code>slave_addr=</code><i>val</i></p>
<dd> Define slave address to use for the <font SIZE="-1">BMC.</font> The default is 0x20.</p>
<dt><code>sdrfile=</code><i>file</i></p>
<dd> file containing raw Sensor Data Records (<font SIZE="-1">SDR</font>) data. The default is none.</p>
<dt><code>fruareasize=</code><i>val</i></p>
<dd> size of a Field Replaceable Unit (<font SIZE="-1">FRU</font>) area. The default is 1024.</p>
<dt><code>frudatafile=</code><i>file</i></p>
<dd> file containing raw Field Replaceable Unit (<font SIZE="-1">FRU</font>) inventory data. The default is none.</p>
<dt><code>guid=</code><i>uuid</i></p>
<dd> value for the <font SIZE="-1">GUID</font> for the <font SIZE="-1">BMC,</font> in standard <font SIZE="-1">UUID</font> format. If this is set, get &#8220;Get <font SIZE="-1">GUID&#8221;</font> command to the <font SIZE="-1">BMC</font> will return it. Otherwise &#8220;Get <font SIZE="-1">GUID&#8221;</font> will return an error.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-device ipmi-bmc-extern,id=</code><i>id</i><code>,chardev=</code><i>id</i><code>[,slave_addr=</code><i>val</i><code>]</code></p>
<dd> Add a connection to an external <font SIZE="-1">IPMI BMC</font> simulator. Instead of locally emulating the <font SIZE="-1">BMC</font> like the above item, instead connect to an external entity that provides the <font SIZE="-1">IPMI</font> services. </p>
<p> A connection is made to an external <font SIZE="-1">BMC</font> simulator. If you do this, it is strongly recommended that you use the &#8220;reconnect=&#8221; chardev option to reconnect to the simulator if the connection is lost. Note that if this is not used carefully, it can be a security issue, as the interface has the ability to send resets, NMIs, and power off the <font SIZE="-1">VM.</font> It&#8217;s best if <font SIZE="-1">QEMU</font> makes a connection to an external simulator running on a secure port on localhost, so neither the simulator nor <font SIZE="-1">QEMU</font> is exposed to any outside network. </p>
<p> See the &#8220;lanserv/README.vm&#8221; file in the OpenIPMI library for more details on the external interface.</p>
<dt><code>-device isa-ipmi-kcs,bmc=</code><i>id</i><code>[,ioport=</code><i>val</i><code>][,irq=</code><i>val</i><code>]</code></p>
<dd> Add a <font SIZE="-1">KCS IPMI</font> interafce on the <font SIZE="-1">ISA</font> bus. This also adds a corresponding <font SIZE="-1">ACPI</font> and <font SIZE="-1">SMBIOS</font> entries, if appropriate.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>bmc=</code><i>id</i></p>
<dd> The <font SIZE="-1">BMC</font> to connect to, one of ipmi-bmc-sim or ipmi-bmc-extern above.</p>
<dt><code>ioport=</code><i>val</i></p>
<dd> Define the I/O address of the interface. The default is 0xca0 for <font SIZE="-1">KCS.</font></p>
<dt><code>irq=</code><i>val</i></p>
<dd> Define the interrupt to use. The default is 5. To disable interrupts, set this to 0.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-device isa-ipmi-bt,bmc=</code><i>id</i><code>[,ioport=</code><i>val</i><code>][,irq=</code><i>val</i><code>]</code></p>
<dd> Like the <font SIZE="-1">KCS</font> interface, but defines a <font SIZE="-1">BT</font> interface. The default port is 0xe4 and the default interrupt is 5.</p>
<dt><code>-name</code> <i>name</i></p>
<dd> Sets the <i>name</i> of the guest. This name will be displayed in the <font SIZE="-1">SDL</font> window caption. The <i>name</i> will also be used for the <font SIZE="-1">VNC</font> server. Also optionally set the top visible process name in Linux. Naming of individual threads can also be enabled on Linux to aid debugging.</p>
<dt><code>-uuid</code> <i>uuid</i></p>
<dd> Set system <font SIZE="-1">UUID.</font></dl>
<p> <i>Block device options</i></p>
<dl>
<dt><code>-fda</code> <i>file</i></p>
<dd>
<dt><code>-fdb</code> <i>file</i></p>
<dd> Use <i>file</i> as floppy disk 0/1 image.</p>
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
<dt><code>-blockdev</code> <i>option</i><code>[,</code><i>option</i><code>[,</code><i>option</i><code>[,&#8230;]]]</code></p>
<dd> Define a new block driver node. Some of the options apply to all block drivers, other options are only accepted for a specific block driver. See below for a list of generic options and options for the most common block drivers. </p>
<p> Options that expect a reference to another node (e.g. <tt>&quot;file&quot;</tt>) can be given in two ways. Either you specify the node name of an already existing node (file=<i>node-name</i>), or you define a new node inline, adding options for the referenced node after a dot (file.filename=<i>path</i>,file.aio=native). </p>
<p> A block driver node created with <code>-blockdev</code> can be used for a guest device by specifying its node name for the <tt>&quot;drive&quot;</tt> property in a <code>-device</code> argument that defines a block device.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>Valid options for any block driver node:</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>&quot;driver&quot;</p>
<dd> Specifies the block driver to use for the given node.</p>
<dt>&quot;node-name&quot;</p>
<dd> This defines the name of the block driver node by which it will be referenced later. The name must be unique, i.e. it must not match the name of a different block driver node, or (if you use <code>-drive</code> as well) the <font SIZE="-1">ID</font> of a drive. </p>
<p> If no node name is specified, it is automatically generated. The generated node name is not intended to be predictable and changes between <font SIZE="-1">QEMU</font> invocations. For the top level, an explicit node name must be specified.</p>
<dt>&quot;read-only&quot;</p>
<dd> Open the node read-only. Guest write attempts will fail. </p>
<p> Note that some block drivers support only read-only access, either generally or in certain configurations. In this case, the default value <code>read-only=off</code> does not work and the option must be specified explicitly.</p>
<dt>&quot;auto-read-only&quot;</p>
<dd> If <code>auto-read-only=on</code> is set, <font SIZE="-1">QEMU</font> may fall back to read-only usage even when <code>read-only=off</code> is requested, or even switch between modes as needed, e.g. depending on whether the image file is writable or whether a writing user is attached to the node.</p>
<dt>&quot;force-share&quot;</p>
<dd> Override the image locking system of <font SIZE="-1">QEMU</font> by forcing the node to utilize weaker shared access for permissions where it would normally request exclusive access. When there is the potential for multiple instances to have the same file open (whether this invocation of <font SIZE="-1">QEMU</font> is the first or the second instance), both instances must permit shared access for the second instance to succeed at opening the file. </p>
<p> Enabling <code>force-share=on</code> requires <code>read-only=on</code>.</p>
<dt>&quot;cache.direct&quot;</p>
<dd> The host page cache can be avoided with <code>cache.direct=on</code>. This will attempt to do disk <font SIZE="-1">IO</font> directly to the guest&#8217;s memory. <font SIZE="-1">QEMU</font> may still perform an internal copy of the data.</p>
<dt>&quot;cache.no-flush&quot;</p>
<dd> In case you don&#8217;t care about data integrity over host failures, you can use <code>cache.no-flush=on</code>. This option tells <font SIZE="-1">QEMU</font> that it never needs to write any data to the disk but can instead keep things in cache. If anything goes wrong, like your host losing power, the disk storage getting disconnected accidentally, etc. your image will most probably be rendered unusable.</p>
<dt>&quot;discard=<i>discard</i>&quot;</p>
<dd> <i>discard</i> is one of &#8220;ignore&#8221; (or &#8220;off&#8221;) or &#8220;unmap&#8221; (or &#8220;on&#8221;) and controls whether <tt>&quot;discard&quot;</tt> (also known as <tt>&quot;trim&quot;</tt> or <tt>&quot;unmap&quot;</tt>) requests are ignored or passed to the filesystem. Some machine types may not support discard requests.</p>
<dt>&quot;detect-zeroes=<i>detect-zeroes</i>&quot;</p>
<dd> <i>detect-zeroes</i> is &#8220;off&#8221;, &#8220;on&#8221; or &#8220;unmap&#8221; and enables the automatic conversion of plain zero writes by the <font SIZE="-1">OS</font> to driver specific optimized zero write commands. You may even choose &#8220;unmap&#8221; if <i>discard</i> is set to &#8220;unmap&#8221; to allow a zero write to be converted to an <tt>&quot;unmap&quot;</tt> operation.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>Driver-specific options for </code>&quot;file&quot;</p>
<dd> This is the protocol-level block driver for accessing regular files.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&quot;filename&quot;</p>
<dd> The path to the image file in the local filesystem</p>
<dt>&quot;aio&quot;</p>
<dd> Specifies the <font SIZE="-1">AIO</font> backend (threads/native, default: threads)</p>
<dt>&quot;locking&quot;</p>
<dd> Specifies whether the image file is protected with Linux <font SIZE="-1">OFD / POSIX</font> locks. The default is to use the Linux Open File Descriptor <font SIZE="-1">API</font> if available, otherwise no lock is applied. (auto/on/off, default: auto)</dl>
</dl>
<dl>
<dt>
<dd>
<p> Example: </p>
<pre>
        -blockdev driver=file,node-name=disk,filename=disk.img
</pre>
</dl>
<dt><code>Driver-specific options for </code>&quot;raw&quot;</p>
<dd> This is the image format block driver for raw images. It is usually stacked on top of a protocol level block driver such as <tt>&quot;file&quot;</tt>.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&quot;file&quot;</p>
<dd> Reference to or definition of the data source block driver node (e.g. a <tt>&quot;file&quot;</tt> driver node)</dl>
</dl>
<dl>
<dt>
<dd>
<p> Example 1: </p>
<pre>
        -blockdev driver=file,node-name=disk_file,filename=disk.img
        -blockdev driver=raw,node-name=disk,file=disk_file
</pre>
<p> Example 2: </p>
<pre>
        -blockdev driver=raw,node-name=disk,file.driver=file,file.filename=disk.img
</pre>
</dl>
<dt><code>Driver-specific options for </code>&quot;qcow2&quot;</p>
<dd> This is the image format block driver for qcow2 images. It is usually stacked on top of a protocol level block driver such as <tt>&quot;file&quot;</tt>.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&quot;file&quot;</p>
<dd> Reference to or definition of the data source block driver node (e.g. a <tt>&quot;file&quot;</tt> driver node)</p>
<dt>&quot;backing&quot;</p>
<dd> Reference to or definition of the backing file block device (default is taken from the image file). It is allowed to pass <tt>&quot;null&quot;</tt> here in order to disable the default backing file.</p>
<dt>&quot;lazy-refcounts&quot;</p>
<dd> Whether to enable the lazy refcounts feature (on/off; default is taken from the image file)</p>
<dt>&quot;cache-size&quot;</p>
<dd> The maximum total size of the L2 table and refcount block caches in bytes (default: the sum of l2-cache-size and refcount-cache-size)</p>
<dt>&quot;l2-cache-size&quot;</p>
<dd> The maximum size of the L2 table cache in bytes (default: if cache-size is not specified &#8211; 32M on Linux platforms, and 8M on non-Linux platforms; otherwise, as large as possible within the cache-size, while permitting the requested or the minimal refcount cache size)</p>
<dt>&quot;refcount-cache-size&quot;</p>
<dd> The maximum size of the refcount block cache in bytes (default: 4 times the cluster size; or if cache-size is specified, the part of it which is not used for the L2 cache)</p>
<dt>&quot;cache-clean-interval&quot;</p>
<dd> Clean unused entries in the L2 and refcount caches. The interval is in seconds. The default value is 600 on supporting platforms, and 0 on other platforms. Setting it to 0 disables this feature.</p>
<dt>&quot;pass-discard-request&quot;</p>
<dd> Whether discard requests to the qcow2 device should be forwarded to the data source (on/off; default: on if discard=unmap is specified, off otherwise)</p>
<dt>&quot;pass-discard-snapshot&quot;</p>
<dd> Whether discard requests for the data source should be issued when a snapshot operation (e.g. deleting a snapshot) frees clusters in the qcow2 file (on/off; default: on)</p>
<dt>&quot;pass-discard-other&quot;</p>
<dd> Whether discard requests for the data source should be issued on other occasions where a cluster gets freed (on/off; default: off)</p>
<dt>&quot;overlap-check&quot;</p>
<dd> Which overlap checks to perform for writes to the image (none/constant/cached/all; default: cached). For details or finer granularity control refer to the <font SIZE="-1">QAPI</font> documentation of <tt>&quot;blockdev-add&quot;</tt>.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Example 1: </p>
<pre>
        -blockdev driver=file,node-name=my_file,filename=/tmp/disk.qcow2
        -blockdev driver=qcow2,node-name=hda,file=my_file,overlap-check=none,cache-size=16777216
</pre>
<p> Example 2: </p>
<pre>
        -blockdev driver=qcow2,node-name=disk,file.driver=http,file.filename=<a rel="nofollow" href="http://example.com/image.qcow2">http://example.com/image.qcow2</a>
</pre>
</dl>
<dt><code>Driver-specific options for other drivers</code></p>
<dd> Please refer to the <font SIZE="-1">QAPI</font> documentation of the <tt>&quot;blockdev-add&quot;</tt> <font SIZE="-1">QMP</font> command.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-drive</code> <i>option</i><code>[,</code><i>option</i><code>[,</code><i>option</i><code>[,&#8230;]]]</code></p>
<dd> Define a new drive. This includes creating a block driver node (the backend) as well as a guest device, and is mostly a shortcut for defining the corresponding <code>-blockdev</code> and <code>-device</code> options. </p>
<p> <code>-drive</code> accepts all options that are accepted by <code>-blockdev</code>. In addition, it knows the following options:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>file=</code><i>file</i></p>
<dd> This option defines which disk image to use with this drive. If the filename contains comma, you must double it (for instance, &#8220;file=my,,file&#8221; to use file &#8220;my,file&#8221;). </p>
<p> Special files such as iSCSI devices can be specified using protocol specific URLs. See the section for &#8220;Device <font SIZE="-1">URL</font> Syntax&#8221; for more information.</p>
<dt><code>if=</code><i>interface</i></p>
<dd> This option defines on which type on interface the drive is connected. Available types are: ide, scsi, sd, mtd, floppy, pflash, virtio, none.</p>
<dt><code>bus=</code><i>bus</i><code>,unit=</code><i>unit</i></p>
<dd> These options define where is connected the drive by defining the bus number and the unit id.</p>
<dt><code>index=</code><i>index</i></p>
<dd> This option defines where is connected the drive by using an index in the list of available connectors of a given interface type.</p>
<dt><code>media=</code><i>media</i></p>
<dd> This option defines the type of the media: disk or cdrom.</p>
<dt><code>snapshot=</code><i>snapshot</i></p>
<dd> <i>snapshot</i> is &#8220;on&#8221; or &#8220;off&#8221; and controls snapshot mode for the given drive (see <code>-snapshot</code>).</p>
<dt><code>cache=</code><i>cache</i></p>
<dd> <i>cache</i> is &#8220;none&#8221;, &#8220;writeback&#8221;, &#8220;unsafe&#8221;, &#8220;directsync&#8221; or &#8220;writethrough&#8221; and controls how the host cache is used to access block data. This is a shortcut that sets the <code>cache.direct</code> and <code>cache.no-flush</code> options (as in <code>-blockdev</code>), and additionally <code>cache.writeback</code>, which provides a default for the <code>write-cache</code> option of block guest devices (as in <code>-device</code>). The modes correspond to the following settings: </p>
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
<dt><code>aio=</code><i>aio</i></p>
<dd> <i>aio</i> is &#8220;threads&#8221;, or &#8220;native&#8221; and selects between pthread based disk I/O and native Linux <font SIZE="-1">AIO.</font></p>
<dt><code>format=</code><i>format</i></p>
<dd> Specify which disk <i>format</i> will be used rather than detecting the format. Can be used to specify format=raw to avoid interpreting an untrusted format header.</p>
<dt><code>werror=</code><i>action</i><code>,rerror=</code><i>action</i></p>
<dd> Specify which <i>action</i> to take on write and read errors. Valid actions are: &#8220;ignore&#8221; (ignore the error and try to continue), &#8220;stop&#8221; (pause <font SIZE="-1">QEMU</font>), &#8220;report&#8221; (report the error to the guest), &#8220;enospc&#8221; (pause <font SIZE="-1">QEMU</font> only if the host disk is full; report the error to the guest otherwise). The default setting is <code>werror=enospc</code> and <code>rerror=report</code>.</p>
<dt><code>copy-on-read=</code><i>copy-on-read</i></p>
<dd> <i>copy-on-read</i> is &#8220;on&#8221; or &#8220;off&#8221; and enables whether to copy read backing file sectors into the image file.</p>
<dt><code>bps=</code><i>b</i><code>,bps_rd=</code><i>r</i><code>,bps_wr=</code><i>w</i></p>
<dd> Specify bandwidth throttling limits in bytes per second, either for all request types or for reads or writes only. Small values can lead to timeouts or hangs inside the guest. A safe minimum for disks is 2 MB/s.</p>
<dt><code>bps_max=</code><i>bm</i><code>,bps_rd_max=</code><i>rm</i><code>,bps_wr_max=</code><i>wm</i></p>
<dd> Specify bursts in bytes per second, either for all request types or for reads or writes only. Bursts allow the guest I/O to spike above the limit temporarily.</p>
<dt><code>iops=</code><i>i</i><code>,iops_rd=</code><i>r</i><code>,iops_wr=</code><i>w</i></p>
<dd> Specify request rate limits in requests per second, either for all request types or for reads or writes only.</p>
<dt><code>iops_max=</code><i>bm</i><code>,iops_rd_max=</code><i>rm</i><code>,iops_wr_max=</code><i>wm</i></p>
<dd> Specify bursts in requests per second, either for all request types or for reads or writes only. Bursts allow the guest I/O to spike above the limit temporarily.</p>
<dt><code>iops_size=</code><i>is</i></p>
<dd> Let every <i>is</i> bytes of a request count as a new request for iops throttling purposes. Use this option to prevent guests from circumventing iops limits by sending fewer but larger requests.</p>
<dt><code>group=</code><i>g</i></p>
<dd> Join a throttling quota group with given name <i>g</i>. All drives that are members of the same group are accounted for together. Use this option to prevent guests from circumventing throttling limits by using many small disks instead of a single larger disk.</dl>
</dl>
<dl>
<dt>
<dd>
<p> By default, the <code>cache.writeback=on</code> mode is used. It will report data writes as completed as soon as the data is present in the host page cache. This is safe as long as your guest <font SIZE="-1">OS</font> makes sure to correctly flush disk caches where needed. If your guest <font SIZE="-1">OS</font> does not handle volatile disk write caches correctly and your host crashes or loses power, then the guest may experience data corruption. </p>
<p> For such guests, you should consider using <code>cache.writeback=off</code>. This means that the host page cache will be used to read and write data, but write notification will be sent to the guest only after <font SIZE="-1">QEMU</font> has made sure to flush each write to the disk. Be aware that this has a major impact on performance. </p>
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
<p> You can connect a <font SIZE="-1">CDROM</font> to the slave of ide0: </p>
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
</dl>
<dt><code>-mtdblock</code> <i>file</i></p>
<dd> Use <i>file</i> as on-board Flash memory image.</p>
<dt><code>-sd</code> <i>file</i></p>
<dd> Use <i>file</i> as SecureDigital card image.</p>
<dt><code>-pflash</code> <i>file</i></p>
<dd> Use <i>file</i> as a parallel flash image.</p>
<dt><code>-snapshot</code></p>
<dd> Write to temporary files instead of disk image files. In this case, the raw disk image you use is not written back. You can however force the write back by pressing <code>C-a s</code>.</p>
<dt><code>-fsdev local,id=</code><i>id</i><code>,path=</code><i>path</i><code>,security_model=</code><i>security_model</i> <code>[,writeout=</code><i>writeout</i><code>][,readonly][,fmode=</code><i>fmode</i><code>][,dmode=</code><i>dmode</i><code>] [,throttling.</code><i>option</i><code>=</code><i>value</i><code>[,throttling.</code><i>option</i><code>=</code><i>value</i><code>[,&#8230;]]]</code></p>
<dd>
<dt><code>-fsdev proxy,id=</code><i>id</i><code>,socket=</code><i>socket</i><code>[,writeout=</code><i>writeout</i><code>][,readonly]</code></p>
<dd>
<dt><code>-fsdev proxy,id=</code><i>id</i><code>,sock_fd=</code><i>sock_fd</i><code>[,writeout=</code><i>writeout</i><code>][,readonly]</code></p>
<dd>
<dt><code>-fsdev synth,id=</code><i>id</i><code>[,readonly]</code></p>
<dd> Define a new file system device. Valid options are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>local</code></p>
<dd> Accesses to the filesystem are done by <font SIZE="-1">QEMU.</font></p>
<dt><code>proxy</code></p>
<dd> Accesses to the filesystem are done by <code><a href="/docs/linux/man/1-virtfs-proxy-helper/">virtfs-proxy-helper</a></code>(1).</p>
<dt><code>synth</code></p>
<dd> Synthetic filesystem, only used by QTests.</p>
<dt><code>id=</code><i>id</i></p>
<dd> Specifies identifier for this device.</p>
<dt><code>path=</code><i>path</i></p>
<dd> Specifies the export path for the file system device. Files under this path will be available to the 9p client on the guest.</p>
<dt><code>security_model=</code><i>security_model</i></p>
<dd> Specifies the security model to be used for this export path. Supported security models are &#8220;passthrough&#8221;, &#8220;mapped-xattr&#8221;, &#8220;mapped-file&#8221; and &#8220;none&#8221;. In &#8220;passthrough&#8221; security model, files are stored using the same credentials as they are created on the guest. This requires <font SIZE="-1">QEMU</font> to run as root. In &#8220;mapped-xattr&#8221; security model, some of the file attributes like uid, gid, mode bits and link target are stored as file attributes. For &#8220;mapped-file&#8221; these attributes are stored in the hidden .virtfs_metadata directory. Directories exported by this security model cannot interact with other unix tools. &#8220;none&#8221; security model is same as passthrough except the sever won&#8217;t report failures if it fails to set file attributes like ownership. Security model is mandatory only for local fsdriver. Other fsdrivers (like proxy) don&#8217;t take security model as a parameter.</p>
<dt><code>writeout=</code><i>writeout</i></p>
<dd> This is an optional argument. The only supported value is &#8220;immediate&#8221;. This means that host page cache will be used to read and write data but write notification will be sent to the guest only when the data has been reported as written by the storage subsystem.</p>
<dt><code>readonly</code></p>
<dd> Enables exporting 9p share as a readonly mount for guests. By default read-write access is given.</p>
<dt><code>socket=</code><i>socket</i></p>
<dd> Enables proxy filesystem driver to use passed socket file for communicating with <code><a href="/docs/linux/man/1-virtfs-proxy-helper/">virtfs-proxy-helper</a></code>(1).</p>
<dt><code>sock_fd=</code><i>sock_fd</i></p>
<dd> Enables proxy filesystem driver to use passed socket descriptor for communicating with <code><a href="/docs/linux/man/1-virtfs-proxy-helper/">virtfs-proxy-helper</a></code>(1). Usually a helper like libvirt will create socketpair and pass one of the fds as sock_fd.</p>
<dt><code>fmode=</code><i>fmode</i></p>
<dd> Specifies the default mode for newly created files on the host. Works only with security models &#8220;mapped-xattr&#8221; and &#8220;mapped-file&#8221;.</p>
<dt><code>dmode=</code><i>dmode</i></p>
<dd> Specifies the default mode for newly created directories on the host. Works only with security models &#8220;mapped-xattr&#8221; and &#8220;mapped-file&#8221;.</p>
<dt><code>throttling.bps-total=</code><i>b</i><code>,throttling.bps-read=</code><i>r</i><code>,throttling.bps-write=</code><i>w</i></p>
<dd> Specify bandwidth throttling limits in bytes per second, either for all request types or for reads or writes only.</p>
<dt><code>throttling.bps-total-max=</code><i>bm</i><code>,bps-read-max=</code><i>rm</i><code>,bps-write-max=</code><i>wm</i></p>
<dd> Specify bursts in bytes per second, either for all request types or for reads or writes only. Bursts allow the guest I/O to spike above the limit temporarily.</p>
<dt><code>throttling.iops-total=</code><i>i</i><code>,throttling.iops-read=</code><i>r</i><code>, throttling.iops-write=</code><i>w</i></p>
<dd> Specify request rate limits in requests per second, either for all request types or for reads or writes only.</p>
<dt><code>throttling.iops-total-max=</code><i>im</i><code>,throttling.iops-read-max=</code><i>irm</i><code>, throttling.iops-write-max=</code><i>iwm</i></p>
<dd> Specify bursts in requests per second, either for all request types or for reads or writes only. Bursts allow the guest I/O to spike above the limit temporarily.</p>
<dt><code>throttling.iops-size=</code><i>is</i></p>
<dd> Let every <i>is</i> bytes of a request count as a new request for iops throttling purposes.</dl>
</dl>
<dl>
<dt>
<dd>
<p> -fsdev option is used along with -device driver &#8220;virtio-9p-&#8230;&#8221;.</dl>
<dt><code>-device virtio-9p-</code><i>type</i><code>,fsdev=</code><i>id</i><code>,mount_tag=</code><i>mount_tag</i></p>
<dd> Options for virtio-9p-&#8230; driver are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>type</i></p>
<dd> Specifies the variant to be used. Supported values are &#8220;pci&#8221;, &#8220;ccw&#8221; or &#8220;device&#8221;, depending on the machine type.</p>
<dt><code>fsdev=</code><i>id</i></p>
<dd> Specifies the id value specified along with -fsdev option.</p>
<dt><code>mount_tag=</code><i>mount_tag</i></p>
<dd> Specifies the tag name to be used by the guest to mount this export point.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-virtfs local,path=</code><i>path</i><code>,mount_tag=</code><i>mount_tag</i> <code>,security_model=</code><i>security_model</i><code>[,writeout=</code><i>writeout</i><code>][,readonly] [,fmode=</code><i>fmode</i><code>][,dmode=</code><i>dmode</i><code>][,multidevs=</code><i>multidevs</i><code>]</code></p>
<dd>
<dt><code>-virtfs proxy,socket=</code><i>socket</i><code>,mount_tag=</code><i>mount_tag</i> <code>[,writeout=</code><i>writeout</i><code>][,readonly]</code></p>
<dd>
<dt><code>-virtfs proxy,sock_fd=</code><i>sock_fd</i><code>,mount_tag=</code><i>mount_tag</i> <code>[,writeout=</code><i>writeout</i><code>][,readonly]</code></p>
<dd>
<dt><code>-virtfs synth,mount_tag=</code><i>mount_tag</i></p>
<dd> Define a new filesystem device and expose it to the guest using a virtio-9p-device. The general form of a Virtual File system pass-through options are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>local</code></p>
<dd> Accesses to the filesystem are done by <font SIZE="-1">QEMU.</font></p>
<dt><code>proxy</code></p>
<dd> Accesses to the filesystem are done by <code><a href="/docs/linux/man/1-virtfs-proxy-helper/">virtfs-proxy-helper</a></code>(1).</p>
<dt><code>synth</code></p>
<dd> Synthetic filesystem, only used by QTests.</p>
<dt><code>id=</code><i>id</i></p>
<dd> Specifies identifier for the filesystem device</p>
<dt><code>path=</code><i>path</i></p>
<dd> Specifies the export path for the file system device. Files under this path will be available to the 9p client on the guest.</p>
<dt><code>security_model=</code><i>security_model</i></p>
<dd> Specifies the security model to be used for this export path. Supported security models are &#8220;passthrough&#8221;, &#8220;mapped-xattr&#8221;, &#8220;mapped-file&#8221; and &#8220;none&#8221;. In &#8220;passthrough&#8221; security model, files are stored using the same credentials as they are created on the guest. This requires <font SIZE="-1">QEMU</font> to run as root. In &#8220;mapped-xattr&#8221; security model, some of the file attributes like uid, gid, mode bits and link target are stored as file attributes. For &#8220;mapped-file&#8221; these attributes are stored in the hidden .virtfs_metadata directory. Directories exported by this security model cannot interact with other unix tools. &#8220;none&#8221; security model is same as passthrough except the sever won&#8217;t report failures if it fails to set file attributes like ownership. Security model is mandatory only for local fsdriver. Other fsdrivers (like proxy) don&#8217;t take security model as a parameter.</p>
<dt><code>writeout=</code><i>writeout</i></p>
<dd> This is an optional argument. The only supported value is &#8220;immediate&#8221;. This means that host page cache will be used to read and write data but write notification will be sent to the guest only when the data has been reported as written by the storage subsystem.</p>
<dt><code>readonly</code></p>
<dd> Enables exporting 9p share as a readonly mount for guests. By default read-write access is given.</p>
<dt><code>socket=</code><i>socket</i></p>
<dd> Enables proxy filesystem driver to use passed socket file for communicating with <code><a href="/docs/linux/man/1-virtfs-proxy-helper/">virtfs-proxy-helper</a></code>(1). Usually a helper like libvirt will create socketpair and pass one of the fds as sock_fd.</p>
<dt><code>sock_fd</code></p>
<dd> Enables proxy filesystem driver to use passed &#8216;sock_fd&#8217; as the socket descriptor for interfacing with <code><a href="/docs/linux/man/1-virtfs-proxy-helper/">virtfs-proxy-helper</a></code>(1).</p>
<dt><code>fmode=</code><i>fmode</i></p>
<dd> Specifies the default mode for newly created files on the host. Works only with security models &#8220;mapped-xattr&#8221; and &#8220;mapped-file&#8221;.</p>
<dt><code>dmode=</code><i>dmode</i></p>
<dd> Specifies the default mode for newly created directories on the host. Works only with security models &#8220;mapped-xattr&#8221; and &#8220;mapped-file&#8221;.</p>
<dt><code>mount_tag=</code><i>mount_tag</i></p>
<dd> Specifies the tag name to be used by the guest to mount this export point.</p>
<dt><code>multidevs=</code><i>multidevs</i></p>
<dd> Specifies how to deal with multiple devices being shared with a 9p export. Supported behaviours are either &#8220;remap&#8221;, &#8220;forbid&#8221; or &#8220;warn&#8221;. The latter is the default behaviour on which virtfs 9p expects only one device to be shared with the same export, and if more than one device is shared and accessed via the same 9p export then only a warning message is logged (once) by qemu on host side. In order to avoid file <font SIZE="-1">ID</font> collisions on guest you should either create a separate virtfs export for each device to be shared with guests (recommended way) or you might use &#8220;remap&#8221; instead which allows you to share multiple devices with only one export instead, which is achieved by remapping the original inode numbers from host to guest in a way that would prevent such collisions. Remapping inodes in such use cases is required because the original device IDs from host are never passed and exposed on guest. Instead all files of an export shared with virtfs always share the same device id on guest. So two files with identical inode numbers but from actually different devices on host would otherwise cause a file <font SIZE="-1">ID</font> collision and hence potential misbehaviours on guest. &#8220;forbid&#8221; on the other hand assumes like &#8220;warn&#8221; that only one device is shared by the same export, however it will not only log a warning message but also deny access to additional devices on guest. Note though that &#8220;forbid&#8221; does currently not block all possible file access operations (e.g. <code>readdir()</code> would still return entries from other devices).</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-virtfs_synth</code></p>
<dd> Create synthetic file system image. Note that this option is now deprecated. Please use <tt>&quot;-fsdev synth&quot;</tt> and <tt>&quot;-device virtio-9p-...&quot;</tt> instead.</p>
<dt><code>-iscsi</code></p>
<dd> Configure iSCSI session parameters.</dl>
<p> <i></i><font SIZE="-1"><i>USB</i></font><i> options</i></p>
<dl>
<dt><code>-usb</code></p>
<dd> Enable <font SIZE="-1">USB</font> emulation on machine types with an on-board <font SIZE="-1">USB</font> host controller (if not enabled by default). Note that on-board <font SIZE="-1">USB</font> host controllers may not support <font SIZE="-1">USB 3.0.</font> In this case <code>-device qemu-xhci</code> can be used instead on machines with <font SIZE="-1">PCI.</font></p>
<dt><code>-usbdevice</code> <i>devname</i></p>
<dd> Add the <font SIZE="-1">USB</font> device <i>devname</i>. Note that this option is deprecated, please use <tt>&quot;-device usb-...&quot;</tt> instead.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>mouse</code></p>
<dd> Virtual Mouse. This will override the <font SIZE="-1">PS/2</font> mouse emulation when activated.</p>
<dt><code>tablet</code></p>
<dd> Pointer device that uses absolute coordinates (like a touchscreen). This means <font SIZE="-1">QEMU</font> is able to report the mouse position without having to grab the mouse. Also overrides the <font SIZE="-1">PS/2</font> mouse emulation when activated.</p>
<dt><code>braille</code></p>
<dd> Braille device. This will use BrlAPI to display the braille output on a real or fake device.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<p> <i>Display options</i></p>
<dl>
<dt><code>-display</code> <i>type</i></p>
<dd> Select type of display to use. This option is a replacement for the old style -sdl/-curses/&#8230; options. Valid values for <i>type</i> are</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>sdl</code></p>
<dd> Display video output via <font SIZE="-1">SDL</font> (usually in a separate graphics window; see the <font SIZE="-1">SDL</font> documentation for other possibilities).</p>
<dt><code>curses</code></p>
<dd> Display video output via curses. For graphics device models which support a text mode, <font SIZE="-1">QEMU</font> can display this output using a curses/ncurses interface. Nothing is displayed when the graphics device is in graphical mode or if the graphics device does not support a text mode. Generally only the <font SIZE="-1">VGA</font> device models support text mode. The font charset used by the guest can be specified with the <tt>&quot;charset&quot;</tt> option, for example <tt>&quot;charset=CP850&quot;</tt> for <font SIZE="-1">IBM CP850</font> encoding. The default is <tt>&quot;CP437&quot;</tt>.</p>
<dt><code>none</code></p>
<dd> Do not display video output. The guest will still see an emulated graphics card, but its output will not be displayed to the <font SIZE="-1">QEMU</font> user. This option differs from the -nographic option in that it only affects what is done with video output; -nographic also changes the destination of the serial and parallel port data.</p>
<dt><code>gtk</code></p>
<dd> Display video output in a <font SIZE="-1">GTK</font> window. This interface provides drop-down menus and other <font SIZE="-1">UI</font> elements to configure and control the <font SIZE="-1">VM</font> during runtime.</p>
<dt><code>vnc</code></p>
<dd> Start a <font SIZE="-1">VNC</font> server on display &lt;arg&gt;</p>
<dt><code>egl-headless</code></p>
<dd> Offload all OpenGL operations to a local <font SIZE="-1">DRI</font> device. For any graphical display, this display needs to be paired with either <font SIZE="-1">VNC</font> or <font SIZE="-1">SPICE</font> displays.</p>
<dt><code>spice-app</code></p>
<dd> Start <font SIZE="-1">QEMU</font> as a Spice server and launch the default Spice client application. The Spice server will redirect the serial consoles and <font SIZE="-1">QEMU</font> monitors. (Since 4.0)</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-nographic</code></p>
<dd> Normally, if <font SIZE="-1">QEMU</font> is compiled with graphical window support, it displays output such as guest graphics, guest console, and the <font SIZE="-1">QEMU</font> monitor in a window. With this option, you can totally disable graphical output so that <font SIZE="-1">QEMU</font> is a simple command line application. The emulated serial port is redirected on the console and muxed with the monitor (unless redirected elsewhere explicitly). Therefore, you can still use <font SIZE="-1">QEMU</font> to debug a Linux kernel with a serial console. Use <code>C-a h</code> for help on switching between the console and monitor.</p>
<dt><code>-curses</code></p>
<dd> Normally, if <font SIZE="-1">QEMU</font> is compiled with graphical window support, it displays output such as guest graphics, guest console, and the <font SIZE="-1">QEMU</font> monitor in a window. With this option, <font SIZE="-1">QEMU</font> can display the <font SIZE="-1">VGA</font> output when in text mode using a curses/ncurses interface. Nothing is displayed in graphical mode.</p>
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
<dd>
<dt><code>unix</code></p>
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
<dd> Configure video stream detection. Default is off.</p>
<dt><code>agent-mouse=[on|off]</code></p>
<dd> Enable/disable passing mouse events via vdagent. Default is on.</p>
<dt><code>playback-compression=[on|off]</code></p>
<dd> Enable/disable audio stream compression (using celt 0.5.1). Default is on.</p>
<dt><code>seamless-migration=[on|off]</code></p>
<dd> Enable/disable spice seamless migration. Default is off.</p>
<dt><code>gl=[on|off]</code></p>
<dd> Enable/disable OpenGL context. Default is off.</p>
<dt><code>rendernode=&lt;file&gt;</code></p>
<dd> <font SIZE="-1">DRM</font> render node for OpenGL rendering. If not specified, it will pick the first available. (Since 2.9)</dl>
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
<dd> Cirrus Logic <font SIZE="-1">GD5446</font> Video card. All Windows versions starting from Windows 95 should recognize and use this graphic card. For optimal performances, use 16 bit color depth in the guest and the host <font SIZE="-1">OS.</font> (This card was the default before <font SIZE="-1">QEMU 2.2</font>)</p>
<dt><code>std</code></p>
<dd> Standard <font SIZE="-1">VGA</font> card with Bochs <font SIZE="-1">VBE</font> extensions. If your guest <font SIZE="-1">OS</font> supports the <font SIZE="-1">VESA 2.0 VBE</font> extensions (e.g. Windows <font SIZE="-1">XP</font>) and if you want to use high resolution modes (&gt;= 1280x1024x16) then you should use this option. (This card is the default since <font SIZE="-1">QEMU 2.2</font>)</p>
<dt><code>vmware</code></p>
<dd> VMWare SVGA-II compatible adapter. Use it if you have sufficiently recent XFree86/XOrg server or Windows guest with a driver for this card.</p>
<dt><code>qxl</code></p>
<dd> <font SIZE="-1">QXL</font> paravirtual graphic card. It is <font SIZE="-1">VGA</font> compatible (including <font SIZE="-1">VESA 2.0 VBE</font> support). Works best with qxl guest drivers installed though. Recommended choice when using the spice protocol.</p>
<dt><code>tcx</code></p>
<dd> (sun4m only) Sun <font SIZE="-1">TCX</font> framebuffer. This is the default framebuffer for sun4m machines and offers both 8-bit and 24-bit colour depths at a fixed resolution of 1024&#215;768.</p>
<dt><code>cg3</code></p>
<dd> (sun4m only) Sun cgthree framebuffer. This is a simple 8-bit framebuffer for sun4m machines available in both 1024&#215;768 (OpenBIOS) and 1152&#215;900 (<font SIZE="-1">OBP</font>) resolutions aimed at people wishing to run older Solaris versions.</p>
<dt><code>virtio</code></p>
<dd> Virtio <font SIZE="-1">VGA</font> card.</p>
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
<dd> Normally, if <font SIZE="-1">QEMU</font> is compiled with graphical window support, it displays output such as guest graphics, guest console, and the <font SIZE="-1">QEMU</font> monitor in a window. With this option, you can have <font SIZE="-1">QEMU</font> listen on <font SIZE="-1">VNC</font> display <i>display</i> and redirect the <font SIZE="-1">VGA</font> display over the <font SIZE="-1">VNC</font> session. It is very useful to enable the usb tablet device when using this option (option <code>-device usb-tablet</code>). When using the <font SIZE="-1">VNC</font> display, you must use the <code>-k</code> parameter to set the keyboard layout if you are not using en-us. Valid syntax for the <i>display</i> is</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>to=</code><i>L</i></p>
<dd> With this option, <font SIZE="-1">QEMU</font> will try next available <font SIZE="-1">VNC</font> <i>display</i>s, until the number <i>L</i>, if the origianlly defined &quot;-vnc <i>display</i>&quot; is not available, e.g. port 5900+<i>display</i> is already used by another application. By default, to=0.</p>
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
<dd> Opens an additional <font SIZE="-1">TCP</font> listening port dedicated to <font SIZE="-1">VNC</font> Websocket connections. If a bare <i>websocket</i> option is given, the Websocket port is 5700+<i>display</i>. An alternative port can be specified with the syntax <tt>&quot;websocket&quot;</tt>=<i>port</i>. </p>
<p> If <i>host</i> is specified connections will only be allowed from this host. It is possible to control the websocket listen address independently, using the syntax <tt>&quot;websocket&quot;</tt>=<i>host</i>:<i>port</i>. </p>
<p> If no <font SIZE="-1">TLS</font> credentials are provided, the websocket connection runs in unencrypted mode. If <font SIZE="-1">TLS</font> credentials are provided, the websocket connection requires encrypted client connections.</p>
<dt><code>password</code></p>
<dd> Require that password based authentication is used for client connections. </p>
<p> The password must be set separately using the <tt>&quot;set_password&quot;</tt> command in the <code>pcsys_monitor</code>. The syntax to change your password is: <tt>&quot;set_password &lt;protocol&gt; &lt;password&gt;&quot;</tt> where &lt;protocol&gt; could be either &#8220;vnc&#8221; or &#8220;spice&#8221;. </p>
<p> If you would like to change &lt;protocol&gt; password expiration, you should use <tt>&quot;expire_password &lt;protocol&gt; &lt;expiration-time&gt;&quot;</tt> where expiration time could be one of the following options: now, never, +seconds or <font SIZE="-1">UNIX</font> time of expiration, e.g. +60 to make password expire in 60 seconds, or 1335196800 to make password expire on &#8220;Mon Apr 23 12:00:00 <font SIZE="-1">EDT 2012&#8221;</font> (<font SIZE="-1">UNIX</font> time for this date and time). </p>
<p> You can also use keywords &#8220;now&#8221; or &#8220;never&#8221; for the expiration time to allow &lt;protocol&gt; password to expire immediately or never expire.</p>
<dt><code>tls-creds=</code><i></i><font SIZE="-1"><i>ID</i></font><i></i></p>
<dd> Provides the <font SIZE="-1">ID</font> of a set of <font SIZE="-1">TLS</font> credentials to use to secure the <font SIZE="-1">VNC</font> server. They will apply to both the normal <font SIZE="-1">VNC</font> server socket and the websocket socket (if enabled). Setting <font SIZE="-1">TLS</font> credentials will cause the <font SIZE="-1">VNC</font> server socket to enable the VeNCrypt auth mechanism. The credentials should have been previously created using the <code>-object tls-creds</code> argument.</p>
<dt><code>tls-authz=</code><i></i><font SIZE="-1"><i>ID</i></font><i></i></p>
<dd> Provides the <font SIZE="-1">ID</font> of the QAuthZ authorization object against which the client&#8217;s x509 distinguished name will validated. This object is only resolved at time of use, so can be deleted and recreated on the fly while the <font SIZE="-1">VNC</font> server is active. If missing, it will default to denying access.</p>
<dt><code>sasl</code></p>
<dd> Require that the client use <font SIZE="-1">SASL</font> to authenticate with the <font SIZE="-1">VNC</font> server. The exact choice of authentication method used is controlled from the system / user&#8217;s <font SIZE="-1">SASL</font> configuration file for the &#8216;qemu&#8217; service. This is typically found in /etc/sasl2/qemu.conf. If running <font SIZE="-1">QEMU</font> as an unprivileged user, an environment variable <font SIZE="-1">SASL_CONF_PATH</font> can be used to make it search alternate locations for the service config. While some <font SIZE="-1">SASL</font> auth methods can also provide data encryption (eg <font SIZE="-1">GSSAPI</font>), it is recommended that <font SIZE="-1">SASL</font> always be combined with the &#8216;tls&#8217; and &#8216;x509&#8217; settings to enable use of <font SIZE="-1">SSL</font> and server certificates. This ensures a data encryption preventing compromise of authentication credentials. See the <code>vnc_security</code> section for details on using <font SIZE="-1">SASL</font> authentication.</p>
<dt><code>sasl-authz=</code><i></i><font SIZE="-1"><i>ID</i></font><i></i></p>
<dd> Provides the <font SIZE="-1">ID</font> of the QAuthZ authorization object against which the client&#8217;s <font SIZE="-1">SASL</font> username will validated. This object is only resolved at time of use, so can be deleted and recreated on the fly while the <font SIZE="-1">VNC</font> server is active. If missing, it will default to denying access.</p>
<dt><code>acl</code></p>
<dd> Legacy method for enabling authorization of clients against the x509 distinguished name and <font SIZE="-1">SASL</font> username. It results in the creation of two <tt>&quot;authz-list&quot;</tt> objects with IDs of <tt>&quot;vnc.username&quot;</tt> and <tt>&quot;vnc.x509dname&quot;</tt>. The rules for these objects must be configured with the <font SIZE="-1">HMP ACL</font> commands. </p>
<p> This option is deprecated and should no longer be used. The new <code>sasl-authz</code> and <code>tls-authz</code> options are a replacement.</p>
<dt><code>lossy</code></p>
<dd> Enable lossy compression methods (gradient, <font SIZE="-1">JPEG, &#8230;</font>). If this option is set, <font SIZE="-1">VNC</font> client may receive lossy framebuffer updates depending on its encoding settings. Enabling this option can save a lot of bandwidth at the expense of quality.</p>
<dt><code>non-adaptive</code></p>
<dd> Disable adaptive encodings. Adaptive encodings are enabled by default. An adaptive encoding will try to detect frequently updated screen regions, and send updates in these regions using a lossy encoding (like <font SIZE="-1">JPEG</font>). This can be really helpful to save bandwidth when playing videos. Disabling adaptive encodings restores the original static behavior of encodings like Tight.</p>
<dt><code>share=[allow-exclusive|force-shared|ignore]</code></p>
<dd> Set display sharing policy. &#8216;allow-exclusive&#8217; allows clients to ask for exclusive access. As suggested by the rfb spec this is implemented by dropping other connections. Connecting multiple clients in parallel requires all clients asking for a shared session (vncviewer: -shared switch). This is the default. &#8216;force-shared&#8217; disables exclusive client access. Useful for shared desktop sessions, where you don&#8217;t want someone forgetting specify -shared disconnect everybody else. &#8216;ignore&#8217; completely ignores the shared flag and allows everybody connect unconditionally. Doesn&#8217;t conform to the rfb spec but is traditional <font SIZE="-1">QEMU</font> behavior.</p>
<dt><code>key-delay-ms</code></p>
<dd> Set keyboard delay, for key down and key up events, in milliseconds. Default is 10. Keyboards are low-bandwidth devices, so this slowdown can help the device and guest to keep up and not lose events in case events are arriving in bulk. Possible causes for the latter are flaky network connections, or scripts for automated testing.</p>
<dt><code>audiodev=</code><i>audiodev</i></p>
<dd> Use the specified <i>audiodev</i> when the <font SIZE="-1">VNC</font> client requests audio transmission. When not using an -audiodev argument, this option must be omitted, otherwise is must be present and specify a valid audiodev.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<p> <i>i386 target only</i></p>
<dl>
<dt><code>-win2k-hack</code></p>
<dd> Use it when installing Windows 2000 to avoid a disk full bug. After Windows 2000 is installed, you no longer need this option (this option slows down the <font SIZE="-1">IDE</font> transfers).</p>
<dt><code>-no-fd-bootchk</code></p>
<dd> Disable boot signature checking for floppy disks in <font SIZE="-1">BIOS.</font> May be needed to boot from old floppy disks.</p>
<dt><code>-no-acpi</code></p>
<dd> Disable <font SIZE="-1">ACPI</font> (Advanced Configuration and Power Interface) support. Use it if your guest <font SIZE="-1">OS</font> complains about <font SIZE="-1">ACPI</font> problems (<font SIZE="-1">PC</font> target machine only).</p>
<dt><code>-no-hpet</code></p>
<dd> Disable <font SIZE="-1">HPET</font> support.</p>
<dt><code>-acpitable [sig=</code><i>str</i><code>][,rev=</code><i>n</i><code>][,oem_id=</code><i>str</i><code>][,oem_table_id=</code><i>str</i><code>][,oem_rev=</code><i>n</i><code>] [,asl_compiler_id=</code><i>str</i><code>][,asl_compiler_rev=</code><i>n</i><code>][,data=</code><i>file1</i><code>[:</code><i>file2</i><code>]&#8230;]</code></p>
<dd> Add <font SIZE="-1">ACPI</font> table with specified header fields and context from specified files. For file=, take whole <font SIZE="-1">ACPI</font> table from the specified files, including all <font SIZE="-1">ACPI</font> headers (possible overridden by other options). For data=, only data portion of the table is used, all header information is specified in the command line. If a <font SIZE="-1">SLIC</font> table is supplied to <font SIZE="-1">QEMU,</font> then the <font SIZE="-1">SLIC</font>&#8216;s oem_id and oem_table_id fields will override the same in the <font SIZE="-1">RSDT</font> and the <font SIZE="-1">FADT</font> (a.k.a. <font SIZE="-1">FACP</font>), in order to ensure the field matches required by the Microsoft <font SIZE="-1">SLIC</font> spec and the <font SIZE="-1">ACPI</font> spec.</p>
<dt><code>-smbios file=</code><i>binary</i></p>
<dd> Load <font SIZE="-1">SMBIOS</font> entry from binary file.</p>
<dt><code>-smbios type=0[,vendor=</code><i>str</i><code>][,version=</code><i>str</i><code>][,date=</code><i>str</i><code>][,release=</code><i></i>%d<i>.%d</i><code>][,uefi=on|off]</code></p>
<dd> Specify <font SIZE="-1">SMBIOS</font> type 0 fields</p>
<dt><code>-smbios type=1[,manufacturer=</code><i>str</i><code>][,product=</code><i>str</i><code>][,version=</code><i>str</i><code>][,serial=</code><i>str</i><code>][,uuid=</code><i>uuid</i><code>][,sku=</code><i>str</i><code>][,family=</code><i>str</i><code>]</code></p>
<dd> Specify <font SIZE="-1">SMBIOS</font> type 1 fields</p>
<dt><code>-smbios type=2[,manufacturer=</code><i>str</i><code>][,product=</code><i>str</i><code>][,version=</code><i>str</i><code>][,serial=</code><i>str</i><code>][,asset=</code><i>str</i><code>][,location=</code><i>str</i><code>]</code></p>
<dd> Specify <font SIZE="-1">SMBIOS</font> type 2 fields</p>
<dt><code>-smbios type=3[,manufacturer=</code><i>str</i><code>][,version=</code><i>str</i><code>][,serial=</code><i>str</i><code>][,asset=</code><i>str</i><code>][,sku=</code><i>str</i><code>]</code></p>
<dd> Specify <font SIZE="-1">SMBIOS</font> type 3 fields</p>
<dt><code>-smbios type=4[,sock_pfx=</code><i>str</i><code>][,manufacturer=</code><i>str</i><code>][,version=</code><i>str</i><code>][,serial=</code><i>str</i><code>][,asset=</code><i>str</i><code>][,part=</code><i>str</i><code>]</code></p>
<dd> Specify <font SIZE="-1">SMBIOS</font> type 4 fields</p>
<dt><code>-smbios type=17[,loc_pfx=</code><i>str</i><code>][,bank=</code><i>str</i><code>][,manufacturer=</code><i>str</i><code>][,serial=</code><i>str</i><code>][,asset=</code><i>str</i><code>][,part=</code><i>str</i><code>][,speed=</code><i></i>%d<i></i><code>]</code></p>
<dd> Specify <font SIZE="-1">SMBIOS</font> type 17 fields</dl>
<p> <i>Network options</i></p>
<dl>
<dt><code>-nic [tap|bridge|user|l2tpv3|vde|netmap|vhost-user|socket][,&#8230;][,mac=macaddr][,model=mn]</code></p>
<dd> This option is a shortcut for configuring both the on-board (default) guest <font SIZE="-1">NIC</font> hardware and the host network backend in one go. The host backend options are the same as with the corresponding <code>-netdev</code> options below. The guest <font SIZE="-1">NIC</font> model can be set with <code>model=</code><i>modelname</i>. Use <code>model=help</code> to list the available device types. The hardware <font SIZE="-1">MAC</font> address can be set with <code>mac=</code><i>macaddr</i>. </p>
<p> The following two example do exactly the same, to show how <code>-nic</code> can be used to shorten the command line length (note that the e1000 is the default on i386, so the <code>model=e1000</code> parameter could even be omitted here, too): </p>
<pre>
        qemu-system-x86_64 -netdev user,id=n1,ipv6=off -device e1000,netdev=n1,mac=52:54:98:76:54:32
        qemu-system-x86_64 -nic user,ipv6=off,model=e1000,mac=52:54:98:76:54:32
</pre>
<dt><code>-nic none</code></p>
<dd> Indicate that no network devices should be configured. It is used to override the default configuration (default <font SIZE="-1">NIC</font> with &#8220;user&#8221; host network backend) which is activated if no other networking options are provided.</p>
<dt><code>-netdev user,id=</code><i>id</i><code>[,</code><i>option</i><code>][,</code><i>option</i><code>][,&#8230;]</code></p>
<dd> Configure user mode host network backend which requires no administrator privilege to run. Valid options are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>id=</code><i>id</i></p>
<dd> Assign symbolic name for use in monitor commands.</p>
<dt><code>ipv4=on|off and ipv6=on|off</code></p>
<dd> Specify that either IPv4 or IPv6 must be enabled. If neither is specified both protocols are enabled.</p>
<dt><code>net=</code><i>addr</i><code>[/</code><i>mask</i><code>]</code></p>
<dd> Set <font SIZE="-1">IP</font> network address the guest will see. Optionally specify the netmask, either in the form a.b.c.d or as number of valid top-most bits. Default is 10.0.2.0/24.</p>
<dt><code>host=</code><i>addr</i></p>
<dd> Specify the guest-visible address of the host. Default is the 2nd <font SIZE="-1">IP</font> in the guest network, i.e. x.x.x.2.</p>
<dt><code>ipv6-net=</code><i>addr</i><code>[/</code><i>int</i><code>]</code></p>
<dd> Set IPv6 network address the guest will see (default is fec0::/64). The network prefix is given in the usual hexadecimal IPv6 address notation. The prefix size is optional, and is given as the number of valid top-most bits (default is 64).</p>
<dt><code>ipv6-host=</code><i>addr</i></p>
<dd> Specify the guest-visible IPv6 address of the host. Default is the 2nd IPv6 in the guest network, i.e. xxxx::2.</p>
<dt><code>restrict=on|off</code></p>
<dd> If this option is enabled, the guest will be isolated, i.e. it will not be able to contact the host and no guest <font SIZE="-1">IP</font> packets will be routed over the host to the outside. This option does not affect any explicitly set forwarding rules.</p>
<dt><code>hostname=</code><i>name</i></p>
<dd> Specifies the client hostname reported by the built-in <font SIZE="-1">DHCP</font> server.</p>
<dt><code>dhcpstart=</code><i>addr</i></p>
<dd> Specify the first of the 16 IPs the built-in <font SIZE="-1">DHCP</font> server can assign. Default is the 15th to 31st <font SIZE="-1">IP</font> in the guest network, i.e. x.x.x.15 to x.x.x.31.</p>
<dt><code>dns=</code><i>addr</i></p>
<dd> Specify the guest-visible address of the virtual nameserver. The address must be different from the host address. Default is the 3rd <font SIZE="-1">IP</font> in the guest network, i.e. x.x.x.3.</p>
<dt><code>ipv6-dns=</code><i>addr</i></p>
<dd> Specify the guest-visible address of the IPv6 virtual nameserver. The address must be different from the host address. Default is the 3rd <font SIZE="-1">IP</font> in the guest network, i.e. xxxx::3.</p>
<dt><code>dnssearch=</code><i>domain</i></p>
<dd> Provides an entry for the domain-search list sent by the built-in <font SIZE="-1">DHCP</font> server. More than one domain suffix can be transmitted by specifying this option multiple times. If supported, this will cause the guest to automatically try to append the given domain suffix(es) in case a domain name can not be resolved. </p>
<p> Example: </p>
<pre>
        qemu-system-x86_64 -nic user,dnssearch=mgmt.example.org,dnssearch=example.org
</pre>
<dt><code>domainname=</code><i>domain</i></p>
<dd> Specifies the client domain name reported by the built-in <font SIZE="-1">DHCP</font> server.</p>
<dt><code>tftp=</code><i>dir</i></p>
<dd> When using the user mode network stack, activate a built-in <font SIZE="-1">TFTP</font> server. The files in <i>dir</i> will be exposed as the root of a <font SIZE="-1">TFTP</font> server. The <font SIZE="-1">TFTP</font> client on the guest must be configured in binary mode (use the command <tt>&quot;bin&quot;</tt> of the Unix <font SIZE="-1">TFTP</font> client).</p>
<dt><code>tftp-server-name=</code><i>name</i></p>
<dd> In <font SIZE="-1">BOOTP</font> reply, broadcast <i>name</i> as the &#8220;<font SIZE="-1">TFTP</font> server name&#8221; (<font SIZE="-1">RFC2132</font> option 66). This can be used to advise the guest to load boot files or configurations from a different server than the host address.</p>
<dt><code>bootfile=</code><i>file</i></p>
<dd> When using the user mode network stack, broadcast <i>file</i> as the <font SIZE="-1">BOOTP</font> filename. In conjunction with <code>tftp</code>, this can be used to network boot a guest from a local directory. </p>
<p> Example (using pxelinux): </p>
<pre>
        qemu-system-x86_64 -hda linux.img -boot n -device e1000,netdev=n1 \
        -netdev user,id=n1,tftp=/path/to/tftp/files,bootfile=/pxelinux.0
</pre>
<dt><code>smb=</code><i>dir</i><code>[,smbserver=</code><i>addr</i><code>]</code></p>
<dd> When using the user mode network stack, activate a built-in <font SIZE="-1">SMB</font> server so that Windows OSes can access to the host files in <i>dir</i> transparently. The <font SIZE="-1">IP</font> address of the <font SIZE="-1">SMB</font> server can be set to <i>addr</i>. By default the 4th <font SIZE="-1">IP</font> in the guest network is used, i.e. x.x.x.4. </p>
<p> In the guest Windows <font SIZE="-1">OS,</font> the line: </p>
<pre>
        10.0.2.4 smbserver
</pre>
<p> must be added in the file <i>C:\WINDOWS\LMHOSTS</i> (for windows 9x/Me) or <i>C:\WINNT\SYSTEM32\DRIVERS\ETC\LMHOSTS</i> (Windows <font SIZE="-1">NT/2000</font>). </p>
<p> Then <i>dir</i> can be accessed in <i>\smbserver\qemu</i>. </p>
<p> Note that a <font SIZE="-1">SAMBA</font> server must be installed on the host <font SIZE="-1">OS.</font></p>
<dt><code>hostfwd=[tcp|udp]:[</code><i>hostaddr</i><code>]:</code><i>hostport</i><code>-[</code><i>guestaddr</i><code>]:</code><i>guestport</i></p>
<dd> Redirect incoming <font SIZE="-1">TCP</font> or <font SIZE="-1">UDP</font> connections to the host port <i>hostport</i> to the guest <font SIZE="-1">IP</font> address <i>guestaddr</i> on guest port <i>guestport</i>. If <i>guestaddr</i> is not specified, its value is x.x.x.15 (default first address given by the built-in <font SIZE="-1">DHCP</font> server). By specifying <i>hostaddr</i>, the rule can be bound to a specific host interface. If no connection type is set, <font SIZE="-1">TCP</font> is used. This option can be given multiple times. </p>
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
<dt><code>guestfwd=[tcp]:</code><i>server</i><code>:</code><i>port</i><code>&#8211;</code><i>dev</i></p>
<dd>
<dt><code>guestfwd=[tcp]:</code><i>server</i><code>:</code><i>port</i><code>&#8211;</code><i>cmd:command</i></p>
<dd> Forward guest <font SIZE="-1">TCP</font> connections to the <font SIZE="-1">IP</font> address <i>server</i> on port <i>port</i> to the character device <i>dev</i> or to a program executed by <i>cmd:command</i> which gets spawned for each connection. This option can be given multiple times. </p>
<p> You can either use a chardev directly and have that one used throughout <font SIZE="-1">QEMU</font>&#8216;s lifetime, like in the following example: </p>
<pre>
        # open 10.10.1.1:4321 on bootup, connect 10.0.2.100:1234 to it whenever
        # the guest accesses it
        qemu-system-x86_64 -nic user,guestfwd=tcp:10.0.2.100:1234-tcp:10.10.1.1:4321
</pre>
<p> Or you can execute a command on every <font SIZE="-1">TCP</font> connection established by the guest, so that <font SIZE="-1">QEMU</font> behaves similar to an inetd process for that virtual server: </p>
<pre>
        # call &quot;netcat 10.10.1.1 4321&quot; on every TCP connection to 10.0.2.100:1234
        # and connect the TCP stream to its stdin/stdout
        qemu-system-x86_64 -nic  'user,id=n1,guestfwd=tcp:10.0.2.100:1234-cmd:netcat 10.10.1.1 4321'
</pre>
</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-netdev tap,id=</code><i>id</i><code>[,fd=</code><i>h</i><code>][,ifname=</code><i>name</i><code>][,script=</code><i>file</i><code>][,downscript=</code><i>dfile</i><code>][,br=</code><i>bridge</i><code>][,helper=</code><i>helper</i><code>]</code></p>
<dd> Configure a host <font SIZE="-1">TAP</font> network backend with <font SIZE="-1">ID</font> <i>id</i>. </p>
<p> Use the network script <i>file</i> to configure it and the network script <i>dfile</i> to deconfigure it. If <i>name</i> is not provided, the <font SIZE="-1">OS</font> automatically provides one. The default network configure script is <i>/etc/qemu-ifup</i> and the default network deconfigure script is <i>/etc/qemu-ifdown</i>. Use <code>script=no</code> or <code>downscript=no</code> to disable script execution. </p>
<p> If running <font SIZE="-1">QEMU</font> as an unprivileged user, use the network helper <i>helper</i> to configure the <font SIZE="-1">TAP</font> interface and attach it to the bridge. The default network helper executable is <i>/path/to/qemu-bridge-helper</i> and the default bridge device is <i>br0</i>. </p>
<p> <code>fd</code>=<i>h</i> can be used to specify the handle of an already opened host <font SIZE="-1">TAP</font> interface. </p>
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
<dt><code>-netdev bridge,id=</code><i>id</i><code>[,br=</code><i>bridge</i><code>][,helper=</code><i>helper</i><code>]</code></p>
<dd> Connect a host <font SIZE="-1">TAP</font> network interface to a host bridge device. </p>
<p> Use the network helper <i>helper</i> to configure the <font SIZE="-1">TAP</font> interface and attach it to the bridge. The default network helper executable is <i>/path/to/qemu-bridge-helper</i> and the default bridge device is <i>br0</i>. </p>
<p> Examples: </p>
<pre>
        #launch a QEMU instance with the default network helper to
        #connect a TAP device to bridge br0
        qemu-system-x86_64 linux.img -netdev bridge,id=n1 -device virtio-net,netdev=n1
        
        #launch a QEMU instance with the default network helper to
        #connect a TAP device to bridge qemubr0
        qemu-system-x86_64 linux.img -netdev bridge,br=qemubr0,id=n1 -device virtio-net,netdev=n1
</pre>
<dt><code>-netdev socket,id=</code><i>id</i><code>[,fd=</code><i>h</i><code>][,listen=[</code><i>host</i><code>]:</code><i>port</i><code>][,connect=</code><i>host</i><code>:</code><i>port</i><code>]</code></p>
<dd> This host network backend can be used to connect the guest&#8217;s network to another <font SIZE="-1">QEMU</font> virtual machine using a <font SIZE="-1">TCP</font> socket connection. If <code>listen</code> is specified, <font SIZE="-1">QEMU</font> waits for incoming connections on <i>port</i> (<i>host</i> is optional). <code>connect</code> is used to connect to another <font SIZE="-1">QEMU</font> instance using the <code>listen</code> option. <code>fd</code>=<i>h</i> specifies an already opened <font SIZE="-1">TCP</font> socket. </p>
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
<dt><code>-netdev socket,id=</code><i>id</i><code>[,fd=</code><i>h</i><code>][,mcast=</code><i>maddr</i><code>:</code><i>port</i><code>[,localaddr=</code><i>addr</i><code>]]</code></p>
<dd> Configure a socket host network backend to share the guest&#8217;s network traffic with another <font SIZE="-1">QEMU</font> virtual machines using a <font SIZE="-1">UDP</font> multicast socket, effectively making a bus for every <font SIZE="-1">QEMU</font> with same multicast address <i>maddr</i> and <i>port</i>. <font SIZE="-1">NOTES:</font></p>
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
</dl>
<dt><code>-netdev l2tpv3,id=</code><i>id</i><code>,src=</code><i>srcaddr</i><code>,dst=</code><i>dstaddr</i><code>[,srcport=</code><i>srcport</i><code>][,dstport=</code><i>dstport</i><code>],txsession=</code><i>txsession</i><code>[,rxsession=</code><i>rxsession</i><code>][,ipv6][,udp][,cookie64][,counter][,pincounter][,txcookie=</code><i>txcookie</i><code>][,rxcookie=</code><i>rxcookie</i><code>][,offset=</code><i>offset</i><code>]</code></p>
<dd> Configure a L2TPv3 pseudowire host network backend. L2TPv3 (<font SIZE="-1">RFC3391</font>) is a popular protocol to transport Ethernet (and other Layer 2) data frames between two systems. It is present in routers, firewalls and the Linux kernel (from version 3.3 onwards). </p>
<p> This transport allows a <font SIZE="-1">VM</font> to communicate to another <font SIZE="-1">VM,</font> router or firewall directly.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>src=</code><i>srcaddr</i></p>
<dd> source address (mandatory)</p>
<dt><code>dst=</code><i>dstaddr</i></p>
<dd> destination address (mandatory)</p>
<dt><code>udp</code></p>
<dd> select udp encapsulation (default is ip).</p>
<dt><code>srcport=</code><i>srcport</i></p>
<dd> source udp port.</p>
<dt><code>dstport=</code><i>dstport</i></p>
<dd> destination udp port.</p>
<dt><code>ipv6</code></p>
<dd> force v6, otherwise defaults to v4.</p>
<dt><code>rxcookie=</code><i>rxcookie</i></p>
<dd>
<dt><code>txcookie=</code><i>txcookie</i></p>
<dd> Cookies are a weak form of security in the l2tpv3 specification. Their function is mostly to prevent misconfiguration. By default they are 32 bit.</p>
<dt><code>cookie64</code></p>
<dd> Set cookie size to 64 bit instead of the default 32</p>
<dt><code>counter=off</code></p>
<dd> Force a &#8216;cut-down&#8217; L2TPv3 with no counter as in draft-mkonstan-l2tpext-keyed-ipv6-tunnel-00</p>
<dt><code>pincounter=on</code></p>
<dd> Work around broken counter handling in peer. This may also help on networks which have packet reorder.</p>
<dt><code>offset=</code><i>offset</i></p>
<dd> Add an extra offset between header and data</dl>
</dl>
<dl>
<dt>
<dd>
<p> For example, to attach a <font SIZE="-1">VM</font> running on host 4.3.2.1 via L2TPv3 to the bridge br-lan on the remote Linux host 1.2.3.4: </p>
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
</dl>
<dt><code>-netdev vde,id=</code><i>id</i><code>[,sock=</code><i>socketpath</i><code>][,port=</code><i>n</i><code>][,group=</code><i>groupname</i><code>][,mode=</code><i>octalmode</i><code>]</code></p>
<dd> Configure <font SIZE="-1">VDE</font> backend to connect to <font SIZE="-1">PORT</font> <i>n</i> of a vde switch running on host and listening for incoming connections on <i>socketpath</i>. Use <font SIZE="-1">GROUP</font> <i>groupname</i> and <font SIZE="-1">MODE</font> <i>octalmode</i> to change default ownership and permissions for communication port. This option is only available if <font SIZE="-1">QEMU</font> has been compiled with vde support enabled. </p>
<p> Example: </p>
<pre>
        # launch vde switch
        vde_switch -F -sock /tmp/myswitch
        # launch QEMU instance
        qemu-system-x86_64 linux.img -nic vde,sock=/tmp/myswitch
</pre>
<dt><code>-netdev vhost-user,chardev=</code><i>id</i><code>[,vhostforce=on|off][,queues=n]</code></p>
<dd> Establish a vhost-user netdev, backed by a chardev <i>id</i>. The chardev should be a unix domain socket backed one. The vhost-user uses a specifically defined protocol to pass vhost ioctl replacement messages to an application on the other end of the socket. On non-MSIX guests, the feature can be forced with <i>vhostforce</i>. Use &#8216;queues=<i>n</i>&#8216; to specify the number of queues to be created for multiqueue vhost-user. </p>
<p> Example: </p>
<pre>
        qemu -m 512 -object memory-backend-file,id=mem,size=512M,mem-path=/hugetlbfs,share=on \
        -numa node,memdev=mem \
        -chardev socket,id=chr0,path=/path/to/socket \
        -netdev type=vhost-user,id=net0,chardev=chr0 \
        -device virtio-net-pci,netdev=net0
</pre>
<dt><code>-netdev hubport,id=</code><i>id</i><code>,hubid=</code><i>hubid</i><code>[,netdev=</code><i>nd</i><code>]</code></p>
<dd> Create a hub port on the emulated hub with <font SIZE="-1">ID</font> <i>hubid</i>. </p>
<p> The hubport netdev lets you connect a <font SIZE="-1">NIC</font> to a <font SIZE="-1">QEMU</font> emulated hub instead of a single netdev. Alternatively, you can also connect the hubport to another netdev with <font SIZE="-1">ID</font> <i>nd</i> by using the <code>netdev=</code><i>nd</i> option.</p>
<dt><code>-net nic[,netdev=</code><i>nd</i><code>][,macaddr=</code><i>mac</i><code>][,model=</code><i>type</i><code>] [,name=</code><i>name</i><code>][,addr=</code><i>addr</i><code>][,vectors=</code><i>v</i><code>]</code></p>
<dd> Legacy option to configure or create an on-board (or machine default) Network Interface Card(<font SIZE="-1">NIC</font>) and connect it either to the emulated hub with <font SIZE="-1">ID 0</font> (i.e. the default hub), or to the netdev <i>nd</i>. The <font SIZE="-1">NIC</font> is an e1000 by default on the <font SIZE="-1">PC</font> target. Optionally, the <font SIZE="-1">MAC</font> address can be changed to <i>mac</i>, the device address set to <i>addr</i> (<font SIZE="-1">PCI</font> cards only), and a <i>name</i> can be assigned for use in monitor commands. Optionally, for <font SIZE="-1">PCI</font> cards, you can specify the number <i>v</i> of MSI-X vectors that the card should have; this option currently only affects virtio cards; set <i>v</i> = 0 to disable MSI-X. If no <code>-net</code> option is specified, a single <font SIZE="-1">NIC</font> is created. <font SIZE="-1">QEMU</font> can emulate several different models of network card. Use <tt>&quot;-net nic,model=help&quot;</tt> for a list of available devices for your target.</p>
<dt><code>-net user|tap|bridge|socket|l2tpv3|vde[,&#8230;][,name=</code><i>name</i><code>]</code></p>
<dd> Configure a host network backend (with the options corresponding to the same <code>-netdev</code> option) and connect it to the emulated hub 0 (the default hub). Use <i>name</i> to specify the name of the hub port.</dl>
<p> <i>Character device options</i> </p>
<p> The general form of a character device option is:</p>
<dl>
<dt><code>-chardev</code> <i>backend</i><code>,id=</code><i>id</i><code>[,mux=on|off][,</code><i>options</i><code>]</code></p>
<dd> Backend is one of: <code>null</code>, <code>socket</code>, <code>udp</code>, <code>msmouse</code>, <code>vc</code>, <code>ringbuf</code>, <code>file</code>, <code>pipe</code>, <code>console</code>, <code>serial</code>, <code>pty</code>, <code>stdio</code>, <code>braille</code>, <code>tty</code>, <code>parallel</code>, <code>parport</code>, <code>spicevmc</code>, <code>spiceport</code>. The specific backend will determine the applicable options. </p>
<p> Use <tt>&quot;-chardev help&quot;</tt> to print all available chardev backend types. </p>
<p> All devices must have an id, which can be any string up to 127 characters long. It is used to uniquely identify this device in other command line directives. </p>
<p> A character device may be used in multiplexing mode by multiple front-ends. Specify <code>mux=on</code> to enable this mode. A multiplexer is a &#8220;1:N&#8221; device, and here the &#8220;1&#8221; end is your specified chardev backend, and the &#8220;N&#8221; end is the various parts of <font SIZE="-1">QEMU</font> that can talk to a chardev. If you create a chardev with <code>id=myid</code> and <code>mux=on</code>, <font SIZE="-1">QEMU</font> will create a multiplexer with your specified <font SIZE="-1">ID,</font> and you can then configure multiple front ends to use that chardev <font SIZE="-1">ID</font> for their input/output. Up to four different front ends can be connected to a single multiplexed chardev. (Without multiplexing enabled, a chardev can only be used by a single front end.) For instance you could use this to allow a single stdio chardev to be used by two serial ports and the <font SIZE="-1">QEMU</font> monitor: </p>
<pre>
        -chardev stdio,mux=on,id=char0 \
        -mon chardev=char0,mode=readline \
        -serial chardev:char0 \
        -serial chardev:char0
</pre>
<p> You can have more than one multiplexer in a system configuration; for instance you could have a <font SIZE="-1">TCP</font> port multiplexed between <font SIZE="-1">UART 0</font> and <font SIZE="-1">UART 1,</font> and stdio multiplexed between the <font SIZE="-1">QEMU</font> monitor and a parallel port: </p>
<pre>
        -chardev stdio,mux=on,id=char0 \
        -mon chardev=char0,mode=readline \
        -parallel chardev:char0 \
        -chardev tcp,...,mux=on,id=char1 \
        -serial chardev:char1 \
        -serial chardev:char1
</pre>
<p> When you&#8217;re using a multiplexed character device, some escape sequences are interpreted in the input. </p>
<p> Note that some other command line options may implicitly create multiplexed character backends; for instance <code>-serial mon:stdio</code> creates a multiplexed stdio backend connected to the serial port and the <font SIZE="-1">QEMU</font> monitor, and <code>-nographic</code> also multiplexes the console and the monitor to stdio. </p>
<p> There is currently no support for multiplexing in the other direction (where a single <font SIZE="-1">QEMU</font> front end takes input and output from multiple chardevs). </p>
<p> Every backend supports the <code>logfile</code> option, which supplies the path to a file to record all data transmitted via the backend. The <code>logappend</code> option controls whether the log file will be truncated or appended to when opened.</dl>
<p> The available backends are:</p>
<dl>
<dt><code>-chardev null,id=</code><i>id</i></p>
<dd> A void device. This device will not emit any data, and will drop any data it receives. The null backend does not take any options.</p>
<dt><code>-chardev socket,id=</code><i>id</i><code>[,</code><i></i><font SIZE="-1"><i>TCP</i></font><i> options</i> <code>or</code> <i>unix options</i><code>][,server][,nowait][,telnet][,websocket][,reconnect=</code><i>seconds</i><code>][,tls-creds=</code><i>id</i><code>][,tls-authz=</code><i>id</i><code>]</code></p>
<dd> Create a two-way stream socket, which can be either a <font SIZE="-1">TCP</font> or a unix socket. A unix socket will be created if <code>path</code> is specified. Behaviour is undefined if <font SIZE="-1">TCP</font> options are specified for a unix socket. </p>
<p> <code>server</code> specifies that the socket shall be a listening socket. </p>
<p> <code>nowait</code> specifies that <font SIZE="-1">QEMU</font> should not block waiting for a client to connect to a listening socket. </p>
<p> <code>telnet</code> specifies that traffic on the socket should interpret telnet escape sequences. </p>
<p> <code>websocket</code> specifies that the socket uses WebSocket protocol for communication. </p>
<p> <code>reconnect</code> sets the timeout for reconnecting on non-server sockets when the remote end goes away. qemu will delay this many seconds and then attempt to reconnect. Zero disables reconnecting, and is the default. </p>
<p> <code>tls-creds</code> requests enablement of the <font SIZE="-1">TLS</font> protocol for encryption, and specifies the id of the <font SIZE="-1">TLS</font> credentials to use for the handshake. The credentials must be previously created with the <code>-object tls-creds</code> argument. </p>
<p> <code>tls-auth</code> provides the <font SIZE="-1">ID</font> of the QAuthZ authorization object against which the client&#8217;s x509 distinguished name will be validated. This object is only resolved at time of use, so can be deleted and recreated on the fly while the chardev server is active. If missing, it will default to denying access. </p>
<p> <font SIZE="-1">TCP</font> and unix socket options are given below:</p>
<dl>
<dt>
<dd>
<dl>
<dt><font SIZE="-1"><code>TCP</code></font><code> options: port=</code><i>port</i><code>[,host=</code><i>host</i><code>][,to=</code><i>to</i><code>][,ipv4][,ipv6][,nodelay]</code></p>
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
<dt><code>-chardev udp,id=</code><i>id</i><code>[,host=</code><i>host</i><code>],port=</code><i>port</i><code>[,localaddr=</code><i>localaddr</i><code>][,localport=</code><i>localport</i><code>][,ipv4][,ipv6]</code></p>
<dd> Sends all traffic from the guest to a remote host over <font SIZE="-1">UDP.</font> </p>
<p> <code>host</code> specifies the remote host to connect to. If not specified it defaults to <tt>&quot;localhost&quot;</tt>. </p>
<p> <code>port</code> specifies the port on the remote host to connect to. <code>port</code> is required. </p>
<p> <code>localaddr</code> specifies the local address to bind to. If not specified it defaults to <tt>0.0.0.0</tt>. </p>
<p> <code>localport</code> specifies the local port to bind to. If not specified any available local port will be used. </p>
<p> <code>ipv4</code> and <code>ipv6</code> specify that either IPv4 or IPv6 must be used. If neither is specified the device may use either protocol.</p>
<dt><code>-chardev msmouse,id=</code><i>id</i></p>
<dd> Forward <font SIZE="-1">QEMU</font>&#8216;s emulated msmouse events to the guest. <code>msmouse</code> does not take any options.</p>
<dt><code>-chardev vc,id=</code><i>id</i><code>[[,width=</code><i>width</i><code>][,height=</code><i>height</i><code>]][[,cols=</code><i>cols</i><code>][,rows=</code><i>rows</i><code>]]</code></p>
<dd> Connect to a <font SIZE="-1">QEMU</font> text console. <code>vc</code> may optionally be given a specific size. </p>
<p> <code>width</code> and <code>height</code> specify the width and height respectively of the console, in pixels. </p>
<p> <code>cols</code> and <code>rows</code> specify that the console be sized to fit a text console with the given dimensions.</p>
<dt><code>-chardev ringbuf,id=</code><i>id</i><code>[,size=</code><i>size</i><code>]</code></p>
<dd> Create a ring buffer with fixed size <code>size</code>. <i>size</i> must be a power of two and defaults to <tt>&quot;64K&quot;</tt>.</p>
<dt><code>-chardev file,id=</code><i>id</i><code>,path=</code><i>path</i></p>
<dd> Log all traffic received from the guest to a file. </p>
<p> <code>path</code> specifies the path of the file to be opened. This file will be created if it does not already exist, and overwritten if it does. <code>path</code> is required.</p>
<dt><code>-chardev pipe,id=</code><i>id</i><code>,path=</code><i>path</i></p>
<dd> Create a two-way connection to the guest. The behaviour differs slightly between Windows hosts and other hosts: </p>
<p> On Windows, a single duplex pipe will be created at <i>\.pipe\</i>path<i></i>. </p>
<p> On other hosts, 2 pipes will be created called <i></i>path<i>.in</i> and <i></i>path<i>.out</i>. Data written to <i></i>path<i>.in</i> will be received by the guest. Data written by the guest can be read from <i></i>path<i>.out</i>. <font SIZE="-1">QEMU</font> will not create these fifos, and requires them to be present. </p>
<p> <code>path</code> forms part of the pipe path as described above. <code>path</code> is required.</p>
<dt><code>-chardev console,id=</code><i>id</i></p>
<dd> Send traffic from the guest to <font SIZE="-1">QEMU</font>&#8216;s standard output. <code>console</code> does not take any options. </p>
<p> <code>console</code> is only available on Windows hosts.</p>
<dt><code>-chardev serial,id=</code><i>id</i><code>,path=</code><code>path</code></p>
<dd> Send traffic from the guest to a serial device on the host. </p>
<p> On Unix hosts serial will actually accept any tty device, not only serial lines. </p>
<p> <code>path</code> specifies the name of the serial device to open.</p>
<dt><code>-chardev pty,id=</code><i>id</i></p>
<dd> Create a new pseudo-terminal on the host and connect to it. <code>pty</code> does not take any options. </p>
<p> <code>pty</code> is not available on Windows hosts.</p>
<dt><code>-chardev stdio,id=</code><i>id</i><code>[,signal=on|off]</code></p>
<dd> Connect to standard input and standard output of the <font SIZE="-1">QEMU</font> process. </p>
<p> <code>signal</code> controls if signals are enabled on the terminal, that includes exiting <font SIZE="-1">QEMU</font> with the key sequence <code>Control-c</code>. This option is enabled by default, use <code>signal=off</code> to disable it.</p>
<dt><code>-chardev braille,id=</code><i>id</i></p>
<dd> Connect to a local BrlAPI server. <code>braille</code> does not take any options.</p>
<dt><code>-chardev tty,id=</code><i>id</i><code>,path=</code><i>path</i></p>
<dd> <code>tty</code> is only available on Linux, Sun, FreeBSD, NetBSD, OpenBSD and DragonFlyBSD hosts. It is an alias for <code>serial</code>. </p>
<p> <code>path</code> specifies the path to the tty. <code>path</code> is required.</p>
<dt><code>-chardev parallel,id=</code><i>id</i><code>,path=</code><i>path</i></p>
<dd>
<dt><code>-chardev parport,id=</code><i>id</i><code>,path=</code><i>path</i></p>
<dd> <code>parallel</code> is only available on Linux, FreeBSD and DragonFlyBSD hosts. </p>
<p> Connect to a local parallel port. </p>
<p> <code>path</code> specifies the path to the parallel port device. <code>path</code> is required.</p>
<dt><code>-chardev spicevmc,id=</code><i>id</i><code>,debug=</code><i>debug</i><code>,name=</code><i>name</i></p>
<dd> <code>spicevmc</code> is only available when spice support is built in. </p>
<p> <code>debug</code> debug level for spicevmc </p>
<p> <code>name</code> name of spice channel to connect to </p>
<p> Connect to a spice virtual machine channel, such as vdiport.</p>
<dt><code>-chardev spiceport,id=</code><i>id</i><code>,debug=</code><i>debug</i><code>,name=</code><i>name</i></p>
<dd> <code>spiceport</code> is only available when spice support is built in. </p>
<p> <code>debug</code> debug level for spicevmc </p>
<p> <code>name</code> name of spice port to connect to </p>
<p> Connect to a spice port, allowing a Spice client to handle the traffic identified by a name (preferably a fqdn).</dl>
<p> <i>Bluetooth(R) options</i></p>
<dl>
<dt><code>-bt hci[&#8230;]</code></p>
<dd> Defines the function of the corresponding Bluetooth <font SIZE="-1">HCI.</font> -bt options are matched with the HCIs present in the chosen machine type. For example when emulating a machine with only one <font SIZE="-1">HCI</font> built into it, only the first <tt>&quot;-bt hci[...]&quot;</tt> option is valid and defines the <font SIZE="-1">HCI</font>&#8216;s logic. The Transport Layer is decided by the machine type. Currently the machines <tt>&quot;n800&quot;</tt> and <tt>&quot;n810&quot;</tt> have one <font SIZE="-1">HCI</font> and all other machines have none. </p>
<p> Note: This option and the whole bluetooth subsystem is considered as deprecated. If you still use it, please send a mail to &lt;<code>qemu-devel [at] nongnu.org</code>&gt; where you describe your usecase. </p>
<p> The following three types are recognized:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-bt hci,null</code></p>
<dd> (default) The corresponding Bluetooth <font SIZE="-1">HCI</font> assumes no internal logic and will not respond to any <font SIZE="-1">HCI</font> commands or emit events.</p>
<dt><code>-bt hci,host[:</code><i>id</i><code>]</code></p>
<dd> (<tt>&quot;bluez&quot;</tt> only) The corresponding <font SIZE="-1">HCI</font> passes commands / events to / from the physical <font SIZE="-1">HCI</font> identified by the name <i>id</i> (default: <tt>&quot;hci0&quot;</tt>) on the computer running <font SIZE="-1">QEMU.</font> Only available on <tt>&quot;bluez&quot;</tt> capable systems like Linux.</p>
<dt><code>-bt hci[,vlan=</code><i>n</i><code>]</code></p>
<dd> Add a virtual, standard <font SIZE="-1">HCI</font> that will participate in the Bluetooth scatternet <i>n</i> (default <tt>0</tt>). Similarly to <code>-net</code> VLANs, devices inside a bluetooth network <i>n</i> can only communicate with other devices in the same network (scatternet).</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-bt vhci[,vlan=</code><i>n</i><code>]</code></p>
<dd> (Linux-host only) Create a <font SIZE="-1">HCI</font> in scatternet <i>n</i> (default 0) attached to the host bluetooth stack instead of to the emulated target. This allows the host and target machines to participate in a common scatternet and communicate. Requires the Linux <tt>&quot;vhci&quot;</tt> driver installed. Can be used as following: </p>
<pre>
        qemu-system-x86_64 [...OPTIONS...] -bt hci,vlan=5 -bt vhci,vlan=5
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
<p> <i></i><font SIZE="-1"><i>TPM</i></font><i> device options</i> </p>
<p> The general form of a <font SIZE="-1">TPM</font> device option is:</p>
<dl>
<dt><code>-tpmdev</code> <i>backend</i><code>,id=</code><i>id</i><code>[,</code><i>options</i><code>]</code></p>
<dd> The specific backend type will determine the applicable options. The <tt>&quot;-tpmdev&quot;</tt> option creates the <font SIZE="-1">TPM</font> backend and requires a <tt>&quot;-device&quot;</tt> option that specifies the <font SIZE="-1">TPM</font> frontend interface model. </p>
<p> Use <tt>&quot;-tpmdev help&quot;</tt> to print all available <font SIZE="-1">TPM</font> backend types.</dl>
<p> The available backends are:</p>
<dl>
<dt><code>-tpmdev passthrough,id=</code><i>id</i><code>,path=</code><i>path</i><code>,cancel-path=</code><i>cancel-path</i></p>
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
<p> Note that the <tt>&quot;-tpmdev&quot;</tt> id is <tt>&quot;tpm0&quot;</tt> and is referenced by <tt>&quot;tpmdev=tpm0&quot;</tt> in the device option.</p>
<dt><code>-tpmdev emulator,id=</code><i>id</i><code>,chardev=</code><i>dev</i></p>
<dd> (Linux-host only) Enable access to a <font SIZE="-1">TPM</font> emulator using Unix domain socket based chardev backend. </p>
<p> <code>chardev</code> specifies the unique <font SIZE="-1">ID</font> of a character device backend that provides connection to the software <font SIZE="-1">TPM</font> server. </p>
<p> To create a <font SIZE="-1">TPM</font> emulator backend device with chardev socket backend: </p>
<pre>
        -chardev socket,id=chrtpm,path=/tmp/swtpm-sock -tpmdev emulator,id=tpm0,chardev=chrtpm -device tpm-tis,tpmdev=tpm0
</pre>
</dl>
<p> <i>Linux/Multiboot boot specific</i> </p>
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
<p> <i>Debug/Expert options</i></p>
<dl>
<dt><code>-fw_cfg [name=]</code><i>name</i><code>,file=</code><i>file</i></p>
<dd> Add named fw_cfg entry with contents from file <i>file</i>.</p>
<dt><code>-fw_cfg [name=]</code><i>name</i><code>,string=</code><i>str</i></p>
<dd> Add named fw_cfg entry with contents from string <i>str</i>. </p>
<p> The terminating <font SIZE="-1">NUL</font> character of the contents of <i>str</i> will not be included as part of the fw_cfg item data. To insert contents with embedded <font SIZE="-1">NUL</font> characters, you have to use the <i>file</i> parameter. </p>
<p> The fw_cfg entries are passed by <font SIZE="-1">QEMU</font> through to the guest. </p>
<p> Example: </p>
<pre>
        -fw_cfg name=opt/com.mycompany/blob,file=./my_blob.bin
</pre>
<p> creates an fw_cfg entry named opt/com.mycompany/blob with contents from ./my_blob.bin.</p>
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
<dd> [Linux only] Pseudo <font SIZE="-1">TTY</font> (a new <font SIZE="-1">PTY</font> is automatically allocated)</p>
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
<p> If you plan to send characters back via netconsole or you want to stop and start <font SIZE="-1">QEMU</font> a lot of times, you should have <font SIZE="-1">QEMU</font> use the same source port each time by using something like <tt>&quot;-serial udp::4555 [at] 4556&quot;</tt> to <font SIZE="-1">QEMU.</font> Another approach is to use a patched version of netcat which can listen to a <font SIZE="-1">TCP</font> port and send and receive characters via udp. If you have a patched version of netcat which activates telnet remote echo and single char transfer, then you can use the following options to set up a netcat redirector to allow telnet on port 5555 to access the <font SIZE="-1">QEMU</font> port.</p>
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
<dt><code>tcp:[</code><i>host</i><code>]:</code><i>port</i><code>[,</code><i>server</i><code>][,nowait][,nodelay][,reconnect=</code><i>seconds</i><code>]</code></p>
<dd> The <font SIZE="-1">TCP</font> Net Console has two modes of operation. It can send the serial I/O to a location or wait for a connection from a location. By default the <font SIZE="-1">TCP</font> Net Console is sent to <i>host</i> at the <i>port</i>. If you use the <i>server</i> option <font SIZE="-1">QEMU</font> will wait for a client socket application to connect to the port before continuing, unless the <tt>&quot;nowait&quot;</tt> option was specified. The <tt>&quot;nodelay&quot;</tt> option disables the Nagle buffering algorithm. The <tt>&quot;reconnect&quot;</tt> option only applies if <i>noserver</i> is set, if the connection goes down it will attempt to reconnect at the given interval. If <i>host</i> is omitted, 0.0.0.0 is assumed. Only one <font SIZE="-1">TCP</font> connection at a time is accepted. You can use <tt>&quot;telnet&quot;</tt> to connect to the corresponding character device.</p>
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
<dt><code>websocket:</code><i>host</i><code>:</code><i>port</i><code>,server[,nowait][,nodelay]</code></p>
<dd> The WebSocket protocol is used instead of raw tcp socket. The port acts as a WebSocket server. Client mode is not supported.</p>
<dt><code>unix:</code><i>path</i><code>[,server][,nowait][,reconnect=</code><i>seconds</i><code>]</code></p>
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
<dt><code>-qmp-pretty</code> <i>dev</i></p>
<dd> Like -qmp but uses pretty <font SIZE="-1">JSON</font> formatting.</p>
<dt><code>-mon [chardev=]name[,mode=readline|control][,pretty[=on|off]]</code></p>
<dd> Setup monitor on chardev <i>name</i>. <tt>&quot;pretty&quot;</tt> turns on <font SIZE="-1">JSON</font> pretty printing easing human reading and debugging.</p>
<dt><code>-debugcon</code> <i>dev</i></p>
<dd> Redirect the debug console to host device <i>dev</i> (same devices as the serial port). The debug console is an I/O port which is typically port 0xe9; writing to that I/O port sends output to this device. The default device is <tt>&quot;vc&quot;</tt> in graphical mode and <tt>&quot;stdio&quot;</tt> in non graphical mode.</p>
<dt><code>-pidfile</code> <i>file</i></p>
<dd> Store the <font SIZE="-1">QEMU</font> process <font SIZE="-1">PID</font> in <i>file</i>. It is useful if you launch <font SIZE="-1">QEMU</font> from a script.</p>
<dt><code>-singlestep</code></p>
<dd> Run the emulation in single step mode.</p>
<dt><code>&#8211;preconfig</code></p>
<dd> Pause <font SIZE="-1">QEMU</font> for interactive configuration before the machine is created, which allows querying and configuring properties that will affect machine initialization. Use <font SIZE="-1">QMP</font> command &#8216;x-exit-preconfig&#8217; to exit the preconfig state and move to the next state (i.e. run guest if -S isn&#8217;t used or pause the second time if -S is used). This option is experimental.</p>
<dt><code>-S</code></p>
<dd> Do not start <font SIZE="-1">CPU</font> at startup (you must type &#8216;c&#8217; in the monitor).</p>
<dt><code>-realtime mlock=on|off</code></p>
<dd> Run qemu with realtime features. mlocking qemu and guest memory can be enabled via <code>mlock=on</code> (enabled by default).</p>
<dt><code>-overcommit mem-lock=on|off</code></p>
<dd>
<dt><code>-overcommit cpu-pm=on|off</code></p>
<dd> Run qemu with hints about host resource overcommit. The default is to assume that host overcommits all resources. </p>
<p> Locking qemu and guest memory can be enabled via <code>mem-lock=on</code> (disabled by default). This works when host memory is not overcommitted and reduces the worst-case latency for guest. This is equivalent to <code>realtime</code>. </p>
<p> Guest ability to manage power state of host cpus (increasing latency for other processes on the same host cpu, but decreasing latency for guest) can be enabled via <code>cpu-pm=on</code> (disabled by default). This works best when host <font SIZE="-1">CPU</font> is not overcommitted. When used, host estimates of <font SIZE="-1">CPU</font> cycle and power utilization will be incorrect, not taking into account guest idle time.</p>
<dt><code>-gdb</code> <i>dev</i></p>
<dd> Wait for gdb connection on device <i>dev</i>. Typical connections will likely be TCP-based, but also <font SIZE="-1">UDP,</font> pseudo <font SIZE="-1">TTY,</font> or even stdio are reasonable use case. The latter is allowing to start <font SIZE="-1">QEMU</font> from within gdb and establish the connection via a pipe: </p>
<pre>
        (gdb) target remote | exec qemu-system-x86_64 -gdb stdio ...
</pre>
<dt><code>-s</code></p>
<dd> Shorthand for -gdb tcp::1234, i.e. open a gdbserver on <font SIZE="-1">TCP</font> port 1234.</p>
<dt><code>-d</code> <i>item1</i><code>[,&#8230;]</code></p>
<dd> Enable logging of specified items. Use &#8216;-d help&#8217; for a list of log items.</p>
<dt><code>-D</code> <i>logfile</i></p>
<dd> Output log in <i>logfile</i> instead of to stderr</p>
<dt><code>-dfilter</code> <i>range1</i><code>[,&#8230;]</code></p>
<dd> Filter debug output to that relevant to a range of target addresses. The filter spec can be either <i>start</i>+<i>size</i>, <i>start</i>&#8211;<i>size</i> or <i>start</i>..<i>end</i> where <i>start</i> <i>end</i> and <i>size</i> are the addresses and sizes required. For example: </p>
<pre>
        -dfilter 0x8000..0x8fff,0xffffffc000080000+0x200,0xffffffc000060000-0x1000
</pre>
<p> Will dump output for any code in the 0x1000 sized block starting at 0x8000 and the 0x200 sized block starting at 0xffffffc000080000 and another 0x1000 sized block starting at 0xffffffc00005f000.</p>
<dt><code>-seed</code> <i>number</i></p>
<dd> Force the guest to use a deterministic pseudo-random number generator, seeded with <i>number</i>. This does not affect crypto routines within the host.</p>
<dt><code>-L</code> <i>path</i></p>
<dd> Set the directory for the <font SIZE="-1">BIOS, VGA BIOS</font> and keymaps. </p>
<p> To list all the data directories, use <tt>&quot;-L help&quot;</tt>.</p>
<dt><code>-bios</code> <i>file</i></p>
<dd> Set the filename for the <font SIZE="-1">BIOS.</font></p>
<dt><code>-enable-kvm</code></p>
<dd> Enable <font SIZE="-1">KVM</font> full virtualization support. This option is only available if <font SIZE="-1">KVM</font> support is enabled when compiling.</p>
<dt><code>-xen-domid</code> <i>id</i></p>
<dd> Specify xen guest domain <i>id</i> (<font SIZE="-1">XEN</font> only).</p>
<dt><code>-xen-attach</code></p>
<dd> Attach to existing xen domain. libxl will use this when starting <font SIZE="-1">QEMU</font> (<font SIZE="-1">XEN</font> only). Restrict set of available xen operations to specified domain id (<font SIZE="-1">XEN</font> only).</p>
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
<dt><code>-rtc [base=utc|localtime|</code><i>datetime</i><code>][,clock=host|rt|vm][,driftfix=none|slew]</code></p>
<dd> Specify <code>base</code> as <tt>&quot;utc&quot;</tt> or <tt>&quot;localtime&quot;</tt> to let the <font SIZE="-1">RTC</font> start at the current <font SIZE="-1">UTC</font> or local time, respectively. <tt>&quot;localtime&quot;</tt> is required for correct date in MS-DOS or Windows. To start at a specific point in time, provide <i>datetime</i> in the format <tt>&quot;2006-06-17T16:01:21&quot;</tt> or <tt>&quot;2006-06-17&quot;</tt>. The default base is <font SIZE="-1">UTC.</font> </p>
<p> By default the <font SIZE="-1">RTC</font> is driven by the host system time. This allows using of the <font SIZE="-1">RTC</font> as accurate reference clock inside the guest, specifically if the host time is smoothly following an accurate external reference clock, e.g. via <font SIZE="-1">NTP.</font> If you want to isolate the guest time from the host, you can set <code>clock</code> to <tt>&quot;rt&quot;</tt> instead, which provides a host monotonic clock if host support it. To even prevent the <font SIZE="-1">RTC</font> from progressing during suspension, you can set <code>clock</code> to <tt>&quot;vm&quot;</tt> (virtual clock). <code>clock=vm</code> is recommended especially in icount mode in order to preserve determinism; however, note that in icount mode the speed of the virtual clock is variable and can in general differ from the host clock. </p>
<p> Enable <code>driftfix</code> (i386 targets only) if you experience time drift problems, specifically with Windows&#8217; <font SIZE="-1">ACPI HAL.</font> This option will try to figure out how many timer interrupts were not processed by the Windows guest and will re-inject them.</p>
<dt><code>-icount [shift=</code><i>N</i><code>|auto][,rr=record|replay,rrfile=</code><i>filename</i><code>,rrsnapshot=</code><i>snapshot</i><code>]</code></p>
<dd> Enable virtual instruction counter. The virtual cpu will execute one instruction every 2^<i>N</i> ns of virtual time. If <tt>&quot;auto&quot;</tt> is specified then the virtual cpu speed will be automatically adjusted to keep virtual time within a few seconds of real time. </p>
<p> When the virtual cpu is sleeping, the virtual time will advance at default speed unless <code>sleep=on|off</code> is specified. With <code>sleep=on|off</code>, the virtual time will jump to the next timer deadline instantly whenever the virtual cpu goes to sleep mode and will not advance if no timer is enabled. This behavior give deterministic execution times from the guest point of view. </p>
<p> Note that while this option can give deterministic behavior, it does not provide cycle accurate emulation. Modern CPUs contain superscalar out of order cores with complex cache hierarchies. The number of instructions executed often has little or no correlation with actual performance. </p>
<p> <code>align=on</code> will activate the delay algorithm which will try to synchronise the host clock and the virtual clock. The goal is to have a guest running at the real frequency imposed by the shift option. Whenever the guest clock is behind the host clock and if <code>align=on</code> is specified then we print a message to the user to inform about the delay. Currently this option does not work when <code>shift</code> is <tt>&quot;auto&quot;</tt>. Note: The sync algorithm will work for those shift values for which the guest clock runs ahead of the host clock. Typically this happens when the shift value is high (how high depends on the host machine). </p>
<p> When <code>rr</code> option is specified deterministic record/replay is enabled. Replay log is written into <i>filename</i> file in record mode and read from this file in replay mode. </p>
<p> Option rrsnapshot is used to create new vm snapshot named <i>snapshot</i> at the start of execution recording. In replay mode this option is used to load the initial <font SIZE="-1">VM</font> state.</p>
<dt><code>-watchdog</code> <i>model</i></p>
<dd> Create a virtual hardware watchdog device. Once enabled (by a guest action), the watchdog must be periodically polled by an agent inside the guest or else the guest will be restarted. Choose a model for which your guest has drivers. </p>
<p> The <i>model</i> is the model of hardware watchdog to emulate. Use <tt>&quot;-watchdog help&quot;</tt> to list available hardware models. Only one watchdog can be enabled for a guest. </p>
<p> The following models may be available:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>ib700</code></p>
<dd> iBASE 700 is a very simple <font SIZE="-1">ISA</font> watchdog with a single timer.</p>
<dt><code>i6300esb</code></p>
<dd> Intel 6300ESB I/O controller hub is a much more featureful PCI-based dual-timer watchdog.</p>
<dt><code>diag288</code></p>
<dd> A virtual watchdog for s390x backed by the diagnose 288 hypercall (currently <font SIZE="-1">KVM</font> only).</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-watchdog-action</code> <i>action</i></p>
<dd> The <i>action</i> controls what <font SIZE="-1">QEMU</font> will do when the watchdog timer expires. The default is <tt>&quot;reset&quot;</tt> (forcefully reset the guest). Other possible actions are: <tt>&quot;shutdown&quot;</tt> (attempt to gracefully shutdown the guest), <tt>&quot;poweroff&quot;</tt> (forcefully poweroff the guest), <tt>&quot;inject-nmi&quot;</tt> (inject a <font SIZE="-1">NMI</font> into the guest), <tt>&quot;pause&quot;</tt> (pause the guest), <tt>&quot;debug&quot;</tt> (print a debug message and continue), or <tt>&quot;none&quot;</tt> (do nothing). </p>
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
<dt><code>-show-cursor</code></p>
<dd> Show cursor.</p>
<dt><code>-tb-size</code> <i>n</i></p>
<dd> Set <font SIZE="-1">TB</font> size.</p>
<dt><code>-incoming tcp:[</code><i>host</i><code>]:</code><i>port</i><code>[,to=</code><i>maxport</i><code>][,ipv4][,ipv6]</code></p>
<dd>
<dt><code>-incoming rdma:</code><i>host</i><code>:</code><i>port</i><code>[,ipv4][,ipv6]</code></p>
<dd> Prepare for incoming migration, listen on a given tcp port.</p>
<dt><code>-incoming unix:</code><i>socketpath</i></p>
<dd> Prepare for incoming migration, listen on a given unix socket.</p>
<dt><code>-incoming fd:</code><i>fd</i></p>
<dd> Accept incoming migration from a given filedescriptor.</p>
<dt><code>-incoming exec:</code><i>cmdline</i></p>
<dd> Accept incoming migration as an output from specified external command.</p>
<dt><code>-incoming defer</code></p>
<dd> Wait for the <font SIZE="-1">URI</font> to be specified via migrate_incoming. The monitor can be used to change settings (such as migration parameters) prior to issuing the migrate_incoming to allow the migration to begin.</p>
<dt><code>-only-migratable</code></p>
<dd> Only allow migratable devices. Devices will not be allowed to enter an unmigratable state.</p>
<dt><code>-nodefaults</code></p>
<dd> Don&#8217;t create default devices. Normally, <font SIZE="-1">QEMU</font> sets the default devices like serial port, parallel port, virtual console, monitor device, <font SIZE="-1">VGA</font> adapter, floppy and CD-ROM drive and others. The <tt>&quot;-nodefaults&quot;</tt> option will disable all those default devices.</p>
<dt><code>-chroot</code> <i>dir</i></p>
<dd> Immediately before starting guest execution, chroot to the specified directory. Especially useful in combination with -runas.</p>
<dt><code>-runas</code> <i>user</i></p>
<dd> Immediately before starting guest execution, drop root privileges, switching to the specified user.</p>
<dt><code>-prom-env</code> <i>variable</i><code>=</code><i>value</i></p>
<dd> Set OpenBIOS nvram <i>variable</i> to given <i>value</i> (<font SIZE="-1">PPC, SPARC</font> only).</p>
<dt><code>-semihosting</code></p>
<dd> Enable semihosting mode (<font SIZE="-1">ARM, M68K,</font> Xtensa, <font SIZE="-1">MIPS,</font> Nios <font SIZE="-1">II</font> only).</p>
<dt><code>-semihosting-config [enable=on|off][,target=native|gdb|auto][,chardev=id][,arg=str[,&#8230;]]</code></p>
<dd> Enable and configure semihosting (<font SIZE="-1">ARM, M68K,</font> Xtensa, <font SIZE="-1">MIPS,</font> Nios <font SIZE="-1">II</font> only).</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>target=</code>&quot;native|gdb|auto&quot;</p>
<dd> Defines where the semihosting calls will be addressed, to <font SIZE="-1">QEMU</font> (<tt>&quot;native&quot;</tt>) or to <font SIZE="-1">GDB</font> (<tt>&quot;gdb&quot;</tt>). The default is <tt>&quot;auto&quot;</tt>, which means <tt>&quot;gdb&quot;</tt> during debug sessions and <tt>&quot;native&quot;</tt> otherwise.</p>
<dt><code>chardev=</code><i>str1</i></p>
<dd> Send the output to a chardev backend output for native or auto output when not in gdb</p>
<dt><code>arg=</code><i>str1</i><code>,arg=</code><i>str2</i><code>,&#8230;</code></p>
<dd> Allows the user to pass input arguments, and can be used multiple times to build up a list. The old-style <tt>&quot;-kernel&quot;</tt>/<tt>&quot;-append&quot;</tt> method of passing a command line is still supported for backward compatibility. If both the <tt>&quot;--semihosting-config arg&quot;</tt> and the <tt>&quot;-kernel&quot;</tt>/<tt>&quot;-append&quot;</tt> are specified, the former is passed to semihosting as it always takes precedence.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-old-param</code></p>
<dd> Old param mode (<font SIZE="-1">ARM</font> only).</p>
<dt><code>-sandbox</code> <i>arg</i><code>[,obsolete=</code><i>string</i><code>][,elevateprivileges=</code><i>string</i><code>][,spawn=</code><i>string</i><code>][,resourcecontrol=</code><i>string</i><code>]</code></p>
<dd> Enable Seccomp mode 2 system call filter. &#8216;on&#8217; will enable syscall filtering and &#8216;off&#8217; will disable it. The default is &#8216;off&#8217;.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>obsolete=</code><i>string</i></p>
<dd> Enable Obsolete system calls</p>
<dt><code>elevateprivileges=</code><i>string</i></p>
<dd> Disable set*uid|gid system calls</p>
<dt><code>spawn=</code><i>string</i></p>
<dd> Disable *fork and execve</p>
<dt><code>resourcecontrol=</code><i>string</i></p>
<dd> Disable process affinity and schedular priority</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-readconfig</code> <i>file</i></p>
<dd> Read device configuration from <i>file</i>. This approach is useful when you want to spawn <font SIZE="-1">QEMU</font> process with many command line options but you don&#8217;t want to exceed the command line character limit.</p>
<dt><code>-writeconfig</code> <i>file</i></p>
<dd> Write device configuration to <i>file</i>. The <i>file</i> can be either filename to save command line and device configuration into file or dash <tt>&quot;-&quot;</tt>) character to print the output to stdout. This can be later used as input file for <tt>&quot;-readconfig&quot;</tt> option.</p>
<dt><code>-no-user-config</code></p>
<dd> The <tt>&quot;-no-user-config&quot;</tt> option makes <font SIZE="-1">QEMU</font> not load any of the user-provided config files on <i>sysconfdir</i>.</p>
<dt><code>-trace [[enable=]</code><i>pattern</i><code>][,events=</code><i>file</i><code>][,file=</code><i>file</i><code>]</code></p>
<dd> Specify tracing options.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>[enable=]</code><i>pattern</i></p>
<dd> Immediately enable events matching <i>pattern</i> (either event name or a globbing pattern). This option is only available if <font SIZE="-1">QEMU</font> has been compiled with the <i>simple</i>, <i>log</i> or <i>ftrace</i> tracing backend. To specify multiple events or patterns, specify the <code>-trace</code> option multiple times. </p>
<p> Use <tt>&quot;-trace help&quot;</tt> to print a list of names of trace points.</p>
<dt><code>events=</code><i>file</i></p>
<dd> Immediately enable events listed in <i>file</i>. The file must contain one event name (as listed in the <i>trace-events-all</i> file) per line; globbing patterns are accepted too. This option is only available if <font SIZE="-1">QEMU</font> has been compiled with the <i>simple</i>, <i>log</i> or <i>ftrace</i> tracing backend.</p>
<dt><code>file=</code><i>file</i></p>
<dd> Log output traces to <i>file</i>. This option is only available if <font SIZE="-1">QEMU</font> has been compiled with the <i>simple</i> tracing backend.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-plugin file=</code><i>file</i><code>[,arg=</code><i>string</i><code>]</code></p>
<dd> Load a plugin.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>file=</code><i>file</i></p>
<dd> Load the given plugin from a shared library file.</p>
<dt><code>arg=</code><i>string</i></p>
<dd> Argument string passed to the plugin. (Can be given multiple times.)</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-enable-fips</code></p>
<dd> Enable <font SIZE="-1">FIPS 140-2</font> compliance mode.</p>
<dt><code>-msg timestamp[=on|off]</code></p>
<dd> prepend a timestamp to each log message.(default:on)</p>
<dt><code>-dump-vmstate</code> <i>file</i></p>
<dd> Dump json-encoded vmstate information for current machine type to file in <i>file</i></p>
<dt><code>-enable-sync-profile</code></p>
<dd> Enable synchronization profiling.</dl>
<p> <i>Generic object creation</i></p>
<dl>
<dt><code>-object</code> <i>typename</i><code>[,</code><i>prop1</i><code>=</code><i>value1</i><code>,&#8230;]</code></p>
<dd> Create a new object of type <i>typename</i> setting properties in the order they are specified. Note that the &#8216;id&#8217; property must be set. These objects are placed in the &#8216;/objects&#8217; path.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-object memory-backend-file,id=</code><i>id</i><code>,size=</code><i>size</i><code>,mem-path=</code><i>dir</i><code>,share=</code><i>on|off</i><code>,discard-data=</code><i>on|off</i><code>,merge=</code><i>on|off</i><code>,dump=</code><i>on|off</i><code>,prealloc=</code><i>on|off</i><code>,host-nodes=</code><i>host-nodes</i><code>,policy=</code><i>default|preferred|bind|interleave</i><code>,align=</code><i>align</i></p>
<dd> Creates a memory file backend object, which can be used to back the guest <font SIZE="-1">RAM</font> with huge pages. </p>
<p> The <code>id</code> parameter is a unique <font SIZE="-1">ID</font> that will be used to reference this memory region when configuring the <code>-numa</code> argument. </p>
<p> The <code>size</code> option provides the size of the memory region, and accepts common suffixes, eg <code>500M</code>. </p>
<p> The <code>mem-path</code> provides the path to either a shared memory or huge page filesystem mount. </p>
<p> The <code>share</code> boolean option determines whether the memory region is marked as private to <font SIZE="-1">QEMU,</font> or shared. The latter allows a co-operating external process to access the <font SIZE="-1">QEMU</font> memory region. </p>
<p> The <code>share</code> is also required for pvrdma devices due to limitations in the <font SIZE="-1">RDMA API</font> provided by Linux. </p>
<p> Setting share=on might affect the ability to configure <font SIZE="-1">NUMA</font> bindings for the memory backend under some circumstances, see Documentation/vm/numa_memory_policy.txt on the Linux kernel source tree for additional details. </p>
<p> Setting the <code>discard-data</code> boolean option to <i>on</i> indicates that file contents can be destroyed when <font SIZE="-1">QEMU</font> exits, to avoid unnecessarily flushing data to the backing file. Note that <code>discard-data</code> is only an optimization, and <font SIZE="-1">QEMU</font> might not discard file contents if it aborts unexpectedly or is terminated using <font SIZE="-1">SIGKILL.</font> </p>
<p> The <code>merge</code> boolean option enables memory merge, also known as <font SIZE="-1">MADV_MERGEABLE,</font> so that Kernel Samepage Merging will consider the pages for memory deduplication. </p>
<p> Setting the <code>dump</code> boolean option to <i>off</i> excludes the memory from core dumps. This feature is also known as <font SIZE="-1">MADV_DONTDUMP.</font> </p>
<p> The <code>prealloc</code> boolean option enables memory preallocation. </p>
<p> The <code>host-nodes</code> option binds the memory range to a list of <font SIZE="-1">NUMA</font> host nodes. </p>
<p> The <code>policy</code> option sets the <font SIZE="-1">NUMA</font> policy to one of the following values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>default</i></p>
<dd> default host policy</p>
<dt><i>preferred</i></p>
<dd> prefer the given host node list for allocation</p>
<dt><i>bind</i></p>
<dd> restrict memory allocation to the given host node list</p>
<dt><i>interleave</i></p>
<dd> interleave memory allocations across the given host node list</dl>
</dl>
<dl>
<dt>
<dd>
<p> The <code>align</code> option specifies the base address alignment when <font SIZE="-1">QEMU</font> <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) <code>mem-path</code>, and accepts common suffixes, eg <code>2M</code>. Some backend store specified by <code>mem-path</code> requires an alignment different than the default one used by <font SIZE="-1">QEMU,</font> eg the device <font SIZE="-1">DAX</font> /dev/dax0.0 requires 2M alignment rather than 4K. In such cases, users can specify the required alignment via this option. </p>
<p> The <code>pmem</code> option specifies whether the backing file specified by <code>mem-path</code> is in host persistent memory that can be accessed using the <font SIZE="-1">SNIA NVM</font> programming model (e.g. Intel <font SIZE="-1">NVDIMM</font>). If <code>pmem</code> is set to &#8216;on&#8217;, <font SIZE="-1">QEMU</font> will take necessary operations to guarantee the persistence of its own writes to <code>mem-path</code> (e.g. in vNVDIMM label emulation and live migration). Also, we will map the backend-file with <font SIZE="-1">MAP_SYNC</font> flag, which ensures the file metadata is in sync for <code>mem-path</code> in case of host crash or a power failure. <font SIZE="-1">MAP_SYNC</font> requires support from both the host kernel (since Linux kernel 4.15) and the filesystem of <code>mem-path</code> mounted with <font SIZE="-1">DAX</font> option.</dl>
<dt><code>-object memory-backend-ram,id=</code><i>id</i><code>,merge=</code><i>on|off</i><code>,dump=</code><i>on|off</i><code>,share=</code><i>on|off</i><code>,prealloc=</code><i>on|off</i><code>,size=</code><i>size</i><code>,host-nodes=</code><i>host-nodes</i><code>,policy=</code><i>default|preferred|bind|interleave</i></p>
<dd> Creates a memory backend object, which can be used to back the guest <font SIZE="-1">RAM.</font> Memory backend objects offer more control than the <code>-m</code> option that is traditionally used to define guest <font SIZE="-1">RAM.</font> Please refer to <code>memory-backend-file</code> for a description of the options.</p>
<dt><code>-object memory-backend-memfd,id=</code><i>id</i><code>,merge=</code><i>on|off</i><code>,dump=</code><i>on|off</i><code>,share=</code><i>on|off</i><code>,prealloc=</code><i>on|off</i><code>,size=</code><i>size</i><code>,host-nodes=</code><i>host-nodes</i><code>,policy=</code><i>default|preferred|bind|interleave</i><code>,seal=</code><i>on|off</i><code>,hugetlb=</code><i>on|off</i><code>,hugetlbsize=</code><i>size</i></p>
<dd> Creates an anonymous memory file backend object, which allows <font SIZE="-1">QEMU</font> to share the memory with an external process (e.g. when using vhost-user). The memory is allocated with memfd and optional sealing. (Linux only) </p>
<p> The <code>seal</code> option creates a sealed-file, that will block further resizing the memory (&#8216;on&#8217; by default). </p>
<p> The <code>hugetlb</code> option specify the file to be created resides in the hugetlbfs filesystem (since Linux 4.14). Used in conjunction with the <code>hugetlb</code> option, the <code>hugetlbsize</code> option specify the hugetlb page size on systems that support multiple hugetlb page sizes (it must be a power of 2 value supported by the system). </p>
<p> In some versions of Linux, the <code>hugetlb</code> option is incompatible with the <code>seal</code> option (requires at least Linux 4.16). </p>
<p> Please refer to <code>memory-backend-file</code> for a description of the other options. </p>
<p> The <code>share</code> boolean option is <i>on</i> by default with memfd.</p>
<dt><code>-object rng-builtin,id=</code><i>id</i></p>
<dd> Creates a random number generator backend which obtains entropy from <font SIZE="-1">QEMU</font> builtin functions. The <code>id</code> parameter is a unique <font SIZE="-1">ID</font> that will be used to reference this entropy backend from the <code>virtio-rng</code> device. By default, the <code>virtio-rng</code> device uses this <font SIZE="-1">RNG</font> backend.</p>
<dt><code>-object rng-random,id=</code><i>id</i><code>,filename=</code><i>/dev/random</i></p>
<dd> Creates a random number generator backend which obtains entropy from a device on the host. The <code>id</code> parameter is a unique <font SIZE="-1">ID</font> that will be used to reference this entropy backend from the <code>virtio-rng</code> device. The <code>filename</code> parameter specifies which file to obtain entropy from and if omitted defaults to <code>/dev/urandom</code>.</p>
<dt><code>-object rng-egd,id=</code><i>id</i><code>,chardev=</code><i>chardevid</i></p>
<dd> Creates a random number generator backend which obtains entropy from an external daemon running on the host. The <code>id</code> parameter is a unique <font SIZE="-1">ID</font> that will be used to reference this entropy backend from the <code>virtio-rng</code> device. The <code>chardev</code> parameter is the unique <font SIZE="-1">ID</font> of a character device backend that provides the connection to the <font SIZE="-1">RNG</font> daemon.</p>
<dt><code>-object tls-creds-anon,id=</code><i>id</i><code>,endpoint=</code><i>endpoint</i><code>,dir=</code><i>/path/to/cred/dir</i><code>,verify-peer=</code><i>on|off</i></p>
<dd> Creates a <font SIZE="-1">TLS</font> anonymous credentials object, which can be used to provide <font SIZE="-1">TLS</font> support on network backends. The <code>id</code> parameter is a unique <font SIZE="-1">ID</font> which network backends will use to access the credentials. The <code>endpoint</code> is either <code>server</code> or <code>client</code> depending on whether the <font SIZE="-1">QEMU</font> network backend that uses the credentials will be acting as a client or as a server. If <code>verify-peer</code> is enabled (the default) then once the handshake is completed, the peer credentials will be verified, though this is a no-op for anonymous credentials. </p>
<p> The <i>dir</i> parameter tells <font SIZE="-1">QEMU</font> where to find the credential files. For server endpoints, this directory may contain a file <i>dh-params.pem</i> providing diffie-hellman parameters to use for the <font SIZE="-1">TLS</font> server. If the file is missing, <font SIZE="-1">QEMU</font> will generate a set of <font SIZE="-1">DH</font> parameters at startup. This is a computationally expensive operation that consumes random pool entropy, so it is recommended that a persistent set of parameters be generated upfront and saved.</p>
<dt><code>-object tls-creds-psk,id=</code><i>id</i><code>,endpoint=</code><i>endpoint</i><code>,dir=</code><i>/path/to/keys/dir</i><code>[,username=</code><i>username</i><code>]</code></p>
<dd> Creates a <font SIZE="-1">TLS</font> Pre-Shared Keys (<font SIZE="-1">PSK</font>) credentials object, which can be used to provide <font SIZE="-1">TLS</font> support on network backends. The <code>id</code> parameter is a unique <font SIZE="-1">ID</font> which network backends will use to access the credentials. The <code>endpoint</code> is either <code>server</code> or <code>client</code> depending on whether the <font SIZE="-1">QEMU</font> network backend that uses the credentials will be acting as a client or as a server. For clients only, <code>username</code> is the username which will be sent to the server. If omitted it defaults to &#8220;qemu&#8221;. </p>
<p> The <i>dir</i> parameter tells <font SIZE="-1">QEMU</font> where to find the keys file. It is called &quot;<i>dir</i>/keys.psk&#8220; and contains &#8221;username:key&quot; pairs. This file can most easily be created using the GnuTLS <tt>&quot;psktool&quot;</tt> program. </p>
<p> For server endpoints, <i>dir</i> may also contain a file <i>dh-params.pem</i> providing diffie-hellman parameters to use for the <font SIZE="-1">TLS</font> server. If the file is missing, <font SIZE="-1">QEMU</font> will generate a set of <font SIZE="-1">DH</font> parameters at startup. This is a computationally expensive operation that consumes random pool entropy, so it is recommended that a persistent set of parameters be generated up front and saved.</p>
<dt><code>-object tls-creds-x509,id=</code><i>id</i><code>,endpoint=</code><i>endpoint</i><code>,dir=</code><i>/path/to/cred/dir</i><code>,priority=</code><i>priority</i><code>,verify-peer=</code><i>on|off</i><code>,passwordid=</code><i>id</i></p>
<dd> Creates a <font SIZE="-1">TLS</font> anonymous credentials object, which can be used to provide <font SIZE="-1">TLS</font> support on network backends. The <code>id</code> parameter is a unique <font SIZE="-1">ID</font> which network backends will use to access the credentials. The <code>endpoint</code> is either <code>server</code> or <code>client</code> depending on whether the <font SIZE="-1">QEMU</font> network backend that uses the credentials will be acting as a client or as a server. If <code>verify-peer</code> is enabled (the default) then once the handshake is completed, the peer credentials will be verified. With x509 certificates, this implies that the clients must be provided with valid client certificates too. </p>
<p> The <i>dir</i> parameter tells <font SIZE="-1">QEMU</font> where to find the credential files. For server endpoints, this directory may contain a file <i>dh-params.pem</i> providing diffie-hellman parameters to use for the <font SIZE="-1">TLS</font> server. If the file is missing, <font SIZE="-1">QEMU</font> will generate a set of <font SIZE="-1">DH</font> parameters at startup. This is a computationally expensive operation that consumes random pool entropy, so it is recommended that a persistent set of parameters be generated upfront and saved. </p>
<p> For x509 certificate credentials the directory will contain further files providing the x509 certificates. The certificates must be stored in <font SIZE="-1">PEM</font> format, in filenames <i>ca-cert.pem</i>, <i>ca-crl.pem</i> (optional), <i>server-cert.pem</i> (only servers), <i>server-key.pem</i> (only servers), <i>client-cert.pem</i> (only clients), and <i>client-key.pem</i> (only clients). </p>
<p> For the <i>server-key.pem</i> and <i>client-key.pem</i> files which contain sensitive private keys, it is possible to use an encrypted version by providing the <i>passwordid</i> parameter. This provides the <font SIZE="-1">ID</font> of a previously created <tt>&quot;secret&quot;</tt> object containing the password for decryption. </p>
<p> The <i>priority</i> parameter allows to override the global default priority used by gnutls. This can be useful if the system administrator needs to use a weaker set of crypto priorities for <font SIZE="-1">QEMU</font> without potentially forcing the weakness onto all applications. Or conversely if one wants wants a stronger default for <font SIZE="-1">QEMU</font> than for all other applications, they can do this through this parameter. Its format is a gnutls priority string as described at &lt;<code><a rel="nofollow" href="https://gnutls.org/manual/html_node/Priority-Strings.html">https://gnutls.org/manual/html_node/Priority-Strings.html</a></code>&gt;.</p>
<dt><code>-object filter-buffer,id=</code><i>id</i><code>,netdev=</code><i>netdevid</i><code>,interval=</code><i>t</i><code>[,queue=</code><i>all|rx|tx</i><code>][,status=</code><i>on|off</i><code>]</code></p>
<dd> Interval <i>t</i> can&#8217;t be 0, this filter batches the packet delivery: all packets arriving in a given interval on netdev <i>netdevid</i> are delayed until the end of the interval. Interval is in microseconds. <code>status</code> is optional that indicate whether the netfilter is on (enabled) or off (disabled), the default status for netfilter will be &#8216;on&#8217;. </p>
<p> queue <i>all|rx|tx</i> is an option that can be applied to any netfilter. </p>
<p> <code>all</code>: the filter is attached both to the receive and the transmit queue of the netdev (default). </p>
<p> <code>rx</code>: the filter is attached to the receive queue of the netdev, where it will receive packets sent to the netdev. </p>
<p> <code>tx</code>: the filter is attached to the transmit queue of the netdev, where it will receive packets sent by the netdev.</p>
<dt><code>-object filter-mirror,id=</code><i>id</i><code>,netdev=</code><i>netdevid</i><code>,outdev=</code><i>chardevid</i><code>,queue=</code><i>all|rx|tx</i><code>[,vnet_hdr_support]</code></p>
<dd> filter-mirror on netdev <i>netdevid</i>,mirror net packet to chardev<i>chardevid</i>, if it has the vnet_hdr_support flag, filter-mirror will mirror packet with vnet_hdr_len.</p>
<dt><code>-object filter-redirector,id=</code><i>id</i><code>,netdev=</code><i>netdevid</i><code>,indev=</code><i>chardevid</i><code>,outdev=</code><i>chardevid</i><code>,queue=</code><i>all|rx|tx</i><code>[,vnet_hdr_support]</code></p>
<dd> filter-redirector on netdev <i>netdevid</i>,redirect filter&#8217;s net packet to chardev <i>chardevid</i>,and redirect indev&#8217;s packet to filter.if it has the vnet_hdr_support flag, filter-redirector will redirect packet with vnet_hdr_len. Create a filter-redirector we need to differ outdev id from indev id, id can not be the same. we can just use indev or outdev, but at least one of indev or outdev need to be specified.</p>
<dt><code>-object filter-rewriter,id=</code><i>id</i><code>,netdev=</code><i>netdevid</i><code>,queue=</code><i>all|rx|tx</i><code>,[vnet_hdr_support]</code></p>
<dd> Filter-rewriter is a part of <font SIZE="-1">COLO</font> project.It will rewrite tcp packet to secondary from primary to keep secondary tcp connection,and rewrite tcp packet to primary from secondary make tcp packet can be handled by client.if it has the vnet_hdr_support flag, we can parse packet with vnet header. </p>
<p> usage: colo secondary: -object filter-redirector,id=f1,netdev=hn0,queue=tx,indev=red0 -object filter-redirector,id=f2,netdev=hn0,queue=rx,outdev=red1 -object filter-rewriter,id=rew0,netdev=hn0,queue=all</p>
<dt><code>-object filter-dump,id=</code><i>id</i><code>,netdev=</code><i>dev</i><code>[,file=</code><i>filename</i><code>][,maxlen=</code><i>len</i><code>]</code></p>
<dd> Dump the network traffic on netdev <i>dev</i> to the file specified by <i>filename</i>. At most <i>len</i> bytes (64k by default) per packet are stored. The file format is libpcap, so it can be analyzed with tools such as tcpdump or Wireshark.</p>
<dt><code>-object colo-compare,id=</code><i>id</i><code>,primary_in=</code><i>chardevid</i><code>,secondary_in=</code><i>chardevid</i><code>,outdev=</code><i>chardevid</i><code>,iothread=</code><i>id</i><code>[,vnet_hdr_support][,notify_dev=</code><i>id</i><code>]</code></p>
<dd> Colo-compare gets packet from primary_in<i>chardevid</i> and secondary_in<i>chardevid</i>, than compare primary packet with secondary packet. If the packets are same, we will output primary packet to outdev<i>chardevid</i>, else we will notify colo-frame do checkpoint and send primary packet to outdev<i>chardevid</i>. In order to improve efficiency, we need to put the task of comparison in another thread. If it has the vnet_hdr_support flag, colo compare will send/recv packet with vnet_hdr_len. If you want to use Xen <font SIZE="-1">COLO,</font> will need the notify_dev to notify Xen colo-frame to do checkpoint. </p>
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
<dt><code>-object cryptodev-backend-builtin,id=</code><i>id</i><code>[,queues=</code><i>queues</i><code>]</code></p>
<dd> Creates a cryptodev backend which executes crypto opreation from the <font SIZE="-1">QEMU</font> cipher <font SIZE="-1">APIS.</font> The <i>id</i> parameter is a unique <font SIZE="-1">ID</font> that will be used to reference this cryptodev backend from the <code>virtio-crypto</code> device. The <i>queues</i> parameter is optional, which specify the queue number of cryptodev backend, the default of <i>queues</i> is 1. </p>
<pre><code>
#qemu - system - x86_64[...] - object cryptodev - backend - builtin, id = cryptodev0 - device virtio - crypto - pci, id = crypto0, cryptodev = cryptodev0[...]
</code></pre>
<dt><code>-object cryptodev-vhost-user,id=</code><i>id</i><code>,chardev=</code><i>chardevid</i><code>[,queues=</code><i>queues</i><code>]</code></p>
<dd> Creates a vhost-user cryptodev backend, backed by a chardev <i>chardevid</i>. The <i>id</i> parameter is a unique <font SIZE="-1">ID</font> that will be used to reference this cryptodev backend from the <code>virtio-crypto</code> device. The chardev should be a unix domain socket backed one. The vhost-user uses a specifically defined protocol to pass vhost ioctl replacement messages to an application on the other end of the socket. The <i>queues</i> parameter is optional, which specify the queue number of cryptodev backend for multiqueue vhost-user, the default of <i>queues</i> is 1. </p>
<p>#qemu &#8211; system &#8211; x86_64[&#8230;] &#8211; chardev socket, id = chardev0, path = / path / to / socket &#8211; object cryptodev &#8211; vhost &#8211; user, id = cryptodev0, chardev = chardev0 &#8211; device virtio &#8211; crypto &#8211; pci, id = crypto0, cryptodev = cryptodev0[&#8230;]</p>
<dt><code>-object secret,id=</code><i>id</i><code>,data=</code><i>string</i><code>,format=</code><i>raw|base64</i><code>[,keyid=</code><i>secretid</i><code>,iv=</code><i>string</i><code>]</code></p>
<dd>
<dt><code>-object secret,id=</code><i>id</i><code>,file=</code><i>filename</i><code>,format=</code><i>raw|base64</i><code>[,keyid=</code><i>secretid</i><code>,iv=</code><i>string</i><code>]</code></p>
<dd> Defines a secret to store a password, encryption key, or some other sensitive data. The sensitive data can either be passed directly via the <i>data</i> parameter, or indirectly via the <i>file</i> parameter. Using the <i>data</i> parameter is insecure unless the sensitive data is encrypted. </p>
<p> The sensitive data can be provided in raw format (the default), or base64. When encoded as <font SIZE="-1">JSON,</font> the raw format only supports valid <font SIZE="-1">UTF-8</font> characters, so base64 is recommended for sending binary data. <font SIZE="-1">QEMU</font> will convert from which ever format is provided to the format it needs internally. eg, an <font SIZE="-1">RBD</font> password can be provided in raw format, even though it will be base64 encoded when passed onto the <font SIZE="-1">RBD</font> sever. </p>
<p> For added protection, it is possible to encrypt the data associated with a secret using the <font SIZE="-1">AES-256-CBC</font> cipher. Use of encryption is indicated by providing the <i>keyid</i> and <i>iv</i> parameters. The <i>keyid</i> parameter provides the <font SIZE="-1">ID</font> of a previously defined secret that contains the <font SIZE="-1">AES-256</font> decryption key. This key should be 32-bytes long and be base64 encoded. The <i>iv</i> parameter provides the random initialization vector used for encryption of this particular secret and should be a base64 encrypted string of the 16-byte <font SIZE="-1">IV.</font> </p>
<p> The simplest (insecure) usage is to provide the secret inline </p>
<pre>
        # qemu-system-x86_64 -object secret,id=sec0,data=letmein,format=raw
</pre>
<p> The simplest secure usage is to provide the secret via a file </p>
<p> # printf &#8220;letmein&#8221; &gt; mypasswd.txt # qemu-system-x86_64 -object secret,id=sec0,file=mypasswd.txt,format=raw </p>
<p> For greater security, <font SIZE="-1">AES-256-CBC</font> should be used. To illustrate usage, consider the openssl command line tool which can encrypt the data. Note that when encrypting, the plaintext must be padded to the cipher block size (32 bytes) using the standard PKCS#5/6 compatible padding algorithm. </p>
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
<p> When launching <font SIZE="-1">QEMU,</font> create a master secret pointing to <tt>&quot;key.b64&quot;</tt> and specify that to be used to decrypt the user password. Pass the contents of <tt>&quot;iv.b64&quot;</tt> to the second secret </p>
<pre>
        # qemu-system-x86_64 \
        -object secret,id=secmaster0,format=base64,file=key.b64 \
        -object secret,id=sec0,keyid=secmaster0,format=base64,\
        data=$SECRET,iv=$(&lt;iv.b64)
</pre>
<dt><code>-object sev-guest,id=</code><i>id</i><code>,cbitpos=</code><i>cbitpos</i><code>,reduced-phys-bits=</code><i>val</i><code>,[sev-device=</code><i>string</i><code>,policy=</code><i>policy</i><code>,handle=</code><i>handle</i><code>,dh-cert-file=</code><i>file</i><code>,session-file=</code><i>file</i><code>]</code></p>
<dd> Create a Secure Encrypted Virtualization (<font SIZE="-1">SEV</font>) guest object, which can be used to provide the guest memory encryption support on <font SIZE="-1">AMD</font> processors. </p>
<p> When memory encryption is enabled, one of the physical address bit (aka the C-bit) is utilized to mark if a memory page is protected. The <code>cbitpos</code> is used to provide the C-bit position. The C-bit position is Host family dependent hence user must provide this value. On <font SIZE="-1">EPYC,</font> the value should be 47. </p>
<p> When memory encryption is enabled, we loose certain bits in physical address space. The <code>reduced-phys-bits</code> is used to provide the number of bits we loose in physical address space. Similar to C-bit, the value is Host family dependent. On <font SIZE="-1">EPYC,</font> the value should be 5. </p>
<p> The <code>sev-device</code> provides the device file to use for communicating with the <font SIZE="-1">SEV</font> firmware running inside <font SIZE="-1">AMD</font> Secure Processor. The default device is &#8216;/dev/sev&#8217;. If hardware supports memory encryption then /dev/sev devices are created by <font SIZE="-1">CCP</font> driver. </p>
<p> The <code>policy</code> provides the guest policy to be enforced by the <font SIZE="-1">SEV</font> firmware and restrict what configuration and operational commands can be performed on this guest by the hypervisor. The policy should be provided by the guest owner and is bound to the guest and cannot be changed throughout the lifetime of the guest. The default is 0. </p>
<p> If guest <code>policy</code> allows sharing the key with another <font SIZE="-1">SEV</font> guest then <code>handle</code> can be use to provide handle of the guest from which to share the key. </p>
<p> The <code>dh-cert-file</code> and <code>session-file</code> provides the guest owner&#8217;s Public Diffie-Hillman key defined in <font SIZE="-1">SEV</font> spec. The <font SIZE="-1">PDH</font> and session parameters are used for establishing a cryptographic session with the guest owner to negotiate keys used for attestation. The file must be encoded in base64. </p>
<p> e.g to launch a <font SIZE="-1">SEV</font> guest </p>
<pre>
        # qemu-system-x86_64 \
        ......
        -object sev-guest,id=sev0,cbitpos=47,reduced-phys-bits=5 \
        -machine ...,memory-encryption=sev0
        .....
</pre>
<dt><code>-object authz-simple,id=</code><i>id</i><code>,identity=</code><i>string</i></p>
<dd> Create an authorization object that will control access to network services. </p>
<p> The <code>identity</code> parameter is identifies the user and its format depends on the network service that authorization object is associated with. For authorizing based on <font SIZE="-1">TLS</font> x509 certificates, the identity must be the x509 distinguished name. Note that care must be taken to escape any commas in the distinguished name. </p>
<p> An example authorization object to validate a x509 distinguished name would look like: </p>
<pre>
        # qemu-system-x86_64 \
        ...
        -object 'authz-simple,id=auth0,identity=CN=laptop.example.com,,O=Example Org,,L=London,,ST=London,,C=GB' \
        ...
</pre>
<p> Note the use of quotes due to the x509 distinguished name containing whitespace, and escaping of &#8216;,&#8217;.</p>
<dt><code>-object authz-listfile,id=</code><i>id</i><code>,filename=</code><i>path</i><code>,refresh=</code><i>yes|no</i></p>
<dd> Create an authorization object that will control access to network services. </p>
<p> The <code>filename</code> parameter is the fully qualified path to a file containing the access control list rules in <font SIZE="-1">JSON</font> format. </p>
<p> An example set of rules that match against <font SIZE="-1">SASL</font> usernames might look like: </p>
<p>{<br />
    &#8220;rules&#8221; : [<br />
        {&#8220;match&#8221; : &#8220;fred&#8221;, &#8220;policy&#8221; : &#8220;allow&#8221;, &#8220;format&#8221; : &#8220;exact&#8221;},<br />
        {&#8220;match&#8221; : &#8220;bob&#8221;, &#8220;policy&#8221; : &#8220;allow&#8221;, &#8220;format&#8221; : &#8220;exact&#8221;},<br />
        {&#8220;match&#8221; : &#8220;danb&#8221;, &#8220;policy&#8221; : &#8220;deny&#8221;, &#8220;format&#8221; : &#8220;glob&#8221;},<br />
        {&#8220;match&#8221; : &#8220;dan*&#8221;, &#8220;policy&#8221; : &#8220;allow&#8221;, &#8220;format&#8221; : &#8220;exact&#8221;},<br />
    ],<br />
              &#8220;policy&#8221; : &#8220;deny&#8221;<br />
}</p>
<p> When checking access the object will iterate over all the rules and the first rule to match will have its <code>policy</code> value returned as the result. If no rules match, then the default <code>policy</code> value is returned. </p>
<p> The rules can either be an exact string match, or they can use the simple <font SIZE="-1">UNIX</font> glob pattern matching to allow wildcards to be used. </p>
<p> If <code>refresh</code> is set to true the file will be monitored and automatically reloaded whenever its content changes. </p>
<p> As with the <tt>&quot;authz-simple&quot;</tt> object, the format of the identity strings being matched depends on the network service, but is usually a <font SIZE="-1">TLS</font> x509 distinguished name, or a <font SIZE="-1">SASL</font> username. </p>
<p> An example authorization object to validate a <font SIZE="-1">SASL</font> username would look like: </p>
<pre>
        # qemu-system-x86_64 \
        ...
        -object authz-simple,id=auth0,filename=/etc/qemu/vnc-sasl.acl,refresh=yes
        ...
</pre>
<dt><code>-object authz-pam,id=</code><i>id</i><code>,service=</code><i>string</i></p>
<dd> Create an authorization object that will control access to network services. </p>
<p> The <code>service</code> parameter provides the name of a <font SIZE="-1">PAM</font> service to use for authorization. It requires that a file <tt>&quot;/etc/pam.d/</tt>service<tt>&quot;</tt> exist to provide the configuration for the <tt>&quot;account&quot;</tt> subsystem. </p>
<p> An example authorization object to validate a <font SIZE="-1">TLS</font> x509 distinguished name would look like: </p>
<pre>
        # qemu-system-x86_64 \
        ...
        -object authz-pam,id=auth0,service=qemu-vnc
        ...
</pre>
<p> There would then be a corresponding config file for <font SIZE="-1">PAM</font> at <tt>&quot;/etc/pam.d/qemu-vnc&quot;</tt> that contains: </p>
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
<dt>
<dd></dl>
</dl>
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
<p> During emulation, if you are using a character backend multiplexer (which is the default if you are using <code>-nographic</code>) then several commands are available via an escape sequence. These key sequences all start with an escape character, which is <code>Ctrl-a</code> by default, but can be changed with <code>-echr</code>. The list below assumes you&#8217;re using the default.</p>
<dl>
<dt><code>Ctrl-a h</code></p>
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
<dd> Rotate between the frontends connected to the multiplexer (usually this switches between the monitor and the console)</p>
<dt><code>Ctrl-a Ctrl-a</code></p>
<dd> Send the escape character to the frontend</dl>
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
<dt><code>-M [sun4u|sun4v|niagara]</code></p>
<dd> Set the emulated machine type. The default is sun4u.</dl>
<p> The following options are specific to the <font SIZE="-1">ARM</font> emulation:</p>
<dl>
<dt><code>-semihosting</code></p>
<dd> Enable semihosting syscall emulation. </p>
<p> On <font SIZE="-1">ARM</font> this implements the &#8220;Angel&#8221; interface. </p>
<p> Note that this allows guest direct access to the host filesystem, so should only be used with trusted guest <font SIZE="-1">OS.</font></dl>
<p> The following options are specific to the ColdFire emulation:</p>
<dl>
<dt><code>-semihosting</code></p>
<dd> Enable semihosting syscall emulation. </p>
<p> On M68K this implements the &#8220;ColdFire <font SIZE="-1">GDB&#8221;</font> interface used by libgloss. </p>
<p> Note that this allows guest direct access to the host filesystem, so should only be used with trusted guest <font SIZE="-1">OS.</font></dl>
<p> The following options are specific to the Xtensa emulation:</p>
<dl>
<dt><code>-semihosting</code></p>
<dd> Enable semihosting syscall emulation. </p>
<p> Xtensa semihosting provides basic file <font SIZE="-1">IO</font> calls, such as open/read/write/seek/select. Tensilica baremetal libc for <font SIZE="-1">ISS</font> and linux platform &#8220;sim&#8221; use this interface. </p>
<p> Note that this allows guest direct access to the host filesystem, so should only be used with trusted guest <font SIZE="-1">OS.</font></dl>
<h2>NOTES</h2>
<p> In addition to using normal file images for the emulated storage devices, <font SIZE="-1">QEMU</font> can also use networked resources such as iSCSI devices. These are specified using a special <font SIZE="-1">URL</font> syntax.</p>
<dl>
<dt><code>iSCSI</code></p>
<dd> iSCSI support allows <font SIZE="-1">QEMU</font> to access iSCSI resources directly and use as images for the guest storage. Both disk and cdrom images are supported. </p>
<p> Syntax for specifying iSCSI LUNs is &#8220;iscsi://&lt;target-ip&gt;[:&lt;port&gt;]/&lt;target-iqn&gt;/&lt;lun&gt;&#8221; </p>
<p> By default qemu will use the iSCSI initiator-name &#8216;iqn.2008-11.org.linux-kvm[:&lt;name&gt;]&#8217; but this can also be set from the command line or a configuration file. </p>
<p> Since version Qemu 2.4 it is possible to specify a iSCSI request timeout to detect stalled requests and force a reestablishment of the session. The timeout is specified in seconds. The default is 0 which means no timeout. Libiscsi 1.15.0 or greater is required for this feature. </p>
<p> Example (without authentication): </p>
<pre>
        qemu-system-x86_64 -iscsi initiator-name=iqn.2001-04.com.example:my-initiator \
                         -cdrom <a href="iscsi://192.0.2.1/iqn.2001-04.com.example/2">iscsi://192.0.2.1/iqn.2001-04.com.example/2</a> \
                         -drive file=<a href="iscsi://192.0.2.1/iqn.2001-04.com.example/1">iscsi://192.0.2.1/iqn.2001-04.com.example/1</a>
</pre>
<p> Example (<font SIZE="-1">CHAP</font> username/password via <font SIZE="-1">URL</font>): </p>
<pre>
        qemu-system-x86_64 -drive file=<a href="iscsi://user%password@192.0.2.1/iqn.2001-04.com.example/1">iscsi://user%password@192.0.2.1/iqn.2001-04.com.example/1</a>
</pre>
<p> Example (<font SIZE="-1">CHAP</font> username/password via environment variables): </p>
<pre>
        LIBISCSI_CHAP_USERNAME=&quot;user&quot; \
        LIBISCSI_CHAP_PASSWORD=&quot;password&quot; \
        qemu-system-x86_64 -drive file=<a href="iscsi://192.0.2.1/iqn.2001-04.com.example/1">iscsi://192.0.2.1/iqn.2001-04.com.example/1</a>
</pre>
<dt><font SIZE="-1"><code>NBD</code></font></p>
<dd> <font SIZE="-1">QEMU</font> supports <font SIZE="-1">NBD</font> (Network Block Devices) both using <font SIZE="-1">TCP</font> protocol as well as Unix Domain Sockets. With <font SIZE="-1">TCP,</font> the default port is 10809. </p>
<p> Syntax for specifying a <font SIZE="-1">NBD</font> device using <font SIZE="-1">TCP,</font> in preferred <font SIZE="-1">URI</font> form: &#8220;nbd://&lt;server-ip&gt;[:&lt;port&gt;]/[&lt;export&gt;]&#8221; </p>
<p> Syntax for specifying a <font SIZE="-1">NBD</font> device using Unix Domain Sockets; remember that &#8216;?&#8217; is a shell glob character and may need quoting: &#8220;nbd+<a href="unix:///[">unix:///[</a>&lt;export&gt;]?socket=&lt;domain-socket&gt;&#8221; </p>
<p> Older syntax that is also recognized: &#8220;nbd:&lt;server-ip&gt;:&lt;port&gt;[:exportname=&lt;export&gt;]&#8221; </p>
<p> Syntax for specifying a <font SIZE="-1">NBD</font> device using Unix Domain Sockets &#8220;nbd:unix:&lt;domain-socket&gt;[:exportname=&lt;export&gt;]&#8221; </p>
<p> Example for <font SIZE="-1">TCP</font> </p>
<pre>
        qemu-system-x86_64 --drive file=nbd:192.0.2.1:30000
</pre>
<p> Example for Unix Domain Sockets </p>
<pre>
        qemu-system-x86_64 --drive file=nbd:unix:/tmp/nbd-socket
</pre>
<dt><font SIZE="-1"><code>SSH</code></font></p>
<dd> <font SIZE="-1">QEMU</font> supports <font SIZE="-1">SSH</font> (Secure Shell) access to remote disks. </p>
<p> Examples: </p>
<pre>
        qemu-system-x86_64 -drive file=<a href="ssh://user@host/path/to/disk.img">ssh://user@host/path/to/disk.img</a>
        qemu-system-x86_64 -drive file.driver=ssh,file.user=user,file.host=host,file.port=22,file.path=/path/to/disk.img
</pre>
<p> Currently authentication must be done using ssh-agent. Other authentication methods may be supported in future.</p>
<dt><code>Sheepdog</code></p>
<dd> Sheepdog is a distributed storage system for <font SIZE="-1">QEMU. QEMU</font> supports using either local sheepdog devices or remote networked devices. </p>
<p> Syntax for specifying a sheepdog device </p>
<p>sheepdog[+tcp | +unix]: //[host:port]/vdiname[?socket=path][#snapid|#tag]</p>
<p> Example </p>
<pre>
        qemu-system-x86_64 --drive file=sheepdog://192.0.2.1:30000/MyVirtualMachine
</pre>
<p> See also &lt;<code><a rel="nofollow" href="https://sheepdog.github.io/sheepdog/">https://sheepdog.github.io/sheepdog/</a></code>&gt;.</p>
<dt><code>GlusterFS</code></p>
<dd> GlusterFS is a user space distributed file system. <font SIZE="-1">QEMU</font> supports the use of GlusterFS volumes for hosting <font SIZE="-1">VM</font> disk images using <font SIZE="-1">TCP,</font> Unix Domain Sockets and <font SIZE="-1">RDMA</font> transport protocols. </p>
<p> Syntax for specifying a <font SIZE="-1">VM</font> disk image on GlusterFS volume is </p>
<p>URI : gluster[+type] : //[host[:port]]/volume/path[?socket=&#8230;][,debug=N][,logfile=&#8230;]</p>
<p>                       JSON :<br />
        &#8216;json:{&#8220;driver&#8221;:&#8221;qcow2&#8243;,&#8221;file&#8221;:{&#8220;driver&#8221;:&#8221;gluster&#8221;,&#8221;volume&#8221;:&#8221;testvol&#8221;,&#8221;path&#8221;:&#8221;a.img&#8221;,&#8221;debug&#8221;:N,&#8221;logfile&#8221;:&#8221;&#8230;&#8221;, &#8220;server&#8221; : [ {&#8220;type&#8221; : &#8220;tcp&#8221;, &#8220;host&#8221; : &#8220;&#8230;&#8221;, &#8220;port&#8221; : &#8220;&#8230;&#8221;},<br />
                                                                                                                                      {&#8220;type&#8221; : &#8220;unix&#8221;, &#8220;socket&#8221; : &#8220;&#8230;&#8221;} ]<br />
}<br />
}<br />
&#8216;</p>
<p> Example </p>
<p>URI : qemu &#8211; system &#8211; x86_64&#8211; drive file = gluster : // 192.0.2.1/testvol/a.img,<br />
                                                      file.debug = 9,<br />
                                     file.logfile = / var / log / qemu &#8211; gluster.log</p>
<p>                                                                             JSON : qemu &#8211;<br />
                                                    system &#8211; x86_64 &#8216;json:{&#8220;driver&#8221;:&#8221;qcow2&#8243;, &#8220;file&#8221;:<br />
{<br />
    &#8220;driver&#8221; : &#8220;gluster&#8221;,<br />
               &#8220;volume&#8221; : &#8220;testvol&#8221;,<br />
                          &#8220;path&#8221; : &#8220;a.img&#8221;,<br />
                                   &#8220;debug&#8221; : 9,<br />
                                   &#8220;logfile&#8221; : &#8220;/var/log/qemu-gluster.log&#8221;,<br />
                                               &#8220;server&#8221; : [ {&#8220;type&#8221; : &#8220;tcp&#8221;, &#8220;host&#8221; : &#8220;1.2.3.4&#8221;, &#8220;port&#8221; : 24007},<br />
                                                            {&#8220;type&#8221; : &#8220;unix&#8221;, &#8220;socket&#8221; : &#8220;/var/run/glusterd.socket&#8221;} ]<br />
}<br />
}<br />
&#8216; qemu &#8211; system &#8211; x86_64 &#8211; drive driver = qcow2, file.driver = gluster, file.volume = testvol, file.path = / path / a.img,<br />
                                 file.debug = 9, file.logfile = / var / log / qemu &#8211; gluster.log,<br />
                                 file.server .0.type = tcp, file.server .0.host = 1.2.3.4, file.server .0.port = 24007,<br />
                                 file.server .1.type = unix, file.server .1.socket = / var / run / glusterd.socket</p>
<p> See also &lt;<code><a rel="nofollow" href="http://www.gluster.org">http://www.gluster.org</a></code>&gt;.</p>
<dt><font SIZE="-1"><code>HTTP/HTTPS/FTP/FTPS</code></font></p>
<dd> <font SIZE="-1">QEMU</font> supports read-only access to files accessed over http(s) and ftp(s). </p>
<p> Syntax using a single filename: </p>
<pre><code>
        &lt;protocol&gt;://[&lt;username&gt;[:&lt;password&gt;]@]&lt;host&gt;/&lt;path&gt;
</code></pre>
<p> where:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>protocol</code></p>
<dd> &#8216;http&#8217;, &#8216;https&#8217;, &#8216;ftp&#8217;, or &#8216;ftps&#8217;.</p>
<dt><code>username</code></p>
<dd> Optional username for authentication to the remote server.</p>
<dt><code>password</code></p>
<dd> Optional password for authentication to the remote server.</p>
<dt><code>host</code></p>
<dd> Address of the remote server.</p>
<dt><code>path</code></p>
<dd> Path on the remote server, including any query string.</dl>
</dl>
<dl>
<dt>
<dd>
<p> The following options are also supported:</p>
<dl>
<dt><code>url</code></p>
<dd> The full <font SIZE="-1">URL</font> when passing options to the driver explicitly.</p>
<dt><code>readahead</code></p>
<dd> The amount of data to read ahead with each range request to the remote server. This value may optionally have the suffix &#8216;T&#8217;, &#8216;G&#8217;, &#8216;M&#8217;, &#8216;K&#8217;, &#8216;k&#8217; or &#8216;b&#8217;. If it does not have a suffix, it will be assumed to be in bytes. The value must be a multiple of 512 bytes. It defaults to 256k.</p>
<dt><code>sslverify</code></p>
<dd> Whether to verify the remote server&#8217;s certificate when connecting over <font SIZE="-1">SSL.</font> It can have the value &#8216;on&#8217; or &#8216;off&#8217;. It defaults to &#8216;on&#8217;.</p>
<dt><code>cookie</code></p>
<dd> Send this cookie (it can also be a list of cookies separated by &#8216;;&#8217;) with each outgoing request. Only supported when using protocols such as <font SIZE="-1">HTTP</font> which support cookies, otherwise ignored.</p>
<dt><code>timeout</code></p>
<dd> Set the timeout in seconds of the <font SIZE="-1">CURL</font> connection. This timeout is the time that <font SIZE="-1">CURL</font> waits for a response from the remote server to get the size of the image to be downloaded. If not set, the default timeout of 5 seconds is used.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Note that when passing options to qemu explicitly, <code>driver</code> is the value of &lt;protocol&gt;. </p>
<p> Example: boot from a remote Fedora 20 live <font SIZE="-1">ISO</font> image </p>
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
</dl>
</dl>
<h2>SEE ALSO</h2>
<p> The <font SIZE="-1">HTML</font> documentation of <font SIZE="-1">QEMU</font> for more precise information and Linux user mode emulator invocation.</p>
<h2>AUTHOR</h2>
<p> Fabrice Bellard </p>
<h2>Index</h2>
