---
title: "amdevcheck(8)"
name: "amdevcheck"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amdevcheck/"
description: "amdevcheck – Validate an Amanda device and volume."
---

<p>amdevcheck &#8211; Validate an Amanda device and volume.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>amdevcheck</code> [&#8211;label] [-properties&nbsp;<wbr><i>list</i>] [<code>-o</code>&nbsp;<wbr><i>configoption</i>&#8230;] <i>config</i> [<i>device-name</i>]</dl>
<h2>Description</h2>
<p><code>Amdevcheck</code></p>
<dd>provides a way to check that a particular Amanda device is accessible, whether or not it contains a volume, and whether or not that volume is labeled. Some devices can&#8217;t distinguish between all of these cases; a missing volume and an unlabeled volume might generate the same error code, for example. In those cases, this tool reports all possible causes of the error. Optionally this tools lists the properties for the device. </p>
<p> See the <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8) man page for more details about Amanda. See <code><a href="/docs/linux/man/7-amanda-devices/">amanda-devices</a></code>(7) for more information on devices.</p>
<h2>Options</h2>
<p><i>config</i></p>
<dl>
<dd>Amanda configuration to use. Note that <code>amdevcheck</code> ignores any tape changer configuration.</dl>
<p> <i>device</i></p>
<dl>
<dd>Amanda device to use. This option overrides any tapedev configuration specified in the configuration file.</dl>
<p> <i>&#8211;label</i></p>
<dl>
<dd>Get the device&#8217;s label. If this option is given, the usual check output is omitted, and the label of the loaded volume is printed to stdout. Returns with error if the label is not found.</dl>
<p> <i>&#8211;properties [list]</i></p>
<dl>
<dd>List device properties. If this option is given, the usual check output is omitted, and property values are printed to stdout, one per line, as a property name, followed by &#8216;=&#8217;, followed by the property value. Returns with error if properties are not available. </p>
<p> If <i>list</i> is given, it is treated as a comma-separated list of properties to display. If it is omitted, all supported properties are displayed.</dl>
<p> <code>-o </code><i>configoption</i></p>
<dl>
<dd>See the &quot;CONFIGURATION OVERRIDE&quot; section in <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8).</dl>
<h2>Output</h2>
<p><code>amdevcheck</code> exit with code 0 if the device is working of if it get an expected error, look at the MESSAGE line for the error. It exit with code 1 if it get an unexpected error. </p>
<p> <code>Amdevcheck</code> returns one or more of the following lines. If multiple lines appear, then at least one, but not necessarily all of the messages apply. This situation can occur when working with hardware or operating systems which cannot distinguish, for example, between a malfunctioning drive and a functional but unloaded drive. </p>
<p> <code>SUCCESS</code></p>
<dl>
<dd>A tape is ready.</dl>
<p> <code>DEVICE_ERROR</code></p>
<dl>
<dd>A device error has occurred.</dl>
<p> <code>DEVICE_BUSY</code></p>
<dl>
<dd>The device is busy.</dl>
<p> <code>VOLUME_MISSING</code></p>
<dl>
<dd>No tape is loaded in the drive.</dl>
<p> <code>VOLUME_UNLABELED</code></p>
<dl>
<dd>The tape in the drive is unlabeled.</dl>
<p> <code>VOLUME_ERROR</code></p>
<dl>
<dd>A volume error has occurred.</dl>
<p> <code>MESSAGE</code> <i>text</i></p>
<dl>
<dd>Where text provides a human-readable description of the problem.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/7-amanda-devices/">amanda-devices</a></code>(7) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Author</h2>
<p><code>Ian Turner</code> &lt;ian [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
