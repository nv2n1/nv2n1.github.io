---

title: "crudini(1)"
name: "crudini"
section: "1"
letter: "c"
url: "/docs/linux/man/1-crudini/"
description: "crudini – manipulate ini files"
---

<p> crudini &#8211; manipulate ini files</p>
<h2>SYNOPSIS</h2>
<p> <code>crudini</code> <i>,&#8211;set /</i>[<i>,OPTION/</i>]&#8230; <i>,config_file section /</i>[<i>,param/</i>] [<i>,value/</i>]<br />
 <code>crudini</code> <i>,&#8211;get /</i>[<i>,OPTION/</i>]&#8230; <i>,config_file /</i>[<i>,section/</i>] [<i>,param/</i>]<br />
 <code>crudini</code> <i>,&#8211;del /</i>[<i>,OPTION/</i>]&#8230; <i>,config_file section /</i>[<i>,param/</i>] [<i>,list value/</i>]<br />
 <code>crudini</code> <i>,&#8211;merge /</i>[<i>,OPTION/</i>]&#8230; <i>,config_file /</i>[<i>,section/</i>]</p>
<h2>DESCRIPTION</h2>
<p> crudini &#8211; A utility for manipulating ini files</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;existing</code>[=<i>,WHAT/</i>]</dt>
<dd> For <code>&#8211;set</code>, <code>&#8211;del</code> and <code>&#8211;merge</code>, fail if item is missing, where WHAT is &#8216;file&#8217;, &#8216;section&#8217;, or &#8216;param&#8217;, or if not specified; all specifed items.</dd>
<dt><code>&#8211;format</code>=<i>,FMT/</i></dt>
<dd> For <code>&#8211;get</code>, select the output FMT. Formats are sh,ini,lines</dd>
<dt><code>&#8211;inplace</code></dt>
<dd> Lock and write files in place. This is not atomic but has less restrictions than the default replacement method.</dd>
<dt><code>&#8211;list</code></dt>
<dd> For <code>&#8211;set</code> and <code>&#8211;del</code>, update a list (set) of values</dd>
<dt><code>&#8211;list-sep</code>=<i>,STR/</i></dt>
<dd> Delimit list values with &quot;STR&quot; instead of &quot; ,&quot;</dd>
<dt><code>&#8211;output</code>=<i>,FILE/</i></dt>
<dd> Write output to FILE instead. &#8216;-&#8216; means stdout</dd>
<dt><code>&#8211;verbose</code></dt>
<dd> Indicate on stderr if changes were made</dd></dl>
<h2>EXAMPLES</h2>
<p> # Add/Update a var</p>
<dl>
<dt>
</dt><dd> crudini &#8211;set config_file section parameter value</dd></dl>
<p> # Update an existing var</p>
<dl>
<dt>
</dt><dd> crudini &#8211;set &#8211;existing config_file section parameter value</dd></dl>
<p> # Delete a var</p>
<dl>
<dt>
</dt><dd> crudini &#8211;del config_file section parameter</dd></dl>
<p> # Delete a section</p>
<dl>
<dt>
</dt><dd> crudini &#8211;del config_file section</dd></dl>
<p> # output a value</p>
<dl>
<dt>
</dt><dd> crudini &#8211;get config_file section parameter</dd></dl>
<p> # output a global value not in a section</p>
<dl>
<dt>
</dt><dd> crudini &#8211;get config_file &#8221; parameter</dd></dl>
<p> # output a section</p>
<dl>
<dt>
</dt><dd> crudini &#8211;get config_file section</dd></dl>
<p> # output a section, parseable by shell</p>
<dl>
<dt>
</dt><dd> eval $(crudini &#8211;get &#8211;format=sh config_file section)</dd></dl>
<p> # update an ini file from shell variable(s)</p>
<dl>
<dt>
</dt><dd> echo name=&quot;$name&quot; | crudini &#8211;merge config_file section</dd></dl>
<p> # merge an ini file from another ini</p>
<dl>
<dt>
</dt><dd> crudini &#8211;merge config_file &lt; another.ini</dd></dl>
<p> # compare two ini files using standard UNIX text processing</p>
<dl>
<dt>
</dt><dd> diff &lt;(crudini &#8211;get &#8211;format=lines file1.ini|sort) \</dd>
<dt>
</dt><dd> &lt;(crudini &#8211;get &#8211;format=lines file2.ini|sort) </dd>
</dl>
