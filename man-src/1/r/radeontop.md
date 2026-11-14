---
title: "radeontop(1)"
name: "radeontop"
section: "1"
letter: "r"
url: "/docs/linux/man/1-radeontop/"
description: "radeontop – tool to show GPU utilization"
---

<h2 class="name">NAME</h2>
<p> radeontop &#8211; tool to show GPU utilization </p>
<h2>SYNOPSIS</h2>
<p> <code>radeontop [-chv] [-b </code><i>bus</i><code>] [-d </code><i>file</i><code>] [-l </code><i>limit</i><code>] [-t </code><i>ticks</i><code>]</code></p>
<h2>DESCRIPTION</h2>
<p> RadeonTop shows the utilization of your GPU, both in general and by blocks. </p>
<p> Supported cards are R600 and up.</p>
<h2>OPTIONS</h2>
<p> <code>-b, &#8211;bus </code><i>bus</i></p>
<dl>
<dt>
<dd> If you have multiple cards, use this parameter to select a specific one. For lspci output <i>01:00.0 VGA compatible controller</i>, bus would be <i>1</i>.</dl>
<p> <code>-c, &#8211;color</code></p>
<dl>
<dt>
<dd> Enables colorized output.</dl>
<p> <code>-d, &#8211;dump </code><i>file</i></p>
<dl>
<dt>
<dd> Instead of displaying the data, dump it to <i>file</i>. Use <i>&#8211;</i> for stdout. The file is appended to, so it&#8217;s safe to specify the same filename for consecutive runs. </p>
<p> Use <i>SIGTERM</i> or <i>SIGINT</i> for graceful termination.</dl>
<p> <code>-h, &#8211;help</code></p>
<dl>
<dt>
<dd> Displays help.</dl>
<p> <code>-l, &#8211;limit </code><i>limit</i></p>
<dl>
<dt>
<dd> Quit after dumping <i>limit</i> lines. Only valid in dump mode. Default is to dump until terminated; use <i>SIGTERM</i> or <i>SIGINT</i> for graceful termination.</dl>
<p> <code>-m, &#8211;mem</code></p>
<dl>
<dt>
<dd> Forces the use of the /dev/mem path, in case autodetection fails. Useful for the proprietary driver.</dl>
<p> <code>-t, &#8211;ticks </code><i>ticks</i></p>
<dl>
<dt>
<dd> How many times per second to sample the data. The default is 120. Higher numbers mean more accurate output and more overhead.</dl>
<p> <code>-v, &#8211;version</code></p>
<dl>
<dt>
<dd> Displays the program version.</dl>
<h2>INTERACTIVE COMMANDS</h2>
<p> <code>C, c</code></p>
<dl>
<dt>
<dd> Toggle colorized output.</dl>
<p> <code>Q, q</code></p>
<dl>
<dt>
<dd> Quit.</dl>
<h2>RESOURCES</h2>
<p> See <a rel="nofollow" href="http://github.com/clbr/radeontop">http://github.com/clbr/radeontop</a> </p>
<h2>Index</h2>
