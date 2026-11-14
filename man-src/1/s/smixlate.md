---
title: "smixlate(1)"
name: "smixlate"
section: "1"
letter: "s"
url: "/docs/linux/man/1-smixlate/"
description: "smixlate – translate SMI/SPPI identifiers"
---

<h2>NAME</h2>
<p> smixlate &#8211; translate SMI/SPPI identifiers</p>
<h2>SYNOPSIS</h2>
<p> <code>smixlate</code> [ <code>-Vhm</code> ] [ <code>-c </code><i>file</i> ] [ <code>-p </code><i>module</i> ] [ <code>-l </code><i>level</i> ] <i>module(s)</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>smixlate</code> program is used to translate identifiers and especially OIDs into a more human readable format.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-V, &#8211;version</code></p>
<dd> Show the smixlate version and exit.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show a help text and exit.</p>
<dt><code>-r, &#8211;recursive</code></p>
<dd> Report errors and warnings also for recursively imported modules.</p>
<dt><code>-c </code><i>file</i><code>, &#8211;config=</code><i>file</i></p>
<dd> Read <i>file</i> instead of any other (global and user) configuration file.</p>
<dt><code>-p </code><i>module</i><code>, &#8211;preload=</code><i>module</i></p>
<dd> Preload the module <i>module</i> before reading the main module(s). This may be helpful if an incomplete main module misses to import some definitions.</p>
<dt><code>-l </code><i>level</i><code>, &#8211;level=</code><i>level</i></p>
<dd> Report errors and warnings up to the given severity <i>level</i>. See the <a href="/docs/linux/man/1-smilint/">smilint</a>(1) manual page for a description of the error levels. The default error level is 3.</p>
<dt><code>-a, &#8211;all</code></p>
<dd> Replace all OIDs including OID prefixes. Without this option, smixlate will only translate OIDs with a corresponding notification, scalar, column, row, or table definition.</p>
<dt><code>-f, &#8211;format</code></p>
<dd> Preserve the input format as much as possible by inserting/removing white space characters.</p>
<dt><i>module(s)</i></p>
<dd> These are the modules to be loaded for the subsequent translation. If a module argument represents a path name (identified by containing at least one dot or slash character), this is assumed to be the exact file to read. Otherwise, if a module is identified by its plain module name, it is searched according to libsmi internal rules. See <code><a href="/docs/linux/man/3-smi_config/">smi_config</a>(3)</code> for more details.</dl>
<h2>EXAMPLE</h2>
<p> This example translates numeric OIDs in the input text into a more human readable format. </p>
<pre>
  $ echo &quot;what is this oid? 1.3.6.1.2.1.2.2.1.3&quot; | &nbsp;<wbr>   
    ./smixlate -l 0 /usr/local/share/mibs/ietf/*
  what is this oid? ifType
  $
</pre>
<h2>SEE ALSO</h2>
<p> The <code><a href="/docs/linux/man/3-libsmi/">libsmi</a></code>(3) project is documented at <code><a rel="nofollow" href="http://www.ibr.cs.tu-bs.de/projects/libsmi/">http://www.ibr.cs.tu-bs.de/projects/libsmi/</a></code>.</p>
<h2>AUTHORS</h2>
<p> (C) 2006-2006 J. Schoenwaelder, International University Bremen, Germany<br />
 and contributions by many other people. </p>
<h2>Index</h2>
