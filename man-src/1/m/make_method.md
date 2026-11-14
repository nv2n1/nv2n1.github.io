---
title: "make_method(1)"
name: "make_method"
section: "1"
letter: "m"
url: "/docs/linux/man/1-make_method/"
description: "make_method – Turn Perl code into an XML description for RPC::XML::Server"
---

<h2 class="name">NAME</h2>
<p> make_method &#8211; Turn Perl code into an XML description for RPC::XML::Server </p>
<h2>SYNOPSIS</h2>
<pre><code>
make_method-- name = system.identification-- helptext = 'System ID string' --signature = string-- code = ident.pl-- output = ident.xpl
                                                                                                                                 make_method-- base = methods / identification
</code></pre>
<h2>DESCRIPTION</h2>
<p> This is a simple tool to create the <font SIZE="-1">XML</font> descriptive files for specifying methods to be published by an <code>RPC::XML::Server</code>-based server. </p>
<p> If a server is written such that the methods it exports (or <i>publishes</i>) are a part of the running code, then there is no need for this tool. However, in cases where the server may be separate and distinct from the code (such as an Apache-based <font SIZE="-1">RPC</font> server), specifying the routines and filling in the supporting information can be cumbersome. </p>
<p> One solution that the <code>RPC::XML::Server</code> package offers is the means to load publishable code from an external file. The file is in a simple <font SIZE="-1">XML</font> dialect that clearly delinates the externally-visible name, the method signatures, the help text and the code itself. These files may be created manually, or this tool may be used as an aide.</p>
<h2>REQUIRED ARGUMENTS</h2>
<p> There are no required arguments, but if there are not sufficient options passed you will be told by an error message.</p>
<h2>OPTIONS</h2>
<p> The tool recognizes the following options:</p>
<dl>
<dt>&#8211;help</p>
<dd> Prints a short summary of the options.</p>
<dt>&#8211;name=STRING</p>
<dd> Specifies the published name of the method being encoded. This is the name by which it will be visible to clients of the server.</p>
<dt>&#8211;namespace=STRING</p>
<dd> Specifies a namespace that the code of the method will be evaluated in, when the <font SIZE="-1">XPL</font> file is loaded by a server instance.</p>
<dt>&#8211;type=STRING</p>
<dd> Specify the type for the resulting file. &#8220;Type&#8221; here refers to whether the container tag used in the resulting <font SIZE="-1">XML</font> will specify a <code>procedure</code> or a <code>method</code>. The default is <code>method</code>. The string is treated case-independant, and only the first character (<tt>&quot;m&quot;</tt> or <tt>&quot;p&quot;</tt>) is actually regarded.</p>
<dt>&#8211;version=STRING</p>
<dd> Specify a version stamp for the code routine.</p>
<dt>&#8211;hidden</p>
<dd> If this is passe, the resulting file will include a tag that tells the server daemon to not make the routine visible through any introspection interfaces.</p>
<dt>&#8211;signature=STRING [ &#8211;signature=STRING &#8230; ]</p>
<dd> Specify one or more signatures for the method. Signatures should be the type names as laid out in the documentation in <font SIZE="-1">RPC::XML</font>, with the elements separated by a colon. You may also separate them with spaces, if you quote the argument. This option may be specified more than once, as some methods may have several signatures.</p>
<dt>&#8211;helptext=STRING</p>
<dd> Specify the help text for the method as a simple string on the command line. Not suited for terribly long help strings.</p>
<dt>&#8211;helpfile=FILE</p>
<dd> Read the help text for the method from the file specified.</p>
<dt>&#8211;code=FILE</p>
<dd> Read the actual code for the routine from the file specified. If this option is not given, the code is read from the standard input file descriptor.</p>
<dt>&#8211;output=FILE</p>
<dd> Write the resulting <font SIZE="-1">XML</font> representation to the specified file. If this option is not given, then the output goes to the standard output file descriptor.</p>
<dt>&#8211;base=NAME</p>
<dd> This is a special, &#8220;all-in-one&#8221; option. If passed, all other options are ignored. </p>
<p> The value is used as the base element for reading information from a file named <font SIZE="-1"><code>BASE</code></font>.base. This file will contain specification of the name, version, hidden status, signatures and other method information. Each line of the file should look like one of the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>Name: </code><font SIZE="-1">STRING</font></p>
<dd> Specify the name of the routine being published. If this line does not appear, then the value of the <code>&#8211;base</code> argument with all directory elements removed will be used.</p>
<dt><code>Version: </code><font SIZE="-1">STRING</font></p>
<dd> Provide a version stamp for the function. If no line matching this pattern is present, no version tag will be written.</p>
<dt><code>Hidden: </code><font SIZE="-1">STRING</font></p>
<dd> If present, <i></i><font SIZE="-1"><i>STRING</i></font><i></i> should be either <tt>&quot;yes&quot;</tt> or <tt>&quot;no&quot;</tt> (case not important). If it is <tt>&quot;yes&quot;</tt>, then the method is marked to be hidden from any introspection <font SIZE="-1">API.</font></p>
<dt><code>Signature: </code><font SIZE="-1">STRING</font></p>
<dd> This line may appear more than once, and is treated cumulatively. Other options override previous values if they appear more than once. The portion following the <tt>&quot;Signature:&quot;</tt> part is taken to be a published signature for the method, with elements separated by whitespace. Each method must have at least one signature, so a lack of any will cause an error.</p>
<dt><code>Helpfile: </code><font SIZE="-1">STRING</font></p>
<dd> Specifies the file from which to read the help text. It is not an error if no help text is specified.</p>
<dt><code>Codefile: </code><font SIZE="-1">STRING</font></p>
<dd> Specifies the file from which to read the code. Code is assumed to be Perl, and will be tagged as such in the resulting file.</p>
<dt><code>Codefile[lang]: </code>string</p>
<dd> Specifies the file from which to read code, while also identifying the language that the code is in. This allows for the creation of a <font SIZE="-1"><code>XPL</code></font> file that includes multiple language implementations of the given method or procedure.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Any other lines than the above patterns are ignored. </p>
<p> If no code has been read, then the tool will exit with an error message. </p>
<p> The output is written to <font SIZE="-1"><code>BASE</code></font>.xpl, preserving the path information so that the resulting file is right alongside the source files. This allows constructs such as: </p>
<pre>
    make_method --base=methods/introspection
