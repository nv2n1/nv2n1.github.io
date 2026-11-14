---
title: "edd_show_raw_data(9)"
name: "edd_show_raw_data"
section: "9"
letter: "e"
url: "/docs/linux/man/9-edd_show_raw_data/"
description: "edd_show_raw_data – copies raw data to buffer for userspace to parse"
---

<p>edd_show_raw_data &#8211; copies raw data to buffer for userspace to parse</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ssize_t edd_show_raw_data(struct edd_device&nbsp;<wbr>*&nbsp;<wbr></code><i>edev</i><code>, char&nbsp;<wbr>*&nbsp;<wbr></code><i>buf</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>edev</i></p>
<dl>
<dd>
<dd>target edd_device</dl>
<p> <i>buf</i></p>
<dl>
<dd>output buffer</dl>
<h2>Return</h2>
<p>number of bytes written, or -EINVAL on failure</p>
<h2>Copyright</h2>
