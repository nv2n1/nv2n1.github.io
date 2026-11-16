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
<dt><code>&#8211;platform=string</code></dt>
<dd> platform (windows, linux, linux-64, osx-intel, osx-ppc, linux-ppc)</dd>
<dt><code>&#8211;server=string</code></dt>
<dd> repository url (<a href="rsync://contextgarden.net)">rsync://contextgarden.net)</a></dd>
<dt><code>&#8211;module=string</code></dt>
<dd> repository url (minimals)</dd>
<dt><code>&#8211;repository=string</code></dt>
<dd> specify version (current, experimental)</dd>
<dt><code>&#8211;context=string</code></dt>
<dd> specify version (current, latest, beta, yyyy.mm.dd)</dd>
<dt><code>&#8211;rsync=string</code></dt>
<dd> rsync binary (rsync)</dd>
<dt><code>&#8211;texroot=string</code></dt>
<dd> installation directory (not guessed for the moment)</dd>
<dt><code>&#8211;engine=string</code></dt>
<dd> tex engine (luatex, pdftex, xetex)</dd>
<dt><code>&#8211;modules=string</code></dt>
<dd> extra modules (can be list or &#8216;all&#8217;)</dd>
<dt><code>&#8211;fonts=string</code></dt>
<dd> additional fonts (can be list or &#8216;all&#8217;)</dd>
<dt><code>&#8211;goodies=string</code></dt>
<dd> extra binaries (like scite and texworks)</dd>
<dt><code>&#8211;force</code></dt>
<dd> instead of a dryrun, do the real thing</dd>
<dt><code>&#8211;update</code></dt>
<dd> update minimal tree</dd>
<dt><code>&#8211;make</code></dt>
<dd> also make formats and generate file databases</dd>
<dt><code>&#8211;keep</code></dt>
<dd> don&#8217;t delete unused or obsolete files</dd>
<dt><code>&#8211;state</code></dt>
<dd> update tree using saved state</dd>
<dt><code>&#8211;cygwin</code></dt>
<dd> adapt drive specs to cygwin</dd>
<dt><code>&#8211;mingw</code></dt>
<dd> assume mingw binaries being used</dd>
<dt><code>&#8211;silent</code></dt>
<dd> less (or no) logging</dd></dl>
<h2>AUTHOR</h2>
<p> More information about ConTeXt and the tools that come with it can be found at: </p>
<p> <code>maillist:</code> ntg-context [at] ntg.nl / <a rel="nofollow" href="http://www.ntg.nl/mailman/listinfo/ntg-context">http://www.ntg.nl/mailman/listinfo/ntg-context</a> </p>
<p> <code>webpage:</code> <a rel="nofollow" href="http://www.pragma-ade.nl">http://www.pragma-ade.nl</a> / <a rel="nofollow" href="http://tex.aanhet.net">http://tex.aanhet.net</a> </p>
<p> <code>wiki:</code> <a rel="nofollow" href="http://contextgarden.net">http://contextgarden.net</a> </p>
<h2>Index</h2>
