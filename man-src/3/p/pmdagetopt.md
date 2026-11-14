---
title: "pmdagetopt(3)"
name: "pmdagetopt"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmdagetopt/"
description: "pmdaGetOpt, pmdaGetOptions – get options from arguments, parsing generic PMDA options"
---

<p><code>pmdaGetOpt</code>, <code>pmdaGetOptions</code> &#8211; get options from arguments, parsing generic PMDA options</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt;<br />
 #include &lt;pcp/impl.h&gt;<br />
 #include &lt;pcp/pmda.h&gt; </p>
<p> int pmdaGetOptions(int </code><i>argc</i>, char *const *<i>argv</i>, pmdaOptions *<i>opts</i>, pmdaInterface&nbsp;<wbr>*<i>dispatch</i>); </p>
<p> int pmdaGetOpt(int <i>argc</i>, char *const *<i>argv</i>, const char&nbsp;<wbr>*<i>optstring</i>, pmdaInterface&nbsp;<wbr>*<i>dispatch</i>, int&nbsp;<wbr>*<i>err</i>); </p>
<p> cc &#8230; -lpcp_pmda -lpcp</p>
<h2>Description</h2>
<p>These functions are wrappers for <code><a href="/docs/linux/man/3-pmgetopt_r/">pmgetopt_r</a></code>(3). The behavior of each function is that certain options are assumed to have a predefined behavior which initializes several fields in the <code>pmdaInterface</code> structure. The <code>pmdaGetOptions</code> interface allows both short and long options to be given, whereas <code>pmdaGetOpt</code> allows for short form options only. </p>
<p> The options that both <code>pmdaGetOptions</code> and <code>pmdaGetOpt</code> will trap are:</p>
<dl>
<dt><code>-D</code><i>trace</i></p>
<dd>Set the <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) debug control variable (<code>pmDebug</code>) to <i>trace</i>. Used for controlling levels of trace output while debugging.</p>
<dt><code>-d</code><i>domain</i></p>
<dd>Set the <i>domain</i> number of this agent.</p>
<dt><code>-h</code><i>helpfile</i></p>
<dd>Obtain the help text (see <code><a href="/docs/linux/man/3-pmdatext/">pmdaText</a></code>(3)) for the metrics from this file rather than from the path specified with <code><a href="/docs/linux/man/3-pmdadso/">pmdaDSO</a></code>(3) or <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3).</p>
<dt><code>-i</code><i>port</i></p>
<dd>Expect PMCD to connect on inet <i>port</i> (number or name).</p>
<dt><code>-6</code><i>port</i></p>
<dd>Expect PMCD to connect on ipv6 <i>port</i> (number or name).</p>
<dt><code>-l</code><i>logfile</i></p>
<dd>Redirect diagnostics and trace output to <i>logfile</i>.</p>
<dt><code>-p</code></p>
<dd>Expect PMCD to supply stdin/stdout pipe.</p>
<dt><code>-u</code><i>socket</i></p>
<dd>Expect PMCD to connect on unix domain <i>socket</i>.</dl>
<p> The <code>pmdaGetOptions</code> interface will also capture the following options, and store them within the <i>opts</i> parameter:</p>
<dl>
<dt><code>-U</code><i>username</i></p>
<dd>Set the user account name under which the PMDA should execute.</dl>
<p> Only one of <code>-i</code>, <code>-6</code>, <code>-p</code> and <code>-u</code> may be specified. If none of these three options is given, a pipe (<code>-p</code>) is assumed. When these options are encountered by <code>pmdaGetOpt</code>, the option is processed and the next option is examined. Therefore, <code>pmdaGetOpt</code> will only return when an option other than those listed above is found, or the end of the list is reached. The returned value will be the argument or EOF, respectively. </p>
<p> A PMDA can control which of these options the program will accept with either the <i>opts</i> or <i>optstring</i> argument. To accept all the options, the PMDA should call <code>pmdaGetOptions</code> with the short_options field of the <i>opts</i> structure set to the PMDA_OPTIONS macro, or <code>pmdaGetOpt</code> with the option string &quot;D:d:h:i:l:pu:&quot;. Any PMDA specific options should be added to these strings in the style of <code><a href="/docs/linux/man/3-getopt/">getopt</a></code>(3), and will be returned by both <code>pmdaGetOptions</code> and <code>pmdaGetOpt</code> if encountered. </p>
<p> When a command line option usage error is detected in the <code>pmdaGetOptions</code> interface, the error field of the <i>opts</i> structure will contain a non-zero error count. </p>
<p> <code>pmdaGetOpt</code> takes a pointer to an int, <i>err</i>, which is used as an error count. This variable should be initialized to zero before <code>pmdaGetOpt </code> is first called, and tested when <code>pmdaGetOpt</code> returns EOF. </p>
<p> Neither <code>pmdaGetOptions</code> nor <code>pmdaGetOpt</code> modify their <i>argc</i> or <i>argv</i> parameters. </p>
<p> The global variables used by the system <code>getopt (3)</code> interface may also be used by the caller of <code>pmdaGetOpt</code> within the argument parsing loop. </p>
<p> On the other hand, the <code>pmdaGetOptions</code> interface does not utilize global variables at all (neither reading nor modifying them). Instead, these variables can be access via the <i>opts</i> fields of the same name.</p>
<h2>Diagnostics</h2>
<p>Both <code>pmdaGetOptions</code> and <code>pmdaGetOpt</code> will display the same error messages as <code>getopt</code>.</p>
<h2>Caveat</h2>
<p>The options <code>-D</code>, <code>-d</code>, <code>-i</code>, <code>-l</code>, <code>-p</code> and <code>-u</code> cannot be reused for other purposes by the PMDA, unless using the <i>override</i> method provided by the <code>pmdaGetOptions</code> interface, which operates in the same way as described for the <code><a href="/docs/linux/man/3-pmgetoptions/">pmGetOptions</a></code>(3) interface used by PMAPI client tools. </p>
<p> The PMDA must be using <code>PMDA_INTERFACE_2 </code> or later, as specified in the call to <code><a href="/docs/linux/man/3-pmdadso/">pmdaDSO</a></code>(3) or <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pmdbg/">pmdbg</a></code>(1), <code><a href="/docs/linux/man/3-getopt/">getopt</a></code>(3), <code><a href="/docs/linux/man/3-pmgetopt_r/">pmgetopt_r</a></code>(3), <code><a href="/docs/linux/man/3-pmgetoptions/">pmGetOptions</a></code>(3), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3), <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3), <code><a href="/docs/linux/man/3-pmdadso/">pmdaDSO</a></code>(3) and <code><a href="/docs/linux/man/3-pmdatext/">pmdaText</a></code>(3). </p>
