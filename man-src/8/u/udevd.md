---
title: "udevd(8)"
name: "udevd"
section: "8"
letter: "u"
url: "/docs/linux/man/8-udevd/"
description: "udevd – event managing daemon"
---

<p>udevd &#8211; event managing daemon</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>udevd</code> [<code>&#8211;daemon</code>] [<code>&#8211;debug</code>] [<code>&#8211;children-max=</code>] [<code>&#8211;exec-delay=</code>] [<code>&#8211;resolve-names=early|late|never</code>] [<code>&#8211;version</code>] [<code>&#8211;help</code>]</dl>
<h2>Description</h2>
<dd>udevd listens to kernel uevents. For every event, udevd executes matching instructions specified in udev rules. See <code><a href="/docs/linux/man/7-udev/">udev</a></code>(7). </p>
<p> On startup the content of the directory /usr/lib/udev/devices is copied to /dev. If kernel modules specify static device nodes, these nodes are created even without a corresponding kernel device, to allow on-demand loading of kernel modules. Matching permissions specified in udev rules are applied to these static device nodes. </p>
<p> The behavior of the running daemon can be changed with <code>udevadm control</code>.</p>
<h2>Options</h2>
<p><code>&#8211;daemon</code></p>
<dl>
<dd>Detach and run in the background.</dl>
<p> <code>&#8211;debug</code></p>
<dl>
<dd>Print debug messages to stderr.</dl>
<p> <code>&#8211;children-max=</code></p>
<dl>
<dd>Limit the number of parallel executed events.</dl>
<p> <code>&#8211;exec-delay=</code></p>
<dl>
<dd>Number of seconds to delay the execution of RUN instructions. This might be useful when debugging system crashes during coldplug cause by loading non-working kernel modules.</dl>
<p> <code>&#8211;resolve-names=</code></p>
<dl>
<dd>Specify when udevd should resolve names of users and groups. When set to <code>early</code> (the default) names will be resolved when the rules are parsed. When set to <code>late</code> names will be resolved for every event. When set to <code>never</code> names will never be resolved and all devices will be owned by root.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dd>Print version number.</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dd>Print help text.</dl>
<h2>Environment</h2>
<p><i>UDEV_LOG=</i></p>
<dl>
<dd>Set the logging priority.</dl>
<h2>Kernel Command Line</h2>
<p><i>udev.log-priority=</i></p>
<dl>
<dd>Set the logging priority.</dl>
<p> <i>udev.children-max=</i></p>
<dl>
<dd>Limit the number of parallel executed events.</dl>
<p> <i>udev.exec-delay=</i></p>
<dl>
<dd>Number of seconds to delay the execution of RUN instructions. This might be useful when debugging system crashes during coldplug cause by loading non-working kernel modules.</dl>
<h2>Author</h2>
<p>Written by Kay Sievers kay.sievers [at] vrfy.org.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-udev/">udev</a></code>(7), <code><a href="/docs/linux/man/8-udevadm/">udevadm</a></code>(8) </p>
