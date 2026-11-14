---
title: "spi_getnspname(3)"
name: "spi_getnspname"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_getnspname/"
description: "SPI_getnspname – return the namespace of the specified relation"
---

<p>SPI_getnspname &#8211; return the namespace of the specified relation </p>
<h2>Synopsis</h2>
<pre>char * SPI_getnspname(Relation <i>rel</i>)</pre>
<h2>Description</h2>
<p><code>SPI_getnspname</code> returns a copy of the name of the namespace that the specified Relation belongs to. This is equivalent to the relation&#8217;s schema. You should <code>pfree</code> the return value of this function when you are finished with it.</p>
<h2>Arguments</h2>
<p>Relation <i>rel</i></p>
<dl COMPACT>
<dd>input relation</dl>
<h2>Return Value</h2>
<p>The name of the specified relation&#8217;s namespace.</p>
