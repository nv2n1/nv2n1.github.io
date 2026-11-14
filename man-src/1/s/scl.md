---
title: "scl(1)"
name: "scl"
section: "1"
letter: "s"
url: "/docs/linux/man/1-scl/"
description: "scl – Setup and run software from Software Collection environment"
---

<h2>NAME</h2>
<p> scl &#8211; Setup and run software from Software Collection environment</p>
<h2>SYNOPSIS</h2>
<p> <code>scl</code> <i>&lt;action&gt;</i> <i>&lt;collection1&gt;</i> [<i>&lt;collection2&gt; &#8230;</i>] <i>&lt;command&gt;</i> </p>
<p> <code>scl</code> <i>&lt;action&gt;</i> <i>&lt;collection1&gt;</i> [<i>&lt;collection2&gt; &#8230;</i>] &#8212; <i>&lt;command&gt;</i> </p>
<p> <code>scl</code> {<code>-l|&#8211;list</code>} [<i>&lt;collection1&gt; &lt;collection2&gt; &#8230;</i>] </p>
<p> <code>scl register</code> <i>&lt;path&gt;</i></p>
<p> <code>scl deregister</code> <i>&lt;collection&gt;</i> [<code>&#8211;force</code>]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents <code>scl</code>, a program which is an utility for running software packaged as a Software Collection. </p>
<p> <code>scl</code> utility allows to execute an application which is not located in the filesystem root hierarchy but is present in an alternative location. This application can still use and benefit from software installed in the root filesystem. In order to let an application be visible to the system one has to use <code>scl</code> utility as an interface. </p>
<p> <i>&lt;action&gt;</i> is a script name to execute in a bash environment before the application itself takes in executed. Currently only <code>enable</code> scriptlet is mandatory which is needed to update search paths, etc. </p>
<p> One can enable more Software Collections if needed and therefore one can use multiple collections which are enabled by the left-right order as present on <code>scl</code> command-line. </p>
<p> <i>&lt;command&gt;</i> marks specified Software Collections as enabled. Executes the script, which is expected to set proper environment. Executes the <i>&lt;command&gt;</i>. Control is returned back to the caller with the original environment as soon as the command finishes. If <i>&lt;command&gt;</i> is &#8216;-&#8216; (dash) then it is read from the standard input. </p>
<p> Note: if you use <i>&lt;command&gt;</i> consisting of multiple arguments, you either need to use quotes or the <code>&#8212;</code> command separator. Everything that follows the separator will be considered a command or its argument. </p>
<p> Note: some commands modify user environment in some way. Those commands may potentially break SCLs, as their activation also usually depends on env. modification as well. Typical examples of such commands are <code>su</code> and <code>sudo</code>. Every collection modifies the environment differently, thus more details may be found in the documentation of the particular collection.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-l, &#8211;list</code></p>
<dd> Lists all installed Software Collections on the system.</p>
<dt><code>-l, &#8211;list</code> <i>&lt;collection1&gt; &lt;collection2&gt; &#8230;</i></p>
<dd> If a collection name is specified then list of installed packages belonging to the collection is listed.</p>
<dt><code>register</code> <i>&lt;path&gt;</i></p>
<dd> If <i>&lt;path&gt;</i> leads to valid SCL file structure, <code>scl</code> will register that as a SCL. <i>&lt;path&gt;</i> directory needs to contain <code>enable</code> scriptlet and <code>root</code> directory, to be considered valid SCL. &lt;path&gt; needs to be an absolute path to the collection location.</p>
<dt><code>deregister</code> <i>&lt;collection&gt;</i> [<code>&#8211;force</code>]</p>
<dd> <i>&lt;collection&gt;</i> will no longer be considered SCL. If the <i>&lt;collection&gt;</i> was installed locally, then the use of <code>&#8211;force</code> is needed.i</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>scl enable example &#8216;less &#8211;version&#8217;</p>
<dd> runs command &#8216;less &#8211;version&#8217; in the environment with collection &#8216;example&#8217; enabled</p>
<dt>scl enable foo bar bash</p>
<dd> runs bash instance with foo and bar Software Collections enabled</p>
<dt>cat my_command | scl enable baz &#8211;</p>
<dd> run set of commands listed in my_command file in the environment with baz Software Collection enabled</p>
<dt>scl -l</p>
<dd> list all installed collections</p>
<dt>scl -l example</p>
<dd> list all packages within example collection scl register /foo/bar registers new collection with a name bar</p>
<dt>scl deregister bar &#8211;force</p>
<dd> forces the deregistration of collection bar</p>
<dt></dl>
<h2>AUTHOR</h2>
<dd>
<p> <code>scl</code> was written by Jindrich Novy &lt;jnovy [at] redhat.com&gt; and Jan Zeleny &lt;jzeleny [at] redhat.com&gt; </p>
<h2>Index</h2>
