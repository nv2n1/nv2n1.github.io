---
title: "i2cget(8)"
name: "i2cget"
section: "8"
letter: "i"
url: "/docs/linux/man/8-i2cget/"
description: "i2cget – read from I2C/SMBus chip registers"
---

<p>i2cget &#8211; read from I2C/SMBus chip registers </p>
<h2>Synopsis</h2>
<p><code>i2cget</code> [<code>-f</code>] [<code>-y</code>] <i>i2cbus</i> <i>chip-address</i> [<i>data-address </i>[<i>mode</i>]]<br />
 <code>i2cget</code> <code>-V</code> </p>
<h2>Description</h2>
<p>i2cget is a small helper program to read registers visible through the I2C bus (or SMBus). </p>
<h2>Options</h2>
<dl>
<dt><code>-V</code></p>
<dd>Display the version and exit.</p>
<dt><code>-f</code></p>
<dd>Force access to the device even if it is already busy. By default, i2cget will refuse to access a device which is already under the control of a kernel driver. Using this flag is dangerous, it can seriously confuse the kernel driver in question. It can also cause i2cget to return an invalid value. So use at your own risk and only if you know what you&#8217;re doing.</p>
<dt><code>-y</code></p>
<dd>Disable interactive mode. By default, i2cget will wait for a confirmation from the user before messing with the I2C bus. When this flag is used, it will perform the operation directly. This is mainly meant to be used in scripts. Use with caution.</dl>
<p> There are two required options to i2cget. <i>i2cbus</i> indicates the number or name of the I2C bus to be scanned. This number should correspond to one of the busses listed by <i>i2cdetect -l</i>. <i>chip-address</i> specifies the address of the chip on that bus, and is an integer between 0x03 and 0x77. </p>
<p> <i>data-address</i> specifies the address on that chip to read from, and is an integer between 0x00 and 0xFF. If omitted, the currently active register will be read (if that makes sense for the considered chip). </p>
<p> The <i>mode</i> parameter, if specified, is one of the letters <code>b</code>, <code>w</code> or <code>c</code>, corresponding to a read byte data, a read word data or a write byte/read byte transaction, respectively. A <code>p</code> can also be appended to the <i>mode</i> parameter to enable PEC. If the <i>mode</i> parameter is omitted, i2cget defaults to a read byte data transaction, unless <i>data-address</i> is also omitted, in which case the default (and only valid) transaction is a single read byte.</p>
<h2>Warning</h2>
<p>i2cget can be extremely dangerous if used improperly. I2C and SMBus are designed in such a way that an SMBus read transaction can be seen as a write transaction by certain chips. This is particularly true if setting <i>mode</i> to <code>cp</code> (write byte/read byte with PEC). Be extremely careful using this program.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-i2cdump/">i2cdump</a>(8), <a href="/docs/linux/man/8-i2cset/">i2cset</a>(8) </p>
<h2>Author</h2>
<p>Jean Delvare </p>
<p> This manual page was strongly inspired from those written by David Z Maze for i2cset.</p>
