---

title: "urxvt-ml-bell-command(1)"
name: "urxvt-ml-bell-command"
section: "1"
letter: "u"
url: "/docs/linux/man/1-urxvt-ml-bell-command/"
---

bell-command - execute a command when the bell rings 

Runs the command specified by the <tt>&quot;URxvt.bell-command&quot;</tt> resource when a bell event occurs. For example, the following pops up a notification bubble with the text ``Beep, Beep'' using notify-send: 

 <pre>
   URxvt.bell-command: notify-send &quot;Beep, Beep&quot;
</pre>
