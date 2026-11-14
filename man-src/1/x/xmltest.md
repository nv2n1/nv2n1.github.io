---
title: "xmltest(1)"
name: "xmltest"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xmltest/"
description: "xmltest – Test script to send CIM-XML (via wbemcat) to CIMOM and compare to known results"
---

<h2>NAME</h2>
<p> xmltest &#8211; Test script to send CIM-XML (via wbemcat) to CIMOM and compare to known results</p>
<h2>SYNOPSIS</h2>
<p> <code>xmltest</code> [<i>FILE</i><code>] </code></p>
<h2>DESCRIPTION</h2>
<p> xmltest is a script that is used to send a raw CIM-XML test file to the sfcb CIMOM (using wbemcat) and then compares the returned CIM-XML results against a previously determined &#8216;OK&#8217; result file to check whether the returned results match the expected results. If there does not yet exist an &#8216;OK&#8217; corresponding to the XML file then xmltest will save the returned results as the new OK file for later use. If the returned CIM-XML results don&#8217;t match the existing &#8216;OK&#8217; file a new &#8216;result&#8217; file will be generated containing the erroneous results. </p>
<p> If no <i>FILE</i><code> is specified xmltest will use all files with a .xml extension in the current directory path. </code></p>
<h2>EXAMPLE</h2>
<p> If there is no &#8216;OK&#8217; file to compare returned CIM-XML results against xmltest will generate one.</p>
<dl>
<dt>
<dd>
<table>
<tr VALIGN=top>
<td># xmltest test/getclass.Linux_OperatingSystem.xml</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Running test test/getclass.Linux_OperatingSystem.xml &#8230; OK</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Saving response as test/getclass.Linux_OperatingSystem.OK</td>
<td>
</td>
</tr>
</table>
</dl>
<p> If the returned CIM-XML results match the existing &#8216;OK&#8217; file xmltest will signal that the test passed.</p>
<dl>
<dt>
<dd>
<table>
<tr VALIGN=top>
<td># xmltest test/getclass.Linux_OperatingSystem.xml</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Running test test/getclass.Linux_OperatingSystem.xml &#8230; Passed</td>
<td>
</td>
</tr>
</table>
</dl>
<p> If the returned CIM-XML results don&#8217;t match the existing &#8216;OK&#8217; file xmltest will signal that the tes failed and generate a &#8216;result&#8217; file containing the erroneous results.</p>
<dl>
<dt>
<dd>
<table>
<tr VALIGN=top>
<td># xmltest test/getclass.Linux_OperatingSystem.xml</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Running test test/getclass.Linux_OperatingSystem.xml &#8230; FAILED</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Check test/getclass.Linux_OperatingSystem.result for errors</td>
<td>
</td>
</tr>
</table>
</dl>
<h2>PREREQUISITES</h2>
<p> Requires wbemcat on search path.</p>
<h2>AUTHOR</h2>
<p> Dr. Gareth S. Bestor &lt;bestor [at] us.ibm.com&gt;</p>
<h2>CONTRIBUTORS</h2>
<p> Adrian Schuur &lt;schuur [at] de.ibm.com&gt;</p>
<h2>BUGS</h2>
<p> Does not adequately deal with additional http headers/footers caused by chunking responses, which will result in false failures when comparing results to existing &quot;x.OK&quot; files. </p>
<p> The SBLIM project maintains a mailing list to which you should direct all questions regarding sfcb, sfcc, wbemcli, or any of the SBLIM providers. To subscribe to this mailing list visit</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://lists.sourceforge.net/lists/listinfo/sblim-issues">http://lists.sourceforge.net/lists/listinfo/sblim-issues</a></dl>
<p> The SBLIM Project Bug tracking page can be found at</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://sourceforge.net/tracker/?group_id=128809">http://sourceforge.net/tracker/?group_id=128809</a>&amp;atid=712784</dl>
<h2>COPYRIGHT</h2>
<p> (C) Copyright IBM Corp. 2004, 2005</p>
<h2>AVAILABILITY</h2>
<p> The Small-Footprint CIM Broker (sfcb) is a part of the SBLIM project. The most recent version is available on the web at</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://sblim.sourceforge.net/">http://sblim.sourceforge.net/</a></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wbemcat/">wbemcat</a></code>(1) </p>
<h2>Index</h2>
