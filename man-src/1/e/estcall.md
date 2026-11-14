---
title: "estcall(1)"
name: "estcall"
section: "1"
letter: "e"
url: "/docs/linux/man/1-estcall/"
description: "estcall – command line interface of the node API"
---

<h2 class="name">NAME</h2>
<p> estcall &#8211; command line interface of the node API</p>
<h2>SYNOPSIS</h2>
<p> <code>estcall put [-proxy host port] [-tout num] [-auth user pass] nurl [file]</code> </p>
<p> <code>estcall out [-proxy host port] [-tout num] [-auth user pass] nurl expr</code> </p>
<p> <code>estcall edit [-proxy host port] [-tout num] [-auth user pass] nurl expr name [value]</code> </p>
<p> <code>estcall get [-proxy host port] [-tout num] [-auth user pass] nurl expr [attr]</code> </p>
<p> <code>estcall etch [-proxy host port] [-tout num] [-auth user pass] nurl expr</code> </p>
<p> <code>estcall uriid [-proxy host port] [-tout num] [-auth user pass] nurl uri</code> </p>
<p> <code>estcall inform [-proxy host port] [-tout num] [-auth user pass] [-ia|-iu|-il] nurl</code> </p>
<p> <code>estcall sync [-proxy host port] [-tout num] [-auth user pass] nurl</code> </p>
<p> <code>estcall optimize [-proxy host port] [-tout num] [-auth user pass] nurl</code> </p>
<p> <code>estcall search [-proxy host port] [-tout num] [-auth user pass] [-vx] [-kw] [-ec] [-sf] [-attr expr] [-ord expr] [-max num] [-sk num] [-aux num] [-dis name] [-dpt num] [-mask num] nurl [phrase]</code> </p>
<p> <code>estcall setuser [-proxy host port] [-tout num] [-auth user pass] nurl name mode</code> </p>
<p> <code>estcall setlink [-proxy host port] [-tout num] [-auth user pass] nurl url label credit</code> </p>
<p> <code>estcall raw [-proxy host port] [-tout num] [-auth user pass] [-np] [-eh expr] url [file]</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>estcall</code> is an aggregation of sub commands. The name of a sub command is specified by the first argument. Other arguments are parsed according to each sub command. The argument <i>nurl</i> specifies the URL of a node. The option <code>-proxy</code> specifies the host name and the port number of a proxy server. The option <code>-tout</code> specifies timeout in seconds. The option <code>-auth</code> specifies the user name and the password of authentication information.</p>
<dl>
<dt><code>estcall put [-proxy host port] [-tout num] [-auth user pass] nurl [file]</code></p>
<dd> Register a document of document draft to a node.<br />
 <i>file</i> specifies a target file. If it is omitted, the standard input is read.</p>
<dt><code>estcall out [-proxy host port] [-tout num] [-auth user pass] nurl expr</code></p>
<dd> Remove information of a document from a node.<br />
 <i>expr</i> specifies the ID number or the URI of a document.</p>
<dt><code>estcall edit [-proxy host port] [-tout num] [-auth user pass] nurl expr name [value]</code></p>
<dd> Edit an attribute of a document in a node.<br />
 <i>expr</i> specifies the ID number or the URI of a document.<br />
 <i>name</i> specifies the name of an attribute.<br />
 <i>value</i> specifies the value of the attribute. If it is omitted, the attribute is removed.</p>
<dt><code>estcall get [-proxy host port] [-tout num] [-auth user pass] nurl expr [attr]</code></p>
<dd> Output document draft of a document in a node.<br />
 <i>expr</i> specifies the ID number or the URI of a document.<br />
 If <i>attr</i> is specified, only the value of the attribute is output.</p>
<dt><code>estcall etch [-proxy host port] [-tout num] [-auth user pass] nurl expr</code></p>
<dd> Output TSV of keywords and their scores of a document in a node.<br />
 <i>expr</i> specifies the ID number or the URI of a document.</p>
<dt><code>estcall uriid [-proxy host port] [-tout num] [-auth user pass] nurl uri</code></p>
<dd> Output the ID number of a document specified by URI.<br />
 <i>uri</i> specifies the URI of a document.</p>
