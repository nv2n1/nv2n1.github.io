---
title: "pom_add_plugin(7)"
name: "pom_add_plugin"
section: "7"
letter: "p"
url: "/docs/linux/man/7-pom_add_plugin/"
description: "pom_add_plugin – add plugin invocation to POM file"
---

<p>pom_add_plugin &#8211; add plugin invocation to POM file</p>
<h2>Synopsis</h2>
<p><code>%pom_add_plugin</code> groupId*:*artifactId[*:*version] [POM-location] [extra-XML]</p>
<h2>Description</h2>
<p>This macro patches specified POM file adding plugin invocation of given groupId and artifactId. </p>
<p> groupId and artifactId are identifiers of Maven plugin artifact of which invocation is to be added. groupId may be ommited, in which case value of &quot;org.apache.maven.plugins&quot; is used as default. artifactId must be specified. If version is not specified then default value of &quot;any&quot; is used. </p>
<p> POM location can be either a full path to the POM file, or a path to the directory containing <code>pom.xml</code>. If POM location is not given then <code>pom.xml</code> from current working directory is used. </p>
<p> Extra XML is additional XML code to be added into the <code>&lt;plugin&gt;</code> node. This parameter can be ommited, in which case no extra XML is appended.</p>
<h2>Examples</h2>
<p><code>%pom_add_plugin com.example:plugin foo</code> &#8211; this call adds invocation of plugin <code>com.example:plugin</code> to <code>foo/pom.xml</code>. </p>
<p> <code>%pom_add_plugin :maven-compiler-plugin . &quot;&lt;target&gt;1.5&lt;/target&gt;&quot;</code> &#8211; this call adds invocation of Maven Compiler Plugin with target configured to 1.5.</p>
<h2>Author</h2>
<p>Written by Mikolaj Izdebski.</p>
<h2>Reporting Bugs</h2>
<p>Bugs should be reported through Red Hat Bugzilla at m[blue]<code><a rel="nofollow" href="http://bugzilla.redhat.com/">http://bugzilla.redhat.com/</a></code>m[].</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-pom_add_dep/">pom_add_dep</a></code>(7), <code><a href="/docs/linux/man/7-pom_add_parent/">pom_add_parent</a></code>(7), <code><a href="/docs/linux/man/7-pom_disable_module/">pom_disable_module</a></code>(7), <code><a href="/docs/linux/man/7-pom_remove_dep/">pom_remove_dep</a></code>(7), <code><a href="/docs/linux/man/7-pom_remove_parent/">pom_remove_parent</a></code>(7), <code><a href="/docs/linux/man/7-pom_remove_plugin/">pom_remove_plugin</a></code>(7), <code><a href="/docs/linux/man/7-pom_set_parent/">pom_set_parent</a></code>(7), <code><a href="/docs/linux/man/7-pom_xpath_inject/">pom_xpath_inject</a></code>(7), <code><a href="/docs/linux/man/7-pom_xpath_remove/">pom_xpath_remove</a></code>(7), <code><a href="/docs/linux/man/7-pom_xpath_replace/">pom_xpath_replace</a></code>(7), <code><a href="/docs/linux/man/7-pom_xpath_set/">pom_xpath_set</a></code>(7). </p>
