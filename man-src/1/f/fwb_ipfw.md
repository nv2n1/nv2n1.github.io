---
title: "fwb_ipfw(1)"
name: "fwb_ipfw"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fwb_ipfw/"
description: "fwb_ipfw – Policy compiler for ipfw"
---

<h2>NAME</h2>
<p> fwb_ipfw &#8211; Policy compiler for ipfw</p>
<h2>SYNOPSIS</h2>
<p> <code>fwb_ipfw</code> <code>[-vVx]</code> <code>[-d wdir]</code> <code>[-o output.fw]</code> <code>[-i]</code> <code>-f data_file.xml</code> object_name </p>
<h2>DESCRIPTION</h2>
<p> <code>fwb_ipfw</code> is a firewall policy compiler component of Firewall Builder (see <a href="/docs/linux/man/1-fwbuilder/">fwbuilder</a>(1)). This compiler generates code for ipfw &#8211; a firewall and traffic shaper in FreeBSD (see <a href="/docs/linux/man/8-ipfw/">ipfw</a>(8)). Compiler reads objects definitions and firewall description from the data file specified with &quot;-f&quot; option and generates firewall configuration and activation script. </p>
<p> The generated file has a name that starts with the name of the firewall object, with an extension &quot;.fw&quot;. It is a shell script that flushes current policy, then loads new filter and nat rules. </p>
<p> The data file and the name of the firewall objects must be specified on the command line. Other command line parameters are optional. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-f FILE</p>
<dd> Specify the name of the data file to be processed. </p>
<dt>-o output.fw</p>
<dd> Specify output file name </p>
<dt>-d wdir</p>
<dd> Specify working directory. Compiler creates firewall activation script in this directory. If this parameter is missing, then all files will be placed in the current working directory. </p>
<dt>-v</p>
<dd> Be verbose: compiler prints diagnostic messages when it works. </p>
<dt>-V</p>
<dd> Print version number and quit. </p>
<dt>-i</p>
<dd> When this option is present, the last argument on the command line is supposed to be firewall object ID rather than its name </p>
<dt>-x</p>
<dd> Generate debugging information while working. This option is intended for debugging only and may produce lots of cryptic messages. </p>
</dl>
<h2>NOTES</h2>
<p> Support for ipfw was added in version 1.0.10 of Firewall Builder </p>
<h2>URL</h2>
<p> Firewall Builder home page is located at the following URL: <code><a rel="nofollow" href="http://www.fwbuilder.org/">http://www.fwbuilder.org/</a></code> </p>
<h2>BUGS</h2>
<p> Please report bugs using bug tracking system on SourceForge: </p>
<p> <code><a rel="nofollow" href="http://sourceforge.net/tracker/?group_id=5314">http://sourceforge.net/tracker/?group_id=5314</a>&amp;atid=105314</code> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-fwbuilder/">fwbuilder</a>(1),</code> <code><a href="/docs/linux/man/1-fwb_ipt/">fwb_ipt</a>(1),</code> <code><a href="/docs/linux/man/1-fwb_pf/">fwb_pf</a>(1)</code> <code><a href="/docs/linux/man/1-fwb_ipf/">fwb_ipf</a>(1)</code> </p>
<h2>Index</h2>
