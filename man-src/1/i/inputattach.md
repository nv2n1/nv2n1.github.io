---
title: "inputattach(1)"
name: "inputattach"
section: "1"
letter: "i"
url: "/docs/linux/man/1-inputattach/"
description: "inputattach – attach a serial line to an input-layer device"
---

<h2 class="name">NAME</h2>
<p> inputattach &#8211; attach a serial line to an input-layer device </p>
<h2>SYNOPSIS</h2>
<p> <code>inputattach</code> [<code>&#8211;daemon</code>] [<code>&#8211;always</code>] [<code>&#8211;noinit</code>] [<code>&#8211;baud</code> <i>baud</i>&gt;] &lt;<i>mode</i>&gt; &lt;<i>device</i>&gt;</p>
<h2>DESCRIPTION</h2>
<p> <code>inputattach</code> attaches a serial line to an input-layer device via a line discipline. </p>
<p> At least one of the available modes must be specified on the command line; if the modes can be probed, up to four can be specified, and they will be tried in sequence until one matches the device.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;daemon</code></p>
<dd> Forks into the background.</p>
<dt><code>&#8211;always</code></p>
<dd> Ignore initialization failures when attaching the device.</p>
<dt><code>&#8211;noinit</code></p>
<dd> Skip device initialization.</p>
<dt><code>&#8211;baud</code></p>
<dd> Specify the baud rate to use. (This is only necessary if the default rate is incorrect.)</dl>
<h3>Modes</h3>
<dl>
<dt><code>-bare</code>, <code>&#8211;microsoft</code></p>
<dd> 2-button Microsoft mouse.</p>
<dt><code>-dump</code>, <code>&#8211;dump</code></p>
<dd> Just enable device.</p>
<dt><code>-eeti</code>, <code>&#8211;eetiegalax</code></p>
<dd> EETI eGalaxTouch.</p>
<dt><code>-elo</code>, <code>&#8211;elotouch</code></p>
<dd> ELO touchscreen, 10-byte mode.</p>
<dt><code>-elo3b</code>, <code>&#8211;elo261-280</code></p>
<dd> ELO Touchscreen, 3-byte mode.</p>
<dt><code>-elo4b</code>, <code>&#8211;elo271-140</code></p>
<dd> ELO touchscreen, 4-byte mode.</p>
<dt><code>-elo6b</code>, <code>&#8211;elo4002</code></p>
<dd> ELO touchscreen, 6-byte mode.</p>
<dt><code>-ep</code>, <code>&#8211;easypen</code></p>
<dd> Genius EasyPen 3&#215;4 tablet.</p>
<dt><code>-fjt</code>, <code>&#8211;fujitsu</code></p>
<dd> Fujitsu serial touchscreen.</p>
<dt><code>-fsia6b</code>, <code>&#8211;fsia6b</code></p>
<dd> FS-iA6B RC Receiver.</p>
<dt><code>-ham</code>, <code>&#8211;hampshire</code></p>
<dd> Hampshire touchscreen.</p>
<dt><code>-ifor</code>, <code>&#8211;iforce</code></p>
<dd> I-Force joystick or wheel.</p>
<dt><code>-ipaq</code>, <code>&#8211;h3600ts</code></p>
<dd> Ipaq h3600 touchscreen.</p>
<dt><code>-ipaqkbd</code>, <code>&#8211;stowawaykbd</code></p>
<dd> Stowaway keyboard.</p>
<dt><code>-lk</code>, <code>&#8211;lkkbd</code></p>
<dd> DEC LK201 / LK401 keyboards.</p>
<dt><code>-mag</code>, <code>&#8211;magellan</code></p>
<dd> Magellan / SpaceMouse.</p>
<dt><code>-mman</code>, <code>&#8211;mouseman</code></p>
<dd> 3-button Logitech / Genius mouse.</p>
<dt><code>-mman4</code>, <code>&#8211;mouseman4</code></p>
<dd> 4-button Logitech / Genius mouse.</p>
<dt><code>-mmw</code>, <code>&#8211;mmwheel</code></p>
<dd> Logitech mouse with 4-5 buttons or a wheel.</p>
<dt><code>-ms</code>, <code>&#8211;mshack</code></p>
<dd> 3-button mouse in Microsoft mode.</p>
<dt><code>-ms3</code>, <code>&#8211;intellimouse</code></p>
<dd> Microsoft IntelliMouse.</p>
<dt><code>-msc</code>, <code>&#8211;mousesystems</code></p>
<dd> 3-button Mouse Systems mouse.</p>
<dt><code>-mtouch</code>, <code>&#8211;mtouch</code></p>
<dd> MicroTouch (3M) touchscreen.</p>
<dt><code>-newt</code>, <code>&#8211;newtonkbd</code></p>
<dd> Newton keyboard.</p>
<dt><code>-orb</code>, <code>&#8211;spaceorb</code></p>
<dd> SpaceOrb 360 / SpaceBall Avenger.</p>
<dt><code>-pm3k</code>, <code>&#8211;penmount3000</code></p>
<dd> PenMount 3000 touchscreen.</p>
<dt><code>-pm6k</code>, <code>&#8211;penmount6000</code></p>
<dd> PenMount 6000 touchscreen.</p>
<dt><code>-pm9k</code>, <code>&#8211;penmount9000</code></p>
<dd> PenMount 9000 touchscreen.</p>
<dt><code>-pmm1</code>, <code>&#8211;penmount6250</code></p>
<dd> PenMount 6250 touchscreen.</p>
<dt><code>-ps2m</code>, <code>&#8211;ps2mult</code></p>
<dd> PS/2 serial multiplexer.</p>
<dt><code>-ps2ser</code>, <code>&#8211;ps2serkbd</code></p>
<dd> PS/2 via serial keyboard.</p>
<dt><code>-pulse8-cec</code>, <code>&#8211;pulse8-cec</code></p>
<dd> Pulse Eight HDMI CEC dongle.</p>
<dt><code>-rainshadow-cec</code>, <code>&#8211;rainshadow-cec</code></p>
<dd> RainShadow Tech HDMI CEC dongle.</p>
<dt><code>-sbl</code>, <code>&#8211;spaceball</code></p>
<dd> SpaceBall 2003 / 3003 / 4000 FLX.</p>
<dt><code>-skb</code>, <code>&#8211;sunkbd</code></p>
<dd> Sun Type 4 and Type 5 keyboards.</p>
<dt><code>-sting</code>, <code>&#8211;stinger</code></p>
<dd> Gravis Stinger.</p>
<dt><code>-sun</code>, <code>&#8211;sunmouse</code></p>
<dd> 3-button Sun mouse.</p>
<dt><code>-t213</code>, <code>&#8211;touchit213</code></p>
<dd> Sahara Touch-iT213 Tablet PC.</p>
<dt><code>-taos</code>, <code>&#8211;taos-evm</code></p>
<dd> TAOS evaluation module.</p>
<dt><code>-tr</code>, <code>&#8211;touchright</code></p>
<dd> Touchright serial touchscreen.</p>
<dt><code>-tsc</code>, <code>&#8211;tsc</code></p>
<dd> TSC-10/25/40 serial touchscreen.</p>
<dt><code>-tw</code>, <code>&#8211;touchwin</code></p>
<dd> Touchwindow serial touchscreen.</p>
<dt><code>-twid</code>, <code>&#8211;twiddler</code></p>
<dd> Handykey Twiddler chording keyboard.</p>
<dt><code>-twidjoy</code>, <code>&#8211;twiddler-joy</code></p>
<dd> Handykey Twiddler used as a joystick.</p>
<dt><code>-vs</code>, <code>&#8211;vsxxx-aa</code></p>
<dd> DEC VSXXX-AA / VSXXX-GA mouse and VSXXX-A tablet.</p>
<dt><code>-w8001</code>, <code>&#8211;w8001</code></p>
<dd> Wacom W8001 pen and/or touch devices. The default baud rate, 38400bps, allows for touch-only or pen and touch devices; for pen-only devices, &quot;<code>&#8211;baud 19200</code>&quot; must be specified.</p>
<dt><code>-wacom_iv</code>, <code>&#8211;wacom_iv</code></p>
<dd> Wacom protocol IV tablet.</p>
<dt><code>-war</code>, <code>&#8211;warrior</code></p>
<dd> WingMan Warrior.</p>
<dt><code>-zhen</code>, <code>&#8211;zhen-hua</code></p>
<dd> Zhen Hua 5-byte protocol.</dl>
<h2>AUTHORS</h2>
<p> <code>inputattach</code> was written by Vojtech Pavlik and Arndt Schoenewald, and improved by many others; see the linuxconsole tools documentation for details. </p>
<p> This manual page was written by Stephen Kitt &lt;steve [at] sk2.org&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
