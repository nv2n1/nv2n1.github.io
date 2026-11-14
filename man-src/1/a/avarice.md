---
title: "avarice(1)"
name: "avarice"
section: "1"
letter: "a"
url: "/docs/linux/man/1-avarice/"
description: "avarice – Provides an interface from avr-gdb to Atmel’s JTAGICE box."
---

<h2 class="name">NAME</h2>
<p> avarice &#8211; Provides an interface from avr-gdb to Atmel&#8217;s JTAGICE box. </p>
<h2>SYNOPSIS</h2>
<p> <code>avarice</code> [<i>OPTIONS</i>]&#8230; [[<i>HOST_NAME</i>]:<i>PORT</i>]</p>
<h2>DESCRIPTION</h2>
<p> AVaRICE runs on a POSIX machine and connects to gdb via a TCP socket and communicates via gdb&#8217;s &quot;serial debug protocol&quot;. This protocol allows gdb to send commands like &quot;set/remove breakpoint&quot; and &quot;read/write memory&quot;. </p>
<p> AVaRICE translates these commands into the Atmel protocol used to control the AVR JTAG ICE. Connection to the AVR JTAG ICE is via a serial port on the POSIX machine. </p>
<p> Because the GDB &lt;&#8212;&gt; AVaRICE connection is via a TCP socket, the two programs do not need to run on the same machine. In an office environment, this allows a developer to debug a target in the lab from the comfort of their cube (or even better, their home!)</p>
<dl>
<dt> <code>NOTE:</code></p>
<dd>Even though you can run <code>avarice</code> and <code>avr-gdb</code> on different systems, it is not recommended because of the security risk involved. <code>avarice</code> was not designed to be a secure server. There is no authentication performed when a client connects to <code>avarice</code> when it is running in gdb server mode.</dl>
<h3>Supported Devices</h3>
<p> <code>avarice</code> currently has support for the following devices:</p>
<dl>
<dt>
<dd> at90can128<br />
 at90can32 (<code>o</code>)<br />
 at90can64 (<code>o</code>)<br />
 at90pwm2 (<code>o</code>) (<code>+</code>)<br />
 at90pwm216 (<code>o</code>) (<code>+</code>)<br />
 at90pwm2b (<code>o</code>) (<code>+</code>)<br />
 at90pwm3 (<code>o</code>) (<code>+</code>)<br />
 at90pwm316 (<code>o</code>) (<code>+</code>)<br />
 at90pwm3b (<code>o</code>) (<code>+</code>)<br />
 at90usb1287 (<code>*</code>)<br />
 at90usb162 (<code>o</code>) (<code>+</code>)<br />
 at90usb646 (<code>*</code>)<br />
 at90usb647 (<code>*</code>)<br />
 atmega128<br />
 atmega1280 (<code>*</code>)<br />
 atmega1281 (<code>*</code>)<br />
 atmega1284p (<code>*</code>)<br />
 atmega16<br />
 atmega162<br />
 atmega164p (<code>o</code>)<br />
 atmega165 (<code>o</code>)<br />
 atmega165p (<code>o</code>)<br />
 atmega168 (<code>o</code>) (<code>+</code>)<br />
 atmega168p (<code>o</code>) (<code>+</code>)<br />
 atmega169<br />
 atmega16hva (<code>o</code>)<br />
 atmega2560 (<code>*</code>)<br />
 atmega2561 (<code>*</code>)<br />
 atmega32<br />
 atmega323<br />
 atmega324p (<code>o</code>)<br />
 atmega325 (<code>o</code>)<br />
 atmega3250 (<code>o</code>)<br />
 atmega3250p (<code>o</code>)<br />
 atmega325p (<code>o</code>)<br />
 atmega328p (<code>o</code>) (<code>+</code>)<br />
 atmega329 (<code>o</code>)<br />
 atmega3290 (<code>o</code>)<br />
 atmega3290p (<code>o</code>)<br />
 atmega329p (<code>o</code>)<br />
 atmega32c1 (<code>o</code>) (<code>+</code>)<br />
 atmega32hvb (<code>o</code>) (<code>+</code>)<br />
 atmega32m1 (<code>o</code>) (<code>+</code>)<br />
 atmega32u4 (<code>o</code>)<br />
 atmega406 (<code>*</code>)<br />
 atmega48 (<code>o</code>) (<code>+</code>)<br />
 atmega48p (<code>o</code>) (<code>+</code>)<br />
 atmega64<br />
 atmega640 (<code>*</code>)<br />
 atmega644 (<code>*</code>)<br />
 atmega644p (<code>*</code>)<br />
 atmega645 (<code>*</code>)<br />
 atmega6450 (<code>*</code>)<br />
 atmega649 (<code>*</code>)<br />
 atmega6490 (<code>*</code>)<br />
 atmega88 (<code>o</code>) (<code>+</code>)<br />
 atmega88p (<code>o</code>) (<code>+</code>)<br />
 attiny13 (<code>o</code>) (<code>+</code>)<br />
 attiny167 (<code>o</code>) (<code>+</code>)<br />
 attiny2313 (<code>o</code>) (<code>+</code>)<br />
 attiny24 (<code>o</code>) (<code>+</code>)<br />
 attiny25 (<code>o</code>) (<code>+</code>)<br />
 attiny261 (<code>o</code>) (<code>+</code>)<br />
 attiny43u (<code>o</code>) (<code>+</code>)<br />
 attiny44 (<code>o</code>) (<code>+</code>)<br />
 attiny45 (<code>o</code>) (<code>+</code>)<br />
 attiny461 (<code>o</code>) (<code>+</code>)<br />
 attiny48 (<code>o</code>) (<code>+</code>)<br />
 attiny84 (<code>o</code>) (<code>+</code>)<br />
 attiny85 (<code>o</code>) (<code>+</code>)<br />
 attiny861 (<code>o</code>) (<code>+</code>)<br />
 attiny88 (<code>o</code>) (<code>+</code>)<br />
 atxmega128a1 (<code>*</code>)</dl>
