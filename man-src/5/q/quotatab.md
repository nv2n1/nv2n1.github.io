---
title: "quotatab(5)"
name: "quotatab"
section: "5"
letter: "q"
url: "/docs/linux/man/5-quotatab/"
description: "quotatab – Descriptions of devices with disk quotas"
---

<p>quotatab &#8211; Descriptions of devices with disk quotas</p>
<h2>Synopsis</h2>
<p><code>/etc/quotatab</code></p>
<h2>Description</h2>
<p>The <code>quotatab</code> file lists human descriptions of devices for the purpose of <code><a href="/docs/linux/man/8-warnquota/">warnquota</a></code>(8) notifications. </p>
<p> Each line consists of a device path name followed by a colon and a description. White space, apostrophe, and double quote characters surrounding the names and descriptions will be stripped. The description field can encode a new-line as a pipe character. </p>
<p> Empty lines or lines starting with a hash sign or a semicolon are ignored.</p>
<h2>Example</h2>
<p># comment</p>
<dl>
<dd>/dev/sda2: Home directories.|This becomes second line.</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/quotatab</code></p>
<dd>list of device descriptions</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-warnquota/">warnquota</a></code>(8). </p>
