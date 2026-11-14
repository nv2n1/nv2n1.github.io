---
title: "luaotfload-conf(5)"
name: "luaotfload-conf"
section: "5"
letter: "l"
url: "/docs/linux/man/5-luaotfload-conf/"
description: "luaotfload.conf – Luaotfload configuration file"
---

<p>luaotfload.conf &#8211; Luaotfload configuration file</p>
<h2>Synopsis</h2>
<dl>
<dt>&bull;</p>
<dd><code>./luaotfload{.conf,rc}</code></p>
<dt>&bull;</p>
<dd><code>XDG_CONFIG_HOME/luaotfload/luaotfload{.conf,rc}</code></p>
<dt>&bull;</p>
<dd><code>~/.luaotfloadrc</code></dl>
<h2>Description</h2>
<p>The file <code>luaotfload.conf</code> contains configuration options for <i>Luaotfload</i>, a font loading and font management component for LuaTeX.</p>
<h2>Example</h2>
<p>A small Luaotfload configuration file with few customizations could look as follows: </p>
<pre>[db]
 formats = afm,ttf
 compress = false
[misc]
 termwidth = 60
[run]
 log-level = 6</pre>
<p>This will make Luaotfload ignore all font files except for PostScript binary fonts with a matching AFM file, and Truetype fonts. Also, an uncompressed index file will be dumped which is going to be much larger than the default gzip’ed index. The terminal width is truncated to 60 characters which influences the verbose output during indexing. Finally, the verbosity is increased greatly: each font file being processed will be printed to the stdout on a separate line, along with lots of other information. </p>
<p> To observe the difference in behavior, save above snippet to <code>./luaotfload.conf</code> and update the font index: </p>
<pre>luaotfload-tool --update --force</pre>
<p>The current configuration can be written to disk using <code>luaotfload-tool</code>: </p>
<pre>luaotfload-tool --dumpconf &gt; luaotfload.conf</pre>
<p>The result can itself be used as a configuration file.</p>
<h2>Syntax</h2>
<p>The configuration file syntax follows the common INI format. For a more detailed description please refer to the section “CONFIGURATION FILE” of <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1). A brief list of rules is given below:</p>
<dl>
<dt>&bull;</p>
<dd>Blank lines and lines starting with a semicolon (<code>;</code>) are ignored.</p>
<dt>&bull;</p>
<dd>A configuration file is partitioned into sections that are declared by specifying the section title in brackets on a separate line: </p>
<pre>[some-section]
... section content ...</pre>
<dt>&bull;</p>
<dd>Sections consist of one or more variable assignments of the form <code>variable-name = value</code> E. g.: </p>
<pre>[foo]
 bar = baz
 quux = xyzzy
 ...</pre>
