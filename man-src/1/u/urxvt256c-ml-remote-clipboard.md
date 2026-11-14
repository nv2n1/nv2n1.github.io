---
title: "urxvt256c-ml-remote-clipboard(1)"
name: "urxvt256c-ml-remote-clipboard"
section: "1"
letter: "u"
url: "/docs/linux/man/1-urxvt256c-ml-remote-clipboard/"
---

<h2 class="name">NAME</h2>
 

 remote-clipboard - manage a shared and possibly remote clipboard 

<h2>DESCRIPTION</h2>

 Somewhat of a misnomer, this extension adds two menu entries to the selection popup that allows one to run external commands to store the selection somewhere and fetch it again. 

 We use it to implement a ``distributed selection mechanism'', which just means that one command uploads the file to a remote server, and another reads it. 

 The commands can be set using the <tt>&quot;URxvt.remote-selection.store&quot;</tt> and <tt>&quot;URxvt.remote-selection.fetch&quot;</tt> resources. The first should read the selection to store from <font SIZE="-1">STDIN </font>(always in <font SIZE="-1">UTF-8</font>), the second should provide the selection data on <font SIZE="-1">STDOUT </font>(also in <font SIZE="-1">UTF-8</font>). 

 The defaults (which are likely useless to you) use rsh and cat: 

 <pre>
   URxvt.remote-selection.store: rsh ruth 'cat &gt;/tmp/distributed-selection'
   URxvt.remote-selection.fetch: rsh ruth 'cat /tmp/distributed-selection'
</pre> 

<h2>Index</h2>


