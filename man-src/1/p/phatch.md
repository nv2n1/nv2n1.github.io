---
title: "phatch(1)"
name: "phatch"
section: "1"
letter: "p"
url: "/docs/linux/man/1-phatch/"
description: "Phatch – Photo Batch Processor"
---

<h2>NAME</h2>
<p> Phatch &#8211; Photo Batch Processor</p>
<h2>DESCRIPTION</h2>
<p> <code>Phatch</code> is a simple photo batch processor. It handles all popular image formats and can duplicate (sub)folder hierarchies. It can also batch resize, rotate, rename, &#8230; and more in minutes instead of hours or days if you do it manually. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt>Phatch [actionlist]</dt>
<dd>
</dd><dt>Phatch [options] [actionlist] [image folders/files/urls]</dt>
<dd>
</dd><dt>Phatch &#8211;inspect [image files/urls]</dt>
<dd>
</dd><dt>Phatch &#8211;droplet [actionlist/recent] [image files/urls]</dt>
<dd>
</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></dt>
<dd> Show program&#8217;s version number and exit.</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Show the command line options which are accepted by Phatch</dd>
<dt><code>-c</code>, <code>&#8211;console</code></dt>
<dd> Run Phatch as console program without a gui</dd>
<dt><code>-d</code>, <code>&#8211;droplet</code></dt>
<dd> Run Phatch as a gui droplet</dd>
<dt><code>&#8211;desktop</code></dt>
<dd> Save always on desktop</dd>
<dt><code>-f</code>, <code>&#8211;force</code></dt>
<dd> Ignore errors</dd>
<dt><code>&#8211;fonts</code></dt>
<dd> Initialize fonts (only for installation scripts)</dd>
<dt><code>-i</code>, <code>&#8211;interactive</code></dt>
<dd> Interactive</dd>
<dt><code>-k</code>, <code>&#8211;keep</code></dt>
<dd> Keep existing images (don&#8217;t overwrite)</dd>
<dt><code>-l LOCALE</code></dt>
<dd> Specify locale language (for example en or en_GB)</dd>
<dt><code>-n</code>, <code>&#8211;inspect</code></dt>
<dd> Inspect metadata (requires exif &amp; iptc plugin)</dd>
<dt><code>&#8211;no-save</code></dt>
<dd> No save action required at the end</dd>
<dt><code>-r</code>, <code>&#8211;recursive</code></dt>
<dd> Include all subfolders</dd>
<dt><code>-t</code>, <code>&#8211;trust</code></dt>
<dd> Do not check images first</dd>
<dt><code>&#8211;unsafe</code></dt>
<dd> Allow Geek action and unsafe expressions</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Verbose </dd>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>phatch action_list.phatch</dt>
<dd>
</dd><dt>phatch &#8211;verbose &#8211;recursive action_list.py image_file.png image_folder</dt>
<dd>
</dd><dt>phatch &#8211;inspect image_file.jpg</dt>
<dd>
</dd><dt>phatch &#8211;droplet recent</dt>
<dd>
</dd><dt>phatch -l el</dt>
<dd>
</dd></dl>
<h2>AUTHOR</h2>
<p> Stani (spe.stani.be (at) gmail.com) </p>
<h2>Index</h2>
