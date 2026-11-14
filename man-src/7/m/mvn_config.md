---
title: "mvn_config(7)"
name: "mvn_config"
section: "7"
letter: "m"
url: "/docs/linux/man/7-mvn_config/"
description: "mvn_config – specify custom XMvn configuration option"
---

<p>mvn_config &#8211; specify custom XMvn configuration option</p>
<h2>Synopsis</h2>
<p><code>%mvn_config</code> key value</p>
<h2>Description</h2>
<p><code>mvn_config</code> macro causes custom configuration options to be added to XMvn reactor configuration.</p>
<h2>Operands</h2>
<p><code>key</code></p>
<dl>
<dd>Configuration option key (unique name). This is XPath-like address of XML configuration node &#8211; list of XML nodes delimited by <i>/</i>. If unknown key is given, behavior is unspecified. For list of available keys see XMvn Configuration Reference.</dl>
<p> <code>value</code></p>
<dl>
<dd>Value of specified option. Must be either plain text or XML content. If value format is inappropriate for particular option, behavior is unspecified.</dl>
<h2>Author</h2>
<p>Originally written by Mikolaj Izdebski. Versions 3.0.0 and later were written by Stanislav Ochotnicky.</p>
<h2>Reporting Bugs</h2>
<p>Bugs should be reported through Red Hat Bugzilla at m[blue]<code><a rel="nofollow" href="http://bugzilla.redhat.com/">http://bugzilla.redhat.com/</a></code>m[].</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-mvn_alias/">mvn_alias</a></code>(7), <code><a href="/docs/linux/man/7-mvn_build/">mvn_build</a></code>(7), <code><a href="/docs/linux/man/7-mvn_compat_version/">mvn_compat_version</a></code>(7), <code><a href="/docs/linux/man/7-mvn_file/">mvn_file</a></code>(7), <code><a href="/docs/linux/man/7-mvn_package/">mvn_package</a></code>(7), <code><a href="/docs/linux/man/1-xmvn/">xmvn</a></code>(1). </p>
