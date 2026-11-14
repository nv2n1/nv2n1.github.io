---
title: "serialver-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64-debug(1)"
name: "serialver-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64-debug"
section: "1"
letter: "s"
url: "/docs/linux/man/1-serialver-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64-debug/"
description: "serialver – Returns the serial version UID for specified classes."
---

<p>serialver &#8211; Returns the serial version UID for specified classes.</p>
<h2>Synopsis</h2>
<pre><code>serialver</code> [ <i>options</i> ] [ <i>classnames</i> ]</pre>
<dl COMPACT>
<dt><i>options</i></p>
<dd>The command-line options. See Options.</p>
<dt><i>classnames</i></p>
<dd>The classes for which the <code>serialVersionUID</code> is to be returned.</dl>
<h2>Description</h2>
<p>The <code>serialver</code> command returns the <code>serialVersionUID</code> for one or more classes in a form suitable for copying into an evolving class. When called with no arguments, the <code>serialver</code> command prints a usage line.</p>
<h2>Options</h2>
<dl COMPACT>
<dt>-classpath <i>path-files</i></p>
<dd>Sets the search path for application classes and resources. Separate classes and resources with a colon (:).</p>
<dt>-show</p>
<dd>Displays a simple user interface. Enter the full class name and press either the <i>Enter</i> key or the <i>Show</i> button to display the <code>serialVersionUID</code>.</p>
<dt>-J<i>option</i></p>
<dd>Passes <code>option</code> to the Java Virtual Machine, where option is one of the options described on the reference page for the Java application launcher. For example, <code>-J-Xms48m</code> sets the startup memory to 48 MB. See <a href="/docs/linux/man/1-java/">java</a>(1).</dl>
<h2>Notes</h2>
<p>The <code>serialver</code> command loads and initializes the specified classes in its virtual machine, and by default, it does not set a security manager. If the <code>serialver</code> command is to be run with untrusted classes, then a security manager can be set with the following option: </p>
<pre><code>-J-Djava.security.manager</code></pre>
<p>When necessary, a security policy can be specified with the following option: </p>
<pre><code>-J-Djava.security.policy=&lt;policy file&gt;</code></pre>
<h2>See Also</h2>
<dl COMPACT>
<dt>&bull;</p>
<dd><a href="/docs/linux/man/1-policytool/">policytool</a>(1)</p>
<dt>&bull;</p>
<dd>The <code>java.io.ObjectStream</code> class description at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/api/java/io/ObjectStreamClass.html">http://docs.oracle.com/javase/8/docs/api/java/io/ObjectStreamClass.html</a> </p>
</dl>
