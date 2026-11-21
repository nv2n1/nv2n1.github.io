---
title: "ninja(1)"
name: "ninja"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ninja/"
description: "ninja – small build system closest in spirit to Make"
---

<h2 class="name">NAME</h2>
<p> ninja &#8211; small build system closest in spirit to Make </p>
<h2>DESCRIPTION</h2>
<p> usage: ninja [options] [targets&#8230;] </p>
<p> if targets are unspecified, builds the &#8216;default&#8217; target (see manual).</p>
<h3>options:</h3>
<dl>
<dt><code>&#8211;version</code></dt>
<dd> print ninja version (&quot;1.10.1&quot;)</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> show all command lines while building</dd>
<dt><code>-C</code> DIR</dt>
<dd> change to DIR before doing anything else</dd>
<dt><code>-f</code> FILE</dt>
<dd> specify input build file [default=build.ninja]</dd>
<dt><code>-j</code> N</dt>
<dd> run N jobs in parallel (0 means infinity) [default=#CPUs]</dd>
<dt><code>-k</code> N</dt>
<dd> keep going until N jobs fail (0 means infinity) [default=1]</dd>
<dt><code>-l</code> N</dt>
<dd> do not start new jobs if the load average is greater than N</dd>
<dt><code>-n</code></dt>
<dd> dry run (don&#8217;t run commands but act like they succeeded)</dd>
<dt><code>-d</code> MODE</dt>
<dd> enable debugging (use &#8216;-d list&#8217; to list modes)</dd>
<dt><code>-t</code> TOOL</dt>
<dd> run a subtool (use &#8216;-t list&#8217; to list subtools)</dd>
<dt>
</dt><dd> terminates toplevel options; further flags are passed to the tool</dd>
<dt><code>-w</code> FLAG</dt>
<dd> adjust warnings (use &#8216;-w list&#8217; to list warnings)</dd></dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Gary Kramlich &lt;grim [at] reaperworld.com&gt; for the Debian GNU/Linux system (but may be used by others). </p>
