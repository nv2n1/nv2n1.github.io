---
title: "tunelp(8)"
name: "tunelp"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tunelp/"
description: "tunelp – set various parameters for the lp device"
---

<p>tunelp &#8211; set various parameters for the lp device</p>
<h2>Synopsis</h2>
<p><code>tunelp</code> <i>device</i> [<code>-i</code> <i>IRQ</i>] [<code>-t</code> <i>TIME</i>] [<code>-c</code> <i>CHARS</i>] [<code>-w</code> <i>WAIT</i>] [<code>-a</code> {<code>on</code>|<code>off</code>}] [<code>-o</code> {<code>on</code>|<code>off</code>}] [<code>-C</code> {<code>on</code>|<code>off</code>}] [<code>-r</code>] [<code>-s</code>] [<code>-q</code> {<code>on</code>|<code>off</code>}] [<code>-T</code> {<code>on</code>|<code>off</code>}]</p>
<h2>Description</h2>
<p><code>tunelp</code> sets several parameters for the /dev/lp<i>?</i> devices, for better performance (or for any performance at all, if your printer won&#8217;t work without it&#8230;) Without parameters, it tells whether the device is using interrupts, and if so, which one. With parameters, it sets the device characteristics accordingly. The parameters are as follows:</p>
<dl>
<dt><code>-i</code><i> IRQ</i></p>
<dd>specifies the IRQ to use for the parallel port in question. If this is set to something non-zero, -t and -c have no effect. If your port does not use interrupts, this option will make printing stop. The command <code>tunelp -i 0</code> restores non-interrupt driven (polling) action, and your printer should work again. If your parallel port does support interrupts, interrupt-driven printing should be somewhat faster and efficient, and will probably be desirable. NOTE: This option will have no effect with kernel 2.1.131 or later since the irq is handled by the parport driver. You can change the parport irq for example via <i>/proc/parport/*/irq</i>. Read <i>/usr/src/linux/Documentation/parport.txt</i> for more details on parport.</p>
<dt><code>-t</code><i> TIME</i></p>
<dd>is the amount of time in jiffies that the driver waits if the printer doesn&#8217;t take a character for the number of tries dictated by the -c parameter. 10 is the default value. If you want fastest possible printing, and don&#8217;t care about system load, you may set this to 0. If you don&#8217;t care how fast your printer goes, or are printing text on a slow printer with a buffer, then 500 (5 seconds) should be fine, and will give you very low system load. This value generally should be lower for printing graphics than text, by a factor of approximately 10, for best performance.</p>
<dt><code>-c</code><i> CHARS</i></p>
<dd>is the number of times to try to output a character to the printer before sleeping for -t <i>TIME</i>. It is the number of times around a loop that tries to send a character to the printer. 120 appears to be a good value for most printers in polling mode. 1000 is the default, because there are some printers that become jerky otherwise, but you <i>must</i> set this to `1&#8242; to handle the maximal CPU efficiency if you are using interrupts. If you have a very fast printer, a value of 10 might make more sense even if in polling mode. If you have a <i>really</i> old printer, you can increase this further. Setting -t <i>TIME</i> to 0 is equivalent to setting -c <i>CHARS</i> to infinity.</p>
<dt><code>-w</code><i> WAIT</i></p>
<dd>is the number of usec we wait while playing with the strobe signal. While most printers appear to be able to deal with an extremely short strobe, some printers demand a longer one. Increasing this from the default 1 may make it possible to print with those printers. This may also make it possible to use longer cables. It&#8217;s also possible to decrease this value to 0 if your printer is fast enough or your machine is slow enough.</p>
<dt><code>-a</code> {<code>on</code>|<code>off</code>}</p>
<dd>This is whether to abort on printer error &#8211; the default is not to. If you are sitting at your computer, you probably want to be able to see an error and fix it, and have the printer go on printing. On the other hand, if you aren&#8217;t, you might rather that your printer spooler find out that the printer isn&#8217;t ready, quit trying, and send you mail about it. The choice is yours.</p>
<dt><code>-o</code> {<code>on</code>|<code>off</code>}</p>
<dd>This option is much like -a. It makes any <i>open()</i> of this device check to see that the device is on-line and not reporting any out of paper or other errors. This is the correct setting for most versions of lpd.</p>
<dt><code>-C</code> {<code>on</code>|<code>off</code>}</p>
<dd>This option adds extra (&quot;careful&quot;) error checking. When this option is on, the printer driver will ensure that the printer is on-line and not reporting any out of paper or other errors before sending data. This is particularly useful for printers that normally appear to accept data when turned off. NOTE: This option is obsolete because it&#8217;s the default in 2.1.131 kernel or later.</p>
<dt><code>-s</code></p>
<dd>This option returns the current printer status, both as a decimal number from 0..255, and as a list of active flags. When this option is specified, -q off, turning off the display of the current IRQ, is implied.</p>
<dt><code>-T</code> {<code>on</code>|<code>off</code>}</p>
<dd>This option is obsolete. It was added in Linux 2.1.131, and removed again in Linux 2.3.10. The below is for these old kernels only. This option tells the lp driver to trust or not the IRQ. This option makes sense only if you are using interrupts. If you tell the lp driver to trust the irq, then, when the lp driver will get an irq, it will send the next pending character to the printer unconditionally, even if the printer still claims to be BUSY. This is the only way to sleep on interrupt (and so the handle the irq printing efficiently) at least on Epson Stylus Color Printers. The lp driver automagically detects if you could get improved performance by setting this flag, and in such case it will warn you with a kernel message. NOTE: Trusting the irq is reported to corrupt the printing on some hardware, you must try to know if your printer will work or not&#8230;</p>
<dt><code>-r</code></p>
<dd>This option resets the port. It requires a Linux kernel version of 1.1.80 or later.</p>
<dt><code>-q</code> {<code>on</code>|<code>off</code>}</p>
<dd>This option sets printing the display of the current IRQ setting. </p>
<h2>Notes</h2>
<p><code>-o</code>, <code>-C</code>, and <code>-s</code> all require a Linux kernel version of 1.1.76 or later. <code>-C</code> requires a Linux version prior to 2.1.131. <code>-T</code> requires a Linux version of 2.1.131 or later. </p>
<h2>Bugs</h2>
<p>By some unfortunate coincidence the ioctl LPSTRICT of 2.0.36 has the same number as the ioctl LPTRUSTIRQ introduced in 2.1.131. So, use of the -T option on a 2.0.36 kernel with an tunelp compiled under 2.1.131 or later may have unexpected effects. </p>
<h2>Files</h2>
<p><i>/dev/lp?</i><br />
 <i>/proc/parport/*/*</i></p>
<h2>Availability</h2>
<p>The tunelp command is part of the util-linux package and is available from <a href="ftp://ftp.kernel.org/pub/linux/utils/util-linux/.">ftp://ftp.kernel.org/pub/linux/utils/util-linux/.</a></p>
