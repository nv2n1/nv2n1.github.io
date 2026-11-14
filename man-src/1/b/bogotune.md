---
title: "bogotune(1)"
name: "bogotune"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bogotune/"
description: "bogotune – find optimum parameter settings for bogofilter"
---

<h2 class="name">NAME</h2>
<p> bogotune &#8211; find optimum parameter settings for bogofilter </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>bogotune</code> [-v] [-c&nbsp;<wbr><i>config</i>] [-C] [-d&nbsp;<wbr><i>dir</i>] [-D] [-r&nbsp;<wbr><i>value</i>] [-T&nbsp;<wbr><i>value</i>] -n&nbsp;<wbr><i>okfile</i>&nbsp;<wbr>[[-n]&nbsp;<wbr><i>okfile</i>&nbsp;<wbr>[&#8230;]] -s&nbsp;<wbr><i>spamfile</i>&nbsp;<wbr>[[-s]&nbsp;<wbr><i>spamfile</i>&nbsp;<wbr>[&#8230;]] [-M&nbsp;<wbr><i>file</i>]</p>
<dt> <code>bogotune</code> [-h]</dl>
<h2>DESCRIPTION</h2>
<dd>Bogotune tries to find optimum parameter settings for bogofilter. It needs at least one set each of spam and non-spam messages. The production wordlist is normally used, but it can be directed to read a different wordlist, or to build its own from half the supplied messages. </p>
<p> In order to produce useful results, bogotune has minimum message count requirements. The wordlist it uses must have at least 2,000 spam and 2,000 non-spam in it and the message files must contain at least 500 spam and 500 non-spam messages. Also, the ratio of spam to non-spam should be in the range 0.2 to 5. If you direct bogotune to build its own wordlist, it will use the half the input or 2000 messages (whichever is larger) for the wordlist. </p>
<p> Message files may be in mbox, maildir, or MH folder or any combination. Msg-count files can also be used, but not mixed with other formats.</p>
<h2>OPTIONS</h2>
<p> The <code>-h</code> option prints the help message and exits. </p>
<p> The <code>-v</code> option increases the verbosity level. Level 1 displays the scan output in detail instead of using a progress meter. </p>
<p> The <code>-c</code> <i>filename</i> option tells bogofilter to read the config file named. </p>
<p> The <code>-C</code> option prevents bogotune from reading a configuration file. </p>
<p> The <code>-d</code> <i>dir</i> option specifies the directory for the database. See the ENVIRONMENT section for other directory setting options. </p>
<p> The <code>-D</code> option tells bogotune to build a wordlist in memory using the input messages. The messages are read and divided into two groups. The first group is used to build a wordlist (in ram) and the second is used for tuning. To meet the minimum requirements of 2000 messages in the wordlist and 500 messages for testing, when <code>-D</code> is used, there must be 2500 non-spam and 2500 spam in the input files. If there are enough messages (more than 4000), they will be split evenly between wordlist and testing. Otherwise, they will be split proportionately. </p>
<p> The <code>-n</code> option tells bogotune that the following argument is a file (or folder) containing non-spam. Since version 1.0.3, multiple arguments to the <code>-n</code> option can be given. All non-option arguments until the next <code>-s</code> option will be treated as though they had been preceded by <code>-n</code> </p>
<p> The <code>-s</code> option tells bogotune that the following argument is a file (or folder) containing spam. It can be repeated as often as necessary. Since version 1.0.3, multiple arguments to the <code>-s</code> can be given. All non-option arguments until the next <code>-n</code> option will be treated as though they had been preceded by <code>-s</code>. </p>
<p> The <code>-r </code><i>value</i> option tells bogotune to use the following parameter as the robx value. </p>
<p> The <code>-T </code><i>value</i> option tells bogotune to use the following parameter as fp target value. </p>
<p> The <code>-M </code><i>file</i> option tells bogotune to convert the file to message count format. This format provides a sorted list of each message&#8217;s unique tokens, along with their ham and spam counts. Sorting hides the sense of the messages quite effectively, thus protecting privacy. The message-count format allows bogotune and bogofilter to score messages quickly without needing the original token database.</p>
<h2>ENVIRONMENT</h2>
<p> Bogofilter uses a database directory, which can be set in the config file. If not set there, bogofilter will use the value of <code>BOGOFILTER_DIR</code>. Both can be overridden by the <code>-d</code><i>dir</i> option. If none of that is available, bogofilter will use directory $HOME/.bogofilter.</p>
<h2>BUGS</h2>
<p> Bogotune is not particularly robust when presented with garbage input.</p>
<h2>AUTHOR</h2>
<p> The bogofilter developer team. </p>
<p> For updates, see m[blue]<code>the bogofilter project page</code>m[]<font SIZE="-2">[1]</font>.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-bogofilter/">bogofilter</a>(1), <a href="/docs/linux/man/1-bogolexer/">bogolexer</a>(1), <a href="/docs/linux/man/1-bogoupgrade/">bogoupgrade</a>(1), <a href="/docs/linux/man/1-bogoutil/">bogoutil</a>(1)</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> the bogofilter project page</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://bogofilter.sourceforge.net/">http://bogofilter.sourceforge.net/</a></dl>
</dl>
<h2>Index</h2>
