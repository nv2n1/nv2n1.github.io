---
title: "session-installer(1)"
name: "session-installer"
section: "1"
letter: "s"
url: "/docs/linux/man/1-session-installer/"
description: "session-installer – allows applications to easily install and remove software"
---

<h2 class="name">NAME</h2>
<p> session-installer &#8211; allows applications to easily install and remove software </p>
<h2>SYNOPSIS</h2>
<p> <code>session-installer</code></p>
<h2>DESCRIPTION</h2>
<p> <code>Session-installer</code> allows applications to easily install additional software (e.g. extensions or GSreamer codecs), uninstall files and perform simple package status queries by calling a distribution neutral D-Bus interface. </p>
<p> The whole process of confirmation, error reporting and progress notification is handled by sessioninstaller. Currently it comes only with a GTK based user interface. </p>
<p> The D-Bus interface is developed under the PackageKit umbrella and is available on the session bus. The reference implementation can be found in gnome-packagekit. It was also adpoted by KPackageKit. </p>
<p> In contrast to gnome-packagekit and KPackageKit it doesn&#8217;t use the PackageKit daemon for querying and installation, but instead makes use of APT and aptdaemon directly (alternatively synaptic can be used). </p>
<p> Normally it is not required to start this programme manually since it makes use of D-Bus activation and will be started on request automatically.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt>SESSIONINSTALLER_BACKEND</p>
<dd> Set the package manager which should be used for installation. Possible values are <i>aptdaemon</i>, <i>synaptic</i> and <i>dummy</i>.</dl>
<h2>HOMEPAGE</h2>
<p> <a rel="nofollow" href="https://launchpad.net/sessioninstaller">https://launchpad.net/sessioninstaller</a></p>
<h2>BUGS</h2>
<p> You can report bugs at the Launchpad site of aptdaemon: <a rel="nofollow" href="https://bugs.launchpad.net/sessioninstaller/+filebug">https://bugs.launchpad.net/sessioninstaller/+filebug</a></p>
<h2>AUTHOR</h2>
<p> Sebastian Heinlein &lt;devel at glatzor dot de&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-aptd/">aptd</a>(1)</code> <code><a rel="nofollow" href="http://www.packagekit.org/pk-faq.html#session-methods">http://www.packagekit.org/pk-faq.html#session-methods</a></code> </p>
<h2>Index</h2>
