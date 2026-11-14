---
title: "pom_add_dep(7)"
name: "pom_add_dep"
section: "7"
letter: "p"
url: "/docs/linux/man/7-pom_add_dep/"
description: "pom_add_dep – add dependency to POM file"
---

<p>pom_add_dep &#8211; add dependency to POM file</p>
<h2>Synopsis</h2>
<p><code>%pom_add_dep</code> groupId*:*artifactId[<code>:*version[</code>:*scope]] [POM-location] [extra-XML] </p>
<p> <code>%pom_add_dep_mgmt</code> groupId:articId[<code>:*version[</code>:*scope]] [POM-location] [extra-XML]</p>
<h2>Description</h2>
<p>These macros patch specified POM file adding a dependency on given version of artifactId from groupId, with given scope (if any). <code>pom_add_dep</code> adds the dependency to <code>&lt;dependencies&gt;</code> XML node, while <code>pom_add_dep_mgmt</code> adds it to <code>dependencyManagement</code>. </p>
<p> groupId and artifactId are identifiers of Maven artifact on which dependency is to be added. They must be specified. If version is not specified then default value of &quot;any&quot; is used. If scope is not specified then no scope is defined (Maven defaults to &quot;compile&quot; in this case). </p>
<p> POM location can be either a full path to the POM file, or a path to the directory containing <code>pom.xml</code>. If POM location is not given then <code>pom.xml</code> from current working directory is used. </p>
<p> Extra XML is additional XML code to be added into the <code>&lt;dependency&gt;</code> node. This parameter can be ommited, in which case no extra XML is appended.</p>
<h2>Examples</h2>
<p><code>%pom_add_dep foo:bar baz</code> &#8211; this call adds dependency on artifact <code>foo:bar</code> to <code>baz/pom.xml</code> file.</p>
<h2>Author</h2>
<p>Written by Mikolaj Izdebski.</p>
<h2>Reporting Bugs</h2>
<p>Bugs should be reported through Red Hat Bugzilla at m[blue]<code><a rel="nofollow" href="http://bugzilla.redhat.com/">http://bugzilla.redhat.com/</a></code>m[].</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-pom_add_parent/">pom_add_parent</a></code>(7), <code><a href="/docs/linux/man/7-pom_add_plugin/">pom_add_plugin</a></code>(7), <code><a href="/docs/linux/man/7-pom_disable_module/">pom_disable_module</a></code>(7), <code><a href="/docs/linux/man/7-pom_remove_dep/">pom_remove_dep</a></code>(7), <code><a href="/docs/linux/man/7-pom_remove_parent/">pom_remove_parent</a></code>(7), <code><a href="/docs/linux/man/7-pom_remove_plugin/">pom_remove_plugin</a></code>(7), <code><a href="/docs/linux/man/7-pom_set_parent/">pom_set_parent</a></code>(7), <code><a href="/docs/linux/man/7-pom_xpath_inject/">pom_xpath_inject</a></code>(7), <code><a href="/docs/linux/man/7-pom_xpath_remove/">pom_xpath_remove</a></code>(7), <code><a href="/docs/linux/man/7-pom_xpath_replace/">pom_xpath_replace</a></code>(7), <code><a href="/docs/linux/man/7-pom_xpath_set/">pom_xpath_set</a></code>(7). </p>
