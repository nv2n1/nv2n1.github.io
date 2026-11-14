---
title: "gcov-tool-8(1)"
name: "gcov-tool-8"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gcov-tool-8/"
description: "gcov-tool – offline gcda profile processing tool"
---

<h2 class="name">NAME</h2>
<p> gcov-tool &#8211; offline gcda profile processing tool </p>
<h2>SYNOPSIS</h2>
<p> gcov-tool [<code>-v</code>|<code>&#8211;version</code>] [<code>-h</code>|<code>&#8211;help</code>] </p>
<p> gcov-tool merge [merge-options] <i>directory1</i> <i>directory2</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-o</code>|<code>&#8211;output</code>&nbsp;<i>directory</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-v</code>|<code>&#8211;verbose</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-w</code>|<code>&#8211;weight</code>&nbsp;<i>w1,w2</i>] </p>
<p> gcov-tool rewrite [rewrite-options] <i>directory</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-n</code>|<code>&#8211;normalize</code>&nbsp;<i>long_long_value</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-o</code>|<code>&#8211;output</code>&nbsp;<i>directory</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-s</code>|<code>&#8211;scale</code>&nbsp;<i>float_or_simple-frac_value</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-v</code>|<code>&#8211;verbose</code>] </p>
<p> gcov-tool overlap [overlap-options] <i>directory1</i> <i>directory2</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-f</code>|<code>&#8211;function</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-F</code>|<code>&#8211;fullname</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-h</code>|<code>&#8211;hotonly</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-o</code>|<code>&#8211;object</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-t</code>|<code>&#8211;hot_threshold</code>]&nbsp;<i>float</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-v</code>|<code>&#8211;verbose</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>gcov-tool</code> is an offline tool to process gcc&#8217;s gcda profile files. </p>
<p> Current gcov-tool supports the following functionalities:</p>
<dl>
<dt>*</p>
<dd> merge two sets of profiles with weights.</p>
<dt>*</p>
<dd> read one set of profile and rewrite profile contents. One can scale or normalize the count values.</dl>
<p> Examples of the use cases for this tool are:</p>
<dl>
<dt>*</p>
<dd> Collect the profiles for different set of inputs, and use this tool to merge them. One can specify the weight to factor in the relative importance of each input.</p>
<dt>*</p>
<dd> Rewrite the profile after removing a subset of the gcda files, while maintaining the consistency of the summary and the histogram.</p>
<dt>*</p>
<dd> It can also be used to debug or libgcov code as the tools shares the majority code as the runtime library.</dl>
<p> Note that for the merging operation, this profile generated offline may contain slight different values from the online merged profile. Here are a list of typical differences:</p>
<dl>
<dt>*</p>
<dd> histogram difference: This offline tool recomputes the histogram after merging the counters. The resulting histogram, therefore, is precise. The online merging does not have this capability &#8212; the histogram is merged from two histograms and the result is an approximation.</p>
<dt>*</p>
<dd> summary checksum difference: Summary checksum uses a <font SIZE="-1">CRC32</font> operation. The value depends on the link list order of gcov-info objects. This order is different in gcov-tool from that in the online merge. It&#8217;s expected to have different summary checksums. It does not really matter as the compiler does not use this checksum anywhere.</p>
<dt>*</p>
<dd> value profile counter values difference: Some counter values for value profile are runtime dependent, like heap addresses. It&#8217;s normal to see some difference in these kind of counters.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8211;help</code></p>
<dd> Display help about using <code>gcov-tool</code> (on the standard output), and exit without doing any further processing.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Display the <code>gcov-tool</code> version number (on the standard output), and exit without doing any further processing.</p>
<dt><code>merge</code></p>
<dd> Merge two profile directories.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-o</code> <i>directory</i></p>
<dd>
<dt><code>&#8211;output</code> <i>directory</i></p>
<dd> Set the output profile directory. Default output directory name is <i>merged_profile</i>.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd> Set the verbose mode.</p>
<dt><code>-w</code> <i>w1</i><code>,</code><i>w2</i></p>
<dd>
<dt><code>&#8211;weight</code> <i>w1</i><code>,</code><i>w2</i></p>
<dd> Set the merge weights of the <i>directory1</i> and <i>directory2</i>, respectively. The default weights are 1 for both.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>rewrite</code></p>
<dd> Read the specified profile directory and rewrite to a new directory.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-n</code> <i>long_long_value</i></p>
<dd>
<dt><code>&#8211;normalize &lt;long_long_value&gt;</code></p>
<dd> Normalize the profile. The specified value is the max counter value in the new profile.</p>
<dt><code>-o</code> <i>directory</i></p>
<dd>
<dt><code>&#8211;output</code> <i>directory</i></p>
<dd> Set the output profile directory. Default output name is <i>rewrite_profile</i>.</p>
<dt><code>-s</code> <i>float_or_simple-frac_value</i></p>
<dd>
<dt><code>&#8211;scale</code> <i>float_or_simple-frac_value</i></p>
<dd> Scale the profile counters. The specified value can be in floating point value, or simple fraction value form, such 1, 2, 2/3, and 5/3.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd> Set the verbose mode.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>overlap</code></p>
<dd> Compute the overlap score between the two specified profile directories. The overlap score is computed based on the arc profiles. It is defined as the sum of min (p1_counter[i] / p1_sum_all, p2_counter[i] / p2_sum_all), for all arc counter i, where p1_counter[i] and p2_counter[i] are two matched counters and p1_sum_all and p2_sum_all are the sum of counter values in profile 1 and profile 2, respectively.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-f</code></p>
<dd>
<dt><code>&#8211;function</code></p>
<dd> Print function level overlap score.</p>
<dt><code>-F</code></p>
<dd>
<dt><code>&#8211;fullname</code></p>
<dd> Print full gcda filename.</p>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8211;hotonly</code></p>
<dd> Only print info for hot objects/functions.</p>
<dt><code>-o</code></p>
<dd>
<dt><code>&#8211;object</code></p>
<dd> Print object level overlap score.</p>
<dt><code>-t</code> <i>float</i></p>
<dd>
<dt><code>&#8211;hot_threshold &lt;float&gt;</code></p>
<dd> Set the threshold for hot counter value.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd> Set the verbose mode.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gpl/">gpl</a></code>(7), <code><a href="/docs/linux/man/7-gfdl/">gfdl</a></code>(7), <code><a href="/docs/linux/man/7-fsf-funding/">fsf-funding</a></code>(7), <code><a href="/docs/linux/man/1-gcc/">gcc</a></code>(1), <code><a href="/docs/linux/man/1-gcov/">gcov</a></code>(1) and the Info entry for <i>gcc</i>.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2014-2018 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with the Invariant Sections being &#8220;<font SIZE="-1">GNU</font> General Public License&#8221; and &#8220;Funding Free Software&#8221;, the Front-Cover texts being (a) (see below), and with the Back-Cover Texts being (b) (see below). A copy of the license is included in the <code><a href="/docs/linux/man/7-gfdl/">gfdl</a></code>(7) man page. </p>
<p> (a) The <font SIZE="-1">FSF</font>&#8216;s Front-Cover Text is: </p>
<pre>
     A GNU Manual
</pre>
<p> (b) The <font SIZE="-1">FSF</font>&#8216;s Back-Cover Text is: </p>
<pre>
     You have freedom to copy and modify this GNU Manual, like GNU
     software.  Copies published by the Free Software Foundation raise
     funds for GNU development.
</pre>
<h2>Index</h2>
