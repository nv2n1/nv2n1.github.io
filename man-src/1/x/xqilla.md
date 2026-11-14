---
title: "xqilla(1)"
name: "xqilla"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xqilla/"
description: "xqilla – run XQuery and XPath 2 expressions"
---

<h2>NAME</h2>
<p> xqilla &#8211; run XQuery and XPath 2 expressions</p>
<h2>SYNOPSIS</h2>
<p> <code>xqilla</code> [<i>OPTION</i>]&#8230; QUERY-FILE&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Run XQuery and XPath 2 expressions from QUERY-FILE.</p>
<dl>
<dt><code>-h</code></p>
<dd> Show help and exit</p>
<dt><code>-p</code></p>
<dd> Parse in XPath 2 mode (default is XQuery mode)</p>
<dt><code>-P</code></p>
<dd> Parse in XPath 1.0 compatibility mode (default is XQuery mode)</p>
<dt><code>-s</code></p>
<dd> Parse XSLT 2.0</p>
<dt><code>-f</code></p>
<dd> Parse using W3C Full-Text extensions</p>
<dt><code>-u</code></p>
<dd> Parse using W3C Update extensions</p>
<dt><code>-e</code></p>
<dd> Parse using XQilla specific extensions</p>
<dt><code>-d</code></p>
<dd> Run the query in interactive debugging mode</p>
<dt><code>-x</code></p>
<dd> Use the Xerces-C data model (default is the FastXDM)</p>
<dt><code>-i</code> <i>file</i></p>
<dd> Load XML document and bind it as the context item</p>
<dt><code>-b</code> <i>baseURI</i></p>
<dd> Set the base URI for the context</p>
<dt><code>-v</code> <i>name</i> <i>value</i></p>
<dd> Bind the name value pair as an external variable</p>
<dt><code>-o</code> <i>file</i></p>
<dd> Write the result to the specified file</p>
<dt><code>-n</code> <i>number</i></p>
<dd> Run the queries a number of times</p>
<dt><code>-q</code></p>
<dd> Quiet mode &#8211; no output</p>
<dt><code>-t</code></p>
<dd> Output an XML representation of the AST</dl>
<p> The <code>xqilla</code> command line tool can be used to run XQuery and XPath 2 expressions. It is also a good example of how to use the <code>Simple API</code> of the <code>XQilla</code> library.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;<a rel="nofollow" href="https://sourceforge.net/projects/xqilla/support">https://sourceforge.net/projects/xqilla/support</a>&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2008 DecisionSoft Limited.<br />
 Copyright &#169; 2004-2008 Oracle. </p>
<p> Licensed under the Apache License, Version 2.0 (the &quot;License&quot;); you may not use this file except in compliance with the License. You may obtain a copy of the License at &lt;<a rel="nofollow" href="http://www.apache.org/licenses/LICENSE-2.0">http://www.apache.org/licenses/LICENSE-2.0</a>&gt; </p>
<p> Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an &quot;AS IS&quot; BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for the <code>XQilla library</code> is available at &lt;<a rel="nofollow" href="http://xqilla.sourceforge.net/Documentation">http://xqilla.sourceforge.net/Documentation</a>&gt;. </p>
<h2>Index</h2>
