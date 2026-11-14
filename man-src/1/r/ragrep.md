---
title: "ragrep(1)"
name: "ragrep"
section: "1"
letter: "r"
url: "/docs/linux/man/1-ragrep/"
description: "ragrep – grep argus(8) user captured data."
---

<h2>NAME</h2>
<p> <code>ragrep</code> &#8211; grep <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> user captured data.</p>
<h2>SYNOPSIS</h2>
<p> <code>ragrep</code> [<code>options</code>] <code>-e</code> <i>pattern</i> [<code>raoptions</code>] [<code>&#8212;</code> <i>filter-expression</i>]<br />
 <code>ragrep</code> [<code>options</code>] <code>-f file</code> [<code>raoptions</code>] [<code>&#8211;</code> <i>filter-expression</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Ragrep</code> reads <code>argus</code> data from an <i>argus-data</i> source, greps the records based on the regexp specified on the command line, and outputs a valid <i>argus-stream</i>. </p>
<p> Ragrep works only on the fields for user captured data. Argus must be started with the configration option <code>ARGUS_CAPTURE_DATA_LEN</code> set to a value greater than 0, to have these data captured. See <code><a href="/docs/linux/man/5-argus-conf/">argus.conf</a>(5)</code> for detail. </p>
<p> Ragrep is based on GNU <code><a href="/docs/linux/man/1-grep/">grep</a>(1)</code>, so the <i>regexp</i> syntax is the same as for <code><a href="/docs/linux/man/1-grep/">grep</a>(1)</code>.</p>
<h2>OPTIONS</h2>
<p> Ragrep, like all ra based clients, supports a number of <code>ra options</code> including filtering of input argus records through a terminating filter expression. See <code><a href="/docs/linux/man/1-ra/">ra</a>(1)</code> for a complete description of <code>ra options</code>. <code><a href="/docs/linux/man/1-ragrep/">ragrep</a>(1)</code> specific options are: </p>
<dl>
<dt><code>-c</code></p>
<dd> Suppress normal output; instead print a count of matching lines for each input file. With the <code>-v</code>, <code>&#8211;invert-match</code> option (see below), count non-matching lines. </p>
<dt><code>-e &lt;regex&gt;</code></p>
<dd> Match regular expression in flow user data fields. Prepend the regex with either &quot;s:&quot; or &quot;d:&quot; to limit the match to either the source or destination user data fields. Examples include: </p>
<pre>
   &quot;^SSH-&quot;           - Look for ssh connections on any port.
   &quot;s:^GET&quot;          - Look for HTTP GET requests in the source buffer.
   &quot;d:^HTTP.*Unauth&quot; - Find unauthorized http response.
</pre>
<dt><code>-f</code><i> FILE</i></p>
<dd> Obtain patterns from <i>FILE</i>, one per line. The empty file contains zero patterns, and therefore matches nothing. </p>
<dt><code>-i</code></p>
<dd> Ignore case distinctions in both the <i>PATTERN</i> and the input files. </p>
<dt><code>-L</code></p>
<dd> Suppress normal output; instead print the name of each input file from which no output would normally have been printed. The scanning will stop on the first match. </p>
<dt><code>-l</code></p>
<dd> Suppress normal output; instead print the name of each input file from which output would normally have been printed. The scanning will stop on the first match. </p>
<dt><code>-q</code></p>
<dd> Quiet; do not write anything to standard output. Exit immediately with zero status if any match is found, even if an error was detected. </p>
<dt><code>-R</code></p>
<dd> Read all files under each directory, recursively; this is equivalent to the <code>-d recurse</code> option. </p>
<dt><code>-v</code></p>
<dd> Reverse the expression matching logic. </p>
</dl>
<h2>DIAGNOSTICS</h2>
<p> Normally, exit status is 0 if selected records are found and 1 otherwise. But the exit status is 2 if an error occurred, unless the <code>-q</code> option is used and a selected line is found. </p>
<h2>INVOCATION</h2>
<p> A sample invocation of <code><a href="/docs/linux/man/1-ragrep/">ragrep</a>(1)</code>. This call reads <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data from <code>inputfile</code> and greps all http transactions that generated a &quot;404 Not Found&quot; error. </p>
<dl>
<dt><code>ragrep</code> -r inputfile -e &quot;HTTP.*404&quot;</p>
<dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ra/">ra</a>(1),</code> <code><a href="/docs/linux/man/5-rarc/">rarc</a>(5),</code> <code><a href="/docs/linux/man/8-argus/">argus</a>(8),</code> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2000-2016 QoSient. All rights reserved.</p>
<h2>AUTHORS</h2>
<pre>
Carter Bullard (carter [at] qosient.com).
</pre>
<h2>BUGS</h2>
<h2>Index</h2>
