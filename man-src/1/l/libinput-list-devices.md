---
title: "libinput-list-devices(1)"
name: "libinput-list-devices"
section: "1"
letter: "l"
url: "/docs/linux/man/1-libinput-list-devices/"
description: "libinput-list-devices – list local devices as recognized by libinput and default values of their configuration"
---

<h2 class="name">NAME</h2>
<p> libinput-list-devices &#8211; list local devices as recognized by libinput and default values of their configuration </p>
<h2>SYNOPSIS</h2>
<p> <code>libinput list-devices [&#8211;help]</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>libinput list-devices</code> tool creates a libinput context on the default seat &quot;seat0&quot; and lists all devices recognized by libinput. Each device shows available configurations the respective default configuration setting. </p>
<p> For options that allow more settings than &quot;enabled/disabled&quot;, all available ones are listed. The default setting is prefixed by an asterisk (*). </p>
<p> This tool usually needs to be run as root to have access to the /dev/input/eventX nodes.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Print help</dl>
<h2>NOTES</h2>
<p> Some specific feature may still be available on a device even when no configuration is exposed, a lack of a configuration option does not necessarily mean that this feature does not work. </p>
<p> A device may be recognized by libinput but not handled by the X.Org libinput driver or the Wayland compositor. </p>
<p> An <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) configuration entry or Wayland compositor setting may have changed configurations on a device. The <code>libinput list-devices</code> tool only shows the device&#8217;s default configuration, not the current configuration.</p>
<h2>LIBINPUT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-libinput/">libinput</a>(1)</code> suite </p>
<h2>Index</h2>
