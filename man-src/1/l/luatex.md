---

title: "luatex(1)"
name: "luatex"
section: "1"
letter: "l"
url: "/docs/linux/man/1-luatex/"
description: "luatex, dviluatex, luahbtex, luajittex, texlua, texluac – An extended version of TeX using Lua as an embedded scripting language"
---

<p> luatex, dviluatex, luahbtex, luajittex, texlua, texluac - An extended version of TeX using Lua as an embedded scripting language </p>
<h2>SYNOPSIS</h2>
<p> <code>luatex</code> [<code>--lua=</code><i>FILE</i>] [<i>OPTION</i>]... [<i>TEXNAME</i>[<i></i><code>.tex</code>]] [<i>COMMANDS</i>] <br />
 <code>luatex</code> [<code>--lua=</code><i>FILE</i>] [<i>OPTION</i>]... <code>\</code><i>FIRST-LINE</i> <br />
 <code>luatex</code> [<code>--lua=</code><i>FILE</i>] [<i>OPTION</i>]... <code>&amp;</code><i>FMT</i> [<i>ARGS</i>]  </p>
<h2>DESCRIPTION</h2>
<p> Run the luaTeX typesetter on <i>TEXNAME</i>, usually creating <i>TEXNAME</i><code>.pdf</code>. Any remaining <i>COMMANDS</i> are processed as luaTeX input, after <i>TEXNAME</i> is read. </p>
<p> Alternatively, if the first non-option argument begins with a backslash, interpret all non-option arguments as a line of luaTeX input. </p>
<p> Alternatively, if the first non-option argument begins with a <code>&amp;</code>, the next word is taken as the <i>FMT</i> to read, overriding all else. Any remaining arguments are processed as above. </p>
<p> If no arguments or options are specified, prompt for input. </p>
<p> If called as <code>texlua</code> it acts as a Lua interpreter. If called as <code>texluac</code> it acts as a Lua bytecode compiler. </p>
<p> LuaTeX began as an extended version of pdfTeX with Unicode and OpenType font support, embedded <code>Lua</code> scripting language, the <code>e-TeX</code> and <code>Omega</code> extensions, as well as an integrated MetaPost engine, that can create <i>PDF</i> files as well as <i>DVI</i> files. For more information about luatex, see <a rel="nofollow" href="http://www.luatex.org;">http://www.luatex.org;</a> and you can read the LuaTeX manual using the texdoc utility (<code>texdoc luatex</code>). </p>
<p> All LuaTeX text input and output is considered to be Unicode text, although various filters make it possible to support any encoding. </p>
<p> In <i>DVI</i> mode, LuaTeX can be used as a complete replacement for the TeX engine. </p>
<p> In <i>PDF</i> mode, LuaTeX can natively handle the <i>PDF</i>, <i>JPG</i>, <i>JBIG2</i>, and <i>PNG</i> graphics formats. LuaTeX cannot include PostScript or Encapsulated PostScript (EPS) graphics files; first convert them to PDF using <code>epstopdf</code> (1). </p>
<p> The luajittex variant includes the Lua just-in-time compiler. </p>
<p> The luahbtex variant can use the HarfBuzz engine for glyph shaping, instead of LuaTeX&#8217;s built-in shaper. </p>
<h2>OPTIONS</h2>
<p> When the LuaTeX executable starts, it looks for the <code>--lua</code> command-line option. If there is no <code>--lua</code> option, the command line is interpreted in a similar fashion as in traditional pdfTeX and Aleph. But if the option is present, LuaTeX will enter an alternative mode of command-line parsing in comparison to the standard web2c programs. The presence of <code>--lua</code> makes most of other options unreliable, because the lua initialization file can disable kpathsea and/or hook functions into various callbacks. </p>
<dl>
<dt><code>--lua=</code><i>FILE</i></dt>
<dd> <p> The lua initialization file. </p>
 </dd></dl>
