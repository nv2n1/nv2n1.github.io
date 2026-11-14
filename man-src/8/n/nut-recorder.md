---
title: "nut-recorder(8)"
name: "nut-recorder"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nut-recorder/"
description: "nut-recorder – utility to record device status and values changes"
---

<p>nut-recorder &#8211; utility to record device status and values changes</p>
<h2>Synopsis</h2>
<p><code>nut-recorder</code> <i>device-name</i> [output-file] [interval]</p>
<h2>Description</h2>
<p><code>nut-recorder</code> is an utility to record sequences from running devices (such as power failures, or any other value changes) from upsd, and dump it in a .seq format. </p>
<p> The .seq file can then be used by the <code><a href="/docs/linux/man/8-dummy-ups/">dummy-ups</a></code>(8) driver to replay the sequence.</p>
<h2>Options</h2>
<p><i>device-name</i></p>
<dl>
<dd>Record the changes of this device. The format for this option is <i>devname[@hostname[:port]]</i>. The default hostname is &quot;localhost&quot;.</dl>
<p> <i>output-file</i></p>
<dl>
<dd>Optional. Data will be saved to this file. The default is <i>dummy-device.seq</i>.</dl>
<p> <i>interval</i></p>
<dl>
<dd>Optional. The status of the device will be checked every <i>interval</i>. The default is 5 seconds.</dl>
<h2>Examples</h2>
<p>To record data from <i>ups1 [at] host1</i> every 10 seconds: </p>
<dl>
<dd>
<pre>$ nut-recorder ups1 [at] host1' ups1-output.seq 10
. . .
battery.charge: 100.0
battery.voltage: 13.9
battery.voltage.nominal: 13.6
ups.status: OL
. . .
battery.charge: 90.0
ups.status: OB
. . .</pre>
</dl>
<p> You can then define a dummy device in <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5): </p>
<dl>
<dd>
<pre>[ups-test]
 driver = dummy-ups
 port = ups1-output.seq</pre>
</dl>
<h2>Author</h2>
<p>Arnaud Quette</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-dummy-ups/">dummy-ups</a></code>(8)</p>
<h2>Internet Resources</h2>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a></p>
