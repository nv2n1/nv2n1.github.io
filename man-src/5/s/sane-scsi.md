---
title: "sane-scsi(5)"
name: "sane-scsi"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-scsi/"
description: "sane-scsi – SCSI adapter tips for scanners"
---

<p>sane-scsi &#8211; SCSI adapter tips for scanners</p>
<h2>Description</h2>
<p>This manual page contains various operating-system specific tips and tricks on how to get scanners with a SCSI interface working.</p>
<h2>General Info</h2>
<p>For scanners with a SCSI interface, it may be necessary to edit the appropriate backend configuration file before using SANE for the first time. For most systems, the configuration file should list the name of the generic SCSI device that the scanner is connected to (e.g., under Linux, <i>/dev/sg4</i> or <i>/dev/sge</i> is such a generic SCSI device). It is customary to create a symlink from <i>/dev/scanner</i> to the generic SCSI device that the scanner is connected to. In this case, the configuration file simply lists the line <i>/dev/scanner</i>. For a detailed description of each backend&#8217;s configuration file, please refer to the relevant backend manual page (e.g., <code><a href="/docs/linux/man/5-sane-epson/">sane-epson</a></code>(5) for Epson scanners, <code><a href="/docs/linux/man/5-sane-hp/">sane-hp</a></code>(5) for HP scanners, etc.). </p>
<p> For some operating systems (e.g. Linux and OS/2), there is an alternate way of specifying scanner devices. This alternate way allows one to identify scanners by the SCSI vendor and model string and/or by the SCSI device address (consisting of bus number, channel number, id, and logical unit number). The syntax for specifying a scanner in this way is: </p>
<dl>
<dd>scsi <i>VENDOR MODEL TYPE BUS CHANNEL ID LUN</i></dl>
<p> where <i>VENDOR</i> is the SCSI vendor string, <i>MODEL</i> is the SCSI model string, <i>TYPE</i> is type SCSI device type string, <i>BUS</i> is the SCSI bus number (named &quot;host&quot; in <i>/proc/scsi/scsi</i>), <i>CHANNEL</i> is the SCSI channel number, <i>ID</i> is the SCSI id, and <i>LUN</i> is the logical unit number of the scanner device. The first two fields are strings which must be enclosed in double-quotes if they contain any whitespace. The remaining four fields are non-negative integer numbers. The correct values for these fields can be found by using operating system specific tools, e.g. for Linux by looking at the output of the command <i>cat /proc/scsi/scsi</i>. To simplify configuration, a field&#8217;s value can be replaced with an asterisk symbol (&#8220;*&#8221;). An asterisk has the effect that any value is allowed for that particular field. This can have the effect that a single scsi-line matches multiple devices. When this happens, each matching device will be probed by the backend one by one and registered if the backend thinks it is a compatible device. For example, the line </p>
<dl>
<dd>scsi MUSTEK MFS-06000CX Scanner 0 00 03 00</dl>
<p> would attach the Mustek SCSI scanner with the following /proc/scsi/scsi entry: </p>
<dl>
<dd>
<pre>Host: scsi0 Channel: 00 Id: 03 Lun: 00
 Vendor: MUSTEK Model: MFS-06000CX Rev: 4.04
 Type: Scanner ANSI SCSI revision: 0</pre>
</dl>
<p> Usually it&#8217;s sufficient to use vendor and model strings only or even only the vendor string. The following example </p>
<dl>
<dd>scsi MUSTEK * * * * * *</dl>
<p> would have the effect that all SCSI devices in the system with a vendor string of MUSTEK would be probed and recognized by the backend. </p>
<p> If the remainder of a scsi-string consists of asterisks only, the asterisks can be omitted. For example, the following line is equivalent to the one specified previously: </p>
<dl>
<dd>scsi MUSTEK</dl>
<p> On some platforms (e.g., OpenStep), SANE device names take a special form. This is explained below in the relevant platform-specific section. </p>
<p> When using a SCSI scanner, ensure that the access permission for the generic SCSI device is set appropriately. We recommend to add a group &quot;scanner&quot; to <i>/etc/group</i> which contains all users that should have access to the scanner. The permission of the device should then be set to allow group read and write access. For example, if the scanner is at generic SCSI device <i>/dev/sg0</i>, then the following two commands would set the permission correctly: </p>
<dl>
<dd>$ chgrp scanner /dev/sg0<br />
 $ chmod 660 /dev/sg0
