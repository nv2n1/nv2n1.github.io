---
title: "dh_installgsettings(1)"
name: "dh_installgsettings"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_installgsettings/"
description: "dh_installgsettings – install GSettings overrides and set dependencies"
---

<h2 class="name">NAME</h2>
<p> dh_installgsettings &#8211; install GSettings overrides and set dependencies </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_installgsettings</code> [<i>debhelper options</i>] [<code>&#8211;priority=&lt;number</code>&gt;]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_installgsettings</code> is a debhelper program that is responsible for installing GSettings override files and generating appropriate dependencies on the GSettings backend. </p>
<p> The dependency on the backend will be generated in <code>${misc:Depends}</code>.</p>
<h2>FILES</h2>
<dl>
<dt>debian/<i>package</i>.gsettings-override</p>
<dd> Installed into usr/share/glib-2.0/schemas/10_<i>package</i>.gschema.override in the package build directory, with &quot;<i>package</i>&quot; replaced by the package name. </p>
<p> The format of the file is the following: </p>
<pre>
  [org.gnome.mypackage]
  boolean-setting=true
  string-setting='string'
  ...
</pre>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;priority</code> <i>priority</i></p>
<dd> Use <i>priority</i> (which should be a 2-digit number) as the override priority instead of 10. Higher values than ten can be used by derived distributions (20), blend distributions (50), or site-specific packages (90).</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Laurent Bigonville &lt;bigon [at] debian.org&gt;, Josselin Mouette &lt;joss [at] debian.org&gt; </p>
<h2>Index</h2>
