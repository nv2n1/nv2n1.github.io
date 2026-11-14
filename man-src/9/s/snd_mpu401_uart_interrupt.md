---
title: "snd_mpu401_uart_interrupt(9)"
name: "snd_mpu401_uart_interrupt"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_mpu401_uart_interrupt/"
description: "snd_mpu401_uart_interrupt – generic MPU401-UART interrupt handler"
---

<p>snd_mpu401_uart_interrupt &#8211; generic MPU401-UART interrupt handler</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>irqreturn_t snd_mpu401_uart_interrupt(int&nbsp;<wbr></code><i>irq</i><code>, void&nbsp;<wbr>*&nbsp;<wbr></code><i>dev_id</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>irq</i></p>
<dl>
<dd>
<dd>the irq number</dl>
<p> <i>dev_id</i></p>
<dl>
<dd>mpu401 instance</dl>
<h2>Description</h2>
<p>Processes the interrupt for MPU401-UART i/o.</p>
<h2>Return</h2>
<p><code>IRQ_HANDLED</code> if the interrupt was handled. <code>IRQ_NONE</code> otherwise.</p>
<h2>Copyright</h2>