<p> <code>*</code> &#8211; Only supported by the JTAG ICE mkII device.<br />
 <code>o</code> &#8211; Only supported by the JTAG ICE mkII and AVR Dragon device.<br />
 <code>+</code> &#8211; debugWire, see below</p>
<h3>Supported File Formats</h3>
<p> <code>avarice</code> uses libbfd for reading input files. As such, it can handle any file format that libbfd knowns about. This includes the Intel Hex, Motorola SRecord and ELF formats, among others. If you tell <code>avarice</code> to read an ELF file, it will automatically handle programming all of the sections contained in the file (e.g. flash, eeprom, etc.).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>,&nbsp;<wbr><code>&#8211;help</code></p>
<dd> Print this message.</p>
<dt><code>-1</code>,&nbsp;<wbr><code>&#8211;mkI</code></p>
<dd> Connect to JTAG ICE mkI (default).</p>
<dt><code>-2</code>,&nbsp;<wbr><code>&#8211;mkII</code></p>
<dd> Connect to JTAG ICE mkII.</p>
<dt><code>-B</code>,&nbsp;<wbr><code>&#8211;jtag-bitrate</code>&nbsp;<wbr>&lt;rate&gt;</p>
<dd> Set the bitrate that the JTAG box communicates with the AVR target device. This must be less than 1/4 of the frequency of the target. Valid values are 1 MHz, 500 kHz, 250 kHz or 125 kHz for the JTAG ICE mkI, anything between 22 kHz through approximately 6400 kHz for the JTAG ICE mkII. (default: 250 kHz)</p>
<dt><code>-C</code>,&nbsp;<wbr><code>&#8211;capture</code></p>
<dd> Capture running program.<br />
 Note: debugging must have been enabled prior to starting the program. (e.g., by running avarice earlier)</p>
<dt><code>-c</code>,&nbsp;<wbr><code>&#8211;daisy-chain</code>&nbsp;<wbr>&lt;ub,ua,bb,ba&gt;</p>
<dd> Setup JTAG daisy-chain information.<br />
 Four comma-separated parameters need to be provided, corresponding to <i>units before</i>, <i>units after</i>, <i>bits before</i>, and <i>bits after</i>.</p>
<dt><code>-D</code>,&nbsp;<wbr><code>&#8211;detach</code></p>
<dd> Detach once synced with JTAG ICE</p>
<dt><code>-d</code>,&nbsp;<wbr><code>&#8211;debug</code></p>
<dd> Enable printing of debug information.</p>
<dt><code>-e</code>,&nbsp;<wbr><code>&#8211;erase</code></p>
<dd> Erase target. Not possible in debugWire mode.</p>
<dt><code>-E</code>,&nbsp;<wbr><code>&#8211;event&nbsp;<wbr>&lt;eventlist&gt;</code></p>
<dd> List of events that do not interrupt. JTAG ICE mkII and AVR Dragon only. Default is &quot;none,run,target_power_on,target_sleep,target_wakeup&quot;</p>
<dt><code>-f</code>,&nbsp;<wbr><code>&#8211;file</code>&nbsp;<wbr>&lt;filename&gt;</p>
<dd> Specify a file for use with the &#8211;program and &#8211;verify options. If &#8211;file is passed and neither &#8211;program or &#8211;verify are given then &#8211;program is implied.</p>
<dt><code>-g</code>,&nbsp;<wbr><code>&#8211;dragon</code></p>
<dd> Connect to an AVR Dragon. This option implies the <code>-2</code> option.</p>
<dt><code>-I</code>,&nbsp;<wbr><code>&#8211;ignore-intr</code></p>
<dd> Automatically step over interrupts.<br />
 Note: EXPERIMENTAL. Can not currently handle devices fused for compatibility.</p>
