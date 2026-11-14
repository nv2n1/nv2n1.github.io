---
title: "sucrack(1)"
name: "sucrack"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sucrack/"
description: "sucrack is a multithreaded Linux/UNIX tool for brute-force cracking of local user accounts via su."
---

<h2 class="name">NAME</h2>
<p> <code>sucrack</code> is a multithreaded Linux/UNIX tool for brute-force cracking of local user accounts via su.</p>
<h2>SYNOPSIS</h2>
<p> <code>sucrack </code> [options] wordlist </p>
<h2>DESCRIPTION</h2>
<p> <code>sucrack</code> is a multithreaded Linux/UNIX tool brute-force cracking tool that drives <a href="/docs/linux/man/1-su/">su</a>(1) with referencing a specific user and uses words from a wordlist as passwords. Running <code>sucrack</code> does not require high privileges on the target system. </p>
<h2>OPTIONS</h2>
<p> <code>sucrack</code> allows reading passwords from stdin. In that case, use &#8216;-&#8216; instead of a filename as wordlist parameter.</p>
<dl>
<dt><code>Common options:</code></p>
<dd>
<dt><i>-h</i></p>
<dd> print help message</p>
<dt><i>-a</i></p>
<dd> use ansi escape codes for nice looking statistics (requires &#8211;enable-statistics configuration flag)</p>
<dt><i>-s &lt;seconds&gt;</i></p>
<dd> statistics display intervall (requires &#8211;enable-statistics configuration flag)</p>
<dt><i>-c</i></p>
<dd> only print statistics if a key other than `q&#8217; is pressed</p>
<dt><i>-r</i></p>
<dd> enable rewriting of dictionary words (see rules below)</p>
<dt><i>-w &lt;num&gt;</i></p>
<dd> number of threads to run with.</p>
<dt><i>-b &lt;size&gt;</i></p>
<dd> size of the word list buffer</p>
<dt><i>-u &lt;user&gt;</i></p>
<dd> user account to su to</p>
<dt><i>-l &lt;rules&gt;</i></p>
<dd> specify certain rules for the rewriting process</dl>
<dl>
<dt><code>Rewriting rules:</code></p>
<dd>
<dt><i>A</i></p>
<dd> Rewrite word with only upper case characters</p>
<dt><i>F</i></p>
<dd> Rewrite word with first character as upper case</p>
<dt><i>L</i></p>
<dd> Rewrite word with last character as upper case</p>
<dt><i>a</i></p>
<dd> Rewrite word with only lower case characters</p>
<dt><i>f</i></p>
<dd> Rewrite word with first character as lower case</p>
<dt><i>l</i></p>
<dd> Rewrite word with last character as lower case</p>
<dt><i>D</i></p>
<dd> Prepend each digit (0-9) to the word</p>
<dt><i>d</i></p>
<dd> Append each digit (0-9) to the word</p>
<dt><i>e</i></p>
<dd> enleet the word</p>
<dt><i>x</i></p>
<dd> apply all rules to a word </p>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><i>SUCRACK_SU_PATH</i></p>
<dd> The path to su (usually /bin/su or /usr/bin/su)</p>
<dt><i>SUCRACK_AUTH_FAILURE</i></p>
<dd> The message su returns on an authentication failure (like &quot;su: Authentication failure&quot; or &quot;su: Sorry&quot;)</p>
<dt><i>SUCRACK_AUTH_SUCCESS</i></p>
<dd> The message that indicates an authentication success. This message must not be a password listed in the wordlist (default is &quot;SUCRACK_SUCCESS&quot;) </p>
</dl>
<h2>AUTHOR</h2>
<dl>
<dt>Nico Leidecker &lt;nfl [at] portcullis-security.com&gt;</p>
<dd> <a rel="nofollow" href="http://www.leidecker.info">http://www.leidecker.info</a> </p>
</dl>
<h2>SEE ALSO</h2>
<dl>
<dt><code><a href="/docs/linux/man/1-su/">su</a>(1)</code></p>
<dd>
</dl>
<h2>Index</h2>
