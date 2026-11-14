---
title: "aiptek(4)"
name: "aiptek"
section: "4"
letter: "a"
url: "/docs/linux/man/4-aiptek/"
description: "aiptek – Aiptek USB Digital Tablet Input Driver for Linux"
---

<p>aiptek &#8211; Aiptek USB Digital Tablet Input Driver for Linux</p>
<h2>Synopsis</h2>
<pre><code>Section N'34'InputDeviceN'34'</code>
<code> Identifier N'34'</code><i>idevname</i><code>N'34'</code>
<code> Driver N'34'aiptekN'34'</code>
<code> Option N'34'DeviceN'34' N'34'</code><i>devpath</i><code>N'34'</code>
&nbsp;<wbr>&nbsp;<wbr>...
<code>EndSection</code></pre>
<h2>Description</h2>
<p><code>aiptek </code> is an Xorg input driver for Aiptek HyperPen USB-based tablet devices. This driver only supports the USB protocol, and only under Linux; for RS-232C-based HyperPens, please see the <i>&quot;hyperpen&quot;</i> driver. </p>
<p> The <code>aiptek</code> driver functions as a pointer input device, and may be used as the X server&#8217;s core pointer.</p>
<h2>Supported Hardware</h2>
<p>This driver supports the Aiptek HyperPen 4000U, 5000U, 6000U, 8000U and 12000U USB-based input tablet on some Linux platforms.</p>
<h2>Configuration Details</h2>
<p>Please refer to <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) for general configuration details and for options that can be used with all input drivers. This section only covers configuration details specific to this driver. </p>
<p> Multiple instances of the Aiptek devices can cohabit. It can be useful to define multiple devices with different active zones. Each device supports the following entries:</p>
<dl>
<dd>
<dl>
<dt><code>Option </code><i>Type</i> <i>stylus|eraser|cursor</i></p>
<dd>sets the type of tool the device represent. This option is mandatory.</p>
<dt><code>Option </code><i>Device</i> <i>path</i></p>
<dd>sets the path to the special file which represents serial line where the tablet is plugged. You have to specify it for each subsection with the same value if you want to have multiple devices with the same tablet. This option is mandatory.</p>
<dt><code>Option </code><i>USB</i> <i>on</i></p>
<dd>specifies that you are using the USB bus to communicate with your tablet. This setting is mandatory, as USB is the only protocol supported by this driver.</p>
<dt><code>Option </code><i>DeviceName</i> <i>name</i></p>
<dd>sets the name of the X device.</p>
<dt><code>Option </code><i>Mode</i> <i>Relative|Absolute</i></p>
<dd>sets the mode of the device.</p>
<dt><code>Option </code><i>HistorySize</i> <i>number</i></p>
<dd>sets the motion history size. By default the value is zero.</p>
<dt><code>Option </code><i>AlwaysCore</i> <i>on</i></p>
<dd>enables the sharing of the core pointer. When this feature is enabled, the device will take control of the core pointer (and thus will emit core events) and at the same time will be able, when asked so, to report extended events. You can use the last available integer feedback to control this feature. When the value of the feedback is zero, the feature is disabled. The feature is enabled for any other value.</p>
<dt><code>Option </code><i>XTop</i> <i>number</i></p>
<dd>First of three sets of parameters to set the active zone. This sets the X coordinate of the top corner of the active zone. <i>&quot;TopX&quot;</i> is a synonym.</p>
<dt><code>Option </code><i>YTop</i> <i>number</i></p>
<dd>First of three sets of parameters to set the active zone. This sets the Y coordinate of the top corner of the active zone. <i>&quot;TopY&quot;</i> is a synonym.</p>
<dt><code>Option </code><i>XBottom</i> <i>Inumber</i></p>
<dd>First of three sets of parameters to set the active zone. This sets the X coordinate of the bottom corner of the active zone. <i>&quot;BottomX&quot;</i> is a synonym.</p>
<dt><code>Option </code><i>YBottom</i> <i>number</i></p>
<dd>First of three sets of parameters to set the active zone. This sets the Y coordinate of the bottom corner of the active zone. <i>&quot;BottomY&quot;</i> is a synonym.</p>
<dt><code>Option </code><i>XMax</i> <i>number</i></p>
<dd>Second of three sets of parameters to set the active zone. This sets the the X coordinate of the bottom corner of the active zone. The Top X corner&#8217;s coordinate is fixed at 0. <i>&quot;MaxX&quot;</i> is a synonym.</p>
<dt><code>Option </code><i>YMax</i> <i>number</i></p>
<dd>Second of three sets of parameters to set the active zone. This sets the the Y coordinate of the bottom corner of the active zone. The Top Y corner&#8217;s coordinate is fixed at 0. <i>&quot;MaxY&quot;</i> is a synonym.</p>
<dt><code>Option </code><i>XOffset</i> <i>number</i></p>
<dd>Third of three sets of parameters to set the active zone. This sets the X coordinate of the top corner of the active zone. <i>&quot;OffsetX&quot;</i> is a synonym.</p>
<dt><code>Option </code><i>YOffset</i> <i>number</i></p>
<dd>Third of three sets of parameters to set the active zone. This sets the Y coordinate of the top corner of the active zone. <i>&quot;OffsetY&quot;</i> is a synonym.</p>
<dt><code>Option </code><i>XSize</i> <i>number</i></p>
<dd>Third of three sets of parameters to set the active zone. This sets the X coordinate of the bottom corner of the active zone. Unlike others, this parameter is expressed in <i>relative</i> coordinates from the <i>&quot;XOffset&quot;</i> parameter. <i>&quot;XSize&quot;</i> is a synonym.</p>
<dt><code>Option </code><i>YSize</i> <i>number</i></p>
<dd>Third of three sets of parameters to set the active zone. This sets the Y coordinate of the bottom corner of the active zone. Unlike others, this parameter is expressed in <i>relative</i> coordinates from the <i>&quot;YOffset&quot;</i> parameter. <i>&quot;YSize&quot;</i> is a synonym.</p>
<dt><code>Option </code><i>ZMin</i> <i>number</i></p>
<dd>Minimum pressure reading that will be accepted from the Stylus tool. <i>&quot;MinZ</i>&quot; is a synonym.</p>
<dt><code>Option </code><i>ZMax</i> <i>number</i></p>
<dd>Maximum pressure reading that will be accepted from the Stylus tool. <i>&quot;MaxZ</i>&quot; is a synonym.</p>
<dt><code>Option </code><i>XThreshold</i> <i>number</i></p>
<dd>Minimal change in X coordinate position that will be accepted as data input. <i>&quot;ThresholdX&quot;</i> is a synonym.</p>
<dt><code>Option </code><i>YThreshold</i> <i>number</i></p>
<dd>Minimal change in Y coordinate position that will be accepted as data input. <i>&quot;ThresholdY&quot;</i> is a synonym.</p>
<dt><code>Option </code><i>ZThreshold</i> <i>number</i></p>
<dd>Minimal change in pressure reading that will be accepted as data input. <i>&quot;ThresholdZ&quot;</i> is a synonym.</p>
<dt><code>Option </code><i>InvX</i> <i>on</i></p>
<dd>Inverts X coordinate reports. <i>&quot;XInv&quot;</i> is a synonym.</p>
<dt><code>Option </code><i>InvY</i> <i>on</i></p>
<dd>Inverts Y coordinate reports. <i>&quot;YInv&quot;</i> is a synonym.</p>
<dt><code>Option </code><i>Pressure</i> <i>soft|hard|linear</i></p>
<dd>Pressure reports either delivered in linearly incremental values (default), or perturbed by one of two log-linear algorithms (<i>&quot;soft&quot;</i> or <i>&quot;hard&quot;</i>.)</p>
<dt><code>Option </code><i>KeepShape</i> <i>on</i></p>
<dd>When this option is enabled, the active zone begins according to TopX and TopY. The bottom corner is adjusted to keep the ratio width/height of the active zone the same as the screen while maximizing the area described by the active area set of parameters, XTop/YTop/XBottom/YBottom, XMax/YMax, or XOffset/YOffset/XSize/YSize.</p>
<dt><code>Option </code><i>DebugLevel</i> <i>number </i></p>
<dd>sets the level of debugging info reported.</dl>
</dl>
<p> This driver is currently Linux specific.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/4-hyperpen/">hyperpen</a>(4).</p>
<h2>Authors</h2>
<p>Bryan W. Headley &lt;bheadley [at] earthlink.net&gt;</p>
<h2>Project Page</h2>
<p><a rel="nofollow" href="http://aiptektablet.sourceforge.net">http://aiptektablet.sourceforge.net</a> tracks ongoing development of this driver, the Linux kernel driver, and a GUI front-end application that works in concert with the above.</p>
