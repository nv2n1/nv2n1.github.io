---
title: "globus_i_ftp_client_features_s(3)"
name: "globus_i_ftp_client_features_s"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_i_ftp_client_features_s/"
---

<h2 class="name">NAME</h2>
 

 globus_i_ftp_client_features_s - 

 FTP server features we are interested in.

<h2>SYNOPSIS</h2>

 
 

 

 #include &lt;globus_i_ftp_client.h&gt;

<h2>Detailed Description</h2>

 

 FTP server features we are interested in. 

 Upon a new connection, we will attempt to probe via the SITE HELP and FEAT commands which the server supports. If we can't determine from that, we'll try using the command and find out if the server supports it. 

<h2>Author</h2>

 

 Generated automatically by Doxygen for globus_ftp_client from the source code. 

<h2>Index</h2>


