---
title: "rrdresize(1)"
name: "rrdresize"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rrdresize/"
description: "rrdresize – alters the size of an RRA and creates a new .rrd file"
---

<h2 class="name">NAME</h2>
<p> rrdresize &#8211; alters the size of an RRA and creates a new .rrd file </p>
<h2>SYNOPSIS</h2>
<p> <code>rrdtool</code> <code>resize</code> <i>filename</i> <i>rra-num</i> <font SIZE="-1"><code>GROW</code></font><i>|</i><font SIZE="-1"><code>SHRINK</code></font> <i>rows</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>resize</code> function is used to modify the number of rows in an <font SIZE="-1"><code>RRA</code></font>.</p>
<dl>
<dt><i>filename</i></p>
<dd> the name of the <font SIZE="-1"><code>RRD</code></font> you want to alter.</p>
<dt><i>rra-num</i></p>
<dd> the <font SIZE="-1"><code>RRA</code></font> you want to alter. You can find the number using <code>rrdtool info</code>.</p>
<dt><font SIZE="-1"><code>GROW</code></font></p>
<dd> used if you want to add extra rows to an <font SIZE="-1">RRA</font>. The extra rows will be inserted as the rows that are oldest.</p>
<dt><font SIZE="-1"><code>SHRINK</code></font></p>
<dd> used if you want to remove rows from an <font SIZE="-1">RRA</font>. The rows that will be removed are the oldest rows.</p>
<dt><i>rows</i></p>
<dd> the number of rows you want to add or remove.</dl>
<h2>NOTES</h2>
<p> The new .rrd file, with the modified RRAs, is written to the file <code>resize.rrd</code> in the current directory. <code>The original .rrd file is not modified</code>. </p>
<p> It is possible to abuse this tool and get strange results by first removing some rows and then reinserting the same amount (effectively clearing them to be Unknown). You may thus end up with unknown data in one <font SIZE="-1">RRA</font> while at the same timestamp this data is available in another <font SIZE="-1">RRA</font>.</p>
<h2>AUTHOR</h2>
<p> Alex van den Bogaerdt &lt;alex [at] vandenbogaerdt.nl&gt; </p>
<h2>Index</h2>
