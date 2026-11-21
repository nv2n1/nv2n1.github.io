---
title: "luaotfload-tool(1)"
name: "luaotfload-tool"
section: "1"
letter: "l"
url: "/docs/linux/man/1-luaotfload-tool/"
description: "luaotfload-tool – generate and query the Luaotfload font names database"
---

<h2>SYNOPSIS</h2>
<p> <code>luaotfload-tool</code> [ -bcDfFiIlLnpqRSuvVhw ]</p>
<dl>
<dt><code>luaotfload-tool</code> &#8211;update [ &#8211;force ] [ &#8211;quiet ] [ &#8211;verbose ]</dt>
<dd> [ &#8211;prefer-texmf ] [ &#8211;dry-run ] [ &#8211;formats=[+|-]EXTENSIONS ] [ &#8211;no-compress ] [ &#8211;no-strip ] [ &#8211;local ] [ &#8211;max-fonts=N ]</dd>
<dt><code>luaotfload-tool</code> &#8211;find=FONTNAME [ &#8211;fuzzy ] [ &#8211;info ] [ &#8211;inspect ]</dt>
<dd> [ &#8211;no-reload ] </dd>
<p> <code>luaotfload-tool</code> &#8211;flush-lookups </p>
<p> <code>luaotfload-tool</code> &#8211;cache=DIRECTIVE </p>
<p> <code>luaotfload-tool</code> &#8211;list=CRITERION[:VALUE] [ &#8211;fields=F1,F2,&#8230;,Fn ] </p>
<p> <code>luaotfload-tool</code> &#8211;bisect=DIRECTIVE </p>
<p> <code>luaotfload-tool</code> &#8211;help </p>
<p> <code>luaotfload-tool</code> &#8211;version </p>
<p> <code>luaotfload-tool</code> &#8211;show-blacklist </p>
<p> <code>luaotfload-tool</code> &#8211;diagnose=CHECK </p>
<p> <code>luaotfload-tool</code> &#8211;conf=FILE &#8211;dumpconf</dl>
<h2>DESCRIPTION</h2>
<p> luaotfload-tool accesses the font names database that is required by the <i>Luaotfload</i> package. There are two general modes: <code>update</code> and <code>query</code>.</p>
<dl>
<dt>&bull;</dt>
<dd> <code>update</code>: update the database or rebuild it entirely;</dd>
<dt>&bull;</dt>
<dd> <code>query</code>: resolve a font name or display close matches.</dd></dl>
<h2>OPTIONS</h2>
<h3>update mode</h3>
<dl>
<dt><code>&#8211;update</code>,<code> -u</code></dt>
<dd> Update the database; indexes new fonts.</dd>
<dt><code>&#8211;force</code>,<code> -f</code></dt>
<dd> Force rebuilding of the database; re-indexes all fonts.</dd>
<dt><code>&#8211;local</code>,<code> -L</code></dt>
<dd> Include font files in <code>$PWD</code>. This option will cause large parts of the database to be rebuilt. Thus it is quite inefficient. Additionally, if local font files are found, the database is prevented from being saved to disk, so the local fonts need to be parsed with every invocation of <code>luaotfload-tool</code>.</dd>
<dt><code>&#8211;no-reload</code>,<code> -n</code></dt>
<dd> Suppress auto-updates to the database (e.g. when <code>&#8211;find</code> is passed an unknown name).</dd>
<dt><code>&#8211;no-compress</code>,<code> -c</code></dt>
<dd> Do not filter the plain text version of the font index through gzip. Useful for debugging if your editor is built without zlib.</dd>
<dt><code>&#8211;prefer-texmf</code>,<code> -p</code></dt>
<dd> Organize the file name database in a way so that it prefer fonts in the <i>TEXMF</i> tree over system fonts if they are installed in both.</dd>
<dt><code>&#8211;formats=</code><i>EXTENSIONS</i></dt>
<dd> Extensions of the font files to index. Where <i>EXTENSIONS</i> is a comma-separated list of supported file extensions (otf, ttf, ttc). If the list is prefixed with a <code>+</code> sign, the given list is added to the currently active one; <code>&#8211;</code> subtracts. Default: <i>otf,ttf,ttc</i>. Examples:</dd>
<dt>1.</dt>
<dd> <code>&#8211;formats=-ttc,ttf</code> would skip TrueType fonts and font collections;</dd>
<dt>2.</dt>
<dd> <code>&#8211;formats=otf</code> would scan only OpenType files;</dd>
<dt>3.</dt>
<dd> <code>&#8211;formats=+afm</code> includes binary Postscript files accompanied by an AFM file.</dd></dl>
<h3>query mode</h3>
<dl>
<dt><code>&#8211;find=</code><i>NAME</i></dt>
<dd> Resolve a font name; this looks up &lt;name&gt; in the database and prints the file name it is mapped to. <code>&#8211;find</code> also understands request syntax, i.e. <code>&#8211;find=file:foo.otf</code> checks whether <code>foo.otf</code> is indexed.</dd>
<dt><code>&#8211;fuzzy</code>,<code> -F</code></dt>
<dd> Show approximate matches to the file name if the lookup was unsuccessful (requires <code>&#8211;find</code>).</dd>
<dt><code>&#8211;info</code>,<code> -i</code></dt>
<dd> Display basic information to a resolved font file (requires <code>&#8211;find</code>).</dd>
<dt><code>&#8211;inspect</code>,<code> -I</code></dt>
<dd> Display detailed information by loading the font and analyzing the font table; very slow! For the meaning of the returned fields see the LuaTeX documentation. (requires <code>&#8211;find</code>).</dd>
<dt><code>&#8211;list=</code><i>CRITERION</i></dt>
<dd> Show entries, where <i>CRITERION</i> is one of the following:</dd>
<dt>1.</dt>
<dd> the character <code>*</code>, selecting all entries;</dd>
<dt>2.</dt>
<dd> a field of a database entry, for instance <i>version</i> or <i>format*</i>, according to which the output will be sorted. Information in an unstripped database (see the option <code>&#8211;no-strip</code> above) is nested: Subfields of a record can be addressed using the <code>-&gt;</code> separator, e. g. <code>file-&gt;location</code>, <code>style-&gt;units_per_em</code>, or <code>names-&gt;sanitized-&gt;english-&gt;prefmodifiers</code>. NB: shell syntax requires that arguments containing <code>-&gt;</code> be properly quoted!</dd>
<dt>3.</dt>
<dd> an expression of the form <code>field:value</code> to limit the output to entries whose <code>field</code> matches <code>value</code>. The <code>value</code> can contain <code>*</code> to match an arbitrary number of characters. </dd>
<p> For example, in order to output file names and corresponding versions, sorted by the font format: </p>
<pre>
./luaotfload-tool.lua --list=&quot;format&quot; --fields=&quot;file-&gt;base,version&quot;
</pre>
<p> This prints: </p>
<pre>
otf latinmodern-math.otf  Version 1.958
otf lmromancaps10-oblique.otf 2.004
otf lmmono8-regular.otf 2.004
otf lmmonoproplt10-bold.otf 2.004
otf lmsans10-oblique.otf  2.004
otf lmromanslant8-regular.otf 2.004
otf lmroman12-italic.otf  2.004
otf lmsansdemicond10-oblique.otf  2.004
...
</pre>
<dt><code>&#8211;fields=</code><i>FIELDS</i></dt>
<dd> Comma-separated list of fields that should be printed. Information in an unstripped database (see the option <code>&#8211;no-strip</code> above) is nested: Subfields of a record can be addressed using the <code>-&gt;</code> separator, e. g. <code>file-&gt;location</code>, <code>style-&gt;units_per_em</code>, or <code>names-&gt;sanitized-&gt;english-&gt;subfamily</code>. The default is plainname,version*. (Only meaningful with <code>&#8211;list</code>.)</dd></dl>
<h3>font and lookup caches</h3>
<dl>
<dt><code>&#8211;flush-lookups</code></dt>
<dd> Clear font name lookup cache (experimental).</dd>
<dt><code>&#8211;cache=</code><i>DIRECTIVE</i></dt>
<dd> Cache control, where <i>DIRECTIVE</i> is one of the following:</dd>
<dt>1.</dt>
<dd> <code>purge</code> -&gt; delete Lua files from cache;</dd>
<dt>2.</dt>
<dd> <code>erase</code> -&gt; delete Lua and Luc files from cache;</dd>
<dt>3.</dt>
<dd> <code>show</code> -&gt; print stats.</dd></dl>
<h3>debugging methods</h3>
<dl>
<dt><code>&#8211;show-blacklist</code>,<code> -b</code></dt>
<dd> Show blacklisted files (not directories).</dd>
<dt><code>&#8211;dry-run</code>,<code> -D</code></dt>
<dd> Don’t load fonts when updating the database; scan directories only. (For debugging file system related issues.)</dd>
<dt><code>&#8211;no-strip</code></dt>
<dd> Do not strip redundant information after building the database. Warning: this will inflate the index to about two to three times the normal size.</dd>
<dt><code>&#8211;max-fonts=</code><i>N</i></dt>
<dd> Process at most <i>N</i> font files, including fonts already indexed in the count.</dd>
<dt><code>&#8211;bisect=</code><i>DIRECTIVE</i></dt>
<dd> Bisection of the font database. This mode is intended as assistance in debugging the Luatex engine, especially when tracking memleaks or buggy fonts. </dd>
<p> <i>DIRECTIVE</i> can be one of the following:</p>
<dt>1.</dt>
<dd> <code>run</code> -&gt; Make <code>luaotfload-tool</code> respect the bisection progress when running. Combined with <code>&#8211;update</code> and possibly <code>&#8211;force</code> this will only process the files from the start up until the pivot and ignore the rest.</dd>
<dt>2.</dt>
<dd> <code>start</code> -&gt; Start bisection: create a bisection state file and initialize the low, high, and pivot indices.</dd>
<dt>3.</dt>
<dd> <code>stop</code> -&gt; Terminate the current bisection session by deleting the state file.</dd>
<dt>4.</dt>
<dd> <code>good</code> | <code>bad</code> -&gt; Mark the section processed last as “good” or “bad”, respectively. The next bisection step will continue with the bad section.</dd>
<dt>5.</dt>
<dd> <code>status</code> -&gt; Print status information about the current bisection session. Hint: Use with higher verbosity settings for more output. </dd>
<p> A bisection session is initiated by issuing the <code>start</code> directive. This sets the pivot to the middle of the list of available font files. Now run <i>luaotfload-tool</i> with the <code>&#8211;update</code> flag set as well as <code>&#8211;bisect=run</code>: only the fonts up to the pivot will be considered. If that task exhibited the issue you are tracking, then tell Luaotfload using <code>&#8211;bisect=bad</code>. The next step of <code>&#8211;bisect=run</code> will continue bisection with the part of the files below the pivot. Likewise, issue <code>&#8211;bisect=good</code> in order to continue with the fonts above the pivot, assuming the tested part of the list did not trigger the bug. </p>
<p> Once the culprit font is tracked down, <code>good</code> or <code>bad</code> will have no effect anymore. <code>run</code> will always end up processing the single font file that was left. Use <code>&#8211;bisect=stop</code> to clear the bisection state.</dl>
<h3>miscellaneous</h3>
<dl>
<dt><code>&#8211;verbose=</code><i>N</i>,<code>&nbsp;-v</code></dt>
<dd> Set verbosity level to <i>n</i> or the number of repetitions of <code>-v</code>.</dd>
<dt><code>&#8211;quiet</code></dt>
<dd> No verbose output (log level set to zero).</dd>
<dt><code>&#8211;log=</code><i>CHANNEL</i></dt>
<dd> Redirect log output (for database troubleshooting), where <i>CHANNEL</i> can be</dd>
<dt>1.</dt>
<dd> <code>stdout</code> -&gt; all output will be dumped to the terminal (default); or</dd>
<dt>2.</dt>
<dd> <code>file</code> -&gt; write to a file to the temporary directory (the name will be chosen automatically.</dd>
<dt><code>&#8211;version</code>,<code> -V</code></dt>
<dd> Show version numbers of components as well as some basic information and exit.</dd>
<dt><code>&#8211;help</code>,<code> -h</code></dt>
<dd> Show help message and exit.</dd>
<dt><code>&#8211;diagnose=</code><i>CHECK</i></dt>
<dd> Run the diagnostic procedure <i>CHECK</i>. Available procedures are:</dd>
<dt>1.</dt>
<dd> <code>files</code> -&gt; check <i>Luaotfload</i> files for modifications;</dd>
<dt>2.</dt>
<dd> <code>permissions</code> -&gt; check permissions of cache directories and files;</dd>
<dt>3.</dt>
<dd>
</dd><dt><code>environment</code> -&gt; print relevant</dt>
<dd> environment and kpse variables;</dd>
<dt>4.</dt>
<dd> <code>repository</code> -&gt; check the git repository for new releases,</dd>
<dt>5.</dt>
<dd> <code>index</code> -&gt; check database, display information about it. </dd>
<p> Procedures can be chained by concatenating with commas, e.g. <code>&#8211;diagnose=files,permissions</code>. Specify <code>thorough</code> to run all checks.</p>
<dt><code>&#8211;conf=</code><i>FILE</i></dt>
<dd> Read the configuration from <i>FILE</i>. See <code>luaotfload.conf</code>(%) for documentation concerning the format and available options.</dd>
<dt><code>&#8211;dumpconf</code></dt>
<dd> Print the currently active configuration; the output can be saved to a file and used for bootstrapping a custom configuration files.</dd>
<dt><code>&#8211;aliases</code></dt>
<dd> Dump the font name database as a kpathsea aliases file. This option is experimental and might go away.</dd></dl>
<h2>FILES</h2>
<p> The font name database is usually located in the directory <code>texmf-var/luatex-cache/generic/names/</code> (<code>$TEXMFCACHE</code> as set in <code>texmf.cnf</code>) of your <i>TeX Live</i> distribution as a zlib-compressed file <code>luaotfload-names.lua.gz</code>. The experimental lookup cache will be created as <code>luaotfload-lookup-cache.lua</code> in the same directory. These Lua tables are not used directly by Luaotfload, though. Instead, they are compiled to Lua bytecode which is written to corresponding files with the extension <code>.luc</code> in the same directory. When modifying the files by hand keep in mind that only if the bytecode files are missing will Luaotfload use the plain version instead. Both kinds of files are safe to delete, at the cost of regenerating them with the next run of <i>LuaTeX</i>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-luaotfload-conf/">luaotfload.conf</a></code>(5), <code><a href="/docs/linux/man/1-luatex/">luatex</a></code>(1), <code><a href="/docs/linux/man/1-lua/">lua</a></code>(1)</p>
<dl>
<dt>&bull;</dt>
<dd> <code>texdoc luaotfload</code> to display the manual for the <i>Luaotfload</i> package</dd>
<dt>&bull;</dt>
<dd> Luaotfload development <i><a rel="nofollow" href="https://github.com/latex3/luaotfload">https://github.com/latex3/luaotfload</a></i></dd>
<dt>&bull;</dt>
<dd> LuaLaTeX mailing list <i><a rel="nofollow" href="http://tug.org/pipermail/lualatex-dev/">http://tug.org/pipermail/lualatex-dev/</a></i></dd>
<dt>&bull;</dt>
<dd> LuaTeX <i><a rel="nofollow" href="http://luatex.org/">http://luatex.org/</a></i></dd>
<dt>&bull;</dt>
<dd> ConTeXt <i><a rel="nofollow" href="http://wiki.contextgarden.net">http://wiki.contextgarden.net</a></i></dd>
<dt>&bull;</dt>
<dd> Luaotfload on CTAN <i><a rel="nofollow" href="http://ctan.org/pkg/luaotfload">http://ctan.org/pkg/luaotfload</a></i></dd></dl>
<h2>BUGS</h2>
<p> Tons, probably.</p>
<h2>AUTHORS</h2>
<p> <i>Luaotfload</i> was developed by the LuaLaTeX dev team (<i><a rel="nofollow" href="https://github.com/lualatex/">https://github.com/lualatex/</a></i>). It is currently maintained by the LaTeX Project Team at <i><a rel="nofollow" href="https://github.com/latex3/luaotfload">https://github.com/latex3/luaotfload</a></i> The fontloader code is provided by Hans Hagen of Pragma ADE, Hasselt NL (<i><a rel="nofollow" href="http://pragma-ade.com/">http://pragma-ade.com/</a></i>). </p>
<p> This manual page was written by Philipp Gesang &lt;<i>phg [at] phi-gamma.net</i>&gt;.</p>
<h2>COPYRIGHT</h2>
<p> GPL v2.0 </p>
