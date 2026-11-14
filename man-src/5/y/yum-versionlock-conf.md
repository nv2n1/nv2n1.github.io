---
title: "yum-versionlock-conf(5)"
name: "yum-versionlock-conf"
section: "5"
letter: "y"
url: "/docs/linux/man/5-yum-versionlock-conf/"
description: "yum-versionlock.conf(5)"
---

<p><code><a href="/docs/linux/man/5-yum-versionlock-conf/">yum-versionlock.conf</a>(5)</code> </p>
<h2>Synopsis</h2>
<p><code><a href="/docs/linux/man/5-yum-versionlock-conf/">yum-versionlock.conf</a>(5)</code> is the configuration file for <code><a href="/docs/linux/man/1-yum-versionlock/">yum-versionlock</a>(1)</code> Yum plugin for excluding packages that aren&#8217;t listed in the versionlock file. The plugin will walk each line of the versionlock file, parse out the name and version of the package. It will then exclude any package by that name that doesn&#8217;t match one of the versions listed within the file (or, optionally, any obsoleter of that package). This is basically the same as doing an exclude for the package name itself (as you cannot exclude installed packages), but yum will still see the versions you have installed/versionlocked as available so that &quot;yum reinstall&quot; will still work, etc. It can also work in the opposite way, like a fast exclude, by prefixing a &#8216;!&#8217; character to the version.</p>
<h2>Files</h2>
<p><i>/etc/yum/pluginconf.d/versionlock.conf</i></p>
<h2>File Format</h2>
<p><code><a href="/docs/linux/man/5-yum-versionlock-conf/">yum-versionlock.conf</a>(5)</code> utilizes configuration options in the form of</p>
<dl>
<dt>OPTION=VALUE</p>
<dd></dl>
<h2>Option</h2>
<dl>
<dt>follow_obsoletes</p>
<dd>This option is a boolean flag which specifies if the versionlock plugin should look at all the obsoletes, and see if any of the packages specified have an obsoleter. If an obsoleter is found then all versions of that package will be excluded. This option is off by default, as <code><a href="/docs/linux/man/1-yum-versionlock/">yum-versionlock</a>(1)</code> will take some time to do the obsoletes processing, and for non-rename obsoletes any issues you had which kept you at a specific version of a package should be different with another package.</dl>
<h2>Option</h2>
<dl>
<dt>locklist</p>
<dd>This option is a string with points to the file which will have the versionlock information in it. Note that the file <code>has</code> to exist (or the versionlock plugin will make yum exit). However it can be empty.</dl>
<h2>Author</h2>
<dl>
<dd>Chitlesh Goorah &lt;chitlesh [at] fedoraproject.org&gt;<br />
 James Antill &lt;james [at] fedoraproject.org&gt;</p>
<dl>
<dd></dl>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-yum-versionlock/">yum-versionlock</a>(1)</code> </p>
