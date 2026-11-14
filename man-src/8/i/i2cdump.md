---
title: "i2cdump(8)"
name: "i2cdump"
section: "8"
letter: "i"
url: "/docs/linux/man/8-i2cdump/"
description: "i2cdump – examine I2C registers"
---

<p>i2cdump &#8211; examine I2C registers </p>
<h2>Synopsis</h2>
<p><code>i2cdump</code> [<code>-f</code>] [<code>-r first-last</code>] [<code>-y</code>] <i>i2cbus</i> <i>address</i> [<i>mode </i>[<i>bank </i>[<i>bankreg</i>]]]<br />
 <code>i2cdump</code> <code>-V</code> </p>
<h2>Description</h2>
<p>i2cdump is a small helper program to examine registers visible through the I2C bus. </p>
<h2>Options</h2>
<dl>
<dt><code>-V</code></p>
<dd>Display the version and exit.</p>
<dt><code>-f</code></p>
<dd>Force access to the device even if it is already busy. By default, i2cdump will refuse to access a device which is already under the control of a kernel driver. Using this flag is dangerous, it can seriously confuse the kernel driver in question. It can also cause i2cdump to return invalid results. So use at your own risk and only if you know what you&#8217;re doing.</p>
<dt><code>-r first-last</code></p>
<dd>Limit the range of registers being accessed. This option is only available with modes <code>b</code>, <code>w</code>, <code>c</code> and <code>W</code>. For mode <code>W</code>, <code>first</code> must be even and <code>last</code> must be odd.</p>
<dt><code>-y</code></p>
<dd>Disable interactive mode. By default, i2cdump will wait for a confirmation from the user before messing with the I2C bus. When this flag is used, it will perform the operation directly. This is mainly meant to be used in scripts.</dl>
<p> At least two options must be provided to i2cdump. <i>i2cbus</i> indicates the number or name of the I2C bus to be scanned. This number should correspond to one of the busses listed by <i>i2cdetect -l</i>. <i>address</i> indicates the address to be scanned on that bus, and is an integer between 0x03 and 0x77. </p>
<p> The <i>mode</i> parameter, if specified, is one of the letters <code>b</code>, <code>w</code>, <code>s</code>, or <code>i</code>, corresponding to a read size of a single byte, a 16-bit word, an SMBus block, an I2C block, respectively. The <code>c</code> mode is a little different, it reads all bytes consecutively, and is useful for chips that have an address auto-increment feature, such as EEPROMs. The <code>W</code> mode is also special, it is similar to <code>w</code> except that a read command will only be issued on even register addresses; this is again mainly useful for EEPROMs. </p>
<p> A <code>p</code> can also be appended to the <i>mode</i> parameter (except for <code>i</code> and <code>W</code>) to enable PEC. If the <i>mode</i> parameter is omitted, i2cdump defaults to byte access without PEC. </p>
<p> The <i>bank</i> and <i>bankreg</i> parameters are useful on the W83781D and similar chips (at the time of writing, all Winbond and Asus chips). <i>bank</i> is an integer between 0 and 7, and <i>bankreg</i> is an integer between 0x00 and 0xFF (default value: 0x4E). The W83781D data sheet has more information on bank selection.</p>
<h2>Warning</h2>
<p>i2cdump can be dangerous if used improperly. Most notably, the <code>c</code> mode starts with WRITING a byte to the chip. On most chips it will be stored in the address pointer register, which is OK, but some chips with a single register or no (visible) register at all will most likely see this as a real WRITE, resulting in possible misbehavior or corruption. Do not use i2cdump on random addresses. Anyway, it is of little use unless you have good knowledge of the chip you&#8217;re working with and an idea of what you are looking for.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-i2cset/">i2cset</a>(8), <a href="/docs/linux/man/8-i2cdetect/">i2cdetect</a>(8), <a href="/docs/linux/man/8-isadump/">isadump</a>(8) </p>
<h2>Author</h2>
<p>Frodo Looijaard, Mark D. Studebaker and Jean Delvare </p>
<p> This manual page was originally written by David Z Maze &lt;dmaze [at] debian.org&gt; for the Debian GNU/Linux system.</p>
