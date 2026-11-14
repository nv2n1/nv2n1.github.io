---
title: "nvclock(1)"
name: "nvclock"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvclock/"
description: "nvclock – Overclock your nVidia graphics adapter."
---

<h2>NAME</h2>
<p> nvclock &#8211; Overclock your nVidia graphics adapter.</p>
<h2>SYNOPSIS</h2>
<p> <code>nvclock</code> <i>[options]</i></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>nvclock</code> command. NVClock is a small program for tweaking nVidia videocards on FreeBSD, Linux and Windows. Originally it was only meant for overclocking but these days it can do much more. For instance it contains hardware monitoring support using which you can view the temperatures and fanspeeds on cards that support it. Further it allows tweaking of OpenGL settings using the NV-CONTROL extension supported by the nVidia Linux/FreeBSD drivers.</p>
<h2>OPTIONS</h2>
<p> The program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options are included below.</p>
<dl>
<dt><code>&#8211;b, &#8211;backend </code><i>backend</i></p>
<dd> By default NVClock uses its so called &#8216;low-level&#8217; backend for reading and adjusting the clockspeeds of cards. Since NVidia driver 1.0-7667 the drivers also provide an overclocking mechanism called &#8216;Coolbits&#8217;. It is only supported on desktop versions of the GeforceFX/6/7. The main advantages it has over the low-level backend is that it allows you to set the clocks to use in 2D and 3D programs. The problem is that various modern GeforceFX/6/7/8 cards run at different clockspeeds depending if you are running a 3D application or not. </p>
<p> Possible values for backend are: coolbits, coolbits2d, coolbits3d and lowlevel. The default option on GeforceFX/6/7 cards is coolbits which sets the same clocks for 2D/3D, further coolbits2d and coolbits3d set respectively the 2D and 3D clocks and finally lowlevel lets you use the lowlevel backend.</p>
<dt><code>-c, &#8211;card </code><i>number</i></p>
<dd> Most systems only contain only one videocard. On systems with multiple cards, this option can be used to select the card to overclock.</p>
<dt><code>-d, &#8211;debug</code></p>
<dd> Enable/Disable overclocking related debug info. This information shows the data stored in the PLLs during various operations.</p>
<dt><code>-D, &#8211;Debug</code></p>
<dd> Print a long list of GPU registers containing their current value. All this info is very usefull for debugging.</p>
<dt><code>-f, &#8211;force</code></p>
<dd> Force support for a card that is currently disabled. Cards can be disabled by default if the code for them is experimental or in case a Laptop is being used. Laptops are disabled for safety reasons as overclocking on them is more dangerous. In case you know what you are doing you can use this option to enable downclocking of your GPU as a way to save power.</p>
<dt><code>-F, &#8211;fanspeed </code><i>speed</i></p>
<dd> Using this option you can adjust the duty cycle of the fanspeed. The value you can enter can be a delta like +10 or -10 which increases/decreases the fanspeed with 10%. Further the value can be a number like 20 which would set the fanspeed to 20%. Further if your sensor supports automatic (temperature controlled) fanspeed adjustments you can also use the value &#8216;auto&#8217; to switch back to automatic control. Note that in all cases the (final) fanspeed should lie between 10% and 100%. A low duty cycle correspons to a low fanspeed. </p>
<p> Note that the duty cycle is NOT the fanspeed. The duty cycle controls the percentage of time in a fixed time interval in which the fan is &#8216;on&#8217;. By choosing a higher value the fan is enabled a larger part of the time which results in a higher fanspeed. Changing the duty cycle from 20% to 40% doesn&#8217;t double the noise or fanspeed.</p>
<dt><code>-i, &#8211;info</code></p>
<dd> Print detailed card info</p>
<dt><code>-m, &#8211;memclk </code><i>speed</i></p>
<dd> Memory speed in MHz</p>
<dt><code>-n, &#8211;nvclk </code><i>speed</i></p>
<dd> Core speed in MHz</p>
<dt><code>-P, &#8211;Punit </code><i>mask</i></p>
<dd> The Geforce6/7 are designed in such a way that one single GPU can be used for creating different types of boards. For instance they produce a NV40 (6800-class) GPU and when the GPU is functioning properly they turn it into a 6800GT/Ultra or when something is damaged or when it can&#8217;t reach high clocks they call it a 6800NU/LE. The same is the case for NV43 based 6200/6600 cards. A 6800LE card ships with 8 disabled pixel units and 2 disabled vertex units. On various cards it is possible to re-enable those units and if it works correctly it can greatly improve 3D performance. The problem is that some units can be broken which results in artifacts or instability. Further not all GPU models can be unlocked either because Nvidia protected the GPUs against modding or because there are no extra units to enable. </p>
<p> Using this option you can enable extra pixel units. First check using the -i switch which pixel units are masked. If none are masked it means that none can be unlocked. For an explanation I will take a 6800LE as an example which by default has 8 of its 16 pixel units disabled. The -i option showed the mask &#8216;1100&#8217; which means that the first and second block of pixel units are disabled. One block of pixel unit contains 4 pipelines in case of most boards with the exception of NV44/NV46 which use 2 pipelines for each pixel unit. To enable the first and second pipeline use -P 1111 (binary) or i you prefer hex 0xf. NVClock will then try to unlock the pipelines note that even when there are masked pipelines some can be locked in hardware so that they can&#8217;t be enabled.</p>
<dt><code>-r, &#8211;reset</code></p>
<dd> Restore the original clockspeeds</p>
<dt><code>-s, &#8211;speeds</code></p>
<dd> Print current clockspeeds in MHz</p>
<dt><code>-S, &#8211;smartdimmer</code></p>
<dd> For use on laptops Nvidia added functionality called smartdimmer which can be used to adjust the brightness of the backlight. At the moment the feature is limited to Geforce6200Go cards but if needed more cards can be added if they really provide Smartdimmer support. To use this option you can select a value between 15% and 100% and the brightness will be set to that level or you can use a delta like +10 / -10 which should decrease the brightness with +10% / -10%.</p>
<dt><code>-V, &#8211;Vunit </code><i>mask</i></p>
<dd> This option can be used to enable disabled vertex pipelines which can appear on Geforce6/7 cards. For an introduction to pipeline modding check the -P option first. The syntax and working option is the same as the pixel unit one with the difference that one bit corresponds to 1 vertex pipeline instead of multiple. Again check -i to see which vertex units are locked. On a 6800LE you might see &#8216;001111&#8217; which means that the fifth and sixth unit are locked. To enable all units use -V 111111 (binary) or 0x3f (hex). Note that it isn&#8217;t certain that a unit can be enabled as on some cards units are locked.</p>
<dt>Below is a list with Display / OpenGL related options</p>
<dd>
<dt><code>-l, &#8211;list </code></p>
<dd> List OpenGL / Display options supported by your chipset/driver</p>
<dt><code>-q, &#8211;query </code><i>option</i></p>
<dd> Query current setting for one of the options listed under OpenGL / Display options.</p>
<dt><code>-a, &#8211;assign </code><i>option / option[display]=value</i></p>
<dd> Set a value for a supported option. </p>
<p> For OpenGL options like fsaa the following syntax is enough: nvclock -a option=value<br />
&nbsp;<wbr> Display specific options like Digital Vibrance sometimes need the display name: nvclock -a vibrance[crt-0]=value.</p>
<dt><code>-x, &#8211;xdisplay </code></p>
<dd> Choose another X display</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of options.</dl>
<h2>AUTHOR</h2>
<p> This manual page was originally written by Wouter de Vries &lt;sax [at] debian.org&gt;, for the Debian GNU/Linux system. Later on it got an update by Kel Modderman &lt;kelrin [at] tpg.com.au&gt; and at last it got rewritten for inclusion in NVClock 0.8 by Roderick Colenbrander &lt;thunderbird [at] linuxhardware.org&gt; </p>
<h2>Index</h2>
