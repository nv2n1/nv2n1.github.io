---
title: "pom_xpath_disable(7)"
name: "pom_xpath_disable"
section: "7"
letter: "p"
url: "/docs/linux/man/7-pom_xpath_disable/"
description: "pom_xpath_disable – Disable all modules whose POM files satisfy given XPath condition"
---

<p>pom_xpath_disable &#8211; Disable all modules whose POM files satisfy given XPath condition</p>
<h2>Synopsis</h2>
<p><code>%pom_xpath_disable</code> XPath-expression [POM-location]&#8230;</p>
<h2>Description</h2>
<p>This macro recursively walks all enabled submodules of given POM and evaluates given XPath expression on them. If the expression returns a true value, matching submodule is disabled. Values considered true are defined by XPath specification as either true boolean value (i.e. returned by comparisons), non-empty node set, non-empty string or non-zero number. </p>
<p> If the main module (specified by POM-location or pom.xml by default) also satisfies the condition, processing is aborted prior to making any changes and an error is raised. When none of the modules satisfy it, an error is also raised. </p>
<p> POM location can be either a full path to the POM file, or a path to the directory containing <code>pom.xml</code>. If POM location is not given then <code>pom.xml</code> from current working directory is used. You can specify more file locations which will be processed.</p>
<h2>Examples</h2>
<p><code>%pom_xpath_disable &quot;/pom:project/pom:classifier = &#8216;test&#8217;&quot;</code> &#8211; this call disables all modules with classifier <code>test</code> </p>
<p> <code>%pom_xpath_disable /pom:project/pom:packaging</code> &#8211; this call disables all sumbodules that explicitly specify packaging</p>
<h2>Author</h2>
<p>Written by Michael Simacek.</p>
<h2>Reporting Bugs</h2>
<p>Bugs should be reported through Red Hat Bugzilla at m[blue]<code><a rel="nofollow" href="http://bugzilla.redhat.com/">http://bugzilla.redhat.com/</a></code>m[].</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-pom_add_dep/">pom_add_dep</a></code>(7), <code><a href="/docs/linux/man/7-pom_add_parent/">pom_add_parent</a></code>(7), <code><a href="/docs/linux/man/7-pom_add_plugin/">pom_add_plugin</a></code>(7), <code><a href="/docs/linux/man/7-pom_remove_dep/">pom_remove_dep</a></code>(7), <code><a href="/docs/linux/man/7-pom_remove_parent/">pom_remove_parent</a></code>(7), <code><a href="/docs/linux/man/7-pom_remove_plugin/">pom_remove_plugin</a></code>(7), <code><a href="/docs/linux/man/7-pom_change_dep/">pom_change_dep</a></code>(7), <code><a href="/docs/linux/man/7-pom_set_parent/">pom_set_parent</a></code>(7), <code><a href="/docs/linux/man/7-pom_xpath_inject/">pom_xpath_inject</a></code>(7), <code><a href="/docs/linux/man/7-pom_xpath_remove/">pom_xpath_remove</a></code>(7), <code><a href="/docs/linux/man/7-pom_xpath_replace/">pom_xpath_replace</a></code>(7), <code><a href="/docs/linux/man/7-pom_xpath_set/">pom_xpath_set</a></code>(7). <code><a href="/docs/linux/man/7-pom_disable_module/">pom_disable_module</a></code>(7). </p>
