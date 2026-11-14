---
title: "preferredmethod(3)"
name: "preferredmethod"
section: "3"
letter: "p"
url: "/docs/linux/man/3-preferredmethod/"
---

XMLTV::PreferredMethod - Adds a preferredmethod argument to XMLTV grabbers 

<h2>Description</h2>Add a --preferredmethod argument to your program, eg 

 <pre> use XMLTV::PreferredMethod 'allatonce';</pre>If a --preferredmethod parameter is supplied on the command-line, it will be caught already by the ``use'' statement, the string supplied in the use-line will be printed to <font SIZE="-1">STDOUT</font> and the program will exit. 

 Don't forget to announce the preferredmethod capability as well.
<h2>See Also</h2>XMLTV::Options, XMLTV::Capabilities.
