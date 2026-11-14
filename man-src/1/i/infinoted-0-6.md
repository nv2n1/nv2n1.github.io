---
title: "infinoted-0-6(1)"
name: "infinoted-0-6"
section: "1"
letter: "i"
url: "/docs/linux/man/1-infinoted-0-6/"
description: "infinoted – dedicated server for the infinote protocol (e.g. Gobby)"
---

<p>infinoted &#8211; dedicated server for the infinote protocol (e.g. Gobby)</p>
<h2>Synopsis</h2>
<p><code>infinoted-0.6</code> [<i>options</i>]</p>
<h2>Description</h2>
<p><code>infinoted</code> is a dedicated server which allows clients to edit plain text documents and source files collaboratively over a network. Changes to the documents are synchronized instantly to the other clients. </p>
<p> This server supports the infinote protocol as implemented by libinfinity. Example clients include Gobby 0.5.x, Kobby and a special plugin for gedit. It is <code>not</code> compatible to the older libobby protocol.</p>
<h2>Options</h2>
<h3>Help Options:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Show help options</dl>
<h3>Application Options:</h3>
<dl>
<dt><code>-c</code>, <code>&#8211;config-file</code>=<i>CONFIG-FILE</i></p>
<dd>Load the given configuration file instead of looking at the standard locations.</p>
<dt><code>-k</code>, <code>&#8211;key-file</code>=<i>KEY-FILE</i></p>
<dd>The server&#8217;s private key</p>
<dt><code>-c</code>, <code>&#8211;certificate-file</code>=<i>CERTIFICATE-FILE</i></p>
<dd>The server&#8217;s certificate</p>
<dt><code>&#8211;certificate-chain</code></p>
<dd>The certificate chain to the root certificate, if not included in the file given in &#8211;certificate-file.</p>
<dt><code>&#8211;create-key</code></p>
<dd>Creates a new random private key</p>
<dt><code>&#8211;create-certificate</code></p>
<dd>Creates a new self-signed certificate using the given key</p>
<dt><code>-p</code>, <code>&#8211;port-number</code>=<i>PORT</i></p>
<dd>The port number to listen on</p>
<dt><code>&#8211;security-policy</code>=<i>no-tls</i>|allow-tls|require-tls</p>
<dd>How to decide whether to use TLS</p>
<dt><code>-r</code>, <code>&#8211;root-directory</code>=<i>DIRECTORY</i></p>
<dd>A directory to save the document tree into in infinoted-xml format. This is the location where the tree is kept persistently so that it is available again after server restart. Usually, documents are saved in this tree 60 seconds after the last user left the session. In addition to this, when the autosave plugin is enabled, it is possible to save sessions into the tree periodically. The default directory is ~/.infinote.</p>
<dt><code>&#8211;plugins</code>=<i>PLUGIN</i></p>
<dd>Additional plugin to load. Repeat the option on the command-line to specify multiple plugins and semi-colons in the configuration file. Plugin options can be configured in the configuration file (one section for each plugin), or with the &#8211;plugin-parameter option.</p>
<dt><code>&#8211;plugin-parameter</code>=<i>PLUGIN:KEY:VALUE</i></p>
<dd>Sets the option KEY for plugin PLUGIN to the given VALUE. Normally, plugin options are specified in the configuration file, but this command line option allows one to set or override plugin options on the command line.</p>
<dt><code>-P</code>, <code>&#8211;password</code>=<i>PASSWORD</i></p>
<dd>Require given password on connections</p>
<dt><code>&#8211;pam-service</code>=<i>SERVICE</i></p>
<dd>Authenticate clients against given pam service on connection</p>
<dt><code>&#8211;pam-allow-user</code>=<i>USERS</i></p>
<dd>Users allowed to connect after pam authentication. Separate entries with semicolons.</p>
<dt><code>&#8211;pam-allow-group</code>=<i>GROUPS</i></p>
<dd>Group allowed to connect after pam authentication. Separate entries with semicolons.</p>
<dt><code>-d</code>, <code>&#8211;daemonize</code></p>
<dd>Daemonize the server</p>
<dt><code>-D</code>, <code>&#8211;kill-daemon</code></p>
<dd>Kill a running daemon</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd>Display version information and exit</dl>
<h2>Author</h2>
<p><code>infinoted</code> and <code>libinfinity</code> were written by Armin Burgmeier &lt;armin [at] arbur.net&gt;</p>
