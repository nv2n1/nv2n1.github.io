---
title: "context(1)"
name: "context"
section: "1"
letter: "c"
url: "/docs/linux/man/1-context/"
description: "mtx-context – ConTeXt Process Management"
---

<h2 class="name">NAME</h2>
<p>&nbsp;mtx-context &#8211; ConTeXt Process Management </p>
<h2>SYNOPSIS</h2>
<p> <code>mtxrun &#8211;script context [</code> <i>OPTIONS &#8230;</i> <code>] [</code> <i>FILENAMES</i> <code>]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>ConTeXt Process Management</code></p>
<h2>OPTIONS: BASIC</h2>
<dl>
<dt><code>&#8211;run</code></p>
<dd> process (one or more) files (default action)</p>
<dt><code>&#8211;make</code></p>
<dd> create context formats</p>
<dt><code>&#8211;ctx=name</code></p>
<dd> use ctx file (process management specification)</p>
<dt><code>&#8211;noctx</code></p>
<dd> ignore ctx directives and flags</p>
<dt><code>&#8211;interface</code></p>
<dd> use specified user interface (default: en)</p>
<dt><code>&#8211;autopdf</code></p>
<dd> close pdf file in viewer and start pdf viewer afterwards</p>
<dt><code>&#8211;purge</code></p>
<dd> purge files either or not after a run (&#8211;pattern=&#8230;)</p>
<dt><code>&#8211;purgeall</code></p>
<dd> purge all files either or not after a run (&#8211;pattern=&#8230;)</p>
<dt><code>&#8211;usemodule=list</code></p>
<dd> load the given module or style, normally part of the distribution</p>
<dt><code>&#8211;environment=list</code></p>
<dd> load the given environment file first (document styles)</p>
<dt><code>&#8211;mode=list</code></p>
<dd> enable given the modes (conditional processing in styles)</p>
<dt><code>&#8211;path=list</code></p>
<dd> also consult the given paths when files are looked for</p>
<dt><code>&#8211;arguments=list</code></p>
<dd> set variables that can be consulted during a run (key/value pairs)</p>
<dt><code>&#8211;randomseed=number</code></p>
<dd> set the randomseed</p>
<dt><code>&#8211;result=name</code></p>
<dd> rename the resulting output to the given name</p>
<dt><code>&#8211;trackers=list</code></p>
<dd> set tracker variables (show list with &#8211;showtrackers)</p>
<dt><code>&#8211;directives=list</code></p>
<dd> set directive variables (show list with &#8211;showdirectives)</p>
<dt><code>&#8211;silent=list</code></p>
<dd> disable logcatgories (show list with &#8211;showlogcategories)</p>
<dt><code>&#8211;strip</code></p>
<dd> strip Lua code (only meant for production where no errors are expected)</p>
<dt><code>&#8211;errors=list</code></p>
<dd> show errors at the end of a run, quit when in list (also when &#8211;silent)</p>
<dt><code>&#8211;htmlerrorpage</code></p>
<dd> generate html error page instead (optional: =scite)</p>
<dt><code>&#8211;noconsole</code></p>
<dd> disable logging to the console (logfile only)</p>
<dt><code>&#8211;nodummy</code></p>
<dd> don&#8217;t create a dummy file (can confuse pdf viewers that keep file in view)</p>
<dt><code>&#8211;purgeresult</code></p>
<dd> purge result file before run</p>
<dt><code>&#8211;forcexml</code></p>
<dd> force xml stub</p>
<dt><code>&#8211;forcecld</code></p>
<dd> force cld (context lua document) stub</p>
<dt><code>&#8211;forcelua</code></p>
<dd> force lua stub (like texlua)</p>
<dt><code>&#8211;forcemp</code></p>
<dd> force mp stub</p>
<dt><code>&#8211;arrange</code></p>
<dd> run extra imposition pass, given that the style sets up imposition</p>
<dt><code>&#8211;noarrange</code></p>
<dd> ignore imposition specifications in the style</p>
<dt><code>&#8211;pages</code></p>
<dd> report pagenumbers of names pages and list references (&#8211;page=&#8230; or &#8211;page=&#8230;)</p>
<dt><code>&#8211;jit</code></p>
<dd> use luajittex with jit turned off (only use the faster virtual machine)</p>
<dt><code>&#8211;jiton</code></p>
<dd> use luajittex with jit turned on (in most cases not faster, even slower)</p>
<dt><code>&#8211;once</code></p>
<dd> only run once (no multipass data file is produced)</p>
<dt><code>&#8211;runs</code></p>
<dd> process at most this many times</p>
<dt><code>&#8211;forcedruns</code></p>
<dd> process this many times (permits for optimization trial runs)</p>
<dt><code>&#8211;batchmode</code></p>
<dd> run without stopping and do not show messages on the console</p>
<dt><code>&#8211;nonstopmode</code></p>
<dd> run without stopping</p>
<dt><code>&#8211;nosynctex</code></p>
<dd> never initializes synctex (for production runs)</p>
<dt><code>&#8211;synctex</code></p>
<dd> run with synctex enabled (better use \setupsynctex[state=start]</p>
<dt><code>&#8211;nodates</code></p>
<dd> omit runtime dates in pdf file (optional value: a number (this 1970 offset time) or string &quot;YYYY-MM-DD HH:MM&quot;)</p>
<dt><code>&#8211;nocompression</code></p>
<dd> forcefully turns off compression in the backend</p>
<dt><code>&#8211;trailerid</code></p>
<dd> alternative trailer id (or constant one)</p>
<dt><code>&#8211;generate</code></p>
<dd> generate file database etc. (as luatools does)</p>
<dt><code>&#8211;paranoid</code></p>
<dd> do not descend to .. and ../..</p>
<dt><code>&#8211;version</code></p>
<dd> report installed context version</p>
<dt><code>&#8211;global</code></p>
<dd> assume given file present elsewhere</p>
<dt><code>&#8211;nofile</code></p>
<dd> use dummy file as jobname</dl>
<h2>OPTIONS: EXPERT</h2>
<dl>
<dt><code>&#8211;touch</code></p>
<dd> update context version number (also provide &#8211;expert, optionally provide &#8211;basepath)</p>
<dt><code>&#8211;nostatistics</code></p>
<dd> omit runtime statistics at the end of the run</p>
<dt><code>&#8211;profile</code></p>
<dd> profile job (use: mtxrun &#8211;script profile &#8211;analyze)</p>
<dt><code>&#8211;timing</code></p>
<dd> generate timing and statistics overview</p>
<dt><code>&#8211;keeptuc</code></p>
<dd> keep previous tuc files (jobname-tuc-[run].tmp)</p>
<dt><code>&#8211;keeplog</code></p>
<dd> keep previous log files (jobname-log-[run].tmp)</p>
<dt><code>&#8211;lmtx</code></p>
<dd> force lmtx mode (when available)</p>
<dt><code>&#8211;overloadmode=error|warning|0&#8211;6|255</code></p>
<dd> enable csname overload checking</p>
<dt><code>&#8211;extra=name</code></p>
<dd> process extra (mtx-context-&#8230; in distribution)</p>
<dt><code>&#8211;extras</code></p>
<dd> show extras</dl>
<h2>OPTIONS: SPECIAL</h2>
<dl>
<dt><code>&#8211;pdftex</code></p>
<dd> process file with texexec using pdftex</p>
<dt><code>&#8211;xetex</code></p>
<dd> process file with texexec using xetex</p>
<dt><code>&#8211;mkii</code></p>
<dd> process file with texexec</p>
<dt><code>&#8211;pipe</code></p>
<dd> do not check for file and enter scroll mode (&#8211;dummyfile=whatever.tmp)</p>
<dt><code>&#8211;sandbox</code></p>
<dd> process file in a limited environment</p>
<dt><code>&#8211;addbinarypath</code></p>
<dd> prepend the (found) binarypath to runners</dl>
<h2>AUTHOR</h2>
<p> More information about ConTeXt and the tools that come with it can be found at: </p>
<p> <code>maillist:</code> ntg-context [at] ntg.nl / <a rel="nofollow" href="http://www.ntg.nl/mailman/listinfo/ntg-context">http://www.ntg.nl/mailman/listinfo/ntg-context</a> </p>
<p> <code>webpage:</code> <a rel="nofollow" href="http://www.pragma-ade.nl">http://www.pragma-ade.nl</a> / <a rel="nofollow" href="http://tex.aanhet.net">http://tex.aanhet.net</a> </p>
<p> <code>wiki:</code> <a rel="nofollow" href="http://contextgarden.net">http://contextgarden.net</a> </p>
<h2>Index</h2>
