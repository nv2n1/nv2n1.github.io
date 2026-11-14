---
title: "deghosting_mask(1)"
name: "deghosting_mask"
section: "1"
letter: "d"
url: "/docs/linux/man/1-deghosting_mask/"
description: "deghosting_mask – Creates mask for removing ghosting in images"
---

<h2 class="name">NAME</h2>
<p> deghosting_mask &#8211; Creates mask for removing ghosting in images </p>
<h2>SYNOPSIS</h2>
<p> <code>deghosting_mask</code> [options] <i>&lt;image1</i>&gt; <i>&lt;image2</i>&gt; <i>&#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> Takes a series of aligned photos, usually three or more, and generates masks for removal of ghosts &#8211; Data that only appears in a minority of photos.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o|&#8211;output</code> &lt;path&gt;</p>
<dd> Prefix for output masks</p>
<dt><code>-s|&#8211;sigma</code> &lt;float&gt;</p>
<dd> Standard deviation of Gaussian weighting function (<font SIZE="-1">SIGMA </font>&gt; 0); default: 30</p>
<dt><code>-i|&#8211;iterations</code> &lt;int&gt;</p>
<dd> Number of iterations, default is (<font SIZE="-1">ITER </font>&gt; 0) default: 4</p>
<dt><code>-t|&#8211;threshold</code> &lt;float&gt;</p>
<dd> Threshold; default: 150</p>
<dt><code>-c|&#8211;contrast</code> &lt;float&gt;</p>
<dd> Change constrast before applying threshold; default: 1.3</p>
<dt><code>-a|&#8211;advanced</code> &lt;f|g|m|t|w&gt;</p>
<dd> Advanced settings. Possible options are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>f</code> Use gray images for computation. It&#8217;s about two times faster but it usually returns worse results. You also have to change threshold to smaller value (around 100)</p>
<dd>
<dt><code>g</code> Use gamma 2.2 correction instead of logarithm if input images are <font SIZE="-1">HDR</font></p>
<dd>
<dt><code>m</code> Do not scale image, <font SIZE="-1">NOTE:</font> slows down process</p>
<dd>
<dt><code>t</code> Use simple threshold, may result in holes in images</p>
<dd>
<dt><code>w</code> Compute &quot;complete&quot; weights, not only probabilities</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-w|&#8211;save</code> &lt;i|w&gt;</p>
<dd> Advanced save settings</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>i</code> Save initial weigths</p>
<dd>
<dt><code>w</code> Save generated weigths</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-b</code> &lt;int&gt;</p>
<dd> Image cache <font SIZE="-1">BLOCKSIZE</font> in kilobytes; default: 2048KB</p>
<dt><code>-m</code> &lt;int&gt;</p>
<dd> Set image <font SIZE="-1">CACHESIZE</font> in megabytes; default: 1024MB</p>
<dt><code>-h|&#8211;help</code></p>
<dd> Display this help</p>
<dt><code>-v|&#8211;verbose</code> &lt;0|1&gt;</p>
<dd> Verbose, repeat for more verbose output</dl>
<h2>AUTHORS</h2>
<p> LukaX Jirkovsky </p>
<h2>Index</h2>
