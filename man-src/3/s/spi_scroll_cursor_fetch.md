---
title: "spi_scroll_cursor_fetch(3)"
name: "spi_scroll_cursor_fetch"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_scroll_cursor_fetch/"
description: "SPI_scroll_cursor_fetch – fetch some rows from a cursor"
---

<p>SPI_scroll_cursor_fetch &#8211; fetch some rows from a cursor </p>
<h2>Synopsis</h2>
<pre>void SPI_scroll_cursor_fetch(Portal <i>portal</i>, FetchDirection <i>direction</i>,
 long <i>count</i>)</pre>
<h2>Description</h2>
<p><code>SPI_scroll_cursor_fetch</code> fetches some rows from a cursor. This is equivalent to the SQL command <code>FETCH</code>.</p>
<h2>Arguments</h2>
<p>Portal <i>portal</i></p>
<dl COMPACT>
<dd>portal containing the cursor</dl>
<p> FetchDirection <i>direction</i></p>
<dl COMPACT>
<dd>one of FETCH_FORWARD, FETCH_BACKWARD, FETCH_ABSOLUTE or FETCH_RELATIVE</dl>
<p> long <i>count</i></p>
<dl COMPACT>
<dd>number of rows to fetch for FETCH_FORWARD or FETCH_BACKWARD; absolute row number to fetch for FETCH_ABSOLUTE; or relative row number to fetch for FETCH_RELATIVE</dl>
<h2>Return Value</h2>
<p><i>SPI_processed</i> and <i>SPI_tuptable</i> are set as in <code>SPI_execute</code> if successful.</p>
<h2>Notes</h2>
<p>See the SQL <code><a href="/docs/linux/man/7-fetch/">FETCH</a></code>(7) command for details of the interpretation of the <i>direction</i> and <i>count</i> parameters. </p>
<p> Direction values other than FETCH_FORWARD may fail if the cursor&#8217;s plan was not created with the CURSOR_OPT_SCROLL option.</p>
