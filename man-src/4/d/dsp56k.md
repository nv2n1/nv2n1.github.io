---
title: "dsp56k(4)"
name: "dsp56k"
section: "4"
letter: "d"
url: "/docs/linux/man/4-dsp56k/"
description: "dsp56k – DSP56001 interface device"
---

<p>dsp56k &#8211; DSP56001 interface device</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;asm/dsp56k.h&gt;

ssize_t read(int fd, void *data, size_t length);
ssize_t write(int fd, void *data, size_t length);

int ioctl(int fd, DSP56K_UPLOAD, struct dsp56k_upload *program);
int ioctl(int fd, DSP56K_SET_TX_WSIZE, int wsize);
int ioctl(int fd, DSP56K_SET_RX_WSIZE, int wsize);
int ioctl(int fd, DSP56K_HOST_FLAGS, struct dsp56k_host_flags *flags);
int ioctl(int fd, DSP56K_HOST_CMD, int cmd);</code></pre>
<h2>Configuration</h2>
<p>The <code>dsp56k</code> device is a character device with major number 55 and minor number 0.</p>
<h2>Description</h2>
<p>The Motorola DSP56001 is a fully programmable 24-bit digital signal processor found in Atari Falcon030-compatible computers. The <i>dsp56k</i> special file is used to control the DSP56001, and to send and receive data using the bidirectional handshaked host port. </p>
<p> To send a data stream to the signal processor, use <code><a href="/docs/linux/man/2-write/">write</a></code>(2) to the device, and <code><a href="/docs/linux/man/2-read/">read</a></code>(2) to receive processed data. The data can be sent or received in 8, 16, 24, or 32-bit quantities on the host side, but will always be seen as 24-bit quantities in the DSP56001. </p>
<p> The following <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) calls are used to control the <i>dsp56k</i> device:</p>
<dl>
<dt><code>DSP56K_UPLOAD</code></p>
<dd>resets the DSP56001 and uploads a program. The third <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) argument must be a pointer to a <i>struct dsp56k_upload</i> with members <i>bin</i> pointing to a DSP56001 binary program, and <i>len</i> set to the length of the program, counted in 24-bit words.</p>
<dt><code>DSP56K_SET_TX_WSIZE</code></p>
<dd>sets the transmit word size. Allowed values are in the range 1 to 4, and is the number of bytes that will be sent at a time to the DSP56001. These data quantities will either be padded with bytes containing zero, or truncated to fit the native 24-bit data format of the DSP56001.</p>
<dt><code>DSP56K_SET_RX_WSIZE</code></p>
<dd>sets the receive word size. Allowed values are in the range 1 to 4, and is the number of bytes that will be received at a time from the DSP56001. These data quantities will either truncated, or padded with a null byte (&#8216;
