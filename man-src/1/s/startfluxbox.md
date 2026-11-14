---
title: "startfluxbox(1)"
name: "startfluxbox"
section: "1"
letter: "s"
url: "/docs/linux/man/1-startfluxbox/"
description: "startfluxbox – start a fluxbox session"
---

<h2 class="name">NAME</h2>
<p> startfluxbox &#8211; start a fluxbox session </p>
<h2>SYNOPSIS</h2>
<p> <code>startfluxbox</code></p>
<h2>DESCRIPTION</h2>
<p> <code>startfluxbox</code> is a script which runs the file <code>~/.fluxbox/startup</code> If it doesn&#8217;t exist it will be generated. </p>
<p> <code>startfluxbox</code> should be started from your <code>~/.xinitrc</code> if you use startx, or <code>~/.xsession</code> if you run a display manager, like xdm.</p>
<h2>FILES</h2>
<p> <code>~/.fluxbox/startup</code></p>
<dl>
<dt>
<dd> This file contains all commands that should be executed before fluxbox is started. The initial file contains helpful comments for beginners. It also starts fluxbox.</dl>
<h2>EXAMPLES</h2>
<p> The default <code>~/.fluxbox/startup</code> is as follows: </p>
<dl>
<dt>
<dd>
<pre>
#!/bin/sh
#
# fluxbox startup-script:
#
# Lines starting with a '#' are ignored.
# Change your keymap:
xmodmap &quot;$HOME/.Xmodmap&quot;
# Applications you want to run with fluxbox.
# MAKE SURE THAT APPS THAT KEEP RUNNING HAVE AN ''&amp;'' AT THE END.
#
# unclutter -idle 2 &amp;
# wmnd &amp;
# wmsmixer -w &amp;
# idesk &amp;
# And last but not least we start fluxbox.
# Because it is the last app you have to run it with ''exec'' before it.
exec fluxbox
# or if you want to keep a log:
# exec fluxbox -log &quot;$fluxdir/log&quot;
</pre>
</dl>
<p> If you need to start applications after fluxbox, you can change the <code>exec fluxbox</code> line above to something like this: </p>
<dl>
<dt>
<dd>
<pre>
exec fluxbox &amp;
fbpid=$!
sleep 1
{
    xsetroot -cursor_name left_ptr -fg white -bg black &amp;
    ipager &amp;
    gkrellm2 &amp;
} &amp;
wait $fbpid
</pre>
</dl>
<p> So xsetroot, ipager, and gkrellm2 will all be started after fluxbox, after giving fluxbox 1 second to startup. </p>
<p> For more details on what else you can do in this script, see <code><a href="/docs/linux/man/1-sh/">sh</a>(1)</code>, or the documentation for your shell.</p>
<h2>AUTHORS</h2>
<p> The author of <code><a href="/docs/linux/man/1-startfluxbox/">startfluxbox</a>(1)</code> is Han Boetes &lt;han at fluxbox.org&gt; </p>
<p> This manpage was converted to asciidoc format by Jim Ramsay &lt;i.am at jimramsay.com&gt; for fluxbox-1.1.2</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1)</p>
<h2>AUTHOR</h2>
<p> <code>Jim Ramsay</code> &lt;i.am [at] jimramsay.com&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>Index</h2>
