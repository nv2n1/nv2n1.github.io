---
title: "avrdude(1)"
name: "avrdude"
section: "1"
letter: "a"
url: "/docs/linux/man/1-avrdude/"
description: "avrdude – driver program for “simple” Atmel AVR MCU programmer"
---

<h2 class="name">NAME</h2>
<p> <code>avrdude</code> &#8211; driver program for &#8220;simple&#8221; Atmel AVR MCU programmer </p>
<h2>SYNOPSIS</h2>
<p> &#8211;<code>p </code><i>partno</i> [-<code>b </code><i>baudrate</i> ] [-<code>B </code><i>bitclock</i> ] [-<code>c </code><i>programmer-id</i> ] [-<code>C </code><i>config-file</i> ] [-<code>D</code> ] [-<code>e</code> ] [-<code>E </code><i>exitspec </i>[, <i>exitspec</i> ] ] [-<code>F</code> ] [-<code>i </code><i>delay</i> ] [-<code>n</code> ] [-<code>O</code> ] [-<code>P </code><i>port</i> ] [-<code>q</code> ] [-<code>s</code> ] [-<code>t</code> ] [-<code>u</code> ] [-<code>U </code><i>memtype:op:filename:filefmt</i> ] [-<code>v</code> ] [-<code>x </code><i>extended_param</i> ] [-<code>V</code> ] [-<code>y</code> ] [-<code>Y</code> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>Avrdude</code> is a program for downloading code and data to Atmel AVR microcontrollers. <code>Avrdude</code> supports Atmel&#8217;s STK500 programmer, Atmel&#8217;s AVRISP and AVRISP mkII devices, Atmel&#8217;s STK600, Atmel&#8217;s JTAG ICE (both mkI and mkII, the latter also in ISP mode), programmers complying to AppNote AVR910 and AVR109 (including the Butterfly), as well as a simple hard-wired programmer connected directly to a <a href="/docs/linux/man/4-ppi/">ppi</a>(4) or <a href="/docs/linux/man/4-parport/">parport</a>(4) parallel port, or to a standard serial port. In the simplest case, the hardware consists just of a cable connecting the respective AVR signal lines to the parallel port. </p>
<p> The MCU is programmed in <i>serial programming mode</i> so, for the <a href="/docs/linux/man/4-ppi/">ppi</a>(4) based programmer, the MCU signals `/RESET&#8217; , `SCK&#8217; , `MISO&#8217; and `MOSI&#8217; need to be connected to the parallel port. Optionally, some otherwise unused output pins of the parallel port can be used to supply power for the MCU part, so it is also possible to construct a passive stand-alone programming device. Some status LEDs indicating the current operating state of the programmer can be connected, and a signal is available to control a buffer/driver IC 74LS367 (or 74HCT367). The latter can be useful to decouple the parallel port from the MCU when in-system programming is used. </p>
<p> A number of equally simple bit-bang programming adapters that connect to a serial port are supported as well, among them the popular Ponyprog serial adapter, and the DASA and DASA3 adapters that used to be supported by <a href="/docs/linux/man/1-uisp/">uisp</a>(1). Note that these adapters are meant to be attached to a physical serial port. Connecting to a serial port emulated on top of USB is likely to not work at all, or to work abysmally slow. </p>
<p> Atmel&#8217;s STK500 programmer is also supported and connects to a serial port. Both, firmware versions 1.x and 2.x can be handled, but require a different programmer type specification (by now). Using firmware version 2, high-voltage programming is also supported, both parallel and serial (programmer types stk500pp and stk500hvsp). </p>
<p> Wiring boards are supported, utilizing STK500 V2.x protocol, but a simple DTR/RTS toggle is used to set the boards into programming mode. The programmer type is &#8220;wiring&#8221;. </p>
<p> The Arduino (which is very similar to the STK500 1.x) is supported via its own programmer type specification &#8220;arduino&#8221;. </p>
<p> The BusPirate is a versatile tool that can also be used as an AVR programmer. A single BusPirate can be connected to up to 3 independent AVRs. See the section on <i>extended parameters</i> below for details. </p>
<p> Atmel&#8217;s STK600 programmer is supported in ISP and high-voltage programming modes, and connects through the USB. For ATxmega devices, the STK600 is supported in PDI mode. For ATtiny4/5/9/10 devices, the STK600 and AVRISP mkII are supported in TPI mode. </p>
<p> The simple serial programmer described in Atmel&#8217;s application note AVR910, and the bootloader described in Atmel&#8217;s application note AVR109 (which is also used by the AVR Butterfly evaluation board), are supported on a serial port. </p>
<p> Atmel&#8217;s JTAG ICE (both mkI and mkII) is supported as well to up- or download memory areas from/to an AVR target (no support for on-chip debugging). For the JTAG ICE mkII, JTAG, debugWire and ISP mode are supported, provided it has a firmware revision of at least 4.14 (decimal). See below for the limitations of debugWire. For ATxmega devices, the JTAG ICE mkII is supported in PDI mode, provided it has a revision 1 hardware and firmware version of at least 5.37 (decimal). </p>
<p> The AVR Dragon is supported in all modes (ISP, JTAG, HVSP, PP, debugWire). When used in JTAG and debugWire mode, the AVR Dragon behaves similar to a JTAG ICE mkII, so all device-specific comments for that device will apply as well. When used in ISP mode, the AVR Dragon behaves similar to an AVRISP mkII (or JTAG ICE mkII in ISP mode), so all device-specific comments will apply there. In particular, the Dragon starts out with a rather fast ISP clock frequency, so the &#8211;<code>B </code><i>bitclock</i> option might be required to achieve a stable ISP communication. For ATxmega devices, the AVR Dragon is supported in PDI mode, provided it has a firmware version of at least 6.11 (decimal). </p>
<p> The avrftdi, USBasp ISP and USBtinyISP adapters are also supported, provided <code>avrdude</code> has been compiled with libusb support. USBasp ISP and USBtinyISP both feature simple firmware-only USB implementations, running on an ATmega8 (or ATmega88), or ATtiny2313, respectively. If libftdi has has been compiled in <code>avrdude</code> the avrftdi device adds support for many programmers using FTDI&#8217;s 2232C/D/H and 4232H parts running in MPSSE mode, which hard-codes (in the chip) SCK to bit 1, MOSI to bit 2, and MISO to bit 3. Reset is usually bit 4. </p>
<p> Input files can be provided, and output files can be written in different file formats, such as raw binary files containing the data to download to the chip, Intel hex format, or Motorola S-record format. There are a number of tools available to produce those files, like <a href="/docs/linux/man/1-asl/">asl</a>(1) as a standalone assembler, or avr-objcopy1 for the final stage of the GNU toolchain for the AVR microcontroller. </p>
<p> <code>Avrdude</code> can program the EEPROM and flash ROM memory cells of supported AVR parts. Where supported by the serial instruction set, fuse bits and lock bits can be programmed as well. These are implemented within as separate memory types and can be programmed using data from a file (see the &#8211;<code>m</code> option) or from terminal mode (see the <i>dump</i> and <i>write</i> commands). It is also possible to read the chip (provided it has not been code-protected previously, of course) and store the data in a file. Finally, a &#8220;terminal&#8221; mode is available that allows one to interactively communicate with the MCU, and to display or program individual memory cells. On the STK500 and STK600 programmer, several operational parameters (target supply voltage, target Aref voltage, master clock) can be examined and changed from within terminal mode as well.</p>
<h3>Options</h3>
<p> In order to control all the different operation modi, a number of options need to be specified to <code>avrdude</code></p>
<dl>
<dt><code>-p </code><i>partno</i></p>
<dd> This is the only option that is mandatory for every invocation of <code>avrdude</code> It specifies the type of the MCU connected to the programmer. These are read from the config file. If <code>avrdude</code> does not know about a part that you have, simply add it to the config file (be sure and submit a patch back to the author so that it can be incorporated for the next version). See the sample config file for the format. Currently, the following MCU types are understood: </p>
<table>
<tr VALIGN=top>
<td><code>Option tag</code></td>
<td><code>Official part name</code>
</td>
</tr>
<tr VALIGN=top>
<td>1200</td>
<td>AT90S1200 (****)
</td>
</tr>
<tr VALIGN=top>
<td>2313</td>
<td>AT90S2313
</td>
</tr>
<tr VALIGN=top>
<td>2333</td>
<td>AT90S2333
</td>
</tr>
<tr VALIGN=top>
<td>2343</td>
<td>AT90S2343 (*)
</td>
</tr>
<tr VALIGN=top>
<td>4414</td>
<td>AT90S4414
</td>
</tr>
<tr VALIGN=top>
<td>4433</td>
<td>AT90S4433
</td>
</tr>
<tr VALIGN=top>
<td>4434</td>
<td>AT90S4434
</td>
</tr>
<tr VALIGN=top>
<td>8515</td>
<td>AT90S8515
</td>
</tr>
<tr VALIGN=top>
<td>8535</td>
<td>AT90S8535
</td>
</tr>
<tr VALIGN=top>
<td>c128</td>
<td>AT90CAN128
</td>
</tr>
<tr VALIGN=top>
<td>c32</td>
<td>AT90CAN32
</td>
</tr>
<tr VALIGN=top>
<td>c64</td>
<td>AT90CAN64
</td>
</tr>
<tr VALIGN=top>
<td>m103</td>
<td>ATmega103
</td>
</tr>
<tr VALIGN=top>
<td>m128</td>
<td>ATmega128
</td>
</tr>
<tr VALIGN=top>
<td>m1280</td>
<td>ATmega1280
</td>
</tr>
<tr VALIGN=top>
<td>m1281</td>
<td>ATmega1281
</td>
</tr>
<tr VALIGN=top>
<td>m1284p</td>
<td>ATmega1284P
</td>
</tr>
<tr VALIGN=top>
<td>m128rfa1</td>
<td>ATmega128RFA1
</td>
</tr>
<tr VALIGN=top>
<td>m16</td>
<td>ATmega16
</td>
</tr>
<tr VALIGN=top>
<td>m161</td>
<td>ATmega161
</td>
</tr>
<tr VALIGN=top>
<td>m162</td>
<td>ATmega162
</td>
</tr>
<tr VALIGN=top>
<td>m163</td>
<td>ATmega163
</td>
</tr>
<tr VALIGN=top>
<td>m164</td>
<td>ATmega164
</td>
</tr>
<tr VALIGN=top>
<td>m164p</td>
<td>ATmega164P
</td>
</tr>
<tr VALIGN=top>
<td>m168</td>
<td>ATmega168
</td>
</tr>
<tr VALIGN=top>
<td>m168p</td>
<td>ATmega168P
</td>
</tr>
<tr VALIGN=top>
<td>m169</td>
<td>ATmega169
</td>
</tr>
<tr VALIGN=top>
<td>m16u2</td>
<td>ATmega16U2
</td>
</tr>
<tr VALIGN=top>
<td>m2560</td>
<td>ATmega2560 (**)
</td>
</tr>
<tr VALIGN=top>
<td>m2561</td>
<td>ATmega2561 (**)
</td>
</tr>
<tr VALIGN=top>
<td>m32</td>
<td>ATmega32
</td>
</tr>
<tr VALIGN=top>
<td>m324p</td>
<td>ATmega324P
</td>
</tr>
<tr VALIGN=top>
<td>m325</td>
<td>ATmega325
</td>
</tr>
<tr VALIGN=top>
<td>m3250</td>
<td>ATmega3250
</td>
</tr>
<tr VALIGN=top>
<td>m328p</td>
<td>ATmega328P
</td>
</tr>
<tr VALIGN=top>
<td>m329</td>
<td>ATmega329
</td>
</tr>
<tr VALIGN=top>
<td>m3290</td>
<td>ATmega3290
</td>
</tr>
<tr VALIGN=top>
<td>m329p</td>
<td>ATmega329P
</td>
</tr>
<tr VALIGN=top>
<td>m3290p</td>
<td>ATmega3290P
</td>
</tr>
<tr VALIGN=top>
<td>m32u2</td>
<td>ATmega32U2
</td>
</tr>
<tr VALIGN=top>
<td>m32u4</td>
<td>ATmega32U4
</td>
</tr>
<tr VALIGN=top>
<td>m48</td>
<td>ATmega48
</td>
</tr>
<tr VALIGN=top>
<td>m64</td>
<td>ATmega64
</td>
</tr>
<tr VALIGN=top>
<td>m640</td>
<td>ATmega640
</td>
</tr>
<tr VALIGN=top>
<td>m644p</td>
<td>ATmega644P
</td>
</tr>
<tr VALIGN=top>
<td>m644</td>
<td>ATmega644
</td>
</tr>
<tr VALIGN=top>
<td>m645</td>
<td>ATmega645
</td>
</tr>
<tr VALIGN=top>
<td>m6450</td>
<td>ATmega6450
</td>
</tr>
<tr VALIGN=top>
<td>m649</td>
<td>ATmega649
</td>
</tr>
<tr VALIGN=top>
<td>m6490</td>
<td>ATmega6490
</td>
</tr>
<tr VALIGN=top>
<td>m8</td>
<td>ATmega8
</td>
</tr>
<tr VALIGN=top>
<td>m8515</td>
<td>ATmega8515
</td>
</tr>
<tr VALIGN=top>
<td>m8535</td>
<td>ATmega8535
</td>
</tr>
<tr VALIGN=top>
<td>m88</td>
<td>ATmega88
</td>
</tr>
<tr VALIGN=top>
<td>m88p</td>
<td>ATmega88P
</td>
</tr>
<tr VALIGN=top>
<td>m8u2</td>
<td>ATmega8U2
</td>
</tr>
<tr VALIGN=top>
<td>pwm2</td>
<td>AT90PWM2
</td>
</tr>
<tr VALIGN=top>
<td>pwm2b</td>
<td>AT90PWM2B
</td>
</tr>
<tr VALIGN=top>
<td>pwm3</td>
<td>AT90PWM3
</td>
</tr>
<tr VALIGN=top>
<td>pwm3b</td>
<td>AT90PWM3B
</td>
</tr>
<tr VALIGN=top>
<td>t10</td>
<td>ATtiny10
</td>
</tr>
<tr VALIGN=top>
<td>t12</td>
<td>ATtiny12 (***)
</td>
</tr>
<tr VALIGN=top>
<td>t13</td>
<td>ATtiny13
</td>
</tr>
<tr VALIGN=top>
<td>t15</td>
<td>ATtiny15
</td>
</tr>
<tr VALIGN=top>
<td>t2313</td>
<td>ATtiny2313
</td>
</tr>
<tr VALIGN=top>
<td>t25</td>
<td>ATtiny25
</td>
</tr>
<tr VALIGN=top>
<td>t26</td>
<td>ATtiny26
</td>
</tr>
<tr VALIGN=top>
<td>t261</td>
<td>ATtiny261
</td>
</tr>
<tr VALIGN=top>
<td>t4</td>
<td>ATtiny4
</td>
</tr>
<tr VALIGN=top>
<td>t4313</td>
<td>ATtiny4313
</td>
</tr>
<tr VALIGN=top>
<td>t44</td>
<td>ATtiny44
</td>
</tr>
<tr VALIGN=top>
<td>t45</td>
<td>ATtiny45
</td>
</tr>
<tr VALIGN=top>
<td>t461</td>
<td>ATtiny461
</td>
</tr>
<tr VALIGN=top>
<td>t5</td>
<td>ATtiny5
</td>
</tr>
<tr VALIGN=top>
<td>t84</td>
<td>ATtiny84
</td>
</tr>
<tr VALIGN=top>
<td>t85</td>
<td>ATtiny85
</td>
</tr>
<tr VALIGN=top>
<td>t861</td>
<td>ATtiny861
</td>
</tr>
<tr VALIGN=top>
<td>t88</td>
<td>ATtiny88
</td>
</tr>
<tr VALIGN=top>
<td>t9</td>
<td>ATtiny9
</td>
</tr>
<tr VALIGN=top>
<td>ucr2</td>
<td>AT32uca0512
</td>
</tr>
<tr VALIGN=top>
<td>usb1286</td>
<td>ATmega1286
</td>
</tr>
<tr VALIGN=top>
<td>usb1287</td>
<td>ATmega1287
</td>
</tr>
<tr VALIGN=top>
<td>usb162</td>
<td>ATmega162
</td>
</tr>
<tr VALIGN=top>
<td>usb646</td>
<td>ATmega647
</td>
</tr>
<tr VALIGN=top>
<td>usb647</td>
<td>ATmega647
</td>
</tr>
<tr VALIGN=top>
<td>usb82</td>
<td>ATmega82
</td>
</tr>
<tr VALIGN=top>
<td>x128a1</td>
<td>ATxmega128A1
</td>
</tr>
<tr VALIGN=top>
<td>x128a1d</td>
<td>ATxmega128A1revD
</td>
</tr>
<tr VALIGN=top>
<td>x128a3</td>
<td>ATxmega128A3
</td>
</tr>
<tr VALIGN=top>
<td>x128a4</td>
<td>ATxmega128A4
</td>
</tr>
<tr VALIGN=top>
<td>x16a4</td>
<td>ATxmega16A4
</td>
</tr>
<tr VALIGN=top>
<td>x192a1</td>
<td>ATxmega192A1
</td>
</tr>
<tr VALIGN=top>
<td>x192a3</td>
<td>ATxmega192A3
</td>
</tr>
<tr VALIGN=top>
<td>x256a1</td>
<td>ATxmega256A1
</td>
</tr>
<tr VALIGN=top>
<td>x256a3</td>
<td>ATxmega256A3
</td>
</tr>
<tr VALIGN=top>
<td>x256a3b</td>
<td>ATxmega256A3B
</td>
</tr>
<tr VALIGN=top>
<td>x32a4</td>
<td>ATxmega32A4
</td>
</tr>
<tr VALIGN=top>
<td>x64a1</td>
<td>ATxmega64A1
</td>
</tr>
<tr VALIGN=top>
<td>x64a3</td>
<td>ATxmega64A3
</td>
</tr>
<tr VALIGN=top>
<td>x64a4</td>
<td>ATxmega64A4
</td>
</tr>
</table>
<dl>
<dt><code>&quot;(*)&quot;</code></p>
<dd> The AT90S2323 and ATtiny22 use the same algorithm.</p>
<dt><code>&quot;(**)&quot;</code></p>
<dd> Flash addressing above 128 KB is not supported by all programming hardware. Known to work are jtag2, stk500v2, and bit-bang programmers.</p>
<dt><code>&quot;(***)&quot;</code></p>
<dd> The ATtiny11 uses the same algorithm, but can only be programmed in high-voltage serial mode.</p>
<dt><code>&quot;(****)&quot;</code></p>
<dd> The ISP programming protocol of the AT90S1200 differs in subtle ways from that of other AVRs. Thus, not all programmers support this device. Known to work are all direct bitbang programmers, and all programmers talking the STK500v2 protocol.</dl>
<dt><code>-b </code><i>baudrate</i></p>
<dd> Override the RS-232 connection baud rate specified in the respective programmer&#8217;s entry of the configuration file.</p>
<dt><code>-B </code><i>bitclock</i></p>
<dd> Specify the bit clock period for the JTAG interface or the ISP clock (JTAG ICE only). The value is a floating-point number in microseconds. The default value of the JTAG ICE results in about 1 microsecond bit clock period, suitable for target MCUs running at 4 MHz clock and above. Unlike certain parameters in the STK500, the JTAG ICE resets all its parameters to default values when the programming software signs off from the ICE, so for MCUs running at lower clock speeds, this parameter must be specified on the command-line. You can use the &#8216;default_bitclock&#8217; keyword in your ${HOME}/.avrduderc file to assign a default value to keep from having to specify this option on every invocation.</p>
<dt><code>-c </code><i>programmer-id</i></p>
<dd> Use the pin configuration specified by the argument. Pin configurations are read from the config file (see the &#8211;<code>C</code> option). New pin configurations can be easily added or modified through the use of a config file to make <code>avrdude</code> work with different programmers as long as the programmer supports the Atmel AVR serial program method. You can use the &#8216;default_programmer&#8217; keyword in your ${HOME}/.avrduderc file to assign a default programmer to keep from having to specify this option on every invocation.</p>
<dt><code>-C </code><i>config-file</i></p>
<dd> Use the specified config file to load configuration data. This file contains all programmer and part definitions that <code>avrdude</code> knows about. If you have a programmer or part that <code>avrdude</code> does not know about, you can add it to the config file (be sure and submit a patch back to the author so that it can be incorporated for the next version). See the config file, located at ${PREFIX}/etc/avrdude/avrdude.conf which contains a description of the format.</p>
<dt><code>-D</code></p>
<dd> Disable auto erase for flash. When the &#8211;<code>U</code> option with flash memory is specified, will perform a chip erase before starting any of the programming operations, since it generally is a mistake to program the flash without performing an erase first. This option disables that. Auto erase is not used for ATxmega devices as these devices can use page erase before writing each page so no explicit chip erase is required. Note however that any page not affected by the current operation will retain its previous contents.</p>
<dt><code>-e</code></p>
<dd> Causes a chip erase to be executed. This will reset the contents of the flash ROM and EEPROM to the value `0xff&#8217; , and clear all lock bits. Except for ATxmega devices which can use page erase, it is basically a prerequisite command before the flash ROM can be reprogrammed again. The only exception would be if the new contents would exclusively cause bits to be programmed from the value `1&#8242; to `0&#8242; Note that in order to reprogram EERPOM cells, no explicit prior chip erase is required since the MCU provides an auto-erase cycle in that case before programming the cell.</p>
<dt><code> -E </code><i>exitspec </i>[, <i>exitspec</i> ]</p>
<dd>
<dd>By default, leaves the parallel port in the same state at exit as it has been found at startup. This option modifies the state of the `/RESET&#8217; and `Vcc&#8217; lines the parallel port is left at, according to the <i>exitspec</i> arguments provided, as follows:</p>
<dl>
<dt><i>reset</i></p>
<dd> The `/RESET&#8217; signal will be left activated at program exit, that is it will be held <i>low</i> in order to keep the MCU in reset state afterwards. Note in particular that the programming algorithm for the AT90S1200 device mandates that the `/RESET&#8217; signal is active <i>before</i> powering up the MCU, so in case an external power supply is used for this MCU type, a previous invocation of with this option specified is one of the possible ways to guarantee this condition.</p>
<dt><i>noreset</i></p>
<dd> The `/RESET&#8217; line will be deactivated at program exit, thus allowing the MCU target program to run while the programming hardware remains connected.</p>
<dt><i>vcc</i></p>
<dd> This option will leave those parallel port pins active (i. e. <i>high</i> ) that can be used to supply `Vcc&#8217; power to the MCU.</p>
<dt><i>novcc</i></p>
<dd> This option will pull the `Vcc&#8217; pins of the parallel port down at program exit.</p>
<dt><i>d_high</i></p>
<dd> This option will leave the 8 data pins on the parallel port active. (i. e. <i>high</i> )</p>
<dt><i>d_low</i></p>
<dd> This option will leave the 8 data pins on the parallel port inactive. (i. e. <i>low</i> )</dl>
<p> Multiple <i>exitspec</i> arguments can be separated with commas.</p>
<dt><code>-F</code></p>
<dd> Normally, tries to verify that the device signature read from the part is reasonable before continuing. Since it can happen from time to time that a device has a broken (erased or overwritten) device signature but is otherwise operating normally, this options is provided to override the check. Also, for programmers like the Atmel STK500 and STK600 which can adjust parameters local to the programming tool (independent of an actual connection to a target controller), this option can be used together with &#8211;<code>t</code> to continue in terminal mode.</p>
<dt><code>-i </code><i>delay</i></p>
<dd> For bitbang-type programmers, delay for approximately <i>delay</i> microseconds between each bit state change. If the host system is very fast, or the target runs off a slow clock (like a 32 kHz crystal, or the 128 kHz internal RC oscillator), this can become necessary to satisfy the requirement that the ISP clock frequency must not be higher than 1/4 of the CPU clock frequency. This is implemented as a spin-loop delay to allow even for very short delays. On Unix-style operating systems, the spin loop is initially calibrated against a system timer, so the number of microseconds might be rather realistic, assuming a constant system load while is running. On Win32 operating systems, a preconfigured number of cycles per microsecond is assumed that might be off a bit for very fast or very slow machines.</p>
<dt><code>-n</code></p>
<dd> No-write &#8211; disables actually writing data to the MCU (useful for debugging <code>avrdude</code> ).</p>
<dt><code>-O</code></p>
<dd> Perform a RC oscillator run-time calibration according to Atmel application note AVR053. This is only supported on the STK500v2, AVRISP mkII, and JTAG ICE mkII hardware. Note that the result will be stored in the EEPROM cell at address 0.</p>
<dt><code>-P </code><i>port</i></p>
<dd> Use <i>port</i> to identify the device to which the programmer is attached. By default the /dev/ppi0 port is used, but if the programmer type normally connects to the serial port, the /dev/cuaa0 port is the default. If you need to use a different parallel or serial port, use this option to specify the alternate port name. </p>
<p> On Win32 operating systems, the parallel ports are referred to as lpt1 through lpt3, referring to the addresses 0x378, 0x278, and 0x3BC, respectively. If the parallel port can be accessed through a different address, this address can be specified directly, using the common C language notation (i. e., hexadecimal values are prefixed by `0x&#8217; ). </p>
<p> For the JTAG ICE mkII, if has been configured with libusb support, <i>port</i> can alternatively be specified as usb [: <i>serialno</i> ] This will cause to search a JTAG ICE mkII on USB. If <i>serialno</i> is also specified, it will be matched against the serial number read from any JTAG ICE mkII found on USB. The match is done after stripping any existing colons from the given serial number, and right-to-left, so only the least significant bytes from the serial number need to be given. </p>
<p> As the AVRISP mkII device can only be talked to over USB, the very same method of specifying the port is required there. </p>
<p> For the USB programmer &quot;AVR-Doper&quot; running in HID mode, the port must be specified as <i>avrdoper.</i> Libusb support is required on Unix but not on Windows. For more information about AVR-Doper see <a rel="nofollow" href="http://www.obdev.at/avrusb/avrdoper.html.">http://www.obdev.at/avrusb/avrdoper.html.</a> </p>
<p> For the USBtinyISP, which is a simplicistic device not implementing serial numbers, multiple devices can be distinguished by their location in the USB hierarchy. See the the respective <i>Troubleshooting</i> entry in the detailed documentation for examples. </p>
<p> For programmers that attach to a serial port using some kind of higher level protocol (as opposed to bit-bang style programmers), <i>port</i> can be specified as net <code>: </code><i>host </i><code>: </code><i>port</i> In this case, instead of trying to open a local device, a TCP network connection to (TCP) <i>port</i> on <i>host</i> is established. The remote endpoint is assumed to be a terminal or console server that connects the network stream to a local serial port where the actual programmer has been attached to. The port is assumed to be properly configured, for example using a transparent 8-bit data connection without parity at 115200 Baud for a STK500. <i>This feature is currently not implemented for Win32 systems.</i></p>
<dt><code>-q</code></p>
<dd> Disable (or quell) output of the progress bar while reading or writing to the device. Specify it a second time for even quieter operation.</p>
<dt><code>-s</code></p>
<dd> Disable safemode prompting. When safemode discovers that one or more fuse bits have unintentionally changed, it will prompt for confirmation regarding whether or not it should attempt to recover the fuse bit(s). Specifying this flag disables the prompt and assumes that the fuse bit(s) should be recovered without asking for confirmation first.</p>
<dt><code>-t</code></p>
<dd> Tells to enter the interactive &#8220;terminal&#8221; mode instead of up- or downloading files. See below for a detailed description of the terminal mode.</p>
<dt><code>-u</code></p>
<dd> Disable the safemode fuse bit checks. Safemode is enabled by default and is intended to prevent unintentional fuse bit changes. When enabled, safemode will issue a warning if the any fuse bits are found to be different at program exit than they were when was invoked. Safemode won&#8217;t alter fuse bits itself, but rather will prompt for instructions, unless the terminal is non-interactive, in which case safemode is disabled. See the &#8211;<code>s</code> option to disable safemode prompting.</p>
<dt><code> -U </code><i>memtype </i><i>: </i><i>op </i><i>: </i><i>filename </i>[: <i>format</i> ]</p>
<dd>
<dd>Perform a memory operation as indicated. The <i>memtype</i> field specifies the memory type to operate on. The available memory types are device-dependent, the actual configuration can be viewed with the <code>part</code> command in terminal mode. Typically, a device&#8217;s memory configuration at least contains the memory types <i>flash</i> and <i>eeprom</i> All memory types currently known are:</p>
<dl>
<dt><code>calibration</code></p>
<dd> One or more bytes of RC oscillator calibration data.</p>
<dt><code>eeprom</code></p>
<dd> The EEPROM of the device.</p>
<dt><code>efuse</code></p>
<dd> The extended fuse byte.</p>
<dt><code>flash</code></p>
<dd> The flash ROM of the device.</p>
<dt><code>fuse</code></p>
<dd> The fuse byte in devices that have only a single fuse byte.</p>
<dt><code>hfuse</code></p>
<dd> The high fuse byte.</p>
<dt><code>lfuse</code></p>
<dd> The low fuse byte.</p>
<dt><code>lock</code></p>
<dd> The lock byte.</p>
<dt><code>signature</code></p>
<dd> The three device signature bytes (device ID).</p>
<dt><code>fuse </code><i>N</i></p>
<dd> The fuse bytes of ATxmega devices, <i>N</i> is an integer number for each fuse supported by the device.</p>
<dt><code>application</code></p>
<dd> The application flash area of ATxmega devices.</p>
<dt><code>apptable</code></p>
<dd> The application table flash area of ATxmega devices.</p>
<dt><code>boot</code></p>
<dd> The boot flash area of ATxmega devices.</p>
<dt><code>prodsig</code></p>
<dd> The production signature (calibration) area of ATxmega devices.</p>
<dt><code>usersig</code></p>
<dd> The user signature area of ATxmega devices.</dl>
<p> The <i>op</i> field specifies what operation to perform:</p>
<dl>
<dt><i>r</i></p>
<dd> read device memory and write to the specified file</p>
<dt><i>w</i></p>
<dd> read data from the specified file and write to the device memory</p>
<dt><i>v</i></p>
<dd> read data from both the device and the specified file and perform a verify</dl>
<p> The <i>filename</i> field indicates the name of the file to read or write. The <i>format</i> field is optional and contains the format of the file to read or write. <i>Format</i> can be one of:</p>
<dl>
<dt><i>i</i></p>
<dd> Intel Hex</p>
<dt><i>s</i></p>
<dd> Motorola S-record</p>
<dt><i>r</i></p>
<dd> raw binary; little-endian byte order, in the case of the flash ROM data</p>
<dt><i>m</i></p>
<dd> immediate; actual byte values specified on the command line, separated by commas or spaces. This is good for programming fuse bytes without having to create a single-byte file or enter terminal mode.</p>
<dt><i>a</i></p>
<dd> auto detect; valid for input only, and only if the input is not provided at <i>stdin</i></p>
<dt><i>d</i></p>
<dd> decimal; this and the following formats are only valid on output. They generate one line of output for the respective memory section, forming a comma-separated list of the values. This can be particularly useful for subsequent processing, like for fuse bit settings.</p>
<dt><i>h</i></p>
<dd> hexadecimal; each value will get the string <i>0x</i> prepended.</p>
<dt><i>o</i></p>
<dd> octal; each value will get a <i>0</i> prepended unless it is less than 8 in which case it gets no prefix.</p>
<dt><i>b</i></p>
<dd> binary; each value will get the string <i>0b</i> prepended.</dl>
<p> The default is to use auto detection for input files, and raw binary format for output files. Note that if <i>filename</i> contains a colon, the <i>format</i> field is no longer optional since the filename part following the colon would otherwise be misinterpreted as <i>format</i> </p>
<p> As an abbreviation, the form &#8211;<code>U </code><i>filename</i> is equivalent to specifying &#8211;<code>U </code><i>flash:w: </i><i>filename </i><code>:a</code> This will only work if <i>filename</i> does not have a colon in it.</p>
<dt><code>-v</code></p>
<dd> Enable verbose output.</p>
<dt><code>-V</code></p>
<dd> Disable automatic verify check when uploading data.</p>
<dt><code>-x </code><i>extended_param</i></p>
<dd> Pass <i>extended_param</i> to the chosen programmer implementation as an extended parameter. The interpretation of the extended parameter depends on the programmer itself. See below for a list of programmers accepting extended parameters.</p>
<dt><code>-y</code></p>
<dd> Tells to use the last four bytes of the connected parts&#8217; EEPROM memory to track the number of times the device has been erased. When this option is used and the &#8211;<code>e</code> flag is specified to generate a chip erase, the previous counter will be saved before the chip erase, it is then incremented, and written back after the erase cycle completes. Presumably, the device would only be erased just before being programmed, and thus, this can be utilized to give an indication of how many erase-rewrite cycles the part has undergone. Since the FLASH memory can only endure a finite number of erase-rewrite cycles, one can use this option to track when a part is nearing the limit. The typical limit for Atmel AVR FLASH is 1000 cycles. Of course, if the application needs the last four bytes of EEPROM memory, this option should not be used.</p>
<dt><code>-Y </code><i>cycles</i></p>
<dd> Instructs to initialize the erase-rewrite cycle counter residing at the last four bytes of EEPROM memory to the specified value. If the application needs the last four bytes of EEPROM memory, this option should not be used.</dl>
<h3>Terminal mode</h3>
<p> In this mode, only initializes communication with the MCU, and then awaits user commands on standard input. Commands and parameters may be abbreviated to the shortest unambiguous form. Terminal mode provides a command history using <a href="/docs/linux/man/3-readline/">readline</a>(3), so previously entered command lines can be recalled and edited. The following commands are currently implemented:</p>
<dl>
<dt><i>dump memtype addr nbytes</i></p>
<dd> Read <i>nbytes</i> bytes from the specified memory area, and display them in the usual hexadecimal and ASCII form.</p>
<dt><i>dump</i></p>
<dd> Continue dumping the memory contents for another <i>nbytes</i> where the previous <i>dump</i> command left off.</p>
<dt><i>write memtype addr byte1 &#8230; byteN</i></p>
<dd> Manually program the respective memory cells, starting at address <i>addr</i> using the values <i>byte1</i> through <i>byteN</i> This feature is not implemented for bank-addressed memories such as the flash memory of ATMega devices.</p>
<dt><i>erase</i></p>
<dd> Perform a chip erase.</p>
<dt><i>send b1 b2 b3 b4</i></p>
<dd> Send raw instruction codes to the AVR device. If you need access to a feature of an AVR part that is not directly supported by <code>,</code> this command allows you to use it, even though does not implement the command. When using direct SPI mode, up to 3 bytes can be omitted.</p>
<dt><i>sig</i></p>
<dd> Display the device signature bytes.</p>
<dt><i>spi</i></p>
<dd> Enter direct SPI mode. The <i>pgmled</i> pin acts as slave select. <i>Only supported on parallel bitbang programmers.</i></p>
<dt><i>part</i></p>
<dd> Display the current part settings and parameters. Includes chip specific information including all memory types supported by the device, read/write timing, etc.</p>
<dt><i>pgm</i></p>
<dd> Return to programming mode (from direct SPI mode).</p>
<dt><i>vtarg voltage</i></p>
<dd> Set the target&#8217;s supply voltage to <i>voltage</i> Volts. <i>Only supported on the STK500 and STK600 programmer.</i></p>
<dt><i>varef </i>[<i>channel voltage</i> ]</p>
<dd> Set the adjustable voltage source to <i>voltage</i> Volts. This voltage is normally used to drive the target&#8217;s <i>Aref</i> input on the STK500. On the Atmel STK600, two reference voltages are available, which can be selected by the optional <i>channel</i> argument (either 0 or 1). <i>Only supported on the STK500 and STK600 programmer.</i></p>
<dt><i>fosc freq </i>[M <code>| k</code> ]</p>
<dd> Set the master oscillator to <i>freq</i> Hz. An optional trailing letter <i>M</i> multiplies by 1E6, a trailing letter <i>k</i> by 1E3. <i>Only supported on the STK500 and STK600 programmer.</i></p>
<dt><i>fosc off</i></p>
<dd> Turn the master oscillator off. <i>Only supported on the STK500 and STK600 programmer.</i></p>
<dt><i>sck period</i></p>
<dd> <i>STK500 and STK600 programmer only:</i> Set the SCK clock period to <i>period</i> microseconds. </p>
<p> <i>JTAG ICE only:</i> Set the JTAG ICE bit clock period to <i>period</i> microseconds. Note that unlike STK500 settings, this setting will be reverted to its default value (approximately 1 microsecond) when the programming software signs off from the JTAG ICE. This parameter can also be used on the JTAG ICE mkII to specify the ISP clock period when operating the ICE in ISP mode.</p>
<dt><i>parms</i></p>
<dd> <i>STK500 and STK600 programmer only:</i> Display the current voltage and master oscillator parameters. </p>
<p> <i>JTAG ICE only:</i> Display the current target supply voltage and JTAG bit clock rate/period.</p>
<dt><i>?</i></p>
<dd>
<dt><i>help</i></p>
<dd> Give a short on-line summary of the available commands.</p>
<dt><i>quit</i></p>
<dd> Leave terminal mode and thus <code>avrdude</code></dl>
<h3>Default Parallel port pin connections</h3>
<p> (these can be changed, see the &#8211;<code>c</code> option) </p>
<table>
<tr VALIGN=top>
<td><code>Pin number</code></td>
<td><code>Function</code>
</td>
</tr>
<tr VALIGN=top>
<td>2-5</td>
<td>Vcc (optional power supply to MCU)
</td>
</tr>
<tr VALIGN=top>
<td>7</td>
<td>/RESET (to MCU)
</td>
</tr>
<tr VALIGN=top>
<td>8</td>
<td>SCK (to MCU)
</td>
</tr>
<tr VALIGN=top>
<td>9</td>
<td>MOSI (to MCU)
</td>
</tr>
<tr VALIGN=top>
<td>10</td>
<td>MISO (from MCU)
</td>
</tr>
<tr VALIGN=top>
<td>18-25</td>
<td>GND
</td>
</tr>
</table>
<h3>debugWire limitations</h3>
<p> The debugWire protocol is Atmel&#8217;s proprietary one-wire (plus ground) protocol to allow an in-circuit emulation of the smaller AVR devices, using the `/RESET&#8217; line. DebugWire mode is initiated by activating the `DWEN&#8217; fuse, and then power-cycling the target. While this mode is mainly intended for debugging/emulation, it also offers limited programming capabilities. Effectively, the only memory areas that can be read or programmed in this mode are flash ROM and EEPROM. It is also possible to read out the signature. All other memory areas cannot be accessed. There is no <i>chip erase</i> functionality in debugWire mode; instead, while reprogramming the flash ROM, each flash ROM page is erased right before updating it. This is done transparently by the JTAG ICE mkII (or AVR Dragon). The only way back from debugWire mode is to initiate a special sequence of commands to the JTAG ICE mkII (or AVR Dragon), so the debugWire mode will be temporarily disabled, and the target can be accessed using normal ISP programming. This sequence is automatically initiated by using the JTAG ICE mkII or AVR Dragon in ISP mode, when they detect that ISP mode cannot be entered.</p>
<h3>Programmers accepting extended parameters</h3>
<dl>
<dt><i>JTAG ICE mkII</i></p>
<dd>
<dt><i>AVR Dragon</i></p>
<dd> When using the JTAG ICE mkII or AVR Dragon in JTAG mode, the following extended parameter is accepted:</p>
<dl>
<dt><i>jtagchain=UB,UA,BB,BA</i></p>
<dd> Setup the JTAG scan chain for <i>UB</i> units before, <i>UA</i> units after, <i>BB</i> bits before, and <i>BA</i> bits after the target AVR, respectively. Each AVR unit within the chain shifts by 4 bits. Other JTAG units might require a different bit shift count.</dl>
<dt><i>AVR910</i></p>
<dd>
<dl>
<dt><i>devcode=VALUE</i></p>
<dd> Override the device code selection by using <i>VALUE</i> as the device code. The programmer is not queried for the list of supported device codes, and the specified <i>VALUE</i> is not verified but used directly within the `T&#8217; command sent to the programmer. <i>VALUE</i> can be specified using the conventional number notation of the C programming language.</dl>
<dl>
<dt><i>no_blockmode</i></p>
<dd> Disables the default checking for block transfer capability. Use <i>no_blockmode</i> only if your <i>AVR910</i> programmer creates errors during initial sequence.</dl>
<dt><i>buspirate</i></p>
<dd>
<dl>
<dt><i>reset={cs,aux,aux2}</i></p>
<dd> The default setup assumes the BusPirate&#8217;s CS output pin connected to the RESET pin on AVR side. It is however possible to have multiple AVRs connected to the same BP with MISO, MOSI and SCK lines common for all of them. In such a case one AVR should have its RESET connected to BusPirate&#8217;s CS pin, second AVR&#8217;s RESET connected to BusPirate&#8217;s AUX pin and if your BusPirate has an AUX2 pin (only available on BusPirate version v1a with firmware 3.0 or newer) use that to activate RESET on the third AVR. </p>
<p> It may be a good idea to decouple the BusPirate and the AVR&#8217;s SPI buses from each other using a 3-state bus buffer. For example 74HC125 or 74HC244 are some good candidates with the latches driven by the appropriate reset pin (cs, aux or aux2). Otherwise the SPI traffic in one active circuit may interfere with programming the AVR in the other design.</p>
<dt><i>speed=&lt;0..7&gt;</i></p>
<dd> BusPirate to AVR SPI speed: </p>
<pre>
0 ..  30 kHz   (default)
1 .. 125 kHz
2 .. 250 kHz
3 ..   1 MHz
4 ..   2 MHz
5 ..   2.6 MHz
6 ..   4 MHz
7 ..   8 MHz
</pre>
<dt><i>ascii</i></p>
<dd> Use ASCII mode even when the firmware supports BinMode (binary mode). BinMode is supported in firmware 2.7 and newer, older FW&#8217;s either don&#8217;t have BinMode or their BinMode is buggy. ASCII mode is slower and makes the above <i>reset=</i> and <i>speed=</i> parameters unavailable.</dl>
<dt><i>Wiring</i></p>
<dd> When using the Wiring programmer type, the following optional extended parameter is accepted:</p>
<dl>
<dt><i>snooze=&lt;0..32767&gt;</i></p>
<dd> After performing the port open phase, AVRDUDE will wait/snooze for <i>snooze</i> milliseconds before continuing to the protocol sync phase. No toggling of DTR/RTS is performed if <i>snooze</i> is greater than 0.</dl>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>/dev/ppi0 </code></p>
<dd> default device to be used for communication with the programming hardware</p>
<dt><code>${PREFIX}/etc/avrdude/avrdude.conf </code></p>
<dd> programmer and parts configuration file</p>
<dt><code>${HOME}/.avrduderc </code></p>
<dd> programmer and parts configuration file (per-user overrides)</p>
<dt><code>~/.inputrc </code></p>
<dd> Initialization file for the <a href="/docs/linux/man/3-readline/">readline</a>(3) library</p>
<dt><code>${PREFIX}/share/doc/avrdude/avrdude.pdf </code></p>
<dd> Schematic of programming hardware</dl>
<h2>DIAGNOSTICS</h2>
<pre>
avrdude: jtagmkII_setparm(): bad response to set parameter command: RSP_FAILED
avrdude: jtagmkII_getsync(): ISP activation failed, trying debugWire
avrdude: Target prepared for ISP, signed off.
avrdude: Please restart avrdude without power-cycling the target.
</pre>
<p> If the target AVR has been set up for debugWire mode (i. e. the <i>DWEN</i> fuse is programmed), normal ISP connection attempts will fail as the <i>/RESET</i> pin is not available. When using the JTAG ICE mkII in ISP mode, the message shown indicates that has guessed this condition, and tried to initiate a debugWire reset to the target. When successful, this will leave the target AVR in a state where it can respond to normal ISP communication again (until the next power cycle). Typically, the same command is going to be retried again immediately afterwards, and will then succeed connecting to the target using normal ISP communication.</p>
<h2>SEE ALSO</h2>
<p> avr-objcopy1, <a href="/docs/linux/man/4-ppi/">ppi</a>(4), <a href="/docs/linux/man/3-readline/">readline</a>(3) </p>
<p> The AVR microcontroller product description can be found at </p>
<blockquote><p><tt>&quot;<a rel="nofollow" href="http://www.atmel.com/products/AVR/">http://www.atmel.com/products/AVR/</a>&quot;</tt></p></blockquote>
<h2>AUTHORS</h2>
<p> <code>Avrdude</code> was written by Brian S. Dean &lt;bsd [at] bsdhome.com&gt;. </p>
<p> This man page by Joerg Wunsch.</p>
<h2>BUGS</h2>
<p> Please report bugs via </p>
<blockquote><p><tt>&quot;<a rel="nofollow" href="http://savannah.nongnu.org/bugs/?group=avrdude">http://savannah.nongnu.org/bugs/?group=avrdude</a>&quot;</tt></p></blockquote>
<p> The JTAG ICE programmers currently cannot write to the flash ROM one byte at a time. For that reason, updating the flash ROM from terminal mode does not work. </p>
<p> Page-mode programming the EEPROM through JTAG (i.e. through an &#8211;<code>U</code> option) requires a prior chip erase. This is an inherent feature of the way JTAG EEPROM programming works. This also applies to the STK500 and STK600 in parallel programming mode. </p>
<p> The USBasp and USBtinyISP drivers do not offer any option to distinguish multiple devices connected simultaneously, so effectively only a single device is supported. </p>
<p> The avrftdi driver allows to select specific devices using any combination of vid,pid serial number (usbsn) vendor description (usbvendoror part description (usbproduct) as seen with lsusb or whatever tool used to view USB device information. Multiple devices can be on the bus at the same time. For the H parts, which have multiple MPSSE interfaces, the interface can also be selected. It defaults to interface &#8216;A&#8217;. </p>
<h2>Index</h2>
