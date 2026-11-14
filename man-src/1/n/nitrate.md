---
title: "nitrate(1)"
name: "nitrate"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nitrate/"
---

<h2>NAME</h2>

 nitrate - Command line interpreter for the Nitrate Python API

<h2>SYNOPSIS</h2>

 

 nitrate

<h2>DESCRIPTION</h2>

 

 python-nitrate provides a high-level Python interface to the Nitrate test case management system. The package also provides standalone script 'nitrate' which allows easy experimenting with the interface directly from the Python interpreter by importing all available objects and enabling the readline support. 

 In short, after setting your configuration you can easily manipulate all Nitrate objects from the command line, for example: 

 <pre>
$ nitrate
&gt;&gt;&gt; for case in TestRun(123):
...     print case
</pre>

<h2>CONFIGURATION</h2>

 

 To be able to contact the Nitrate server a minimal user config file ~/.nitrate has to be provided in the user home directory: 

 <pre>
[nitrate]
url = <a rel="nofollow" HREF="https://nitrate.server/xmlrpc/">https://nitrate.server/xmlrpc/</a>
</pre>

<h2>SEE ALSO</h2>

 

 python-nitrate nitrate-notes

<h2>AUTHOR</h2>

 

 Petr Šplíchal &lt;<i>psplicha [at] redhat.com</i>&gt; 

<h2>Index</h2>


