---

title: "mktexfmt(1)"
name: "mktexfmt"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mktexfmt/"
description: "fmtutil – manage TeX formats and Metafont bases, per-user fmtutil-sys – manage TeX formats and Metafont bases, system-wide mktexfmt – create a TeX format or Metafont base"
---

<p> fmtutil &#8211; manage TeX formats and Metafont bases, per-user<br/>
 fmtutil-sys &#8211; manage TeX formats and Metafont bases, system-wide<br/>
 mktexfmt &#8211; create a TeX format or Metafont base </p>
<h2>SYNOPSIS</h2>
<p> <code>fmtutil</code> [<i>,-user|-sys/</i>] [<i>,OPTION/</i>] &#8230; [<i>,COMMAND/</i>]<br/>
 <code>fmtutil-sys</code> [<i>,OPTION/</i>] &#8230; [<i>,COMMAND/</i>]<br/>
 <code>fmtutil-user</code> [<i>,OPTION/</i>] &#8230; [<i>,COMMAND/</i>]<br/>
 <code>mktexfmt</code> <i>,FORMAT.fmt|BASE.base|FMTNAME/</i></p>
<h2>DESCRIPTION</h2>
<p> fmtutil version r59143 (2021-05-09 04:23:44 +0200) </p>
<p> Rebuild and manage TeX fmts and Metafont bases, collectively called &quot;formats&quot; here. (MetaPost no longer uses the past-equivalent &quot;mems&quot;.) </p>
<p> If not operating in mktexfmt mode, exactly one command must be given, filename suffixes should generally not be specified, no non-option arguments are allowed, and multiple formats can be generated. </p>
<p> If the command name ends in mktexfmt, only one format can be created. The only options supported are <code>&#8211;help</code> and <code>&#8211;version</code>, and the command line must be either a format name, with extension, or a plain name that is passed as the argument to <code>&#8211;byfmt</code> (see below). The full name of the generated file (if any) is written to stdout, and nothing else. The system directories are used if they are writable, else the user directories. </p>
<p> By default, the return status is zero if all formats requested are successfully built, else nonzero.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;sys</code></dt>
<dd> use TEXMFSYS{VAR,CONFIG}</dd>
<dt><code>&#8211;user</code></dt>
<dd> use TEXMF{VAR,CONFIG}</dd>
<dt><code>&#8211;cnffile</code> FILE</dt>
<dd> read FILE instead of fmtutil.cnf (can be given multiple times, in which case all the files are used)</dd>
<dt><code>&#8211;dry-run</code>, <code>-n</code></dt>
<dd> don&#8217;t actually build formts</dd>
<dt><code>&#8211;fmtdir</code> DIR</dt>
<dd> write formats under DIR instead of TEXMF[SYS]VAR</dd>
<dt><code>&#8211;no-engine-subdir</code></dt>
<dd> don&#8217;t use engine-specific subdir of the fmtdir</dd>
<dt><code>&#8211;no-error-if-no-format</code></dt>
<dd> exit successfully if no format is selected</dd>
<dt><code>&#8211;no-error-if-no-engine</code>=<i>,ENGINE1/</i>,ENGINE2,&#8230;</dt>
<dd> exit successfully even if a required ENGINE</dd>
<dt>
</dt><dd> is missing, if it is included in the list.</dd>
<dt><code>&#8211;no-strict</code></dt>
<dd> exit successfully even if a format fails to build</dd>
<dt><code>&#8211;nohash</code></dt>
<dd> don&#8217;t update ls-R files</dd>
<dt><code>&#8211;recorder</code></dt>
<dd> pass the <code>-recorder</code> option and save .fls files</dd>
<dt><code>&#8211;refresh</code></dt>
<dd> recreate only existing format files</dd>
<dt><code>&#8211;status-file</code> FILE</dt>
<dd> append status information about built formats to FILE</dd>
<dt><code>&#8211;quiet</code></dt>
<dd> be silent</dd>
<dt><code>&#8211;catcfg</code></dt>
<dd> (does nothing, exists for compatibility)</dd>
<dt><code>&#8211;dolinks</code></dt>
<dd> (does nothing, exists for compatibility)</dd>
<dt><code>&#8211;force</code></dt>
<dd> (does nothing, exists for compatibility)</dd>
<dt><code>&#8211;test</code></dt>
<dd> (does nothing, exists for compatibility)</dd></dl>
<h3>Commands:</h3>
<dl>
<dt><code>&#8211;all</code></dt>
<dd> recreate all format files</dd>
<dt><code>&#8211;missing</code></dt>
<dd> create all missing format files</dd>
<dt><code>&#8211;byengine</code> ENGINE</dt>
<dd> (re)create formats built with ENGINE</dd>
<dt><code>&#8211;byfmt</code> FORMAT</dt>
<dd> (re)create format FORMAT</dd>
<dt><code>&#8211;byhyphen</code> HYPHENFILE</dt>
<dd> (re)create formats that depend on HYPHENFILE</dd>
<dt><code>&#8211;enablefmt</code></dt>
<dd> FORMAT[/ENGINE] enable FORMAT, as built with ENGINE</dd>
<dt><code>&#8211;disablefmt</code> FORMAT[/ENGINE]</dt>
<dd> disable FORMAT, as built with ENGINE If multiple formats have the same name and</dd>
<dt>
</dt><dd> different engines, <i>,/ENGINE/</i> specifier is required.</dd>
<dt><code>&#8211;listcfg</code></dt>
<dd> list (enabled and disabled) configurations, filtered to available formats</dd>
<dt><code>&#8211;showhyphen</code> FORMAT</dt>
<dd> print name of hyphen file for FORMAT</dd>
<dt><code>&#8211;version</code></dt>
<dd> show version information and exit</dd>
<dt><code>&#8211;help</code></dt>
<dd> show this message and exit</dd></dl>
<h2>ENVIRONMENT</h2>
<p> Explanation of trees and files normally used:</p>
<dl>
<dt>
</dt><dd> If <code>&#8211;cnffile</code> is specified on the command line (possibly multiple times), its value(s) are used. Otherwise, fmtutil reads all the fmtutil.cnf files found by running &quot;kpsewhich <code>-all</code> fmtutil.cnf&quot;, in the order returned by kpsewhich. Files specified via <code>&#8211;cnffile</code> are first tried to be loaded directly, and if not found and the file names don&#8217;t contain directory parts, are searched via kpsewhich.</dd>
<dt>
</dt><dd> In any case, if multiple fmtutil.cnf files are found, all the format definitions found in all the fmtutil.cnf files are merged.</dd>
<dt>
</dt><dd> Thus, if fmtutil.cnf files are present in all trees, and the default layout is used as shipped with TeX Live, the following files are read, in the given order. </dd>
<pre>
<dt></dt><dd>For fmtutil-sys:
TEXMFSYSCONFIG <i>,$TEXLIVE/YYYY/texmf-config/web2c/fmtutil.cnf/</i>
TEXMFSYSVAR    <i>,$TEXLIVE/YYYY/texmf-var/web2c/fmtutil.cnf/</i>
TEXMFLOCAL     <i>,$TEXLIVE/texmf-local/web2c/fmtutil.cnf/</i>
TEXMFDIST      <i>,$TEXLIVE/YYYY/texmf-dist/web2c/fmtutil.cnf/</i>
</dd><dt></dt><dd>For fmtutil-user:
TEXMFCONFIG    $HOME/.texliveYYYY/texmf-config/web2c/fmtutil.cnf
TEXMFVAR       $HOME/.texliveYYYY/texmf-var/web2c/fmtutil.cnf
TEXMFHOME      <i>,$HOME/texmf/web2c/fmtutil.cnf/</i>
TEXMFSYSCONFIG <i>,$TEXLIVE/YYYY/texmf-config/web2c/fmtutil.cnf/</i>
TEXMFSYSVAR    <i>,$TEXLIVE/YYYY/texmf-var/web2c/fmtutil.cnf/</i>
TEXMFLOCAL     <i>,$TEXLIVE/texmf-local/web2c/fmtutil.cnf/</i>
TEXMFDIST      <i>,$TEXLIVE/YYYY/texmf-dist/web2c/fmtutil.cnf/</i>
</dd><dt></dt><dd>(where YYYY is the TeX Live release version).
</pre>
</dd><dt>
</dt><dd> According to the actions, fmtutil might update one of the existing cnf files or create a new fmtutil.cnf, as described below.</dd></dl>
<p> Where format files are written:</p>
<dl>
<dt>
</dt><dd> By default, format files are (re)written in <i>,$TEXMFSYSVAR/ENGINE/</i> by fmtutil-sys, and <i>,$TEXMFVAR/ENGINE/</i> by fmtutil-user, where <i>,/ENGINE/</i> is a subdirectory named for the engine used, such as &quot;pdftex&quot;.</dd>
<dt>
</dt><dd> For mktexfmt, TEXMFSYSVAR is used if it is writable, else TEXMFVAR.</dd>
<dt>
</dt><dd> If the <code>&#8211;fmtdir</code>=<i>,DIR/</i> option is specified, DIR is used instead of TEXMF[SYS]VAR, but the <i>,/ENGINE/</i> subdir is still used by default.</dd>
<dt>
</dt><dd> In all cases, if the <code>&#8211;no-engine-subdir</code> option is specified, the <i>,/ENGINE/</i> subdir is omitted.</dd></dl>
<p> Where configuration changes are saved:</p>
<dl>
<dt>
</dt><dd> If config files are given on the command line, then the first one given will be used to save any changes from <code>&#8211;enable</code> or <code>&#8211;disable</code>.</dd>
<dt>
</dt><dd> If the config files are taken from kpsewhich output, then the algorithm is more complicated:</dd>
<dt>
</dt><dd> 1) If <i>,$TEXMFCONFIG/web2c/fmtutil.cnf/</i> or <i>,$TEXMFHOME/web2c/fmtutil.cnf/</i> appears in the list of used files, then the one listed first by kpsewhich <code>&#8211;all</code> (equivalently, the one returned by &quot;kpsewhich fmtutil.cnf&quot;), is used.</dd>
<dt>
</dt><dd> 2) If neither of the above two are present and changes are made, a new config file is created in <i>,$TEXMFCONFIG/web2c/fmtutil.cnf/</i>.</dd>
<dt>
</dt><dd> In general, the idea is that if a given config file is not writable, a higher-level one can be used. That way, the distribution&#8217;s settings can be overridden system-wide using TEXMFLOCAL, and system settings can be overridden again in a particular user&#8217;s TEXMFHOME or TEXMFCONF.</dd></dl>
<p> Resolving multiple definitions of a format:</p>
<dl>
<dt>
</dt><dd> If a format is defined in more than one config file, then the definition coming from the first-listed fmtutil.cnf is used.</dd></dl>
<p> Disabling formats:</p>
<dl>
<dt>
</dt><dd> fmtutil.cnf files with higher priority (listed earlier) can disable formats in lower priority (listed later) fmtutil.cnf files by writing a line like this in the higher-priority fmtutil.cnf file:</dd>
<dt>
</dt><dd> #! &lt;fmtname&gt; &lt;enginename&gt; &lt;hyphen&gt; &lt;args&gt;</dd>
<dt>
</dt><dd> The #! must be at the beginning of the line, with at least one space or tab afterward, and there must be whitespace between each word on the list.</dd>
<dt>
</dt><dd> For example, you can disable the luajitlatex format by creating the file <i>,$TEXMFCONFIG/web2c/fmtutil.cnf/</i> with the line</dd>
<dt>
</dt><dd> #! luajitlatex luajittex language.dat,language.dat.lua lualatex.ini</dd>
<dt>
</dt><dd> (As it happens, the luajittex-related formats are precisely why the <code>&#8211;no-error-if-no-engine</code> option exists, since luajittex cannot be compiled on all platforms. So this is not needed.)</dd></dl>
<p> fmtutil-user (fmtutil <code>-user</code>) vs. fmtutil-sys (fmtutil <code>-sys</code>):</p>
<dl>
<dt>
</dt><dd> When fmtutil-sys is run or the command line option <code>-sys</code> is used, TEXMFSYSCONFIG and TEXMFSYSVAR are used instead of TEXMFCONFIG and TEXMFVAR, respectively. This is the primary difference between fmtutil-sys and fmtutil-user.</dd>
<dt>
</dt><dd> See <a rel="nofollow" href="https://tug.org/texlive/scripts-sys-user.html">https://tug.org/texlive/scripts-sys-user.html</a> for details.</dd>
<dt>
</dt><dd> Other locations may be used if you give them on the command line, or these trees don&#8217;t exist, or you are not using the original TeX Live.</dd></dl>
<p> Supporting development binaries:</p>
<dl>
<dt>
</dt><dd> If an engine name ends with &quot;-dev&quot;, formats are created in the respective directory with the <code>-dev</code> stripped. This allows for easily running development binaries in parallel with the released binaries.</dd></dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs to: tex-live [at] tug.org<br/>
 TeX Live home page: &lt;<a rel="nofollow" href="https://tug.org/texlive/">https://tug.org/texlive/</a>&gt; </p>
