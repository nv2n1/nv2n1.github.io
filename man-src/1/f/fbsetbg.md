---
title: "fbsetbg(1)"
name: "fbsetbg"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fbsetbg/"
description: "fbsetbg – Set a background wallpaper or pattern"
---

<h2 class="name">NAME</h2>
<p> fbsetbg &#8211; Set a background wallpaper or pattern </p>
<h2>SYNOPSIS</h2>
<p> <code>fbsetbg</code> [<code>-uU</code> <i>wallpapersetter</i>] [<code>-fFcCtTaA</code>] <i>wallpaper</i> </p>
<p> <code>fbsetbg</code> [<code>-uU</code> <i>wallpapersetter</i>] <code>-rR</code> <i>path</i> </p>
<p> <code>fbsetbg</code> <code>-bB</code> <i>fbsetrootoptions&#8230;</i> </p>
<p> <code>fbsetbg</code> [-<code>l</code>|<code>h</code>|<code>i</code>|<code>p</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code><a href="/docs/linux/man/1-fbsetbg/">fbsetbg</a>(1)</code> is a wrapper that tries to find a suitable background-setting app and then tries to set the wallpaper using that app. You don&#8217;t have to configure fbsetbg. It just uses the first app it can find. </p>
<p> Furthermore it supports remembering the last set wallpaper so you don&#8217;t have to edit the style or init-file to change the wallpaper. </p>
<p> It aims to provide clear error messages in a window that make debugging problems easy.</p>
<h2>OPTIONS</h2>
<p> <code>-f</code> <i>file</i></p>
<dl>
<dt>
<dd> Set fullscreen wallpaper.</dl>
<p> <code>-c</code> <i>file</i></p>
<dl>
<dt>
<dd> Set centered wallpaper.</dl>
<p> <code>-t</code> <i>file</i></p>
<dl>
<dt>
<dd> Set tiled wallpaper.</dl>
<p> <code>-a</code> <i>file</i></p>
<dl>
<dt>
<dd> Set maximized wallpaper, preserving aspect (if your bgsetter doesn&#8217;t support this option fbsetbg falls back to <code>-f</code>).</dl>
<p> <code>-u</code> <i>wallpapersetter</i></p>
<dl>
<dt>
<dd> Use specified wallpapersetter, use no argument to forget.</dl>
<p> <code>-b</code> <i>fbsetrootoptions</i></p>
<dl>
<dt>
<dd> Forward the options to <code><a href="/docs/linux/man/1-fbsetroot/">fbsetroot</a>(1)</code>. These can be used to set a solid, pattern, or gradient background texture.</dl>
<p> <code>-r</code> <i>directory</i></p>
<dl>
<dt>
<dd> Set random wallpaper from a directory.</dl>
<p> <code>-F</code>, <code>-C</code>, <code>-T</code>, <code>-A</code>, <code>-U</code>, <code>-B</code>, <code>-R</code></p>
<dl>
<dt>
<dd> Same as the lowercase option but without remembering.</dl>
<p> <code>-l</code></p>
<dl>
<dt>
<dd> Set previous wallpaper. Or, if the random feature was last used, set another random wallpaper from the same directory.</dl>
<p> <code>-i</code></p>
<dl>
<dt>
<dd> Display useful information about best wallpapersetter found.</dl>
<p> <code>-p</code></p>
<dl>
<dt>
<dd> Display some useful tips.</dl>
<p> <code>-h</code></p>
<dl>
<dt>
<dd> Display a help message.</dl>
<h2>FILES</h2>
<p> <code>~/.fluxbox/lastwallpaper</code></p>
<dl>
<dt>
<dd> In this file the wallpaper you set will be stored, for the <code>-l</code> option.</dl>
<h2>ENVIRONMENT</h2>
<p> <code>wpsetters</code></p>
<dl>
<dt>
<dd> Wallpapersetters to use. This can be a space-delimited list of the applications to try, or just a single name.</dl>
<p> <code>DISPLAY</code></p>
<dl>
<dt>
<dd> The display you want to set the wallpaper on.</dl>
<h2>EXAMPLES</h2>
<p> To use <code><a href="/docs/linux/man/1-feh/">feh</a>(1)</code> as wallpapersetter and set <code>wallpapper.jpg</code> from the current directory as wallpaper. </p>
<dl>
<dt>
<dd>
<pre>
$ wpsetters=feh fbsetbg wallpaper.jpg
</pre>
</dl>
<p> Recall the last set wallpaper on display <code>:0.0</code> with the stored options. </p>
<dl>
<dt>
<dd>
<pre>
$ DISPLAY=:0.0 fbsetbg -l
</pre>
</dl>
<h2>BUGS</h2>
<p> <code><a href="/docs/linux/man/1-fbsetbg/">fbsetbg</a>(1)</code> is not foolproof.</p>
<h2>AUTHORS</h2>
<p> The author of fbsetbg is Han Boetes &lt;han at fluxbox.org&gt; </p>
<p> This manpage was converted to asciidoc format by Jim Ramsay &lt;i.am at jimramsay.com&gt; for fluxbox-1.1.2</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1) <a href="/docs/linux/man/1-fbsetroot/">fbsetroot</a>(1)</p>
<h2>AUTHOR</h2>
<p> <code>Jim Ramsay</code> &lt;i.am [at] jimramsay.com&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>Index</h2>
