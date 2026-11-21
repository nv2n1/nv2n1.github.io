---

title: "mtx-fonts(1)"
name: "mtx-fonts"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mtx-fonts/"
description: "mtx-fonts – ConTeXt Font Database Management"
---

<p> <code>mtxrun &#8211;script fonts [</code> <i>OPTIONS &#8230;</i> <code>] [</code> <i>FILENAMES</i> <code>]</code></p>
<p> <code>ConTeXt Font Database Management</code></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;convert</code></dt>
<dd> save open type font in raw table</dd>
<dt><code>&#8211;unpack</code></dt>
<dd> save a tma file in a more readable format</dd>
<dt><code>&#8211;reload</code></dt>
<dd> generate new font database (use &#8211;force when in doubt)</dd>
<dt><code>&#8211;reload</code></dt>
<dd> &#8211;simple:generate luatex-fonts-names.lua (not for context!)</dd>
<dt><code>&#8211;list</code></dt>
<dd> &#8211;name: list installed fonts, filter by name [&#8211;pattern]</dd>
<dt><code>&#8211;list</code></dt>
<dd> &#8211;spec: list installed fonts, filter by spec [&#8211;filter]</dd>
<dt><code>&#8211;list</code></dt>
<dd> &#8211;file: list installed fonts, filter by file [&#8211;pattern]</dd>
<dt><code>&#8211;pattern=str</code></dt>
<dd> filter files using pattern</dd>
<dt><code>&#8211;filter=list</code></dt>
<dd> key-value pairs</dd>
<dt><code>&#8211;all</code></dt>
<dd> show all found instances (combined with other flags)</dd>
<dt><code>&#8211;info</code></dt>
<dd> give more details</dd>
<dt><code>&#8211;trackers=list</code></dt>
<dd> enable trackers</dd>
<dt><code>&#8211;statistics</code></dt>
<dd> some info about the database</dd>
<dt><code>&#8211;names</code></dt>
<dd> use name instead of unicodes</dd>
<dt><code>&#8211;cache=str</code></dt>
<dd> use specific cache (otl or otf)</dd></dl>
<h2>AUTHOR</h2>
<p> More information about ConTeXt and the tools that come with it can be found at: </p>
<p> <code>maillist:</code> ntg-context [at] ntg.nl / <a rel="nofollow" href="http://www.ntg.nl/mailman/listinfo/ntg-context">http://www.ntg.nl/mailman/listinfo/ntg-context</a> </p>
<p> <code>webpage:</code> <a rel="nofollow" href="http://www.pragma-ade.nl">http://www.pragma-ade.nl</a> / <a rel="nofollow" href="http://tex.aanhet.net">http://tex.aanhet.net</a> </p>
<p> <code>wiki:</code> <a rel="nofollow" href="http://contextgarden.net">http://contextgarden.net</a> </p>
