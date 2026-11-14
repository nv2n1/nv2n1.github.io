---
title: "ldattach(8)"
name: "ldattach"
section: "8"
letter: "l"
url: "/docs/linux/man/8-ldattach/"
description: "ldattach – attach a line discipline to a serial line"
---

<p>ldattach &#8211; attach a line discipline to a serial line</p>
<h2>Synopsis</h2>
<p><code>ldattach</code> [<code>-1278denoVh</code>] [<code>-i</code> <i>iflag</i>] [<code>-s</code> <i>speed</i>] <i>ldisc device</i></p>
<h2>Description</h2>
<p>The <code>ldattach</code> daemon opens the specified <i>device</i> file (which should refer to a serial device) and attaches the line discipline <i>ldisc</i> to it for processing of the sent and/or received data. It then goes into the background keeping the device open so that the line discipline stays loaded. </p>
<p> The line discipline <i>ldisc</i> may be specified either by name or by number. </p>
<p> In order to detach the line discipline, <code><a href="/docs/linux/man/1-kill/">kill</a></code>(1) the <code>ldattach</code> process. </p>
<p> With no arguments, <code>ldattach</code> prints usage information.</p>
<h2>Line Disciplines</h2>
<p>Depending on the kernel release, the following line disciplines are supported: </p>
<p> <code>TTY</code>(<code>0</code>)</p>
<dl>
<dd>The default line discipline, providing transparent operation (raw mode) as well as the habitual terminal line editing capabilities (cooked mode).</dl>
<p> <code>SLIP</code>(<code>1</code>)</p>
<dl>
<dd>Serial Line IP (SLIP) protocol processor for transmitting TCP/IP packets over serial lines.</dl>
<p> <code>MOUSE</code>(<code>2</code>)</p>
<dl>
<dd>Device driver for RS232 connected pointing devices (serial mice).</dl>
<p> <code>PPP</code>(<code>3</code>)</p>
<dl>
<dd>Point to Point Protocol (PPP) processor for transmitting network packets over serial lines.</dl>
<p> <code>STRIP</code>(<code>4</code>); <code>AX25</code>(<code>5</code>); <code>X25</code>(<code>6</code>)</p>
<dl>
<dd>Line driver for transmitting X.25 packets over asynchronous serial lines.</dl>
<p> <code>6PACK</code>(<code>7</code>); <code>R3964</code>(<code>9</code>)</p>
<dl>
<dd>Driver for Simatic R3964 module.</dl>
<p> <code>IRDA</code>(<code>11</code>)</p>
<dl>
<dd>Linux IrDa (infrared data transmission) driver &#8211; see <i></i> &lt;<a rel="nofollow" href="http://irda.sourceforge.net/">http://irda.sourceforge.net/</a>&gt;</dl>
<p> <code>HDLC</code>(<code>13</code>)</p>
<dl>
<dd>Synchronous HDLC driver.</dl>
<p> <code>SYNC_PPP</code>(<code>14</code>)</p>
<dl>
<dd>Synchronous PPP driver.</dl>
<p> <code>HCI</code>(<code>15</code>)</p>
<dl>
<dd>Bluetooth HCI UART driver.</dl>
<p> <code>GIGASET_M101</code>(<code>16</code>)</p>
<dl>
<dd>Driver for Siemens Gigaset M101 serial DECT adapter.</dl>
<p> <code>PPS</code>(<code>18</code>)</p>
<dl>
<dd>Driver for serial line Pulse Per Second (PPS) source.</dl>
<p> <code>GSM0710</code>(<code>21</code>)</p>
<dl>
<dd>Driver for GSM 07.10 multiplexing protocol modem (CMUX).</dl>
<h2>Options</h2>
<p><code>-1</code>, <code>&#8211;onestopbit</code></p>
<dl>
<dd>Set the number of stop bits of the serial line to one.</dl>
<p> <code>-2</code>, <code>&#8211;twostopbits</code></p>
<dl>
<dd>Set the number of stop bits of the serial line to two.</dl>
<p> <code>-7</code>, <code>&#8211;sevenbits</code></p>
<dl>
<dd>Set the character size of the serial line to 7 bits.</dl>
<p> <code>-8</code>, <code>&#8211;eightbits</code></p>
<dl>
<dd>Set the character size of the serial line to 8 bits.</dl>
<p> <code>-d</code>, <code>&#8211;debug</code></p>
<dl>
<dd>Keep <code>ldattach</code> in the foreground so that it can be interrupted or debugged, and to print verbose messages about its progress to standard error output.</dl>
<p> <code>-e</code>, <code>&#8211;evenparity</code></p>
<dl>
<dd>Set the parity of the serial line to even.</dl>
<p> <code>-i</code>, <code>&#8211;iflag</code> <i>value</i>&#8230;</p>
<dl>
<dd>Set the specified bits in the c_iflag word of the serial line. The given <i>value</i> may be a number or a symbolic name. If <i>value</i> is prefixed by a minus sign, the specified bits are cleared instead. Several comma-separated values may be given in order to set and clear multiple bits.</dl>
<p> <code>-n</code>, <code>&#8211;noparity</code></p>
<dl>
<dd>Set the parity of the serial line to none.</dl>
<p> <code>-o</code>, <code>&#8211;oddparity</code></p>
<dl>
<dd>Set the parity of the serial line to odd.</dl>
<p> <code>-s</code>, <code>&#8211;speed</code> <i>value</i></p>
<dl>
<dd>Set the speed (the baud rate) of the serial line to the specified <i>value</i>.</dl>
<p> <code>-c</code>, <code>&#8211;intro-command</code> <i>string</i></p>
<dl>
<dd>Define an intro command that is sent through the serial line before the invocation of ldattach. E.g. in conjunction with line discipline GSM0710, the command &#8216;AT+CMUX=0&#8217; is commonly suitable to switch the modem into the CMUX mode.</dl>
<p> <code>-p</code>, <code>&#8211;pause</code> <i>value</i></p>
<dl>
<dd>Sleep for <i>value</i> seconds before the invocation of ldattach. Default is one second.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<h2>Authors</h2>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-inputattach/">inputattach</a></code>(1), <code><a href="/docs/linux/man/4-ttys/">ttys</a></code>(4)</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>ldattach</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
