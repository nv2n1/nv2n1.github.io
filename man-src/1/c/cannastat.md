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
<p> <code>cannastat [{-cs|-cannaserver} </code><i>canna-server</i>] [-p] [-t] [-a]</p>
<p> <i><a href="/docs/linux/man/1-cannastat/">cannastat</a>(1)</i> displays information about the Kana-Kanji conversion server <i>cannaserver(1M)</i>. The information includes the following: the name of the machine on which the connected server exists, the <i>cannaserver(1M)</i>&#8216;s version, the number of clients connecting to the server, the name of the user connecting to the server, its user number, the socket number, the number of contexts, the time of connection to the server, the time of use of the server, the idle time, the name of the host under which the client exists, and the frequency of using each protocol. </p>
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
<dt>USER_NAME</dt>
<dd> User name</dd>
<dt>ID</dt>
<dd> Socket number</dd>
<dt>NO</dt>
<dd> User number</dd>
<dt>U_CX</dt>
<dd> Context number</dd>
<dt>C_TIME</dt>
<dd> Time of connection (h:min)</dd>
<dt>U_TIME</dt>
<dd> User time (h:min:s)</dd>
<dt>I_TIME</dt>
<dd> Idle time (h:min)</dd>
<dt>HOST_NAME</dt>
<dd> Name of the host under which the client exists</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt>-cs <i>canna-server</i> (or -cannaserver <i>canna-server</i>)</dt>
<dd> Specifies the Kana-Kanji conversion server.</dd>
<dt>-p</dt>
<dd> Displays the frequency of using the protocol.</dd>
<dt>-t</dt>
<dd> Displays information about the user who started cannastat. It includes the frequency of using the protocol, as well as ID, NO, U_CX, C_TIME, U_TIME, I_TIME, and HOST_NAME.</dd>
<dt>-a</dt>
<dd> Displays all information about all users.</dd></dl>
<h2>FILES</h2>
<dl>
<dt>/etc/canna/cannahost</dt>
<dd> Name of the host under which cannaserver is in operation.</dd></dl>
<h2>SEE ALSO</h2>
<p> cannaserver(1M), cannakill(1M), <a href="/docs/linux/man/1-cannacheck/">cannacheck</a>(1) </p>
<h2>ENVIRONMENT</h2>
<dl>
<dt>CANNAHOST</dt>
<dd> Specifies the name of the host under which <i>cannaserver(1M)</i> is in operation. </dd>
</dl>
