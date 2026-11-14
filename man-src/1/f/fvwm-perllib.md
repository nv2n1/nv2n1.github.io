---
title: "fvwm-perllib(1)"
name: "fvwm-perllib"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwm-perllib/"
description: "fvwm-perllib – shows the documentation of the Fvwm Perl library"
---

<h2 class="name">NAME</h2>
<p> fvwm-perllib &#8211; shows the documentation of the Fvwm Perl library </p>
<h2>SYNOPSIS</h2>
<p> <code>fvwm-perllib</code> [ <code>&#8211;help</code>|<code>-h</code>|<code>-?</code> ] [ <code>&#8211;version</code>|<code>-v</code>|<code>-V</code> ] [ <code>man</code> [ <i>Perl::Class</i> ] ] [ <code>cat</code> [ <i>Perl::Class</i> ] ] [ <code>raw</code> [ <i>Perl::Class</i> ] ] [ <code>dir</code> ]</p>
<h2>DESCRIPTION</h2>
<p> Starting from fvwm-2.5.x versions there is a built-in support for creating fvwm modules in Perl. This <code>fvwm-perllib</code> utility provides help services for the Fvwm Perl library.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code> show the help and exit </p>
<p> <code>&#8211;version</code> show the version and exit </p>
<p> <code>&#8211;man</code> or <code>man</code> [ <i>Perl::Class</i> ] show manual page just like <i><a href="/docs/linux/man/1-man/">man</a></i>(1) </p>
<p> <code>&#8211;cat</code> or <code>cat</code> [ <i>Perl::Class</i> ] show manual page in plain text </p>
<p> <code>&#8211;raw</code> or <code>raw</code> [ <i>Perl::Class</i> ] generate output in man format (not human readable) </p>
<p> <code>&#8211;dir</code> or <code>dir</code> print perllib directory without a trailing end of line</p>
<h2>USAGE</h2>
<p> Use this in the fvwm modules written in Perl: </p>
<pre>
    use lib `fvwm-perllib dir`;
</pre>
<p> Introduction to the Fvwm Perl library: </p>
<pre>
    % fvwm-perllib man
</pre>
<p> Manual page for the <tt>&quot;FVWM::Module&quot;</tt> class: </p>
<pre>
    % fvwm-perllib man FVWM::Module
</pre>
<p> Standard options: </p>
<pre>
    % fvwm-perllib --help
    % fvwm-perllib --version
</pre>
<h2>AUTHORS</h2>
<p> Mikhael Goikhman &lt;migo [at] homemail.com&gt;.</p>
<h2>COPYING</h2>
<p> The script is distributed by the same terms as fvwm itself. See <font SIZE="-1">GNU</font> General Public License for details.</p>
<h2>BUGS</h2>
<p> No known bugs. </p>
<p> Report bugs to fvwm-bug [at] fvwm.org. </p>
<h2>Index</h2>
