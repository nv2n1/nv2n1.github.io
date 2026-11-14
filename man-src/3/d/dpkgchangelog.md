---
title: "dpkgchangelog(3)"
name: "dpkgchangelog"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpkgchangelog/"
description: "Dpkg::Changelog – base class to implement a changelog parser"
---

<p>Dpkg::Changelog &#8211; base class to implement a changelog parser </p>
<h2>Description</h2>
<p>Dpkg::Changelog is a class representing a changelog file as an array of changelog entries (Dpkg::Changelog::Entry). By deriving this object and implementing its parse method, you add the ability to fill this object with changelog entries.</p>
<h3><font SIZE="-1">FUNCTIONS</font></h3>
<dl COMPACT>
<dt>my $c = Dpkg::Changelog-&gt;new(%options)</p>
<dd>Creates a new changelog object.</p>
<dt>$c-&gt;load($filename)</p>
<dd>Parse <tt>$filename</tt> as a changelog.</p>
<dt>$c-&gt;set_options(%opts)</p>
<dd>Change the value of some options. &#8220;verbose&#8221; (defaults to 1) defines whether parse errors are displayed as warnings by default. &#8220;reportfile&#8221; is a string to use instead of the name of the file parsed, in particular in error messages. &#8220;range&#8221; defines the range of entries that we want to parse, the parser will stop as soon as it has parsed enough data to satisfy <tt>$c</tt>-&gt;get_range($opts{range}).</p>
<dt>$c-&gt;<i>reset_parse_errors()</i></p>
<dd>Can be used to delete all information about errors occurred during previous parse runs.</p>
<dt>$c-&gt;parse_error($file, $line_nr, $error, [$line])</p>
<dd>Record a new parse error in <tt>$file</tt> at line <tt>$line_nr</tt>. The error message is specified with <tt>$error</tt> and a copy of the line can be recorded in <tt>$line</tt>.</p>
<dt>$c-&gt;<i>get_parse_errors()</i></p>
<dd>Returns all error messages from the last parse run. If called in scalar context returns a human readable string representation. If called in list context returns an array of arrays. Each of these arrays contains</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>1.</p>
<dd>a string describing the origin of the data (a filename usually). If the reportfile configuration option was given, its value will be used instead.</p>
<dt>2.</p>
<dd>the line number where the error occurred</p>
<dt>3.</p>
<dd>an error description</p>
<dt>4.</p>
<dd>the original line</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>$c-&gt;set_unparsed_tail($tail)</p>
<dd>Add a string representing unparsed lines after the changelog entries. Use undef as <tt>$tail</tt> to remove the unparsed lines currently set.</p>
<dt>$c-&gt;<i>get_unparsed_tail()</i></p>
<dd>Return a string representing the unparsed lines after the changelog entries. Returns undef if there&#8217;s no such thing.</p>
<dt>@{$c}</p>
<dd>Returns all the Dpkg::Changelog::Entry objects contained in this changelog in the order in which they have been parsed.</p>
<dt>$c-&gt;get_range($range)</p>
<dd>Returns an array (if called in list context) or a reference to an array of Dpkg::Changelog::Entry objects which each represent one entry of the changelog. <tt>$range</tt> is a hash reference describing the range of entries to return. See section &#8220;<font SIZE="-1">RANGE SELECTION&#8221;</font>.</p>
<dt>$c-&gt;<i>abort_early()</i></p>
<dd>Returns true if enough data have been parsed to be able to return all entries selected by the range set at creation (or with set_options).</p>
<dt>$c-&gt;save($filename)</p>
<dd>Save the changelog in the given file.</p>
<dt>$c-&gt;<i>output()</i></p>
<dd>
<dt>&quot;$c&quot;</p>
<dd>Returns a string representation of the changelog (it&#8217;s a concatenation of the string representation of the individual changelog entries).</p>
<dt>$c-&gt;output($fh)</p>
<dd>Output the changelog to the given filehandle.</p>
<dt>my $control = $c-&gt;dpkg($range)</p>
<dd>Returns a Dpkg::Control::Changelog object representing the entries selected by the optional range specifier (see &#8220;<font SIZE="-1">RANGE SELECTION&#8221;</font> for details). Returns undef in no entries are matched. </p>
<p> The following fields are contained in the object:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Source</p>
<dd>package name (in the first entry)</p>
<dt>Version</p>
<dd>packages&#8217; version (from first entry)</p>
<dt>Distribution</p>
<dd>target distribution (from first entry)</p>
<dt>Urgency</p>
<dd>urgency (highest of all printed entries)</p>
<dt>Maintainer</p>
<dd>person that created the (first) entry</p>
<dt>Date</p>
<dd>date of the (first) entry</p>
<dt>Closes</p>
<dd>bugs closed by the entry/entries, sorted by bug number</p>
<dt>Changes</p>
<dd>content of the the entry/entries</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>my @controls = $c-&gt;rfc822($range)</p>
<dd>Returns a Dpkg::Index containing Dpkg::Control::Changelog objects where each object represents one entry in the changelog that is part of the range requested (see &#8220;<font SIZE="-1">RANGE SELECTION&#8221;</font> for details). For the format of such an object see the description of the &#8220;dpkg&#8221; method (while ignoring the remarks about which values are taken from the first entry).</dl>
<h2>Range Selection</h2>
<p>A range selection is described by a hash reference where the allowed keys and values are described below. </p>
<p> The following options take a version number as value.</p>
<dl COMPACT>
<dt>since</p>
<dd>Causes changelog information from all versions strictly later than <code>version</code> to be used.</p>
<dt>until</p>
<dd>Causes changelog information from all versions strictly earlier than <code>version</code> to be used.</p>
<dt>from</p>
<dd>Similar to <tt>&quot;since&quot;</tt> but also includes the information for the specified <code>version</code> itself.</p>
<dt>to</p>
<dd>Similar to <tt>&quot;until&quot;</tt> but also includes the information for the specified <code>version</code> itself.</dl>
<p> The following options don&#8217;t take version numbers as values:</p>
<dl COMPACT>
<dt>all</p>
<dd>If set to a true value, all entries of the changelog are returned, this overrides all other options.</p>
<dt>count</p>
<dd>Expects a signed integer as value. Returns <tt>&quot;value&quot;</tt> entries from the top of the changelog if set to a positive integer, and <tt>&quot;abs(value)&quot;</tt> entries from the tail if set to a negative integer.</p>
<dt>offset</p>
<dd>Expects a signed integer as value. Changes the starting point for <tt>&quot;count&quot;</tt>, either counted from the top (positive integer) or from the tail (negative integer). <tt>&quot;offset&quot;</tt> has no effect if <tt>&quot;count&quot;</tt> wasn&#8217;t given as well.</dl>
<p> Some examples for the above options. Imagine an example changelog with entries for the versions 1.2, 1.3, 2.0, 2.1, 2.2, 3.0 and 3.1. </p>
<pre> Range Included entries
 C&lt;{ since =E&lt;gt&gt; '2.0' }&gt; 3.1, 3.0, 2.2
 C&lt;{ until =E&lt;gt&gt; '2.0' }&gt; 1.3, 1.2
 C&lt;{ from =E&lt;gt&gt; '2.0' }&gt; 3.1, 3.0, 2.2, 2.1, 2.0
 C&lt;{ to =E&lt;gt&gt; '2.0' }&gt; 2.0, 1.3, 1.2
 C&lt;{ count =E&lt;gt&gt; 2 }&gt; 3.1, 3.0
 C&lt;{ count =E&lt;gt&gt; -2 }&gt; 1.3, 1.2
 C&lt;{ count =E&lt;gt&gt; 3, offset=E&lt;gt&gt; 2 }&gt; 2.2, 2.1, 2.0
 C&lt;{ count =E&lt;gt&gt; 2, offset=E&lt;gt&gt; -3 }&gt; 2.0, 1.3
 C&lt;{ count =E&lt;gt&gt; -2, offset=E&lt;gt&gt; 3 }&gt; 3.0, 2.2
 C&lt;{ count =E&lt;gt&gt; -2, offset=E&lt;gt&gt; -3 }&gt; 2.2, 2.1</pre>
<p>Any combination of one option of <tt>&quot;since&quot;</tt> and <tt>&quot;from&quot;</tt> and one of <tt>&quot;until&quot;</tt> and <tt>&quot;to&quot;</tt> returns the intersection of the two results with only one of the options specified.</p>
<h2>Changes</h2>
<h3>Version 1.00</h3>
<p>Mark the module as public.</p>
<h2>Author</h2>
<p>Frank Lichtenheld, &lt;frank [at] lichtenheld.de&gt; Raphaël Hertzog, &lt;hertzog [at] debian.org&gt;</p>
