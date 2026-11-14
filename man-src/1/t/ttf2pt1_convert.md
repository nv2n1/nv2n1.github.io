---
title: "ttf2pt1_convert(1)"
name: "ttf2pt1_convert"
section: "1"
letter: "t"
url: "/docs/linux/man/1-ttf2pt1_convert/"
description: "ttf2pt1_convert – convenience font conversion script"
---

<h2 class="name">NAME</h2>
<p> ttf2pt1_convert &#8211; convenience font conversion script </p>
<h2>SYNOPSIS</h2>
<p> ttf2pt1_convert <code>[config-file]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>Ttf2pt1_Convert</code>&#8216; is the master conversion script provided with ttf2pt1. </p>
<p> If the configuration file is not specified as an argument then the file `<tt>&quot;convert.cfg&quot;</tt>&#8216; in the current directory is used. This file contains a set of configuration variables. The distribution contains a sample file file `<tt>&quot;convert.cfg.sample&quot;</tt>&#8216;. Please copy it to `<tt>&quot;convert.cfg&quot;</tt>&#8216;, look inside it and change the configuration variables. The more stable configuration variables, such as the path names of the scripts and encoding files are located in `<tt>&quot;ttf2pt1_convert&quot;</tt>&#8216; itself, they are automatically updated when installing <code>ttf2pt1</code>. </p>
<p> Put all the <font SIZE="-1">TTF</font> fonts you want to convert into some directory (this may be just the directory that already contains all the Windows fonts on a mounted <font SIZE="-1">FAT</font> filesystem). If you have fonts in different source encoding then put the fonts in each of the encodings into a separate directory. Up to 10 source directories are supported. If you (in a rather unlikely case) have more source directories then you can make two separate runs of the converter, converting up to 10 directories at a time. </p>
<p> The variables in the configuration file are:</p>
<dl>
<dt>&bull;</p>
<dd> &quot;SRCDIRS&quot; &#8211; the list of directories (with absolute paths) with <font SIZE="-1">TTF</font> fonts. Each line contains at least 3 fields: the name of the directory, the language of the fonts in it (if you have fonts for different languages you have to put them into the separate directories) and the encoding of the fonts. Again, if you have some of the <font SIZE="-1">TTF</font> typefaces in one encoding, and some in another (say, <font SIZE="-1">CP-1251</font> and <font SIZE="-1">KOI-8</font>), you have to put them into the separate source directories. Some lines may contain 4 fields. Then the fourth field is the name of the external map to convert the Unicode fonts into the desirable encoding. This map is used instead of the built-in map for the specified language. </p>
<p> *8* An interesting thing is that some languages have more than one widely used character encodings. For example, the widely used encodings for Russian are <font SIZE="-1">IBM CP-866 </font>(MS-DOS and Unix), <font SIZE="-1">KOI-8 </font>(Unix and <font SIZE="-1">VAX,</font> also the standard Internet encoding), <font SIZE="-1">IBM CP-1251 </font>(<font SIZE="-1">MS</font> Windows). That&#8217;s why I have provided the means to generate the converted fonts in more than one encoding. See the file encodings/README for details about the encoding tables. Actually, if you plan to use these fonts with Netscape Navigator better use the aliases cp-866 instead of ibm-866 and windows-1251 instead of ibm-1251 because that&#8217;s what Netscape wants.</p>
<dt>&bull;</p>
<dd> &quot;DSTDIR&quot; &#8211; directory for the resulting Type1 fonts. Be careful! This directory gets completely wiped out before conversion, so don&#8217;t use any already existing directory for this purpose.</p>
<dt>&bull;</p>
<dd> &quot;DSTENC{language}&quot; &#8211; the list of encodings in which the destination fonts will be generated for each language. Each font of that language will be generated in each of the specified encodings. If you don&#8217;t want any translation, just specify both <tt>&quot;SRCENC&quot;</tt> and <tt>&quot;DSTENC&quot;</tt> as iso8859-1 (or if you want any other encoding specified in the fonts.dir, copy the description of 8859-1 with new name and use this new name for <tt>&quot;SRCENC&quot;</tt> and <tt>&quot;DSTENC&quot;</tt>).</p>
<dt>&bull;</p>
<dd> &quot;FOUNDRY&quot; &#8211; the foundry name to be used in the fonts.dir file. I have set it to `fromttf&#8217; to avoid name conflicts with any existing font for sure. But this foundry name is not registered in X11 standards and if you want to get the full standard compliance or have a font server that enforces such a compliance, use `misc&#8217;.</dl>
<p> The next few parameters control the general behavior of the converter. They default values are set to something reasonable.</p>
<dl>
<dt>&bull;</p>
<dd> &quot;CORRECTWIDTH&quot; &#8211; if the value is set to &quot;YES&quot; then use the converter option <tt>&quot;</tt>-w<tt>&quot;</tt>, otherwise don&#8217;t use it. See the description of this option in the <font SIZE="-1">README</font> file.</p>
<dt>&bull;</p>
<dd> &quot;REMOVET1A&quot; &#8211; if the value is set to &quot;YES&quot; then after conversion remove the un-encoded <tt>&quot;.t1a&quot;</tt> font files and the intermediate <tt>&quot;.xpfa&quot;</tt> font metric files.</p>
<dt>&bull;</p>
<dd> &quot;INSTALLFONTMAP&quot; &#8211; a Ghostscript parameter, if the value is set to &quot;YES&quot; then install the entries for the new fonts right into the main <tt>&quot;Fontmap&quot;</tt> file. Otherwise just leave the file <tt>&quot;Fontmap.ttf&quot;</tt> in the Ghostscript configuration directory.</p>
<dt>&bull;</p>
<dd> &quot;HINTSUBST&quot; &#8211; if the value is set to &quot;YES&quot; use the option <tt>&quot;</tt>-H<tt>&quot;</tt>, otherwise don&#8217;t use it. This option enables the hint substitution technique. If you have not installed the X11 patch described above, use this option with great caution. See further description of this option in the <font SIZE="-1">README</font> file.</p>
<dt>&bull;</p>
<dd> &quot;ENFORCEISO&quot; &#8211; if the value is set to &quot;YES&quot; then disguise the resulting fonts as the fonts in ISOLatin1 encoding. Historically this was neccessary due to the way the installer scripts created the X11 font configuration files. It is not neccessary any more for this purpose. But if you plan to use these fonts with some other application that expects ISOLatin1 encoding then better enable this option.</p>
<dt>&bull;</p>
<dd> &quot;ALLGLYPHS&quot; &#8211; if the value is set to &quot;YES&quot; then include all the glyphs from the source fonts into the resulting fonts, even if these glyphs are inaccessible. If it&#8217;s set to &quot;NO&quot; then include only the glyphs which have codes assigned to them. The glyphs without codes can not be used directly. But some clever programs, such as the Type 1 library from XFree86 3.9 and higher can change the encoding on the fly and use another set of glyphs. If you have not installed the X11 patch described above, use this option with great caution. See further description of the option option <tt>&quot;</tt>-a<tt>&quot;</tt> in the <font SIZE="-1">README</font> file.</p>
<dt>&bull;</p>
<dd> &quot;GENUID&quot; &#8211; if the value is set to &quot;YES&quot; then use the option <tt>&quot;</tt>-uA<tt>&quot;</tt> of the converter to generate UniqueIDs for the converted fonts. The standard X11 Type 1 library does not use this <font SIZE="-1">ID,</font> so it may only be neccessary for the other applications. The script is clever enough to generate different UniqueID for the same font converted to multiple encodings. Also after conversion it checks all the fonts generacted during the session for duplicated UniqueID and shows those. Still, this does not quarantee that these UniqueIDs won&#8217;t overlap with some other fonts. The UniqueIDs are generated as hash values from the font names, so it&#8217;s guaranteed that if the `<tt>&quot;ttf2pt1_convert&quot;</tt>&#8216; script runs multiple times it will generate the same UniqueIDs during each run. See further description of this option in the <font SIZE="-1">README</font> file.</p>
<dt>&bull;</p>
<dd> &quot;GENUID&quot; &#8211; if the value is set to &quot;YES&quot; then create the <tt>&quot;.pfb&quot;</tt> files, otherwise the <tt>&quot;.pfa&quot;</tt> files. The <tt>&quot;.pfb&quot;</tt> files are more compact but contain binary data, so you may experience some troubles when transferring them through the network.</dl>
<p> The following parameters are used to locate the other scripts and configuration files. By default the scripts do a bit of guessing for them: they search in the <code>ttf2pt1</code> installation directory if <code>ttf2pt1</code> was installed or otherwise suppose that you are running `<tt>&quot;ttf2pt1_convert&quot;</tt>&#8216; with `<tt>&quot;scripts&quot;</tt>&#8216; subdirectory being the current directory.</p>
<dl>
<dt>&bull;</p>
<dd> &quot;ENCDIR&quot; &#8211; directory containing the descriptions of encodings</p>
<dt>&bull;</p>
<dd> &quot;MAPDIR&quot; &#8211; directory containing the external map files</dl>
<p> Besides that a few parameters are built into the `<tt>&quot;ttf2pt1_convert&quot;</tt>&#8216; script itself. You probably won&#8217;t need to change them:</p>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;</tt>T1ASM<tt>&quot;</tt>, <tt>&quot;</tt>TTF2PT1<tt>&quot;</tt>, <tt>&quot;</tt>TRANS<tt>&quot;</tt>, <tt>&quot;</tt>T1FDIR<tt>&quot;</tt>, <tt>&quot;</tt>FORCEISO<tt>&quot;</tt> &#8211; paths to the other script</dl>
<p> Also there are a few parameters controlling the installation of fonts for Ghostscript. Please look at their description in the Ghostscript section of documentation or in the <a href="/docs/linux/man/1-ttf2pt1_x2gs/">ttf2pt1_x2gs</a><code>(1)</code> manual page before running `<tt>&quot;ttf2pt1_convert&quot;</tt>&#8216;. If these parameters are set, `<tt>&quot;ttf2pt1_convert&quot;</tt>&#8216; will call the `<tt>&quot;x2gs&quot;</tt>&#8216; script automatically to install the newly converted fonts in Ghostscript. </p>
<p> After creating the configuration file run the `<tt>&quot;ttf2pt1_convert&quot;</tt>&#8216; script. Look at the result and the log file in <tt>&quot;DSTDIR&quot;</tt>. </p>
<p> Add the directory with newly converted fonts to the configuration of X server or font server. For most of the systems this step is very straightforward. For HP-UX it&#8217;s rather tricky and poorly documented, so the file <font SIZE="-1">FONTS</font>.hpux gives a short description. </p>
<p> If you don&#8217;t have the privileges of the root user, you still can configure your private font server. Just use some non-standard port number (see <font SIZE="-1">FONTS</font>.hpux for an example, exept that you won&#8217;t need all the HP-related stuff on any other system).</p>
<h2>FILES</h2>
<dl>
<dt>&bull;</p>
<dd> /usr/share/doc/ttf2pt1-3.4.4/convert.cfg.sample</p>
<dt>&bull;</p>
<dd> /usr/share/ttf2pt1/scripts/*</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">/usr/share/doc/ttf2pt1-3.4.4/README</font></p>
<dt>&bull;</p>
<dd> <font SIZE="-1">/usr/share/doc/ttf2pt1-3.4.4/FONTS</font></p>
<dt>&bull;</p>
<dd> /usr/share/ttf2pt1/*</p>
<dt>&bull;</p>
<dd> /usr/bin/ttf2pt1</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</p>
<dd> <i><a href="/docs/linux/man/1-ttf2pt1/">ttf2pt1</a></i>(1)</p>
<dt>&bull;</p>
<dd> <i><a href="/docs/linux/man/1-ttf2pt1_x2gs/">ttf2pt1_x2gs</a></i>(1)</p>
<dt>&bull;</p>
<dd> <i><a href="/docs/linux/man/1-t1asm/">t1asm</a></i>(1)</dl>
<h2>BUGS</h2>
<h3>Known problems</h3>
<dl>
<dt>&bull;</p>
<dd> The <tt>&quot;fonts.scale&quot;</tt> files created by the older versions of the <tt>&quot;ttf2pt1&quot;</tt> installation program (up to release 3.1) have conflicted with the language definitions of the <tt>&quot;Xfsft&quot;</tt> font server and parts of it included into XFree86. To overcome this incompatibility the never versions creats the <tt>&quot;fonts.scale&quot;</tt> file describing all the fonts as belonging to the <tt>&quot;adobe-fontspecific&quot;</tt> encoding and the <tt>&quot;fonts.alias&quot;</tt> file with the proper names. The drawback of this solution is that <tt>&quot;xlsfonts&quot;</tt> gives the list of twice more fonts. But as a side effect the option <tt>&quot;</tt>ENFORCEISO<tt>&quot;</tt> in `<tt>&quot;convert.cfg&quot;</tt>&#8216; is not required for X11 any more.</p>
<dt>&bull;</p>
<dd> The conversion script has no support for Eastern multi-plane fonts. Contribution of such a support would be welcome. </p>
</dl>
<h2>Index</h2>
