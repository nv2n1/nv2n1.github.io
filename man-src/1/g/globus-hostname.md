---
title: "globus-hostname(1)"
name: "globus-hostname"
section: "1"
letter: "g"
url: "/docs/linux/man/1-globus-hostname/"
description: "globus-hostname – Print the system host name"
---

<h2 class="name">NAME</h2>
<p> globus-hostname &#8211; Print the system host name </p>
<h2>SYNOPSIS</h2>
<p> <code>globus-hostname</code> [ -help | -h ] [ -version|-versions ]</p>
<h2>DESCRIPTION</h2>
<p> <code>globus-hostname</code> attempts to determine a fully-qualified name for the host it is executing on. It performs the same name checks that the C globus_common library uses, including checking for the GLOBUS_HOSTNAME environment variable, and optionally performing a name server lookup of the local host name. </p>
<p> The full set of options to <code>globus-hostname</code> are </p>
<p> <code>-help, -h</code></p>
<dl>
<dt>
<dd> Show usage information and exit.</dl>
<p> <code>-version, -versions</code></p>
<dl>
<dt>
<dd> Show version information and exit.</dl>
<h2>AUTHOR</h2>
<p> Copyright &#169; 1999-2016 University of Chicago </p>
<h2>Index</h2>