</dl>
<p> When your system uses the device filesystem (devfs), you have to edit <i>/etc/devfs/perms.</i> There you should search the line </p>
<dl>
<dd>REGISTER ^sg[^/]* PERMISSIONS root.root 0600</dl>
<p> and add a new line (eg. for changing permissions of sg4): </p>
<dl>
<dd>REGISTER ^sg4 PERMISSIONS root.scanner 0660</dl>
<h2>Freebsd Info</h2>
<p>Auto-configuration using the &quot;scsi *&quot; lines in the config files only works if the user running the frontend has read/write access to <i>/dev/xpt0</i>. Instead, you can also set a link <i>/dev/scanner</i> to the appropriate <i>/dev/uk</i> device.</p>
<dl>
<dd>
<dl>
<dt>Adaptec AHA1542CF</p>
<dd>Reported to work fine under FreeBSD 2.2.2R with the <code>aha</code> driver.</p>
<dt>Adaptec 2940</p>
<dd>Reported to work fine under FreeBSD 2.2.2.</p>
<dt>Adaptec 1522</p>
<dd>The scanner probes ok but any attempt to access it <i>hangs</i> the entire system. It looks like something is disabling interrupts and then not re-enabling them, so it looks like a bug in the FreeBSD <code>aic</code> driver.</p>
<dt>Adaptec 1505</p>
<dd>Works on FreeBSD 2.2.5R and 3.0 using the <code>aic</code> driver, provided that Plug-and-Play support is disabled on the card. If there are no <i>uk</i> devices, just do a <i>sh MAKEDEV uk0</i> in the <i>/dev</i> directory. The scanner should then be accessible as <i>/dev/uk0</i> if it was probed during boot.</p>
<dt>Tekram DC390</p>
<dd>Reported to work fine under FreeBSD 2.2.2R with the <code>amd</code> driver.</dl>
</dl>
<h2>Linux Info</h2>
<p>First, make sure your kernel has SCSI generic support enabled. In <i>make xconfig</i>, this shows up under &#8220;SCSI support-&gt;SCSI generic support&#8221;. </p>
<p> To keep scanning times to a minimum, it is strongly recommended to use a large buffer size for the generic SCSI driver. From SG driver version 2.0 on, the maximum buffer size can be changed at program run time, and there is no restriction in size. This driver version is part of the Linux kernels from version 2.2.7 on. If the new SG driver is available some backends (e.g. <code><a href="/docs/linux/man/5-sane-umax/">sane-umax</a></code>(5), <code><a href="/docs/linux/man/5-sane-mustek/">sane-mustek</a></code>(5)<code>,</code> <code><a href="/docs/linux/man/5-sane-sharp/">sane-sharp</a></code>(5)) automatically request larger SCSI buffers. If a backend does not automatically request a larger SCSI buffer, set the environment variable <code>SANE_SG_BUFFERSIZE</code> to the desired buffer size in bytes. It is not recommended to use more than 1 MB, because for large values the probability increases that the SG driver cannot allocate the necessary buffer(s). For ISA cards, even 1 MB might be a too large value. For a detailed discussion of memory issues of the SG driver, see <i><a rel="nofollow" href="http://www.torque.net/sg.">http://www.torque.net/sg.</a></i> </p>
<p> For Linux kernels before version 2.2.7 the size of the buffer is only 32KB. This works, but for many cheaper scanners this causes scanning to be slower by about a factor of four than when using a size of 127KB. Linux defines the size of this buffer by macro <code>SG_BIG_BUFF</code> in header file <i>/usr/include/scsi/sg.h</i>. Unless a system is seriously short on memory, it is recommended to increase this value to the maximum legal value of 128*1024-512=130560 bytes. After changing this value, it is necessary to recompile both the kernel (or the SCSI generic module) and the SCSI backends. Keep in mind that this is only necessary with older Linux kernels. </p>
<p> A common issue with SCSI scanners is what to do when you booted the system while the scanner was turned off. In such a case, the scanner won&#8217;t be recognized by the kernel and SANE won&#8217;t be able to access it. Fortunately, Linux provides a simple mechanism to probe a SCSI device on demand. Suppose you have a scanner connected to SCSI bus 2 and the scanner has a SCSI id of 5. When the system is up and running and the scanner is turned on, you can issue the command: </p>
<dl>
<dd>echo &quot;scsi add-single-device 2 0 5 0&quot; &gt; /proc/scsi/scsi</dl>
<p> and the kernel will probe and recognize your scanner (this needs to be done as root). It&#8217;s also possible to dynamically remove a SCSI device by using the &#8220;remove-single-device&#8221; command. For details, please refer to to the SCSI-2.4-HOWTO. </p>
<p> Scanners are known to work with the following SCSI adapters under Linux. This list isn&#8217;t complete, usually any SCSI adapter supported by Linux should work. </p>
<dl>
<dd>
<dl>
<dt>Acard/Advance SCSI adapters</p>
<dd>Some old versions of the kernel driver (<i>atp870u.c</i>) cut the inquiry information. Therefore the scanner couldn&#8217;t be detected correctly. Use a current kernel.</p>
<dt>Adaptec AHA-1505/AHA-1542/AHA-2940</p>
<dd>Reported to work fine with Linux since v2.0. If you encounter kernel freezes or other unexpected behaviour get the latest Linux kernel (2.2.17 seems to work) or reduce SCSI buffer size to 32 kB.</p>
<dt>ASUS SC200</p>
<dd>Reported to work fine with Linux v2.0.</p>
<dt>BusLogic BT958</p>
<dd>To configure the BusLogic card, you may need to follow these instructions (contributed by Jeremy &lt;jeremy [at] xxedgexx.com&gt;): During boot, when your BusLogic adapter is being initialized, press Ctrl-B to enter your BusLogic adapter setup. Choose the address which your BusLogic containing your scanner is located. Choose &#8220;SCSI Device Configuration&#8221;. Choose &#8220;Scan SCSI Bus&#8221;. Choose whatever SCSI id that contains your scanner and then choose &#8220;View/Modify SCSI configuration&#8221;. Change &#8220;Negotiation&#8221; to &#8220;async&#8221; and change &#8220;Disconnect&#8221; to &#8220;off&#8221;. Press Esc, save, and Esc again until you are asked to reboot.</p>
<dt>NCR/Symbios 53c400/53c400a or Domex DTC3181E/L/LE (DTCT436/436P) ISA SCSI card</p>
<dd>This card is supplied by Mustek (and other vendors). It&#8217;s supported since Linux 2.2. The SCSI cards are supported by the module g_NCR5380. It&#8217;s necessary to tell the kernel the io port and type of card. Example for a 53c400a: <i>modprobe g_NCR5380 ncr_addr=0x280 ncr_53c400a=1 .</i> Once the kernel detects the card, it should work all right. However, while it should work, do not expect good performance out of this card&#8212;it has no interrupt line and therefore while a scan is in progress, the system becomes almost unusable. You may change the values of the USLEEP macros in <i>drivers/scsi/g_NCR5380.c</i>. Some documentation is in this file and <i>NCR5380.c</i>.</p>
<dt>NCR/Symbios 810</p>
<dd>For some scanners it may be necessary to disable disconnect/reconnect. To achieve this use the option ncr53c8xx=&quot;disc:n&quot;. Some people reported that their scanner only worked with the 53c7,8xx driver, not the ncr53c8xx. Try both if you have trouble.<br />
 For Linux kernels before 2.0.33 it may be necessary to increase the SCSI timeout. The default timeout for the Linux kernels before 2.0.33 is 10 seconds, which is way too low when scanning large area. If you get messages of the form &#8220;restart (ncr dead ?)&#8221; in your <i>/var/log/messages</i> file or on the system console, it&#8217;s an indication that the timeout is too short. In this case, find the line &#8220;if (np-&gt;latetime&gt;10)&#8221; in file <i>ncr53c8xx.</i> (normally in directory <i>/usr/src/linux/drivers/scsi</i>) and change the constant 10 to, say, 60 (one minute). Then rebuild the kernel/module and try again.</p>
