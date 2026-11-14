---
title: "xmlgeneratordom(3)"
name: "xmlgeneratordom"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmlgeneratordom/"
---

XML::Generator::DOM - XML::Generator subclass for producing DOM trees instead of strings. 

<h2>Synopsis</h2><pre> use XML::Generator::DOM;
 my $dg = XML::Generator::DOM-&gt;new();
 my $doc = $dg-&gt;xml($dg-&gt;xmlcmnt(&quot;Test document.&quot;),
 $dg-&gt;foo({'baz' =&gt; 'bam'}, 42));
 print $doc-&gt;toString;</pre>yields: 

 <pre> &lt;?xml version=&quot;1.0&quot; standalone=&quot;yes&quot;?&gt;
 &lt;!--Test document--&gt;
 &lt;foo baz=&quot;bam&quot;&gt;42&lt;/foo&gt;</pre><h2>Description</h2>XML::Generator::DOM subclasses XML::Generator in order to produce <font SIZE="-1">DOM</font> trees instead of strings (see XML::Generator and <font SIZE="-1">XML::DOM</font>). This module is still experimental and its semantics might change. 

 Essentially, tag methods return XML::DOM::DocumentFragment objects, constructed either from a <font SIZE="-1">DOM</font> document passed into the constructor or a default document that XML::Generator::DOM will automatically construct. 

 Calling the <i>xml()</i> method will return this automatically constructed document and cause a fresh one to be constructed for future tag method calls. If you passed in your own document, you may not call the <i>xml()</i> method. 

 Below, we just note the remaining differences in semantics between XML::Generator methods and XML::Generator::DOM methods.
<h2>Constructor</h2>These configuration options are accepted but have no effect on the semantics of the returned object: escape, pretty, conformance and empty.
<h2>Tag Methods</h2>Subsequently, tag method semantics are somewhat different for this module compared to XML::Generator. The primary difference is that tag method return XML::DOM::DocumentFragment objects. Namespace and attribute processing remains the same, but remaining arguments to tag methods must either be text or other XML::DOM::DocumentFragment objects. No escape processing, syntax checking, or output control is done; this is all left up to <font SIZE="-1">XML::DOM.</font>
<h2>Special Tags</h2>All special tags are available by default with XML::Generator::DOM; you don't need to use 'conformance' =&gt; 'strict'.
<h3>xmlpi(@args)</h3>Arguments will simply be concatenated and passed as the data to the XML::DOM::ProcessingInstruction object that is returned.
<h3>xmlcmnt</h3>Escaping of '--' is done by XML::DOM::Comment, which replaces both hyphens with '&amp;#45;'. An XML::DOM::Comment object is returned.
<h3>xmldecl</h3>Returns an XML::DOM::XMLDecl object. Respects 'version', 'encoding' and 'dtd' settings in the object.
<h3>xmldecl</h3>Returns an XML::DOM::DocumentType object.
<h3>xmlcdata</h3>Returns an XML::DOM::CDATASection object.
<h3>xml</h3>As described above, <i>xml()</i> can only be used when dom_document was not set in the object. The automatically created document will have its <font SIZE="-1">XML</font> Declaration set and the arguments to <i>xml()</i> will be appended to it. Then a new <font SIZE="-1">DOM</font> document is automatically generated and the old one is returned. This is the only way to get a <font SIZE="-1">DOM</font> document from this module.
