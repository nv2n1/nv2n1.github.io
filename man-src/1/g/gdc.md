---
title: "gdc(1)"
name: "gdc"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdc/"
description: "gdc – Client utility for GoodData on-demand Business Intelligence platform"
---

<h2 class="name">NAME</h2>
<p> gdc &#8211; Client utility for GoodData on-demand Business Intelligence platform </p>
<h2>SYNOPSIS</h2>
<p> gdc [global options] &lt;command&gt; [command options]</p>
<h2>DESCRIPTION</h2>
<p> <code>gdc</code> is the command-line and interactive client for GoodData REST-ful service <font SIZE="-1">API</font> built on top of WWW::GoodData client library.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print a brief help message and exits.</p>
<dt><code>-H</code>, <code>&#8211;man</code></p>
<dd> Prints the manual page and exits.</p>
<dt><code>-u</code>, <code>&#8211;user</code> <code>&lt;email&gt;</code></p>
<dd> Use the identity of specified user. See also the <code>login</code> command.</p>
<dt><code>-p</code>, <code>&#8211;password</code></p>
<dd> Log in on start, provided <code>&#8211;user</code> option was set as well.</p>
<dt><code>-P</code>, <code>&#8211;project</code></p>
<dd> Project <font SIZE="-1">URI.</font> It is used as a default value for commands that accept project <font SIZE="-1">URI</font> option (such as <code>rmproject</code> and <code>lsreports</code>) and can be changed from within the shell (see <code>project</code> and <code>mkproject</code> commands). </p>
<p> No checking is done with the project <font SIZE="-1">URI</font> util a command that acts upon the project is issued.</p>
<dt><code>-r</code>, <code>&#8211;root</code></p>
<dd> <font SIZE="-1">URL</font> of the service <font SIZE="-1">API</font> root. Defaults to &lt;<a rel="nofollow" href="https://secure.gooddata.com/gdc/">https://secure.gooddata.com/gdc/</a>&gt;.</dl>
<h2>COMMANDS</h2>
<h3>shell</h3>
<p> Launch an interactive client session. </p>
<p> This is the default action that is taken unless another command is specified.</p>
<h3>login [user] [password]</h3>
<p> Verify user identity and obtain an authorization token. If no credentials are supplied, global ones are used. </p>
<p> If the password is not specified, it is requested from terminal provided terminal echo can be turned off. </p>
<p> This action is taken implicitly if user name has been specified.</p>
<dl>
<dt><code>-u</code>, <code>&#8211;user</code> <code>&lt;email&gt;</code></p>
<dd> Alternative way to specifiy user login.</p>
<dt><code>-p</code>, <code>&#8211;password</code></p>
<dd> Alternative way to specifiy user password.</dl>
<h3>logout</h3>
<p> Drop credentials if user is logged in, otherwise do nothing. Automatically done upon utility exit.</p>
<h3>project [uri]</h3>
<p> Change or print the default project <font SIZE="-1">URI.</font> Default project is used by various commands involving projects, including <code>mkproject</code> and <code>rmproject</code>.</p>
<dl>
<dt><code>-P</code>, <code>&#8211;project</code></p>
<dd> Project <font SIZE="-1">URI.</font> No checking is done with the project <font SIZE="-1">URI.</font></dl>
<h3>lsprojects</h3>
<p> Print a list of available projects.</p>
<dl>
<dt><code>-v</code>, <code>&#8211;long</code></p>
<dd> Add unnecessary details.</dl>
<h3>lsroles</h3>
<p> Print a list of available roles in project.</p>
<dl>
<dt><code>-P</code>, <code>&#8211;project</code></p>
<dd> Set or override the project to act on. See global <code>&#8211;project</code> option for the detailed description.</dl>
<h3>rmproject</h3>
<p> Delete a project.</p>
<dl>
<dt><code>-P</code>, <code>&#8211;project</code></p>
<dd> Set or override the project to act on. See global <code>&#8211;project</code> option for the detailed description.</dl>
<h3>mkuser &lt;email&gt; &lt;firstname&gt; &lt;lastname&gt;</h3>
<p> Create user.</p>
<dl>
<dt><code>-d</code>, <code>&#8211;domain</code></p>
<dd> <font SIZE="-1">URI</font> of an user domain in which will be user created. </p>
<p> Defaults to <tt>&quot;/gdc/account/domains/default&quot;</tt>, which is almost definitely useless to you. Get a proper domain <font SIZE="-1">URI</font> from your support representative.</p>
<dt><code>-e</code>, <code>&#8211;email</code></p>
<dd> User email.</p>
<dt><code>-l</code>, <code>&#8211;login</code></p>
<dd> User login. Same as email if no login is provided</p>
<dt><code>-p</code>, <code>&#8211;password</code></p>
<dd> User password. Will be asked for if not provided.</p>
<dt><code>-f</code>, <code>&#8211;firstname</code></p>
<dd> User first name.</p>
<dt><code>-l</code>, <code>&#8211;lastname</code></p>
<dd> User last name.</p>
<dt><code>-t</code>, <code>&#8211;phone</code></p>
<dd> User phone number.</p>
<dt><code>-c</code>, <code>&#8211;company</code></p>
<dd> User company.</p>
<dt><code>-o</code>, <code>&#8211;sso</code></p>
<dd> User company&#8217;s <font SIZE="-1">DNS</font> suffix, if <font SIZE="-1">SSO</font> is used.</dl>
<h3>mkproject &lt;title&gt; [summary]</h3>
<p> Create a project.</p>
<dl>
<dt><code>-t</code>, <code>&#8211;title</code></p>
<dd> Title of the project.</p>
<dt><code>-s</code>, <code>&#8211;summary</code></p>
<dd> Descriptive summary of the project.</p>
<dt><code>-e</code>, <code>&#8211;template</code></p>
<dd> Project template. The list of valid project templates is available from the template server: &lt;<a rel="nofollow" href="https://secure.gooddata.com/projectTemplates/">https://secure.gooddata.com/projectTemplates/</a>&gt;.</p>
<dt><code>-d</code>, <code>&#8211;driver</code></p>
<dd> Valid db engine drivers are &#8216;Pg&#8217; (default) and &#8216;mysql&#8217;.</p>
<dt><code>-k</code>, <code>&#8211;token</code></p>
<dd> Authorization token.</dl>
<h3>lsreports</h3>
<p> Print a list of reports in a project.</p>
<dl>
<dt><code>-P</code>, <code>&#8211;project</code></p>
<dd> Set or override the project to act on. See global <code>&#8211;project</code> option for the detailed description.</p>
<dt><code>-v</code>, <code>&#8211;long</code></p>
<dd> Add unnecessary details.</dl>
<h3>export</h3>
<p> Export a report computation result into file.</p>
<dl>
<dt><code>-P</code>, <code>&#8211;project</code></p>
<dd> Set or override the project to act on. See global <code>&#8211;project</code> option for the detailed description.</p>
<dt><code>-r</code>, <code>&#8211;report</code></p>
<dd> Set report <font SIZE="-1">URI </font>(see <code>lsreports</code>).</p>
<dt><code>-f</code>, <code>&#8211;file</code></p>
<dd> File to place the result into.</p>
<dt><code>-F</code>, <code>&#8211;format</code></p>
<dd> One of <code>pdf</code>, <code>xls</code>, <code>png</code> (latter only valid for chart reports), Can be unspecified if file name ends with a dot and format name (extension).</dl>
<h3>model</h3>
<p> Export a Logical Data Model (<font SIZE="-1">LDM</font>) picture in <font SIZE="-1">PNG</font> format into file.</p>
<dl>
<dt><code>-P</code>, <code>&#8211;project</code></p>
<dd> Set or override the project to act on. See global <code>&#8211;project</code> option for the detailed description.</p>
<dt><code>-f</code>, <code>&#8211;file</code></p>
<dd> File to place the result into.</dl>
<h3>chmodel</h3>
<p> Change a Logical Data Model (<font SIZE="-1">LDM</font>) with <font SIZE="-1">MAQL DDL</font> script. </p>
<p> The <font SIZE="-1">MAQL</font> script can be either specified inline as argument to <code>chmodel</code>, or read from file specified with <code>&#8211;file</code> option (see below).</p>
<dl>
<dt><code>-P</code>, <code>&#8211;project</code></p>
<dd> Set or override the project to act on. See global <code>&#8211;project</code> option for the detailed description.</p>
<dt><code>-f</code>, <code>&#8211;file</code></p>
<dd> Read <font SIZE="-1">MAQL</font> script from specified file.</dl>
<h3>upload</h3>
<p> Update data set with new data.</p>
<dl>
<dt><code>-P</code>, <code>&#8211;project</code></p>
<dd> Set or override the project to act on. See global <code>&#8211;project</code> option for the detailed description.</p>
<dt><code>-f</code>, <code>&#8211;file</code></p>
<dd> <font SIZE="-1">SLI</font> Manifest of the upload.</dl>
<h3>mkobject &lt;type&gt; &lt;title&gt; &lt;expression&gt;</h3>
<p> Create a new metadata object of a given type with expression as the only content.</p>
<dl>
<dt><code>-T</code>, <code>&#8211;type</code></p>
<dd> Type of the object.</p>
<dt><code>-t</code>, <code>&#8211;title</code></p>
<dd> Title of the object.</p>
<dt><code>-s</code>, <code>&#8211;summary</code></p>
<dd> Descriptive summary of the object.</p>
<dt><code>-e</code>, <code>&#8211;expr</code></p>
<dd> Expression (typically <font SIZE="-1">MAQL</font>).</p>
<dt><code>-u</code>, <code>&#8211;uri</code></p>
<dd> Instead of creating a new object, rewrite an old one with a given <font SIZE="-1">URI.</font></p>
<dt><code>-P</code>, <code>&#8211;project</code></p>
<dd> Set or override the project to act on. See global <code>&#8211;project</code> option for the detailed description.</dl>
<h3>mkreportdef &lt;title&gt; [summary]</h3>
<p> Create a new reportDefinition in metadata.</p>
<dl>
<dt><code>-t</code>, <code>&#8211;title</code></p>
<dd> Title of the object.</p>
<dt><code>-s</code>, <code>&#8211;summary</code></p>
<dd> Descriptive summary of the object.</p>
<dt><code>-m</code>, <code>&#8211;metric</code></p>
<dd> Add a metric by its <font SIZE="-1">URL.</font></p>
<dt><code>-d</code>, <code>&#8211;dim</code></p>
<dd> Add an attribute to dimensionality by its <font SIZE="-1">URL.</font></p>
<dt><code>-f</code>, <code>&#8211;filter</code></p>
<dd> Add a filter by its expression.</p>
<dt><code>-u</code>, <code>&#8211;uri</code></p>
<dd> Instead of creating a new object, rewrite an old one with a given <font SIZE="-1">URI.</font></p>
<dt><code>-P</code>, <code>&#8211;project</code></p>
<dd> Set or override the project to act on. See global <code>&#8211;project</code> option for the detailed description.</dl>
<h3>help</h3>
<p> Print list of available commands.</p>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</p>
<dd> &lt;<a rel="nofollow" href="https://secure.gooddata.com/gdc/">https://secure.gooddata.com/gdc/</a>&gt; &#8212; Browsable GoodData <font SIZE="-1">API</font></p>
<dt>&bull;</p>
<dd> &lt;<a rel="nofollow" href="http://developer.gooddata.com/api/maql-ddl.html">http://developer.gooddata.com/api/maql-ddl.html</a>&gt; &#8212; <font SIZE="-1">MAQL DDL</font> language documentation</p>
<dt>&bull;</p>
<dd> WWW::GoodData &#8212; Client library for GoodData</p>
<dt>&bull;</p>
<dd> LWP::UserAgent &#8212; Perl <font SIZE="-1">HTTP</font> client</dl>
<h2>COPYRIGHT</h2>
<p> Copyright 2011, 2012, 2013 Lubomir Rintel </p>
<p> Copyright 2012, 2013 Adam Stulpa, Tomas Janousek </p>
<p> This program is free software; you can redistribute it and/or modify it under the same terms as Perl itself.</p>
<h2>AUTHOR</h2>
<p> Lubomir Rintel <tt>&quot;lkundrak [at] v3.sk&quot;</tt> </p>
<h2>Index</h2>
