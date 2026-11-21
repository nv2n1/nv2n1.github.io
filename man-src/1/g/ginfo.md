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
<p> ginfo [options] Object [attribute_to_filter=&#8217;value of the attribute&#8217;] [attribute_to_display]</p>
<p> List attributes corresponding to an object. By default, all the attributes of an object are displayed.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-H, &#8211;host</code> <i>host</i></dt>
<dd> Specify a host to query. By default the environmental variable LCG_GFAL_INFOSYS will be used.</dd>
<dt><code>-b, &#8211;bind</code> <i>binding</i></dt>
<dd> Specify the binding (o=glue by default).</dd>
<dt><code>-l, &#8211;list</code> <i>attribute</i></dt>
<dd> List all the possible values of the specified attribute.</dd>
<dt><code>-c, &#8211;csv</code></dt>
<dd> Output in CSV formating</dd>
<dt><code>-j, &#8211;json</code></dt>
<dd> Output in JSON formating</dd>
<dt><code>-t, &#8211;timeout</code></dt>
<dd> Change the ldap timeout (15 seconds by default).</dd>
<dt><code>-v, &#8211;verbose</code></dt>
<dd> Enable verbose mode</dd>
<dt><code>-V, &#8211;version</code></dt>
<dd> Print the version of ginfo</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> Print this helpful message</dd></dl>
<h2>OBJECTS AND CORRESPONDING ATTRIBUTES</h2>
<dl>
<dt><code>AdminDomain:</code></dt>
<dd> <i>ID, Description.</i></dd>
<dt><code>ComputingManager:</code></dt>
<dd> <i>ID, ProductName, ProductVersion, ServiceID.</i></dd>
<dt><code>ComputingShare:</code></dt>
<dd> <i>ID, MaxCPUTime, MaxWallTime, ServingState,</i> <i>ExecutionEnvironmentForeignKey, RunningJobs, WaitingJobs.</i></dd>
<dt><code>Endpoint:</code></dt>
<dd> <i>ID, URL, Capability, InterfaceName, InterfaceVersion, Implementor,</i> <i>ImplementationVersion, QualityLevel, HealthState, ServingState,</i> <i>ServiceForeignKey.</i></dd>
<dt><code>ExecutionEnvironment:</code></dt>
<dd> <i>ID, OSName, ConnectivityOut, MainMemorySize, VirtualMemorySize.</i></dd>
<dt><code>Location:</code></dt>
<dd> <i>ID, Country, Latitude, Longitude.</i></dd>
<dt><code>MappingPolicy:</code></dt>
<dd> <i>ID, Scheme, Rule, ComputingShareID.</i></dd>
<dt><code>Service:</code></dt>
<dd> <i>ID, Capability, Type, QualityLevel, StatusInfo, AdminDomainID.</i></dd>
<dt><code>StorageShare:</code></dt>
<dd> <i>ID, Path, AccessMode, AccessLatency, ServingState, RetentionPolicy,</i> <i>ExpirationMode, DefaultLifeTime, MaximumLifeTime, Tag.</i></dd></dl>
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
<dt>1) List all information for all Endpoint attributes</dt>
<dd> ginfo &#8211;host bdii.example.com Endpoint </dd>
<dt>2) Use the host from the LCG_GFAL_INFOSYS environment variable and list all Location countries</dt>
<dd> export LCG_GFAL_INFOSYS=bdii.example.com:2170<br />
 ginfo Location country </dd>
<dt>3) List all the Service types</dt>
<dd> ginfo -l Type Service </dd>
<dt>4) List all IDs from Endpoint which have &#8216;org.glite.FileTransfer&#8217; as name of Interface</dt>
<dd> ginfo Endpoint InterfaceName=org.glite.FileTransfer ID </dd>
<dt>5) Show the version too</dt>
<dd> ginfo Endpoint InterfaceName=org.glite.FileTransfer ID InterfaceVersion </dd>
<dt>6) Show all available information about these Endpoints</dt>
<dd> ginfo Endpoint InterfaceName=org.glite.FileTransfer </dd>
<dt>7) Export to CSV</dt>
<dd> ginfo &#8211;csv Endpoint InterfaceName=org.glite.FileTransfer </dd>
</dl>
<h2>AUTHOR</h2>
<p> Ivan Calvet &lt;ivan.calvet at cern dot ch&gt; </p>
