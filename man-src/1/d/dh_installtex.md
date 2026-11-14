---
title: "dh_installtex(1)"
name: "dh_installtex"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_installtex/"
description: "dh_installtex – register Type 1 fonts, hyphenation patterns, or formats with TeX"
---

<h2 class="name">NAME</h2>
<p> dh_installtex &#8211; register Type 1 fonts, hyphenation patterns, or formats with TeX </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_installtex</code> [<i>debhelper options</i>] [<code>-n</code>] [<code>&#8211;flavor=</code><i>flavor</i>[,<i>flavor</i>]] [<code>map=MixedMap,</code><i>file.map</i>] [<code>map=Map,</code><i>file.map</i>] [<code>map=KanjiMap,</code><i>file.map</i>] [<code>mapfile=</code><i>file.cfg</i>] [<code>hyphen=</code><i>lang</i>,<i>file</i>[,lhm=<i>n</i>][,rhm=<i>n</i>][,synonym=<i>syn</i>,&#8230;]] [<code>hyphenfile=</code><i>file.cnf</i>] [<code>format=</code><i>format</i>,<i>engine</i>,<i>hyphenfile</i>,<i>rest args</i>] [<code>formatfile=</code><i>file.cnf</i>]</p>
<h2>DESCRIPTION</h2>
<p> dh_installtex is a debhelper program that is responsible for updating the ls-R databases, registering map files, new formats, and new hyphenation patterns with TeX. </p>
<p> Your package should depend on an appropriate version of tex-common so that the update-* commands are available. (This program adds that dependency to ${misc:Depends}.) </p>
<p> <font SIZE="-1"><code>WARNING</code></font> This program does <code>not</code> check for the actual existence of any input files in <font SIZE="-1">TEXMF</font> trees. If you call it without any further specification on which packages to work on (using <tt>&quot;-p&quot;</tt> or <tt>&quot;-N&quot;</tt>) it will add calls to management functions to <code>all</code> packages. In this case don&#8217;t forget to add ${misc:Depends} to all packages&#8217; dependencies.</p>
<h2>SIMPLE USAGE: Registering Files</h2>
<p> If you only install files into /usr/share/texmf, nothing has to be done, tex-common will automatically detect changes and run mktexlsr.</p>
<h2>COMPLEX USAGE: Registering fonts, hyphenation patterns and formats</h2>
<p> If in addition, you have to install map files, hyphenation patterns for additional languages, or format definitions you can use three different methods to specify what should be installed: </p>
<p> 1) <code>Pre made config files:</code> These files can be specified with the different <i>type</i>file= options. <i>type</i> can be one of map, format and hyphen, and these files will be installed into /var/lib/tex-common/<i>configdir</i>/ for the respective type (fontmap-cfg for map files, hyphen-cnf for hyphenation patterns, and fmtutil-cnf for format definitions). </p>
<p> Example: </p>
<pre>
        dh_installtex mapfile=foo.cfg formatfile=debian/bar.cnf
</pre>
<p> would install foo.cfg as /var/lib/tex-common/fontmap-cfg/texmf/foo.cfg, and debian/bar.cnf as /var/lib/tex-common/fmtutil-cnf/texmf/bar.cnf. </p>
<p> 2) <code>Directly on the cmd line:</code> You can specify maps, formats, and hyphenations on the cmd line. The items are stored in the respective config file 20package </p>
<p> Example: </p>
<pre>
        dh_installtex map=Map,foo.map hyphen=ngerman-x-2011-07-01,dehyphn-x-2011-07-01.tex,hyph-de-1996.pat.txt,lhm=2,rhm=2,synonym=ngerman-x-latest,exceptions=hyph-de-1996.hyp.txt
</pre>
<p> would install a file /var/lib/tex-common/fontmap-cfg/texmf/package.cfg containing the line </p>
<pre>
        Map foo.map
