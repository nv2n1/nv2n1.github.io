---
title: "pom_change_dep(7)"
name: "pom_change_dep"
section: "7"
letter: "p"
url: "/docs/linux/man/7-pom_change_dep/"
description: "pom_change_dep – change dependency in Maven POM file or Ivy module"
---

<p>pom_change_dep &#8211; change dependency in Maven POM file or Ivy module</p>
<h2>Synopsis</h2>
<p><code>%pom_change_dep</code> [OPTIONS] SOURCE_ARTIFACT CHANGED_ARTIFACT [POM-location]&#8230; [extra-XML] </p>
<p> <code>%pom_change_dep</code> [OPTIONS] SOURCE_ARTIFACT CHANGED_ARTIFACT [Ivy-module-location]&#8230; [extra-XML]</p>
<h2>Options</h2>
<p><code>-r</code></p>
<dl>
<dd>Work in recursive mode. That means that given dependency is also changed in all enabled submodules of given POM file(s). Has no effect if the file is not Maven POM.</dl>
<p> <code>-f</code></p>
<dl>
<dd>Do not throw an error when one of the specified files doesn&#8217;t contain given dependency.</dl>
<h2>Description</h2>
<p>These macros patch specified POM or Ivy file changing a dependency on given Maven artifact specified by artifact coordinates to artifact specified by second set of Maven coordinates. The artifact specification has same format as <code>%pom_add_dep</code>. The omitted or empty parts in second artifact specification cause the original value to be left unmodified. Supplying a special value of <code>&#8211;</code> for given part causes that part of artifact specification to be deleted. </p>
<p> POM location can be either a full path to the POM or Ivy file, or a path to the directory containing <code>pom.xml</code> or <code>ivy.xml</code>. If POM location is not given then <code>pom.xml</code> or <code>ivy.xml</code> from current working directory is used. When both <code>pom.xml</code> and <code>ivy.xml</code> are present, <code>pom.xml</code> is processed. You can specify more file locations which will be processed. </p>
<p> Extra XML is additional XML code to be added into the <code>&lt;dependency&gt;</code> node. This parameter can be ommited, in which case no extra XML is appended.</p>
<h2>Examples</h2>
<p><code>pom_change_dep foo: com.example.foo:</code> &#8211; this call changes groupId of all dependencies which have groupId foo to com.example.foo. Their artifactId, versions and other possible parts are left unmodified.</p>
<h2>Author</h2>
<p>Written by Michael Simacek.</p>
<h2>Reporting Bugs</h2>
<p>Bugs should be reported through Red Hat Bugzilla at m[blue]<code><a rel="nofollow" href="http://bugzilla.redhat.com/">http://bugzilla.redhat.com/</a></code>m[].</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-pom_add_dep/">pom_add_dep</a></code>(7), <code><a href="/docs/linux/man/7-pom_add_parent/">pom_add_parent</a></code>(7), <code><a href="/docs/linux/man/7-pom_add_plugin/">pom_add_plugin</a></code>(7), <code><a href="/docs/linux/man/7-pom_disable_module/">pom_disable_module</a></code>(7), <code><a href="/docs/linux/man/7-pom_remove_dep/">pom_remove_dep</a></code>(7), <code><a href="/docs/linux/man/7-pom_remove_parent/">pom_remove_parent</a></code>(7), <code><a href="/docs/linux/man/7-pom_remove_plugin/">pom_remove_plugin</a></code>(7), <code><a href="/docs/linux/man/7-pom_set_parent/">pom_set_parent</a></code>(7), <code><a href="/docs/linux/man/7-pom_xpath_inject/">pom_xpath_inject</a></code>(7), <code><a href="/docs/linux/man/7-pom_xpath_remove/">pom_xpath_remove</a></code>(7), <code><a href="/docs/linux/man/7-pom_xpath_replace/">pom_xpath_replace</a></code>(7), <code><a href="/docs/linux/man/7-pom_xpath_set/">pom_xpath_set</a></code>(7). </p>
