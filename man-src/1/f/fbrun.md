---
title: "fbrun(1)"
name: "fbrun"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fbrun/"
description: "fbrun – display run dialog window"
---

<h2 class="name">NAME</h2>
<p> fbrun &#8211; display run dialog window </p>
<h2>SYNOPSIS</h2>
<p> <code>fbrun</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code><a href="/docs/linux/man/1-fbrun/">fbrun</a>(1)</code> is basically equivalent to the &#8220;Run&#8230;&#8221; dialog in other desktop environments. This means that it is an easy way to start a program that isn&#8217;t contained in the menu (or needs a special set of parameters for this particular invocation). </p>
<p> Pressing &#8220;Enter&#8221; will close the window and execute the command in your present <code>$SHELL</code>. Pressing &#8220;Esc&#8221; will close the window and does not execute anything. </p>
<p> Another way fbrun can be useful is to be called from the menu with a preloaded command line that you can edit and then execute. An example might be sshing to a very long host name with lots of options of which one changes all the time. In this case, you could add an entry for fbrun to your menu that contains all the options and the host name. When you use said entry, you could edit the line as necessary and execute it.</p>
<h2>OPTIONS</h2>
<p> <code>-title</code> <i>title</i></p>
<dl>
<dt>
<dd> Set title</dl>
<p> <code>-text</code> <i>text</i></p>
<dl>
<dt>
<dd> Text input</dl>
<p> <code>-w</code> <i>width</i></p>
<dl>
<dt>
<dd> Window width in pixels</dl>
<p> <code>-h</code> <i>height</i></p>
<dl>
<dt>
<dd> Window height in pixels</dl>
<p> <code>-display</code> <i>display</i></p>
<dl>
<dt>
<dd> Display name, defaults to <code>$DISPLAY</code></dl>
<p> <code>-pos</code> <i>x</i> <i>y</i></p>
<dl>
<dt>
<dd> Window position in pixels</dl>
<p> <code>-nearmouse</code></p>
<dl>
<dt>
<dd> Position the window under the mouse cursor</dl>
<p> <code>-fg</code> <i>color</i></p>
<dl>
<dt>
<dd> Foreground text color. The default is <code>black</code></dl>
<p> <code>-bg</code> <i>color</i></p>
<dl>
<dt>
<dd> Background color. The default is <code>white</code></dl>
<p> <code>-font</code> <i>name</i></p>
<dl>
<dt>
<dd> Text font name</dl>
<p> <code>-hf</code> <i>filename</i></p>
<dl>
<dt>
<dd> History file to load. The default is <code>~/.fluxbox/fbrun_history</code>.</dl>
<p> <code>-help</code></p>
<dl>
<dt>
<dd> Show this help</dl>
<h2>EXAMPLE</h2>
<dl>
<dt>
<dd>
<pre>
fbrun -fg black -bg white -text xterm -title &quot;run xterm&quot;
</pre>
</dl>
<h2>AUTHORS</h2>
<p> This manpage was originally written by Bastian Kleineidam &lt;calvin at debian.org&gt; for the Debian distribution of fluxbox (but may be used by others). </p>
<p> It was then converted to asciidoc format by Jim Ramsay &lt;i.am at jimramsay.com&gt; for fluxbox-1.1.2</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1)</p>
<h2>AUTHOR</h2>
<p> <code>Jim Ramsay</code> &lt;i.am [at] jimramsay.com&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>Index</h2>
