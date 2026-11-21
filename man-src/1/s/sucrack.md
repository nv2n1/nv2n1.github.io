---

title: "sucrack(1)"
name: "sucrack"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sucrack/"
description: "sucrack is a multithreaded Linux/UNIX tool for brute-force cracking of local user accounts via su."
---

<p> <code>sucrack</code> is a multithreaded Linux/UNIX tool for brute-force cracking of local user accounts via su.</p>
<h2>SYNOPSIS</h2>
<p> <code>sucrack </code> [options] wordlist </p>
<h2>DESCRIPTION</h2>
<p> <code>sucrack</code> is a multithreaded Linux/UNIX tool brute-force cracking tool that drives <a href="/docs/linux/man/1-su/">su</a>(1) with referencing a specific user and uses words from a wordlist as passwords. Running <code>sucrack</code> does not require high privileges on the target system. </p>
<h2>OPTIONS</h2>
<p> <code>sucrack</code> allows reading passwords from stdin. In that case, use &#8216;-&#8216; instead of a filename as wordlist parameter.</p>
<dl>
<dt><code>Common options:</code></dt>
<dd>
</dd><dt><i>-h</i></dt>
<dd> print help message</dd>
<dt><i>-a</i></dt>
<dd> use ansi escape codes for nice looking statistics (requires &#8211;enable-statistics configuration flag)</dd>
<dt><i>-s &lt;seconds&gt;</i></dt>
<dd> statistics display intervall (requires &#8211;enable-statistics configuration flag)</dd>
<dt><i>-c</i></dt>
<dd> only print statistics if a key other than `q&#8217; is pressed</dd>
<dt><i>-r</i></dt>
<dd> enable rewriting of dictionary words (see rules below)</dd>
<dt><i>-w &lt;num&gt;</i></dt>
<dd> number of threads to run with.</dd>
<dt><i>-b &lt;size&gt;</i></dt>
<dd> size of the word list buffer</dd>
<dt><i>-u &lt;user&gt;</i></dt>
<dd> user account to su to</dd>
<dt><i>-l &lt;rules&gt;</i></dt>
<dd> specify certain rules for the rewriting process</dd></dl>
<dl>
<dt><code>Rewriting rules:</code></dt>
<dd>
</dd><dt><i>A</i></dt>
<dd> Rewrite word with only upper case characters</dd>
<dt><i>F</i></dt>
<dd> Rewrite word with first character as upper case</dd>
<dt><i>L</i></dt>
<dd> Rewrite word with last character as upper case</dd>
<dt><i>a</i></dt>
<dd> Rewrite word with only lower case characters</dd>
<dt><i>f</i></dt>
<dd> Rewrite word with first character as lower case</dd>
<dt><i>l</i></dt>
<dd> Rewrite word with last character as lower case</dd>
<dt><i>D</i></dt>
<dd> Prepend each digit (0-9) to the word</dd>
<dt><i>d</i></dt>
<dd> Append each digit (0-9) to the word</dd>
<dt><i>e</i></dt>
<dd> enleet the word</dd>
<dt><i>x</i></dt>
<dd> apply all rules to a word </dd>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><i>SUCRACK_SU_PATH</i></dt>
<dd> The path to su (usually /bin/su or /usr/bin/su)</dd>
<dt><i>SUCRACK_AUTH_FAILURE</i></dt>
<dd> The message su returns on an authentication failure (like &quot;su: Authentication failure&quot; or &quot;su: Sorry&quot;)</dd>
<dt><i>SUCRACK_AUTH_SUCCESS</i></dt>
<dd> The message that indicates an authentication success. This message must not be a password listed in the wordlist (default is &quot;SUCRACK_SUCCESS&quot;) </dd>
</dl>
<h2>AUTHOR</h2>
<dl>
<dt>Nico Leidecker &lt;nfl [at] portcullis-security.com&gt;</dt>
<dd> <a rel="nofollow" href="http://www.leidecker.info">http://www.leidecker.info</a> </dd>
</dl>
<h2>SEE ALSO</h2>
<dl>
<dt><code><a href="/docs/linux/man/1-su/">su</a>(1)</code></dt>
<dd>
</dd></dl>
