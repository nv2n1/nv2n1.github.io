---
title: "foomatic-searchprinter(1)"
name: "foomatic-searchprinter"
section: "1"
letter: "f"
url: "/docs/linux/man/1-foomatic-searchprinter/"
---


 </p>
<h2>NAME</h2>
<p> foomatic-searchprinter &#8211; Search Foomatic database  </p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>foomatic-searchprinter</code> [-m <i>M</i>] [-dFID] <i>SEARCHTERM</i></dt>
<dt><code>foomatic-searchprinter</code> -h <h2>DESCRIPTION</h2>
<dd> <p> This command displays Foomatic database entries matching <i>SEARCHTERM</i>. </p>
<h3>Options</h3>
<p> <code>-m</code><i>M</i> </p>
 </dd>
<dl>
<dd> <p> Search mode: </p>
<p> <i>M</i> = 0 </p>
 </dd>
<dl>
<dd> <p> Match everything (default) </p>
 </dd></dl>
<p> <i>M</i> = 1 </p>
<dl>
<dd> <p> No matches on only the manufacturer </p>
 </dd></dl>
<p> <i>M</i> = 2 </p>
<dl>
<dd> <p> No matches on only the manufacturer or only the model </p>
 </dd></dl>
<p> <i>M</i> = 3 </p>
<dl>
<dd> <p> Exact matches of device ID, make/model, or Foomatic ID plus matches of the page description language in the device ID to appropriate &quot;Generic&quot; printers </p>
 </dd></dl>
<p> <i>M</i> = 4 </p>
<dl>
<dd> <p> Exact matches of device ID, make/model, or Foomatic ID only </p>
 </dd></dl>
</dl>
<p> <code>-d</code><i>D</i> </p>
<dl>
<dd> <p> Display results: </p>
<p> <i>D</i> = 0 </p>
 </dd>
<dl>
<dd> <p> Everything </p>
 </dd></dl>
<p> <i>D</i> = 1 </p>
<dl>
<dd> <p> Only best match class (default) </p>
 </dd></dl>
<p> <i>D</i> = 2 </p>
<dl>
<dd> <p> Only best match </p>
 </dd></dl>
</dl>
<p> <code>-h</code> </p>
<dl>
<dd> <p> Show help message and exit. </p>
 </dd></dl>
<h2>BUGS</h2>
<p> None so far. </p>
<p> Please post bug reports on </p>
<p> <a rel="nofollow" href="http://lists.freestandards.org/mailman/listinfo/printing-foomatic">http://lists.freestandards.org/mailman/listinfo/printing-foomatic</a> </p>
<h2>Index</h2>
