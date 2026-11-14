---
title: "setserial(8)"
name: "setserial"
section: "8"
letter: "s"
url: "/docs/linux/man/8-setserial/"
description: "setserial – get/set Linux serial port information"
---

<p>setserial &#8211; get/set Linux serial port information</p>
<h2>Synopsis</h2>
<p><code>setserial</code> <code>[ -abqvVWz ]</code> device <code>[ </code>parameter1<code> [ </code>arg<code> ] ] &#8230;</code> </p>
<p> <code>setserial -g</code> <code>[ -abGv ]</code> device1 &#8230;</p>
<h2>Description</h2>
<p><code>setserial</code> is a program designed to set and/or report the configuration information associated with a serial port. This information includes what I/O port and IRQ a particular serial port is using, and whether or not the break key should be interpreted as the Secure Attention Key, and so on. During the normal bootup process, only COM ports 1-4 are initialized, using the default I/O ports and IRQ values, as listed below. In order to initialize any additional serial ports, or to change the COM 1-4 ports to a nonstadard configuration, the <code>setserial </code> program should be used. Typically it is called from an <i>rc.serial</i> script, which is usually run out of <i>/etc/rc.local</i>. The <i>device</i> argument or arguments specifies the serial device which should be configured or interrogated. It will usually have the following form: <code>/dev/cua[0-3]</code>. If no parameters are specified, <code>setserial</code> will print out the port type (i.e., 8250, 16450, 16550, 16550A, etc.), the hardware I/O port, the hardware IRQ line, its &quot;baud base,&quot; and some of its operational flags. If the <code>-g</code> option is given, the arguments to setserial are interpreted as a list of devices for which the characteristics of those devices should be printed. Without the <code>-g</code> option, the first argument to setserial is interpreted as the device to be modified or characteristics to be printed, and any additional arguments are interpreted as parameters which should be assigned to that serial device. For the most part, superuser privilege is required to set the configuration parameters of a serial port. A few serial port parameters can be set by normal users, however, and these will be noted as exceptions in this manual page. </p>
<h2>Options</h2>
<p><code>Setserial</code> accepts the following options: </p>
<dl>
<dt><code>-a</code></p>
<dd>When reporting the configuration of a serial device, print all available information.</p>
<dt><code>-b</code></p>
<dd>When reporting the configuration of a serial device, print a summary of the device&#8217;s configuration, which might be suitable for printing during the bootup process, during the /etc/rc script.</p>
<dt><code>-G</code></p>
<dd>Print out the configuration information of the serial port in a form which can be fed back to setserial as command-line arguments.</p>
<dt><code>-q</code></p>
<dd>Be quiet. <code>Setserial</code> will print fewer lines of output.</p>
<dt><code>-v</code></p>
<dd>Be verbose. <code>Setserial</code> will print additional status output.</p>
<dt><code>-V</code></p>
<dd>Display version and exit.</p>
<dt><code>-W</code></p>
<dd>Do wild interrupt initialization and exit. This option is no longer relevant in Linux kernels after version 2.1.</p>
<dt><code>-z</code></p>
<dd>Zero out the serial flags before starting to set flags. This is related to the automatic saving of serial flags using the -G flag. </p>
</dl>
<h2>Parameters</h2>
<p>The following parameters can be assigned to a serial port. </p>
<p> All argument values are assumed to be in decimal unless preceeded by &quot;0x&quot;. </p>
<dl>
<dt><code>port</code> port_number</p>
<dd>The <code>port</code> option sets the I/O port, as described above.</p>
<dt><code>irq</code> irq_number</p>
<dd>The <code>irq</code> option sets the hardware IRQ, as described above.</p>
<dt><code>uart</code> uart_type</p>
<dd>This option is used to set the UART type. The permitted types are <code>none</code>, 8250, 16450, 16550, 16550A, 16650, 16650V2, 16654, 16750, 16850, 16950, and 16954. Using UART type <code>none</code> will disable the port. </p>
<p> Some internal modems are billed as having a &quot;16550A UART with a 1k buffer&quot;. This is a lie. They do not have really have a 16550A compatible UART; instead what they have is a 16450 compatible UART with a 1k receive buffer to prevent receiver overruns. This is important, because they do not have a transmit FIFO. Hence, they are not compatible with a 16550A UART, and the autoconfiguration process will correctly identify them as 16450&#8217;s. If you attempt to override this using the <code>uart</code> parameter, you will see dropped characters during file transmissions. These UART&#8217;s usually have other problems: the <code>skip_test</code> parameter also often must be specified.</p>
<dt><code>autoconfig</code></p>
<dd>When this parameter is given, <code>setserial</code> will ask the kernel to attempt to automatically configure the serial port. The I/O port must be correctly set; the kernel will attempt to determine the UART type, and if the <code>auto_irq </code> parameter is set, Linux will attempt to automatically determine the IRQ. The <code>autoconfig</code> parameter should be given after the <code>port</code>,<code>auto_irq</code>, and <code>skip_test</code> parameters have been specified.</p>
<dt><code>auto_irq</code></p>
<dd>During autoconfiguration, try to determine the IRQ. This feature is not guaranteed to always produce the correct result; some hardware configurations will fool the Linux kernel. It is generally safer not to use the <code>auto_irq</code> feature, but rather to specify the IRQ to be used explicitly, using the <code>irq </code> parameter.</p>
<dt><code>^auto_irq</code></p>
<dd>During autoconfiguration, do <i>not</i> try to determine the IRQ.</p>
<dt><code>skip_test</code></p>
<dd>During autoconfiguration, skip the UART test. Some internal modems do not have National Semiconductor compatible UART&#8217;s, but have cheap imitations instead. Some of these cheasy imitations UART&#8217;s do not fully support the loopback detection mode, which is used by the kernel to make sure there really is a UART at a particular address before attempting to configure it. So for certain internal modems you will need to specify this parameter so Linux can initialize the UART correctly.</p>
<dt><code>^skip_test</code></p>
<dd>During autoconfiguration, do <i>not</i> skip the UART test.</p>
<dt><code>baud_base</code> baud_base</p>
<dd>This option sets the base baud rate, which is the clock frequency divided by 16. Normally this value is 115200, which is also the fastest baud rate which the UART can support.</p>
<dt><code>spd_hi</code></p>
<dd>Use 57.6kb when the application requests 38.4kb. This parameter may be specified by a non-privileged user.</p>
<dt><code>spd_vhi</code></p>
<dd>Use 115kb when the application requests 38.4kb. This parameter may be specified by a non-privileged user.</p>
<dt><code>spd_shi</code></p>
<dd>Use 230kb when the application requests 38.4kb. This parameter may be specified by a non-privileged user.</p>
<dt><code>spd_warp</code></p>
<dd>Use 460kb when the application requests 38.4kb. This parameter may be specified by a non-privileged user.</p>
<dt><code>spd_cust</code></p>
<dd>Use the custom divisor to set the speed when the application requests 38.4kb. In this case, the baud rate is the <code>baud_base</code> divided by the <code>divisor</code>. This parameter may be specified by a non-privileged user.</p>
<dt><code>spd_normal</code></p>
<dd>Use 38.4kb when the application requests 38.4kb. This parameter may be specified by a non-privileged user.</p>
<dt><code>divisor</code> divisor</p>
<dd>This option sets the custom divison. This divisor will be used then the <code>spd_cust</code> option is selected and the serial port is set to 38.4kb by the application. This parameter may be specified by a non-privileged user.</p>
<dt><code>sak</code></p>
<dd>Set the break key at the Secure Attention Key.</p>
<dt><code>^sak</code></p>
<dd>disable the Secure Attention Key.</p>
<dt><code>fourport</code></p>
<dd>Configure the port as an AST Fourport card.</p>
<dt><code>^fourport</code></p>
<dd>Disable AST Fourport configuration.</p>
<dt><code>close_delay</code> delay</p>
<dd>Specify the amount of time, in hundredths of a second, that DTR should remain low on a serial line after the callout device is closed, before the blocked dialin device raises DTR again. The default value of this option is 50, or a half-second delay.</p>
<dt><code>closing_wait</code> delay</p>
<dd>Specify the amount of time, in hundredths of a second, that the kernel should wait for data to be transmitted from the serial port while closing the port. If &quot;none&quot; is specified, no delay will occur. If &quot;infinite&quot; is specified the kernel will wait indefinitely for the buffered data to be transmitted. The default setting is 3000 or 30 seconds of delay. This default is generally appropriate for most devices. If too long a delay is selected, then the serial port may hang for a long time if when a serial port which is not connected, and has data pending, is closed. If too short a delay is selected, then there is a risk that some of the transmitted data is output at all. If the device is extremely slow, like a plotter, the closing_wait may need to be larger.</p>
<dt><code>session_lockout</code></p>
<dd>Lock out callout port (/dev/cuaXX) accesses across different sessions. That is, once a process has opened a port, do not allow a process with a different session ID to open that port until the first process has closed it.</p>
<dt><code>^session_lockout</code></p>
<dd>Do not lock out callout port accesses across different sessions.</p>
<dt><code>pgrp_lockout</code></p>
<dd>Lock out callout port (/dev/cuaXX) accesses across different process groups. That is, once a process has opened a port, do not allow a process in a different process group to open that port until the first process has closed it.</p>
<dt><code>^pgrp_lockout</code></p>
<dd>Do not lock out callout port accesses across different process groups.</p>
<dt><code>hup_notify</code></p>
<dd>Notify a process blocked on opening a dial in line when a process has finished using a callout line (either by closing it or by the serial line being hung up) by returning EAGAIN to the open. </p>
<p> The application of this parameter is for getty&#8217;s which are blocked on a serial port&#8217;s dial in line. This allows the getty to reset the modem (which may have had its configuration modified by the application using the callout device) before blocking on the open again.</p>
<dt><code>^hup_notify</code></p>
<dd>Do not notify a process blocked on opening a dial in line when the callout device is hung up.</p>
<dt><code>split_termios</code></p>
<dd>Treat the termios settings used by the callout device and the termios settings used by the dialin devices as separate.</p>
<dt><code>^split_termios</code></p>
<dd>Use the same termios structure to store both the dialin and callout ports. This is the default option.</p>
<dt><code>callout_nohup</code></p>
<dd>If this particular serial port is opened as a callout device, do not hangup the tty when carrier detect is dropped.</p>
<dt><code>^callout_nohup</code></p>
<dd>Do not skip hanging up the tty when a serial port is opened as a callout device. Of course, the HUPCL termios flag must be enabled if the hangup is to occur.</p>
<dt><code>low_latency</code></p>
<dd>Minimize the receive latency of the serial device at the cost of greater CPU utilization. (Normally there is an average of 5-10ms latency before characters are handed off to the line discpline to minimize overhead.) This is off by default, but certain real-time applications may find this useful.</p>
<dt><code>^low_latency</code></p>
<dd>Optimize for efficient CPU processing of serial characters at the cost of paying an average of 5-10ms of latency before the characters are processed. This is the default.</dl>
<h2>Considerations Of Configuring Serial Ports</h2>
<p>It is important to note that setserial merely tells the Linux kernel where it should expect to find the I/O port and IRQ lines of a particular serial port. It does *not* configure the hardware, the actual serial board, to use a particular I/O port. In order to do that, you will need to physically program the serial board, usually by setting some jumpers or by switching some DIP switches. </p>
<p> This section will provide some pointers in helping you decide how you would like to configure your serial ports. </p>
<p> The &quot;standard MS-DOS&quot; port associations are given below: </p>
<pre><dl><dt><dd>/dev/ttys0 (COM1), port 0x3f8, irq 4
/dev/ttys1 (COM2), port 0x2f8, irq 3
/dev/ttys2 (COM3), port 0x3e8, irq 4
/dev/ttys3 (COM4), port 0x2e8, irq 3
</dl></pre>
<p>Due to the limitations in the design of the AT/ISA bus architecture, normally an IRQ line may not be shared between two or more serial ports. If you attempt to do this, one or both serial ports will become unreliable if you try to use both simultaneously. This limitation can be overcome by special multi-port serial port boards, which are designed to share multiple serial ports over a single IRQ line. Multi-port serial cards supported by Linux include the AST FourPort, the Accent Async board, the Usenet Serial II board, the Bocaboard BB-1004, BB-1008, and BB-2016 boards, and the HUB-6 serial board. </p>
<p> The selection of an alternative IRQ line is difficult, since most of them are already used. The following table lists the &quot;standard MS-DOS&quot; assignments of available IRQ lines: </p>
<pre><dl><dt><dd>IRQ 3: COM2
IRQ 4: COM1
IRQ 5: LPT2
IRQ 7: LPT1
</dl></pre>
<p>Most people find that IRQ 5 is a good choice, assuming that there is only one parallel port active in the computer. Another good choice is IRQ 2 (aka IRQ 9); although this IRQ is sometimes used by network cards, and very rarely VGA cards will be configured to use IRQ 2 as a vertical retrace interrupt. If your VGA card is configured this way; try to disable it so you can reclaim that IRQ line for some other card. It&#8217;s not necessary for Linux and most other Operating systems. </p>
<p> The only other available IRQ lines are 3, 4, and 7, and these are probably used by the other serial and parallel ports. (If your serial card has a 16bit card edge connector, and supports higher interrupt numbers, then IRQ 10, 11, 12, and 15 are also available.) </p>
<p> On AT class machines, IRQ 2 is seen as IRQ 9, and Linux will interpret it in this manner. </p>
<p> IRQ&#8217;s other than 2 (9), 3, 4, 5, 7, 10, 11, 12, and 15, should <i>not</i> be used, since they are assigned to other hardware and cannot, in general, be changed. Here are the &quot;standard&quot; assignments: </p>
<pre><dl><dt><dd>IRQ 0 Timer channel 0
IRQ 1 Keyboard
IRQ 2 Cascade for controller 2
IRQ 3 Serial port 2
IRQ 4 Serial port 1
IRQ 5 Parallel port 2 (Reserved in PS/2)
IRQ 6 Floppy diskette
IRQ 7 Parallel port 1
IRQ 8 Real-time clock
IRQ 9 Redirected to IRQ2
IRQ 10 Reserved
IRQ 11 Reserved
IRQ 12 Reserved (Auxillary device in PS/2)
IRQ 13 Math coprocessor
IRQ 14 Hard disk controller
IRQ 15 Reserved
</dl></pre>
<h2>Multiport Configuration</h2>
<p>Certain multiport serial boards which share multiple ports on a single IRQ use one or more ports to indicate whether or not there are any pending ports which need to be serviced. If your multiport board supports these ports, you should make use of them to avoid potential lockups if the interrupt gets lost. </p>
<p> In order to set these ports specify <code>set_multiport</code> as a parameter, and follow it with the multiport parameters. The multiport parameters take the form of specifying the <i>port</i> that should be checked, a <i>mask</i> which indicate which bits in the register are significant, and finally, a <i>match</i> parameter which specifies what the significant bits in that register must match when there is no more pending work to be done. </p>
<p> Up to four such port/mask/match combinations may be specified. The first such combinations should be specified by setting the parameters <code>port1</code>, <code>mask1</code>, and <code>match1</code>. The second such combination should be specified with <code>port2</code>, <code>mask2</code>, and <code>match2</code>, and so on. In order to disable this multiport checking, set <code>port1</code> to be zero. </p>
<p> In order to view the current multiport settings, specify the parameter <code>get_multiport</code> on the command line. </p>
<p> Here are some multiport settings for some common serial boards: </p>
<pre><dl><dt><dd>AST FourPort port1 0x1BF mask1 0xf match1 0xf
Boca BB-1004/8 port1 0x107 mask1 0xff match1 0
Boca BB-2016 port1 0x107 mask1 0xff match1 0 
 port2 0x147 mask2 0xff match2 0
