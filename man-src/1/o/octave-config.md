---
title: "octave-config(1)"
name: "octave-config"
section: "1"
letter: "o"
url: "/docs/linux/man/1-octave-config/"
description: "octave-config – GNU Octave component and library information retrieval"
---

<h2>NAME</h2>
<p> octave-config &#8211; GNU Octave component and library information retrieval</p>
<h2>SYNOPSIS</h2>
<p> <code>octave-config</code> [<i>OPTION</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>octave-config</code> is a tool to obtain directory information for <code>.oct</code> and <code>.m</code> files for <code><a href="/docs/linux/man/1-octave/">octave</a></code>(1).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;m-site-dir</code></p>
<dd> Display the main directory for local, or site-specific, <code>.m</code> script files.</p>
<dt><code>&#8211;oct-site-dir</code></p>
<dd> Display the main directory for local, or site-specific, <code>.oct</code> dynamic-link libraries.</p>
<dt><code>-p </code><i>VAR</i>,<code> &#8211;print </code><i>VAR</i></p>
<dd> Print the default value of the Octave configuration variable <i>VAR</i>. Recognized variables are:</p>
<dl>
<dt>
<dd>
<pre>
   API_VERSION             LOCALAPIOCTFILEDIR
   ARCHLIBDIR              LOCALARCHLIBDIR
   BINDIR                  LOCALFCNFILEDIR
   CANONICAL_HOST_TYPE     LOCALOCTFILEDIR
   DATADIR                 LOCALSTARTUPFILEDIR
   DATAROOTDIR             LOCALVERARCHLIBDIR
   DEFAULT_PAGER           LOCALVERFCNFILEDIR
   EXEC_PREFIX             LOCALVEROCTFILEDIR
   FCNFILEDIR              MAN1DIR
   IMAGEDIR                MAN1EXT
   INCLUDEDIR              MANDIR
   INFODIR                 OCTFILEDIR
   INFOFILE                OCTINCLUDEDIR
   LIBDIR                  OCTLIBDIR
   LIBEXECDIR              PREFIX
   LOCALAPIARCHLIBDIR      STARTUPFILEDIR
   LOCALAPIFCNFILEDIR      VERSION
</pre>
</dl>
<dt><code>-v</code>,<code> &#8211;version</code></p>
<dd> Display the version number of <code><a href="/docs/linux/man/1-octave/">octave</a></code>(1).</p>
<dt><code>-h</code>, <code>-?</code>, <code>&#8211;help</code></p>
<dd> Print help message.</dl>
<h2>AUTHOR</h2>
<p> John W. Eaton &lt;jwe [at] octave.org&gt; </p>
<p> This manual page was contributed by Dirk Eddelbuettel &lt;edd [at] debian.org&gt; for the Debian GNU/Linux distribution but may be used by others.</p>
<h2>SEE ALSO</h2>
<p> octave (1). </p>
<h2>Index</h2>
