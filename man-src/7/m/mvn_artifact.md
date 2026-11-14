---
title: "mvn_artifact(7)"
name: "mvn_artifact"
section: "7"
letter: "m"
url: "/docs/linux/man/7-mvn_artifact/"
description: "mvn_artifact – request installation of Maven artifact"
---

<p>mvn_artifact &#8211; request installation of Maven artifact</p>
<h2>Synopsis</h2>
<p><code>%mvn_artifact</code> model [artifact-file] <code>%mvn_artifact</code> artifact-coordinates artifact-file</p>
<h2>Description</h2>
<p><code>mvn_artifact</code> macro marks specified Maven artifact to be installed by further call to <code>mvn_install</code>. Multiple calls to <code>mvn_artifact</code> and/or <code>mvn_build</code> can be made to request installation of multiple artifacts.</p>
<h2>Operands</h2>
<p><code>model</code></p>
<dl>
<dd>Path to raw project object model (POM) file to be associated and installed with artifact.</dl>
<p> <code>artifact-file</code></p>
<dl>
<dd>Path to file to be used as artifact file. If omitted then no artifact file is installed.</dl>
<p> <code>artifact-coordinates</code></p>
<dl>
<dd>Artifact coordinates specify artifact to be installed. If specified then no model file is installed with artifact. Coordinates are in format <code>groupId:artifactId[:extension[:classifier]]:version</code>. If extension is omitted then &quot;jar&quot; is used. If classifier is omitted then empty classifier is used. For more information see XMvn Configuration Reference.</dl>
<h2>Author</h2>
<p>Written by Michal Srb.</p>
<h2>Reporting Bugs</h2>
<p>Bugs should be reported through Red Hat Bugzilla at m[blue]<code><a rel="nofollow" href="http://bugzilla.redhat.com/">http://bugzilla.redhat.com/</a></code>m[].</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-mvn_build/">mvn_build</a></code>(7), <code><a href="/docs/linux/man/7-mvn_install/">mvn_install</a></code>(7). </p>
