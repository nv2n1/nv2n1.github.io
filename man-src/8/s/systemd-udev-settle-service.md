---
title: "systemd-udev-settle-service(8)"
name: "systemd-udev-settle-service"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-udev-settle-service/"
description: "systemd-udev-settle.service – Wait for all pending udev events to be handled"
---

<p>systemd-udev-settle.service &#8211; Wait for all pending udev events to be handled</p>
<h2>Synopsis</h2>
<p>systemd-udev-settle.service</p>
<h2>Description</h2>
<p>This service calls <code>udevadm settle</code> to wait until all events that have been queued by <code><a href="/docs/linux/man/7-udev/">udev</a></code>(7) have been processed. It is a crude way to wait until &quot;all&quot; hardware has been discovered. Services may pull in this service and order themselves after it to wait for the udev queue to be empty. </p>
<p> <i>Using this service is not recommended.</i> There can be no guarantee that hardware is fully discovered at any specific time, because the kernel does hardware detection asynchronously, and certain buses and devices take a very long time to become ready, and also additional hardware may be plugged in at any time. Instead, services should subscribe to udev events and react to any new hardware as it is discovered. Services that, based on configuration, expect certain devices to appear, may warn or report failure after a timeout. This timeout should be tailored to the hardware type. Waiting for systemd-udev-settle.service usually slows boot significantly, because it means waiting for all unrelated events too.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-udev/">udev</a></code>(7), <code><a href="/docs/linux/man/8-udevadm/">udevadm</a></code>(8) </p>
