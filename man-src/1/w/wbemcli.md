---
title: "wbemcli(1)"
name: "wbemcli"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wbemcli/"
description: "wbemcli – independent command line CIM Client"
---

<h2>SYNOPSIS</h2>
<p> <code>wbemcli</code> <code>gc|gcd|dc|ec|ecn|gi|ci|mi|di|ei|ein|ai|ain|ri|rin|gp|sp|cm|cmx</code> [<code>-nl</code>] [<code>-h</code>] [<code>-t</code>] [<code>-cte]</code> [<code>-dx</code>] [<code>-dr</code>] [<code>-noverify</code>] [<code>-cacert</code>&nbsp;<wbr>file] [<code>-clientcert</code>&nbsp;<wbr>file] [<code>-clientkey</code>&nbsp;<wbr>file] [<code>-ac</code><i>&nbsp;<wbr>assocClass</i>] [<code>-arc</code><i>&nbsp;<wbr>resultClass</i>] [<code>-ar</code><i>&nbsp;<wbr>role</i>] [<code>-arr</code><i>&nbsp;<wbr>resultRole</i>] <i>objectPath</i> [<i>prop=value[,&#8230;]]</i> [<i>prop[,&#8230;]]</i></p>
<h2>Alternate formats:</h2>
<p> <code>wbemgc </code> [<code>-nl</code>] [<code>-h</code>] [<code>-t</code>] [<code>-dx</code>] [<code>-dr</code>] <i>objectPath</i> [<i>prop[,&#8230;]]</i> </p>
<p> <code>wbemgcd </code> [<code>-nl</code>] [<code>-h</code>] [<code>-t</code>] [<code>-dx</code>] [<code>-dr</code>] <i>objectPath</i> </p>
<p> <code>wbemdc </code> [<code>-nl</code>] [<code>-h</code>] [<code>-t</code>] [<code>-dx</code>] [<code>-dr</code>] <i>objectPath</i> </p>
<p> <code>wbemec </code> [<code>-nl</code>] [<code>-h</code>] [<code>-t</code>] [<code>-cte]</code> [<code>-dx</code>] [<code>-dr</code>] <i>objectPath</i> [<i>prop[,&#8230;]]</i> </p>
<p> <code>wbemecn </code> [<code>-nl</code>] [<code>-h</code>] [<code>-t</code>] [<code>-dx</code>] [<code>-dr</code>] <i>objectPath</i> </p>
<p> <code>wbemgi </code> [<code>-nl</code>] [<code>-h</code>] [<code>-t</code>] [<code>-dx</code>] [<code>-dr</code>] <i>objectPath</i> [<i>prop[,&#8230;]]</i> </p>
<p> <code>wbemci </code> [<code>-nl</code>] [<code>-h</code>] [<code>-t</code>] [<code>-dx</code>] [<code>-dr</code>] <i>objectPath</i> [<i>prop=value[,&#8230;]]</i> </p>
<p> <code>wbemmi </code> [<code>-nl</code>] [<code>-h</code>] [<code>-t</code>] [<code>-dx</code>] [<code>-dr</code>] <i>objectPath</i> [<i>prop=value[,&#8230;]]</i> </p>
<p> <code>wbemdi </code> [<code>-nl</code>] [<code>-h</code>] [<code>-t</code>] [<code>-dx</code>] [<code>-dr</code>] <i>objectPath</i> </p>
<p> <code>wbemei </code> [<code>-nl</code>] [<code>-h</code>] [<code>-t</code>] [<code>-cte]</code> [<code>-dx</code>] [<code>-dr</code>] <i>objectPath</i> [<i>prop[,&#8230;]]</i> </p>
<p> <code>wbemein </code> [<code>-nl</code>] [<code>-h</code>] [<code>-t</code>] [<code>-dx</code>] [<code>-dr</code>] <i>objectPath</i> </p>
<p> <code>wbemai </code> [<code>-nl</code>] [<code>-h</code>] [<code>-t</code>] [<code>-cte]</code> [<code>-dx</code>] [<code>-dr</code>] [<code>-ac</code><i>&nbsp;<wbr>assocClass</i>] [<code>-arc</code><i>&nbsp;<wbr>resultClass</i>] [<code>-ar</code><i>&nbsp;<wbr>role</i>] [<code>-arr</code><i>&nbsp;<wbr>resultRole</i>] <i>objectPath</i> [<i>prop[,&#8230;]]</i> </p>
<p> <code>wbemain </code> [<code>-nl</code>] [<code>-h</code>] [<code>-t</code>] [<code>-dx</code>] [<code>-dr</code>] [<code>-ac</code><i>&nbsp;<wbr>assocClass</i>] [<code>-arc</code><i>&nbsp;<wbr>resultClass</i>] [<code>-ar</code><i>&nbsp;<wbr>role</i>] [<code>-arr</code><i>&nbsp;<wbr>resultRole</i>] <i>objectPath</i> </p>
<p> <code>wbemri </code> [<code>-nl</code>] [<code>-h</code>] [<code>-t</code>] [<code>-cte]</code> [<code>-dx</code>] [<code>-dr</code>] [<code>-arc</code><i>&nbsp;<wbr>resultClass</i>] [<code>-ar</code><i>&nbsp;<wbr>role</i>] <i>objectPath</i> [<i>prop[,&#8230;]]</i> </p>
<p> <code>wbemrin </code> [<code>-nl</code>] [<code>-h</code>] [<code>-t</code>] [<code>-dx</code>] [<code>-dr</code>] [<code>-arc</code><i>&nbsp;<wbr>resultClass</i>] [<code>-ar</code><i>&nbsp;<wbr>role</i>] <i>objectPath</i> </p>
<p> <code>wbemgp </code> [<code>-nl</code>] [<code>-h</code>] [<code>-t</code>] [<code>-dx</code>] [<code>-dr</code>] <i>objectPath</i> <i>prop</i> </p>
<p> <code>wbemsp </code> [<code>-nl</code>] [<code>-h</code>] [<code>-t</code>] [<code>-dx</code>] [<code>-dr</code>] <i>objectPath</i> <i>prop=value</i> </p>
<p> <code>wbemcm </code> [<code>-nl</code>] [<code>-h</code>] [<code>-t</code>] [<code>-dx</code>] [<code>-dr</code>] <i>objectPath</i> <i>method[.param=value[,&#8230;]]</i> </p>
<p> <code>wbemcmx </code> [<code>-nl</code>] [<code>-h</code>] [<code>-t</code>] [<code>-dx</code>] [<code>-dr</code>] <i>objectPath</i> <i>method[.param=value[,&#8230;]]</i></p>
<h2>DESCRIPTION</h2>
<p> <i>wbemcli</i> is a command line based CIM Client. It uses one of the <i>gc|gcd|dc|ec|ecn|gi|ci|mi|di|ei|ein|ai|ain|ri|rin|gp|sp|cm|cmx</i> operations and the fully qualified path to the CIM Object to get to the host and execute the specified operation. This implementation is CIMOM library independent and can be used with all WBEM compliant CIMOM implementations. The <i>objectPath</i> parameter is used to locate the CIM object and has the following format: </p>
<p> <code> &lt;scheme&gt;://[user:pwd@]&lt;host&gt;:&lt;port&gt;/&lt;namespace[/..]&gt;:&lt;classname&gt;[.&lt;key=value[,..]&gt;]</code></p>
<dl>
<dt>The <i>objectPath</i> should be enclosed in single quotes so that double quoted</dt>
<dd> strings are perserved by the command line shell. Refer to the examples section.</dd>
<dt>The only scheme supported is http. Example:</dt>
<dd> <code> <a rel="nofollow" href="http://krz:xyz@localhost:5988/root/cimv2:rpm_package.name=glibc">http://krz:xyz@localhost:5988/root/cimv2:rpm_package.name=glibc</a></code></dd></dl>
<p> The <i>prop=value[,&#8230;]</i> parameter is used to specify &lt;Property&gt;=&lt;Value&gt; pairs for the ci, mi and sp operations. Only one &lt;Property&gt;=&lt;Value&gt; pair must be specified for the sp operation.</p>
<dl>
<dt>Example:</dt>
<dd> <code>stringProp=a string,booleanProp=true,numericProp=25</code></dd>
<dt>Arrays of property values are supported by specifying additional values</dt>
<dd> separated by commas</dd>
<dt>Example:</dt>
<dd> <code>stringProp=a string,another string,numericProp=25,49,12</code></dd></dl>
<p> The <i>prop[,&#8230;]</i> parameter specifies the properties to be returned. One <i>prop</i> must be specified for the gp operation. For other operations this parameter is optional, if none are specified all properties will be returned.</p>
<dl>
<dt>Example:</dt>
<dd> <code>stringProp,booleanProp,numericProp</code></dd></dl>
<p> The <i>method[.param=value[,&#8230;]</i> parameter is used to specify &lt;Parameter&gt;=&lt;Value&gt; pairs for the cm operation.</p>
<dl>
<dt>Example:</dt>
<dd> <code>Method2Execute.stringParam=a string,booleanParam=true,numericParam=25</code></dd>
<dt>Arrays of property values are supported by specifying additional values</dt>
<dd> separated by commas</dd>
<dt>Example:</dt>
<dd> <code>Method2Execute.stringParam=a string,another string,numericParam=25,49,12</code></dd></dl>
<h2>OPERATIONS:</h2>
<p> Supported operations are:</p>
<dl>
<dt><code>gc</code></dt>
<dd> get class</dd>
<dt><code>gcd</code></dt>
<dd> get class definition</dd>
<dt><code>dc</code></dt>
<dd> delete class</dd>
<dt><code>ec</code></dt>
<dd> enumerate classes</dd>
<dt><code>ecn</code></dt>
<dd> enumerate class names</dd>
<dt><code>gi</code></dt>
<dd> get instance</dd>
<dt><code>ci</code></dt>
<dd> create instance</dd>
<dt><code>mi</code></dt>
<dd> modify instance</dd>
<dt><code>di</code></dt>
<dd> delete instance</dd>
<dt><code>ei</code></dt>
<dd> enumerate instances</dd>
<dt><code>ein</code></dt>
<dd> enumerate instance names</dd>
<dt><code>ai</code></dt>
<dd> enumerate association instances</dd>
<dt><code>ain</code></dt>
<dd> enumerate association instance names</dd>
<dt><code>ri</code></dt>
<dd> enumerate reference instances</dd>
<dt><code>rin</code></dt>
<dd> enumerate reference instance names</dd>
<dt><code>gp</code></dt>
<dd> get property</dd>
<dt><code>sp</code></dt>
<dd> set property</dd>
<dt><code>cm</code></dt>
<dd> call method</dd>
<dt><code>cmx</code></dt>
<dd> call method (return XML)</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></dt>
<dd> Print a help message</dd>
<dt><code>-nl</code></dt>
<dd> Start a new line for every property returned</dd>
<dt><code>-t</code></dt>
<dd> Append array ([]), reference (&amp;) and key property (#) indicators to property names</dd>
<dt><code>-cte</code></dt>
<dd> Enable support for chunked responses from CIMOM</dd>
<dt><code>-v</code></dt>
<dd> Show version information</dd>
<dt><code>-dx</code></dt>
<dd> Show XML messages payload as received from CIMOM</dd>
<dt><code>-dr</code></dt>
<dd> Delineate references with { } pairs</dd>
<dt><code>-noverify</code></dt>
<dd> Do not verify the server certificate for https URLs (useful for testing)</dd>
<dt><code>-cacert</code></dt>
<dd> CA certificate file (required for https URLS unless -noverify is specified)</dd>
<dt><code>-clientcert</code></dt>
<dd> Client certificate file (if the CIM server requires client certificates)</dd>
<dt><code>-clientkey</code></dt>
<dd> Client private key file (required if -clientcert is specified)</dd>
<dt><code>-ac</code></dt>
<dd> association class name (ai, ain only)</dd>
<dt><code>-arc</code></dt>
<dd> result class name (ai, ain, rin, ri only)</dd>
<dt><code>-ar</code></dt>
<dd> role name (ai, ain, rin, ri only)</dd>
<dt><code>-arr</code></dt>
<dd> result role name (ai, ain only)</dd></dl>
<h2>LIBRARIES</h2>
<p> <code>wbemcli</code> requires either libghttp, libwww, or winhttp, depending on build options used.</p>
<h2>Example</h2>
<p> To get all instances of rpm_packages, i.e. all installed rpm packages on the local system, the following command can be used:</p>
<dl>
<dt>
</dt><dd> <code>wbemcli ei &#8216;<a rel="nofollow" href="http://localhost:5988/root/cimv2:rpm_package'">http://localhost:5988/root/cimv2:rpm_package&#8217;</a></code></dd></dl>
<p> The get instance operation can be specified to get more information about a certain package:</p>
<dl>
<dt>
</dt><dd> <code>wbemcli gi &#8216;<a rel="nofollow" href="http://localhost:5988/root/cimv2:rpm_package.name=glibc'">http://localhost:5988/root/cimv2:rpm_package.name=glibc&#8217;</a></code> The create instance (ci) operation can be called using the following format example. Property values can also be specified/add to the sytax.</dd>
<dt>
</dt><dd> <code>wbemcli ci &#8216;<a rel="nofollow" href="http://localhost:5988/root/cimv2:TST_InstanceProperties.CreationClassName=TST_InstanceProperties,Id=Instance">http://localhost:5988/root/cimv2:TST_InstanceProperties.CreationClassName=TST_InstanceProperties,Id=Instance</a> #2&#8242; &#8216;CreationClassName=TST_InstanceProperties,Id=Instance #2,Property_string2=This is instance#2,Property_uint8=250&#8217;</code></dd>
<dt>
</dt><dd> More command line examples can be found from the wbemcli/samples directory.</dd>
</dl>
<h2>Host indirection support</h2>
<p> The scheme and host specification in the object path can be replaced by an arbitrary token that will be used to locate the proper scheme and host specification in ./wbemcli.ind or any file specified via the WBEMCLI_IND environment variable. The format of this file is as follows:</p>
<dl>
<dt><code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;token&gt;: &lt;scheme&gt;://[user:pwd@]&lt;host&gt;:&lt;port&gt;</code></dt>
<dd>
</dd><dt>Assuming the following entry in ./wbemcli.ind:</dt>
<dd>
</dd><dt><code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>myCimom: <a rel="nofollow" href="http://localhost:5988">http://localhost:5988</a></code></dt>
<dd>
</dd><dt>The example in the previous section can then be specified as:</dt>
<dd>
</dd><dt>
</dt><dd> <code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>wbemcli gi &#8216;myCimom/root/cimv2:rpm_package.name=&quot;glibc&quot;&#8217;</code></dd></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>WBEMCLI_CURL_SSLVERSION</code></dt>
<dd> Specifies the SSL protocol that will be used. Valid values are SSLv2, SSLv3, TLSv1, TLSv1.0 (TLSv1_0), TLSv1.1 (TLSv1_1) or TLSv1.2 (TLSv1_2). If this variable is not set, wbemcli will attempt to figure out the remote SSL protocol version.</dd></dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/Pegasus/client.pem</i></dt>
<dd> The default CA certificate file. Can be overriden with -cacert.</dd></dl>
<h2>AUTHOR</h2>
<p> Adrian Schuur &lt;schuur [at] de.ibm.com&gt;</p>
<h2>BUGS</h2>
<p> The SBLIM project maintains a mailing list to which you should direct all questions regarding sfcb, sfcc, wbemcli, or any of the SBLIM providers. To subscribe to this mailing list visit</p>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://lists.sourceforge.net/lists/listinfo/sblim-issues">http://lists.sourceforge.net/lists/listinfo/sblim-issues</a></dd></dl>
<p> The SBLIM Project Bug tracking page can be found at</p>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://sourceforge.net/tracker/?group_id=128809">http://sourceforge.net/tracker/?group_id=128809</a>&amp;atid=712784</dd></dl>
<h2>COPYRIGHT</h2>
<p> (C) Copyright IBM Corp. 2002, 2004, 2005, 2009</p>
<h2>AVAILABILITY</h2>
<p> wbemcli is a part of the SBLIM project. The most recent version is available on the web at</p>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://sblim.sourceforge.net/">http://sblim.sourceforge.net/</a></dd></dl>
<h2>SEE ALSO</h2>
<p> <code>cimserver</code>(1) </p>
