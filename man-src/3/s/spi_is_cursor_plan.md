---
title: "spi_is_cursor_plan(3)"
name: "spi_is_cursor_plan"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_is_cursor_plan/"
description: "SPI_is_cursor_plan – return true if a statement prepared by SPI_prepare can be used with SPI_cursor_open"
---

<p>SPI_is_cursor_plan &#8211; return true if a statement prepared by <code>SPI_prepare</code> can be used with <code>SPI_cursor_open</code> </p>
<h2>Synopsis</h2>
<pre>bool SPI_is_cursor_plan(SPIPlanPtr <i>plan</i>)</pre>
<h2>Description</h2>
<p><code>SPI_is_cursor_plan</code> returns true if a statement prepared by <code>SPI_prepare</code> can be passed as an argument to <code>SPI_cursor_open</code>, or false if that is not the case. The criteria are that the <i>plan</i> represents one single command and that this command returns tuples to the caller; for example, <code>SELECT</code> is allowed unless it contains an INTO clause, and <code>UPDATE</code> is allowed only if it contains a RETURNING clause.</p>
<h2>Arguments</h2>
<p>SPIPlanPtr <i>plan</i></p>
<dl COMPACT>
<dd>prepared statement (returned by <code>SPI_prepare</code>)</dl>
<h2>Return Value</h2>
<p>true or false to indicate if the <i>plan</i> can produce a cursor or not, with <i>SPI_result</i> set to zero. If it is not possible to determine the answer (for example, if the <i>plan</i> is NULL or invalid, or if called when not connected to SPI), then <i>SPI_result</i> is set to a suitable error code and false is returned.</p>