<dt>&bull;</p>
<dd>Section and variable names may contain only uppercase and lowercase letters as well as dashes (<code>&#8211;</code>).</dl>
<h2>Variables</h2>
<p>Variables in belong into a configuration section and their values must be of a certain type. Some of them have further constraints. For example, the “color callback” must be a string of one of the values <code>post_linebreak_filter</code>, <code>pre_linebreak_filter</code>, or <code>pre_output_filter</code>, defined in the section <i>run</i> of the configuration file. </p>
<p> Currently, the configuration is organized into four sections:</p>
<dl>
<dt><code>db</code></p>
<dd>Options relating to the font index.</p>
<dt><code>misc</code></p>
<dd>Options without a clearly defined category.</p>
<dt><code>paths</code></p>
<dd>Path and file name settings.</p>
<dt><code>run</code></p>
<dd>Options controlling runtime behavior of Luaotfload. </p>
<p> The list of valid variables, the sections they are part of and their type is given below. Types represent Lua types that the values must be convertible to; they are abbreviated as follows: <code>s</code> for the <i>string</i> type, <code>n</code> for <i>number</i>, <code>b</code> for <i>boolean</i>. A value of <code>nil</code> means the variable is unset.</dl>
<h3>Section <code>db</code></h3>
<p><center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> variable </td>
<td> type </td>
<td> default
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> compress </td>
<td> b </td>
<td> <code>true</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> designsize-dimen </td>
<td> b </td>
<td> <code>bp</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> formats </td>
<td> s </td>
<td> <code>&quot;otf,ttf,ttc&quot;</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> max-fonts </td>
<td> n </td>
<td> <code>2^51</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> scan-local </td>
<td> b </td>
<td> <code>false</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> skip-read </td>
<td> b </td>
<td> <code>false</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> strip </td>
<td> b </td>
<td> <code>true</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> update-live </td>
<td> b </td>
<td> <code>true</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> The flag <code>compress</code> determines whether the font index (usually <code>luaotfload-names.lua[.gz]</code> will be stored in compressed forms. If unset it is equivalent of passing <code>&#8211;no-compress</code> to <code>luaotfload-tool</code>. Since the file is only created for convenience and has no effect on the runtime behavior of Luaotfload, the flag should remain set. Most editors come with zlib support anyways. </p>
<p> The setting <code>designsize-dimen</code> applies when looking up fonts from families with design sizes. In Opentype, these are specified as “decipoints” where one decipoint equals ten DTP style “big points”. When indexing fonts these values are converted to <code>sp</code>. In order to treat the values as though they were specified in TeX points or Didot points, set <code>designsize-dimen</code> to <code>pt</code> or <code>dd</code>. </p>
<p> The list of <code>formats</code> must be a comma separated sequence of strings containing one or more of these elements:</p>
<dl>
<dt>&bull;</p>
<dd><code>otf</code> (OpenType format),</p>
<dt>&bull;</p>
<dd><code>ttf</code> and <code>ttc</code> (TrueType format),</p>
<dt>&bull;</p>
<dd><code>afm</code> (Adobe Font Metrics), </p>
<p> It corresponds loosely to the <code>&#8211;formats</code> option to <code>luaotfload-tool</code>. Invalid or duplicate members are ignored; if the list does not contain any useful identifiers, the default list <code>&quot;otf,ttf,ttc&quot;</code> will be used. </p>
<p> The variable <code>max-fonts</code> determines after processing how many font files the font scanner will terminate the search. This is useful for debugging issues with the font index and has the same effect as the option <code>&#8211;max-fonts</code> to <code>luaotfload-tools</code>. </p>
<p> The <code>scan-local</code> flag, if set, will incorporate the current working directory as a font search location. NB: This will potentially slow down document processing because a font index with local fonts will not be saved to disk, so these fonts will have to be re-indexed whenever the document is built. </p>
<p> The <code>skip-read</code> flag is only useful for debugging: It makes Luaotfload skip reading fonts. The font information for rebuilding the index is taken from the presently existing one. </p>
<p> Unsetting the <code>strip</code> flag prevents Luaotfload from removing data from the index that is only useful when processing font files. NB: this can increase the size of the index files significantly and has no effect on the runtime behavior. </p>
<p> If <code>update-live</code> is set, Luaotfload will reload the database if it cannot find a requested font. Those who prefer to update manually using <code>luaotfload-tool</code> should unset this flag. This option does not affect rebuilds due to version mismatch.</dl>
<h3>Section <code>default-features</code></h3>
<p>By default Luaotfload enables <code>node</code> mode and picks the default font features that are prescribed in the OpenType standard. This behavior may be overridden in the <code>default-features</code> section. Global defaults that will be applied for all scripts can be set via the <code>global</code> option, others by the script they are to be applied to. For example, a setting of </p>
<pre>[default-features]
 global = mode=base,color=0000FF
 dflt = smcp,onum</pre>
<p>would force <i>base</i> mode, tint all fonts blue and activate small capitals and text figures globally. Features are specified as a comma separated list of variables or variable-value pairs. Variables without an explicit value are set to <code>true</code>.</p>
<h3>Section <code>misc</code></h3>
<p><center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> variable </td>
<td> type </td>
<td> default
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> statistics </td>
<td> b </td>
<td> <code>false</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> termwidth </td>
<td> n </td>
<td> <code>nil</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> version </td>
<td> s </td>
<td> &lt;Luaotfload version&gt;
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> With <code>statistics</code> enabled, extra statistics will be collected during index creation and appended to the index file. It may then be queried at the Lua end or inspected by reading the file itself. </p>
<p> The value of <code>termwidth</code>, if set, overrides the value retrieved by querying the properties of the terminal in which Luatex runs. This is useful if the engine runs with <code>shell_escape</code> disabled and the actual terminal dimensions cannot be retrieved. </p>
<p> The value of <code>version</code> is derived from the version string hard-coded in the Luaotfload source. Override at your own risk.</p>
<h3>Section <code>paths</code></h3>
<p><center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> variable </td>
<td> type </td>
<td> default
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> cache-dir </td>
<td> s </td>
<td> <code>&quot;fonts&quot;</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> names-dir </td>
<td> s </td>
<td> <code>&quot;names&quot;</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> index-file </td>
<td> s </td>
<td> <code>&quot;luaotfload-names.lua&quot;</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> lookups-file </td>
<td> s </td>
<td> <code>&quot;luaotfload-lookup-cache.lua&quot;</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> The paths <code>cache-dir</code> and <code>names-dir</code> determine the subdirectory inside the Luaotfload subtree of the <code>luatex-cache</code> directory where the font cache and the font index will be stored, respectively. </p>
<p> Inside the index directory, the names of the index file and the font lookup cache will be derived from the respective values of <code>index-file</code> and <code>lookups-file</code>. This is the filename base for the bytecode compiled version as well as &#8212; for the index &#8212; the gzipped version.</p>
<h3>Section <code>run</code></h3>
<p><center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> variable </td>
<td> type </td>
<td> default
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> anon-sequence </td>
<td> s </td>
<td> <code>&quot;tex,path,name&quot;</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> color-callback </td>
<td> s </td>
<td> <code>&quot;post_linebreak_filter&quot;</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> definer </td>
<td> s </td>
<td> <code>&quot;patch&quot;</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> log-level </td>
<td> n </td>
<td> <code>0</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> resolver </td>
<td> s </td>
<td> <code>&quot;cached&quot;</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> fontloader </td>
<td> s </td>
<td> <code>&quot;default&quot;</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> Unqualified font lookups are treated with the flexible “anonymous” mechanism. This involves a chain of lookups applied successively until the first one yields a match. By default, the lookup will first search for TFM fonts using the Kpathsea library. If this wasn’t successful, an attempt is made at interpreting the request as an absolute path (like the <code>[/path/to/font/foo.ttf]</code> syntax) or a file name (<code>file:foo.ttf</code>). Finally, the request is interpreted as a font name and retrieved from the index (<code>name:Foo Regular</code>). This behavior can be configured by specifying a list as the value to <code>anon-sequence</code>. Available items are <code>tex</code>, <code>path</code>, <code>name</code> &#8212; representing the lookups described above, respectively &#8211;, and <code>file</code> for searching a filename but not an absolute path. Also, <code>my</code> lookups are valid values but they should only be used from within TeX documents, because there is no means of customizing a <code>my</code> lookups on the command line. </p>
<p> The <code>color-callback</code> option determines the stage at which fonts that defined with a <code>color=xxyyzz</code> feature will be colorized. By default this happens in a <code>post_linebreak_filter</code> but alternatively the <code>pre_linebreak_filter</code> or <code>pre_output_filter</code> may be chosen, which is faster but might produce inconsistent output. The <code>pre_output_filter</code> used to be the default in the 1.x series of Luaotfload, whilst later versions up to and including 2.5 hooked into the <code>pre_linebreak_filter</code> which naturally didn’t affect any glyphs inserting during hyphenation. Both are kept around as options to restore the previous behavior if necessary. </p>
<p> The <code>definer</code> allows for switching the <code>define_font</code> callback. Apart from the default <code>patch</code> one may also choose the <code>generic</code> one that comes with the vanilla fontloader. Beware that this might break tools like Fontspec that rely on the <code>patch_font</code> callback provided by Luaotfload to perform important corrections on font data. </p>
<p> The fontloader backend can be selected by setting the value of <code>fontloader</code>. The most important choices are <code>default</code>, which will load the dedicated Luaotfload fontloader, and <code>reference</code>, the upstream package as shipped with Luaotfload. Other than those, a file name accessible via kpathsea can be specified. </p>
<p> Alternatively, the individual files that constitute the fontloader can be loaded directly. While less efficient, this greatly aids debugging since error messages will reference the actual line numbers of the source files and explanatory comments are not stripped. Currently, three distinct loading strategies are available: <code>unpackaged</code> will load the batch that is part of Luaotfload. These contain the identical source code that the reference fontloader has been compiled from. Another option, <code>context</code> will attempt to load the same files by their names in the Context format from the search path. Consequently this option allows to use the version of Context that comes with the TeX distribution. Distros tend to prefer the stable version (“current” in Context jargon) of those files so certain bugs encountered in the more bleeding edge Luaotfload can be avoided this way. A third option is to use <code>context</code> with a colon to specify a directory prefix where the <i>TEXMF</i> is located that the files should be loaded from, e. g. <code>context:~/context/tex/texmf-context</code>. This can be used when referencing another distribution like the Context minimals that is installed under a different path not indexed by kpathsea. </p>
<p> The value of <code>log-level</code> sets the default verbosity of messages printed by Luaotfload. Only messages defined with a verbosity of less than or equal to the supplied value will be output on the terminal. At a log level of five Luaotfload can be very noisy. Also, printing too many messages will slow down the interpreter due to line buffering being disabled (see <code><a href="/docs/linux/man/3-setbuf/">setbuf</a></code>(3)). </p>
<p> The <code>resolver</code> setting allows choosing the font name resolution function: With the default value <code>cached</code> Luaotfload saves the result of a successful font name request to a cache file to speed up subsequent lookups. The alternative, <code>normal</code> circumvents the cache and resolves every request individually. (Since to the restructuring of the font name index in Luaotfload 2.4 the performance difference between the cached and uncached lookups should be marginal.)</p>
<h2>Files</h2>
<p>Luaotfload only processes the first configuration file it encounters at one of the search locations. The file name may be either <code>luaotfload.conf</code> or <code>luaotfloadrc</code>, except for the dotfile in the user’s home directory which is expected at <code>~/.luaotfloadrc</code>. </p>
<p> Configuration files are located following a series of steps. The search terminates as soon as a suitable file is encountered. The sequence of locations that Luaotfload looks at is</p>
<dl>
<dt>i.</p>
<dd>The current working directory of the LuaTeX process.</p>
<dt>ii.</p>
<dd>The subdirectory <code>luaotfload/</code> inside the XDG configuration tree, e. g. <code>/home/oenothea/config/luaotfload/</code>.</p>
<dt>iii.</p>
<dd>The dotfile.</p>
<dt>iv.</p>
<dd>The <i>TEXMF</i> (using kpathsea).</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-luaotfload-tool/">luaotfload-tool</a></code>(1), <code><a href="/docs/linux/man/1-luatex/">luatex</a></code>(1), <code><a href="/docs/linux/man/1-lua/">lua</a></code>(1)</p>
<dl>
<dt>&bull;</p>
<dd><code>texdoc luaotfload</code> to display the PDF manual for the <i>Luaotfload</i> package</p>
<dt>&bull;</p>
<dd>Luaotfload development <i><a rel="nofollow" href="https://github.com/latex3/luaotfload">https://github.com/latex3/luaotfload</a></i></p>
<dt>&bull;</p>
<dd>LuaLaTeX mailing list <i><a rel="nofollow" href="http://tug.org/pipermail/lualatex-dev/">http://tug.org/pipermail/lualatex-dev/</a></i></p>
<dt>&bull;</p>
<dd>LuaTeX <i><a rel="nofollow" href="http://luatex.org/">http://luatex.org/</a></i></p>
<dt>&bull;</p>
<dd>Luaotfload on CTAN <i><a rel="nofollow" href="http://ctan.org/pkg/luaotfload">http://ctan.org/pkg/luaotfload</a></i></dl>
<h2>References</h2>
<dl>
<dt>&bull;</p>
<dd>The XDG base specification <i><a rel="nofollow" href="http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html">http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html</a></i>.</dl>
<h2>Authors</h2>
<p><i>Luaotfload</i> was developed by the LuaLaTeX dev team (<i><a rel="nofollow" href="https://github.com/lualatex/">https://github.com/lualatex/</a></i>). It is currently maintained by the LaTeX Project Team at <i><a rel="nofollow" href="https://github.com/latex3/luaotfload">https://github.com/latex3/luaotfload</a></i> </p>
<p> This manual page was written by Philipp Gesang &lt;<i>phg [at] phi-gamma.net</i>&gt;.</p>
<h2>Copyright</h2>
<p>GPL v2.0</p>
