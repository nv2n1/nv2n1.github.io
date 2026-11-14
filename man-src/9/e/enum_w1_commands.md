---
title: "enum_w1_commands(9)"
name: "enum_w1_commands"
section: "9"
letter: "e"
url: "/docs/linux/man/9-enum_w1_commands/"
description: "enum_w1_commands – commands available for master or slave operations"
---

<p>enum_w1_commands &#8211; commands available for master or slave operations</p>
<h2>Synopsis</h2>
<pre>enum w1_commands {
 W1_CMD_READ,
 W1_CMD_WRITE,
 W1_CMD_SEARCH,
 W1_CMD_ALARM_SEARCH,
 W1_CMD_TOUCH,
 W1_CMD_RESET,
 W1_CMD_SLAVE_ADD,
 W1_CMD_SLAVE_REMOVE,
 W1_CMD_LIST_SLAVES,
 W1_CMD_MAX
}; </pre>
<h2>Constants</h2>
<p>W1_CMD_READ</p>
<dl>
<dd>read len bytes</dl>
<p> W1_CMD_WRITE</p>
<dl>
<dd>write len bytes</dl>
<p> W1_CMD_SEARCH</p>
<dl>
<dd>initiate a standard search, returns only the slave devices found during that search</dl>
<p> W1_CMD_ALARM_SEARCH</p>
<dl>
<dd>search for devices that are currently alarming</dl>
<p> W1_CMD_TOUCH</p>
<dl>
<dd>Touches a series of bytes.</dl>
<p> W1_CMD_RESET</p>
<dl>
<dd>sends a bus reset on the given master</dl>
<p> W1_CMD_SLAVE_ADD</p>
<dl>
<dd>adds a slave to the given master, 8 byte slave id at data[0]</dl>
<p> W1_CMD_SLAVE_REMOVE</p>
<dl>
<dd>removes a slave to the given master, 8 byte slave id at data[0]</dl>
<p> W1_CMD_LIST_SLAVES</p>
<dl>
<dd>list of slaves registered on this master</dl>
<p> W1_CMD_MAX</p>
<dl>
<dd>number of available commands</dl>
<h2>Author</h2>
<p><code>David Fries</code> &lt;David [at] Fries.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
