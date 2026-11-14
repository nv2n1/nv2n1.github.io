---
title: "cmis-client(1)"
name: "cmis-client"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cmis-client/"
description: "______cmis-client ____ – command line CMIS client tool."
---

<h2 class="name">NAME</h2>
<p> ______cmis-client ____ &#8211; command line CMIS client tool. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>cmis-client</code> help</p>
<dt> <code>cmis-client</code> [-v] &#8211;url&nbsp;<wbr><i><a href="url://to/binding">url://to/binding</a></i> list-repos</p>
<dt> <code>cmis-client</code> [-v] [-u&nbsp;<wbr><i>login</i>] [-p&nbsp;<wbr><i>secret</i>] &#8211;url&nbsp;<wbr><i><a href="url://to/binding">url://to/binding</a></i> -r&nbsp;<wbr><i>repo-id</i> repo-infos</p>
<dt> <code>cmis-client</code> [-v] [-u&nbsp;<wbr><i>login</i>] [-p&nbsp;<wbr><i>secret</i>] &#8211;url&nbsp;<wbr><i><a href="url://to/binding">url://to/binding</a></i> -r&nbsp;<wbr><i>repo-id</i> show-root</p>
<dt> <code>cmis-client</code> [-v] [-u&nbsp;<wbr><i>login</i>] [-p&nbsp;<wbr><i>secret</i>] &#8211;url&nbsp;<wbr><i><a href="url://to/binding">url://to/binding</a></i> -r&nbsp;<wbr><i>repo-id</i> get-content&nbsp;<wbr><i>id</i></p>
<dt> <code>cmis-client</code> [-v] [-u&nbsp;<wbr><i>login</i>] [-p&nbsp;<wbr><i>secret</i>] &#8211;url&nbsp;<wbr><i><a href="url://to/binding">url://to/binding</a></i> -r&nbsp;<wbr><i>repo-id</i> &#8211;input-file&nbsp;<wbr><i>path/to/file</i> &#8211;input-type&nbsp;<wbr><i>mime/type</i> [&#8211;input-name&nbsp;<wbr><i>name.ext</i>] set-content&nbsp;<wbr><i>id</i></p>
<dt> <code>cmis-client</code> [-v] [-u&nbsp;<wbr><i>login</i>] [-p&nbsp;<wbr><i>secret</i>] &#8211;url&nbsp;<wbr><i><a href="url://to/binding">url://to/binding</a></i> -r&nbsp;<wbr><i>repo-id</i> [&#8211;object-type&nbsp;<wbr><i>some:cmistype</i>] [&#8211;object-property&nbsp;<wbr><i>prop-id=prop-value</i>&#8230;] create-folder&nbsp;<wbr><i>parent-id name</i></p>
<dt> <code>cmis-client</code> [-v] [-u&nbsp;<wbr><i>login</i>] [-p&nbsp;<wbr><i>secret</i>] &#8211;url&nbsp;<wbr><i><a href="url://to/binding">url://to/binding</a></i> -r&nbsp;<wbr><i>repo-id</i> &#8211;input-file&nbsp;<wbr><i>path/to/file</i> &#8211;input-type&nbsp;<wbr><i>mime/type</i> [&#8211;input-name&nbsp;<wbr><i>name.ext</i>] [&#8211;object-type&nbsp;<wbr><i>some:cmistype</i>] [&#8211;object-property&nbsp;<wbr><i>prop-id=prop-value</i>&#8230;] create-document&nbsp;<wbr><i>parent-id name</i></p>
<dt> <code>cmis-client</code> [-v] [-u&nbsp;<wbr><i>login</i>] [-p&nbsp;<wbr><i>secret</i>] &#8211;url&nbsp;<wbr><i><a href="url://to/binding">url://to/binding</a></i> -r&nbsp;<wbr><i>repo-id</i> [&#8211;object-property&nbsp;<wbr><i>prop-id=prop-value</i>&#8230;] update-object&nbsp;<wbr><i>object-id</i></p>
<dt> <code>cmis-client</code> [-v] [-u&nbsp;<wbr><i>login</i>] [-p&nbsp;<wbr><i>secret</i>] &#8211;url&nbsp;<wbr><i><a href="url://to/binding">url://to/binding</a></i> -r&nbsp;<wbr><i>repo-id</i> [type-by-id] | [show-by-id] | [show-by-path] | [delete] <i>arg</i>&#8230;</p>
<dt> <code>cmis-client</code> [-v] [-u&nbsp;<wbr><i>login</i>] [-p&nbsp;<wbr><i>secret</i>] &#8211;url&nbsp;<wbr><i><a href="url://to/binding">url://to/binding</a></i> -r&nbsp;<wbr><i>repo-id</i> [checkout] | [cancel-checkout] | [get-versions] <i>arg</i></p>
<dt> <code>cmis-client</code> [-v] [-u&nbsp;<wbr><i>login</i>] [-p&nbsp;<wbr><i>secret</i>] &#8211;url&nbsp;<wbr><i><a href="url://to/binding">url://to/binding</a></i> -r&nbsp;<wbr><i>repo-id</i> [&#8211;input-file&nbsp;<wbr><i>path/to/file</i>] [&#8211;input-type&nbsp;<wbr><i>mime/type</i>] [&#8211;input-name&nbsp;<wbr><i>name.ext</i>] [&#8211;object-property&nbsp;<wbr><i>prop-id=prop-value</i>&#8230;] [&#8211;major] [&#8211;message] checkin&nbsp;<wbr><i>pwc id</i></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>cmis-client</code> tool sends queries over the net to a CMIS-enabled server to access or modify its content. It is originally demonstrating what libcmis is capable of.</p>
<h2>OPTIONS</h2>
<h3>GLOBAL OPTIONS</h3>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> Shows a lot of information to monitor what is happening behind the scene. This helps a lot to debug libcmis.</dl>
<p> &#8211;help</p>
<dl>
<dt>
<dd> Show the help and exit. This is equivalent to use the help command.</dl>
<p> &#8211;url <i><a href="url://to/binding">url://to/binding</a></i></p>
<dl>
<dt>
<dd> <i><a href="url://to/binding">url://to/binding</a></i> needs to point to the service document of either AtomPub or WebService binding.</dl>
<p> -r,&#8211;repository <i>repo-id</i></p>
<dl>
<dt>
<dd> Operate on the <i>repo-id</i> CMIS repository. If there is only one repository on the server, this parameter is not needed and that repository will be automatically selected. Use this parameter if there are several repositories on the server.</dl>
<p> -u,&#8211;username <i>login</i></p>
<dl>
<dt>
<dd> Connect as <i>login</i> to the CMIS server. If not provided connect anonymously.</dl>
<p> -p,&#8211;password <i>secret</i></p>
<dl>
<dt>
<dd> Use <i>secret</i> to authenticate on the CMIS server.</dl>
<p> &#8211;no-ssl-check</p>
<dl>
<dt>
<dd> Disables the SSL certificate verifications. Lowers the security, but may be handy to work around bad certificates like expired or self-signed ones.</dl>
<p> &#8211;proxy <i>url</i></p>
<dl>
<dt>
<dd> Use <i>url</i> as the HTTP proxy. Setting this value will override the system proxy settings.</dl>
<p> &#8211;proxy-username <i>login</i></p>
<dl>
<dt>
<dd> Use <i>login</i> to authenticate on the HTTP proxy.</dl>
<p> &#8211;proxy-password <i>secret</i></p>
<dl>
<dt>
<dd> Use <i>secret</i> to authenticate on the HTTP proxy.</dl>
<p> &#8211;noproxy <i>list</i></p>
<dl>
<dt>
<dd> Proxy settings won&#8217;t apply to hostnames and domain names listed in <i>list</i>. This value is a coma separated list.</dl>
<p> &#8211;oauth2-client-id <i>client_id</i></p>
<dl>
<dt>
<dd> Application client id to use in the OAuth2 authentication flow.</dl>
<p> &#8211;oauth2-client-secret <i>client_secret</i></p>
<dl>
<dt>
<dd> Application client secret to use in the OAuth2 authentication flow.</dl>
<p> &#8211;oauth2-auth-url <i>url</i></p>
<dl>
<dt>
<dd> URL to authenticate the user in the OAuth2 authentication flow.</dl>
<p> &#8211;oauth2-token-url <i>url</i></p>
<dl>
<dt>
<dd> URL to authenticate the application in the OAuth2 authentication flow. The access and refresh tokens are provided by this URL.</dl>
<p> &#8211;oauth2-redirect-uri <i>uri</i></p>
<dl>
<dt>
<dd> URI where the OAuth2 authentication flow will redirect after a sucessful authentication.</dl>
<p> &#8211;oauth2-scope <i>scope</i></p>
<dl>
<dt>
<dd> Requested scope to access in the OAuth2 authentication flow.</dl>
<h3>MODIFICATION OPERATIONS OPTIONS</h3>
<p> &#8211;input-file <i>path/to/file</i></p>
<dl>
<dt>
<dd> Upload <i>path/to/file</i> as the new content stream of the object.</dl>
<p> &#8211;input-type <i>mime/type</i></p>
<dl>
<dt>
<dd> Set the mime type of the new content stream of the object to <i>mime/type</i>.</dl>
<p> &#8211;input-name <i>name.ext</i></p>
<dl>
<dt>
<dd> Set the remote content stream filename of the new content stream of the object to <i>name.ext</i>.</dl>
<p> &#8211;object-type <i>some:cmistype</i></p>
<dl>
<dt>
<dd> Set the object type of the CMIS object to be created to <i>some:cmistype</i>. This is the equivalent of &#8211;object-property cmis:objectTypeId=some:cmistype.</dl>
<p> &#8211;object-property <i>prop-id=prop-value</i></p>
<dl>
<dt>
<dd> Set a property to be updated or added to the CMIS object. <i>prop-id</i> is the property definition id and <i>prop-value</i> is the value to set on it.</dl>
<p> &#8211;major</p>
<dl>
<dt>
<dd> Create a major version when performing a checkin.</dl>
<p> -m, &#8211;message <i>message</i></p>
<dl>
<dt>
<dd> Set the checking message.</dl>
<h3>COMMANDS</h3>
<p> help</p>
<dl>
<dt>
<dd> Show the help and exit.</dl>
<p> list-repos</p>
<dl>
<dt>
<dd> List the repositories available on the server.</dl>
<p> repo-infos</p>
<dl>
<dt>
<dd> Displays the informations and capabilities of the selected repository</dl>
<p> show-root</p>
<dl>
<dt>
<dd> Displays the root node infos and children.</dl>
<p> get-content <i>id</i></p>
<dl>
<dt>
<dd> Download the content of the CMIS object corresponding to <i>id</i> in the current directory.</dl>
<p> set-content <i>id</i></p>
<dl>
<dt>
<dd> Upload a file as the content stream of the CMIS object corresponding to <i>id</i>.</dl>
<p> create-folder <i>parent-id name</i></p>
<dl>
<dt>
<dd> Create a sub folder in folder <i>parent-id</i> named <i>name</i>. The default type of the folder to create is cmis:folder, but this can be changed using &#8211;object-type option.</dl>
<p> create-document <i>parent-id name</i></p>
<dl>
<dt>
<dd> Create a document in folder <i>parent-id</i> named <i>name</i>. The default type of the document to create is cmis:document, but this can be changed using &#8211;object-type option. </p>
<p> Note that the &#8211;input-file and &#8211;input-type may be mandatory, depending on the type of the document to create and its constraints.</dl>
<p> update-object <i>object-id</i></p>
<dl>
<dt>
<dd> Replace the writeable properties given with &#8211;object-property option on the object matching id <i>object-id</i>.</dl>
<p> type-by-id <i>arg&#8230;</i></p>
<dl>
<dt>
<dd> Displays the infos and children (if any) of all the CMIS types corresponding to the listed ids.</dl>
<p> show-by-id <i>arg&#8230;</i></p>
<dl>
<dt>
<dd> Displays the infos and children (if any) of all the CMIS objects corresponding to the listed ids.</dl>
<p> show-by-path <i>arg&#8230;</i></p>
<dl>
<dt>
<dd> Displays the infos and children (if any) of all the CMIS objects corresponding to the listed paths.</dl>
<p> delete <i>arg&#8230;</i></p>
<dl>
<dt>
<dd> Deletes the CMIS objects corresponding to the listed ids. If the node is a folder, its content will be removed as well.</dl>
<p> checkout <i>arg</i></p>
<dl>
<dt>
<dd> Checkout the document corresponding to the provided id and display the infos of the created private working copy.</dl>
<p> cancel-checkout <i>arg</i></p>
<dl>
<dt>
<dd> Cancel the Private Working Copy corresponding to the node id.</dl>
<p> get-versions <i>arg</i></p>
<dl>
<dt>
<dd> Display the versions (if any) of all the CMIS object corresponding to the provided id.</dl>
<p> checkin <i>arg</i></p>
<dl>
<dt>
<dd> Check in the private working copy corresponding to the provided id and display the infos of the resulting document. Use the &#8211;major and &#8211;message options to define the version to create and the commit to associate to it. Note that repositories without the ability to update the private working copies will need the &#8211;input-file, &#8211;input-type and &#8211;object-property options.</dl>
<h2>USAGE</h2>
<p> Displays the root node of repository A1: </p>
<p> <code>cmis-client</code> -r A1 &#8211;url <a rel="nofollow" href="http://localhost/atom">http://localhost/atom</a> show-root </p>
<p> Displays the nodes with id 133 and 116 of repository A1: </p>
<p> <code>cmis-client</code> -r A1 &#8211;url <a rel="nofollow" href="http://localhost/atom">http://localhost/atom</a> show-by id 133 116</p>
<h2>AUTHOR</h2>
<p> C&eacute;dric Bosdonnat cbosdo </p>
<h2>Index</h2>
