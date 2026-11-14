---
title: "urxvt-bell-command(1)"
name: "urxvt-bell-command"
section: "1"
letter: "u"
url: "/docs/linux/man/1-urxvt-bell-command/"
---

<h2 class="name">NAME</h2>
 

 bell-command - execute a command when the bell rings 

<h2>DESCRIPTION</h2>

 Runs the command specified by the <tt>&quot;URxvt.bell-command&quot;</tt> resource when a bell event occurs. For example, the following pops up a notification bubble with the text ``Beep, Beep'' using notify-send: 

 <pre>
   URxvt.bell-command: notify-send &quot;Beep, Beep&quot;
</pre> 

<h2>Index</h2>