<dt><code>-j</code>,&nbsp;<wbr><code>&#8211;jtag</code>&nbsp;<wbr>&lt;devname&gt;</p>
<dd> Port attached to JTAG box (default: /dev/avrjtag). If the JTAG_DEV environmental variable is set, avarice will use that as the default instead.<br />
 If <code>avarice</code> has been configured with libusb support, the JTAG ICE mkII can be connected through USB. In that case, the string <i>usb</i> is used as the name of the device. If there are multiple JTAG ICE mkII devices connected to the system through USB, this string may be followed by the (trailing part of the) ICE&#8217;s serial number, delimited from the <i>usb</i> by a colon.<br />
 The AVR Dragon can only be connected through USB, so this option defaults to &quot;usb&quot; in that case.</p>
<dt><code>-k</code>,&nbsp;<wbr><code>&#8211;known-devices</code></p>
<dd> Print a list of known devices.</p>
<dt><code>-L</code>,&nbsp;<wbr><code>&#8211;write-lockbits</code>&nbsp;<wbr>&lt;ll&gt;</p>
<dd> Write lock bits. The lock byte data must be given in two digit hexidecimal format with zero padding if needed.</p>
<dt><code>-l</code>,&nbsp;<wbr><code>&#8211;read-lockbits</code></p>
<dd> Read the lock bits from the target. The individual bits are also displayed with names.</p>
<dt><code>-P</code>,&nbsp;<wbr><code>&#8211;part</code>&nbsp;<wbr>&lt;name&gt;</p>
<dd> Target device name (e.g. atmega16)</p>
<dt><code>-p</code>,&nbsp;<wbr><code>&#8211;program</code></p>
<dd> Program the target. Binary filename must be specified with &#8211;file option.<br />
 <code>NOTE:</code> The old behaviour of automatically erasing the target before programming is no longer done. You must explicitly give the &#8211;erase option for the target to be erased.</p>
<dt><code>-R</code>,&nbsp;<wbr><code>&#8211;reset-srst</code></p>
<dd> Apply nSRST signal (external reset) when connecting. This can override applications that set the JTD bit.</p>
<dt><code>-r</code>,&nbsp;<wbr><code>&#8211;read-fuses</code></p>
<dd> Read fuses bytes.</p>
<dt><code>-V</code>,&nbsp;<wbr><code>&#8211;version</code></p>
<dd> Print version information.</p>
<dt><code>-v</code>,&nbsp;<wbr><code>&#8211;verify</code></p>
<dd> Verify program in device against file specified with &#8211;file option.</p>
<dt><code>-w</code>,&nbsp;<wbr><code>&#8211;debugwire</code></p>
<dd> Connect to JTAG ICE mkII (or AVR Dragon), talking debugWire protocol to the target. This option implies the <code>-2</code> option. See the DEBUGWIRE section below.</p>
<dt><code>-W</code>,&nbsp;<wbr><code>&#8211;write-fuses</code>&nbsp;<wbr>&lt;eehhll&gt;</p>
<dd> Write fuses bytes. <code>ee</code> is the extended fuse byte, <code>hh</code> is the high fuse byte and <code>ll</code> is the low fuse byte. The fuse byte data must be given in two digit hexidecimal format with zero padding if needed. All three bytes must currently be given.</p>
<dt><code>-x</code>,&nbsp;<wbr><code>&#8211;xmega</code></p>
<dd> The target device is an ATxmega part. Since the ATxmega uses a different JTAG communication than other AVRs, the normal device autodetection based on the JTAG ID does not work. If the device has been explicitly selected through the -P option, it is not necessary to also specify the -x option.<br />
 <code>NOTE:</code> Current, if the target device doesn&#8217;t have an extended fuse byte (e.g. the atmega16), the you should set ee==ll when writing the fuse bytes.</dl>
