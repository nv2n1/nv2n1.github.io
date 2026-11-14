---
title: "elographics(4)"
name: "elographics"
section: "4"
letter: "e"
url: "/docs/linux/man/4-elographics/"
description: "elographics – Elographics input driver"
---

<p>elographics &#8211; Elographics input driver</p>
<h2>Synopsis</h2>
<p><code>Section N&#8217;34&#8217;InputDeviceN&#8217;34&#8217;</code><br />
 <code> Identifier N&#8217;34&#8217;</code><i>idevname</i><code>N&#8217;34&#8217;</code><br />
 <code> Driver N&#8217;34&#8217;elographicsN&#8217;34&#8217;</code><br />
 <code> Option N&#8217;34&#8217;DeviceN&#8217;34&#8217; N&#8217;34&#8217;</code><i>devpath</i><code>N&#8217;34&#8217;</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&#8230;<br />
 <code>EndSection</code></p>
<h2>Description</h2>
<p><code>elographics </code> is an Xorg input driver for Elographics touchscreen devices. </p>
<p> The <code>elographics</code> driver functions as a pointer input device, and may be used as the X server&#8217;s core pointer.</p>
<h2>Supported Hardware</h2>
<p>E271-2210 and E271-2200 devices are supported. E281-2310 and compatible devices are supported with some features unavailable.</p>
<h2>Configuration Details</h2>
<p>Please refer to <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) for general configuration details and for options that can be used with all input drivers. This section only covers configuration details specific to this driver. </p>
<p> The following driver options are supported:</p>
<dl>
<dt><code>Option N&#8217;34&#8217;DeviceN&#8217;34&#8217; N&#8217;34&#8217;</code><i>string</i><code>N&#8217;34&#8217;</code></p>
<dd>The device that is attached to the touchscreen interface. Default is &quot;/dev/ttyS1&quot;.</p>
<dt><code>Option N&#8217;34&#8217;DeviceNameN&#8217;34&#8217; N&#8217;34&#8217;</code><i>string</i><code>N&#8217;34&#8217;</code></p>
<dd>Set the X11 device name for the touchscreen. Default is &quot;TOUCHSCREEN&quot;.</p>
<dt><code>Option N&#8217;34&#8217;MinXN&#8217;34&#8217; N&#8217;34&#8217;</code><i>integer</i><code>N&#8217;34&#8217;</code></p>
<dd>Set the minimum value for the touchscreen X axis. Default is 600.</p>
<dt><code>Option N&#8217;34&#8217;MaxXN&#8217;34&#8217; N&#8217;34&#8217;</code><i>integer</i><code>N&#8217;34&#8217;</code></p>
<dd>Set the maximum value for the touchscreen X axis. Default is 3000.</p>
<dt><code>Option N&#8217;34&#8217;MinYN&#8217;34&#8217; N&#8217;34&#8217;</code><i>integer</i><code>N&#8217;34&#8217;</code></p>
<dd>Set the minimum value for the touchscreen Y axis. Default is 600.</p>
<dt><code>Option N&#8217;34&#8217;MaxYN&#8217;34&#8217; N&#8217;34&#8217;</code><i>integer</i><code>N&#8217;34&#8217;</code></p>
<dd>Set the maximum value for the touchscreen Y axis. Default is 3000.</p>
<dt><code>Option N&#8217;34&#8217;ScreenNoN&#8217;34&#8217; N&#8217;34&#8217;</code><i>integer</i><code>N&#8217;34&#8217;</code></p>
<dd>The screen to attach to the touchscreen when running with multiple screens. Default is screen 0.</p>
<dt><code>Option N&#8217;34&#8217;PortraitModeN&#8217;34&#8217; N&#8217;34&#8217;</code><i>string</i><code>N&#8217;34&#8217;</code></p>
<dd>Set the X/Y axis orientation. The default is &quot;Landscape&quot; but you can rotate clockwise (&quot;Portrait&quot;) or counter-clockwise (&quot;PortraitCCW&quot;).</p>
<dt><code>Option N&#8217;34&#8217;SwapXYN&#8217;34&#8217; N&#8217;34&#8217;</code><i>boolean</i><code>N&#8217;34&#8217;</code></p>
<dd>Swap the X and Y axis on the display. Default is false.</p>
<dt><code>Option N&#8217;34&#8217;UntouchDelayN&#8217;34&#8217; N&#8217;34&#8217;</code><i>integer</i><code>N&#8217;34&#8217;</code></p>
<dd>The period that finger must be released for an untouch event to occur. Default: 5 (50ms).</p>
<dt><code>Option N&#8217;34&#8217;ReportDelayN&#8217;34&#8217; N&#8217;34&#8217;</code><i>integer</i><code>N&#8217;34&#8217;</code></p>
<dd>Delay between report packets. Default: 1 (10ms).</p>
<dt><code>Option N&#8217;34&#8217;ModelN&#8217;34&#8217; N&#8217;34&#8217;</code><i>string</i><code>N&#8217;34&#8217;</code></p>
<dd>The touchscreen model. Default: unset. Supported models: &quot;Sunit dSeries&quot;.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-xorgconfig/">xorgconfig</a>(1), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7).</p>
<h2>Authors</h2>
<p>Authors include:<br />
&nbsp;<wbr>Patrick Lecoanet </p>
<p> This manpage was written by Lee Maguire on behalf of the Debian Project.</p>
