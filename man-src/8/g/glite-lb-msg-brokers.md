---
title: "glite-lb-msg-brokers(8)"
name: "glite-lb-msg-brokers"
section: "8"
letter: "g"
url: "/docs/linux/man/8-glite-lb-msg-brokers/"
description: "glite-lb-msg-brokers – manipulate messaging brokers information"
---

<p>glite-lb-msg-brokers &#8211; manipulate messaging brokers information</p>
<h2>Synopsis</h2>
<p><code>glite-lb-msg-brokers</code> [<i></i><i>OPTIONS</i><i></i>] <code>find</code>|<code>list</code></p>
<h2>Description</h2>
<p><code>glite-lb-msg-brokers</code> has two different modes of operation. In all cases, it manipulates information about messaging brokers and reports a (possibly empty) list of broker URIs, one per line.</p>
<dl>
<dt><code>list</code></dt>
<dd>list all the URIs declared in the BDII, optionally filtered by network</dd>
<dt><code>find</code></dt>
<dd>the <code>list</code> functionality described above plus filter by GlueServiceStatus</dd></dl>
<p> A fatal error (e.g. cannot contact the BDII) will halt the program. A warning (e.g. a given URI cannot be contacted) will be reported unless <code>&#8211;quiet</code> is used. Both will be sent to STDERR. </p>
<p> The exit status will be 0 on success (with or without warnings) or different from 0 in case of a fatal error.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;bdii</code> <i>string</i></dt>
<dd>specify the <i>name</i> or <i>name</i>:<i>port</i> of the BDII to contact; this can also be a list, separated by commas or semicolons; if not set, it defaults to <tt>$LCG_GFAL_INFOSYS</tt></dd>
<dt><code>&#8211;cache</code> <i>path</i></dt>
<dd>specify the path of a file to update with the list of URIs; if this is set, nothing will be printed on STDOUT; note: if the list is empty, the file will <i>not</i> be updated</dd>
<dt><code>&#8211;debug</code>, <code>-d</code></dt>
<dd>report debugging information; can be used multiple times for increased verbosity</dd>
<dt><code>&#8211;help</code>, <code>-h</code>, <code>-?</code></dt>
<dd>show some help</dd>
<dt><code>&#8211;manual</code>, <code>-m</code></dt>
<dd>show the complete man page</dd>
<dt><code>&#8211;network</code> <i>string</i></dt>
<dd>consider only the brokers for this network (for example PROD or TEST-NWOB)</dd>
<dt><code>&#8211;quiet</code>, <code>-q</code></dt>
<dd>suppress the printing of warnings</dd>
<dt><code>&#8211;sort</code>, <code>-s</code></dt>
<dd>sort the brokers per elapsed time to perform the test</dd></dl>
<h2>Environment</h2>
<dl>
<dt><code>LCG_GFAL_INFOSYS</code></dt>
<dd><i>host</i>[:<i>port</i>] of the BDII to contact</dd></dl>
<h2>Bugs</h2>
<p>Please report all bugs to CESNET gLite L&amp;B issue tracker available at <i><a rel="nofollow" href="https://github.com/CESNET/glite-lb/issues">https://github.com/CESNET/glite-lb/issues</a></i></p>
<h2>Authors</h2>
<p>Lionel Cons &lt;<a rel="nofollow" href="http://cern.ch/lionel.cons">http://cern.ch/lionel.cons</a>&gt; </p>
<p> L&amp;B Product Team, CESNET &lt;<a rel="nofollow" href="http://cesnet.cz">http://cesnet.cz</a>&gt;</p>
<h2>See Also</h2>
<p>Net::STOMP::Client </p>
