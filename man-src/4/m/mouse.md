---
title: "mouse(4)"
name: "mouse"
section: "4"
letter: "m"
url: "/docs/linux/man/4-mouse/"
description: "mouse – serial mouse interface"
---

<p>mouse &#8211; serial mouse interface</p>
<h2>Configuration</h2>
<p>Serial mice are connected to a serial RS232/V24 dialout line, see <code><a href="/docs/linux/man/4-ttys/">ttyS</a></code>(4) for a description.</p>
<h2>Description</h2>
<h3>Introduction</h3>
<p>The pinout of the usual 9 pin plug as used for serial mice is: </p>
<p> <center></p>
<table>
<tr VALIGN=top>
<td ALIGN=right>pin</td>
<td ALIGN=center>name</td>
<td>used for
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>2</td>
<td ALIGN=center>RX</td>
<td>Data
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>3</td>
<td ALIGN=center>TX</td>
<td>-12 V, Imax = 10 mA
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>4</td>
<td ALIGN=center>DTR</td>
<td>+12 V, Imax = 10 mA
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>7</td>
<td ALIGN=center>RTS</td>
<td>+12 V, Imax = 10 mA
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>5</td>
<td ALIGN=center>GND</td>
<td>Ground
</td>
</tr>
</table>
<p></center> </p>
<p> This is the specification, in fact 9 V suffices with most mice. </p>
<p> The mouse driver can recognize a mouse by dropping RTS to low and raising it again. About 14 ms later the mouse will send 0x4D (&#8216;M&#8217;) on the data line. After a further 63 ms, a Microsoft-compatible 3-button mouse will send 0x33 (&#8216;3&#8217;). </p>
<p> The relative mouse movement is sent as <i>dx</i> (positive means right) and <i>dy</i> (positive means down). Various mice can operate at different speeds. To select speeds, cycle through the speeds 9600, 4800, 2400, and 1200 bit/s, each time writing the two characters from the table below and waiting 0.1 seconds. The following table shows available speeds and the strings that select them: </p>
<p> <center></p>
<table>
<tr VALIGN=top>
<td>bit/s</td>
<td>string
</td>
</tr>
<tr VALIGN=top>
<td>9600</td>
<td>*q
</td>
</tr>
<tr VALIGN=top>
<td>4800</td>
<td>*p
</td>
</tr>
<tr VALIGN=top>
<td>2400</td>
<td>*o
</td>
</tr>
<tr VALIGN=top>
<td>1200</td>
<td>*n
</td>
</tr>
</table>
<p></center> </p>
<p> The first byte of a data packet can be used for synchronization purposes.</p>
<h3>Microsoft protocol</h3>
<p>The <code>Microsoft</code> protocol uses 1 start bit, 7 data bits, no parity and one stop bit at the speed of 1200 bits/sec. Data is sent to RxD in 3-byte packets. The <i>dx</i> and <i>dy</i> movements are sent as two&#8217;s-complement, <i>lb</i> (<i>rb</i>) are set when the left (right) button is pressed: </p>
<p> <center></p>
<table>
<tr VALIGN=top>
<td ALIGN=right>byte</td>
<td ALIGN=center>d6</td>
<td ALIGN=center>d5</td>
<td ALIGN=center>d4</td>
<td ALIGN=center>d3</td>
<td ALIGN=center>d2</td>
<td ALIGN=center>d1</td>
<td ALIGN=center>d0
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>1</td>
<td ALIGN=center>1</td>
<td ALIGN=center>lb</td>
<td ALIGN=center>rb</td>
<td ALIGN=center>dy7</td>
<td ALIGN=center>dy6</td>
<td ALIGN=center>dx7</td>
<td ALIGN=center>dx6
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>2</td>
<td ALIGN=center>0</td>
<td ALIGN=center>dx5</td>
<td ALIGN=center>dx4</td>
<td ALIGN=center>dx3</td>
<td ALIGN=center>dx2</td>
<td ALIGN=center>dx1</td>
<td ALIGN=center>dx0
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>3</td>
<td ALIGN=center>0</td>
<td ALIGN=center>dy5</td>
<td ALIGN=center>dy4</td>
<td ALIGN=center>dy3</td>
<td ALIGN=center>dy2</td>
<td ALIGN=center>dy1</td>
<td ALIGN=center>dy0
</td>
</tr>
</table>
<p></center></p>
<h3>3-button Microsoft protocol</h3>
<p>Original Microsoft mice only have two buttons. However, there are some three button mice which also use the Microsoft protocol. Pressing or releasing the middle button is reported by sending a packet with zero movement and no buttons pressed. (Thus, unlike for the other two buttons, the status of the middle button is not reported in each packet.)</p>
<h3>Logitech protocol</h3>
<p>Logitech serial 3-button mice use a different extension of the Microsoft protocol: when the middle button is up, the above 3-byte packet is sent. When the middle button is down a 4-byte packet is sent, where the 4th byte has value 0x20 (or at least has the 0x20 bit set). In particular, a press of the middle button is reported as 0,0,0,0&#215;20 when no other buttons are down.</p>
<h3>Mousesystems protocol</h3>
<p>The <code>Mousesystems</code> protocol uses 1 start bit, 8 data bits, no parity and two stop bits at the speed of 1200 bits/sec. Data is sent to RxD in 5-byte packets. <i>dx</i> is sent as the sum of the two two&#8217;s-complement values, <i>dy</i> is send as negated sum of the two two&#8217;s-complement values. <i>lb</i> (<i>mb</i>, <i>rb</i>) are cleared when the left (middle, right) button is pressed: </p>
<p> <center></p>
<table>
<tr VALIGN=top>
<td ALIGN=right>byte</td>
<td ALIGN=center>d7</td>
<td ALIGN=center>d6</td>
<td ALIGN=center>d5</td>
<td ALIGN=center>d4</td>
<td ALIGN=center>d3</td>
<td ALIGN=center>d2</td>
<td ALIGN=center>d1</td>
<td ALIGN=center>d0
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>1</td>
<td ALIGN=center>1</td>
<td ALIGN=center>0</td>
<td ALIGN=center>0</td>
<td ALIGN=center>0</td>
<td ALIGN=center>0</td>
<td ALIGN=center>lb</td>
<td ALIGN=center>mb</td>
<td ALIGN=center>rb
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>2</td>
<td ALIGN=center>0</td>
<td ALIGN=center>dxa6</td>
<td ALIGN=center>dxa5</td>
<td ALIGN=center>dxa4</td>
<td ALIGN=center>dxa3</td>
<td ALIGN=center>dxa2</td>
<td ALIGN=center>dxa1</td>
<td ALIGN=center>dxa0
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>3</td>
<td ALIGN=center>0</td>
<td ALIGN=center>dya6</td>
<td ALIGN=center>dya5</td>
<td ALIGN=center>dya4</td>
<td ALIGN=center>dya3</td>
<td ALIGN=center>dya2</td>
<td ALIGN=center>dya1</td>
<td ALIGN=center>dya0
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>4</td>
<td ALIGN=center>0</td>
<td ALIGN=center>dxb6</td>
<td ALIGN=center>dxb5</td>
<td ALIGN=center>dxb4</td>
<td ALIGN=center>dxb3</td>
<td ALIGN=center>dxb2</td>
<td ALIGN=center>dxb1</td>
<td ALIGN=center>dxb0
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>5</td>
<td ALIGN=center>0</td>
<td ALIGN=center>dyb6</td>
<td ALIGN=center>dyb5</td>
<td ALIGN=center>dyb4</td>
<td ALIGN=center>dyb3</td>
<td ALIGN=center>dyb2</td>
<td ALIGN=center>dyb1</td>
<td ALIGN=center>dyb0
</td>
</tr>
</table>
<p></center> </p>
<p> Bytes 4 and 5 describe the change that occurred since bytes 2 and 3 were transmitted.</p>
<h3>Sun protocol</h3>
<p>The <code>Sun</code> protocol is the 3-byte version of the above 5-byte Mousesystems protocol: the last two bytes are not sent.</p>
<h3>MM protocol</h3>
<p>The <code>MM</code> protocol uses 1 start bit, 8 data bits, odd parity and one stop bit at the speed of 1200 bits/sec. Data is sent to RxD in 3-byte packets. <i>dx</i> and <i>dy</i> are sent as single signed values, the sign bit indicating a negative value. <i>lb</i> (<i>mb</i>, <i>rb</i>) are set when the left (middle, right) button is pressed: </p>
<p> <center></p>
<table>
<tr VALIGN=top>
<td ALIGN=right>byte</td>
<td ALIGN=center>d7</td>
<td ALIGN=center>d6</td>
<td ALIGN=center>d5</td>
<td ALIGN=center>d4</td>
<td ALIGN=center>d3</td>
<td ALIGN=center>d2</td>
<td ALIGN=center>d1</td>
<td ALIGN=center>d0
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>1</td>
<td ALIGN=center>1</td>
<td ALIGN=center>0</td>
<td ALIGN=center>0</td>
<td ALIGN=center>dxs</td>
<td ALIGN=center>dys</td>
<td ALIGN=center>lb</td>
<td ALIGN=center>mb</td>
<td ALIGN=center>rb
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>2</td>
<td ALIGN=center>0</td>
<td ALIGN=center>dx6</td>
<td ALIGN=center>dx5</td>
<td ALIGN=center>dx4</td>
<td ALIGN=center>dx3</td>
<td ALIGN=center>dx2</td>
<td ALIGN=center>dx1</td>
<td ALIGN=center>dx0
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>3</td>
<td ALIGN=center>0</td>
<td ALIGN=center>dy6</td>
<td ALIGN=center>dy5</td>
<td ALIGN=center>dy4</td>
<td ALIGN=center>dy3</td>
<td ALIGN=center>dy2</td>
<td ALIGN=center>dy1</td>
<td ALIGN=center>dy0
</td>
</tr>
</table>
<p></center></p>
<h2>Files</h2>
<dl>
<dt><i>/dev/mouse</i></p>
<dd>A commonly used symbolic link pointing to a mouse device.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/4-ttys/">ttyS</a></code>(4), <code><a href="/docs/linux/man/8-gpm/">gpm</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
