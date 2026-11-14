---
title: "spi_cursor_close(3)"
name: "spi_cursor_close"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_cursor_close/"
description: "SPI_cursor_close – close a cursor"
---

<p>SPI_cursor_close &#8211; close a cursor </p>
<h2>Synopsis</h2>
<pre>void SPI_cursor_close(Portal <i>portal</i>)</pre>
<h2>Description</h2>
<p><code>SPI_cursor_close</code> closes a previously created cursor and releases its portal storage. </p>
<p> All open cursors are closed automatically at the end of a transaction. <code>SPI_cursor_close</code> need only be invoked if it is desirable to release resources sooner.</p>
<h2>Arguments</h2>
<p>Portal <i>portal</i></p>
<dl COMPACT>
<dd>portal containing the cursor</dl>
