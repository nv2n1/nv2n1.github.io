---
title: "sendinpaths(8)"
name: "sendinpaths"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sendinpaths/"
description: "sendinpaths – Send Usenet Path: statistics via e-mail"
---

<p>sendinpaths &#8211; Send Usenet Path: statistics via e-mail</p>
<h2>Synopsis</h2>
<p><code>sendinpaths</code> [<code>-cdhn</code>] [<code>-k</code> <i>keep-days</i>] [<code>-r</code> <i>report-days</i>] [<i>address</i> [<i>address</i> &#8230;]]</p>
<h2>Description</h2>
<p><code>sendinpaths</code> checks <i>pathlog</i>/path for <code>ninpaths</code> dump files, finds dump files generated in the past <i>report-days</i> days, makes sure they are valid by running <code>ninpaths</code> on each one and making sure the exit status is zero, and passes them to <code>ninpaths</code> to generate a cumulative report. By default, that report is mailed to the e-mail addresses configured at the beginning of this script (by default, only one address is configured: &lt;top1000 [at] anthologeek.net&gt;) in order to supply the <font SIZE="-1">TOP1000</font> project with useful statistics. See &lt;<a rel="nofollow" href="http://top1000.anthologeek.net/">http://top1000.anthologeek.net/</a>&gt; for more information. </p>
<p> When finished, <code>sendinpaths</code> deletes all dump files in <i>pathlog</i>/path that are older than <i>keep-days</i> days. </p>
<p> For more information on how to set up <code>ninpaths</code>, see <i><a href="/docs/linux/man/8-ninpaths/">ninpaths</a></i>(8).</p>
<h2>Options</h2>
<dl>
<dt><code>-c</code></p>
<dd>When this flag is used, the report is also e-mailed, besides the default submission addresses or those given as command-line arguments, to the newsmaster&#8217;s address set at configure time.</p>
<dt><code>-d</code></p>
<dd>Enables debug messages.</p>
<dt><code>-h</code></p>
<dd>Gives usage information.</p>
<dt><code>-k</code> <i>keep-days</i></p>
<dd>After having processed dump files, <code>sendinpaths</code> removes those that are older than <i>keep-days</i> days. The default is <tt>0</tt>, that is to say to remove all dump files. </p>
<p> Setting <i>keep-days</i> to another value can be useful for debugging purpose because it permits to keep a few dump files.</p>
<dt><code>-n</code></p>
<dd>Don&#8217;t e-mail the report; instead, just print it to standard output. Don&#8217;t delete old dump files.</p>
<dt><code>-r</code> <i>report-days</i></p>
<dd>Process dump files generated during the last <i>report-days</i> days. The default is <tt>32</tt>, that is to say to process all the dump files that have been generated during the last 32 days (if, of course, they have not been deleted yet by a previous run of <code>sendinpaths</code> according to the value set by the <code>-k</code> flag).</p>
<dt><i>address</i> &#8230;</p>
<dd>E-mail the report to the mentioned address or addresses, instead of the default one. Several addresses can be used, separated by whitespace (sending the e-mail to your own e-mail address can be useful for debugging purpose, to check that everything works fine). For instance, for two addresses: </p>
<pre> sendinpaths pathsurvey [at] example.org top1000 [at] anthologeek.net</pre>
</dl>
<h2>History</h2>
<p><code>sendinpaths</code> was written by Olaf Titz &lt;olaf [at] bigred.inka.de&gt;. </p>
<p> <tt>$Id:</tt> sendinpaths.pod 9625 2014-03-16 13:24:22Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-ninpaths/">ninpaths</a></i>(8). </p>
