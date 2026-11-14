---
title: "google(1)"
name: "google"
section: "1"
letter: "g"
url: "/docs/linux/man/1-google/"
description: "google – command-line access to (some) Google services"
---

<h2>NAME</h2>
<p> google &#8211; command-line access to (some) Google services</p>
<h2>SYNOPSIS</h2>
<p> <code>google</code> [<i>picasa|blogger|youtube|docs|contacts|calendar</i>] <i>TASK </i>[<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> This program provides command-line access to (some) google services via their gdata APIs. Called without a service name, it starts an interactive session. </p>
<p> Available tasks for service picasa: &#8216;get&#8217;, &#8216;create&#8217;, &#8216;list&#8217;, &#8216;list-albums&#8217;, &#8216;tag&#8217;, &#8216;post&#8217;, &#8216;delete&#8217;</p>
<dl>
<dt>
<dd> get: Download albums</p>
<dt>
<dd> Requires: none Optional: title, owner, format Arguments: LOCATION</p>
<dt>
<dd> create: Create an album</p>
<dt>
<dd> Requires: title Optional: date, summary, tags Arguments: PATH_TO_PHOTOS</p>
<dt>
<dd> list: List photos</p>
<dt>
<dd> Requires: delimiter Optional: title, query, owner</p>
<dt>
<dd> list-albums: List albums</p>
<dt>
<dd> Requires: delimiter Optional: title, owner</p>
<dt>
<dd> tag: Tag photos</p>
<dt>
<dd> Requires: tags AND (title OR query) Optional: owner</p>
<dt>
<dd> post: Post photos to an album</p>
<dt>
<dd> Requires: title Optional: tags, owner Arguments: PATH_TO_PHOTOS</p>
<dt>
<dd> delete: Delete photos or albums</p>
<dt>
<dd> Requires: (title OR query)</dl>
<p> Available tasks for service blogger: &#8216;post&#8217;, &#8216;tag&#8217;, &#8216;list&#8217;, &#8216;delete&#8217;</p>
<dl>
<dt>
<dd> post: Post content.</p>
<dt>
<dd> Requires: none Optional: blog, title, tags Arguments: PATH_TO_CONTENT or CONTENT</p>
<dt>
<dd> tag: Label posts</p>
<dt>
<dd> Requires: tags AND title Optional: blog</p>
<dt>
<dd> list: List posts in a blog</p>
<dt>
<dd> Requires: delimiter Optional: blog, title, owner</p>
<dt>
<dd> delete: Delete a post.</p>
<dt>
<dd> Requires: title Optional: blog</dl>
<p> Available tasks for service youtube: &#8216;post&#8217;, &#8216;tag&#8217;, &#8216;list&#8217;, &#8216;delete&#8217;</p>
<dl>
<dt>
<dd> post: Post a video.</p>
<dt>
<dd> Requires: category AND devkey Optional: title, summary, tags Arguments: PATH_TO_VIDEO</p>
<dt>
<dd> tag: Add tags to a video and/or change its category.</p>
<dt>
<dd> Requires: devkey AND title AND (category OR tags)</p>
<dt>
<dd> list: List videos by user.</p>
<dt>
<dd> Requires: delimiter Optional: title, owner</p>
<dt>
<dd> delete: Delete videos.</p>
<dt>
<dd> Requires: devkey Optional: title</dl>
<p> Available tasks for service docs: &#8216;edit&#8217;, &#8216;delete&#8217;, &#8216;list&#8217;, &#8216;upload&#8217;, &#8216;get&#8217;</p>
<dl>
<dt>
<dd> edit: Edit a document</p>
<dt>
<dd> Requires: title Optional: format, editor, folder</p>
<dt>
<dd> delete: Delete documents</p>
<dt>
<dd> Requires: none Optional: title</p>
<dt>
<dd> list: List documents</p>
<dt>
<dd> Requires: delimiter Optional: title, folder</p>
<dt>
<dd> upload: Upload a document</p>
<dt>
<dd> Requires: none Optional: title, folder, format Arguments: PATH_TO_FILE</p>
<dt>
<dd> get: Download a document</p>
<dt>
<dd> Requires: (title OR folder) Optional: format Arguments: LOCATION</dl>
<p> Available tasks for service contacts: &#8216;list&#8217;, &#8216;list-groups&#8217;, &#8216;add&#8217;, &#8216;add-groups&#8217;, &#8216;delete-groups&#8217;, &#8216;delete&#8217;</p>
<dl>
<dt>
<dd> list: List contacts</p>
<dt>
<dd> Requires: none Arguments: Fields to show (example: name,email)</p>
<dt>
<dd> list-groups: List contact groups</p>
<dt>
<dd> Requires: none Arguments: Specific groups to list (if any)</p>
<dt>
<dd> add: Add contacts</p>
<dt>
<dd> Requires: none Arguments: &quot;name,email&quot; pair or CSV filename</p>
<dt>
<dd> add-groups: Add contact group(s)</p>
<dt>
<dd> Requires: none Arguments: Group name(s)</p>
<dt>
<dd> delete-groups: Delete contact group(s)</p>
<dt>
<dd> Requires: none Arguments: Group name(s)</p>
<dt>
<dd> delete: Delete contacts</p>
<dt>
<dd> Requires: none Arguments: names of contact(s) to delete (e.g. &quot;John Doe&quot; &quot;Jane Doe&quot;)</dl>
<p> Available tasks for service calendar: &#8216;add&#8217;, &#8216;list&#8217;, &#8216;today&#8217;, &#8216;delete&#8217;</p>
<dl>
<dt>
<dd> add: Add event to a calendar</p>
<dt>
<dd> Requires: none Optional: cal Arguments: QUICK_ADD_TEXT</p>
<dt>
<dd> list: List events on a calendar</p>
<dt>
<dd> Requires: delimiter Optional: title, query, date, cal</p>
<dt>
<dd> today: List events for the next 24 hours</p>
<dt>
<dd> Requires: delimiter Optional: title, query, cal</p>
<dt>
<dd> delete: Delete event from a calendar</p>
<dt>
<dd> Requires: (title OR query) Optional: date, cal</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> show program&#8217;s version number and exit</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help message and exit</p>
<dt><code>&#8211;blog</code>=<i>BLOG</i></p>
<dd> Blogger only &#8211; specify a blog other than your primary.</p>
<dt><code>&#8211;cal</code>=<i>CAL</i></p>
<dd> Calendar only &#8211; specify a calendar other than your primary.</p>
<dt><code>-c</code> CATEGORY, <code>&#8211;category</code>=<i>CATEGORY</i></p>
<dd> YouTube only &#8211; specify video categories as a commaseparated list, e.g. &quot;Film, Travel&quot;</p>
<dt><code>&#8211;config</code>=<i>CONFIG</i></p>
<dd> Specify location of config file.</p>
<dt><code>&#8211;devtags</code>=<i>DEVTAGS</i></p>
<dd> YouTube only &#8211; specify developer tags as a commaseparated list.</p>
<dt><code>&#8211;devkey</code>=<i>DEVKEY</i></p>
<dd> YouTube only &#8211; specify a developer key</p>
<dt><code>-d</code> DATE, <code>&#8211;date</code>=<i>DATE</i></p>
<dd> Date in YYYY-MM-DD format. Picasa only &#8211; sets the date of the album Calendar only &#8211; date of the event to add / look for. Can also specify a range with a comma: &quot;YYYY-MM-DD&quot;, events between date and future. &quot;YYYYMM-DD,YYYY-MM-DD&quot; events between two dates.</p>
<dt><code>&#8211;debug</code></p>
<dd> Enable all debugging output, including HTTP data</p>
<dt><code>&#8211;delimiter</code>=<i>DELIMITER</i></p>
<dd> Specify a delimiter for the output of the list task.</p>
<dt><code>&#8211;draft</code></p>
<dd> Blogger only &#8211; post as a draft</p>
<dt><code>&#8211;editor</code>=<i>EDITOR</i></p>
<dd> Docs only &#8211; editor to use on a file.</p>
<dt><code>-f</code> FOLDER, <code>&#8211;folder</code>=<i>FOLDER</i></p>
<dd> Docs only &#8211; specify folder(s) to upload to / search in.</p>
<dt><code>&#8211;format</code>=<i>FORMAT</i></p>
<dd> Docs only &#8211; format to download documents as.</p>
<dt><code>&#8211;hostid</code>=<i>HOSTID</i></p>
<dd> Label the machine being used.</p>
<dt><code>-n</code> TITLE, <code>&#8211;title</code>=<i>TITLE</i></p>
<dd> Title of the item</p>
<dt><code>&#8211;no-convert</code></p>
<dd> Google Apps Premier only &#8211; do not convert the file on upload. (Else converts to native Google Docs format)</p>
<dt><code>-o</code> OWNER, <code>&#8211;owner</code>=<i>OWNER</i></p>
<dd> Username or ID of the owner of the resource. For example, &#8216;picasa list-albums <code>-o</code> bob&#8217; to list bob&#8217;s albums</p>
<dt><code>-q</code> QUERY, <code>&#8211;query</code>=<i>QUERY</i></p>
<dd> Full text query string for specifying items. Searches on titles, captions, and tags.</p>
<dt><code>&#8211;quiet</code></p>
<dd> Print only prompts and error messages</p>
<dt><code>&#8211;reminder</code>=<i>REMINDER</i></p>
<dd> Calendar only &#8211; specify time for added event&#8217;s reminder, e.g. &quot;10m&quot;, &quot;3h&quot;, &quot;1d&quot;</p>
<dt><code>-s</code> SUMMARY, <code>&#8211;summary</code>=<i>SUMMARY</i></p>
<dd> Description of the upload, or file containing the description.</p>
<dt><code>-t</code> TAGS, <code>&#8211;tags</code>=<i>TAGS</i></p>
<dd> Tags for item, e.g. &quot;Sunsets, Earth Day&quot;</p>
<dt><code>-u</code> USER, <code>&#8211;user</code>=<i>USER</i></p>
<dd> Username to log in with for the service.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Print all messages.</dl>
<h2>EXAMPLES</h2>
<pre><code>
google blogger post-- title 'foo' 'command line posting' google calendar add 'Lunch with Jim at noon tomorrow' google contacts list name, email &gt; contacts.csv
                                                                                                                                                          google docs edit-- title 'Shopping list' google.py picasa create-- title 'Cat Photos' ~ /
                                                                                                                                                      photos / cats/*.jpg
google youtube post --category Education killer_robots.avi
</code></pre>
<h2>Index</h2>
