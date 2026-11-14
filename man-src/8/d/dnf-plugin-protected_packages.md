---
title: "dnf-plugin-protected_packages(8)"
name: "dnf-plugin-protected_packages"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dnf-plugin-protected_packages/"
description: "dnf.plugin.protected_packages – DNF protected_packages Plugin"
---

<p>dnf.plugin.protected_packages &#8211; DNF protected_packages Plugin</p>
<h2>Description</h2>
<p>Prevents any DNF operation that would result in a removal of one of the protected packages from the system. These are typically packages essential for proper system boot and basic operation.</p>
<h2>Configuration</h2>
<p>Deciding whether a package is protected is based on the package name. The set of packages names considered protected is loaded from configuration files under: </p>
<pre>/etc/dnf/protected.d
/etc/yum/protected.d</pre>
<p>Every line in all <code>*.conf</code> files there is taken as a protected package name. Moreover, the currently booted kernel package is always protected. </p>
<p> Complete disabling of the protected packages feature is done by disabling the plugin: </p>
<pre>dnf --disableplugin=protected_packages erase dnf</pre>
<h2>Author</h2>
<p>See AUTHORS in your Core DNF Plugins distribution</p>
<h2>Copyright</h2>
<p>2014, Red Hat, Licensed under GPLv2+</p>
