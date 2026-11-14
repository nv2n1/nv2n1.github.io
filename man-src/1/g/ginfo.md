---
title: "ginfo(1)"
name: "ginfo"
section: "1"
letter: "g"
url: "/docs/linux/man/1-ginfo/"
description: "ginfo – fetch service information"
---

<h2>NAME</h2>
<p> ginfo &#8211; fetch service information</p>
<h2>SYNOPSIS</h2>
<p> ginfo [options] Object [attribute_to_filter=&#8217;value of the attribute&#8217;] [attribute_to_display]</p>
<h2>DESCRIPTION</h2>
<p> List attributes corresponding to an object. By default, all the attributes of an object are displayed.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-H, &#8211;host</code> <i>host</i></p>
<dd> Specify a host to query. By default the environmental variable LCG_GFAL_INFOSYS will be used.</p>
<dt><code>-b, &#8211;bind</code> <i>binding</i></p>
<dd> Specify the binding (o=glue by default).</p>
<dt><code>-l, &#8211;list</code> <i>attribute</i></p>
<dd> List all the possible values of the specified attribute.</p>
<dt><code>-c, &#8211;csv</code></p>
<dd> Output in CSV formating</p>
<dt><code>-j, &#8211;json</code></p>
<dd> Output in JSON formating</p>
<dt><code>-t, &#8211;timeout</code></p>
<dd> Change the ldap timeout (15 seconds by default).</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Enable verbose mode</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Print the version of ginfo</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Print this helpful message</dl>
<h2>OBJECTS AND CORRESPONDING ATTRIBUTES</h2>
<dl>
<dt><code>AdminDomain:</code></p>
<dd> <i>ID, Description.</i></p>
<dt><code>ComputingManager:</code></p>
<dd> <i>ID, ProductName, ProductVersion, ServiceID.</i></p>
<dt><code>ComputingShare:</code></p>
<dd> <i>ID, MaxCPUTime, MaxWallTime, ServingState,</i> <i>ExecutionEnvironmentForeignKey, RunningJobs, WaitingJobs.</i></p>
<dt><code>Endpoint:</code></p>
<dd> <i>ID, URL, Capability, InterfaceName, InterfaceVersion, Implementor,</i> <i>ImplementationVersion, QualityLevel, HealthState, ServingState,</i> <i>ServiceForeignKey.</i></p>
<dt><code>ExecutionEnvironment:</code></p>
<dd> <i>ID, OSName, ConnectivityOut, MainMemorySize, VirtualMemorySize.</i></p>
<dt><code>Location:</code></p>
<dd> <i>ID, Country, Latitude, Longitude.</i></p>
<dt><code>MappingPolicy:</code></p>
<dd> <i>ID, Scheme, Rule, ComputingShareID.</i></p>
<dt><code>Service:</code></p>
<dd> <i>ID, Capability, Type, QualityLevel, StatusInfo, AdminDomainID.</i></p>
<dt><code>StorageShare:</code></p>
<dd> <i>ID, Path, AccessMode, AccessLatency, ServingState, RetentionPolicy,</i> <i>ExpirationMode, DefaultLifeTime, MaximumLifeTime, Tag.</i></dl>
<h2>OUTPUT FORMAT</h2>
<p> Standard output for an Endpoint:<br />
&nbsp;<wbr>HealthState: Value<br />
&nbsp;<wbr>Implementor: Value<br />
&nbsp;<wbr>InterfaceName: Value<br />
&nbsp;<wbr>ServingState: Value<br />
&nbsp;<wbr>URL: Value<br />
&nbsp;<wbr>ImplementationVersion: Value<br />
&nbsp;<wbr>Capability: Value<br />
&nbsp;<wbr>ServiceForeignKey: Value<br />
&nbsp;<wbr>QualityLevel: Value<br />
&nbsp;<wbr>ID: Value<br />
&nbsp;<wbr>InterfaceVersion: Value </p>
<p> JSON output for an Endpoint:<br />
&nbsp;<wbr>[&#8230;&nbsp;<wbr>&quot;Value_of_the_ID&quot;:&nbsp;<wbr>{<br />
&nbsp;<wbr>&quot;HealthState&quot;: Value,<br />
&nbsp;<wbr>&quot;Implementor&quot;: Value,<br />
&nbsp;<wbr>&quot;InterfaceName&quot;: Value,<br />
&nbsp;<wbr>&quot;ServingState&quot;: Value,<br />
&nbsp;<wbr>&quot;URL&quot;: Value,<br />
&nbsp;<wbr>&quot;ImplementationVersion&quot;: Value,<br />
&nbsp;<wbr>&quot;Capability&quot;: Value,<br />
&nbsp;<wbr>&quot;ServiceForeignKey&quot;: Value,<br />
&nbsp;<wbr>&quot;QualityLevel&quot;: Value,<br />
&nbsp;<wbr>&quot;ID&quot;: Value,<br />
&nbsp;<wbr>&quot;InterfaceVersion&quot;: Value}, &#8230;] </p>
<p> CSV output for an Endpoint:<br />
&nbsp;<wbr>HealthState,Implementor,InterfaceName,ServingState,URL,<br />
&nbsp;<wbr>ImplementationVersion,Capability,ServiceForeignKey,QualityLevel,<br />
&nbsp;<wbr>ID,InterfaceVersion </p>
<h2>EXAMPLES</h2>
<dl>
<dt>1) List all information for all Endpoint attributes</p>
<dd> ginfo &#8211;host bdii.example.com Endpoint </p>
<dt>2) Use the host from the LCG_GFAL_INFOSYS environment variable and list all Location countries</p>
<dd> export LCG_GFAL_INFOSYS=bdii.example.com:2170<br />
 ginfo Location country </p>
<dt>3) List all the Service types</p>
<dd> ginfo -l Type Service </p>
<dt>4) List all IDs from Endpoint which have &#8216;org.glite.FileTransfer&#8217; as name of Interface</p>
<dd> ginfo Endpoint InterfaceName=org.glite.FileTransfer ID </p>
<dt>5) Show the version too</p>
<dd> ginfo Endpoint InterfaceName=org.glite.FileTransfer ID InterfaceVersion </p>
<dt>6) Show all available information about these Endpoints</p>
<dd> ginfo Endpoint InterfaceName=org.glite.FileTransfer </p>
<dt>7) Export to CSV</p>
<dd> ginfo &#8211;csv Endpoint InterfaceName=org.glite.FileTransfer </p>
</dl>
<h2>AUTHOR</h2>
<p> Ivan Calvet &lt;ivan.calvet at cern dot ch&gt; </p>
<h2>Index</h2>
