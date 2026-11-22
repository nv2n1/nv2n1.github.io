---

title: "kjs(1)"
name: "kjs"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kjs/"
description: "kjs – KDE ECMAScript compatible interpreter"
---

<p> kjs &#8211; KDE ECMAScript compatible interpreter </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>kjs</code> [[&#8211;help] | [-help] | [-h]] [[-e<i>&nbsp;<wbr>statement</i>]] [<i>script</i>]</dt></dl>
<h2>DESCRIPTION</h2>
<p> <code>kjs</code></p>
<dd>is KDE ECMAScript/JavaScript engine.</dd>
<h2>APPLICATION OPTIONS</h2>
<p> <code>&#8211;help</code>,<code>-help</code>,<code>-h</code></p>
<dl>
<dt>
</dt><dd> Show <code>kjscmd</code> usage.</dd></dl>
<p> <code>-e</code><i> statement</i></p>
<dl>
<dt>
</dt><dd> Executes the statement and exits. For example: </dd>
<dl>
<dt>
</dt><dd>
<pre>
<code>kjs</code> -e &quot;print('hello world')&quot;
</pre>
</dd></dl>
</dl>
<p> <i>script</i></p>
<dl>
<dt>
</dt><dd> Executes the statements included in file <i>script</i>.</dd></dl>
<h2>USAGE</h2>
<p> <code>kjs</code><i>file</i>, as many other interpreters, when called without parameters uses a line editor to enter statements, showing the prompt </p>
<dl>
<dt>
</dt><dd>
<pre>
JS&gt;
</pre>
</dd></dl>
<p> To exit the line editor type <code>quit()</code> or press <code>Ctrl+D</code>.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-kjs/">kjs</a></i>(1)</p>
<h2>BUGS</h2>
<p> There are probably tons of bugs. Use m[blue]<code>bugs.kde.org</code>m[][1] to report them.</p>
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
