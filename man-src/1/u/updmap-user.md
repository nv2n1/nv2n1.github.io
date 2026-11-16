---
title: "updmap-user(1)"
name: "updmap-user"
section: "1"
letter: "u"
url: "/docs/linux/man/1-updmap-user/"
description: "updmap – manage TeX font maps updmap-sys – manage TeX font maps, system-wide updmap-user – manage TeX font maps, per-user"
---

<h2 class="name">NAME</h2>
<p> updmap &#8211; manage TeX font maps<br />
 updmap-sys &#8211; manage TeX font maps, system-wide<br />
 updmap-user &#8211; manage TeX font maps, per-user </p>
<h2>SYNOPSIS</h2>
<p> <code>updmap</code> [<i>,-user|-sys/</i>] [<i>,OPTION/</i>] &#8230; [<i>,COMMAND/</i>]<br />
 <code>updmap-user</code> [<i>,OPTION/</i>] &#8230; [<i>,COMMAND/</i>]<br />
 <code>updmap-sys</code> [<i>,OPTION/</i>] &#8230; [<i>,COMMAND/</i>]</p>
<h2>DESCRIPTION</h2>
<p> updmap version r59152 (2021-05-09 23:49:52 +0200) </p>
<p> Update the default font map files used by pdftex and dvipdfm(x) (pdftex.map), dvips (psfonts.map), and optionally pxdvi, as determined by all configuration files updmap.cfg (usually the ones returned by running &quot;kpsewhich <code>&#8211;all</code> updmap.cfg&quot;, but see below). </p>
<p> Among other things, these map files are used to determine which fonts should be used as bitmaps and which as outlines, and to determine which font files are included, typically subsetted, in the PDF or PostScript output. </p>
<p> updmap-sys (or updmap <code>-sys</code>) is intended to affect the system-wide configuration, while updmap-user (or updmap <code>-user</code>) affects personal configuration files only, overriding the system files. </p>
<p> As a consequence, once updmap-user has been run, even a single time, running updmap-sys no longer has any effect. updmap-sys issues a warning about this, since it is rarely desirable. See <a rel="nofollow" href="https://tug.org/texlive/scripts-sys-user.html">https://tug.org/texlive/scripts-sys-user.html</a> for details. </p>
<p> By default, the TeX filename database (ls-R) is also updated. </p>
<p> The updmap system is regrettably complicated, for both inherent and historical reasons. A general overview: </p>
<p> &#8211; updmap.cfg files are mainly about listing other files, namely the</p>
<dl>
<dt>
</dt><dd> font-specific .maps, in which each line gives information about a different TeX (.tfm) font.</dd></dl>
<p> &#8211; updmap reads the updmap.cfg files and then concatenates the</p>
<dl>
<dt>
</dt><dd> contents of those .map files into the main output files: psfonts.map for dvips and pdftex.map for pdftex and dvipdfmx.</dd></dl>
<p> &#8211; The updmap.cfg files themselves are created and updated at package</p>
<dl>
<dt>
</dt><dd> installation time, by the system installer or the package manager or by hand, and not (by default) by updmap.</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;cnffile</code> FILE</dt>
<dd> read FILE for the updmap configuration (can be given multiple times, in which case all the files are used)</dd>
<dt><code>&#8211;dvipdfmxoutputdir</code> DIR</dt>
<dd> specify output directory (dvipdfm(x) syntax)</dd>
<dt><code>&#8211;dvipsoutputdir</code> DIR</dt>
<dd> specify output directory (dvips syntax)</dd>
<dt><code>&#8211;pdftexoutputdir</code> DIR</dt>
<dd> specify output directory (pdftex syntax)</dd>
<dt><code>&#8211;pxdvioutputdir</code> DIR</dt>
<dd> specify output directory (pxdvi syntax)</dd>
<dt><code>&#8211;outputdir</code> DIR</dt>
<dd> specify output directory (for all files)</dd>
<dt><code>&#8211;copy</code></dt>
<dd> cp generic files rather than using symlinks</dd>
<dt><code>&#8211;force</code></dt>
<dd> recreate files even if config hasn&#8217;t changed</dd>
<dt><code>&#8211;nomkmap</code></dt>
<dd> do not recreate map files</dd>
<dt><code>&#8211;nohash</code></dt>
<dd> do not run mktexlsr (a.k.a. texhash)</dd>
<dt><code>&#8211;sys</code></dt>
<dd> affect system-wide files (equivalent to updmap-sys)</dd>
<dt><code>&#8211;user</code></dt>
<dd> affect personal files (equivalent to updmap-user)</dd>
<dt><code>-n</code>, <code>&#8211;dry-run</code></dt>
<dd> only show the configuration, no output</dd>
<dt><code>&#8211;quiet</code>, <code>&#8211;silent</code></dt>
<dd> reduce verbosity</dd></dl>
<h3>Commands:</h3>
<dl>
<dt><code>&#8211;help</code></dt>
<dd> show this message and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> show version information and exit</dd>
<dt><code>&#8211;showoption</code> OPTION</dt>
<dd> show the current setting of OPTION</dd>
<dt><code>&#8211;showoptions</code> OPTION</dt>
<dd> show possible settings for OPTION</dd>
<dt><code>&#8211;setoption</code> OPTION VALUE</dt>
<dd> set OPTION to value; option names below</dd>
<dt><code>&#8211;setoption</code> OPTION=VALUE</dt>
<dd> as above, just different syntax</dd>
<dt><code>&#8211;enable</code> MAPTYPE MAPFILE</dt>
<dd> add &quot;MAPTYPE MAPFILE&quot; to updmap.cfg, where MAPTYPE is Map, MixedMap, or KanjiMap</dd>
<dt><code>&#8211;enable</code> Map=MAPFILE</dt>
<dd> add &quot;Map MAPFILE&quot; to updmap.cfg</dd>
<dt><code>&#8211;enable</code> MixedMap=MAPFILE</dt>
<dd> add &quot;MixedMap MAPFILE&quot; to updmap.cfg</dd>
<dt><code>&#8211;enable</code> KanjiMap=MAPFILE</dt>
<dd> add &quot;KanjiMap MAPFILE&quot; to updmap.cfg</dd>
<dt><code>&#8211;disable</code> MAPFILE</dt>
<dd> disable MAPFILE, of whatever type</dd>
<dt><code>&#8211;listmaps</code></dt>
<dd> list all maps (details below)</dd>
<dt><code>&#8211;listavailablemaps</code></dt>
<dd> list available maps (details below)</dd>
<dt><code>&#8211;syncwithtrees</code></dt>
<dd> disable unavailable map files in updmap.cfg</dd></dl>
<p> The main output:</p>
<dl>
<dt>
</dt><dd> The main output of updmap is the files containing the individual font map lines which the drivers (dvips, pdftex, etc.) read to handle fonts.</dd>
<dt>
</dt><dd> The map files for dvips (psfonts.map) and pdftex and dvipdfmx (pdftex.map) are written to TEXMFVAR/fonts/map/updmap/{dvips,pdftex}/.</dd>
<dt>
</dt><dd> In addition, information about Kanji fonts is written to TEXMFVAR/fonts/map/updmap/dvipdfmx/kanjix.map, and optionally to TEXMFVAR/fonts/map/updmap/pxdvi/xdvi-ptex.map. These are for Kanji only and are not like other map files. dvipdfmx reads pdftex.map for the map entries for non-Kanji fonts.</dd>
<dt>
</dt><dd> If no option is given, so the invocation is just &quot;updmap-user&quot; or &quot;updmap-sys&quot;, these output files are always recreated.</dd>
<dt>
</dt><dd> Otherwise, if an option such as <code>&#8211;enable</code> or <code>&#8211;disable</code> is given, the output files are recreated if the list of enabled map files (from updmap.cfg) has changed. The <code>&#8211;force</code> option overrides this, always recreating the output files.</dd></dl>
<p> Explanation of the map types:</p>
<dl>
<dt>
</dt><dd> The normal type is Map.</dd>
<dt>
</dt><dd> The only difference between Map and MixedMap is that MixedMap entries are not added to psfonts_pk.map. The purpose is to help users with devices that render Type 1 outline fonts worse than mode-tuned Type 3 bitmap fonts. So, MixedMap is used for fonts that are available as both Type 1 and Metafont.</dd>
<dt>
</dt><dd> KanjiMap entries are added to psfonts_t1.map and kanjix.map.</dd></dl>
<p> Explanation of the OPTION names for <code>&#8211;showoptions</code>, <code>&#8211;showoption</code>, <code>&#8211;setoption</code>:</p>
<dl>
<dt>dvipsPreferOutline</dt>
<dd> true,false (default true)</dd>
<dt>
</dt><dd> Whether dvips uses bitmaps or outlines, when both are available.</dd>
<dt>dvipsDownloadBase35</dt>
<dd> true,false (default true)</dd>
<dt>
</dt><dd> Whether dvips includes the standard 35 PostScript fonts in its output.</dd>
<dt>pdftexDownloadBase14</dt>
<dd> true,false (default true)</dd>
<dt>
</dt><dd> Whether pdftex includes the standard 14 PDF fonts in its output.</dd>
<dt>pxdviUse</dt>
<dd> true,false (default false)</dd>
<dt>
</dt><dd> Whether maps for pxdvi (Japanese-patched xdvi) are under updmap&#8217;s control.</dd>
<dt>jaEmbed</dt>
<dd> (any string)</dd>
<dt>jaVariant</dt>
<dd> (any string)</dd>
<dt>scEmbed</dt>
<dd> (any string)</dd>
<dt>tcEmbed</dt>
<dd> (any string)</dd>
<dt>koEmbed</dt>
<dd> (any string)</dd>
<dt>
</dt><dd> See below.</dd>
<dt>LW35</dt>
<dd> URWkb,URW,ADOBEkb,ADOBE (default URWkb)</dd>
<dt>
</dt><dd> Adapt the font and file names of the standard 35 PostScript fonts. </dd>
<pre>
<dt>URWkb</dt><dd>URW fonts with &quot;berry&quot; filenames    (e.g. uhvbo8ac.pfb)
</dd><dt>URW</dt><dd>URW fonts with &quot;vendor&quot; filenames   (e.g. n019064l.pfb)
</pre>
</dd><dt>ADOBEkb</dt>
<dd> Adobe fonts with &quot;berry&quot; filenames (e.g. phvbo8an.pfb)</dd>
<dt>ADOBE</dt>
<dd> Adobe fonts with &quot;vendor&quot; filenames (e.g. hvnbo___.pfb)</dd>
<dt>
</dt><dd> These options are only read and acted on by updmap; dvips, pdftex, etc., do not know anything about them. They work by changing the default map file which the programs read, so they can be overridden by specifying command-line options or configuration files to the programs, as explained at the beginning of updmap.cfg.</dd>
<dt>
</dt><dd> The options jaEmbed and jaVariant (formerly kanjiEmbed and kanjiVariant) specify special replacements in the map lines. If a map contains the string @jaEmbed@, then this will be replaced by the value of that option; similarly for jaVariant. In this way, users of Japanese TeX can select different fonts to be included in the final output. The counterpart for Simplified Chinese, Traditional Chinese and Korean fonts are scEmbed, tcEmbed and koEmbed respectively.</dd></dl>
<h2>ENVIRONMENT</h2>
<p> Explanation of trees and files normally used:</p>
<dl>
<dt>
</dt><dd> If <code>&#8211;cnffile</code> is specified on the command line (can be given multiple times), its value(s) is(are) used. Otherwise, updmap reads all the updmap.cfg files found by running `kpsewhich <code>-all</code> updmap.cfg&#8217;, in the order returned by kpsewhich (which is the order of trees defined in texmf.cnf).</dd>
<dt>
</dt><dd> In either case, if multiple updmap.cfg files are found, all the maps mentioned in all the updmap.cfg files are merged.</dd>
<dt>
</dt><dd> Thus, if updmap.cfg files are present in all trees, and the default layout is used as shipped with TeX Live on Debian, the following files are read, in the given order. </dd>
<pre>
<dt></dt><dd>For updmap-sys:
TEXMFSYSCONFIG <i>,/etc/texmf/web2c/updmap.cfg/</i>
TEXMFSYSVAR    <i>,/var/lib/texmf/web2c/updmap.cfg/</i>
TEXMFLOCAL     <i>,/usr/local/share/texmf/web2c/updmap.cfg/</i>
TEXMFDEBIAN    <i>,/usr/share/texmf/web2c/updmap.cfg/</i>
TEXMFDIST      <i>,/usr/share/texlive/texmf/web2c/updmap.cfg/</i>
</dd><dt></dt><dd>For updmap-user:
TEXMFCONFIG    $HOME/.texmf-config/web2c/updmap.cfg
TEXMFVAR       $HOME/.texmf-var/web2c/updmap.cfg
TEXMFHOME      <i>,$HOME/texmf/web2c/updmap.cfg/</i>
TEXMFSYSCONFIG <i>,/etc/web2c/updmap.cfg/</i>
TEXMFSYSVAR    <i>,/var/lib/texmf/web2c/updmap.cfg/</i>
TEXMFLOCAL     <i>,/usr/local/share/texmf/web2c/updmap.cfg/</i>
TEXMFDEBIAN    <i>,/usr/share/texmf/web2c/updmap.cfg/</i>
TEXMFDIST      <i>,/usr/share/texlive/texmf/web2c/updmap.cfg/</i>
</dd><dt></dt><dd></pre>
</dd><dt>
</dt><dd> According to the actions, updmap might write to one of the given files or create a new updmap.cfg, described further below.</dd></dl>
<p> Where and which updmap.cfg changes are saved:</p>
<dl>
<dt>
</dt><dd> When no options are given, the updmap.cfg file(s) are only read, not written. It&#8217;s when an option <code>&#8211;setoption</code>, <code>&#8211;enable</code> or <code>&#8211;disable</code> is specified that an updmap.cfg needs to be updated. In this case:</dd>
<dt>
</dt><dd> 1) If config files are given on the command line, then the first one given is used to save any such changes.</dd>
<dt>
</dt><dd> 2) If the config files are taken from kpsewhich output, then the algorithm is more complex:</dd>
<dt>
</dt><dd> 2a) If <i>,$TEXMFCONFIG/web2c/updmap.cfg/</i> or <i>,$TEXMFHOME/web2c/updmap.cfg/</i> appears in the list of used files, then the one listed first by kpsewhich <code>&#8211;all</code> (equivalently, the one returned by kpsewhich updmap.cfg), is used.</dd>
<dt>
</dt><dd> 2b) If neither of the above two are present and changes are made, a new config file is created in <i>,$TEXMFCONFIG/web2c/updmap.cfg/</i>.</dd>
<dt>
</dt><dd> In general, the idea is that if the user cannot write to a given config file, a higher-level one can be used. That way, the distribution&#8217;s settings can be overridden system-wide using TEXMFLOCAL, and system settings can be overridden again in a particular user&#8217;s TEXMFHOME or TEXMFCONFIG.</dd></dl>
<p> Resolving multiple definitions of a font:</p>
<dl>
<dt>
</dt><dd> If a font is defined in more than one map file, then the definition coming from the first-listed updmap.cfg is used. If a font is defined multiple times within the same map file, one is chosen arbitrarily. In both cases a warning is issued.</dd></dl>
<p> Disabling maps:</p>
<dl>
<dt>
</dt><dd> updmap.cfg files with higher priority (listed earlier) can disable maps mentioned in lower priority (listed later) updmap.cfg files by writing, e.g.,</dd>
<dt>
</dt><dd> #! Map mapname.map</dd>
<dt>
</dt><dd> or</dd>
<dt>
</dt><dd> #! MixedMap mapname.map</dd>
<dt>in the higher-priority updmap.cfg file.</dt>
<dd> (The #! must be at the</dd>
<dt>
</dt><dd> beginning of the line, with at least one space or tab afterward, and whitespace between each word on the list.)</dd>
<dt>
</dt><dd> As an example, suppose you have a copy of MathTime Pro fonts and want to disable the Belleek version of the fonts; that is, disable the map belleek.map. You can create the file <i>,$TEXMFCONFIG/web2c/updmap.cfg/</i> with the content</dd>
<dt>
</dt><dd> #! Map belleek.map Map mt-plus.map Map mt-yy.map</dd>
<dt>
</dt><dd> and call updmap.</dd></dl>
<p> Listing of maps:</p>
<dl>
<dt>
</dt><dd> The two options <code>&#8211;listmaps</code> and <code>&#8211;listavailablemaps</code> list all maps defined in any of the updmap.cfg files (for <code>&#8211;listmaps</code>), and only those actually found on the system (for <code>&#8211;listavailablemaps</code>). The output format is one line per font map, with the following fields separated by tabs: map, type (Map, MixedMap, KanjiMap), status (enabled, disabled), origin (the updmap.cfg file where it is mentioned, or &#8216;builtin&#8217; for the three basic maps).</dd>
<dt>
</dt><dd> In the case of <code>&#8211;listmaps</code> there can be one additional fields (again separated by tab) containing &#8216;(not available)&#8217; for those map files that cannot be found.</dd></dl>
<p> updmap-user vs. updmap-sys:</p>
<dl>
<dt>
</dt><dd> When updmap-sys is run, TEXMFSYSCONFIG and TEXMFSYSVAR are used instead of TEXMFCONFIG and TEXMFVAR, respectively. This is the primary difference between updmap-sys and updmap-user.</dd>
<dt>
</dt><dd> Other locations may be used if you give them on the command line, or these trees don&#8217;t exist, or you are not using the original TeX Live.</dd></dl>
<p> To see the precise locations of the various files that will be read and written, give the <code>-n</code> option (or read the source).</p>
<h2>EXAMPLES</h2>
<p> The log file is written to TEXMFVAR/web2c/updmap.log. </p>
<p> For step-by-step instructions on making new fonts known to TeX, read <a rel="nofollow" href="https://tug.org/fonts/fontinstall.html.">https://tug.org/fonts/fontinstall.html.</a> For even more terse instructions, read the beginning of the main updmap.cfg file.</p>
<h2>FILES</h2>
<p> Configuration and input files:</p>
<dl>
<dt><i>updmap.cfg</i></dt>
<dd> Main configuration file. In <i>texmf-dist/web2c</i> by default, but may be located elsewhere depending on your distribution. Each texmf tree read should have its own <i>updmap.cfg</i>.</dd>
<dt><i>dvips35.map</i></dt>
<dd> Map file for standard 35 PostScript fonts for use with <code><a href="/docs/linux/man/1-dvips/">dvips</a></code>(1).</dd>
<dt><i>pdftex35.map</i></dt>
<dd> Map file for standard 35 PostScript fonts for use with <code><a href="/docs/linux/man/1-pdftex/">pdftex</a></code>(1).</dd>
<dt><i>ps2pk35.map</i></dt>
<dd> Map file for standard 35 PostScript fonts for use with <code><a href="/docs/linux/man/1-ps2pk/">ps2pk</a></code>(1).</dd></dl>
<p> Output files:</p>
<dl>
<dt><i>psfonts.map</i></dt>
<dd> For <code><a href="/docs/linux/man/1-dvips/">dvips</a></code>(1). Same as <i>psfonts_t1.map</i> if option <code>dvipsPreferOutline</code> active, else as <i>psfonts_pk.map</i>.</dd>
<dt><i>psfonts_pk.map</i></dt>
<dd> For <code><a href="/docs/linux/man/1-dvips/">dvips</a></code>(1). Without information from MixedMap files. (Setting of <code>dvipsPreferOutline</code> ignored.)</dd>
<dt><i>psfonts_t1.map</i></dt>
<dd> For <code><a href="/docs/linux/man/1-dvips/">dvips</a></code>(1). With information from MixedMap files. (Setting of <code>dvipsPreferOutline</code> ignored.)</dd>
<dt><i>download35.map</i></dt>
<dd> For <code><a href="/docs/linux/man/1-dvips/">dvips</a></code>(1). Always downloads the standard 35 fonts. (Setting of <code>dvipsDownloadBase35</code> ignored.)</dd>
<dt><i>builtin35.map</i></dt>
<dd> For <code><a href="/docs/linux/man/1-dvips/">dvips</a></code>(1). Never downloads the standard 35 fonts. (Setting of <code>dvipsDownloadBase35</code> ignored.)</dd>
<dt><i>pdftex.map</i></dt>
<dd> For <code><a href="/docs/linux/man/1-pdftex/">pdftex</a></code>(1). Same as <i>pdftex_dl14.map</i> if option <code>pdftexDownloadBase14</code> active, else as <i>pdftex_ndl14.map</i>.</dd>
<dt><i>pdftex_dl14.map</i></dt>
<dd> For <code><a href="/docs/linux/man/1-pdftex/">pdftex</a></code>(1). Always downloads the standard 14 fonts.</dd>
<dt><i>pdftex_ndl14.map</i></dt>
<dd> For <code><a href="/docs/linux/man/1-pdftex/">pdftex</a></code>(1). Never downloads the standard 14 fonts.</dd>
<dt><i>ps2pk.map</i></dt>
<dd> Similar to <i>psfonts.map</i> file, but forces all fonts to be downloaded, so this map file can be used with <code><a href="/docs/linux/man/1-xdvi/">xdvi</a></code>(1) and <code><a href="/docs/linux/man/1-ps2pk/">ps2pk</a></code>(1).</dd></dl>
<p> Configuration files for <code><a href="/docs/linux/man/1-dvips/">dvips</a></code>(1):</p>
<dl>
<dt><i>config.builtin35</i></dt>
<dd> Loads <i>builtin35.map</i> instead of <i>psfonts.map</i>.</dd>
<dt><i>config.download35</i></dt>
<dd> Loads <i>download35.map</i> instead of <i>psfonts.map</i>.</dd>
<dt><i>config.outline</i></dt>
<dd> Loads <i>psfonts_t1.map</i> instead of <i>psfonts.map</i>.</dd>
<dt><i>config.pdf</i></dt>
<dd> Loads <i>psfonts_t1.map</i> instead of <i>psfonts.map</i> and has additional settings for PDF generation.</dd>
<dt><i>config.pk</i></dt>
<dd> Loads <i>psfonts_pk.map</i> instead of <i>psfonts.map</i>.</dd>
<dt><i>config.www</i></dt>
<dd> Loads <i>psfonts_t1.map</i> instead of <i>psfonts.map</i>. (For compatibility with old versions.)</dd>
<dt><i>config.gstopk</i></dt>
<dd> Loads <i>psfonts_t1.map</i> instead of <i>psfonts.map</i>.</dd></dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs to: tex-live [at] tug.org<br />
 TeX Live home page: &lt;<a rel="nofollow" href="https://tug.org/texlive/">https://tug.org/texlive/</a>&gt; </p>
<h2>Index</h2>
