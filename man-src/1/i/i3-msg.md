---

title: "i3-msg(1)"
name: "i3-msg"
section: "1"
letter: "i"
url: "/docs/linux/man/1-i3-msg/"
---

i3-msg - send messages to i3 window manager 

i3-msg &quot;message&quot;

i3-msg is a sample implementation for a client using the unix socket IPC interface to i3. At the moment, it can only be used for sending commands (like in configuration file for key bindings), but this may change in the future (staying backwards-compatible, of course).

<h2>EXAMPLE</h2>

 

<dl>
<dt>
</dt><dd> <pre>
i3-msg &quot;bp&quot; # Use 1-px border for current client
</pre></dd></dl>

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/1-i3/">i3</a>(1)

<h2>AUTHOR</h2>

 

 Michael Stapelberg and contributors
