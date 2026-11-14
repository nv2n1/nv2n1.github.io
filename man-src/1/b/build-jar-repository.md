---
title: "build-jar-repository(1)"
name: "build-jar-repository"
section: "1"
letter: "b"
url: "/docs/linux/man/1-build-jar-repository/"
description: "build-jar-repository – create a symbolic link to a JAR"
---

<h2 class="name">NAME</h2>
<p> build-jar-repository &#8211; create a symbolic link to a JAR </p>
<h2>SYNOPSIS</h2>
<p> <code>build-jar-repository</code> [OPTION]&#8230; DIRECTORY JAR|artifact-coordinates</p>
<h2>DESCRIPTION</h2>
<p> Build a JAR repository in the named directory by copying files or creating symbolic links. The JARs can be identified by their names or Maven artifact coordinates. Artifact coordinates specify Maven artifact and are in format <code>groupId:artifactId[:extension[:classifier]]:version</code>. If extension is omitted then &quot;jar&quot; is used. If classifier is omitted then empty classifier is used. For more information see XMvn Configuration Reference.</p>
<h2>OPTIONS</h2>
<p> If no option is specified the default action will be to create symbolic links </p>
<p> <code>-c, &#8211;copy</code></p>
<dl>
<dt>
<dd> Copy files.</dl>
<p> <code>-h, &#8211;hard</code></p>
<dl>
<dt>
<dd> Create hard links.</dl>
<p> <code>-p, &#8211;preserve-naming</code> Try to preserve the names of the original JAR files (in case of a nested hit the slashes in the path will still be replaced by underscores). Using this option makes any future automated repository rebuild impossible, and implies -c unless specified otherwise. </p>
<p> <code>-s, &#8211;soft, &#8211;symbolic</code> Create symbolic links (default). </p>
<p> <code>&#8211;help</code> Display help text</p>
<h2>EXAMPLES</h2>
<p> <code>build-jar-repository . jndi</code> &#8211; This will create a symbolic link to the jndi JAR in the current working directory. </p>
<p> <code>build-jar-repository -h /tmp log4j</code> &#8211; This will create a hard link to the log4j JAR in /tmp directory. </p>
<p> <code>build-jar-repository -c . org.apache.commons:commons-io</code> &#8211; This will copy commons-io JAR to the current working directory.</p>
<h2>AUTHOR</h2>
<p> Originally written by Nicholas Mailhot and David Walluck.</p>
<h2>REPORTING BUGS</h2>
<p> Bugs should be reported through Red Hat Bugzilla at m[blue]<code><a rel="nofollow" href="http://bugzilla.redhat.com/">http://bugzilla.redhat.com/</a></code>m[].</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-build-classpath/">build-classpath</a></code>(1), <code><a href="/docs/linux/man/1-rebuild-jar-repository/">rebuild-jar-repository</a></code>(1), </p>
<h2>Index</h2>
