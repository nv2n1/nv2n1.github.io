---
title: "openct-tool(1)"
name: "openct-tool"
section: "1"
letter: "o"
url: "/docs/linux/man/1-openct-tool/"
description: "openct-tool – OpenCT smart card utility"
---

<h2>NAME</h2>
<p> openct-tool &#8211; OpenCT smart card utility</p>
<h2>SYNOPSIS</h2>
<p> openct-tool [options] command &#8230;</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code></p>
<dd> enable debugging; repeat to increase verbosity</p>
<dt><code>-f</code> <i>configfile</i></p>
<dd> specify config file (default @openct_conf_path@)</p>
<dt><code>-r</code> <i>reader</i></p>
<dd> specify index of reader to use</p>
<dt><code>-h</code></p>
<dd> display this message</p>
<dt><code>-v</code></p>
<dd> display version and exit</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>list</code></p>
<dd> list all readers found</p>
<dt><code>atr</code></p>
<dd> print ATR of card in selected reader</p>
<dt><code>wait</code></p>
<dd> wait for card to be inserted</p>
<dt><code>rwait</code></p>
<dd> wait for reader to be attached</p>
<dt><code>mf</code></p>
<dd> try to select main folder of card</p>
<dt><code>read</code></p>
<dd> dump memory of synchronous card </p>
</dl>
<h2>Index</h2>
