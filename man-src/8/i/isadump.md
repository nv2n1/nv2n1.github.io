---
title: "isadump(8)"
name: "isadump"
section: "8"
letter: "i"
url: "/docs/linux/man/8-isadump/"
description: "isadump – examine ISA registers"
---

<p>isadump &#8211; examine ISA registers</p>
<h2>Synopsis</h2>
<p><code>isadump</code> [<code>-y</code>] [<code>-W</code>|<code>-L</code>] [<code>-k V1,V2&#8230;</code>] <i>addrreg</i> <i>datareg</i> [<i>bank </i>[<i>bankreg</i>]] #for I2C-like access<br />
 <code>isadump</code> <code>-f</code> [<code>-y</code>] [<code>-W</code>|<code>-L</code>] <i>address</i> [<i>range </i>[<i>bank </i>[<i>bankreg</i>]]] #for flat address space </p>
<h2>Description</h2>
<p>isadump is a small helper program to examine registers visible through the ISA bus. It is intended to probe any chip that lives on the ISA bus working with an address register and a data register (I2C-like access) or a flat range (of up to 256 bytes). </p>
<h2>Options</h2>
<dl>
<dt><code>-f</code></p>
<dd>Enable flat address space mode.</p>
<dt><code>-y</code></p>
<dd>Disable interactive mode. By default, isadump will wait for a confirmation from the user before messing with the ISA bus. When this flag is used, it will perform the operation directly. This is mainly meant to be used in scripts.</p>
<dt><code>-k V1,V2&#8230;</code></p>
<dd>Specify a comma-separated list of bytes to send as the key sequence to enter the chip configuration mode. Most Super-I/O chips need this. Known key sequences are: 0x87,0x01,0x55,0x55 for ITE, 0x55 for SMSC, 0x87,0x87 for Winbond and VIA, none needed for National Semiconductor.</p>
<dt><code>-W</code></p>
<dd>Perform 16-bit reads.</p>
<dt><code>-L</code></p>
<dd>Perform 32-bit reads. </p>
</dl>
<h2>OPTIONS (I2C-like access mode)</h2>
<p>At least two options must be provided to isadump. <i>addrreg</i> contains the ISA address of the address register for the chip to probe; <i>datareg</i> contains the address of the data register. Both addresses are integers between 0x0000 and 0x3FFF. Usually, if the chip&#8217;s base address is 0x0nn0, the address register is at 0x0nn5 and the data register is at 0x0nn6. The most common base address for hardware monitoring chips is 0x0290. </p>
<p> For Super-I/O chips, address register is typically at 0x2E with data register at 0x2F. </p>
<p> The <i>bank</i> and <i>bankreg</i> parameters are useful on the Winbond chips as well as on Super-I/O chips. <i>bank</i> is an integer between 0 and 31, and <i>bankreg</i> is an integer between 0x00 and 0xFF (default value: 0x4E for Winbond chips, 0x07 for Super-I/O chips). The W83781D datasheet has more information on bank selection.</p>
<h2>OPTIONS (flat address space mode)</h2>
<p>In flat mode, only one parameter is mandatory. <i>address</i> contains the ISA address of the chip to probe; it is an integer between 0x0000 and 0xFFFF. If provided, <i>range</i> is how many bytes should be read (must be a multiple of 16). If the range isn&#8217;t provided, it defaults to 256 bytes and the address is forcibly aligned on a 256-byte boundary. </p>
<p> The <i>bank</i> and <i>bankreg</i> parameters are useful on the National Semiconductor PC87365 and PC87366 Super-I/O chips. <i>bank</i> is an integer between 0 and 31, and <i>bankreg</i> is an integer between 0x00 and 0xFF (default value: 0x09; must fit in the specified range). See the PC87365 datasheet for more information on bank selection.</p>
<h2>Notes</h2>
<p>If no bank is specified, no bank change operation is performed. If a bank is specified, the original value is restored before isadump exits. Dumping Super-I/O chips is typically a two-step process. First, you will have to access the main Super-I/O address using a command like: isadump 0x2e 0x2f 0x09. This will select logical device 9 (correct value depend on the chip). At 0x60 you will find the logical device address word, for example &quot;ec c0&quot;. Then you can use a command like: isadump -f 0xecc0 16. This will dump the logical device registers. The correct range depends on the chip. </p>
<h2>Warning</h2>
<p>Poking around in ISA data space is extremely dangerous. Running isadump with random parameters can cause system crashes, data loss, and worse! Be extremely careful when using this program.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-i2cdump/">i2cdump</a>(8), <a href="/docs/linux/man/8-isaset/">isaset</a>(8) </p>
<h2>Author</h2>
<p>Frodo Looijaard, Mark D. Studebaker, and the lm_sensors group (<a rel="nofollow" href="https://hwmon.wiki.kernel.org/lm_sensors)">https://hwmon.wiki.kernel.org/lm_sensors)</a> </p>
<p> This manual page was originally written by David Z Maze &lt;dmaze [at] debian.org&gt; for the Debian GNU/Linux system. It was then reviewed and augmented by the lm_sensors team and is now part of the lm_sensors source distribution.</p>
