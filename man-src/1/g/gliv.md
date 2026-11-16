---
title: "gliv(1)"
name: "gliv"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gliv/"
description: "gliv – An OpenGL Image Viewer"
---

<h2>NAME</h2>
<p> gliv &#8211; An OpenGL Image Viewer</p>
<h2>SYNOPSIS</h2>
<p> <code>gliv</code> [OPTIONS]&#8230; [FILES]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <i>gliv</i> uses gdk-pixbuf to load images and OpenGL to render them. It allows to do some moving, rotating, zooming and slide show.</p>
<h2>OPTIONS</h2>
<p> The options are first set to their default values, &quot;off&quot; for flags, then read either from ~/.glivrc or /etc/glivrc or a configuration file specified on the command line, and finally read from the command line.<br />
 Omitting the argument for an option that takes an &quot;on|off&quot; argument (flags) is like giving it &quot;on&quot;, so &#8211;foo is the same as &#8211;foo=on if foo is an on|off flag.</p>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Print help and exit.</dd>
<dt><code>-V, &#8211;version</code></dt>
<dd> Print version and exit.</dd>
<dt><code>-a, &#8211;add-all[=on|off]</code></dt>
<dd> Add all files in the directory. With this option, when you open a file on the command line or with the open dialog, all others files in the directory are added as well.</dd>
<dt><code>-R, &#8211;recursive[=on|off]</code></dt>
<dd> Recursive directory traversal. If <i>gliv</i> tries to load a direcory, it will also load every image all its subdirectories.</dd>
<dt><code>-S, &#8211;sort[=on|off]</code></dt>
<dd> Show images in sorted order. The images list will be sorted before the slide show.</dd>
<dt><code>-s, &#8211;shuffle[=on|off]</code></dt>
<dd> Show images in random order. The images list will be shuffled before the slide show.</dd>
<dt><code>-F, &#8211;force-load[=on|off]</code></dt>
<dd> Try to load every file. When loading a file, the loader is chosen according to the filename extension in order to optimize the loading time. If the extension is unknown, the file is ignored, with this option <i>gliv</i> will always try to load the file.</dd>
<dt><code>-C, &#8211;client[=on|off]</code></dt>
<dd> Connect to an already running <i>gliv</i>. With this option, <i>gliv</i> will open the files passed in the arguments in the <i>gliv</i> server window. It can also be used with the -0 option. The <i>gliv</i> server is the latest launched <i>gliv</i> or the one which has been chosen using the Options menu.</dd>
<dt><code>-e, &#8211;build-menus[=on|off]</code></dt>
<dd> No images menu at startup. Disabling the images menus creation at startup makes it faster, especially with many files on the command line.</dd>
<dt><code>-g, &#8211;glivrc[=FILE]</code></dt>
<dd> Use this configuration file or none. Specify it to disable loading of the rc file. With a filename as argument it will use it as a configuration file.</dd>
<dt><code>-w, &#8211;slide-show[=on|off]</code></dt>
<dd> Start the slide show immediately. This way you will not have to start it manually from the menu.</dd>
<dt><code>-0, &#8211;null[=on|off]</code></dt>
<dd> Read null-terminated filenames. This can be used with &quot;find -print0&quot; or with &quot;tr &#8216;
&#8217; &#8216;
</dd></dl>