---
title: "zim(1)"
name: "zim"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zim/"
description: "zim – A Desktop Wiki Editor"
---

<h2>NAME</h2>
<p> zim &#8211; A Desktop Wiki Editor </p>
<h2>SYNOPSIS</h2>
<p> usage: zim [OPTIONS] [NOTEBOOK [PAGE]]<br />
or: zim &#8211;server&nbsp;<wbr>[OPTIONS]&nbsp;<wbr>[NOTEBOOK]<br />
or: zim &#8211;export&nbsp;<wbr>[OPTIONS]&nbsp;<wbr>NOTEBOOK&nbsp;<wbr>[PAGE]<br />
or: zim &#8211;search NOTEBOOK QUERY<br />
or: zim &#8211;index&nbsp;<wbr>&nbsp;<wbr>NOTEBOOK<br />
or: zim &#8211;plugin PLUGIN&nbsp;<wbr>[ARGUMENTS]<br />
or: zim &#8211;manual&nbsp;<wbr>[OPTIONS]&nbsp;<wbr>[PAGE]<br />
or: zim &#8211;help </p>
<h2>DESCRIPTION</h2>
<p> Zim is a graphical text editor used to maintain a collection of wiki pages. Each page can contain links to other pages, simple formatting and images. Pages are stored in a folder structure, like in an outliner, and can have attachments. Creating a new page is as easy as linking to a nonexistent page. All data is stored in plain text files with wiki formatting. Various plugins provide additional functionality, like a task list manager, an equation editor, a tray icon, and support for version control. </p>
<p> Zim can be used to: * Keep an archive of notes * Take notes during meetings or lectures * Organize task lists * Draft blog entries and emails * Do brainstorming</p>
<h2>OPTIONS</h2>
<p> General Options:<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;gui&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>run the editor&nbsp;<wbr>(this is the default)<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;server&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>run the web server<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;export&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>export to a different format<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;search&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>run a search query on a notebook<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;index&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>build an index for a notebook<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;plugin&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>call a specific plugin function<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;manual&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>open the user manual<br />
&nbsp;<wbr>&nbsp;<wbr>-V, &#8211;verbose&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print information to terminal<br />
&nbsp;<wbr>&nbsp;<wbr>-D, &#8211;debug&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print debug messages<br />
&nbsp;<wbr>&nbsp;<wbr>-v, &#8211;version&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print version and exit<br />
&nbsp;<wbr>&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print this text </p>
<p> GUI Options:<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;list&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show the list with notebooks instead of<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>opening the default notebook<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;geometry&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>window size and position as WxH+X+Y<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;fullscreen&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>start in fullscreen mode<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;standalone&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>start a single instance, no background process </p>
<p> Server Options:<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;port&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>port to use&nbsp;<wbr>(defaults to 8080)<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;template&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>name of the template to use<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;gui&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>run the gui wrapper for the server </p>
<p> Export Options:<br />
&nbsp;<wbr>&nbsp;<wbr>-o, &#8211;output&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>output directory&nbsp;<wbr>(mandatory option)<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;format&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>format to use&nbsp;<wbr>(defaults to&nbsp;<wbr>&#8216;html&#8217;)<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;template&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>name of the template to use<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;root-url&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>url to use for the document root<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;index-page&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>index page name<br />
&nbsp;<wbr>&nbsp;<wbr>-r, &#8211;recursive&nbsp;<wbr>&nbsp;<wbr>when exporting a page, also export sub-pages<br />
&nbsp;<wbr>&nbsp;<wbr>-s, &#8211;singlefile export all pages to a single output file<br />
&nbsp;<wbr>&nbsp;<wbr>-O, &#8211;overwrite&nbsp;<wbr>&nbsp;<wbr>force overwriting existing file(s) </p>
<p> Search Options:<br />
&nbsp;<wbr>&nbsp;<wbr>None </p>
<p> Index Options:<br />
&nbsp;<wbr>&nbsp;<wbr>None </p>
<p> Try &#8216;zim &#8211;manual&#8217; for more help. </p>
<h2>AUTHOR</h2>
<p> Jaap Karssenberg &lt;jaap.karssenberg [at] gmail.com&gt; </p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>zim</code> is maintained as a zim notebook. The command</p>
<dl>
<dt>
<dd> <code>zim &#8211;manual</code></dl>
<p> should give you access to the complete manual. </p>
<p> The website for <code>zim</code> can be found at <i><a rel="nofollow" href="http://www.zim-wiki.org">http://www.zim-wiki.org</a></i> </p>
<h2>Index</h2>