<p> The following two options alter the executable behaviour: </p>
<dl>
<dt><code>--luaonly</code></dt>
<dd> <p> Start LuaTeX as a Lua interpreter. In this mode, it will set Lua&#8217;s <i>arg[0]</i> to the found script name, pushing preceding options in negative values and the rest of the command line in the positive values, just like the Lua interpreter. LuaTeX will exit immediately after executing the specified Lua script. </p>
 </dd>
<dt><code>--luaconly</code></dt>
<dd> <p> Start LuaTeX as a Lua byte compiler. In this mode, LuaTeX is exactly like <code>luac</code> from the standalone Lua distribution, except that it does not have the <code>-l</code> switch, and that it accepts (but ignores) the <code>--luaconly</code> switch. </p>
 </dd></dl>
<p> Then the regular web2c options: </p>
<dl>
<dt><code>--debug-format</code></dt>
<dd> <p> <br />
 Debug format loading. </p>
 </dd>
<dt><code>--draftmode</code></dt>
<dd> <p> Sets \pdfdraftmode so luaTeX doesn&#8217;t write a PDF and doesn&#8217;t read any included images, thus speeding up execution. </p>
 </dd>
<dt><code>--enable-write18</code></dt>
<dd> <p> <br />
 Synonym for <code>--shell-escape</code>. </p>
 </dd>
<dt><code>--disable-write18</code></dt>
<dd> <p> <br />
 Synonym for <code>--no-shell-escape</code>. </p>
 </dd>
<dt><code>--shell-escape</code></dt>
<dd> <p> <br />
 Enable the <code>\write18{</code><i>command</i><code>}</code> construct, and Lua functions <code>os.execute()</code>, <code>os.exec()</code>, <code>os.spawn()</code>, and <code>io.popen()</code>. The <i>command</i> can be any shell command. This construct is normally disallowed for security reasons. </p>
 </dd>
<dt><code>--no-shell-escape</code></dt>
<dd> <p> <br />
 Disable the <code>\write18{</code><i>command</i><code>}</code> construct and the other Lua functions, even if it is enabled in the <i>texmf.cnf</i> file. </p>
 </dd>
<dt><code>--shell-restricted</code></dt>
<dd> <p> Enable restricted version of <code>\write18</code>, <code>os.execute()</code>, <code>os.exec()</code>, <code>os.spawn()</code>, and <code>io.popen()</code>, only commands listed in <i>texmf.cnf</i> file are allowed. </p>
 </dd>
<dt><code>--file-line-error</code></dt>
<dd> <p> Print error messages in the form <i>file:line:error</i> which is similar to the way many compilers format them. </p>
 </dd>
<dt><code>--no-file-line-error</code></dt>
<dd> <p> Disable printing error messages in the <i>file:line:error</i> style. </p>
 </dd>
<dt><code>--fmt=</code><i>FORMAT</i></dt>
<dd> <p> Use <i>FORMAT</i> as the name of the format to be used, instead of the name by which luaTeX was called or a <i>%&amp;</i> line. </p>
 </dd>
<dt><code>--help</code></dt>
<dd> <p> Print help message and exit. </p>
 </dd>
<dt><code>--ini</code></dt>
<dd> <p> Start in <i>INI</i> mode, which is used to dump formats. The <i>INI</i> mode can be used for typesetting, but no format is preloaded, and basic initializations like setting catcodes may be required. </p>
 </dd>
<dt><code>--interaction=</code><i>MODE</i></dt>
<dd> <p> Sets the interaction mode. The <i>MODE</i> can be either <i>batchmode</i>, <i>nonstopmode</i>, <i>scrollmode</i>, and <i>errorstopmode</i>. The meaning of these modes is the same as that of the corresponding \commands. </p>
 </dd>
<dt><code>--jobname=</code><i>NAME</i></dt>
<dd> <p> Use <i>NAME</i> for the job name, instead of deriving it from the name of the input file. </p>
 </dd>
