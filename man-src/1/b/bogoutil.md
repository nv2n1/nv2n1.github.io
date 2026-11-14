---
title: "bogoutil(1)"
name: "bogoutil"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bogoutil/"
description: "bogoutil – Dumps, loads, and maintains bogofilter database files"
---

<h2 class="name">NAME</h2>
<p> bogoutil &#8211; Dumps, loads, and maintains bogofilter database files </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>bogoutil</code> {-h | -V}</p>
<dt> <code>bogoutil</code> [options] {-d&nbsp;<wbr><i>file</i> | -H&nbsp;<wbr><i>file</i> | -l&nbsp;<wbr><i>file</i> | -m&nbsp;<wbr><i>file</i> | -w&nbsp;<wbr><i>file</i> | -p&nbsp;<wbr><i>file</i>}</p>
<dt> <code>bogoutil</code> {-r&nbsp;<wbr><i>file</i> | -R&nbsp;<wbr><i>file</i>}</p>
<dt> <code>bogoutil</code> {&#8211;db-print-leafpage-count&nbsp;<wbr><i>file</i> | &#8211;db-print-pagesize&nbsp;<wbr><i>file</i> | &#8211;db-verify&nbsp;<wbr><i>file</i> | &#8211;db-checkpoint&nbsp;<wbr><i>directory</i>&nbsp;<wbr>[flag&#8230;] | &#8211;db-list-logfiles&nbsp;<wbr><i>directory</i> | &#8211;db-prune&nbsp;<wbr><i>directory</i> | &#8211;db-recover&nbsp;<wbr><i>directory</i> | &#8211;db-recover-harder&nbsp;<wbr><i>directory</i> | &#8211;db-remove-environment&nbsp;<wbr><i>directory</i>}</dl>
<dd>where <code>options</code> is</p>
<dl>
<dt> <code>bogoutil</code> [-v] [-n] [-C] [-D] [-a&nbsp;<wbr><i>age</i>] [-c&nbsp;<wbr><i>count</i>] [-s&nbsp;<wbr><i>min,max</i>] [-y&nbsp;<wbr><i>date</i>] [-I&nbsp;<wbr><i>file</i>] [-O&nbsp;<wbr><i>file</i>] [-x&nbsp;<wbr><i>flags</i>] [&#8211;config-file&nbsp;<wbr><i>file</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>Bogoutil is part of the bogofilter Bayesian spam filter package. </p>
<p> It is used to dump and load bogofilter&#8217;s Berkeley DB databases to and from text files, perform database maintenance functions, and to display the values for specific words.</p>
<h2>OPTIONS</h2>
<p> The <code>-d </code><i>file</i> option tells bogoutil to print the contents of the database file to <code>stdout</code>. </p>
<p> The <code>-H </code><i>file</i> option tells bogoutil to print a histogram of the database file to <code>stdout</code>. The output is similar to bogofilter -vv. Finally, hapaxes (tokens which were only seen once) and pure tokens (tokens which were encountered only in ham or only in spam) are counted. </p>
<p> The <code>-l </code><i>file</i> option tells bogoutil to load the data from <code>stdin</code> into the database file. If the database file exists, <code>stdin</code> data is merged into the database file, with counts added up. </p>
<p> The <code>-m</code> option tells bogoutil to perform maintenance functions on the specified database, i.e. discard tokens that are older than desired, have counts that are too small, or sizes (lengths) that are too long or too short. </p>
<p> The <code>-w </code><i>file</i> option tells bogoutil to display token information from the database file. The option takes an argument, which is either the name of the wordlist (usually wordlist.db) or the name of the directory containing it. Tokens can be listed on the command line or piped to bogoutil. When there are extra arguments on the command line, bogoutil will use them as the tokens to lookup. If there are no extra arguments, bogoutil will read tokens from <code>stdin</code>. </p>
<p> The <code>-p </code><i>file</i> option tells bogoutil to display the database information for one or more tokens. The display includes a probability column with the token&#8217;s spam score (computed using bogofilter&#8217;s default values). Option <code>-p</code> takes the same arguments as option <code>-w</code> . </p>
<p> The <code>-r </code><i>file</i> option tells bogoutil to recalculate the ROBX value and print it as a six-digit fraction. </p>
<p> The <code>-R </code><i>file</i> option does the same as <code>-r</code>, but saves the result in the training database without printing it. </p>
<p> The <code>-I </code><i>file</i> option tells bogoutil to read its input from <i>file</i> rather than stdin. </p>
<p> The <code>-O </code><i>file</i> option tells bogoutil to write its output to <i>file</i> rather than stdout. </p>
<p> The <code>-v</code> option produces verbose output on <code>stderr</code>. This option is primarily useful for debugging. </p>
<p> The <code>-C</code> inhibits reading configuration files and lets bogoutil go with the defaults. </p>
<p> The <code>&#8211;config-file </code><i>file</i> option tells bogoutil to read <i>file</i> instead of the standard configuration file. </p>
<p> The <code>-D</code> redirects debug output to stdout (it usually goes to stderr). </p>
<p> The <code>-x </code><i>flags</i> option sets debugging flags. </p>
<p> Option <code>-n</code> stands for &quot;replace non-ascii characters&quot;. It will replace characters with the high bit (0x80) by question marks. This can be useful if a word list has lots of unreadable tokens, for example from Asian spam. The &quot;bad&quot; characters will be converted to question marks and matching tokens will be combined when used with <code>-m</code> or <code>-l</code>, but not with <code>-d</code>. </p>
<p> Option <code>-a age</code> indicates an acceptable token age, with older ones being discarded. The age can be a date (in form YYYYMMMDD) or a day count, i.e. discard tokens older than <code>age</code> days. </p>
<p> Option <code>-c value</code> indicates that tokens with counts less than or equal to <code>value</code> are to be discarded. </p>
<p> Option <code>-s min,max</code> is used to discard tokens based on their size, i.e. length. All tokens shorter than <code>min</code> or longer than <code>max</code> will be discarded. </p>
<p> Option <code>-y date</code> is specifies the date to give to tokens that don&#8217;t have dates. The format is YYYYMMDD. </p>
<p> The <code>-h</code> option prints the help message and exits. </p>
<p> The <code>-V</code> option prints the version number and exits.</p>
<h2>ENVIRONMENT MAINTENANCE</h2>
<p> The <code>&#8211;db-checkpoint </code><i>dir</i> option causes bogoutil to flush the buffer caches and checkpoint the database environment. </p>
<p> The <code>&#8211;db-list-logfiles </code><i>dir</i> option causes bogoutil to list the log files in the environment. Zero or more keywords can be added or combined (separated by whitespace) to modify the behavior of this mode. The default behavior is to list only inactive log files with relative paths. You can add <code>all</code> to list all log files (inactive and active). You can add <code>absolute</code> to switch the listing to absolute paths. </p>
<p> The <code>&#8211;db-prune </code><i>dir</i> option causes bogoutil to checkpoint the database environment and remove inactive log files. </p>
<p> The <code>&#8211;db-recover </code><i>dir</i> option runs a regular database recovery in the specified database directory. If that fails, it will retry with a (usually slower) catastrophic database recovery. If that fails, too, your database cannot be repaired and must be rebuilt from scratch. This is only supported when compiled with Berkeley DB support with transactions enabled. Trying recovery with QDBM or SQLite3 support will result in an error. </p>
<p> The <code>&#8211;db-recover-harder </code><i>dir</i> option runs a catastrophic data base recovery in the specified database directory. If that fails, your database cannot be repaired and must be rebuilt from scratch. This is only supported when compiled with Berkeley DB support with transactions enabled. Trying recovery with QDBM or SQLite3 support will result in an error. </p>
<p> The <code>&#8211;db-remove-environment </code><i>directory</i> option has no short option equivalent. It runs recovery in the given directory and then removes the database environment. Use this <i>before</i> upgrading to a new Berkeley DB version if the new version to be installed requires a log file format update. </p>
<p> The <code>&#8211;db-print-leafpage-count </code><i>file</i> option prints the number of leaf pages in the database file <i>file</i> as a decimal number, or UNKNOWN if the database does not support querying this figure. </p>
<p> The <code>&#8211;db-print-pagesize </code><i>file</i> option prints the size of a database page in <i>file</i> as a decimal number, or UNKNOWN for databases with variable page size or databases that do not allow a query of the database page size. </p>
<p> The <code>&#8211;db-verify </code><i>file</i> option requests that bogofilter verifies the database file. It prints only errors, unless in verbose mode.</p>
<h2>DATA FORMAT</h2>
<p> Bogoutil reads and writes text files where each nonblank line consists of a word, any amount of horizontal whitespace, a numeric word count, more whitespace, and (optionally) a date in form YYYYMMDD. Blank lines are skipped.</p>
<h2>RETURN VALUES</h2>
<p> 0 for successful operation. 1 for most errors. 3 for I/O or other errors. Error 3 usually means that something is seriously wrong with the database files.</p>
<h2>AUTHOR</h2>
<p> Gyepi Sam gyepi [at] praxis-sw.com. </p>
<p> Matthias Andree matthias.andree [at] gmx.de. </p>
<p> David Relson relson [at] osagesoftware.com. </p>
<p> For updates, see m[blue]<code>the bogofilter project page</code>m[]<font SIZE="-2">[1]</font>.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-bogofilter/">bogofilter</a>(1), <a href="/docs/linux/man/1-bogolexer/">bogolexer</a>(1), <a href="/docs/linux/man/1-bogotune/">bogotune</a>(1), <a href="/docs/linux/man/1-bogoupgrade/">bogoupgrade</a>(1)</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> the bogofilter project page</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://bogofilter.sourceforge.net/">http://bogofilter.sourceforge.net/</a></dl>
</dl>
<h2>Index</h2>
