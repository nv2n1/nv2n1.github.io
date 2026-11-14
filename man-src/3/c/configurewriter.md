---
title: "configurewriter(3)"
name: "configurewriter"
section: "3"
letter: "c"
url: "/docs/linux/man/3-configurewriter/"
description: "XMLTV::Configure::Writer – Configuration file writer for XMLTV grabbers"
---

<p>XMLTV::Configure::Writer &#8211; Configuration file writer for XMLTV grabbers </p>
<h2>Description</h2>
<p>Utility class that helps grabbers write configuration descriptions.</p>
<h2>Synopsis</h2>
<pre> use XMLTV::Configure::Writer;
 my $result;
 my $writer = new XMLTV::Writer::Configure( OUTPUT =&gt; \$result,
 encoding =&gt; 'iso-8859-1' );
 $writer-&gt;start( { grabber =&gt; 'tv_grab_xxx' } );
 $writer-&gt;write_string( {
 id =&gt; 'username', 
 title =&gt; [ [ 'Username', 'en' ],
 [ 'Anva.ndarnamn', 'sv' ] ],
 description =&gt; [ [ 'The username for logging in to DataDirect.', 'en' ],
 [ 'Anva.ndarnamn hos DataDirect', 'sv' ] ],
 } );
 $writer-&gt;start_selectone( {
 id =&gt; 'lineup', 
 title =&gt; [ [ 'Lineup', 'en' ],
 [ 'Programpaket', 'sv' ] ],
 description =&gt; [ [ 'The lineup of channels for your region.', 'en' ],
 [ 'Programpaket fo.r din region', 'sv' ] ],
 } );
 $writer-&gt;write_option( { 
 value=&gt;'eastcoast',
 text=&gt; =&gt; [ [ 'East Coast', 'en' ],
 [ 'O.stkusten', 'sv' ] ] 
 } );
 $writer-&gt;write_option( { 
 value=&gt;'westcoast',
 text=&gt; =&gt; [ [ 'West Coast', 'en' ],
 [ 'Va.stkusten', 'sv' ] ] 
 } );
 $writer-&gt;end_selectone();
 $writer-&gt;end();
 print $result;</pre>
<h2>Exported Functions</h2>
<p>None.</p>
<h2>Methods</h2>
<dl COMPACT>
<dt><i>start()</i></p>
<dd>Write the start of the &lt;xmltvconfiguration&gt; element. Parameter is a hashref which gives the attributes of this element.</p>
<dt><i>write_string()</i></p>
<dd>Write a &lt;string&gt; element. Parameter is a hashref with the data for the element: </p>
<pre> $writer-&gt;write_string( {
 id =&gt; 'username', 
 title =&gt; [ [ 'Username', 'en' ],
 [ 'Anva.ndarnamn', 'sv' ] ],
 description =&gt; [ [ 'The username for logging in to DataDirect.', 'en' ],
 [ 'Anva.ndarnamn hos DataDirect', 'sv' ] ],
 default =&gt; &quot;&quot;,
 } );</pre>
<p>To add a constant use &#8216;constant&#8217; key: <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>If constant value is empty then revert to &#8216;ask&#8217; procedure.</p>
<pre> $writer-&gt;write_string( {
 id =&gt; 'version', 
 title =&gt; [ [ 'Version number', 'en' ] ],
 description =&gt; [ [ 'Automatically added version number - no user input', 'en' ] ],
 constant =&gt; '123',
 } );</pre>
</dl>
<h2>Pod Errors</h2>
<p>Hey! <code>The above document had some coding errors, which are explained below:</code></p>
<dl COMPACT>
<dt>Around line 44:</p>
<dd>Non-ASCII character seen before =encoding in &#8221;Anva.ndarnamn&#8217;,&#8217;. Assuming <font SIZE="-1">ISO8859-1</font> </p>
</dl>
