---
title: "texlua(1)"
name: "texlua"
section: "1"
letter: "t"
url: "/docs/linux/man/1-texlua/"
description: "luatex, dviluatex, luahbtex, luajittex, texlua, texluac – An extended version of TeX using Lua as an embedded scripting language"
---

<h2 class="name">NAME</h2>
<p> luatex, dviluatex, luahbtex, luajittex, texlua, texluac &#8211; An extended version of TeX using Lua as an embedded scripting language </p>
<h2>SYNOPSIS</h2>
<p> <code>luatex</code> [<code>&#8211;lua=</code><i>FILE</i>] [<i>OPTION</i>]&#8230; [<i>TEXNAME</i>[<i></i><code>.tex</code>]] [<i>COMMANDS</i>]<br />
 <code>luatex</code> [<code>&#8211;lua=</code><i>FILE</i>] [<i>OPTION</i>]&#8230; <code>\</code><i>FIRST-LINE</i><br />
 <code>luatex</code> [<code>&#8211;lua=</code><i>FILE</i>] [<i>OPTION</i>]&#8230; <code>&amp;</code><i>FMT</i> [<i>ARGS</i>]</p>
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
<p> When the LuaTeX executable starts, it looks for the <code>&#8211;lua</code> command-line option. If there is no <code>&#8211;lua</code> option, the command line is interpreted in a similar fashion as in traditional pdfTeX and Aleph. But if the option is present, LuaTeX will enter an alternative mode of command-line parsing in comparison to the standard web2c programs. The presence of <code>&#8211;lua</code> makes most of other options unreliable, because the lua initialization file can disable kpathsea and/or hook functions into various callbacks.</p>
<dl>
<dt><code>&#8211;lua=</code><i>FILE</i></p>
<dd> The lua initialization file.</dl>
<p> The following two options alter the executable behaviour:</p>
<dl>
<dt><code>&#8211;luaonly</code></p>
<dd> Start LuaTeX as a Lua interpreter. In this mode, it will set Lua&#8217;s <i>arg[0]</i> to the found script name, pushing preceding options in negative values and the rest of the command line in the positive values, just like the Lua interpreter. LuaTeX will exit immediately after executing the specified Lua script.</p>
<dt><code>&#8211;luaconly</code></p>
<dd> Start LuaTeX as a Lua byte compiler. In this mode, LuaTeX is exactly like <code>luac</code> from the standalone Lua distribution, except that it does not have the <code>-l</code> switch, and that it accepts (but ignores) the <code>&#8211;luaconly</code> switch.</dl>
<p> Then the regular web2c options:</p>
<dl>
<dt><code>&#8211;debug-format</code></p>
<dd>
 Debug format loading.</p>
<dt><code>&#8211;draftmode</code></p>
<dd> Sets \pdfdraftmode so luaTeX doesn&#8217;t write a PDF and doesn&#8217;t read any included images, thus speeding up execution.</p>
<dt><code>&#8211;enable-write18</code></p>
<dd>
 Synonym for <code>&#8211;shell-escape</code>.</p>
<dt><code>&#8211;disable-write18</code></p>
<dd>
 Synonym for <code>&#8211;no-shell-escape</code>.</p>
<dt><code>&#8211;shell-escape</code></p>
<dd>
 Enable the <code>\write18{</code><i>command</i><code>}</code> construct, and Lua functions <code>os.execute()</code>, <code>os.exec()</code>, <code>os.spawn()</code>, and <code>io.popen()</code>. The <i>command</i> can be any shell command. This construct is normally disallowed for security reasons.</p>
<dt><code>&#8211;no-shell-escape</code></p>
<dd>
 Disable the <code>\write18{</code><i>command</i><code>}</code> construct and the other Lua functions, even if it is enabled in the <i>texmf.cnf</i> file.</p>
<dt><code>&#8211;shell-restricted</code></p>
<dd> Enable restricted version of <code>\write18</code>, <code>os.execute()</code>, <code>os.exec()</code>, <code>os.spawn()</code>, and <code>io.popen()</code>, only commands listed in <i>texmf.cnf</i> file are allowed.</p>
<dt><code>&#8211;file-line-error</code></p>
<dd> Print error messages in the form <i>file:line:error</i> which is similar to the way many compilers format them.</p>
<dt><code>&#8211;no-file-line-error</code></p>
<dd> Disable printing error messages in the <i>file:line:error</i> style.</p>
<dt><code>&#8211;fmt=</code><i>FORMAT</i></p>
<dd> Use <i>FORMAT</i> as the name of the format to be used, instead of the name by which luaTeX was called or a <i>%&amp;</i> line.</p>
<dt><code>&#8211;help</code></p>
<dd> Print help message and exit.</p>
<dt><code>&#8211;ini</code></p>
<dd> Start in <i>INI</i> mode, which is used to dump formats. The <i>INI</i> mode can be used for typesetting, but no format is preloaded, and basic initializations like setting catcodes may be required.</p>
<dt><code>&#8211;interaction=</code><i>MODE</i></p>
<dd> Sets the interaction mode. The <i>MODE</i> can be either <i>batchmode</i>, <i>nonstopmode</i>, <i>scrollmode</i>, and <i>errorstopmode</i>. The meaning of these modes is the same as that of the corresponding 
