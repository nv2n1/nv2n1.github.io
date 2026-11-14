---
title: "mongoc_host_list_t(3)"
name: "mongoc_host_list_t"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_host_list_t/"
description: "mongoc_host_list_t – typedef struct { mongoc_host_list_t *next; char host [BSON_HOST_NAME_MAX + 1]; char host_and_port [BSON_HOST_NAME_MAX + 7]; uint16_t port; int family; void *padding [4]; } mong..."
---

<p>mongoc_host_list_t &#8211; typedef struct {<br />
mongoc_host_list_t&nbsp;<wbr>*next;<br />
char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>host&nbsp;<wbr>[BSON_HOST_NAME_MAX&nbsp;<wbr>+&nbsp;<wbr>1];<br />
char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>host_and_port&nbsp;<wbr>[BSON_HOST_NAME_MAX&nbsp;<wbr>+&nbsp;<wbr>7];<br />
uint16_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>port;<br />
int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>family;<br />
void&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*padding&nbsp;<wbr>[4]; } mongoc_host_list_t;</p>
<h2>Synopsis</h2>
<pre>typedef struct
{
 mongoc_host_list_t *next;
 char host [BSON_HOST_NAME_MAX + 1];
 char host_and_port [BSON_HOST_NAME_MAX + 7];
 uint16_t port;
 int family;
 void *padding [4];
} mongoc_host_list_t;</pre>
<h2>Description</h2>
<p>The host and port of a MongoDB server. Can be part of a linked list: for example the return value of <code>mongoc_uri_get_hosts</code> when multiple hosts are provided in the MongoDB URI. </p>
<h2>See Also</h2>
<p><code>mongoc_uri_get_hosts</code> and <code>mongoc_cursor_get_host</code> \&amp;. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
