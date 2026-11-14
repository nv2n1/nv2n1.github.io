---
title: "abrt-bugzilla(7)"
name: "abrt-bugzilla"
section: "7"
letter: "a"
url: "/docs/linux/man/7-abrt-bugzilla/"
---

Bugzilla plugin for <a HREF="/docs/linux/man/8-abrt/">abrt</a>(8)

<h2>Description</h2>

<i>abrt</i> is a daemon that watches for application crashes. When a crash occurs, it collects the crash data and takes action according to its configuration. This manual page describes the <i>Bugzilla</i> plugin for <i>abrt</i>. This plugin is used to report the crash to a Bugzilla instance. The plugin will determine the package name and distribution version. The crash data is attached to the bug report.

<h2>Invocation</h2>

The plugin is invoked in the <i>abrt.conf</i> configuration file. No parameters are necessary.

<h2>Configuration</h2>

The <i>Bugzilla.conf</i> configuration file contains several entries in the format &quot;Option = Value&quot;. The options are:

<h3>BugzillaURL</h3>

The URL of the Bugzilla instance that you want to use, including the path to the xmlrpc. The default is <a rel="nofollow" HREF="https://bugzilla.redhat.com/xmlrpc.cgi">https://bugzilla.redhat.com/xmlrpc.cgi</a>

<h3>Login</h3>

Your Bugzilla login. If you have no Bugzilla account, you cannot use the plugin.

<h3>Password</h3>

Your Bugzilla password.

<h2>Examples</h2>

This is a snippet from the <i>abrt.conf</i> configuration file. When something crashes, use the Bugzilla plugin: [common] 
 ActionsAndReporters = Bugzilla

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/8-abrt/">abrt</a></i>(8), <i><a HREF="/docs/linux/man/5-abrt-conf/">abrt.conf</a></i>(5), <i><a HREF="/docs/linux/man/7-abrt-plugins/">abrt-plugins</a></i>(7)

<h2>Author</h2>

Written by Zdenek Prikryl &lt;zprikryl [at] redhat.com&gt;. Manual page written by Daniel Novotny &lt;dnovotny [at] redhat.com&gt;.
