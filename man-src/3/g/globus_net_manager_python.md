---
title: "globus_net_manager_python(3)"
name: "globus_net_manager_python"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_net_manager_python/"
---

<h2 class="name">NAME</h2>
 

 Python Module - 

 Net Manager Python Module. Net Manager Python Module. 

 The Net Manager Python module is an example module that provides basic Python language bindings to the Network Manager callout functionality. To use this example, define a python module that implements the some subset of the following functions: 

 <pre><code>
1 def pre_listen(task_id, transport, attrs) : 2 #return list of(scope, name, value)
tuples or None 3 def post_listen(task_id, transport, local_contact, attrs) : 4 #return a tuple containing(local_contact_out, [ (scope, name, value), ... ]) 5 def end_listen(task_id, transport, local_contact, attrs) : 6 #return a list of(scope, name, value)
tuples or None 7 def pre_accept(task_id, transport, local_contact, attrs) : 8 #return list of(scope, name, value)
tuples or None 9 def post_accept(task_id, transport, local_contact, remote_contact, attrs) : 10 #return list of(scope, name, value)
tuples or None 11 def pre_connect(task_id, transport, remote_contact, attrs) : 12 #return a tuple containing(remote_contact_out, [ (scope, name, value), ... ]) 13 def post_connect(task_id, transport, local_contact, remote_contact, attrs) : 14 #return list of(scope, name, value)
tuples or None 15 def pre_close(task_id, transport, local_contact, remote_contact, attrs) : 16 #return None
    17 def post_close(task_id, transport, local_contact, remote_contact, attrs) : 18 #return None
</code></pre> 

 
&nbsp;<wbr>The&nbsp;<wbr><i>task_id</i>,&nbsp;<wbr><i>transport</i>,&nbsp;<wbr><i>local_contact</i>, and&nbsp;<wbr><i>remote_contact</i>&nbsp;<wbr>parameters to these functions are all string objects. The&nbsp;<wbr><i>attrs</i>&nbsp;<wbr>parameter to these functions are lists of 3-tuples&nbsp;<wbr>(scope, name, value). 

 To use this with the GridFTP server, add a file containing the following to the GridFTP configuration directory /etc/grid

<a HREF="ftp://ftp.d">ftp.d</a>: 

 <pre>
$PYTHONPATH PATH
xnetmgr &quot;manager=python;pymod=MODULE_NAME;&quot;
</pre> 

 
&nbsp;<wbr>Where&nbsp;<wbr>'PATH'&nbsp;<wbr>is the directory containing your module and&nbsp;<wbr>'MODULE_NAME'&nbsp;<wbr>is the name of the python module that you would use to import it&nbsp;<wbr>(i.e. without the&nbsp;<wbr>'.py'&nbsp;<wbr>extension). So a module&nbsp;<wbr>'/usr/local/globus/routeman.py'&nbsp;<wbr>would require&nbsp;<wbr> 

 <pre>
$PYTHONPATH /usr/local/globus
xnetmgr &quot;manager=python;pymod=routeman;&quot;
</pre> 

 

 To use this with the XIO module directly, set the string options manager=python;pymod=routeman;. You'll need to set the PYTHONPATH environment variable elsewhere. 

 To configure the network manager to use this module directly without XIO, set the 'pymod' attribute in the 'python' scope to the name of the python module to import and use. For example: 

 <pre>
globus_net_manager_attr_init(
    &amp;attr,
    &quot;python&quot;,
    &quot;pymod&quot;,
    &quot;routeman&quot;);
</pre> 

 
&nbsp;<wbr>and pass this to the context functions.&nbsp;<wbr>

<h2>Author</h2>

 

 Generated automatically by Doxygen for globus_net_manager from the source code. 

<h2>Index</h2>


