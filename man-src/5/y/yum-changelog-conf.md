---
title: "yum-changelog-conf(5)"
name: "yum-changelog-conf"
section: "5"
letter: "y"
url: "/docs/linux/man/5-yum-changelog-conf/"
description: "yum-changelog.conf(5)"
---

<p><code><a href="/docs/linux/man/5-yum-changelog-conf/">yum-changelog.conf</a>(5)</code> </p>
<h2>Synopsis</h2>
<p><code><a href="/docs/linux/man/5-yum-changelog-conf/">yum-changelog.conf</a>(5)</code> is the configuration file for <code><a href="/docs/linux/man/1-yum-changelog/">yum-changelog</a>(1)</code> Yum plugin for viewing package changelogs before/after updating. By default, this plugin will show the changelogs before the updates.</p>
<h2>Files</h2>
<p><i>/etc/yum/pluginconf.d/changelog.conf</i></p>
<h2>File Format</h2>
<p><code><a href="/docs/linux/man/5-yum-changelog-conf/">yum-changelog.conf</a>(5)</code> utilizes configuration options in the form of</p>
<dl>
<dt>OPTION=VALUE</dt>
<dd></dd></dl>
<h2>Option</h2>
<dl>
<dt>when</dt>
<dd>This option reflects when <code><a href="/docs/linux/man/1-yum-changelog/">yum-changelog</a>(1)</code> will allow changelog viewing during yum updates.</dd></dl>
<h2>Value</h2>
<dl>
<dt>pre</dt>
<dd>To make <code>yum-changelog(5)</code> show the changelog <code>before</code> the yum updates</dd>
<dt>post</dt>
<dd>To make <code>yum-changelog(5)</code> show the changelog <code>after</code> the yum updates.</dd></dl>
<h2>Option</h2>
<dl>
<dt>always</dt>
<dd>This option reflects specifies if the changelog should always be shown.</dd></dl>
<h2>Value</h2>
<dl>
<dt>true</dt>
<dd>The changelog is always displayed.</dd>
<dt>false</dt>
<dd>A command line option is required for the changelog to be displayed.</dd></dl>
<h2>Option</h2>
<dl>
<dt>updateinfo</dt>
<dd>This option specifies that the &quot;changelog&quot; from the repo. updateinfo should be shown.</dd></dl>
<h2>Value</h2>
<dl>
<dt>true</dt>
<dd>The updateinfo is displayed.</dd>
<dt>false</dt>
<dd>The updateinfo is never displayed.</dd></dl>
<h2>Option</h2>
<dl>
<dt>updateinfo_always</dt>
<dd>This option reflects specifies if the &quot;changelog&quot; from the repo. should always be shown (note that if updateinfo is false then this option has no meaning).</dd></dl>
<h2>Value</h2>
<dl>
<dt>true</dt>
<dd>The updateinfo is always displayed.</dd>
<dt>false</dt>
<dd>A command line option is required for the updateinfo to be displayed.</dd></dl>
<h2>Author</h2>
<dl>
<dd>Chitlesh Goorah &lt;chitlesh [at] fedoraproject.org&gt;</dd>
<dl>
<dd></dd></dl>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-yum-changelog/">yum-changelog</a>(1)</code> </p>
