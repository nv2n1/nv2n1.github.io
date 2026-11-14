---
title: "spi_cursor_fetch(3)"
name: "spi_cursor_fetch"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_cursor_fetch/"
description: "SPI_cursor_fetch – fetch some rows from a cursor"
---

<p>SPI_cursor_fetch &#8211; fetch some rows from a cursor </p>
<h2>Synopsis</h2>
<pre>void SPI_cursor_fetch(Portal <i>portal</i>, bool <i>forward</i>, long <i>count</i>)</pre>
<h2>Description</h2>
<p><code>SPI_cursor_fetch</code> fetches some rows from a cursor. This is equivalent to a subset of the SQL command <code>FETCH</code> (see <code>SPI_scroll_cursor_fetch</code> for more functionality).</p>
<h2>Arguments</h2>
<p>Portal <i>portal</i></p>
<dl COMPACT>
<dd>portal containing the cursor</dl>
<p> bool <i>forward</i></p>
<dl COMPACT>
<dd>true for fetch forward, false for fetch backward</dl>
<p> long <i>count</i></p>
<dl COMPACT>
<dd>maximum number of rows to fetch</dl>
<h2>Return Value</h2>
<p><i>SPI_processed</i> and <i>SPI_tuptable</i> are set as in <code>SPI_execute</code> if successful.</p>
<h2>Notes</h2>
<p>Fetching backward may fail if the cursor&#8217;s plan was not created with the CURSOR_OPT_SCROLL option.</p>
