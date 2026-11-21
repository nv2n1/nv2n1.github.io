---
title: "kjscmd(1)"
name: "kjscmd"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kjscmd/"
description: "kjscmd – KDE KJSEmbed interpreter"
---

<h2>SYNOPSIS</h2>
<dl>
<dt> <code>kjscmd</code> [&#8211;help] [[-e] | [&#8211;exec]] [[-i] | [-interactive]] [[-n] | [-no-kde]] [file]</dt></dl>
<h2>DESCRIPTION</h2>
<p> <code>kjscmd</code></p>
<dd>is a tool for launching KJSEmbed scripts from the command line. It will run the scripts contained in the named <i>file</i> using KJSEmbed. It does not accept &#8211; (stdin) as a <i>file</i>.</dd>
<h2>APPLICATION OPTIONS</h2>
<p> <code>-e</code>,<code>&#8211;exec</code></p>
<dl>
<dt>
</dt><dd> execute script in <i>file</i> without gui support.</dd></dl>
<p> <code>-i</code>,<code>&#8211;interactive</code></p>
<dl>
<dt>
</dt><dd> start interactive <code>kjs</code> interpreter.</dd></dl>
<p> <code>-n</code>,<code>&#8211;no-kde</code></p>
<dl>
<dt>
</dt><dd> start without KDE KApplication support.</dd></dl>
<h2>USAGE</h2>
<p> The most common way to run <code>kjscmd</code> is simply as </p>
<dl>
<dt>
</dt><dd>
<pre>
<code>kjscmd</code><i>file</i>
</pre>
</dd></dl>
<p> If no parameter <i>file</i> is used, it executes a predefined test script that measures the start speed of <code>kjscmd</code>.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-kjs/">kjs</a></i>(1)</p>
<h2>BUGS</h2>
<p> There are probably tons of bugs. Use m[blue]<code>bugs.kde.org</code>m[]<font SIZE="-2">[1]</font> to report them.</p>
<h2>AUTHOR</h2>
<p> <code>Harri Porten</code> &lt;porten [at] kde.org&gt;</p>
<dl>
<dt>
</dt><dd> Author.</dd></dl>
<h2>NOTES</h2>
<dl>
<dt> 1.</dt>
<dd> bugs.kde.org</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://bugs.kde.org">http://bugs.kde.org</a></dd></dl>
</dl>
