---

title: "xml_grep(1)"
name: "xml_grep"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xml_grep/"
description: "xml_grep – grep XML files looking for specific elements"
---

<p> xml_grep &#8211; grep XML files looking for specific elements </p>
<h2>SYNOPSYS</h2>
<pre>
  xml_grep [options] &lt;file list&gt;
</pre>
<p> or </p>
<pre>
  xml_grep &lt;xpath expression&gt; &lt;file list&gt;
</pre>
<p> By default you can just give <tt>&quot;xml_grep&quot;</tt> an XPath expression and a list of files, and get an XML file with the result. </p>
<p> This is equivalent to writing </p>
<pre>
  xml_grep --group_by_file file --pretty_print indented --cond &lt;file list&gt;
</pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></dt>
<dd> brief help message</dd>
<dt><code>&#8211;man</code></dt>
<dd> full documentation</dd>
<dt><code>&#8211;Version</code></dt>
<dd> display the tool version</dd>
<dt><code>&#8211;root</code> &lt;cond&gt;</dt>
<dd> look for and return xml chunks matching &lt;cond&gt; </dd>
<p> if neither <tt>&quot;--root&quot;</tt> nor <tt>&quot;--file&quot;</tt> are used then the element(s) that trigger the <tt>&quot;--cond&quot;</tt> option is (are) used. If <tt>&quot;--cond&quot;</tt> is not used then all elements matching the &lt;cond&gt; are returned </p>
<p> several <tt>&quot;--root&quot;</tt> can be provided</p>
<dt><code>&#8211;cond</code> &lt;cond&gt;</dt>
<dd> return the chunks (or file names) only if they contain elements matching &lt;cond&gt; </dd>
<p> several <tt>&quot;--cond&quot;</tt> can be provided (in which case they are OR&#8216;ed)</p>
<dt><code>&#8211;files</code></dt>
<dd> return only file names (do not generate an XML output) </dd>
<p> usage of this option precludes using any of the options that define the XML output: <tt>&quot;--roots&quot;</tt>, <tt>&quot;--encoding&quot;</tt>, <tt>&quot;--wrap&quot;</tt>, <tt>&quot;--group_by_file&quot;</tt> or <tt>&quot;--pretty_print&quot;</tt></p>
<dt><code>&#8211;count</code></dt>
<dd> return only the number of matches in each file </dd>
<p> usage of this option precludes using any of the options that define the XML output: <tt>&quot;--roots&quot;</tt>, <tt>&quot;--encoding&quot;</tt>, <tt>&quot;--wrap&quot;</tt>, <tt>&quot;--group_by_file&quot;</tt> or <tt>&quot;--pretty_print&quot;</tt></p>
<dt><code>&#8211;strict</code></dt>
<dd> without this option parsing errors are reported to STDOUT and the file skipped</dd>
<dt><code>&#8211;date</code></dt>
<dd> when on (by default) the wrapping element get a <tt>&quot;date&quot;</tt> attribute that gives the date the tool was run. </dd>
<p> with <tt>&quot;--nodate&quot;</tt> this attribute is not added, which can be useful if you need to compare 2 runs.</p>
<dt><code>&#8211;encoding</code> &lt;enc&gt;</dt>
<dd> encoding of the xml output (utf-8 by default)</dd>
<dt><code>&#8211;nb_results</code> &lt;nb&gt;</dt>
<dd> output only &lt;nb&gt; results</dd>
<dt><code>&#8211;by_file</code></dt>
<dd> output only &lt;nb&gt; results by file</dd>
<dt><code>&#8211;wrap</code> &lt;tag&gt;</dt>
<dd> wrap the xml result in the provided tag (defaults to &#8216;xml_grep&#8217;) </dd>
<p> If wrap is set to an empty string (<tt>&quot;--wrap ''&quot;</tt>) then the xml result is not wrapped at all.</p>
<dt><code>&#8211;nowrap</code></dt>
<dd> same as using <tt>&quot;--wrap ''&quot;</tt>: the xml result is not wrapped.</dd>
<dt><code>&#8211;descr</code> &lt;string&gt;</dt>
<dd> attributes of the wrap tag (defaults to <tt>&quot;version=&quot;&lt;VERSION&gt;&quot; date=&quot;&lt;date&gt;&quot;&quot;</tt>)</dd>
<dt><code>&#8211;group_by_file</code> &lt;optional_tag&gt;</dt>
<dd> wrap results for each files into a separate element. By default that element is named <tt>&quot;file&quot;</tt>. It has an attribute named <tt>&quot;filename&quot;</tt> that gives the name of the file. </dd>
<p> the short version of this option is <code>-g</code></p>
<dt><code>&#8211;exclude</code> &lt;condition&gt;</dt>
<dd> same as using <tt>&quot;-v&quot;</tt> in grep: the elements that match the condition are excluded from the result, the input file(s) is (are) otherwise unchanged </dd>
<p> the short form of this option is <code>-v</code></p>
<dt><code>&#8211;pretty_print</code> &lt;optional_style&gt;</dt>
<dd> pretty print the output using XML::Twig styles (&#8216;<tt>&quot;indented&quot;</tt>&#8216;, &#8216;<tt>&quot;record&quot;</tt>&#8216; or &#8216;<tt>&quot;record_c&quot;</tt>&#8216; are probably what you are looking for) </dd>
<p> if the option is used but no style is given then &#8216;<tt>&quot;indented&quot;</tt>&#8216; is used </p>
<p> short form for this argument is <code>-s</code></p>
<dt><code>&#8211;text_only</code></dt>
<dd> Displays the text of the results, one by line.</dd>
<dt><code>&#8211;html</code></dt>
<dd> Allow HTML input, files are converted using HTML::TreeBuilder</dd>
<dt><code>&#8211;Tidy</code></dt>
<dd> Allow HTML input, files are converted using HTML::Tidy</dd></dl>
<h3>Condition Syntax</h3>
<p> &lt;cond&gt; is an XPath-like expression as allowed by XML::Twig to trigger handlers. </p>
<p> exemples:<br/>
&nbsp;<wbr>&nbsp;<wbr>&#8216;para&#8217;<br/>
&nbsp;<wbr>&nbsp;<wbr>&#8216;para[@compact=&#8220;compact&#8221;]&#8217;<br/>
&nbsp;<wbr>&nbsp;<wbr>&#8216;*[@urgent]&#8217;<br/>
&nbsp;<wbr>&nbsp;<wbr>&#8216;*[@urgent=&#8220;1&#8221;]&#8217;<br/>
&nbsp;<wbr>&nbsp;<wbr>&#8216;para[<i>string()</i>=&#8220;WARNING&#8221;]&#8217; </p>
<p> see XML::Twig for a more complete description of the &lt;cond&gt; syntax </p>
<p> options are processedby Getopt::Long so they can start with &#8216;-&#8216; or &#8216;&#8211;&#8216; and can be abbreviated (<tt>&quot;-r&quot;</tt> instead of <tt>&quot;--root&quot;</tt> for example)</p>
<h2>DESCRIPTION</h2>
<p> <code>xml_grep</code> does a grep on XML files. Instead of using regular expressions it uses XPath expressions (in fact the subset of XPath supported by XML::Twig) </p>
<p> the results can be the names of the files or XML elements containing matching elements.</p>
<h2>SEE ALSO</h2>
<p> XML::Twig Getopt::Long</p>
<h2>LICENSE</h2>
<p> This library is free software; you can redistribute it and/or modify it under the same terms as Perl itself.</p>
<h2>AUTHOR</h2>
<p> Michel Rodriguez &lt;mirod [at] xmltwig.com&gt; </p>
