---
title: "mongoc_read_mode_t(3)"
name: "mongoc_read_mode_t"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_read_mode_t/"
description: "mongoc_read_mode_t – Read Preference Modes"
---

<p>mongoc_read_mode_t &#8211; Read Preference Modes</p>
<h2>Synopsis</h2>
<pre>typedef enum
{
 MONGOC_READ_PRIMARY = (1 &lt;&lt; 0),
 MONGOC_READ_SECONDARY = (1 &lt;&lt; 1),
 MONGOC_READ_PRIMARY_PREFERRED = (1 &lt;&lt; 2) | MONGOC_READ_PRIMARY,
 MONGOC_READ_SECONDARY_PREFERRED = (1 &lt;&lt; 2) | MONGOC_READ_SECONDARY,
 MONGOC_READ_NEAREST = (1 &lt;&lt; 3) | MONGOC_READ_SECONDARY,
} mongoc_read_mode_t;</pre>
<h2>Description</h2>
<p>This enum describes how reads should be dispatched. The default is MONGOC_READ_PRIMARY. </p>
<p> Please see the MongoDB website for a description of <code>Read Preferences</code> \&amp;. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
