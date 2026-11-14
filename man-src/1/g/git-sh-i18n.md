---
title: "git-sh-i18n(1)"
name: "git-sh-i18n"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-sh-i18n/"
description: "git-sh-i18n – Git’s i18n setup code for shell scripts"
---

<h2 class="name">NAME</h2>
<p> git-sh-i18n &#8211; Git&#8217;s i18n setup code for shell scripts </p>
<h2>SYNOPSIS</h2>
<pre>
<i>. &quot;$(git --exec-path)/git-sh-i18n&quot;</i>
</pre>
<h2>DESCRIPTION</h2>
<p> This is not a command the end user would want to run. Ever. This documentation is meant for people who are studying the Porcelain-ish scripts and/or are writing new ones. </p>
<p> The &#8216;git sh-i18n scriptlet is designed to be sourced (using <code>.</code>) by Git&#8217;s porcelain programs implemented in shell script. It provides wrappers for the GNU <code>gettext</code> and <code>eval_gettext</code> functions accessible through the <code>gettext.sh</code> script, and provides pass-through fallbacks on systems without GNU gettext.</p>
<h2>FUNCTIONS</h2>
<p> gettext</p>
<dl>
<dt>
<dd> Currently a dummy fall-through function implemented as a wrapper around <code><a href="/docs/linux/man/1-printf/">printf</a>(1)</code>. Will be replaced by a real gettext implementation in a later version.</dl>
<p> eval_gettext</p>
<dl>
<dt>
<dd> Currently a dummy fall-through function implemented as a wrapper around <code><a href="/docs/linux/man/1-printf/">printf</a>(1)</code> with variables expanded by the <code><a href="/docs/linux/man/1-git-sh-i18n--envsubst/">git-sh-i18n&#8211;envsubst</a></code>(1) helper. Will be replaced by a real gettext implementation in a later version.</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
