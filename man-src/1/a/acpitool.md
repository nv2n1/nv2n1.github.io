---
title: "acpitool(1)"
name: "acpitool"
section: "1"
letter: "a"
url: "/docs/linux/man/1-acpitool/"
description: "acpitool – a Linux ACPI client, allowing you to query or set ACPI values"
---

<h2>NAME</h2>
<p> acpitool &#8211; a Linux ACPI client, allowing you to query or set ACPI values</p>
<h2>SYNOPSIS</h2>
<p> <code>acpitool [ -aAbBcefFhjlmnosStTvVwWz ]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>acpitool </code> is a Linux ACPI client. It simply reads <i>/proc/acpi </i> or <i>/sys/class </i> entries and presents the output in a meaningfull, human-readable format. </p>
<p> It provides a.o. information on battery status, AC adapter presence, thermal reading, etc. This command is most useful on laptops with an ACPI compliant BIOS and a Linux kernel, preferably from the 2.6 series, with ACPI enabled. </p>
<p> <code>Acpitool </code> also allows the machine to be put into standby, if your laptop supports it. </p>
<p> If your laptop is a <code>Toshiba</code> , it allows you to set the LCD brighness level and toggle the fan on/off. </p>
<p> If you have an <code>Asus</code> laptop, it can also set the LCD brightness level, switch the LCD panel on or off, and control the mail led and wireless led. </p>
<p> If you have an <code>IBM Thinkpad</code> laptop, it can once again set the LCD brightness level, and also eject the ultrabay device. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a, &#8211;ac_adapter </code></dt>
<dd> Show AC adapter presence</dd>
<dt><code>-A </code></dt>
<dd> Show supported Asus ACPI extensions (LCD brightness level, video out routing DSDT/acpi4asus info)</dd>
<dt><code>-b</code></dt>
<dd> Show battery status information, available batteries only.</dd>
<dt><code>-B, &#8211;battery</code></dt>
<dd> Show detailed battery status information, for all battery entries found.</dd>
<dt><code>-c, &#8211;cpu</code></dt>
<dd> Show CPU information (type, speed, PM capabilities, throttling states, c-state usage, frequency scaling).</dd>
<dt><code>-e</code></dt>
<dd> Show just about everything : more info on the batteries, ACPI version, kernel version, CPU, . . .</dd>
<dt><code>-f, &#8211;fan</code></dt>
<dd> Show fan status (shows fan info specific to Toshiba or IBM Thinkpad, if applicable).</dd>
<dt><code>-F x</code></dt>
<dd> Force the fan on (x=1) or switch back to auto mode (x=0). Works only on Toshiba laptops. The fan is switched off ONLY if it was forced on first, not if it was switched on automatically. Requires write access to <i>/proc/acpi/toshiba/fan</i></dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> Show help text.</dd>
<dt><code>-j</code></dt>
<dd> Eject Thinkpad ultrabay device. Requires write acces to <i>/proc/acpi/ibm/bay</i></dd>
<dt><code>-l x</code></dt>
<dd> Set LCD brightness level to x, where x is in the range 0..7. Works only on Toshiba and IBM Thinkpad laptops. Requires write access to <i>/proc/acpi/tochiba/lcd</i> or <i>/proc/acpi/ibm/brightness</i><br />
 Illegal values for x will result in the value being set to either 0 or 7.</dd>
<dt><code>-m x</code></dt>
<dd> Switch the mail led on (x=1) or off (x=0). Works only on Asus laptops. Requires write access to <i>/proc/acpi/asus/mled</i> </dd>
<dt><code>-n x</code></dt>
<dd> Switch the wireless led on (x=1) or off (x=0). Works only on Asus laptops. Requires write access to <i>/proc/acpi/asus/wled</i> </dd>
<dt><code>-o x</code></dt>
<dd> Switch the LCD panel on (x=1) or off (x=0). Works only on Asus laptops. Requires write access to <i>/proc/acpi/asus/lcd</i> </dd>
<dt><code>-s, &#8211;suspend to memory</code></dt>
<dd> Put the machine into sleep state S3, if possible. Requires write access to <i>/proc/acpi/sleep </i> (kernel 2.4.x) or <i>/sys/power/state</i> (kernel 2.6.x)</dd>
<dt><code>-S, &#8211;suspend to disk ?</code></dt>
<dd> Put the machine into sleep state S4, if possible. Requires write access to <i>/proc/acpi/sleep </i> (kernel 2.4.x) or <i>/sys/power/state</i> (kernel 2.6.x)</dd>
<dt><code>-t, &#8211;thermal</code></dt>
<dd> Show thermal zone(s) information, including trip_points.</dd>
<dt><code>-T, &#8211;Toshiba</code></dt>
<dd> Show supported Toshiba ACPI extensions, currently being LCD brightness level, video out routing (what display is the video chip sending to) and fan status (on/off, forced or not).</dd>
<dt><code>-v</code></dt>
<dd> Show more verbose output when something is not found. Makes sense only when used together with other options.</dd>
<dt><code>-V, &#8211;version</code></dt>
<dd> Show acpitool version number and release date, then exit.</dd>
<dt><code>-w</code></dt>
<dd> Show the wakeup capable devices. (Available since ACPI 20040715, check your version).</dd>
<dt><code>-W x</code></dt>
<dd> Enable/disable wakeup capable device x. Run &#8216;acpitool -w&#8217; to see valid numbers for x. Requires write access to <i>/proc/acpi/wakeup</i></dd>
<dt><code>-z x</code></dt>
<dd> Set Asus LCD brightness level to x, where x is 0..15. Works only on Asus laptops. Requires write access to <i>/proc/acpi/asus/brn</i></dd></dl>
<h2>REMARKS</h2>
<p> This program absolutely requires a Linux kernel with ACPI support enabled. This program will not work without it. </p>
<p> IBM Thinkpad support is part of the Linux kernel since kernel 2.6.10. </p>
<p> Don&#8217;t blame me if <code>acpitool</code> can&#8217;t suspend your laptop : there are quite some problematic laptops out there. Check the acpi-bugzilla list if you don&#8217;t believe me ;) </p>
<p> Note that some options, like -F, -l , -j, -s, -W and -z, require write access to some of the <i>/proc/acpi</i> entries. This requires <code>acpitool</code> either to be run as <code>root</code> or either administrative measures must be taken, most likely by root, to allow ordinary users to write to these files. Creating a group for ACPI users and setting permissions accordingly comes to mind. </p>
<p> Also note that older laptops (&lt; 2000) often simply don&#8217;t have ACPI support, they usually support APM only.</p>
<h2>BUGS</h2>
<p> Let me know if you think you found one.</p>
<h2>FILES</h2>
<p> <i>/proc/acpi/&#8230;</i><br />
 <i>/proc/acpi/toshiba</i><br />
 <i>/proc/acpi/asus</i><br />
 <i>/proc/acpi/ibm</i><br />
 <i>/sys/power/state</i></p>
<h2>HOMEPAGE</h2>
<p> <a rel="nofollow" href="http://freeunix.dyndns.org:8000/site2/acpitool.shtml">http://freeunix.dyndns.org:8000/site2/acpitool.shtml</a></p>
<h2>AUTHOR</h2>
<p> This program is written and maintained by David Leemans (davidleemans |at| scarlet |dot| be) and may be freely distributed under the terms of the GNU General Public License. There is ABSOLUTELY NO WARRANTY for this program. </p>
