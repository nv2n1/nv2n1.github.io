---

title: "context(1)"
name: "context"
section: "1"
letter: "c"
url: "/docs/linux/man/1-context/"
description: "mtx-context – ConTeXt Process Management"
---

<p> <code>mtxrun &#8211;script context [</code> <i>OPTIONS &#8230;</i> <code>] [</code> <i>FILENAMES</i> <code>]</code></p>
<p> <code>ConTeXt Process Management</code></p>
<h2>OPTIONS: BASIC</h2>
<dl>
<dt><code>&#8211;run</code></dt>
<dd> process (one or more) files (default action)</dd>
<dt><code>&#8211;make</code></dt>
<dd> create context formats</dd>
<dt><code>&#8211;ctx=name</code></dt>
<dd> use ctx file (process management specification)</dd>
<dt><code>&#8211;noctx</code></dt>
<dd> ignore ctx directives and flags</dd>
<dt><code>&#8211;interface</code></dt>
<dd> use specified user interface (default: en)</dd>
<dt><code>&#8211;autopdf</code></dt>
<dd> close pdf file in viewer and start pdf viewer afterwards</dd>
<dt><code>&#8211;purge</code></dt>
<dd> purge files either or not after a run (&#8211;pattern=&#8230;)</dd>
<dt><code>&#8211;purgeall</code></dt>
<dd> purge all files either or not after a run (&#8211;pattern=&#8230;)</dd>
<dt><code>&#8211;usemodule=list</code></dt>
<dd> load the given module or style, normally part of the distribution</dd>
<dt><code>&#8211;environment=list</code></dt>
<dd> load the given environment file first (document styles)</dd>
<dt><code>&#8211;mode=list</code></dt>
<dd> enable given the modes (conditional processing in styles)</dd>
<dt><code>&#8211;path=list</code></dt>
<dd> also consult the given paths when files are looked for</dd>
<dt><code>&#8211;arguments=list</code></dt>
<dd> set variables that can be consulted during a run (key/value pairs)</dd>
<dt><code>&#8211;randomseed=number</code></dt>
<dd> set the randomseed</dd>
<dt><code>&#8211;result=name</code></dt>
<dd> rename the resulting output to the given name</dd>
<dt><code>&#8211;trackers=list</code></dt>
<dd> set tracker variables (show list with &#8211;showtrackers)</dd>
<dt><code>&#8211;directives=list</code></dt>
<dd> set directive variables (show list with &#8211;showdirectives)</dd>
<dt><code>&#8211;silent=list</code></dt>
<dd> disable logcatgories (show list with &#8211;showlogcategories)</dd>
<dt><code>&#8211;strip</code></dt>
<dd> strip Lua code (only meant for production where no errors are expected)</dd>
<dt><code>&#8211;errors=list</code></dt>
<dd> show errors at the end of a run, quit when in list (also when &#8211;silent)</dd>
<dt><code>&#8211;htmlerrorpage</code></dt>
<dd> generate html error page instead (optional: =scite)</dd>
<dt><code>&#8211;noconsole</code></dt>
<dd> disable logging to the console (logfile only)</dd>
<dt><code>&#8211;nodummy</code></dt>
<dd> don&#8217;t create a dummy file (can confuse pdf viewers that keep file in view)</dd>
<dt><code>&#8211;purgeresult</code></dt>
<dd> purge result file before run</dd>
<dt><code>&#8211;forcexml</code></dt>
<dd> force xml stub</dd>
<dt><code>&#8211;forcecld</code></dt>
<dd> force cld (context lua document) stub</dd>
<dt><code>&#8211;forcelua</code></dt>
<dd> force lua stub (like texlua)</dd>
<dt><code>&#8211;forcemp</code></dt>
<dd> force mp stub</dd>
<dt><code>&#8211;arrange</code></dt>
<dd> run extra imposition pass, given that the style sets up imposition</dd>
<dt><code>&#8211;noarrange</code></dt>
<dd> ignore imposition specifications in the style</dd>
<dt><code>&#8211;pages</code></dt>
<dd> report pagenumbers of names pages and list references (&#8211;page=&#8230; or &#8211;page=&#8230;)</dd>
<dt><code>&#8211;jit</code></dt>
<dd> use luajittex with jit turned off (only use the faster virtual machine)</dd>
<dt><code>&#8211;jiton</code></dt>
<dd> use luajittex with jit turned on (in most cases not faster, even slower)</dd>
<dt><code>&#8211;once</code></dt>
<dd> only run once (no multipass data file is produced)</dd>
<dt><code>&#8211;runs</code></dt>
<dd> process at most this many times</dd>
<dt><code>&#8211;forcedruns</code></dt>
<dd> process this many times (permits for optimization trial runs)</dd>
<dt><code>&#8211;batchmode</code></dt>
<dd> run without stopping and do not show messages on the console</dd>
<dt><code>&#8211;nonstopmode</code></dt>
<dd> run without stopping</dd>
<dt><code>&#8211;nosynctex</code></dt>
<dd> never initializes synctex (for production runs)</dd>
<dt><code>&#8211;synctex</code></dt>
<dd> run with synctex enabled (better use \setupsynctex[state=start]</dd>
<dt><code>&#8211;nodates</code></dt>
<dd> omit runtime dates in pdf file (optional value: a number (this 1970 offset time) or string &quot;YYYY-MM-DD HH:MM&quot;)</dd>
<dt><code>&#8211;nocompression</code></dt>
<dd> forcefully turns off compression in the backend</dd>
<dt><code>&#8211;trailerid</code></dt>
<dd> alternative trailer id (or constant one)</dd>
<dt><code>&#8211;generate</code></dt>
<dd> generate file database etc. (as luatools does)</dd>
<dt><code>&#8211;paranoid</code></dt>
<dd> do not descend to .. and ../..</dd>
<dt><code>&#8211;version</code></dt>
<dd> report installed context version</dd>
<dt><code>&#8211;global</code></dt>
<dd> assume given file present elsewhere</dd>
<dt><code>&#8211;nofile</code></dt>
<dd> use dummy file as jobname</dd></dl>
<h2>OPTIONS: EXPERT</h2>
<dl>
<dt><code>&#8211;touch</code></dt>
<dd> update context version number (also provide &#8211;expert, optionally provide &#8211;basepath)</dd>
<dt><code>&#8211;nostatistics</code></dt>
<dd> omit runtime statistics at the end of the run</dd>
<dt><code>&#8211;profile</code></dt>
<dd> profile job (use: mtxrun &#8211;script profile &#8211;analyze)</dd>
<dt><code>&#8211;timing</code></dt>
<dd> generate timing and statistics overview</dd>
<dt><code>&#8211;keeptuc</code></dt>
<dd> keep previous tuc files (jobname-tuc-[run].tmp)</dd>
<dt><code>&#8211;keeplog</code></dt>
<dd> keep previous log files (jobname-log-[run].tmp)</dd>
<dt><code>&#8211;lmtx</code></dt>
<dd> force lmtx mode (when available)</dd>
<dt><code>&#8211;overloadmode=error|warning|0&#8211;6|255</code></dt>
<dd> enable csname overload checking</dd>
<dt><code>&#8211;extra=name</code></dt>
<dd> process extra (mtx-context-&#8230; in distribution)</dd>
<dt><code>&#8211;extras</code></dt>
<dd> show extras</dd></dl>
<h2>OPTIONS: SPECIAL</h2>
<dl>
<dt><code>&#8211;pdftex</code></dt>
<dd> process file with texexec using pdftex</dd>
<dt><code>&#8211;xetex</code></dt>
<dd> process file with texexec using xetex</dd>
<dt><code>&#8211;mkii</code></dt>
<dd> process file with texexec</dd>
<dt><code>&#8211;pipe</code></dt>
<dd> do not check for file and enter scroll mode (&#8211;dummyfile=whatever.tmp)</dd>
<dt><code>&#8211;sandbox</code></dt>
<dd> process file in a limited environment</dd>
<dt><code>&#8211;addbinarypath</code></dt>
<dd> prepend the (found) binarypath to runners</dd></dl>
<h2>AUTHOR</h2>
<p> More information about ConTeXt and the tools that come with it can be found at: </p>
<p> <code>maillist:</code> ntg-context [at] ntg.nl / <a rel="nofollow" href="http://www.ntg.nl/mailman/listinfo/ntg-context">http://www.ntg.nl/mailman/listinfo/ntg-context</a> </p>
<p> <code>webpage:</code> <a rel="nofollow" href="http://www.pragma-ade.nl">http://www.pragma-ade.nl</a> / <a rel="nofollow" href="http://tex.aanhet.net">http://tex.aanhet.net</a> </p>
<p> <code>wiki:</code> <a rel="nofollow" href="http://contextgarden.net">http://contextgarden.net</a> </p>
