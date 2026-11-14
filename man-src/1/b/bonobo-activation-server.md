---
title: "bonobo-activation-server(1)"
name: "bonobo-activation-server"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bonobo-activation-server/"
description: "bonobo-activation-server – GNOME component tracker"
---

<h2 class="name">NAME</h2>
<p> bonobo-activation-server &#8211; GNOME component tracker </p>
<h2>DESCRIPTION</h2>
<p> This application tracks information about installed components and brokers components, in conjunction with its client library; libbonobo-activation. </p>
<p> It reads the component descriptions from ${prefix}/lib/bonobo/servers/*.server. These files provide an XML description of a components capabilities which can be queried and manipulated by clients from the client library. </p>
<p> Bonobo-activation-server also ensures that the minimum neccessary number of servers for your display setup are running. </p>
<p> Bonobo-activation-server executes all components with the environment inherited from the first process to start the server. In addition to using your prefix, it will examine the BONOBO_ACTIVATION_PATH and the GNOME2_PATH environment variables to find .server files. </p>
<p> In addition it examines an XML configuration file in ${prefix}/etc/bonobo-activation/bonobo-activation-config.xml </p>
<p> For more information see <code><a rel="nofollow" href="http://www.gnome.org">http://www.gnome.org</a></code>. </p>
<h2>Index</h2>
