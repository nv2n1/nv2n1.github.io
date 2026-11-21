---
title: "lrfviewer(1)"
name: "lrfviewer"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lrfviewer/"
description: "lrfviewer – view LRF ebook"
---

<h2 class="name">NAME</h2>
<p> <code> lrfviewer </code>&#8211; view LRF ebook </p>
<h2>USAGE</h2>
<p> lrfviewer [options] book.lrf</p>
<h2>DESCRIPTION</h2>
<p> Read the LRF ebook book.lrf </p>
<p> Whenever you pass arguments to lrfviewer that have spaces in them, enclose the arguments in quotation marks.</p>
<h2>MAIN OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></dt>
<dd> show program&#8217;s version number and exit</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show this help message and exit</dd>
<dt><code>&#8211;redirect-console-output</code></dt>
<dd> Redirect console output to a dialog window (both stdout and stderr). Useful on windows where GUI apps do not have a output streams.</dd>
<dt><code>&#8211;verbose</code></dt>
<dd> Print more information about the rendering process</dd>
<dt><code>&#8211;visual-debug</code></dt>
<dd> Turn on visual aids to debugging the rendering engine</dd>
<dt><code>&#8211;disable-hyphenation</code></dt>
<dd> Disable hyphenation. Should significantly speed up rendering.</dd>
<dt><code>&#8211;white-background</code></dt>
<dd> By default the background is off white as I find this easier on the eyes. Use this option to make the background pure white.</dd>
<dt><code>&#8211;profile</code></dt>
<dd> Profile the LRF renderer</dd></dl>
<h2>AUTHOR</h2>
<p> Created by Kovid Goyal &lt;kovid [at] kovidgoyal.net&gt; </p>
