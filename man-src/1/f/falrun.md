---
title: "falrun(1)"
name: "falrun"
section: "1"
letter: "f"
url: "/docs/linux/man/1-falrun/"
description: "flcrun – The Falcon command line execution tool"
---

<h2>NAME</h2>
<p> flcrun &#8211; The Falcon command line execution tool </p>
<h2>SYNOPSIS</h2>
<p> <code>falrun [options] [main_script] [script_options]</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>falrun</code> command line tool is a subset of the <code><a href="/docs/linux/man/1-falcon/">falcon</a>(1)</code> command line interpreter which only executes pre-compiled falcon scripts in &quot;.fam&quot; module files. This is meant to launch Falcon based application which were compiled on a different system, and whose source is not shipped. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-e&nbsp;<wbr>&lt;enc&gt;</p>
<dd> Set given encoding as default for VM I/O. Unless the scripts select a different I/O encoding, the streams that are provided to the falcon VM (like the output stream for printf) are encoded using the given ISO encoding. This overrides the default encoding that is detected by reading the environment settings. In example, if your system uses iso-8859-1 encoding by default, but you want your script to read and write utf-8 files, use the option </p>
<dt>-h or -?</p>
<dd> Prints a brief help on stdout and exits.</p>
<dt>-L&nbsp;<wbr>&lt;path&gt;</p>
<dd> Changes the default load path. This overrides both the internal built in settings and the contents of environment variable FALCON_LOAD_PATH. Each directory in the path should be separated by &quot;;&quot; and use forward slashes, like this: </p>
<dt>-p&nbsp;<wbr>&lt;module&gt;</p>
<dd> Preloads the given module as if it were loaded by the main script.</p>
<dt>-P</p>
<dd> Ignore default load paths and uses only the paths set via the -L switch.</p>
<dt>-v</p>
<dd> Prints copyright notice and version and exits. </p>
</dl>
<h2>FILES</h2>
<p> <i>/usr/lib/libfalcon_engine.so</i></p>
<dl>
<dt>
<dd> Default location of the Falcon Engine loadable module.</dl>
<p> <i>/usr/lib/falcon</i></p>
<dl>
<dt>
<dd> Default directory containing Falcon binary modules.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt>FALCON_LOAD_PATH</p>
<dd> Default search path for modules loaded by the scripts. </p>
<dt>FALCON_SRC_ENCODING</p>
<dd> Default encoding for the source scripts loaded by falcon (when different from the system default). </p>
<dt>FALCON_VM_ENCODING</p>
<dd> Default encoding for the VM I/O streams (when different from system default). </p>
</dl>
<h2>AUTHOR</h2>
<p> Giancarlo Niccolai &lt;gc [at] falconpl.org&gt; </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-falcon/">falcon</a></code>(1) <code><a href="/docs/linux/man/1-faldisass/">faldisass</a></code>(1) </p>
<h2>LICENSE</h2>
<p> This document is released under the &quot;GNU Free Documentation License, version 1.2&quot;. On Debian systems, the complete text of the Free Documentation License, version 1.2, can be found in /usr/share/common-licenses/. </p>
<h2>Index</h2>
