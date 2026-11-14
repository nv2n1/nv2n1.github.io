---
title: "cimsub(1)"
name: "cimsub"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cimsub/"
description: "cimsub – list, enable, disable,remove or create CIM indication subscriptions"
---

<h2>NAME</h2>
<p> cimsub &#8211; list, enable, disable,remove or create CIM indication subscriptions</p>
<h2>SYNOPSIS</h2>
<p> <code>cimsub</code> <code>-l</code> <code>s</code>|<code>f</code>|fB-v][<code>-n</code> namespace][<code>-F</code> [fnamespace:]filtername][<code>-H</code> [hnamespace:][hclassname.]handlername] </p>
<p> <code>cimsub</code> <code>-e</code> [<code>-n</code> namespace] <code>-F</code> [fnamespace:]filtername <code>-H</code> [hnamespace:][hclassname.]handlername </p>
<p> <code>cimsub</code> <code>-d</code> [<code>-n</code> namespace] <code>-F</code> [fnamespace:]filtername <code>-H</code> [hnamespace:][hclassname.]handlername </p>
<p> <code>cimsub</code> <code>-r</code> <code>s</code>|<code>f</code>|fBa [<code>-n</code> namespace][<code>-F</code> [fnamespace:]filtername][<code>-H</code> [hnamespace:][hclassname.]handlername] </p>
<p> <code>cimsub</code> <code>-c</code> <code>f</code> [fnamespace:]filtername <code>-Q</code> query [<code>-L</code> querylanguage] [<code>-N</code> sourcenamespace(s)] </p>
<p> <code>cimsub</code> <code>-c</code> <code>h</code> [hnamespace:][hclassname.]handlername [<code>-D</code> destination]|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>-M</code>&nbsp;<wbr>mailto&nbsp;<wbr>[<code>-C</code>&nbsp;<wbr>mailcc]&nbsp;<wbr><code>-S</code>&nbsp;<wbr>mailsubject]|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>-T</code>&nbsp;<wbr>snmptargethost&nbsp;<wbr>[<code>-P</code>&nbsp;<wbr>snmpportnumber]&nbsp;<wbr><code>-V</code>&nbsp;<wbr>snmpversion]&nbsp;<wbr>[<code>-U</code>&nbsp;<wbr>snmpsecurityname]&nbsp;<wbr>[<code>-E</code>&nbsp;<wbr>snmpengineid]] </p>
<p> <code>cimsub</code> <code>-c</code> <code>s</code> [<code>-n</code> namespace] <code>-F</code> [fnamespace:]filtername <code>-H</code> [hnamespace:][hclassname.]handlername </p>
<p> <code>cimsub</code> <code>&#8211;help</code> </p>
<p> <code>cimsub</code> <code>&#8211;version</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>cimsub </code> command provides a command line interface to manage CIM indication subscriptions on the local CIM Server. </p>
<p> The first form of <code>cimsub </code> lists all or selected indication subscriptions, filters, or handlers, and displays the requested information about the instance(s). </p>
<p> The second form of <code>cimsub </code> enables the specified subscription, i.e. the subscription instance is modified to set the value of the SubscriptionState property to Enabled. When a subscription is enabled, the CIM Server attempts to process the subscription if at least one provider is available to serve the subscription. </p>
<p> The third form of <code>cimsub </code> disables the specified subscription, i.e. the subscription instance is modified to set the value of the SubscriptionState property to Disabled. When a subscription is disabled, the CIM Server does not attempt to process the subscription, regardless of whether any providers are available to serve the subscription. </p>
<p> The fourth form of <code>cimsub </code> removes the specified subscription, filter, handler, or subscription and its referenced filter and handler, i.e. each instance is deleted from the repository, and the CIM Server will no longer have any information about the instance(s). A filter or handler may not be removed if it is referenced by any other subscription. </p>
<p> The fifth form of <code>cimsub</code> command creates the specified Subscription, filter, or handler. i.e each instance is created into the repository and CIM Server will get the new information about the created Instance(s). </p>
<h3>Options</h3>
<p> The <code>cimsub </code> command recognizes the following options:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-l</code></p>
<dd> List and display information about all or selected indication subscriptions (&quot;s&quot;), filters (&quot;f&quot;), or handlers (&quot;h&quot;). It is an error to specify the -F option with -lh. It is an error to specify the -H option with -lf. With the -lf or -lh option, fnamespace or hnamespace takes precedence over the -n namespace option if both are specified.</p>
<dt><code>-e</code></p>
<dd> Enable the specified subscription (set the SubscriptionState to Enabled).</p>
<dt><code>-d</code></p>
<dd> Disable the specified subscription (set the SubscriptionState to Disabled).</p>
<dt><code>-r</code></p>
<dd> Remove the specified subscription (&quot;s&quot;), filter (&quot;f&quot;), handler (&quot;h&quot;), or subscription and its referenced filter and handler (&quot;a&quot;) (delete the instance(s) from the repository). The -F and -H options are required with -rs or -ra. It is an error to specify the -F option with -rh. It is an error to specify the -H option with -rf. With the -rf or -rh option, fnamespace or hnamespace takes precedence over the -n namespace option if both are specified.</p>
<dt><code>-c</code></p>
<dd> Create the specified subscription (&quot;s&quot;), filter (&quot;f&quot;) or handler (&quot;h&quot;). The -F filter and -H handler options are required with -cs. The Filtername and -Q Query are required with -cf. The Handler Name is required with -ch.With the -cf or -ch option, fnamespace or hnamespace takes precedence over the -n namespace option if both are specified.</p>
<dt><code>-v</code></p>
<dd> Include verbose information in the information displayed for each listed instance.</p>
<dt><code>-n </code><i>namespace</i></p>
<dd> Specify the namespace. For the -l forms of the command, if no namespace is specified, instances in all namespaces are listed. For all other forms of the command, if no namespace is specified, the command operates on an instance in the namespace root/PG_InterOp.</p>
<dt><code>-F </code><i>[fnamespace:]filtername</i></p>
<dd> Specify the Filter Name. Omission of the filter namespace specifies that it is the same as that of the subscription.</p>
<dt><code>-H </code><i>[hnamespace:][classname.]handlername</i></p>
<dd> Specify the Handler Name. Omission of the handler namespace specifies that it is the same as that of the subscription. Omission of the handler classname specifies that it is CIM_ListenerDestinationCIMXML.</p>
<dt><code>-Q</code></p>
<dd> Specify the Query Expression for the Filter.</p>
<dt><code>-L</code></p>
<dd> Specify the Query Language for the Filter.</p>
<dt><code>-N</code></p>
<dd> To Use SourceNamespaces property, Specify multiple SourceNamespaces with coma separated or append comma to the single SourceNamespace. By default SourceNamespace property is populated if the single SourceNamespace is specified.</p>
<dt><code>-D </code></p>
<dd> Specify Destination of a CIM_IndicationHandlerCIMXML Handler. Required option for CIM_IndicationHandlerCIMXML or CIM_ListenerDestinationCIMXML Handler.</p>
<dt><code>-M </code></p>
<dd> Specify Mailto of a PG_ListenerDestinationEmail Handler.</p>
<dt><code>-C </code></p>
<dd> Specify Mailcc of a PG_ListenerDestinationEmail Handler.</p>
<dt><code>-S </code></p>
<dd> Specify Subject of a PG_ListenerDestinationEmail Handler.</p>
<dt><code>-T </code></p>
<dd> Specify Target Host of PG_IndicationHandlerSNMPMapper Handler. Required option for SNMPMapper handler.</p>
<dt><code>-U </code></p>
<dd> Specify Security Name of PG_IndicationHandlerSNMPMapper Handler.</p>
<dt><code>-P </code></p>
<dd> Specify Port Number of a PG_IndicationHandlerSNMPMapper Handler.(default 162)</p>
<dt><code>-V </code></p>
<dd> Specify SNMPVersion of a PG_IndicationHandlerSNMPMapper Handler.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2 : SNMPv1 Trap<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>3 : SNMPv2C Trap<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>4 : SNMPv2C Inform<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>5 : SNMPv3 Trap<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>6 : SNMPv3 Inform<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Required option for SNMPMapper Handler</p>
<dt><code>-E </code></p>
<dd> Specify Engine ID of a PG_IndicationHandlerSNMPMapper Handler.</p>
<dt><code>&#8211;help</code></p>
<dd> Display command usage information.</p>
<dt><code>&#8211;version</code></p>
<dd> Display the CIM Server version.</dl>
</dl>
<h2>EXIT STATUS</h2>
<p> When an error occurs, an error message is written to stderr and an error value is returned. The following return values are returned:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>0</code></p>
<dd> Successful completion</p>
<dt><code>1</code></p>
<dd> General error</p>
<dt><code>2</code></p>
<dd> Connection failed</p>
<dt><code>3</code></p>
<dd> Connection timed out</p>
<dt><code>4</code></p>
<dd> Access was denied</p>
<dt><code>5</code></p>
<dd> Namespace does not exist</p>
<dt><code>6</code></p>
<dd> Object could not be found</p>
<dt><code>7</code></p>
<dd> Operation is not supported</dl>
</dl>
<h2>USAGE NOTES</h2>
<p> The <code>cimsub </code> command requires the CIM Server to be running. </p>
<p> If the enableSubscriptionsForNonprivilegedUsers configuration property is set to false, only a privileged user may list, enable, disable, remove or create a subscription, filter, or handler. If the enableSubscriptionsForNonprivilegedUsers configuration property is set to true, even a non privileged user or the instance creator may enable, disable, remove or create a subscription, filter or handler. </p>
<p> Caution should be used when specifying the -r option, since subscriptions, filters or handlers removed may not be easily re-created, and may not be re-created using this command.</p>
<h2>EXAMPLES</h2>
<p> List all indication subscriptions in all namespaces on the local CIM Server:</p>
<dl>
<dt>
<dd> <code>cimsub -ls</code></dl>
<p> List all indication subscriptions referencing the Filter with Name &#8216;TestFilter&#8217; in all namespaces on the local CIM Server:</p>
<dl>
<dt>
<dd> <code>cimsub -ls -F TestFilter</code></dl>
<p> List all indication subscriptions referencing the CIM_ListenerDestinationCIMXML Handler with Name &#8216;TestHandler&#8217; in all namespaces on the local CIM Server:</p>
<dl>
<dt>
<dd> <code>cimsub -ls -H TestHandler</code></dl>
<p> List all indication subscriptions in the root/cimv2 namespace on the local CIM Server, including subscription state, filter query and handler destination (verbose listing output):</p>
<dl>
<dt>
<dd> <code>cimsub -ls -v -n root/cimv2</code></dl>
<p> Display information about the subscription referencing Filter with Name &#8216;TestFilter&#8217; and referencing CIM_ListenerDestinationCIMXML Handler with Name &#8216;TestHandler&#8217; (all in namespace root/PG_InterOp), including subscription state, filter query and handler destination (verbose listing output):</p>
<dl>
<dt>
<dd> <code>cimsub -ls -v -n root/PG_InterOp -F TestFilter -H TestHandler </code></dl>
<p> Display information about the Filter with Name &#8216;TestFilter&#8217; in the root/cimv2 namespace (verbose listing output):</p>
<dl>
<dt>
<dd> <code>cimsub -lf -v -F root/cimv2:TestFilter</code></dl>
<p> List all handlers in all namespaces on the local CIM Server:</p>
<dl>
<dt>
<dd> <code>cimsub -lh</code></dl>
<p> Enable the subscription referencing Filter with Name &#8216;TestFilter&#8217; and referencing CIM_ListenerDestinationCIMXML Handler with Name &#8216;TestHandler&#8217; (all in namespace root/PG_InterOp):</p>
<dl>
<dt>
<dd> <code>cimsub -e -F TestFilter -H TestHandler</code></dl>
<p> Disable the subscription in namespace root/cimv2, referencing Filter with Name &#8216;TestFilter&#8217; in namespace test1/cimv2, and referencing PG_ListenerDestinationSystemLog Handler with Name &#8216;TestHandler&#8217; in namespace test2/cimv2:</p>
<dl>
<dt>
<dd> <code>cimsub -d -n root/cimv2 -F test1/cimv2:TestFilter -H test2/cimv2:PG_ListenerDestinationSystemLog.TestHandler</code></dl>
<p> Remove the subscription referencing Filter with Name &#8216;TestFilter&#8217;, and referencing CIM_ListenerDestinationCIMXML Handler with Name &#8216;TestHandler&#8217; (all in namespace root/cimv2), also removing the filter and handler instances (if not referenced by any other subscription):</p>
<dl>
<dt>
<dd> <code>cimsub -ra -n root/cimv2 -F TestFilter -H TestHandler</code></dl>
<p> Create filter with Name &#8216;filteraa&#8217; with the Query &#8216;select * from IndicationStressTestClass&#8217; with SourceNamespaces test/TestProvider and test/testIndSrcNS1.</p>
<dl>
<dt>
<dd> <code>cimsub -c f filteraa -Q select * from IndicationStressTestClass -N test/TestProvider,test/testIndSrcNS1</code></dl>
<p> Create handler with Name &#8216;handler01&#8217; and Destination &#8216;/Pegasus_IndicationStressTestConsumer&#8217;.</p>
<dl>
<dt>
<dd> <code>cimsub -c h handler01 -D /Pegasus_IndicationStressTestConsumer</code></dl>
<p> Create Subscription with referencing Filter with Name &#8216;TestFilter&#8217;, and referencing CIM_ListenerDestinationCIMXML Handler with Name &#8216;TestHandler&#8217;</p>
<dl>
<dt>
<dd> <code>cimsub -c s -F filteraa -H handler01 </code></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cimserver/">cimserver</a>(1), <a href="//www.systutorials.com/docs/linux/man/1M-cimconfig/">cimconfig</a>(1M). </p>
<h2>Index</h2>
