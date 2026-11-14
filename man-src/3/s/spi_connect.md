---
title: "spi_connect(3)"
name: "spi_connect"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_connect/"
description: "SPI_connect – connect a procedure to the SPI manager"
---

<p>SPI_connect &#8211; connect a procedure to the SPI manager </p>
<h2>Synopsis</h2>
<pre>int SPI_connect(void)</pre>
<h2>Description</h2>
<p><code>SPI_connect</code> opens a connection from a procedure invocation to the SPI manager. You must call this function if you want to execute commands through SPI. Some utility SPI functions can be called from unconnected procedures. </p>
<p> If your procedure is already connected, <code>SPI_connect</code> will return the error code SPI_ERROR_CONNECT. This could happen if a procedure that has called <code>SPI_connect</code> directly calls another procedure that calls <code>SPI_connect</code>. While recursive calls to the SPI manager are permitted when an SQL command called through SPI invokes another function that uses SPI, directly nested calls to <code>SPI_connect</code> and <code>SPI_finish</code> are forbidden. (But see <code>SPI_push</code> and <code>SPI_pop</code>.)</p>
<h2>Return Value</h2>
<p>SPI_OK_CONNECT</p>
<dl COMPACT>
<dd>on success</dl>
<p> SPI_ERROR_CONNECT</p>
<dl COMPACT>
<dd>on error</dl>