<dt><code>--kpathsea-debug=</code><i>BITMASK</i></dt>
<dd> <p> Sets path searching debugging flags according to the <i>BITMASK</i>. See the <i>Kpathsea</i> manual for details. </p>
 </dd>
<dt><code>--mktex=</code><i>FMT</i></dt>
<dd> <p> Enable mktex <i>FMT</i> generation, where <i>FMT</i> must be either <i>tex</i> or <i>tfm</i>. </p>
 </dd>
<dt><code>--nosocket</code></dt>
<dd> <p> Disable the luasocket (network) library. </p>
 </dd>
<dt><code>--output-comment=</code><i>STRING</i></dt>
<dd>  </dd>
<dd> <p> In <i>DVI</i> mode, use <i>STRING</i> for the <i>DVI</i> file comment instead of the date. This option is ignored in <i>PDF</i> mode. </p>
 </dd>
<dt><code>--output-directory=</code><i>DIRECTORY</i></dt>
<dd> <p> Write output files in <i>DIRECTORY</i> instead of the current directory. Look up input files in <i>DIRECTORY</i> first, then along the normal search path. </p>
 </dd>
<dt><code>--output-format=</code><i>FORMAT</i></dt>
<dd> <p> Set the output format mode, where <i>FORMAT</i> must be either <i>pdf</i> or <i>dvi</i>. This also influences the set of graphics formats understood by luaTeX. </p>
 </dd>
<dt><code>--progname=</code><i>NAME</i></dt>
<dd> <p> Pretend to be program <i>NAME</i> (only for kpathsea). </p>
 </dd>
<dt><code>--recorder</code></dt>
<dd> <p> Enable the filename recorder. This leaves a trace of the files opened for input and output in a file with extension <i>.fls</i>. </p>
 </dd>
<dt><code>--safer</code></dt>
<dd> <p> Disable some Lua commands that can easily be abused by a malicious document. </p>
 </dd>
<dt><code>--synctex=</code><i>NUMBER</i></dt>
<dd> <p> Enable/disable SyncTeX extension. </p>
 </dd>
<dt><code>--version</code></dt>
<dd> <p> Print version information and exit. </p>
 </dd>
<dt><code>--credits</code></dt>
<dd> <p> Print credits and version details. </p>
 </dd>
<dt>The following options are ignored:</dt>
<dd>  </dd>
<dt><code>--8bit</code>,&nbsp;<code>--etex</code>,&nbsp;<code>--parse-first-line</code>,&nbsp;<code>--no-parse-first-line</code></dt>
<dd> <p> These are always on. </p>
 </dd>
<dt><code>--default-translate-file=</code><i>TCXNAME</i>,&nbsp;<code>--translate-file=</code><i>TCXNAME</i></dt>
<dd> <p> These are always off. </p>
 </dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pdftex/">pdftex</a></code>(1), <code><a href="/docs/linux/man/1-etex/">etex</a></code>(1), <code><a href="/docs/linux/man/1-aleph/">aleph</a></code>(1), <code><a href="/docs/linux/man/1-lua/">lua</a></code>(1).  </p>
<h2>AUTHORS</h2>
<p> The primary authors of LuaTeX are Taco Hoekwater, Hartmut Henkel, Hans Hagen, and Luigi Scarso, with help from Martin Schr&ouml;der, Karel Skoupy, and Han The Thanh. </p>
<p> TeX was designed by Donald E. Knuth, who implemented it using his Web system for Pascal programs. It was ported to Unix at Stanford by Howard Trickey, and at Cornell by Pavel Curtis. The version now offered with the Unix TeX distribution is that generated by the Web to C system (<code>web2c</code>), originally written by Tomas Rokicki and Tim Morgan. </p>
<p> The LuaTeX home page is <a rel="nofollow" href="http://luatex.org.">http://luatex.org.</a> </p>
