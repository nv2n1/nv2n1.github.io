---
title: "snd_mpu401_uart_new(9)"
name: "snd_mpu401_uart_new"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_mpu401_uart_new/"
---

snd_mpu401_uart_new - create an MPU401-UART instance

<h2>Synopsis</h2>

<pre><code>int snd_mpu401_uart_new(struct snd_card *card, int device, unsigned short hardware, unsigned long port, unsigned int info_flags, int irq, struct snd_rawmidi **rrawmidi);</code></pre>

<h2>Arguments</h2>

<i>card</i>
<dl><dd><dd>the card instance</dl>
 

 <i>device</i>
<dl><dd>the device index, zero-based</dl>
 

 <i>hardware</i>
<dl><dd>the hardware type, MPU401_HW_XXXX</dl>
 

 <i>port</i>
<dl><dd>the base address of MPU401 port</dl>
 

 <i>info_flags</i>
<dl><dd>bitflags MPU401_INFO_XXX</dl>
 

 <i>irq</i>
<dl><dd>the ISA irq number, -1 if not to be allocated</dl>
 

 <i>rrawmidi</i>
<dl><dd>the pointer to store the new rawmidi instance</dl>

<h2>Description</h2>

Creates a new MPU-401 instance. 

 Note that the rawmidi instance is returned on the rrawmidi argument, not the mpu401 instance itself. To access to the mpu401 instance, cast from rawmidi-&gt;private_data (with struct snd_mpu401 magic-cast).

<h2>Return</h2>

Zero if successful, or a negative error code.

<h2>Copyright</h2>


