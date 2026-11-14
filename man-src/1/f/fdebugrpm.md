---
title: "fdebugrpm(1)"
name: "fdebugrpm"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fdebugrpm/"
description: "fdebugrpm – install missing debuginfo packages"
---

<h2 class="name">NAME</h2>
<p> fdebugrpm &#8211; install missing debuginfo packages </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>fdebugrpm</code> [<i>options</i>] {<i>program</i>&nbsp;<wbr><i>arg</i>&nbsp;<wbr>&#8230; | <i>pid</i>&#8230; | <i>core-file</i>&nbsp;<wbr>[&nbsp;<wbr><i>core-executable</i>&nbsp;<wbr>]&#8230; }</dl>
<h2>DESCRIPTION</h2>
<p> <code>fdebugrpm</code></p>
<dd>is a bash script that uses the utility <a href="/docs/linux/man/1-fdebuginfo/">fdebuginfo</a>(1) to determine any missing Debug Information, allowing the user to install the missing debuginfo packages. User needs to be in the <a href="/docs/linux/man/5-sudoers/">sudoers</a>(5) file.</p>
<h3>Standard Frysk Options</h3>
<p> <code>-exe</code></p>
<dl>
<dt>
<dd> The full path of the executable to read.</dl>
<p> <code>-noexe</code></p>
<dl>
<dt>
<dd> Do not attempt to read the corresponding executable when loading a core file.</dl>
<p> <code>-sysroot </code><i>directory</i></p>
<dl>
<dt>
<dd> The system root directory under which all executables, libraries, and source are located.</dl>
<p> <code>-debug </code><i>class</i><code>=</code><i>level</i><code>&#8230;</code></p>
<dl>
<dt>
<dd> Set internal debug-tracing of the specified Java <i>class</i> to <i>level</i> (level can be NONE, INFO, WARNING, FINE, and FINEST). If the <i>level</i> is absent, FINE is assumed; if the <i>class</i> is absent, the global level is set.</dl>
<h2>EXAMPLE</h2>
<dl>
<dt>
<dd>
<pre>
fdebugrpm 1234
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-frysk/">frysk</a>(7) <a href="/docs/linux/man/1-fdebuginfo/">fdebuginfo</a>(1)</p>
<h2>BUGS</h2>
<p> Report bugs to m[blue]<code><a rel="nofollow" href="http://sourceware.org/frysk">http://sourceware.org/frysk</a></code>m[] </p>
<h2>Index</h2>
