---
title: "module_w1_family(9)"
name: "module_w1_family"
section: "9"
letter: "m"
url: "/docs/linux/man/9-module_w1_family/"
description: "module_w1_family – Helper macro for registering a 1-Wire families"
---

<p>module_w1_family &#8211; Helper macro for registering a 1-Wire families</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>module_w1_family(</code><i>__w1_family</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>__w1_family</i></p>
<dl>
<dd>
<dd>w1_family struct</dl>
<h2>Description</h2>
<p>Helper macro for 1-Wire families which do not do anything special in module init/exit. This eliminates a lot of boilerplate. Each module may only use this macro once, and calling it replaces <code>module_init</code> and <code>module_exit</code></p>
<h2>Author</h2>
<p><code>David Fries</code> &lt;David [at] Fries.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
