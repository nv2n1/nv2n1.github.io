---
title: "proofgeneral(1)"
name: "proofgeneral"
section: "1"
letter: "p"
url: "/docs/linux/man/1-proofgeneral/"
description: "proofgeneral – manual page for proofgeneral ()"
---

<h2>NAME</h2>
<p> proofgeneral &#8211; manual page for proofgeneral ()</p>
<h2>SYNOPSIS</h2>
<p> <code>proofgeneral</code> [<i>OPTION</i>] [<i>FILE</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Launches Emacs Proof General, editing the proof script FILE.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;emacs</code></p>
<dd> startup Proof General with emacs (GNU Emacs)</p>
<dt><code>&#8211;xemacs</code></p>
<dd> startup Proof General with xemacs (XEmacs)</p>
<dt><code>&#8211;emacsbin</code> &lt;EMACS&gt;</p>
<dd> startup Proof General with emacs binary &lt;EMACS&gt;</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help and exit</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> Unrecognized options are passed to Emacs, along with file names.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>proofgeneral Example.thy</p>
<dd> Load Proof General editing Isar file Example.thy</p>
<dt>proofgeneral example.v</p>
<dd> Load Proof General editing Coq file Example.v</dl>
<p> For documentation and latest versions, visit <a rel="nofollow" href="http://proofgeneral.inf.ed.ac.uk.">http://proofgeneral.inf.ed.ac.uk.</a></p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;da+pg-bugs [at] inf.ed.ac.uk&gt;. </p>
<p> David Aspinall.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1998-2005 LFCS, University of Edinburgh, UK.<br />
 This is free software; see the source for copying conditions.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>proofgeneral</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>proofgeneral</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info proofgeneral</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
