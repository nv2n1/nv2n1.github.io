---
title: "fvwm-config(1)"
name: "fvwm-config"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwm-config/"
description: "fvwm-config – query an existing fvwm installation"
---

<h2 class="name">NAME</h2>
<p> fvwm-config &#8211; query an existing fvwm installation </p>
<h2>SYNOPSIS</h2>
<p> <code>fvwm-config</code> [<i>&#8211;help</i>] [<i>&#8211;version</i>] [<i>&#8211;info</i>] [<i>&#8211;prefix</i>] [<i>&#8211;exec-prefix</i>] [<i>&#8211;bindir</i>] [<i>&#8211;datadir</i>] [<i>&#8211;libexecdir</i>] [<i>&#8211;sysconfdir</i>] [<i>&#8211;mandir</i>] [<i>&#8211;localedir</i>] [<i>&#8211;fvwm-moduledir</i>] [<i>&#8211;fvwm-datadir</i>] [<i>&#8211;fvwm-perllibdir</i>] [<i>&#8211;default-imagepath</i>] [<i>&#8211;default-userdir</i>] [<i>&#8211;fvwm-exe</i>] [<i>&#8211;supports</i>] [<i>&#8211;supports-&lt;feature&gt;</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>fvwm-config</code> is a shell script that provides an information about the fvwm version, installation directories, built-in paths and supported features.</p>
<h2>OPTIONS</h2>
<p> <code>fvwm-config</code> prints to the standard output in all options. Both short and long GNU-like option names may be used.</p>
<dl>
<dt><code>-h &#8211;help -?</code></dt>
<dd> prints the short usage</dd>
<dt><code>-v &#8211;version -V</code></dt>
<dd> prints the version</dd>
<dt><code>-i &#8211;info</code></dt>
<dd> prints the full info page</dd>
<dt><code>-P &#8211;prefix</code></dt>
<dd> prints the installation prefix</dd>
<dt><code>-E &#8211;exec-prefix</code></dt>
<dd> prints the installation exec-prefix</dd>
<dt><code>-B &#8211;bindir</code></dt>
<dd> prints the installation bindir</dd>
<dt><code>-D &#8211;datadir</code></dt>
<dd> prints the installation datadir</dd>
<dt><code>-L &#8211;libexecdir</code></dt>
<dd> prints the installation libexecdir</dd>
<dt><code>-S &#8211;sysconfdir</code></dt>
<dd> prints the installation sysconfdir</dd>
<dt><code>-M &#8211;mandir</code></dt>
<dd> prints the installation mandir</dd>
<dt><code>-O &#8211;localedir</code></dt>
<dd> prints the installation localedir</dd>
<dt><code>-m &#8211;fvwm-moduledir</code></dt>
<dd> prints FVWM_MODULEDIR, where the modules are installed</dd>
<dt><code>-d &#8211;fvwm-datadir</code></dt>
<dd> prints FVWM_DATADIR, where the system wide configs are installed</dd>
<dt><code>-p &#8211;fvwm-perllibdir</code></dt>
<dd> prints FVWM_PERLLIBDIR, where the perl library is installed</dd>
<dt><code>-I &#8211;default-imagepath</code></dt>
<dd> prints the built-in ImagePath</dd>
<dt><code>-U &#8211;default-userdir</code></dt>
<dd> prints the default FVWM_USERDIR, note: $HOME is not expanded</dd>
<dt><code>-e &#8211;fvwm-exe</code></dt>
<dd> prints the fvwm executable name (in bindir)</dd>
<dt><code>-s &#8211;supports</code></dt>
<dd> lists all supported features, one per line</dd>
<dt><code>&#8211;supports-</code><i>&lt;feature&gt;</i></dt>
<dd> prints nothing, returns: 0 if the <i>&lt;feature&gt;</i> is supported, 100 if not, 200 if unknown. All or supported feature names may be found using <i>&#8211;info</i> or <i>&#8211;supports</i> respectively.</dd>
<dt></dt></dl>
<h2>USAGE</h2>
<dd> Here are some real life usages. </dd>
<p> Checks for xft support: </p>
<pre><code>
if fvwm
    - config-- supports - xft;
then echo 1;
else echo 0;
fi
</code></pre>
<p> <i>fvwm-themes</i> package checks for the correct <i>fvwm</i> version installed using: </p>
<pre>
fvwm-config --version
</pre>
<p> and tries to use the same installation directories: </p>
<pre>
fvwm-config --bindir --mandir --fvwm-datadir
</pre>
<p> A way to find the full path to the fvwm executable: </p>
<pre>
echo `fvwm-config --bindir`/`fvwm-config --fvwm-exe`
</pre>
<p> A way to start modules in perl: </p>
<pre>
use lib `fvwm-config -p | tr -d '`;
use FVWM::Module;
</pre>
<p> For a more human readable output, try: </p>
<pre>
fvwm-config --info
</pre>
<h2>COPYING</h2>
<p> <code>fvwm-config</code> is a part of fvwm package and distributed by the same terms, see GNU GPL.</p>
<h2>AUTHOR</h2>
<p> Mikhael Goikhman &lt;migo [at] homemail.com&gt; </p>