</pre>
<p> and a file /var/lib/tex-common/hyphen-cnf/texmf/package.cnf containing the lines </p>
<pre>
    name=ngerman-x-2011-07-01 file=dehyphn-x-2011-07-01.tex file_patterns=hyph-de-1996.pat.txt lefthyphenmin=2 righthyphenmin=2 synonym=ngerman-x-latest file_exceptions=hyph-de-1996.hyp.txt
</pre>
<p> 3) <code>Package files:</code> You create a file debian/package.maps or debian/maps, debian/package.hyphens or debian/hyphens, debian/package.formats or debian/formats. These files are installed with the name of the package. Each of these files will be installed into the first package dh_installtex is told to act on. By default this is the first binary package in debian/control, but if you use -p, -i, or -a flags, it will be the first package specified by those flags. </p>
<p> Example: </p>
<pre>
        dh_installtex
</pre>
<p> would install a present debian/package.formats file as /var/lib/tex-common/fmtutil-cnf/texmf/package.cnf.</p>
<h3>Mixing the different variants</h3>
<p> The command line items (Variant 2) are merged into the debian/package.maps (debian/package.hyphens, debian/package.formats) file. If you specify an additional package.cfg/cnf (Variant 1) this will raise an error since both files would be installed as package.cfg/cnf.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-n</code>, <code>&#8211;noscripts</code></p>
<dd> Do not modify postinst/prerm scripts.</p>
<dt><code>&#8211;flavor=</code><i>flavor</i>[,<i>flavor</i>]</p>
<dd> This option is used to select a different tree then the default /usr/share/texmf, and to switch on additional options. The argument specify a list from flavors to be selected. At the moment you can select from the following list of flavors: <code>tree:texlive</code>, <code>map:config_for_active_maps</code>, <code>map:config_for_all_maps</code>, <code>format:add_one:</code>formatname. </p>
<p> <code>tree:texlive</code> will select the tree /usr/share/texlive/texmf-dist and should only be used for files installed into this tree. </p>
<p> <code>map:config_for_active_maps</code> will create a file <i>config.bar</i> for each active (i.e. uncommented) map in each of the cfg file generated by one of the three methods described above. These files are installed in /usr/share/texmf/dvips/config/. </p>
<p> If you select <code>map:config_for_all_maps</code> the script will generate <i>config.bar</i> even for those map files which are present in a cfg file, but deactivated by a comment. </p>
<p> The file <i>config.bar</i> is used when called by `dvips -Pbar &#8230;&#8217;. Thus it allows the activation of single map files even if they are not automatically activated via the updmap(-sys) mechanism. </p>
<p> Default is <i>not</i> to generate any config files. </p>
<p> <code>format:add_one:</code>formatname allows one to add the generation of a specific format without actually providing it (in a cnf file). This is useful if a package adds hyphenation patterns to an existing formats. </p>
<p> <code>format:no_links</code>: Usually, for every format that is specified in a configuration file, dh_installtex will create a symlink /usr/bin/<i>format</i> that points to the corresponding engine. For example, /usr/bin/latex would be created as a symlink to pdftex. </p>
<p> The flavor <code>format:no_links</code> inhibits this. If a link already exists, dh_installtex will skip this format with an informational message, even if this option is not given.</dl>
<h2>NOTES</h2>
<p> &#8220;dh_installtex&#8221; adds a dependency relation onto tex-common to misc:Depends. </p>
<p> Note that this command is not idempotent. &#8220;dh_clean -k&#8221; should be called between invocations of this command, unless using the <code>-n</code> option. Otherwise, it may cause multiple instances of the same text to be added to maintainer scripts. </p>
<p> Please refer to the Debian TeX policy for details about fonts configuration for TeX by Debian packages.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-debhelper/">debhelper</a></code>(7)</p>
<h2>AUTHOR</h2>
<p> This program and its documentation was written by Norbert Preining for the Debian Operating System and both are licensed under the <font SIZE="-1">GNU</font> General Public License Version 2 or later. </p>
<h2>Index</h2>
