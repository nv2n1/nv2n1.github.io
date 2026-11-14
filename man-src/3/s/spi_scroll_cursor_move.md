---
title: "spi_scroll_cursor_move(3)"
name: "spi_scroll_cursor_move"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_scroll_cursor_move/"
description: "SPI_scroll_cursor_move – move a cursor"
---

<p>SPI_scroll_cursor_move &#8211; move a cursor </p>
<h2>Synopsis</h2>
<pre>void SPI_scroll_cursor_move(Portal <i>portal</i>, FetchDirection <i>direction</i>,
 long <i>count</i>)</pre>
<h2>Description</h2>
<p><code>SPI_scroll_cursor_move</code> skips over some number of rows in a cursor. This is equivalent to the SQL command <code>MOVE</code>.</p>
<h2>Arguments</h2>
<p>Portal <i>portal</i></p>
<dl COMPACT>
<dd>portal containing the cursor</dl>
<p> FetchDirection <i>direction</i></p>
<dl COMPACT>
<dd>one of FETCH_FORWARD, FETCH_BACKWARD, FETCH_ABSOLUTE or FETCH_RELATIVE</dl>
<p> long <i>count</i></p>
<dl COMPACT>
<dd>number of rows to move for FETCH_FORWARD or FETCH_BACKWARD; absolute row number to move to for FETCH_ABSOLUTE; or relative row number to move to for FETCH_RELATIVE</dl>
<h2>Return Value</h2>
<p><i>SPI_processed</i> is set as in <code>SPI_execute</code> if successful. <i>SPI_tuptable</i> is set to NULL, since no rows are returned by this function.</p>
<h2>Notes</h2>
<p>See the SQL <code><a href="/docs/linux/man/7-fetch/">FETCH</a></code>(7) command for details of the interpretation of the <i>direction</i> and <i>count</i> parameters. </p>
<p> Direction values other than FETCH_FORWARD may fail if the cursor&#8217;s plan was not created with the CURSOR_OPT_SCROLL option.</p>
