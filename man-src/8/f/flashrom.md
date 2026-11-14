---
title: "flashrom(8)"
name: "flashrom"
section: "8"
letter: "f"
url: "/docs/linux/man/8-flashrom/"
description: "flashrom – detect, read, write, verify and erase flash chips"
---

<p>flashrom &#8211; detect, read, write, verify and erase flash chips</p>
<h2>Synopsis</h2>
<p><code>flashrom </code>[<code>-n</code>] [<code>-V</code>] [<code>-f</code>] [<code>-h</code>|<code>-R</code>|<code>-L</code>|<code>-z</code>|<code>-E</code>|<code>-r</code> &lt;file&gt;|<code>-w</code> &lt;file&gt;|<code>-v</code> &lt;file&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>-c</code>&nbsp;<wbr>&lt;chipname&gt;]&nbsp;<wbr>[<code>-m</code>&nbsp;<wbr>[&lt;vendor&gt;:]&lt;board&gt;]&nbsp;<wbr>[<code>-l</code>&nbsp;<wbr>&lt;file&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>-i</code>&nbsp;<wbr>&lt;image&gt;]&nbsp;<wbr>[<code>-p</code>&nbsp;<wbr>&lt;programmername&gt;[:&lt;parameters&gt;]]</p>
<h2>Description</h2>
<p><code>flashrom</code> is a utility for detecting, reading, writing, verifying and erasing flash chips. It&#8217;s often used to flash BIOS/EFI/coreboot/firmware images in-system using a supported mainboard, but it also supports flashing of network cards (NICs), SATA controller cards, and other external devices which can program flash chips. </p>
<p> It supports a wide range of DIP32, PLCC32, DIP8, SO8/SOIC8, TSOP32, TSOP40, and TSOP48 chips, which use various protocols such as LPC, FWH, parallel flash, or SPI.</p>
<h2>Options</h2>
<p><code>IMPORTANT:</code> Please note that the command line interface for flashrom will change before flashrom 1.0. Do not use flashrom in scripts or other automated tools without checking that your flashrom version won&#8217;t interpret options in a different way. </p>
<p> You can specify one of <code>-h</code>, <code>-R</code>, <code>-L</code>, <code>-z</code>, <code>-E</code>, <code>-r</code>, <code>-w</code>, <code>-v</code> or no operation. If no operation is specified, flashrom will only probe for flash chips. It is recommended that if you try flashrom the first time on a system, you run it in probe only mode and check the output. Also you are advised to make a backup of your current ROM contents with <code>-r</code> before you try to write a new image.</p>
<dl>
<dt><code>-r, &#8211;read &lt;file&gt;</code></p>
<dd>Read flash ROM contents and save them into the given <code>&lt;file&gt;</code>.</p>
<dt><code>-w, &#8211;write &lt;file&gt;</code></p>
<dd>Write <code>&lt;file&gt;</code> into flash ROM. This will first automatically <code>erase</code> the chip, then write to it.</p>
<dt><code>-n, &#8211;noverify</code></p>
<dd>Skip the automatic verification of flash ROM contents after writing. Using this option is <code>not</code> recommended, you should only use it if you know what you are doing and if you feel that the time for verification takes too long. </p>
<p> Typical usage is: <code>flashrom -n -w &lt;file&gt;</code> </p>
<p> This option is only useful in combination with <code>&#8211;write</code>.</p>
<dt><code>-v, &#8211;verify &lt;file&gt;</code></p>
<dd>Verify the flash ROM contents against the given <code>&lt;file&gt;</code>.</p>
<dt><code>-E, &#8211;erase</code></p>
<dd>Erase the flash ROM chip.</p>
<dt><code>-V, &#8211;verbose</code></p>
<dd>More verbose output. This option can be supplied multiple times (max. 2 times, i.e. <code>-VV</code>) for even more debug output.</p>
<dt><code>-c, &#8211;chip &lt;chipname&gt;</code></p>
<dd>Probe only for the specified flash ROM chip. This option takes the chip name as printed by <code>flashrom -L</code> without the vendor name as parameter. Please note that the chip name is case sensitive.</p>
<dt><code>-m, &#8211;mainboard [&lt;vendor&gt;:]&lt;board&gt;</code></p>
<dd>Override mainboard settings. </p>
<p> flashrom reads the coreboot table to determine the current mainboard. If no coreboot table could be read or if you want to override these values, you can specify -m, e.g.: </p>
<p> <code> flashrom &#8211;mainboard AGAMI:ARUMA -w agami_aruma.rom</code> </p>
<p> See the &#8216;Known boards&#8217; or &#8216;Known laptops&#8217; section in the output of &#8216;flashrom -L&#8217; for a list of boards which require the specification of the board name, if no coreboot table is found.</p>
<dt><code>-f, &#8211;force</code></p>
<dd>Force one or more of the following actions: </p>
<p> * Force chip read and pretend the chip is there. </p>
<p> * Force chip access even if the chip is bigger than the maximum supported size for the flash bus. </p>
<p> * Force erase even if erase is known bad. </p>
<p> * Force write even if write is known bad.</p>
<dt><code>-l, &#8211;layout &lt;file&gt;</code></p>
<dd>Read ROM layout from <code>&lt;file&gt;</code>. </p>
<p> flashrom supports ROM layouts. This allows you to flash certain parts of the flash chip only. A ROM layout file looks like follows: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>00000000:00008fff gfxrom<br />
&nbsp;<wbr>&nbsp;<wbr>00009000:0003ffff normal<br />
&nbsp;<wbr>&nbsp;<wbr>00040000:0007ffff fallback </p>
<p>&nbsp;<wbr>&nbsp;<wbr>i.e.:<br />
&nbsp;<wbr>&nbsp;<wbr>startaddr:endaddr name </p>
<p> All addresses are offsets within the file, not absolute addresses! If you only want to update the normal image in a ROM you can say: </p>
<p> <code> flashrom &#8211;layout rom.layout &#8211;image normal -w agami_aruma.rom</code> </p>
<p> To update normal and fallback but leave the VGA BIOS alone, say: </p>
<p> <code> flashrom -l rom.layout -i normal<br />
 </code> <code> -i fallback -w agami_aruma.rom</code> </p>
