---
title: "fpit(4)"
name: "fpit"
section: "4"
letter: "f"
url: "/docs/linux/man/4-fpit/"
description: "fpit – Fujitsu Stylistic input driver"
---

<p>fpit &#8211; Fujitsu Stylistic input driver</p>
<h2>Synopsis</h2>
<pre><code>Section N'34'InputDeviceN'34'</code>
<code> Identifier N'34'</code><i>idevname</i><code>N'34'</code>
<code> Driver N'34'fpitN'34'</code>
<code> Option N'34'DeviceN'34' N'34'</code><i>devpath</i><code>N'34'</code>
&nbsp;<wbr>&nbsp;<wbr>...
<code>EndSection</code></pre>
<h2>Description</h2>
<p><code>fpit </code> is an Xorg input driver for Fujitsu Stylistic Tablet PCs. </p>
<p> The <code>fpit</code> driver functions as a pointer input device, and may be used as the X server&#8217;s core pointer.</p>
<h2>Supported Hardware</h2>
<p>This driver supports the touchscreen of the Stylistic LT and (with special options) of the Stylistic 500, 1000, 1200, 2300, and 3400. Modern FinePoint MP800 devices will also work with this driver. </p>
<p> Under Linux the Fujitsu&#8217;s serial port is not, by default, detected. Therefore the port must be configured manually as described in the accompanying readme.txt file. </p>
<p> For example, add the following to your startup scripts for Stylistic xx00 devices: </p>
<dl>
<dt><code>setserial /dev/ttyS3 autoconfig</code></p>
<dd>
<dt><code>setserial /dev/ttyS3 IRQ 15 baud_base 115200 port 0xfce8</code></p>
<dd></dl>
<p> This driver now supports Stylistic 3400 (and possibly other passive-pen systems) with a special <i>&quot;Passive&quot;</i> paramter. Try this serial configuration for the 3400: </p>
<dl>
<dt><code>setserial /dev/ttyS3 autoconfig</code></p>
<dd>
<dt><code>setserial /dev/ttyS3 uart 16450 irq 5 port 0xfd68</code></p>
<dd></dl>
<h2>Configuration Details</h2>
<p>Please refer to <a href="//www.systutorials.com/docs/linux/man/5x-xorg.conf/">xorg.conf</a>(5x) for general configuration details and for options that can be used with all input drivers. This section only covers configuration details specific to this driver. </p>
<p> The device supports the following options:</p>
<dl>
<dd>
<dl>
<dt><code>Option </code><i>MaximumXPosition</i> <i>number</i></p>
<dd>Sets the maximum X position, use this to calibrate your touchscreen&#8217;s right hand edge.</p>
<dt><code>Option </code><i>MinimumXPosition</i> <i>number</i></p>
<dd>Sets the minimum X position, use this to calibrate your touchscreen&#8217;s left hand edge.</p>
<dt><code>Option </code><i>MaximumYPosition</i> <i>number</i></p>
<dd>
<dt><code>Option </code><i>MinimumYPosition</i> <i>number</i></p>
<dd>Same as for X axis, but for Y axis.</p>
<dt><code>Option </code><i>InvertX</i></p>
<dd>
<dt><code>Option </code><i>InvertY</i></p>
<dd>Invert the specified axis.</p>
<dt><code>Option </code><i>SwapXY</i></p>
<dd>Swap the X and Y axis (after inversions).</p>
<dt><code>Option </code><i>Rotate</i> <i>CW</i></p>
<dd><code>Option </code><i>Rotate</i> <i>CWW</i> Manipulate the invert and swap options to match screen rotations. (Will behave strangely if combined with invert or swap options.) New users should consider the <i>&quot;TrackRandR&quot;</i> option instead.</p>
<dt><code>Option </code><i>DeviceName</i> <i>name</i></p>
<dd><code>Option </code><i>DeviceName</i> <i>name</i> sets the name of the X device.</p>
<dt><code>Option </code><i>AlwaysCore</i> <i>on</i></p>
<dd>enables the sharing of the core pointer. When this feature is enabled, the device will take control of the core pointer (and thus will emit core events) and at the same time will be able, when asked so, to report extended events. You can use the last available integer feedback to control this feature. When the value of the feedback is zero, the feature is disabled. The feature is enabled for any other value.</p>
<dt><code>Option </code><i>DebugLevel</i> <i>number </i></p>
<dd>sets the level of debugging info reported.</p>
<dt><code>Option </code><i>BaudRate</i> <i>38400</i>, <i>19200</i> (default) or <i>9600</i></p>
<dd>changes the serial link speed.</p>
<dt><code>Option </code><i>Passive</i></p>
<dd>decodes the passive pen. <code>Option </code><i>TrackRandR</i> automatically keeps the cursor synchronized with the pen&#8217;s position, even when the screen is resized or rotated. (Recommended for tablet PC&#8217;s.)</dl>
</dl>
<p> Example, for Stylistic LT setup is: </p>
<pre><code>Section N'34'InputDeviceN'34'</code>
<code> Identifier N'34'</code><i>mouse0</i><code>N'34'</code>
<code> Driver N'34'fpitN'34'</code>
<code> Option N'34'DeviceN'34' N'34'/dev/ttyS3</code><i>N'34'</i>
<code> # Option N'34'TrackRandRN'34'</code>
<code>EndSection</code></pre>
<p>And for other Stylistic devices try: </p>
<pre><code>Section N'34'InputDeviceN'34'</code>
<code> Identifier N'34'</code><i>mouse0</i><code>N'34'</code>
<code> Driver N'34'fpitN'34'</code>
<code> Option N'34'DeviceN'34' N'34'/dev/ttyS3</code><i>N'34'</i>
<code> Option N'34'BaudRateN'34' N'34'19200</code><i>N'34'</i>
<code> Option N'34'MaximumXPositionN'34' N'34'6250</code><i>N'34'</i>
<code> Option N'34'MaximumYPositionN'34' N'34'4950</code><i>N'34'</i>
<code> Option N'34'MinimumXPositionN'34' N'34'130</code><i>N'34'</i>
<code> Option N'34'MinimumYPositionN'34' N'34'0</code><i>N'34'</i>
<code> Option N'34'InvertYN'34'</code>
<code> # Option N'34'TrackRandRN'34'</code>
<code>EndSection</code></pre>
<p>For Stylistic 3400: </p>
<pre><code>Section N'34'InputDeviceN'34'</code>
<code> Identifier N'34'</code><i>mouse0</i><code>N'34'</code>
<code> Driver N'34'fpitN'34'</code>
<code> Option N'34'DeviceN'34' N'34'/dev/ttyS3</code><i>N'34'</i>
<code> Option N'34'BaudRateN'34' N'34'9600</code><i>N'34'</i>
<code> Option N'34'MaximumXPositionN'34' N'34'4070</code><i>N'34'</i>
<code> Option N'34'MaximumYPositionN'34' N'34'4020</code><i>N'34'</i>
<code> Option N'34'MinimumXPositionN'34' N'34'0</code><i>N'34'</i>
<code> Option N'34'MinimumYPositionN'34' N'34'0</code><i>N'34'</i>
<code> Option N'34'PassiveN'34'</code>
<code> Option N'34'SendCoreEventsN'34'</code>
<code> # Option N'34'TrackRandRN'34'</code>
<code>EndSection</code></pre>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7).</p>
<h2>Authors</h2>
<p>Original FPIT port: Rob Tsuk &lt;rob [at] tsuk.com&gt; and John Apfelbaum &lt;johnapf [at] linuxslate.com&gt; </p>
<p> X4 Port: Richard Miller-Smith &lt;richard.miller-smith [at] philips.com&gt;, based on Elographics code from: Patrick Lecoanet </p>
<p> X4.2 Cleanup: Alan Cox</p>
