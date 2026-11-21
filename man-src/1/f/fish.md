---

title: "fish(1)"
name: "fish"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fish/"
description: "fish — the friendly interactive shell"
---

<p> <code>fish</code> &#8212; the friendly interactive shell </p>
<h3>Synopsis</h3>
<pre><code>
fish[OPTIONS][-c command][FILE[ARGUMENTS...]]
</code></pre>
<h3>Description</h3>
<p> fish is a command-line shell written mainly with interactive use in mind. The full manual is available in HTML by using the help command from inside fish. </p>
<p> The following options are available: </p>
<dl>
<dt>&bull;</dt>
<dd> -c or &#8211;command=COMMANDS evaluate the specified commands instead of reading from the commandline</dd>
<dt>&bull;</dt>
<dd> -d or &#8211;debug-level=DEBUG_LEVEL specify the verbosity level of fish. A higher number means higher verbosity. The default level is 1.</dd>
<dt>&bull;</dt>
<dd> -i or &#8211;interactive specify that fish is to run in interactive mode</dd>
<dt>&bull;</dt>
<dd> -l or &#8211;login specify that fish is to run as a login shell</dd>
<dt>&bull;</dt>
<dd> -n or &#8211;no-execute do not execute any commands, only perform syntax checking</dd>
<dt>&bull;</dt>
<dd> -p or &#8211;profile=PROFILE_FILE when fish exits, output timing information on all executed commands to the specified file</dd>
<dt>&bull;</dt>
<dd> -v or &#8211;version display version and exit</dd></dl>
<p> The fish exit status is generally the exit status of the last foreground command. If fish is exiting because of a parse error, the exit status is 127. </p>
