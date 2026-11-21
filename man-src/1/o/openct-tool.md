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
<dt><code>-d</code></dt>
<dd> enable debugging; repeat to increase verbosity</dd>
<dt><code>-f</code> <i>configfile</i></dt>
<dd> specify config file (default @openct_conf_path@)</dd>
<dt><code>-r</code> <i>reader</i></dt>
<dd> specify index of reader to use</dd>
<dt><code>-h</code></dt>
<dd> display this message</dd>
<dt><code>-v</code></dt>
<dd> display version and exit</dd></dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>list</code></dt>
<dd> list all readers found</dd>
<dt><code>atr</code></dt>
<dd> print ATR of card in selected reader</dd>
<dt><code>wait</code></dt>
<dd> wait for card to be inserted</dd>
<dt><code>rwait</code></dt>
<dd> wait for reader to be attached</dd>
<dt><code>mf</code></dt>
<dd> try to select main folder of card</dd>
<dt><code>read</code></dt>
<dd> dump memory of synchronous card </dd>
</dl>
