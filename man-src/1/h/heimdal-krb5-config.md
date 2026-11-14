---
title: "heimdal-krb5-config(1)"
name: "heimdal-krb5-config"
section: "1"
letter: "h"
url: "/docs/linux/man/1-heimdal-krb5-config/"
description: "krb5-config – give information on how to link code against Heimdal libraries"
---

<h2 class="name">NAME</h2>
<p> <code>krb5-config</code> &#8211; give information on how to link code against Heimdal libraries </p>
<h2>SYNOPSIS</h2>
<p> [-<code>-prefix </code>[= <i>dir</i> ] ] [-<code>-exec-prefix </code>[= <i>dir</i> ] ] [-<code>-libs</code> ] [-<code>-cflags</code> ] [<i>libraries</i> ]</p>
<h2>DESCRIPTION</h2>
<p> tells the application programmer what special flags to use to compile and link programs against the libraries installed by Heimdal. </p>
<p> Options supported:</p>
<dl>
<dt><code>&#8211;prefix </code>[= <i>dir</i> ]</p>
<dd> Print the prefix if no <i>dir</i> is specified, otherwise set prefix to <i>dir</i></p>
<dt><code>&#8211;exec-prefix </code>[= <i>dir</i> ]</p>
<dd> Print the exec-prefix if no <i>dir</i> is specified, otherwise set exec-prefix to <i>dir</i></p>
<dt><code>&#8211;libs</code></p>
<dd> Output the set of libraries that should be linked against.</p>
<dt><code>&#8211;cflags</code></p>
<dd> Output the set of flags to give to the C compiler when using the Heimdal libraries.</dl>
<p> By default will output the set of flags and libraries to be used by a normal program using the krb5 API. The user can also supply a library to be used, the supported ones are:</p>
<dl>
<dt><code>krb5</code></p>
<dd> (the default)</p>
<dt><code>gssapi</code></p>
<dd> use the krb5 gssapi mechanism</p>
<dt><code>kadm-client</code></p>
<dd> use the client-side kadmin libraries</p>
<dt><code>kadm-server</code></p>
<dd> use the server-side kadmin libraries</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cc/">cc</a>(1)</p>
<h2>HISTORY</h2>
<p> appeared in Heimdal 0.3d. </p>
<h2>Index</h2>
