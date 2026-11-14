---
title: "irattach(8)"
name: "irattach"
section: "8"
letter: "i"
url: "/docs/linux/man/8-irattach/"
description: "irattach – binds the Linux-IrDA stack to a IrDA port"
---

<p>irattach &#8211; binds the Linux-IrDA stack to a IrDA port</p>
<h2>Synopsis</h2>
<p><code>irattach</code> [ <code>&lt;dev&gt;</code> ] [ <i>-s</i> ] [ <i>-d dongle</i> ] [ <i>-v</i> ] [ <i>-h</i> ] </p>
<h2>Description</h2>
<p><code>irattach</code> binds the Linux-IrDA stack to an IrDA port. It configures the low level of the Linux-IrDA stack in the kernel. This step is usually necessary before you (or applications) can use the higher layer of the IrDA stack. </p>
<p> The <code>irattach</code> command loads the necessary Linux-IrDA driver, which configures the IrDA hardware, and configures the IrDA stack to operate on the new IrDA port. Multiple IrDA ports can be activated through multiple <code>irattach</code> commands. </p>
<p> <code>irattach</code> by default uses the <code>irtty</code> driver which connects to the Linux TTY subsystem and use the standard Linux serial driver. This works well for most machines and configurations, but limits the baud rate to 115200bps (IrDA SIR mode). The mode of operation will work with most FIR hardware (as found in laptops &#8211; they provide serial emulation) and most serial dongles (provided the proper dongle type is specified), making it a safe choice. However, USB dongles and a few FIR hardware don&#8217;t support serial emulation and can&#8217;t be used with the <code>irtty</code> driver. </p>
<p> <code>irattach</code> can also use one of the Linux FIR drivers (including USB dongle drivers) instead of the <code>irtty</code> driver. Most FIR drivers require proper configuration of module parameters (this is documented below). FIR drivers allow you to use higher baud rates (generally up to 4Mbps). In general, Linux FIR support is not as stable and mature, due to lack of time and documentation. </p>
<p> <code>irattach</code> must be run as root or installed setuid root, as it requires root privileges. If you have compiled the IrDA stack as modules (recommended), then you will need to edit the <i>/etc/modules.conf</i> file. See the Infrared-HOWTO for details.</p>
<h2>Options</h2>
<p><code>&lt;dev&gt;</code> : this is the name of a TTY, an IrDA interface or IrDA driver. <code>irattach</code> decides to use the <code>irtty</code> driver or one of the FIR drivers based on this argument.</p>
<dl>
<dt>&bull;</p>
<dd><code>TTY name</code> : this is the serial port to be configured using the <code>irtty</code> driver, such as <code>/dev/ttyS0</code>. <code>irattach</code> will use the <code>irtty</code> driver, so only SIR will be available. You need to check your serial configuration or BIOS to know which serial port is the IrDA port that need to be passed to <code>irattach</code>.</p>
<dt>&bull;</p>
<dd><code>interface name</code> : this is the device name of an IrDA interface, such as <code>irda0</code>. <code>irattach</code> will use one of the FIR drivers (including USB dongle drivers). The selected FIR driver must be loaded prior to the call to <code>irattach</code>, or the proper alias for the device name must be set in <i>/etc/modules.conf</i>.</p>
<dt>&bull;</p>
<dd><code>module name</code> : this is the name of an FIR driver module, such as <code>nsc-ircc</code> (see list below). All new IrDA interfaces created after loading the module will be configured, so this won&#8217;t work if the module is already loaded. This feature is still experimental.</dl>
<p> <code>-s</code> : starts discovery of remote IrDA devices (note that the form &quot;-s 1&quot; is no longer supported) </p>
<p> <code>-v</code> : shows version information (this happens, when no option is given, too) </p>
<p> <code>-h</code> : shows help information. </p>
<p> <code>-d dongle</code> : attaches an additional dongle driver to the IrDA port. </p>
<p> You need a dongle driver if you have an infrared device that connects to your computer&#8217;s serial port (normal 9-pin serial port connector). These devices are called dongles, and can currently be used by any SIR driver (IrTTY or irport). This option is not compatible with FIR drivers, and only works with the irtty and irport drivers. </p>
<p> The currently known (serial) dongles are:</p>
<dl>
<dt>&bull;</p>
<dd><code>esi</code> Extended Systems JetEye PC ESI-9680</p>
<dt>&bull;</p>
<dd><code>tekram</code> Tekram IrMate IR-210B dongle</p>
<dt>&bull;</p>
<dd><code>actisys</code> ACTiSYS IR-220L dongle</p>
<dt>&bull;</p>
<dd><code>actisys+</code> ACTiSYS IR-220L+ dongle</p>
<dt>&bull;</p>
<dd><code>girbil</code> Greenwich GIrBIL dongle</p>
<dt>&bull;</p>
<dd><code>litelink </code> Parallax LiteLink dongle &amp; Extended Systems JetEye PC ESI-9680B</p>
<dt>&bull;</p>
<dd><code>airport</code> N.N.</p>
<dt>&bull;</p>
<dd><code>old_belkin</code> Belkin (old) SmartBeam dongle or any dongle only capable of 9600 bauds</p>
<dt>&bull;</p>
<dd><code>ep7211</code> IR port driver for the Cirrus Logic EP7211 processor (ARM based)</p>
<dt>&bull;</p>
<dd><code>mcp2120</code> Dongles based on the MCP2120 (Microchip)</p>
<dt>&bull;</p>
<dd><code>act200l</code> ACTiSYS Ir-200L dongles</p>
<dt>&bull;</p>
<dd><code>ma600</code> Mobile Action ma600 dongles</p>
<dt>&bull;</p>
<dd><code>toim3232</code> Vishay/Temic TOIM3232 and TOIM4232 based dongles</dl>
<h2>Fir Driver Modules</h2>
<p>If you are one of the lucky people which have a FIR chipset or USB dongle that is supported by one of the Linux-IrDA drivers, you can use <code>irattach</code> with the interface name of the IrDA port to configure. You will need to configure <i>/etc/conf.modules</i> appropriately, with at least an alias of <code>irda0</code> to the driver name, or load the driver manually beforehand. </p>
<p> You don&#8217;t strictly need to use <code>irattach</code> with FIR drivers, you can use <code>modprobe</code> to load the driver, <code>ifconfig</code> to bring up the interface and set the various sysctl by hand, but <code>irattach</code> offer a convenient way to do it. </p>
<p> Of course, you need to know which FIR driver applies to your hardware. You may use <code>findchip</code> to get information about the FIR chip. If this doesn&#8217;t help, the Infrared-HOWTO shows other means to retrieve these data. </p>
<p> Also, you often need to configure the <code>Linux-serial driver</code> to ignore the IrDA port, otherwise both drivers will conflict. This can usually be done with <code>setserial /dev/ttySx uart none</code>. </p>
<p> The currently known FIR drivers are:</p>
<dl>
<dt>&bull;</p>
<dd><code>ali-ircc</code> ALi FIR Controller Driver for ALi M5123 (options: io, irq, dma). This driver supports SIR, MIR and FIR (4Mbps) speeds. This chipset is used by e.g.: </p>
<p> The ALi M5123 FIR Controller is embedded in ALi M1543C, M1535, M1535D, M1535+, M1535D South Bridge.</p>
<dt>&bull;</p>
<dd><code>irda-usb</code> IrDA-USB device driver, for USB devices/dongles that comply with the official IrDA-USB class specification. Note: USB 2.0 is not yet tested. (options: qos_mtt_bits int, description &quot;Minimum Turn Time&quot;). This is used, for e.g.: </p>
<p> ACTiSYS ACT-IR2000U </p>
<p> KC Technology KC-180 </p>
<p> Extended Systems XTNDAccess ESI-9685 </p>
<p> Note that there is another USB driver for those devices called <code>ir-usb</code> which is NOT compatible with the IrDA stack and conflict with <code>irda-usb</code>. Because it always loads first, you have to remove <code>ir-usb</code> completely. </p>
<p> Devices based on the SigmaTel chip are not not compliant with the IrDA-USB class specification and therfore not supported by this driver.</p>
<dt>&bull;</p>
<dd><code>nsc-ircc</code> NSC IrDA device driver (options: io, irq, dma, dongle_id, qos_mtt_bits). This chipset is used by e.g.: </p>
<p> IBM ThinkPad dongle_id=0x09 </p>
<p> HP OmniBook 6000 dongle_id=0x08</p>
<dt>&bull;</p>
<dd><code>sa1100_ir</code> Infrared driver for devices based on the StrongARM SA1100 embedded microprocessor (options: power_level, tx_lpm). This driver may support FIR on devices that can do it. This chipset is used by e.g.: </p>
<p> Samsung YOPY, COMPAQ iPAQ, SHARP Zaurus SL5000/5500</p>
<dt>&bull;</p>
<dd><code>smc-ircc</code> SMC IrCC controller driver (options: ircc_dma, ircc_irq). This chipset is used by e.g.: </p>
<p> Fujitsu-Siemens Lifebook 635t Sony PCG-505TX</p>
<dt>&bull;</p>
<dd><code>w83977af_ir</code> Winbond W83977AF IrDA device driver (options: io, irq, qos_mtt_bits). This chipset is used by e.g.: </p>
<p> Corel NetWinder</p>
<dt>&bull;</p>
<dd><code>toshoboe</code> Toshiba OBOE IrDA device driver, supports Toshiba Type-O IR chipset. (options: max_baud). This chipset is used by e.g.: </p>
<p> Toshiba Libretto 100CT., and many more old Toshiba laptops.</p>
<dt>&bull;</p>
<dd><code>donauboe</code> is a new version of <code>toshoboe</code> and has better FIR support and compability with the Donauoboe chip <a rel="nofollow" href="http://libxg.free.fr/lib-irda.html">http://libxg.free.fr/lib-irda.html</a> (options: ..). This chipset is used by e.g.: </p>
<p> Toshiba Libretto 100CT., Tecra 8100, Portege 7020 and many more Toshiba laptops.</p>
<dt>&bull;</p>
<dd><code>vlsi_ir</code> VLSI 82C147 SIR/MIR/FIR device driver This chipset is used by e.g.: </p>
<p> HP Omnibook 800 </p>
<p> (options: ..).</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>clksrc int, description &quot;clock input source selection&quot;</p>
<dt>&bull;</p>
<dd>ringsize int array (min = 1, max = 2), description &quot;tx, rx ring descriptor size&quot;</p>
<dt>&bull;</p>
<dd>sirpulse int, description &quot;sir pulse width tuning&quot;</p>
<dt>&bull;</p>
<dd>mtt_bits int, description &quot;IrLAP bitfield representing min-turn-time&quot;</dl>
</dl>
</dl>
<h2>Examples</h2>
<p>Attach the IrDA stack to the second serial port (integrated IrDA port using serial emulation) and start discovery:</p>
<dl>
<dt>&bull;</p>
<dd><code>irattach /dev/ttyS1 -s</code></dl>
<p> Attach the IrDA stack to the first serial port where you have an external ACTiSYS serial dongle and start discovery:</p>
<dl>
<dt>&bull;</p>
<dd><code>irattach /dev/ttyS0 -d actisys+ -s</code></dl>
<p> Attach the IrDA stack to the first IrDA-USB dongle and start discovery:</p>
<dl>
<dt>&bull;</p>
<dd><code>modprobe irda-usb ; irattach irda0 -s</code></dl>
<p> Attach the IrDA stack to the NSC FIR (4Mbps) device driver on a Thinkpad laptop:</p>
<dl>
<dt>&bull;</p>
<dd><code>modprobe nsc-ircc dongle_id=0x9 ; irattach irda0 -s</code>.</dl>
<p> Attach the IrDA stack to the NSC FIR (4Mbps) device driver on a Thinkpad laptop:</p>
<dl>
<dt>&bull;</p>
<dd><code>irattach irda0 -s</code>. </p>
<p> This assume that you have added the following entries to <i>/etc/conf.modules</i>: </p>
<p> options nsc-ircc dongle_id=0x09 </p>
<p> alias irda0 nsc-ircc</dl>
<h2>Caveats</h2>
<p>The following hints are a very short introduction into the configuration of Linux/IrDA. If this doesn&#8217;t help read the Linux/IrDA-Tutorial and/or the Infrared-HOWTO . Before configuring Linux/IrDA make sure whether you want to configure SIR or FIR. It&#8217;s recommended to try SIR first, unless your device is not compatible with SIR (for example USB dongles). </p>
<p> To get the SIR &quot;serial&quot; device have a look into the BIOS. Then run <code>dmesg | grep tty</code> to get a survey of tty devices supported by your machine. Now try to choose the one, which is probably the IrDA device and use <code>irattach /dev/ttySx -s</code>. </p>
<p> If you don&#8217;t succeed with SIR (which seems a rare case) you may try FIR. First look up the BIOS. Then run <code>findchip</code> to get information about the IrDA controller chip. Use <code>setserial /dev/ttySx uart none </code> to avoid conflicts with the serial driver. Note: don&#8217;t use <code>setserial</code> if you configure SIR. Now you may use <code>irattach</code>. </p>
<p> Finally <code>irdadump</code> should show at least your computer itself. If it doesn&#8217;t start at the beginning. </p>
<p> This man page deal only with the low level of the IrDA stack (IrDA ports and IrDA drivers). After this step is done, you usually need to setup your favorite application to access the high level IrDA stack (via IrCOMM, IrLPT, IrNET, IrLAN or IrSOCK), which is documented elsewhere. </p>
<p> This man page doesn&#8217;t document the usage of the irport driver. The irport driver support the same hardware as the irtty driver, but is configured like a FIR driver.</p>
<h2>Diagnostics</h2>
<p>This section currently contains the raw error messages from source code only. </p>
<p> &quot;ioctl(TIOCGETD): %m&quot; </p>
<p> &quot;irattach: tty: set_disc(%d): %s&quot; </p>
<p> &quot;tcsetattr: %m&quot; </p>
<p> &quot;Failed to open %s: %m&quot; </p>
<p> &quot;Couldn&#8217;t get device fd flags: %m&quot; </p>
<p> &quot;Couldn&#8217;t set device to non-blocking mode: %m&quot;</p>
<h2>Bugs</h2>
<p>N.N.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-irattach/">irattach</a>(8), <a href="/docs/linux/man/8-irdaping/">irdaping</a>(8), <a href="/docs/linux/man/8-irdadump/">irdadump</a>(8), <a href="/docs/linux/man/8-findchip/">findchip</a>(8), <a href="/docs/linux/man/8-irpsion5/">irpsion5</a>(8), <a href="/docs/linux/man/8-modprobe/">modprobe</a>(8) </p>
<p> Linux/IrDA Project <a rel="nofollow" href="http://irda.sourceforge.net">http://irda.sourceforge.net</a> -*- Linux/IrDA-Tutorial <a rel="nofollow" href="http://www.hpl.hp.com/personal/Jean_Tourrilhes/IrDA/index.html">http://www.hpl.hp.com/personal/Jean_Tourrilhes/IrDA/index.html</a> -*- Infrared-HOWTO <a rel="nofollow" href="http://tuxmobil.org/howtos.html">http://tuxmobil.org/howtos.html</a> -*- Infrared-Hardware-Survey <a rel="nofollow" href="http://tuxmobil.org/ir_misc.html">http://tuxmobil.org/ir_misc.html</a></p>
<h2>Author</h2>
<p>This manual page is written by Werner Heuser &lt;wehe [at] tuxmobil.org&gt;. It is based on the READMEs from <code>irda-utils</code> by the Linux/IrDA Project and the Linux/IrDA-Tutorial. It was subsequently updated and modified by Jean Tourrilhes &lt;jt [at] hpl.hp.com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright (c) 2001 Werner Heuser Copyright (c) 2002 Jean Tourrilhes </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License (GFDL), Version 1.1 or any later version published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts and no Back-Cover Texts.</p>