</dl></pre>
<h2>Hayes ESP Configuration</h2>
<p><code>Setserial</code> may also be used to configure ports on a Hayes ESP serial board. </p>
<p> The following parameters when configuring ESP ports:</p>
<dl>
<dt><code>rx_trigger</code></p>
<dd>This is the trigger level (in bytes) of the receive FIFO. Larger values may result in fewer interrupts and hence better performance; however, a value too high could result in data loss. Valid values are 1 through 1023.</p>
<dt><code>tx_trigger</code></p>
<dd>This is the trigger level (in bytes) of the transmit FIFO. Larger values may result in fewer interrupts and hence better performance; however, a value too high could result in degraded transmit performance. Valid values are 1 through 1023.</p>
<dt><code>flow_off</code></p>
<dd>This is the level (in bytes) at which the ESP port will &quot;flow off&quot; the remote transmitter (i.e. tell him to stop stop sending more bytes). Valid values are 1 through 1023. This value should be greater than the receive trigger level and the flow on level.</p>
<dt><code>flow_on</code></p>
<dd>This is the level (in bytes) at which the ESP port will &quot;flow on&quot; the remote transmitter (i.e. tell him to resume sending bytes) after having flowed it off. Valid values are 1 through 1023. This value should be less than the flow off level, but greater than the receive trigger level.</p>
<dt><code>rx_timeout</code></p>
<dd>This is the amount of time that the ESP port will wait after receiving the final character before signaling an interrupt. Valid values are 0 through 255. A value too high will increase latency, and a value too low will cause unnecessary interrupts. </p>
</dl>
<h2>Caution</h2>
<p>CAUTION: Configuring a serial port to use an incorrect I/O port can lock up your machine.</p>
<h2>Files</h2>
<p><code>/etc/rc.local</code> <code>/etc/rc.serial</code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/4-tty/">tty</a></code>(4), <code><a href="/docs/linux/man/4-ttys/">ttys</a></code>(4), kernel/chr_drv/serial.c</p>
<h2>Author</h2>
<p>The original version of setserial was written by Rick Sladkey (jrs [at] world.std.com), and was modified by Michael K. Johnson (johnsonm [at] stolaf.edu). </p>
<p> This version has since been rewritten from scratch by Theodore Ts&#8217;o (tytso [at] mit.edu) on 1/1/93. Any bugs or problems are solely his responsibility.</p>