<dt><code>estcall inform [-proxy host port] [-tout num] [-auth user pass] [-ia|-iu|-il] nurl</code></p>
<dd> Output the name, the label, the number of documents, the number of unique words, and the cache usage of a node.<br />
 If <code>-ia</code> is specified, names of administrators are output.<br />
 If <code>-iu</code> is specified, names of users are output.<br />
 If <code>-il</code> is specified, expressions of links are output.</p>
<dt><code>estcall sync [-proxy host port] [-tout num] [-auth user pass] nurl</code></p>
<dd> Synchronize updating contents of the database of a node.</p>
<dt><code>estcall optimize [-proxy host port] [-tout num] [-auth user pass] nurl</code></p>
<dd> Optimize the database of a node.</p>
<dt><code>estcall search [-proxy host port] [-tout num] [-auth user pass] [-vx] [-kw] [-ec] [-sf] [-attr expr] [-ord expr] [-max num] [-sk num] [-aux num] [-dis name] [-dpt num] [-mask num] nurl [phrase]</code></p>
<dd> Search a node for documents.<br />
 <i>phrase</i> specifies the search phrase.<br />
 If <code>-vx</code> is specified, XML including including attributes and snippets is output.<br />
 If <code>-kw</code> is specified, keyword vectors are retrieved.<br />
 <code>-ec</code> specifies lower limit of similarity eclipse.<br />
 If <code>-sf</code> is specified, the phrase is treated as a simplified form.<br />
 <code>-attr</code> specifies an attribute search condition. This option can be specified multiple times.<br />
 <code>-ord</code> specifies the order expression. By default, it is descending by score.<br />
 <code>-max</code> specifies the maximum number of show documents. Negative means unlimited. By default, it is 10.<br />
 <code>-sk</code> specifies the number of documents to be skipped. By default, it is 0.<br />
 <code>-aux</code> specifies permission to adopt result of the auxiliary index. If it is not more than 0, the auxiliary index is not used. By default, it is 32.<br />
 <code>-dis</code> specifies the name of the distinct attribute.<br />
 <code>-dpt</code> specifies the depth of meta search. by default it is 0.<br />
 <code>-mask</code> specifies the mask of meta search. by default it is 0.</p>
<dt><code>estcall setuser [-proxy host port] [-tout num] [-auth user pass] nurl name mode</code></p>
<dd> Set permission of a user.<br />
 <i>name</i> specifies the name of a user.<br />
 <i>mode</i> specifies operation mode. 1 means to set the user as an administrator, 2 means to set the user as a guest, and 0 means to revoke the user account.</p>
<dt><code>estcall setlink [-proxy host port] [-tout num] [-auth user pass] nurl url label credit</code></p>
<dd> Set a link to another node.<br />
 <i>url</i> specifies the URL of a destination node.<br />
 <i>label</i> specifies the label of the link.<br />
 <i>credit</i> specifies the credit of the link. If the value is negative, the link is removed.</p>
<dt><code>estcall raw [-proxy host port] [-tout num] [-auth user pass] [-np] [-eh expr] url [file]</code></p>
<dd> Output response of an HTTP request.<br />
 <i>url</i> specifies the URL of a target.<br />
 If <i>file</i> is specified, the content is sent by POST method. If not, GET method is used. If &quot;-&quot; is specified, the standard input is read.<br />
 If <code>-np</code> is specified, output response headers also.<br />
 <code>-eh</code> specifies an additional HTTP header. By default, &quot;Host&quot;, &quot;Connection&quot;, &quot;User-Agent&quot;, and &quot;Content-Length&quot; is added.</dl>
<p> All sub commands return 0 if the operation is success, else return 1. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-estconfig/">estconfig</a></code>(1), <code><a href="/docs/linux/man/1-estcmd/">estcmd</a></code>(1), <code><a href="/docs/linux/man/1-estmaster/">estmaster</a></code>(1), <code><a href="/docs/linux/man/1-estwaver/">estwaver</a></code>(1), <code><a href="/docs/linux/man/3-estraier/">estraier</a></code>(3), <code><a href="/docs/linux/man/3-estnode/">estnode</a></code>(3) </p>
<p> Please see <code><a rel="nofollow" href="http://hyperestraier.sourceforge.net/nguide-en.html">http://hyperestraier.sourceforge.net/nguide-en.html</a></code> for detail. </p>
<h2>Index</h2>
