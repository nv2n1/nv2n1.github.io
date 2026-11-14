---
title: "axspawn(5)"
name: "axspawn"
section: "5"
letter: "a"
url: "/docs/linux/man/5-axspawn/"
description: "axspawn.conf – Control the operation of axspawn."
---

<p>axspawn.conf &#8211; Control the operation of axspawn.</p>
<h2>Description</h2>
<p>The <code>axspawn.conf</code> file controls the operation of the <a href="/docs/linux/man/8-axspawn/">axspawn</a>(8) program. The operation of the config file can best be seen in an example: </p>
<dl>
<dd># this is /etc/ax25/axspawn.conf<br />
 #<br />
 # allow automatic creation of user accounts<br />
 create yes<br />
 # allow empty password field (so user may login via telnet, too) [default no]<br />
 create_empty_password no<br />
 #create_empty_password yes<br />
 # create with system utility <a href="/docs/linux/man/8-useradd/">useradd</a>(8)? [default no]<br />
 #create_with_useradd no<br />
 create_with_useradd yes<br />
 #<br />
 # pwcheck method: password or call or group. [default: password]<br />
 #pwcheck call<br />
 #pwcheck group<br />
 pwcheck password<br />
 #<br />
 # guest user if above is &#8216;no&#8217; or everything else<br />
 # fails. Disable with &quot;no&quot;<br />
 guest guest<br />
 #<br />
 # group id or name for autoaccount<br />
 group hams<br />
 #<br />
 # first user id to use<br />
 first_uid 400<br />
 #<br />
 # maximum user id<br />
 max_uid 2000<br />
 #<br />
 # where to add the home directory for the new user<br />
 home /home/hams<br />
 #<br />
 # secure homedirectories (g-rwx)<br />
 #secure_home yes<br />
 #<br />
 # user&#8217;s shell<br />
 shell /bin/bash<br />
 #<br />
 # bind user id to callsign for outgoing connects.<br />
 associate yes</dl>
<p> The lqassociaterq option has to be used with great care. If a user logs on it removes any existing callsign from the translation table for this userid and replaces it with the callsign and SSID of the user. This will happen with multiple connects (same callsign, different SSIDs), too. Unless you want your users to be able to call out from your machine disable lqassociaterq.</p>
<h2>Files</h2>
<p>/etc/ax25/axspawn.conf</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-axspawn/">axspawn</a></code>(8). </p>
