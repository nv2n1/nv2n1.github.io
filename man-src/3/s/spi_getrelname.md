---
title: "spi_getrelname(3)"
name: "spi_getrelname"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_getrelname/"
description: "SPI_getrelname – return the name of the specified relation"
---

<p>SPI_getrelname &#8211; return the name of the specified relation </p>
<h2>Synopsis</h2>
<pre>char * SPI_getrelname(Relation <i>rel</i>)</pre>
<h2>Description</h2>
<p><code>SPI_getrelname</code> returns a copy of the name of the specified relation. (You can use <code>pfree</code> to release the copy of the name when you don&#8217;t need it anymore.)</p>
<h2>Arguments</h2>
<p>Relation <i>rel</i></p>
<dl COMPACT>
<dd>input relation</dl>
<h2>Return Value</h2>
<p>The name of the specified relation.</p>
