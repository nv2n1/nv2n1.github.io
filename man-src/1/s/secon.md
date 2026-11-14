---
title: "secon(1)"
name: "secon"
section: "1"
letter: "s"
url: "/docs/linux/man/1-secon/"
description: "secon – See an SELinux context, from a file, program or user input."
---

<h2>NAME</h2>
<p> secon &#8211; See an SELinux context, from a file, program or user input.</p>
<h2>SYNOPSIS</h2>
<p> <code>secon</code> [<code>-hVurtscmPRfLp</code>] [<i>CONTEXT</i>]<br />
 [<code>&#8211;file</code>] <i>FILE</i><br />
 [<code>&#8211;link</code>] <i>FILE</i><br />
 [<code>&#8211;pid</code>] <i>PID</i></p>
<h2>DESCRIPTION</h2>
<p> See a part of a context. The context is taken from a file, pid, user input or the context in which <code>secon</code> is originally executed.</p>
<dl>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> shows the current version of secon</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> shows the usage information for secon</p>
<dt><code>-P</code>, <code>&#8211;prompt</code></p>
<dd> outputs data in a format suitable for a prompt</p>
<dt><code>-C</code>, <code>&#8211;color</code></p>
<dd> outputs data with the associated ANSI color codes (requires -P)</p>
<dt><code>-u</code>, <code>&#8211;user</code></p>
<dd> show the user of the security context</p>
<dt><code>-r</code>, <code>&#8211;role</code></p>
<dd> show the role of the security context</p>
<dt><code>-t</code>, <code>&#8211;type</code></p>
<dd> show the type of the security context</p>
<dt><code>-s</code>, <code>&#8211;sensitivity</code></p>
<dd> show the sensitivity level of the security context</p>
<dt><code>-c</code>, <code>&#8211;clearance</code></p>
<dd> show the clearance level of the security context</p>
<dt><code>-m</code>, <code>&#8211;mls-range</code></p>
<dd> show the sensitivity level and clearance, as a range, of the security context</p>
<dt><code>-R</code>, <code>&#8211;raw</code></p>
<dd> outputs the sensitivity level and clearance in an untranslated format.</p>
<dt><code>-f</code>, <code>&#8211;file</code></p>
<dd> gets the context from the specified file FILE</p>
<dt><code>-L</code>, <code>&#8211;link</code></p>
<dd> gets the context from the specified file FILE (doesn&#8217;t follow symlinks)</p>
<dt><code>-p</code>, <code>&#8211;pid</code></p>
<dd> gets the context from the specified process PID</p>
<dt><code>&#8211;pid-exec</code></p>
<dd> gets the exec context from the specified process PID</p>
<dt><code>&#8211;pid-fs</code></p>
<dd> gets the fscreate context from the specified process PID</p>
<dt><code>&#8211;pid-key</code></p>
<dd> gets the key context from the specified process PID</p>
<dt><code>&#8211;current</code>, <code>&#8211;self</code></p>
<dd> gets the context from the current process</p>
<dt><code>&#8211;current-exec</code>, <code>&#8211;self-exec</code></p>
<dd> gets the exec context from the current process</p>
<dt><code>&#8211;current-fs</code>, <code>&#8211;self-fs</code></p>
<dd> gets the fscreate context from the current process</p>
<dt><code>&#8211;current-key</code>, <code>&#8211;self-key</code></p>
<dd> gets the key context from the current process</p>
<dt><code>&#8211;parent</code></p>
<dd> gets the context from the parent of the current process</p>
<dt><code>&#8211;parent-exec</code></p>
<dd> gets the exec context from the parent of the current process</p>
<dt><code>&#8211;parent-fs</code></p>
<dd> gets the fscreate context from the parent of the current process</p>
<dt><code>&#8211;parent-key</code></p>
<dd> gets the key context from the parent of the current process</dl>
<p> Additional argument <i>CONTEXT</i> may be provided and will be used if no options have been specified to make <code>secon</code> get its context from another source. If that argument is <i>&#8211;</i> then the context will be read from stdin.<br />
 If there is no argument, <code>secon</code> will try reading a context from stdin, if that is not a tty, otherwise <code>secon</code> will act as though <code>&#8211;self</code> had been passed. </p>
<p> If none of <code>&#8211;user</code>, <code>&#8211;role</code>, <code>&#8211;type</code>, <code>&#8211;level</code> or <code>&#8211;mls-range</code> is passed. Then all of them will be output. </p>
<h2>SEE ALSO</h2>
<p> <code>chcon</code> (1)</p>
<h2>AUTHORS</h2>
<pre>
James Antill (james.antill [at] redhat.com) 
</pre>
<h2>Index</h2>
