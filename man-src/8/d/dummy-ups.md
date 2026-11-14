---
title: "dummy-ups(8)"
name: "dummy-ups"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dummy-ups/"
description: "dummy-ups – Driver for multi-purpose UPS emulation"
---

<p>dummy-ups &#8211; Driver for multi-purpose UPS emulation</p>
<h2>Note</h2>
<p>This man page only documents the specific features of the dummy-ups driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8).</p>
<h2>Description</h2>
<p>This program is a multi-purpose UPS emulation tool. Its behavior depends on the running mode:</p>
<h3>Dummy Mode</h3>
<p><code>dummy-ups</code> looks like a standard device driver to <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8) and allows one to change any value for testing purposes. It is both interactive, controllable through the <code><a href="/docs/linux/man/1-upsrw/">upsrw</a></code>(1) and <code><a href="/docs/linux/man/1-upscmd/">upscmd</a></code>(1) commands (or equivalent graphical tool), and batchable through script files. It can be configured, launched and used as any other real driver. This mode is mostly useful for development and testing purposes.</p>
<h3>Repeater Mode</h3>
<p><code>dummy-ups</code> acts as a NUT client, simply forwarding data. This can be useful for supervision purposes. This can also allow some load sharing between several UPS instances, using a point-to-point communication with the UPS.</p>
<h2>Implementation</h2>
<p>The port specification depends on the running mode, and allows the driver to select the right mode.</p>
<h3>Dummy Mode</h3>
<p>Port is a definition file name for <code>dummy-ups</code>. This can either be an absolute or a relative path name. In the latter case the NUT sysconfig directory (ie /etc/nut, /usr/local/ups/etc, &#8230;) is prepended. </p>
<p> For instance: </p>
<dl>
<dd>
<pre>[dummy]
 driver = dummy-ups
 port = evolution500.dev
 desc = &quot;dummy-ups in dummy mode&quot;</pre>
</dl>
<p> This file is generally named &quot;something.dev&quot;. It contains a list of all valid data and associated values, and has the same format as an <code><a href="/docs/linux/man/8-upsc/">upsc</a></code>(8) dump (&lt;varname&gt;: &lt;value&gt;). So you can easily create definition files from an existing UPS using &quot;upsc &gt; file.dev&quot;. It can also be empty, in which case only a basic set of data is available: device.<code>, driver.</code>, ups.mfr, ups.model, ups.status </p>
<p> Samples definition files are available in the &quot;data&quot; directory of the nut source tree, and generally in the sysconfig directory of your system distribution. </p>
<p> Since <code>dummy-ups</code> will loop on reading this file, you can dynamically modify it to interact with the driver. This will avoid message spam into your system log files, if you are using NUT default configuration. </p>
<p> You can also use the &quot;TIMER &lt;seconds&gt;&quot; instruction to create scheduled events sequences. For example, the following sequence will loop on switching ups.status between &quot;OL&quot;, &quot;OB&quot; and &quot;OB LB&quot; every minute: </p>
<dl>
<dd>
<pre>ups.status: OL
TIMER 60
ups.status: OB
TIMER 60
ups.status: LB
TIMER 60</pre>
</dl>
<p> It is wise to end the script with a TIMER. Otherwise dummy-ups will directly go back to the beginning of the file.</p>
<h3>Repeater Mode</h3>
<p>Port is the name of a remote UPS, using the NUT form, ie: </p>
<dl>
<dd>
<pre>&lt;upsname&gt;[@&lt;hostname&gt;[:&lt;port&gt;]]</pre>
</dl>
<p> For instance: </p>
<dl>
<dd>
<pre>[repeater]
 driver = dummy-ups
 port = ups [at] hostname
 desc = &quot;dummy-ups in repeater mode&quot;</pre>
</dl>
<h2>Interaction</h2>
<p>Once the driver is loaded in dummy mode, you can change any variables, except those of the driver.* and server.* collections. You can do this by either editing the definition file, or use the <code><a href="/docs/linux/man/1-upsrw/">upsrw</a></code>(1) and <code><a href="/docs/linux/man/1-upscmd/">upscmd</a></code>(1) commands. </p>
<p> Note that in simulation mode, new variables can be added on the fly, by adding these to the definition file. Conversely, if you need to remove variable (such as transient ones, like ups.alarm), simply update these by setting an empty value. As a result, they will get removed from the data. </p>
<p> In repeater mode, the driver acts according to the capabilities of the UPS, and so support the same instant commands and settable values.</p>
<h2>Background</h2>
<p>This driver was written in one evening to replace the previous dummycons testing driver. It was too limited and required to work from a terminal to interact. </p>
<p> <code>dummy-ups</code> is useful for NUT client development, and other testing purpose. </p>
<p> It also helps the NUT Quality Assurance effort, by automating some tests on the NUT framework. </p>
<p> It now offers a repeater mode. This will help in building the Meta UPS approach, which allows one to build a virtual device, composed of several other devices (either UPS, PDUs).</p>
<h2>Bugs</h2>
<p>Instant commands are not yet supported in Dummy Mode, and data need name/value checking enforcement, as well as boundaries or enumeration definition.</p>
<h2>Author</h2>
<p>Arnaud Quette</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-upscmd/">upscmd</a></code>(1), <code><a href="/docs/linux/man/1-upsrw/">upsrw</a></code>(1), <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5), <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8)</p>
<h3>Internet Resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
