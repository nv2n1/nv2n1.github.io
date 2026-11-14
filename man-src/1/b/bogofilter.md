---
title: "bogofilter(1)"
name: "bogofilter"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bogofilter/"
description: "bogofilter – fast Bayesian spam filter"
---

<h2 class="name">NAME</h2>
<p> bogofilter &#8211; fast Bayesian spam filter </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>bogofilter</code> [help options | classification options | registration options | parameter options | info options] [general options] [config file options]</dl>
<dd>where </p>
<p> <code>help options</code> are:</p>
<dl>
<dt> [-h] [&#8211;help] [-V] [-Q]</dl>
<p> <code>classification options</code></p>
<dd>are:</p>
<dl>
<dt> [-p] [-e] [-t] [-T] [-u] [-H] [-M] [-b] [-B&nbsp;<wbr><i>object &#8230;</i>] [-R] [general options] [parameter options] [config file options]</dl>
<p> <code>registration options</code></p>
<dd>are:</p>
<dl>
<dt> [-s | -n] [-S | -N] [general options]</dl>
<p> <code>general options</code></p>
<dd>are:</p>
<dl>
<dt> [-c&nbsp;<wbr><i>filename</i>] [-C] [-d&nbsp;<wbr><i>dir</i>] [-k&nbsp;<wbr><i>cachesize</i>] [-l] [-L&nbsp;<wbr><i>tag</i>] [-I&nbsp;<wbr><i>filename</i>] [-O&nbsp;<wbr><i>filename</i>]</dl>
<p> <code>parameter options</code></p>
<dd>are:</p>
<dl>
<dt> [-E&nbsp;<wbr><i>value</i><i>[,value]</i>] [-m&nbsp;<wbr><i>value</i><i>[,value]</i><i>[,value]</i>] [-o&nbsp;<wbr><i>value</i><i>[,value]</i>]</dl>
<p> <code>info options</code></p>
<dd>are:</p>
<dl>
<dt> [-v] [-y&nbsp;<wbr><i>date</i>] [-D] [-x&nbsp;<wbr><i>flags</i>]</dl>
<p> <code>config file options</code></p>
<dd>are:</p>
<dl>
<dt> [&#8211;<i>option=value</i>]</dl>
<dd>Note: Use <code>bogofilter &#8211;help</code> to display the complete list of options.</p>
<h2>DESCRIPTION</h2>
<p> Bogofilter is a Bayesian spam filter. In its normal mode of operation, it takes an email message or other text on standard input, does a statistical check against lists of &quot;good&quot; and &quot;bad&quot; words, and returns a status code indicating whether or not the message is spam. Bogofilter is designed with a fast algorithm, uses the Berkeley DB for fast startup and lookups, coded directly in C, and tuned for speed, so it can be used for production by sites that process a lot of mail.</p>
<h2>THEORY OF OPERATION</h2>
<p> Bogofilter treats its input as a bag of tokens. Each token is checked against a wordlist, which maintains counts of the numbers of times it has occurred in non-spam and spam mails. These numbers are used to compute an estimate of the probability that a message in which the token occurs is spam. Those are combined to indicate whether the message is spam or ham. </p>
<p> While this method sounds crude compared to the more usual pattern-matching approach, it turns out to be extremely effective. Paul Graham&#8217;s paper m[blue]<code>A Plan For Spam</code>m[]<font SIZE="-2">[1]</font> is recommended reading. </p>
<p> This program substantially improves on Paul&#8217;s proposal by doing smarter lexical analysis. Bogofilter does proper MIME decoding and a reasonable HTML parsing. Special kinds of tokens like hostnames and IP addresses are retained as recognition features rather than broken up. Various kinds of MTA cruft such as dates and message-IDs are ignored so as not to bloat the wordlist. Tokens found in various header fields are marked appropriately. </p>
<p> Another improvement is that this program offers Gary Robinson&#8217;s suggested modifications to the calculations (see the parameters robx and robs below). These modifications are described in Robinson&#8217;s paper m[blue]<code>Spam Detection</code>m[]<font SIZE="-2">[2]</font>. </p>
<p> Since then, Robinson (see his Linux Journal article m[blue]<code>A Statistical Approach to the Spam Problem</code>m[]<font SIZE="-2">[3]</font>) and others have realized that the calculation can be further optimized using Fisher&#8217;s method. m[blue]<code>Another improvement</code>m[]<font SIZE="-2">[4]</font> compensates for token redundancy by applying separate effective size factors (ESF) to spam and nonspam probability calculations. </p>
<p> In short, this is how it works: The estimates for the spam probabilities of the individual tokens are combined using the &quot;inverse chi-square function&quot;. Its value indicates how badly the null hypothesis that the message is just a random collection of independent words with probabilities given by our previous estimates fails. This function is very sensitive to small probabilities (hammish words), but not to high probabilities (spammish words); so the value only indicates strong hammish signs in a message. Now using inverse probabilities for the tokens, the same computation is done again, giving an indicator that a message looks strongly spammish. Finally, those two indicators are subtracted (and scaled into a 0-1-interval). This combined indicator (bogosity) is close to 0 if the signs for a hammish message are stronger than for a spammish message and close to 1 if the situation is the other way round. If signs for both are equally strong, the value will be near 0.5. Since those message don&#8217;t give a clear indication there is a tristate mode in bogofilter to mark those messages as unsure, while the clear messages are marked as spam or ham, respectively. In two-state mode, every message is marked as either spam or ham. </p>
<p> Various parameters influence these calculations, the most important are: </p>
<p> robx: the score given to a token which has not seen before. robx is the probability that the token is spammish. </p>
<p> robs: a weight on robx which moves the probability of a little seen token towards robx. </p>
<p> min-dev: a minimum distance from .5 for tokens to use in the calculation. Only tokens farther away from 0.5 than this value are used. </p>
<p> spam-cutoff: messages with scores greater than or equal to will be marked as spam. </p>
<p> ham-cutoff: If zero or spam-cutoff, all messages with values strictly below spam-cutoff are marked as ham, all others as spam (two-state). Else values less than or equal to ham-cutoff are marked as ham, messages with values strictly between ham-cutoff and spam-cutoff are marked as unsure; the rest as spam (tristate) </p>
<p> sp-esf: the effective size factor (ESF) for spam. </p>
<p> ns-esf: the ESF for nonspam. These ESF values default to 1.0, which is the same as not using ESF in the calculation. Values suitable to a user&#8217;s email population can be determined with the aid of the bogotune program.</p>
<h2>OPTIONS</h2>
<p> HELP OPTIONS </p>
<p> The <code>-h</code> option prints the help message and exits. </p>
<p> The <code>-V</code> option prints the version number and exits. </p>
<p> The <code>-Q</code> (query) option prints bogofilter&#8217;s configuration, i.e. registration parameters, parsing options, bogofilter directory, etc. </p>
<p> CLASSIFICATION OPTIONS </p>
<p> The <code>-p</code> (passthrough) option outputs the message with an X-Bogosity line at the end of the message header. This requires keeping the entire message in memory when it&#8217;s read from stdin (or from a pipe or socket). If the message is read from a file that can be rewound, bogofilter will read it a second time. </p>
<p> The <code>-e</code> (embed) option tells bogofilter to exit with code 0 if the message can be classified, i.e. if there is not an error. Normally bogofilter uses different codes for spam, ham, and unsure classifications, but this simplifies using bogofilter with procmail or maildrop. </p>
<p> The <code>-t</code> (terse) option tells bogofilter to print an abbreviated spamicity message containing 1 letter and the score. Spam is indicated with &quot;Y&quot;, ham by &quot;N&quot;, and unsure by &quot;U&quot;. Note: the formatting can be customized using the config file. </p>
<p> The <code>-T</code> provides an invariant terse mode for scripts to use. bogofilter will print an abbreviated spamicity message containing 1 letter and the score. Spam is indicated with &quot;S&quot;, ham by &quot;H&quot;, and unsure by &quot;U&quot;. </p>
<p> The <code>-TT</code> provides an invariant terse mode for scripts to use. Bogofilter prints only the score and displays it to 16 significant digits. </p>
<p> The <code>-u</code> option tells bogofilter to register the message&#8217;s text after classifying it as spam or non-spam. A spam message will be registered on the spamlist and a non-spam message on the goodlist. If the classification is &quot;unsure&quot;, the message will not be registered. Effectively this option runs bogofilter with the <code>-s</code> or <code>-n</code> flag, as appropriate. Caution is urged in the use of this capability, as any classification errors bogofilter may make will be preserved and will accumulate until manually corrected with the <code>-Sn</code> and <code>-Ns</code> option combinations. Note this option causes the database to be opened for write access, which can entail massive slowdowns through lock contention and synchronous I/O operations. </p>
<p> The <code>-H</code> option tells bogofilter to not tag tokens from the header. This option is for testing, you should not use it in normal operation. </p>
<p> The <code>-M</code> option tells bogofilter to process its input as a mbox formatted file. If the <code>-v</code> or <code>-t</code> option is also given, a spamicity line will be printed for each message. </p>
<p> The <code>-b</code> (streaming bulk mode) option tells bogofilter to classify multiple objects whose names are read from stdin. If the <code>-v</code> or <code>-t</code> option is also given, bogofilter will print a line giving file name and classification information for each file. This is an alternative to <code>-B</code> which lists objects on the command line. </p>
<p> An object in this context shall be a maildir (autodetected), or if it&#8217;s not a maildir, a single mail unless <code>-M</code> is given &#8211; in that case it&#8217;s processed as mbox. (The Content-Length: header is not taken into account currently.) </p>
<p> When reading mbox format, bogofilter relies on the empty line after a mail. If needed, <code>formail -es</code> will ensure this is the case. </p>
<p> The <code>-B </code><i>object &#8230;</i> (bulk mode) option tells bogofilter to classify multiple objects named on the command line. The objects may be filenames (for single messages), mailboxes (files with multiple messages), or directories (of maildir and MH format). If the <code>-v</code> or <code>-t</code> option is also given, bogofilter will print a line giving file name and classification information for each file. This is an alternative to <code>-b</code> which lists objects on stdin. </p>
<p> The <code>-R</code> option tells bogofilter to output an R data frame in text form on the standard output. See the section on integration with R, below, for further detail. </p>
<p> REGISTRATION OPTIONS </p>
<p> The <code>-s</code> option tells bogofilter to register the text presented as spam. The database is created if absent. </p>
<p> The <code>-n</code> option tells bogofilter to register the text presented as non-spam. </p>
<p> Bogofilter doesn&#8217;t detect if a message registered twice. If you do this by accident, the token counts will off by 1 from what you really want and the corresponding spam scores will be slightly off. Given a large number of tokens and messages in the wordlist, this doesn&#8217;t matter. The problem <i>can</i> be corrected by using the <code>-S</code> option or the <code>-N</code> option. </p>
<p> The <code>-S</code> option tells bogofilter to undo a prior registration of the same message as spam. If a message was incorrectly entered as spam by <code>-s</code> or <code>-u</code> and you want to remove it and enter it as non-spam, use <code>-Sn</code>. If <code>-S</code> is used for a message that wasn&#8217;t registered as spam, the counts will still be decremented. </p>
<p> The <code>-N</code> option tells bogofilter to undo a prior registration of the same message as non-spam. If a message was incorrectly entered as non-spam by <code>-n</code> or <code>-u</code> and you want to remove it and enter it as spam, then use <code>-Ns</code>. If <code>-N</code> is used for a message that wasn&#8217;t registered as non-spam, the counts will still be decremented. </p>
<p> GENERAL OPTIONS </p>
<p> The <code>-c </code><i>filename</i> option tells bogofilter to read the config file named. </p>
<p> The <code>-C</code> option prevents bogofilter from reading configuration files. </p>
<p> The <code>-d </code><i>dir</i> option allows you to set the directory for the database. See the ENVIRONMENT section for other directory setting options. </p>
<p> The <code>-k </code><i>cachesize</i> option sets the cache size for the BerkeleyDB subsystem, in units of 1 MiB (1,048,576 bytes). Properly sizing the cache improves bogofilter&#8217;s performance. The recommended size is one third of the size of the database file. You can run the bogotune script (in the tuning directory) to determine the recommended size. </p>
<p> The <code>-l</code> option writes an informational line to the system log each time bogofilter is run. The information logged depends on how bogofilter is run. </p>
<p> The <code>-L </code><i>tag</i> option configures a tag which can be included in the information being logged by the <code>-l</code> option, but it requires a custom format that includes the %l string for now. This option implies <code>-l</code>. </p>
<p> The <code>-I </code><i>filename</i> option tells bogofilter to read its input from the specified file, rather than from <code>stdin</code>. </p>
<p> The <code>-O </code><i>filename</i> option tells bogofilter where to write its output in passthrough mode. Note that this only works when -p is explicitly given. </p>
<p> PARAMETER OPTIONS </p>
<p> The <code>-E </code><i>value</i><i>[,value]</i> option allows setting the sp-esf value and the ns-esf value. With two values, both sp-esf and ns-esf are set. If only one value is given, parameters are set as described in the note below. </p>
<p> The <code>-m </code><i>value</i><i>[,value]</i><i>[,value]</i> option allows setting the min-dev value and, optionally, the robs and robx values. With three values, min-dev, robs, and robx are all set. If fewer values are given, parameters are set as described in the note below. </p>
<p> The <code>-o </code><i>value</i><i>[,value]</i> option allows setting the spam-cutoff ham-cutoff values. With two values, both spam-cutoff and ham-cutoff are set. If only one value is given, parameters are set as described in the note below. </p>
<p> Note: All of these options allow fewer values to be provided. Values can be skipped by using just the comma delimiter, in which case the corresponding parameter(s) won&#8217;t be changed. If only the first value is provided, then only the first parameter is set. Trailing values can be skipped, in which case the corresponding parameters won&#8217;t be changed. Within the parameter list, spaces are not allowed after commas. </p>
<p> INFO OPTIONS </p>
<p> The <code>-v</code> option produces a report to standard output on bogofilter&#8217;s analysis of the input. Each additional <code>v</code> will increase the verbosity of the output, up to a maximum of 4. With <code>-vv</code>, the report lists the tokens with highest deviation from a mean of 0.5 association with spam. </p>
<p> Option <code>-y date</code> can be used to override the current date when timestamping tokens. A value of zero (0) turns off timestamping. </p>
<p> The <code>-D</code> option redirects debug output to stdout. </p>
<p> The <code>-x </code><i>flags</i> option allows setting of debug flags for printing debug information. See header file debug.h for the list of usable flags. </p>
<p> CONFIG FILE OPTIONS </p>
<p> Using GNU longopt <code>&#8212;</code> syntax, a config file&#8217;s <i>name=value</i> statement becomes a command line&#8217;s <code>&#8212;</code><i>option=value</i>. Use command <code>bogofilter &#8211;help</code> for a list of options and see bogofilter.cf.example for more info on them. For example to change the X-Bogosity header to &quot;X-Spam-Header&quot;, use: </p>
<p> <i>&#8211;spam-header-name=X-Spam-Header</i></p>
<h2>ENVIRONMENT</h2>
<p> Bogofilter uses a database directory, which can be set in the config file. If not set there, bogofilter will use the value of <code>BOGOFILTER_DIR</code>. Both can be overridden by the <code>-d </code><i>dir</i> option. If none of that is available, bogofilter will use directory $HOME/.bogofilter.</p>
<h2>CONFIGURATION</h2>
<p> The bogofilter command line allows setting of many options that determine how bogofilter operates. File /etc/bogofilter.cf can be used to set additional parameters that affect its operation. File /etc/bogofilter.cf.example has samples of all of the parameters. Status and logging messages can be customized for each site.</p>
<h2>RETURN VALUES</h2>
<p> 0 for spam; 1 for non-spam; 2 for unsure ; 3 for I/O or other errors. </p>
<p> If both <code>-p</code> and <code>-e</code> are used, the return values are: 0 for spam or non-spam; 3 for I/O or other errors. </p>
<p> Error 3 usually means that the wordlist file bogofilter wants to read at startup is missing or the hard disk has filled up in <code>-p</code> mode.</p>
<h2>INTEGRATION WITH OTHER TOOLS</h2>
<p> Use with procmail </p>
<p> The following recipe (a) spam-bins anything that bogofilter rates as spam, (b) registers the words in messages rated as spam as such, and (c) registers the words in messages rated as non-spam as such. With this in place, it will normally only be necessary for the user to intervene (with <code>-Ns</code> or <code>-Sn</code>) when bogofilter miscategorizes something. </p>
<dl>
<dt>
<dd>
<pre><code>
#filter mail through bogofilter, tagging it as Ham, Spam, or Unsure,
#and updating the wordlist
:0fw
| bogofilter -u -e -p
#if bogofilter failed, return the mail to the queue;
#the MTA will retry to deliver it later
# 75 is the value for EX_TEMPFAIL in / usr / include / sysexits.h
:0e
{ EXITCODE=75 HOST }
#file the mail to spam - bogofilter if it's spam.
:0:
* ^X-Bogosity: Spam, tests=bogofilter
spam-bogofilter
#file the mail to unsure - bogofilter
#if it's neither ham nor spam.
:0:
* ^X-Bogosity: Unsure, tests=bogofilter
unsure-bogofilter
#With this recipe, you can train bogofilter starting with an empty
#wordlist.Be sure to check your unsure - folder regularly, take the
#messages out of it, classify them as ham(or spam), and use them to
#train bogofilter.
</code></pre>
</dl>
<p> The following procmail rule will take mail on stdin and save it to file spam if bogofilter thinks it&#8217;s spam: </p>
<dl>
<dt>
<dd>
<pre>
:0HB:
* ? bogofilter
spam
</pre>
</dl>
<p> and this similar rule will also register the tokens in the mail according to the bogofilter classification: </p>
<dl>
<dt>
<dd>
<pre>
:0HB:
* ? bogofilter -u
spam
</pre>
</dl>
<p> If bogofilter fails (returning 3) the message will be treated as non-spam. </p>
<p> This one is for maildrop, it automatically defers the mail and retries later when the xfilter command fails, use this in your ~/.mailfilter: </p>
<dl>
<dt>
<dd>
<pre>
xfilter &quot;bogofilter -u -e -p&quot;
if (/^X-Bogosity: Spam, tests=bogofilter/)
{
  to &quot;spam-bogofilter&quot;
}
</pre>
</dl>
<p> The following .muttrc lines will create mutt macros for dispatching mail to bogofilter. </p>
<dl>
<dt>
<dd>
<pre>
macro index d &quot;&lt;enter-command&gt;unset wait_key
\
&lt;pipe-entry&gt;bogofilter -n
\
&lt;enter-command&gt;set wait_key
\
&lt;delete-message&gt;&quot; &quot;delete message as non-spam&quot;
macro index d &quot;&lt;enter-command&gt;unset wait_key
\
&lt;pipe-entry&gt;bogofilter -s
\
&lt;enter-command&gt;set wait_key
\
&lt;delete-message&gt;&quot; &quot;delete message as spam&quot;
</pre>
</dl>
<p> Integration with Mail Transport Agent (MTA) </p>
<dl>
<dt>
<dd> 1. bogofilter can also be integrated into an MTA to filter all incoming mail. While the specific implementation is MTA dependent, the general steps are as follows:</dl>
<dl>
<dt>
<dd> 2. Install bogofilter on the mail server</dl>
<dl>
<dt>
<dd> 3. Prime the bogofilter databases with a spam and non-spam corpus. Since bogofilter will be serving a larger community, it is important to prime it with a representative set of messages.</dl>
<dl>
<dt>
<dd> 4. Set up the MTA to invoke bogofilter on each message. While this is an MTA specific step, you&#8217;ll probably need to use the <code>-p</code>, <code>-u</code>, and <code>-e</code> options.</dl>
<dl>
<dt>
<dd> 5. Set up a mechanism for users to register spam/non-spam messages, as well as to correct mis-classifications. The most generic solution is to set up alias email addresses to which users bounce messages.</dl>
<dl>
<dt>
<dd> 6. See the doc and contrib directories for more information.</dl>
<p> Use of R to verify bogofilter&#8217;s calculations </p>
<p> The -R option tells bogofilter to generate an R data frame. The data frame contains one row per token analyzed. Each such row contains the token, the sum of its database &quot;good&quot; and &quot;spam&quot; counts, the &quot;good&quot; count divided by the number of non-spam messages used to create the training database, the &quot;spam&quot; count divided by the spam message count, Robinson&#8217;s f(w) for the token, the natural logs of (1 &#8211; f(w)) and f(w), and an indicator character (+ if the token&#8217;s f(w) value exceeded the minimum deviation from 0.5, &#8211; if it didn&#8217;t). There is one additional row at the end of the table that contains a label in the token field, followed by the number of words actually used (the ones with + indicators), Robinson&#8217;s P, Q, S, s and x values and the minimum deviation. </p>
<p> The R data frame can be saved to a file and later read into an R session (see m[blue]<code>the R project website</code>m[]<font SIZE="-2">[5]</font> for information about the mathematics package R). Provided with the bogofilter distribution is a simple R script (file bogo.R) that can be used to verify bogofilter&#8217;s calculations. Instructions for its use are included in the script in the form of comments.</p>
<h2>LOG MESSAGES</h2>
<p> Bogofilter writes messages to the system log when the <code>-l</code> option is used. What is written depends on which other flags are used. </p>
<p> A classification run will generate (we are not showing the date and host part here): </p>
<dl>
<dt>
<dd>
bogofilter[1412] : X &#8211; Bogosity : Ham, spamicity = 0.000227 bogofilter[1415] : X &#8211; Bogosity : Spam, spamicity = 0.998918
</dl>
<p> Using <code>-u</code> to classify a message and update a wordlist will produce (one a single line): </p>
<dl>
<dt>
<dd>
<pre>
bogofilter[1426]: X-Bogosity: Spam, spamicity=0.998918,
  register -s, 329 words, 1 messages
    
</pre>
</dl>
<p> Registering words (<code>-l</code> and <code>-s</code>, <code>-n</code>, <code>-S</code>, or <code>-N</code>) will produce: </p>
<dl>
<dt>
<dd>
<pre>
bogofilter[1440]: register-n, 255 words, 1 messages
</pre>
</dl>
<p> A registration run (using <code>-s</code>, <code>-n</code>, <code>-N</code>, or <code>-S</code>) will generate messages like: </p>
<dl>
<dt>
<dd>
bogofilter[17330] : register &#8211; n, 574 words, 3 messages bogofilter[6244] : register &#8211; s, 1273 words, 4 messages
</dl>
<h2>FILES</h2>
<p> /etc/bogofilter.cf</p>
<dl>
<dt>
<dd> System configuration file.</dl>
<p> ~/.bogofilter.cf</p>
<dl>
<dt>
<dd> User configuration file.</dl>
<p> ~/.bogofilter/wordlist.db</p>
<dl>
<dt>
<dd> Combined list of good and spam tokens.</dl>
<h2>AUTHOR</h2>
<dl>
<dt>
<dd>
<pre><code>
Eric S.Raymond esr[at] thyrsus.com.David Relson relson[at] osagesoftware.com.Matthias Andree matthias.andree[at] gmx.de.Greg Louis glouis[at] dynamicro.on.ca.
</code></pre>
</dl>
<p> For updates, see the m[blue]<code>bogofilter project page</code>m[]<font SIZE="-2">[6]</font>.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-bogolexer/">bogolexer</a>(1), <a href="/docs/linux/man/1-bogotune/">bogotune</a>(1), <a href="/docs/linux/man/1-bogoupgrade/">bogoupgrade</a>(1), <a href="/docs/linux/man/1-bogoutil/">bogoutil</a>(1)</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> A Plan For Spam</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.paulgraham.com/spam.html">http://www.paulgraham.com/spam.html</a></dl>
<dt> 2.</p>
<dd> Spam Detection</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://radio-weblogs.com/0101454/stories/2002/09/16/spamDetection.html">http://radio-weblogs.com/0101454/stories/2002/09/16/spamDetection.html</a></dl>
<dt> 3.</p>
<dd> A Statistical Approach to the Spam Problem</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.linuxjournal.com/article/6467">http://www.linuxjournal.com/article/6467</a></dl>
<dt> 4.</p>
<dd> Another improvement</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.garyrobinson.net/2004/04/improved%5fchi.html">http://www.garyrobinson.net/2004/04/improved%5fchi.html</a></dl>
<dt> 5.</p>
<dd> the R project website</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://cran.r-project.org/">http://cran.r-project.org/</a></dl>
<dt> 6.</p>
<dd> bogofilter project page</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://bogofilter.sourceforge.net/">http://bogofilter.sourceforge.net/</a></dl>
</dl>
<h2>Index</h2>
