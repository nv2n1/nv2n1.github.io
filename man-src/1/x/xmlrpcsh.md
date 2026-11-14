---
title: "xmlrpcsh(1)"
name: "xmlrpcsh"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xmlrpcsh/"
---

XMLRPCsh.pl - Interactive shell for XMLRPC calls 

<h2>Synopsis</h2><pre> perl XMLRPCsh.pl <a rel="nofollow" HREF="http://betty.userland.com/RPC2">http://betty.userland.com/RPC2</a> 
 &gt; <a HREF="//www.systutorials.com/docs/linux/man/2-examples.getStateName/">examples.getStateName</a>(2)
 &gt; examples.getStateNames(1,2,3,7)
 &gt; examples.getStateList([1,9])
 &gt; examples.getStateStruct({a=&gt;1, b=&gt;24})
 &gt; Ctrl-D (Ctrl-Z on Windows)</pre>or 

 <pre> # all parameters after uri will be executed as methods
 perl XMLRPCsh.pl <a rel="nofollow" HREF="http://betty.userland.com/RPC2">http://betty.userland.com/RPC2</a> <a HREF="//www.systutorials.com/docs/linux/man/2-examples.getStateName/">examples.getStateName</a>(2)
 &gt; Ctrl-D (Ctrl-Z on Windows)</pre><h2>Description</h2>XMLRPCsh.pl is a shell for making <font SIZE="-1">XMLRPC</font> calls. It takes one parameter, endpoint (actually it will tell you about it if you try to run it). Additional commands can follow. 

 After that you'll be able to run any methods of XMLRPC::Lite, like autotype, readable, etc. You can run it the same way as you do it in your Perl script. You'll see output from method, result of <font SIZE="-1">XMLRPC</font> call, detailed info on <font SIZE="-1">XMLRPC</font> faulure or transport error. 

 For full list of available methods see documentation for XMLRPC::Lite. 

 Along with methods of XMLRPC::Lite you'll be able (and that's much more interesting) run any <font SIZE="-1">XMLRPC</font> methods you know about on remote server and see processed results. You can even switch on debugging (with call something like: <tt>&quot;on_debug(sub{print@_})&quot;</tt>) and see <font SIZE="-1">XMLRPC</font> code with headers sent and recieved.
<h2>Copyright</h2>Copyright (C) 2000 Paul Kulchenko. All rights reserved.
<h2>Author</h2>Paul Kulchenko (paulclinger [at] yahoo.com)
