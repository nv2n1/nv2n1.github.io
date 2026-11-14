---
title: "spi_exec(3)"
name: "spi_exec"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_exec/"
description: "SPI_exec – execute a read/write command"
---

<p>SPI_exec &#8211; execute a read/write command </p>
<h2>Synopsis</h2>
<pre>int SPI_exec(const char * <i>command</i>, long <i>count</i>)</pre>
<h2>Description</h2>
<p><code>SPI_exec</code> is the same as <code>SPI_execute</code>, with the latter&#8217;s <i>read_only</i> parameter always taken as false.</p>
<h2>Arguments</h2>
<p>const char * <i>command</i></p>
<dl COMPACT>
<dd>string containing command to execute</dl>
<p> long <i>count</i></p>
<dl COMPACT>
<dd>maximum number of rows to return, or 0 for no limit</dl>
<h2>Return Value</h2>
<p>See <code>SPI_execute</code>.</p>
