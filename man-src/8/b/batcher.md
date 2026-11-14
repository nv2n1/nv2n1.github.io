---
title: "batcher(8)"
name: "batcher"
section: "8"
letter: "b"
url: "/docs/linux/man/8-batcher/"
description: "batcher – Article batching for InterNetNews"
---

<p>batcher &#8211; Article batching for InterNetNews</p>
<h2>Synopsis</h2>
<p><code>batcher</code> [<code>-rv</code>] [<code>-a</code> <i>articles</i>] [<code>-A</code> <i>total-articles</i>] [<code>-b</code> <i>size</i>] [<code>-B</code> <i>total-size</i>] [<code>-i</code> <i>string</i>] [<code>-N</code> <i>batches</i>] [<code>-p</code> <i>process</i>] [<code>-s</code> <i>separator</i>] <i>host</i> [<i>input</i>]</p>
<h2>Description</h2>
<p><code>batcher</code> reads a list of files and prepares news batches for the specified host. It is generally used to prepare <font SIZE="-1">UUCP</font> feeds, but the resulting batches can be used by any application that uses <i><a href="/docs/linux/man/8-rnews/">rnews</a></i>(8) to inject the articles. It is normally invoked by a script run out of cron that uses <code>shlock</code> to lock the host, followed by <code>ctlinnd</code> to flush the batch file. See <i><a href="/docs/linux/man/8-send-uucp/">send-uucp</a></i>(8) for a front-end for <code>batcher</code>. </p>
<p> <code>batcher</code> reads the file <i>input</i>, or standard input if no file is given. If <i>input</i> is a relative file name, it is assumed to be in <i>pathoutgoing</i> as set in <i>inn.conf</i>. Blank lines and lines starting with a number sign (<tt>&quot;#&quot;</tt>) are ignored. All other lines in the input should consist of one or two fields separated by a single space. The first field is the storage <font SIZE="-1">API</font> token of an article. The second field, if present, specifies the size of the article in bytes. </p>
<p> By default, batches are written to standard output (which isn&#8217;t very useful if more than one batch is output), but see the <code>-p</code> option.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code> <i>articles</i></p>
<dd>This flag limits the number of articles included in each batch. The default is no limit. A new batch will be started when either the total bytes or the number of articles written exceeds the specified limits.</p>
<dt><code>-A</code> <i>total-articles</i></p>
<dd>Limits the total number of articles written for all batches. As soon as the total number of articles written to batches reaches or exceeds <i>total-articles</i>, all additional articles in the input will be deferred. The default is no limit.</p>
<dt><code>-b</code> <i>size</i></p>
<dd>This flag sets the size limit for each batch; as soon as at least this much data has been written out, a new batch will be started. The default size is 60&nbsp;<wbr><font SIZE="-1">KB</font>. Using <tt>&quot;-b 0&quot;</tt> will allow unlimited batch sizes.</p>
<dt><code>-B</code> <i>total-size</i></p>
<dd>Limits the total number of bytes written for all batches. As soon as the total bytes written to batches reaches or exceeds <i>total-size</i>, all additional articles in the input will be deferred. The default is no limit.</p>
<dt><code>-i</code> <i>string</i></p>
<dd>A batch starts with an identifying line to specify the unpacking method to be used on the receiving end. When this flag is used, <i>string</i>, followed by a newline, will be output at the start of each batch. The default is to have no initial string (under the assumption that either the processor specified with the <code>-p</code> flag or some other later process will add the appropriate line).</p>
<dt><code>-N</code> <i>batches</i></p>
<dd>Limits the total number of batches written. As soon as the number of batches written reaches or exceeds <i>batches</i>, all additional articles in the input will be deferred. The default is no limit.</p>
<dt><code>-p</code> <i>process</i></p>
<dd>By default, batches are written to standard output, which is not useful when more than one output batch is created. If this option is given, each batch will instead be fed via a pipe to the shell command <i>process</i>. The <i>process</i> argument must be an <i><a href="/docs/linux/man/3-sprintf/">sprintf</a></i>(3) format string, which may have a single <tt>%s</tt> parameter that will be replaced with the host name. </p>
<p> A common value is: </p>
<pre> ( echo '#! gunbatch' ; exec gzip -c ) | uux - -r -z %s!rnews</pre>
<p>which generates gzip-compressed batches and feeds them to <code>uux</code>.</p>
<dt><code>-r</code></p>
<dd>By default, <code>batcher</code> reports errors to <i>pathlog</i>/errlog. To suppress this redirection and report errors to standard error, use the <code>-r</code> flag.</p>
<dt><code>-s</code> <i>separator</i></p>
<dd>Each article in a batch starts with a separator line that indicates the size of the article. <i>separator</i> must be an <i><a href="/docs/linux/man/3-sprintf/">sprintf</a></i>(3) string, which may have a single <tt>%ld</tt> in the string that will be replaced with the size of the article. If the separator is not empty, a newline will also be appended to it when it is added to the beginning of each article. </p>
<p> The default separator is: </p>
<pre> #! rnews %ld</pre>
<p>and this should rarely be changed.</p>
<dt><code>-v</code></p>
<dd>Upon exit, <code>batcher</code> reports statistics via syslog. With this flag, the statistics will also be printed to standard output.</dl>
<h2>Exit Status</h2>
<p>If the input is exhausted and all batches are created successfully, <code>batcher</code> will exit with a zero status. </p>
<p> If any of the limits specified with <code>-A</code>, <code>-B</code>, or <code>-N</code> flags are reached, or if there is an error in writing a batch, <code>batcher</code> will try to spool the remaining input by copying it to a file as follows:</p>
<dl>
<dt>&bull;</p>
<dd>If there was no input filename, the remaining input will be copied to <i>pathoutgoing</i>/<i>host</i>.</p>
<dt>&bull;</p>
<dd>If an input filename was given, the remaining input will be copied to a temporary file named by appending <tt>&quot;.bch&quot;</tt> to the end of <i>input</i> (and qualified by adding <i>pathoutgoing</i> if <i>input</i> was not a fully qualified path). If this happens successfully, <code>batcher</code> will then try to rename this temporary file to <i>input</i> (thus replacing <i>input</i> with a copy of itself with all of lines for the successfully batched articles removed).</dl>
<p> Upon receipt of an interrupt or termination signal, <code>batcher</code> will finish batching the current article, close the batch, and then rewrite the batch file as described above.</p>
<h2>History</h2>
<p>Written by Rich <tt>$alz</tt> &lt;rsalz [at] uunet.uu.net&gt; for InterNetNews. Rewritten by Russ Allbery &lt;eagle [at] eyrie.org&gt; in <font SIZE="-1">POD</font>. </p>
<p> <tt>$Id:</tt> batcher.pod 9768 2014-12-07 21:22:57Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-ctlinnd/">ctlinnd</a></i>(8), <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/5-newsfeeds/">newsfeeds</a></i>(5), <i><a href="/docs/linux/man/8-rnews/">rnews</a></i>(8), <i><a href="/docs/linux/man/8-send-uucp/">send-uucp</a></i>(8), <i><a href="/docs/linux/man/1-shlock/">shlock</a></i>(1). </p>
