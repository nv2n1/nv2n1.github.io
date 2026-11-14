---
title: "alink(1)"
name: "alink"
section: "1"
letter: "a"
url: "/docs/linux/man/1-alink/"
description: "alink – link (reloacatable) object files created by AS"
---

<h2 class="name">NAME</h2>
<p> <code>alink &#8211; link (reloacatable) object files created by AS</code></p>
<h2>SYNTAX</h2>
<p> <code>alink</code> &lt;source file(s)&gt; &lt;target file&gt; [options] </p>
<h2>DESCRIPTION</h2>
<p> alink will one day be a the linker companion tool to asl. It is work in progress, and it won&#8217;t be of much use for most users in its current state. Contact the author (see below) if you want to experiment with it. </p>
<h2>COMMAND-LINE PARAMETERS</h2>
<dl>
<dt><code>-v</code></p>
<dd>
<p> be more verbose while linking. </p>
</dl>
<h2>NATIONAL LANGUAGE SUPPORT</h2>
<p> alink supports national languages in the same way as AS. See the manual page for <a href="/docs/linux/man/1-asl/">asl</a>(1) for maore information about this. </p>
<h2>RETURN CODES</h2>
<p> <code>alink</code> may return with the following codes:</p>
<dl>
<dt><code>0</code></p>
<dd> no errors.</p>
<dt><code>1</code></p>
<dd> incorrect command line parameters.</p>
<dt><code>2</code></p>
<dd> I/O-error.</p>
<dt><code>3</code></p>
<dd> An input file had an incorrect format. </p>
</dl>
<h2>EXAMPLES</h2>
<h2>TIPS</h2>
<p> Calling ALINK without any arguments will print a short help listing all command line parameters. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-asl/">asl</a>(1), <a href="/docs/linux/man/1-pbind/">pbind</a>(1), <a href="/docs/linux/man/1-plist/">plist</a>(1) <a href="/docs/linux/man/1-p2hex/">p2hex</a>(1), <a href="/docs/linux/man/1-p2bin/">p2bin</a>(1) </p>
<h2>BUGS</h2>
<p> In its current (incomplete) state, this program is a bug by itself ;-) </p>
<h2>AUTHOR(S)</h2>
<p> Alfred Arnold (alfred [at] ccac.rwth-aachen.de) </p>
<h2>Index</h2>
