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
<p> <code>pw-inspector</code> [-i FILE] [-o FILE] [-m MINLEN] [-M MAXLEN] [-c MINSETS] -l -u -n -p -s </p>
<p> PW-Inspector reads passwords in and prints those which meet the requirements. The return code is the number of valid passwords found, 0 if none was found. Use for security: check passwords, if 0 is returned, reject password choice. Use for hacking: trim your dictionary file to the pw requirements of the target. Usage only allowed for legal purposes.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i FILE</code></dt>
<dd> file to read passwords from (default: stdin)</dd>
<dt><code>-o FILE</code></dt>
<dd> file to write valid passwords to (default: stdout)</dd>
<dt><code>-m MINLEN</code></dt>
<dd> minimum length of a valid password</dd>
<dt><code>-M MAXLEN</code></dt>
<dd> maximum length of a valid password</dd>
<dt><code>-c MINSETS </code></dt>
<dd> the minimum number of sets required (default: all given)</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> Show summary of options.</dd></dl>
<h2>SETS</h2>
<dl>
<dt><code>-l</code></dt>
<dd> lowcase characters (a,b,c,d, etc.)</dd>
<dt><code>-u </code></dt>
<dd> upcase characters (A,B,C,D, etc.)</dd>
<dt><code>-n</code></dt>
<dd> numbers (1,2,3,4, etc.)</dd>
<dt><code>-p </code></dt>
<dd> printable characters (which are not -l/-n/-p, e.g. $,!,/,(,*, etc.)</dd>
<dt><code>&nbsp;<wbr>-s</code></dt>
<dd> special characters &#8211; all others not withint the sets above</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-hydra/">hydra</a></code>(1), <code><a href="/docs/linux/man/1-xhydra/">xhydra</a></code>(1). </p>
<h2>AUTHOR</h2>
<p> hydra was written by van Hauser / THC &lt;vh [at] thc.org&gt; and co-maintained by David Maciejak &lt;david.maciejak [at] gmail.com&gt;. </p>
<p> This manual page was written by Daniel Echeverry &lt;epsilon77 [at] gmail.com&gt;, for the Debian project (and may be used by others). </p>
