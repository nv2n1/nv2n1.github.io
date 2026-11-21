---

title: "inputattach(1)"
name: "inputattach"
section: "1"
letter: "i"
url: "/docs/linux/man/1-inputattach/"
description: "inputattach – attach a serial line to an input-layer device"
---

<p> inputattach &#8211; attach a serial line to an input-layer device </p>
<h2>SYNOPSIS</h2>
<p> <code>inputattach</code> [<code>&#8211;daemon</code>] [<code>&#8211;always</code>] [<code>&#8211;noinit</code>] [<code>&#8211;baud</code> <i>baud</i>&gt;] &lt;<i>mode</i>&gt; &lt;<i>device</i>&gt;</p>
<h2>DESCRIPTION</h2>
<p> <code>inputattach</code> attaches a serial line to an input-layer device via a line discipline. </p>
<p> At least one of the available modes must be specified on the command line; if the modes can be probed, up to four can be specified, and they will be tried in sequence until one matches the device.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;daemon</code></dt>
<dd> Forks into the background.</dd>
<dt><code>&#8211;always</code></dt>
<dd> Ignore initialization failures when attaching the device.</dd>
<dt><code>&#8211;noinit</code></dt>
<dd> Skip device initialization.</dd>
<dt><code>&#8211;baud</code></dt>
<dd> Specify the baud rate to use. (This is only necessary if the default rate is incorrect.)</dd></dl>
<h3>Modes</h3>
<dl>
<dt><code>-bare</code>, <code>&#8211;microsoft</code></dt>
<dd> 2-button Microsoft mouse.</dd>
<dt><code>-dump</code>, <code>&#8211;dump</code></dt>
<dd> Just enable device.</dd>
<dt><code>-eeti</code>, <code>&#8211;eetiegalax</code></dt>
<dd> EETI eGalaxTouch.</dd>
<dt><code>-elo</code>, <code>&#8211;elotouch</code></dt>
<dd> ELO touchscreen, 10-byte mode.</dd>
<dt><code>-elo3b</code>, <code>&#8211;elo261-280</code></dt>
<dd> ELO Touchscreen, 3-byte mode.</dd>
<dt><code>-elo4b</code>, <code>&#8211;elo271-140</code></dt>
<dd> ELO touchscreen, 4-byte mode.</dd>
<dt><code>-elo6b</code>, <code>&#8211;elo4002</code></dt>
<dd> ELO touchscreen, 6-byte mode.</dd>
<dt><code>-ep</code>, <code>&#8211;easypen</code></dt>
<dd> Genius EasyPen 3&#215;4 tablet.</dd>
<dt><code>-fjt</code>, <code>&#8211;fujitsu</code></dt>
<dd> Fujitsu serial touchscreen.</dd>
<dt><code>-fsia6b</code>, <code>&#8211;fsia6b</code></dt>
<dd> FS-iA6B RC Receiver.</dd>
<dt><code>-ham</code>, <code>&#8211;hampshire</code></dt>
<dd> Hampshire touchscreen.</dd>
<dt><code>-ifor</code>, <code>&#8211;iforce</code></dt>
<dd> I-Force joystick or wheel.</dd>
<dt><code>-ipaq</code>, <code>&#8211;h3600ts</code></dt>
<dd> Ipaq h3600 touchscreen.</dd>
<dt><code>-ipaqkbd</code>, <code>&#8211;stowawaykbd</code></dt>
<dd> Stowaway keyboard.</dd>
<dt><code>-lk</code>, <code>&#8211;lkkbd</code></dt>
<dd> DEC LK201 / LK401 keyboards.</dd>
<dt><code>-mag</code>, <code>&#8211;magellan</code></dt>
<dd> Magellan / SpaceMouse.</dd>
<dt><code>-mman</code>, <code>&#8211;mouseman</code></dt>
<dd> 3-button Logitech / Genius mouse.</dd>
<dt><code>-mman4</code>, <code>&#8211;mouseman4</code></dt>
<dd> 4-button Logitech / Genius mouse.</dd>
<dt><code>-mmw</code>, <code>&#8211;mmwheel</code></dt>
<dd> Logitech mouse with 4-5 buttons or a wheel.</dd>
<dt><code>-ms</code>, <code>&#8211;mshack</code></dt>
<dd> 3-button mouse in Microsoft mode.</dd>
<dt><code>-ms3</code>, <code>&#8211;intellimouse</code></dt>
<dd> Microsoft IntelliMouse.</dd>
<dt><code>-msc</code>, <code>&#8211;mousesystems</code></dt>
<dd> 3-button Mouse Systems mouse.</dd>
<dt><code>-mtouch</code>, <code>&#8211;mtouch</code></dt>
<dd> MicroTouch (3M) touchscreen.</dd>
<dt><code>-newt</code>, <code>&#8211;newtonkbd</code></dt>
<dd> Newton keyboard.</dd>
<dt><code>-orb</code>, <code>&#8211;spaceorb</code></dt>
<dd> SpaceOrb 360 / SpaceBall Avenger.</dd>
<dt><code>-pm3k</code>, <code>&#8211;penmount3000</code></dt>
<dd> PenMount 3000 touchscreen.</dd>
<dt><code>-pm6k</code>, <code>&#8211;penmount6000</code></dt>
<dd> PenMount 6000 touchscreen.</dd>
<dt><code>-pm9k</code>, <code>&#8211;penmount9000</code></dt>
<dd> PenMount 9000 touchscreen.</dd>
<dt><code>-pmm1</code>, <code>&#8211;penmount6250</code></dt>
<dd> PenMount 6250 touchscreen.</dd>
<dt><code>-ps2m</code>, <code>&#8211;ps2mult</code></dt>
<dd> PS/2 serial multiplexer.</dd>
<dt><code>-ps2ser</code>, <code>&#8211;ps2serkbd</code></dt>
<dd> PS/2 via serial keyboard.</dd>
<dt><code>-pulse8-cec</code>, <code>&#8211;pulse8-cec</code></dt>
<dd> Pulse Eight HDMI CEC dongle.</dd>
<dt><code>-rainshadow-cec</code>, <code>&#8211;rainshadow-cec</code></dt>
<dd> RainShadow Tech HDMI CEC dongle.</dd>
<dt><code>-sbl</code>, <code>&#8211;spaceball</code></dt>
<dd> SpaceBall 2003 / 3003 / 4000 FLX.</dd>
<dt><code>-skb</code>, <code>&#8211;sunkbd</code></dt>
<dd> Sun Type 4 and Type 5 keyboards.</dd>
<dt><code>-sting</code>, <code>&#8211;stinger</code></dt>
<dd> Gravis Stinger.</dd>
<dt><code>-sun</code>, <code>&#8211;sunmouse</code></dt>
<dd> 3-button Sun mouse.</dd>
<dt><code>-t213</code>, <code>&#8211;touchit213</code></dt>
<dd> Sahara Touch-iT213 Tablet PC.</dd>
<dt><code>-taos</code>, <code>&#8211;taos-evm</code></dt>
<dd> TAOS evaluation module.</dd>
<dt><code>-tr</code>, <code>&#8211;touchright</code></dt>
<dd> Touchright serial touchscreen.</dd>
<dt><code>-tsc</code>, <code>&#8211;tsc</code></dt>
<dd> TSC-10/25/40 serial touchscreen.</dd>
<dt><code>-tw</code>, <code>&#8211;touchwin</code></dt>
<dd> Touchwindow serial touchscreen.</dd>
<dt><code>-twid</code>, <code>&#8211;twiddler</code></dt>
<dd> Handykey Twiddler chording keyboard.</dd>
<dt><code>-twidjoy</code>, <code>&#8211;twiddler-joy</code></dt>
<dd> Handykey Twiddler used as a joystick.</dd>
<dt><code>-vs</code>, <code>&#8211;vsxxx-aa</code></dt>
<dd> DEC VSXXX-AA / VSXXX-GA mouse and VSXXX-A tablet.</dd>
<dt><code>-w8001</code>, <code>&#8211;w8001</code></dt>
<dd> Wacom W8001 pen and/or touch devices. The default baud rate, 38400bps, allows for touch-only or pen and touch devices; for pen-only devices, &quot;<code>&#8211;baud 19200</code>&quot; must be specified.</dd>
<dt><code>-wacom_iv</code>, <code>&#8211;wacom_iv</code></dt>
<dd> Wacom protocol IV tablet.</dd>
<dt><code>-war</code>, <code>&#8211;warrior</code></dt>
<dd> WingMan Warrior.</dd>
<dt><code>-zhen</code>, <code>&#8211;zhen-hua</code></dt>
<dd> Zhen Hua 5-byte protocol.</dd></dl>
<h2>AUTHORS</h2>
<p> <code>inputattach</code> was written by Vojtech Pavlik and Arndt Schoenewald, and improved by many others; see the linuxconsole tools documentation for details. </p>
<p> This manual page was written by Stephen Kitt &lt;steve [at] sk2.org&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
