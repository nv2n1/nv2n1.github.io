---
title: "apgd(8)"
name: "apgd"
section: "8"
letter: "a"
url: "/docs/linux/man/8-apgd/"
description: "apgd – server that generates several random passwords"
---

<p>apgd &#8211; server that generates several random passwords </p>
<h2>Synopsis</h2>
<p><code>apgd</code> [<code>-a algorithm</code>] [<code>-M mode</code>] [<code>-E char_string</code>] [<code>-n num_of_pass</code>] [<code>-m min_pass_len</code>] [<code>-x max_pass_len</code>] [<code>-r</code> <i>dictfile</i>] [<code>-b</code> <i>filter_file</i>] [<code>-p min_substr_len</code>] [<code>-k</code>] [<code>-t</code>] [<code>-l</code>] </p>
<h2>Description</h2>
<p><code>apgd</code> program is a server that supports <code>Password Generation Protocol</code> described in <code>RFC972.</code> It uses several password generation algorithms (currently two) and a built-in pseudo random number generator. <code>apgd</code> is normally invoked by the Internet superserver (see <code>inetd</code> (8)) for requests to connect to the pwdgen port (pwdgen port is 129 according to <code>RFC1700</code> ) as indicated by the <i>/etc/services</i> file (see <code>services</code> (5)). Default algorithm is pronounceable password generation algorithm designed by <code>Morrie Gasser</code> and described in <code>A Random Word Generator For Pronounceable Passwords</code> <i>National Technical Information Service (NTIS)</i> <code>AD-A-017676.</code> The original paper is very old and had never been put online, so I have to use <i>NIST</i> implementation described in <code>FIPS-181.</code> Another algorithm is simple random character generation algorithm, but it uses four user-defined symbol sets to produce random password. It means that user can choose type of symbols that should appear in password. Symbol sets are: numeric symbol set <i>(0,&#8230;,9)</i> , capital letters symbol set <i>(A,&#8230;,Z)</i> , small letters symbol set <i>(a,&#8230;,z)</i> and special symbols symbol set <i>(#,@,!,&#8230;).</i> Built-in pseudo random number generator is an implementation of algorithm described in <code>Appendix C of ANSI X9.17</code> or <code>RFC1750</code> with exception that it uses <i>CAST</i> or <i>SHA-1</i> instead of <i>Triple DES.</i> It uses local time with precision of microseconds (see <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></code>(2)) and <i>/dev/random</i> (if available) to produce initial random seed. <code>apgd</code> also have the ability to check generated password quality using dictionary. You can use this ability if you specify command-line option <code>-r</code> <i>dictfile</i> or <code>-b</code> <i>filtername</i> where <i>dictfile</i> is dictionary file name and <i>filtername</i> is the name of Bloom filter file. In that dictionary you may place words (one per line) that should not appear as generated passwords. For example: user names common words, etc. You even can use one of the dictionaries that come with <i>dictionary password crackers.</i> Bloom filter file should be created with <code><a href="/docs/linux/man/1-apgbfm/">apgbfm</a></code>(1) utility included in apg distribution. In future releases I plan to implement some other techniques to check passwords just to make life easier. <code>apgd</code> has the ability log user password generation activity and internal debug information. It does this using<br />
 <i>facility</i> = <i>daemon</i></p>
<dl>
<dd><i>priority</i> = <i>info</i> for user password generation activity logging<br />
 <i>priority</i> = <i>debug</i> for internal debug information
</dl>
<p> See the <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8) and <code><a href="/docs/linux/man/5-syslog-conf/">syslog.conf</a></code>(5) man pages for information on how to configure your syslog daemon. </p>
<h2>Options</h2>
<h3>Password generation modes options</h3>
<dl>
<dt><code>-a algorithm</code></p>
<dd>use <code>algorithm</code> for password generation.</p>
<dl>
<dd><code>0</code> &#8211; (default) pronounceable password generation<br />
 <code>1</code> &#8211; random character password generation</dl>
