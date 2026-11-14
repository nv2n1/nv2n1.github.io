---
title: "radius(5)"
name: "radius"
section: "5"
letter: "r"
url: "/docs/linux/man/5-radius/"
---

radius.conf - Configuration for nnrpd RADIUS authenticator

<h2>Description</h2>

This describes the format and attributes of the configuration file for the nnrpd <font SIZE="-1">RADIUS</font> authenticator. See <i><a HREF="/docs/linux/man/1-radius/">radius</a></i>(1) for more information about the authenticator program. The default location for this file is <i>radius.conf</i> in <i>pathetc</i>. 

 Blank lines and lines beginning with <tt>&quot;#&quot;</tt> are ignored, as is anything after a <tt>&quot;#&quot;</tt> on a line. All other lines should begin with a parameter name followed by a colon and the value of that key, except that each section of configuration for a particular server should be enclosed in: 

 <pre> server &lt;name&gt; {
 # parameters...
 }</pre>where &lt;name&gt; is just some convenient label for that server. 

 The available parameters are:
<dl><dt><i>radhost</i>
<dd>The hostname of the <font SIZE="-1">RADIUS</font> server to use for authentication. This parameter must be set.
<dt><i>radport</i>
<dd>The port to query on the <font SIZE="-1">RADIUS</font> server. Defaults to 1645 if not set.
<dt><i>lochost</i>
<dd>The hostname or <font SIZE="-1">IP</font> address making the request. The <font SIZE="-1">RADIUS</font> server expects an <font SIZE="-1">IP</font> address; a hostname will be translated into an <font SIZE="-1">IP</font> address with <i>gethostbyname()</i>. If not given, this information isn't included in the request (not all <font SIZE="-1">RADIUS</font> setups require this information).
<dt><i>locport</i>
<dd>The port the client being authenticated is connecting to. If not given, defaults to 119. This doesn't need to be set unless readers are connecting to a non-standard port.
<dt><i>secret</i>
<dd>The shared secret with the <font SIZE="-1">RADIUS</font> server. If your secret includes spaces, tabs, or <tt>&quot;#&quot;</tt>, be sure to include it in double quotes. This parameter must be set.
<dt><i>prefix</i>
<dd>Prepend the value of this parameter to all usernames before passing them to the <font SIZE="-1">RADIUS</font> server. Can be used to prepend something like <tt>&quot;news-&quot;</tt> to all usernames in order to put news users into a different namespace from other accounts served by the same server. If not set, nothing is prepended.
<dt><i>suffix</i>
<dd>Append the value of this parameter to all usernames before passing them to the <font SIZE="-1">RADIUS</font> server. This is often something like <tt>&quot;@example.com&quot;</tt>, depending on how your <font SIZE="-1">RADIUS</font> server is set up. If not set, nothing is appended.
<dt><i>ignore-source</i>
<dd>Can be set to <tt>&quot;true&quot;</tt> or <tt>&quot;false&quot;</tt>. If set to false, the <font SIZE="-1">RADIUS</font> authenticator will check to ensure that the response it receives is from the same <font SIZE="-1">IP</font> address as it sent the request to (for some added security). If set to true, it will skip this verification check (if your <font SIZE="-1">RADIUS</font> server has multiple <font SIZE="-1">IP</font> addresses or if other odd things are going on, it may be perfectly normal for the response to come from a different <font SIZE="-1">IP</font> address).</dl>

<h2>Example</h2>

Here is a configuration for a news server named news.example.com, authenticating users against radius.example.com and appending <tt>&quot;@example.com&quot;</tt> to all client-supplied usernames before passing them to the <font SIZE="-1">RADIUS</font> server: 

 <pre> server example {
 radhost: radius.example.com
 lochost: news.example.com
 secret: IamARADIUSsecRET
 suffix: @example.com
 }</pre>The shared secret with the <font SIZE="-1">RADIUS</font> server is <tt>&quot;IamARADIUSsecRET&quot;</tt>.

<h2>History</h2>

This documentation was written by Russ Allbery &lt;rra [at] stanford.edu&gt; based on the comments in the sample <i>radius.conf</i> file by Yury B. Razbegin. 

 $Id: radius.conf.pod 8200 2008-11-30 13:31:30Z iulius $

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/1-radius/">radius</a></i>(1) 
