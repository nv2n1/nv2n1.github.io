---

title: "csscapture_py2(1)"
name: "csscapture_py2"
section: "1"
letter: "c"
url: "/docs/linux/man/1-csscapture_py2/"
description: "csscapture – Downloads CSS stylesheets."
---

<p> <code>csscapture</code> &#8211; Downloads CSS stylesheets. </p>
<p> <code>csscapture</code> [<i>options</i>&#8230;] <i>URL</i></p>
<p> <code>CSSCapture</code> downloads all referenced CSS stylesheets of a given <i>URL</i> and saves them to a given target directory.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;debug</code></dt>
<dd> Show debug messages during capturing.</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Show help message and exit.</dd>
<dt><code>-m</code>. <code>&#8211;minified</code></dt>
<dd> Saves minified version of captured files.</dd>
<dt><code>-n</code>, <code>&#8211;notsave</code></dt>
<dd> If given, files are NOT saved, only log is written.</dd>
<dt><code>-s</code><i> DIR</i>, <code>&#8211;saveto</code>=<i>DIR</i></dt>
<dd> Save retrieved files to <i>DIR</i>, defaults to <code>./_CSSCapture_SAVED</code>.</dd>
<dt><code>-u</code><i> UA</i>, <code>&#8211;useragent</code>=<i>UA</i></dt>
<dd> Useragent to use for request of <i>URL</i>, default is urllib2s default.</dd></dl>
<h2>SEE ALSO</h2>
<dl>
<dt>/usr/share/doc/python-cssutils-doc/docs/html/docs/index.html</dt>
<dd>
</dd></dl>
