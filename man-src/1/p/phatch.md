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
<dt>Phatch [actionlist]</p>
<dd>
<dt>Phatch [options] [actionlist] [image folders/files/urls]</p>
<dd>
<dt>Phatch &#8211;inspect [image files/urls]</p>
<dd>
<dt>Phatch &#8211;droplet [actionlist/recent] [image files/urls]</p>
<dd>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> Show program&#8217;s version number and exit.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show the command line options which are accepted by Phatch</p>
<dt><code>-c</code>, <code>&#8211;console</code></p>
<dd> Run Phatch as console program without a gui</p>
<dt><code>-d</code>, <code>&#8211;droplet</code></p>
<dd> Run Phatch as a gui droplet</p>
<dt><code>&#8211;desktop</code></p>
<dd> Save always on desktop</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> Ignore errors</p>
<dt><code>&#8211;fonts</code></p>
<dd> Initialize fonts (only for installation scripts)</p>
<dt><code>-i</code>, <code>&#8211;interactive</code></p>
<dd> Interactive</p>
<dt><code>-k</code>, <code>&#8211;keep</code></p>
<dd> Keep existing images (don&#8217;t overwrite)</p>
<dt><code>-l LOCALE</code></p>
<dd> Specify locale language (for example en or en_GB)</p>
<dt><code>-n</code>, <code>&#8211;inspect</code></p>
<dd> Inspect metadata (requires exif &amp; iptc plugin)</p>
<dt><code>&#8211;no-save</code></p>
<dd> No save action required at the end</p>
<dt><code>-r</code>, <code>&#8211;recursive</code></p>
<dd> Include all subfolders</p>
<dt><code>-t</code>, <code>&#8211;trust</code></p>
<dd> Do not check images first</p>
<dt><code>&#8211;unsafe</code></p>
<dd> Allow Geek action and unsafe expressions</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Verbose </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>phatch action_list.phatch</p>
<dd>
<dt>phatch &#8211;verbose &#8211;recursive action_list.py image_file.png image_folder</p>
<dd>
<dt>phatch &#8211;inspect image_file.jpg</p>
<dd>
<dt>phatch &#8211;droplet recent</p>
<dd>
<dt>phatch -l el</p>
<dd>
</dl>
<h2>AUTHOR</h2>
<p> Stani (spe.stani.be (at) gmail.com) </p>
<h2>Index</h2>
