---
title: "pkcs15-profile(5)"
name: "pkcs15-profile"
section: "5"
letter: "p"
url: "/docs/linux/man/5-pkcs15-profile/"
description: "pkcs15-profile – format of profile for pkcs15-init"
---

<p>pkcs15-profile &#8211; format of profile for pkcs15-init</p>
<h2>Synopsis</h2>
<h2>Description</h2>
<p>The <code>pkcs15-init</code> utility for PKCS #15 smart card personalization is controlled via profiles. When starting, it will read two such profiles at the moment, a generic application profile, and a card specific profile. The generic profile must be specified on the command line, while the card-specific file is selected based on the type of card detected. </p>
<p> The generic application profile defines general information about the card layout, such as the path of the application DF, various PKCS #15 files within that directory, and the access conditions on these files. It also defines general information about PIN, key and certificate objects. Currently, there is only one such generic profile, <code>pkcs15.profile</code>. </p>
<p> The card specific profile contains additional information required during card intialization, such as location of PIN files, key references etc. Profiles currently reside in <code>@pkgdatadir@</code></p>
<h2>Syntax</h2>
<p>This section should contain information about the profile syntax. Will add this soonishly.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-pkcs15/">pkcs15</a></code>(7), <code><a href="/docs/linux/man/1-pkcs15-init/">pkcs15-init</a></code>(1), <code><a href="/docs/linux/man/1-pkcs15-crypt/">pkcs15-crypt</a></code>(1), <code><a href="/docs/linux/man/7-opensc/">opensc</a></code>(7), </p>
