---
title: "b43-fwcutter(1)"
name: "b43-fwcutter"
section: "1"
letter: "b"
url: "/docs/linux/man/1-b43-fwcutter/"
description: "b43-fwcutter – Utility for extracting Broadcom 43xx firmware"
---

<h2>NAME</h2>
<p> b43-fwcutter &#8211; Utility for extracting Broadcom 43xx firmware</p>
<h2>SYNOPSIS</h2>
<p> <code>b43-fwcutter</code> [<i>OPTION</i>] [<i>DRIVER</i>]</p>
<h2>DESCRIPTION</h2>
<p> b43-fwcutter can extract the firmware for your Broadcom 43xx hardware from different closed source drivers. The b43 driver depends on these firmware files and can&#8217;t work without them. </p>
<p> Currently b43-fwcutter supports Apple MacOS X, Microsoft Windows and Linux drivers, but keep in mind that b43-fwcutter doesn&#8217;t support all driver versions. </p>
<p> Example:</p>
<dl>
<dt>
</dt><dd> b43-fwcutter bcmwl5.sys</dd></dl>
<p> to cut the firmware out of bcmwl5.sys</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-l</code>|&#8211;list</dt>
<dd> List supported driver versions</dd>
<dt><code>-i</code>|&#8211;identify</dt>
<dd> Only identify the driver file (don&#8217;t extract)</dd>
<dt><code>-w</code>|&#8211;target-dir DIR</dt>
<dd> Extract and write firmware to DIR</dd>
<dt><code>-a</code>|&#8211;alt-iv</dt>
<dd> Extract alternative initvals (only 3.10.x.x)</dd>
<dt><code>-v</code>|&#8211;version</dt>
<dd> Print b43-fwcutter version</dd>
<dt><code>-h</code>|&#8211;help</dt>
<dd> Print help information</dd></dl>
<h2>AUTHORS</h2>
<p> b43 development team, <a rel="nofollow" href="http://wireless.kernel.org/en/users/Drivers/b43">http://wireless.kernel.org/en/users/Drivers/b43</a> </p>
