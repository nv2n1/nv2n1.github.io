---
title: "cimprovider(1)"
name: "cimprovider"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cimprovider/"
description: "cimprovider – disable, enable, remove , group, list or display status of registered CIM providers or CIM provider modules"
---

<h2>NAME</h2>
<p> cimprovider &#8211; disable, enable, remove , group, list or display status of registered CIM providers or CIM provider modules</p>
<h2>SYNOPSIS</h2>
<p> <code>cimprovider</code> <code>-d</code> <code>-m</code> module </p>
<p> <code>cimprovider</code> <code>-e</code> <code>-m</code> module </p>
<p> <code>cimprovider</code> <code>-r</code> <code>-m</code> module [ <code>-p</code> provider ] </p>
<p> <code>cimprovider</code> <code>-g</code> group <code>-m</code> module </p>
<p> <code>cimprovider</code> <code>-l</code> [ <code>-s</code> | <code>-f</code> | <code>-m</code> module ] </p>
<p> <code>cimprovider</code> <code>-h</code> </p>
<p> <code>cimprovider</code> <code>&#8211;help</code> </p>
<p> <code>cimprovider</code> <code>&#8211;version</code> </p>
<h3>Remarks</h3>
<p> The <code>-l</code> option for this command can be executed by any user(s). All other options require superuser permissions. </p>
<p> This command disables, enables, or removes one CIM provider module or CIM provider at a time.</p>
<h2>DESCRIPTION</h2>
<p> The <code>cimprovider </code> command provides a command line interface to disable, enable, unregister, group and list registered CIM providers. If a CIM provider is disabled, the CIM Server rejects any requests to the provider. If a CIM provider is enabled, the CIM Server forwards requests to the provider. And if a CIM provider is unregistered, the CIM Server will no longer have any information about the provider. </p>
<p> In order to use the <code>cimprovider </code> command, <code>cimserver</code> has to be running and the specified provider module (a grouping of providers in the same shared library) or provider has to be registered with WBEM Services. </p>
<p> The first form of <code>cimprovider </code> disables the specified provider module. When a specified provider module is in the disabled state, any new requests to the providers that are contained in the specified provider module will be rejected. </p>
<p> The second form of <code>cimprovider </code> enables the providers that are contained in the specified provider module. The providers that are contained in the specified provider module are now ready to accept new requests. </p>
<p> The third form of <code>cimprovider </code> removes (un-registers) the specified provider module and all of its contained providers or the specified provider in the specified provider module. Once removed, a provider or provider module must be re-registered (typically by loading its registration schema via the <code>cimmof </code> command). </p>
<p> The fourth form of <code>cimprovider</code> sets the provider module group. If the provider module is active, provider module is disabled first, group is set and enabled again. If group name is <code>CIMServer,</code> provider module is loaded into <code>CIMServer</code> process depending on <code>UserContext</code> value. Specify empty string to remove from grouping. </p>
<p> The last form of <code>cimprovider </code> lists all the registered provider modules and module status or all the providers in the specified provider module. To list all providers in all modules, issue a <code>cimprovider -l </code> command, followed by <code>cimprovider -l -m </code> for each listed module. </p>
<p> The following provider module status values are defined:</p>
<dl>
<dt><code>OK</code></p>
<dd> The provider module is enabled.</p>
<dt><code>Stopping</code></p>
<dd> The provider module is in the process of being disabled.</p>
<dt><code>Stopped</code></p>
<dd> The provider module is disabled.</p>
<dt><code>Degraded</code></p>
<dd> A failure was detected in an out-of-process provider module. Disable and re-enable the provider module to ensure any active indication subscriptions are being served.</p>
<dt><code>Error</code></p>
<dd> An invalid registration instance was encountered upon CIM Server initialization.</dl>
<p> Specifying no options with the <code>cimprovider </code> command displays the command usage.</p>
<h3>Options</h3>
<p> The <code>cimprovider </code> command recognizes the following options:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-d</code></p>
<dd> Disables the specified CIM provider <i>R module . </i> If user(s) try to disable a module that is already disabled, an error message is returned and no action is taken.</p>
<dt><code>-e</code></p>
<dd> Enables the specified CIM provider <i>R module . </i> If user(s) try to enable a module that is already enabled or try to enable a module that is disabling, an error message is returned and no action is taken.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Display command usage information.</p>
<dt><code>-l </code></p>
<dd> Displays all the registered provider modules.</p>
<dt><code>-m</code> module</p>
<dd> Specifies the provider <i>module</i> for the operation.</p>
<dt><code>-p</code> provider</p>
<dd> Specifies the <i>provider</i> for the operation.</p>
<dt><code>-r</code></p>
<dd> Removes the specified provider <i>module </i> and all of its contained providers. If <i>provider</i> is specified, removes the specified <i>provider</i> in the specified provider <i>module</i> (not affecting any other providers in that module).</p>
<dt><code>-g</code></p>
<dd> Sets the CIM provider module <i>group.</i> Specify empty string to remove from <i>grouping.</i> If the <i>provider module</i> is active, <i>provider module</i> is disabled first, <i>group</i> is set and enabled again. All <i>provider modules</i> with the same <i>group</i> name are loaded into a single agent process except when overridden by specific <i>UserContext</i> values. If <i>group</i> name is <i>CIMServer</i> , <i>provider module</i> is loaded into <i>CIMServer process depending on </i> <i>UserContext</i> value.</p>
<dt><code>-s</code></p>
<dd> Displays the status of provider modules.</p>
<dt><code>-f</code></p>
<dd> Displays the full status of provider modules with group name.</p>
<dt><code>&#8211;version</code></p>
<dd> Display CIM Server version number.</dl>
</dl>
<h2>EXIT STATUS</h2>
<p> When an error occurs, an error message is written to stderr and an error value 1 is returned. The following return values are returned:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>0</code></p>
<dd> Successful completion</p>
<dt><code>1</code></p>
<dd> Error</dl>
</dl>
<h2>USAGE NOTES</h2>
<p> The <code>cimprovider </code> command requires that the CIM Server is running. If an operation requires more than two minutes to be processed, the <code>cimprovider </code> command prints a timeout message and returns an error value.</p>
<h2>EXAMPLES</h2>
<p> Disable provider module &quot;OperatingSystemProvider&quot; and all of its contained providers (placing them in a stopped state).</p>
<dl>
<dt>
<dd> <code>cimprovider -d -m OperatingSystemProvider</code></dl>
<p> Enable provider module &quot;OperatingSystemProvider&quot; and all of its contained providers (placing them in an OK state).</p>
<dl>
<dt>
<dd> <code>cimprovider -e -m OperatingSystemProvider</code></dl>
<p> Remove (un-register) the &quot;OperatingSystemProvider&quot; provider module and all of its contained providers.</p>
<dl>
<dt>
<dd> <code>cimprovider -r -m OperatingSystemProvider</code></dl>
<p> Remove (un-register) the &quot;PG_OperatingSystemProvider&quot; provider that is contained in the &quot;OperatingSystemProvider&quot; provider module.</p>
<dl>
<dt>
<dd> <code>cimprovider -r -m OperatingSystemProvider -p PG_OperatingSystemProvider</code></dl>
<p> List the registered provider modules.</p>
<dl>
<dt>
<dd> <code>cimprovider -l</code></dl>
<p> List the registered provider modules and their status (such as OK, Stopping, Stopped).</p>
<dl>
<dt>
<dd> <code>cimprovider -l -s</code></dl>
<p> List the registered providers which are contained in the &quot;OperatingSystemProvider&quot; provider module.</p>
<dl>
<dt>
<dd> <code>cimprovider -l -m OperatingSystemProvider</code></dl>
<p> Set the group name of the &quot;OperatingSystemProvider&quot; provider module to &quot;CIMServer&quot;.</p>
<dl>
<dt>
<dd> <code>cimprovider -g CIMServer -m OperatingSystemProvider</code></dl>
<p> Remove &quot;OperatingSystemProvider&quot; provider module from grouping.</p>
<dl>
<dt>
<dd> <code>cimprovider -g -m OperatingSystemProvider</code></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cimmof/">cimmof</a>(1), <a href="/docs/linux/man/1-cimserver/">cimserver</a>(1). </p>
<h2>Index</h2>
