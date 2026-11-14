---
title: "soapsh(1)"
name: "soapsh"
section: "1"
letter: "s"
url: "/docs/linux/man/1-soapsh/"
---

SOAPsh.pl - Interactive shell for SOAP calls 

<h2>Synopsis</h2><pre> perl SOAPsh.pl <a rel="nofollow" HREF="http://services.soaplite.com/examples.cgi">http://services.soaplite.com/examples.cgi</a> <a HREF="http://www.soaplite.com/My/Examples">http://www.soaplite.com/My/Examples</a>
 &gt; <a HREF="//www.systutorials.com/docs/linux/man/2-getStateName/">getStateName</a>(2)
 &gt; getStateNames(1,2,3,7)
 &gt; getStateList([1,9])
 &gt; getStateStruct({a=&gt;1, b=&gt;24})
 &gt; Ctrl-D (Ctrl-Z on Windows)</pre>or 

 <pre> # all parameters after uri will be executed as methods
 perl SOAPsh.pl <a rel="nofollow" HREF="http://soap.4s4c.com/ssss4c/soap.asp">http://soap.4s4c.com/ssss4c/soap.asp</a> <a HREF="http://simon.fell.com/calc">http://simon.fell.com/calc</a> doubler([10,20,30])
 &gt; Ctrl-D (Ctrl-Z on Windows)</pre><h2>Description</h2>SOAPsh.pl is a shell for making <font SIZE="-1">SOAP</font> calls. It takes two parameters: mandatory endpoint and optional uri (actually it will tell you about it if you try to run it). Additional commands can follow. 

 After that you'll be able to run any methods of SOAP::Lite, like autotype, readable, encoding, etc. You can run it the same way as you do it in your Perl script. You'll see output from method, result of <font SIZE="-1">SOAP</font> call, detailed info on <font SIZE="-1">SOAP</font> faulure or transport error. 

 For full list of available methods see documentation for SOAP::Lite. 

 Along with methods of SOAP::Lite you'll be able (and that's much more interesting) run any <font SIZE="-1">SOAP</font> methods you know about on remote server and see processed results. You can even switch on debugging (with call something like: <tt>&quot;on_debug(sub{print@_})&quot;</tt>) and see <font SIZE="-1">SOAP</font> code with headers sent and recieved.
<h2>Copyright</h2>Copyright (C) 2000 Paul Kulchenko. All rights reserved.
<h2>Author</h2>Paul Kulchenko (paulclinger [at] yahoo.com)
