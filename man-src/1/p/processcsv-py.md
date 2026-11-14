---
title: "processcsv-py(1)"
name: "processcsv-py"
section: "1"
letter: "p"
url: "/docs/linux/man/1-processcsv-py/"
description: "processcsv.py – process virt-top CSV files"
---

<p>processcsv.py &#8211; process virt-top CSV files </p>
<h2>Summary</h2>
<pre> virt-top --csv data.csv
 processcsv.py &lt; data.csv</pre>
<h2>Description</h2>
<p>virt-top is a <i><a href="/docs/linux/man/1-top/">top</a></i>(1)-like utility for showing stats of virtualized domains. </p>
<p> processcsv.py is a simple Python script that post-processes the output of <tt>&quot;virt-top --csv&quot;</tt>. </p>
<p> It is used like this: </p>
<pre> virt-top --csv data.csv
 processcsv.py &lt; data.csv</pre>
<p>The second command will <code>overwrite</code> the following files in the current directory:</p>
<dl COMPACT>
<dt>&quot;global.csv&quot;</p>
<dd>This contains the global (host) statistics columns from the <font SIZE="-1">CSV</font> file.</p>
<dt>&quot;domainNN<tt>.csv&quot; (multiple files)</p>
<dd>For each libvirt domain </tt><font SIZE="-1"><tt>ID </tt></font><tt></tt><i></i><font SIZE="-1"><i>NN</i></font><i></i>, a file is created containing the per-domain statistics from the <font SIZE="-1">CSV</font> file.</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-virt-top/">virt-top</a></i>(1)</p>
<h2>Authors</h2>
<p>Richard W.M. Jones &lt;rjones @ redhat . com&gt;</p>
<h2>Copyright</h2>
<p>(C) Copyright 2007-2012 Red Hat Inc., Richard W.M. Jones <a rel="nofollow" href="http://libvirt.org/">http://libvirt.org/</a> </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, <font SIZE="-1">MA 02139, USA.</font></p>
