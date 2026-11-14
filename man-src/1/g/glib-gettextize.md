---
title: "glib-gettextize(1)"
name: "glib-gettextize"
section: "1"
letter: "g"
url: "/docs/linux/man/1-glib-gettextize/"
description: "glib-gettextize – gettext internationalization utility"
---

<h2 class="name">NAME</h2>
<p> glib-gettextize &#8211; gettext internationalization utility </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>glib-gettextize</code> [OPTION&#8230;] [DIRECTORY]</dl>
<h2>DESCRIPTION</h2>
<p> <code>glib-gettextize</code></p>
<dd>helps to prepare a source package for being internationalized through gettext. It is a variant of the <code>gettextize</code> that ships with gettext. </p>
<p> <code>glib-gettextize</code> differs from <code>gettextize</code> in that it doesn&#8217;t create an intl/ subdirectory and doesn&#8217;t modify po/ChangeLog (note that newer versions of <code>gettextize</code> behave like this when called with the <code>&#8211;no-changelog</code> option).</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> print help and exit</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> print version information and exit</dl>
<p> <code>-c</code>, <code>&#8211;copy</code></p>
<dl>
<dt>
<dd> copy files instead of making symlinks</dl>
<p> <code>-f</code>, <code>&#8211;force</code></p>
<dl>
<dt>
<dd> force writing of new files even if old ones exist</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gettextize/">gettextize</a></code>(1) </p>
<h2>Index</h2>
