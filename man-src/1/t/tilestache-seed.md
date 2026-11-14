---
title: "tilestache-seed(1)"
name: "tilestache-seed"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tilestache-seed/"
description: "tilestache-seed – seed a single layer in your TileStache configuration"
---

<h2>NAME</h2>
<p> tilestache-seed &#8211; seed a single layer in your TileStache configuration</p>
<h2>SYNOPSIS</h2>
<p> <code>tilestache-seed</code> [<i>options</i>]<i> zoom</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>tilestache-seed</code> command. </p>
<p> <code>tilestache-seed</code> seeds a single layer in your TileStache configuration. No images are returned, but TileStache ends up with a pre-filled cache. Bounding box is given as a pair of lat/lon coordinates, e.g. &quot;37.788 -122.349 37.833 -122.246&quot;. Output is a list of tile paths as they are created.<br />
 Configuration, BBox, and Layer options are required.</p>
<h2>REQUIRED OPTIONS</h2>
<dl>
<dt><code>-c</code>, <code>&#8211;config</code> <i>file</i></p>
<dd> Path to configuration file. <code>Required</code>.</p>
<dt><code>-l</code>, <code>&#8211;layer</code> <i>layer</i></p>
<dd> Layer name from configuration. <code>Required</code>.</p>
<dt><code>-b</code>, <code>&#8211;bbox</code> <i>south</i> <i>west</i> <i>north</i> <i>east</i></p>
<dd> Bounding box in floating point geographic coordinates. <code>Required</code>.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of options.</p>
<dt><code>-p</code>, <code>&#8211;padding</code> <i>padding</i></p>
<dd> Extra margin of tiles to add around bounded area. Default value is 0 (no extra tiles).</p>
<dt><code>-e</code>, <code>&#8211;extension</code> <i>extension</i></p>
<dd> Optional file type for rendered tiles. Default value is &quot;png&quot; for most image layers and some variety of JSON for Vector or Mapnik Grid providers.</p>
<dt><code>-f</code>, <code>&#8211;progress-file</code> <i>file</i></p>
<dd> Optional JSON progress file that gets written on each iteration, so you don&#8217;t have to pay close attention.</p>
<dt><code>-q</code></p>
<dd> Suppress chatty output, &#8211;progress-file works well with this.</p>
<dt><code>-i, &#8211;include-path</code></p>
<dd> Add the following colon-separated list of paths to Python&#8217;s include path (aka sys.path).</p>
<dt><code>-d, &#8211;output-directory</code></p>
<dd> Optional output directory for tiles, to override configured cache with the equivalent of:<br />
&nbsp;<wbr>{&quot;name&quot;:&nbsp;<wbr>&quot;Disk&quot;,&nbsp;<wbr>&quot;path&quot;:&nbsp;<wbr>&lt;output directory&gt;,&nbsp;<wbr>&quot;dirs&quot;:&nbsp;<wbr>&quot;portable&quot;,&nbsp;<wbr>&quot;gzip&quot;:&nbsp;<wbr>[]}. </p>
<p> More information in <a rel="nofollow" href="http://tilestache.org/doc/#caches.">http://tilestache.org/doc/#caches.</a></p>
<dt><code>&#8211;to-mbtiles</code></p>
<dd> Optional output file for tiles, will be created as an MBTiles 1.1 tileset. See <a rel="nofollow" href="http://mbtiles.org">http://mbtiles.org</a> for more information.</p>
<dt><code>&#8211;from-mbtiles</code></p>
<dd> Optional input file for tiles, will be read as an MBTiles 1.1 tileset. See <a rel="nofollow" href="http://mbtiles.org">http://mbtiles.org</a> for more information. Overrides &#8211;extension, &#8211;bbox and &#8211;padding (this may change).</p>
<dt><code>&#8211;to-s3</code></p>
<dd> Optional output bucket for tiles, will be populated with tiles in a standard Z/X/Y layout. Three required arguments: AWS access-key, secret, and bucket name.</p>
<dt><code>&#8211;tile-list</code></p>
<dd> Optional file of tile coordinates, a simple text list of Z/X/Y coordinates. Overrides &#8211;bbox and &#8211;padding.</p>
<dt><code>&#8211;error-list</code></p>
<dd> Optional file of failed tile coordinates, a simple text list of Z/X/Y coordinates. If provided, failed tiles will be logged to this file instead of stopping tilestache-seed.</p>
<dt><code>&#8211;enable-retries</code></p>
<dd> If true this will cause tilestache-seed to retry failed tile renderings up to (3) times. Default value is False.</p>
<dt><code>-x, &#8211;ignore-cached</code></p>
<dd> Re-render every tile, whether it is in the cache already or not.</p>
<dt><code>&#8211;jsonp-callback</code></p>
<dd> Add a JSONP callback for tiles with a json mime-type, causing &quot;*.js&quot; tiles to be written to the cache wrapped in the callback function. Ignored for non-JSON tiles.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tilestache-render/">tilestache-render</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> <code>TileStache</code> was written by Michal Migurski &lt;mike [at] stamen.com&gt;. </p>
<p> This manual page was written by David Paleino &lt;dapal [at] debian.org&gt;, for the Debian project (and may be used by others). </p>
<h2>Index</h2>
