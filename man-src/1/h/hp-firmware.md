---

title: "hp-firmware(1)"
name: "hp-firmware"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hp-firmware/"
description: "hp-firmware – Firmware Download Utility"
---

<p> Download firmware to a device that requires downloaded firmware to function. (Note: Most printers do not require the use of this utility).</p>
<p> <code>hp-firmware [DEVICE_URI|PRINTER_NAME] [MODE] [OPTIONS]</code></p>
<h2>PRINTER|DEVICE-URI</h2>
<dl>
<dt>To specify a device-URI:</dt>
<dd> -d&lt;device-uri&gt; or &#8211;device=&lt;device-uri&gt;</dd>
<dt>To specify a CUPS printer:</dt>
<dd> -p&lt;printer&gt; or &#8211;printer=&lt;printer&gt;</dd></dl>
<h2>MODE</h2>
<dl>
<dt>Run in interactive mode:</dt>
<dd> -i or &#8211;interactive</dd>
<dt>Run in non-interactive mode:</dt>
<dd> -n or &#8211;non-interactive</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt>Set the logging level:</dt>
<dd> -l&lt;level&gt; or &#8211;logging=&lt;level&gt; &lt;level&gt;: none, info*, error, warn, debug (*default)</dd>
<dt>Run in debug mode:</dt>
<dd> -g (same as option: -ldebug)</dd>
<dt>This help information:</dt>
<dd> -h or &#8211;help</dd>
<dt>Use USB IDs to specify printer:</dt>
<dd> -s bbb:ddd, where bbb is the USB bus ID and ddd is the USB device ID. The &#8216;:&#8217; and all leading zeroes must be present.</dd>
<dt>Seconds to delay before download:</dt>
<dd> -y&lt;secs&gt; or &#8211;delay=&lt;secs&gt; (float value, e.g. 0.5)</dd></dl>
<h2>SEE ALSO</h2>
<p> hp-plugin hp-toolbox</p>
<h2>AUTHOR</h2>
<p> HPLIP (HP Linux Imaging and Printing) is an HP developed solution for printing, scanning, and faxing with HP inkjet and laser based printers in Linux.</p>
<h2>REPORTING BUGS</h2>
<p> The HPLIP Launchpad.net site <code><a rel="nofollow" href="https://launchpad.net/hplip">https://launchpad.net/hplip</a></code> is available to get help, report bugs, make suggestions, discuss the HPLIP project or otherwise contact the HPLIP Team.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2001-18 HP Development Company, L.P. </p>
<p> This software comes with ABSOLUTELY NO WARRANTY. This is free software, and you are welcome to distribute it under certain conditions. See COPYING file for more details. </p>
