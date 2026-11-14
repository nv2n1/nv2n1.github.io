---
title: "spi_cursor_find(3)"
name: "spi_cursor_find"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_cursor_find/"
description: "SPI_cursor_find – find an existing cursor by name"
---

<p>SPI_cursor_find &#8211; find an existing cursor by name </p>
<h2>Synopsis</h2>
<pre>Portal SPI_cursor_find(const char * <i>name</i>)</pre>
<h2>Description</h2>
<p><code>SPI_cursor_find</code> finds an existing portal by name. This is primarily useful to resolve a cursor name returned as text by some other function.</p>
<h2>Arguments</h2>
<p>const char * <i>name</i></p>
<dl COMPACT>
<dd>name of the portal</dl>
<h2>Return Value</h2>
<p>pointer to the portal with the specified name, or NULL if none was found</p>
