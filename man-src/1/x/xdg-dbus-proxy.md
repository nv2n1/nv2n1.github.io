---
title: "xdg-dbus-proxy(1)"
name: "xdg-dbus-proxy"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xdg-dbus-proxy/"
description: "xdg-dbus-proxy – D-Bus proxy"
---

<h2 class="name">NAME</h2>
<p> xdg-dbus-proxy &#8211; D-Bus proxy </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>xdg-dbus-proxy</code> [<i>OPTION</i>&#8230;] [<i>ADDRESS</i>&nbsp;<i>PATH</i>&nbsp;[<i>OPTION</i>&#8230;]&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>xdg-dbus-proxy</code></p>
<dd>is a filtering proxy for D-Bus connections. Its arguments are one or more <i>ADDRESS</i>&#8211;<i>PATH</i> pairs specifying the buses to proxy, with options that specify what filtering to apply.</p>
<h3>Basic Operation</h3>
<p> The proxy listens to the unix domain socket at <i>PATH</i>, and for each client that connects to the socket, it opens up a new connection to the specified D-Bus <i>ADDRESS</i> (typically the session bus) and forwards data between the two. During the authentication phase all data is forwarded as received, and additionally for the first 1 byte zero we also send the proxy credentials to the bus. </p>
<p> Once the connection is authenticated there are two modes, filtered and unfiltered. In the unfiltered mode all messages are sent on as they are received. In the filtering mode policy is applied to determine which messages to allow, and which to drop. </p>
<p> Filtering is applied only to outgoing signals and method calls and incoming broadcast signals. All replies (errors or method returns) are allowed once for an outstanding method call, and never otherwise. </p>
<p> If a client ever receives a message from another peer on the bus, the senders unique name is made visible, so the client can track caller lifetimes via NameOwnerChanged signals. If a client calls a method on or receives a broadcast signal from a name (even if filtered to some subset of paths or interfaces), that names basic policy is considered to be (at least) TALK, from then on.</p>
<h3>Policy</h3>
<p> The policy for the filtering consists of a mapping from well-known names to a policy that is either SEE, TALK or OWN. The default initial policy is that the the user is only allowed to TALK to the bus itself (org.freedesktop.DBus, or no destination specified), and TALK to its own unique ID. All other clients are invisible. </p>
<p> Here is a description of the policy levels (each level implies the ones before it): </p>
<p> SEE</p>
<dl>
<dt>
<dd> The name/ID is visible in the ListNames reply </p>
<p> The name/ID is visible in the ListActivatableNames reply </p>
<p> You can call GetNameOwner on the name </p>
<p> You can call NameHasOwner on the name </p>
<p> You see NameOwnerChanged signals on the name </p>
<p> You see NameOwnerChanged signals on the ID when the client disconnects </p>
<p> You can call the GetXXX methods on the name/ID to get e.g. the peer pid </p>
<p> You get AccessDenied rather than NameHasNoOwner when sending messages to the name/ID</dl>
<p> TALK</p>
<dl>
<dt>
<dd> You can send any method calls and signals to the name/ID </p>
<p> You will receive broadcast signals from the name/ID (if you have a match rule for them) </p>
<p> You can call StartServiceByName on the name</dl>
<p> OWN</p>
<dl>
<dt>
<dd> You are allowed to call RequestName/ReleaseName/ListQueuedOwners on the name</dl>
<p> Policy is specified with the <code>&#8211;see</code>, <code>&#8211;talk</code> and <code>&#8211;own</code> options. The well-known names in these options can have a &#8216;.*&#8217; suffix. A name of &quot;org.foo.*&quot; matches &quot;org.foo&quot;, org.foo.bar&quot;, and &quot;org.foo.bar.gazonk&quot;, but not &quot;org.foobar&quot;. </p>
<p> Polices are specified for well-known names, but they also affect the owner of that name, so that the policy for a unique ID is the union of the polices for all the names it owns. For technical reasons, the policy for a unique name is &quot;sticky&quot;, in that the highest policy granted by a once-owned name is kept, even when the client releases that name. This is impossible to avoid in a race-free way in a proxy. But it is rarely a problem in practice, as few clients release names and stay on the bus. </p>
<p> In addition to the basic SEE/TALK/OWN policy, it is possible to specify more complicated rules about what method calls can be made on and what broadcast signals can be received from well-known names. A rule can restrict the allowed calls/signals to a specific object path or a subtree of object paths, and it can restrict the allowed interface down to an individual method or signal name. </p>
<p> Rules are specified with the <code>&#8211;call</code> and <code>&#8211;broadcast</code> options. The <i>RULE</i> in these options determines what interfaces, methods and object paths are allowed. It must be of the form [<i>METHOD</i>][@<i>PATH</i>], where <i>METHOD</i> can be either &#8216;*&#8217; or a D-Bus interface, possible with a &#8216;.*&#8217; suffix, or a fully-qualified method name, and <i>PATH</i> is a D-Bus object path, possible with a &#8216;/*&#8217; suffix.</p>
<h2>OPTIONS</h2>
<p> When options are used multiple times, the last option wins, unless otherwise specified. </p>
<p> General options: </p>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print help and exit</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print version</dl>
<p> <code>&#8211;fd=</code><code>FD</code></p>
<dl>
<dt>
<dd> Write to FD when the proxies are ready, and stop when it is closed.</dl>
<p> <code>&#8211;args=</code><code>FD</code></p>
<dl>
<dt>
<dd> Parse nul-separated arguments from the given file descriptor. This option can be used multiple times to parse options from multiple sources.</dl>
<p> Proxy Options: </p>
<p> These options can only be used after an ADDRESS and apply to the proxy for that address. </p>
<p> <code>&#8211;filter</code></p>
<dl>
<dt>
<dd> Enable filtering</dl>
<p> <code>&#8211;log</code></p>
<dl>
<dt>
<dd> Turn on logging</dl>
<p> <code>&#8211;sloppy-names</code></p>
<dl>
<dt>
<dd> Make all unique names visible.</dl>
<p> <code>&#8211;see=</code><i>NAME</i></p>
<dl>
<dt>
<dd> Set the SEE policy for the given name.</dl>
<p> <code>&#8211;talk=</code><i>NAME</i></p>
<dl>
<dt>
<dd> Set the TALK policy for the given name.</dl>
<p> <code>&#8211;own=</code><i>NAME</i></p>
<dl>
<dt>
<dd> Set the OWN policy for the given name.</dl>
<p> <code>&#8211;call=</code><i>NAME</i><code>=</code><i>RULE</i></p>
<dl>
<dt>
<dd> Set a rule for calls on the given name.</dl>
<p> <code>&#8211;broadcast=</code><i>NAME</i><code>=</code><i>RULE</i></p>
<dl>
<dt>
<dd> Set a rule for broadcast signals from the given name.</dl>
<h2>EXAMPLES</h2>
<p> <code>$ xdg-dbus-proxy &#8211;fd=26 unix:path=/run/usr/1000/bus /run/usr/1000/.dbus-proxy/session-bus-proxy &#8211;filter &#8211;own=org.gnome.ghex.* &#8211;talk=ca.desrt.dconf &#8211;call=org.freedesktop.portal.*=* &#8211;broadcast=org.freedesktop.portal.*=@/org/freedesktop/portal/*</code> </p>
<h2>Index</h2>
