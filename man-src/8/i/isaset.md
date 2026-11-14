---
title: "isaset(8)"
name: "isaset"
section: "8"
letter: "i"
url: "/docs/linux/man/8-isaset/"
description: "isaset – set ISA registers"
---

<p>isaset &#8211; set ISA registers</p>
<h2>Synopsis</h2>
<p><code>isaset</code> [<code>-y</code>] [<code>-W</code>|<code>-L</code>] <i>addrreg</i> <i>datareg</i> <i>address</i> <i>value</i> [<i>mask</i>] #for I2C-like access<br />
 <code>isaset</code> <code>-f</code> [<code>-y</code>] [<code>-W</code>|<code>-L</code>] <i>address</i> <i>value</i> [<i>mask</i>] #for flat address space </p>
<h2>Description</h2>
<p>isaset is a small helper program to set registers visible through the ISA bus. </p>
<h2>Options</h2>
<dl>
<dt><code>-f</code></p>
<dd>Enable flat address space mode.</p>
<dt><code>-y</code></p>
<dd>Disable interactive mode. By default, isaset will wait for a confirmation from the user before messing with the ISA bus. When this flag is used, it will perform the operation directly. This is mainly meant to be used in scripts.</p>
<dt><code>-W</code></p>
<dd>Perform a 16-bit write.</p>
<dt><code>-L</code></p>
<dd>Perform a 32-bit write. </p>
</dl>
<h2>OPTIONS (I2C-like access mode)</h2>
<p>Four options must be provided to isaset. <i>addrreg</i> contains the ISA address of the address register for the chip to probe; <i>datareg</i> contains the address of the data register. Both addresses are integers between 0x0000 and 0x3FFF. Usually, if the chip&#8217;s base address is 0x0nn0, the address register is at 0x0nn5 and the data register is at 0x0nn6. The most common base address for hardware monitoring chips is 0x0290. For Super-I/O chips, address register is typically at 0x2E with data register at 0x2F. The <i>address</i> and <i>value</i> parameters are two integers between 0x00 and 0xFF. isaset will write value <i>value</i> to address <i>address</i>. An optional <i>mask</i> can be provided as a fifth parameter, preserving unmasked bits at the written location.</p>
<h2>OPTIONS (flat address space mode)</h2>
<p>In flat mode, two parameters must be provided. <i>address</i> contains the ISA address of the register to write to; it is an integer between 0x0000 and 0xFFFF. Basically, it is the sum of the chip&#8217;s base address and the chip register&#8217;s address. isaset will write value <i>value</i> at this address. An optional <i>mask</i> can be provided as a third parameter, preserving unmasked bits at the written location.</p>
<h2>Warning</h2>
<p>Poking around in ISA data space is extremely dangerous. Running isaset with random parameters can cause system crashes, data loss, and worse! Be extremely careful when using this program.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-i2cset/">i2cset</a>(8), <a href="/docs/linux/man/8-isadump/">isadump</a>(8) </p>
<h2>Author</h2>
<p>Mark D. Studebaker, and the lm_sensors group (<a rel="nofollow" href="https://hwmon.wiki.kernel.org/lm_sensors)">https://hwmon.wiki.kernel.org/lm_sensors)</a> </p>
<p> This manual page was shamelessly ripped from the i2cset and isadump manual pages by Jean Delvare.</p>
