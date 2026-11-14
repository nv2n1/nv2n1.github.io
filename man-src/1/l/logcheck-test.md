---
title: "logcheck-test(1)"
name: "logcheck-test"
section: "1"
letter: "l"
url: "/docs/linux/man/1-logcheck-test/"
description: "logcheck-test – test new logcheck rules easily"
---

<h2>NAME</h2>
<p> logcheck-test &#8211; test new logcheck rules easily</p>
<h2>SYNOPSIS</h2>
<p> <code>logcheck-test</code> [<code>-q</code>|<code>-i</code>] [<code>-a</code>|<code>-s</code>|<code>-l</code> <i>FILE</i>] [<code>-e</code>] [<code>-P</code> <i>PREFIX</i>] [<code>-S</code> <i>SUFFIX</i>] <i>RULE</i><br />
 <code>logcheck-test</code> [<code>-q</code>|<code>-i</code>] [<code>-a</code>|<code>-s</code>|<code>-l</code> <i>FILE</i>] <code>-r</code> <i>RULEFILE</i></p>
<h2>DESCRIPTION</h2>
<p> <code>logcheck-test</code> parses a log file for matching lines specified by a single rule or a rule file. If using a single <i>RULE</i> you can set a <i>PREFIX</i> and a <i>SUFFIX</i> to write new rules easily. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show usage information</p>
<dt><code>-a, &#8211;auth.log</code></p>
<dd> Parse /var/log/auth.log for matching lines</p>
<dt><code>-s, &#8211;syslog</code></p>
<dd> Parse /var/log/syslog for matching lines</p>
<dt><code>-l, &#8211;log-file FILE</code></p>
<dd> Parse FILE for matching lines</p>
<dt><code>-i, &#8211;invert-match</code></p>
<dd> Show line that don&#8217;t match the RULE or the RULEFILE</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> Suppress rule summary at the end of output</p>
<dt><code>-e, &#8211;surround-rule</code></p>
<dd> Surround RULE with standard prefix and suffix: </p>
<p> ^[[:alpha:]]{3} [ :[:digit:]]{11} [._[:alnum:]-]+ <i>RULE</i>$</p>
<dt><code>-P, &#8211;append-prefix PREFIX</code></p>
<dd> Append PREFIX to rule prefix. Option can be given multiple times</p>
<dt><code>-S, &#8211;prepend-suffix SUFFIX</code></p>
<dd> Prepend SUFFIX to rule suffix. Option can be given multiple times</p>
<dt><code>-r, &#8211;rule-file RULEFILE</code></p>
<dd> Use file RULEFILE for rule input</dl>
<h2>EXAMPLES</h2>
<p> With <code>logcheck-test</code> you can easily write and test new rules. </p>
<p> Test a single rule against /var/log/syslog:</p>
<dl>
<dt>
<dd> logcheck-test -s &quot;RULE&quot;</dl>
<p> Test a single rule against ~/log, surround the rule with standard prefix and suffix and append &quot;kernel &quot; to prefix:</p>
<dl>
<dt>
<dd> logcheck-test -l ~/log -e -P &quot;kernel &quot; &quot;RULE&quot;</dl>
<p> Test the rules in rulefiles/linux/ignore.d.server/kernel against ~/log:</p>
<dl>
<dt>
<dd> logcheck-test -l ~/log -r rulefiles/linux/ignore.d.server/kernel</dl>
<p> Test which lines the rules in rulefiles/linux/ignore.d.server/kernel doesn&#8217;t match:</p>
<dl>
<dt>
<dd> logcheck-test -l ~/log -r rulefiles/linux/ignore.d.server/kernel -i</dl>
<h2>EXIT STATUS</h2>
<p> On successful matching <code>logcheck-test</code> will complete with exit code 0. An exit code of 1 indicates no successful matching. </p>
<p> An exit code greater then 1 indicates an error occurred. Textual errors are written to the standard error stream.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-logcheck/">logcheck</a></code>(8)</p>
<h2>AUTHOR</h2>
<p> logcheck is developed by Debian logcheck Team at alioth: <a rel="nofollow" href="http://alioth.debian.org/projects/logcheck/.">http://alioth.debian.org/projects/logcheck/.</a> This manual was written by Hannes von Haugwitz &lt;hannes [at] vonhaugwitz.com&gt;. </p>
<h2>Index</h2>
