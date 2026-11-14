---
title: "libinput-replay(1)"
name: "libinput-replay"
section: "1"
letter: "l"
url: "/docs/linux/man/1-libinput-replay/"
description: "libinput-replay – replay kernel events from a recording"
---

<h2 class="name">NAME</h2>
<p> libinput-replay &#8211; replay kernel events from a recording </p>
<h2>SYNOPSIS</h2>
<p> <code>libinput replay [options] </code><i>recording</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>libinput replay</code> tool replays kernel events from a device recording made by the <code>libinput <a href="/docs/linux/man/1-record/">record</a>(1)</code> tool. This tool needs to run as root to create a device and/or replay events. </p>
<p> If the recording contains more than one device, all devices are replayed simultaneously.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Print help</dl>
<h2>NOTES</h2>
<p> This tool replays events from a recording through the the kernel and is independent of libinput. In other words, updating or otherwise changing libinput will not alter the output from this tool. libinput itself does not need to be in use to replay events.</p>
<h2>LIBINPUT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-libinput/">libinput</a>(1)</code> suite </p>
<h2>Index</h2>