<dt><code>-n num_of_pass</code></p>
<dd>generate <code>num_of_pass</code> number of passwords. Default is 6.</p>
<dt><code>-m min_pass_len</code></p>
<dd>generate password with minimum length <code>min_pass_len.</code> If <code>min_pass_len &gt; max_pass_len</code> then <code>max_pass_len = min_pass_len</code>. Default minimum password length is 8.</p>
<dt><code>-x max_pass_len</code></p>
<dd>generate password with maximum length <code>max_pass_len</code> If <code>min_pass_len &gt; max_pass_len</code> then <code>max_pass_len = min_pass_len</code>. Default maximum password length is 10.</p>
<dt><code>-M mode</code></p>
<dd>Use symbolsets specified with <code>mode</code> for password generation. <code>mode</code> is a text string consisting of characters <code>S</code>, <code>s</code>, <code>N</code>, <code>n</code>, <code>C</code>, <code>c</code>, <code>L</code>, <code>l</code>. Where:</p>
<dl>
<dd>
<dl>
<dt><code>S</code></p>
<dd>generator <code>must</code> use special symbol set for every generated password.</p>
<dt><code>s</code></p>
<dd>generator <code>should</code> use special symbol set for password generation.</p>
<dt><code>N</code></p>
<dd>generator <code>must</code> use numeral symbol set for every generated password.</p>
<dt><code>n</code></p>
<dd>generator <code>should</code> use numeral symbol set for password generation.</p>
<dt><code>C</code></p>
<dd>generator <code>must</code> use capital symbol set for every generated password.</p>
<dt><code>c</code></p>
<dd>generator <code>should</code> use capital symbol set for password generation.</p>
<dt><code>L</code></p>
<dd>generator <code>must</code> use small letters symbol set for every generated password (always present if pronounceable password generation algorithm is used).</p>
<dt><code>l</code></p>
<dd>generator <code>should</code> use small letters symbol set for password generation.</p>
<dt><code>R,r</code></p>
<dd>not supported any more. Use <code>-E char_string</code> option instead.</dl>
</dl>
<dl>
<dd><code>mode</code> can not be more than 4 characters in length. </p>
<p> <code>Note:</code><br />
 Usage of L, M, N, C will slow down password generation process. </p>
<p> <code>Examples:</code><br />
 <code>-M sncl</code> or <code>-M SNCL</code> or <code>-M Cn</code></dl>
<dt><code>-E char_string</code></p>
<dd>exclude characters in <code>char_string</code> from password generation process (in pronounceable password generation mode you can not exclude small letters). To include special symbols that can be recognized by shell (apostrophe, quotes, dollar sign, etc.) in <code>char_string</code> use the backslashed versions.</p>
<dl>
<dd><code>Examples:</code> </p>
<p> Command <code>apgd -a 1 -M n -n 3 -m 8 -e 23456789</code> will generate a set of passwords that will look like this<br />
 <code>10100110</code><br />
 <code>01111000</code><br />
 <code>11011101</code> </p>
<p> Command <code>apgd -a 1 -M nc -n 3 -m 26 -e GHIJKLMNOPQRSTUVWXYZ</code> will generate a set of passwords that will look like this<br />
 <code>16A1653CD4DE5E7BD9584A3476</code><br />
 <code>C8F78E06944AFD57FB9CB882BC</code><br />
 <code>8C8DF37CD792D36D056BBD5002</code>
</dl>
</dl>
<h3>Password quality control options</h3>
<dl>
<dt><code>-k</code></p>
<dd>check every generated password using <code>cracklib</code>. To use this ability you must enable cracklib support during programm building.</p>
<dt><code>-r </code><i>dictfile</i></p>
<dd>check generated passwords for their appearance in <code>dictfile</code></p>
<dt><code>-b </code><i>filter_file</i></p>
<dd>check generated passwords for their appearance in <i>filter_file</i>. <i>filter_file</i> should be created with <code><a href="/docs/linux/man/1-apgbfm/">apgbfm</a></code>(1) utility.</p>
<dt><code>-p min_substr_len</code></p>
<dd>this option tells <code><a href="/docs/linux/man/1-apg/">apg</a></code>(1) to check every substring of the generated password for appearance in <i>filter_file</i>. If any of such substrings would be found in the <i>filter_file</i> then generated password would be rejected and <a href="/docs/linux/man/1-apg/">apg</a>(1) will generate another one. <code>min_substr_len</code> is specifies minimum substring length to check. This option is active only if <code>-b</code> option is defined.</dl>
<h3>Password output options</h3>
<dl>
<dt><code>-l</code></p>
<dd>spell genetated passwords. Useful when you want to read generated password by telephone.</p>
<dl>
<dd><code>WARNING:</code> Think twice before read your password by phone.</dl>
<dt><code>-t</code></p>
<dd>print pronunciation for generated pronounceable password</dl>
<h2>Default Options</h2>
<p><code>apgd -a 0 -M sncl -n 6 -x 10 -m 8</code> (new style)</p>
<h2>Exit Code</h2>
<p>On successful completion of its task, <code>apgd</code> will complete with exit code 0. An exit code of -1 indicates an error occurred. Textual errors are written to the <code>syslogd</code> (8).</p>
<h2>Diagnostics</h2>
<p>All textual info is written to the <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8).</p>
<h2>Files</h2>
<p><code>None.</code></p>
<h2>Bugs</h2>
<p><code>None.</code> If you&#8217;ve found one, please send bug description to the author.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-apg/">apg</a></code>(1), <code><a href="/docs/linux/man/1-apgbfm/">apgbfm</a></code>(1)</p>
<h2>Author</h2>
<p>Adel I. Mirzazhanov, &lt;a-del [at] iname.com&gt;<br />
 Project home page: <a rel="nofollow" href="http://www.adel.nursat.kz/apg/">http://www.adel.nursat.kz/apg/</a></p>
