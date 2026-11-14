---
title: "apg(1)"
name: "apg"
section: "1"
letter: "a"
url: "/docs/linux/man/1-apg/"
description: "apg – generates several random passwords"
---

<h2 class="name">NAME</h2>
<p> apg &#8211; generates several random passwords</p>
<h2>SYNOPSIS</h2>
<p> <code>apg</code> [<code>-a algorithm</code>] [<code>-M mode</code>] [<code>-E char_string</code>] [<code>-n num_of_pass</code>] [<code>-m min_pass_len</code>] [<code>-x max_pass_len</code>] [<code>-r</code> <i>dictfile</i>] [<code>-b</code> <i>filter_file</i>] [<code>-p min_substr_len</code>] [<code>-s</code>] [<code>-c cl_seed</code>] [<code>-d</code>] [<code>-y</code>] [<code>-l</code>] [<code>-t</code>] [<code>-q</code>] [<code>-h</code>] [<code>-v</code>] </p>
<h2>DESCRIPTION</h2>
<p> <code>apg</code> generates several random passwords. It uses several password generation algorithms (currently two) and a built-in pseudo random number generator. </p>
<p> Default algorithm is pronounceable password generation algorithm designed by <code>Morrie Gasser</code> and described in <code>A Random Word Generator For Pronounceable Passwords</code> <i>National Technical Information Service (NTIS)</i> <code>AD-A-017676.</code> The original paper is very old and had never been put online, so I have to use <i>NIST</i> implementation described in <code>FIPS-181.</code> </p>
<p> Another algorithm is simple random character generation algorithm, but it uses four user-defined symbol sets to produce random password. It means that user can choose type of symbols that should appear in password. Symbol sets are: numeric symbol set (0,&#8230;,9), capital letters symbol set (A,&#8230;,Z), small letters symbol set (a,&#8230;,z) and special symbols symbol set (#,@,!,&#8230;). </p>
<p> Built-in pseudo random number generator is an implementation of algorithm described in <code>Appendix C of ANSI X9.17</code> or <code>RFC 1750</code> with exception that it uses <i>CAST</i> or <i>SHA-1</i> instead of <i>Triple DES.</i> It uses local time with precision of microseconds (see <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></code>(2)) and <i>/dev/random</i> (if available) to produce initial random seed. </p>
<p> <code>apg</code> also have the ability to check generated password quality using dictionary. You can use this ability if you specify command-line options <code>-r</code> <i>dictfile</i> or <code>-b</code> <i>filtername</i> where <i>dictfile</i> is the dictionary file name and <i>filtername</i> is the name of Bloom filter file. In that dictionary you may place words (one per line) that should not appear as generated passwords. For example: user names, common words, etc. You even can use one of the dictionaries that come with <i>dictionary password crackers.</i> Bloom filter file should be created with <code><a href="/docs/linux/man/1-apgbfm/">apgbfm</a></code>(1) utility included in apg distribution. In future releases I plan to implement some other techniques to check passwords (like pattern check) just to make life easier. </p>
<h2>OPTIONS</h2>
<h3>Password generation modes options</h3>
<dl>
<dt><code>-a algorithm</code></p>
<dd> Use <code>algorithm</code> for password generation.</p>
<dl>
<dt>
<dd> <code>0</code> &#8211; pronounceable password generation (default)<br />
 <code>1</code> &#8211; random character password generation</dl>
<dt><code>-n num_of_pass</code></p>
<dd> Generate <code>num_of_pass</code> number of passwords. Default is 6.</p>
<dt><code>-m min_pass_len</code></p>
<dd> Generate password with minimum length <code>min_pass_len.</code> If <code>min_pass_len &gt; max_pass_len</code> then <code>max_pass_len = min_pass_len</code>. Default minimum password length is 8.</p>
<dt><code>-x max_pass_len</code></p>
<dd> Generate password with maximum length <code>max_pass_len.</code> If <code>min_pass_len &gt; max_pass_len</code> then <code>max_pass_len = min_pass_len</code>. Default maximum password length is 10.</p>
<dt><code>-M mode</code></p>
<dd> Use symbolsets specified with <code>mode</code> for password generation. <code>mode</code> is a text string consisting of characters <code>S</code>, <code>s</code>, <code>N</code>, <code>n</code>, <code>C</code>, <code>c</code>, <code>L</code>, <code>l</code>. Where:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>S</code></p>
<dd> Generator <code>must</code> use special symbol set for every generated password.</p>
<dt><code>s</code></p>
<dd> Generator <code>should</code> use special symbol set for password generation.</p>
<dt><code>N</code></p>
<dd> Generator <code>must</code> use numeral symbol set for every generated password.</p>
<dt><code>n</code></p>
<dd> Generator <code>should</code> use numeral symbol set for password generation.</p>
<dt><code>C</code></p>
<dd> Generator <code>must</code> use capital symbol set for every generated password.</p>
<dt><code>c</code></p>
<dd> Generator <code>should</code> use capital symbol set for password generation.</p>
<dt><code>L</code></p>
<dd> Generator <code>must</code> use small letters symbol set for every generated password (always present if pronounceable password generation algorithm is used).</p>
<dt><code>l</code></p>
<dd> Generator <code>should</code> use small letters symbol set for password generation.</p>
<dt><code>R,r</code></p>
<dd> Not supported any more. Use <code>-E char_string</code> option instead.</dl>
</dl>
<dl>
<dt>
<dd>
 <code>mode</code> can not be more than 4 characters in length. </p>
<p> <code>Note:</code><br />
 Usage of L, M, S, C will slow down password generation process. </p>
<p> <code>Examples:</code><br />
 <code>-M sncl</code><br />
 <code>-M SNCL</code><br />
 <code>-M Cn</code></dl>
<dt><code>-E char_string</code></p>
<dd> Exclude characters in <code>char_string</code> from password generation process (in pronounceable password generation mode you can not exclude small letters). To include special symbols that can be recognized by shell (apostrophe, quotes, dollar sign, etc.) in <code>char_string</code> use the backslashed versions.</p>
<dl>
<dt>
<dd>
<p> <code>Examples:</code> </p>
<p> Command <code>apg -a 1 -M n -n 3 -m 8 -E 23456789</code> will generate a set of passwords that will look like this:<br />
 <code>10100110</code><br />
 <code>01111000</code><br />
 <code>11011101</code> </p>
<p> Command <code>apg -a 1 -M nc -n 3 -m 26 -E GHIJKLMNOPQRSTUVWXYZ</code> will generate a set of passwords that will look like this:<br />
 <code>16A1653CD4DE5E7BD9584A3476</code><br />
 <code>C8F78E06944AFD57FB9CB882BC</code><br />
 <code>8C8DF37CD792D36D056BBD5002</code>
</dl>
</dl>
<h3>Password quality control options</h3>
<dl>
<dt><code>-r </code><i>dictfile</i></p>
<dd> Check generated passwords for their appearance in <i>dictfile</i></p>
<dt><code>-b </code><i>filter_file</i></p>
<dd> Check generated passwords for their appearance in <i>filter_file</i>. <i>filter_file</i> should be created with the <code><a href="/docs/linux/man/1-apgbfm/">apgbfm</a></code>(1) utility.</p>
<dt><code>-p min_substr_len</code></p>
<dd> This option tells <code><a href="/docs/linux/man/1-apg/">apg</a></code>(1) to check every substring of the generated password for appearance in <i>filter_file</i>. If any of such substrings would be found in the <i>filter_file</i> then generated password would be rejected and <a href="/docs/linux/man/1-apg/">apg</a>(1) will generate another one. <code>min_substr_len</code> specifies minimum substring length to check. This option is active only if <code>-b</code> option is defined.</dl>
<h3>Pseudo random number generator options</h3>
<dl>
<dt><code>-s</code></p>
<dd> Ask user for random sequence for password generation</p>
<dt><code>-c cl_seed</code></p>
<dd> Use <code>cl_seed</code> as a random seed for password generation. I use it when i have to generate passwords in a shell script.</p>
<dl>
<dt>
<dd> <code>Examples:</code><br />
 <code>-c /dev/urandom</code><br />
 <code>-c /tmp/seed_file</code></dl>
</dl>
<h3>Password output options</h3>
<dl>
<dt><code>-d</code></p>
<dd> Do NOT use any delimiters between generated passwords. I use it when i have to generate passwords in a shell script.</p>
<dt><code>-y</code></p>
<dd> Print generated passwords and crypted passwords (see <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3))</p>
<dt><code>-q</code></p>
<dd> Quiet mode (do not print warnings)</p>
<dt><code>-l</code></p>
<dd> Spell generated passwords. Useful when you want to read generated password by telephone.</p>
<dl>
<dt>
<dd> <code>WARNING:</code> Think twice before read your password by phone.</dl>
<dt><code>-t</code></p>
<dd> Print pronunciation for generated pronounceable password. Ignored if <code>-a 1</code> is set.</p>
<dt><code>-h</code></p>
<dd> Print help information and exit</p>
<dt><code>-v</code></p>
<dd> Print version information and exit</dl>
<h2>DEFAULT OPTIONS</h2>
<p> <code>apg -a 0 -M sncl -n 6 -x 10 -m 8</code> (new style) </p>
<p> If you want to generate really secure passwords, you should use option <code>-s</code>. To simplify <code>apg</code> usage, you can write a small shell script. For example:<br />
 <code>[begin]&#8212;-&gt; pwgen.sh</code><br />
 <code>#!/bin/sh</code><br />
 <code>/usr/local/bin/apg -m 8 -x 12 -s</code><br />
 <code>[ end ]&#8212;-&gt; pwgen.sh</code></p>
<h2>EXIT CODE</h2>
<p> On successful completion of its task, <code>apg</code> will complete with exit code 0. An exit code of -1 indicates an error occurred. Textual errors are written to the standard error stream.</p>
<h2>DIAGNOSTICS</h2>
<p> If <i>/dev/random</i> is not available, <code>apg</code> will display a message about it.</p>
<h2>FILES</h2>
<p> <code>None.</code></p>
<h2>BUGS</h2>
<p> <code>None.</code> If you&#8217;ve found one, please send bug description to the author.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-apgbfm/">apgbfm</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Adel I. Mirzazhanov, &lt;a-del [at] iname.com&gt;<br />
 Project home page: <a rel="nofollow" href="http://www.adel.nursat.kz/apg/">http://www.adel.nursat.kz/apg/</a> </p>
<h2>Index</h2>
