---
title: "pom_set_parent(7)"
name: "pom_set_parent"
section: "7"
letter: "p"
url: "/docs/linux/man/7-pom_set_parent/"
description: "pom_set_parent – set parent POM reference in POM file"
---

<p>pom_set_parent &#8211; set parent POM reference in POM file</p>
<h2>Synopsis</h2>
<p><code>%pom_set_parent</code> groupId*:*artifactId[*:*version] [POM-location]</p>
<h2>Description</h2>
<p>This macro patches specified POM file setting reference to parent POM to specified groupId, artifactId and version. </p>
<p> This macros first removes parent POM reference and then adds a new one. It&#8217;s (more or less) equivalent to call to <code>%pom_remove_parent</code> followed by invocation of <code>%pom_add_parent</code>. See <code><a href="/docs/linux/man/7-pom_remove_parent/">pom_remove_parent</a></code>(7) and <code><a href="/docs/linux/man/7-pom_add_parent/">pom_add_parent</a></code>(7) for more information about parameters.</p>
<h2>Examples</h2>
<p><code>%pom_set_parent com.example:example-parent module</code> &#8211; this call sets parent POM of <code>module/pom.xml</code> to <code>com.example:example-parent</code>.</p>
<h2>Author</h2>
<p>Written by Mikolaj Izdebski.</p>
<h2>Reporting Bugs</h2>
<p>Bugs should be reported through Red Hat Bugzilla at m[blue]<code><a rel="nofollow" href="http://bugzilla.redhat.com/">http://bugzilla.redhat.com/</a></code>m[].</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-pom_add_dep/">pom_add_dep</a></code>(7), <code><a href="/docs/linux/man/7-pom_add_parent/">pom_add_parent</a></code>(7), <code><a href="/docs/linux/man/7-pom_add_plugin/">pom_add_plugin</a></code>(7), <code><a href="/docs/linux/man/7-pom_disable_module/">pom_disable_module</a></code>(7), <code><a href="/docs/linux/man/7-pom_remove_dep/">pom_remove_dep</a></code>(7), <code><a href="/docs/linux/man/7-pom_remove_parent/">pom_remove_parent</a></code>(7), <code><a href="/docs/linux/man/7-pom_remove_plugin/">pom_remove_plugin</a></code>(7), <code><a href="/docs/linux/man/7-pom_xpath_inject/">pom_xpath_inject</a></code>(7), <code><a href="/docs/linux/man/7-pom_xpath_remove/">pom_xpath_remove</a></code>(7), <code><a href="/docs/linux/man/7-pom_xpath_replace/">pom_xpath_replace</a></code>(7), <code><a href="/docs/linux/man/7-pom_xpath_set/">pom_xpath_set</a></code>(7). </p>