<dt>Tekram DC315</p>
<dd>The driver can be downloaded from <i><a rel="nofollow" href="http://www.garloff.de/kurt/linux/dc395/">http://www.garloff.de/kurt/linux/dc395/</a></i>. For some older scanners it may be necessary to disable all the more advanced features by using e.g. <i>modprobe dc395x_trm dc395x_trm=7,5,1,32</i>.</p>
<dt>Tekram DC390</p>
<dd>Version 1.11 of the Tekram driver seems to work fine mostly, except that the scan does not terminate properly (it causes a SCSI timeout after 10 minutes). The generic AM53C974 also seems to work fine and does not suffer from the timeout problems. </p>
</dl>
</dl>
<h2>Solaris, Openstep And Nextstep Info</h2>
<p>Under Solaris, OpenStep and NeXTStep, the generic SCSI device name refers to a SCSI bus, not to an individual device. For example, <i>/dev/sg0</i> refers to the first SCSI bus. To tell SANE which device to use, append the character &#8216;a&#8217;+target-id to the special device name. For example, the SCSI device connected to the first SCSI controller and with target-id 0 would be called <i>/dev/sg0a</i>, and the device with target-id 1 on that same bus would be called <i>/dev/sg0b,</i> and so on.</p>
<h2>Environment</h2>
<dl>
<dt><code>SANE_DEBUG_SANEI_SCSI</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for the generic SCSI I/O subsystem. E.g., a value of 128 requests all debug output to be printed by the backend. A value of 255 also prints kernel messages from the SCSI subsystem (where available). Smaller levels reduce verbosity.</p>
<dt><code>SANE_SCSICMD_TIMEOUT</code></p>
<dd>sets the timeout value for SCSI commands in seconds. Overriding the default value of 120 seconds should only be necessary for very slow scanners. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1), <code><a href="/docs/linux/man/5-sane-backendname/">sane-backendname</a></code>(5), <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5) </p>
<h2>Author</h2>
<p>David Mosberger</p>
