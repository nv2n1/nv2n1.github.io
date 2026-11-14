---
title: "spi_push(3)"
name: "spi_push"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_push/"
description: "SPI_push – push SPI stack to allow recursive SPI usage"
---

<p>SPI_push &#8211; push SPI stack to allow recursive SPI usage </p>
<h2>Synopsis</h2>
<pre>void SPI_push(void)</pre>
<h2>Description</h2>
<p><code>SPI_push</code> should be called before executing another procedure that might itself wish to use SPI. After <code>SPI_push</code>, SPI is no longer in a &#8220;connected&#8221; state, and SPI function calls will be rejected unless a fresh <code>SPI_connect</code> is done. This ensures a clean separation between your procedure&#8217;s SPI state and that of another procedure you call. After the other procedure returns, call <code>SPI_pop</code> to restore access to your own SPI state. </p>
<p> Note that <code>SPI_execute</code> and related functions automatically do the equivalent of <code>SPI_push</code> before passing control back to the SQL execution engine, so it is not necessary for you to worry about this when using those functions. Only when you are directly calling arbitrary code that might contain <code>SPI_connect</code> calls do you need to issue <code>SPI_push</code> and <code>SPI_pop</code>.</p>
