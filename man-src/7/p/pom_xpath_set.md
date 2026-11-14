---
title: "pom_xpath_set(7)"
name: "pom_xpath_set"
section: "7"
letter: "p"
url: "/docs/linux/man/7-pom_xpath_set/"
description: "pom_xpath_set – set text contents of XML node from POM file"
---

<p>pom_xpath_set &#8211; set text contents of XML node from POM file</p>
<h2>Synopsis</h2>
<p><code>%pom_xpath_set</code> XPath new-contents [POM-location]</p>
<h2>Description</h2>
<p>This macro patches specified POM file replacing text contents of all XML nodes described by the XPath expression with given new text content. </p>
<p> XPath is an expression describing a set of XML nodes to be removed from the POM file. It must be a properly formated XPath 1.0 expression, as described in m[blue]<code><a rel="nofollow" href="http://www.w3.org/TR/xpath/">http://www.w3.org/TR/xpath/</a></code>m[]. </p>
<p> POM location can be either a full path to the POM file, or a path to the directory containing <code>pom.xml</code>. If POM location is not given then <code>pom.xml</code> from current working directory is used.</p>
<h2>Bugs</h2>
<p>POM files use a specific namespace &#8211; m[blue]<code><a rel="nofollow" href="http://maven.apache.org/POM/4.0.0">http://maven.apache.org/POM/4.0.0</a></code>m[]. Currently this namespace needs to be explicitly specified in all XPath POM macros by prefixing all node names with <code>pom:</code>.</p>
<h2>Author</h2>
<p>Written by Mikolaj Izdebski.</p>
<h2>Reporting Bugs</h2>
<p>Bugs should be reported through Red Hat Bugzilla at m[blue]<code><a rel="nofollow" href="http://bugzilla.redhat.com/">http://bugzilla.redhat.com/</a></code>m[].</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-pom_add_dep/">pom_add_dep</a></code>(7), <code><a href="/docs/linux/man/7-pom_add_parent/">pom_add_parent</a></code>(7), <code><a href="/docs/linux/man/7-pom_add_plugin/">pom_add_plugin</a></code>(7), <code><a href="/docs/linux/man/7-pom_disable_module/">pom_disable_module</a></code>(7), <code><a href="/docs/linux/man/7-pom_remove_dep/">pom_remove_dep</a></code>(7), <code><a href="/docs/linux/man/7-pom_remove_parent/">pom_remove_parent</a></code>(7), <code><a href="/docs/linux/man/7-pom_remove_plugin/">pom_remove_plugin</a></code>(7), <code><a href="/docs/linux/man/7-pom_set_parent/">pom_set_parent</a></code>(7), <code><a href="/docs/linux/man/7-pom_xpath_inject/">pom_xpath_inject</a></code>(7), <code><a href="/docs/linux/man/7-pom_xpath_remove/">pom_xpath_remove</a></code>(7), <code><a href="/docs/linux/man/7-pom_xpath_replace/">pom_xpath_replace</a></code>(7). </p>
