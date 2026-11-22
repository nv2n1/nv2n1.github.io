---

title: "xqilla(1)"
name: "xqilla"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xqilla/"
description: "xqilla – run XQuery and XPath 2 expressions"
---

<p> xqilla &#8211; run XQuery and XPath 2 expressions</p>
<h2>SYNOPSIS</h2>
<p> <code>xqilla</code> [<i>OPTION</i>]&#8230; QUERY-FILE&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Run XQuery and XPath 2 expressions from QUERY-FILE.</p>
<dl>
<dt><code>-h</code></dt>
<dd> Show help and exit</dd>
<dt><code>-p</code></dt>
<dd> Parse in XPath 2 mode (default is XQuery mode)</dd>
<dt><code>-P</code></dt>
<dd> Parse in XPath 1.0 compatibility mode (default is XQuery mode)</dd>
<dt><code>-s</code></dt>
<dd> Parse XSLT 2.0</dd>
<dt><code>-f</code></dt>
<dd> Parse using W3C Full-Text extensions</dd>
<dt><code>-u</code></dt>
<dd> Parse using W3C Update extensions</dd>
<dt><code>-e</code></dt>
<dd> Parse using XQilla specific extensions</dd>
<dt><code>-d</code></dt>
<dd> Run the query in interactive debugging mode</dd>
<dt><code>-x</code></dt>
<dd> Use the Xerces-C data model (default is the FastXDM)</dd>
<dt><code>-i</code> <i>file</i></dt>
<dd> Load XML document and bind it as the context item</dd>
<dt><code>-b</code> <i>baseURI</i></dt>
<dd> Set the base URI for the context</dd>
<dt><code>-v</code> <i>name</i> <i>value</i></dt>
<dd> Bind the name value pair as an external variable</dd>
<dt><code>-o</code> <i>file</i></dt>
<dd> Write the result to the specified file</dd>
<dt><code>-n</code> <i>number</i></dt>
<dd> Run the queries a number of times</dd>
<dt><code>-q</code></dt>
<dd> Quiet mode &#8211; no output</dd>
<dt><code>-t</code></dt>
<dd> Output an XML representation of the AST</dd></dl>
<p> The <code>xqilla</code> command line tool can be used to run XQuery and XPath 2 expressions. It is also a good example of how to use the <code>Simple API</code> of the <code>XQilla</code> library.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;<a rel="nofollow" href="https://sourceforge.net/projects/xqilla/support">https://sourceforge.net/projects/xqilla/support</a>&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2008 DecisionSoft Limited.<br/>
 Copyright &#169; 2004-2008 Oracle. </p>
<p> Licensed under the Apache License, Version 2.0 (the &quot;License&quot;); you may not use this file except in compliance with the License. You may obtain a copy of the License at &lt;<a rel="nofollow" href="http://www.apache.org/licenses/LICENSE-2.0">http://www.apache.org/licenses/LICENSE-2.0</a>&gt; </p>
<p> Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an &quot;AS IS&quot; BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for the <code>XQilla library</code> is available at &lt;<a rel="nofollow" href="http://xqilla.sourceforge.net/Documentation">http://xqilla.sourceforge.net/Documentation</a>&gt;. </p>
