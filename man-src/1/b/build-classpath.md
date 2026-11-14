---
title: "build-classpath(1)"
name: "build-classpath"
section: "1"
letter: "b"
url: "/docs/linux/man/1-build-classpath/"
description: "build-classpath – build a Java CLASSPATH"
---

<h2 class="name">NAME</h2>
<p> build-classpath &#8211; build a Java CLASSPATH </p>
<h2>SYNOPSIS</h2>
<p> <code>build-classpath</code> JAR|artifact-coordinates [JAR|artifact-coordinates &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Small utility to build a Java CLASSPATH with the named JARs or Maven artifact coordinates. Artifact coordinates specify Maven artifact and are in format <code>groupId:artifactId[:extension[:classifier]]:version</code>. If extension is omitted then &quot;jar&quot; is used. If classifier is omitted then empty classifier is used. For more information see XMvn Configuration Reference. The CLASSPATH is returned to standard output.</p>
<h2>EXAMPLES</h2>
<p> <code>build-classpath junit xerces-j2 wsdl4j</code> &#8211; this will return a string to standard out that is a valid CLASSPATH containing junit, xerces-j2, and wsdl4j JARs. </p>
<p> <code>build-classpath log4j:log4j org.apache.commons:commons-io</code> &#8211; this will return a string to standard out that is a valid CLASSPATH containing log4j and commons-io JARs. </p>
<p> <code>build-classpath com.google.inject:guice::no_aop:</code> &#8211; this will return a string to standard out that is a valid CLASSPATH containing google-guice JAR with classifier no_aop.</p>
<h2>AUTHOR</h2>
<p> Originally written by David Walluck.</p>
<h2>REPORTING BUGS</h2>
<p> Bugs should be reported through Red Hat Bugzilla at m[blue]<code><a rel="nofollow" href="http://bugzilla.redhat.com/">http://bugzilla.redhat.com/</a></code>m[].</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-build-jar-repository/">build-jar-repository</a></code>(1), <code><a href="/docs/linux/man/1-rebuild-jar-repository/">rebuild-jar-repository</a></code>(1), </p>
<h2>Index</h2>
