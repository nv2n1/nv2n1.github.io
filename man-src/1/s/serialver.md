---
title: "serialver(1)"
name: "serialver"
section: "1"
letter: "s"
url: "/docs/linux/man/1-serialver/"
description: "serialver – Returns the serial version UID for specified classes."
---

<h2>NAME</h2>
<p> serialver &#8211; Returns the serial version UID for specified classes.</p>
<h2>SYNOPSIS</h2>
<pre><code>
serialver[options][classnames]
</code></pre>
<dl>
<dt><i>options</i></p>
<dd> The command-line options. See Options.</p>
<dt><i>classnames</i></p>
<dd> The classes for which the <code>serialVersionUID</code> is to be returned.</dl>
<h2>DESCRIPTION</h2>
<p> The <code>serialver</code> command returns the <code>serialVersionUID</code> for one or more classes in a form suitable for copying into an evolving class. When called with no arguments, the <code>serialver</code> command prints a usage line.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-classpath <i>path-files</i></p>
<dd>
 Sets the search path for application classes and resources. Separate classes and resources with a colon (:).</p>
<dt>-show</p>
<dd>
 Displays a simple user interface. Enter the full class name and press either the <i>Enter</i> key or the <i>Show</i> button to display the <code>serialVersionUID</code>.</p>
<dt>-J<i>option</i></p>
<dd>
 Passes <code>option</code> to the Java Virtual Machine, where option is one of the options described on the reference page for the Java application launcher. For example, <code>-J-Xms48m</code> sets the startup memory to 48 MB. See <a href="/docs/linux/man/1-java/">java</a>(1).</dl>
<h2>NOTES</h2>
<p> The <code>serialver</code> command loads and initializes the specified classes in its virtual machine, and by default, it does not set a security manager. If the <code>serialver</code> command is to be run with untrusted classes, then a security manager can be set with the following option: </p>
<pre>
<code>-J-Djava.security.manager</code>
</pre>
<pre>
</pre>
<p> When necessary, a security policy can be specified with the following option: </p>
<pre>
<code>-J-Djava.security.policy=&lt;policy file&gt;</code>
</pre>
<pre>
</pre>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</p>
<dd> The <code>java.io.ObjectStream</code> class description at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/api/java/io/ObjectStreamClass.html">http://docs.oracle.com/javase/8/docs/api/java/io/ObjectStreamClass.html</a> </p>
</dl>
<h2>Index</h2>
