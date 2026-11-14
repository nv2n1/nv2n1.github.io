---
title: "cannastat(1)"
name: "cannastat"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cannastat/"
description: "cannastat – Display information about the Kana-Kanji conversion server"
---

<h2>NAME</h2>
<p> cannastat &#8211; Display information about the Kana-Kanji conversion server</p>
<h2>SYNOPSIS</h2>
<p> <code>cannastat [{-cs|-cannaserver} </code><i>canna-server</i>] [-p] [-t] [-a]</p>
<h2>DESCRIPTION</h2>
<p> <i><a href="/docs/linux/man/1-cannastat/">cannastat</a>(1)</i> displays information about the Kana-Kanji conversion server <i><a href="//www.systutorials.com/docs/linux/man/1M-cannaserver/">cannaserver</a>(1M)</i>. The information includes the following: the name of the machine on which the connected server exists, the <i><a href="//www.systutorials.com/docs/linux/man/1M-cannaserver/">cannaserver</a>(1M)</i>&#8216;s version, the number of clients connecting to the server, the name of the user connecting to the server, its user number, the socket number, the number of contexts, the time of connection to the server, the time of use of the server, the idle time, the name of the host under which the client exists, and the frequency of using each protocol. </p>
<p> If <i><a href="/docs/linux/man/1-cannastat/">cannastat</a>(1)</i> is called without options, the following is displayed: </p>
<pre>
  Connected to machine1
  Canna Server (Ver. 2.1)
  Total connecting clients 1
  USER_NAME    ID   NO U_CX          C_TIME   U_TIME   I_TIME  HOST_NAME
  kon           5    0    4  Tue 21  8:49am       11    12:48   machine2
</pre>
<p> The items represent the following:</p>
<dl>
<dt>USER_NAME</p>
<dd> User name</p>
<dt>ID</p>
<dd> Socket number</p>
<dt>NO</p>
<dd> User number</p>
<dt>U_CX</p>
<dd> Context number</p>
<dt>C_TIME</p>
<dd> Time of connection (h:min)</p>
<dt>U_TIME</p>
<dd> User time (h:min:s)</p>
<dt>I_TIME</p>
<dd> Idle time (h:min)</p>
<dt>HOST_NAME</p>
<dd> Name of the host under which the client exists</dl>
<h2>OPTIONS</h2>
<dl>
<dt>-cs <i>canna-server</i> (or -cannaserver <i>canna-server</i>)</p>
<dd> Specifies the Kana-Kanji conversion server.</p>
<dt>-p</p>
<dd> Displays the frequency of using the protocol.</p>
<dt>-t</p>
<dd> Displays information about the user who started cannastat. It includes the frequency of using the protocol, as well as ID, NO, U_CX, C_TIME, U_TIME, I_TIME, and HOST_NAME.</p>
<dt>-a</p>
<dd> Displays all information about all users.</dl>
<h2>FILES</h2>
<dl>
<dt>/etc/canna/cannahost</p>
<dd> Name of the host under which cannaserver is in operation.</dl>
<h2>SEE ALSO</h2>
<p> <a href="//www.systutorials.com/docs/linux/man/1M-cannaserver/">cannaserver</a>(1M), <a href="//www.systutorials.com/docs/linux/man/1M-cannakill/">cannakill</a>(1M), <a href="/docs/linux/man/1-cannacheck/">cannacheck</a>(1) </p>
<h2>ENVIRONMENT</h2>
<dl>
<dt>CANNAHOST</p>
<dd> Specifies the name of the host under which <i><a href="//www.systutorials.com/docs/linux/man/1M-cannaserver/">cannaserver</a>(1M)</i> is in operation. </p>
</dl>
<h2>Index</h2>
