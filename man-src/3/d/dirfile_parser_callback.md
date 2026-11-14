---
title: "dirfile_parser_callback(3)"
name: "dirfile_parser_callback"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dirfile_parser_callback/"
description: "dirfile_parser_callback — set the syntax error callback handler for a dirfile"
---

<h2>NAME</h2>
<p> dirfile_parser_callback &#8212; set the syntax error callback handler for a dirfile</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>void dirfile_parser_callback(DIRFILE *</code><i>dirfile</i><code>, gd_parser_callback_t</code> <i>sehandler</i><code>, void *</code><i>extra</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>dirfile_parser_callback</code>() updates the syntax error callback function of the DIRFILE object <i>dirfile</i> to be <i>sehandler</i>, and the caller supplied extra pointer passed to the handler to be <i>extra</i>, discarding any syntax error handler and extra pointer which were previously registered for this DIRFILE. If <i>sehandler</i> is NULL, the existing handler will be removed and the default behaviour (abort on error) restored. See <code><a href="/docs/linux/man/3-dirfile_cbopen/">dirfile_cbopen</a></code>(3) for a discussion on the requirements for the syntax handler. </p>
<p> Since parsing of an existing format file occurs when the DIRFILE object is created, before this function can be called, this function is only useful to set or modify a callback function or its caller data before calling <code><a href="/docs/linux/man/3-dirfile_include/">dirfile_include</a></code>(3), which will invoke the callback function if syntax errors are found in the included fragment. </p>
<p> This function always succeeds, and has no return value. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-dirfile_cbopen/">dirfile_cbopen</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_include/">dirfile_include</a></code>(3), <code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5) </p>
<h2>Index</h2>
