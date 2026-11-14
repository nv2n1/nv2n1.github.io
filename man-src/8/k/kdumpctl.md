---
title: "kdumpctl(8)"
name: "kdumpctl"
section: "8"
letter: "k"
url: "/docs/linux/man/8-kdumpctl/"
description: "kdumpctl – control interface for kdump"
---

<p>kdumpctl &#8211; control interface for kdump</p>
<h2>Synopsis</h2>
<p><code>kdumpctl</code> <i>COMMAND</i> </p>
<h2>Description</h2>
<p><code>kdumpctl</code> is used to check or control the kdump service. In most cases, you should use <code>systemctl</code> to start / stop / enable kdump service instead. However, <code>kdumpctl</code> provides more details for debug and a helper to setup ssh key authentication. </p>
<h2>Commands</h2>
<dl>
<dt><i>start</i></p>
<dd>Start the service.</p>
<dt><i>stop</i></p>
<dd>Stop the service.</p>
<dt><i>status</i></p>
<dd>Prints the current status of kdump service. It returns non-zero value if kdump is not operational.</p>
<dt><i>restart</i></p>
<dd>Is equal to <i>start; stop</i></p>
<dt><i>propagate</i></p>
<dd>Helps to setup key authentication for ssh storage since it&#8217;s impossible to use password authentication during kdump.</p>
<dt><i>showmem</i></p>
<dd>Prints the size of reserved memory for crash kernel in megabytes. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-kdump-conf/">kdump.conf</a></code>(5), <code><a href="/docs/linux/man/8-mkdumprd/">mkdumprd</a></code>(8) </p>
