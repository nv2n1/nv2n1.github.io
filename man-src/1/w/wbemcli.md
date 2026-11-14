---
title: "wbemcli(1)"
name: "wbemcli"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wbemcli/"
description: "wbemcli – independent command line CIM Client"
---

<h2 class="name">NAME</h2>
<p> wbemcli &#8211; independent command line CIM Client </p>
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
<dt>The <i>objectPath</i> should be enclosed in single quotes so that double quoted</p>
<dd> strings are perserved by the command line shell. Refer to the examples section.</p>
<dt>The only scheme supported is http. Example:</p>
<dd> <code> <a rel="nofollow" href="http://krz:xyz@localhost:5988/root/cimv2:rpm_package.name=glibc">http://krz:xyz@localhost:5988/root/cimv2:rpm_package.name=glibc</a></code></dl>
<p> The <i>prop=value[,&#8230;]</i> parameter is used to specify &lt;Property&gt;=&lt;Value&gt; pairs for the ci, mi and sp operations. Only one &lt;Property&gt;=&lt;Value&gt; pair must be specified for the sp operation.</p>
<dl>
<dt>Example:</p>
<dd> <code>stringProp=a string,booleanProp=true,numericProp=25</code></p>
<dt>Arrays of property values are supported by specifying additional values</p>
<dd> separated by commas</p>
<dt>Example:</p>
<dd> <code>stringProp=a string,another string,numericProp=25,49,12</code></dl>
<p> The <i>prop[,&#8230;]</i> parameter specifies the properties to be returned. One <i>prop</i> must be specified for the gp operation. For other operations this parameter is optional, if none are specified all properties will be returned.</p>
<dl>
<dt>Example:</p>
<dd> <code>stringProp,booleanProp,numericProp</code></dl>
<p> The <i>method[.param=value[,&#8230;]</i> parameter is used to specify &lt;Parameter&gt;=&lt;Value&gt; pairs for the cm operation.</p>
<dl>
<dt>Example:</p>
<dd> <code>Method2Execute.stringParam=a string,booleanParam=true,numericParam=25</code></p>
<dt>Arrays of property values are supported by specifying additional values</p>
<dd> separated by commas</p>
<dt>Example:</p>
<dd> <code>Method2Execute.stringParam=a string,another string,numericParam=25,49,12</code></dl>
<h2>OPERATIONS:</h2>
<p> Supported operations are:</p>
<dl>
<dt><code>gc</code></p>
<dd> get class</p>
<dt><code>gcd</code></p>
<dd> get class definition</p>
<dt><code>dc</code></p>
<dd> delete class</p>
<dt><code>ec</code></p>
<dd> enumerate classes</p>
<dt><code>ecn</code></p>
<dd> enumerate class names</p>
<dt><code>gi</code></p>
<dd> get instance</p>
<dt><code>ci</code></p>
<dd> create instance</p>
<dt><code>mi</code></p>
<dd> modify instance</p>
<dt><code>di</code></p>
<dd> delete instance</p>
<dt><code>ei</code></p>
<dd> enumerate instances</p>
<dt><code>ein</code></p>
<dd> enumerate instance names</p>
<dt><code>ai</code></p>
<dd> enumerate association instances</p>
<dt><code>ain</code></p>
<dd> enumerate association instance names</p>
<dt><code>ri</code></p>
<dd> enumerate reference instances</p>
<dt><code>rin</code></p>
<dd> enumerate reference instance names</p>
<dt><code>gp</code></p>
<dd> get property</p>
<dt><code>sp</code></p>
<dd> set property</p>
<dt><code>cm</code></p>
<dd> call method</p>
<dt><code>cmx</code></p>
<dd> call method (return XML)</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> Print a help message</p>
<dt><code>-nl</code></p>
<dd> Start a new line for every property returned</p>
<dt><code>-t</code></p>
<dd> Append array ([]), reference (&amp;) and key property (#) indicators to property names</p>
<dt><code>-cte</code></p>
<dd> Enable support for chunked responses from CIMOM</p>
<dt><code>-v</code></p>
<dd> Show version information</p>
<dt><code>-dx</code></p>
<dd> Show XML messages payload as received from CIMOM</p>
<dt><code>-dr</code></p>
<dd> Delineate references with { } pairs</p>
<dt><code>-noverify</code></p>
<dd> Do not verify the server certificate for https URLs (useful for testing)</p>
<dt><code>-cacert</code></p>
<dd> CA certificate file (required for https URLS unless -noverify is specified)</p>
<dt><code>-clientcert</code></p>
<dd> Client certificate file (if the CIM server requires client certificates)</p>
<dt><code>-clientkey</code></p>
<dd> Client private key file (required if -clientcert is specified)</p>
<dt><code>-ac</code></p>
<dd> association class name (ai, ain only)</p>
<dt><code>-arc</code></p>
<dd> result class name (ai, ain, rin, ri only)</p>
<dt><code>-ar</code></p>
<dd> role name (ai, ain, rin, ri only)</p>
<dt><code>-arr</code></p>
<dd> result role name (ai, ain only)</dl>
<h2>LIBRARIES</h2>
<p> <code>wbemcli</code> requires either libghttp, libwww, or winhttp, depending on build options used.</p>
<h2>Example</h2>
<p> To get all instances of rpm_packages, i.e. all installed rpm packages on the local system, the following command can be used:</p>
<dl>
<dt>
<dd> <code>wbemcli ei &#8216;<a rel="nofollow" href="http://localhost:5988/root/cimv2:rpm_package'">http://localhost:5988/root/cimv2:rpm_package&#8217;</a></code></dl>
<p> The get instance operation can be specified to get more information about a certain package:</p>
<dl>
<dt>
<dd> <code>wbemcli gi &#8216;<a rel="nofollow" href="http://localhost:5988/root/cimv2:rpm_package.name=glibc'">http://localhost:5988/root/cimv2:rpm_package.name=glibc&#8217;</a></code> The create instance (ci) operation can be called using the following format example. Property values can also be specified/add to the sytax.</p>
<dt>
<dd> <code>wbemcli ci &#8216;<a rel="nofollow" href="http://localhost:5988/root/cimv2:TST_InstanceProperties.CreationClassName=TST_InstanceProperties,Id=Instance">http://localhost:5988/root/cimv2:TST_InstanceProperties.CreationClassName=TST_InstanceProperties,Id=Instance</a> #2&#8242; &#8216;CreationClassName=TST_InstanceProperties,Id=Instance #2,Property_string2=This is instance#2,Property_uint8=250&#8217;</code></p>
<dt>
<dd> More command line examples can be found from the wbemcli/samples directory.</p>
<dt>
<dd></dl>
<h2>Host indirection support</h2>
<p> The scheme and host specification in the object path can be replaced by an arbitrary token that will be used to locate the proper scheme and host specification in ./wbemcli.ind or any file specified via the WBEMCLI_IND environment variable. The format of this file is as follows:</p>
<dl>
<dt><code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;token&gt;: &lt;scheme&gt;://[user:pwd@]&lt;host&gt;:&lt;port&gt;</code></p>
<dd>
<dt>Assuming the following entry in ./wbemcli.ind:</p>
<dd>
<dt><code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>myCimom: <a rel="nofollow" href="http://localhost:5988">http://localhost:5988</a></code></p>
<dd>
<dt>The example in the previous section can then be specified as:</p>
<dd>
<dt>
<dd> <code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>wbemcli gi &#8216;myCimom/root/cimv2:rpm_package.name=&quot;glibc&quot;&#8217;</code></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>WBEMCLI_CURL_SSLVERSION</code></p>
<dd> Specifies the SSL protocol that will be used. Valid values are SSLv2, SSLv3, TLSv1, TLSv1.0 (TLSv1_0), TLSv1.1 (TLSv1_1) or TLSv1.2 (TLSv1_2). If this variable is not set, wbemcli will attempt to figure out the remote SSL protocol version.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/Pegasus/client.pem</i></p>
<dd> The default CA certificate file. Can be overriden with -cacert.</dl>
<h2>AUTHOR</h2>
<p> Adrian Schuur &lt;schuur [at] de.ibm.com&gt;</p>
<h2>BUGS</h2>
<p> The SBLIM project maintains a mailing list to which you should direct all questions regarding sfcb, sfcc, wbemcli, or any of the SBLIM providers. To subscribe to this mailing list visit</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://lists.sourceforge.net/lists/listinfo/sblim-issues">http://lists.sourceforge.net/lists/listinfo/sblim-issues</a></dl>
<p> The SBLIM Project Bug tracking page can be found at</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://sourceforge.net/tracker/?group_id=128809">http://sourceforge.net/tracker/?group_id=128809</a>&amp;atid=712784</dl>
<h2>COPYRIGHT</h2>
<p> (C) Copyright IBM Corp. 2002, 2004, 2005, 2009</p>
<h2>AVAILABILITY</h2>
<p> wbemcli is a part of the SBLIM project. The most recent version is available on the web at</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://sblim.sourceforge.net/">http://sblim.sourceforge.net/</a></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cimserver/">cimserver</a></code>(1) </p>
<h2>Index</h2>
