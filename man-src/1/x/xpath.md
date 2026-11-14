---
title: "xpath(1)"
name: "xpath"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xpath/"
description: "XML::XPath – a set of modules for parsing and evaluating XPath statements"
---

<h2 class="name">NAME</h2>
<p> XML::XPath &#8211; a set of modules for parsing and evaluating XPath statements </p>
<h2>DESCRIPTION</h2>
<p> This module aims to comply exactly to the XPath specification at <a rel="nofollow" href="http://www.w3.org/TR/xpath">http://www.w3.org/TR/xpath</a> and yet allow extensions to be added in the form of functions. Modules such as <font SIZE="-1">XSLT</font> and XPointer may need to do this as they support functionality beyond XPath.</p>
<h2>SYNOPSIS</h2>
<pre><code>
use XML::XPath;
use XML::XPath::XMLParser;

my $xp = XML::XPath-&gt;new (filename = &gt; 'test.xhtml');

my $nodeset = $xp-&gt;find('/html/body/p');
#find all paragraphs

    foreach my
    $node($nodeset-&gt;get_nodelist)
{
    print "FOUND

",
        XML::XPath::XMLParser::as_string($node),
        "

";
}
</code></pre>
<h2>DETAILS</h2>
<p> There&#8217;s an awful lot to all of this, so bear with it &#8211; if you stick it out it should be worth it. Please get a good understanding of XPath by reading the spec before asking me questions. All of the classes and parts herein are named to be synonimous with the names in the specification, so consult that if you don&#8217;t understand why I&#8217;m doing something in the code.</p>
<h2>API</h2>
<p> The <font SIZE="-1">API</font> of XML::XPath itself is extremely simple to allow you to get going almost immediately. The deeper <font SIZE="-1">API</font>&#8216;s are more complex, but you shouldn&#8217;t have to touch most of that.</p>
<h3><i>new()</i></h3>
<p> This constructor follows the often seen named parameter method call. Parameters you can use are: filename, parser, xml, ioref and context. The filename parameter specifies an <font SIZE="-1">XML</font> file to parse. The xml parameter specifies a string to parse, and the ioref parameter specifies an ioref to parse. The context option allows you to specify a context node. The context node has to be in the format of a node as specified in XML::XPath::XMLParser. The 4 parameters filename, xml, ioref and context are mutually exclusive &#8211; you should only specify one (if you specify anything other than context, the context node is the root of your document). The parser option allows you to pass in an already prepared XML::Parser object, to save you having to create more than one in your application (if, for example, you&#8217;re doing more than just XPath). </p>
<pre><code>
my $xp = XML::XPath-&gt;new (context = &gt; $node);
</code></pre>
<p> It is very much recommended that you use only 1 XPath object throughout the life of your application. This is because the object (and it&#8217;s sub-objects) maintain certain bits of state information that will be useful (such as XPath variables) to later calls to <i>find()</i>. It&#8217;s also a good idea because you&#8217;ll use less memory this way.</p>
<h3><i>nodeset</i> = find($path, [$context])</h3>
<p> The find function takes an XPath expression (a string) and returns either an XML::XPath::NodeSet object containing the nodes it found (or empty if no nodes matched the path), or one of XML::XPath::Literal (a string), XML::XPath::Number, or XML::XPath::Boolean. It should always return something &#8211; and you can use -&gt;<i>isa()</i> to find out what it returned. If you need to check how many nodes it found you should check <tt>$nodeset</tt>-&gt;size. See XML::XPath::NodeSet. An optional second parameter of a context node allows you to use this method repeatedly, for example <font SIZE="-1">XSLT</font> needs to do this.</p>
<h3>findnodes($path, [$context])</h3>
<p> Returns a list of nodes found by <tt>$path</tt>, optionally in context <tt>$context</tt>. In scalar context returns an XML::XPath::NodeSet object.</p>
<h3>findnodes_as_string($path, [$context])</h3>
<p> Returns the nodes found reproduced as <font SIZE="-1">XML.</font> The result is not guaranteed to be valid <font SIZE="-1">XML</font> though.</p>
<h3>findvalue($path, [$context])</h3>
<p> Returns either a <tt>&quot;XML::XPath::Literal&quot;</tt>, a <tt>&quot;XML::XPath::Boolean&quot;</tt> or a <tt>&quot;XML::XPath::Number&quot;</tt> object. If the path returns a NodeSet, <tt>$nodeset</tt>-&gt;to_literal is called automatically for you (and thus a <tt>&quot;XML::XPath::Literal&quot;</tt> is returned). Note that for each of the objects stringification is overloaded, so you can just print the value found, or manipulate it in the ways you would a normal perl value (e.g. using regular expressions).</p>
<h3>exists($path, [$context])</h3>
<p> Returns true if the given path exists.</p>
<h3>matches($node, $path, [$context])</h3>
<p> Returns true if the node matches the path (optionally in context <tt>$context</tt>).</p>
<h3>getNodeText($path)</h3>
<p> Returns the text string for a particular <font SIZE="-1">XML</font> node. Returns a string, or undef if the node doesn&#8217;t exist.</p>
<h3>setNodeText($path, $text)</h3>
<p> Sets the text string for a particular <font SIZE="-1">XML</font> node. The node can be an element or an attribute. If the node to be set is an attribute, and the attribute node does not exist, it will be created automatically.</p>
<h3>createNode($path)</h3>
<p> Creates the node matching the path given. If part of the path given, or all of the path do not exist, the necessary nodes will be created automatically.</p>
<h3>set_namespace($prefix, $uri)</h3>
<p> Sets the namespace prefix mapping to the uri. </p>
<p> Normally in XML::XPath the prefixes in XPath node tests take their context from the current node. This means that foo:bar will always match an element &lt;foo:bar&gt; regardless of the namespace that the prefix foo is mapped to (which might even change within the document, resulting in unexpected results). In order to make prefixes in XPath node tests actually map to a real <font SIZE="-1">URI,</font> you need to enable that via a call to the set_namespace method of your XML::XPath object.</p>
<h3><i>clear_namespaces()</i></h3>
<p> Clears all previously set namespace mappings.</p>
<h3>$XML::XPath::Namespaces</h3>
<p> Set this to 0 if you <i>don&#8217;t</i> want namespace processing to occur. This will make everything a little (tiny) bit faster, but you&#8217;ll suffer for it, probably.</p>
<h2>Node Object Model</h2>
<p> See XML::XPath::Node, XML::XPath::Node::Element, XML::XPath::Node::Text, XML::XPath::Node::Comment, XML::XPath::Node::Attribute, XML::XPath::Node::Namespace, and XML::XPath::Node::PI.</p>
<h2>On Garbage Collection</h2>
<p> XPath nodes work in a special way that allows circular references, and yet still lets Perl&#8217;s reference counting garbage collector to clean up the nodes after use. This should be totally transparent to the user, with one caveat: <code>If you free your tree before letting go of a sub-tree, consider that playing with fire and you may get burned</code>. What does this mean to the average user? Not much. Provided you don&#8217;t free (or let go out of scope) either the tree you passed to XML::XPath-&gt;new, or if you didn&#8217;t pass a tree, and passed a filename or IO-ref, then provided you don&#8217;t let the XML::XPath object go out of scope before you let results of <i>find()</i> and its friends go out of scope, then you&#8217;ll be fine. Even if you <code>do</code> let the tree go out of scope before results, you&#8217;ll probably still be fine. The only case where you may get stung is when the last part of your path/query is either an ancestor or parent axis. In that case the worst that will happen is you&#8217;ll end up with a circular reference that won&#8217;t get cleared until interpreter destruction time. You can get around that by explicitly calling <tt>$node</tt>-&gt;<font SIZE="-1">DESTROY</font> on each of your result nodes, if you really need to do that. </p>
<p> Mail me direct if that&#8217;s not clear. Note that it&#8217;s not doom and gloom. It&#8217;s by no means perfect, but the worst that will happen is a long running process could leak memory. Most long running processes will therefore be able to explicitly be careful not to free the tree (or XML::XPath object) before freeing results. AxKit, an application that uses XML::XPath, does this and I didn&#8217;t have to make any changes to the code &#8211; it&#8217;s already sensible programming. </p>
<p> If you <i>really</i> don&#8217;t want all this to happen, then set the variable <tt>$XML::XPath::SafeMode</tt>, and call <tt>$xp</tt>-&gt;<i>cleanup()</i> on the XML::XPath object when you&#8217;re finished, or <tt>$tree</tt>-&gt;<i>dispose()</i> if you have a tree instead.</p>
<h2>Example</h2>
<p> Please see the test files in t/ for examples on how to use XPath.</p>
<h2>Support/Author</h2>
<p> This module is copyright 2000 AxKit.com Ltd. This is free software, and as such comes with <font SIZE="-1">NO WARRANTY.</font> No dates are used in this module. You may distribute this module under the terms of either the Gnu <font SIZE="-1">GPL, </font> or the Artistic License (the same terms as Perl itself). </p>
<p> For support, please subscribe to the Perl-XML mailing list at the <font SIZE="-1">URL </font> <a rel="nofollow" href="http://listserv.activestate.com/mailman/listinfo/perl-xml">http://listserv.activestate.com/mailman/listinfo/perl-xml</a> </p>
<p> Matt Sergeant, matt [at] sergeant.org</p>
<h2>SEE ALSO</h2>
<p> XML::XPath::Literal, XML::XPath::Boolean, XML::XPath::Number, XML::XPath::XMLParser, XML::XPath::NodeSet, XML::XPath::PerlSAX, XML::XPath::Builder. </p>
<h2>Index</h2>
<dt><a href="#lbAT">Node Object Model</a></p>
<dd>
<dt><a href="#lbAU">On Garbage Collection</a></p>
<dd>
<dt><a href="#lbAV">Example</a></p>
<dd>
<dt><a href="#lbAW">Support/Author</a></p>
<dd>
<dt><a href="#lbAX">SEE ALSO</a></p>
<dd></dl>
