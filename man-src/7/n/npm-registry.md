---
title: "npm-registry(7)"
name: "npm-registry"
section: "7"
letter: "n"
url: "/docs/linux/man/7-npm-registry/"
description: "npm-registry – The JavaScript Package Registry"
---

<p><code>npm-registry</code> &#8211; The JavaScript Package Registry</p>
<h2>Description</h2>
<p>To resolve packages by name and version, npm talks to a registry website that implements the CommonJS Package Registry specification for reading package info. </p>
<p> Additionally, npm&#8217;s package registry implementation supports several write APIs as well, to allow for publishing packages and managing user account information. </p>
<p> The official public npm registry is at <i><a rel="nofollow" href="http://registry.npmjs.org/">http://registry.npmjs.org/</a></i>. It is powered by a CouchDB database, of which there is a public mirror at <i><a rel="nofollow" href="http://skimdb.npmjs.com/registry">http://skimdb.npmjs.com/registry</a></i>. The code for the couchapp is available at <i><a rel="nofollow" href="http://github.com/npm/npm-registry-couchapp">http://github.com/npm/npm-registry-couchapp</a></i>. </p>
<p> The registry URL used is determined by the scope of the package (see npm help 7 <code>npm-scope</code>). If no scope is specified, the default registry is used, which is supplied by the <code>registry</code> config parameter. See npm help <code>npm-config</code>, npm help 5 <code>npmrc</code>, and npm help 7 <code>npm-config</code> for more on managing npm&#8217;s configuration.</p>
<h2>Can I run my own private registry?</h2>
<p>Yes! </p>
<p> The easiest way is to replicate the couch database, and use the same (or similar) design doc to implement the APIs. </p>
<p> If you set up continuous replication from the official CouchDB, and then set your internal CouchDB as the registry config, then you&#8217;ll be able to read any published packages, in addition to your private ones, and by default will only publish internally. </p>
<p> If you then want to publish a package for the whole world to see, you can simply override the <code>&#8211;registry</code> option for that <code>publish</code> command.</p>
<h2>I don&#8217;t want my package published in the official registry. It&#8217;s private.</h2>
<p>Set <code>&quot;private&quot;: true</code> in your package.json to prevent it from being published at all, or <code>&quot;publishConfig&quot;:{&quot;registry&quot;:&quot;<a rel="nofollow" href="http://my-internal-registry.local">http://my-internal-registry.local</a>&quot;}</code> to force it to be published only to your internal registry. </p>
<p> See npm help 5 <code>package.json</code> for more info on what goes in the package.json file.</p>
<h2>Will you replicate from my registry into the public one?</h2>
<p>No. If you want things to be public, then publish them into the public registry using npm. What little security there is would be for nought otherwise.</p>
<h2>Do I have to use couchdb to build a registry that npm can talk to?</h2>
<p>No, but it&#8217;s way easier. Basically, yes, you do, or you have to effectively implement the entire CouchDB API anyway.</p>
<h2>Is there a website or something to see package docs and such?</h2>
<p>Yes, head over to <i><a rel="nofollow" href="https://npmjs.com/">https://npmjs.com/</a></i></p>
<h2>See Also</h2>
<dl>
<dt>&bull;</p>
<dd>npm help config</p>
<dt>&bull;</p>
<dd>npm help 7 config</p>
<dt>&bull;</p>
<dd>npm help 5 npmrc</p>
<dt>&bull;</p>
<dd>npm help 7 developers</p>
<dt>&bull;</p>
<dd>npm help 7 disputes</p>
<dd>
