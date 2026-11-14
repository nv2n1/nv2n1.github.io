---
title: "fwb_pix(1)"
name: "fwb_pix"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fwb_pix/"
description: "fwb_ipt – Policy compiler for Cisco PIX"
---

<h2>NAME</h2>
<p> fwb_ipt &#8211; Policy compiler for Cisco PIX</p>
<h2>SYNOPSIS</h2>
<p> <code>fwb_pix</code> <code>[-vVi]</code> <code>[-d wdir]</code> <code>-f data_file.xml</code> object_name </p>
<h2>DESCRIPTION</h2>
<p> <code>fwb_pix</code> is firewall policy compiler component of Firewall Builder (see <a href="/docs/linux/man/1-fwbuilder/">fwbuilder</a>(1)). Compiler reads objects definitions and firewall description from the data file specified with &quot;-f&quot; option and generates resultant Cisco PIX configuration file. The configuration is written to the file with the name the same as the name of the firewall object, plus extension &quot;.fw&quot;. </p>
<p> The data file and the name of the firewall objects must be specified on the command line. Other command line parameters are optional. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-f FILE</p>
<dd> Specify the name of the data file to be processed. </p>
<dt>-d wdir</p>
<dd> Specify working directory. Compiler creates file with PIX configuration in this directory. If this parameter is missing, then PIX configuration will be placed in the current working directory. </p>
<dt>-v</p>
<dd> Be verbose: compiler prints diagnostic messages when it works. </p>
<dt>-V</p>
<dd> Print version number and quit. </p>
<dt>-i</p>
<dd> When this option is present, the last argument on the command line is supposed to be firewall object ID rather than its name </p>
</dl>
<h2>URL</h2>
<p> Firewall Builder home page is located at the following URL: <code><a rel="nofollow" href="http://www.fwbuilder.org/">http://www.fwbuilder.org/</a></code> </p>
<h2>BUGS</h2>
<p> Please report bugs using bug tracking system on SourceForge: </p>
<p> <code><a rel="nofollow" href="http://sourceforge.net/tracker/?group_id=5314">http://sourceforge.net/tracker/?group_id=5314</a>&amp;atid=105314</code> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-fwbuilder/">fwbuilder</a>(1),</code> <code><a href="/docs/linux/man/1-fwb_ipf/">fwb_ipf</a>(1),</code> <code><a href="/docs/linux/man/1-fwb_ipt/">fwb_ipt</a>(1)</code> <code><a href="/docs/linux/man/1-fwb_pf/">fwb_pf</a>(1)</code> </p>
<h2>Index</h2>
