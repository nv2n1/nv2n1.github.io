---
title: "qmgr(1)"
name: "qmgr"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qmgr/"
description: "qmgr – pbs batch system manager"
---

<h2 class="name">NAME</h2>
<p> qmgr &#8211; pbs batch system manager </p>
<h2>SYNOPSIS</h2>
<p> qmgr [-a] [-c command] [-e] [-n] [-z] [server&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The <code>qmgr</code> command provides an administrator interface to the batch system. </p>
<p> The command reads directives from standard input. The syntax of each directive is checked and the appropriate request is sent to the batch server or servers. </p>
<p> The list or print subcommands of qmgr can be executed by general users. Creating or deleting a queue requries PBS Manager privilege. Setting or unsetting server or queue attributes requires PBS Operator or Manager privilege.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-a</p>
<dd> Abort <code>qmgr </code> on any syntax errors or any requests rejected by a server.</p>
<dt>-c command</p>
<dd> Execute a single <i> and exit </i><code>qmgr .</code></p>
<dt>-e</p>
<dd> Echo all commands to standard output.</p>
<dt>-n</p>
<dd> No commands are executed, syntax checking only is performed.</p>
<dt>-z</p>
<dd> No errors are written to standard error.</dl>
<h2>OPERANDS</h2>
<p> The <i> operands identify the name of the batch server to which the administrator requests are sent. Each conforms to the following syntax:<br />
 </i><code><br />
 where is the network name of the host on which the server is running and is the port number to which to connect. If is not specified, the default port number is used. </p>
<p> If </code><i> is not specified, the administrator requests are sent to the local server. </i></p>
<h2>STANDARD INPUT</h2>
<p> The <code>qmgr</code> command reads standard input for directives until end of file is reached, or the <i>exit </i> or <i>quit</i> directive is read.</p>
<h2>STANDARD OUTPUT</h2>
<p> If Standard Output is connected to a terminal, a command prompt will be written to standard output when qmgr is ready to read a directive. </p>
<p> If the <i> option is specified, </i><code>qmgr</code> will echo the directives read from standard input to standard output.</p>
<h2>STANDARD ERROR</h2>
<p> If the <i> option is not specified, the qmgr command will write a diagnostic message to standard error for each error occurrence. </i></p>
<h2>EXTENDED DESCRIPTION</h2>
<p> If <code>qmgr</code> is invoked without the <i> option and standard output is connected to a terminal, qmgr will write a prompt to standard output and read a directive from standard input. </p>
<p> Commands can be abbreviated to their minimum unambiguous form. A command is terminated by a new line character or a semicolon, &quot;;&quot;, character. Multiple commands may be entered on a single line. A command may extend across lines by escaping the new line character with a back-slash &quot;\&quot;. </p>
<p> Comments begin with the # character and continue to end of the line. Comments and blank lines are ignored by qmgr. </i></p>
<h2>DIRECTIVE SYNTAX</h2>
<p> A qmgr directive is one of the following forms: </p>
<p> <code> </p>
<p> Where,</p>
<dl>
<dt>command</p>
<dd> is the command to perform on a object. Commands are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>active</p>
<dd> sets the active objects. If the active objects are specified, and the name is not given in a qmgr cmd the active object names will be used.</p>
<dt>create</p>
<dd> is to create a new object, applies to queues and nodes.</p>
<dt>delete</p>
<dd> is to destroy an existing object, applies to queues and nodes.</p>
<dt>set</p>
<dd> is to define or alter attribute values of the object.</p>
<dt>unset</p>
<dd> is to clear the value of attributes of the object. Note, this form does not accept an OP and value, only the attribute name.</p>
<dt>list</p>
<dd> is to list the current attributes and associated values of the object.</p>
<dt>print</p>
<dd> is to print all the queue and server attributes in a format that will be usable as input to the qmgr command.</dl>
</dl>
<dt>names</p>
<dd> is a list of one or more names of specific objects The name list is in the form: </p>
<p> with no intervening white space. The name of an object is declared when the object is first created. If the name is @server, then all the objects of specified type at the server will be effected.</p>
<dt>attr</p>
<dd> specifies the name of an attribute of the object which is to be set or modified. If the attribute is one which consist of a set of resources, then the attribute is specified in the form:<br />
 &nbsp;<wbr>&nbsp;<wbr>attribute_name.resource_name</code> </p>
<dt>OP</p>
<dd> operation to be performed with the attribute and its value:</p>
<dl>
<dt>
<dd>
<dl>
<dt>=</p>
<dd> set the value of the attribute. If the attribute has a existing value, the current value is replaced with the new value.</p>
<dt>+=</p>
<dd> increase the current value of the attribute by the amount in the new value.</p>
<dt>-=</p>
<dd> decrease the current value of the attribute by the amount in the new value.</dl>
</dl>
<dt>value</p>
<dd> the value to assign to an attribute. If the value includes white space, commas or other special characters, such as the # character, the value string must be inclosed in quote marks (&quot;).</dl>
<p> The following are examples of qmgr directives: </p>
<h2>EXIT STATUS</h2>
<p> Upon successful processing of all the operands presented to the qmgr command, the exit status will be a value of zero. </p>
<p> If the qmgr command fails to process any operand, the command exits with a value greater than zero.</p>
<h2>SEE ALSO</h2>
<p> <a href="//www.systutorials.com/docs/linux/man/8B-pbs_server/">pbs_server</a>(8B), <a href="//www.systutorials.com/docs/linux/man/7B-pbs_queue_attributes/">pbs_queue_attributes</a>(7B), <a href="//www.systutorials.com/docs/linux/man/7B-pbs_server_attributes/">pbs_server_attributes</a>(7B), <a href="//www.systutorials.com/docs/linux/man/8B-qstart/">qstart</a>(8B), <a href="//www.systutorials.com/docs/linux/man/8B-qstop/">qstop</a>(8B), <a href="//www.systutorials.com/docs/linux/man/8B-qenable/">qenable</a>(8B), <a href="/docs/linux/man/8-qdisable/">qdisable</a>(8), <a href="//www.systutorials.com/docs/linux/man/7B-pbs_resources/">pbs_resources</a>(7B) and the PBS External Reference Specification </p>
<h2>Index</h2>
