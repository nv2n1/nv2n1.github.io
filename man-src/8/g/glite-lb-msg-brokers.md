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
<p><code>glite-lb-msg-brokers</code> [<i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i>] <code>find</code>|<code>list</code></p>
<h2>Description</h2>
<p><code>glite-lb-msg-brokers</code> has two different modes of operation. In all cases, it manipulates information about messaging brokers and reports a (possibly empty) list of broker URIs, one per line.</p>
<dl>
<dt><code>list</code></p>
<dd>list all the URIs declared in the <font SIZE="-1">BDII,</font> optionally filtered by network</p>
<dt><code>find</code></p>
<dd>the <code>list</code> functionality described above plus filter by GlueServiceStatus</dl>
<p> A fatal error (e.g. cannot contact the <font SIZE="-1">BDII</font>) will halt the program. A warning (e.g. a given <font SIZE="-1">URI</font> cannot be contacted) will be reported unless <code>&#8211;quiet</code> is used. Both will be sent to <font SIZE="-1">STDERR.</font> </p>
<p> The exit status will be 0 on success (with or without warnings) or different from 0 in case of a fatal error.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;bdii</code> <i>string</i></p>
<dd>specify the <i>name</i> or <i>name</i>:<i>port</i> of the <font SIZE="-1">BDII</font> to contact; this can also be a list, separated by commas or semicolons; if not set, it defaults to <tt>$LCG_GFAL_INFOSYS</tt></p>
<dt><code>&#8211;cache</code> <i>path</i></p>
<dd>specify the path of a file to update with the list of URIs; if this is set, nothing will be printed on <font SIZE="-1">STDOUT</font>; note: if the list is empty, the file will <i>not</i> be updated</p>
<dt><code>&#8211;debug</code>, <code>-d</code></p>
<dd>report debugging information; can be used multiple times for increased verbosity</p>
<dt><code>&#8211;help</code>, <code>-h</code>, <code>-?</code></p>
<dd>show some help</p>
<dt><code>&#8211;manual</code>, <code>-m</code></p>
<dd>show the complete man page</p>
<dt><code>&#8211;network</code> <i>string</i></p>
<dd>consider only the brokers for this network (for example <font SIZE="-1">PROD</font> or TEST-NWOB)</p>
<dt><code>&#8211;quiet</code>, <code>-q</code></p>
<dd>suppress the printing of warnings</p>
<dt><code>&#8211;sort</code>, <code>-s</code></p>
<dd>sort the brokers per elapsed time to perform the test</dl>
<h2>Environment</h2>
<dl>
<dt><font SIZE="-1"><code>LCG_GFAL_INFOSYS</code></font></p>
<dd><i>host</i>[:<i>port</i>] of the <font SIZE="-1">BDII</font> to contact</dl>
<h2>Bugs</h2>
<p>Please report all bugs to <font SIZE="-1">CESNET</font> gLite L&amp;B issue tracker available at <i><a rel="nofollow" href="https://github.com/CESNET/glite-lb/issues">https://github.com/CESNET/glite-lb/issues</a></i></p>
<h2>Authors</h2>
<p>Lionel Cons &lt;<a rel="nofollow" href="http://cern.ch/lionel.cons">http://cern.ch/lionel.cons</a>&gt; </p>
<p> L&amp;B Product Team, <font SIZE="-1">CESNET </font>&lt;<a rel="nofollow" href="http://cesnet.cz">http://cesnet.cz</a>&gt;</p>
<h2>See Also</h2>
<p>Net::STOMP::Client </p>
