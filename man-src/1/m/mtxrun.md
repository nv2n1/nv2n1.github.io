---
title: "mtxrun(1)"
name: "mtxrun"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mtxrun/"
description: "mtxrun – ConTeXt TDS Runner Tool"
---

<h2 class="name">NAME</h2>
<p>&nbsp;mtxrun &#8211; ConTeXt TDS Runner Tool </p>
<h2>SYNOPSIS</h2>
<p> <code>mtxrun [</code> <i>OPTIONS &#8230;</i> <code>] [</code> <i>FILENAMES</i> <code>]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>ConTeXt TDS Runner Tool</code></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;script</code></p>
<dd> run an mtx script (lua preferred method) (&#8211;noquotes), no script gives list</p>
<dt><code>&#8211;evaluate</code></p>
<dd> run code passed on the commandline (between quotes) (=loop) (exit|quit aborts)</p>
<dt><code>&#8211;execute</code></p>
<dd> run a script or program (texmfstart method) (&#8211;noquotes)</p>
<dt><code>&#8211;resolve</code></p>
<dd> resolve prefixed arguments</p>
<dt><code>&#8211;ctxlua</code></p>
<dd> run internally (using preloaded libs)</p>
<dt><code>&#8211;internal</code></p>
<dd> run script using built in libraries (same as &#8211;ctxlua)</p>
<dt><code>&#8211;locate</code></p>
<dd> locate given filename in database (default) or system (&#8211;first &#8211;all &#8211;detail)</p>
<dt><code>&#8211;tree=pathtotree</code></p>
<dd> use given texmf tree (default file: setuptex.tmf)</p>
<dt><code>&#8211;path=runpath</code></p>
<dd> go to given path before execution</p>
<dt><code>&#8211;ifchanged=filename</code></p>
<dd> only execute when given file has changed (md checksum)</p>
<dt><code>&#8211;iftouched=old,new</code></p>
<dd> only execute when given file has changed (time stamp)</p>
<dt><code>&#8211;makestubs</code></p>
<dd> create stubs for (context related) scripts</p>
<dt><code>&#8211;removestubs</code></p>
<dd> remove stubs (context related) scripts</p>
<dt><code>&#8211;stubpath=binpath</code></p>
<dd> paths where stubs wil be written</p>
<dt><code>&#8211;windows</code></p>
<dd> create windows (mswin) stubs</p>
<dt><code>&#8211;unix</code></p>
<dd> create unix (linux) stubs</p>
<dt><code>&#8211;addbinarypath</code></p>
<dd> prepend the (found) binarypath to runners</p>
<dt><code>&#8211;verbose</code></p>
<dd> give a bit more info</p>
<dt><code>&#8211;trackers=list</code></p>
<dd> enable given trackers</p>
<dt><code>&#8211;progname=str</code></p>
<dd> format or backend</p>
<dt><code>&#8211;systeminfo=str</code></p>
<dd> show current operating system, processor, etc</p>
<dt><code>&#8211;edit</code></p>
<dd> launch editor with found file</p>
<dt><code>&#8211;launch</code></p>
<dd> launch files like manuals, assumes os support (&#8211;all,&#8211;list)</p>
<dt><code>&#8211;timedrun</code></p>
<dd> run a script and time its run</p>
<dt><code>&#8211;autogenerate</code></p>
<dd> regenerate databases if needed (handy when used to run context in an editor)</p>
<dt><code>&#8211;usekpse</code></p>
<dd> use kpse as fallback (when no mkiv and cache installed, often slower)</p>
<dt><code>&#8211;forcekpse</code></p>
<dd> force using kpse (handy when no mkiv and cache installed but less functionality)</p>
<dt><code>&#8211;prefixes</code></p>
<dd> show supported prefixes</p>
<dt><code>&#8211;generate</code></p>
<dd> generate file database</p>
<dt><code>&#8211;variables</code></p>
<dd> show configuration variables</p>
<dt><code>&#8211;configurations</code></p>
<dd> show configuration order</p>
<dt><code>&#8211;directives</code></p>
<dd> show (known) directives</p>
<dt><code>&#8211;trackers</code></p>
<dd> show (known) trackers</p>
<dt><code>&#8211;experiments</code></p>
<dd> show (known) experiments</p>
<dt><code>&#8211;expand-braces</code></p>
<dd> expand complex variable</p>
<dt><code>&#8211;resolve-path</code></p>
<dd> expand variable (completely resolve paths)</p>
<dt><code>&#8211;expand-path</code></p>
<dd> expand variable (resolve paths)</p>
<dt><code>&#8211;expand-var</code></p>
<dd> expand variable (resolve references)</p>
<dt><code>&#8211;show-path</code></p>
<dd> show path expansion of &#8230;</p>
<dt><code>&#8211;var-value</code></p>
<dd> report value of variable</p>
<dt><code>&#8211;find-file</code></p>
<dd> report file location</p>
<dt><code>&#8211;find-path</code></p>
<dd> report path of file</p>
<dt><code>&#8211;pattern=string</code></p>
<dd> filter variables</dl>
<h2>AUTHOR</h2>
<p> More information about ConTeXt and the tools that come with it can be found at: </p>
<p> <code>maillist:</code> ntg-context [at] ntg.nl / <a rel="nofollow" href="http://www.ntg.nl/mailman/listinfo/ntg-context">http://www.ntg.nl/mailman/listinfo/ntg-context</a> </p>
<p> <code>webpage:</code> <a rel="nofollow" href="http://www.pragma-ade.nl">http://www.pragma-ade.nl</a> / <a rel="nofollow" href="http://tex.aanhet.net">http://tex.aanhet.net</a> </p>
<p> <code>wiki:</code> <a rel="nofollow" href="http://contextgarden.net">http://contextgarden.net</a> </p>
<h2>Index</h2>
