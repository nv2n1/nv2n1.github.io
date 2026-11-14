---
title: "serialver-java-1(1)"
name: "serialver-java-1"
section: "1"
letter: "s"
url: "/docs/linux/man/1-serialver-java-1/"
description: "serialver – The Serial Version Command"
---

<h2>Name</h2>
<p> serialver &#8211; The Serial Version Command </p>
<p> The <code>serialver</code> command returns the <i>serialVersionUID</i>. </p>
<h2>SYNOPSIS</h2>
<pre><code>
serialver[options][classnames]
</code></pre>
<dl>
<dt>
<dd>
<dl>
<dt>options</p>
<dd> Command-line options, as specified in this document.</p>
<dt>classnames</p>
<dd> One or more class names</dl>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>serialver</code> returns the <i>serialVersionUID</i> for one or more classes in a form suitable for copying into an evolving class. When invoked with no arguments it prints a usage line. </p>
<h2>OPTIONS</h2>
<dl>
<dt>
<dd>
<dl>
<dt>-classpath &lt;directories and zip/jar files separated by :&gt;</p>
<dd> Set search path for application classes and resources.</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>-show</p>
<dd> Displays a simple user interface. Enter the full class name and press either the Enter key or the Show button to display the serialVersionUID.</p>
<dt>-Joption</p>
<dd> Pass <i>option</i> to the Java virtual machine, where <i>option</i> is one of the options described on the reference page for the <a href="/docs/linux/man/1-java/">java</a>(1). For example, <code>-J-Xms48m</code> sets the startup memory to 48 megabytes.</dl>
</dl>
<h2>NOTES</h2>
<p> The <code>serialver</code> command loads and initializes the specified classes in its virtual machine, and by default, it does not set a security manager. If <code>serialver</code> is to be run with untrusted classes, a security manager can be set with the following option: </p>
<p> <i>-J-Djava.security.manager</i> </p>
<p> and, if necessary, a security policy can be specified with the following option: </p>
<p> <i>-J-Djava.security.policy=&lt;policy file&gt;</i> </p>
<h2>SEE ALSO</h2>
<p> <i>java.io.ObjectStreamClass</i> @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/api/java/io/ObjectStreamClass.html">http://docs.oracle.com/javase/7/docs/api/java/io/ObjectStreamClass.html</a> </p>
<p>&nbsp;<wbr> </p>
<h2>Index</h2>
