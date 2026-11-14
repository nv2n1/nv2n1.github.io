---
title: "setupcon(1)"
name: "setupcon"
section: "1"
letter: "s"
url: "/docs/linux/man/1-setupcon/"
description: "setupcon – sets up the font and the keyboard on the console"
---

<h2 class="name">NAME</h2>
<p> setupcon &#8211; sets up the font and the keyboard on the console</p>
<h2>SYNOPSIS</h2>
<p> <code>setupcon</code> [<i>OPTION</i>]&#8230;&nbsp;[<i>VARIANT</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>setupcon</code> is a program for fast and easy setup of the font and the keyboard on the console. Most of the time you invoke <code>setupcon</code> without arguments. The keyboard configuration is specified in <i>~/.keyboard</i> or <i>/etc/default/keyboard</i>. The font configuration is specified in <i>~/.console-setup</i> or <i>/etc/default/console-setup</i>. Consult <code><a href="/docs/linux/man/5-keyboard/">keyboard</a></code>(5) and <code><a href="/docs/linux/man/5-console-setup/">console-setup</a></code>(5) for instructions how to configure these two files. </p>
<p> If you have to switch often between different encodings, keyboards or languages, you can prepare several alternative configuration files for <code>setupcon</code>. Suppose that most of the time you will use Greek language with Greek keyboard layout, but sometimes you need to type in German with German keyboard layout. In this situation you should customize the main configuration files (<i>keyboard</i> and <i>console-setup</i>) for Greek. Also, create alternative configuration files for German named <i>keyboard.german</i> and <i>console-setup.german</i>. Then in order to configure the console for Greek you will simply run the command with no arguments: <i>setupcon</i> and in order to configure the console for German you will use <i>setupcon german</i>. </p>
<h2>OPTIONS</h2>
<dl>
<dt><i>VARIANT</i></p>
<dd> Specifies which configuration file to use. With no variant, the configuration files of <code>setupcon</code> are named <i>console-setup</i> and <i>keyboard</i>. On the other hand, if you use e.g. <i>chukchi</i> as <i>VARIANT</i> then the configuration files are <i>console-setup.chukchi</i> and <i>keyboard.chukchi</i>. In this way you can have easy access to several different configurations &#8211; for example one for the Chukchi language and another for the default configuration. </p>
<dt><code>-v</code>,&nbsp;<code>&#8211;verbose</code></p>
<dd> Be more verbose. Use this option if something goes wrong or while experimenting with the configuration files. </p>
<dt><code>-k</code>,&nbsp;<code>&#8211;keyboard-only</code></p>
<dd> Setup the keyboard only, do not setup the font or the terminal. On Linux it is enough to do this configuration only once. </p>
<dt><code>-f</code>,&nbsp;<code>&#8211;font-only</code></p>
<dd> Setup the font only, do not setup the keyboard or the terminal. On Linux this configuration should be repeated each time a new console driver is activated (for example when the frame buffer becomes active). </p>
<dt><code>-t</code>,&nbsp;<code>&#8211;terminal-only</code></p>
<dd> Setup the terminal only, do not setup the keyboard or the font. </p>
<dt><code>&#8211;current-tty</code></p>
<dd> Setup the only the current virtual terminal. </p>
<dt><code>&#8211;force</code></p>
<dd> Do not check whether we are on the console. Notice that you can be forced to hard-reboot your computer if you run <code>setupcon</code> with this option and the screen is controlled by a X server. </p>
<dt><code>&#8211;save</code></p>
<dd> This option can be useful if you want to use <code>setupcon</code> early in the boot process while <i>/usr</i> is not yet mounted and the required data are not available. This option will make <code>setupcon</code> copy the required files in <i>/etc/console-setup/</i> in order to make them available before <i>/usr</i> is mounted. If you use <code>setupcon</code> early in the boot process, then you should run it with this option after every change of the console configuration. </p>
<dt><code>&#8211;save-only</code></p>
<dd> The same as <i>&#8211;save</i>, but does not setup anything. This option can be useful if you want to save the required files while the screen is controlled by a X server. </p>
<dt><code>&#8211;save-keyboard&nbsp;</code><i>FILE</i></p>
<dd> For use by initrd builders. Do not configure anything. Save an usable keyboard layout in <i>FILE</i>. </p>
<dt><code>&#8211;setup-dir&nbsp;</code><i>DIR</i></p>
<dd> For use by initrd builders. Do not configure anything. Arrange in the directory <i>DIR</i> everything necessary in order to configure the console. The file <i>DIR/morefiles</i> lists all binaries the initrd builder has to install in the initrd image. All other files in <i>DIR</i> have to be copied unchanged in the initrd. In order to configure the console one has to run the script <i>DIR/bin/setupcon</i>. </p>
<dt><code>-h</code>,&nbsp;<code>&#8211;help</code></p>
<dd> Display usage information. </p>
</dl>
<h2>FILES</h2>
<p> <i>~/.console-setup</i><br />
 <i>~/.keyboard</i><br />
 <i>/etc/default/console-setup</i><br />
 <i>/etc/default/keyboard</i><br />
 <i>/etc/default/console-setup.VARIANT</i><br />
 <i>/etc/default/keyboard.VARIANT</i><br />
 <i>/etc/console-setup/</i> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-keyboard/">keyboard</a></code>(5), <code><a href="/docs/linux/man/5-console-setup/">console-setup</a></code>(5) </p>
<h2>Index</h2>
