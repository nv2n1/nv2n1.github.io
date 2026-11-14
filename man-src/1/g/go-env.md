---
title: "go-env(1)"
name: "go-env"
section: "1"
letter: "g"
url: "/docs/linux/man/1-go-env/"
description: "go-env – print Go environment information"
---

<h2 class="name">NAME</h2>
<p> go-env &#8211; print Go environment information </p>
<h2>SYNOPSIS</h2>
<p> <code>go env</code> [ <i>var &#8230;</i> ]</p>
<h2>DESCRIPTION</h2>
<p> Env prints Go environment information. </p>
<p> By default env prints information as a shell script (on Windows, a batch file). If one or more variable names is given as arguments, env prints the value of each named variable on its own line.</p>
<dl>
<dt><code>-json</code></p>
<dd> prints the environment in JSON format instead of as a shell script.</p>
<dt><code>-u</code></p>
<dd> requires one or more arguments and unsets the default setting for the named environment variables, if one has been set with &#8216;go env -w&#8217;.</p>
<dt><code>-w</code></p>
<dd> requires one or more arguments of the form NAME=VALUE and changes the default settings of the named environment variables to the given values.</dl>
<p> For more about environment variables, see &#8216;go help environment&#8217;.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Michael Stapelberg &lt;stapelberg [at] debian.org&gt; and is maintained by the Debian Go Compiler Team &lt;team+go-compiler [at] tracker.debian.org&gt; based on the output of &#8216;go help env&#8217; for the Debian project (and may be used by others). </p>
<h2>Index</h2>
