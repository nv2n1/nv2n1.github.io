---
title: "void(4)"
name: "void"
section: "4"
letter: "v"
url: "/docs/linux/man/4-void/"
---

<pre><code>void - null input driver</code></pre>
<h2>Synopsis</h2>
<pre><code>Section &#34;InputDevice&#34;</code>
<code> Identifier &#34;</code><i>idevname</i><code>&#34;</code>
<code> Driver &#34;void&#34;</code>
&nbsp;<wbr>&nbsp;<wbr>...
<code>EndSection</code></pre>
<h2>Description</h2>
<p><code>void </code> is an dummy/null Xorg input driver. It doesn&#8217;t connect to any physical device, and it never delivers any events. It functions as both a pointer and keyboard device, and may be used as X server&#8217;s core pointer and/or core keyboard. It&#8217;s purpose is to allow X servers pre version 1.4 to operate without a core pointer and/or core keyboard.</p>
<h2>Configuration Details</h2>
<p>Please refer to <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) for general configuration details and for options that can be used with all input drivers. This driver doesn&#8217;t have any configuration options in addition to those.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7). </p>
