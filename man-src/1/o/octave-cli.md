---
title: "octave-cli(1)"
name: "octave-cli"
section: "1"
letter: "o"
url: "/docs/linux/man/1-octave-cli/"
description: "octave-cli – A high-level interactive language for numerical computations."
---

<h2>NAME</h2>
<p> octave-cli &#8211; A high-level interactive language for numerical computations.</p>
<h2>SYNOPSIS</h2>
<p> <code>octave-cli</code> [<i>options</i>]&#8230; [<i>file</i>]</p>
<h2>DESCRIPTION</h2>
<p> Octave is a high-level language, primarily intended for numerical computations. It provides a convenient command line interface for solving linear and nonlinear problems numerically. <code>octave-cli</code> has been compiled without any GUI support (Qt) which makes it smaller than the default <code>octave</code> executable, but also limits it to providing just the command line interface (CLI).</p>
<h2>OPTIONS</h2>
<p> The complete set of command-line options for <code>octave-cli</code> is available by running the following command from the shell. </p>
<pre>
    octave-cli --help
</pre>
<h2>DOCUMENTATION</h2>
<p> The primary documentation for Octave is written using Texinfo, the GNU documentation system, which allows the same source files to be used to produce online and printed versions of the manual. </p>
<p> You can read the online copy of the Octave documentation by issuing the following command from within Octave. </p>
<pre>
    octave:1&gt; doc
</pre>
<p> The Info files may also be read with a stand-alone program such as <code>info</code> or <code>xinfo</code>. HTML, Postscript, or PDF versions of the documentation are installed on many systems as well.</p>
<h2>BUGS</h2>
<p> The Octave project maintains a bug tracker at <a rel="nofollow" href="http://bugs.octave.org.">http://bugs.octave.org.</a> Before submitting a new item please read the instructions at <a rel="nofollow" href="http://www.octave.org/bugs.html">http://www.octave.org/bugs.html</a> on how to submit a useful report.</p>
<h2>FILES</h2>
<p> Upon startup Octave looks for four initialization files. Each file may contain any number of valid Octave commands.</p>
<dl>
<dt><i>octave-home</i>/share/octave/site/m/startup/octaverc</p>
<dd> Site-wide initialization file which changes options for all users. <i>octave-home</i> is the directory where Octave was installed such as <code>/usr/local</code>.</p>
<dt><i>octave-home</i>/share/octave/<i>version</i>/m/startup/octaverc</p>
<dd> Site-wide initialization file for Octave version <i>version</i>.</p>
<dt>~/.octaverc</p>
<dd> User&#8217;s personal initialization file.</p>
<dt>.octaverc</p>
<dd> Project-specific initialization file located in the current directory.</dl>
<h2>AUTHOR</h2>
<p> John W. Eaton &lt;jwe [at] octave.org&gt;</p>
<h2>SEE ALSO</h2>
<p> octave (1) </p>
<h2>Index</h2>
