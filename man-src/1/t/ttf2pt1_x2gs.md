---
title: "ttf2pt1_x2gs(1)"
name: "ttf2pt1_x2gs"
section: "1"
letter: "t"
url: "/docs/linux/man/1-ttf2pt1_x2gs/"
description: "ttf2pt1_x2gs – font installer for Ghostscript"
---

<h2 class="name">NAME</h2>
<p> ttf2pt1_x2gs &#8211; font installer for Ghostscript </p>
<h2>SYNOPSIS</h2>
<p> ttf2pt1_x2gs <code>[config-file]</code></p>
<h2>DESCRIPTION</h2>
<p> The fonts generated with <code>ttf2pt1</code> work fine with Ghostscript by themselves. The script `<code>ttf2pt1_x2gs</code>&#8216; links the font files from the X11 direcotry into the Ghostscript directory and automatically creates the description file (<tt>&quot;Fontmap&quot;</tt>) in Ghostscript format. </p>
<p> If the configuration file is not specified as an argument then the file `<tt>&quot;convert.cfg&quot;</tt>&#8216; in the current directory is used, just like the `<tt>&quot;convert&quot;</tt>&#8216; script does. Indeed, this configuration file is used for both scripts. </p>
<p> The Ghostscript-related parameters in the configuration file are: </p>
<p> &quot;DSTDIR&quot; &#8211; the X11 font directory used by `<tt>&quot;ttf2pt1_x2gs&quot;</tt>&#8216; as the source of the fonts. This parameter is common with the X11 configuration. </p>
<p> &quot;GSDIR&quot; &#8211; the base directory of Ghostsript. If this parameter is set to an empty string then `<tt>&quot;ttf2pt1_convert&quot;</tt>&#8216; won&#8217;t call `<tt>&quot;x2gs&quot;</tt>&#8216;. So if you want to get only the X11 fonts installed then set this parameter to an empty string. This directory may vary on various system, so please check your system and set this value accordingly before running the script. </p>
<p> &quot;GSFONTDIR&quot; &#8211; the font directory of Ghostscript. In the standard Ghostscript installation it&#8217;s a subdirectory of <tt>&quot;GSDIR&quot;</tt> but some systems may use completely different directories. </p>
<p> &quot;GSCONFDIR&quot; &#8211; the configuration subdirectory of Ghostscript that contains the <tt>&quot;Fontmap&quot;</tt> file. </p>
<p> &quot;INSTALLFONTMAP&quot; &#8211; if the value is set to &quot;YES&quot; then install the entries for the new fonts right into the main <tt>&quot;Fontmap&quot;</tt> file. Otherwise just leave the file <tt>&quot;Fontmap.ttf&quot;</tt> in the Ghostscript configuration directory. </p>
<p> After preparing the configuration file run the script. It symbolicaly links all the font files and creates the description file <tt>&quot;Fontmap.ttf&quot;</tt> in <tt>&quot;GSCONDFIR&quot;</tt>. After that there are two choices. </p>
<p> If the option <tt>&quot;INSTALLFONTMAP&quot;</tt> was set to <tt>&quot;YES&quot;</tt> then the font descriptions are also automatically installed into the master <tt>&quot;Fontmap&quot;</tt> file. The script is clever enough to detect if it was run multiple times with the same directories and if so it replaces the old <tt>&quot;Fontmap&quot;</tt> entries with the new ones instead of just accumulating all of them. You may also run it multiple times for multiple X11 directories and all the results will be properly collected in the <tt>&quot;Fontmap&quot;</tt>. But it&#8217;s your responsibility to watch that the names of the font files don&#8217;t overlap. If the X11 font directory gets renamed then you have to remove its font entries from the <tt>&quot;Fontmap&quot;</tt> and only after that re-run `<tt>&quot;ttf2pt1_x2gs&quot;</tt>&#8216; for the new directory. </p>
<p> On the other hand if the option <tt>&quot;INSTALLFONTMAP&quot;</tt> was set to <tt>&quot;NO&quot;</tt> then go to the <tt>&quot;GSCONFDIR&quot;</tt> directory and insert the contents of <tt>&quot;Fontmap.ttf&quot;</tt> into the <tt>&quot;Fontmap&quot;</tt> file manually. This step may be left manual to make the installation a little bit more safe. </p>
<p> After that you may also want to redefine some of the aliases in <tt>&quot;Fontmap&quot;</tt> to refer to the newly installed fonts. But the redefinition of the aliases may be dangerous if the width of characters in the new font will be different from the old font. Alas, there is no visible solution of this problem yet.</p>
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
<dd> <i><a href="/docs/linux/man/1-ttf2pt1_convert/">ttf2pt1_convert</a></i>(1)</p>
<dt>&bull;</p>
<dd> <i><a href="/docs/linux/man/1-t1asm/">t1asm</a></i>(1) </p>
</dl>
<h2>Index</h2>
