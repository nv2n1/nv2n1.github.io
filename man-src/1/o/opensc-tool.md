---
title: "opensc-tool(1)"
name: "opensc-tool"
section: "1"
letter: "o"
url: "/docs/linux/man/1-opensc-tool/"
description: "opensc-tool – generic smart card utility"
---

<h2 class="name">NAME</h2>
<p> opensc-tool &#8211; generic smart card utility </p>
<h2>SYNOPSIS</h2>
<p> <code>opensc-tool</code> [OPTIONS]</p>
<h2>DESCRIPTION</h2>
<p> The <code>opensc-tool</code> utility can be used from the command line to perform miscellaneous smart card operations such as getting the card ATR or sending arbitrary APDU commands to a card.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;atr, -a</code></p>
<dl>
<dt>
</dt><dd> Print the Answer To Reset (ATR) of the card, output is in hex byte format</dd></dl>
<p> <code>&#8211;serial</code></p>
<dl>
<dt>
</dt><dd> Print the card serial number (normally the ICCSN), output is in hex byte format</dd></dl>
<p> <code>&#8211;send-apdu</code> apdu, <code>-s</code> apdu</p>
<dl>
<dt>
</dt><dd> Sends an arbitrary APDU to the card in the format AA:BB:CC:DD:EE:FF&#8230;</dd></dl>
<p> <code>&#8211;list-files, -f</code></p>
<dl>
<dt>
</dt><dd> Recursively lists all files stored on card</dd></dl>
<p> <code>&#8211;list-readers, -l</code></p>
<dl>
<dt>
</dt><dd> Lists all configured readers</dd></dl>
<p> <code>&#8211;list-drivers, -D</code></p>
<dl>
<dt>
</dt><dd> Lists all installed card drivers</dd></dl>
<p> <code>&#8211;list-rdrivers, -R</code></p>
<dl>
<dt>
</dt><dd> Lists all installed reader drivers</dd></dl>
<p> <code>&#8211;reader</code> num, <code>-r</code> num</p>
<dl>
<dt>
</dt><dd> Use the given reader number. The default is 0, the first reader in the system.</dd></dl>
<p> <code>&#8211;card-driver</code> driver, <code>-c</code> driver</p>
<dl>
<dt>
</dt><dd> Use the given card driver. The default is auto-detected.</dd></dl>
<p> <code>&#8211;verbose, -v</code></p>
<dl>
<dt>
</dt><dd> Causes <code>opensc-tool</code> to be more verbose. Specify this flag several times to enable debug output in the opensc library.</dd></dl>
<h2>SEE ALSO</h2>
<p> opensc(7), <a href="/docs/linux/man/1-opensc-explorer/">opensc-explorer</a>(1) </p>
