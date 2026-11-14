---
title: "find-jar(1)"
name: "find-jar"
section: "1"
letter: "f"
url: "/docs/linux/man/1-find-jar/"
description: "find-jar – find extension JAR or directory"
---

<h2 class="name">NAME</h2>
<p> find-jar &#8211; find extension JAR or directory </p>
<h2>SYNOPSIS</h2>
<p> <code>find-jar</code> element</p>
<h2>DESCRIPTION</h2>
<p> The <code>find-jar</code> command tests the resolution of a given element. If successful it will return a JAR file or a directory. </p>
<p> This command is solely intended for testing resolution and should not be used in scripts. Even for single-element classpath building <code>build-classpath</code> is preferred since single-element searches can produce multiple file results when resolving into a directory.</p>
<h2>EXAMPLES</h2>
<p> <code>find-jar xpp3</code> will print <code>/usr/share/java/xpp3.jar</code> on standard output. </p>
<p> <code>find-jar javamail</code> will print <code>/usr/share/java/javamail</code> on standard output.</p>
<h2>REPORTING BUGS</h2>
<p> Bugs should be reported through Red Hat Bugzilla at m[blue]<code><a rel="nofollow" href="http://bugzilla.redhat.com/">http://bugzilla.redhat.com/</a></code>m[].</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-build-classpath/">build-classpath</a></code>(1), <code><a href="/docs/linux/man/1-build-jar-repository/">build-jar-repository</a></code>(1), <code><a href="/docs/linux/man/1-xmvn-resolve/">xmvn-resolve</a></code>(1). </p>
<h2>Index</h2>
