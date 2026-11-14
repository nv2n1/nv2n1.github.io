---
title: "eurephia_saltdecode(7)"
name: "eurephia_saltdecode"
section: "7"
letter: "e"
url: "/docs/linux/man/7-eurephia_saltdecode/"
description: "eurephia_saltdecode – Debug utility for eurephia"
---

<p>eurephia_saltdecode &#8211; Debug utility for eurephia</p>
<h2>Synopsis</h2>
<p><code>eurephia_saltdecode</code> &lt;password hash salt&gt;</p>
<h2>Description</h2>
<p>This program will decode the given eurephia password hash. To be able to decode the information correctly you will need to know the password for the hash. The salt is scrambled by using data from the users password and with the wrong password the information will be decoded wrong. </p>
<p> Only the first 8 bytes of the password hash is needed.</p>
<h2>Example</h2>
<p>user [at] host: ~ $ <code>eurephia_saltdecode 4d93ea21</code> </p>
<p> You will need to give the correct password for this salt. If you give the wrong password, the decoded information will be wrong. </p>
<p> Password: <code>&#8230;&#8230;&#8230;</code> </p>
<p> Salt length: 32 Hash rounds: 21763 </p>
<p> user [at] host: ~ $</p>
<h2>Author</h2>
<p>Copyright (C) 2009-2010 David Sommerseth &lt;dazo [at] users.sourceforge.net&gt;</p>
