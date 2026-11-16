---
title: "kjs5(1)"
name: "kjs5"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kjs5/"
description: "kjs5 – KDE ECMAScript compatible interpreter"
---

<h2 class="name">NAME</h2>
<p> kjs5 &#8211; KDE ECMAScript compatible interpreter </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>kjs5</code> [[&#8211;help] | [-help] | [-h]] [[&#8211;version] | [-version] | [-v]] [[-e<i>&nbsp;<wbr>statement</i>]] [<i>script</i>]</dt></dl>
<h2>DESCRIPTION</h2>
<p> <code>kjs</code></p>
<dd>is KDE ECMAScript/JavaScript engine.</dd>
<h2>APPLICATION OPTIONS</h2>
<p> <code>&#8211;help</code>,<code>-help</code>,<code>-h</code></p>
<dl>
<dt>
</dt><dd> Show <code>kjs5</code> usage.</dd></dl>
<p> <code>&#8211;version</code>,<code>-version</code>,<code>-v</code></p>
<dl>
<dt>
</dt><dd> Show <code>kjs5</code> version.</dd></dl>
<p> <code>-e</code><i> statement</i></p>
<dl>
<dt>
</dt><dd> Executes the statement and exits. For example: </dd>
<dl>
<dt>
</dt><dd>
<pre>
<code>kjs5</code> -e &quot;print('hello world')&quot;
</pre>
</dd></dl>
</dl>
<p> <i>script</i></p>
<dl>
<dt>
</dt><dd> Executes the statements included in file <i>script</i>.</dd></dl>
<h2>USAGE</h2>
<p> <code>kjs5</code><i>file</i>, as many other interpreters, when called without parameters uses a line editor to enter statements, showing the prompt </p>
<dl>
<dt>
</dt><dd>
<pre>
JS&gt;
</pre>
</dd></dl>
<p> To exit the line editor type <code>quit()</code> or press <code>Ctrl+D</code>.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-kjscmd5/">kjscmd5</a></i>(1)</p>
<h2>BUGS</h2>
<p> Please use m[blue]<code>KDE&#8217;s bugtracker</code>m[]<font SIZE="-2">[1]</font> to report bugs.</p>
<h2>AUTHOR</h2>
<p> <code>Harri Porten</code> &lt;porten [at] kde.org&gt;</p>
<dl>
<dt>
</dt><dd> Author.</dd></dl>
<h2>NOTES</h2>
<dl>
<dt> 1.</dt>
<dd> KDE&#8217;s bugtracker</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://bugs.kde.org">http://bugs.kde.org</a></dd></dl>
</dl>
<h2>Index</h2>
