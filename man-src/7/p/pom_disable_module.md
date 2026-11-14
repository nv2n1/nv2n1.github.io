---
title: "pom_disable_module(7)"
name: "pom_disable_module"
section: "7"
letter: "p"
url: "/docs/linux/man/7-pom_disable_module/"
description: "pom_disable_module – disable given project module in POM file"
---

<p>pom_disable_module &#8211; disable given project module in POM file</p>
<h2>Synopsis</h2>
<p><code>%pom_disable_module</code> module-name [POM-location]</p>
<h2>Description</h2>
<p>This macro patches specified POM file not to contain reference to given project module. </p>
<p> Module name is the exact name of the module to be disabled. It must not be ommited. </p>
<p> POM location can be either a full path to the POM file, or a path to the directory containing <code>pom.xml</code>. If POM location is not given then <code>pom.xml</code> from current working directory is used.</p>
<h2>Examples</h2>
<p><code>%pom_disable_module nonfree</code> &#8211; this call removes aggregated module <code>nonfree</code> from POM file in current working directory.</p>
<h2>Author</h2>
<p>Written by Mikolaj Izdebski.</p>
<h2>Reporting Bugs</h2>
<p>Bugs should be reported through Red Hat Bugzilla at m[blue]<code><a rel="nofollow" href="http://bugzilla.redhat.com/">http://bugzilla.redhat.com/</a></code>m[].</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-pom_add_dep/">pom_add_dep</a></code>(7), <code><a href="/docs/linux/man/7-pom_add_parent/">pom_add_parent</a></code>(7), <code><a href="/docs/linux/man/7-pom_add_plugin/">pom_add_plugin</a></code>(7), <code><a href="/docs/linux/man/7-pom_remove_dep/">pom_remove_dep</a></code>(7), <code><a href="/docs/linux/man/7-pom_remove_parent/">pom_remove_parent</a></code>(7), <code><a href="/docs/linux/man/7-pom_remove_plugin/">pom_remove_plugin</a></code>(7), <code><a href="/docs/linux/man/7-pom_set_parent/">pom_set_parent</a></code>(7), <code><a href="/docs/linux/man/7-pom_xpath_inject/">pom_xpath_inject</a></code>(7), <code><a href="/docs/linux/man/7-pom_xpath_remove/">pom_xpath_remove</a></code>(7), <code><a href="/docs/linux/man/7-pom_xpath_replace/">pom_xpath_replace</a></code>(7), <code><a href="/docs/linux/man/7-pom_xpath_set/">pom_xpath_set</a></code>(7). </p>
