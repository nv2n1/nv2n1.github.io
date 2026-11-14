---
title: "mtx-update(1)"
name: "mtx-update"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mtx-update/"
description: "mtx-update – ConTeXt Minimals Updater"
---

<h2 class="name">NAME</h2>
<p>&nbsp;mtx-update &#8211; ConTeXt Minimals Updater </p>
<h2>SYNOPSIS</h2>
<p> <code>mtxrun &#8211;script update [</code> <i>OPTIONS &#8230;</i> <code>] [</code> <i>FILENAMES</i> <code>]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>ConTeXt Minimals Updater</code></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;platform=string</code></p>
<dd> platform (windows, linux, linux-64, osx-intel, osx-ppc, linux-ppc)</p>
<dt><code>&#8211;server=string</code></p>
<dd> repository url (<a href="rsync://contextgarden.net)">rsync://contextgarden.net)</a></p>
<dt><code>&#8211;module=string</code></p>
<dd> repository url (minimals)</p>
<dt><code>&#8211;repository=string</code></p>
<dd> specify version (current, experimental)</p>
<dt><code>&#8211;context=string</code></p>
<dd> specify version (current, latest, beta, yyyy.mm.dd)</p>
<dt><code>&#8211;rsync=string</code></p>
<dd> rsync binary (rsync)</p>
<dt><code>&#8211;texroot=string</code></p>
<dd> installation directory (not guessed for the moment)</p>
<dt><code>&#8211;engine=string</code></p>
<dd> tex engine (luatex, pdftex, xetex)</p>
<dt><code>&#8211;modules=string</code></p>
<dd> extra modules (can be list or &#8216;all&#8217;)</p>
<dt><code>&#8211;fonts=string</code></p>
<dd> additional fonts (can be list or &#8216;all&#8217;)</p>
<dt><code>&#8211;goodies=string</code></p>
<dd> extra binaries (like scite and texworks)</p>
<dt><code>&#8211;force</code></p>
<dd> instead of a dryrun, do the real thing</p>
<dt><code>&#8211;update</code></p>
<dd> update minimal tree</p>
<dt><code>&#8211;make</code></p>
<dd> also make formats and generate file databases</p>
<dt><code>&#8211;keep</code></p>
<dd> don&#8217;t delete unused or obsolete files</p>
<dt><code>&#8211;state</code></p>
<dd> update tree using saved state</p>
<dt><code>&#8211;cygwin</code></p>
<dd> adapt drive specs to cygwin</p>
<dt><code>&#8211;mingw</code></p>
<dd> assume mingw binaries being used</p>
<dt><code>&#8211;silent</code></p>
<dd> less (or no) logging</dl>
<h2>AUTHOR</h2>
<p> More information about ConTeXt and the tools that come with it can be found at: </p>
<p> <code>maillist:</code> ntg-context [at] ntg.nl / <a rel="nofollow" href="http://www.ntg.nl/mailman/listinfo/ntg-context">http://www.ntg.nl/mailman/listinfo/ntg-context</a> </p>
<p> <code>webpage:</code> <a rel="nofollow" href="http://www.pragma-ade.nl">http://www.pragma-ade.nl</a> / <a rel="nofollow" href="http://tex.aanhet.net">http://tex.aanhet.net</a> </p>
<p> <code>wiki:</code> <a rel="nofollow" href="http://contextgarden.net">http://contextgarden.net</a> </p>
<h2>Index</h2>
