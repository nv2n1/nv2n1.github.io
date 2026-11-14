---
title: "sethdlc(8)"
name: "sethdlc"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sethdlc/"
description: "sethdlc – get/set Linux HDLC packet radio modem driver port information"
---

<p>sethdlc &#8211; get/set Linux HDLC packet radio modem driver port information</p>
<h2>Synopsis</h2>
<p><code>sethdlc</code> <code>[ -bdhs ]</code> <code>[-i device]</code> <code>sethdlc [-i device] -c</code> cal <code>sethdlc -p</code> <code>[-i device]</code> <code>[&nbsp;<wbr>mode&nbsp;<wbr></code>mode<code>&nbsp;<wbr>]</code> <code>[&nbsp;<wbr>io&nbsp;<wbr></code>iobase<code>&nbsp;<wbr>]</code> <code>[&nbsp;<wbr>irq&nbsp;<wbr></code>irq<code>&nbsp;<wbr>]</code> <code>[&nbsp;<wbr>dma&nbsp;<wbr></code>dma<code>&nbsp;<wbr>]</code> <code>[&nbsp;<wbr>dma2&nbsp;<wbr></code>dma2<code>&nbsp;<wbr>]</code> <code>[&nbsp;<wbr>serio&nbsp;<wbr></code>seriobase<code>&nbsp;<wbr>]</code> <code>[&nbsp;<wbr>pario&nbsp;<wbr></code>pariobase<code>&nbsp;<wbr>]</code> <code>[&nbsp;<wbr>midiio&nbsp;<wbr></code>midiiobase<code>&nbsp;<wbr>]</code> <code>[&nbsp;<wbr>options&nbsp;<wbr></code>options<code>&nbsp;<wbr>]</code> <code>sethdlc -a</code> <code>[-i device]</code> <code>[&nbsp;<wbr>txd&nbsp;<wbr></code>txdelay<code>&nbsp;<wbr>]</code> <code>[&nbsp;<wbr>txtail&nbsp;<wbr></code>txtail<code>&nbsp;<wbr>]</code> <code>[&nbsp;<wbr>slot&nbsp;<wbr></code>slottime<code>&nbsp;<wbr>]</code> <code>[&nbsp;<wbr>ppersist&nbsp;<wbr></code>ppersistence<code>&nbsp;<wbr>]</code> <code>[&nbsp;<wbr>full&nbsp;<wbr>]</code> <code>[&nbsp;<wbr>half&nbsp;<wbr>]</code> </p>
<h2>Description</h2>
<p><code>sethdlc</code> is a program designed to set and/or report the configuration information associated with a soundcard radio modem port. This information includes the modem type, what I/O port, IRQ and DMA channel a particular modem port is using, and where to output a transmitter keying (PTT) signal. With the <code>-p</code> option, <code>sethdlc</code> sets and/or reports the port configuration. With the <code>-a</code> option, <code>sethdlc</code> sets and/or reports the AX.25 channel access parameters. These parameters can also be set with the <i>kissparms</i> utility. With the <code>-c</code> option, <code>sethdlc</code> instructs the driver to send a calibration pattern for <i>cal</i> seconds. Without the <code>-p,</code> <code>-a</code> and <code>-c</code> option, <code>sethdlc</code> will stay in the foreground and display received packets. The AX.25 header and eventually a FlexNet compressed header are decoded. CTRL-C terminates <code>sethdlc.</code> Specifying additional options, <code>sethdlc</code> may display additional information. </p>
<h2>Options</h2>
<p><code>sethdlc</code> accepts the following options: </p>
<dl>
<dt><code>-b</code></p>
<dd>Trace the bits at the output of the demodulator, after RX clock recovery. This option is only available if <code>sethdlc</code> and the soundcard modem kernel driver is compiled with debugging support on. This is useful for driver debugging.</p>
<dt><code>-d</code></p>
<dd>Trace DCD, PTT and other status information on stdout. <code>sethdlc</code> displays two times per second a line containing these informations.</p>
<dt><code>-h</code></p>
<dd>Display an overview of the available command line parameters and exit.</p>
<dt><code>-i</code></p>
<dd>The <i>device</i> argument specifies the HDLC modem device which should be configured or interrogated. It will usually have the following form: <i>bc[0-3]</i> for the baycom driver and <i>sm[0-3]</i> for the soundcard modem driver.</p>
<dt><code>-s</code></p>
<dd>Trace the bits at the demodulator output, <i>before</i> the RX clock recovery, to stdout. This option is only available the modem driver is compiled with debugging support on. It may not be available on some modem, such as the <i>par96</i>. </p>
</dl>
<h2>Parameters</h2>
<p>The following parameters can be assigned to a soundcard radio modem port. </p>
<p> All numerical parameter values are assumed to be in decimal unless preceeded by &quot;0x&quot;. </p>
<p> The <code>mode</code> parameter sets the type of hardware and the operating mode of the driver. <i>ser12</i> and <i>par96</i> are valid modes for the <code>baycom</code> driver. A star &quot;<i>*</i>&quot; may be added to enable software DCD. The <code>mode</code> string format of the <code>soundmodem</code> driver is as follows: <i>hw:mode</i>. <i>hw</i> may be either <i>sbc</i>, <i>wss</i> or <i>wssfdx</i>. The first one specifies SoundBlaster compatible soundcards, the second one WindowsSoundSystem compatible hardware, and the third one WSS fullduplex operation (which currently works with Crystal Semiconductor Chipsets CS423[126]). The <i>mode</i> portion may be <i>afsk1200</i> or <i>fsk9600</i>. Optionally, the receive and transmit modes may be different (<i>hw:txmode.rxmode</i>). </p>
<p> The <code>ioport</code> parameter sets the I/O port address. Typical values for the <i>ser12</i> modem are 0x3f8, 0x2f8, 0x3e8 or 0x2e8, for the <i>par96</i> modem 0x378, 0x278 or 0x3bc, for the <i>sbc</i> modems 0x220 and for the <i>wss</i> modems 0x530, 0x608, 0xe80 or 0xf40. </p>
<p> The <code>irq</code> parameter sets the hardware IRQ number. Typical values for the <i>ser12</i> modem are 4 and 3, for the <i>par96</i> modem 7 or 5, for the <i>sbc</i> modems are 7 or 5 and for the <i>wss</i> modems, any free IRQ from the set 2, 7, 9, 10, 11 will do. The driver automatically configures the WSS soundcard to the correct IRQ. </p>
<p> The <code>dma</code> parameter sets the hardware DMA number. Typical values for the <i>sbc</i> modems are 1 or 0 and for the <i>wss</i> modems, any free DMA from 0 to 3 (except 2) will do. The driver automatically configures the WSS soundcard to the correct DMA. The Baycom modems do not need DMA. </p>
<p> The <code>dma2</code> parameter sets the second hardware DMA number. This is only needed for full duplex operation with the <code>soundmodem</code> driver. </p>
<p> The <code>seriobase</code> parameter optionally sets the address of a serial port, where the driver will output a PTT signal at the TxD and RTS pins, and a DCD signal at the DTR pin. As Baycom modems do have their own PTT pin, this parameter is not used by the Baycom modem driver. </p>
<p> The <code>pariobase</code> parameter optionally sets the address of a LPT port where the driver will output a PTT signal on the DATA0 line and a DCD signal on the DATA1 line. As Baycom modems do have their own PTT pin, this parameter is not used by the Baycom modem driver. </p>
<p> The <code>midiiobase</code> parameter optionally sets the address of a MPU401 compatible MIDI port, where the driver will output a PTT signal. Since the MIDI port is effectively an UART and therefore cannot output a DC signal, the output must be fed through a retriggerable monoflop with a period of about 15ms. See <i><a rel="nofollow" href="http://www.ife.ee.ethz.ch/~sailer/pcf/ptt_circ/ptt.html">http://www.ife.ee.ethz.ch/~sailer/pcf/ptt_circ/ptt.html</a></i> for a sample schematic diagram. As Baycom modems do have their own PTT pin, this parameter is not used by the Baycom modem driver. </p>
<p> The <code>txdelay</code> sets the transmitter keyup delay time. Unlike <i>kissparms</i>, the unit is <i>tens of ms</i>. This is the time the transmitter needs to switch its PA on and for its frequency synthesizer to settle. Typical values for a handheld transceiver are 200ms (i.e. 20), and for a good crystal driven transceiver 20ms (i.e. 2). </p>
<p> The <code>txtail</code> sets the time PTT is held after the last packet. Unlike <i>kissparms</i>, the unit is <i>tens of ms</i>. Do not set this value to 0. Most modems need some extra time to actually clock the last bits out to the transmitter. </p>
<p> The <code>slottime</code> parameter specifies how often the channel access algorithm is executed. Unlike <i>kissparms</i>, the unit is <i>tens of ms</i>. Unless you have very specific requirements, set this to 100ms (i.e. 10). </p>
<p> The <code>ppersist</code> sets how &quot;eagerly&quot; the station starts to transmit as soon as the channel gets free. The optimum value is 256 divided by the number of stations on the channel. (This should really be done automatically by the L2) </p>
<p> <code>full</code> sets the modem to full duplex mode. Note that some modems do not actually support full duplex mode, in this case this parameter makes the modem start its transmission as soon as it gets packets from the upper layer, without waiting for the channel to become free. This is needed by some implementations of alternative channel access algorithms, e.g. <i>DAMA</i>. </p>
<p> <code>half</code> sets the modem to half duplex mode.</p>
<h2>Considerations Of Configuring Baycom Ports</h2>
<p>It is important to note that sethdlc merely tells the Linux kernel where it should expect to find the I/O port and IRQ lines of a particular serial port. It does <i>not</i> configure the hardware to use a particular I/O port. In order to do that, you will need to physically program the serial board, usually by setting some jumpers or by switching some DIP switches. </p>
<p> This section will provide some pointers in helping you decide how you would like to configure your baycom ports. </p>
<p> The &quot;standard MS-DOS&quot; port associations are given below: </p>
<pre><dl><dt><dd>COM1, port 0x3f8, irq 4
COM2, port 0x2f8, irq 3
COM3, port 0x3e8, irq 4
COM4, port 0x2e8, irq 3
LPT1, port 0x378, irq 7
LPT1 (on hercules graphics adapter), port 0x3bc, irq 7
LPT1, port 0x278, irq 5
</dl></pre>
<h2>Considerations Of Configuring Soundcard Radio Modem Ports</h2>
<p>Some cards need to be initialized before they act as a WSS or SoundBlaster compatible card. This driver does <i>not</i> do this. You can use the standard linux sound driver, if compiled as a module. Just load the sound driver (insmod sound) and remove it again (rmmod sound). The card should then be configured for either soundblaster or WSS compatibility. If this does not work for some reason, you&#8217;ll have to write your own soundcard configuration utility. This is not as complicated as it sounds; it can be done from user space (but requiring root privileges) using <i>ioperm</i> and/or <i>iopl</i>. </p>
<p> It is important that the audio levels of your radio match those of the soundcard. To help achieve this, there are two utilities: <i>smdiag</i> and <i>smmixer</i>. See their respective manpage. </p>
<p> The sound driver and the soundcard modem driver are mutually exclusive, i.e. they cannot both access the same soundcard at the same time. Even worse, the sound driver reserves the soundcard as soon as it gets loaded. The souncard modem driver however reserves the card only when the interface is started, i.e. during ifconfig sm[0-3] up. </p>
<p> 9600 baud may not currently work on SoundBlaster cards with DSP revision 4.x, i.e. SB16 and SB32 AWE. This is because they seem to not be fully backwards compatible.</p>
<h2>Caution</h2>
<p>CAUTION: Using an invalid port can lock up your machine.</p>
<h2>See Also</h2>
<pre><code>smdiag</code>&nbsp;<wbr>(8), <code>smmixer</code>&nbsp;<wbr>(8), <code>kissparms</code>&nbsp;<wbr>(8),
linux/drivers/net/hdlcdrv.c,
linux/drivers/net/baycom.c,
linux/drivers/net/soundmodem.c</pre>
<h2>Author</h2>
<p>sethdlc was written by Thomas Sailer, HB9JNX/AE4WA (t.sailer [at] alumni.ethz.ch). Inspired by setserial.</p>
