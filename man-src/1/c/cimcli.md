---
title: "cimcli(1)"
name: "cimcli"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cimcli/"
description: "cimcli – command line WBEM Client"
---

<h2>NAME</h2>
<p> cimcli &#8211; command line WBEM Client</p>
<h2>SYNOPSIS</h2>
<p> <i>Operation</i> [<i>OperationTarget</i>] [<i>ValueParameter</i> <i>&#8230;</i>] [ <code>-hc</code> ] [ <code>-h </code><i>operationName</i> ] [ <code>-ho</code> ] [ <code>&#8211;help</code> ] [ <code>-n </code><i>namespace</i> ] [ <code>-l </code><i>location</i> ] [ <code>-u </code><i>user </i><code>name</code> ] [ <code>-p </code><i>password</i> ] [ <code>-s</code> ] [ <code>&#8211;cert </code><i>certFilePath</i> ] [ <code>&#8211;key </code><i>keyFilePath</i> ] [ <code>&#8211;truststore </code><i>clientTrustStorePath</i> ] [ <code>&#8211;sort</code> ] [ <code>&#8211;r </code><i>repeat </i><code>count</code> ] [ <code>-delay </code><i>seconds</i> ] [ <code>&#8211;sum</code> ] [ <code>&#8211;count </code><i>object </i><code>count</code> ] [ <code>&#8211;timeout </code><i>seconds</i> ] [ <code>-o </code><i>XML|MOF|TABLE</i> ] [ <code>&#8211;verbose</code> ] [ <code>-pl </code><i>propertyList</i> ] [ <code>-niq</code> ] [ <code>-di</code> ] [ <code>-ic</code> ] [ <code>-ac </code><i>associationClassName</i> ] [ <code>-rc </code><i>resultClassName</i> ] [ <code>-r </code><i>role</i> ] [ <code>-rr </code><i>resultRole</i> ] [ <code>-f </code><i>filter</i> ] [ <code>-ql </code><i>query </i><code>language</code> ] [ <code>&#8211;version</code> ] [ <code>&#8211;expExit </code><i>exitCode</i> ] [ <code>&nbsp;<wbr>-pt </code><i>pullTimeout</i> ] [ <code>-mr </code><i>maxObjectsToReceive</i> ] [ <code>-pullDelay </code><i>pullDelayinSec</i> ] [ <code>-mo </code><i>maxObjectCount</i> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>cimcli</code> is a command line tool for executing CIM client operations using the CIM/XML protocol. It implements all of the DMTF CIM operations defined in the DMTF specification DSP0200 (CIM Operations over HTTP) except for the modify and create class/instance operations and includes several other operations that are useful in working with CIM Servers.<br />
&nbsp;<wbr> <code>cimcli</code> is available for all platforms that support the Pegasus CIM Server. </p>
<p> For the execution of the DMTF defined CIM operations (ex. enumerateInstances CIM/XML operation). <code>cimcli</code> includes as command line options all of the parameters defined in the DMTF specification. (ex. -di for deep inheritance for the enumerateInstances operation).<br />
&nbsp;<wbr> Effective OpenPegasus 2.14 <code>cimcli</code> incorporates the pull operations defined by DMTF into its operations list . See the section on Pull Client Operations </p>
<p> In addition to the CIM Operations defined in the DMTF specification DMTF DSP0200, <code>cimcli</code> implements a number of other operations that support testing and querying CIM servers (ex. operation to query for namespaces and another to get all instances in a namespace) which require multiple CIM Operations. The additional operations include: </p>
<dl>
<dt>1.</p>
<dd> Enumerate namespaces (ns) &#8211; Returns a list of the namespaces available from the CIMOM.</p>
<dt>2.</p>
<dd> Enumerate all instance names (niall) &#8211; Returns a list of all instance names in a single defined namespace.</p>
<dt>3.</p>
<dd> Turn CIM Server statistics on and off (DEPRECATED) &#8211; Turns the statistics flag in the Server CIMObjectManager Class on or off for the OpenPegasus server. This enables and disables execution of statistics gathering in the server. This command is retained for compatibility but is DEPRECATED and will be removed when a real alternative is included in the Pegasus release. </p>
<p> <code>NOTE:</code> This operation may be CIMServer type specific since not all CIM servers implement the statistics functions.</p>
<dt>4.</p>
<dd> Test instances (ti) &#8211; Executes tests of the characteristics of an instance requested from the CIM Server. This operation extends the capabilities of <code>cimcli</code> to actually compare information from the server with information in the command line input.</p>
<dt>5.</p>
<dd> classtree (ct) &#8211; Display a tree of either superclasses or subclasses of defined classes in the repository.</p>
<dt>6.</p>
<dd> countinstance (cci) &#8211; Count the number of instances by class in a namespace. </p>
<p> <code>WARNING:</code> This operation could cause problems if executed against a server which returns very large numbers of instances since it retrieves all of the instances and counts them in cimcli.</dl>
<p> The format of the <code>cimcli</code> command is: </p>
<p> <code>cimcli [Operation] [OperationTarget] [options] [ValueParameters]</code> </p>
<p> Options may be interspersed with the [OperationTarget] parameter but the ordering and position on the command line of [Operation] [OperationTarget] is fixed and any [value parameters] MUST occur after the [OperationTarget] parameter. </p>
<h3>[Operation]</h3>
<p> Defines the operation to be executed. <code>cimcli</code> executes all of the DMTF CIM Operations (ex. getclass) and a set of compound operations (enumeratenamespaces). There are two forms for each [Operation] definition: </p>
<p> * a short form typically two characters (i.e. gc for getclass) and </p>
<p> * a long form which is the full name of the operation (i.e. getclass). </p>
<p> The complete set of operations can be viewed by calling <code>cimcli</code> with the option -hc. </p>
<h3>[OperationTarget]</h3>
<p> The [OperationTarget] is the name of the object for which the the operation is requested. </p>
<p> This parameter is operation dependent. For example, with the getClass operation the [OperationTarget] is a CIM class name. With the getInstance operation the object is a CIM instance name. Note that some of the commands do not require an [OperationTarget] parameter. Thus, for example, the [OperationTarget] is optional with the enumerateClasses operation as it is with the equivalent enumerateClassNames CIM operation. Normally this is either a CIM class name or an instance name (classname plus keybindings). In some operations one or the other is required. In other operations, the behavior of the operation is dependent on whether class name or instance name is supplied. See the definition of each operation for detailed requirements for the [OperationTarget] </p>
<p> The format for &lt;instancename&gt; (CIMObjectPath) is defined as the model path in the CIM Specification(DMTF DSP0004) and has the form: </p>
<p> <code>&lt;classname&gt;.&lt;keyPropertyName&gt;=&lt;value&gt;[,&lt;keypropertyName&gt;=&lt;value&gt;]*</code> </p>
<p> where: </p>
<dl>
<dt>
<dd> <code>&lt;keyPropertyName&gt;</code> is the name of a property in <code>&lt;className&gt;</code></p>
<dt>
<dd> <code>&lt;value&gt;</code> is a string that represents either a numeric value or a string value (enveloped in quotes). Quote marks surrounding string values are required.</dl>
<p> To simplify inputting command line object names, <code>cimcli</code> offers a second option for defining the object name as [OperationTarget]. In this second form, the [OperationTarget] object is the class name and zero or more &lt;value parameter&gt;s are used to define each feature/value. In this case, the quotation marks around string property values are optional and are required only in the case where quotation marks would be required to define a value such as a string that includes quotation marks or spaces. </p>
<p> The syntax for this form is: </p>
<p> <code>&lt;classname&gt; &lt;keyPropertyName&gt;=&lt;value&gt; [,&lt;keypropertyName&gt;=&lt;value&gt;]*</code> </p>
<p> where:</p>
<dl>
<dt>
<dd> <code>&lt;keyPropertyName&gt;</code> is the name of a property in <code>&lt;className&gt;</code></p>
<dt>
<dd> <code>&lt;value&gt;</code> is either a numeric value or a string value (enveloped in quotes only if there are spaces in the string).</dl>
<p> Note that each name/value definition is treated as a single command line parameter so that MUST not include spaces between the name and value components. (ex. name=fred, not name = fred and name=\&quot;freds name\&quot;) </p>
<p> As an example, the input for a getInstance might be: </p>
<dl>
<dt>
<dd> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>cimcli gi TennisPlayer.first=\&quot;Patrick\&quot;,last=\&quot;Rafter\&quot;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>or<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>cimcli gi &#8216;TennisPlayer.first=&quot;Patrick&quot;,last=&quot;Rafter&quot;&#8217;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>or the simplified form:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>cimcli gi TennisPlayer first=Patrick last=Rafter
</dl>
<p> In the second case, <code>cimcli</code> gets the class from the CIM Server and uses the parameters to form a correct CIMObjectPath. In the first case, generally <code>cimcli</code> uses the input path directly without getting the class from the server. The quotation marks in the first case are required by the CIMObjectPath format defined by the DMTF. </p>
<h3>[options&#8230;]</h3>
<p> Options are identified on the command line with the &#8211; or &#8212; notation. They are identified in a <code>cimcli</code> config file with the form &lt;name&gt;=value where name is a long name for the option. Each <code>cimcli</code> option has both a short name for command line use and a long name for configuration file use. There are several types of options: </p>
<dl>
<dt>1.</p>
<dd> Execution Modification Options &#8211; Options that are universal and modify or define the execution of the command or the form of the return. This includes options like setting the output format for object responses or requesting only summary operation. </p>
<dt>2.</p>
<dd> Connection Options &#8211; Options that define the connection for the operation. This includes options for defining the CIM server address, namespace, and security options such as user name, password and SSL settings. </p>
<dt>3.</p>
<dd> Operation Parameter Options &#8211; Options that represent the optional input parameters for operations. The [operation] defines the CIM Operation that will be executed and the options define the optional request parameters. Typical context options might be -n namespace (used on most but not all operations) or -niq which sets includequalifiers to false for operations that use the includeQualifiers optional parameter. </p>
<dt>4.</p>
<dd> Help Options &#8211; Options to display help (-h, &#8211;help, &#8211;ho to get a list of all options, and -hc to get a list of all operations). When these options are requested, no server request is executed. </p>
</dl>
<h3>[value-parameter]</h3>
<p> Some of the operations allow or require extra parameters, for example to supply property value definitions for create and modify instance. These are typically keywords or keyword/value pairs and are defined as part of the particular operation that use them. </p>
<p> Any extra parameter entities on the command line that occur after the [Operation] and [Operation Target] and are not proceeded by &quot;-&quot; to indicate an option are considered value parameters. These are used in some of the operations to provide additional information required or optionally desired by the operation. See each operation definition to determine if extra parameters are required or allowed. These may be either keyname/value pairs in some cases or simply strings depending on the operation. </p>
<p> <code>NOTE:</code> <code>cimcli</code> does not protect the user against inputting extra options or parameters. Since the options are heavily dependent on the operation to be executed, it ignores options that are not used with a particular operation. Thus, entering the -r option (role) with a getClass operation is syntactically allowed but <code>cimcli</code> ignores the parameter. </p>
<h2>OPTIONS</h2>
<p> There are 4 types of options</p>
<dl>
<dt><code>Boolean</code></p>
<dd> where the option sets some condition (ex. -verbose).</p>
<dt><code>String</code></p>
<dd> requires a string parameter following the option (ex. -n root/test).</p>
<dt><code>Integer</code></p>
<dd> requires an integer following the option (ex. &#8211;delay 4).</p>
<dt><code>Keyword</code></p>
<dd> requires a defined keyword following the option. </p>
</dl>
<h3>CONNECTION OPTIONS</h3>
<p> The following set of options re general to all of the CIM Operations and most of the compound operations They provide parameters for the initiation or execution of the operations (ie. identify the target server and namespace and set connection security parameters).<br />
&nbsp;<wbr>&nbsp;<wbr> These include:</p>
<dl>
<dt><code>-n [namespace]</code></p>
<dd> String option where [namespace] defines the namespace name for this operation (ex. -n root). The default namespace is root/cimv2 if this parameter is not entered</p>
<dt><code>-l [location]</code></p>
<dd> String option where [location] defines the host name or IP address and optionally port for this operation. The default for this command if the -n option is not used is to use the OpenPegasus connectLocal() function to connect to the server. Note that this means that a command like cimcli gc CIM_Door may not work when trying to connect to a server other than Pegasus on the same system. If <code>cimcli</code> is to be used to connect to a CIM Server other than Pegasus on the same system use -l localhost or -l 127.0.0.1 or the actual name or IP address. This will force <code>cimcli</code> to make the connection in the normal way, not using connectLocal().</p>
<dt><code>-u [user-name]</code></p>
<dd> String option where [user-name] defines he user name to be used in the connection to the CIM server for the command.</p>
<dt><code>-p [password]</code></p>
<dd> String option where [password] defines the password to be used in the connection to the CIM server for the command.</p>
<dt><code>-s</code></p>
<dd> Connect with SSL &#8211; Specifies that <code>cimcli</code> should attempt to connect over a secure connection using SSL. This option causes <code>cimcli</code> to modify the client connect call to set the SSLContext option to the certificate defined with the &#8211;cert and &#8211;key options. If this option is set but neither the &#8211;cert or &#8211;key options are included, the SSLContext for the connect call is submitted with the Cert and key marked NULL. </p>
<p> <code>NOTE</code> Since SSL is a compile <code>cimcli</code> compile option, the -s options and following options will not even exist in a <code>cimcli</code> that was compiled with the SSL capabilities disabled.</p>
<dt><code>&#8211;cert [certificate file path]</code></p>
<dd> String options. [certificate-file path defines the file name of a certificate to be used with the client connect if the -s option is set. This is optional and used only with the -s and &#8211;key options. If exits, the client key (&#8211;key option) must also exist</p>
<dt><code>&#8211;key [client key file path]</code></p>
<dd> Defines the file name of a Client private key. This is optional and only has an effect on connections made over HTTPS using the -s option. If exists the client certificate (&#8211;cert option) must also exist. </p>
<dt><code>&#8211;truststore [clientTrustStorePath]</code></p>
<dd> Defines a file or directory containing a truststore that the client uses to verify server certificates. Default is that no trust store exists </p>
</dl>
<h3>CIMCLI OPERATION MODIFICATION OPTIONS</h3>
<p> A set of options that modifies the manner in which the command is executed or the display of information on response including the following:</p>
<dl>
<dt><code>&#8211;t</code></p>
<dd> When set measures time for the operation to be completed and report it upon command completion. If this option is set, the time for the operation is recorded upon completion of the operation. In addition, the client infrastructure is queried to determine if the operation execution times optionally measured in the infrastructure and at the server are available. If so, they are displayed also. This would allow the user to see a) time spent in the server, b) round trip time for the operation, c) application round trip time for the operation. Note that when combined with the repeat option, the output includes maximum, minimum, and average times for the operation. There are a specific operations in <code>cimcli</code> to turn control statistics generation (See son and soff operations) at least for the Pegasus CIM server.</p>
<dt><code>&#8211;sort</code></p>
<dd> Requests <code>cimcli</code> to sort the returned entities for multi-entity operations (ex. enumerate, reference, associator). Normally the order of returned entities is random from most CIM Servers; setting this option outputs the objects in a defined order. The order is based on the name element for classes and qualifier declarations and on the object path returned for CIM instances and CIM objects.</p>
<dt><code>&#8211;r [repeat_count]</code></p>
<dd> Repeat the operation [repeat_count] times. This repeats the operation without disconnecting. This option is useful for defining tests that load the server with repeated calls and also for getting average times for an operation by taking the average of a number of calls (when used with the summary information option (&#8211;sum) and the measure time option (&#8211;t)).</p>
<dt><code>-delay [seconds]</code></p>
<dd> Delay [seconds] seconds between connect and issuing the operation request.</p>
<dt><code>&#8211;sum</code></p>
<dd> When set, <code>cimcli</code> presents only summary information, not full output. Generally <code>cimcli</code> presents counts of objects returned in place of the names or objects themselves when this option is set. See also the repeat (&#8211;r) and measure time (&#8211;t) options.</p>
<dt><code>&#8211;count [object_count]</code></p>
<dd> Defines an expected count of objects to be returned in the response. <code>cimcli</code> is terminated with an error exit if the number of objects returned does not match the object_count supplied with the option. This can be used in batch files to test for number of objects returned by an operation. In addition to the error status code, a message of the general form:</p>
<dl>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&quot;Failed count test. Expected=&nbsp;<wbr>xx. Received=&nbsp;<wbr>yy&quot;&nbsp;<wbr>is output to cerr.</dl>
<p> <code>Example:</code><br />
cimcli en CIM_ManagedElement -count 100 </p>
<p>&nbsp;<wbr>If the count of instances returned is not equal to 100,<br />
&nbsp;<wbr>cimcli exits with error code 60 and the Failed count test&nbsp;<wbr><br />
&nbsp;<wbr>error message.</p>
<dt><code>&#8211;timeout [seconds]</code></p>
<dd> When defined, set the connect timeout [seconds] seconds rather than the default timeout.</p>
<dt><code>-o [ xml | mof | table]</code></p>
<dd> KeyWord option. Output type for commands that output objects. Used with commands that present CIM objects in their response. Presents the output in the form of xml corresponding to DMTF CIM/XML specification, mof, or for instances a table of the data in each property.</p>
<dt><code>-verbose</code></p>
<dd> When set <code>cimcli</code> displays details on the input options and execution of <code>cimcli</code> for the operation.</p>
<dt><code>&#8211;setRtnHostNames [SubstituteHostName]</code></p>
<dd> String option with a required parameter that set a substitute host name which <code>cimcli</code> will insert into returned objects to replace host names returned from the server. This option was defined because the object paths/references returned by the CIM Server may include the host name as part of the returned object path which makes it difficult to compare the returned paths to a defined path. Using this option forces any returned host names to be changed to the string parameter supplied with the option.</p>
<dt><code>&#8211;expExit [exitCode]</code></p>
<dd> Integer option that defines an exit code that is expected when <code>cimcli</code> terminates. If <code>cimcli</code> tries to exit with the defined code, the code is changed to 0 (OK). Any other exit code generates an error exit code. </p>
</dl>
<h3>OPERATION PARAMETER OPTIONS</h3>
<p> Options that define request parameters for specific <code>cimcli</code> Operation requests. These are typically optional parameters on the CIM operation request that modify the behavior of the server to the request. This includes things like requesting localonly, deep inheritance, etc. Note that the actual behavior may be dependent on the particular operation request type. The full definition of these options is below here and their use with each specific <code>cimcli</code> operation is defined with the operations.</p>
<dl>
<dt><code>-pl [propertylist]</code></p>
<dd> String Option. Set the propertylist parameter for those operations that allow this parameter. The propertylist value for this parameter is a comma-separated list of class properties (without spaces between items). This sets the optionsl propertylist parameter on those CIM operations that allow this parameter including: getClass, getInstance, modifyInstance, enumerateInstances, associators, references, OpenEnumerateInstances, OpenReferenceInstances, and OpenAssociatorInstances. If this option is not defined on the execution of one of these operations, <code>cimcli</code> sets the propertylist parameter to NULL indicating that all properties should be returned.<br />
&nbsp;<wbr> If a comma-separated list of one or more properties is defined as the value for this option, a propertylist with these values is set on the CIM request operation.<br />
&nbsp;<wbr> Since this CIM request parameter specifically allows 3 options: 1) list of properties, 2) NULL which is the indicator that all properties are to be returned, and 3) Empty which is the indicator that no properties are to be include in the response, the <code>cimcli</code> options specifically allows defining the empty option by setting propertylist to either &quot;&quot; or \&quot;\&quot;. <code>cimcli</code> accepts either an input that the command processor interprets as an empty string or as a string consisting of two quotation marks. </p>
<p> The syntax of propertylist is: </p>
<p> <code>&lt;propertyName&gt;[,&lt;propertyName&gt;]* | </code> </p>
<p> <code>Examples:</code><br />
&nbsp;<wbr>&nbsp;<wbr>cimcli gc CIM_ManagedElement -pl Caption<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>getclass with a propertylist with one property </p>
<p>&nbsp;<wbr>&nbsp;<wbr>cimcli gc CIM_ManagedElement -pl Caption,Description<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>getClass with a propertylist with two properties </p>
<p>&nbsp;<wbr>&nbsp;<wbr>cimcli gc CIM_ManagedElement -pl&nbsp;<wbr>\&quot;\&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gc operation with empty property list&nbsp;<wbr>(return no <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> properties)</p>
<dt><code>-niq</code></p>
<dd> Boolean (not_include_Qualifiers) that sets the operation parameter for include_qualifiers to false. Note that this form is required because the default for this option in the DMTF CIM Operations is true (include qualifiers). Not including this option sets the request to include qualifiers on those commands to which this option applies.</p>
<dt><code>-nlo</code></p>
<dd> Boolean that defines whether properties from superclasses are included in the response. the -nlo option turns this parameter off. The default if this parameter is not included is to request that the server return only local properties and ignore those from superclasses.</p>
<dt><code>-di</code></p>
<dd> Boolean to set the deep inheritance CIM operation parameter to true.</p>
<dt><code>-ic</code></p>
<dd> Boolean parameter sets the CIM operation parameter classOrigin in the operation request to true. the CIMServer is expected to return classOrigin information as part of the response.</p>
<dt><code>-ac [assocatonClassName]</code></p>
<dd> String defining the association Class parameter for the CIM Operation. Used with reference and association operations.</p>
<dt><code>-rc [resultClassName]</code></p>
<dd> String defining the resultClass parameter for the CIM associator and reference operations.</p>
<dt><code>-r [role]</code></p>
<dd> String defining the role parameter for the CIM associator and reference operations.</p>
<dt><code>-rr [resultrole]</code></p>
<dd> String defining the resultrole parameter for the CIM associator and reference operations. </p>
</dl>
<h2>OPERATIONS</h2>
<p> This section defines the individual operations supported by <code>cimcli</code>. Note that either the names (ex. EnumerateInstances) or the shortcut (ei) may be used in defining an [Operation] on the command line and they are case independent. </p>
<h3>Pull Client Operations and OpenPegasus Overview (OpenPegasus 2.14 extension)</h3>
<p> The DMTF has extended the client xml protocol with new operations that return multiple instance or path responses to allow the client to pull the responses as components of an enumeration sequence rather than a single monolothic operation. This allows the server improved management of operation resources and allows the client to control its memory use. cimcli has created a set of new operations that use this pull model. cimcli did not create an operation corresponding to each client api but one that uses the client apis and a set of options to execute complete pull enumertation sequences. </p>
<p> These operations correspond directly to the original operations as shown in the table below but with extra cimcli options to control the enumeration sequence parameters. </p>
<p> OriginalOperation shortcut PullOperation shortcut enumerateInstances ei PullEnumerateInstances pei enumerateInstanceNames ni PullEnumerateInstancePaths pni references r PullReferenceInstances pr referenceNames rn PullReferenceNames prn associators a PullAssociators pa associatorNames an PullAssociatorPaths pan execQuery xq pullExecQuery pxq </p>
<p> The pull operations generally duplicate the parameters of the original operations with some options to allow the new arguments required to define the enumeration context, control of the size of individual responses, timing, and maximum size. </p>
<p> The pull operations have a common set of options including: <code>-ql [filterQueryLanguage]</code> Optional definition of the filter query language used for this operation. </p>
<p> This option allows specification of filter query languages like the DMTF FQL which apply specifically to filtering instances from enumerations. </p>
<p> WQL and CQL are not allowed with this parameter in the pull operations except for pullExecQuery. FQL is the single normalized filter query language for the pull operations. </p>
<p> Since FQL is a required query language for systems that support the pull operations, it is the definition normally used for this option (&quot;DMTF:FQL&quot;) </p>
<p> <code>-f [filter]</code> Optional filter for the language defined in the -ql option. The response is filtered using this filter specification. The required query language is FQL (Filter Query Language) which is a simple query language that allows only comparison between properties within an instance and literals boolean combinations of these property comparison expressions with AND and OR documented in detail in the DMTF specification DSP0212 and generally is of the form:<br />
property comparison expression:<br />
Scalarproperty operation scalarliteral or ScalarProperty<br />
ArrayProperty operation arrayLiteral or ArrayProperty<br />
ArrayProperty arrayOps scalarProperty or scalarLiteral<br />
Arrayproperty[index]&nbsp;<wbr>operation&nbsp;<wbr>(scalarLiteral or scalarProprty or <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> ArrayProperty[index])</p>
<p>literals: <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ScalarLteral which may be:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> integer (decimal, hex, octal) 123, 0123, 0X1abc<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> String &quot;&#8217;&quot; chars &quot;&#8217;&quot;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> real<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> DateTime<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> Reference<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ArrayLiteral:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> &quot;{&quot; scalarLiteral * (&quot;,&quot; ScalarLiteral ) &quot;}&quot;</p>
<p>&nbsp;<wbr>Operation:<br />
&nbsp;<wbr>&nbsp;<wbr>where the operations allowed are dependent on the <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>left argument of the expression and may include:</p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>equality comparison&nbsp;<wbr>&quot;=&quot;&nbsp;<wbr>&quot;&lt;&gt;&quot;&nbsp;<wbr>&quot;LIKE&quot;&nbsp;<wbr>&quot;NOT LIKE&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> * ordering &quot;&gt;=&quot; &quot;&lt;=&quot; &quot;&gt;&quot; &quot;&lt;&quot;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> * arrayOps &quot;ANY&quot;, &quot;EVERY&quot;</p>
<dl>
<dt><code>-pt [pullTimeout]</code></p>
<dd> The timeout value that <code>cimcli</code> sends to the server as part of the open request. This is the minimum time in seconds that the server will keep the enumeration context open between sending a response and receiving the next request within a single pull sequence.</p>
<dt><code>-mr [maxObjectsToReceive]</code></p>
<dd> The maximum number of instances or paths that will be accepted by cimcli before issuing a close operation.</p>
<dt><code>-pullDelay [pullDelayinSec]</code></p>
<dd> Delay in seconds that <code>cimcli</code> will execute between each of the operations of the pullsequence. The primary use for this is testing delay issues.</p>
<dt><code>-mo [maxObjectCount]</code></p>
<dd> The maximum object count that <code>cimcli</code> sends to the server for each request in an enumeration context. The server returns no more than this number of instances or paths </p>
</dl>
<h3>ci CreateInstance Operation</h3>
<p> The CreateInstance operation executes the DMTF CIM/XML createInstance operation request. It builds an instance of the class defined on the command line building the properties of the instance from a combination of the class retrieved from the CIM server and value parameters provided with the input. <code>cimcli</code> issues the CIM operation createInstance with the created instance It requires the [OperationTarget] parameter defining the class for which the instance is to be created and optional set of property definition (name=value) parameters that define properties and their values for the created instance. </p>
<p> CreateInstance returns the object path of the created instance if the call to the CIM server was executed successfully. Otherwise it returns the exception from the server.<br />
&nbsp;<wbr> <code>cimcli</code> can define property values for either scalar or array properties for any of the CIM Data types including embedded instance and embedded object types </p>
<p> The syntax for createInstance is: </p>
<dl>
<dt>
<dd> <code>cimcli ci &lt;className&gt; &lt;propertyDef[,&lt;propertyDef&gt;]*</code><br />
&nbsp;<wbr> where &lt;propertyDef&gt; is defined as follows: </p>
<dl>
<dt>&lt;propertyName&gt;=&lt;scalarValueString&gt;</p>
<dd> Defines a value for a property where propertyName is a scalar property of any type except the types representing embedded instances or embedded objects (i.e. String with EmbeddedInstance or EmbeddedObject qualifier). The scalalValueString may represent any CIM Data type (string, integer, datatime, real)with the same syntax as MOF input. Strings with embedded spaces must be enclosed in quotation marks.</p>
<dt>&lt;propertyName&gt;=&lt;scalarValueString&gt;[,&lt;scalarValueString&gt;]*</p>
<dd> Defines an array of values for a property which is an array property and each valueString is one value in the array.</p>
<dt>&lt;propertyName&gt;!</p>
<dd> Defines a value of NULL for a String property.</p>
<dt>&lt;propertyName]&gt;=</p>
<dd> Defines a property with NULL value.</p>
<dt>&lt;propertyName&gt;={&lt;embeddedClassName&gt; [&lt;propertyDef&gt;]* }</p>
<dd> Defines a property that is an embedded instance, embedded object, or reference(CIMObjectPath) where &lt;embeddedClassName&gt; is the class name for the embedded object or instance and &lt;propertyDefinition&gt;.<br />
&nbsp;<wbr>This syntax is recursive so that instances of embedded classes can be embedded in properties that are themselves embedded instance types.</p>
<dt>&lt;propertyName&gt;={&lt;embeddedClassName&gt; [&lt;propertyDef&gt;]* [}.{ [&lt;propertyDef&gt;]*]*</p>
<dd> Defines a property that is an array of embedded instances or embedded objects &lt;embeddedClassName&gt; is the class name for the embedded object or instance and &lt;propertyDefinition&gt;</dl>
</dl>
<p> NOTE: The value of array properties may also be defined by repeating the property multiple times with the different values. <code>cimcli</code> will consolidate these multiple property definitions into an array </p>
<p> The use of the value parameters is further defined in the following paragraphs. Note that the syntax for value parameters for DMTF data types differes from the syntax for value parameters for embedded instances and objects. </p>
<p> <code>1.</code> Scalar property values &#8211; The string form of the property similar to MOF input of constant values is used to input scalar values. The scalar value input includes all CIM Types. Numeric values may be input in hex, octal, decimal or binary in the same form as the DMTF specification for MOF. Quotations are not required surrounding values unless the value includes spaces. Quote marks can be embedded by escaping them (ex. ab\&quot;cd) with whatever the shell uses as an escape character.. </p>
<p> <code>2.</code> Array property values &#8211; Array property values are defined by defining a string that is comma-separated scalar value entities. of the form : </p>
<dl>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&lt;scalarvalueString&gt;[,&lt;scalarvalueString&gt;]*</dl>
<p> The array MUST NOT include any spaces between the scalar value entities. It must appear to <code>cimcli</code> as a single input parameter. In addition, array value can be input by repeating the complete parameter so that values input will be appended to an already created array. </p>
<p> <code>3.</code> If the propertyName parameter is provided with no value, the default value or NULL if there is no default value is inserted. </p>
<p> <code>4.</code> String property values are special because there are two concepts that must be covered when there is no value, 1) Empty String or 2. NULL/default value. These are different for CIM Strings. </p>
<p> When a property that requires an empty string is to be input, the user will specify it with no value after the = sign. If, a NULL or default value is desired, the = sign terminator is replaced with the ! (exclamation mark). </p>
<p> <code>5.</code> The value defined in the name/value pair must be decodable into the CIMType of the CIMClass for which the instance is being created. For example a String cannot be supplied for a property that is of type Uint32. <code>cimcli</code> get the CIMType for the property from the server and checks this against the data input. </p>
<p> The execution of this operation first accesses the CIM server for the class definition and uses this information to build the proper value types and values for the instance. This means that values that cannot be decoded with values to match the CIM Type in the class will be rejected. </p>
<p> This command builds the instance with all of the properties for which name/value pairs representing the properties of the class are input. It does not include any properties that are not defined on the command line. </p>
<p> To create an instance with less than the full set of properties, supply only those properties that are to be submitted to the CIM Server. </p>
<p> The command will be rejected if the class does not exist in the namespace or if the input includes property names that are not in the class. </p>
<p> <code>6.</code> If the property defines an embedded instance or embedded object (defined in MOF as a CIMTYpe String but with the qualifer &quot;embeddedInstance&quot; or &quot;embeddedObject&quot; the embedded instance can be built directly from the command line by supplying the class name and property definitions for the embedded instance. Note that <code>cimcli</code> builds embedded instances in any case (It cannot build embedded classes) but sends them to the server as either embedded instances or embedded objects per the MOF definiton. </p>
<p> An embedded instance definition is delineated by either &quot;{&quot; or &quot;={&quot; separating the property name and value definition &quot;}&quot; to end the embedded instance definition as shown below: </p>
<dl>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&lt;propertyName&gt;={&lt;embeddedClassName&gt;&nbsp;<wbr>[&lt;propertyDef&gt;]*&nbsp;<wbr>}</dl>
<p> The embedded instance termination marker &quot;}&quot; must be separated by spaces from other parameters. </p>
<p> Arrays of embedded instances can also be created following the pattern for arrays of properties of other CIM types as follows: </p>
<dl>
<dt>&bull;</p>
<dd> Define the property multiple times. Each time the property is defined for an embedded instance (with the same property name and same class name) the new definition is appended to the array. </p>
<dt>&bull;</p>
<dd> Use the special terminator &quot;},{&quot; which allows <code>cimcli</code> to start a new instance definition (in effect using the comma separated values as in the arrays of other CIM types. </p>
<p> <code>Examples:</code><br />
&nbsp;<wbr>cimcli ci CIM_xxxx ID=abc size=32 age=O12<br />
&nbsp;<wbr>&nbsp;<wbr>Creates an instance of CIM_xxxx with&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>property ID value&nbsp;<wbr>=&nbsp;<wbr>abc,&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>property size with value 32<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>property age with value octal 012 </p>
<p>&nbsp;<wbr>cimcli ci CIM_xxxx ID=grrrr&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>arrayParam={abc,def,ghi,&quot;jkl mno&quot;&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>numArray=1,2,3,4<br />
&nbsp;<wbr>&nbsp;<wbr>Creates an instance of CIM_xxxx with<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>property ID with value&nbsp;<wbr>=&nbsp;<wbr>grrr<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>property arrayParam&nbsp;<wbr>(a String array property)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>with the values<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>abc<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>def<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ghi<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>jkl mno<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>property numArray&nbsp;<wbr>(Uint32 array)&nbsp;<wbr>with<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the values&nbsp;<wbr>&nbsp;<wbr>1, 2, 3, 4<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>cimcli ci CIM_xxxx ID=blah&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>numArray=1,2,3 numArray=4,5<br />
&nbsp;<wbr>&nbsp;<wbr>Creates an instance with the ID property and<br />
&nbsp;<wbr>&nbsp;<wbr>the numArray property having the&nbsp;<wbr>&nbsp;<wbr>values<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1,2,3,4,5 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>cimcli ci&nbsp;<wbr>&nbsp;<wbr>Test_yyy id=301&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>comment=&quot;test with multiple embedded instances&quot;&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>embeddedInst{Test_CLITestEmbedded1 Id=302&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>comment=&quot;First property with embedded instance&quot;&nbsp;<wbr>}&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>embeddedInst2{Test_CLITestEmbedded2 Id=303 name=fred&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>comment=&quot;Second property with embedded instance&quot;&nbsp;<wbr>}<br />
&nbsp;<wbr>&nbsp;<wbr>Creates an instance of class Test_yyy with a single scalar<br />
&nbsp;<wbr>&nbsp;<wbr>property&nbsp;<wbr>(comment)&nbsp;<wbr>and two embedded instance properties<br />
&nbsp;<wbr>&nbsp;<wbr>(embeddedInst and embeddedInst2). Each of the embedded<br />
&nbsp;<wbr>&nbsp;<wbr>instances contains 3 properties&nbsp;<wbr>(Id, name, and comment). </p>
<p>&nbsp;<wbr>&nbsp;<wbr>//&nbsp;<wbr>create an association with two REF properties, parent and child<br />
&nbsp;<wbr>&nbsp;<wbr>cimcli ci Test_assoc&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>parent={Test_target id=301&nbsp;<wbr>}&nbsp;<wbr>\ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> child={Test_associated id=972 }</p>
<p>&nbsp;<wbr>&nbsp;<wbr>same as defining the<br />
&nbsp;<wbr>&nbsp;<wbr>cimcli ci Test_assoc&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>parent=Test_target.id=301&nbsp;<wbr>}&nbsp;<wbr>\ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> child=Test_associated.id=972 }</p>
</dl>
<h3>mi ModifyInstance Operation</h3>
<p> This operation allows the modification of existing instances in the target server by building the properties from a combination of the target Class and properties provided with the input. The command issues the CIM operation modifyInstance with an instance built from the parameters provided. It requires the [OperationTarget] parameter defining the class for which the instance is to be created and a set of value parameters that define properties to be provided in the created instance in the format defined for CreateInstance above. The modified instance may also be built from a combination of the CIMObjectPath for the instance to be modified and value parameters for other properties.<br />
&nbsp;<wbr> In the same manner as the createInstance, this command first acquires the class or objectPath definition for the server and uses the property type information from the class to properly create the property value types from the input property values. </p>
<p> This operation also allows the specific interactive mode where the classname and properties to be modified (minus key properties) are supplied and <code>cimcli</code> presents a selection of instance names that can be modified. </p>
<p> For a detailed definition of the name/value input see the createInstance description. </p>
<p> In addition to the property definitions, this command allows the property list option (-pl) that defines a property list to be supplied to the target server with the modifyInstance CIM Operation. </p>
<p> NOTE: For some versions of Pegasus the -pl option may be required to allow the server to correctly modify the instance since without this option the pegasus server may remove properties that are not in the modified instance. </p>
<p> The syntax for the modifyInstance operation is as follows: </p>
<dl>
<dt>
<dd> <code>cimcli mi &lt;className&gt; [&lt;propertyDef&gt;]* [-pl &lt;propertyList]</code></p>
<dl>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>where the properties defined MUST include the key<br />
&nbsp;<wbr>&nbsp;<wbr>properties</dl>
<p>&nbsp;<wbr>or </p>
<p> <code>cimcli mi &lt;objectPath&gt; [&lt;propertyDef&gt;]* [-pl &lt;propertyList]</code></p>
<dl>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>where the properties defined do not include the key<br />
&nbsp;<wbr>&nbsp;<wbr>properties</dl>
</dl>
<p> See createInstance operation for detailed definition of &lt;propertyDef&gt; and more examples: </p>
<p> <code>Examples:</code><br />
&nbsp;<wbr>cimcli mi CIM_xxxx name=abc size=zyx<br />
&nbsp;<wbr>or<br />
&nbsp;<wbr>cimcli mi&nbsp;<wbr>&#8216;CIM_xxx.name=&quot;abc&quot;&#8217;&nbsp;<wbr>size=zyx<br />
&nbsp;<wbr>or<br />
&nbsp;<wbr>cimcli mi CIM_xxxx name=abc arrayParam=&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>{abc,def,ghi,&quot;jkl mno&quot;&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>numericArray=1,2,3,4 </p>
<h3>ec EnumerateClasses Operation</h3>
<p> Issues the enumerateClasses CIM operation which enumerates the class hierarchy starting at the level defined by &lt;classname&gt;. </p>
<p> The syntax for this operation is: </p>
<p> <code>cimcli ec [&lt;classname&gt;] [options]</code> </p>
<p> where classname is not required. If it is omitted, <code>cimcli</code> inserts an empty classname into the CIM operation which tells the CIM Server to start at the top of the class inheritance tree. The possible options that represent the parameters of the enumerateClasses operation are: </p>
<p> <code>-niq</code> Boolean (not_include_Qualifiers) that sets the operation parameter for include_qualifiers to false. </p>
<p> <code>-nlo </code> Boolean that defines whether properties from superclasses are included in the response. the -nlo option turns this parameter off </p>
<p> <code>-ic</code> Boolean parameter sets the operation parameter includeClassOrigin in the operation request. the CIM server is expected to return classOrigin information as part of the response. </p>
<p> <code>-pl [propertyList]</code> Optional property list for the operation. </p>
<p> <code>Example:</code><br />
cimcli ec CIM_ManagedElement -di -nlo </p>
<h3>nc EnumerateClassNames Operation</h3>
<p> The EnumerateClassNames <code>cimcli</code> operation issues the enumerateClassNames CIM Operation. </p>
<p> The syntax for this operation is: </p>
<p> <code>cimcli nc [&lt;classname&gt;] [options]</code> </p>
<p> The classname parameter optional and the default it is not provided is to return the class names of the top level classes. </p>
<p> The options specific to this operation include; </p>
<p> <code>-di</code> set the operation deepInheritance parameter = true not localOnly </p>
<p> <code>Examples:</code><br />
&nbsp;<wbr>&nbsp;<wbr>cimcli nc CIM_door<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Issue getClass CIM Operation for the class CIM_Door. </p>
<dl>
<dt><code>ni EnumerateInstanceNames Operation</code></p>
<dd> Execute the enumerateInstanceNames CIM Operation. The syntax for this operation is: </p>
<p> <code>cimcli ni &lt;classname&gt; [&lt;option&gt;]*</code> </p>
<p> Where: </p>
<p> <code>&lt;classname&gt;</code> &#8211; classname for which instance names are to be enumerated. </p>
<p> It displays the instances names that were returned by the CIM server in response to the enumerateInstances CIM operation with the defined input parameters. </p>
<p> <code>Examples:</code><br />
&nbsp;<wbr>cimcli ni CIM_ManagedElement -p password -n name&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>-n root/PG_Interop &#8211;sort </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Execute the enumerateInstanceNames operation on<br />
&nbsp;<wbr>&nbsp;<wbr>CIM_ManagedElement in the root/PG_Interop namespace.<br />
&nbsp;<wbr>&nbsp;<wbr>Sort the returned list of instance paths. </p>
<p>&nbsp;<wbr>cimcli ni CIM_Door &#8211;sum<br />
&nbsp;<wbr>&nbsp;<wbr>Execute the enumerateInstanceNames operation on the class<br />
&nbsp;<wbr>&nbsp;<wbr>CIM_Door and return the count of instance paths returned. </p>
</dl>
<h3>ei EnumerateInstances Operation</h3>
<p> Execute the CIM operation enumerateInstances. The syntax for this operation is: </p>
<p> <code>cimcli ei [className] [&lt;option&gt;]*</code> </p>
<p> This operation requests instances from the CIM server and displays the returned instances in a user selected format. </p>
<p> The following options represent specific parameters for this operation: </p>
<p> <code>-nlo</code> not local only operation parameter to false. Note that this negative form for the option is used because the default for local only parameter is true. Thus, not including this parameter means that the parameter is not set. </p>
<p> <code>-iq</code> Boolean (include_Qualifiers) that sets the operation parameter for include_qualifiers to true, </p>
<p> <code>-ic</code> Boolean to set include class origin operation parameter to true. </p>
<p> <code>-di</code> Set deep inheritance operation parameter to true.<br />
&nbsp;<wbr> <code>-o [xml|mof|table]</code> Set the output format for the instances to display the returns as mof </p>
<p> <code>-pl [propertyList]</code> Optional property list for the operation<br />
&nbsp;<wbr>&nbsp;<wbr> It returns the instances found either as MOF, XML, or a table of property values with each property a column in the table depending on the output options parameter. </p>
<p> <code>Examples:</code><br />
&nbsp;<wbr>cimcli ei CIM_ComputerSystem -niq -di<br />
&nbsp;<wbr>&nbsp;<wbr>This example enumerates CIM_ComputerSystem in the<br />
&nbsp;<wbr>&nbsp;<wbr>namespace root/CIMV2&nbsp;<wbr>(default)&nbsp;<wbr>requesting without<br />
&nbsp;<wbr>&nbsp;<wbr>qualifiers&nbsp;<wbr>(-niq)&nbsp;<wbr>with deepInheritance&nbsp;<wbr>(-di).&nbsp;<wbr>&nbsp;<wbr> </p>
<h3>niall enumerateallinstanceNames Operation</h3>
<p> Execute an enumerateinstancenames on all classes to get all class names within the defined namespace or class hiearchy below the target input class. if no class name is psecified on input this function enumerates the complete set of classes namespace to get the classes and the enumerateInstanceNames command to enumerate all of the instances for each class. It returns the list of all of the instance names found in the namespace and a summary of the number of instances of each class that has instances. </p>
<p> The syntax for this operation is: </p>
<p> <code>cimcli niall [className] [options]</code> </p>
<p> where the options include any of the universal options (ex. namespace, location, etc.). Specifically the &#8211;sum option allows returning only the summary information including count of instances for each class that has instances in the namespace. </p>
<p> <code>Examples:</code><br />
&nbsp;<wbr>cimcli niall -n test/testproviders </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Returns all instancenames in the namespace<br />
&nbsp;<wbr>&nbsp;<wbr>test/testproviders by executing<br />
&nbsp;<wbr>&nbsp;<wbr>enumerateinstancenames on each class in<br />
&nbsp;<wbr>&nbsp;<wbr>the namespace.<br />
&nbsp;<wbr>cimcli niall CIM_OperatingSystem<br />
&nbsp;<wbr>&nbsp;<wbr>Returns all instance names in the namespace root/cimv2 for<br />
&nbsp;<wbr>&nbsp;<wbr>classes in the hiearchy starting at PG_OperatingSystem. </p>
<h3>gi GetInstance Operation</h3>
<p> Gets the instance defined by the instance name parameter and displays it in the format chosen for this operation (xml, mof, or table). </p>
<p> The syntax for this operation is: </p>
<p> <code>cimcli gi [objectname] [&lt;option&gt;]*</code> </p>
<p> which causes execution of the CIM getinstance operation. OR </p>
<p> <code>cimcli gi [classname] [&lt;option&gt;]*</code> </p>
<p> which presents a list of possible instances to the user from which one can be selected for the getinstance. In this case, the command actually executes an enumerateInstanceNames to get the list of instances that is presented to the user for selection of a single instance. The getInstance is executed after the user makes a selection. </p>
<p> This command requires the [objectname] parameter. If the parameter is an instance with keys defined (a CIMObjectPath), the a getInstance CIM operation is executed and the return from the CIM Server presented (in either xml or mof depending on the output option). If the input is a class name, a enumerateinstanceNames CIM Operation is executed and if any instance names are returned the result is presented to the console for the user to select one of the instances to be deleted. </p>
<p> If there are no instances, the return from this command is normally an exception as defined in the DMTF CIM Operations specification.. </p>
<p> The possible options specific to this operation are: </p>
<p> <code>-iq</code> include qualifiers. The default for getInstance is includQualifiers=false so use of this parameter is required if the user wants qualifiers returned. NOTE: The use of the parameter in CIM/XML has been deprecated so the provider may not return qualifiers even if requested. </p>
<p> <code>-nlo</code> </p>
<p> localonly </p>
<p> <code>-pl [propertyList]</code> Optional property list for the operation </p>
<p> <code>Examples:</code><br />
&nbsp;<wbr>cimcli gi cim_ManagedElement </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This is an interactive request that returns a list of<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>CIMObjectPaths from an enumerateInstance of<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>CIM_ManagedElement from which the user can select<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>one path which cimcli will uses as the&nbsp;<wbr>[objectname]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>to execute a getInstance operation returning the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>instance. </p>
<h3>di deleteInstance Operation</h3>
<p> Delete instance executed a single deleteInstance command to the CIM Server. The syntax is: </p>
<p> <code>cimcli di [objectname] [&lt;option&gt;]*</code> </p>
<p> This command requires the [objectname] parameter. If this parameter is a full instance name with className and key bindings, the deleteInstance CIM Operation is executed directly. If it is a class name with no keybindings, the enumerateInstances CIM Operation is executed and the list of returned instance paths presented to the console for the user to senroff manpages html tablect one to delete. <code>cimcli</code> then executes CIM deleteInstance operation with the selected [objectname] and returns the response. </p>
<p> The response to this operation is either an empty response if the instance was successfully deleted or an exception return if there were any errors. </p>
<p> <code>Examples:</code><br />
&nbsp;<wbr>cimcli di President.&quot;name=fred&quot;&nbsp;<wbr>-n test/testnamespace </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Attempt to delete the instance of President with the key<br />
&nbsp;<wbr>&nbsp;<wbr>property name(fred)&nbsp;<wbr>from the test/testnamespace namespace. </p>
<p>&nbsp;<wbr>cimcli di President&nbsp;<wbr>&nbsp;<wbr>-n test/testnamespace </p>
<p>&nbsp;<wbr>&nbsp;<wbr>cimcli requests instance paths for the President class in<br />
&nbsp;<wbr>&nbsp;<wbr>the test/testnamespace and puts the complete list on the<br />
&nbsp;<wbr>&nbsp;<wbr>console for the user to select one instance to delete. </p>
<h3>gq getQualifier Operation</h3>
<p> getQualifier displays the target qualifier. The syntax is: </p>
<p> <code>cimcli gq [qualifier name] [&lt;option&gt;]*</code> </p>
<p> <code>Examples:</code><br />
&nbsp;<wbr>cimcli gq abstract </p>
<p>&nbsp;<wbr>&nbsp;<wbr>returns the mof or XML for the abstract qualifier. </p>
<h3>sq setQualifier Operation</h3>
<p> This command is not implemented. We do not intend to implement this operation in <code>cimcli</code> because of the syntax complexity. Use a mof compiler to create new qualifiers in the CIM server </p>
<h3>eq enumeratequalifiers Operation</h3>
<p> Issues the CIM Operation to enumerate all of the qualifiers defined in the target namespace. The syntax is: </p>
<p> <code>cimcli eq [&lt;option&gt;]*</code> </p>
<p> There are no special options for this operation. </p>
<h3>dq deletequalifier Operation</h3>
<p> Issues the CIM operation to delete the target qualifier defined by qualifier_name in the target namespace. The Syntax is: </p>
<p> <code>cimcli dq [qualifier_name] [&lt;option&gt;]*</code> </p>
<p> NOTE: This operation should be used with great caution as it removes qualifier declarations that may be used by other components of the model. </p>
<h3>a associators Operation</h3>
<p> Execute the CIM Operation enumerate associators for the target object name. The syntax for this operation is:<br />
&nbsp;<wbr> <code>cimcli a [objectname] [&lt;option&gt;]*</code> </p>
<p> Note that the objectname may be either a classname or an instancename. If classname is supplied, the return is a set of classes that match the objectname supplied unless the -i (interactive) parameter is used. If objectname is used, the response is instances of the association that matches the classname. </p>
<p> The options provide the various operation parameters including; </p>
<p> <code>-ac [assocatonClassName]</code> association Class parameter </p>
<p> <code>-rc [resultClassName]</code> resultClass parameter </p>
<p> <code>-r [role]</code> String defining the role parameter for the CIM Operation </p>
<p> <code>-rr [resultrole]</code> resultrole parameter </p>
<p> <code>-ic</code> Set includeClassOrigin input parameter true </p>
<p> <code>-pl [properytlist]</code> Optional PropertyList </p>
<p> <code>-i</code> Interactive request &#8211; If this parameter is supplied and the objectname is a classname, the environment performs an enumerateInstances on the objectname and presents the list of possible instances for user selection </p>
<h3>an associatornames Operation</h3>
<p> Enumerate the associator names for the target object. The syntax for this operation is: </p>
<p> <code>cimcli an [objectname] [&lt;option&gt;]*</code> </p>
<p> where objectname can be either a class name or an instance name. </p>
<p> The following options provide the various operation parameters; </p>
<p> <code>-ac [assocatonClassName]</code> association Class parameter </p>
<p> <code>-rc [resultClassName]</code> resultClass parameter </p>
<p> <code>-r [role]</code> String defining the role parameter for the CIM Operation </p>
<p> <code>-rr [resultrole]</code> resultrole parameter </p>
<p> <code>-i</code> Interactive request &#8211; If this parameter is supplied and the objectname is a classname, the environment performs an enumerateinstances on the objectname and presents the list of possible instances for user selection </p>
<h3>r references Operation</h3>
<p> Executes the CIM references Operation. Which returns CIM Objects. The syntax for this the operation is: </p>
<p> <code>cimcli r [objectname] [&lt;option&gt;]*</code> </p>
<p> Note that the objectname may be either a class name or an instance name. If a class name is supplied, the return is a set of classes that of the association. If the -i (interactive) parameter is used with a class name input, the user is queried for the objectname parameter. If objectname is used, the response is instances of the associations that match the classname </p>
<p> The options specifically used by this operation are: </p>
<p> <code>-r [role]</code> role parameter for the CIM Operation. </p>
<p> <code>-rc [resultClassName]</code> resultClass parameter for the CIM Operation </p>
<p> <code>-iq</code> includeQualifiers (The default is false) </p>
<p> <code>-ic</code> Boolean to set include class origin operation parameter to true. </p>
<p> <code>-pl [propertyList]</code> Optional property list for the operation </p>
<p> <code>-i</code> Interactive request &#8211; This option is used only with commands that will accept either classname or object name as input (reference, referencenames, associatiors, associatornames). It allows the interactive mode where the user picks an instance from a list returned by <code>cimcli</code> (similar to gi where if only the classname is supplied, <code>cimcli</code> knows that the user wants to pick from a list) with these commands. If this parameter is supplied and the objectname is a classname, the environment performs an enumerateinstances on the objectname and presents the list of possible instances for user selection. Thus, the user can execute interactive reference, etc. operations </p>
<p> <code>Examples:</code><br />
&nbsp;<wbr>&nbsp;<wbr>cimcli a CIM_ManagedElement<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>would return classs that associate with<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>CIM_ManagedElement </p>
<p>&nbsp;<wbr>&nbsp;<wbr>cimcli a CIM_ManagedElement -i<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>executes an enumerateInstanceNames on<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>CIM_ManagedElement and presents the user with<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>a list of instances names so that the user can<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pick an instance name that will be used for<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the associator request. </p>
<h3>rn referencenames Operation</h3>
<p> Executes the CIM Operation referencenames that returns CIMObject paths of the references of the objectname parameter. </p>
<p> The syntax for this operation is: </p>
<p> <code>cimcli rn [objectname] [&lt;option&gt;]*</code> </p>
<p> Note that the objectname may be either a class name or a specific instance name. If classname is supplied, the return is a set of classnames that are references of the objectname supplied. If the -i parameter is used with a class name as objectname, the user is queried to select an instance name for the objectname input. If objectname is used, the response is instance names of the associations that matches the classname. </p>
<p> The options specifically used by this operation are: </p>
<p> <code>-r [role]</code> role parameter for the CIM Operation </p>
<p> <code>-rc [resultClassName]</code> resultClass parameter for the CIM Operation </p>
<p> <code>-i</code> Interactive request &#8211; If this parameter is supplied and the objectname is a classname, the environment performs an enumerateinstances on the objectname and presents the list of possible instances for user selection </p>
<h3>im invokeMethod Operation</h3>
<p> This operation sends a CIM extrinsic operation to the CIM server to execute a method on a CIM class or instance. </p>
<p> The syntax of the command is: <code>cimcli im [objectname] [methodname] [&lt;parameDef&gt;]* [&lt;option&gt;]*</code> Note that there are two required parameters to this command, the [objectname] and the [methodname]. Parameter definitions &lt;paramDef&gt; are optional. </p>
<p> NOTE: Earlier versions of <code>cimcli</code> allowed only String values and used the -ip option. This option has been removed. Parameters are input in the form:</p>
<dl>
<dt>&lt;paramName&gt;=&lt;scalarValueString&gt;</p>
<dd> Defines a value for a parameter where paramName is a scalar parameter of any type except the types representing embedded instances or embedded objects (i.e. String with EmbeddedInstance or EmbeddedObject qualifier).</p>
<dt>&lt;paramName&gt;=&lt;scalarValueString&gt;[,&lt;scalarValueString&gt;]*</p>
<dd> Defines an array of values for a parameter which is an array parameter and each valueString is one value in the array.</p>
<dt>&lt;paramName&gt;!</p>
<dd> Defines a value of NULL for a String parameter</p>
<dt>&lt;paramName&gt;=</p>
<dd> Defines a parameter with NULL value</p>
<dt>&lt;paramName&gt;={&lt;className&gt; [&lt;paramDef&gt;]* }</p>
<dd> Defines a parameter that is an embedded instance or embedded object where &lt;className&gt; is the class name for the embedded object or instance and &lt;paramDef&gt;. This syntax is recursive so that instances of embedded classes can be embedded in properties that are themselves embedded instance types.</p>
<dt>&lt;paramName&gt;={&lt;className&gt; [&lt;paramDef&gt;]*[}.{ [&lt;paramDef&gt;]*]*</p>
<dd> Defines a parameter that is an array of embedded instances or embedded objects &lt;className&gt; is the class name for the embedded object or instance and &lt;paramDefinition&gt; </p>
<p> NOTE: The value of array prammeters may also be defined by simply repeating the prameter definition multiple times with the different values. <code>cimcli</code> will consolidate these multiple property definitions into an array </p>
<p> The completed operations displays the return code from the command and any returned parameters that are qualified as OUT parameters. </p>
<p> <code>Example:</code><br />
&nbsp;<wbr>&nbsp;<wbr>cimcli PG_WBEMSLPTemplate register -n root/PG_Interop<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Calls PG_WBEMSLPTemplate class with the method named<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>register </p>
<p>&nbsp;<wbr>&nbsp;<wbr>cimcli PG_XXX dosomething input1=true input2=1111<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Calls PG_XXX class method dosomething with two<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>parameters:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>input1 is boolean parameter with value true<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>input2 is Uint32 parameter with value 1111 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>The completed operation displays the return code from the <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> command and any returned parameters that are qualified as<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> OUT parameters.</p>
</dl>
<h3>gp getProperty Operation</h3>
<p> Executes the getProperty CIM operation which gets a single property from the server. Note that this operation has been deprecated in the DMTF specifications because a) it is effectively redundant with the getInstance operation and property lists b) there was an error in the design such that the CIM data type is not returned with the response so the client does not know what data type is being returned from the response data. </p>
<p> It is implemented in <code>cimcli</code> but simply tries to convert the response to a string which means that it would get confused with a CIMInstance or CIMObject response. </p>
<p> The syntax of this operation is:</p>
<dl>
<dt>
<dd> <code>gp &lt;objectPath&gt; &lt;propertyName&gt;</code></dl>
<h3>sp setProperty Operation</h3>
<p> The setProperty executes the setProperty operation which attempts to set a single property on an instance in the CIM Server.<br />
 The syntax of this operation is: </p>
<dl>
<dt>
<dd> <code>sp &lt;objectPath&gt; &lt;propertyName=&lt;&lt;value&gt;</code></dl>
<h3>xq execQuery Operation</h3>
<p> The execQuery operation directly executes the CIM Operation execQuery with the input parameter supplied either by direct parameter input or the options for filter and querylanguage. The syntax of the operation is </p>
<p>cimcli xq&nbsp;<wbr>&lt;query_filter&gt;&nbsp;<wbr>&lt;query_language&gt;&nbsp;<wbr>[&lt;option&gt;]* The query_filter and the query_language may be supplied directly on the command line as parameter or as options (-f for the query filter and -ql for query language. </p>
<p> The execQuery CIM Operation is executed directly with the input parameters or options. If neither a query_filter parameter or option are supplied <code>cimcli</code> returns an error. If the query_language parameter (-ql) is omitted the default is &quot;WQL&quot;. The operation does not validate the query language parameter but simply passes the input string on to the CIM server </p>
<p> <code>Examples</code><br />
&nbsp;<wbr>&nbsp;<wbr>cimcli xq&nbsp;<wbr>&quot;Select&nbsp;<wbr>*&nbsp;<wbr>from CIM_Something&quot;&nbsp;<wbr>CQL </p>
<p>&nbsp;<wbr>&nbsp;<wbr>cimcli xq&nbsp;<wbr>&quot;Select&nbsp;<wbr>*&nbsp;<wbr>from CIM_blah&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>uses WQL as default query language </p>
<h3>pei pullEnumerateInstances Operation</h3>
<p> Execute the CIM enumeration sequence to pull instances from the server. This compromises the openEnumerateInstances possible followed by pullInstancesWithPath operations. This <code>cimcli</code> operation executes the complete sequence. The syntax for this operation is: </p>
<p> <code>cimcli pei [className] [&lt;option&gt;]*</code> </p>
<p> This enumeration sequence requests instances from the CIM server and displays the returned instances in a user selected format. This is the pull equivalent to the enumerateInstances operation and matches its format but with extra options. </p>
<p> The following options represent specific parameters for this operation: </p>
<p> <code>-nlo</code> not local only operation parameter to false. Note that this negative form for the option is used because the default for local only parameter is true. Thus, not including this parameter means that the parameter is not set. </p>
<p> <code>-iq</code> Boolean (include_Qualifiers) that sets the operation parameter for include_qualifiers to true, </p>
<p> <code>-ic</code> Boolean to set include class origin operation parameter to true. </p>
<p> <code>-di</code> Set deep inheritance operation parameter to true.<br />
&nbsp;<wbr> <code>-o [xml|mof|table]</code> Set the output format for the instances to display the returns as mof </p>
<p> <code>-pl [propertyList]</code> Optional property list for the operation </p>
<p> <code>-ql [filterQueryLanguage]</code> Optional definition of the filter query language used for this operation </p>
<p> <code>-f [filter]</code> Optional filter for the language defined in the -ql option. The response is filtered using this filter specification. See the section Pull Client Operations for more information on query language syntax. </p>
<p> <code>-pt [pullTimeout]</code> The timeout value that <code>cimcli</code> sends to the server as part of the open request. This is the minimum time in seconds that the server will keep the enumeration context open between sending a response and receiving the next request within a single pull sequence. </p>
<p> <code>-mr [maxObjectsToReceive]</code> The maximum number of instances or paths that will be accepted by cimcli before issuing a close operation. </p>
<p> <code>-pullDelay [pullDelayinSec]</code> Delay in seconds that <code>cimcli</code> will execute between each of the operations of the pullsequence. The primary use for this is testing delay issues. </p>
<p> <code>-mo [maxObjectCount]</code> The maximum object count that <code>cimcli</code> ends to the server for each request in an enumeration context. The server returns no more than this number of instances or paths<br />
&nbsp;<wbr>&nbsp;<wbr> It returns the instances found either as MOF, XML, or a table of property values with each property a column in the table depending on the output options parameter. </p>
<p> <code>Example:</code><br />
&nbsp;<wbr>cimcli pei CIM_ComputerSystem -niq -di -mo 100<br />
&nbsp;<wbr>&nbsp;<wbr>This example enumerates CIM_ComputerSystem in the<br />
&nbsp;<wbr>&nbsp;<wbr>namespace root/CIMV2&nbsp;<wbr>(default)&nbsp;<wbr>requesting without<br />
&nbsp;<wbr>&nbsp;<wbr>qualifiers&nbsp;<wbr>(-niq)&nbsp;<wbr>with deepInheritance&nbsp;<wbr>(-di). Each response to <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> cimcli will contain no more than 100 instances</p>
<p>&nbsp;<wbr>cimcli pei CIM_ComputerSystem -ql&nbsp;<wbr>&quot;DMTF:FQL&quot;&nbsp;<wbr>-f&nbsp;<wbr>&quot;Dedicated&nbsp;<wbr>=&nbsp;<wbr>3&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>Enumerate CIM_Computer system in root/CIMV2 and return any <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> instances where the dedicated property equals 3</p>
<p>&nbsp;<wbr>&nbsp;<wbr> </p>
<h3>pni pullEnumerateInstancePaths Operation</h3>
<p> Execute the CIM enumeration sequence to pull instance paths from the server. This compromises the openEnumerateInstancePaths possibly followed by pullInstancePaths operations. This <code>cimcli</code> operation executes the complete sequence. The syntax for this operation is: </p>
<p> <code>cimcli pni [className] [&lt;option&gt;]*</code> </p>
<p> This enumeration sequence requests instance paths from the CIM server and displays the returned instances in a user selected format. </p>
<p> The following options represent specific parameters for this operation: </p>
<p> <code>-nlo</code> not local-only operation parameter to false. Note that this negative form for the option is used because the default for local-only parameter is true. Thus, not including this parameter means that the parameter is not set. </p>
<p> <code>-ql [filterQueryLanguage]</code> Optional definition of the filter query language used for this operation. Required if the -f option is specified. </p>
<p> <code>-f [filter]</code> Optional filter for the language defined in the -ql option. The response is filtered using this filter specification. The query language syntax is documented in the general section above. NOTE: The filter may not be allowed for the paths operations for some servers, specifically OpenPegasus. </p>
<p> <code>-pt [pullTimeout]</code> The timeout value that <code>cimcli</code> sends to the server as part of the open request. This is the minimum time in seconds that the server will keep the enumeration context open between sending a response and receiving the next request within a single pull sequence. </p>
<p> <code>-mr [maxObjectsToReceive]</code> The maximum number of instances or paths that will be accepted by cimcli before issuing a close operation. </p>
<p> <code>-pullDelay [pullDelayinSec]</code> Delay in seconds that <code>cimcli</code> will execute between each of the operations of the pullsequence. The primary use for this is testing delay issues. </p>
<p> <code>-mo [maxObjectCount]</code> The maximum object count that <code>cimcli</code> sends to the server for each request in an enumeration context. The server returns no more than this number of instances or paths<br />
&nbsp;<wbr>&nbsp;<wbr> It returns the instances found either as MOF, XML, or a table of property values with each property a column in the table depending on the output options parameter. </p>
<p> <code>Example:</code><br />
&nbsp;<wbr>cimcli pni CIM_ComputerSystem -n root/testproviders -mo 100<br />
&nbsp;<wbr>&nbsp;<wbr>This example enumerates the paths of CIM_ComputerSystem in the<br />
&nbsp;<wbr>&nbsp;<wbr>namespace root/testProviders&nbsp;<wbr>(default). Each response to <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> cimcli will contain no more than 100 paths</p>
<h3>pa pullAssociators Operation</h3>
<p> Execute the enumeration context that starts with openAssociatorInstances and may continue with pullInstancesWithPath for the target object name. This is similar to the associators operation. </p>
<p> The syntax for this operation is:<br />
&nbsp;<wbr> <code>cimcli pa [objectname] [&lt;option&gt;]*</code> </p>
<p> Note that the objectname may be either a classname or an instancename. If classname is supplied, the interactive mode is used and a list of possible objectnames for the target of the association is presented to the user. If objectname is used, the response is instances of the association that matches the classname. </p>
<p> The options provide the various operation parameters including; </p>
<p> <code>-ac [assocatonClassName]</code> association Class parameter </p>
<p> <code>-rc [resultClassName]</code> resultClass parameter </p>
<p> <code>-r [role]</code> String defining the role parameter for the CIM Operation </p>
<p> <code>-rr [resultrole]</code> resultrole parameter </p>
<p> <code>-ic</code> includeClassOrigin The -ic parameter </p>
<p> <code>-pl [properytlist]</code> Optional PropertyList </p>
<p> <code>-ql [filterQueryLanguage]</code> Optional definition of the filter query language used for this operation. Required if the -f option is specified. </p>
<p> <code>-f [filter]</code> Optional filter for the language defined in the -ql option. The response is filtered using this filter specification. The query language syntax is documented in the general section above. NOTE: The filter may not be allowed for the paths operations for some servers, specifically OpenPegasus. </p>
<p> <code>-pt [pullTimeout]</code> The timeout value that <code>cimcli</code> sends to the server as part of the open request. This is the minimum time in seconds that the server will keep the enumeration context open between sending a response and receiving the next request within a single pull sequence. </p>
<p> <code>-mr [maxObjectsToReceive]</code> The maximum number of instances or paths that will be accepted by cimcli before issuing a close operation. </p>
<p> <code>-pullDelay [pullDelayinSec]</code> Delay in seconds that <code>cimcli</code> will execute between each of the operations of the pullsequence. The primary use for this is testing delay issues. </p>
<p> <code>-mo [maxObjectCount]</code> The maximum object count that <code>cimcli</code> sends to the server for each request in an enumeration context. The server returns no more than this number of instances or paths </p>
<p> <code>Example:</code><br />
&nbsp;<wbr>cimcli pa -n test/providers Test_CLITestProviderClass.Id=<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-ac Test_CLITestProviderLinkClass -rc Test_CLITestProviderClass&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-r child -rr parent -pl requestInputParameters</p>
<p>&nbsp;<wbr><br />
&nbsp;<wbr>defines an associators request where the target object is:<br />
&nbsp;<wbr>&nbsp;<wbr>Test_CLITestProviderClass.Id=&quot;Mike&quot;<br />
&nbsp;<wbr>the associated class is: Test_CLITestProviderLinkClass<br />
&nbsp;<wbr>the associated role is: child<br />
&nbsp;<wbr>the reference role is: parent<br />
&nbsp;<wbr>and the propertylist includes a single property: requestInputParameters<br />
&nbsp;<wbr> </p>
<h3>pan pullAssociatorPaths Operation</h3>
<p> Execute the enumeration context that starts with openAssociatorInstancePaths and may continue with pullInstancesPaths for the target object name. This is similar to the associators operation associatorPaths except that only instances are returned. </p>
<p> The syntax for this operation is: </p>
<p> <code>cimcli pan [objectname] [&lt;option&gt;]*</code> </p>
<p> where objectname can be either a class name or an instance name. If it is a class name, the <code>cimcli</code> interactive mode is used to present a list of possible object paths for the class to the user. </p>
<p> The following options provide the various operation parameters; </p>
<p> <code>-ac [assocatonClassName]</code> association Class parameter </p>
<p> <code>-rc [resultClassName]</code> resultClass parameter </p>
<p> <code>-r [role]</code> String defining the role parameter for the CIM Operation </p>
<p> <code>-rr [resultrole]</code> resultrole parameter </p>
<p> <code>-ql [filterQueryLanguage]</code> Optional definition of the filter query language used for this operation. Required if the -f option is specified. </p>
<p> <code>-f [filter]</code> Optional filter for the language defined in the -ql option. The response is filtered using this filter specification. The query language syntax is documented in the general section above. NOTE: The filter may not be allowed for the paths operations for some servers, specifically OpenPegasus. </p>
<p> <code>-pt [pullTimeout]</code> The timeout value that <code>cimcli</code> sends to the server as part of the open request. This is the minimum time in seconds that the server will keep the enumeration context open between sending a response and receiving the next request within a single pull sequence. </p>
<p> <code>-mr [maxObjectsToReceive]</code> The maximum number of instances or paths that will be accepted by cimcli before issuing a close operation. </p>
<p> <code>-pullDelay [pullDelayinSec]</code> Delay in seconds that <code>cimcli</code> will execute between each of the operations of the pullsequence. The primary use for this is testing delay issues. </p>
<p> <code>-mo [maxObjectCount]</code> The maximum object count that <code>cimcli</code> sends to the server for each request in an enumeration context. The server returns no more than this number of instances or paths </p>
<h3>pr pullreferenceInstances Operation</h3>
<p> Executes the an enumeration sequence that starts with OpenReferenceInstances and may continue with pullReferenceInstances. the sequence returns CIM Instances. It is similar to the references operation in basic parameters except that it returns instances only (it does not return classes as does the references operation). </p>
<p> The syntax for this the operation is: </p>
<p> <code>cimcli pr [objectname] [&lt;option&gt;]*</code> </p>
<p> Note that the objectname may be either a class name or an instance name. If a class name is supplied, the user is queried for the objectname parameter. If objectname is used, the response is instances of the references that match the objectname. </p>
<p> The options specifically used by this operation are: </p>
<p> <code>-r [role]</code> role parameter for the CIM Operation. </p>
<p> <code>-rc [resultClassName]</code> resultClass parameter for the CIM Operation </p>
<p> <code>-iq</code> includeQualifiers (The default is false) </p>
<p> <code>-ic</code> Boolean to set include class origin operation parameter to true. </p>
<p> <code>-pl [propertyList]</code> Optional property list for the operation </p>
<p> <code>-ql [filterQueryLanguage]</code> Optional definition of the filter query language used for this operation. Required if the -f option is specified. </p>
<p> <code>-f [filter]</code> Optional filter for the language defined in the -ql option. The response is filtered using this filter specification. The query language syntax is documented in the general section above. NOTE: The filter may not be allowed for the paths operations for some servers, specifically OpenPegasus. </p>
<p> <code>-pt [pullTimeout]</code> The timeout value that <code>cimcli</code> sends to the server as part of the open request. This is the minimum time in seconds that the server will keep the enumeration context open between sending a response and receiving the next request within a single pull sequence. </p>
<p> <code>-mr [maxObjectsToReceive]</code> The maximum number of instances or paths that will be accepted by cimcli before issuing a close operation. </p>
<p> <code>-pullDelay [pullDelayinSec]</code> Delay in seconds that <code>cimcli</code> will execute between each of the operations of the pullsequence. The primary use for this is testing delay issues. </p>
<p> <code>-mo [maxObjectCount]</code> The maximum object count that<code>cimcli</code>sends to the server for each request in an enumeration context. The server returns no more than this number of instances or paths </p>
<p> <code>Examples:</code><br />
&nbsp;<wbr>cimcli pr CIM_ManagedElement<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>enter the interactive mode and presents the cimcli user with a <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> list of all objectPaths for CIM_ManagedElement from which it<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> builds the openReferenceInstances request.</p>
<h3>prn pullreferencePaths Operation</h3>
<p> Executes an enumeration sequence that startes with openReferencePaths and continues with pullInstancePaths. This operation is the pull parallel of the referenceNames operation. </p>
<p> The syntax for this operation is: </p>
<p> <code>cimcli prn [objectname] [&lt;option&gt;]*</code> </p>
<p> Note that the objectname may be either a class name or a specific instance name. If classname is supplied, the user is queried to select an instance name for the clas name input. If objectname is used, the response is instance names of the references that matches the objectname. </p>
<p> The options specifically used by this operation are: </p>
<p> <code>-r [role]</code> role parameter for the CIM Operation </p>
<p> <code>-rc [resultClassName]</code> resultClass parameter for the CIM Operation </p>
<p> <code>-ql [filterQueryLanguage]</code> Optional definition of the filter query language used for this operation. Required if the -f option is specified. </p>
<p> <code>-f [filter]</code> Optional filter for the language defined in the -ql option. The response is filtered using this filter specification. The query language syntax is documented in the general section above. NOTE: The filter may not be allowed for the paths operations for some servers, specifically OpenPegasus. </p>
<p> <code>-pt [pullTimeout]</code> The timeout value that <code>cimcli</code> sends to the server as part of the open request. This is the minimum time in seconds that the server will keep the enumeration context open between sending a response and receiving the next request within a single pull sequence. </p>
<p> <code>-mr [maxObjectsToReceive]</code> The maximum number of instances or paths that will be accepted by cimcli before issuing a close operation. </p>
<p> <code>-pullDelay [pullDelayinSec]</code> Delay in seconds that <code>cimcli</code> will execute between each of the operations of the pullsequence. The primary use for this is testing delay issues. </p>
<p> <code>-mo [maxObjectCount]</code> The maximum object count that <code>cimcli</code> sends to the server for each request in an enumeration context. The server returns no more than this number of instances or paths </p>
<h3>pxq pullExecQuery Operation</h3>
<p> The pullExecQuery executes an enumeration sequence that opens with the openQueryInstances client request and continues with pullInstances if required. This operation is parallel to the execQuery <code>cimcli</code> operation. </p>
<p> <code>Example:</code><br />
cimcli pxq&nbsp;<wbr>&lt;query_filter&gt;&nbsp;<wbr>&lt;query_language&gt;&nbsp;<wbr>[&lt;option&gt;]* The query_filter and the query_language may be supplied directly on the command line as parameter or as options (-f for the query filter and -ql for query language. </p>
<p> The query languages used for this operation are languages like WQL and CQL. they are NOT FQL which supports only the enumerate, associator, and reference type operations. </p>
<p> The pullExecQuery CIM Operation is executed directly with the input parameters or options. If neither a query_filter parameter or option are supplied <code>cimcli</code> returns an error. If the query_language parameter (-ql) is omitted the default is &quot;WQL&quot;. The operation does not validate the query language parameter but simply passes the input string on to the CIM server. </p>
<p> Today this operation does not support the openQueryInstances client request parameter returnQueryResultClass that requests that the cimserver generate a class corresponding to the returned objects. </p>
<p> <code>Examples</code><br />
&nbsp;<wbr>&nbsp;<wbr>cimcli pxq&nbsp;<wbr>&quot;Select&nbsp;<wbr>*&nbsp;<wbr>from CIM_Something&quot;&nbsp;<wbr>CQL </p>
<p>&nbsp;<wbr>&nbsp;<wbr>cimcli pxq&nbsp;<wbr>&quot;Select&nbsp;<wbr>*&nbsp;<wbr>from CIM_blah&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>uses WQL as default query language </p>
<h3>son Operation (Deprecated)</h3>
<p> Set the CIM server statistics to enabled by doing a modify instance of the CIM_ObjectManager instance that defines the server. This depends on the server having implemented statistics and having also implemented the functionality of enabling and disabling statistics through setting this property in CIM_ObjectManager. This should be considered a temporary operation in <code>cimcli</code> until a more permanent utility is provided with OpenPegasus to manage this type of functionality. The corresponding operation soff will attempt to disable statistics on the server. This works with OpenPegasus servers starting with version 2.5.1. </p>
<p> <code>DEPRECATED to be replaced at some time in the future.</code> </p>
<p> The syntax of the operation is: </p>
<p> <code>cimcli son</code> </p>
<h3>soff Operation (Deprecated)</h3>
<p> See the operation son. This is the corresponding operation to turn off statistics in the server. </p>
<p> DEPRECATED to be replaced by at some time in the future. </p>
<p> The syntax of the operation is: </p>
<p> <code>cimcli soff</code> </p>
<h3>ns enumeratenamespaces Operation</h3>
<p> Request an Enumeration of all the namespaces in the target CIM Server. This command uses both the CIM_Namespace class and if that fails, the __Namespace class to determine the list of namespaces. </p>
<p> RETURN &#8211; It displays a list of the namespace names returned by the CIM Server. </p>
<p> The syntax for this operation is: </p>
<p> <code>cimcli ns [&lt;option&gt;]*</code> </p>
<p> Note that since this operation enumerates namespaces, the namespace option (-n) is not used. </p>
<p> <code>Examples</code><br />
cimcli ns<br />
&nbsp;<wbr>request list of all namespaces from the CIM server </p>
<h3>cci countInstances Operation</h3>
<p> Counts the number of instances by class in a namespace (if no [OperationTarget] is specified or of the subclasses of the class specified by [OperationTarget]. </p>
<p> <code>WARNING:</code> This operation could cause problems if executed against a server which returns very large numbers of instances since it retrieves all of the instances and counts them in cimcli. </p>
<p> This operation counts the number of instances of each class in the class hiearchy. Note that an enumerateInstances returns instances of all classes in a hiearchy but that this operation actually counts the number of instances of each class separately. </p>
<p> The syntax for this operation is:</p>
<dl>
<dt>
<dd> <code>cimcli cci &lt;[targetClass]&gt; [option]&#8230;</code></dl>
<p> The output option does not apply. The output is always a text display of classes with instances and count of number of instances. All association class instances are suffixed with an asterick(*). </p>
<p> <code>Examples</code><br />
&nbsp;<wbr>cimcli cci </p>
<p>&nbsp;<wbr>cimcli cci CIM_ComputerSystem -n PG_InterOp -l localhost </p>
<h3>ct classtree Operation</h3>
<p> Display the class hiearchy for the class provided as a parameter with the operation request. </p>
<p> This operation can display either the subclass tree or if the -nlo (no local only) option is specified, the superclass tree for the defined class. Note that the class parameter is required if the superclass tree is requested but not if the subclass tree is requested. </p>
<p> In addition, if the class is an association class, the reference classes are included in the display if text output is requested (-di). </p>
<p> The syntax is as follows:</p>
<dl>
<dt>
<dd> <code>cimcli ct &lt;classname&gt; [&lt;option&gt;]*</code></dl>
<p> <code>Examples</code><br />
&nbsp;<wbr>cimcli ct<br />
&nbsp;<wbr>&nbsp;<wbr>displays class tree for one namespace<br />
&nbsp;<wbr>cimcli ct CIM_ComputerSystem<br />
&nbsp;<wbr>&nbsp;<wbr>displays class tree starting at CIM_ComputerSystem<br />
&nbsp;<wbr>cimcli ct CIM_ComputerSystem -nlo<br />
&nbsp;<wbr>&nbsp;<wbr>displays a tree of the superclasses of CIM_ComputerSystem<br />
&nbsp;<wbr>cimcli ct CIM_ComputerSystem -o txt<br />
&nbsp;<wbr>&nbsp;<wbr>displays class tree startign at CIM_Computer system and for<br />
&nbsp;<wbr>&nbsp;<wbr>any association class displays the class defined for each<br />
&nbsp;<wbr>&nbsp;<wbr>reference property </p>
<h2>OPTIONS LIST</h2>
<p> There are a significant number of options to this utility, some if which provide specific information for one or more commands and some of which are universal across all of the commands. In general, the program does not check for spurious options so that if you input an option that is not used by a particular operation, it is simply ignored. Note that some of the options require parameters. </p>
<p> The following is an alphabetic list of the options:</p>
<dl>
<dt><code>-ac [assocatonClassName]</code></p>
<dd> The association class name parameter defines an assocClass string for Associator calls (associators and associatornames). Default(). </p>
<p> <code>Example:</code><br />
-ac CIM_ManagedElement</p>
<dt><code>-ar association_role_name</code></p>
<dd> Defines an association role for associator operations. Example: -ar dependent. This optional parameter is used only with the association CIM Operations. </p>
<dt><code>&#8211;cert [certificateFilePath]</code></p>
<dd> Defines a certificate to be used with the client connect if the -s option is set. This is optional and used only with the -s and &#8211;key options. The parameter value certificateFilePath is required with the parameter and defined the file containing the certificate. If this parameter exists the &#8211;key parameter must also exist to be a valid SSL request. This represents the X509 certificate of the client that will be sent to the server during an SLL handshake if the server requests it. </p>
<dt><code>&#8211;count [object_count]</code></p>
<dd> Defines an expected count of objects to be returned in the response. <code>cimcli</code> is terminated with an error exit if the number of objects returned does not match the object_count supplied with the option. This test can be used in batch files to test for number of objects returned by an operation. In addition to the error status code, a message of the general form:<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;Failed count test. Expected=&nbsp;<wbr>xx. Received=&nbsp;<wbr>yy&quot; is output to cerr. </p>
<p> <code>Example:</code><br />
cimcli en CIM_ManagedElement -count 100 </p>
<p>&nbsp;<wbr>If the count of instances returned is not equal to 100,<br />
&nbsp;<wbr>cimcli exits with error code 60 and the Failed count test&nbsp;<wbr><br />
&nbsp;<wbr>error message.</p>
<dt><code>-delay [time in seconds]</code></p>
<dd> Delay between connection and request . Default(0). example -delay 3 delays 3 seconds between the call and the transmission of the actual CIM operation. This is used only in some testing environments.</p>
<dt><code>-di</code></p>
<dd> Specifies the boolean parameter deepInheritance parameter for selected commands. Setting this options causes the deepinheritance=true to be transmitted for the operation. Note that this means different things to different commands and is used only with the enumerate commands. </p>
<dt><code>-d</code></p>
<dd> More detailed debug messages from <code>cimcli</code>. This can be useful in the case where the user is debugging CIM functionality. </p>
<dt><code>-h &lt;command-name&gt;</code></p>
<dd> Prints the help for a particular operation including the definition of the operation, applicable options, and examples of usage.</p>
<dl>
<dt>
<dd> cimcli -h gc </p>
<p>&nbsp;<wbr>show information on the getclass operation</dl>
<dt><code>&#8211;help</code></p>
<dd> Prints full help message with commands, options, examples. </p>
<dt><code>-ho</code></p>
<dd> Prints list of <code>cimcli</code> options with definitions. </p>
<dt><code>-hc</code></p>
<dd> Print <code>cimcli</code> Operation command list. This list includes the CIM Operatons defined by the CIM Operations specification and other operations that were felt to be useful in testing CIM environments. It includes defintion and examples of each operation. </p>
<dt><code>-ic</code></p>
<dd> Boolean to set include class origin operation parameter to true. </p>
<dt><code>-f [filter]</code></p>
<dd> Defines a filter to use for query. One String input . Default() </p>
<dt><code>-o [ xml | mof | table ]</code></p>
<dd> Output in xml, mof, or table format. Default(mof) if the -o options is not included. Note that the output formatting is only for CIM objects (classes and instances). Object paths are always displayed as strings. </p>
<p> The meaning of the keywords is:</p>
<dt>
<dd> /fBxml.fR Display class or instance in CIM-XML format /fBmof/fR Display class or instance as MOF /fBtable/fR Display instance as a table with one column per property an a row for each instance returned. This format does NOT wrap at 80 columns or wrap long strings. </p>
<p>&nbsp;<wbr>-o xml<br />
&nbsp;<wbr>display the output in xml </p>
<dt><code>-iq</code></p>
<dd> Specifies the includeQualifiers operation input parameter for selected commands.Since the CIM/XML default for this parameter is true for some operations (class operations) and false for others (instance operations), the option is useful only for instance operations. Also the includeQualifiers parameter has been deprecated in the CIM/XML specification so the results for instance operations is undetermined. See also -niq for the includeQualifiers parameter for class operations. </p>
<dt><code>&#8211;key [client key file path]</code></p>
<dd> Defines a Client private key. This is optional and only has an effect on connections made over HTTPS using the -ssl option. If this parameter exists the client certificate parameter (&#8211;cert) must also exist to be usable. </p>
<dt><code>-l [location]</code></p>
<dd> Define CIM Server host address for the operation. This includes either name or IP address and optional port number(HostName:port). The default is localhost:5988. If name is used without port, port 5988 is assumed. Examples include -l fred, -l fred:9999, -l 10.1.134.66 -l 10.1.134.123:5977 </p>
<dt><code>-lo</code></p>
<dd> Specifies the localOnly operation parameter for selected commands if the option is set. See the commands for more information. This option is Deprecated in favor of the -nlo because the default for local only is on so that generally the -lo is simply the default. We recommend using -nlo to turn off local only. </p>
<dt><code>-n [namespace]</code></p>
<dd> Defines the namespace for the operation.host name. The default is root/cimv2. Example -n root/PG_Interop sets the root/PG_Interop namespace as the namespace for the current operation. </p>
<dt><code>-p [password]</code></p>
<dd> Allows input of a password for server authentication of the command. ( ex. -p 12345678). The default is that the command is submitted with no password. </p>
<dt><code>-u [User]</code></p>
<dd> Defines user name for CIM Server authentication. Default is no user name and no authentication. ( ex -u john) Default is no user name and no authentication from the client. </p>
<dt><code>-lo </code></p>
<dd> DEPRECATED. This was used to set LocalOnly. However, default should be true and we cannot use True as default. See -nlo. Default(true). </p>
<dt><code>-nlo</code></p>
<dd> When set, sets LocalOnly = false on the CIM operation . Default(false) meaning that the operation sets LocalOnly = true.. </p>
<dt><code>-ic</code></p>
<dd> Sets includeClassOrigin = true for operation that support this parameter (i.e. get and enumerate classes and instances, associators, and references operations). Note that the class origin information is only output for the -o xml output operation since class origin is not part of the MOF format.</p>
<dt><code>-niq</code></p>
<dd> Sets includeQualifiers = false on operations. Default(false). </p>
<dt><code>-pl [propertyList]</code></p>
<dd> Defines a propertyName List which is an optional parameter for some CIM Operations. Format is p1,p2,p3 (without spaces). Default is that the property list is set to NULL indicating normally that the operation should return all properties. The property list typically has 3 possibilities 1) empty which means return no properties, 2) list of properties to be returned, 3) NULL which means return all properties. Since the default is NULL, not applying the option means that all properties are being requested. To set this parameter to empty use the form -pl &quot;&quot;. </p>
<dt><code>-r [role]</code></p>
<dd> Defines a role string for reference role parameter. Default() </p>
<dt><code>-rc [resultClassName]</code></p>
<dd> Defines a resultClass string for References and Associators. Default() </p>
<dt><code>-rr [resultRole]</code></p>
<dd> Defines a role string for associators operation resultRole parameter.<br />
&nbsp;<wbr></p>
<dt><code>&#8211;setRtnHostNames [SubstituteHostName]</code></p>
<dd> String option with a required parameter that set a substitute host name which <code>cimcli</code> will insert into returned objects to replace host names returned from the server. This option was defined because the object paths/references returned by the CIM Server may include the host name as part of the returned object path which makes it difficult to compare the returned paths to a defined path. Using this option forces any returned host names to be changed to the string parameter supplied with the option. </p>
<dt><code>&#8211;sum</code></p>
<dd> Displays only summary counts for enumerations, associators, etc.This option is used to with the repeat option to repeat an operation without getting the full return display. It reduces the display to summary information. It is often used with the time option &#8211;t to generate time for execution information on many repetitions of a command. </p>
<dt><code>&#8211;timeout [seconds]</code></p>
<dd> Set the connection timeout in seconds. If not set, the timeout is the default Pegasus client timeout which for Pegasus is normally to about 30 seconds. This option executes the client call to set timeout. </p>
<dt><code>-trace [trace_level]</code></p>
<dd> Set Pegasus Common Components Trace. Sets the Trace level. 0 is off. Default(0). The trace level can be set to 0 &#8211; 5. Note that since mose trace definitions have been removed from <code>cimcli</code>, this is of little value. </p>
<dt><code>&#8211;truststore [clientTrustStorePath]</code></p>
<dd> The value of this parameter specifies a file or directory that is the truststore that the client uses to verify server certificates. The default is that no truststore is defined so the client does not verify certificates from the server. This parameter is used only if cimcli is compiled with SSL enabled and the -s option (use SSL) is specified for the request. </p>
<dt><code>&#8211;v</code></p>
<dd> Displays <code>cimcli</code> and Pegasus software Version. </p>
<dt><code>-v</code></p>
<dd> Verbose Display. Includes Detailed parameter Input display and display of each operation in an enumeration sequence (open, pull, close). Default(false). Outputs extra information about the parameters actually used in the request and the return from the operation. This is primarily a debugging tool. for enumeration context it outputs information on each request/response in the sequence including timing information. </p>
<dt><code>&#8211;r [repeat_count]</code></p>
<dd> Number of times to repeat the function. Zero means one time. The option can be used to repeat an operation within a single call to <code>cimcli</code>. It simply repeats the operation defined the number of times defined by the repeat_count within the same connection. Thus, it establishes the connection executes the operation repeat_count times and then terminates. It can be used with the &#8211;time option to measure execution times for many repetitions of an operation. </p>
<dt><code>-s</code></p>
<dd> Boolean option that specifies that the Client should attempt to connect over the secure connection using SSL. This option causes <code>cimcli</code> to modify the client connect call to set the SSLContext option to the certificate defined with the &#8211;cert and &#8211;key options. If this option is set but neither the &#8211;cert or &#8211;key options are included, the SSLContext for the connect call is submitted with the Cert and key marked NULL. </p>
<p> NOTE: since SSL is considered a compilable option with <code>cimcli</code>, these options may not even exist in a Pegasus environment that was compiled with the SSL capabilities disabled. </p>
<dt><code>&#8211;sort</code></p>
<dd> Sort the output objects before display for multi-object outputs such as enumerates, references, associations, and their corrsponding &#8230;names operations and for the enumerateQualifierDecls. Whereever <code>cimcli</code> delivers multiple entities in the response, the use of this option tells <code>cimcli</code> to attempt to sort the output entities. Generally the sort order is assending order using a) class name for operations that return classes and b) CIM Object Path for operations that return instances. </p>
<dt><code>&#8211;t</code></p>
<dd> Measure time for the operation and present results. When set the response time for the operation is presented with the command output. If the &#8211;r (repeat) option is set, minimum, maximum, and average times are presented. Note that the time for the operation itself is presented in addition to the overall time for connect, operation, and disconnect. If statistics are being gathered by the server, setting this option also presents the server time, and the client round trip time which are calculated by the server and client infrastructure. </p>
<dt><code>-x</code></p>
<dd> Output objects in xml instead of mof format. Default(false) </p>
<dt><code>-pt [pullTimeout]</code></p>
<dd> The timeout value that <code>cimcli</code> sends to the server as part of the open request. This is the minimum time in seconds that the server will keep the enumeration context open between sending a response and receiving the next request within a single pull sequence. </p>
<dt><code>-mr [maxObjectsToReceive]</code></p>
<dd> The maximum number of instances or paths that will be accepted by <code>cimcli</code> before issuing a close operation. </p>
<dt><code>-pullDelay [pullDelayinSec]</code></p>
<dd> Delay in seconds that <code>cimcli</code> will execute between each of the operations of the pull sequence. The primary use for this is testing delay issues. </p>
<dt><code>-mo [maxObjectCount]</code></p>
<dd> The maximum object count that <code>cimcli</code> sends to the server for each request in an enumeration context (one of the pull&#8230; operations. The server returns no more than this number of instances or paths </p>
</dl>
<h2>EXAMPLES</h2>
<p> NOTE: Many examples are available for each operation through the -h command line options. </p>
<p> Execute an enumerateinstancenames CIM operation for the pg_computersystem Class: </p>
<p>&nbsp;<wbr>cimcli enumerateinstancenames pg_computersystem </p>
<p>or </p>
<p>&nbsp;<wbr>cimcli ei pg_computersystem </p>
<p> Enumerate the class names from the default namespace &quot;root/cimv2&quot;: </p>
<p>&nbsp;<wbr>cimcli enumerateclassnames &#8212; Enumerate classnames from root/cimv2. </p>
<p> Enumerate class names from the namespace &quot;root&quot;: </p>
<p>&nbsp;<wbr>cimcli ec&nbsp;<wbr>/n root &#8212; Enumerate classnames from namespace root. </p>
<p>&nbsp;<wbr>cimcli ec -o xml&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8212; Enumerate classes with XML output starting at root. </p>
<p>&nbsp;<wbr>cimcli enumerateclasses CIM_ComputerSystem -di<br />
&nbsp;<wbr>&#8212; Enumerate classes starting at CIM_ComputerSystem and the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>remainder of the class hiearchy&nbsp;<wbr>(-di)&nbsp;<wbr>with mof output of the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>classes. </p>
<p>&nbsp;<wbr>cimcli getclass CIM_door -a -u guest -p guest<br />
&nbsp;<wbr>&#8212; Get class with authentication set and user&nbsp;<wbr>=&nbsp;<wbr>guest, password&nbsp;<wbr>=&nbsp;<wbr>guest. </p>
<p>&nbsp;<wbr>cimcli rn TST_Person.name=@MIKE@&nbsp;<wbr>-n root/sampleprovider -rc TST_Lineage. </p>
<p>&nbsp;<wbr>cimcli ec -o XML &#8212; enumerate classes and output XML rather than MOF. </p>
<p>&nbsp;<wbr>cimcli getqualifiers &#8212; Get the qualifiers in mof output format </p>
<h2>RETURN VALUE</h2>
<p> <code>cimcli</code> returns a significant number of error codes as follows: </p>
<p> <code>0</code> Successful execution of the operation. </p>
<p> <code>1-49</code> A CIM Operation executed as part of the <code>cimcli</code> operation returned a CIM Exception as defined in the DMTF CIM Operations over HTTP specification. The status code of the error is returned. While today only not all of the numbers from 1 to 49 are used for CIM Status errors, <code>cimcli</code> has reserved this set of numbers with the expectation that this list will expand in the future. </p>
<p> <code>cimcli</code> will not return any error codes in this range that are not specifically defined by DMTF error status codes and generated by the CIM Operation calls. </p>
<p> <code>50</code> Pegasus Exception encountered during execution of Pegasus Functions </p>
<p> <code>51</code> <code>cimcli</code> general error not covered by other errors </p>
<p> <code>52</code> Unknown exception occurred during execution of the operation </p>
<p> <code>53</code> Command line or configuration file input parsing error. </p>
<p> <code>54</code> Connection to server failed error. </p>
<p> <code>60</code> <code>cimcli</code> failed a compare with one of the test operations such as testInstance. The returned entity did not match the properties of the object defined by the input parameters. </p>
<p> <code>70</code> <code>cimcli</code> internal error that cannot be attributed to external issues such as commmand line input or server response. This usually indicates a bug in <code>cimcli</code>. </p>
<h2>AUTHOR</h2>
<p> Karl Schopmeyer k.schopmeyer [at] opengroup.org </p>
<h2>Index</h2>
