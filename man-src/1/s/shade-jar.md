---
title: "shade-jar(1)"
name: "shade-jar"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shade-jar/"
description: "shade-jar – rename Java namespace in JAR file"
---

<h2 class="name">NAME</h2>
<p> shade-jar &#8211; rename Java namespace in JAR file </p>
<h2>SYNOPSIS</h2>
<p> <code>bin/shade-jar</code> <code>orig-namespace</code> <code>shaded-namespace</code> <code>in-jar</code> <code>out-jar</code></p>
<h2>DESCRIPTION</h2>
<p> <code>shade-jar</code> utility is means for changing JAR file namespaces. Basically it replaces all occurences of given pattern with a given replacement. The replacament is performed on class file names and inside the class files themselves. This is commonly known as <i>shading</i>.</p>
<h2>EXAMPLES</h2>
<p> <code>shade-jar org.apache.log4j com.example.shaded.log4j /usr/share/java/log4j.jar lib/shaded-log4j.jar</code> will replace all occurences of <code>org.apache.log4j</code> in JAR file <code>/usr/share/java/log4j.jar</code> with <code>com.example.shaded.log4j</code> and store the resulting JAR in <code>lib/shaded-log4j.jar</code>.</p>
<h2>BUGS</h2>
<p> Currently only class files are shaded. Resources are not renamed. Neither contents of resource files nor manifests are processed.</p>
<h2>AUTHOR</h2>
<p> Written by Mikolaj Izdebski.</p>
<h2>REPORTING BUGS</h2>
<p> Bugs should be reported through Red Hat Bugzilla at m[blue]<code><a rel="nofollow" href="http://bugzilla.redhat.com/">http://bugzilla.redhat.com/</a></code>m[]. </p>
<h2>Index</h2>
