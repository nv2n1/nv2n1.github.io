---
title: "wminput(1)"
name: "wminput"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wminput/"
description: "wminput – an event driver for the wiimote"
---

<h2 class="name">NAME</h2>
<p> wminput &#8211; an event driver for the wiimote </p>
<h2>SYNOPSIS</h2>
<p> <code>wminput</code> [<i>options</i>] </p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>wminput</code> command. </p>
<p> <code>wminput</code> is a program that provides an event driver for the wiimote, supporting all buttons (except Power) and pointer tracking, and featuring a tracking algorithm plugin architecture. </p>
<p> Your kernel must be configured with uinput support (INPUT_UINPUT, or Device Drivers/Input Device Support/Miscellaneous Drivers/User Level Driver Support under menuconfig). Compile into the kernel or as a module. See <a rel="nofollow" href="http://gentoo-wiki.com/HOWTO_Compile_a_Kernel_Manually">http://gentoo-wiki.com/HOWTO_Compile_a_Kernel_Manually</a> for information on kernel compilation. By default, some (most? all?) udev configurations set up a uinput device file readable only by root. Using wminput as a user other than root requires configuration udev to change the permissions on uinput. Place the following line in a file in /etc/udev/rules.d (see the documentation for your distro for the recommended file for local rules) to allow anyone on the system to use uinput: </p>
<p> KERNEL==&quot;uinput&quot;, MODE=&quot;0666&quot; </p>
<p> A more secure method uses the following line to allow anyone in &lt;group&gt; to use wminput, and adds only the desired users to &lt;group&gt;: </p>
<p> KERNEL==&quot;uinput&quot;, GROUP=&quot;&lt;group&gt;&quot; </p>
<p> A uinput group can be created specifically for this purpose, or another existing group such as wheel can be used. </p>
<p> See usr/share/doc/wminput/wminput.conf.sample for an example wminput configuration file. Copy this file to ~/.CWiid/wminput.conf and change as desired. </p>
<p> Getting X to recognize non-standard key symbols, and mapping actions to those symbols, is not automatic. An excellent tutorial at <a rel="nofollow" href="http://gentoo-wiki.com/HOWTO_Use_Multimedia_Keys">http://gentoo-wiki.com/HOWTO_Use_Multimedia_Keys</a> can help you set this up. An overview of the process (see the HOWTO for more information):<br />
 1.Edit ~/.CWiid/wminput.conf<br />
 2.Use xev, wminput, and your wiimote to find out if the key symbols are already mapped, and find the key codes if they are not.<br />
 3.If the codes are not mapped to the appropriate symbols, edit ~/.Xmodmap, and use xmodmap to map them. (A copy of my ~/.Xmodmap is included in CWiid/doc)<br />
 4.Use xbindkeys or a window manager-specific utility to map the key symbols to specific actions. </p>
<p> wminput tracking plugins are, by default, installed to /usr/lib/CWiid/plugins. Plugins may also be placed in ~/.CWiid/plugins, and plugins placed here will take precedence. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> Show summary of options.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Output version information and exit.</p>
<dt><code>-c, &#8211;config [file]</code></p>
<dd> Choose config file to use.</p>
<dt><code>-d, &#8211;daemon</code></p>
<dd> Implies -q, -r, and -w.</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> Reduce output to errors</p>
<dt><code>-r, &#8211;reconnect [wait]</code></p>
<dd> Automatically try reconnect after wiimote disconnect.</p>
<dt><code>-w, &#8211;wait</code></p>
<dd> Wait indefinitely for wiimote to connect.</p>
<dt><code>bdaddr</code></p>
<dd> Specify the wiimote bluetooth address. The bluetooth device address (bdaddr) of the wiimote can be specified on the command-line, or through the WIIMOTE_BDADDR environment variable, in the that order of precedence. If neither is given, the first wiimote found by hci_inquiry will be used. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wmgui/">wmgui</a></code>(1), </p>
<h2>AUTHOR</h2>
<p> wminput was written by L. Donnie Smith &lt;donnie.smith [at] gatech.edu&gt; </p>
<p> This manual page was written by Romain Beauxis &lt;toots [at] rastageeks.org&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
