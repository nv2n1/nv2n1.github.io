---
title: "pw-inspector(1)"
name: "pw-inspector"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pw-inspector/"
description: "pw-inspector – A tool to reduce the password list"
---

<h2>NAME</h2>
<p> pw-inspector &#8211; A tool to reduce the password list</p>
<h2>SYNOPSIS</h2>
<p> <code>pw-inspector</code> [-i FILE] [-o FILE] [-m MINLEN] [-M MAXLEN] [-c MINSETS] -l -u -n -p -s </p>
<h2>DESCRIPTION</h2>
<p> PW-Inspector reads passwords in and prints those which meet the requirements. The return code is the number of valid passwords found, 0 if none was found. Use for security: check passwords, if 0 is returned, reject password choice. Use for hacking: trim your dictionary file to the pw requirements of the target. Usage only allowed for legal purposes.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i FILE</code></p>
<dd> file to read passwords from (default: stdin)</p>
<dt><code>-o FILE</code></p>
<dd> file to write valid passwords to (default: stdout)</p>
<dt><code>-m MINLEN</code></p>
<dd> minimum length of a valid password</p>
<dt><code>-M MAXLEN</code></p>
<dd> maximum length of a valid password</p>
<dt><code>-c MINSETS </code></p>
<dd> the minimum number of sets required (default: all given)</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of options.</dl>
<h2>SETS</h2>
<dl>
<dt><code>-l</code></p>
<dd> lowcase characters (a,b,c,d, etc.)</p>
<dt><code>-u </code></p>
<dd> upcase characters (A,B,C,D, etc.)</p>
<dt><code>-n</code></p>
<dd> numbers (1,2,3,4, etc.)</p>
<dt><code>-p </code></p>
<dd> printable characters (which are not -l/-n/-p, e.g. $,!,/,(,*, etc.)</p>
<dt><code>&nbsp;<wbr>-s</code></p>
<dd> special characters &#8211; all others not withint the sets above</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-hydra/">hydra</a></code>(1), <code><a href="/docs/linux/man/1-xhydra/">xhydra</a></code>(1). </p>
<h2>AUTHOR</h2>
<p> hydra was written by van Hauser / THC &lt;vh [at] thc.org&gt; and co-maintained by David Maciejak &lt;david.maciejak [at] gmail.com&gt;. </p>
<p> This manual page was written by Daniel Echeverry &lt;epsilon77 [at] gmail.com&gt;, for the Debian project (and may be used by others). </p>
<h2>Index</h2>
