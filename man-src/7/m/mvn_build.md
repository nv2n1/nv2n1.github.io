---
title: "mvn_build(7)"
name: "mvn_build"
section: "7"
letter: "m"
url: "/docs/linux/man/7-mvn_build/"
description: "mvn_build – build Maven project with XMvn"
---

<p>mvn_build &#8211; build Maven project with XMvn</p>
<h2>Synopsis</h2>
<p><code>%mvn_build</code> [options] [&#8211; Maven-arguments]</p>
<h2>Description</h2>
<p><code>mvn_build</code> macro builds Maven project by calling XMvn and generates reactor structure information to be used by <code>mvn_install</code>. </p>
<p> By default Maven phase <code>verify</code> and goal <code>javadoc:aggregate</code> are executed, as well as some additional XMvn-specific goals or phases. If <code>-f</code> is specified then phase <code>package</code> is executed instead of <code>verify</code>. If <code>-j</code> is given then goal <code>javadoc:aggregate</code> is skipped. </p>
<p> Any arguments after <code>&#8212;</code> are passed directly to XMvn. See <code><a href="/docs/linux/man/1-xmvn/">xmvn</a>(1)</code> for more information on availability of XMvn options.</p>
<h2>Options</h2>
<p><code>-d, &#8211;xmvn-debug</code></p>
<dl>
<dd>Enable XMvn debugging output. This option causes XMvn to write verbose debugging information to standard output. Debugging information includes at least details about artifact resolution from system repositories.</dl>
<p> <code>-f, &#8211;force</code></p>
<dl>
<dd>Skip compilation and execution of unit and integration tests, as well as resolution of build dependencies with scope <code>test</code>. This option causes Maven phase <code>package</code> to be executed instead of default phase <code>verify</code>, defines property <code>maven.test.skip=true</code> which disables compilation and execution of tests and causes XMvn to remove any project dependencies with scope <code>test</code>.</dl>
<p> <code>-i, &#8211;skip-install</code></p>
<dl>
<dd>Skip artifact installation. This option disables generation of reactor structure information so that future calls to <code>mvn_install</code> will not result in installation of artifacts produced in current Maven reactor.</dl>
<p> <code>-j, &#8211;skip-javadoc</code></p>
<dl>
<dd>Skip javadoc generation. This option skips running Maven Javadoc Plugin. Useful for packages which don&#8217;t want to produce Java API documentation.</dl>
<p> <code>-s, &#8211;singleton</code></p>
<dl>
<dd>Enable singleton packaging (one artifact per package). This option causes artifacts with identical <code>artifactId</code> to be installed as part of the same subpackage. This behavior can be further customized by adding more specific packaging rules with <code>mvn_package</code>.</dl>
<p> <code>-X, &#8211;debug</code></p>
<dl>
<dd>Enable Maven debugging output. Implies <code>-d</code>. This option causes Maven to write verbose debugging information to standard output.</dl>
<h2>Environment</h2>
<p><code>xmvn_bootstrap</code></p>
<dl>
<dd>Run XMvn in online mode. If <code>xmvn_bootstrap</code> RPM macro is defined to any value then XMvn is ran in online mode. Otherwise XMvn is ran in offline mode. Online mode of XMvn allows missing dependency artifacts to be fetched from remote repositories. This behavior is mostly useful when bootstrapping new packages, which dependecies have not yet been packaged.</dl>
<h2>Author</h2>
<p>Originally written by Mikolaj Izdebski. Versions 3.0.0 and later were written by Stanislav Ochotnicky.</p>
<h2>Reporting Bugs</h2>
<p>Bugs should be reported through Red Hat Bugzilla at m[blue]<code><a rel="nofollow" href="http://bugzilla.redhat.com/">http://bugzilla.redhat.com/</a></code>m[].</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-mvn_alias/">mvn_alias</a></code>(7), <code><a href="/docs/linux/man/7-mvn_compat_version/">mvn_compat_version</a></code>(7), <code><a href="/docs/linux/man/7-mvn_config/">mvn_config</a></code>(7), <code><a href="/docs/linux/man/7-mvn_file/">mvn_file</a></code>(7), <code><a href="/docs/linux/man/7-mvn_package/">mvn_package</a></code>(7), <code><a href="/docs/linux/man/1-xmvn/">xmvn</a></code>(1). </p>
