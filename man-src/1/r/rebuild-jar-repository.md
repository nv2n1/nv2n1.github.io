---
title: "rebuild-jar-repository(1)"
name: "rebuild-jar-repository"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rebuild-jar-repository/"
description: "rebuild-jar-repository – rebuild a JAR repository"
---

<h2 class="name">NAME</h2>
<p> rebuild-jar-repository &#8211; rebuild a JAR repository </p>
<h2>SYNOPSIS</h2>
<p> <code>rebuild-jar-repository</code> [OPTION]&#8230; DIRECTORY</p>
<h2>DESCRIPTION</h2>
<p> Rebuild a jar repository (built by <code>build-jar-repository</code>) based on the current JVM settings</p>
<h2>OPTIONS</h2>
<p> If no option is specified the default action will be to rebuild with symbolic links </p>
<p> <code>-c, &#8211;copy</code></p>
<dl>
<dt>
<dd> Copy files.</dl>
<p> <code>-h, &#8211;hard</code></p>
<dl>
<dt>
<dd> Create hard links.</dl>
<p> <code>-s, &#8211;soft, &#8211;symbolic</code> Create symbolic links (default).</p>
<h2>EXAMPLES</h2>
<p> <code>rebuild-jar-repository .</code> &#8211; This will update all links created by <code>build-jar-repository</code> in the current working directory. Updated links will be symbolic links. </p>
<p> <code>rebuild-jar-repository -h /tmp</code> &#8211; This will update all links created by <code>build-jar-repository</code> in the /tmp directory. Updated links will be hard links.</p>
<h2>AUTHOR</h2>
<p> Written by the JPackage Project (m[blue]<code><a rel="nofollow" href="http://www.jpackage.org/">http://www.jpackage.org/</a></code>m[]).</p>
<h2>REPORTING BUGS</h2>
<p> Bugs should be reported through Red Hat Bugzilla at m[blue]<code><a rel="nofollow" href="http://bugzilla.redhat.com/">http://bugzilla.redhat.com/</a></code>m[].</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-build-jar-repository/">build-jar-repository</a></code>(1), <code><a href="/docs/linux/man/1-build-classpath/">build-classpath</a></code>(1), </p>
<h2>Index</h2>
