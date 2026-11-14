---
title: "i2c-stub-from-dump(8)"
name: "i2c-stub-from-dump"
section: "8"
letter: "i"
url: "/docs/linux/man/8-i2c-stub-from-dump/"
description: "i2c-stub-from-dump – feed i2c-stub with a dump file"
---

<p>i2c-stub-from-dump &#8211; feed i2c-stub with a dump file </p>
<h2>Synopsis</h2>
<p><code>i2c-stub-from-dump </code> <i>address</i> <i>dump-file</i> </p>
<h2>Description</h2>
<p>i2c-stub-from-dump is a small helper script for the i2c-stub kernel driver. It lets you setup a fake I2C chip on the i2c-stub bus based on a dump of the chip you want to emulate. i2c-stub-from-dump requires i2cdetect and i2cset to be installed and reachable through the user&#8217;s PATH. The former is used to find out the i2c-stub bus number, while the latter is used to write to the fake I2C chip. </p>
<h2>Example</h2>
<p>You have an I2C chip on system A. You would like to do some development on its driver on system B. Here are the few steps you have to follow. On system A, use i2cdump to capture a dump from the chip. Assuming that the chip in question lives at address 0x4c on I2C bus 0, you would run:<br />
&nbsp;<wbr>&nbsp;<wbr>i2cdump -y 0 0x4c b&nbsp;<wbr>&gt;&nbsp;<wbr>chip.dump Adjust the bus number and chip address for your case. i2cdetect can help you find out their values. If the device uses word (16-bit) register access instead of the traditional byte (8-bit) access, use mode <code>w</code> instead of <code>b</code>. Copy the dump file to system B. On system B, run:<br />
&nbsp;<wbr>&nbsp;<wbr>i2c-stub-from-dump 0x4c chip.dump This will load the required i2c-dev and i2c-stub kernel drivers if needed, then write all the register values to the emulated I2C chip at address 0x4c. Again, adjust the address as needed. </p>
<h2>Limitations</h2>
<p>There are some limitations to the kind of devices that can be handled:</p>
<dl>
<dt>*</p>
<dd>Device must not have banks (as most Winbond devices do). </p>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-i2cdump/">i2cdump</a>(8), <a href="/docs/linux/man/8-i2cdetect/">i2cdetect</a>(8), <a href="/docs/linux/man/8-i2cset/">i2cset</a>(8) </p>
<h2>Author</h2>
<p>Jean Delvare</p>
