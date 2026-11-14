---
title: "mvn_compat_version(7)"
name: "mvn_compat_version"
section: "7"
letter: "m"
url: "/docs/linux/man/7-mvn_compat_version/"
description: "mvn_compat_version – set version(s) for Maven artifact(s)"
---

<p>mvn_compat_version &#8211; set version(s) for Maven artifact(s)</p>
<h2>Synopsis</h2>
<p><code>%mvn_compat_version</code> artifact-coordinates version [version &#8230;]</p>
<h2>Description</h2>
<p><code>mvn_compat_version</code> macro causes instructions for artifact installation to be added to XMvn reactor configuration. It is used to specify versions for Maven artifacts. </p>
<p> Specified artifact coordinates must match at least one artifact. If not then behavior is unspecified. It is possible to specify artifact coordinates matching multiple artifacts, so one call to <code>mvn_compat_version</code> can affect installation of more than one artifact.</p>
<h2>Operands</h2>
<p><code>artifact-coordinates</code></p>
<dl>
<dd>Artifact coordinates specify artifact(s) that this rule applies to. Coordinates are in format <code>groupId:artifactId[:extension[:classifier]][:version]</code>. If extension is specified then version must be specified too. If any part is omitted or equal to empty string then it matches any string. Wildcards and brace expansions are supported in each part. For more information see XMvn Configuration Reference.</dl>
<p> <code>version</code></p>
<dl>
<dd>Strings specifying artifact version. Backreferences are supported in form <code>@n</code>, where <code>n</code> is an integer corresponding to brace in <code>artifact-coordinates</code>.</dl>
<h2>Author</h2>
<p>Written by Stanislav Ochotnicky.</p>
<h2>Reporting Bugs</h2>
<p>Bugs should be reported through Red Hat Bugzilla at m[blue]<code><a rel="nofollow" href="http://bugzilla.redhat.com/">http://bugzilla.redhat.com/</a></code>m[].</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-mvn_alias/">mvn_alias</a></code>(7), <code><a href="/docs/linux/man/7-mvn_build/">mvn_build</a></code>(7), <code><a href="/docs/linux/man/7-mvn_config/">mvn_config</a></code>(7), <code><a href="/docs/linux/man/7-mvn_file/">mvn_file</a></code>(7), <code><a href="/docs/linux/man/7-mvn_package/">mvn_package</a></code>(7), <code><a href="/docs/linux/man/1-xmvn/">xmvn</a></code>(1). </p>
