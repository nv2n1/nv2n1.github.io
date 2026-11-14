---
title: "mosquitto_passwd(1)"
name: "mosquitto_passwd"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mosquitto_passwd/"
description: "mosquitto_passwd – manage password files for mosquitto"
---

<h2 class="name">NAME</h2>
<p> mosquitto_passwd &#8211; manage password files for mosquitto </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mosquitto_passwd</code> [<code>-c</code> | <code>-D</code>] <i>passwordfile</i> <i>username</i></p>
<dt> <code>mosquitto_passwd</code> <code>-b</code> <i>passwordfile</i> <i>username</i> <i>password</i></p>
<dt> <code>mosquitto_passwd</code> <code>-U</code> <i>passwordfile</i></dl>
<h2>DESCRIPTION</h2>
<p> <code>mosquitto_passwd</code></p>
<dd>is a tool for managing password files the mosquitto MQTT broker. </p>
<p> Usernames must not contain &quot;:&quot;. Passwords are stored in a similar format to <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3).</p>
<h2>OPTIONS</h2>
<p> <code>-b</code></p>
<dl>
<dt>
<dd> Run in batch mode. This allows the password to be provided at the command line which can be convenient but should be used with care because the password will be visible on the command line and in command history.</dl>
<p> <code>-c</code></p>
<dl>
<dt>
<dd> Create a new password file. If the file already exists, it will be overwritten.</dl>
<p> <code>-D</code></p>
<dl>
<dt>
<dd> Delete the specified user from the password file.</dl>
<p> <code>-U</code></p>
<dl>
<dt>
<dd> This option can be used to upgrade/convert a password file with plain text passwords into one using hashed passwords. It will modify the specified file. It does not detect whether passwords are already hashed, so using it on a password file that already contains hashed passwords will generate new hashes based on the old hashes and render the password file unusable.</dl>
<p> <code>passwordfile</code></p>
<dl>
<dt>
<dd> The password file to modify.</dl>
<p> <code>username</code></p>
<dl>
<dt>
<dd> The username to add/update/delete.</dl>
<p> <code>password</code></p>
<dl>
<dt>
<dd> The password to use when in batch mode.</dl>
<h2>EXAMPLES</h2>
<p> Add a user to a new password file: </p>
<dl>
<dt>
<dd> &bull; mosquitto_passwd -c /etc/mosquitto/passwd ral</dl>
<p> Delete a user from a password file </p>
<dl>
<dt>
<dd> &bull; mosquitto_passwd -D /etc/mosquitto/passwd ral</dl>
<h2>BUGS</h2>
<p> <code>mosquitto_passwd</code> bug information can be found at <a rel="nofollow" href="https://bugs.eclipse.org/bugs/describecomponents.cgi?product=Mosquitto">https://bugs.eclipse.org/bugs/describecomponents.cgi?product=Mosquitto</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-mosquitto/">mosquitto</a></code>(8), <code><a href="/docs/linux/man/5-mosquitto-conf/">mosquitto.conf</a></code>(5), <code><a href="/docs/linux/man/7-mqtt/">mqtt</a></code>(7)</p>
<h2>AUTHOR</h2>
<p> Roger Light &lt;roger [at] atchoo.org&gt; </p>
<h2>Index</h2>
