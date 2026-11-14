---
title: "spi_prepare_cursor(3)"
name: "spi_prepare_cursor"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_prepare_cursor/"
description: "SPI_prepare_cursor – prepare a statement, without executing it yet"
---

<p>SPI_prepare_cursor &#8211; prepare a statement, without executing it yet </p>
<h2>Synopsis</h2>
<pre>SPIPlanPtr SPI_prepare_cursor(const char * <i>command</i>, int <i>nargs</i>,
 Oid * <i>argtypes</i>, int <i>cursorOptions</i>)</pre>
<h2>Description</h2>
<p><code>SPI_prepare_cursor</code> is identical to <code>SPI_prepare</code>, except that it also allows specification of the planner&#8217;s &#8220;cursor options&#8221; parameter. This is a bit mask having the values shown in nodes/parsenodes.h for the options field of DeclareCursorStmt. <code>SPI_prepare</code> always takes the cursor options as zero.</p>
<h2>Arguments</h2>
<p>const char * <i>command</i></p>
<dl COMPACT>
<dd>command string</dl>
<p> int <i>nargs</i></p>
<dl COMPACT>
<dd>number of input parameters ($1, $2, etc.)</dl>
<p> Oid * <i>argtypes</i></p>
<dl COMPACT>
<dd>pointer to an array containing the OIDs of the data types of the parameters</dl>
<p> int <i>cursorOptions</i></p>
<dl COMPACT>
<dd>integer bit mask of cursor options; zero produces default behavior</dl>
<h2>Return Value</h2>
<p><code>SPI_prepare_cursor</code> has the same return conventions as <code>SPI_prepare</code>.</p>
<h2>Notes</h2>
<p>Useful bits to set in <i>cursorOptions</i> include CURSOR_OPT_SCROLL, CURSOR_OPT_NO_SCROLL, CURSOR_OPT_FAST_PLAN, CURSOR_OPT_GENERIC_PLAN, and CURSOR_OPT_CUSTOM_PLAN. Note in particular that CURSOR_OPT_HOLD is ignored.</p>
