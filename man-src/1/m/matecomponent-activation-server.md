---
title: "matecomponent-activation-server(1)"
name: "matecomponent-activation-server"
section: "1"
letter: "m"
url: "/docs/linux/man/1-matecomponent-activation-server/"
description: "matecomponent-activation-server – MATE component tracker"
---

<h2>NAME</h2>
<p> matecomponent-activation-server &#8211; MATE component tracker</p>
<h2>DESCRIPTION</h2>
<p> This application tracks information about installed components and brokers components, in conjunction with its client library; libmatecomponent-activation. </p>
<p> It reads the component descriptions from ${prefix}/lib/matecomponent/servers/*.server. These files provide an XML description of a components capabilities which can be queried and manipulated by clients from the client library. </p>
<p> MateComponent-activation-server also ensures that the minimum necessary number of servers for your display setup are running. </p>
<p> MateComponent-activation-server executes all components with the environment inherited from the first process to start the server. In addition to using your prefix, it will examine the MATECOMPONENT_ACTIVATION_PATH and the MATE2_PATH environment variables to find .server files. </p>
<p> In addition it examines an XML configuration file in ${prefix}/etc/matecomponent-activation/matecomponent-activation-config.xml </p>
<p> For more information see <code><a rel="nofollow" href="http://www.gnome.org">http://www.gnome.org</a></code>. </p>
<h2>Index</h2>
