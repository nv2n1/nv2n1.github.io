---

title: "texmfstart(1)"
name: "texmfstart"
section: "1"
letter: "t"
url: "/docs/linux/man/1-texmfstart/"
description: "mtxrun – ConTeXt TDS Runner Tool"
---

<p> <code>mtxrun [</code> <i>OPTIONS &#8230;</i> <code>] [</code> <i>FILENAMES</i> <code>]</code></p>
<p> <code>ConTeXt TDS Runner Tool</code></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;script</code></dt>
<dd> run an mtx script (lua preferred method) (&#8211;noquotes), no script gives list</dd>
<dt><code>&#8211;evaluate</code></dt>
<dd> run code passed on the commandline (between quotes) (=loop) (exit|quit aborts)</dd>
<dt><code>&#8211;execute</code></dt>
<dd> run a script or program (texmfstart method) (&#8211;noquotes)</dd>
<dt><code>&#8211;resolve</code></dt>
<dd> resolve prefixed arguments</dd>
<dt><code>&#8211;ctxlua</code></dt>
<dd> run internally (using preloaded libs)</dd>
<dt><code>&#8211;internal</code></dt>
<dd> run script using built in libraries (same as &#8211;ctxlua)</dd>
<dt><code>&#8211;locate</code></dt>
<dd> locate given filename in database (default) or system (&#8211;first &#8211;all &#8211;detail)</dd>
<dt><code>&#8211;tree=pathtotree</code></dt>
<dd> use given texmf tree (default file: setuptex.tmf)</dd>
<dt><code>&#8211;path=runpath</code></dt>
<dd> go to given path before execution</dd>
<dt><code>&#8211;ifchanged=filename</code></dt>
<dd> only execute when given file has changed (md checksum)</dd>
<dt><code>&#8211;iftouched=old,new</code></dt>
<dd> only execute when given file has changed (time stamp)</dd>
<dt><code>&#8211;makestubs</code></dt>
<dd> create stubs for (context related) scripts</dd>
<dt><code>&#8211;removestubs</code></dt>
<dd> remove stubs (context related) scripts</dd>
<dt><code>&#8211;stubpath=binpath</code></dt>
<dd> paths where stubs wil be written</dd>
<dt><code>&#8211;windows</code></dt>
<dd> create windows (mswin) stubs</dd>
<dt><code>&#8211;unix</code></dt>
<dd> create unix (linux) stubs</dd>
<dt><code>&#8211;addbinarypath</code></dt>
<dd> prepend the (found) binarypath to runners</dd>
<dt><code>&#8211;verbose</code></dt>
<dd> give a bit more info</dd>
<dt><code>&#8211;trackers=list</code></dt>
<dd> enable given trackers</dd>
<dt><code>&#8211;progname=str</code></dt>
<dd> format or backend</dd>
<dt><code>&#8211;systeminfo=str</code></dt>
<dd> show current operating system, processor, etc</dd>
<dt><code>&#8211;edit</code></dt>
<dd> launch editor with found file</dd>
<dt><code>&#8211;launch</code></dt>
<dd> launch files like manuals, assumes os support (&#8211;all,&#8211;list)</dd>
<dt><code>&#8211;timedrun</code></dt>
<dd> run a script and time its run</dd>
<dt><code>&#8211;autogenerate</code></dt>
<dd> regenerate databases if needed (handy when used to run context in an editor)</dd>
<dt><code>&#8211;usekpse</code></dt>
<dd> use kpse as fallback (when no mkiv and cache installed, often slower)</dd>
<dt><code>&#8211;forcekpse</code></dt>
<dd> force using kpse (handy when no mkiv and cache installed but less functionality)</dd>
<dt><code>&#8211;prefixes</code></dt>
<dd> show supported prefixes</dd>
<dt><code>&#8211;generate</code></dt>
<dd> generate file database</dd>
<dt><code>&#8211;variables</code></dt>
<dd> show configuration variables</dd>
<dt><code>&#8211;configurations</code></dt>
<dd> show configuration order</dd>
<dt><code>&#8211;directives</code></dt>
<dd> show (known) directives</dd>
<dt><code>&#8211;trackers</code></dt>
<dd> show (known) trackers</dd>
<dt><code>&#8211;experiments</code></dt>
<dd> show (known) experiments</dd>
<dt><code>&#8211;expand-braces</code></dt>
<dd> expand complex variable</dd>
<dt><code>&#8211;resolve-path</code></dt>
<dd> expand variable (completely resolve paths)</dd>
<dt><code>&#8211;expand-path</code></dt>
<dd> expand variable (resolve paths)</dd>
<dt><code>&#8211;expand-var</code></dt>
<dd> expand variable (resolve references)</dd>
<dt><code>&#8211;show-path</code></dt>
<dd> show path expansion of &#8230;</dd>
<dt><code>&#8211;var-value</code></dt>
<dd> report value of variable</dd>
<dt><code>&#8211;find-file</code></dt>
<dd> report file location</dd>
<dt><code>&#8211;find-path</code></dt>
<dd> report path of file</dd>
<dt><code>&#8211;pattern=string</code></dt>
<dd> filter variables</dd></dl>
<h2>AUTHOR</h2>
<p> More information about ConTeXt and the tools that come with it can be found at: </p>
<p> <code>maillist:</code> ntg-context [at] ntg.nl / <a rel="nofollow" href="http://www.ntg.nl/mailman/listinfo/ntg-context">http://www.ntg.nl/mailman/listinfo/ntg-context</a> </p>
<p> <code>webpage:</code> <a rel="nofollow" href="http://www.pragma-ade.nl">http://www.pragma-ade.nl</a> / <a rel="nofollow" href="http://tex.aanhet.net">http://tex.aanhet.net</a> </p>
<p> <code>wiki:</code> <a rel="nofollow" href="http://contextgarden.net">http://contextgarden.net</a> </p>
