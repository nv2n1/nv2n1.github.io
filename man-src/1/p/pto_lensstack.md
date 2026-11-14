---
title: "pto_lensstack(1)"
name: "pto_lensstack"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pto_lensstack/"
description: "pto_lensstack – modify assigned lenses and stack in pto files"
---

<h2 class="name">NAME</h2>
<p> pto_lensstack &#8211; modify assigned lenses and stack in pto files </p>
<h2>SYNOPSIS</h2>
<p> <code>pto_lensstack</code> [options] input.pto</p>
<h2>DESCRIPTION</h2>
<p> <code>pto_lensstack</code> can manipulate lenses and stacks in Hugin .pto project files. This is intended for use in scripting.</p>
<h2>USAGE</h2>
<pre><code>
pto_lensstack-- output = output.pto-- new - lens | --new - stack | --change - lens | --change - stack images input.pto
</code></pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;new-lens</code></p>
<dd>
<dt><code>&#8211;new-stack</code></p>
<dd> For assigned a new lens or stack to an image provide a list of image numbers. The counting starts with zero. Several images can be given at same time. Separate them with a comma. </p>
<p> Examples:<br />
&nbsp;<wbr>&nbsp;<wbr>pto_lensstack &#8211;new-lens i1,i3 input.pto<br />
&nbsp;<wbr>&nbsp;<wbr>pto_lensstack &#8211;new-stack i2,i4 input.pto </p>
<p> will assign a new lens to image 1 and 3 and a new stack to images 2 and 4.</p>
<dt><code>&#8211;change-lens</code></p>
<dd>
<dt><code>&#8211;change-stack</code></p>
<dd> For changing the lens or the stack provide a list of image numbers and the new lens/stack number. For both the counting starts with zero and you can supply several images separated by a comma at the same time. </p>
<p> Examples:<br />
&nbsp;<wbr>&nbsp;<wbr>pto_lensstack &#8211;change-lens i1=4,i5=1 input.pto<br />
&nbsp;<wbr>&nbsp;<wbr>pto_lensstack &#8211;change-stack i2=0,i4=0 input.pto</p>
<dt><code>-o|&#8211;output</code></p>
<dd> Output a pto file with the given filename. If not given it will append &#8220;_lens&#8221; to the input filename.</p>
<dt><code>-h|&#8211;help</code></p>
<dd> Display help</dl>
<h2>AUTHORS</h2>
<p> Thomas Modes </p>
<h2>Index</h2>
