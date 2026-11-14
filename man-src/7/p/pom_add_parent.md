---
title: "pom_add_parent(7)"
name: "pom_add_parent"
section: "7"
letter: "p"
url: "/docs/linux/man/7-pom_add_parent/"
description: "pom_add_parent – add parent POM reference to POM file"
---

<p>pom_add_parent &#8211; add parent POM reference to POM file</p>
<h2>Synopsis</h2>
<p><code>%pom_add_parent</code> groupId*:*artifactId[*:*version] [POM-location]</p>
<h2>Description</h2>
<p>This macro patches specified POM file adding a reference to parent POM with specified groupId, artifactId and version. </p>
<p> groupId and artifactId are identifiers of Maven group and artifact of the POM to be referenced as parent POM. They must be specified. If version is not specified then default value of &quot;any&quot; is used. </p>
<p> POM location can be either a full path to the POM file, or a path to the directory containing <code>pom.xml</code>. If POM location is not given then <code>pom.xml</code> from current working directory is used.</p>
<h2>Examples</h2>
<p><code>%pom_add_parent foo:bar baz</code> &#8211; this call adds reference to parent POM artifact <code>foo:bar</code> to <code>baz/pom.xml</code> file.</p>
<h2>Bugs</h2>
<p>If specified POM has already a reference to parent POM this macro will not alter or remove it. Instead a second reference will be added. This is usually not the expected behavior as it results in creating invalid POM file. In order to replace existing parent POM reference, <code><a href="/docs/linux/man/7-pom_set_parent/">pom_set_parent</a></code>(7) should be used instead.</p>
<h2>Author</h2>
<p>Written by Mikolaj Izdebski.</p>
<h2>Reporting Bugs</h2>
<p>Bugs should be reported through Red Hat Bugzilla at m[blue]<code><a rel="nofollow" href="http://bugzilla.redhat.com/">http://bugzilla.redhat.com/</a></code>m[].</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-pom_add_dep/">pom_add_dep</a></code>(7), <code><a href="/docs/linux/man/7-pom_add_plugin/">pom_add_plugin</a></code>(7), <code><a href="/docs/linux/man/7-pom_disable_module/">pom_disable_module</a></code>(7), <code><a href="/docs/linux/man/7-pom_remove_dep/">pom_remove_dep</a></code>(7), <code><a href="/docs/linux/man/7-pom_remove_parent/">pom_remove_parent</a></code>(7), <code><a href="/docs/linux/man/7-pom_remove_plugin/">pom_remove_plugin</a></code>(7), <code><a href="/docs/linux/man/7-pom_set_parent/">pom_set_parent</a></code>(7), <code><a href="/docs/linux/man/7-pom_xpath_inject/">pom_xpath_inject</a></code>(7), <code><a href="/docs/linux/man/7-pom_xpath_remove/">pom_xpath_remove</a></code>(7), <code><a href="/docs/linux/man/7-pom_xpath_replace/">pom_xpath_replace</a></code>(7), <code><a href="/docs/linux/man/7-pom_xpath_set/">pom_xpath_set</a></code>(7). </p>
