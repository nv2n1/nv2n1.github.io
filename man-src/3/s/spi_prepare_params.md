---
title: "spi_prepare_params(3)"
name: "spi_prepare_params"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_prepare_params/"
description: "SPI_prepare_params – prepare a statement, without executing it yet"
---

<p>SPI_prepare_params &#8211; prepare a statement, without executing it yet </p>
<h2>Synopsis</h2>
<pre>SPIPlanPtr SPI_prepare_params(const char * <i>command</i>,
 ParserSetupHook <i>parserSetup</i>,
 void * <i>parserSetupArg</i>,
 int <i>cursorOptions</i>)</pre>
<h2>Description</h2>
<p><code>SPI_prepare_params</code> creates and returns a prepared statement for the specified command, but doesn&#8217;t execute the command. This function is equivalent to <code>SPI_prepare_cursor</code>, with the addition that the caller can specify parser hook functions to control the parsing of external parameter references.</p>
<h2>Arguments</h2>
<p>const char * <i>command</i></p>
<dl COMPACT>
<dd>command string</dl>
<p> ParserSetupHook <i>parserSetup</i></p>
<dl COMPACT>
<dd>Parser hook setup function</dl>
<p> void * <i>parserSetupArg</i></p>
<dl COMPACT>
<dd>passthrough argument for <i>parserSetup</i></dl>
<p> int <i>cursorOptions</i></p>
<dl COMPACT>
<dd>integer bit mask of cursor options; zero produces default behavior</dl>
<h2>Return Value</h2>
<p><code>SPI_prepare_params</code> has the same return conventions as <code>SPI_prepare</code>.</p>
