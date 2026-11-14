---
title: "fish(1)"
name: "fish"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fish/"
description: "fish — the friendly interactive shell"
---

<h2 class="name">NAME</h2>
<p> <code>fish</code> &#8212; the friendly interactive shell </p>
<h3>Synopsis</h3>
<pre><code>
fish[OPTIONS][-c command][FILE[ARGUMENTS...]]
</code></pre>
<h3>Description</h3>
<p> fish is a command-line shell written mainly with interactive use in mind. The full manual is available in HTML by using the help command from inside fish. </p>
<p> The following options are available: </p>
<dl>
<dt>&bull;</p>
<dd> -c or &#8211;command=COMMANDS evaluate the specified commands instead of reading from the commandline</p>
<dt>&bull;</p>
<dd> -d or &#8211;debug-level=DEBUG_LEVEL specify the verbosity level of fish. A higher number means higher verbosity. The default level is 1.</p>
<dt>&bull;</p>
<dd> -i or &#8211;interactive specify that fish is to run in interactive mode</p>
<dt>&bull;</p>
<dd> -l or &#8211;login specify that fish is to run as a login shell</p>
<dt>&bull;</p>
<dd> -n or &#8211;no-execute do not execute any commands, only perform syntax checking</p>
<dt>&bull;</p>
<dd> -p or &#8211;profile=PROFILE_FILE when fish exits, output timing information on all executed commands to the specified file</p>
<dt>&bull;</p>
<dd> -v or &#8211;version display version and exit</dl>
<p> The fish exit status is generally the exit status of the last foreground command. If fish is exiting because of a parse error, the exit status is 127. </p>
<h2>Index</h2>
