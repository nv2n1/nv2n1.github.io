---
title: "i2cdetect(8)"
name: "i2cdetect"
section: "8"
letter: "i"
url: "/docs/linux/man/8-i2cdetect/"
description: "i2cdetect – detect I2C chips"
---

<p>i2cdetect &#8211; detect I2C chips </p>
<h2>Synopsis</h2>
<p><code>i2cdetect</code> [<i>-y</i>] [<i>-a</i>] [<i>-q</i>|<i>-r</i>] <i>i2cbus</i> [<i>first last</i>]<br />
 <code>i2cdetect</code> <i>-F</i> <i>i2cbus</i><br />
 <code>i2cdetect</code> <i>-V</i><br />
 <code>i2cdetect</code> <i>-l</i> </p>
<h2>Description</h2>
<p>i2cdetect is a userspace program to scan an I2C bus for devices. It outputs a table with the list of detected devices on the specified bus. <i>i2cbus</i> indicates the number or name of the I2C bus to be scanned, and should correspond to one of the busses listed by <i>i2cdetect -l</i>. The optional parameters <i>first</i> and <i>last</i> restrict the scanning range (default: from 0x03 to 0x77). i2cdetect can also be used to query the functionalities of an I2C bus (see option <code>-F</code>.) </p>
<h2>Warning</h2>
<p>This program can confuse your I2C bus, cause data loss and worse!</p>
<h2>Interpreting The Output</h2>
<p>Each cell in the output table will contain one of the following symbols:</p>
<dl>
<dt>*</p>
<dd>&quot;&#8211;&quot;. The address was probed but no chip answered.</p>
<dt>*</p>
<dd>&quot;UU&quot;. Probing was skipped, because this address is currently in use by a driver. This strongly suggests that there is a chip at this address.</p>
<dt>*</p>
<dd>An address number in hexadecimal, e.g. &quot;2d&quot; or &quot;4e&quot;. A chip was found at this address. </p>
</dl>
<h2>Options</h2>
<dl>
<dt><code>-y</code></p>
<dd>Disable interactive mode. By default, i2cdetect will wait for a confirmation from the user before messing with the I2C bus. When this flag is used, it will perform the operation directly. This is mainly meant to be used in scripts.</p>
<dt><code>-a</code></p>
<dd>Force scanning of non-regular addresses. Not recommended.</p>
<dt><code>-q</code></p>
<dd>Use SMBus &quot;quick write&quot; commands for probing (by default, the command used is the one believed to be the safest for each address). Not recommended. This is known to corrupt the Atmel AT24RF08 EEPROM found on many IBM Thinkpad laptops.</p>
<dt><code>-r</code></p>
<dd>Use SMBus &quot;read byte&quot; commands for probing (by default, the command used is the one believed to be the safest for each address). Not recommended. This is known to lock SMBus on various write-only chips (most notably clock chips at address 0x69).</p>
<dt><code>-F</code></p>
<dd>Display the list of functionalities implemented by the adapter and exit.</p>
<dt><code>-V</code></p>
<dd>Display the version and exit.</p>
<dt><code>-l</code></p>
<dd>Output a list of installed busses. </p>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-i2cdump/">i2cdump</a>(8), <a href="/docs/linux/man/8-sensors-detect/">sensors-detect</a>(8) </p>
<h2>Author</h2>
<p>Frodo Looijaard, Mark D. Studebaker and Jean Delvare </p>
<p> This manual page was originally written by Aurelien Jarno &lt;aurel32 [at] debian.org&gt;, for the Debian GNU/Linux system.</p>
