---
title: "sgmldiff(1)"
name: "sgmldiff"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sgmldiff/"
description: "sgmldiff – Find differences in the markup of two SGML files"
---

<h2 class="name">NAME</h2>
<p> sgmldiff &#8211; Find differences in the markup of two SGML files </p>
<h2>SYNOPSIS</h2>
<p> <code>sgmldiff</code> [ <code>options </code><i> &#8230;</i> ] <i>file1</i> <i>file2</i> [ <code>-a</code> | <code>&#8211;attributes</code><br />
&nbsp;<wbr>|&nbsp;<wbr><code>-c&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr>attributes | nesting | textpos&nbsp;<wbr>]</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;context&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr>attributes | nesting | textpos&nbsp;<wbr>]</code><br />
&nbsp;<wbr>|&nbsp;<wbr><code>-s</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;statistics</code><br />
&nbsp;<wbr>|&nbsp;<wbr><code>-h</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;help</code><br />
&nbsp;<wbr>|&nbsp;<wbr><code>-v</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;version</code>&nbsp;<wbr>] </p>
<h2>DESCRIPTION</h2>
<p> This perl script allows to determine the structural differences between two SGML files. It compares the files, regardless of what is in between the tags, to only focus on the markup. Its output is similar to <code><a href="/docs/linux/man/1-diff/">diff</a></code>(1). </p>
<p> The typical use of <code>sgmldiff</code> is to compare an SGML file with its translation into another language. If the translation was done cleanly, <code>sgmldiff</code> returns without finding any difference in the markup. </p>
<p> An example of a typical call to sgmldiff is: </p>
<pre>
      sgmldiff english.sgml italiano.sgml
    
</pre>
<p> If there are differences in markup between both files, <code>sgmldiff</code> will output a series of differences reports summarized with lines of the form:</p>
<dl>
<dt><code>169a164</code></p>
<dd> At line 169 of the first file, line 164 of the second file has been added.</p>
<dt><code>8a12,15</code></p>
<dd> At line 8 of the first file, lines 12 to 15 of the second file have been added.</p>
<dt><code>41d28</code></p>
<dd> Line 41 of the first file has been destroyed, to obtain line 28 of the second file.</p>
<dt><code>63,66d61</code></p>
<dd> Lines 63 to 66 of the first file have been destroyed. to obtain line 61 of the second file.</p>
<dt><code>52c51</code></p>
<dd> Line 52 of the first file has been changed into line 51 of the second file.</p>
<dt><code>5,7c8,10</code></p>
<dd> Lines 5 to 7 of the first file have been changed into lines 8 to 10 of the second line. In addition to those summaries, the lines of the first file are shown preceeded by &#8216;&lt;&#8216; and the lines of the second file are shown preceeded by &#8216;&gt;&quot;.</dl>
<h2>OPTIONS</h2>
<p> Here is the list of actions that can be requested to sgmldiff:</p>
<dl>
<dt><code> [ -a | &#8211;attributes ] </code></p>
<dd> Include the attribute values in the difference tests. Don&#8217;t set this value if the attributes are likely to be translated. Set this value if the attributes value shouldn&#8217;t change between both files. Default is to don&#8217;t include the attributes in the difference tests.</p>
<dt><code> [ -c [ attributes | nesting | textpos ] | &#8211;context [ attributes | nesting | textpos ] ] </code></p>
<dd> Add more context to the difference. Since every test between the tags is removed before testing the differences, <code>sgmldiff</code> is likely to resynchronize itself at the wrong place, by thinking the location in both files correspond, while it&#8217;s not true. By adding more context to the compared area, such risk is disminished. </p>
<p> The allowed values for the <code>&#8211;context</code> option are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>attributes</code></p>
<dd> Take into account the attribute <code>names</code>. The attribute <code>values</code> are controlled by the <code>attributes</code> option.</p>
<dt><code>nesting</code></p>
<dd> Take into account the nesting level of all the compared tags.</p>
<dt><code>textpos</code></p>
<dd> Take into account the position in the text.</dl>
</dl>
<dt><code> [ -s | &#8211;statistics ] </code></p>
<dd> Print some SGML information at the end.</p>
<dt><code> [ -h | &#8211;help ] </code></p>
<dd> Print a short help message and exit</p>
<dt><code> [ -v | &#8211;version ] </code></p>
<dd> Print the version identifier and exit</dl>
<h2>FILES</h2>
<h2>AUTHORS</h2>
<dl>
<dt><code> Frederik Fouvry </code></p>
<dd> Developer of <code>sgmldiff</code>.</dl>
<h2>SEE ALSO</h2>
<dl>
<dt><code> <a href="/docs/linux/man/1-jw/">jw</a>(1) </code></p>
<dd> conversion from a SGML file to other file formats</p>
<dt><code> <a href="/docs/linux/man/1-nsgmls/">nsgmls</a>(1) </code></p>
<dd> a base component of <code>Jade</code> DSSSL engine</p>
<dt><code> <a rel="nofollow" href="http://sources.redhat.com/docbook-tools/">http://sources.redhat.com/docbook-tools/</a> &lt;URL:<a href="http://sources.redhat.com/docbook-tools/">http://sources.redhat.com/docbook-tools/</a>&gt; </code></p>
<dd> the home page of the DocBook tools, a compendium of all tools necessary to process DocBook files, including the DocBook-utils </p>
</dl>
<h2>Index</h2>
