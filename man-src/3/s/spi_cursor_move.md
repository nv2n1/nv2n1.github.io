---
title: "spi_cursor_move(3)"
name: "spi_cursor_move"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_cursor_move/"
description: "SPI_cursor_move – move a cursor"
---

<p>SPI_cursor_move &#8211; move a cursor </p>
<h2>Synopsis</h2>
<pre>void SPI_cursor_move(Portal <i>portal</i>, bool <i>forward</i>, long <i>count</i>)</pre>
<h2>Description</h2>
<p><code>SPI_cursor_move</code> skips over some number of rows in a cursor. This is equivalent to a subset of the SQL command <code>MOVE</code> (see <code>SPI_scroll_cursor_move</code> for more functionality).</p>
<h2>Arguments</h2>
<p>Portal <i>portal</i></p>
<dl COMPACT>
<dd>portal containing the cursor</dl>
<p> bool <i>forward</i></p>
<dl COMPACT>
<dd>true for move forward, false for move backward</dl>
<p> long <i>count</i></p>
<dl COMPACT>
<dd>maximum number of rows to move</dl>
<h2>Notes</h2>
<p>Moving backward may fail if the cursor&#8217;s plan was not created with the CURSOR_OPT_SCROLL option.</p>
