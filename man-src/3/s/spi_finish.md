---
title: "spi_finish(3)"
name: "spi_finish"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_finish/"
description: "SPI_finish – disconnect a procedure from the SPI manager"
---

<p>SPI_finish &#8211; disconnect a procedure from the SPI manager </p>
<h2>Synopsis</h2>
<pre>int SPI_finish(void)</pre>
<h2>Description</h2>
<p><code>SPI_finish</code> closes an existing connection to the SPI manager. You must call this function after completing the SPI operations needed during your procedure&#8217;s current invocation. You do not need to worry about making this happen, however, if you abort the transaction via elog(ERROR). In that case SPI will clean itself up automatically. </p>
<p> If <code>SPI_finish</code> is called without having a valid connection, it will return SPI_ERROR_UNCONNECTED. There is no fundamental problem with this; it means that the SPI manager has nothing to do.</p>
<h2>Return Value</h2>
<p>SPI_OK_FINISH</p>
<dl COMPACT>
<dd>if properly disconnected</dl>
<p> SPI_ERROR_UNCONNECTED</p>
<dl COMPACT>
<dd>if called from an unconnected procedure</dl>