<p> Currently overlapping sections are not supported.</p>
<dt><code>-i, &#8211;image &lt;name&gt;</code></p>
<dd>Only flash image <code>&lt;name&gt;</code> from flash layout.</p>
<dt><code>-L, &#8211;list-supported</code></p>
<dd>List the flash chips, chipsets, mainboards, and PCI card &quot;programmers&quot; supported by flashrom. </p>
<p> There are many unlisted boards which will work out of the box, without special support in flashrom. Please let us know if you can verify that other boards work or do not work out of the box. </p>
<p> <code>IMPORTANT:</code> For verification you have to test an ERASE and/or WRITE operation, so make sure you only do that if you have proper means to recover from failure!</p>
<dt><code>-z, &#8211;list-supported-wiki</code></p>
<dd>Same as <code>&#8211;list-supported</code>, but outputs the supported hardware in MediaWiki syntax, so that it can be easily pasted into the wiki page at <a rel="nofollow" href="http://www.flashrom.org/.">http://www.flashrom.org/.</a> Please note that MediaWiki output is not compiled in by default.</p>
<dt><code>-p, &#8211;programmer &lt;name&gt;[:parameter[,parameter[,parameter]]]</code></p>
<dd>Specify the programmer device. Currently supported are: </p>
<p> <code>* internal</code> (default, for in-system flashing in the mainboard) </p>
<p> <code>* dummy</code> (just prints all operations and accesses) </p>
<p> <code>* nic3com</code> (for flash ROMs on 3COM network cards) </p>
<p> <code>* nicrealtek</code> (for flash ROMs on Realtek network cards) </p>
<p> <code>* nicsmc1211</code> (for flash ROMs on RTL8139-compatible SMC2 network cards) </p>
<p> <code>* nicnatsemi</code> (for flash ROMs on National Semiconductor DP838* network cards) </p>
<p> <code>* gfxnvidia</code> (for flash ROMs on NVIDIA graphics cards) </p>
<p> <code>* drkaiser</code> (for flash ROMs on Dr. Kaiser PC-Waechter PCI cards) </p>
<p> <code>* satasii</code> (for flash ROMs on Silicon Image SATA/IDE controllers) </p>
<p> <code>* atahpt</code> (for flash ROMs on Highpoint ATA/RAID controllers) </p>
<p> <code>* it87spi</code> (for flash ROMs behind an ITE IT87xx Super I/O LPC/SPI translation unit) </p>
<p> <code>* ft2232_spi</code> (for SPI flash ROMs attached to a FT2232H/FT4232H/JTAGkey based USB SPI programmer) </p>
<p> <code>* serprog</code> (for flash ROMs attached to a programmer speaking serprog) </p>
<p> <code>* buspirate_spi</code> (for SPI flash ROMs attached to a Bus Pirate) </p>
<p> <code>* dediprog</code> (for SPI flash ROMs attached to a Dediprog SF100) </p>
<p> <code>* rayer_spi</code> (for SPI flash ROMs attached to a RayeR parport based programmer) </p>
<p> <code>* nicintel_spi</code> (for SPI flash ROMs attached to an Intel Gigabit network cards) </p>
<p> Some programmers have optional or mandatory parameters which are described in detail in the <code>PROGRAMMER SPECIFIC INFO</code> section. Support for some programmers can be disabled at compile time. <code>flashrom -h</code> lists all supported programmers.</p>
<dt><code>-h, &#8211;help</code></p>
<dd>Show a help text and exit.</p>
<dt><code>-R, &#8211;version</code></p>
<dd>Show version information and exit.</dl>
<h2>Programmer Specific Info</h2>
<p>Some programmer drivers accept further parameters to set programmer-specific parameters. These parameters are separated from the programmer name by a colon. While some programmers take arguments at fixed positions, other programmers use a key/value interface in which the key and value is separated by an equal sign and different pairs are separated by a comma or a colon.</p>
<dl>
<dt><code>internal </code>programmer</p>
<dd>Some mainboards require to run mainboard specific code to enable flash erase and write support (and probe support on old systems with parallel flash). The mainboard brand and model (if it requires specific code) is usually autodetected using one of the following mechanisms: If your system is running coreboot, the mainboard type is determined from the coreboot table. Otherwise, the mainboard is detected by examining the onboard PCI devices and possibly DMI info. If PCI and DMI do not contain information to uniquely identify the mainboard (which is the exception), it might be necessary to specify the mainboard using the <code>-m</code> switch (see above). </p>
<p> Some of these board-specific flash enabling functions (called <code>board enables</code>) in flashrom have not yet been tested. If your mainboard is detected needing an untested board enable function, a warning message is printed and the board enable is not executed, because a wrong board enable function might cause the system to behave erratically, as board enable functions touch the low-level internals of a mainboard. Not executing a board enable function (if one is needed) might cause detection or erasing failure. If your board protects only part of the flash (commonly the top end, called boot block), flashrom might encounter an error only after erasing the unprotected part, so running without the board-enable function might be dangerous for erase and write (which includes erase). </p>
<p> The suggested procedure for a mainboard with untested board specific code is to first try to probe the ROM (just invoke flashrom and check that it detects your flash chip type) without running the board enable code (i.e. without any parameters). If it finds your chip, fine. Otherwise, retry probing your chip with the board-enable code running, using </p>
<p> <code> flashrom -p internal:boardenable=force</code> </p>
<p> If your chip is still not detected, the board enable code seems to be broken or the flash chip unsupported. Otherwise, make a backup of your current ROM contents (using <code>-r</code>) and store it to a medium outside of your computer, like a USB drive or a network share. If you needed to run the board enable code already for probing, use it for reading too. Now you can try to write the new image. You should enable the board enable code in any case now, as it has been written because it is known that writing/erasing without the board enable is going to fail. In any case (success or failure), please report to the flashrom mailing list, see below. </p>
<p> On systems running coreboot, flashrom checks whether the desired image matches your mainboard. This needs some special board ID to be present in the image. If flashrom detects that the image you want to write and the current board do not match, it will refuse to write the image unless you specify </p>
<p> <code> flashrom -p internal:boardmismatch=force</code> </p>
<p> If your mainboard uses an ITE IT87 series Super I/O for LPC&lt;-&gt;SPI flash bus translation, flashrom should autodetect that configuration. You can use the </p>
<p> <code> flashrom -p internal:it87spiport=portnum</code> </p>
<p> syntax as explained in the <code>it87spi</code> programmer section to use a non-default port for controlling the IT87 series Super I/O. In the unlikely case flashrom doesn&#8217;t detect an active IT87 LPC&lt;-&gt;SPI bridge, you can try to force recognition by using the <code>it87spi</code> programmer. </p>
<p> Using flashrom on laptops is dangerous and may easily make your hardware unusable (see also the <code>BUGS</code> section). The embedded controller (EC) in these machines often interacts badly with flashing. <code><a rel="nofollow" href="http://www.flashrom.org/Laptops">http://www.flashrom.org/Laptops</a></code> has more information. If flash is shared with the EC, erase is guaranteed to brick your laptop and write is very likely to brick your laptop. Chip read and probe may irritate your EC and cause fan failure, backlight failure, sudden poweroff, and other nasty effects. flashrom will attempt to detect laptops and abort immediately for safety reasons. If you want to proceed anyway at your own risk, use </p>
<p> <code> flashrom -p internal:laptop=force_I_want_a_brick</code> </p>
<p> You have been warned. </p>
<p> We will not help you if you force flashing on a laptop because this is a really dumb idea.</p>
<dt><code>dummy </code>programmer</p>
<dd>An optional parameter specifies the bus types it should support. For that you have to use the <code>flashrom -p dummy:bus=[type[+type[+type]]]</code> syntax where <code>type</code> can be any of <code>parallel</code>, <code>lpc</code>, <code>fwh</code>, <code>spi</code> in any order. If you specify bus without type, all buses will be disabled. If you do not specify bus, all buses will be enabled. </p>
<p> Example: <code>flashrom -p dummy:bus=lpc+fwh</code></p>
<dt><code>nic3com</code>,<code> nicrealtek</code>,<code> nicsmc1211</code>,<code> nicnatsemi</code>,<code> gfxnvidia</code>,<code> satasii </code>and<code> atahpt </code>programmers</p>
<dd>These programmers have an option to specify the PCI address of the card your want to use, which must be specified if more than one card supported by the selected programmer is installed in your system. The syntax is <code>flashrom -p xxxx:pci=bb:dd.f</code>, where <code>xxxx</code> is the name of the programmer <code>bb</code> is the PCI bus number, <code>dd</code> is the PCI device number, and <code>f</code> is the PCI function number of the desired device. </p>
<p> Example: <code>flashrom -p nic3com:pci=05:04.0</code></p>
<dt><code>it87spi </code>programmer</p>
<dd>An optional <code>it87spiport</code> parameter sets the I/O base port of the IT87 series SPI controller interface to the port specified in the parameter instead of using the port address set by the BIOS. For that you have to use the </p>
<p> <code> flashrom -p it87spi:it87spiport=portnum</code> </p>
<p> syntax where <code>portnum</code> is an I/O port number which must be a multiple of 8.</p>
<dt><code>ft2232_spi </code>programmer</p>
<dd>An optional parameter specifies the controller type and interface/port it should support. For that you have to use the </p>
<p> <code> flashrom -p ft2232_spi:type=model,port=interface</code> </p>
<p> syntax where <code>model</code> can be any of <code>2232H</code>, <code>JTAGkey</code>, or <code>4232H</code> and <code>interface</code> can be any of <code>A</code>, or <code>B</code>. The default model is <code>4232H</code> and the default interface is <code>B</code>.</p>
<dt><code>serprog </code>programmer</p>
<dd>A mandatory parameter specifies either a serial device/baud combination or an IP/port combination for communication with the programmer. In the device/baud combination, the device has to start with a slash. For serial, you have to use the </p>
<p> <code> flashrom -p serprog:dev=/dev/device:baud</code> </p>
<p> syntax and for IP, you have to use </p>
<p> <code> flashrom -p serprog:ip=ipaddr:port</code> </p>
<p> instead. More information about serprog is available in <code>serprog-protocol.txt</code> in the source distribution.</p>
<dt><code>buspirate_spi </code>programmer</p>
<dd>A required <code>dev</code> parameter specifies the Bus Pirate device node and an optional <code>spispeed</code> parameter specifies the frequency of the SPI bus. The parameter delimiter is a comma. Syntax is </p>
<p> <code>flashrom -p buspirate_spi:dev=/dev/device,spispeed=frequency</code> </p>
<p> where <code>frequency</code> can be any of <code>30k</code>, <code>125k</code>, <code>250k</code>, <code>1M</code>, <code>2M</code>, <code>2.6M</code>, <code>4M</code>, <code>8M</code> (in Hz). The default is the maximum frequency of 8 MHz.</p>
<dt><code>dediprog </code>programmer</p>
<dd>No parameters defined yet.</p>
<dt><code>rayer_spi </code>programmer</p>
<dd>The default I/O base address used for the parallel port is 0x378 and you can use the optional <code>iobase</code> parameter to specify an alternate base I/O address with the </p>
<p> <code> flashrom -p rayer_spi:iobase=baseaddr</code> </p>
<p> syntax where <code>baseaddr</code> is base I/O port address of the parallel port, which must be a multiple of four. Make sure to not forget the &quot;0x&quot; prefix for hexadecimal port addresses. </p>
<p> More information about the hardware is available at <a rel="nofollow" href="http://rayer.ic.cz/elektro/spipgm.htm">http://rayer.ic.cz/elektro/spipgm.htm</a></dl>
<h2>Exit Status</h2>
<p>flashrom exits with 0 on success, 1 on most failures but with 2 if /dev/mem (/dev/xsvc on Solaris) can not be opened and with 3 if a call to mmap() fails.</p>
<h2>Requirements</h2>
<p>flashrom needs different access permissions for different programmers. </p>
<p> <code>internal</code> needs raw memory access, PCI configuration space access, raw I/O port access (x86) and MSR access (x86). </p>
<p> <code>it87spi</code> needs raw I/O port access (x86). </p>
<p> <code>nic3com</code>, <code>nicrealtek</code>, <code>nicsmc1211</code> and <code>nicnatsemi</code> need PCI configuration space read access and raw I/O port access. </p>
<p> <code>atahpt</code> needs PCI configuration space access and raw I/O port access. </p>
<p> <code>gfxnvidia</code> and <code>drkaiser</code> need PCI configuration space access and raw memory access. </p>
<p> <code>rayer_spi</code> needs raw I/O port access. </p>
<p> <code>satasii</code> needs PCI configuration space read access and raw memory access. </p>
<p> <code>serprog</code> needs TCP access to the network or userspace access to a serial port. </p>
<p> <code>buspirate_spi</code> needs userspace access to a serial port. </p>
<p> <code>dediprog</code> and <code>ft2232_spi</code> need access to the USB device via libusb. </p>
<p> <code>dummy</code> needs no access permissions at all. </p>
<p> <code>internal</code>, <code>it87spi</code>, <code>nic3com</code>, <code>nicrealtek</code>, <code>nicsmc1211</code>, <code>nicnatsemi</code>, <code>gfxnvidia</code>, <code>drkaiser</code>, <code>satasii</code> and <code>atahpt</code> have to be run as superuser/root, and need additional raw access permission. </p>
<p> <code>serprog</code>, <code>buspirate_spi</code>, <code>dediprog</code> and <code>ft2232_spi</code> can be run as normal user on most operating systems if appropriate device permissions are set. </p>
<p> On OpenBSD, you can obtain raw access permission by setting securelevel=-1 in /etc/rc.securelevel and rebooting, or rebooting into single user mode.</p>
<h2>Bugs</h2>
<p>Please report any bugs at </p>
<p> <code> <a rel="nofollow" href="http://www.flashrom.org/trac/flashrom/newticket">http://www.flashrom.org/trac/flashrom/newticket</a></code> </p>
<p> or on the flashrom mailing list at <code>&lt;flashrom [at] flashrom.org&gt;</code> </p>
<p> We recommend to subscribe first at </p>
<p> <code> <a rel="nofollow" href="http://www.flashrom.org/mailman/listinfo/flashrom">http://www.flashrom.org/mailman/listinfo/flashrom</a></code> </p>
<p> Using flashrom on laptops is dangerous and may easily make your hardware unusable unless you can desolder the flash chip and have a full flash chip backup. This is caused by the embedded controller (EC) present in many laptops, which interacts badly with any flash attempts. This is a hardware limitation and flashrom will attempt to detect it and abort immediately for safety reasons.</p>
<h2>Licence</h2>
<p><code>flashrom</code> is covered by the GNU General Public License (GPL), version 2. Some files are additionally available under the GPL (version 2, or any later version).</p>
<h2>Copyright</h2>
<p>Please see the individual files.</p>
<h2>Authors</h2>
<p>Andrew Morgan<br />
 Carl-Daniel Hailfinger<br />
 Claus Gindhart<br />
 David Borg<br />
 David Hendricks<br />
 Dominik Geyer<br />
 Eric Biederman<br />
 Giampiero Giancipoli<br />
 Helge Wagner<br />
 Idwer Vollering<br />
 Joe Bao<br />
 Jörg Fischer<br />
 Joshua Roys<br />
 Luc Verhaegen<br />
 Li-Ta Lo<br />
 Markus Boas<br />
 Mattias Mattsson<br />
 Michael Karcher<br />
 Nikolay Petukhov<br />
 Patrick Georgi<br />
 Peter Lemenkov<br />
 Peter Stuge<br />
 Reinder E.N. de Haan<br />
 Ronald G. Minnich<br />
 Ronald Hoogenboom<br />
 Sean Nelson<br />
 Stefan Reinauer<br />
 Stefan Wildemann<br />
 Stephan Guilloux<br />
 Steven James<br />
 Uwe Hermann<br />
 Wang Qingpei<br />
 Yinghai Lu<br />
 some others, please see the flashrom svn changelog for details.<br />
 All authors can be reached via e-mail at &lt;flashrom [at] flashrom.org&gt;. </p>
<p> This manual page was written by Uwe Hermann &lt;uwe [at] hermann-uwe.de&gt; and Carl-Daniel Hailfinger. It is licensed under the terms of the GNU GPL (version 2 or later).</p>
