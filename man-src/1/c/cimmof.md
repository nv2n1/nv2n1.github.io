---
title: "cimmof(1)"
name: "cimmof"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cimmof/"
description: "cimmof – compile MOF files into the CIM Repository"
---

<h2>NAME</h2>
<p> cimmof &#8211; compile MOF files into the CIM Repository</p>
<h2>SYNOPSIS</h2>
<p> <code>cimmof</code> <code>-h</code> | <code>&#8211;help</code> </p>
<p> <code>cimmof</code> <code>&#8211;version</code> </p>
<p> <code>cimmof</code> [ <code>-w</code> ] [ <code>-E</code> ] [ <code>-uc</code> ] [ <code>-aE | -aV | -aEV</code> ] [ <code>-I</code> path ]<br />
&nbsp;<wbr>[&nbsp;<wbr><code>-n</code>&nbsp;<wbr>namespace&nbsp;<wbr>]&nbsp;<wbr>[&nbsp;<wbr><code>&#8211;namespace</code>&nbsp;<wbr>namespace&nbsp;<wbr>]&nbsp;<wbr>[&nbsp;<wbr><code>&#8211;xml</code>&nbsp;<wbr>]&nbsp;<wbr><br />
&nbsp;<wbr>[&nbsp;<wbr><code>&#8211;trace</code>&nbsp;<wbr>]&nbsp;<wbr>[&nbsp;<wbr>mof_file &#8230;&nbsp;<wbr>]</p>
<h3>Remarks</h3>
<p> Only a superuser or user with write access to the default or specified namespace can run the <code>cimmof</code> command to compile MOFs in the CIM Repository. </p>
<p> Superclasses must be compiled before subclasses, else the compile will fail. </p>
<p> It is strongly recommended that MOF files include all necessary subclasses, so they can compile properly even if certain classes are not in the CIM Repository.</p>
<h2>DESCRIPTION</h2>
<p> The <code>cimmof</code> command is the command line interface to the Managed Object Format (MOF) Compiler. The MOF Compiler is a utility that compiles MOF files (using the MOF format defined by the DMTF CIM Specification) into CIM classes and instances that are stored in the CIM Repository. </p>
<p> The <code>cimmof</code> command can be used to compile MOF files at any time after installation. If no input file is specified, stdin is used as the input. </p>
<p> The MOF Compiler requires that the input MOF files be in the current directory or that a fully qualified path be given. To simplify the specification of multiple MOF files in the <code>cimmof</code> command line, the MOF Compiler allows compiling from files containing a list of MOF files using the include pragma (as shown below).</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>#pragma include (application.mof)</code></p>
<dt><code>#pragma include (server.mof)</code></p>
<dd></dl>
</dl>
<p> MOF files using the include pragma must be in the current directory or in a directory specified by the <code>-I</code> command line option. </p>
<p> The <code>-n</code> option can be used to specify a <i>R namespace </i> in which the CIM classes and instances will be compiled. If this option is not specified, the default <i>R namespace </i> is root/cimv2 (with the exception of provider registration schemas). </p>
<p> For provider registration schemas, if the <code>-n</code> option is not specified, the default <i>R namespace </i> is root/PG_InterOp. If <code>-n</code> option is specified, the <i>R namespace </i> specified must be root/PG_InterOp, otherwise, the error message &quot;The requested operation is not supported.&quot; is returned. For provider MOFs, the <i>R namespace </i> specified must match one of the namespaces specified in the PG_ProviderCapabilities class schema definition.</p>
<h3>Options</h3>
<p> The <code>cimmof</code> command recognizes the following options:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-aE</code></p>
<dd> Allow Experimental Schema changes.</p>
<dt><code>-aEV</code></p>
<dd> Allow both Experimental and Version Schema changes.</p>
<dt><code>-aV</code></p>
<dd> Allow both Major and Down Revision Schema changes.</p>
<dt><code>-E</code></p>
<dd> Syntax check only</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Display command usage information.</p>
<dt><code>-I</code> path</p>
<dd> Specify the path to included MOF files. This path may be relative or absolute.</p>
<dt>
<dd> If the input MOF file has include pragmas and the included files do not reside in the current directory, the directive must be used to specify a path to them on the <code>cimmof</code> command line.</p>
<dt><code>-n</code></p>
<dd> Override the default CIM Repository namespace. The <i>namespace </i> specified must be a valid CIM namespace name. For the definition of a valid CIM namespace name, refer to the Administrator&#8217;s Guide. For provider registration schemas, the <i>namepace</i> specified must be root/PG_InterOp.</p>
<dt><code>&#8211;namespace</code></p>
<dd> Override the default CIM Repository namespace. The <i>namespace </i> specified must be a valid CIM namespace name. For the definition of a valid CIM namespace name, refer to the Administrator&#8217;s Guide. For provider registration schemas, the <i>namepace</i> specified must be root/PG_InterOp.</p>
<dt><code>&#8211;trace</code></p>
<dd> Trace to file (default to stdout)</p>
<dt><code>-uc</code></p>
<dd> Allow update of an existing class definition.</p>
<dt><code>&#8211;version</code></p>
<dd> Display CIM Server version.</p>
<dt><code>-w</code></p>
<dd> Suppress warning messages.</p>
<dt>
<dd> When compiling the MOF files, if there are CIM elements (such as classes, instances, properties, or methods) defined in the MOF files which already exist in the CIM Repository, the <code>cimmof</code> command returns warning messages. The <code>-w</code> option can be used to suppress these warning messages.</p>
<dt><code>&#8211;xml</code></p>
<dd> Output XML only, to stdout. Do not update repository.</dl>
</dl>
<h2>EXIT STATUS</h2>
<p> The <code>cimmof</code> command returns one of the following values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>0</code></p>
<dd> Successful completion</p>
<dt><code>1 </code></p>
<dd> Error</dl>
</dl>
<p> When an error occurs, an error message is written to stderr and an error value of 1 is returned.</p>
<h2>USAGE NOTES</h2>
<p> The <code>cimmof</code> command requires that the CIM Server is running. If an operation requires more than two minutes to be processed, the <code>cimmof</code> command prints a timeout message and returns an error value.</p>
<h2>DIAGNOSTICS</h2>
<p> <code>Error trying to create Repository in path localhost:5988: Cannot connect to: localhost:5988 Failed to set DefaultNamespacePath.</code></p>
<dl>
<dt>
<dd> The CIM Server is not running. Start the CIM Server with the command and re-run <code>cimmof .</code></dl>
<p> If the MOF Compiler detects an error in the MOF file while parsing the file, a parsing error is returned with the line number of the MOF file containing the error. </p>
<p> <code>Operation cannot be carried out since the specified superclass does not exist. </code></p>
<dl>
<dt>
<dd> The MOF Compiler compiled a MOF file with superclasses that were not in the CIM Repository.</dl>
<p> For a list of possible error messages that may be returned, refer to the Chapter on WBEM messages in the Administrator&#8217;s Guide.</p>
<h2>EXAMPLES</h2>
<p> Compile a MOF file into the default namespace in the CIM Repository, issue the <code>cimmof</code> command with no options.</p>
<dl>
<dt>
<dd> <code>cimmof processInfo.mof</code></dl>
<p> Compile the MOF files into the &quot;root/application&quot; namespace.</p>
<dl>
<dt>
<dd> <code>cimmof -nroot/application test1.mof test2.mof</code></dl>
<p> Compile the MOF file defined in the directory ./MOF with the name CIMSchema25.mof, and containing include pragmas for other MOF files also in the ./MOF directory.</p>
<dl>
<dt>
<dd> <code>cimmof -w -I./MOF MOF/CIMSchema25.mof</code></dl>
<p> Display Usage Info for the <code>cimmof</code> command.</p>
<dl>
<dt>
<dd> <code>cimmof -h</code></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cimserver/">cimserver</a>(1). </p>
<h2>Index</h2>
