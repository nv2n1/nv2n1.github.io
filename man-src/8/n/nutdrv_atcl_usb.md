---
title: "nutdrv_atcl_usb(8)"
name: "nutdrv_atcl_usb"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nutdrv_atcl_usb/"
description: "nutdrv_atcl_usb – Driver for ‘ATCL FOR UPS’ equipment"
---

<p>nutdrv_atcl_usb &#8211; Driver for &#8216;ATCL FOR UPS&#8217; equipment</p>
<h2>Note</h2>
<p>This man page only documents the specific features of the nutdrv_atcl_usb driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8).</p>
<h2>Supported Hardware</h2>
<p>This driver is for UPS hardware which identifies itself as USB idVendor 0001 and idProduct 0000, and iManufacturer ATCL FOR UPS. Known manufacturers include Kanji and Plexus. The UPS interface seems to be a USB frontend to a traditional contact-closure interface, which translates into only three states in ups.status: <code>OL</code>, <code>OB</code> and <code>OB LB</code>. See also <code><a href="/docs/linux/man/8-genericups/">genericups</a></code>(8).</p>
<h2>Extra Arguments</h2>
<p>This driver supports the following optional setting: </p>
<p> <code>vendor</code>=<i>name</i></p>
<dl>
<dd>In case your iManufacturer (Vendor) string does not exactly match ATCL FOR UPS, you may provide an alternate string here. Note that a more likely case is that your device is handled by another driver for 0001:0000 devices, such as <code><a href="/docs/linux/man/8-nutdrv_qx/">nutdrv_qx</a></code>(8).</dl>
<h2>Bugs</h2>
<p>The UPS returns the same code for &quot;load power is off&quot; as for &quot;on line power&quot;. This condition will not be observed if the NUT master is powered by the UPS, but may be an issue if the UPS is monitored by a remote system. </p>
<p> The time between the shutdown command and removal of power seems to be fixed at 30 seconds. Ensure that the NUT shutdown script is invoked as late as possible in the shutdown procedure (in case some services take longer than others to clean up). </p>
<p> Most contact-closure UPSes will not power down the load if the line power is present. This can create a race when using slave <code><a href="/docs/linux/man/8-upsmon/">upsmon</a></code>(8) systems. See the <code><a href="/docs/linux/man/8-upsmon/">upsmon</a></code>(8) man page for more information. The solution to this problem is to upgrade to a smart protocol UPS of some kind that allows detection and proper load cycling on command.</p>
<h2>Authors</h2>
<p>Charles Lepple</p>
<h2>See Also</h2>
<h3>The core driver:</h3>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8)</p>
<h3>The generic serial driver:</h3>
<p><code><a href="/docs/linux/man/8-genericups/">genericups</a></code>(8)</p>
<h3>The Qx driver:</h3>
<p><code><a href="/docs/linux/man/8-nutdrv_qx/">nutdrv_qx</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
