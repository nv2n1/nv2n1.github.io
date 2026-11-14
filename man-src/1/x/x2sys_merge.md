---
title: "x2sys_merge(1)"
name: "x2sys_merge"
section: "1"
letter: "x"
url: "/docs/linux/man/1-x2sys_merge/"
description: "x2sys_merge – Merge an updated COEs table (smaller) into the main table (bigger)"
---

<h2>NAME</h2>
<p> x2sys_merge &#8211; Merge an updated COEs table (smaller) into the main table (bigger)</p>
<h2>SYNOPSIS</h2>
<p> <code>x2sys_merge</code> <i>main_COElist.d</i> <i>new_COElist.d</i> </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>x2sys_merge</code> will read two crossovers data base and output the contents of the main one updated with the COEs in the second one. The second file should only contain updated COEs relatively to the first one. That is, it MUST NOT contain any new two tracks intersections (This point is NOT checked in the code). This program is useful when, for any good reason like file editing NAV correction or whatever, one had to recompute only the COEs between the edited files and the rest of the database.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><code>-A</code><i>main_COElist.d</i></p>
<dd> Specify the file <i>main_COElist.d</i> with the main crossover error data base.</p>
<dt><code>-M</code><i>new_COElist.d</i></p>
<dd> Specify the file <i>new_COElist.d</i> with the newly computed crossover error data base.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<h2>EXAMPLES</h2>
<p> To update the main COE_data.txt with the new COEs estimations saved in the smaller COE_fresh.txt, try </p>
<pre>
gmt x2sys_merge -ACOE_data.txt -MCOE_fresh.txt &gt; COE_updated.txt
</pre>
<h2>SEE ALSO</h2>
<p> <code>x2sys_binlist</code>, <code>x2sys_cross</code>, <code>x2sys_datalist</code>, <code>x2sys_get</code>, <code>x2sys_init</code>, <code>x2sys_list</code>, <code>x2sys_put</code>, <code>x2sys_report</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
