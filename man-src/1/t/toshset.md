---
title: "toshset(1)"
name: "toshset"
section: "1"
letter: "t"
url: "/docs/linux/man/1-toshset/"
description: "toshset – manipulate bios and hardware settings of Toshiba laptops"
---

<h2 class="name">NAME</h2>
<p> toshset &#8211; manipulate bios and hardware settings of Toshiba laptops </p>
<h2>SYNOPSIS</h2>
<p> <code>toshset</code> [<i>TOGGLEOPTIONS</i> | <i>QUERYOPTIONS</i> | <i>FEATUREOPTIONS</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Toshset ia a command-line tool to allow access to much of the Toshiba hardware interface developed by Jonathan Buzzard. It can do things like set the hard drive spin-down time, turn off the display and set the fan speed. </p>
<p> Credit for the difficult task of reverse-engineering the Toshiba hardware interface goes to Jonathan Buzzard. A link for Jonathan&#8217;s tools is <a rel="nofollow" href="http://www.buzzard.org.uk/toshiba/">http://www.buzzard.org.uk/toshiba/</a> </p>
<p> All options are listed by running toshset with no arguments. </p>
<p> If an argument option is specified as the &#8220;-&#8221; character, stdin is read for that option. This is particularly convenient when setting the owner string. </p>
<p> The method used for access to the laptop hardware is given by the the HCI/SCI access mode query field. This should be kernel or direct. The kernel method requires kernel support and it is the only access method supported for ACPI kernels. If ACPI is not used this package does not require a special kernel module. Also, it is highly likely that this tool will work under different flavors of *NIX. As a result of this design consideration, and because of my own desire that not every user be able to change my laptop&#8217;s hardware settings, the user must have read/write permission to /dev/toshiba in order for this program to run properly. </p>
<h3>Toggle Options:</h3>
<dl>
<dt><code>-l</code></dt>
<dd> toggle long query in which the assocated command-line option is printed with each queried feature.</dd>
<dt><code>-fast</code></dt>
<dd> run in fast mode: a startup check is skipped, and values are not queried after the are set. On machines for which ioctl is slow, this can speed toshset up by up to a factor of 2/5.</dd>
<dt><code>-v</code></dt>
<dd> toggle verbose mode in which normally silent messages are printed.</dd></dl>
<h3>Query Options:</h3>
<dl>
<dt><code>-q</code> <i> [glob]</i></dt>
<dd> query features specified by glob (all features if glob omitted). The glob string is sandwiched between asterisks, so specifying -q bat will query all features whose names contain the &#8220;bat&#8221; substring. If no glob is given, then all features are queried.</dd></dl>
<h3>Feature Options:</h3>
<p> Valid settings for features can be listed by omitting the argument. The current list of feature options is</p>
<dl>
<dt><code>-b</code> <i> &lt;off|on&gt; </i></dt>
<dd> enable/disable system beep</dd>
<dt><code>-lcd</code> <i>&lt;setting&gt;</i></dt>
<dd> set lcd brightness.</dd>
<dt><code>-inten</code> <i>&lt;setting&gt;</i></dt>
<dd> set lcd brightness. Not all models support both -lcd and -inten.</dd>
<dt><code>-pow</code> <i>&lt;setting&gt;</i></dt>
<dd> set power-up mode</dd>
<dt><code>-vol</code> <i>&lt;0-4&gt;</i></dt>
<dd> set beep volume. Note that this controls the modem volume for my PCMCIA modem.</dd>
<dt><code>-hdd</code> <i>&lt;num&gt;</i></dt>
<dd> number of minutes until disk spindown</dd>
<dt><code>-dstretch</code> <i>&lt;off|on&gt;</i></dt>
<dd> enable/disable display stretch</dd>
<dt><code>-d</code> <i>&lt;num&gt;</i></dt>
<dd> number of minutes until display auto-off</dd>
<dt><code>-c</code> <i>&lt;method&gt;</i></dt>
<dd> set cooling method</dd>
<dt><code>-bs</code> <i>&lt;setting&gt;</i></dt>
<dd> set battery-save mode</dd>
<dt><code>-bl</code> <i>&lt;off|on&gt;</i></dt>
<dd> control lcd backlight</dd>
<dt><code>-bluetooth</code> <i>&lt;off|on&gt;</i></dt>
<dd> power-up + attach internal bluetooth device, or shutdown.</dd>
<dt><code>-fan</code> <i>&lt;setting&gt;</i></dt>
<dd> control fan</dd>
<dt><code>-video</code> <i>&lt;int|ext|both|tv|mode5|mode6|mode7&gt;</i></dt>
<dd> set display device for video: internal lcd, external monitor, or tv-out</dd>
<dt><code>-cpu</code> <i>&lt;slow|fast&gt;</i></dt>
<dd> set CPU speed</dd>
<dt><code>-cpucache</code> <i>&lt;off|on&gt;</i></dt>
<dd> enable/disable CPU cache</dd>
<dt><code>-sleep</code> <i>&lt;off|on&gt;</i></dt>
<dd> enable/disable CPU sleep mode</dd>
<dt><code>-balarm</code> <i>&lt;off|on&gt;</i></dt>
<dd> enable/disable battery alarm</dd>
<dt><code>-palarm</code> <i>&lt;off|on&gt;</i></dt>
<dd> enable/disable lid-closed alarm</dd>
<dt><code>-walarm</code> <i>&lt;dis|HH:MM[/everyday|DD/MM[/YYYY]]&gt;</i></dt>
<dd> set time/date to wake</dd>
<dt><code>-ppower</code> <i>&lt;off|on&gt;</i></dt>
<dd> enable/disable annoying feature of powering-off computer when lid is closed.</dd>
<dt><code>-parallel</code> <i>&lt;mode&gt;</i></dt>
<dd> set parallel port mode</dd>
<dt><code>-autooff</code> &lt;num&gt;</dt>
<dd> number of minutes of idle time until system auto-off</dd>
<dt><code>-ostring</code> <i>&lt;owner string&gt;</i></dt>
<dd> set owner string. This string is displayed at boot or resume time, if a user or supervisor password is set.</dd>
<dt><code>-upasswd</code></dt>
<dd> set or clear the user password. Toshset must be run on the console for this to work. The password should be entered when the prompt is displayed. If the password is currently set, entering it will clear the password.</dd>
<dt><code>-spasswd</code></dt>
<dd> set the supervisor password. See the docs for -upasswd.</dd>
<dt><code>-usblegacy</code></dt>
<dd> USB legacy mode: enable/disable using an USB mouse as it would be a PS/2 one, without the need to install a USB driver.</dd>
<dt><code>-3g</code></dt>
<dd> power-up + attach internal 3g modem device, or shutdown.</dd>
<dt><code>-usbfdd</code></dt>
<dd> USB FDD emulation mode: is almost the same of the previous one for a floppy. It enables the use of an USB floppy as it would be attached to an internal FD controller (for booting etc.)</dd>
<dt><code>-lan</code></dt>
<dd> Enables/disables internal LAN controller.</dd>
<dt><code>-soundlogo</code></dt>
<dd> enable/disable startup sound logo.</dd>
<dt><code>-startlogo</code></dt>
<dd> startup logo mode (picture or animation&gt;.</dd>
<dt><code>-trmode</code></dt>
<dd> enable/disable the display&#8217;s transreflective mode. </dd>
<p> Features may also be set by specifying the (zero-offset) index of the option. e.g. toshset -cpu 0 sets the cpu speed to slow. </p>
</dl>
<h2>BUGS</h2>
<p> Many features are locked and can not be changed when the battery save mode is not &#8220;user.&#8221; Since I only have one laptop, I can&#8217;t test this utility on other hardware. User feedback in this regard is helpful. Some features do not work on my laptop and they may work on your&#8217;s, and visa-versa. </p>
<p> Toshset requires an experimental version of the toshiba_acpi kernel module with an ACPI-enabled kernel. </p>
<h2>AUTHOR</h2>
<p> Written by &lt;Charles [at] Schwieters.org&gt;<br />
 News, updates and documentation: visit <a rel="nofollow" href="http://schwieters.org/toshset.html">http://schwieters.org/toshset.html</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2002-8 Charles D. Schwieters<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
