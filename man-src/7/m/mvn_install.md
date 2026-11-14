---
title: "mvn_install(7)"
name: "mvn_install"
section: "7"
letter: "m"
url: "/docs/linux/man/7-mvn_install/"
description: "mvn_install – install Maven artifacts"
---

<p>mvn_install &#8211; install Maven artifacts</p>
<h2>Synopsis</h2>
<p><code>%mvn_install</code> [-X] [-J directory]</p>
<h2>Description</h2>
<p><code>mvn_install</code> macro installs Maven artifacts into <code>%buildroot</code>. </p>
<p> Specification of artifacts to be installed is taken from <code>.xmvn-reactor</code> file. This file can be populated using <code>mvn_build</code> and/or <code>mvn_artifact</code> macros. </p>
<p> Specification how artifacts should be installed is taken from installer settings section in XMvn configuration. See XMvn Configuration Reference for more information. Macros <code><a href="/docs/linux/man/7-mvn_alias/">mvn_alias</a></code>(7), <code><a href="/docs/linux/man/7-mvn_build/">mvn_build</a></code>(7), <code><a href="/docs/linux/man/7-mvn_compat_version/">mvn_compat_version</a></code>(7), <code><a href="/docs/linux/man/7-mvn_config/">mvn_config</a></code>(7), <code><a href="/docs/linux/man/7-mvn_file/">mvn_file</a></code>(7) and <code><a href="/docs/linux/man/7-mvn_package/">mvn_package</a></code>(7) are capable of writing configuration that can affect behavior of <code>mvn_install</code>.</p>
<h2>Options</h2>
<p><code>-X</code></p>
<dl>
<dd>Enable debugging output. This option causes XMvn installer to write verbose debugging information to standard output.</dl>
<p> <code>-J</code> directory</p>
<dl>
<dd>Specify alternative API documentation directory. By default API documentation is searched for in <code>target/site/apidocs</code> directory. The <code>-J</code> option allows to override this default location.</dl>
<h2>Author</h2>
<p>Written by Mikolaj Izdebski.</p>
<h2>Reporting Bugs</h2>
<p>Bugs should be reported through Red Hat Bugzilla at m[blue]<code><a rel="nofollow" href="http://bugzilla.redhat.com/">http://bugzilla.redhat.com/</a></code>m[].</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-mvn_alias/">mvn_alias</a></code>(7), <code><a href="/docs/linux/man/7-mvn_artifact/">mvn_artifact</a></code>(7), <code><a href="/docs/linux/man/7-mvn_build/">mvn_build</a></code>(7), <code><a href="/docs/linux/man/7-mvn_compat_version/">mvn_compat_version</a></code>(7), <code><a href="/docs/linux/man/7-mvn_config/">mvn_config</a></code>(7), <code><a href="/docs/linux/man/7-mvn_file/">mvn_file</a></code>(7), <code><a href="/docs/linux/man/7-mvn_package/">mvn_package</a></code>(7), <code><a href="/docs/linux/man/1-xmvn/">xmvn</a></code>(1). </p>
