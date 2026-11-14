---
title: "hashdeep(1)"
name: "hashdeep"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hashdeep/"
description: "hashdeep – Compute, compare, or audit multiple message digests"
---

<h2 class="name">NAME</h2>
<p> hashdeep &#8211; Compute, compare, or audit multiple message digests</p>
<h2>SYNOPSIS</h2>
<p> <code>hashdeep </code> -V | -h<br />
 <code>hashdeep</code> [-c &lt;alg1&gt;[,&lt;alg2&gt;]] [-k &lt;file&gt;] [-i &lt;size&gt;] [-f &lt;file&gt;] [-o &lt;fbcplsde&gt;] [-amxwMXreEspblvv] [-F&lt;bum&gt;] [-j &lt;num&gt;] [<code>FILES</code>] </p>
<h2>DESCRIPTION</h2>
<p> Computes multiple hashes, or message digests, for any number of files while optionally recursively digging through the directory structure. By default the program computes MD5 and SHA-256 hashes, equivalent to -c md5,sha256. Can also take a list of known hashes and display the filenames of input files whose hashes either do or do not match any of the known hashes. Can also use a list of known hashes to audit a set of FILES. Errors are reported to standard error. If no FILES are specified, reads from standard input. </p>
<dl>
<dt><code>-c &lt;alg1&gt;[,&lt;alg2&gt;&#8230;]</code></p>
<dd> Computation mode. Compute hashes of FILES using the algorithms specified. Legal values are md5, sha1, sha256, tiger, and whirlpool. </p>
<dt><code>-k </code></p>
<dd> Load a file of known hashes. This flag is required when using any of the matching or audit modes (i.e. -m, -x, -M, -X, or -a) This flag may be used more than once to add multiple sets of known hashes. </p>
<p> Loading sets with different hash algorithms can sometimes generate spurrious hash collisions. For example, let&#8217;s say we have two hash sets, A and B, which have some overlapping files. For example, the file /usr/bin/bad is in both sets. In A we&#8217;ve recorded the MD5 and SHA-256. In B we&#8217;ve recorded the MD5, SHA-1, and SHA-256. Because these two records are different, they will both be loaded. When the program computes all three hashes and compares them to the set of knowns, we will get an exact match from the record in B and a collision from the record in A. </p>
<dt><code>-a </code></p>
<dd> Audit mode. Each input file is compared against the set of knowns. An audit is said to pass if each input file is matched against exactly one file in set of knowns. Any collisions, new files, or missing files will make the audit fail. Using this flag alone produces a message, either &quot;Audit passed&quot; or &quot;Audit Failed&quot;. Use the verbose modes, -v, for more details. Using -v prints the number of files in each category. Using -v a second time prints any discrepancies. Using -v a third time prints the results for every file examined and every known file.<br />
 Due to limitations in the program, any filenames with Unicode characters will appear to have moved during an audit. See the section &quot;UNICODE SUPPORT&quot; below. </p>
<dt><code>-m </code></p>
<dd> Positive matching, requires at least one use of the -k flag. The input files are examined one at a time, and only those files that match the list of known hashes are output. The only acceptable format for known hashes is the output of previous hashdeep runs.<br />
 If standard input is used with the -m flag, displays &quot;stdin&quot; if the input matches one of the hashes in the list of known hashes. If the hash does not match, the program displays no output.<br />
 This flag may not be used in conjunction with the -x, -X, or -a flags. See the section &quot;UNICODE SUPPORT&quot; below. </p>
<dt><code>-x </code></p>
<dd> Negative matching. Same as the -m flag above, but does negative matching. That is, only those files NOT in the list of known hashes are displayed.<br />
 This flag may not be used in conjunction with the -m, -M, or -a flags. See the section &quot;UNICODE SUPPORT&quot; below. </p>
<dt><code>-f</code> &lt;file&gt;</p>
<dd> Takes a list of files to be hashed from the specified file. Each line is assumed to be a filename. This flag can only be used once per invocation. If it&#8217;s used a second time, the second instance will clobber the first.<br />
 Note that you can still use other flags, such as the -m or -x modes, and submit additional FILES on the command line. </p>
<dt><code>-w </code></p>
<dd> When used with positive matching modes (-m,-M) displays the filename of the known hash that matched the input file. See the section &quot;UNICODE SUPPORT&quot; below. </p>
<dt><code>-M</code> and <code>-X</code></p>
<dd> Same as -m and -x above, but displays the hash for each file that does (or does not) match the list of known hashes. </p>
<dt><code>-r</code></p>
<dd> Enables recursive mode. All subdirectories are traversed. Please note that recursive mode cannot be used to examine all files of a given file extension. For example, calling hashdeep -r *.txt will examine all files in <i>directories</i> that end in .txt. </p>
<dt><code>-e</code></p>
<dd> Displays a progress indicator and estimate of time remaining for each file being processed. Time estimates for files larger than 4GB are not available on Windows. This mode may not be used with th -p mode. </p>
<dt><code>-E</code></p>
<dd> When in audit mode, performs case insensitive matching of filenames. For example, ooar will match to \Foo\BAR. This can be important on Windows systems, where filenames are case insensitive. </p>
<dt><code>-i &lt;size&gt; </code></p>
<dd> Size threshold mode. Only hash files smaller than the given the threshold. Sizes may be specified using IEC multipliers b,k,m,g,t,p, and e. </p>
<dt><code>-o</code> &lt;bcpflsd&gt;</p>
<dd> Enables expert mode. Allows the user specify which (and only which) types of files are processed. Directory processing is still controlled with the -r flag. The expert mode options allowed are:<br />
 f &#8211; Regular files<br />
 b &#8211; Block Devices<br />
 c &#8211; Character Devices<br />
 p &#8211; Named Pipes<br />
 l &#8211; Symbolic Links<br />
 s &#8211; Sockets<br />
 d &#8211; Solaris Doors<br />
 e &#8211; Windows PE executables </p>
<dt><code>-s</code></p>
<dd> Enables silent mode. All error messages are supressed. </p>
<dt><code>-p</code></p>
<dd> Piecewise mode. Breaks files into chunks before hashing. Chunks may be specified using IEC multipliers b,k,m,g,t,p, and e. (Never let it be said that the author didn’t plan ahead.) </p>
<dt><code>-b</code></p>
<dd> Enables bare mode. Strips any leading directory information from displayed filenames. This flag may not be used in conjunction with the -l flag. </p>
<dt><code>-l</code></p>
<dd> Enables relative file paths. Instead of printing the absolute path for each file, displays the relative file path as indicated on the command line. This flag may not be used in conjunction with the -b flag. </p>
<dt><code>-v</code></p>
<dd> Enables verbose mode. Use again to make the program more verbose. This mostly changes the behvaior of the audit mode, -a. </p>
<dt><code>-jnn</code></p>
<dd> Controls multi-threading. By default the program will create one producer thread to scan the file system and one hashing thread per CPU core. Multi-threading causes output filenames to be in non-deterministic order, as files that take longer to hash will be delayed while they are hashed. If a deterministic order is required, specify <code>-j0</code> to disable multi-threading </p>
<dt><code>-d</code></p>
<dd> Output in Digital Forensics XML (DFXML) format. </p>
<dt><code>-u</code></p>
<dd> Quote Unicode output. For example, the snowman is shown as <code>U+C426</code>. </p>
<dt><code>-F&lt;bum&gt;</code></p>
<dd> Specifies the input mode that is used to read files. The default is <code>-Fb</code> (buffered I/O) which reads files with fopen(). Specifying <code>-Fu</code> will use unbuffered I/O and read the file with open(). Specifying <code>-Fm</code> will use memory-mapped I/O which will be faster on some platforms, but which (currently) will not work with files that produce I/O errors. </p>
<dt><code>-h</code></p>
<dd> Show a help screen and exit. </p>
<dt><code>-V</code></p>
<dd> Show the version number and exit. </p>
</dl>
<h2>UNICODE SUPPORT</h2>
<p> As of version 3.0 the program supports Unicode characters in filenames on Microsoft Windows systems for filenames specified on the command line with globbing (e.g. *), for files specified with the <code>-f</code> of files to hash, and for files read from directories using the <code>-r</code> option. </p>
<p> By default all program input and output should be in UTF-8. The program automatically converts this to UTF-16 for opening files). </p>
<p> On Unix/Linux/MacOS, you should use a terminal emulator that supports UTF-8 and UTF-8 characters in filenames will be properly displayed. </p>
<p> On Windows, the programs do not display Unicode characters on the console. You must either redirect output to a file and open the file with Wordpad (which can display Unicode), or you must specify the <code>-u</code> option to quote Unicode using standard <code>U+XXXX</code> notation. </p>
<p> Currently the file name of a file containing known hashes may not be specified as a unicode filename, but you can specify the name using tab completition or an asterisk (e.g. md5deep -m *.txt where there is only one file with a .txt extension). </p>
<h2>RETURN VALUE</h2>
<p> Returns a bit-wise value based on the success of the operation and the status of any matching operations. </p>
<dl>
<dt>0</p>
<dd> Success. Note that the program considers itself successful even when it encounters read errors, permission denied errors, or finds directories when not in recursive mode.</p>
<dt>1</p>
<dd> Unused hashes. Under any of the matching modes, returns this value if one or more of the known hashes was not matched by any of the input files.</p>
<dt>2</p>
<dd> Unmatched inputs. Under any of the matching modes, returns this value if one or more of the input values did not match any of the known hashes.</p>
<dt>64</p>
<dd> User error, such as trying to do both positive and negative matching at the same time.</p>
<dt>128</p>
<dd> Internal error, such as memory corruption or uncaught cycle. All internal errors should be reported to the developer! See the section &quot;Reporting Bugs&quot; below. </p>
</dl>
<h2>AUTHOR</h2>
<p> hashdeep was written by Jesse Kornblum, research [at] jessekornblum.com, and Simson Garfinkel. </p>
<h2>KNOWN ISSUES</h2>
<p> Using the -r flag cannot be used to recursively process all files of a given extension in a directory. This is a feature, not a bug. If you need to do this, use the <code><a href="/docs/linux/man/1-find/">find</a></code>(1) command. </p>
<p> The program will fail if you attempt to compare 2^64 or more input files against a set of known files. </p>
<h2>REPORTING BUGS</h2>
<p> We take all bug reports <i>very</i> seriously. Any bug that jeopardizes the forensic integrity of this program could have serious consequences on people&#8217;s lives. When submitting a bug report, please include a description of the problem, how you found it, and your contact information. </p>
<p> Send bug reports to the author at the address above. </p>
<h2>COPYRIGHT</h2>
<p> This program is a work of the US Government. In accordance with 17 USC 105, copyright protection is not available for any work of the US Government. This program is PUBLIC DOMAIN. Portions of this program contain code that is licensed under the terms of the General Public License (GPL). Those portions retain their original copyright and license. See the file COPYING for more details. </p>
<p> There is NO warranty for this program; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> More information and installation instructions can be found in the README file. Current versions of both documents can be found on the project homepage: <a rel="nofollow" href="http://md5deep.sourceforge.net/">http://md5deep.sourceforge.net/</a> </p>
<p> The MD5 specification, RFC 1321, is available at<br />
 <a rel="nofollow" href="http://www.ietf.org/rfc/rfc1321.txt">http://www.ietf.org/rfc/rfc1321.txt</a> </p>
<p> The SHA-1 specification, RFC 3174, is available at<br />
 <a rel="nofollow" href="http://www.faqs.org/rfcs/rfc3174.html">http://www.faqs.org/rfcs/rfc3174.html</a> </p>
<p> The SHA-256 specification, FIPS 180-2, is available at<br />
 <a rel="nofollow" href="http://csrc.nist.gov/publications/fips/fips180-2/fips180-2.pdf">http://csrc.nist.gov/publications/fips/fips180-2/fips180-2.pdf</a> </p>
<p> The Tiger specification is available at<br />
 <a rel="nofollow" href="http://www.cs.technion.ac.il/~biham/Reports/Tiger/">http://www.cs.technion.ac.il/~biham/Reports/Tiger/</a> </p>
<p> The Whirlpool specification is available at<br />
 <a rel="nofollow" href="http://planeta.terra.com.br/informatica/paulobarreto/WhirlpoolPage.html">http://planeta.terra.com.br/informatica/paulobarreto/WhirlpoolPage.html</a> </p>
<h2>Index</h2>
