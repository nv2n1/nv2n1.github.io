---

title: "kawa(1)"
name: "kawa"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kawa/"
description: "kawa – Scheme language implemented using on a Java VM"
---

<p> kawa &#8211; Scheme language implemented using on a Java VM </p>
<h2>SYNOPSIS</h2>
<p> <code>kawa</code> <i>[options]</i><br/>
 <code>java kawa.repl</code> <i>[options]</i></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>kawa</code> package, a Scheme dialect written completely in the Java language. Scheme forms are compiled into Java bytecodes for efficiency. </p>
<p> Scheme is a high-level non-pure functional language in the Lisp family, with lexical scoping dynamically-types. The Kawa dialect of Scheme contains hooks to access and control Java objects. </p>
<p> Using the <code>kawa</code> script is equivalent to invoking an interpreter of the Java language on the <code>kawa.repl</code> class. </p>
<p> This manual page is just a quick synopsis. For more information, read the <code>kawa</code> manual &#8211; see below. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-e </code><i>expression</i></dt>
<dd> Evaluate the <i>expression</i>.</dd>
<dt><code>-c </code><i>expression</i></dt>
<dd> Evaluate the <i>expression</i>, but does not cause the start-up file <i>~/.kawarc.scm</i> to be read.</dd>
<dt><code>-f </code><i>filename</i></dt>
<dd> Read and evaluate Scheme commands from the <i>filename</i>.</dd>
<dt><code>-s</code></dt>
<dd> Enter an interactive read-evaluate-print command loop.</dd>
<dt><code>-w</code></dt>
<dd> Enter an interactive read-evaluate-print in a new top-level window.</dd>
<dt><code>-C </code><i>filename</i></dt>
<dd> Compile <i>filename</i> to one or more Java class files. See the Kawa manual for details. If no options are specified, it is equivalent to <code>-s</code>.<br/>
 GNU <code><a href="/docs/linux/man/3-readline/">readline</a>(3)</code> can normally be used to edit commands. </dd>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>/usr/bin/kawa</code></dt>
<dd> The <code>kawa</code> executable, which starts a <code>java</code> interpreter.</dd>
<dt><code>~/.kawarc.scm</code></dt>
<dd> Commands that are executed when <code>kawa</code> is started.</dd></dl>
<h2>AUTHOR</h2>
<p> Per Bothner &lt;per [at] bothner.com&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code>info kawa</code> &#8211; the complete Kawa manual. <i><a rel="nofollow" href="http://www.gnu.org/software/kawa/">http://www.gnu.org/software/kawa/</a></i> &#8211; the <code>kawa</code> home page, based on the same Kawa manual. <code>qexo(1)</code> &#8211; an implementation of XQuery using the same engine. </p>
