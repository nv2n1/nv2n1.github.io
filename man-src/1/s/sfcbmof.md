---

title: "sfcbmof(1)"
name: "sfcbmof"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sfcbmof/"
description: "sfcbmof – MOF compile for the Small-Footprint CIM Broker (sfcb)"
---

<p> sfcbmof &#8211; MOF compile for the Small-Footprint CIM Broker (sfcb)</p>
<h2>SYNOPSIS</h2>
<p> <code>sfcbmof</code> [<i>options</i>] <i>infile</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> The MOF compiler for sfcb generates binary class data from plaintext MOF class definitions.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></dt>
<dd> Display help message and exit.</dd>
<dt><code>-v</code></dt>
<dd> Verbose mode.</dd>
<dt><code>-V</code></dt>
<dd> Print version information and exit.</dd>
<dt><code>-I</code> <i>includepath</i></dt>
<dd> Directory to search for include files.</dd>
<dt><code>-i</code> <i>extrafile</i></dt>
<dd> File to load before parsing. This option can be used to preload the CIM schema or other pre-requisite classes.</dd>
<dt><code>-o</code> <i>outfile</i></dt>
<dd> Output file to generate. The default is <i>mofc.out</i>.</dd>
<dt><code>-b</code> <i>backendopts</i></dt>
<dd> Backend options. Refer to backend documentation.</dd></dl>
<h2>LIBRARIES</h2>
<p> Requires libsfcBrokerCore.a</p>
<h2>AUTHOR</h2>
<p> Viktor Mihajlovski &lt;MIHAJLOV [at] de.ibm.com&gt;</p>
<h2>BUGS</h2>
<p> The SBLIM project maintains a mailing list to which you should direct all questions regarding sfcb, sfcc, wbemcli, or any of the SBLIM providers. To subscribe to this mailing list visit</p>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://lists.sourceforge.net/lists/listinfo/sblim-issues">http://lists.sourceforge.net/lists/listinfo/sblim-issues</a></dd></dl>
<p> The SBLIM Project Bug tracking page can be found at</p>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://sourceforge.net/tracker/?group_id=128809">http://sourceforge.net/tracker/?group_id=128809</a>&amp;atid=712784</dd></dl>
<h2>COPYRIGHT</h2>
<p> (C) Copyright IBM Corp. 2004, 2005 </p>
<h2>AVAILABILITY</h2>
<p> The Small-Footprint CIM Broker (sfcb) is a part of the SBLIM project. The most recent version is available on the web at</p>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://sblim.sourceforge.net/">http://sblim.sourceforge.net/</a></dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-sfcbd/">sfcbd</a></code>(1) </p>