<p> <i>HOST_NAME</i> defaults to 0.0.0.0 (listen on any interface) if not given. </p>
<p> :<i>PORT</i> is required to put avarice into gdb server mode.</p>
<h2>EXAMPLE USAGE</h2>
<p> avarice &#8211;erase &#8211;program &#8211;file test.bin &#8211;jtag /dev/ttyS0 :4242 </p>
<p> Program the file <i>test.bin</i> into the JTAG ICE (mkI) connected to /dev/ttyS0 after erasing the device, then listen in GDB mode on the local port 4242. </p>
<p> avarice &#8211;jtag usb:1234 &#8211;mkII :4242 </p>
<p> Connect to the JTAG ICE mkII attached to USB which serial number ends in <i>1234</i>, and listen in GDB mode on local port 4242.</p>
<h2>DEBUGGING WITH AVARICE</h2>
<p> The JTAG ICE debugging environment has a few restrictions and changes:</p>
<dl>
<dt>*</p>
<dd> No &quot;soft&quot; breakpoints, and only three hardware breakpoints. The break command sets hardware breakpoints. The easiest way to deal with this restriction is to enable and disable breakpoints as needed.</p>
<dt>*</p>
<dd> Two 1-byte hardware watchpoints (but each hardware watchpoint takes away one hardware breakpoint). If you set a watchpoint on a variable which takes more than one byte, execution will be abysmally slow. Instead it is better to do the following:</p>
<dt>
<dd>
<dl>
<dt>
<dd> watch *(char *)&amp;myvariable</dl>
<dt>
<dd> which watches the least significant byte of <code>myvariable</code>.</p>
<dt>*</p>
<dd> The Atmel AVR processors have a Harvard architecture (separate code and data buses). To distinguish data address 0 from code address 0, <code>avr-gdb</code> adds 0x800000 to all data addresses. Bear this in mind when examining printed pointers, or when passing absolute addresses to gdb commands.</dl>
<h2>DEBUGWIRE</h2>
<p> The <i>debugWire</i> protocol is a proprietary protocol introduced by Atmel to allow debugging small AVR controllers that don&#8217;t offer enough pins (and enough chip resources) to implement full JTAG. The communication takes place over the <i>/RESET</i> pin which needs to be turned into a debugWire connection pin by programming the <i>DWEN</i> fuse (debugWire enable), using a normal programmer connection (in-system programming, high-voltage programming). Note that by enabling this fuse, the standard reset functionality of that pin will be lost, so any in-system programming will cease to work as it requires a functional <i>/RESET</i> pin. Thus it should be made <code>absolutely sure there is a way back</code>, like a device (as the STK500, for example) that can handle high-voltage programming of the AVR. Currently, <code>avarice</code> offers no option to turn off the DWEN fuse. However, <code>avrdude</code> offers the option to turn it off either through high-voltage programming, or by using the JTAG ICE mkII to first turn the target into an ISP-compatible mode, and then using normal ISP commands to change the fuse settings.<br />
 Note that the debugWire environment is further limited, compared to JTAG. It does not offer hardware breakpoints, so all breakpoints have to be implemented as software breakpoints by rewriting flash pages using <i>BREAK</i> instructions. (Software breakpoints are currently not implemented by <code>avarice</code>.) Some memory spaces (fuse and lock bits) are not accessible through the debugWire protocol.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gdb/">gdb</a></code>(1), <code><a href="/docs/linux/man/1-avrdude/">avrdude</a></code>(1), <code><a href="/docs/linux/man/1-avr-gdb/">avr-gdb</a></code>(1), <code><a href="/docs/linux/man/1-insight/">insight</a></code>(1), <code><a href="/docs/linux/man/1-avr-insight/">avr-insight</a></code>(1), <code><a href="/docs/linux/man/1-ice-gdb/">ice-gdb</a></code>(1), <code><a href="/docs/linux/man/1-ice-insight/">ice-insight</a></code>(1)</p>
<h2>AUTHORS</h2>
<p> Avarice (up to version 1.5) was originally written by Scott Finneran with help from Peter Jansen. They did the work of figuring out the jtagice communication protocol before Atmel released the spec (appnote AVR060). </p>
<p> David Gay made major improvements bringing avarice up to 2.0. </p>
<p> Joerg Wunsch reworked the code to abstract the JTAG ICE communication from the remainder, and then extended the code to support the JTAG ICE mkII protocol (see Atmel appnote AVR067). </p>
<h2>Index</h2>
