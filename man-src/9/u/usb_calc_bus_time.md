---
title: "usb_calc_bus_time(9)"
name: "usb_calc_bus_time"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_calc_bus_time/"
---

usb_calc_bus_time - approximate periodic transaction time in nanoseconds

<h2>Synopsis</h2>

<pre><code>long usb_calc_bus_time(int speed, int is_input, int isoc, int bytecount);</code></pre>

<h2>Arguments</h2>

<i>speed</i>
<dl><dd><dd>from dev-&gt;speed; USB_SPEED_{LOW,FULL,HIGH}</dl>
 

 <i>is_input</i>
<dl><dd>true iff the transaction sends data to the host</dl>
 

 <i>isoc</i>
<dl><dd>true for isochronous transactions, false for interrupt ones</dl>
 

 <i>bytecount</i>
<dl><dd>how many bytes in the transaction.</dl>

<h2>Return</h2>

Approximate bus time in nanoseconds for a periodic transaction.

<h2>Note</h2>

See USB 2.0 spec section 5.11.3; only periodic transfers need to be scheduled in software, this function is only used for such scheduling.

<h2>Copyright</h2>