</pre>
</dl>
</dl>
<h2>FILE FORMAT AND DTD</h2>
<p> The file format for these published routines is a very simple <font SIZE="-1">XML</font> dialect. This is less due to <font SIZE="-1">XML</font> being an ideal format than it is the availability of the parser, given that the <code>RPC::XML::Server</code> class will already have the parser code in core. Writing a completely new format would not have gained anything. </p>
<p> The Document Type Declaration for the format can be summarized by: </p>
<pre>
    &lt;!ELEMENT  proceduredef (name, namespace?, version?, hidden?,
                             signature+, help?, code)&gt;
    &lt;!ELEMENT  methoddef  (name, namespace?, version?, hidden?,
                           signature+, help?, code)&gt;
    &lt;!ELEMENT  functiondef (name, namespace?, version?, hidden?,
                            signature+, help?, code)&gt;
    &lt;!ELEMENT  name       (#PCDATA)&gt;
    &lt;!ELEMENT  namespace  (#PCDATA)&gt;
    &lt;!ELEMENT  version    (#PCDATA)&gt;
    &lt;!ELEMENT  hidden     EMPTY&gt;
    &lt;!ELEMENT  signature  (#PCDATA)&gt;
    &lt;!ELEMENT  help       (#PCDATA)&gt;
    &lt;!ELEMENT  code       (#PCDATA)&gt;
    &lt;!ATTLIST  code       language (#PCDATA)&gt;
</pre>
<p> The file <tt>&quot;rpc-method.dtd&quot;</tt> that comes with the distribution has some commentary in addition to the actual specification. </p>
<p> A file is (for now) limited to one definition. This is started by the one of the opening tags <tt>&quot;&lt;methoddef&gt;&quot;</tt>, <tt>&quot;&lt;functiondef&gt;&quot;</tt> or <tt>&quot;&lt;proceduredef&gt;&quot;</tt>. This is followed by exactly one <tt>&quot;&lt;name&gt;&quot;</tt> container specifying the method name, an optional version stamp, an optional hide-from-introspection flag, one or more <tt>&quot;&lt;signature&gt;&quot;</tt> containers specifying signatures, an optional <tt>&quot;&lt;help&gt;&quot;</tt> container with the help text, then the <tt>&quot;&lt;code&gt;&quot;</tt> container with the actual program code. All text should use entity encoding for the symbols: </p>
<pre>
    &amp; C&lt;&amp;amp;&gt; (ampersand)
    E&lt;lt&gt; C&lt;&amp;lt;&gt;  (less-than)
    E&lt;gt&gt; C&lt;&amp;gt;&gt;  (greater-than)
</pre>
<p> The parsing process within the server class will decode the entities. To make things easier, the tool scans all text elements and encodes the above entities before writing the file.</p>
<h3>The Specification of Code</h3>
<p> This is not <i>&#8220;Programming 101&#8221;</i>, nor is it <i>&#8220;Perl for the Somewhat Dim&#8221;</i>. The code that is passed in via one of the <tt>&quot;*.xpl&quot;</tt> files gets passed to <tt>&quot;eval&quot;</tt> with next to no modification (see below). Thus, badly-written or malicious code can very well wreak havoc on your server. This is not the fault of the server code. The price of the flexibility this system offers is the responsibility on the part of the developer to ensure that the code is tested and safe. </p>
<p> Code itself is treated as verbatim as possible. Some edits may occur on the server-side, as it make the code suitable for creating an anonymous subroutine from. The <code>make_method</code> tool will attempt to use a <tt>&quot;CDATA&quot;</tt> section to embed the code within the <font SIZE="-1">XML</font> document, so that there is no need to encode entities or such. This allows for the resulting <i>*.xpl</i> files to be syntax-testable with <tt>&quot;perl -cx&quot;</tt>. You can aid this by ensuring that the code does not contain either of the two following character sequences: </p>
<pre>
    ]]&gt;
    __DATA__
</pre>
<p> The first is the <tt>&quot;CDATA&quot;</tt> terminator. If it occurs naturally in the code, it would trigger the end-of-section in the parser. The second is the familiar Perl token, which is inserted so that the remainder of the <font SIZE="-1">XML</font> document does not clutter up the Perl parser.</p>
<h2>EXAMPLES</h2>
<p> The <font SIZE="-1"><code>RPC::XML</code></font> distribution comes with a number of default methods in a subdirectory called (cryptically enough) <tt>&quot;methods&quot;</tt>. Each of these is expressed as a set of (<tt>&quot;*.base&quot;</tt>, <tt>&quot;*.code&quot;</tt>, <tt>&quot;*.help&quot;</tt>) files. The Makefile.PL file configures the resulting Makefile such that these are used to create <tt>&quot;*.xpl&quot;</tt> files using this tool, and then install them.</p>
<h2>DIAGNOSTICS</h2>
<p> Most problems come out in the form of error messages followed by an abrupt exit.</p>
<h2>EXIT STATUS</h2>
<p> The tool exits with a status of 0 upon success, and 255 otherwise.</p>
<h2>CAVEATS</h2>
<p> I don&#8217;t much like this approach to specifying the methods, but I liked my other ideas even less.</p>
<h2>BUGS</h2>
<p> Please report any bugs or feature requests to <tt>&quot;bug-rpc-xml at rt.cpan.org&quot;</tt>, or through the web interface at &lt;<a rel="nofollow" href="http://rt.cpan.org/NoAuth/ReportBug.html?Queue=RPC-XML">http://rt.cpan.org/NoAuth/ReportBug.html?Queue=RPC-XML</a>&gt;. I will be notified, and then you&#8217;ll automatically be notified of progress on your bug as I make changes.</p>
<h2>SUPPORT</h2>
<dl>
<dt>&bull;</p>
<dd> <font SIZE="-1">RT: CPAN</font>&#8216;s request tracker </p>
<p> &lt;<a rel="nofollow" href="http://rt.cpan.org/NoAuth/Bugs.html?Dist=RPC-XML">http://rt.cpan.org/NoAuth/Bugs.html?Dist=RPC-XML</a>&gt;</p>
<dt>&bull;</p>
<dd> AnnoCPAN: Annotated <font SIZE="-1">CPAN</font> documentation </p>
<p> &lt;<a rel="nofollow" href="http://annocpan.org/dist/RPC-XML">http://annocpan.org/dist/RPC-XML</a>&gt;</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">CPAN</font> Ratings </p>
<p> &lt;<a rel="nofollow" href="http://cpanratings.perl.org/d/RPC-XML">http://cpanratings.perl.org/d/RPC-XML</a>&gt;</p>
<dt>&bull;</p>
<dd> Search <font SIZE="-1">CPAN</font> </p>
<p> &lt;<a rel="nofollow" href="http://search.cpan.org/dist/RPC-XML">http://search.cpan.org/dist/RPC-XML</a>&gt;</p>
<dt>&bull;</p>
<dd> Source code on GitHub </p>
<p> &lt;<a rel="nofollow" href="http://github.com/rjray/rpc-xml">http://github.com/rjray/rpc-xml</a>&gt;</dl>
<h2>LICENSE AND COPYRIGHT</h2>
<p> This module and the code within are released under the terms of the Artistic License 2.0 (<a rel="nofollow" href="http://www.opensource.org/licenses/artistic-license-2.0.php">http://www.opensource.org/licenses/artistic-license-2.0.php</a>). This code may be redistributed under either the Artistic License or the <font SIZE="-1">GNU</font> Lesser General Public License (<font SIZE="-1">LGPL</font>) version 2.1 (<a rel="nofollow" href="http://www.opensource.org/licenses/lgpl-2.1.php">http://www.opensource.org/licenses/lgpl-2.1.php</a>).</p>
<h2>SEE ALSO</h2>
<p> <font SIZE="-1">RPC::XML</font>, RPC::XML::Server</p>
<h2>CREDITS</h2>
<p> The <code>XML-RPC</code> standard is Copyright (c) 1998-2001, UserLand Software, Inc. See &lt;<a rel="nofollow" href="http://www.xmlrpc.com">http://www.xmlrpc.com</a>&gt; for more information about the <code>XML-RPC</code> specification.</p>
<h2>AUTHOR</h2>
<p> Randy J. Ray &lt;rjray [at] blackperl.com&gt; </p>
<h2>Index</h2>
