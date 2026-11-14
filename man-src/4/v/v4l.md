---
title: "v4l(4)"
name: "v4l"
section: "4"
letter: "v"
url: "/docs/linux/man/4-v4l/"
description: "v4l – video4linux driver"
---

<p>v4l &#8211; video4linux driver</p>
<h2>Synopsis</h2>
<pre><code>Section &#34;Module&#34;</code>
&nbsp;<wbr>&nbsp;<wbr>...
<code> Load &#34;v4l&#34;</code>
<code>EndSection</code></pre>
<h2>Description</h2>
<p><code>v4l </code> is an Xorg driver for video4linux cards. It provides a Xvideo extension port for video overlay. Just add the driver to the module list within the module section of your xorg.conf file if you want to use it. There are no config options. </p>
<p> Note that the extmod module is also required for the Xvideo support (and lots of other extensions too).</p>
<h2>Supported Hardware</h2>
<p>The <code>v4l</code> driver works with every piece of hardware which is supported by a video4linux (kernel-) device driver and is able to handle video overlay. </p>
<p> bt848/bt878-based TV cards are the most popular hardware these days.</p>
<h2>Configuration Details</h2>
<p>Please refer to <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) for general configuration details. This section only covers configuration details specific to this driver.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-xorgconfig/">xorgconfig</a>(1), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7)</p>
<h2>Authors</h2>
<p>Authors include: Gerd Knorr &lt;kraxel [at] bytesex.org&gt;</p>
